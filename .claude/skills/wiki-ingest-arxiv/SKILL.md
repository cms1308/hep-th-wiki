---
name: wiki-ingest-arxiv
description: Ingest one or more arXiv papers into the hep-th wiki — fetch TeX source, deep-read, create/update all touched wiki pages, update Index and Log. Use when the user gives arXiv ids/urls to add to the wiki.
---

# Ingest arXiv paper(s)

Input: one or more arXiv ids or urls (e.g. `hep-th/9711200`, `2303.01111`,
`https://arxiv.org/abs/1905.08255`). For multiple papers, run steps 1–2 for all papers in
parallel, then integrate one paper at a time (step 3 onward) to avoid write conflicts.

## 1. Fetch

```
scripts/arxiv-fetch.sh <id-or-url>
```

This writes `sources/arxiv/<safe-id>/` with `meta.json`, `abstract.md`, `tex/` (or
`paper.pdf` when no TeX exists — then follow the PDF path of `/wiki-ingest` instead), and
INSPIRE data: `inspire.json` + `refs.json` (recid, citation count, resolved reference list).
INSPIRE being unreachable is non-fatal — proceed and note it in the Log entry.
If the paper is already in `sources/arxiv/` and has a paper page, stop and tell the user it's
already ingested (offer to re-integrate).

## 2. Deep-read

Spawn the `paper-analyst` agent on the fetched source directory, using the host/model
preference in CLAUDE.md. Ask it to inventory substantive source content before writing
the structured extraction, including a Reading guide, reusable technical details and
Evidence. Do not impose a result/equation count that drops important content.

## 3. Reconcile against the existing wiki

Read `Index.md`. For each suggested entity decide:
- page exists → **update** it (add this paper to "Where it appears" / "Key papers" /
  "Historical development", enrich sections if the paper adds substance);
- doesn't exist but is a distinct linkable entity → **create** from `templates/<type>.md`;
- marginal → just link it in prose (broken link = "write later").

Check for contradictions with existing pages; if found, state both claims with citations on
the affected page under a `> [!warning] Tension` callout.

Reconcile conventions (see CLAUDE.md → Math & convention policy): if the touched topic has a
canonical convention, translate the paper's equations into it and record the conversion
dictionary in the paper page's "Conventions" section — never convert silently. If the
difference is physical (e.g. a different supercharge defining an index), disambiguate
instead of unifying.

## 4. Write

- `wiki/papers/<safe-id>.md` from `templates/paper.md` — the full digest, LaTeX math in
  `$...$`, custom macros expanded. Follow CLAUDE.md → Paper explanations and technical
  completeness: teach the argument in readable prose, retain precise statements and
  calculation ingredients in the appropriate sections or linked canonical pages. Keep
  required details on the paper page when the user requests paper-only scope.
  Fill the "Wiki links" section with every touched page.
  Preserve the analyst's `Evidence` table for every main result and key equation, including
  source locators, assumptions, certainty, and convention conversions. Reconcile IDs if
  results are reordered. Put source citations/locators only in Evidence, not also after body
  paragraphs or formulas; map other sourced passages by section/claim name. For claims
  propagated to other pages, follow CLAUDE.md → Evidence and document verification.
  This provenance does not mark the ingest as independently reviewed.
  Frontmatter `inspire:`/`citations:` come from `refs.json`; set `arxiv_url:` to
  `https://arxiv.org/abs/<arxiv id>` (use the full id — do not let a trailing zero drop).
- Citation graph: run `python3 scripts/citation-links.py <safe-id>` and fill the paper's
  "Citation graph" section. **Both directions**: also append this paper to the "Cited by"
  line of every wiki paper it cites, and check whether previously ingested papers cite this
  one (older papers gain a "Cited by" entry when a classic they cite finally gets ingested
  — the script reports this).
- Create/update the topic, concept, method, result, question, person pages decided in step 3.
  Every claim sourced from this paper links back as `[[<safe-id>|Author Year]]`.
- Follow all conventions in `CLAUDE.md` (frontmatter, naming, math).

Before bookkeeping, compare the written pages against the analyst's Source inventory.
Fill the paper's Source coverage table with Evidence IDs and actual destinations
(page section or linked page); record reasons for intentional omissions and restore
missing important content. Include a source locator only for items without an Evidence entry.
Check that editing retained the equations, assumptions and
material caveats. This checks coverage of the extraction, not its independent correctness;
do not run a refute agent or create a verification record as part of ingest.

## 5. Bookkeep

- Update `Index.md`: add every new page under its type heading with a one-line summary.
- Append one entry to `Log.md`:
  `## [YYYY-MM-DD] ingest | <arxiv-id> | <title>` + created/updated page lists.
- **Before committing**, run `scripts/check-wikilinks.sh` and `scripts/check-frontmatter.sh` —
  both must report clean (exit 0).
  A `[[...]]` split across a newline renders as plain text in Obsidian; join any offender it
  lists onto one line and re-run until clean.

## 6. Report

**Minimal, token-saving** (user request, 2026-09-01): no process narration during the ingest
and no content summary at the end — the pages and `Log.md` carry the content. Report only:
commit hash, page counts (created/updated), and anything that needs the user's attention
(tensions, source inconsistencies, failures, follow-ups). A few lines at most.

Verification is **not** part of ingest — it runs separately, only when the user asks, via
`/wiki-verify <arxiv-id>` (see the `wiki-verify` skill). Ingest writes pages directly from the
`paper-analyst` extraction and commits.
