---
type: concept
title: Non-commuting RG flows
aliases: []
tags: [rg-flow, supersymmetry, scft]
prerequisites: [renormalization-group]
created: 2026-07-04
updated: 2026-07-04
---

## Definition

The phenomenon that the IR endpoint of a sequence of superpotential deformations depends
on the *order* in which they are applied: deforming by $\mathcal{O}_1$ then
$\mathcal{O}_2$ can land on a different fixed point than $\mathcal{O}_2$ then
$\mathcal{O}_1$ — including cases where one ordering reaches an interacting SCFT and the
other does not. First observed in Barnes-Intriligator-Wecht-Wright
([hep-th/0408156](https://arxiv.org/abs/hep-th/0408156)).

## Motivation

Physically this is a statement about scales: "deform by $\mathcal{O}_1$ then
$\mathcal{O}_2$" means the coupling of $\mathcal{O}_2$ is turned on far below the scale
where $\mathcal{O}_1$ has driven the theory to its new fixed point. An operator can be
relevant at one intermediate fixed point and irrelevant at another, so the reachable IR
theories genuinely differ. Any deformation-based classification must therefore explore
orderings, not just sets, of deformations.

## Key formulas

Example from [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]: at the $H_0$ fixed point
(realized in $SU(2)$ $N_f=1$ adjoint SQCD with flips), deforming by $M_1^2$ reaches the
SCFT with $(a,c)=(\tfrac{263}{768},\tfrac{271}{768})$ only if the mass scale lies below
the $M_1\phi q^2$ coupling scale; integrating out $M_1$ first generates $(\phi q^2)^2$,
which is irrelevant at the intermediate fixed point, and the flow misses that endpoint.

## Relations

- A systematic feature of the [[4d-n1-scft-landscape|landscape program]]: nine
  non-commuting cases are tabulated in the $SU(2)$ $N_f=1$ adjoint landscape alone, and
  fixed points "missing" from one seed's landscape reappear in a larger seed's
  ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]).
- Interacts with [[flip-deformation|flip deformations]] and with operators decoupling at
  the unitarity bound, both of which change what is relevant at each step.

## Where it appears

- [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]] — catalogued; a systematic
  understanding is listed among the open problems.
