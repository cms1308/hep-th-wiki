---
type: concept
title: Cardy density of states
aliases: [rho_0, Virasoro Cardy density, universal density of states, C_0 density]
tags: [conformal-field-theory, virasoro, cardy-formula, virasoro-tqft]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The universal (chiral) density of Virasoro primaries above the black-hole threshold, written
in the Liouville-momentum variable $P$ (with $h=\tfrac{Q^2}{4}+P^2$, $c=1+6Q^2$,
$Q=b+b^{-1}$):
$$\rho_0(P) = 4\sqrt2\,\sinh(2\pi b P)\,\sinh(2\pi b^{-1}P).$$
It is the Cardy formula in its exact "modular $S$-matrix" form: $\rho_0(P)=\mathbb S_{\id\,P}[\id]$,
the vacuum-to-$P$ entry of the Virasoro modular kernel. In [[virasoro-tqft|Virasoro TQFT]] and
[[conformal-turaev-viro-theory|CTV theory]] it is the measure on internal edges,
$$\int_i \;\equiv\; \int_0^\infty dP_i\,\rho_0(P_i),$$
i.e. the continuous replacement for the quantum dimension of ordinary
[[turaev-viro-theory|Turaev-Viro theory]].

## Motivation

For an irrational/continuous spectrum there is no finite set of quantum dimensions to sum
over; the state sum instead integrates over continuous weights, and $\rho_0(P)$ is the
canonical weight fixed by modular invariance (the asymptotic density of the identity block's
$S$-transform). It also equals the tree-level (semiclassical) universal OPE data
$C_0$ evaluated on the diagonal, tying the TQFT measure to CFT structure constants.

## Key formulas

- $\rho_0(P)=4\sqrt2\,\sinh(2\pi bP)\sinh(2\pi b^{-1}P)=\mathbb S_{\id\,P}[\id]$.
- Heavy limit $P\to\infty$: $\rho_0(P)\sim \sqrt2\,e^{2\pi Q P}$, the Cardy exponential growth
  $S=2\pi\sqrt{\tfrac{c}{6}(h-\tfrac{c}{24})}$ recast in $P$.

## Relations

- Same functional form as the [[jt-spectral-curve|JT gravity density of states]]
  $\rho_0(E)\propto\sinh(2\pi\sqrt{2\gamma E})$: the JT/Schwarzian density is the fixed-$b$
  (semiclassical, near-extremal) limit of the double-$\sinh$ Virasoro density, reflecting that
  [[schwarzian-theory|Schwarzian]] dynamics governs the density of near-threshold Virasoro
  descendants. The $\sinh$ structure is the shared signature of a continuous, gravitationally
  dressed spectrum.
- Sets the measure in the [[ctv-equals-s-transform-of-zvir-squared|CTV state sum]] and the
  normalization of the [[virasoro-6j-symbol|Virasoro $6j$-symbol]] and
  [[virasoro-modular-s-matrix|modular $S$-matrix]].

## Where it appears

- Universal OPE / $C_0$ origin: Collier-Maloney-Maxfield-Tsiares 2019.
- As the internal-edge measure of [[conformal-turaev-viro-theory|CTV theory]]:
  [[2507.11652|Hartman 2025]].
