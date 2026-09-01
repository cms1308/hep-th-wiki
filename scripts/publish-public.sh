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

# Commit as the same identity as the private vault (a machine may have no global git config).
git -C "$TMP" config user.name  "$(git -C "$VAULT" config user.name)"
git -C "$TMP" config user.email "$(git -C "$VAULT" config user.email)"

# The public mirror is a schema/skills/scripts showcase — it keeps a single
# curated example ingest (the Maldacena paper) under wiki/, and its own Index.md
# and Log.md describing just that example. Never overwrite the wiki content or
# its navigation with the private vault's full contents.
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete \
    --exclude .git \
    --exclude sources/ \
    --exclude wiki/ \
    --exclude Index.md \
    --exclude Log.md \
    --exclude .obsidian/ \
    --exclude .DS_Store \
    "$VAULT"/ "$TMP"/
else
  # Portable fallback (Git Bash on Windows ships no rsync), same semantics:
  # replace the mirror's infrastructure, protecting its curated wiki/, Index.md, Log.md.
  find "$TMP" -mindepth 1 -maxdepth 1 \
    ! -name .git ! -name wiki ! -name Index.md ! -name Log.md -exec rm -rf {} +
  (cd "$VAULT" && find . -mindepth 1 -maxdepth 1 \
    ! -name .git ! -name sources ! -name wiki ! -name Index.md ! -name Log.md \
    ! -name .obsidian -exec cp -R {} "$TMP"/ \;)
  find "$TMP" -path "$TMP/.git" -prune -o -name .DS_Store -type f -print0 | xargs -0 -r rm -f
  find "$TMP" -path "$TMP/.git" -prune -o -name .obsidian -type d -print0 | xargs -0 -r rm -rf
fi

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
