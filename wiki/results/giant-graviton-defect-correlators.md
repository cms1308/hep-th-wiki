---
type: result
title: Strong-Coupling Giant Graviton Correlators
aliases: ["giant graviton defect correlators", "two-giant two-light correlators", "giant graviton correlator generating function"]
tags: [ads-cft, giant-graviton, defect-cft, holographic-correlators, n4-sym]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

All four-point functions of two maximal [[giant-graviton|giant gravitons]] ($\Delta=N$ determinant operators $\mathcal{D}$) and two arbitrary light $\tfrac12$-BPS single-trace operators $\mathcal{O}_{k_1},\mathcal{O}_{k_2}$ in 4d $\mathcal{N}=4$ SYM are determined at strong coupling (leading order in $1/N$). Recast as [[giant-graviton-defect|defect]] two-point functions $\langle\!\langle\mathcal{O}_{k_1}\mathcal{O}_{k_2}\rangle\!\rangle=\langle\mathcal{O}_{k_1}\mathcal{O}_{k_2}\mathcal{D}\mathcal{D}\rangle/\langle\mathcal{D}\mathcal{D}\rangle$, they are fixed up to a single overall constant, and all infinitely many of them follow from one seed correlator by the [[ten-dimensional-hidden-conformal-symmetry|partially broken 10d hidden symmetry]]:
$$H_{k_1k_2}=\frac{\sqrt{k_1k_2}}{2}\,\mathbf{H}(x_i;t_i;\lambda_1,\lambda_2)\big|_{\lambda_1^{k_1-2}\lambda_2^{k_2-2}},\qquad
H_{22}=\frac{2V(V^2-2V\log V-1)}{N\,(P_1\!\cdot\!\mathbb{N}\!\cdot\!P_1)^2(P_2\!\cdot\!\mathbb{N}\!\cdot\!P_2)^2\,U\,(1-V)^3}.$$
The reduced correlators also admit a Mellin representation with a $k$-independent 10d amplitude $\boldsymbol{\mathcal{M}}_{k_1k_2}=1/[(\boldsymbol\delta-1)(\boldsymbol\gamma-1)]$, whose high-energy behavior matches string–D-brane scattering.

## Derivation sketch

The [[analytic-defect-bootstrap]]: a finite ansatz of bulk-/defect-exchange and contact Witten diagrams (truncated by non-extremality) with coefficients fixed by the superconformal Ward identity, the overall constant set by the D3-brane action normalization, and the whole family generated from $H_{22}$ by the hidden-symmetry replacement $P_a\!\cdot\!\mathbb{N}\!\cdot\!P_b\to Z_a\!\cdot\!(\mathbb{N}+\mathbb{M})\!\cdot\!Z_b$.

## Assumptions

- Leading order in $1/N$ (tree-level supergravity); maximal giant gravitons; external $\tfrac12$-BPS operators.
- Moduli-space averaging performed *before* computing (quantum superposition), required for two-point and higher correlators to factorize correctly.

## Status

Established, with three independent checks: agreement with free-theory determinant-operator results (up to a $U(N)$-vs-$SU(N)$ one-point term), with a direct supergravity computation of bulk one-point functions, and with the Brown–Wen–Xie 2024 integrated-correlator localization prediction at $k_1=k_2=2$. A weak-coupling counterpart (a hidden-symmetry generating function for loop integrands) is conjectured and verified at one and two loops.

## Implications

- Provides the first strong-coupling four-point data for heavy operators in $\mathcal{N}=4$ SYM, and a benchmark for integrability (defect $g$-functions / boundary-state overlaps).
- Together with the extracted [[giant-graviton-defect-anomalous-dimensions|defect double-particle spectrum]], it makes non-planar dynamics computable.
- Belongs to [[giant-graviton-correlators]]; distinct from the [[giant-graviton-expansion]] (which reconstructs the finite-$N$ index).

## References

[[2503.22987|Chen-Jiang-Zhou 2025]] (letter); [[2602.13570|Chen-Jiang-Zhou 2026]] (long version, all KK levels + Mellin + spectrum).
