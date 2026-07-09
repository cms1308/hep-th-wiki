---
type: question
title: Does entropic order survive the thermodynamic limit taken before β→0?
aliases: [order of limits in entropic order]
tags: [entropic-order, statistical-mechanics, open-question]
status: open
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[entropic-order]] constructions demonstrate high-temperature order, but the order in which two limits are taken matters: the thermodynamic limit (system size $L\to\infty$, or number of fields $N\to\infty$) and the high-temperature limit ($\beta \to 0$). Does high-$T$ order survive when the **thermodynamic limit is taken first**, before $\beta \to 0$?

## Why it matters

A genuine thermodynamic phase requires order that survives $L\to\infty$ at fixed (high) temperature, not merely order in a $\beta\to0$ limit taken at finite size or finite $N$. If the two limits do not commute, "high-$T$ order" could be an artifact of the limit ordering rather than a true phase. Settling this is what separates a rigorous phase from a formal construction.

## Main attempts

- [[2503.22789|Han et al. 2025]] conjecture the order *does* survive whenever the template Hamiltonian $\bar H$ is not infinitesimally close to a transition, but give no proof.
- The [[2512.07980|Minimal Models paper]] supplies Monte Carlo evidence at finite size and a [[large-flavor-expansion-entropic-order|large-flavor expansion]] controlling the $N=k\to\infty$ direction, but the rigorous order-of-limits statement is not established.

## Current status

Open. Numerically and within controlled expansions the order is robust, but a rigorous proof that the thermodynamic limit taken before $\beta\to0$ preserves the ordered phase is not available. Related: the exactness of the $U_c = \mu/2$ threshold at finite flavor number — see [[finite-k-corrections-entropic-transition]].
