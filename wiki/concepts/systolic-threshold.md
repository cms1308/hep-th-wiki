---
type: concept
title: Systolic threshold
aliases: ["L_*", systolic length]
tags: [string-field-theory, hyperbolic-geometry, moduli-space]
prerequisites: [hyperbolic-string-vertices]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The critical geodesic length
$$L_*=2\,\mathrm{arcsinh}(1)=1.76274717\ldots$$
that separates the [[hyperbolic-string-vertices|hyperbolic string vertex]] region of moduli space
(systole $\ge L_*$) from the Feynman-diagram region (systole $<L_*$). It is the largest vertex-length
cutoff for which the collar/geometry of the hyperbolic surfaces is consistent with the geometric BV
master equation of [[closed-string-field-theory|closed string field theory]] — larger $L$ would let
the plumbing regions overlap and spoil the single-cover of moduli space.

## Motivation

A string vertex must tile a definite region of moduli space with no overcounting and no gaps once the
Feynman diagrams are added. Hyperbolic surfaces with systole below a collar-dependent bound develop
degenerating necks; $L_*=2\,\mathrm{arcsinh}(1)$ is the threshold at which the vertex region and the
propagator region match cleanly. All vertex data — mapping radii, kernels, $b$-ghost coefficients —
are evaluated at border lengths set relative to $L_*$.

## Key formulas

- $L_*=2\,\mathrm{arcsinh}(1)=1.76274717\ldots$
- Reduced length $\lambda_*=L_*/(2\pi)=0.28055\ldots$
- Conformal weight at a puncture of reduced length $\lambda_j$: $\Delta_j=(1+\lambda_j^2)/2$.
- Evaluated vertex/ghost data at threshold: $\mathrm{BG}(L_*)=1.126$; tachyon seed
  $g_T^{(0)}(L_*)\simeq8.10\times10^{-10}$.

## Relations

- The defining cutoff of [[hyperbolic-string-vertices]] within [[closed-string-field-theory]].
- The [[seam-graded-expansion|seam-graded solution]] evaluates every grade's linearized operator at
  $L_*$ — the point-evaluation that makes each grade algebraic.

## Where it appears

- Fixed by the hyperbolic-vertex construction (Moosavian–Pius; Costello–Zwiebach 2019).
- Used throughout the recursive-algebraic tachyon-vacuum solution: [[2603.29926|Kim 2026]].
