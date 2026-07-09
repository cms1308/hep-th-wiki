---
type: concept
title: Hyperbolic string vertices
aliases: [hyperbolic vertices, Fırat local coordinates]
tags: [string-field-theory, hyperbolic-geometry, moduli-space, weil-petersson]
prerequisites: [closed-string-field-theory]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A construction of the interaction vertices $V_{0,n}$ of
[[closed-string-field-theory|closed string field theory]] using surfaces with a
**constant-curvature hyperbolic metric** ($K=-1$) whose systole
(shortest closed geodesic) is bounded below by a fixed length $L$. The region of moduli space with
systole $\ge L$ defines the string vertex; the complementary region (systole $<L$) is filled in by
Feynman-diagram propagators. Requiring the vertices to satisfy the geometric BV master equation fixes
the threshold at the [[systolic-threshold|systolic length]] $L_*=2\,\mathrm{arcsinh}(1)$.

The decisive practical feature is that the local coordinates around each puncture are **computable in
closed form**. For the cubic vertex $V_{0,3}$ the mapping radii $\rho_j$ follow from the Fuchsian
equation on the three-punctured sphere and are given by hypergeometric functions of the border
lengths (Fırat 2021). This turns the vertices from numerically-sampled minimal-area data into
explicit analytic input.

## Motivation

Older CSFT vertices came from minimal-area metrics, known only numerically for $n=4,5$ and
impractical beyond. Hyperbolic vertices are analytically tractable and, crucially, plug into
Mirzakhani's [[weil-petersson-volumes|Weil–Petersson volume]] machinery: the
[[mirzakhani-topological-recursion|topological recursion]] then generates every $V_{0,n}$ from the
single cubic vertex $V_{0,3}$, so $V_{0,4}, V_{0,5},\dots$ never have to be constructed directly.

## Key formulas

- Systolic threshold: $L_*=2\,\mathrm{arcsinh}(1)=1.76274717\ldots$; reduced length
  $\lambda=L/(2\pi)$, conformal weight at a puncture $\Delta_j=(1+\lambda_j^2)/2$.
- Cubic vertex leading data: mapping radii $\rho_j(\lambda_j)$ from the Fuchsian/hypergeometric
  construction; the tachyon vertex $V_T=\rho_1^{-2}\rho_2^{-2}\rho_3^{-2}$.
- Fenchel–Nielsen $b$-ghost leading coefficient
  $\mathrm{BG}(L_j,L_i,L_k)=\frac{1}{2\pi\rho_j}\frac{d\rho_j}{d\lambda_j}$, with
  $\mathrm{BG}(L_*)=1.126$.

## Relations

- Belong to [[closed-string-field-theory]]; the systole bound is set by the
  [[systolic-threshold|systolic threshold]].
- Feed the [[mirzakhani-topological-recursion|topological recursion]] built on
  [[weil-petersson-volumes|Weil–Petersson volumes]], generating all $V_{0,n}$ from $V_{0,3}$.
- The recursion + Feynman-region subtraction produces the
  [[twisted-mirzakhani-kernels|twisted Mirzakhani kernels]] and hence the
  [[fvm-quadratic-integral-equation|FVM quadratic integral equation]].
- Same Weil–Petersson/Mirzakhani machinery as in [[jt-gravity]], applied to string vertices rather
  than to gravitational amplitudes.

## Where it appears

- Constant-curvature vertices with systole $\ge L$: Moosavian–Pius; Costello–Zwiebach 2019.
- Explicit cubic-vertex local coordinates from the Fuchsian equation: Fırat 2021.
- Central input to the recursive-algebraic tachyon-vacuum solution: [[2603.29926|Kim 2026]].
