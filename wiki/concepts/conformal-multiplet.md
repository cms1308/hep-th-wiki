---
type: concept
title: Conformal multiplet
aliases: ["conformal family", "primary and descendants", "conformal tower"]
tags: [conformal-field-theory, representation-theory]
prerequisites: [state-operator-correspondence]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A conformal multiplet is an irreducible representation of the conformal group $SO(d+1,1)$: a **primary** operator $O$ (annihilated by the special conformal generators $K_\mu$, labeled by dimension $\Delta$, spin $\ell$, and — in parity-invariant theories — parity $P$) together with the infinite tower of **descendants** obtained by acting with derivatives $\partial_\mu$. Under the [[state-operator-correspondence]] the primary maps to a lowest-weight state on $S^{d-1}$ and each descendant to a definite excited state, so an entire multiplet appears as a fixed pattern of levels above the primary.

## Motivation

If a critical Hamiltonian is genuinely conformal, its spectrum must decompose *exactly* into these multiplets — every predicted descendant present, no extra states. Checking this pattern, sector by sector, is what turns "the spectrum looks scale-invariant" into "the theory is conformal." Missing or surplus states would falsify conformal symmetry.

## Key formulas

In $d=3$ (rotation group $SO(3)$, spins $\ell$), the descendants of a spin-$\ell$ primary $O_{\mu_1\cdots\mu_\ell}$ of dimension $\Delta$ come in two families:
- **Parity-even type:** $\partial_{\nu_1}\!\cdots\partial_{\nu_j}\,\partial_{\mu_1}\!\cdots\partial_{\mu_i}\,\square^n O_{\mu_1\cdots\mu_\ell}$, with $(\Delta+2n+j+i,\ \ell+j-i)$.
- **Parity-flipping type:** $\varepsilon_{\mu_\ell\rho\tau}\partial_\rho\,\partial_{\nu_1}\!\cdots\square^n O_{\mu_1\cdots\mu_\ell}$, with $(\Delta+2n+j+i+1,\ \ell+j-i)$; the $\varepsilon$-tensor raises $\Delta$ by 1 and **flips parity**, so a $P=+1$ primary spawns $P=-1$ descendants and vice versa.
- Scalar special case: $\partial_{\nu_1}\!\cdots\partial_{\nu_j}\square^n O$ has $(\Delta+2n+j,\ j)$.

## Relations

- Organized by the [[state-operator-correspondence]].
- The unit of spectrum-matching in [[fuzzy-sphere-regularization]].
- Conserved currents (e.g. the stress tensor $T_{\mu\nu}$) sit at the top of *short* multiplets, with $\Delta_T=d$.

## Where it appears

- [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]] — the entire low-lying $S^2$ spectrum of the [[3d-ising-cft]] is matched multiplet-by-multiplet, including the $\varepsilon$-tensor parity-flipping descendants (see [[fuzzy-sphere-ising-spectrum]]).
