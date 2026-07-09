---
type: result
title: No signal can be a GME measure
aliases: [signal no-go, no-go for GME measures]
tags: [quantum-information, multipartite-entanglement, entanglement-measures]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

No [[entanglement-signal|signal]] can serve as a genuine multipartite entanglement (GME)
**measure**. A GME measure must be an entanglement monotone: non-negative and non-increasing (on
average) under local operations and classical communication (LOCC). For a signal — an LU-invariant
that vanishes exactly on [[genuine-multipartite-entanglement|layerwise-separable]] states — these
two requirements are mutually incompatible.

## Derivation sketch

The obstruction is exhibited by a single local operation. One constructs a trace-preserving local
(Kraus) operation that maps a **layerwise-separable** state — on which any signal vanishes — to a
**non-layerwise-separable**, GHZ-type state, on which a signal is nonzero (indeed one can produce
two GHZ-equivalent outputs). LOCC monotonicity would demand the average output value not exceed the
input value $0$; positivity on the GME output demands a strictly positive value. The two cannot both
hold, so a signal cannot be a monotone. (Full construction: Appendix of the source.)

## Assumptions

- Pure $q$-partite states; the signal is a genuine signal (vanishes on all layerwise-separable
  states), not merely a pre-signal.
- "GME measure" means a non-negative, LOCC-monotone-on-average entanglement monotone.

## Status

**Proven** in [[2603.07680|Gadde 2026]] (Theorem 1), by explicit counterexample operation.

## Implications

- A GME measure does **not** need to be a signal; it only needs to be a **pre-signal** (vanishing on
  separable states) that is additionally positive and LOCC-monotone. In this precise sense
  [[entanglement-signal|pre-signals]] are the more natural resource-theoretic objects than signals.
- Whether positive, LOCC-monotone pre-signals — hence actual GME measures, ideally computable on
  mixed states — can be built from this framework is left [[pre-signals-to-gme-measures|open]].
