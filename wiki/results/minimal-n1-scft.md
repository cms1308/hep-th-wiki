---
type: result
title: Minimal-known 4d N=1 SCFT and its Lagrangians
aliases: [minimal N=1 SCFT]
tags: [scft, central-charges, argyres-douglas, supersymmetry]
status: established
created: 2026-07-04
updated: 2026-07-04
---

Conventions: $a = \tfrac{3}{32}(3\mathrm{Tr}R^3-\mathrm{Tr}R)$,
$c = \tfrac{1}{32}(9\mathrm{Tr}R^3-5\mathrm{Tr}R)$; reduced index
$\mathcal{I}_{\rm red} = (1-t^3y)(1-t^3/y)(\mathcal{I}-1)$, as in
[[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]].

## Statement

The interacting 4d $\mathcal{N}=1$ SCFT with the smallest known central charges,
$$ (a, c) = \left(\frac{633}{2000},\, \frac{683}{2000}\right) \simeq (0.3165,\ 0.3415)\,,$$
is the $\mathcal{N}=1$ deformation of the $(A_1,A_4)$
[[argyres-douglas-theories|Argyres-Douglas theory]] by its dimension-$\tfrac{10}{7}$
Coulomb branch operator (identified by Xie-Yan,
[2109.04090](https://arxiv.org/abs/2109.04090)).
[[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]] give it a Lagrangian: the fixed point of
$SU(2)$ $N_f=2$ adjoint SQCD (adjoint $\phi$, doublets $q_i, \tilde q_i$, flip fields
$M_i$, $X_1$) with
$$W = M_1 q_1 q_2 + M_2 q_1\tilde q_1 + \phi q_1 \tilde q_2 + M_2 \phi q_2^2
+ M_1 M_2 + \phi\tilde q_1^2 + X_1 \mathrm{Tr}\,\phi^2\,,$$
plus a second dual description via $Sp(2)$ $N_f=1$ adjoint SQCD. The matching reduced
index is
$\mathcal{I}_{\rm red} = t^{2.4} + t^{3.6}(1-\chi_{1/2}(y)) + t^{4.8} + t^{7.2} + O(t^9)$.

## Derivation sketch

Found by exhaustive deformation search in the [[4d-n1-scft-landscape|landscape program]]:
[[a-maximization]] along each deformation chain determines $(a,c)$; the
$(a,c)$ values and superconformal indices of the $SU(2)$ and $Sp(2)$ realizations agree
with each other and with the deformed-$(A_1,A_4)$ prediction.

## Assumptions

No accidental symmetry spoiling the R-charge assignment (the standing caveat of the
landscape program); "minimal known" — smaller theories are not excluded.

## Status

Established as the minimal *known* interacting $\mathcal{N}=1$ SCFT (it beats the
deformed minimal-AD value $(\tfrac{263}{768},\tfrac{271}{768})$); whether it is *the*
minimal $\mathcal{N}=1$ SCFT is open ([[n1-central-charge-bounds]]).

## Implications

- A non-Lagrangian-descended theory of near-minimal size now has two dual Lagrangians —
  its chiral ring and index become computable ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]
  list the chiral-ring study as future work).
- Benchmark for conjectured lower bounds on $\mathcal{N}=1$ central charges
  ([[n1-central-charge-bounds]]): compare the $\mathcal{N}=2$ bound $c \ge \tfrac{11}{30}$,
  saturated by $H_0$.
