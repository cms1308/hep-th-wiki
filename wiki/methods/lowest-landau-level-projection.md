---
type: method
title: Lowest Landau level projection
aliases: ["LLL projection", "monopole sphere construction", "Haldane pseudopotential construction"]
tags: [condensed-matter, quantum-hall, fuzzy-sphere, numerics]
prerequisites: [fuzzy-sphere]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

A rotationally invariant, finite-dimensional quantum many-body Hamiltonian on a two-sphere, built so that its low-energy physics realizes a target $2+1$D field theory on $S^2\times\mathbb R$. It is the engine of [[fuzzy-sphere-regularization]]: it turns a continuum interaction into a matrix of two-body couplings on $N=2s+1$ orbitals that can be handed to [[exact-diagonalization]].

## Prerequisites

- Landau levels of a charged particle on a sphere threaded by a magnetic monopole (Haldane 1983).
- Wu–Yang monopole harmonics as the single-particle orbitals.
- Haldane pseudopotentials: the decomposition of a rotationally invariant two-body interaction by relative angular momentum.

## How it works

1. **Monopole sphere.** Place charged particles on a radius-$r$ sphere with a $4\pi s$ magnetic monopole. The single-particle spectrum splits into Landau levels $E_n=\frac{n(n+1)+(2n+1)s}{2M_er^2}$; the lowest is $(2s+1)$-fold degenerate.
2. **LLL projection.** Restrict to the lowest Landau level. Its orbitals are the monopole harmonics $\Phi_m(\theta,\varphi)=N_m e^{im\varphi}\cos^{s+m}\!\tfrac\theta2\sin^{s-m}\!\tfrac\theta2$, forming an $SO(3)$ spin-$s$ irrep. Projection makes the coordinates non-commuting — the [[fuzzy-sphere]].
3. **Pseudopotential interactions.** Expand an ultra-local real-space interaction $U(\Omega_{ab})=g_0R^{-2}\delta(\Omega_{ab})+g_1R^{-4}\nabla^2\delta(\Omega_{ab})+\cdots$ in monopole harmonics and Wigner $3j/6j$ symbols to get Haldane pseudopotentials $V_0,V_1,\dots$ labeled by relative angular momentum.
4. **Second-quantized Hamiltonian.** Assemble $H=\sum V_{m_1m_2m_3m_4}\,\mathbf c^\dagger_{m_1}\mathbf c^\dagger_{m_2}\mathbf c_{m_3}\mathbf c_{m_4}\,\delta_{m_1+m_2,m_3+m_4}$ plus on-site (e.g. transverse-field) terms, tuned to place the system at a quantum critical point.

## Regime of validity

- Requires a partially/fully filled LLL with a large single-particle gap to higher Landau levels, so the projection is controlled.
- $N=2s+1$ is simultaneously the orbital count, the UV cutoff, and the effective spatial volume; approach to the continuum CFT is the $N\to\infty$ (equivalently $s\to\infty$) limit.
- Physical low-energy fields live on the ordinary commutative sphere; non-commutativity affects only the UV, avoiding the UV–IR mixing of generic non-commutative field theories.

## Canonical applications

- [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]] — the fuzzy-sphere Ising model realizing the [[3d-ising-cft]] (see [[fuzzy-sphere-ising-spectrum]]).
- Ippoliti–Mong–Assaad–Zaletel 2018 — half-filled-LLL regularization as a general lattice-model design tool (the methodological precursor).
