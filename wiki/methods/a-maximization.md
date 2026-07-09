---
type: method
title: a-maximization
aliases: []
tags: [supersymmetry, scft, anomalies, rg-flow]
prerequisites: [conformal-field-theory, supersymmetry-basics]
created: 2026-07-03
updated: 2026-07-04
---

## What it computes

The exact superconformal $U(1)_R$ symmetry of a 4d $\mathcal{N}=1$ SCFT — and with it the
central charges $a$, $c$ and flavor central charges $k_F$ — from the anomalies of the UV
description (Intriligator-Wecht, [hep-th/0304128](https://arxiv.org/abs/hep-th/0304128)).

## Prerequisites

The UV gauge theory description: gauge group, chiral multiplet content, superpotential;
the set of $U(1)$ symmetries that can mix with $R$.

## How it works

1. Write the trial R-symmetry $R_t = R_0 + \sum_I s_I F_I$, a reference R-charge mixed
   with all non-R $U(1)$ flavor symmetries.
2. Impose anomaly-freedom with the gauge group, $\mathrm{Tr}\, R_t\, G G = 0$ (and
   consistency with the superpotential, each term having $R=2$).
3. Maximize the trial central charge
   $$a(R_t) = \frac{3}{32}\left(3\,\mathrm{Tr} R_t^3 - \mathrm{Tr} R_t\right)$$
   over the mixing parameters $s_I$. The superconformal R-symmetry is the local maximum.
4. Evaluate at the maximum:
   $a = \frac{3}{32}(3\,\mathrm{Tr}R^3 - \mathrm{Tr}R)$,
   $c = \frac{1}{32}(9\,\mathrm{Tr}R^3 - 5\,\mathrm{Tr}R)$, and
   $k_F = -3\,\mathrm{Tr}\,RFF$ for each remaining flavor symmetry
   ([[flavor-central-charge]]).

When an operator's R-charge falls below the unitarity value $R = \tfrac23$, it decouples
as a free field and the maximization must be corrected
(Kutasov-Parnachev-Sahakyan, [hep-th/0308071](https://arxiv.org/abs/hep-th/0308071)):
$$a_{\text{new}} = a_{\text{old}} + \frac{3}{32}\left(\frac{2}{9}
- \big(3(R(\mathcal{O}_d)-1)^3 - (R(\mathcal{O}_d)-1)\big)\right),$$
equivalent to flipping the decoupled operator $\mathcal{O}_d$
([[flip-deformation]]).

## Regime of validity

Assumes the theory flows to an interacting SCFT and that the R-symmetry visible in the UV
is the superconformal one (no accidental IR symmetries; operators hitting the unitarity
bound must be handled by the decoupling correction above). Undetected accidental
symmetries are the standing caveat of every large-scale application.

## Canonical applications

- [[2308.01717|Cho-Choi-Lee-Song 2023]] — applied to every asymptotically free
  superconformal gauge theory with a large-$N$ limit and no superpotential, to compute the
  central charges entering the [[modified-ads-wgc-3c-2a|modified WGC bound]].
- [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]] — the computational engine of the
  [[4d-n1-scft-landscape|landscape program]], re-run at every step of every deformation
  chain (deformations change which operators are relevant, so charges must be
  recomputed each time).
- [[2510.19136|Cho-Lee-Song 2025]] — solved analytically at large $N$ (with a Lagrange
  multiplier for the anomaly constraint): the leading solution depends on the matter
  only through $\dim(\mathbf{R})/T(\mathbf{R})$, which is the origin of the
  [[large-n-universality-classes|Type I/II/III universality]].
