---
type: concept
title: Arithmetic Ising Model
aliases: [AIM, arithmetic Ising model, quantum arithmetic Ising model, qAIM]
tags: [entropic-order, statistical-mechanics, lattice-model, bose-hubbard, ising]
prerequisites: [entropic-order]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The **Arithmetic Ising Model (AIM)** is the Ising model with each spin replaced by a *non-negative integer* $n_x \in \{0,1,2,\dots\}$ and only a nearest-neighbor repulsion:

$$H(n_x) = \mu\sum_x n_x + U\sum_{\langle x,y\rangle} n_x n_y, \qquad U,\mu \ge 0 .$$

Its ground state is the empty lattice ($n_x = 0$) — a disordered gas at low $T$. But at *high* temperature it spontaneously breaks sublattice translation symmetry into a **checkerboard "solid"** with $\langle n_x\rangle \sim T$ on one sublattice and $\sim 0$ on the other. This is the minimal realization of [[entropic-order|entropic order]]: unlike the [[transmutation-boson-mechanism|transmutation-boson construction]], no contrived $e^{\bar H_S}$ dressing is needed — the bare quadratic repulsion of Bose–Hubbard / Rydberg-atom type suffices.

## Motivation

Occupying only one sublattice lets those sites hold large occupations (entropy $\sim \log T$ each) while the interaction energy stays finite; spreading occupation over both sublattices costs interaction energy that caps the accessible occupations. At high $T$ the entropic gain of the ordered (checkerboard) arrangement wins.

## Key formulas

- **Ordering threshold (mean field, apparently exact as $T\to\infty$):**
$$U/\mu > 1/2 .$$
- **Colored (large-flavor) partition function:** with $k$ species per site and $U\to U/k$,
$$Z_k = \sum_{\{n_x\}} e^{-\beta H_1(n_x)} \prod_x \binom{n_x + k - 1}{k-1}, \qquad \bar\rho = \sqrt{T/4U}.$$
- **$1/k$-corrected transition line:** $\ \dfrac{U}{\mu} > \dfrac12 + \dfrac{\sqrt{\beta\mu}}{2\sqrt2\,\pi k}\log\dfrac{1}{\beta\mu} + \cdots$ (so $U=\mu/2$ survives to first order as $T\to\infty$).
- **Order parameter / susceptibility:** $O = \tfrac{1}{2L^2}(\sum_{x\in A} n_x - \sum_{x\in B} n_x)$, $\chi = L^2(\langle O^2\rangle - \langle O\rangle^2)$; Monte Carlo collapse gives 2d Ising exponents $\nu = 1$, $\gamma = 7/4$, $U_c \approx 0.63$ at $k=1$.
- **Quantum AIM (qAIM):** add hopping $-t\sum_{\langle x,y\rangle}(b_x^\dagger b_y + \text{h.c.})$; the boson bands $E_k^\pm = \mu + \sigma \pm \sqrt{\eta^2 + \varepsilon_k^2}$, $\varepsilon_k = -2t(\cos k_x + \cos k_y)$, retain a solid ($\eta\ne0$) for $U > \mu/2$ — order survives quantum kinetics.

## Relations

- Minimal model of the [[entropic-order]] program; a cleaner realization than the [[transmutation-boson-mechanism]].
- Analyzed with the [[large-flavor-expansion-entropic-order|large-flavor ($1/k$) expansion]], which makes mean-field theory exact as $k\to\infty$.
- The $U\to\infty$ limit maps to Baxter's exactly solvable hardcore square-lattice gas ($T_c \approx 4.27\,\mu$).
- Exhibits an [[entropic-order|emergent staggered continuous symmetry]] at $T\to\infty$ (in the large-$k$ continuum limit) that protects $U_c = \mu/2$ and gives a light $(\pi,\pi)$ mode with an anomalously large high-$T$ correlation length.

## Where it appears

- Introduced and analyzed in [[2512.07980|Huang et al. 2025]] (Minimal Models of Entropic Order) — mean field, $1/k$ expansion, Monte Carlo, quantum version, and continuum-gas analogues.
- Descends from the checkerboard bosonic-lattice-gas solid ($H = U\sum n_u^2 n_v^2 + \sum_v n_v$) of [[2503.22789|Han et al. 2025]].
