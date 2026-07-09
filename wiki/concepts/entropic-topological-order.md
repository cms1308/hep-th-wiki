---
type: concept
title: Entropic Topological Order
aliases: [entropic topological order, high-temperature topological order]
tags: [entropic-order, topological-order, quantum-information, stabilizer-code]
prerequisites: [entropic-order]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

**Entropic topological order** is topological order in a Gibbs state that persists to *arbitrarily high* temperature, obtained by dressing a CSS / stabilizer code (e.g. the four-dimensional toric code) with commuting [[transmutation-boson-mechanism|transmutation bosons]]. The qubit reduced density matrix of the resulting thermal state remains topologically ordered as $\beta \to 0$ — a direct counterexample to the finite-dimensional [[heat-death-of-entanglement|"heat death of entanglement"]] theorem, which forbids any long-range entanglement in a local finite-dimensional system above an $O(1)$ temperature.

## Motivation

Topological order is a form of long-range entanglement. The heat-death theorem shows it cannot survive high $T$ if the local Hilbert space is finite-dimensional. Coupling the code's stabilizers to unbounded bosons supplies the infinite local Hilbert space needed to evade that theorem: the bosons carry the entropy, so the topologically ordered configuration is entropically favored at high $T$ while the code degrees of freedom stay pinned in the code space.

## Key formulas

- Built on a CSS/stabilizer Hamiltonian $H_{\rm code} = -\sum_a S_a$ (commuting stabilizers $S_a$) dressed as $H = \sum_a e^{S_a} n_a$ with $n_a \in \{0,1,2,\dots\}$, the [[transmutation-boson-mechanism|transmutation-boson]] pattern. Because the stabilizers commute, the boson dressing preserves exact solvability, and the reduced state on the qubits equals the code's ground-space projector at all $T$.

## Relations

- A special case of the [[transmutation-boson-mechanism]] applied to a stabilizer code, within the [[entropic-order]] program.
- The counterexample partner of [[heat-death-of-entanglement]]: the theorem holds for finite-dimensional systems; this construction adds an infinite local space and evades it.
- Uses that tracing out cannot *create* topological order and finite-depth channels cannot reproduce it — the standard certificates of genuine topological order.

## Where it appears

- Introduced in [[2503.22789|Han et al. 2025]] (Entropic Order), building on the finite-$T$ topological order of the four-dimensional toric code (Alicki et al. 2008).
