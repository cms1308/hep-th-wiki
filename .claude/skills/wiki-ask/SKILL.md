---
name: wiki-ask
description: Answer a physics question from the hep-th wiki with citations, going to raw TeX sources when equation-level depth is needed, and file new synthesis back into the wiki. Use for any physics question asked in this vault.
---

# Answer a question from the wiki

Input: a physics question.

If the question is really "how is X derived?" or asks for a worked derivation, use the
`wiki-derive` skill instead — derivations get their own page type and verification pass.

## 1. Locate

Read `Index.md`, identify candidate pages, read them, follow `[[links]]` (including
`prerequisites:`) until the question is covered. Grep `wiki/` for keywords the Index misses.

## 2. Deepen if needed

If the wiki's distillation is too shallow (equation-level detail, derivation steps), open the
underlying `sources/` TeX/PDF cited by the pages. Never answer from memory alone when sources
exist.

## 3. Answer

Cite wiki pages and papers inline (`[[hep-th-9711200|Maldacena 1997]]`). Match the user's
level; LaTeX math `$...$`.

## When the wiki and sources can't answer

The boundary must stay visible — never blur wiki-backed claims with model memory:

1. **Label the gap.** Answer what the wiki covers with citations; for the rest, state
   explicitly "not in the wiki — answering from general knowledge" and answer as well as you
   can. Never fabricate a `[[...]]` citation for a claim no page supports.
2. **Escalate to the literature.** If the question deserves a sourced answer (nontrivial
   physics, user needs to rely on it), search for the canonical reference: arXiv API
   (`https://export.arxiv.org/api/query?search_query=...`) or WebSearch. Present the 1-3 most
   relevant papers and offer to `/wiki-ingest-arxiv` them — the fix for a missing answer is
   ingesting the source that has it. If the user already said to go ahead (or asked
   autonomously), ingest directly and then answer from the new pages.
3. **Record the gap.** An unanswerable question is a coverage signal: append
   `## [YYYY-MM-DD] query | <question> | GAP` to `Log.md` with what was missing, and plant a
   red link on the nearest topic/concept page so it enters the "write next" queue.

## 4. Compound

If the answer produced genuinely new synthesis (a connection, a worked derivation, a
clarified confusion not already on any page):
- small addition → edit the relevant concept/result page;
- substantial standalone synthesis → new `wiki/notes/<slug>.md` linked from related pages;
- before filing, verify (CLAUDE.md → Verification gate): re-check each sourced claim against
  the cited paper's TeX inline; a substantial new note gets the same independent refute-pass
  as an ingest (`/wiki-ingest-arxiv` step 5);
- then update `Index.md` if a page was added, and append `Log.md`:
  `## [YYYY-MM-DD] query | <short question> ` + pages touched.

If nothing new was produced (pure lookup), skip filing — don't create noise.
