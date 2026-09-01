#!/usr/bin/env bash
# check-frontmatter.sh — flag wiki pages whose YAML frontmatter does not parse.
#
# Obsidian shows these as "invalid properties" and silently drops aliases/tags.
# The two failure modes seen in practice, both from unquoted values:
#   1. Brackets/braces inside a flow sequence:
#        aliases: [foo, [A_n]_1, bar]        -> quote it: "[A_n]_1"
#      (note commas inside {} () [] are fine once the item is quoted)
#   2. A colon inside an unquoted scalar:
#        title: Strip tension: instanton...  -> quote the whole value
#
# Lists offenders (file: error). Exit 1 if any are found, 0 otherwise.
# Skips files with no frontmatter (e.g. the user's own scratch notes).
#
# Usage: scripts/check-frontmatter.sh [dir]   (default dir: wiki)
root="${1:-wiki}"
python3 - "$root" <<'PY'
import sys, pathlib
try:
    import yaml
except ImportError:
    print("SKIP: PyYAML not installed (pip3 install pyyaml) — frontmatter unchecked")
    sys.exit(0)
root = pathlib.Path(sys.argv[1])
bad = []
for f in sorted(root.rglob('*.md')):
    t = f.read_text(encoding='utf-8', errors='replace')
    if not t.startswith('---\n'):
        continue                      # no frontmatter: not a knowledge page
    end = t.find('\n---', 4)
    if end == -1:
        bad.append((str(f), 'frontmatter never closed')); continue
    try:
        d = yaml.safe_load(t[4:end])
        if not isinstance(d, dict):
            bad.append((str(f), 'frontmatter is not a key/value mapping'))
    except Exception as e:
        bad.append((str(f), str(e).splitlines()[0][:80]))
for f, e in bad:
    print(f"  {f}: {e}")
if bad:
    print(f"FAIL: {len(bad)} page(s) with unparseable frontmatter — quote the offending value")
    sys.exit(1)
print("OK: all frontmatter parses")
PY
