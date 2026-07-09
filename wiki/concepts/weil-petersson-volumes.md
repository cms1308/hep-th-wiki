---
type: concept
title: Weil–Petersson volumes
aliases: [Weil-Petersson volume, WP volume, moduli-space volume]
tags: [jt-gravity, hyperbolic-geometry, moduli-space, matrix-models]
prerequisites: [jt-gravity]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

$V_{g,n}(b_1,\dots,b_n)$ is the volume, in the Weil–Petersson symplectic measure, of the moduli
space $\mathcal M_{g,n}$ of genus-$g$ hyperbolic Riemann surfaces with $n$ geodesic boundaries of
fixed lengths $b_1,\dots,b_n$. In Fenchel–Nielsen coordinates (geodesic lengths $\ell_a$ and twists
$\tau_a$ of a pants decomposition) the symplectic form is $\Omega=\sum_a d\ell_a\wedge d\tau_a$
(Wolpert), and $V_{g,n}=\int_{\mathcal M_{g,n}}\frac{\Omega^{3g-3+n}}{(3g-3+n)!}$.

## Motivation

In [[jt-gravity|JT gravity]] the bulk metric is rigidly hyperbolic, so the entire path integral
over a genus-$g$ surface reduces to an integral over its moduli — and that integral is exactly the
Weil–Petersson volume. $V_{g,n}$ is therefore the nontrivial, topology-dependent factor in every
JT amplitude, with the [[trumpet-geometry|trumpets]] supplying the boundary dressing.

## Key formulas

Each $V_{g,n}$ is a polynomial in the $b_i^2$; e.g. $V_{1,1}(b)=\frac{1}{48}(b^2+4\pi^2)$,
$V_{0,3}=1$. **Mirzakhani's recursion** computes them recursively by integrating over how a pair of
pants is glued on. After the Laplace transform
$W_{g,n}(z)=\prod_i\int_0^\infty b_i\,db_i\,e^{-b_iz_i}V_{g,n}$, Mirzakhani's recursion becomes the
[[eynard-orantin-topological-recursion|Eynard–Orantin topological recursion]] for the spectral
curve $y=\frac{\sin 2\pi z}{4\pi}$ (Eynard–Orantin theorem) — the statement that JT volumes are
matrix-model correlators. Their [[large-genus-weil-petersson-asymptotics|large-genus growth]] is
factorial, $\sim(4\pi^2)^{2g}\Gamma(2g-\tfrac52)$.

## Relations

- Moduli-space geometry (Wolpert's form) → [[jt-gravity]] amplitude via
  $Z_{g,n}=\prod_i\int b_i\,db_i\,Z^{\rm tr}_{\rm Sch}\,V_{g,n}$.
- Computed by [[mirzakhani-topological-recursion|Mirzakhani's recursion]] ≡
  [[eynard-orantin-topological-recursion|topological recursion]].
- Large-genus behavior: [[large-genus-weil-petersson-asymptotics]].

## Where it appears

- [[1903.11115|Saad–Shenker–Stanford 2019]] — identifies $V_{g,n}$ as the genus-$g$ integrand of
  JT gravity and uses Mirzakhani ⇔ topological recursion to establish the matrix-integral duality.
- Same machinery underlies [[hyperbolic-string-vertices]] in [[closed-string-field-theory]], where
  the [[mirzakhani-topological-recursion|recursion]] generates all string vertices $V_{0,n}$ from
  $V_{0,3}$ ([[2603.29926|Kim 2026]]).
