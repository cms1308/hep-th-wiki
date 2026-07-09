---
type: method
title: Flat space limit of Witten diagrams
aliases: [Carrollian limit of holographic correlators, position-space flat limit]
tags: [flat-space-holography, ads-cft, witten-diagrams, carrollian-physics]
prerequisites: ["ads-cft-correspondence", "carrollian-amplitude"]
created: 2026-07-03
updated: 2026-07-03
---

## What it computes

[[carrollian-amplitude|Carrollian amplitudes]] (massless $\mathcal S$-matrix elements in
position space at [[null-infinity]]) as the $\ell\to\infty$ limit of AdS Witten diagrams —
in *position space*, without passing through momentum space. This is the computational
engine behind the [[flat-carrollian-limit-correspondence]]
([[2406.19343|Alday–Nocchi–Ruzziconi–Yelleshpur Srikant 2024]]; reviewed in
[[2602.02644|Ruzziconi 2026]] §9).

## Prerequisites

Witten-diagram technology in AdS ([[ads-boundary-dictionary|GKP–Witten dictionary]]),
Bondi-type coordinates for AdS, the electric/magnetic branch structure of
[[carrollian-cft]] correlators.

## How it works

Two routes that agree diagram by diagram:

1. **Bulk route.** Write AdS$_4$ in Bondi coordinates,
   $ds^2 = -\tfrac{r^2}{\ell^2}du^2 - 2dudr + 2r^2dzd\bar z$, and take $\ell\to\infty$ at
   fixed $(u,r,z,\bar z)$. AdS bulk-to-bulk and bulk-to-boundary propagators limit to their
   flat counterparts (the flat bulk-to-boundary propagator
   $\propto \Gamma(\Delta)/(-u - q\cdot X + i\epsilon\varepsilon)^\Delta$), so each Witten
   diagram (2-, 3-, 4-point, contact and exchange) limits to the corresponding
   position-space Feynman diagram at $\mathscr I$ computing a Carrollian amplitude.
2. **Boundary route (intrinsic in the CFT).** Since $c_{\text{boundary}} =
   \ell^{-1}_{\text{bulk}}$, the same limit is a Carrollian $c\to0$ limit of the holographic
   correlator: analytically continue to Lorentzian boundary signature, restore $c$, scale
   operators electrically ($\Phi_\Delta \sim c^{\Delta-1}\mathcal O_\Delta$), and extract
   the leading **electric branch**. The distributional $\delta^{(2)}(z_{ij})$ support arises
   from the **bulk-point singularity** of the Lorentzian $\bar D$-functions as
   $Z \to \bar Z$.

## Regime of validity

Established for massless external states, tree-level contact and exchange Witten diagrams at
2-, 3-, 4-point in AdS$_4$/CFT$_3$ (and applied top-down to ABJM half-BPS correlators,
[[carrollian-abjm-correspondence]]). Loops, massive states ($\Delta\sim\ell$ scaling), and
higher-point functions are open frontiers.

## Canonical applications

- Diagram-by-diagram verification of the [[flat-carrollian-limit-correspondence]].
- [[carrollian-abjm-correspondence]]: Carrollian limit of ABJM correlators = 11d
  supergravity Carrollian amplitudes with restricted kinematics
  ([[2504.10291|Lipstein et al. 2025]]).
