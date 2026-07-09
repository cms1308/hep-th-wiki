---
type: result
title: Defect Double-Particle Anomalous Dimensions of Giant Gravitons
aliases: ["giant graviton defect anomalous dimensions", "defect double-particle spectrum", "defect-channel anomalous dimensions"]
tags: [ads-cft, giant-graviton, defect-cft, anomalous-dimensions, n4-sym]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

Unmixing the degenerate defect-channel double-particle operators $\widehat{[\mathcal{O}_p]}_{n,s}$ that appear in the [[giant-graviton-defect-correlators|giant graviton defect correlators]] yields their complete leading-order (tree-level) anomalous dimensions in closed form:
$$\widehat{\gamma}^{(1)}_p=-\frac{2\,M_t^{(2)}\,M_{t+s+1}^{(2)}}{(s+p-r_1-1)_3},\qquad M_t^{(2)}=(t-1)(t+r_1),\quad t=\frac{\widehat{\tau}-r_1-r_2}{2},$$
with $(a)_3$ a Pochhammer symbol, $s$ the transverse spin, and $(r_1,r_2)$ the R-symmetry labels. These are the [[giant-graviton|giant graviton]]/light-supergraviton "binding energies," and they structurally mirror the bulk-channel double-trace anomalous dimensions obtained from four-point unmixing.

## Derivation sketch

Two routes give the same spectrum. (1) Solve the unmixing equations $\mathbf{B}\mathbf{B}^T=\mathbf{N}$, $\mathbf{B}\mathbf{\Gamma}\mathbf{B}^T=\mathbf{\Omega}$ sector by sector. (2) Use the [[ten-dimensional-hidden-conformal-symmetry|partially broken 10d hidden symmetry]]: decomposing the 10d generating function into single-twist $p=4$, $q=6$ defect blocks automatically produces mutually orthogonal projectors, so the anomalous dimensions come out already diagonalized ($\mathbb{\Gamma}^{(1)}_s=-24/(s+1)_3$), with no matrix diagonalization required. A fourth-order differential operator $\widehat{\mathbf{\Delta}}^{(4)}$ has the long defect superconformal blocks as eigenfunctions with eigenvalue $M_t^{(2)}M_{t+s+1}^{(2)}$, generating the $\log^\kappa V$ leading-log coefficient at any loop order $\kappa$ as $(\widehat{\mathbf{\Delta}}^{(4)})^{\kappa-1}h^{(\kappa)}$ — the defect analogue of the eighth-order operator of Caron-Huot–Trinh.

## Assumptions

Leading order in $1/N$ (with dimensions expanded as $\widehat\Delta=\widehat\Delta^{(0)}+\tfrac2N\widehat\gamma^{(1)}+\dots$); maximal giant gravitons; $\tfrac12$-BPS light operators.

## Status

Established at tree level; the fourth-order operator gives the all-loop leading logs. Full higher-loop (subleading-log) data would require the AdS unitarity method.

## Implications

- A complete, closed-form window into non-planar CFT data — a natural benchmark for integrability to reproduce.
- Demonstrates that the hidden symmetry not only generates correlators but also diagonalizes their OPE decomposition.
- Belongs to [[giant-graviton-correlators]].

## References

[[2602.13570|Chen-Jiang-Zhou 2026]] (the closed-form spectrum, hidden-symmetry diagonalization, and $\widehat{\mathbf{\Delta}}^{(4)}$).
