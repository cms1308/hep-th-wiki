---
type: question
title: Is the U_c = μ/2 threshold exact at finite flavor number?
aliases: [finite-k corrections to entropic transition, exactness of AIM threshold]
tags: [entropic-order, arithmetic-ising-model, large-flavor-expansion, open-question]
status: open
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[arithmetic-ising-model|Arithmetic Ising Model]] orders into its high-temperature checkerboard solid at $U/\mu > 1/2$ in mean field, and this threshold appears to become *exact* as $T\to\infty$. But mean field is only controlled at large flavor number $k$. Does $U_c = \mu/2$ (at $T\to\infty$) survive at finite $k$ — in particular at the physical value $k = 1$ — or does it receive corrections, possibly non-perturbative?

## Why it matters

The threshold is the sharpest quantitative prediction of the minimal entropic-order model. Its apparent exactness is tied to an emergent staggered continuous symmetry at $T\to\infty$ that forbids a mass term for the ordering mode — but that symmetry relies on the field $\phi_x$ being continuous, which strictly holds only at large $k$. Whether the protection persists at finite $k$ decides whether $U_c = \mu/2$ is an exact feature of the physical model or a large-$k$ idealization.

## Main attempts

- The [[large-flavor-expansion-entropic-order|$1/k$ expansion]] gives $\tfrac{U}{\mu} > \tfrac12 + \tfrac{\sqrt{\beta\mu}}{2\sqrt2\,\pi k}\log\tfrac{1}{\beta\mu} + \cdots$, so the correction vanishes as $\beta\to0$ at first order — evidence for exactness at $T\to\infty$.
- Monte Carlo at $k=1$ finds $U_c \approx 0.63$ at finite temperature (2d Ising universality), consistent with but not proving the $T\to\infty$ value.

## Current status

Open. The emergent continuous symmetry that would enforce exactness is only established in the large-$k$ continuum limit; its fate at finite $k$ (and possible non-perturbative corrections) is deferred to future work in [[2512.07980|Huang et al. 2025]].
