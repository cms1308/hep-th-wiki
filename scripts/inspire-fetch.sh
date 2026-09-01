#!/usr/bin/env bash
# inspire-fetch.sh <arxiv-id-or-url>
# Fetches INSPIRE-HEP bibliographic data for a paper already in sources/arxiv/<safe-id>/:
#   inspire.json  - raw INSPIRE record (selected fields)
#   refs.json     - trimmed: recid, citation_count, resolved reference list
# Non-fatal design: exits 0 with a warning if INSPIRE is unreachable or has no record.
set -uo pipefail

VAULT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

RAW="$1"
ID="$(echo "$RAW" | sed -E 's#https?://arxiv.org/(abs|pdf|e-print)/##; s#\.pdf$##; s#v[0-9]+$##')"
SAFE_ID="${ID//\//-}"
DEST="$VAULT_DIR/sources/arxiv/$SAFE_ID"
mkdir -p "$DEST"

FIELDS="titles,control_number,citation_count,citation_count_without_self_citations,arxiv_eprints,dois,publication_info,references"
curl -sL --max-time 30 "https://inspirehep.net/api/arxiv/$ID?fields=$FIELDS" -o "$DEST/inspire.json"
if [ ! -s "$DEST/inspire.json" ]; then
  echo "[inspire-fetch] WARNING: no response from INSPIRE for $ID (offline?); skipping" >&2
  rm -f "$DEST/inspire.json"
  exit 0
fi

python3 - "$DEST" "$ID" <<'EOF'
import json, sys
from datetime import date
dest, arxiv_id = sys.argv[1], sys.argv[2]
try:
    with open(f"{dest}/inspire.json", encoding="utf-8") as f:
        rec = json.load(f)
    meta = rec["metadata"]
except Exception:
    print(f"[inspire-fetch] WARNING: no INSPIRE record for {arxiv_id}; skipping",
          file=sys.stderr)
    sys.exit(0)

refs = []
for r in meta.get("references", []):
    ref = r.get("reference", {})
    entry = {
        "label": ref.get("label"),
        "arxiv": ref.get("arxiv_eprint"),
        "title": (ref.get("title") or {}).get("title"),
        "first_author": (ref.get("authors") or [{}])[0].get("full_name"),
        "year": (ref.get("publication_info") or {}).get("year"),
        "inspire_recid": (r.get("record") or {}).get("$ref", "").rsplit("/", 1)[-1] or None,
    }
    refs.append({k: v for k, v in entry.items() if v})

out = {
    "arxiv_id": arxiv_id,
    "inspire_recid": meta.get("control_number"),
    "citation_count": meta.get("citation_count"),
    "citation_count_without_self": meta.get("citation_count_without_self_citations"),
    "fetched": date.today().isoformat(),
    "references": refs,
}
with open(f"{dest}/refs.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=1)
n_arxiv = sum(1 for r in refs if "arxiv" in r)
print(f"[inspire-fetch] recid={out['inspire_recid']} citations={out['citation_count']} "
      f"refs={len(refs)} (with arXiv id: {n_arxiv})")
EOF
