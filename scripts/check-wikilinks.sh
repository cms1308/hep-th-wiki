#!/usr/bin/env bash
# check-wikilinks.sh — flag malformed Obsidian [[wikilinks]].
#
# Four checks (all break rendering in Obsidian):
#   1. A newline anywhere between `[[` and its closing `]]` stops Obsidian from
#      rendering the link — join it onto one line.
#   2. `$...$` math inside a wikilink (alias or target) shows as raw LaTeX in
#      Live Preview/Reading mode — move the math outside the link and link an
#      adjacent plain word, or use a plain/Unicode alias (see CLAUDE.md).
#   3. An unescaped alias pipe in a table splits the link across table cells.
#      Write [[target\|alias]] inside tables, including Evidence block links.
#   4. Evidence rows must have the same column count as their delimiter row;
#      literal pipes in code/math can split these cells too.
#
# Lists offenders (file:line). Exit 1 if any are found, 0 otherwise.
#
# Usage: scripts/check-wikilinks.sh [dir]   (default dir: wiki)
root="${1:-wiki}"
python3 - "$root" <<'PY'
import sys, re, pathlib
root = pathlib.Path(sys.argv[1])
pat = re.compile(r'\[\[[^\]]*?\]\]', re.S)   # a wikilink, possibly spanning lines
split, math, table_pipes, evidence_columns = [], [], [], []
pipe = re.compile(r'(?<!\\)(?:\\\\)*\|')
def columns(row):
    row = row.strip()
    delimiters = list(pipe.finditer(row))
    return (len(delimiters) + 1
            - bool(delimiters and delimiters[0].start() == 0)
            - bool(delimiters and delimiters[-1].end() == len(row)))

for f in sorted(root.rglob('*.md')):
    text = f.read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()
    table_rows = set()
    fence = None
    in_table = False
    evidence = False
    width = None
    for i, row in enumerate(lines):
        marker = re.match(r'^\s*(`{3,}|~{3,})', row)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            in_table = False
            continue
        if fence:
            continue
        if row.startswith('## '):
            evidence = row.strip() == '## Evidence'
        if re.fullmatch(r'\s*\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)+\|?\s*', row):
            table_rows.update((i, i + 1))  # previous header and this delimiter, 1-based
            in_table = True
            width = columns(row)
            if evidence and i > 0 and columns(lines[i - 1]) != width:
                evidence_columns.append((str(f), i, f'Evidence header: expected {width} columns, found {columns(lines[i - 1])}'))
        elif in_table and row.strip() and '|' in row:
            table_rows.add(i + 1)
            if evidence and columns(row) != width:
                evidence_columns.append((str(f), i + 1, f'Evidence row: expected {width} columns, found {columns(row)}'))
        else:
            in_table = False
    for m in pat.finditer(text):
        line = text[:m.start()].count('\n') + 1
        if '\n' in m.group(0):
            split.append((str(f), line, m.group(0).replace('\n', '\\n')))
        if '$' in m.group(0):
            math.append((str(f), line, m.group(0)))
        if line in table_rows and pipe.search(m.group(0)):
            table_pipes.append((str(f), line, m.group(0)))
for f, line, s in split + math + table_pipes + evidence_columns:
    print(f"  {f}:{line}: {s}")
fails = []
if split:
    fails.append(f"{len(split)} wikilink(s) split across a newline — join each onto one line")
if math:
    fails.append(f"{len(math)} wikilink(s) containing $ math — move math outside the link")
if table_pipes:
    fails.append(f"{len(table_pipes)} wikilink(s) with unescaped table pipes — use \\| inside tables")
if evidence_columns:
    fails.append(f"{len(evidence_columns)} Evidence row(s) with mismatched columns — escape literal pipes or repair shifted cells")
if fails:
    print("FAIL: " + "; ".join(fails))
    sys.exit(1)
print("OK: no split wikilinks, no math inside wikilinks, no unescaped table-link pipes; Evidence columns consistent")
PY
