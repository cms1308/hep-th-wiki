# hep-th wiki

An LLM-maintained knowledge wiki for theoretical high-energy physics (hep-th), built on
[Andrej Karpathy's LLMwiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
the human curates sources and asks questions; the LLM (Claude Code) does the summarizing,
cross-referencing, filing, and bookkeeping.

## How it works

Three layers:

1. **`sources/`** — immutable raw data: arXiv TeX sources (fetched by
   `scripts/arxiv-fetch.sh`), INSPIRE-HEP bibliographic data, PDFs, notes.
   *Excluded from the public mirror for copyright reasons — the scripts re-fetch
   everything from arXiv/INSPIRE.*
2. **`wiki/`** — the LLM-owned knowledge layer: cross-linked markdown pages typed as
   topic / concept / method / result / derivation / question / person / paper / note,
   navigable via `Index.md`, with an append-only operation log in `Log.md`.
3. **`CLAUDE.md`** — the schema: conventions and workflows the LLM follows. Notable
   design points: layered convention policy (no global unification; per-page declared
   consistency + recorded conversion dictionaries), verified derivations anchored to
   source TeX, on-demand verification of ingested pages against their source
   (`/wiki-verify`), and a bidirectional citation graph from INSPIRE data.

## Workflows (Claude Code skills, in `.claude/skills/`)

| Skill | Does |
|---|---|
| `/wiki-ingest-arxiv <id>` | fetch TeX + INSPIRE data, deep-read, integrate into the wiki |
| `/wiki-ingest <path\|url>` | same for PDFs, web pages, notes; lazy chapter-wise mode for books |
| `/wiki-ask <question>` | answer from the wiki with citations; file new synthesis back |
| `/wiki-derive <what>` | work out a derivation, verify it, record it |
| `/wiki-verify <id>` | refute-pass: check a paper's pages against its source, fix unsupported claims / altered formulas |
| `/wiki-lint` | health check: contradictions, orphans, broken links, convention hygiene |
| `/wiki-next` | ranked suggestions for what to add next |

Best viewed as an [Obsidian](https://obsidian.md) vault (wikilinks, MathJax, graph view).
