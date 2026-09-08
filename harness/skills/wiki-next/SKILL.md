---
name: wiki-next
description: Suggest what to add to the hep-th wiki next, ranked by recorded signals (red links, unanswered-question GAPs, topic frontiers, unread book chapters). Use when the user asks what to ingest or write next.
---

# Suggest the next wiki additions

No new pages are written — this is a recommendation pass. Aggregate the vault's recorded
signals; do not recommend from memory alone.

## 1. Collect signals (all mechanical, from disk)

- **Red links**: grep `wiki/` for `[[targets]]` with no file; rank by inbound-link count.
  Include the "red links (write next)" lists in `Log.md`.
- **GAPs**: `grep "| GAP" Log.md` — questions the wiki couldn't answer are the strongest
  demand signal.
- **Integration frontiers**: topic pages' "Open questions" and "Historical development"
  entries pointing at papers not yet in `wiki/papers/`; results with `status: conjectured`
  whose resolving/refining papers are missing.
- **Unread chapters**: book hub pages with `unread` rows.
- **Derivation debt**: result pages whose "Derivation sketch" has no `[[derivation]]` link.

## 2. Rank and concretize

Order by: GAPs (user actually asked) > heavily-linked red links > frontier papers that would
close several red links at once > chapters/derivations. For each suggestion, name the
**concrete action**: the arXiv id to `/wiki-ingest-arxiv` (search arXiv/web if the canonical
reference isn't already cited somewhere in the wiki), the page slug to write, or the
`/wiki-derive` target.

Two INSPIRE-powered signals sharpen the ranking:
- **Reference frequency**: `sources/arxiv/*/refs.json` — a paper referenced by several
  already-ingested papers (but not yet ingested itself) is load-bearing; count occurrences
  of each arXiv id across all refs.json files.
- **Citation count as tie-breaker**: when choosing among candidate papers for the same red
  link, `curl -sL "https://inspirehep.net/api/arxiv/<id>?fields=citation_count"` identifies
  the canonical reference.

## 3. Report

A short ranked list (≤ ~7 items): action · why (which signal) · what it unlocks. End with the
single best next command to run. Do not log or commit — nothing changed.
