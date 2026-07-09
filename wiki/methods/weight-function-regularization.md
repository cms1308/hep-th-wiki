---
type: method
title: Weight-function regularization
aliases: [weight function regulator, descent regularization]
tags: [n2-scft, regularization, extended-operators, cohomology]
prerequisites: [twisted-schur-descent]
created: 2026-07-08
updated: 2026-07-08
---

## What it computes

A regulator that makes the divergent world-volume integrals of [[twisted-schur-descent]]
absolutely convergent **without breaking the $\mathbb T_\pm$ Ward identities** — so that the
regularized descent operators remain genuine cohomology classes and their correlators are
well-defined meromorphic functions on the [[extended-vertex-algebra|VOA plane]].

## Prerequisites

- [[twisted-schur-descent]] and the descent operators $\mathbf D^X[\mathcal E]$.
- The [[twisted-schur-supercharges]] $\mathbb T_\pm$ and the notion of $\mathbb T$-closedness.

## How it works

Descent correlators generically diverge — from parallel-line kinematics or from world volumes
that intersect at infinity. Insert a **weight function** $F(\delta,\alpha)$ into the descent
integral:
$$\mathbf D^X[F;\mathcal E] = \lim_{\delta\to0^+}\int d\alpha\; F(\delta,\alpha)\;
  \xi\circ e^{\alpha X}\circ\mathcal E,$$
with $F$ required to satisfy a short list of properties (i)–(iv): it must approach $1$ as
$\delta\to0^+$, decay fast enough in $\alpha$ to make the integral absolutely convergent, and be
compatible with the $\mathbb T_\pm$ action so that Ward identities survive the limit. Explicit
choices used in the paper are
$$F_M = (1 + i\delta\alpha)^{-M},\qquad F_\infty = e^{-\delta\alpha^2}.$$
The "hatted" surface/wall operators need stronger fall-off (e.g. $N_R > 1 + \tilde\jmath$,
$N_+ > 2$) than the unhatted ones. Light-cone singularities are separately handled with a causal
$i\epsilon$ prescription $t_{12}\to(1+i\epsilon)t_{12}$, and the divergent
$\langle\mathbf S\mathbf S\rangle$ is computed by Euclidean ($S^4$) continuation.

## Regime of validity

Established for the descent operators of a 4d $\mathcal N=2$ SCFT in $\mathbb T_\pm$-cohomology;
demonstrated in detail for the free hypermultiplet. **Regulator independence** — whether the
resulting cohomology classes are the same for any admissible $F$ — is conjectured with
preliminary evidence but **not proven**; this is the open point tracked at
[[descent-regulator-independence]].

## Canonical applications

- [[free-hypermultiplet-extended-va-opes]] — the $\mathcal O$–$\mathbf L^\pm$–$\mathbf S$ OPEs,
  which are finite only after this regularization.
- Introduced in [[2211.04410|Argyres-Lotito-Weaver 2022]].
