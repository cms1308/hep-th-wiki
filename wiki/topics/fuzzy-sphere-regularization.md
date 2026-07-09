---
type: topic
title: Fuzzy sphere regularization
aliases: ["fuzzy sphere", "non-commutative sphere regularization"]
tags: [conformal-field-theory, numerics, condensed-matter, fuzzy-sphere]
prerequisites: [state-operator-correspondence, 3d-ising-cft]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

Fuzzy sphere regularization is a way to study a $d=3$ conformal field theory *directly on its natural radial-quantization geometry* $S^2\times\mathbb R$, rather than on a flat torus or a lattice that cannot tile a curved sphere. Interacting charged particles (spinful electrons) are placed on a two-sphere threaded by a magnetic monopole and projected onto the lowest Landau level; the projection turns the sphere into a [[fuzzy-sphere|fuzzy (non-commutative) sphere]] with a finite number $N=2s+1$ of orbitals, which acts as the UV cutoff. Physical low-energy fields still live on an ordinary commutative sphere, so tuning the microscopic Hamiltonian to a quantum critical point yields a genuine 3D CFT whose [[state-operator-correspondence]] can be read off a small [[exact-diagonalization|exact-diagonalization]] spectrum.

The payoff is that a finite-size quantum spectrum on $S^2$ maps energies onto CFT scaling dimensions via $\delta E_n=(v/R)\Delta_n$ — the same logic that works for critical spin chains on $S^1$ in $d=2$ — now available in $d=3$ for the first time. This is the wiki's first entry point into numerical/condensed-matter conformal field theory.

## Historical development

- **Polyakov 1970** — conjectured emergent conformal symmetry at critical points, the target this program finally tests directly in 3D (see [[emergent-conformal-symmetry-3d-ising]]).
- **Cardy 1984–85** — the finite-size [[state-operator-correspondence]] on the cylinder, the diagnostic the whole program relies on.
- **Haldane 1983** — Landau levels on a monopole sphere and pseudopotentials; the [[lowest-landau-level-projection]] technology (see [[fdm-haldane]]).
- **Madore 1992** — the fuzzy two-sphere as a matrix geometry.
- **Ippoliti–Mong–Assaad–Zaletel 2018** — half-filled-LLL regularization as a design tool for lattice models; the direct methodological ancestor.
- **Zhu–Han–Huffman–Hofmann–He 2022** — [[2210.13482|the founding paper]]: builds the fuzzy-sphere Ising model, verifies the 3D state-operator correspondence, and extracts 15 primaries (see [[fuzzy-sphere-ising-spectrum]]).

## Key concepts

- [[fuzzy-sphere]] — the non-commutative sphere from LLL projection, $[\tilde x_\mu,\tilde x_\nu]=i(r/s)\epsilon_{\mu\nu\rho}\tilde x_\rho$.
- [[state-operator-correspondence]] — the radial-quantization map turning energies on $S^2\times\mathbb R$ into scaling dimensions.
- [[conformal-multiplet]] — how the spectrum organizes: primaries plus $\partial/\square/\varepsilon$ descendants.
- [[virial-current]] — the scale-vs-conformal diagnostic whose absence at low $\Delta$ certifies genuine conformal invariance.

## Key results

- [[fuzzy-sphere-ising-spectrum]] — the 3D Ising state-operator correspondence with 13 parity-even and 2 new parity-odd primaries, matching the [[conformal-bootstrap]] to $<1.6\%$.

## Current status

Established for the 3D Ising CFT and rapidly extended (in the broader literature since 2022) to $O(N)$ Wilson–Fisher and other 3D critical points, OPE coefficients, and defect/boundary CFT data. Within this wiki only the founding Ising result is ingested so far.

## Open questions

- [[emergent-conformal-symmetry-3d-ising]] — now largely answered for Ising; the method's reach to gauge-theory conformal windows and deconfined criticality is the live frontier.
- Whether fuzzy-sphere regularization can be recast rigorously in non-commutative geometry and applied to continuum QFTs without UV–IR mixing.
