---
type: concept
title: Spectral form factor (ramp and plateau)
aliases: [spectral form factor, SFF, ramp, plateau, slope-ramp-plateau]
tags: [quantum-chaos, jt-gravity, random-matrix-theory, spectral-form-factor]
prerequisites: [jt-gravity]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The spectral form factor is the analytically continued double partition function
$$\big|Z(\beta+iT)\big|^2=\langle Z(\beta+iT)\,Z(\beta-iT)\rangle=\sum_{m,n}e^{-\beta(E_m+E_n)}e^{iT(E_m-E_n)},$$
a diagnostic of energy-level statistics as a function of time $T$. In chaotic (random-matrix)
systems it shows a universal three-part shape: an early-time **slope** (decay), an intermediate
**ramp** rising linearly in $T$, and a late-time **plateau** at height $\sim Z(2\beta)$ reached at
the Heisenberg time $T\sim e^{S}$.

## Motivation

The ramp and plateau are the sharp signatures that a system's spectrum has random-matrix
correlations (level repulsion, rigidity). Seeing them emerge from a *gravitational* path integral
is direct evidence that [[jt-gravity|JT gravity]] computes an ensemble average and is governed by
random-matrix theory.

## Key formulas

- **Ramp from the cylinder.** The connected genus-zero double-trumpet
  $Z_{0,2}(\beta_1,\beta_2)=\frac{\sqrt{\beta_1\beta_2}}{2\pi(\beta_1+\beta_2)}$ continues under
  $\beta_{1,2}\to\beta\pm iT$ to $\frac{T}{4\pi\beta}$ — the linear ramp. See
  [[trumpet-geometry|double trumpet]].
- **Plateau from nonperturbative oscillations.** The sine-kernel pair correlation
  $\langle\rho(E)\rho(E')\rangle\supset\frac{\cos\!\big(2\pi\!\int_E^{E'}\!\rho_0^{\rm total}\big)}{2\pi^2(E-E')^2}$
  — a nonperturbative (D-brane / eigenvalue-discreteness) effect — flattens the ramp into the
  plateau at $T\sim e^{S_0}$.

## Relations

- The ramp is a [[factorization-vs-wormholes|wormhole]] (connected two-boundary) contribution.
- The plateau needs the [[nonperturbative-completion-jt|nonperturbative completion]] of the JT
  matrix integral.
- Established for JT by the [[jt-gravity-matrix-integral-duality|matrix-integral duality]].

## Where it appears

- [[1903.11115|Saad–Shenker–Stanford 2019]] — cylinder ramp and nonperturbative plateau in JT
  gravity.
