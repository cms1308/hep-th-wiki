---
type: concept
title: Imaginary distance bound
aliases: [IDB, imaginary distance conjecture, imaginary distance]
tags: [swampland, wormholes, moduli-space, complex-metrics, weak-gravity-conjecture]
prerequisites: [euclidean-axion-wormhole, weak-gravity-conjecture]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A conjectured upper bound on how far a coupling constant (scalar modulus) can be analytically
continued in the *imaginary* direction before the low-energy gravity description must break
down. Starting from a real point in moduli space and displacing a canonically normalized scalar
to $\varphi=i\tau$, the bound is
$$\tau\le\tau_{\rm IDB}=\frac{\pi}{2}\sqrt{\frac{2(D-1)}{D-2}}\qquad(\text{flat space, }D\text{ dimensions})$$
([[2605.05336|Maldacena-Maloney-McPeak 2026]]). In AdS$_D$ with flat slicing the bound tightens
to $\tau'_{\rm IDB}=\tfrac{\pi}{2}\sqrt{2(D-2)/(D-1)}$. The value is set by
[[euclidean-axion-wormhole|Euclidean scalar wormholes]]: the imaginary displacement across a
wormhole is size-independent, $\Delta\tau_\infty=\pi\sqrt{2(D-1)/(D-2)}=2\tau_{\rm IDB}$, and at
half that displacement zero-action wormholes of arbitrary size begin to contribute to
$Z(p+i\tau)Z(p-i\tau)$, making it diverge.

The companion [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] phrases the same physics as an
**imaginary distance conjecture** for a single axion of decay constant $f_a$: axion wormhole
amplitudes diverge when the imaginary axion excursion reaches a universal critical value,
$$|\mathrm{Im}\,\Delta a|\le\frac{1}{f_a}\sqrt{\frac{\pi(d-1)}{8d\,G_N}}\quad(\text{AdS}_{d+1}),$$
independent of the AdS radius and of the wormhole slicing.

## Motivation

Euclidean wormholes are usually interpreted as an average over couplings, which sits uneasily
with the absence of fundamental free couplings in string theory. Taking the imaginary scalar of
the wormhole solution seriously as a complexified coupling, the divergence of the two-point
function of partition functions at $\tau_{\rm IDB}$ signals that a *single* theory cannot be
continued past that point — some UV effect (instantons, a light tower) must intervene. The
conjecture is that this always happens at or before $\tau_{\rm IDB}$.

## Key formulas

- Flat bound: $\tau_{\rm IDB}=\tfrac{\pi}{2}\sqrt{2(D-1)/(D-2)}$; AdS bound
  $\tau'_{\rm IDB}=\tfrac{\pi}{2}\sqrt{2(D-2)/(D-1)}$.
- Wormhole displacement (flat): $\Delta\tau_\infty=\pi\sqrt{2(D-1)/(D-2)}=2\tau_{\rm IDB}$.
- Enforcing corrections: terms $c_n e^{\pm i n\varphi}$, bounded for real $\varphi$, diverge at
  $\varphi=i\tau$.
- Torus reduction: the [[kontsevich-segal-witten-criterion|KSW]] longest timelike geodesic gives
  $\tau^2<\tfrac{\pi^2}{4}\tfrac{2(D-1)}{D-2}=\tau_{\rm IDB}^2$ — IDB $\equiv$ KSW for metric
  moduli, and the IDB generalizes KSW to *all* moduli.

## Relations

- **Generalizes the [[kontsevich-segal-witten-criterion|KSW criterion]]**: for $T^N$ metric
  moduli the IDB reproduces KSW exactly; the IDB extends the admissibility condition from the
  metric to all fields (scalars, form fields).
- **Contains the [[weak-gravity-conjecture|WGC]]**: reducing Einstein-Maxwell on $S^1$, a
  wrapped charged particle's action vanishes on the extremal lines exactly when the WGC bound is
  saturated; demanding a superextremal state to spoil the wormhole reproduces the WGC (and the
  [[convex-hull-condition]] with many gauge fields).
- **Derives the axionic WGC coefficient**: in [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]],
  requiring [[gravitational-path-integral-positivity|path-integral positivity]] to survive the
  wormhole divergence forces $S_{\rm inst}\le\tfrac12|\mathrm{Im}\,\Delta a_{\rm crit}|$ — the
  axionic WGC with a fixed $\mathcal O(1)$ constant.
- **Distinct from the swampland distance conjecture**: that bounds displacement in the *real*
  moduli direction (light towers at infinite distance); the IDB is a *finite imaginary*
  displacement bound. Part of the [[swampland-program]].

## Where it appears

- [[2605.05336|Maldacena-Maloney-McPeak 2026]] — introduces the IDB; flat/AdS values, KK/KSW
  equivalence, WGC as a special case, and string checks (type IIB, $T^4$).
- [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] — the imaginary distance conjecture for axions;
  derives the sharp axionic WGC from path-integral positivity.
