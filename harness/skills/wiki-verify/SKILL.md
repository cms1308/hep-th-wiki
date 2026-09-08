---
name: wiki-verify
description: Verify already-written wiki pages against their source — a refute-pass that flags unsupported claims, altered formulas, dropped qualifiers, and invented terminology, then fixes confirmed findings. Use when the user wants to check an ingest (verification is no longer automatic).
---

# Verify wiki pages against source

Runs a refute-pass on demand. Ingest does not verify automatically; use this skill when
the user requests a source-based review of written pages.

Input: what to verify. Accept any of —
- an arXiv id / safe-id (e.g. `2507.08588`, `hep-th/9711200`) → verify that paper's pages;
- a non-arXiv source slug → verify that source's pages;
- `last` / nothing → verify the most recent `ingest` entry in `Log.md`.

## 1. Resolve target pages and source

- **Source path**: `sources/arxiv/<safe-id>/tex/` for arXiv papers (safe-id = id with `/`→`-`),
  or the filed `sources/pdf|web|notes/<slug>.*` for non-arXiv material.
- **Pages to check**: the paper page plus pages citing this source. Start from the ingest's
  created/updated lists in `Log.md`, then search current wiki backlinks to include later
  integrations. Resolve non-arXiv paper slugs and book chapter mappings from their hub/source
  metadata; do not assume the source slug equals the paper basename. If checking only a
  chapter, section, or selection of claims, state that scope explicitly.
- Read existing `verification/*.json` records for this target and their unresolved findings.
  A later limited review does not clear findings outside its scope.

## 2. Spawn the refute agent

Spawn a general-purpose agent. Give it the page list and the source path. Prompt it to
**refute, not confirm**: for every claim cited to this paper, locate the supporting statement
in the source; flag
- (a) claims the source doesn't support,
- (b) formulas that differ from the source (factors, signs, indices, ranges, exponents),
- (c) qualifiers or assumptions dropped — a claim stated more generally than the source proves,
- (d) terminology not in the source and not standard usage,
- plus author/date/arXiv-id attributions that don't match `meta.json` / the `.bbl`.

Use the paper's Evidence table as a navigation aid, but locate the actual support in the
source independently. Missing tables on legacy pages do not prevent verification; construct
locators while checking. Check assumptions, source certainty, and convention conversions.

Ask for a concise findings list (page/claim, source location, correction or unresolved reason),
the precise claims/sections covered, and the actual source files consulted. Claims that check
out need not be listed individually, but the coverage must be explicit. Record the reviewer's
identity; use an actual model ID only when available, otherwise say it is unknown.

## 3. Fix and record

- Fix every confirmed finding. A claim that can't be settled from the source is removed or kept
  only with an explicit `> [!warning] Unverified` callout — never silently.
- Recheck corrected claims against the source, update edited pages' `updated:`, and preserve
  their evidence locators. Run `scripts/check-wikilinks.sh` and `scripts/check-frontmatter.sh`.
- After final checks, prepare a temporary JSON manifest for the internal helper. Example
  shape (replace placeholders with actual checked paths and scope; do not copy as a verdict):

  ```json
  {
    "target": "source slug or arXiv ID",
    "reviewer": "independent refute agent; model unknown",
    "scope": "Claims R1–R3 on listed pages against this source only; history excluded",
    "outcome": "clean",
    "findings": [],
    "pages": ["wiki/papers/example.md"],
    "sources": ["sources/arxiv/example/tex/main.tex"]
  }
  ```

  `outcome` is `clean`, `corrected`, or `unresolved`. Findings record page/claim, source
  locator, correction, and whether resolved; do not omit unresolved items. `sources` lists
  every file actually used, including macro files, bibliography, metadata, or PDF where
  relevant. `pages` lists only checked pages. Scope must not imply checking uncited sources
  or the entire page when only selected claims were reviewed.
- Run `python3 scripts/verification-record.py --record <temporary-manifest.json>` to create
  an append-only `verification/<timestamp>.json` with exact-byte SHA-256 hashes of the final
  pages and sources. Hashes record versions, not truth. If files changed during review,
  recheck the affected content before recording; do not bless concurrent edits. Keep the
  manifest outside the tracked repository; the saved record is the durable artifact.
- Append `## [YYYY-MM-DD] verify | <id> | <title>` to `Log.md` with scope, outcome, fixes and
  record path. Commit and push the record and log even for a clean review with no page edits.
  A later edit leaves this record intact; `wiki-lint` reports it stale when hashes differ.
- Report the scoped verdict, unresolved items, and specific corrections. Do not equate
  matching hashes, no findings in a limited scope, or a model check with a physical proof.
