---
name: wiki-verify
description: Verify already-written wiki pages against their source — a refute-pass that flags unsupported claims, altered formulas, dropped qualifiers, and invented terminology, then fixes confirmed findings. Use when the user wants to check an ingest (verification is no longer automatic).
---

# Verify wiki pages against source

Runs the refute-pass that used to be step 5 of ingest, on demand. Ingest no longer verifies
automatically — this skill is how the user checks a paper's pages whenever they want.

Input: what to verify. Accept any of —
- an arXiv id / safe-id (e.g. `2507.08588`, `hep-th/9711200`) → verify that paper's pages;
- a non-arXiv source slug → verify that source's pages;
- `last` / nothing → verify the most recent `ingest` entry in `Log.md`.

## 1. Resolve target pages and source

- **Source path**: `sources/arxiv/<safe-id>/tex/` for arXiv papers (safe-id = id with `/`→`-`),
  or the filed `sources/pdf|web|notes/<slug>.*` for non-arXiv material.
- **Pages to check**: the paper page `wiki/papers/<safe-id>.md` plus every page it created or
  updated. Get this list from the paper's `Log.md` entry (created/updated lists). If the ingest
  is recent and uncommitted, `git diff --name-only` works too. Include only pages that cite this
  source (`[[<safe-id>|...]]`).

## 2. Spawn the refute agent

Spawn a general-purpose agent. Give it the page list and the source path. Prompt it to
**refute, not confirm**: for every claim cited to this paper, locate the supporting statement
in the source; flag
- (a) claims the source doesn't support,
- (b) formulas that differ from the source (factors, signs, indices, ranges, exponents),
- (c) qualifiers or assumptions dropped — a claim stated more generally than the source proves,
- (d) terminology not in the source and not standard usage,
- plus author/date/arXiv-id attributions that don't match `meta.json` / the `.bbl`.

Ask it to return a concise findings list (page, source location, correct version); claims that
check out are not listed.

## 3. Fix and record

- Fix every confirmed finding. A claim that can't be settled from the source is removed or kept
  only with an explicit `> [!warning] Unverified` callout — never silently.
- Append a `Log.md` entry: `## [YYYY-MM-DD] verify | <id> | <title>` with what was checked and
  any findings fixed. `git commit` (and push) if fixes were made.
- Report to the user: verdict (clean / N findings fixed) and the specific corrections.
