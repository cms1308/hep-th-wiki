---
type: method
title: KK reduction of wormholes
aliases: [Kaluza-Klein reduction of wormholes, black hole to wormhole reduction]
tags: [wormholes, kaluza-klein, moduli-space, complex-metrics]
prerequisites: [euclidean-axion-wormhole]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

Maps higher-dimensional black-hole and Schwarzschild geometries to lower-dimensional
[[euclidean-axion-wormhole|scalar wormholes]] by Kaluza-Klein reduction, so that the
[[imaginary-distance-bound|imaginary distance bound]] in the reduced theory can be read off from
the parent geometry — and, conversely, identifies which wormholes are complex-metric continuations
of familiar black holes ([[2605.05336|Maldacena-Maloney-McPeak 2026]]).

## Prerequisites

- [[euclidean-axion-wormhole]] — the wormhole solutions being reproduced.
- [[anti-de-sitter-space]] and basic Kaluza-Klein reduction on $S^1$/$T^N$.

## How it works

- **$S^1$ reduction of pure gravity.** Reducing $(D+1)$-dimensional gravity on a circle produces
  a non-compact radion scalar $\nu=\log\tilde r$ with kinetic normalization $\hat\kappa^2=2(D-1)/(D-2)$.
  The scalar wormhole in $D$ dimensions is literally the $(D+1)$-dimensional Schwarzschild
  solution evaluated on a complex-$r$ contour, matching the
  [[spectral-form-factor|Saad-Shenker-Stanford double cone]]. The IDB becomes $|\mathrm{Im}\,\nu|\le\pi/2$,
  which coincides with the [[kontsevich-segal-witten-criterion|KSW criterion]] for the circle
  metric component.
- **$S^1$ reduction of Einstein-Maxwell.** Gives moduli $(\nu,\tilde\alpha)$ on hyperbolic space
  of radius $\hat\kappa$; a wrapped charged particle's action vanishes on the extremal lines
  exactly when $m=\hat\kappa q$, so demanding a superextremal state to spoil the wormhole
  reproduces the [[weak-gravity-conjecture|WGC]].
- **$T^N$ reduction.** The internal-metric moduli carry the KSW eigenphases $\theta_i$ with
  $\sum_i|\theta_i|<\pi$; the longest allowed timelike geodesic reproduces the flat-space IDB
  $\tau_{\rm IDB}$ exactly.

## Regime of validity

Semiclassical, low-energy Einstein(-Maxwell) gravity with a compact internal circle/torus. The
identification holds where the KK modes decouple and the complex-metric continuation stays
KSW-allowable; it says nothing about whether the wormhole contour genuinely contributes to the
path integral (an open question — [[factorization-vs-wormholes]]).

## Canonical applications

- Deriving the [[imaginary-distance-bound|IDB]] and its equivalence to the
  [[kontsevich-segal-witten-criterion|KSW criterion]] and the
  [[weak-gravity-conjecture|WGC]] ([[2605.05336|Maldacena-Maloney-McPeak 2026]]).
- Identifying the [[spectral-form-factor|double-cone wormhole]] as a KK-reduced Schwarzschild
  geometry.
