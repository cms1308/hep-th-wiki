---
type: concept
title: $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ Orbifold Geometry
aliases: ["AdS3 Z_k orbifold", "conical defect geometry", "spectrally flowed orbifold saddle"]
tags: [ads3-cft2, conical-defect, giant-graviton-expansion, supergravity]
prerequisites: [ads3-cft2-correspondence, anti-de-sitter-space]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ orbifold is the quotient of global $\mathrm{AdS}_3\times\mathrm{S}^3$ by a $\mathbb{Z}_k$ acting simultaneously on the AdS$_3$ angular circle and an $\mathrm{S}^3$ Hopf fiber. Reduced to 3d it is an asymptotically-AdS$_3$ conical defect with deficit angle $2\pi(1-1/k)$, carrying $SU(2)\times SU(2)$ R-symmetry gauge fields. These geometries (conical defects / Maldacena–Maoz / Lunin–Mathur type) are BPS saddles of the D1–D5 system; their $k=1$ case is global AdS$_3$.

## Motivation

In the [[ads3-giant-graviton-expansion]] these orbifolds are the bulk saddles whose one-loop supersymmetric partition functions $\widehat Z_k^{\,\mu}$ sum up to the finite-$N$ chiral-primary spectrum. They are the AdS$_3$ analog of giant-graviton branes: their BPS fluctuations are holographically dual to the [[finite-n-null-states]] that must be subtracted from the KK spectrum.

## Key formulas

Classical BPS ground-state charge: $\quad h=\bar h=j=\bar j=\tfrac N2\left(1-\tfrac1k\right)$.

One-loop "staggered" charge (K3): $\quad h=\bar h=j=\bar j=\tfrac N2\left(1-\tfrac1k\right)+\tfrac14(k-1)$,
which resolves the $k\to\infty$ accumulation at $E=N$ and pushes orbifolds with $k\gtrsim\sqrt{2N}$ past the chiral-primary black-hole charge.

Worldsheet realization: fractional spectral flow $w=n/k$ of the [[tensionless-string-ads3|$\mathfrak{psu}(1,1|2)_1$ string]] reproduces the $\mathbb{Z}_k$-twisted BPS spectrum.

## Relations

- Bulk saddles of the [[ads3-giant-graviton-expansion]]; enter with alternating signs via [[negative-modes-contour-rotation]].
- Spectral-flow images $\mu\in\{(0,0),(2,0),(0,2),(2,2)\}$ are the asymmetric orbifolds selected by the [[stokes-sectors-partition-function|Stokes sectors]].
- Their fluctuations are dual to [[finite-n-null-states]].

## Where it appears

- Constructed as conical-defect / fuzzball geometries (Martinec; Maldacena–Maoz; Balasubramanian et al; Lunin–Mathur); tensionless worldsheet spectra by Gaberdiel et al (2023).
- Assembled into the finite-$N$ bulk sum in [[2511.00636|Lee-Li 2025]].
