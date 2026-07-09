---
type: concept
title: Schwarzian theory
aliases: [Schwarzian, Schwarzian action, Schwarzian derivative theory]
tags: [jt-gravity, near-ads2, syk, quantum-chaos]
prerequisites: [jt-gravity]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The Schwarzian theory is the 1d boundary dynamics of [[jt-gravity|JT gravity]]: a path integral
over reparametrizations $f(u)$ of the boundary time circle, weighted by the Schwarzian derivative
$$I_{\rm Sch}=-\gamma\int du\,\{f,u\},\qquad \{f,u\}=\frac{f'''}{f'}-\frac32\Big(\frac{f''}{f'}\Big)^2 .$$
It arises because integrating out the dilaton pins the bulk to rigid hyperbolic space, leaving only
the wiggle of the boundary curve as a physical degree of freedom. It is also the universal
low-energy (infrared) limit of the SYK model.

## Motivation

Near-extremal black holes develop a long, nearly-$AdS_2$ throat whose soft mode is exactly this
reparametrization mode; the Schwarzian captures the leading gravitational back-reaction and the
maximal-chaos Lyapunov behavior. It is one of the very few interacting quantum-mechanical theories
that is *one-loop exact*, which is what makes
the [[jt-gravity-matrix-integral-duality|JT/matrix duality]] computable.

## Key formulas

Disk and [[trumpet-geometry|trumpet]] partition functions (with $\gamma=\tfrac12$):
$$Z^{\rm disk}_{\rm Sch}(\beta)=\frac{\gamma^{3/2}\,e^{2\pi^2\gamma/\beta}}{(2\pi)^{1/2}\beta^{3/2}},
\qquad Z^{\rm tr}_{\rm Sch}(\beta,b)=\frac{\gamma^{1/2}\,e^{-\gamma b^2/(2\beta)}}{(2\pi)^{1/2}\beta^{1/2}}.$$
The disk gives the genus-zero density of states $\rho_0(E)=\frac{\gamma}{2\pi^2}\sinh(2\pi\sqrt{2\gamma E})$
— the input to the [[jt-spectral-curve|JT spectral curve]]. The trumpet is what glues an asymptotic
boundary of renormalized length $\beta$ to a geodesic of length $b$.

## Relations

- Boundary dual of [[jt-gravity]]; its disk fixes the spectral curve.
- Its one-loop-exact structure feeds each factor $Z^{\rm tr}_{\rm Sch}$ in
  $Z_{g,n}=\prod_i\int b_i\,db_i\,Z^{\rm tr}_{\rm Sch}\,V_{g,n}$.
- Infrared limit of SYK.

## Where it appears

- [[1903.11115|Saad–Shenker–Stanford 2019]] — disk and trumpet partition functions as the
  boundary building blocks of the genus expansion.
