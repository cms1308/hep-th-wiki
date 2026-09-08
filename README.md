# hep-th wiki

An LLM-maintained knowledge wiki for theoretical high-energy physics (hep-th), built on
[Andrej Karpathy's LLMwiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
the human curates sources and asks questions; the LLM (Claude Code or OpenAI Codex) does the
summarizing, cross-referencing, filing, and bookkeeping.

## How it works

Three layers:

1. **`sources/`** — immutable raw data: arXiv TeX sources (fetched by
   `scripts/arxiv-fetch.sh`), INSPIRE-HEP bibliographic data, PDFs, textbooks, notes.
   *Excluded from the public mirror for copyright reasons — the scripts re-fetch
   everything from arXiv/INSPIRE.*
2. **`wiki/`** — the LLM-owned knowledge layer: cross-linked markdown pages typed as
   topic / concept / method / result / derivation / lecture / question / qa / person / paper / note,
   navigable via `Index.md`, with an append-only operation log in `Log.md`.
3. **`CLAUDE.md` / `AGENTS.md`** — the schema: conventions and workflows the LLM follows
   (same content, one file per agent CLI — see below). Notable design points: layered
   convention policy (no global unification; per-page declared consistency + recorded
   conversion dictionaries), verified derivations anchored to source TeX, on-demand
   verification of ingested pages against their source (`/wiki-verify`), subject-scoped
   lecture notes merged from textbooks, and a bidirectional citation graph from INSPIRE data.

## Works with Claude Code and Codex

The same vault drives either CLI; the only difference is which files each one reads:

| | Claude Code | OpenAI Codex |
|---|---|---|
| schema | `CLAUDE.md` | `AGENTS.md` |
| skills | `.claude/skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` |
| `paper-analyst` agent | `.claude/agents/paper-analyst.md` | `.codex/agents/paper-analyst.toml` |

The shared definitions are maintained in `harness/schema.md`, `harness/skills/`, and
`harness/paper-analyst.md`. Internal helper `python3 scripts/sync-harness.py` generates both
front-ends; `--check` detects drift. Edit the shared definitions, then regenerate and commit
both together. These are maintenance helpers, not additional user-facing wiki skills.
Claude Code invokes `/wiki-ask`, Codex `$wiki-ask` or implicit selection. Codex requires
sub-agents enabled for paper analysis during ingest.

Main results and key equations retain source locators, assumptions, certainty, and convention
conversions in an Evidence table. On-demand `wiki-verify` saves scoped review records under
private `verification/`; `wiki-lint` reports whether their page/source hashes still match.
Review freshness is separate from physical proof status, and ingest still needs no refute-pass.

## Workflows (skills)

| Skill | Does |
|---|---|
| `wiki-ingest-arxiv <id>` | fetch TeX + INSPIRE data, deep-read, integrate into the wiki |
| `wiki-ingest <path\|url>` | same for PDFs, web pages, notes; lazy chapter-wise mode for books, feeding lecture notes |
| `wiki-ask <question>` | answer from the wiki with citations; file new synthesis back |
| `wiki-derive <what>` | work out a derivation, verify it, record it |
| `wiki-verify <id>` | refute-pass: check a paper's pages against its source, fix unsupported claims / altered formulas |
| `wiki-lint` | health check: contradictions, orphans, broken links, convention hygiene |
| `wiki-next` | ranked suggestions for what to add next |

Best viewed as an [Obsidian](https://obsidian.md) vault (wikilinks, MathJax, graph view).
