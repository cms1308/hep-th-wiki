# Log

Append-only operation log. Entry format:
`## [YYYY-MM-DD] ingest|query|lint|schema|note | identifier | title`

## [2026-07-03] schema | inspire | INSPIRE-HEP integration + citation graph
- scripts/inspire-fetch.sh (recid, citation counts, resolved references → refs.json;
  called by arxiv-fetch.sh, non-fatal) and scripts/citation-links.py (cites/cited-by
  among ingested papers)
- paper pages gain inspire:/citations: frontmatter + "Citation graph" section, maintained
  bidirectionally at ingest; wiki-next gains reference-frequency + citation-count signals
- backfilled hep-th-9711200 (recid 451647, 22288 citations, 97 refs / 70 with arXiv ids)

## [2026-07-03] schema | wiki-next | Recommendation skill added
- /wiki-next aggregates GAPs, red links (by inbound count), topic frontiers, unread book
  chapters, derivation debt → ranked concrete actions; read-only, no commit

## [2026-07-03] schema | conventions | Layered convention policy
- no global unification; page-level declared consistency (mandatory), topic-level canonical
  conventions (default), recorded conversion dictionaries on paper pages (never silent),
  physical differences (e.g. index supercharge choice) disambiguated rather than unified
- paper template + paper-analyst gain a Conventions section; ingest reconciles; lint checks
- backfilled Conventions section on papers/hep-th-9711200

## [2026-07-03] derive | d3-near-horizon-limit | D3-brane near-horizon limit → AdS5×S5
- status: verified (dimensions, source eqs \nh/\sugra verbatim, flat-space limit, symmetry)
- created: derivations/d3-near-horizon-limit
- updated: results/maldacena-conjecture, methods/brane-decoupling-limit, Index

## [2026-07-03] schema | derivations | New page type + /wiki-derive skill
- added wiki/derivations/ (type: derivation, status verified|unverified),
  templates/derivation.md, skill wiki-derive (ground in source TeX, derive, verify
  via dimensional analysis/limits/independent check, record + cross-link)
- wiki-ask now routes "how is X derived?" to wiki-derive

## [2026-07-03] schema | wiki-ingest | Long-source (book) policy added
- sources > ~100 pages: TOC-first hub page with per-chapter status, chapter-sized
  paper-analyst units (parallelizable), lazy deep-read by default (fill on demand)

## [2026-07-03] schema | wiki-ask | Gap policy added
- when neither wiki nor sources answer a question: label the gap (no fake citations),
  escalate via arXiv/web search + offer ingest, record the gap in Log + red link

## [2026-07-03] ingest | hep-th/9711200 | The Large N Limit of Superconformal Field Theories and Supergravity
- created: papers/hep-th-9711200, topics/ads-cft-correspondence, concepts/anti-de-sitter-space,
  concepts/large-n-thooft-limit, concepts/holographic-radial-coordinate,
  methods/brane-decoupling-limit, results/maldacena-conjecture,
  questions/ads-boundary-dictionary, people/juan-maldacena, people/gerard-t-hooft
- updated: Index
- red links (write next): gkp-witten, holographic-principle, d1-d5-system,
  strominger-vafa-entropy, near-horizon-limit, near-horizon-supersymmetry-enhancement,
  btz-black-hole, matrix-theory, brane-probe-action, andrew-strominger, alexander-polyakov,
  black-hole-information-paradox

## [2026-07-03] schema | initial | Vault initialized
- created: CLAUDE.md (schema), Index, Log, templates/ (8 page types),
  scripts/arxiv-fetch.sh, skills (wiki-ingest-arxiv, wiki-ingest, wiki-ask, wiki-lint),
  agent (paper-analyst)
