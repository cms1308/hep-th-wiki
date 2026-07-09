---
type: result
title: Supersymmetric Cardy formula (4d)
aliases: [Cardy-like limit of the superconformal index, 4d SUSY Cardy formula]
tags: [superconformal-index, cardy-formula, black-hole-entropy, supersymmetry]
status: proven
created: 2026-07-03
updated: 2026-07-03
---

Conventions: index and fugacities as on [[2308.01717|Cho-Choi-Lee-Song 2023]] —
$\mathcal{I} = \mathrm{Tr}[(-1)^F e^{-\omega_1(J_1+R/2)}e^{-\omega_2(J_2+R/2)}]$ with
$\omega_1$ shifted by $-2\pi i$ so that $(-1)^F \to e^{\pi i R}$;
$\delta \equiv \tfrac{\omega_1+\omega_2-2\pi i}{2}$, $J \equiv \tfrac{J_1+J_2}{2}$.

## Statement

In the Cardy-like limit $\omega_{1,2}\to 0$ of the 4d $\mathcal{N}=1$
[[superconformal-index|superconformal index]] (flavor fugacities off),
$$\log\mathcal{I} \;\sim\; \mathrm{Tr}R^3\,\frac{\delta^3}{6\omega_1\omega_2}
+ \mathrm{Tr}R\,\frac{\pi^2\delta}{6\omega_1\omega_2}
\;=\; \frac{8(5a-3c)}{27\,\omega_1\omega_2}\delta^3
+ \frac{8\pi^2(a-c)}{3\,\omega_1\omega_2}\delta\,,$$
equivalently $\mathrm{Re}\log\mathcal{I} \sim (3c-2a)\,
\frac{16\pi^3\,\mathrm{Im}(\omega_1\omega_2)}{27|\omega_1|^2|\omega_2|^2}$. The Legendre
transform (unrefined, $\omega_1=\omega_2$) gives the microcanonical entropy at large $J$:
$$\mathrm{Re}(S) \;=\; 2^{1/3}\,3^{1/2}\,(3c-2a)^{1/3}\,\pi\, J^{2/3} + O(J^{1/3})\,,$$
positive for any interacting SCFT by the [[hofman-maldacena-bound|Hofman-Maldacena bound]]
$\tfrac12 < a/c < \tfrac32$. This is the 4d supersymmetric analog of Cardy's 2d
high-temperature formula: universal asymptotics fixed entirely by anomaly coefficients.

## Derivation sketch

The shift $\omega_1 \to \omega_1 - 2\pi i$ turns $(-1)^F$ into $e^{\pi i R}$, obstructing
boson/fermion cancellations (the $\mathcal{N}=1$ R-charges are not integer-quantized, so
the index is not $2\pi i$-periodic). The $\omega_{1,2}\to 0$ asymptotics is then computed
either by saddle point of the matrix integral (the vanishing-gauge-holonomy saddle
dominates) or from the anomaly-based effective field theory on the Cardy background; both
give the universal $\mathrm{Tr}R^3$/$\mathrm{Tr}R$ terms above. Established across
[1810.12067](https://arxiv.org/abs/1810.12067),
[1904.03455](https://arxiv.org/abs/1904.03455),
[1904.05865](https://arxiv.org/abs/1904.05865),
[1904.10009](https://arxiv.org/abs/1904.10009),
[2104.01464](https://arxiv.org/abs/2104.01464); reviewed in
[[2308.01717|Cho-Choi-Lee-Song 2023]].

## Assumptions

4d $\mathcal{N}=1$ superconformal symmetry; Cardy limit $|\omega_{1,2}| \to 0$ (large
charges/angular momenta dominate); the vanishing-holonomy saddle dominating (established
for the theories used in [[2308.01717|Cho-Choi-Lee-Song 2023]]).

## Status

Proven (derived by multiple independent methods and cross-checked).

## Implications

- For holographic SCFTs it reproduces the Bekenstein-Hawking entropy of large BPS black
  holes in $AdS_5$ (Gutowski-Reall and generalizations) — the index does count black hole
  microstates.
- The combination $3c-2a$ — not $c$ — is the universal quantity controlling
  high-energy/large-charge density of states, which motivates replacing $c \to 3c-2a$ in
  the AdS WGC bound ([[modified-ads-wgc-3c-2a]]).
- A 4d analog of the modularity used to prove the 2d WGC may act through this formula
  ([[higher-dimensional-modularity]]).
