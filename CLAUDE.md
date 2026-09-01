# hep-th LLMwiki — Schema

This vault is a **hep-th knowledge wiki** maintained by Claude, following the LLMwiki pattern
(Karpathy): the human curates sources and asks questions; the LLM does all summarizing,
cross-referencing, filing, and bookkeeping. It is the user's second brain for theoretical
physics and a self-contained knowledge base that other physics projects can read.

## Three layers

1. **`sources/`** — raw, immutable input data. Never edit files here (only add via ingest).
2. **`wiki/`** — the knowledge layer. LLM-owned markdown. Freely create/update/restructure.
3. **This file** — the schema. Conventions and workflows. Co-evolves with the wiki: when a
   convention proves wrong, update it here and note the change in `Log.md`.

## Directory layout

```
CLAUDE.md            this schema
Index.md             navigation: every wiki page, grouped by type, one-line summary each
Log.md               append-only operation log
wiki/
  topics/            research areas (hubs with history)   e.g. ads-cft-correspondence
  concepts/          single ideas/objects/structures      e.g. holographic-principle
  methods/           techniques and how to apply them     e.g. large-n-expansion
  results/           established results & conjectures    e.g. ryu-takayanagi-formula
  derivations/       full worked derivations              e.g. rt-formula-derivation
  lectures/          textbook-derived lecture notes, subject-scoped  e.g. string-theory-worldsheet-cft
  questions/         open questions (research; from ingest) e.g. black-hole-information-paradox
  qa/                the user's resolved learning Q&A      e.g. ntk-vs-mup-lazy-vs-feature-learning
  people/            physicists                           e.g. juan-maldacena
  papers/            one digest page per ingested paper   e.g. hep-th-9711200
  notes/             user's own results and findings from other projects
sources/
  arxiv/<safe-id>/   TeX source + meta.json + INSPIRE data (inspire.json, refs.json)
                     (safe-id = arxiv id with / → -)
  pdf/               papers without TeX source
  books/             textbooks (pdf + pdftotext .txt search index + meta .md); wiki hub
                     page per book tracks per-chapter ingest status
  web/               clipped web content (markdown, url in frontmatter)
  notes/             user-written .tex/.md raw material
templates/           one template per page type — always start new pages from these
scripts/arxiv-fetch.sh    download arXiv metadata + TeX source (calls inspire-fetch.sh)
scripts/inspire-fetch.sh  INSPIRE-HEP recid, citation count, resolved references → refs.json
scripts/citation-links.py cites / cited-by among ingested papers (from refs.json files)
```

## Page types

Every wiki page answers a different question:

| type | answers | key sections |
|---|---|---|
| **topic** | "what is this field, how did it develop?" | Overview · Historical development (chronological, paper-linked) · Key concepts · Key results · Current status · Open questions |
| **concept** | "what is this thing?" | Definition · Motivation · Key formulas · Relations to other concepts · Where it appears |
| **method** | "how do I compute/derive with this?" | What it computes · Prerequisites · How it works · Regime of validity · Canonical applications |
| **result** | "what is known, and how solid is it?" | Statement · Derivation sketch · Assumptions · Status (proven / conjectured / disputed) · Implications |
| **derivation** | "how do you actually get this?" | Goal · Setup and conventions · Derivation (numbered, gap-free) · Checks · References — anchored to source TeX where it exists; `status: verified / unverified` |
| **question** | "what is unknown and why does it matter?" (research open problem, raised by an ingested paper) | Statement · Why it matters · Main attempts · Current status |
| **qa** | "what did *I* ask and understand?" (a confusion the user resolved via `/wiki-ask`) | Question · Answer · Key points · See also |
| **person** | "who is this, what did they do?" | Contributions · Key papers · Context |
| **paper** | "what does this paper say?" | TL;DR (structured block, see below) · Motivation · Historical context · Main results · Methods · Key equations · Open questions raised · Wiki links |
| **lecture** | "teach me this subject, chapter by chapter" (prose lecture note merged from all ingested textbooks; see below) | Narrative prose (motivation → development → key formulas) · Conventions · Coverage (which book chapters are digested) |
| **note** | "what did *I* find/learn?" | free-form, but must link into the wiki |

Motivation, ideas, and 기초지식(prerequisites) are **facets, not page types**: motivation is a
section on concept/paper/topic pages; prerequisites are the `prerequisites:` frontmatter list
plus inline links.

### Paper TL;DR block

The `## TL;DR` of a paper page is a structured block, not a single compressed sentence — it
is the accessible on-ramp for a reader unfamiliar with the subfield:

```
One-sentence plain summary of what the paper does.

**Problem**
- 1–2 bullets: what was unclear/unsolved and why it matters.

**Method**
- 1–3 bullets: the key idea/technique that does the work.

**Results**
- 2–3 bullets: what was established.

**Takeaway**
- 1–2 bullets: what changes now / the bigger picture.
```

Writing rules (these matter more than the structure):
- Every bullet must be readable **without following any link** — at most 1–2 wikilinks per
  bullet, jargon spelled out or dropped.
- One idea per bullet, complete sentences.
- Formulas, numbered claims, and precision live in the body sections (Main results, Key
  equations) — the TL;DR states the same content at lower resolution. The overlap with
  Motivation/Main results is intended (abstract vs. body).

Relatedly, each **Methods** entry notes which main result it feeds, ending with
"→ used in result 3" (omit only when the method is genuinely global to the paper).

### Lecture notes (textbooks)

Textbook chapters are ingested into **lecture notes** (`wiki/lectures/`): prose, pedagogical
write-ups for the user's learning — in addition to, not instead of, the usual concept /
method / result / derivation pages a chapter also feeds.

- **Subject-scoped, not book-scoped.** A note is "notes on worldsheet CFT", never "notes on
  Polchinski ch. 2". The first book ingested on a subject seeds the note structure — one
  note per chapter-sized topic, named after the topic. Later books on the same subject
  **merge** into the existing notes: supplements, alternative arguments, and filled gaps are
  added in place, each passage citing its source book (hub-page link + chapter/section).
- **The unit is a chapter-sized topic, not a chapter.** The book-chapter ↔ note mapping need
  not stay 1:1 across books: a later book's chapter may feed several notes, or two chapters
  one note. If a note outgrows a few screens, split it by topic and log the restructuring.
- **Notes own the narrative; concept pages stay canonical.** A note carries motivation,
  logical flow, and the key formulas needed to read it linearly as self-contained prose.
  Canonical definitions, full statements, and complete derivations live on concept / method /
  result / derivation pages, densely linked from the note — never duplicate a derivation
  into a note, link it.
- **Conventions**: a note declares its conventions up front (normally the first ingested
  book's); merged material from later books is translated into them, with the dictionary
  recorded in the note's Conventions section (the same layered-consistency policy as papers).
- The per-book **hub page** (under `papers/`) keeps tracking chapter ingest status and page
  mappings; its chapter table also records which lecture note(s) each chapter fed.

## Frontmatter schema

Every wiki page starts with YAML frontmatter:

```yaml
---
type: topic | concept | method | result | derivation | question | qa | person | paper | lecture | note
title: Human-readable title
aliases: []          # alternative names, common abbreviations
tags: []             # free-form, kebab-case, e.g. [holography, string-theory]
prerequisites: []    # page names this assumes, e.g. ["conformal-field-theory"]
status:              # results/questions: proven | established | conjectured | disputed | open | resolved; derivations: verified | unverified; qa: always resolved
arxiv:               # papers only: canonical id, e.g. hep-th/9711200
arxiv_url:           # papers only: https://arxiv.org/abs/<arxiv id> — clickable in Obsidian Properties
inspire:             # papers only: INSPIRE recid
citations:           # papers only: INSPIRE citation count at ingest (snapshot)
authors: []          # papers only
date:                # papers only: YYYY-MM-DD publication date
source:              # path under sources/ this page derives from
coverage: []         # lectures only: book chapters digested, e.g. ["polchinski-vol1 ch.2"]
read:                # papers only: false | YYYY-MM-DD — whether/when the USER read the paper
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Omit fields that don't apply. Always bump `updated:` when editing.

**Frontmatter must be valid YAML** — Obsidian shows a page whose frontmatter fails to parse as
having "invalid properties" and silently drops its aliases and tags. The two failure modes are
both unquoted values, and both are easy to hit with physics notation: brackets or braces inside
a flow sequence (`aliases: [foo, [A_n]_1, bar]`) and a colon inside a scalar
(`title: Strip tension: instanton strings`). Quote the offending value —
`aliases: [foo, "[A_n]_1", bar]`, `title: "Strip tension: instanton strings"` (commas inside
`{}`/`()`/`[]` are fine once the item is quoted). **Enforcement**: mechanical, via
`scripts/check-frontmatter.sh`, run alongside `scripts/check-wikilinks.sh` before committing.

`read:` is user-owned read-status tracking: ingest sets `read: false`; the user flips it to
the date they read the paper (Obsidian Properties panel). Claude never sets it to a date.
Filter unread papers in Obsidian search with `["read":false]`.

## Naming & linking conventions

- **File names**: kebab-case English slugs — `eternal-black-holes.md`, `juan-maldacena.md`.
- **Paper pages**: named by sanitized arXiv id — `hep-th-9711200.md`, `1905.08255.md`.
  Non-arXiv papers: `<firstauthor><year>-<slug>.md`.
- **Lecture notes**: subject-prefixed topic slugs — `string-theory-worldsheet-cft.md`,
  `string-theory-t-duality.md` — never a book's chapter number. The prefix keeps basenames
  vault-unique (Obsidian resolves wikilinks by basename, so a lecture must not collide with
  a concept page).
- **Links**: Obsidian wikilinks. Paper links always carry a human display alias:
  `[[hep-th-9711200|Maldacena 1997]]`. Concept links read naturally in prose:
  `the [[holographic-principle]]`.
- **Never wrap a line inside a wikilink**: the whole `[[target|alias]]` stays on one line —
  a newline anywhere between `[[` and its closing `]]` breaks Obsidian rendering (the link
  silently stops working). When wrapping prose, break *before* or *after* the link; a line
  that runs past the usual wrap width to keep a link whole is fine. **Enforcement**: any
  operation that writes wiki pages must run `scripts/check-wikilinks.sh` (and
  `scripts/check-frontmatter.sh`) before committing —
  it lists every split link (`file:line`) and exits non-zero; join each onto one line until
  it reports clean. This check is mechanical, so never rely on eyeballing alone.
- **Never put `$...$` math inside a wikilink alias**: Obsidian renders the alias text as
  raw LaTeX in both Live Preview and Reading mode (the `$\lambda$` shows literally, not as
  $\lambda$). Keep math *outside* the `[[...]]` and link an adjacent plain word: write
  `$\lambda$-[[holomorphic-lambda-bracket|brackets]]`,
  not `[[holomorphic-lambda-bracket|$\lambda$-brackets]]`. When the alias would be pure math,
  use a plain/Unicode alias (`[[critical-dimension|D=26]]`, `[[ads4-s-fold-solution|AdS₄ S-fold]]`)
  or put the math in prose and follow it with a parenthetical link whose alias is plain
  Unicode/English: `$\Gamma_0(2)$ ([[gamma0-2-duality-0b|Γ₀(2)]])`. **Enforcement**: also
  checked mechanically by `scripts/check-wikilinks.sh` (flags any `$` inside a wikilink).
- **Broken links are allowed** — a red link means "worth a page, not written yet". The lint
  workflow surfaces them as a TODO list.
- **Citations in prose**: claims taken from a paper cite it inline via its paper-page link.

## Math & convention policy

- Obsidian MathJax: `$...$` inline, `$$...$$` display.
- Expand paper-specific custom macros to standard LaTeX when writing wiki pages —
  pages must be self-contained.
- Use only macros MathJax actually has: package macros like `\slashed` don't render in
  Obsidian — write `\not D` for the Dirac slash.

Sources use conflicting conventions (signatures, normalizations, supercharge choices,
factors of $2\pi$). The wiki does **not** enforce one global convention — it enforces
**layered consistency with explicit conversion maps**:

1. **Page level (mandatory)**: every page is internally consistent and *declares* its
   conventions where they matter (derivations: the "Setup and conventions" section;
   concept/result pages: a one-line note next to the first formula).
2. **Topic level (default)**: a topic may declare a wiki-canonical convention (a
   "Conventions" section on the topic page). Pages under that topic default to it, and
   ingested material is translated into it.
3. **Translation is recorded, never silent**: when a paper's equations are converted, the
   paper page's "Conventions" section states the source's conventions and the dictionary to
   the wiki-canonical ones (e.g. $g^2_{\text{paper}} = 2 g^2_{\text{wiki}}$). Nontrivial
   conversions (signs, spinors) are spot-checked against a known result before being used.
4. **Physical differences are not conventions**: when a "convention choice" changes the
   observable (e.g. a superconformal index defined with a different supercharge has a
   different commutant and different fugacities), do **not** unify — create disambiguated
   pages/sections and state the relation between the objects.

## Workflows (implemented as skills)

- **`/wiki-ingest-arxiv <id|url> [...]`** — fetch TeX + metadata, deep-read via the
  `paper-analyst` agent, write the paper page, create/update every touched topic / concept /
  method / result / question / person page, update `Index.md`, append to `Log.md`.
- **`/wiki-ingest <path|url>`** — same integration for non-arXiv material (PDF, web, user tex,
  project results → `notes/`). Textbook chapters additionally create or merge into the
  subject's lecture note (see "Lecture notes (textbooks)").
- **`/wiki-ask <question>`** — answer from the wiki first (Index → pages → sources when depth
  is needed). Cite pages and papers. If the answer produced genuinely new synthesis, file it
  back (usually a `notes/` page or an update to a concept page) — queries compound the wiki.
- **`/wiki-derive <what>`** — work out a derivation step by step (anchored to source TeX when
  it exists), verify it (dimensions, limits, independent check), record it as a
  `derivations/` page linked from the relevant result/concept pages.
- **`/wiki-lint`** — health check: contradictions, orphan pages, broken links worth writing,
  missing prerequisites, stale `Index.md` entries, papers ingested but poorly integrated.
- **`/wiki-next`** — ranked suggestions for what to add next, aggregated from recorded
  signals (GAPs, red links, topic frontiers, unread chapters, missing derivations).

- **`/wiki-verify`** — on-demand refute-pass of already-written pages against their source:
  claims cited to a paper but not supported by its source, formulas that differ,
  qualifiers/assumptions dropped (claim stated more generally than the source proves),
  terminology not in the source or standard usage. Fixes confirmed findings.

**Verification is on-demand, not a gate**: ingest writes pages directly from the
`paper-analyst` extraction and commits — it does **not** verify automatically. Verification
runs only when the user asks, via `/wiki-verify <id>` (an independent agent prompted to
**refute**, on the written pages + the source). Fix every confirmed finding; a claim that
can't be settled from the source is removed or explicitly flagged, never silently kept. For
small manual edits, re-check the claim against the cited source inline. (Derivation pages have
their own check — `/wiki-derive` step 3.)

Any ingest touching the wiki **must** end by updating `Index.md` and appending one `Log.md`
line, then `git commit` and `git push` (origin = the **private** repo, full sources). `wiki/`
**is tracked by git** — a commit carries the pages it created and edited alongside `sources/`,
`Index.md`, `Log.md`, and infrastructure, so the diff shows what the message and `Log.md`
claim, a page's provenance survives later rewrites (`git log -p wiki/...`), and a bad ingest
reverts atomically. Obsidian Sync stays the cross-device sync layer; it is not the history.
`.obsidian/` and `.DS_Store` remain ignored. Every operation ends committed — sessions are
disposable; the vault (files + git history + Obsidian Sync) is the only state that matters.
A fresh session recovers all context from this file, `Index.md`, and `Log.md`.

The **public mirror** (github.com/cms1308/hep-th-wiki) is a separate, sources-free history:
`scripts/publish-public.sh` rsyncs infrastructure only — it excludes `sources/`, `wiki/`,
`Index.md` and `Log.md`, so the mirror keeps its own curated one-paper example. Run it after
the private push whenever an update touched `CLAUDE.md`, `.claude/skills/`, `scripts/` or
`templates/`; it is a clean no-op for a pure-ingest commit. Never push the private history
public: past commits contain copyrighted arXiv TeX.

## New page vs. edit heuristic

- Distinct, linkable entity (a concept someone would say "look up X" about) → **new page**.
- An attribute, example, or update to something existing → **edit in place**.
- One paper typically touches 5–15 pages. Prefer dense linking over long pages: if a section
  outgrows ~a screen, consider splitting it into its own concept page.
- **No page without a source.** Every knowledge page (topic / concept / method / result /
  derivation / question / person / paper / lecture / note) must derive its substantive content from
  ingested material under `sources/` and cite it. Never write a page from model general
  knowledge alone — if a needed concept has no ingested source, leave it as a red link and
  ingest a proper reference first. Background sentences woven into a sourced page are
  tolerated only when they are unambiguous standard usage; anything nontrivial (definitions,
  theorems, worked computations) needs a source. `qa` pages record the user's resolved
  understanding from a conversation and cite the pages/papers the answer drew on; any part of
  a qa answer that came from general knowledge must say so explicitly in the text.

## Log.md format

Append-only, one entry per operation, parseable by grep:

```
## [YYYY-MM-DD] ingest | hep-th/9711200 | The Large N Limit of ...
- created: papers/hep-th-9711200, topics/ads-cft-correspondence, ...
- updated: Index
```

Prefixes: `ingest | query | derive | lint | schema | note`.

## Answering physics questions (also from other projects)

When any Claude session uses this vault as a knowledge base: **read `Index.md` first**, follow
links, trust wiki pages as the distilled state of knowledge, and drop to `sources/` TeX only
when equation-level detail is required. Wiki pages cite their sources — propagate those
citations into any downstream answer.
