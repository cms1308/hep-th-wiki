---
type: method
title: Double-scaling limit
aliases: [double scaling, double-scaled matrix model]
tags: [matrix-models, two-dimensional-gravity, jt-gravity]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

The double-scaling limit turns a finite $L\times L$ matrix integral into a continuum theory of 2d
gravity by focusing on the edge of the eigenvalue distribution while sending $L\to\infty$. It is
what makes the $1/L$ topological expansion into the genus expansion of a string, with
$e^{-S_0}$ the string coupling.

## Prerequisites

- A one-matrix ensemble $\mathcal Z=\int dH\,e^{-L\,\mathrm{Tr}V(H)}$ and its leading eigenvalue
  density $\rho_0(E)$ (spectral curve).

## How it works

Tune the potential $V$ and take $L\to\infty$ so that one edge of the eigenvalue support is pushed
away while the local density near the edge is held fixed at a finite value $e^{S_0}$. The genus
expansion parameter $1/L$ is traded for $e^{-S_0}$:
$$\langle R(z_1)\cdots R(z_n)\rangle_{\rm conn.}\simeq\sum_{g}\frac{R_{g,n}}{(e^{S_0})^{2g+n-2}} .$$
In the limit $\rho_0$ becomes non-normalizable (the "sea" is infinite) and only the edge behavior —
the [[jt-spectral-curve|spectral curve]] — survives. For [[jt-gravity|JT gravity]] the surviving
density is $\rho_0(E)\propto\sinh(2\pi\sqrt{2\gamma E})$.

## Regime of validity

- Perturbative genus expansion; the series is asymptotic, so a
  [[nonperturbative-completion-jt|nonperturbative completion]] (choice of eigenvalue contour) must
  be supplied separately.

## Canonical applications

- Original double-scaled matrix models of 2d gravity / [[minimal-string|minimal strings]]
  (Brézin–Kazakov, Douglas–Shenker, Gross–Migdal, 1990).
- [[1903.11115|Saad–Shenker–Stanford 2019]] — the ensemble dual to JT gravity is a double-scaled
  Hermitian matrix integral; the double-scaling is what matches $1/L$ to the JT genus weight
  $(e^{S_0})^\chi$.
