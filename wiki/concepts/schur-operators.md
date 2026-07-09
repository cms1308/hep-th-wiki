---
type: concept
title: Schur operators
aliases: [Schur sector, Schur operator]
tags: [n2-scft, protected-operators, superconformal, vertex-operator-algebra]
prerequisites: [superconformal-index]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

**Schur operators** are the local BPS operators of a 4d $\mathcal N=2$ SCFT that survive in the
cohomology of a nilpotent supercharge and organize into a 2d chiral algebra. After a
**twist-translation** — dressing ordinary translation along a fixed spatial plane with an
$SU(2)_R$ rotation — a Schur operator is annihilated by the [[twisted-schur-supercharges]]
$\mathbb T_\pm$, and its correlators become meromorphic functions of a single complex plane
coordinate $z$. The resulting algebra of cohomology classes is the
[[scft-voa-correspondence|vertex operator algebra]] (VOA) of the SCFT.

They are named for the **Schur limit** of the [[superconformal-index]], which counts exactly
these operators: a Schur operator saturates $E - (j_1 + j_2) - 2R = 0$ and
$j_2 - j_1 + \bar j\text{-type constraints}$, leaving a half-BPS-like locus whose index is a
character of the chiral algebra.

## Motivation

The Schur sector is the analytically controllable window into a 4d $\mathcal N=2$ SCFT: its OPE
coefficients, central charges, and flavor levels map to 2d chiral-algebra data
($c_{2d} = -12\,c_{4d}$, $k_{2d} = -\tfrac12 k_{4d}$) that can be computed even for strongly
coupled, non-Lagrangian theories. It is the local half of the SCFT/VOA correspondence; extending
it to nonlocal operators is what [[twisted-schur-descent]] does.

## Key formulas

- The protected supercharges (source conventions):
  $$\mathbb T_+ \doteq Q^1_{\ 2} + \tilde S^{2\dot2},\qquad
    \mathbb T_- \doteq S_1^{\ 2} - \tilde Q_{2\dot2}.$$
- Chiral weight $h_{\mathcal O} \in \mathbb N/2$; in the free hypermultiplet the scalar $q$ has
  $h_q = 1/2$ (a symplectic boson) and the Virasoro operator has $h_T = 2$.
- Correlators of twist-translated Schur operators depend only holomorphically on $z$ — the
  statement that they form a VOA.

## Relations

- Live in the cohomology of the [[twisted-schur-supercharges]].
- The local generators of the [[scft-voa-correspondence|SCFT/VOA correspondence]].
- Extended in [[twisted-schur-descent]] to line/surface/wall operators, enlarging the VOA to an
  [[extended-vertex-algebra]].
- Counted by the Schur limit of the [[superconformal-index]].

## Where it appears

- [[2211.04410|Argyres-Lotito-Weaver 2022]] — starting point for the descent construction of
  extended operators; the free-hypermultiplet Schur operators $q_I$ and $T$ generate the worked
  example ([[free-hypermultiplet-extended-va-opes]]).
