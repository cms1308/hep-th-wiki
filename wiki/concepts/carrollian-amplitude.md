---
type: concept
title: Carrollian amplitude
aliases: [Carrollian correlator, position-space amplitude at null infinity]
tags: [carrollian-physics, flat-space-holography, scattering-amplitudes]
prerequisites: ["carrollian-cft", "null-infinity"]
created: 2026-07-03
updated: 2026-07-03
---

## Definition

The massless $\mathcal S$-matrix written in position space at [[null-infinity]]: Fourier
transform each external leg's frequency $\omega_k$ to retarded time $u_k$ on $\mathscr I$.
The result transforms as a correlator of conformal Carrollian primaries of the boundary
[[carrollian-cft]] — it *is* the holographic correlator of
[[flat-space-holography|flat space holography]] in the Carrollian formulation
([[2312.10138|Mason–Ruzziconi–Srikant 2023]]):

$$\mathcal C_n \equiv
\langle\Phi^{\epsilon_1}_{\Delta_1,J_1}\cdots\Phi^{\epsilon_n}_{\Delta_n,J_n}\rangle
= \frac{1}{(2\pi)^n}\prod_{k=1}^n\int_0^{+\infty}\! d\omega_k\,\omega_k^{\Delta_k-1}\,
e^{-i\epsilon_k\omega_k u_k}\,
\mathcal A_n\big(\{\omega_k, z_k, \bar z_k\}^{\epsilon_k}_{J_k}\big),$$

with $\epsilon_k = \pm1$ for outgoing/incoming ([[2602.02644|Ruzziconi 2026]] conventions).
For $\Delta_k \ne 1$ this is the *modified Mellin transform* of Banerjee et al.; the
$\Delta\ne1$ operators are redundant $\partial_u$-descendants of the $\Delta=1$ ones.

## Motivation

Boundary values of massless spin-$J$ bulk fields,
$\Phi^\epsilon_J = \lim_{r\to\infty} r^{1-s}\phi^{(s)}|_{\mathscr I^\epsilon}$, are
Carrollian primaries with $k = \tfrac{1+\epsilon J}2$, $\bar k = \tfrac{1-\epsilon J}2$
($\Delta = 1$) — so the extrapolate dictionary of AdS/CFT has a direct flat-space analogue,
and scattering becomes boundary correlation. Unlike celestial amplitudes, Carrollian
amplitudes keep bulk translation invariance manifest and have non-distributional behavior in
$u$.

## Key formulas

- Two-point amplitude (free propagation, populating the electric branch):
  $$\langle\Phi^-_{\Delta_1,J}\Phi^+_{\Delta_2,J}\rangle = \frac{K_J^2}{4\pi}
  \frac{\Gamma(\Delta_1+\Delta_2-2)}{(u_{12}+i\varepsilon)^{\Delta_1+\Delta_2-2}}\,
  \delta^{(2)}(z_{12}) .$$
- Explicit 3-point (Klein signature) and 4-point (MHV gluon/graviton, $\phi^3$, $\phi^4$)
  amplitudes populate the electric branches of the [[carrollian-cft]] Ward identities.
- Computable directly by position-space Feynman rules at $\mathscr I$ with bulk-to-boundary
  propagator $\mathcal G^{\text{Flat},\Delta}_{Bb,\epsilon} \propto
  \Gamma(\Delta)/(-u - q\cdot X + i\epsilon\varepsilon)^\Delta$ — the flat analogue of
  Witten diagrams; these arise as
  [[flat-space-limit-of-witten-diagrams|flat limits of AdS Witten diagrams]].
- Soft physics: leading/subleading [[soft-graviton-theorems]] = large-$u$ limits of
  Carrollian stress-tensor Ward identities; collinear limits = Carrollian OPEs.
- Invertible transform to [[celestial-amplitude|celestial amplitudes]]:
  see [[carrollian-celestial-equivalence]].

## Relations

- Correlators of the boundary [[carrollian-cft]] (electric branches).
- Equivalent to celestial amplitudes ([[carrollian-celestial-equivalence]]).
- Arise as Carrollian limits of holographic CFT correlators
  ([[flat-carrollian-limit-correspondence]], [[carrollian-abjm-correspondence]]).

## Where it appears

[[2312.10138|Mason–Ruzziconi–Srikant 2023]] (definition), [[2602.02644|Ruzziconi 2026]] §7
(systematic treatment), [[2406.19343|Alday et al. 2024]] (from Witten diagrams),
[[2411.04902|Ruzziconi et al. 2024]] (soft theorems).
