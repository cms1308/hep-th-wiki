---
type: concept
title: Negative Modes and Contour Rotation
aliases: ["negative-mode contour rotation", "alternating signs from negative modes", "Wick-rotated negative modes"]
tags: [ads3-cft2, giant-graviton-expansion, path-integral, bps]
prerequisites: [ads3-z-k-orbifold-geometry, ads3-giant-graviton-expansion]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

When a BPS saddle is quantized at one loop, some fluctuation modes have negative conformal dimension and charge — "negative modes." Their Gaussian integrals converge only along a rotated (Wick-rotated) contour, and the analytic continuation flips the sign of the corresponding factor in the one-loop determinant. Summed over a $\mathbb{Z}_k$-twisted sector this yields an overall factor $(-1)^{k-1}$, so successive orbifold saddles in the [[ads3-giant-graviton-expansion]] contribute with **alternating signs**.

## Motivation

The alternating signs are the mechanism behind the [[stringy-exclusion-principle]]: without them the sum over saddles would only add states, never remove them. The negative modes are the AdS$_3$ counterpart of the negative modes of wrapped giant-graviton branes in the AdS$_5$ [[giant-graviton-expansion]], and their contour rotation is what encodes the subtraction of [[finite-n-null-states|finite-$N$ null states]].

## Key formulas

Sign-flip identity (K3 twisted-sector negative modes):
$$\frac{1}{\prod_{n=1}^{k-1}\left(1-y^{\frac nk-1}\bar y^{\frac nk-1}\right)}=\frac{(-1)^{k-1}\,y^{\frac{k-1}{2}}\bar y^{\frac{k-1}{2}}}{\prod_{n=1}^{k-1}\left(1-y^{1-\frac nk}\bar y^{1-\frac nk}\right)}.$$
The factor $(-1)^{k-1}$ makes the $k\ge2$ orbifold saddles subtract rather than add.

## Relations

- Supplies the alternating signs in the [[ads3-giant-graviton-expansion]] and the [[grand-canonical-residue-expansion]].
- Realizes, in AdS$_3$, the negative-mode/contour-rotation logic [[ji-hoon-lee|Lee]] developed for giant gravitons in the [[giant-graviton-expansion]].
- Enables the subtraction of [[finite-n-null-states]].

## Where it appears

- Applied to the $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ orbifold saddles in [[2511.00636|Lee-Li 2025]].
