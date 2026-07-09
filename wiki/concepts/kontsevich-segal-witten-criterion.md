---
type: concept
title: Kontsevich-Segal-Witten criterion
aliases: [KSW criterion, complex metric admissibility, Kontsevich-Segal criterion]
tags: [complex-metrics, quantum-gravity, path-integral, allowability]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

An admissibility condition on complex spacetime metrics appearing in the gravitational path
integral (Kontsevich-Segal 2021; Witten 2021). A complex metric $g_{\mu\nu}$ is *allowable* if
every $p$-form field has a convergent (positive-real-part) kinetic action. Diagonalizing the
metric so its eigenvalues are $\lambda_i=|\lambda_i|e^{i\theta_i}$, the criterion is
$$\sum_{i=1}^{D}\big|\mathrm{Arg}\,\lambda_i\big|=\sum_{i=1}^D|\theta_i|<\pi.$$
Real Euclidean metrics ($\theta_i=0$) and real Lorentzian metrics (one $\theta=\pi$, saturating
the bound) are the boundary cases; the criterion selects which complex saddles may legitimately
appear on the integration contour.

## Motivation

Complex saddles are unavoidable in gravity (e.g. the analytic continuations underlying
wormholes and no-boundary proposals), but not every complex metric gives a sensible,
convergent theory. The KSW criterion is the minimal requirement that matter path integrals on
the background converge, giving a sharp, field-content-independent (for the standard $p$-forms)
notion of an allowable metric.

## Key formulas

- Allowability: $\sum_i|\mathrm{Arg}\,\lambda_i|<\pi$ for the complex metric eigenvalues.
- Circle-reduction form: for a KK circle with metric component $e^{2\nu}$, allowability is
  $|\mathrm{Im}\,\nu|\le\pi/2$ — exactly the [[imaginary-distance-bound|IDB]] value for that
  modulus ([[2605.05336|Maldacena-Maloney-McPeak 2026]]).

## Relations

- **Equivalent to the [[imaginary-distance-bound|IDB]] for torus moduli**: reducing on $T^N$,
  the longest KSW-allowed timelike geodesic in the internal-metric moduli space gives
  $\tau^2<\tfrac{\pi^2}{4}\tfrac{2(D-1)}{D-2}=\tau_{\rm IDB}^2$. The IDB generalizes KSW from the
  metric to all fields, so KSW is the metric-sector special case of the IDB.
- Controls which [[euclidean-axion-wormhole|wormhole]] continuations are on-contour; the
  breakdown of the low-energy theory at the IDB is where KSW allowability is lost for the
  relevant modulus.
- A duality-invariant generalization of KSW covering all fields is an open direction raised by
  [[2605.05336|Maldacena-Maloney-McPeak 2026]].

## Where it appears

- [[2605.05336|Maldacena-Maloney-McPeak 2026]] — identifies KSW as the metric-moduli case of the
  IDB and matches the two bounds exactly for $T^N$ reductions.
