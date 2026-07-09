---
type: concept
title: Twisted Schur supercharges
aliases: [twisted Schur supercharge, T-pm supercharges, twisted-translated supercharge]
tags: [n2-scft, supercharge, cohomology, superconformal]
prerequisites: [schur-operators]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

The **twisted Schur supercharges** are a pair of nilpotent supercharges $\mathbb T_\pm$ of a 4d
$\mathcal N=2$ superconformal algebra whose cohomology defines the protected
[[schur-operators|Schur sector]] and, through it, the
[[scft-voa-correspondence|SCFT/VOA correspondence]]. In the conventions of
[[2211.04410|Argyres-Lotito-Weaver 2022]],
$$\mathbb T_+ \doteq Q^1_{\ 2} + \tilde S^{2\dot2},\qquad
  \mathbb T_- \doteq S_1^{\ 2} - \tilde Q_{2\dot2},$$
each a sum of a Poincaré supercharge and a conformal supercharge. They coincide with the
$\mathbb Q_1,\mathbb Q_2$ of Beem–Lemos–Liendo–Peelaers–Rastelli–van Rees (2015) and are the
$\zeta = 1$ point of a one-parameter family (Lemos 2020). Each is nilpotent, $\mathbb T_\pm^2 = 0$.

"Twisted" refers to the fact that these are the combinations left unbroken once ordinary
translation in the VOA plane is dressed with an $SU(2)_R$ rotation, so that operators can be
moved around the plane while staying in the cohomology.

## Motivation

Passing to $\mathbb T_\pm$-cohomology is what turns a subset of 4d $\mathcal N=2$ correlators into
holomorphic, VOA-like data. Working with *both* $\mathbb T_+$ and $\mathbb T_-$ (rather than one)
is what pins operators to genuine meromorphy: a class must be closed with respect to both. For
extended operators this double closedness is nontrivial and is the crux of
[[twisted-schur-descent]].

## Key formulas

- Nilpotency: $\mathbb T_\pm^2 = 0$.
- Anticommutator gives the central element: $\mathbb T_\pm\circ\mathbb T_\mp = \mathcal Z$, with
  $\mathcal Z\circ N_\pm = \pm N_\pm$ on the descent generators $N_\pm$. Here $\mathcal Z$ is the
  **negative** of the $\mathcal Z$ of Beem et al. (2015)/Lemos (2020).
- R-charge assignment: $r(\mathbb T_\pm) = \mp 1$ (with $r(Q) = -1$ in the
  Córdova–Dumitrescu–Intriligator 2016 normalization).

## Relations

- Cohomology of $\mathbb T_\pm$ contains the local [[schur-operators]] and, after
  [[twisted-schur-descent]], the extended operators of the [[extended-vertex-algebra]].
- Underlies the [[scft-voa-correspondence]].

## Where it appears

- [[2211.04410|Argyres-Lotito-Weaver 2022]] — the double $\mathbb T_\pm$-closedness of descent
  operators (from the superconformal algebra, not unitarity) is what enlarges the VOA.
