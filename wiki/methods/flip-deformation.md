---
type: method
title: Flip deformation
aliases: [flip field]
tags: [supersymmetry, scft, rg-flow, superpotential]
prerequisites: [supersymmetry-basics]
created: 2026-07-04
updated: 2026-07-04
---

Conventions: $\Delta = \tfrac32 R$ for scalar chiral primaries; relevant means $R<2$,
as in [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]].

## What it computes

A controlled way to remove a chiral operator $\mathcal{O}$ from the chiral ring and
generate a new RG flow: add a gauge-singlet chiral field $M$ ("flip field") with
superpotential
$$\delta W = M\,\mathcal{O}\,.$$
The F-term of $M$ sets $\mathcal{O}=0$ in the chiral ring; the fixed point reached is
generally different from the original. Introduced in this role by
Barnes-Intriligator-Wecht-Wright ([hep-th/0408156](https://arxiv.org/abs/hep-th/0408156))
and used systematically for SUSY-enhancing flows (Benvenuti-Giacomelli,
[1706.02225](https://arxiv.org/abs/1706.02225); Maruyoshi-Song).

## Prerequisites

The R-charges of the candidate operator at the current fixed point (from
[[a-maximization]]); the deformation $M\mathcal{O}$ is relevant iff $\mathcal{O}$ is
"super-relevant", $R(\mathcal{O}) < \tfrac43$ (so that $R(M\mathcal{O}) = R(M) +
R(\mathcal{O}) < 2$ with $R(M) = \tfrac23$ at the UV free value).

## How it works

1. **Active flip**: for $R(\mathcal{O}) < \tfrac43$, add $\delta W = M\mathcal{O}$ and
   flow. If $\mathcal{O}$ is flavor-neutral, the R-mixing is fixed without maximization
   ($\epsilon = \tfrac43 - R(\mathcal{O})$) and the central charges shift by
   $$a_{\rm IR} = a + \tfrac{3}{32}(1-R)(3R^2-6R+2)\,,\quad
   c_{\rm IR} = c + \tfrac{1}{32}(1-R)(9R^2-18R+4)\,,\quad R\equiv R(\mathcal{O})\,,$$
   so successive flavor-neutral flips trace straight lines in the $(a,c)$ plane with
   slope $s = \frac{9R^2-18R+4}{9R^2-18R+6} \in (\tfrac53,2)$.
2. **Passive flip**: when an operator's R-charge falls below the unitarity value
   $R=\tfrac23$, it decouples as a free field; flipping it implements the decoupling,
   equivalent to the Kutasov-Parnachev-Sahakyan correction in [[a-maximization]].
   With many unitarity violations at once, the operator *farthest below* the bound is
   flipped first (justified by the $a$-theorem), then the maximization is redone —
   iterated $O(N)$ times for [[dense-spectrum-scft|dense-spectrum]] theories
   ([[2510.19136|Cho-Lee-Song 2025]]).

## Regime of validity

Assumes the flipped theory flows to an interacting fixed point and that no accidental
symmetry invalidates the R-charge assignment; ordering matters — flips and mass
deformations need not commute ([[non-commuting-rg-flows]]).

## Canonical applications

- SUSY-enhancing flows from Lagrangian theories to
  [[argyres-douglas-theories|Argyres-Douglas theories]].
- The [[4d-n1-scft-landscape|landscape program]]: flips are half of the deformation
  moves generating the 7,346-entry database of
  [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]].
