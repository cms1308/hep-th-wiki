---
type: topic
title: Entropic Order
aliases: [entropic order, high-temperature order, high-temperature symmetry breaking]
tags: [entropic-order, statistical-mechanics, high-temperature-order, spontaneous-symmetry-breaking, condensed-matter]
prerequisites: [spontaneous-symmetry-breaking]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

**Entropic order** is spontaneous symmetry breaking that appears — and *persists* — at arbitrarily high temperature, contrary to the textbook rule that heating destroys order. The mechanism: an ordered configuration of one set of degrees of freedom *unlocks* larger fluctuations in a second set (bosons with an unbounded local Hilbert space), so the ordered state carries the *higher* entropy and, through $F = E - TS$, wins at high $T$. The order is genuine spontaneous symmetry breaking of a real Gibbs measure — solids, ferromagnets, superfluids, topological order, and superconductors can all be arranged to survive to $T\to\infty$.

The key structural ingredient is an **infinite (unbounded) local configuration space**. This is exactly the assumption violated by the standard no-go theorems — high-$T$ disordering results and the [[heat-death-of-entanglement|"heat death of entanglement"]] separability theorem all assume finite-dimensional on-site spaces. Entropic-order models sidestep them by construction, without contradicting them.

This is the wiki's first [statistical-mechanics / condensed-matter](https://arxiv.org/list/cond-mat.stat-mech/recent) topic; it connects to hep-th through the large-$N$ QFT constructions of [[high-temperature-order-in-qft]].

## Historical development

- **1950 — physical prototype.** The [[pomeranchuk-effect|Pomeranchuk effect]]: solid $^3$He is the *higher*-temperature phase because solidifying frees nuclear-spin entropy. The paradigmatic intermediate-$T$ entropic ordering.
- **2020– — high-$T$ order in QFT.** Multicritical $O(N)$-type CFTs that break a symmetry at all temperatures (Chai, Komargodski et al.), later a local unitary $d=2$ model (Hawashin–Komargodski) — see [[high-temperature-order-in-qft]]. These showed high-$T$ order exists in UV-complete theories, but left open whether simple *local lattice* models could do it.
- **2024 — the sharpened no-go.** The [[heat-death-of-entanglement|heat death of entanglement]]: finite-dimensional local Gibbs states become fully separable above an $O(1)$ temperature. This framed the puzzle: what must a model give up to order at high $T$?
- **2025 — Entropic Order.** [[2503.22789|Han–Huang–Komargodski–Lucas–Popov 2025]] named the mechanism, gave explicit local classical and quantum lattice models (a bosonic checkerboard solid, an exactly solvable high-$T$ ferromagnet, [[entropic-topological-order|entropic topological order]]), the general [[transmutation-boson-mechanism|transmutation-boson]] construction, the large-$N$ QFT realization, and a toy [[high-temperature-entropic-superconductivity|high-$T_c$ superconductor]].
- **2025 — Minimal Models.** [[2512.07980|Huang–Komargodski–Lucas–Popov–Sulejmanpasic 2025]] reduced the effect to the [[arithmetic-ising-model|Arithmetic Ising Model]] (a Bose–Hubbard-like nearest-neighbor repulsion), established the $U/\mu > 1/2$ threshold via a controlled [[large-flavor-expansion-entropic-order|large-flavor expansion]], and showed the order survives quantum hopping.

## Key concepts

- [[transmutation-boson-mechanism]] — append unbounded bosons to each interaction term to convert temperature into an effective coupling; builds a high-$T$ ordered model from *any* ordered template.
- [[arithmetic-ising-model]] — the minimal model: Ising sites promoted to non-negative integers with nearest-neighbor repulsion.
- [[pomeranchuk-effect]] — the physical prototype.
- [[entropic-topological-order]] — high-$T$ topological order from bosons dressing a stabilizer code.
- [[high-temperature-order-in-qft]] — the large-$N$ multicritical QFT realization.

## Key results

- [[heat-death-of-entanglement]] — the finite-dimensional separability no-go theorem that entropic order evades.
- [[high-temperature-entropic-superconductivity]] — BCS coupled to critical bosons gives $g_{\rm eff}(T)$ growing with $T$ and $\Delta^2 \sim t^{-1} T^{d-1}$.
- The [[arithmetic-ising-model|AIM]] high-$T$ solid is second order and in the 2d Ising universality class, with mean-field threshold $U/\mu > 1/2$ (apparently exact as $T\to\infty$).

## Current status

The mechanism is established in explicit local classical and quantum lattice models, in continuum gases, and in large-$N$ QFT. The core requirement — an unbounded local Hilbert space — is understood, and the effect is robust to quantum kinetics. Open frontiers concern rigor (survival of order under the thermodynamic limit taken before $\beta\to0$), the exactness of thresholds at finite flavor number, and experimental realization (Rydberg-atom arrays, many-band superconductors).

## Open questions

- [[high-t-order-thermodynamic-limit]] — does high-$T$ order survive if $N\to\infty$ (or $L\to\infty$) is taken *before* $\beta\to0$?
- [[finite-k-corrections-entropic-transition]] — is the $U_c = \mu/2$ threshold at $T\to\infty$ exact at finite flavor number $k$?
- Can a real material realize entropic high-$T_c$ superconductivity, versus a mere zero-$T$ coupling enhancement?
