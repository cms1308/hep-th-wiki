---
type: concept
title: Einstein cylinder
aliases: [Einstein static universe, Lorentzian cylinder]
tags: [conformal-geometry, ads-cft, celestial-holography]
created: 2026-07-06
updated: 2026-07-06
---

## Definition

The Lorentzian cylinder EC$^4=S^3\times\mathbb R$ with metric
$$ds^2_{EC_4}=-dt^2+d\theta^2+\sin^2\theta\,(d\psi^2+\sin^2\psi\,d\phi^2),$$
the shared conformal completion of 4d Minkowski space and AdS$_4$: both embed with Weyl
factors $\Omega_{M^4}=(\cos t-\cos\theta)^{-1}$ and
$\Omega_{AdS_4}=(\sin\theta\cos\psi)^{-1}$ ([[2601.00096|Sheta et al. 2025]] conventions,
unit radius). One dimension down, EC$^3=S^2\times\mathbb R$ is the conformal frame of a
CFT$_3$ — the boundary of global AdS$_4$ — where every null geodesic runs from a point
$x_i$ to its antipode $x_f$, and the sphere's worth of such geodesics $S^2_{x_i}$ forms a
null Cauchy surface ([[2603.26459|Strominger–Wei 2026]]).

## Motivation

Because $M^4$ and AdS$_4$ are conformal to (portions of) the *same* cylinder, conformally
invariant structures can be transported between them. With $i^0$ chosen to lie *in*
$\partial\mathrm{AdS}_4$, a one-parameter family of null generators of $\mathscr I^+$ lies
simultaneously in $\mathscr I^+$ and $\partial\mathrm{AdS}_4$, running from $i^0$ to its
antipode; the common subgroup preserved by both embeddings is $ISO(2,1)\times D$. This
"judicious" embedding is what maps flat-space soft operators to boundary
[[light-ray-operators]] ([[2601.00096|Sheta et al. 2025]]).

## Key formulas

- The antipodal map $A(t,\theta,\hat x)=(t+\pi,\pi-\theta,-\hat x)$ is the $\mathbb Z_2$
  center of $SO(4,2)$.
- EC$^3$ in null coordinates: $ds^2=-4d\tau^+d\tau^-+\sin^2(\tau^+-\tau^-)\,d\phi^2$,
  $\tau^\pm=(\tau\pm\theta)/2$.

## Relations

[[anti-de-sitter-space]] (global AdS$_4$ conformal frame) · [[null-infinity]] (the
Minkowski $\mathscr I^\pm$ are null cones in EC$^4$) · [[light-ray-operators]] (antipodal
null geodesics are the integration contours).

## Where it appears

[[2601.00096|Sheta–Strominger–Tropper–Wei 2025]] · [[2603.26459|Strominger–Wei 2026]].
