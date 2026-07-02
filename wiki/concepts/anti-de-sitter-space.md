---
type: concept
title: Anti-de Sitter space
aliases: [AdS, AdS space]
tags: [geometry, general-relativity, holography]
prerequisites: [general-relativity]
created: 2026-07-03
updated: 2026-07-03
---

## Definition

Maximally symmetric spacetime of constant negative curvature. $AdS_{p+2}$ is the hyperboloid

$$-X_{-1}^2 - X_0^2 + \sum_{i=1}^{p+1} X_i^2 = -R^2$$

in $\mathbb{R}^{2,p+1}$, with isometry group $SO(2,p+1)$ — the same as the conformal group of
$(p{+}1)$-dimensional Minkowski space, the group-theoretic seed of [[ads-cft-correspondence]].

## Motivation

Arises as the near-horizon geometry of extremal black branes ([[near-horizon-limit]]) and as
the natural home of holography: gravity in AdS is dual to a CFT on its conformal boundary.

## Key formulas

Poincaré patch (horospheric coordinates), covering the region $U>0$:
$$ds^2 = \frac{U^2}{R^2}\,dx_{||}^2 + R^2\,\frac{dU^2}{U^2}$$
The radial coordinate $U$ acts as field-theory energy scale
([[holographic-radial-coordinate]]). Global coordinates cover the full hyperboloid; the
boundary is at $U\to\infty$ (Poincaré) and light reaches it in finite coordinate time, so AdS
is not globally hyperbolic — boundary conditions matter ([[ads-boundary-dictionary]]).

## Relations

Parent: maximally symmetric spaces (with dS, Minkowski). Appears in
[[ads-cft-correspondence]] via $AdS_5\times S^5$, $AdS_7\times S^4$, $AdS_4\times S^7$,
$AdS_3\times S^3$. Black holes in $AdS_3$: [[btz-black-hole]].

## Where it appears

[[hep-th-9711200|Maldacena 1997]] (near-horizon geometries, appendix on coordinates).
