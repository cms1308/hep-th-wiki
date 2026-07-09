---
type: concept
title: Giant Graviton
aliases: ["giant gravitons", "determinant operator", "maximal giant graviton", "sub-determinant operator"]
tags: [ads-cft, giant-graviton, n4-sym, bps, d-brane]
prerequisites: ["maldacena-conjecture", "large-n-thooft-limit"]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A **giant graviton** is a heavy $\tfrac12$-BPS state of a holographic gauge theory dual to a D-brane wrapping a sphere in the internal space, rather than to a graviton mode. In 4d $\mathcal{N}=4$ SYM / IIB on $AdS_5\times S^5$ it is created by a **(sub)determinant operator** in the adjoint scalars $\Phi^I$; the maximal giant is the full determinant
$$\mathcal{D}(x,t)=\det\big(\Phi^I(x)\,t^I\big),\qquad \Delta=N,\quad \text{$SO(6)_R$ rep }[0,N,0],$$
with $t^I$ a null R-symmetry polarization ($t\cdot t=0$). Its dual is a D3-brane wrapping an $S^3\subset S^5$; a sub-determinant $\mathcal{D}_M$ ($\Delta=M<N$) is a non-maximal giant, growing with its angular momentum until it saturates at $M=N$. Because the dimension $\Delta=N$ scales with the rank, giant gravitons are genuinely non-planar objects: their determinant structure invalidates naive ribbon-graph counting and their large dimension signals nonperturbative physics.

## Motivation

Giant gravitons realize the [[stringy-exclusion-principle]] geometrically — an angular momentum cannot exceed $N$ because the wrapped brane cannot grow past the sphere — and provide heavy states whose correlators probe the "granular" (finite-$N$) structure of the gauge theory that light single-trace operators cannot see.

## Key formulas

- Maximal giant operator: $\mathcal{D}(x,t)=\det(\Phi^I(x)t^I)$, $\Delta=N$.
- Light single-trace ($\tfrac12$-BPS) probe: $\mathcal{O}_k(x,t)=\mathcal{N}_k\,\mathrm{tr}(\Phi^I(x)t^I)^k$, $\Delta=k$.
- D3-brane probe action supplying the fluctuation spectrum: $S_{\rm D3}=-\dfrac{N}{2\pi^2}\displaystyle\int_{\mathbb{R}\times S^3}\!\big(\sqrt{\det g^{\rm P.B.}}-C_4^{\rm P.B.}\big)$.

## Relations

- Dual to a D3-brane; the physical origin of the [[stringy-exclusion-principle]] in AdS$_5$/CFT$_4$.
- Its geodesic in AdS$_5$ acts as a zero-dimensional [[giant-graviton-defect|conformal defect]] for light operators — the basis of the [[giant-graviton-correlators|defect approach]].
- Distinct from the [[giant-graviton-expansion]], which sums giant-graviton branes to reconstruct the *finite-$N$ superconformal index*; here single giant gravitons are external heavy operators in a *correlator*.
- Belongs to [[ads-cft-correspondence]].

## Where it appears

- Introduced as heavy BPS D3-brane states following [[hep-th-9711200|Maldacena 1997]] (McGreevy–Schwarz–Verlinde 2000; Balasubramanian–Berkooz–Naqvi–Strassler 2001; Hashimoto–Hirano–Itzhaki 2000).
- Treated as defect-creating operators in [[2503.22987|Chen-Jiang-Zhou 2025]] and [[2602.13570|Chen-Jiang-Zhou 2026]].
