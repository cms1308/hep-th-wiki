---
type: topic
title: Jackiw–Teitelboim (JT) gravity
aliases: [JT gravity, Jackiw-Teitelboim gravity, 2d dilaton gravity]
tags: [jt-gravity, two-dimensional-gravity, holography, quantum-chaos, matrix-models]
prerequisites: [anti-de-sitter-space]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

Jackiw–Teitelboim (JT) gravity is two-dimensional dilaton gravity with a linear dilaton
potential: a metric $g$ and a scalar $\phi$ with action
$$I=-\frac{S_0}{2\pi}\Big[\tfrac12\!\int\!\sqrt g\,R+\int\!\sqrt h\,K\Big]-\Big[\tfrac12\!\int\!\sqrt g\,\phi(R+2)+\int\!\sqrt h\,\phi(K-1)\Big].$$
Integrating out $\phi$ forces $R=-2$, so the bulk is locally rigid hyperbolic space ($AdS_2$);
all dynamics lives on the wiggling boundary and is governed by the
[[schwarzian-theory|Schwarzian derivative]]. The first bracket is topological, equal to
$S_0\,\chi$, so surfaces of Euler character $\chi=2-2g-n$ are weighted by $(e^{S_0})^\chi$ and
$e^{-S_0}$ plays the role of a string coupling.

JT gravity is the simplest model in which a gravitational path integral can be computed *exactly,
to all orders in topology*. It is the low-energy dual of the near-extremal / near-$AdS_2$ throat
of higher-dimensional black holes and the effective bulk description of the SYK model. Its
signature result — [[1903.11115|Saad–Shenker–Stanford 2019]] — is that the full genus expansion
equals a double-scaled Hermitian [[jt-gravity-matrix-integral-duality|matrix integral]], making
JT gravity the cleanest laboratory for quantum chaos, wormholes, ensemble averaging, and the
black-hole information problem.

## Historical development

- **1983–1985** — Teitelboim and Jackiw introduce 2d dilaton gravity as a soluble model of
  gravity with a nontrivial equation of motion.
- **2014–2016** — near-$AdS_2$/near-$CFT_1$ revival: Almheiri–Polchinski; the boundary dynamics
  is identified as the [[schwarzian-theory|Schwarzian theory]] and connected to the low-energy
  limit of SYK (Maldacena–Stanford–Yang; Engelsöy–Mertens–Verlinde; Jensen).
- **2018** — the SYK/JT [[spectral-form-factor|spectral form factor]] "ramp" is traced to a
  cylinder ("double cone") geometry (Saad–Shenker–Stanford).
- **2019** — [[1903.11115|Saad–Shenker–Stanford]] show the JT genus expansion is a
  [[jt-gravity-matrix-integral-duality|matrix integral]] with
  [[jt-spectral-curve|spectral curve]] $y=\tfrac{\sin 2\pi z}{4\pi}$, via
  [[weil-petersson-volumes|Weil–Petersson volumes]] and
  [[eynard-orantin-topological-recursion|topological recursion]]; the plateau and large-genus
  volume asymptotics follow from nonperturbative (D-brane–type) effects.

## Key concepts

- [[schwarzian-theory]] — the boundary theory; one-loop-exact disk and trumpet partition functions.
- [[trumpet-geometry]] — hyperbolic piece joining a Schwarzian boundary to a length-$b$ geodesic.
- [[weil-petersson-volumes]] — moduli-space volumes $V_{g,n}(b)$; the nontrivial part of $Z_{g,n}$.
- [[jt-spectral-curve]] — $y=\tfrac{\sin 2\pi z}{4\pi}$, $\rho_0\propto\sinh(2\pi\sqrt{2\gamma E})$.
- [[spectral-form-factor]] — ramp (cylinder) and plateau (nonperturbative), the diagnostics of chaos.
- [[minimal-string]] — JT as the $p\to\infty$ limit of the $(2,p)$ minimal string.

## Key results

- [[jt-gravity-matrix-integral-duality]] — the genus expansion of JT gravity equals a
  double-scaled Hermitian matrix integral.
- [[large-genus-weil-petersson-asymptotics]] — resurgence prediction for $V_{g,0}$, $V_{g,1}(b)$.

## Current status

The matrix-integral duality is established for orientable JT gravity; Stanford–Witten extended it
to the other Altland–Zirnbauer symmetry classes (time reversal, fermions, unorientable surfaces).
JT gravity is now the standard testing ground for the
[[factorization-vs-wormholes|factorization puzzle]], replica wormholes and the Page curve, and ensemble-averaged holography. The
[[nonperturbative-completion-jt|nonperturbative completion]] is non-unique and (in the bosonic
orientable model) unstable, which remains an active question.

## Open questions

- [[factorization-vs-wormholes]] — connected geometries imply an ensemble; what happens for a
  single, fixed boundary theory, and how is factorization restored?
- [[nonperturbative-completion-jt]] — is there a canonical, stable definition, and can the
  eigenvalue/matrix constituents be seen from the bulk?
