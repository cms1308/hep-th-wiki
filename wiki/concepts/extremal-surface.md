---
type: concept
title: RT / HRT surface
aliases: [RT surface, HRT surface, minimal surface, extremal surface, minimal-surface-in-ads, holographic minimal surface]
tags: [holography, entanglement, extremal-surface, differential-geometry]
prerequisites: [entanglement-entropy]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The bulk codimension-two surface whose area computes a boundary region's
[[entanglement-entropy|entanglement entropy]]. Anchored on the entangling surface,
$\partial\gamma_A=\partial A$, it comes in two forms:

- **RT (static) — minimal surface.** On a constant-time slice of a static bulk, $\gamma_A$ is
  the surface of least area homologous to $A$: it extremizes area and has vanishing mean
  (trace) extrinsic curvature.
- **HRT (covariant) — extremal surface.** In a general, time-dependent Lorentzian bulk, a
  minimal spacelike surface is ill-defined (wiggling in time lowers the area without bound),
  so $\gamma_A$ is instead an **extremal** surface — a saddle of the Lorentzian area
  functional, characterized covariantly by vanishing of both null expansions,
  $$\theta_+=\theta_-=0.$$
  When several extremal surfaces are anchored on $\partial A$, the one of **minimum area
  among those homologous to $A$** is selected.

The two agree in static spacetimes: the extremal surface then sits on the constant-$t$ slice
and $\theta_+=\theta_-=0$ reduces to the minimal-surface condition.

## Motivation

Extremality is the covariant replacement for minimality: it is the surface picked out by the
gravitational action principle / GKP-Witten dictionary, and it is well-defined without any
preferred bulk time-slicing. The vanishing-null-expansion characterization ties it directly to
the [[bousso-bound|covariant entropy bound]] (a light-sheet just grazing the surface saturates
the bound).

## Key formulas

- Area variation $\delta(\mathrm{Area})\propto\int_{\gamma}\big(\theta_+N_+^\mu+\theta_-N_-^\mu\big)\,\delta X_\mu$,
  so $\theta_\pm=0\Leftrightarrow$ extremal.
- Entropy: $S_A=\dfrac{\mathrm{Area}(\gamma_A)}{4G_N}$ — the [[ryu-takayanagi-formula|RT]] /
  [[hrt-formula|HRT]] formula.

## Relations

- Area gives $S_A$ via [[ryu-takayanagi-formula]] (static) and [[hrt-formula]] (covariant).
- Homology / minimum-area selection underlies later phase transitions between competing
  surfaces and the quantum-extremal-surface refinement (islands).
- Belongs to the topic [[holographic-entanglement-entropy]].

## Where it appears

- Static minimal surface: [[hep-th-0603001|Ryu-Takayanagi 2006]].
- Covariant extremal surface ($\theta_\pm=0$): [[0705.0016|Hubeny-Rangamani-Takayanagi 2007]].
