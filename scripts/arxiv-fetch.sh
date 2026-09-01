#!/usr/bin/env bash
# arxiv-fetch.sh <arxiv-id-or-url>
# Downloads arXiv metadata + TeX source (or PDF fallback) into sources/arxiv/<sanitized-id>/
#   meta.json        - title, authors, date, abstract, categories
#   abstract.md      - human-readable metadata summary
#   tex/             - extracted TeX source (if available)
#   paper.pdf        - only if no TeX source exists
# Exits 0 on success. Prints the target directory on the last line.
set -euo pipefail

VAULT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

RAW="$1"
# Accept URLs like https://arxiv.org/abs/hep-th/9711200v3 or bare ids
ID="$(echo "$RAW" | sed -E 's#https?://arxiv.org/(abs|pdf|e-print)/##; s#\.pdf$##; s#v[0-9]+$##')"
SAFE_ID="${ID//\//-}"
DEST="$VAULT_DIR/sources/arxiv/$SAFE_ID"
mkdir -p "$DEST"

echo "[arxiv-fetch] id=$ID -> $DEST"

# --- metadata via arXiv API (retry on rate limit / transient errors) ---
for attempt in 1 2 3; do
  curl -sL "https://export.arxiv.org/api/query?id_list=$ID" -o "$DEST/api-response.xml"
  if head -c 6 "$DEST/api-response.xml" | grep -q "^<?xml"; then
    break
  fi
  echo "[arxiv-fetch] non-XML API response (attempt $attempt): $(head -c 60 "$DEST/api-response.xml")" >&2
  [ "$attempt" -lt 3 ] && sleep $((attempt * 10))
done
python3 - "$DEST" "$ID" <<'EOF'
import json, re, sys, xml.etree.ElementTree as ET
dest, arxiv_id = sys.argv[1], sys.argv[2]
ns = {'a': 'http://www.w3.org/2005/Atom'}
root = ET.parse(f"{dest}/api-response.xml").getroot()
e = root.find('a:entry', ns)
if e is None or e.find('a:title', ns) is None:
    sys.exit(f"ERROR: no arXiv entry found for {arxiv_id}")
clean = lambda s: re.sub(r'\s+', ' ', (s or '').strip())
meta = {
    'arxiv_id': arxiv_id,
    'title': clean(e.findtext('a:title', '', ns)),
    'authors': [clean(a.findtext('a:name', '', ns)) for a in e.findall('a:author', ns)],
    'date': e.findtext('a:published', '', ns)[:10],
    'updated': e.findtext('a:updated', '', ns)[:10],
    'abstract': clean(e.findtext('a:summary', '', ns)),
    'categories': [c.get('term') for c in e.findall('a:category', ns)],
    'abs_url': f"https://arxiv.org/abs/{arxiv_id}",
}
with open(f"{dest}/meta.json", 'w', encoding='utf-8') as f:
    json.dump(meta, f, indent=2)
with open(f"{dest}/abstract.md", 'w', encoding='utf-8') as f:
    f.write(f"# {meta['title']}\n\n")
    f.write(f"- arXiv: {meta['abs_url']}\n")
    f.write(f"- Authors: {', '.join(meta['authors'])}\n")
    f.write(f"- Date: {meta['date']}\n")
    f.write(f"- Categories: {', '.join(meta['categories'])}\n\n")
    f.write(f"## Abstract\n\n{meta['abstract']}\n")
print(f"[arxiv-fetch] metadata: {meta['title']}")
EOF

# --- TeX source (e-print) ---
TMP="$DEST/eprint.download"
curl -sL "https://arxiv.org/e-print/$ID" -o "$TMP"
KIND="$(file -b "$TMP")"
echo "[arxiv-fetch] e-print type: $KIND"

rm -rf "$DEST/tex"
mkdir -p "$DEST/tex"
case "$KIND" in
  *gzip*)
    if tar -tzf "$TMP" >/dev/null 2>&1; then
      tar -xzf "$TMP" -C "$DEST/tex"
    else
      gunzip -c "$TMP" > "$DEST/tex/main.tex"
    fi
    rm "$TMP"
    echo "[arxiv-fetch] TeX source extracted:"
    find "$DEST/tex" -type f | sed "s#$DEST/##"
    ;;
  *tar*)
    tar -xf "$TMP" -C "$DEST/tex"
    rm "$TMP"
    echo "[arxiv-fetch] TeX source extracted:"
    find "$DEST/tex" -type f | sed "s#$DEST/##"
    ;;
  *PDF*)
    rmdir "$DEST/tex"
    mv "$TMP" "$DEST/paper.pdf"
    echo "[arxiv-fetch] no TeX source; saved paper.pdf"
    ;;
  *)
    # single uncompressed tex file
    mv "$TMP" "$DEST/tex/main.tex"
    echo "[arxiv-fetch] saved as tex/main.tex"
    ;;
esac

# --- INSPIRE-HEP bibliographic data (non-fatal if unavailable) ---
"$VAULT_DIR/scripts/inspire-fetch.sh" "$ID" || true

echo "$DEST"
