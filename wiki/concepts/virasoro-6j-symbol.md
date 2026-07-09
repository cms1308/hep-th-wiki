---
type: concept
title: Virasoro 6j-symbol
aliases: [Virasoro 6j symbol, Racah-Wigner 6j, Virasoro fusion kernel, crossing kernel, F-kernel]
tags: [conformal-field-theory, virasoro, crossing-kernel, virasoro-tqft]
prerequisites: [cardy-density-of-states]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The Racah-Wigner $6j$-symbol of the Virasoro algebra, the crossing (fusion) kernel for
four-point conformal blocks written in a symmetric, tetrahedrally invariant normalization:
$$\begin{Bmatrix} P_1 & P_2 & P_3\\ P_4 & P_5 & P_6\end{Bmatrix}
=\frac{1}{\rho_0(P_6)}\sqrt{\frac{C_0(P_1P_2P_3)\,C_0(P_3P_4P_5)}{C_0(P_1P_5P_6)\,C_0(P_2P_4P_6)}}\;
\mathbb F_{P_3P_6}\!\begin{bmatrix}P_4 & P_2\\ P_5 & P_1\end{bmatrix},$$
with $\mathbb F$ the Ponsot-Teschner fusion kernel, $C_0$ the universal OPE coefficient, and
$\rho_0$ the [[cardy-density-of-states|Cardy density]]. It has the full tetrahedral symmetry
of the $6$ weights, so it is naturally assigned to a tetrahedron.

## Motivation

It is the elementary crossing move on Virasoro conformal blocks, and — being the amplitude
of a tetrahedron — the fundamental building block of the state sum in
[[conformal-turaev-viro-theory|Conformal Turaev-Viro theory]], exactly as the classical
$6j$-symbol is in [[turaev-viro-theory|Turaev-Viro theory]]. Its normalization is fixed by
$\langle\Theta\text{-graph}\rangle=1$, which strips all factors of $C_0$ from amplitudes.

## Key formulas

- **Pentagon identity** — associativity of fusion; it is what makes the CTV state sum
  invariant under the 2-3 / 3-2 Pachner moves.
- **Self-duality under the $S$-transform** (tetrahedron graph in $S^3$):
$$\begin{Bmatrix}P_4'&P_5'&P_6'\\ P_1'&P_2'&P_3'\end{Bmatrix}^{2}
=\int_0^\infty\Big(\prod_{i=1}^{6}dP_i\,S_{P_i'P_i}\Big)
\begin{Bmatrix}P_1&P_2&P_3\\ P_4&P_5&P_6\end{Bmatrix}^{2},$$
a special case of the [[ctv-equals-s-transform-of-zvir-squared|CTV main identity]] with
$S_{P'P}=2\sqrt2\cos(4\pi P'P)$ the [[virasoro-modular-s-matrix|modular $S$-matrix]].

## Relations

- Built from the Ponsot-Teschner fusion kernel $\mathbb F$ and the universal OPE data
  $C_0$; related to the [[virasoro-modular-s-matrix|Racah-Wigner modular $S$-matrix]]
  $\widehat{\mathbb S}$ by the Post-Tsiares irrational Verlinde formula.
- Tetrahedron amplitude of [[virasoro-tqft|Virasoro TQFT]] / weight $W(\Delta)$ of
  [[conformal-turaev-viro-theory|CTV theory]].

## Where it appears

- Conventions and derivation: Ponsot-Teschner 2000, Eberhardt 2023 (review),
  Collier-Eberhardt-Mühlmann-Zhang 2023.
- As the tetrahedron weight and its $S$-transform identities: [[2507.11652|Hartman 2025]].
