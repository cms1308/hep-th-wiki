---
type: concept
title: Flavor central charge
aliases: [k_F]
tags: [scft, anomalies, central-charges]
prerequisites: [conformal-field-theory]
created: 2026-07-03
updated: 2026-07-03
---

Conventions here follow [[2308.01717|Cho-Choi-Lee-Song 2023]].

## Definition

For a $U(1)$ non-R flavor symmetry $F$ of a 4d $\mathcal{N}=1$ SCFT, the flavor central
charge is the 't Hooft anomaly
$$k_F \;\equiv\; -3\,\mathrm{tr}\, R F F\,,$$
computable from the matter content as
$\mathrm{Tr}\,R F_i F_j = \sum_\chi (R_\chi - 1)\, q_i(\chi)\, q_j(\chi)\, |\mathbf{R}_\chi|$
(sum over chiral multiplets $\chi$ of superconformal R-charge $R_\chi$, flavor charges
$q_i$, in gauge representation $\mathbf{R}_\chi$). Equivalently it normalizes the flavor
current two-point function, $C_F = \frac{3}{4\pi^4} k_F$.

## Motivation

$k_F$ is to the flavor current what $c$ is to the stress tensor. In a holographic dual it
sets the bulk gauge coupling: $C_F = \frac{6L}{\pi^2} g^{-2}$, so ratios like $C_T/C_F$
translate into $g^2/G_N$ — exactly the combination entering extremal-black-hole
kinematics. This makes $k_F$ the denominator of every AdS/CFT
[[weak-gravity-conjecture|WGC]] bound.

## Key formulas

- [[nakayama-nomura-wgc-bound|Nakayama-Nomura bound]]:
  $\Delta^2/q^2 \le \frac{9}{40}\frac{C_T}{C_F} = \frac{12 c}{k_F}$.
- [[modified-ads-wgc-3c-2a|Modified bound]]: $\Delta^2/q^2 \le \frac{12(3c-2a)}{k_F}$.
- Several $U(1)$'s: the matrix $\mathrm{Tr}\,R F_i F_j$ is Gram-Schmidt-orthonormalized to
  $\delta_{ij}$ before applying the [[convex-hull-condition|convex hull condition]].

## Relations

- Determined by [[a-maximization]] (which fixes the superconformal R-charges entering the
  anomaly).
- Sibling of the conformal central charges $a$, $c$; all are 't Hooft anomalies of the
  superconformal R-current.

## Where it appears

- [[2308.01717|Cho-Choi-Lee-Song 2023]] — computed for every theory in the large-$N$
  classification to test the modified WGC.
