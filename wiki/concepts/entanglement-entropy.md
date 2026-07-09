---
type: concept
title: Entanglement entropy
aliases: [entanglement entropy, von Neumann entropy, reduced density matrix, EE]
tags: [quantum-information, entanglement, conformal-field-theory, holography]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

For a quantum system in a state $|\Psi\rangle$ divided into a region $A$ and its complement
$B$, the **entanglement entropy** of $A$ is the von Neumann entropy of the reduced density
matrix $\rho_A=\mathrm{tr}_B\,|\Psi\rangle\langle\Psi|$:
$$S_A=-\mathrm{tr}_A\,\rho_A\log\rho_A.$$
It measures how entangled $A$ is with $B$. For a pure global state $S_A=S_B$; at finite
temperature (mixed global state) this equality fails and $S_A$ picks up the thermal entropy.

## Motivation

It is an order-parameter-free diagnostic of quantum correlations, sensitive to critical
points, topological order, and the effective number of degrees of freedom. In holography it
becomes geometric: the [[ryu-takayanagi-formula|Ryu-Takayanagi formula]] computes $S_A$ from
the area of a bulk [[extremal-surface|minimal surface]], the entry point to the "entanglement
builds geometry" program.

## Key formulas

- **Replica trick:** $S_A=-\partial_n\,\mathrm{tr}\,\rho_A^{\,n}\big|_{n=1}$, computing the
  Rényi entropies $\mathrm{tr}\,\rho_A^n$ (a partition function on an $n$-sheeted cover) and
  continuing in $n$.
- **2d CFT (single interval, Calabrese-Cardy):** $S_A=\frac{c}{3}\log\frac{\ell}{a}$ for an
  interval of length $\ell$ with UV cutoff $a$; the twist operators have dimension
  $\Delta_n=\frac{c}{24}\!\left(n-\frac1n\right)$.
- **Area law:** the leading UV divergence scales with the boundary,
  $S_A\sim \mathrm{Area}(\partial A)/a^{d-1}$, in $d+1$ spacetime dimensions.

## Relations

- Computed holographically by the [[ryu-takayanagi-formula|RT formula]] (static) and its
  covariant generalization [[hrt-formula|HRT]]; both live in the topic
  [[holographic-entanglement-entropy]].
- Structurally mirrors [[bekenstein-hawking-entropy|Bekenstein-Hawking entropy]]
  (Area$/4G_N$): the traced-out region is analogous to a black-hole interior.

## Where it appears

- Area-law origin: Bombelli-Koul-Lee-Sorkin 1986, Srednicki 1993.
- 2d CFT: Holzhey-Larsen-Wilczek 1994, Calabrese-Cardy 2004.
- Holographic computation: [[hep-th-0603001|Ryu-Takayanagi 2006]],
  [[0705.0016|Hubeny-Rangamani-Takayanagi 2007]].
