---
type: concept
title: Euclidean axion wormhole
aliases: [axion wormhole, Giddings-Strominger wormhole, scalar wormhole, Euclidean scalar wormhole]
tags: [wormholes, axions, instantons, quantum-gravity, moduli-space]
prerequisites: [anti-de-sitter-space]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A Euclidean solution of Einstein gravity coupled to a massless scalar (or, dually, an axion)
in which two asymptotic regions are joined by a throat. The scalar profile is supported by a
conserved charge $q=-i\int_{S^{D-1}}\partial_n\varphi$; for a real charge the scalar takes
*imaginary* values through the throat, flipping the sign of its stress tensor so that the
throat can be held open. Introduced by Giddings-Strominger (1987) for the axion and extended to
string theory by Arkani-Hamed-Orgera-Polchinski (2007).

For $D$-dimensional gravity plus a canonically normalized scalar $\varphi=i\tau(a)$ with
$ds^2=da^2/F(a)+a^2\,d\Omega_{D-1}^2$, the flat-space solution has $F=1-(a_0/a)^{2(D-2)}$, and
the total imaginary displacement across the wormhole is independent of the throat size $a_0$:
$$\Delta\tau_\infty=\pi\sqrt{\frac{2(D-1)}{D-2}},\qquad I_{\rm on\text{-}shell}=0.$$
The vanishing action follows from the trace of the Einstein equations plus the scale invariance
of the $\Lambda=0$ solution ([[2605.05336|Maldacena-Maloney-McPeak 2026]]).

## Motivation

Wormholes connecting distinct boundaries make the gravitational path integral non-factorize,
which underlies the ensemble interpretation of gravity ([[factorization-vs-wormholes]]) and the
[[spectral-form-factor|spectral form factor]] ramp. The axion wormhole is the simplest such
saddle, and — because its scalar must be imaginary — it is the seed for the
[[imaginary-distance-bound|imaginary distance bound]]: the size-independent displacement fixes an
absolute limit on imaginary continuation of couplings.

## Key formulas

- Sigma-model action: $I=\tfrac{1}{16\pi G_N}\int d^Dx\sqrt g\big[-(R-2\Lambda)+\tfrac12 h_{ab}\nabla\varphi^a\nabla\varphi^b\big]$.
- Flat displacement $\Delta\tau_\infty=\pi\sqrt{2(D-1)/(D-2)}$, zero on-shell action.
- Dualized description: axion $\to$ $(D-2)$-form $B$ with $H=dB$, fixed integer flux
  $\tfrac{1}{2\pi}\int_{\Sigma}H=m$; real saddles for imaginary axion, action linear in $|m|$
  ([[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]]).
- Dirichlet amplitude from the flux sum:
  $Z_{\rm WH}(\Delta a)\sim\dfrac{\sinh(\mathrm{Im}\,\Delta a_{\rm crit})}{\cosh(\mathrm{Im}\,\Delta a_{\rm crit})-\cos(\Delta a)}$,
  diverging as $\mathrm{Im}\,\Delta a\to\mathrm{Im}\,\Delta a_{\rm crit}$.

## Relations

- KK reduction of higher-dimensional Schwarzschild gives a non-compact-scalar wormhole equal to
  the [[spectral-form-factor|Saad-Shenker-Stanford double cone]] on a complex-$r$ contour
  ([[kaluza-klein-reduction-wormholes]]).
- The imaginary scalar is why the [[kontsevich-segal-witten-criterion|KSW criterion]] and the
  [[imaginary-distance-bound|IDB]] apply: continuation of the metric/moduli into the complex
  plane is exactly what the wormhole realizes.
- In the axio-dilaton case the wormhole is a timelike geodesic in Lorentzian AdS$_2$ moduli
  space; $D(-1)$ instantons destabilize it before its amplitude diverges.

## Where it appears

- [[2605.05336|Maldacena-Maloney-McPeak 2026]] — scalar wormholes across $D$; the
  size-independent displacement; string realizations.
- [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] — axion wormhole amplitude, its divergence, and
  the resulting positivity constraint.
- [[1903.11115|Saad-Shenker-Stanford 2019]] — the double-cone / half-wormhole context.
