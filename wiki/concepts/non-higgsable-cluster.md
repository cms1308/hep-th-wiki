---
type: concept
title: Non-Higgsable cluster
aliases: [non-Higgsable cluster, NHC, non-Higgsable clusters]
tags: [6d-supergravity, f-theory, non-higgsable-cluster, string-landscape]
prerequisites: []
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A **non-Higgsable cluster (NHC)** is a minimal configuration of intersecting curves in the
base of an F-theory compactification that necessarily carries a nontrivial gauge algebra
with *no charged matter available to Higgs it away* — the gauge symmetry is rigid. The
complete list on a rational base was given by Morrison-Taylor (2012, `Morrison:2012np`).

For a single curve of self-intersection $-n$ the minimal (un-Higgsable) gauge algebra is:

| self-intersection | algebra |
|---|---|
| $-3$ | $\mathfrak{su}_3$ |
| $-4$ | $\mathfrak{so}_8$ |
| $-5$ | $\mathfrak{f}_4$ |
| $-6$ | $\mathfrak{e}_6$ |
| $-7$ | $\mathfrak{e}_7$ (with a half-hyper) |
| $-8$ | $\mathfrak{e}_7$ |
| $-12$ | $\mathfrak{e}_8$ |

plus a small number of two- and three-curve clusters (e.g. $\overset{\mathfrak{su}_2}{2}\,\overset{\mathfrak{so}_7}{3}\,\overset{\mathfrak{su}_2}{2}$-type chains).
Curves of self-intersection $-1$ or $-2$ carry no gauge algebra on their own.

## Motivation

NHCs are the rigid "skeleton" of the 6d $(1,0)$ landscape: on any tensor base some curves
are forced to carry these minimal algebras. In the block program of
[[2607.05496|Hamada-Jeon-Kim 2026]], a [[supergravity-block]] whose tensors carry *only*
NHC algebras (no further Higgsable enhancement) is a
[[non-higgsable-gravity-block]] — the finite, fully enumerable subclass classified first.

## Key formulas

- Un-Higgsable rank grows with $|{-n}|$: from $\mathfrak{su}_3$ at $-3$ up to
  $\mathfrak{e}_8$ at $-12$.
- **Frozen-singularity** NHCs (Bhardwaj et al. 2019) extend the list in the presence of
  frozen singularities, e.g.
  $\overset{\mathfrak{su}_8}{\hat 1}$,
  $\overset{\mathfrak{su}_8}{2}\,\overset{\mathfrak{su}_{16}}{\hat 1}$,
  $\overset{\mathfrak{su}_8}{2}\!=\!\overset{\mathfrak{so}_{16}}{4}$; the middle cluster
  ($\mathfrak{su}_{16}$ on $\hat 1$) cannot embed in any supergravity.

## Relations

- Building blocks of the [[non-higgsable-gravity-block]] classification.
- Live on the tensor base whose intersection form is the
  [[tensor-charge-lattice|tensor charge lattice]].
- Gauge algebras constrained by the [[green-schwarz-sagnotti-mechanism]] anomaly conditions.

## Where it appears

- Morrison-Taylor 2012 (`Morrison:2012np`) — original classification (not yet ingested).
- [[2607.05496|Hamada-Jeon-Kim 2026]] — assembles non-Higgsable gravity blocks from the NHC
  catalogue, including frozen-singularity variants.
