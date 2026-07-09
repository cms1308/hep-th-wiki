---
type: concept
title: Trumpet geometry
aliases: [trumpet, trumpet partition function]
tags: [jt-gravity, hyperbolic-geometry]
prerequisites: [jt-gravity, schwarzian-theory]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The trumpet is the hyperbolic ($R=-2$) piece of a JT surface that connects one asymptotic
Schwarzian boundary to a closed geodesic of length $b$ in the interior. Metrically it is
$ds^2=d\sigma^2+\cosh^2\!\sigma\,d\tau^2$ with $\tau\sim\tau+b$: an infinite flaring throat
(the asymptotic boundary) narrowing to a geodesic "waist" of length $b$ at $\sigma=0$.

## Motivation

Every JT amplitude on a surface with handles is built by cutting each asymptotic boundary off along
its neighboring geodesic. The outer part is always a trumpet (fixing the
[[schwarzian-theory|Schwarzian]] boundary data), and the inner part is a bordered hyperbolic
surface whose moduli are integrated with the [[weil-petersson-volumes|Weil–Petersson measure]].
This factorization is what turns the gravitational path integral into
$Z_{g,n}=\prod_i\int b_i\,db_i\,Z^{\rm tr}_{\rm Sch}(\beta_i,b_i)\,V_{g,n}(b)$.

## Key formulas

$$Z^{\rm tr}_{\rm Sch}(\beta,b)=\frac{\gamma^{1/2}}{(2\pi)^{1/2}\beta^{1/2}}\,e^{-\gamma b^2/(2\beta)}\qquad(\gamma=\tfrac12).$$
The gluing measure $b\,db$ is the Weil–Petersson symplectic measure $\int_0^b d\tau\,db$ over the
geodesic length $b$ and the twist $\tau$ along it. The genus-zero **double trumpet** (two trumpets
glued waist-to-waist, no handle) gives
$Z_{0,2}(\beta_1,\beta_2)=\frac{\sqrt{\beta_1\beta_2}}{2\pi(\beta_1+\beta_2)}$, the cylinder that
produces the universal [[spectral-form-factor|ramp]].

## Relations

- Outer building block of every JT geometry; complements [[weil-petersson-volumes|$V_{g,n}$]].
- Its Laplace transform in $b$ links the Schwarzian to the
  [[eynard-orantin-topological-recursion|topological-recursion]] variables $z$ ($z^2=-E$).

## Where it appears

- [[1903.11115|Saad–Shenker–Stanford 2019]] — introduces the trumpet decomposition of JT surfaces
  and the double-trumpet ramp.
