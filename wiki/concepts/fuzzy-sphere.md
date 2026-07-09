---
type: concept
title: Fuzzy sphere
aliases: ["non-commutative sphere", "fuzzy two-sphere"]
tags: [non-commutative-geometry, fuzzy-sphere, condensed-matter, numerics]
prerequisites: [lowest-landau-level-projection]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The fuzzy (non-commutative) sphere is the quantum geometry obtained when the coordinates of a particle on a two-sphere are projected onto a finite-dimensional Hilbert space — concretely, the lowest Landau level of a charged particle on a monopole sphere. The projected coordinate operators no longer commute:
$$[\tilde x_\mu,\tilde x_\nu]=i\,\frac{r}{s}\,\epsilon_{\mu\nu\rho}\,\tilde x_\rho,$$
where $r$ is the sphere radius and $2s$ the monopole strength. The lowest Landau level is $(2s+1)$-dimensional, so the sphere carries only $N=2s+1$ "cells" — a finite, tunable UV cutoff. As $s\to\infty$ the commutator vanishes and the ordinary commutative sphere is recovered.

## Motivation

A regular lattice cannot tile a curved sphere $S^{d-1\ge2}$, which blocks the standard route to a CFT's [[state-operator-correspondence]] in $d\ge3$. The fuzzy sphere sidesteps this: it is a rotationally invariant ($SO(3)$-exact) discretization of $S^2$ with a finite number of degrees of freedom, so a many-body Hamiltonian can be defined on it and diagonalized while the full rotation symmetry — essential for reading off spins $\ell$ — is preserved.

## Key formulas

- Non-commutativity: $[\tilde x_\mu,\tilde x_\nu]=i\frac{r}{s}\epsilon_{\mu\nu\rho}\tilde x_\rho$.
- Lowest-Landau-level orbitals (monopole harmonics): $\Phi_m(\theta,\varphi)=N_m\,e^{im\varphi}\cos^{s+m}\!\tfrac\theta2\,\sin^{s-m}\!\tfrac\theta2$, $m=-s,\dots,s$, forming an $SO(3)$ spin-$s$ irrep.
- Number of orbitals / effective volume: $N=2s+1$, identified with the number of Ising spins and the spatial volume ($L_x=\sqrt N$).

## Relations

- Built by [[lowest-landau-level-projection]].
- Provides the regularized geometry underlying [[fuzzy-sphere-regularization]].
- Preserves the $SO(3)$ needed for the [[state-operator-correspondence]] and [[conformal-multiplet]] decomposition.

## Where it appears

- [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]] — introduces the fuzzy sphere as a CFT regulator and realizes the [[3d-ising-cft]] on it.
- Concept originates with Madore's fuzzy two-sphere (1992); the LLL realization is Haldane's monopole-sphere construction (see [[fdm-haldane]]).
