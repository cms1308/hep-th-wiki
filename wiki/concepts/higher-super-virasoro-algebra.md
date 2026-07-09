---
type: concept
title: Higher super-Virasoro algebra svir(2|N-1)
aliases: [svir(2|1), svir(2|N-1), super 2-Virasoro, higher super-Virasoro]
tags: [holomorphic-twist, extended-supersymmetry, higher-symmetry, superalgebra, a-equals-c]
prerequisites: [holomorphic-twist, two-virasoro-algebra]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

For a 4d theory with **extended** supersymmetry, the additional supercurrents enlarge the
[[two-virasoro-algebra|2-Virasoro algebra]] into a super-analogue
$$\mathfrak{svir}(2|\mathcal N-1),$$
realized geometrically as (derived) holomorphic **super** vector fields on the punctured super-space
$\mathbb C^{2|\mathcal N-1}\setminus\{0\}$ — concretely on the total space
$\mathrm{Tot}\big(\Pi K^{1/3}\otimes\mathbb C^{\mathcal N-1}\to\mathbb C^2\setminus\{0\}\big)$
(divergence-free for $\mathcal N=4$). The underlying (non-extended) algebra is the
$\bar{\mathbf Q}$-cohomology of the 4d superconformal algebra: $\mathfrak{sl}(3|\mathcal N-1)$
(and $\mathfrak{psl}(3|3)$ for $\mathcal N=4$).

For $\mathcal N=2$ the twisted stress-tensor multiplet contributes the semi-chiral superfields
$(\mathbf S_i,\mathbf R,\mathbf G_i,\widetilde{\mathbf G})$, whose brackets generate
$\mathfrak{svir}(2|1)_{a,c}$.

## Motivation

The holomorphic twist only needs $\mathcal N=1$, but when the parent theory has more
supersymmetry the twist "remembers" it as extra semi-chiral currents and a larger symmetry
algebra. Making that algebra explicit both organizes the twisted OPE and — through the
uniqueness of its central extension — reproduces standard superconformal facts from a purely
algebraic input.

## Key formulas

- $\mathcal N=2$ geometric realization (derived super vector fields):
  $$\mathbf S_i\rightsquigarrow-\omega\partial_i-\tfrac13(\partial_i\omega)\theta\partial_\theta,\quad
  \mathbf G_i\rightsquigarrow\omega\theta\partial_i,\quad
  \widetilde{\mathbf G}\rightsquigarrow\omega\partial_\theta,\quad
  \mathbf R\rightsquigarrow\omega\theta\partial_\theta.$$
- **$a=c$ for $\mathcal N\geq3$:** the space of relevant 3-cocycles is one-dimensional
  (Fuks 1986), so the two independent central charges collapse to a single one, forcing $a=c$
  — recovering the classic result (Sohnius; Aharony–Evtikhiev 2015) algebraically.
- For $\mathcal N=2$ the space of central extensions is **two**-dimensional, corresponding to the
  degree-four Chern-class combinations $(c_1^2,c_2)$ (pimenov).

## Relations

- Extended-SUSY generalization of [[two-virasoro-algebra]]; the extra generator
  $\widetilde{\mathbf G}$ is what implements the
  [[superconformal-deformation-to-voa|superconformal deformation]] to the VOA (deforming by $\int z^2\widetilde{\mathbf G}$).
- Explicit supergeometric representatives of its 3-cocycles are only partly known —
  [[supergeometric-3-cocycles-svir]].

## Where it appears

- Constructed for $\mathcal N=2,3,4$ in ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]]; the
  non-extended holomorphic superconformal symmetry appears in Saberi–Williams 2019.
