---
name: wiki-ingest
description: Ingest non-arXiv material into the hep-th wiki — PDFs, web pages, user-written tex/notes, results from other projects. Use when the user provides any source that is not an arXiv id.
---

# Ingest a non-arXiv source

Input: a file path, URL, or pasted content.

## 1. File the raw source (immutable)

- **PDF**: copy to `sources/pdf/<kebab-slug>.pdf`; write `sources/pdf/<kebab-slug>.md` with
  frontmatter (`title`, `authors`, `date`, `origin`) so the source is findable.
- **Web page**: WebFetch it; save the content as `sources/web/<kebab-slug>.md` with `url` and
  `fetched` date in frontmatter.
- **User tex / notes / project results**: copy (or write) into `sources/notes/<kebab-slug>.tex|md`.
  If the content exists only in conversation, write it to a file first — sources must be on disk.

## 2. Read and extract

Read the source (PDF via the Read tool page by page). For paper-like sources, extract the same
structure paper-analyst produces (TL;DR / motivation / results / methods / key equations /
concepts / people / open questions); for long sources spawn a general-purpose agent to do the
reading. For short notes/web clips, a lighter extraction is fine — don't pad.

## 3. Integrate

Same as `/wiki-ingest-arxiv` steps 3–5 (verification is not part of ingest — run
`/wiki-verify` separately if wanted):
- paper-like → `wiki/papers/<firstauthor><year>-<slug>.md`; notes/project results →
  `wiki/notes/<kebab-slug>.md`; then create/update touched topic/concept/method/result/
  question/person pages per the CLAUDE.md heuristic.
- Update `Index.md`; append `Log.md` entry (`ingest | <slug> | <title>`, or `note | ...` for
  user results).
- **Before committing**, run `scripts/check-wikilinks.sh` — it must report clean (exit 0); a
  `[[...]]` split across a newline renders as plain text in Obsidian. Join any offender it
  lists onto one line and re-run until clean.

## Long sources (textbooks, lecture notes, long reviews)

A source too big for one reading pass (rule of thumb: > ~100 pages or > 300KB of TeX / > 60
PDF pages) must NOT be fed to a single analyst agent — it will overflow its context and
produce a truncated digest. Ingest hierarchically instead:

1. **Extract structure first** (cheap, mechanical): TOC from `\chapter`/`\section` commands,
   or the PDF's outline/first pages.
2. **Create a hub page** in `wiki/papers/<slug>.md`: normal frontmatter plus a chapter table —
   each row `chapter | one-line scope | status (unread / ingested YYYY-MM-DD) | links`.
   The hub holds no digest of its own; it tracks coverage.
3. **Ingest per chapter**: each chapter is one paper-analyst unit (pass it the file/line range
   for that chapter only; run chapters in parallel when doing several). Textbook chapters
   mostly feed **concept** and **method** pages — they are the wiki's 기초지식 layer, the
   targets of other pages' `prerequisites:`.
4. **Default to lazy**: on first ingest, build only the hub + TOC and deep-read nothing (or
   just the chapters the user asked about). Fill remaining chapters on demand — when
   `/wiki-ask` needs one, or when the user says "ingest chapter N" / "ingest the whole book".
   Update the hub's status column and log each chapter as
   `ingest | <slug> ch.N | <chapter title>`.

## 4. Report

Summarize what was learned, pages created/updated, tensions found. For long sources: report
the coverage state (which chapters are ingested, which remain).
