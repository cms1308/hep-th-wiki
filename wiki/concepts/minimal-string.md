---
type: concept
title: Minimal string
aliases: [(2,p) minimal string, minimal string theory, minimal model gravity]
tags: [two-dimensional-gravity, matrix-models, liouville, jt-gravity]
prerequisites: [jt-gravity]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The minimal string is 2d gravity built from a $(2,p)$ minimal-model matter CFT coupled to Liouville
theory, equivalently a double-scaled one-matrix model. It is one of the oldest exactly solvable
models of noncritical string theory: its all-genus amplitudes are computed by matrix-model loop
equations, and its D-branes are the ZZ and FZZT branes of Liouville theory.

## Motivation

It provides the historical template for "gravity = matrix integral," and it contains
[[jt-gravity|JT gravity]] as a limit: the $(2,p)$ minimal-string density of states
$$\rho_0(E)\propto\sinh\!\Big[\tfrac p2\,\mathrm{arccosh}\!\big(1+E/\kappa\big)\Big]$$
tends to $\sinh(2\pi\sqrt{E_{\rm JT}})$ as $p\to\infty$ with $E=\frac{2\pi}{p}E_{\rm JT}$ held fixed.
Because the two matrix models then agree, so do all their genus amplitudes — JT gravity is the
$p\to\infty$ minimal string.

## Key formulas

- Minimal-string spectral curve $y\propto\sin\!\big(p\,\mathrm{arccos}(\cdots)\big)$, degenerating
  to the JT curve $y=\frac{\sin 2\pi z}{4\pi}$ as $p\to\infty$. See [[jt-spectral-curve]].
- Nonperturbative effects organized by ZZ branes (one-eigenvalue instantons) and FZZT branes
  ($\det(E-H)$ insertions).

## Relations

- $p\to\infty$ limit gives [[jt-gravity]] (Saad–Stanford–Seiberg line of work).
- Same [[eynard-orantin-topological-recursion|topological-recursion]] machinery; ZZ/FZZT branes
  reappear in JT's [[nonperturbative-completion-jt|nonperturbative sector]].

## Where it appears

- [[1903.11115|Saad–Shenker–Stanford 2019]] — identifies JT gravity as the $p\to\infty$ $(2,p)$
  minimal string and imports its brane technology.
