---
type: topic
title: Flat space holography
aliases: [flat holography, holography in asymptotically flat spacetimes]
tags: [flat-space-holography, holography, carrollian-physics, celestial-holography]
prerequisites: ["ads-cft-correspondence"]
created: 2026-07-03
updated: 2026-07-03
---

## Overview

The program of finding a holographic dual for quantum gravity in *asymptotically flat*
spacetimes — the setting of real collider and gravitational-wave physics — where the
conformal boundary [[null-infinity|null infinity]] $\mathscr I$ is a null hypersurface rather
than the timelike boundary of AdS. The natural observable is the $\mathcal S$-matrix, and the
dual theory should compute it. Two bottom-up formulations exist and are now known to be
equivalent for massless scattering ([[carrollian-celestial-equivalence]]):

- **Carrollian holography**: the dual is a 3d [[carrollian-cft]] living on $\mathscr I$, one
  dimension down; $\mathcal S$-matrix elements in position space at $\mathscr I$ are its
  correlators ([[carrollian-amplitude|Carrollian amplitudes]]).
- **[[celestial-holography|Celestial holography]]**: the dual is a 2d CFT on the celestial
  sphere, two dimensions down; Mellin-transformed amplitudes are its correlators.

The modern claim, reviewed in [[2602.02644|Ruzziconi 2026]], is that flat space holography
need not be conjectured independently: it *arises as a controlled limit of the
[[ads-cft-correspondence]]*, with the bulk flat limit $\ell\to\infty$ implemented on the
boundary as a Carrollian limit $c\to0$ ([[flat-carrollian-limit-correspondence]]).

## Historical development

- **1998–2003 — early flat limits of AdS/CFT**: Susskind, Polchinski, Giddings extract flat
  $\mathcal S$-matrix elements from AdS correlators; de Boer–Solodukhin propose holography at
  $\mathscr I$. The program stalls without boundary symmetry control.
- **2013–17 — the IR triangle**: [[andrew-strominger|Strominger]] connects soft theorems,
  asymptotic ([[bms-symmetry|BMS]]) symmetries, and memory effects; soft theorems become Ward
  identities of $\mathscr I$-symmetries → [[soft-graviton-theorems]].
- **2016–21 — celestial amplitudes**: Pasterski–Shao–Strominger recast amplitudes as 2d
  celestial correlators via Mellin transform; $Lw_{1+\infty}$ symmetry discovered
  ([[lw-infinity-algebra]]).
- **2022–23 — Carrollian route**: BMS = conformal Carroll ([[1402.5894|DGH 2014]]) is turned
  into a holographic dictionary ([[2212.12553|Donnay–Fiorucci–Herfray–Ruzziconi 2022]],
  [[2202.08438|Bagchi et al. 2022]]); [[2312.10138|Mason–Ruzziconi–Srikant 2023]] define
  Carrollian amplitudes and the invertible transform to celestial ones.
- **2024–26 — derivation from AdS/CFT**: flat limits of Witten diagrams reproduce Carrollian
  amplitudes diagram by diagram ([[2406.19343|Alday–Nocchi–Ruzziconi–Yelleshpur Srikant 2024]]);
  soft theorems from Carrollian stress-tensor Ward identities
  ([[2411.04902|Ruzziconi et al. 2024]]); top-down realization in ABJM/M-theory
  ([[2504.10291|Lipstein et al. 2025]]). Consolidated in [[2602.02644|Ruzziconi 2026]].

## Key concepts

- [[null-infinity]] — the boundary; carries a universal Carroll structure.
- [[bms-symmetry]] — the asymptotic symmetry group replacing the conformal group.
- [[carrollian-amplitude]] and [[celestial-amplitude]] — the two correlator presentations of
  the $\mathcal S$-matrix.
- [[carrollian-cft]] — the proposed dual theory class.
- [[soft-graviton-theorems]] — Ward identities of the boundary symmetries.

## Key results

- [[carrollian-celestial-equivalence]] — the two formulations are one (massless sector).
- [[flat-carrollian-limit-correspondence]] — flat holography as the $c=\ell^{-1}\to0$ limit
  of AdS/CFT, verified at correlator level via
  [[flat-space-limit-of-witten-diagrams|flat limits of Witten diagrams]].
- [[carrollian-abjm-correspondence]] — first top-down example: Carrollian ABJM = 11d
  supergravity amplitudes with restricted kinematics.

## Current status

Kinematic dictionary established and cross-checked; massless tree-level scattering fully
translated. The dual is so far *defined by the limit* rather than intrinsically; loops,
massive states, and non-perturbative structure remain largely open. The celestial and
Carrollian communities are effectively merged through the equivalence.

## Open questions

- [[intrinsic-definition-of-carrollian-cft]] — a standalone definition of the dual.
- [[massive-states-in-carrollian-holography]] — massive scattering at $\mathscr I$ (or
  timelike infinity).
- [[internal-space-decompactification]] — seeing full 11d kinematics from Carrollian ABJM.
- IR/hard factorization as magnetic/electric Carrollian sectors.
- Spacetime interpretation of [[lw-infinity-algebra]] beyond the self-dual sector.
