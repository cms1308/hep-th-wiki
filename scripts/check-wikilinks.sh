#!/usr/bin/env bash
# check-wikilinks.sh — flag malformed Obsidian [[wikilinks]].
#
# Two checks (both break rendering in Obsidian):
#   1. A newline anywhere between `[[` and its closing `]]` stops Obsidian from
#      rendering the link — join it onto one line.
#   2. `$...$` math inside a wikilink (alias or target) shows as raw LaTeX in
#      Live Preview/Reading mode — move the math outside the link and link an
#      adjacent plain word, or use a plain/Unicode alias (see CLAUDE.md).
#
# Lists offenders (file:line). Exit 1 if any are found, 0 otherwise.
#
# Usage: scripts/check-wikilinks.sh [dir]   (default dir: wiki)
root="${1:-wiki}"
python3 - "$root" <<'PY'
import sys, re, pathlib
root = pathlib.Path(sys.argv[1])
pat = re.compile(r'\[\[[^\]]*?\]\]', re.S)   # a wikilink, possibly spanning lines
split, math = [], []
for f in sorted(root.rglob('*.md')):
    text = f.read_text(encoding='utf-8', errors='replace')
    for m in pat.finditer(text):
        line = text[:m.start()].count('\n') + 1
        if '\n' in m.group(0):
            split.append((str(f), line, m.group(0).replace('\n', '\\n')))
        if '$' in m.group(0):
            math.append((str(f), line, m.group(0)))
for f, line, s in split + math:
    print(f"  {f}:{line}: {s}")
fails = []
if split:
    fails.append(f"{len(split)} wikilink(s) split across a newline — join each onto one line")
if math:
    fails.append(f"{len(math)} wikilink(s) containing $ math — move math outside the link")
if fails:
    print("FAIL: " + "; ".join(fails))
    sys.exit(1)
print("OK: no split wikilinks, no math inside wikilinks")
PY
