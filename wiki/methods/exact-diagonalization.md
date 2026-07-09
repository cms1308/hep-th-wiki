---
type: method
title: Exact diagonalization
aliases: ["ED", "Lanczos diagonalization"]
tags: [numerics, condensed-matter, many-body]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

The low-lying eigenvalues and eigenvectors of a quantum many-body Hamiltonian by directly diagonalizing its matrix in a finite Hilbert space. For a critical model realized via [[fuzzy-sphere-regularization]], the eigenvalues are the finite-size energies whose ratios give CFT scaling dimensions through the [[state-operator-correspondence]], and the eigenvectors carry the exact quantum numbers $(\mathbb Z_2,P,\ell)$ used to sort states into [[conformal-multiplet|conformal multiplets]].

## Prerequisites

- A second-quantized Hamiltonian on a finite orbital basis (here from [[lowest-landau-level-projection]]).
- Symmetry sectors to block-diagonalize: total $S^z$/particle number, angular momentum $\ell$ and $L_z$, $\mathbb Z_2$, and particle-hole/parity $P$.
- Sparse-matrix eigensolvers (Lanczos/Arnoldi) for the lowest states.

## How it works

1. Build the many-body basis in a fixed symmetry sector (fixing conserved quantum numbers drastically shrinks each block).
2. Represent $H$ as a sparse matrix in that basis.
3. Apply an iterative eigensolver (Lanczos) to extract the lowest eigenpairs.
4. Label each eigenstate by its exact quantum numbers, then feed the spectrum to the multiplet-decomposition analysis.

## Regime of validity

- Exact but limited by exponential Hilbert-space growth: feasible for small systems. In the fuzzy-sphere Ising study, $N\le16$ spins (~16 GB, ~30 min on a laptop); larger sizes ($N$ up to 36) use DMRG instead.
- The virtue on the fuzzy sphere is that finite-size effects are far smaller than in 3D classical Monte Carlo, so even $N=4$–$16$ already resolves the conformal spectrum.

## Canonical applications

- [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]] — ED (with DMRG for finite-size scaling) extracts the [[3d-ising-cft]] spectrum and its 15 primaries (see [[fuzzy-sphere-ising-spectrum]]).
- The standard workhorse of quantum-critical spin-chain studies in $d=2$, here lifted to $d=3$ via the sphere.
