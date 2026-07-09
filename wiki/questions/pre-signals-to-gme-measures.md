---
type: question
title: Can pre-signals be upgraded to GME measures?
aliases: [GME measures from pre-signals]
tags: [quantum-information, multipartite-entanglement, entanglement-measures]
status: open
created: 2026-07-07
updated: 2026-07-07
---

## Statement

A genuine multipartite entanglement (GME) **measure** must be a [[entanglement-signal|pre-signal]]
that is additionally **non-negative** and **LOCC-monotone** (an entanglement monotone). Signals are
ruled out ([[no-signal-is-gme-measure]]), so the target is a pre-signal with these extra properties.
Can the Möbius-vector pre-signals of the [[entanglement-signal|signal]] framework be chosen or
combined to be positive and LOCC-monotone — and, ideally, computed on **mixed** states?

## Why it matters

Signals and pre-signals detect GME but do not *quantify* it in a resource-theoretically meaningful
way. A computable GME measure would give a genuine multipartite entanglement resource theory, with
direct use for holographic states and for gapped ground states (where signals already identify the
low-energy TQFT).

## Main attempts

- The graph technology, in particular **edge-convexity** of the underlying
  [[local-unitary-invariant|multi-invariants]] (Gadde and collaborators), is proposed as the tool to
  enforce monotonicity.
- Because multi-invariants are polynomials in the state coefficients, extension to mixed states via
  the **convex roof** may be tractable — more so than for entropy-based quantities.

## Current status

**Open**, flagged as future work in [[2603.07680|Gadde 2026]]. Belongs to the topic
[[multipartite-entanglement]].
