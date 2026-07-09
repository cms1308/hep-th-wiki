---
type: result
title: Giant-Graviton Expansion (AdS$_5$/CFT$_4$)
aliases: ["giant graviton expansion", "GGE", "brane expansion of the index"]
tags: [ads-cft, giant-graviton-expansion, superconformal-index, holography]
status: conjectured
created: 2026-07-07
updated: 2026-07-08
---

## Statement

The giant-graviton expansion expresses the finite-$N$ superconformal index (or BPS partition function) of a holographic gauge theory as the large-$N$ (KK/graviton) index times a sum over contributions of giant-graviton branes wrapping cycles in the internal space:
$$\mathcal{I}_N=\mathcal{I}_\infty\times\sum_{m\ge0}(\text{contribution of }m\text{ giant gravitons}),$$
with the $m$-brane terms weighted by $x^{mN}$-type factors that encode the finite-$N$ trace relations. In $\mathcal{N}=4$ SYM / IIB on $\mathrm{AdS}_5\times\mathrm{S}^5$ the branes are giant gravitons wrapping $\mathrm{S}^3\subset\mathrm{S}^5$; their inclusion truncates the infinite KK spectrum to the exact finite-$N$ answer.

## Derivation sketch

The finite-$N$ index is extracted from a grand-canonical generating function by a contour integral in a $\mathrm{U}(1)$ (rank/flux) fugacity. Rotating the contour past the poles picks up giant-graviton saddles; the negative modes of the wrapped branes force a contour rotation that produces **alternating signs**, and the resulting series reorganizes $\mathcal{I}_\infty$ into $\mathcal{I}_N$. The brane contributions encode the trace relations that make only finitely many multi-graviton states independent at finite $N$.

## Assumptions

- Holographic gauge theory with a giant-graviton (D-brane) sector in the bulk dual.
- Convergence / Borel-type control of the brane sum in the relevant fugacity domain.

## Status

Conjectured and checked in many cases (Imamura; Gaiotto–Lee 2021; and follow-ups, including the negative-mode contour-rotation derivation by [[ji-hoon-lee|Lee]]). Not proven in general.

## Implications

- The direct template for the [[ads3-giant-graviton-expansion]]: [[2511.00636|Lee-Li 2025]] transplants the "grand-canonical residue → brane saddle with alternating sign" logic to AdS$_3$/CFT$_2$, with $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ orbifold geometries playing the role of giant gravitons and the [[finite-n-null-states]] playing the role of trace relations.
- Realizes the truncation of a bulk BPS spectrum — the higher-dimensional cousin of the [[stringy-exclusion-principle]] — as cancellations among brane saddles.

## Related

A distinct use of the same objects: here [[giant-graviton|giant gravitons]] are *summed* to reconstruct the finite-$N$ index, whereas in the [[giant-graviton-correlators|defect approach to giant graviton correlators]] individual giant gravitons are *external heavy operators* and their pair is traded for a [[giant-graviton-defect|conformal defect]] ([[2503.22987|Chen-Jiang-Zhou 2025]], [[2602.13570|Chen-Jiang-Zhou 2026]]).
