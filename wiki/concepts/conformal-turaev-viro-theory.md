---
type: concept
title: Conformal Turaev-Viro theory
aliases: [CTV theory, Conformal Turaev-Viro, CTV]
tags: [tqft, 3d-gravity, virasoro-tqft, 3-manifolds, conformal-field-theory]
prerequisites: [turaev-viro-theory, virasoro-tqft, virasoro-6j-symbol, cardy-density-of-states]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A triangulation-based dual of [[virasoro-tqft|Virasoro TQFT]], defined in
[[2507.11652|Hartman 2025]]. For a closed 3-manifold $M_E$ with an embedded framed trivalent
graph $\Gamma(\mathsf P)$ and an admissible triangulation $T\supset\Gamma$, label edges by
continuous conformal weights (Liouville momenta $P$), assign each tetrahedron a
[[virasoro-6j-symbol|Virasoro $6j$-symbol]], and integrate internal edges with the
[[cardy-density-of-states|Cardy density]]:
$$Z_{\rm CTV}(M_E,\Gamma(\mathsf P))
=\int_{\mathbb R_+^{m}}\Big(\prod_{i=1}^{m} d\tilde P_i\,\rho_0(\tilde P_i)\Big)
\prod_{\Delta\in T} W(\Delta),\qquad
W(\Delta)=\begin{Bmatrix}P_4&P_5&P_6\\ P_1&P_2&P_3\end{Bmatrix}.$$
This is the [[turaev-viro-theory|Turaev-Viro]] state sum with the quantum dimension replaced
by $\rho_0(P)$ and the sum over spins by an integral over weights; the divergent
total-quantum-dimension prefactor is dropped.

## Motivation

Pure 3d gravity in AdS$_3$ can be computed on fixed topology by [[virasoro-tqft|Virasoro TQFT]], but VTQFT amplitudes live on framed graphs and their connection to an actual
triangulated metric geometry is indirect (phases that are hard to read geometrically). CTV
recasts the amplitude as a state sum over geometric tetrahedra, so one can translate directly
between semiclassical hyperbolic geometries and the TQFT. In the companion gravity program
$Z_{\rm CTV}$ is identified with the exact gravitational path integral on
$M=M_E-N(\Gamma)$ with fixed dihedral angles $\psi_i=2\pi i b P_i$ on the boundary geodesics.

## Key formulas

- **Main identity** — CTV is the modular $S$-transform of $|Z_{\rm Vir}|^2$:
$$Z_{\rm CTV}(M_E,\Gamma(\mathsf P'))
=\int_{\mathbb R_+^{n}} d\mathsf P\,\Big(\prod_{i=1}^{n} S_{P_i'P_i}\Big)
\big|Z_{\rm Vir}(M_E,\Gamma(\mathsf P))\big|^2,\qquad S_{P'P}=2\sqrt2\cos(4\pi P'P).$$
  See [[ctv-equals-s-transform-of-zvir-squared]].
- **Admissibility (large triangulations):** finiteness and triangulation-independence hold
  when $H_2(M_E-V_{\rm int})=0$. Large triangulations allow the 2-3/3-2 Pachner moves
  (invariance $\Leftarrow$ the pentagon identity) but forbid 1-4 moves, whose interior
  vertices create contractible $\Omega$-loops that diverge for the unbounded Virasoro
  spectrum.

## Relations

- Discrete predecessor: [[turaev-viro-theory]] (finite fusion category); CTV is its
  continuous/irrational Virasoro lift.
- Surgery dual: [[virasoro-tqft|Virasoro TQFT]] (analog of Reshetikhin-Turaev).
- Proof technique: [[chain-mail-formalism|Virasoro chain mail]] via marked Heegaard diagrams.
- Building blocks: [[virasoro-6j-symbol]], [[cardy-density-of-states]],
  [[virasoro-modular-s-matrix]].

## Where it appears

- Introduced in [[2507.11652|Hartman 2025]], with the AdS$_3$-gravity path-integral
  application developed in a companion paper.
