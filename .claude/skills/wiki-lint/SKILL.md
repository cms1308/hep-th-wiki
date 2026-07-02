---
name: wiki-lint
description: Health-check the hep-th wiki — contradictions, orphan pages, broken links, stale Index, missing prerequisites, poorly integrated papers. Use periodically or when the user asks for a wiki check.
---

# Lint the wiki

## Checks

1. **Index freshness** — every `wiki/**/*.md` appears in `Index.md` and vice versa; summaries
   still match page content.
2. **Broken links** — collect all `[[targets]]` with no file. These are features (planned
   pages), but rank them by inbound-link count as a "write next" list.
3. **Orphans** — wiki pages with zero inbound links from other wiki pages.
4. **Frontmatter** — missing/invalid `type`, missing `updated`, papers without `arxiv`/`source`.
5. **Integration depth** — paper pages whose "Wiki links" section is empty or that no
   topic/concept page links back to (ingested but not integrated).
6. **Contradictions / staleness** — spawn parallel Explore agents over `wiki/` clusters
   (by topic) to flag pages making conflicting claims, or `status: conjectured` results the
   wiki elsewhere treats as proven. Flag, don't silently fix.
7. **Prerequisite gaps** — `prerequisites:` entries with no page and no red-link mention.
8. **Convention hygiene** — pages mixing conventions without declaring them; equations
   translated from a source without a conversion dictionary on the paper page; two pages
   silently using clashing conventions inside one topic.

Use `grep`/`scripts` for mechanical checks (1–5); read pages only for 6.

## Output

A ranked report: contradictions first, then integration gaps, then top-N broken links worth
writing, then mechanical fixes. Apply mechanical fixes (Index sync, frontmatter) directly;
propose content fixes to the user. Append a `## [YYYY-MM-DD] lint | ...` entry to `Log.md`
with what was found/fixed.
