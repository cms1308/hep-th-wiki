---
type: result
title: Heat Death of Entanglement
aliases: [heat death of entanglement, high-temperature separability theorem]
tags: [entropic-order, quantum-information, entanglement, no-go-theorem, statistical-mechanics]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

For a *local, finite-dimensional* quantum lattice system, the Gibbs state $\rho_\beta \propto e^{-\beta H}$ becomes **fully separable** (unentangled) above an $O(1)$ temperature: there is a $\beta_* = O(1)$ such that for all $\beta < \beta_*$

$$\rho_\beta = \sum_a p_a\, |\psi_a\rangle\langle\psi_a|,$$

a convex mixture of product states. All long-range entanglement — including topological order — is destroyed at high temperature. (Bakshi et al. 2024; related finite-$T$ disordering results of Kliesch et al. 2014.)

## Derivation sketch

The argument bounds the thermal state by a high-temperature (small-$\beta$) expansion around the maximally mixed state and shows the resulting operator admits an explicit separable decomposition once $\beta$ is small enough, with $\beta_*$ set by the local interaction strength and coordination number. The finite on-site dimension is what makes the expansion converge to a separable form.

## Assumptions

- **Finite local Hilbert-space dimension** (finite $d$ per site) — the load-bearing assumption.
- Local (bounded-range, bounded-strength) interactions.

## Status

Proven, within its stated finite-dimensional assumptions. It is *not* violated by [[entropic-order]] models — those use an **unbounded** local Hilbert space ($n_x \in \{0,1,2,\dots\}$), so the theorem simply does not apply. The [[entropic-topological-order|entropic topological order]] construction is an explicit high-$T$-entangled Gibbs state that sits just outside the theorem's hypotheses.

## Implications

- Frames the central puzzle the entropic-order program answers: to keep order (or entanglement) at high $T$, a local model *must* give up finite on-site dimension.
- Identifies the infinite local Hilbert space as the necessary structural ingredient for high-temperature long-range entanglement.

## Where it appears

- Invoked as the sharpened no-go theorem in [[2503.22789|Han et al. 2025]], and evaded by the [[transmutation-boson-mechanism]] / [[entropic-topological-order]] constructions there.
