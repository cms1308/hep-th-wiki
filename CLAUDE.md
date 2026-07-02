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
  questions/         open questions                       e.g. black-hole-information-paradox
  people/            physicists                           e.g. juan-maldacena
  papers/            one digest page per ingested paper   e.g. hep-th-9711200
  notes/             user's own results, Q&A outcomes, findings from other projects
sources/
  arxiv/<safe-id>/   TeX source + meta.json + INSPIRE data (inspire.json, refs.json)
                     (safe-id = arxiv id with / → -)
  pdf/               papers without TeX source
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
| **question** | "what is unknown and why does it matter?" | Statement · Why it matters · Main attempts · Current status |
| **person** | "who is this, what did they do?" | Contributions · Key papers · Context |
| **paper** | "what does this paper say?" | TL;DR · Motivation · Historical context · Main results · Methods · Key equations · Open questions raised · Wiki links |
| **note** | "what did *I* find/learn?" | free-form, but must link into the wiki |

Motivation, ideas, and 기초지식(prerequisites) are **facets, not page types**: motivation is a
section on concept/paper/topic pages; prerequisites are the `prerequisites:` frontmatter list
plus inline links.

## Frontmatter schema

Every wiki page starts with YAML frontmatter:

```yaml
---
type: topic | concept | method | result | derivation | question | person | paper | note
title: Human-readable title
aliases: []          # alternative names, common abbreviations
tags: []             # free-form, kebab-case, e.g. [holography, string-theory]
prerequisites: []    # page names this assumes, e.g. ["conformal-field-theory"]
status:              # results/questions: proven | conjectured | open | resolved; derivations: verified | unverified
arxiv:               # papers only: canonical id, e.g. hep-th/9711200
inspire:             # papers only: INSPIRE recid
citations:           # papers only: INSPIRE citation count at ingest (snapshot)
authors: []          # papers only
date:                # papers only: YYYY-MM-DD publication date
source:              # path under sources/ this page derives from
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Omit fields that don't apply. Always bump `updated:` when editing.

## Naming & linking conventions

- **File names**: kebab-case English slugs — `eternal-black-holes.md`, `juan-maldacena.md`.
- **Paper pages**: named by sanitized arXiv id — `hep-th-9711200.md`, `1905.08255.md`.
  Non-arXiv papers: `<firstauthor><year>-<slug>.md`.
- **Links**: Obsidian wikilinks. Paper links always carry a human display alias:
  `[[hep-th-9711200|Maldacena 1997]]`. Concept links read naturally in prose:
  `the [[holographic-principle]]`.
- **Broken links are allowed** — a red link means "worth a page, not written yet". The lint
  workflow surfaces them as a TODO list.
- **Citations in prose**: claims taken from a paper cite it inline via its paper-page link.

## Math & convention policy

- Obsidian MathJax: `$...$` inline, `$$...$$` display.
- Expand paper-specific custom macros to standard LaTeX when writing wiki pages —
  pages must be self-contained.

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
  project results → `notes/`).
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

Any ingest touching the wiki **must** end by updating `Index.md` and appending one `Log.md`
line, then `git commit`. Every operation ends committed — sessions are disposable; the vault
(files + git history) is the only state that matters. A fresh session recovers all context
from this file, `Index.md`, and `Log.md`.

## New page vs. edit heuristic

- Distinct, linkable entity (a concept someone would say "look up X" about) → **new page**.
- An attribute, example, or update to something existing → **edit in place**.
- One paper typically touches 5–15 pages. Prefer dense linking over long pages: if a section
  outgrows ~a screen, consider splitting it into its own concept page.

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
