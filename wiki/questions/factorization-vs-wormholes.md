---
type: question
title: Factorization vs. wormholes
aliases: [factorization puzzle, factorization problem, wormhole factorization]
tags: [jt-gravity, wormholes, holography, ensemble-averaging]
status: open
created: 2026-07-07
updated: 2026-07-07
---

## Statement

If the gravitational path integral includes connected geometries ("wormholes") linking distinct
asymptotic boundaries, then $\langle Z(\beta_1)Z(\beta_2)\rangle\neq\langle Z(\beta_1)\rangle
\langle Z(\beta_2)\rangle$: the two-boundary answer does **not** factorize. But a single, ordinary
holographic boundary theory has $Z(\beta_1)Z(\beta_2)$ factorizing by definition. What, then, does
a bulk wormhole compute — and for a fixed (non-averaged) boundary theory, what forbids the wormhole
or restores factorization?

## Why it matters

In [[jt-gravity|JT gravity]] the resolution [[1903.11115|Saad–Shenker–Stanford]] give is that the
bulk is dual not to one theory but to an **ensemble**: the
[[jt-gravity-matrix-integral-duality|matrix integral]] computes disorder-averaged quantities, and
the non-factorization is just the variance
$\overline{Z_1Z_2}-\overline{Z_1}\,\overline{Z_2}$ — the [[trumpet-geometry|double trumpet]] and the
[[spectral-form-factor|ramp]]. This is clean in 2d, but higher-dimensional gravity (e.g.
$\mathcal N=4$ SYM dual to $AdS_5\times S^5$) is expected to be a single theory, where an ensemble
interpretation is problematic. The puzzle sits at the center of the black-hole information problem,
replica wormholes, and the meaning of the gravitational path integral.

## Main attempts

- **Ensemble averaging** (2d): accept that JT / SYK gravity is dual to a distribution of boundary
  theories; wormholes compute connected moments. Extended to other symmetry classes by
  Stanford–Witten.
- **$\alpha$-states / baby universes**: a Hilbert space of "$\alpha$-states" in which the bulk
  wormhole amplitudes are diagonalized and each member is a fixed theory that factorizes
  (Marolf–Maxfield, Coleman-type third quantization).
- **Half-wormholes / self-averaging**: for a single realization, extra saddle-like contributions
  restore factorization on average (Saad–Shenker–Stanford–Yang and follow-ups).
- **Positivity as a filter on the ensemble**: an ensemble interpretation is only consistent if
  its measure is positive. [[2605.05305|Di Ubaldo–Iliesiu–Lin–Yan 2026]] show that
  [[euclidean-axion-wormhole|axion wormholes]] make the two-boundary variance diverge while the
  mean stays finite, violating [[gravitational-path-integral-positivity|path-integral positivity]]
  unless instantons intervene — turning the puzzle into a swampland constraint (the axionic
  [[weak-gravity-conjecture|WGC]]). Whether these imaginary-scalar wormholes belong on the
  integration contour at all is itself contested ([[2605.05336|Maldacena–Maloney–McPeak 2026]];
  Held–Kaplan–Marolf–Wang; Witten 2026).

## Current status

**Open.** In 2d the ensemble picture is well established and consistent. Whether higher-dimensional
holographic theories (which appear to be single, non-averaged CFTs) admit connected wormhole
contributions, and how factorization is enforced there, remains unresolved — one of the sharpest
open problems raised by the [[1903.11115|JT/matrix duality]].
