#!/usr/bin/env bash
# publish-public.sh
# Publishes a sources-free snapshot of the vault to the public mirror repo.
# The public repo gets its own history (never the private one, which contains
# copyrighted arXiv TeX in past commits).
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/.." && pwd)"
PUBLIC_REMOTE="${PUBLIC_REMOTE:-https://github.com/cms1308/hep-th-wiki.git}"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Reuse the mirror's existing history if it has one; otherwise start fresh.
if git clone --depth 1 "$PUBLIC_REMOTE" "$TMP" 2>/dev/null; then
  echo "[publish] cloned existing mirror"
else
  git -C "$TMP" init -q -b main
  git -C "$TMP" remote add origin "$PUBLIC_REMOTE"
  echo "[publish] initialized new mirror"
fi

# The public mirror is a schema/skills/scripts showcase — it keeps a single
# curated example ingest (the Maldacena paper) under wiki/, and its own Index.md
# and Log.md describing just that example. Never overwrite the wiki content or
# its navigation with the private vault's full contents.
rsync -a --delete \
  --exclude .git \
  --exclude sources/ \
  --exclude wiki/ \
  --exclude Index.md \
  --exclude Log.md \
  --exclude .obsidian/ \
  --exclude .DS_Store \
  "$VAULT"/ "$TMP"/

# Public clones should keep re-fetched sources out of git.
grep -q "^sources/$" "$TMP/.gitignore" 2>/dev/null || echo "sources/" >> "$TMP/.gitignore"

cd "$TMP"
git add -A
if git diff --cached --quiet; then
  echo "[publish] mirror already up to date"
  exit 0
fi
git commit -q -m "publish: snapshot $(date +%F)"
git push -u origin main
echo "[publish] pushed snapshot to $PUBLIC_REMOTE"
