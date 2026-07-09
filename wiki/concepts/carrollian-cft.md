---
type: concept
title: Carrollian CFT
aliases: [conformal Carrollian field theory, CCFT3, BMS field theory]
tags: [carrollian-physics, flat-space-holography, conformal-field-theory]
prerequisites: ["carroll-group", "carrollian-geometry", "bms-symmetry"]
created: 2026-07-03
updated: 2026-07-03
---

## Definition

A quantum field theory whose global spacetime symmetry is the conformal Carroll group —
equivalently, by [[bms-conformal-carroll-isomorphism]], a BMS-invariant field theory. In the
holographically relevant case $d=3$, $N=2$: fields live on the flat Carroll structure
$(u, z, \bar z)$ at [[null-infinity]] and organize into **conformal Carrollian primaries**
with weights $(k, \bar k)$, $\Delta = k+\bar k$, $s = k - \bar k$, transforming as

$$\delta_\xi\Phi = \Big[\big(\mathcal T + \tfrac u2(\partial\mathcal Y +
\bar\partial\bar{\mathcal Y})\big)\partial_u + \mathcal Y\partial +
\bar{\mathcal Y}\bar\partial + k\,\partial\mathcal Y +
\bar k\,\bar\partial\bar{\mathcal Y}\Big]\Phi .$$

Because no satisfactory Lagrangian quantization exists (see
[[electric-magnetic-carrollian-theories]]), the holographic Carrollian CFT is currently
defined by its symmetries — Ward identities, correlator branches, OPEs — and, operationally,
as the Carrollian limit of a holographic CFT ([[flat-carrollian-limit-correspondence]]).

## Motivation

This is the proposed dual of gravity in 4d asymptotically flat space
([[flat-space-holography]]): a 3d theory at $\mathscr I$ whose correlators are
[[carrollian-amplitude|Carrollian amplitudes]], i.e. the massless $\mathcal S$-matrix in
position space. Its ultra-locality naturally produces the distributional features that look
pathological from the 2d celestial viewpoint.

## Key formulas

Conventions of [[2602.02644|Ruzziconi 2026]] §6. Stress-tensor conditions on the flat
Carroll background (quantum Ward identities of $\mathfrak{eCCarr}_3$):

$$\partial_a T^a{}_b = 0, \qquad T^A{}_u = 0 \;(\text{boost invariance — no energy
transport}), \qquad T^a{}_a = 0 .$$

**Branch structure**: solving the global Ward identities does *not* fix low-point functions
uniquely; they split into

- a **magnetic branch** — $u$-independent, equal to 2d CFT correlators, e.g.
  $\langle\Phi_1\Phi_2\rangle^{(m)} \propto z_{12}^{-2k}\bar z_{12}^{-2\bar k}$;
- **electric branches** — distributional, e.g.
  $\langle\Phi_1\Phi_2\rangle^{(e)} = C^{(e)}_{12}\, u_{12}^{2-\Delta_1-\Delta_2}\,
  \delta^{(2)}(z_{12})$, and in Klein signature branches supported on $\delta(\bar z_{ij})$.
  The four-point electric branch depends on the Carroll invariant
  $F_{1234} = u_4 - u_1 z\,|z_{24}/z_{12}|^2 + \ldots$ on the support $z = \bar z$.

Carrollian amplitudes populate the electric branches; soft theorems are large-$u$ limits of
the stress-tensor Ward identities; collinear limits give **Carrollian OPEs** (uniform and
holomorphic), derived from symmetry alone. No state-operator correspondence is known.

## Relations

- Symmetry algebra: [[bms-symmetry]] $\simeq$ [[conformal-carrollian-algebra]].
- Correlator branches mirror [[electric-magnetic-carrollian-theories]].
- Correlators = [[carrollian-amplitude|Carrollian amplitudes]]; integral transform to
  [[celestial-holography|celestial CFT]] correlators ([[carrollian-celestial-equivalence]]).
- Obtained as $c\to0$ limits of relativistic CFTs; obstruction to intrinsic quantization:
  [[carrollian-quantization-obstruction]].

## Where it appears

[[2602.02644|Ruzziconi 2026]] §6–7; [[2212.12553|Donnay–Fiorucci–Herfray–Ruzziconi 2022]]
and [[2202.08438|Bagchi et al. 2022]] (holographic proposal);
[[2503.15607|Nguyen–Ruzziconi 2025]] (OPEs and branches). Central open question:
[[intrinsic-definition-of-carrollian-cft]].
