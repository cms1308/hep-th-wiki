---
type: concept
title: Covariant entropy bound (Bousso bound)
aliases: [Bousso bound, covariant entropy bound, light-sheet, light sheet, null expansion, holographic entropy bound]
tags: [holography, entropy-bounds, black-holes, general-relativity]
prerequisites: [bekenstein-hawking-entropy]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A covariant, background-independent bound on entropy (Bousso 1999). Given any codimension-two
spacelike surface $\Sigma$, follow a **light-sheet** $L_\Sigma$ — a null congruence orthogonal
to $\Sigma$ with non-positive expansion, $\theta\le0$ (the rays are locally converging). The
entropy $S_{L_\Sigma}$ that passes through the light-sheet is bounded by the area of $\Sigma$:
$$S_{L_\Sigma}\le\frac{\mathrm{Area}(\Sigma)}{4G_N}.$$
This repairs the naive spacelike "entropy $\le$ area of enclosing surface" bound, which fails
in cosmology and inside black holes, by projecting along null directions instead.

## Motivation

It is the sharpest general form of the holographic principle: it holds in arbitrary
time-dependent spacetimes and reduces to the Bekenstein and 't Hooft-Susskind bounds in the
appropriate limits. The light-sheet's defining data — a codimension-two surface with
controlled **null expansions** $\theta_\pm$ — is exactly the data that defines the covariant
holographic entanglement surface.

## Key formulas

- Bound: $S_{L_\Sigma}\le \mathrm{Area}(\Sigma)/4G_N$.
- Null expansions $\theta_\pm=(\chi_\pm)^\mu{}_\mu$ are traces of the two null extrinsic
  curvatures of $\Sigma$; a light-sheet requires $\theta\le0$.

## Relations

- Motivates the [[hrt-formula|HRT proposal]]: minimizing the area of a surface that supports
  both future and past light-sheets ($\theta_{\hat+}\le0,\ \theta_{\hat-}\le0$) drives it to
  the [[extremal-surface|extremal surface]] with $\theta_+=\theta_-=0$, which saturates the
  bound. The observation that entanglement entropy saturates a thermodynamic entropy bound was
  flagged as surprising and important.
- Covariant refinement of [[bekenstein-hawking-entropy|Bekenstein-Hawking]] area/entropy laws.

## Where it appears

- Original: Bousso 1999 (covariant entropy bound, light-sheets).
- As the conceptual engine of the covariant HEE proposal:
  [[0705.0016|Hubeny-Rangamani-Takayanagi 2007]].
