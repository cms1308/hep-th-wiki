# Log

Append-only operation log. Entry format:
`## [YYYY-MM-DD] ingest|query|lint|schema|note | identifier | title`

## [2026-07-03] note | null-infinity | Concept page written (top red link, 12 inbound)
- created: concepts/null-infinity (from sources/arxiv/2602.02644 §4.4–4.5, topic-canonical
  rectangular Bondi conventions)
- updated: Index

## [2026-07-03] ingest | 2602.02644 | Carrollian Physics and Holography
- created: papers/2602.02644, topics/carrollian-physics, topics/flat-space-holography,
  topics/celestial-holography, concepts/carroll-group, concepts/carrollian-geometry,
  concepts/bms-symmetry, concepts/electric-magnetic-carrollian-theories,
  concepts/carrollian-cft, concepts/carrollian-amplitude,
  methods/flat-space-limit-of-witten-diagrams, results/flat-carrollian-limit-correspondence,
  results/carrollian-celestial-equivalence, questions/intrinsic-definition-of-carrollian-cft,
  people/romain-ruzziconi
- updated: topics/ads-cft-correspondence (flat-limit era), papers/hep-th-9711200 (cited-by),
  Index
- conventions: Ruzziconi 2026 adopted as topic-canonical for carrollian-physics /
  flat-space-holography (signature, rectangular Bondi coords, k·n=-1, N=2, Δ=1 boundary
  operators)
- red links (write next): null-infinity, conformal-carrollian-algebra, celestial-amplitude,
  soft-graviton-theorems, lw-infinity-algebra, null-brown-york-stress-tensor,
  membrane-paradigm, bms-conformal-carroll-isomorphism, carrollian-abjm-correspondence,
  carrollian-quantization-obstruction, massive-states-in-carrollian-holography,
  internal-space-decompactification, andrew-strominger, marc-henneaux,
  jean-marc-levy-leblond; papers: 2406.19343 (cited 24x), 2212.12553 (19x), 2312.10138 (15x),
  2503.15607 (11x), 2504.10291 (11x), 2411.04902 (9x), 2407.11971 (8x), 2109.06708 (8x),
  2110.02319 (7x), 2202.08438, 1402.5894 (foundational)
- note: initial arXiv API fetch was rate-limited; succeeded on retry ~6 min later

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

## [2026-07-03] ingest | 2308.01717 | Supersymmetric Cardy Formula and the Weak Gravity Conjecture in AdS/CFT
- created: papers/2308.01717, results/modified-ads-wgc-3c-2a, results/nakayama-nomura-wgc-bound, results/supersymmetric-cardy-formula-4d, results/hofman-maldacena-bound, concepts/weak-gravity-conjecture, concepts/superconformal-index, concepts/flavor-central-charge, concepts/conformal-window, methods/a-maximization, methods/convex-hull-condition, questions/gravity-derivation-of-modified-wgc, questions/higher-dimensional-modularity, people/jaewon-song
- updated: topics/ads-cft-correspondence (WGC-in-AdS/CFT entry), papers/hep-th-9711200 (cited-by), Index
- note: citation-links.py missed the hep-th/9711200 citation (INSPIRE ref lacked arXiv id); verified in main.bbl and recorded manually.

## [2026-07-04] ingest | 2408.02953 | Large Landscape of 4d Superconformal Field Theories from Small Gauge Theories
- created: papers/2408.02953, topics/4d-n1-scft-landscape, methods/flip-deformation, concepts/argyres-douglas-theories, concepts/non-commuting-rg-flows, results/minimal-n1-scft, questions/n1-central-charge-bounds, questions/candidate-rank-1-cb-dimension-5-4, people/kazunobu-maruyoshi
- updated: methods/a-maximization (KPS decoupling correction), concepts/superconformal-index ((t,y) convention dictionary, reduced index, t^6 diagnostic), results/hofman-maldacena-bound (a/c record 507/419 supersedes ISS 183/158), papers/2308.01717 (cited-by, superseded a/c note, companion-paper status), papers/hep-th-9711200 (cited-by), people/jaewon-song, Index
- note: NOT the companion classification paper announced in 2308.01717 (Cho-Lee-Song, still in preparation); citation-links.py again missed a citation (2308.01717, no arXiv id in INSPIRE refs) — verified in main.tex and recorded manually.

## [2026-07-04] ingest | 2510.19136 | Large N Universality of 4d N=1 SCFTs with Simple Gauge Groups
- created: papers/2510.19136, results/large-n-universality-classes, concepts/dense-spectrum-scft, concepts/veneziano-limit, questions/holographic-duals-of-type-ii-iii
- updated: results/modified-ads-wgc-3c-2a (comprehensive validation, zero counterexamples), results/nakayama-nomura-wgc-bound (new violation catalog), questions/n1-central-charge-bounds (a/c gap, 3/5 lower bound), questions/higher-dimensional-modularity, concepts/conformal-window (per-family windows), methods/a-maximization + convex-hull-condition + flip-deformation (new canonical applications), topics/4d-n1-scft-landscape (2025 entry), topics/ads-cft-correspondence, papers/2308.01717 + 2408.02953 (companion published; cited-by), papers/hep-th-9711200 (cited-by), people/jaewon-song, Index
- note: this IS the companion classification paper announced in 2308.01717 and 2408.02953; citation-links.py resolved all three citations this time.

## [2026-07-04] schema | read-status tracking for paper pages
- updated: CLAUDE.md (frontmatter schema: `read:` field, papers only, user-owned), templates/paper, all 5 papers/* (read: false)
- note: `read: false` at ingest; user flips to YYYY-MM-DD in Obsidian when actually read. Filter unread via Obsidian search `["read":false]`.
## [2026-07-04] query | why is a-maximization only a consistency check in SQCD?
- updated: methods/a-maximization (expanded the SQCD parenthetical: traceless/baryonic symmetries cannot mix with R, anomaly freedom alone fixes R_Q)
## [2026-07-04] query | follow-up: SQCD bullet removed from a-maximization
- updated: methods/a-maximization (dropped the SQCD consistency-check bullet from Canonical applications per user — SQCD needs no maximization, so it is not an application)
## [2026-07-04] query | check 2510.19136 claim: conformal-manifold deformation at N_f=0,1 in every family
- created: notes/conformal-manifold-claim-check-2510-19136 (verified for all Type II/III families; Type I not established, SU adjoint SQCD N_f=1 is the paper's own counterexample)
- updated: papers/2510.19136 (scoped the blanket claim in item 6), Index
## [2026-07-04] note | removed conformal-manifold-claim-check-2510-19136 per user
- deleted: notes/conformal-manifold-claim-check-2510-19136; updated: Index, papers/2510.19136 (kept scoped claim, dropped note link)
## [2026-07-04] schema | verification gate before wiki writes
- updated: CLAUDE.md (Workflows — Verification gate paragraph: refute-pass on source-derived claims before commit), skills/wiki-ingest-arxiv (new step 5 Verify, renumbered 6 Bookkeep / 7 Report), skills/wiki-ingest (Integrate now references steps 3–6), skills/wiki-ask (Compound verifies sourced claims before filing)

## [2026-07-04] ingest | hep-th/0601001 | The String Landscape, Black Holes and Gravity as the Weakest Force
- created: papers/hep-th-0601001, topics/swampland-program, questions/wgc-strong-vs-weak-form, people/cumrun-vafa, people/nima-arkani-hamed
- updated: concepts/weak-gravity-conjecture (forms I/II/III, magnetic/cutoff form, p-form/axion generalization, heterotic evidence), methods/convex-hull-condition (AMNV basis-of-directions seed), results/nakayama-nomura-wgc-bound (AdS question lineage), papers/2308.01717 + papers/2510.19136 (Cited by ↔ Cites), Index
- verification ran (refute-pass vs source TeX): 10 findings fixed — dropped qualifiers (BPS "central charges only", "integral U(1) from left-movers", "heuristic" labeling, strong-form hedge), misread GW-testability claim, wrong remnant/species-problem mechanisms, decay-condition formula re-attributed to 2308.01717, Douglas added to finiteness lineage
- note: citation-links.py misses 2308.01717 → hep-th/0601001 (INSPIRE ref entry has recid 707820 but no arXiv id; script matches arXiv ids only); wired by hand

## [2026-07-05] schema | no line breaks inside wikilinks
- updated: CLAUDE.md (Naming & linking conventions — a newline inside `[[...]]` breaks Obsidian rendering; keep the whole link on one line, wrap before/after it instead)
- fixed: 16 broken-across-lines wikilinks joined and paragraphs rewrapped in concepts/argyres-douglas-theories, concepts/carrollian-amplitude, concepts/carrollian-cft, papers/2602.02644, people/jaewon-song, people/romain-ruzziconi, questions/intrinsic-definition-of-carrollian-cft, results/hofman-maldacena-bound, results/large-n-universality-classes, results/minimal-n1-scft, results/nakayama-nomura-wgc-bound, topics/carrollian-physics, topics/celestial-holography, topics/flat-space-holography

## [2026-07-06] ingest | hep-th/9501106 | Trouble For Remnants
- created: papers/hep-th-9501106, concepts/black-hole-remnant
- updated: papers/hep-th-0601001 (Historical context, Methods, Wiki links, Citation graph — replaced plain-text Susskind 1995 mentions with [[hep-th-9501106]] links; flagged that Susskind's paper never discusses symmetry, AMNV's global-symmetry tie is their own inference), concepts/weak-gravity-conjecture (Motivation section links the remnant pathology to the new page), Index
- prompted by user follow-up: /wiki-ask answer had asserted an unsourced "entropy-counting/species-finiteness" mechanism for why remnants are pathological; user asked to research the actual reference (`\cite{remn}`) and get the real argument into the wiki
- verification ran (refute-pass vs source TeX main.tex): no findings — all formulas ($N_i\sim e^{-2\pi\rho M_i}$, $N_R\sim e^{S_R-2\pi\rho M_p}$, $\rho=S_R/M_p$, $S/A\sim S_R^2M_p^2$, $S/A=1/(4G)$) and quotes confirmed verbatim; confirmed "symmetry" is never mentioned in Susskind's paper

## [2026-07-06] ingest | hep-th/9501106 | Trouble For Remnants (re-ingest)
- re-ingest requested by user (fresh deep-read after model change); sources unchanged
- created: results/susskind-uglum-low-energy-theorem, questions/black-hole-information-paradox, people/leonard-susskind (all previously red links)
- updated: papers/hep-th-9501106 (rewritten: full numbered equation chain eqs. 1-13, new "Assumptions and qualifiers" section, sixth reference Thorne-Price-MacDonald membrane paradigm added, links to the three new pages), concepts/black-hole-remnant (theorem link; wording tightened to source phrasing), Index
- verification ran (refute-pass vs source TeX + AMNV TeX): all 13 equations, equation numbering, and every quotation confirmed verbatim; 11 interpretive/sourcing findings fixed — unsourced "species problem" implication removed from theorem page, theorem status flagged as not-yet-verified-here (hep-th/9401070 not ingested), invented either/or framing on remnant Definition replaced with source wording, non-verbatim "same pathology" scare quote corrected to "same problems", "four-page" vs INSPIRE's 5 pages softened, "nucleation"/"wormhole-like"/"entanglement"/"original proposal" and contradiction-framing interpolations replaced with source language
- GAP noted: black-hole-information-paradox page lacks modern island/replica-wormhole coverage; hep-th/9401070 (Susskind-Uglum) worth ingesting to anchor the low-energy theorem

## [2026-07-06] ingest | 2601.00096 | Soft Algebras in AdS4 from Light Ray Operators in CFT3
- created: papers/2601.00096, concepts/s-algebra, concepts/light-ray-operators, concepts/einstein-cylinder, concepts/lw-infinity-algebra (healed red links from celestial-holography and flat-space-holography), results/ads4-s-algebra-from-cft3-light-transforms, questions/soft-algebras-for-gravity-in-ads4, people/andrew-strominger (healed red links)
- updated: topics/celestial-holography (2025-26 development, key concepts/results), topics/ads-cft-correspondence (2025-26 development), papers/hep-th-9711200 + papers/2602.02644 (Citation graph both directions: 2601 cites Maldacena; Ruzziconi review cites 2601), Index
- verification ran (refute-pass vs source TeX Andydecember.tex): all equation numbers and transcribed formulas confirmed character-by-character; 10 findings fixed — "nonabelian" qualifier restored on the current, nonperturbative claim narrowed to the p=1 subalgebra (tower is "potentially well-defined at the quantum level" per source), light-transform weight marked operator-specific, linearly-polarized-combination index reflection restored, SDYM "perturbatively exact" re-attributed to the paper's own phrasing, "$S^1$-worth" and "Jacobi bootstrap" coinages removed, "enables importing" hedged to source's "hopes may enable", EC3 null-Cauchy claim re-cited to 2603.26459

## [2026-07-06] ingest | 2603.26459 | Every CFT3 has an L_Lambda w(1+infinity) symmetry
- created: papers/2603.26459, concepts/lambda-deformed-w-algebra, concepts/anec-operator, results/every-cft3-has-l-lambda-w-symmetry
- updated: questions/soft-algebras-for-gravity-in-ads4 (CFT3 side established; remaining: bulk Dirichlet derivation, dS interpretation, outside-wedge), concepts/lw-infinity-algebra + concepts/s-algebra (deformation cross-links), Index
- verification ran (refute-pass vs source TeX aslightray.tex, compiled aux for eq numbers): deformed commutator, E/K/N definitions, Fourier commutators, dictionary, wedge, Casimir all confirmed exact; 10 findings fixed — "(unit AdS radius)" gloss on Lambda=-1 removed (not in source; standard 4d convention would give Lambda=-3), "physical consequences" open question re-marked as wiki's own, bulk-combination conjecture softened to source's "perhaps involving", discovery narrative put on the source's equal footing (Taylor-Zhu/Bittleston et al./Mago et al./Schwarz talk), Cartan-weight vs lowering-annihilation steps disentangled in derivation sketch, plane-model eq numbers corrected (54/55/56), "celestial circle/angle" and "Jacobi-identity bootstrap" coinages removed, Himwich-Pate neutrally cited, Mago et al. restored to the extended-results list

## [2026-07-06] ingest | 2606.08582 | Soft Algebra for N=4 SYM
- created: papers/2606.08582, results/undeformed-s-algebra-planar-n4-sym, people/luis-alday
- updated: concepts/s-algebra (planar N=4 quantum status), topics/celestial-holography (development + key results), Index; red links seeded for the N=4 amplitude stack: bds-ansatz, amplitude-wilson-loop-duality, dual-conformal-symmetry, remainder-function, wilson-loop-ope, cusp-anomalous-dimension, momentum-twistors
- verification ran (refute-pass vs source TeX softfinalA.tex + N4refs.bib): eqs 2.3/2.7/2.20/4.2/4.6-4.7/5.3/5.6, coupling and mode conventions, terminology, and all author attributions confirmed; 13 findings fixed — appendix eq numbers corrected to A.8/A.19 (A.20-21 don't exist), unclaimed "first evidence" dropped (2601/2603 are prior non-twistorial cases per the paper's own intro), leading-log relation restricted to l>=2 with the one-loop check re-assigned to log R-hat vs Brandhuber et al., R_5=0 restated as consequence of collinear universality, G_n def cited as eq 4.3, "super-ratio" de-coined, "positive powers" fixed to source's "essentially resum to (p1.p2)^c, c nonnegative", finite-coupling P_n soft-limit claim downgraded to "expected" (OPE argument is for half-collinear), BDN conjugation formula quoted with both G_n and G_{n-1} and "divergent" qualifier, Assumption 1' (dual superconformal) separated from Assumption 1, saddle-point phase factor (zbar/z)^{m/2} restored, hard-amplitude qualifier added on person page

## [2026-07-07] ingest | 2507.08588 | Symmetries and operators in TTbar deformed CFTs
- created: papers/2507.08588, topics/ttbar-deformation, concepts/{jt-bar-deformation, dressed-operator-deformed-cft, physical-operator-deformed-cft, nonlocal-conformal-symmetry-deformed-cft, tst-holography}, methods/hamiltonian-flow-deformed-cft, results/{ttbar-deformed-spectrum, deformed-cft-two-point-function}, questions/quantum-operators-deformed-cft, people/{wei-song, monica-guica}
- updated: Index (new TTbar cluster across all type headings)
- note: opens a fresh subject area (TTbar/JTbar solvable deformations); no prior wiki content. INSPIRE recid 2944958, 11 citations at ingest.

## [2026-07-07] ingest | 2511.10557 | Symmetries, operators and correlators in JTbar deformed CFTs
- created: papers/2511.10557
- updated: concepts/jt-bar-deformation and the shared dressed/physical/nonlocal-symmetry/tst pages (JTbar sections), methods/hamiltonian-flow-deformed-cft, results/deformed-cft-two-point-function (JTbar 2pt + instanton), questions/quantum-operators-deformed-cft, papers/hep-th-9711200 (Cited by += 2511.10557), Index
- note: JTbar companion to 2507.08588; cites it and Maldacena 1997. INSPIRE recid 3082760, 2 citations at ingest.

## [2026-07-07] ingest | 1903.11115 | JT gravity as a matrix integral
- created: papers/1903.11115, topics/jt-gravity, results/jt-gravity-matrix-integral-duality, results/large-genus-weil-petersson-asymptotics, concepts/schwarzian-theory, concepts/trumpet-geometry, concepts/weil-petersson-volumes, concepts/jt-spectral-curve, concepts/spectral-form-factor, concepts/minimal-string, methods/eynard-orantin-topological-recursion, methods/double-scaling-limit, questions/factorization-vs-wormholes, questions/nonperturbative-completion-jt, people/phil-saad, people/stephen-shenker, people/douglas-stanford, people/maryam-mirzakhani, people/bertrand-eynard
- updated: Index
- note: opens a new area (JT gravity / matrix models). Saad-Shenker-Stanford; INSPIRE recid 1726905, 946 citations at ingest. Citation graph empty — cites none of the currently ingested wiki papers.

## [2026-07-07] ingest | 2408.00082 | TASI Lectures on Physics for Machine Learning
- created: papers/2408.00082, topics/physics-for-machine-learning, concepts/neural-network-field-theory, concepts/neural-network-gaussian-process, concepts/neural-tangent-kernel, concepts/feature-learning, concepts/maximal-update-parameterization, concepts/universal-approximation-theorem, concepts/kolmogorov-arnold-network, results/nngp-correspondence, people/jim-halverson
- updated: Index
- note: opens a new machine-learning area (vault was previously all holography/hep-th); citation graph empty (references are ML literature, none ingested). red link: phi4-from-neural-networks.

## [2026-05-06] ingest | 2605.05336 | Wormholes and the imaginary distance bound
- created: papers/2605.05336, concepts/imaginary-distance-bound, concepts/euclidean-axion-wormhole, concepts/kontsevich-segal-witten-criterion, methods/kaluza-klein-reduction-wormholes, people/alexander-maloney
- updated: concepts/weak-gravity-conjecture, topics/swampland-program, questions/factorization-vs-wormholes, people/juan-maldacena, papers/1903.11115 (cited-by), papers/hep-th-0601001 (cited-by), Index
- note: companion to 2605.05305 (mutual citation added manually — both new). Cites 1903.11115, hep-th-0601001. red links: brian-mcpeak.

## [2026-05-06] ingest | 2605.05305 | Positivity of the gravitational path integral implies the axionic weak gravity conjecture
- created: papers/2605.05305, concepts/gravitational-path-integral-positivity, people/luca-iliesiu, people/henry-lin
- updated: concepts/weak-gravity-conjecture, topics/swampland-program, questions/factorization-vs-wormholes, papers/hep-th-0601001 (cited-by), Index
- note: companion to 2605.05336. Cites hep-th-0601001. red links: gabriele-di-ubaldo, cynthia-yan.

## [2026-07-07] ingest | 2507.11652 | Conformal Turaev-Viro Theory
- created: papers/2507.11652, topics/virasoro-tqft, concepts/conformal-turaev-viro-theory, concepts/turaev-viro-theory, concepts/chain-mail-formalism, concepts/virasoro-6j-symbol, concepts/cardy-density-of-states, concepts/virasoro-modular-s-matrix, results/ctv-equals-s-transform-of-zvir-squared, people/thomas-hartman
- updated: Index
- notes: new subgraph (3d gravity / Virasoro TQFT), no citation overlap with existing wiki papers; cardy-density-of-states cross-linked to jt-spectral-curve (shared sinh spectrum)

## [2026-07-07] ingest | hep-th/0603001 + 0705.0016 | Ryu-Takayanagi + HRT holographic entanglement entropy
- created: papers/hep-th-0603001, papers/0705.0016, topics/holographic-entanglement-entropy, results/ryu-takayanagi-formula, results/hrt-formula, concepts/entanglement-entropy, concepts/extremal-surface, concepts/bousso-bound, concepts/bekenstein-hawking-entropy, people/shinsei-ryu, people/tadashi-takayanagi, people/veronika-hubeny, people/mukund-rangamani, people/raphael-bousso
- updated: Index, topics/ads-cft-correspondence (link HEE), papers/hep-th-9711200 + 2511.10557 + 2602.02644 (citation graph both directions)
- notes: RT (static minimal surface) + HRT (covariant extremal surface); citation links: both cite Maldacena 1997, HRT cites RT, and RT cited by already-ingested 2511.10557 + 2602.02644

## [2026-07-07] ingest | 2511.00636 | AdS$_3$ Quantum Gravity and Finite $N$ Chiral Primaries
- created: papers/2511.00636, topics/ads3-cft2-correspondence, concepts/stringy-exclusion-principle, concepts/symmetric-orbifold-cft, concepts/chiral-primary-states, concepts/tensionless-string-ads3, concepts/finite-n-null-states, concepts/stokes-sectors-partition-function, concepts/ads3-z-k-orbifold-geometry, concepts/negative-modes-contour-rotation, results/ads3-giant-graviton-expansion, results/dmvv-formula, results/giant-graviton-expansion, methods/grand-canonical-residue-expansion, people/ji-hoon-lee, people/wei-li, people/jan-de-boer
- updated: Index, papers/hep-th-9711200 (cited-by), topics/ads-cft-correspondence (key concepts)

## [2026-07-07] ingest | 2603.07680 | On genuine multipartite entanglement signals
- created: papers/2603.07680, topics/multipartite-entanglement, concepts/genuine-multipartite-entanglement, concepts/local-unitary-invariant, concepts/partition-lattice, concepts/entanglement-signal, concepts/multi-entropy, methods/mobius-inversion, results/no-signal-is-gme-measure, results/q-information-odd-q-vanishing, questions/pre-signals-to-gme-measures, questions/structural-characterization-compatibility, people/abhijit-gadde
- updated: Index
- note: wiki's first quantum-information paper; no reference overlap with existing (holography) papers, so citation graph empty

## [2026-07-07] ingest | 2603.29926 | Recursive-algebraic solution of the closed string tachyon vacuum equation
- created: papers/2603.29926, topics/closed-string-field-theory, methods/seam-graded-expansion, methods/mirzakhani-topological-recursion, concepts/closed-string-tachyon-vacuum, concepts/hyperbolic-string-vertices, concepts/systolic-threshold, concepts/fvm-quadratic-integral-equation, concepts/twisted-mirzakhani-kernels, results/ghost-dilaton-condensation-tachyon-vacuum, questions/closed-string-tachyon-vacuum-convergence, people/manki-kim, people/atakan-hilmi-firat
- updated: Index, concepts/weil-petersson-volumes, methods/eynard-orantin-topological-recursion
- note: wiki's first string-field-theory area; INSPIRE citations=0 at ingest; no wiki-internal citation links (refs not yet ingested)

## [2026-07-07] ingest | 2503.22789 | Entropic Order
- created: papers/2503.22789, topics/entropic-order, concepts/transmutation-boson-mechanism, concepts/pomeranchuk-effect, concepts/entropic-topological-order, concepts/high-temperature-order-in-qft, results/heat-death-of-entanglement, results/high-temperature-entropic-superconductivity, questions/high-t-order-thermodynamic-limit, people/zohar-komargodski, people/andrew-lucas
- updated: Index

## [2026-07-07] ingest | 2512.07980 | Minimal Models of Entropic Order
- created: papers/2512.07980, concepts/arithmetic-ising-model, methods/large-flavor-expansion-entropic-order, questions/finite-k-corrections-entropic-transition
- updated: Index, papers/2503.22789 (cited-by)

## [2026-07-07] ingest | 2210.13482 | Uncovering conformal symmetry in the 3D Ising transition: State-operator correspondence from a fuzzy sphere regularization
- created: papers/2210.13482, topics/fuzzy-sphere-regularization, topics/3d-ising-cft, concepts/fuzzy-sphere, concepts/state-operator-correspondence, concepts/conformal-multiplet, concepts/virial-current, methods/lowest-landau-level-projection, methods/exact-diagonalization, methods/conformal-bootstrap, results/fuzzy-sphere-ising-spectrum, questions/emergent-conformal-symmetry-3d-ising, people/yin-chen-he, people/wei-zhu, people/alexander-polyakov, people/john-cardy, people/fdm-haldane
- updated: Index
- note: wiki's first numerical-CFT / condensed-matter-CFT cluster; no in-wiki citation links (isolated subfield so far)

## [2026-07-08] ingest | 2603.00245 | Proliferation transitions from a topological phase in 2+1 dimensions
- created: papers/2603.00245, topics/topological-phase-transitions-2plus1d, concepts/proliferation-transition, concepts/anyon-condensation, concepts/one-form-global-symmetry, concepts/abelian-hierarchy-construction, methods/gauging-one-form-symmetry, results/proliferation-transition-single-integer-p, results/p-zero-transition-implements-gauging, questions/gauging-noninvertible-one-form-symmetry-transitions, people/nathan-seiberg, people/meng-cheng
- updated: Index
- notes: wiki's first topological-order / 2+1d TQFT material. No wiki-internal citation overlap. Red links left for later: chern-simons-theory, chern-simons-matter-transition-theory, minimal-tqft-Anp, symmetry-fractionalization-enrichment, particle-vortex-duality, enrichment-incompatibility-fractional-charge.

## [2026-07-08] ingest | 2503.22987 | Giant Graviton Correlators as Defect Systems
- created: papers/2503.22987, topics/giant-graviton-correlators, concepts/giant-graviton, concepts/giant-graviton-defect, concepts/ten-dimensional-hidden-conformal-symmetry, concepts/llhh-correlator, methods/analytic-defect-bootstrap, results/giant-graviton-defect-correlators, results/giant-graviton-defect-anomalous-dimensions, questions/four-giant-graviton-correlators, people/junding-chen, people/yunfeng-jiang, people/xinan-zhou
- updated: Index, topics/ads-cft-correspondence, results/giant-graviton-expansion (cross-link the two giant-graviton threads)
- note: ingested together with its long-version companion 2602.13570 (shared page set). Wiki's first giant-graviton-correlator / defect-CFT cluster. Citation-links found no automatic wiki cross-links — INSPIRE populated arXiv ids for only 3/62 references; the companion link to 2602.13570 recorded by hand.

## [2026-07-08] ingest | 2602.13570 | Defect approach to giant graviton dynamics
- created: papers/2602.13570 (all other touched pages shared with 2503.22987, created above)
- updated: Index; paper 2503.22987 "Cited by" (companion long paper, recorded by hand from the .bbl)
- note: long version of the letter 2503.22987 (cites it as \cite{longpaper}). Adds all KK levels, parity-odd p=0 defect blocks, Mellin/flat-space limit, the complete defect double-particle anomalous-dimension spectrum, quantum-vs-classical moduli averaging, and the universal LLHH defect reduction. INSPIRE arXiv ids populated for only 10/98 references.

## [2026-07-08] ingest | 2607.02905 | Pre-Strings Lectures on Artificial Intelligence
- created: papers/2607.02905, topics/machine-learning-in-string-theory, results/nn-ft-universality-theorem, results/liouville-from-neural-networks, results/string-amplitudes-from-neural-networks, results/critical-dimension-from-mode-counting-nn-ft, concepts/parameter-space-ward-identities, concepts/topological-sectors-nn-ft, people/sergei-gukov, people/fabian-ruehle
- updated: concepts/neural-network-field-theory, topics/physics-for-machine-learning, people/jim-halverson, papers/2408.00082 (cited-by), Index

## [2026-07-08] ingest | 2211.04410 | Vertex algebra of extended operators in 4d N=2 superconformal field theories
- created: papers/2211.04410, topics/scft-voa-correspondence, concepts/schur-operators, concepts/twisted-schur-supercharges, concepts/twisted-schur-descent, concepts/extended-vertex-algebra, methods/weight-function-regularization, results/free-hypermultiplet-extended-va-opes, questions/extended-va-conformal-vertex-algebra, people/philip-argyres, people/matteo-lotito, people/mitch-weaver
- updated: Index
- note: wiki's first 4d N=2 SCFT/VOA material; no citation-graph overlap with ingested papers yet. INSPIRE recid 2178133, citations 6.

## [2026-07-08] ingest | 2607.05496 | 6d Supergravity Blocks
- created: papers/2607.05496, topics/6d-supergravity-swampland, concepts/supergravity-block, concepts/non-higgsable-gravity-block, concepts/h-string, concepts/non-higgsable-cluster, concepts/tensor-charge-lattice, methods/green-schwarz-sagnotti-mechanism, results/classification-non-higgsable-gravity-blocks, questions/uv-completion-frozen-nhc-supergravities, people/hee-cheol-kim, people/yuta-hamada
- updated: topics/swampland-program, people/cumrun-vafa, Index
- note: no INSPIRE record at ingest (citation graph empty)

## [2026-07-08] query | i.i.d. abbreviation expansion
- updated: concepts/neural-network-gaussian-process

## [2026-07-08] ingest | 2509.16737 | Unravelling the Holomorphic Twist II: Anomalies and Extended Supersymmetry
- created: papers/2509.16737, topics/holomorphic-twist, concepts/semi-chiral-superfield, concepts/holomorphic-lambda-bracket, concepts/two-virasoro-algebra, concepts/higher-kac-moody-algebra, concepts/higher-super-virasoro-algebra, concepts/schur-superfield, methods/superconformal-deformation-to-voa, methods/holomorphic-a-maximization, results/ac-anomalies-as-central-extensions, people/brian-williams, people/ingmar-saberi, questions/intrinsic-holomorphic-a-maximization, questions/supergeometric-3-cocycles-svir
- updated: topics/scft-voa-correspondence, papers/2408.02953 (cited-by), Index

## [2026-07-08] query | why deforming holomorphic twist changes the differential
- updated: methods/superconformal-deformation-to-voa (why differential = {S,-}, so deform → new differential)

## [2026-07-09] schema | paper pages: add arxiv_url frontmatter
- updated: all 32 wiki/papers/*.md (arxiv_url clickable link), templates/paper.md, CLAUDE.md schema, wiki-ingest-arxiv skill
- fixed: truncated arxiv id in 2512.07980, 2603.07680 (trailing zero dropped by YAML)
