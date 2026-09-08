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
   relevant papers and **offer** to `/wiki-ingest-arxiv` them — the fix for a missing answer is
   ingesting the source that has it. **Never ingest without the user's explicit go-ahead**:
   a question is a request for an answer, not for an ingest. Answer from what is available,
   label the gap (step 1), name the paper that would close it, and stop there — even when you
   are confident the ingest is the right next step, and even when running autonomously.
   Fetching a source to *read* while answering is fine; writing pages and committing is not.
3. **Record the gap.** An unanswerable question is a coverage signal: append
   `## [YYYY-MM-DD] query | <question> | GAP` to `Log.md` with what was missing, and plant a
   red link on the nearest topic/concept page so it enters the "write next" queue.

## 4. Compound

**Default output when the user resolved a genuine confusion.** If the user asked because they
were confused about something and the exchange clarified it (a multi-step "I don't get X → now I
do"), file a **`qa` page**: `wiki/qa/<slug>.md` from `templates/qa.md` (`type: qa`,
`status: resolved`). Distill the *core* of what confused them into **Question**, the resolved
understanding into **Answer** + **Key points**, and link the concepts/papers under **See also**.
This is distinct from `questions/` (research open problems raised by ingested papers) — do not
put learning Q&A there.

Otherwise, if the answer produced genuinely new *physics* synthesis (a connection or worked
result not already on any page):
- small addition → edit the relevant concept/result page;
- substantial standalone synthesis → new `wiki/notes/<slug>.md` linked from related pages.

Before filing anything, verify (AGENTS.md → Verification gate): re-check each sourced claim
against the cited paper's TeX inline; a substantial new note gets the same independent
refute-pass as an ingest (`/wiki-ingest-arxiv` step 5). Then run `scripts/check-wikilinks.sh`
and `scripts/check-frontmatter.sh`,
update `Index.md` if a page was added (a `qa` page goes under the `## Q&A` section), and append
`Log.md`: `## [YYYY-MM-DD] query | <short question> ` + pages touched.

If nothing new was produced and no confusion was resolved (pure lookup), skip filing — don't
create noise.
