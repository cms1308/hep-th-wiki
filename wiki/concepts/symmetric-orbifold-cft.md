---
type: concept
title: Symmetric Orbifold CFT
aliases: ["symmetric orbifold", "Sym^N", "symmetric product orbifold"]
tags: [ads3-cft2, cft2, symmetric-orbifold, string-theory]
prerequisites: [ads3-cft2-correspondence]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The symmetric orbifold $\mathrm{Sym}^N(\mathcal{M})=\mathcal{M}^{\otimes N}/S_N$ is the CFT built from $N$ copies of a seed CFT $\mathcal{M}$, quotiented by the permutation group $S_N$. Its Hilbert space decomposes into **twisted sectors** labelled by conjugacy classes of $S_N$ (partitions of $N$): a length-$w$ cycle glues $w$ copies into a single "long string" of central charge $wc_{\text{seed}}$, on which the seed fields have fractional (twisted) moding. The total central charge is $c=N\,c_{\text{seed}}$.

For AdS$_3$/CFT$_2$ the relevant seed is a sigma model on $\mathcal{M}_4=\mathbb{T}^4$ or K3 ($c_{\text{seed}}=6$), giving a 2d $\mathcal{N}=(4,4)$ SCFT with $c=6N$. This is the dual of type IIB on $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathcal{M}_4$ at a special ("orbifold") point of the D1–D5 moduli space, with $N=Q_1Q_5$ ($\mathbb{T}^4$) or $Q_1Q_5+1$ (K3).

## Motivation

The symmetric orbifold is the free/solvable corner of the D1–D5 moduli space, where the boundary spectrum can be enumerated combinatorially and matched to the bulk. Its twisted sectors are the CFT image of multi-wound strings, which is why the [[dmvv-formula|DMVV formula]] presents the grand-canonical partition function as a **second-quantized string** partition function. Protected quantities — [[chiral-primary-states|chiral primaries]], the elliptic genus — are invariant across the moduli space, so orbifold-point computations test the bulk everywhere.

## Key formulas

Central charge: $c=N\,c_{\text{seed}}=6N$ for $\mathcal{M}_4$.

Grand-canonical (second-quantized) partition function — the [[dmvv-formula|DMVV formula]] schematically:
$$\sum_{N\ge0}p^N\,Z_{\mathrm{Sym}^N(\mathcal{M})}(q,\bar q)=\prod_{n\ge1}\prod_{h,\bar h}\big(1-p^n q^{h}\bar q^{\bar h}\big)^{-c(nh,\bar h,\dots)},$$
with exponents fixed by the seed degeneracies $c(\cdot)$.

Chiral-primary projection: with fugacities $y,\bar y$ for the R-charges $J_0,\bar J_0$,
$$Z_N(y,\bar y)=\lim_{q,\bar q\to0}\mathrm{Tr}\big(q^{L_0-J_0}\bar q^{\bar L_0-\bar J_0}\,y^{2J_0}\bar y^{2\bar J_0}\big),$$
a finite palindromic polynomial by the [[stringy-exclusion-principle]].

## Relations

- Boundary dual in the [[ads3-cft2-correspondence]].
- Its grand-canonical partition function is the [[dmvv-formula|DMVV formula]]; the pole structure of that object drives the [[grand-canonical-residue-expansion]] and the [[ads3-giant-graviton-expansion]].
- Hosts [[chiral-primary-states]] and [[finite-n-null-states]]; the finite-$N$ truncation of its chiral-primary spectrum is the [[stringy-exclusion-principle]].
- Twisted sectors are reproduced on the worldsheet by the spectrally-flowed [[tensionless-string-ads3|tensionless string]].

## Where it appears

- Dual CFT identified in [[hep-th-9711200|Maldacena 1997]].
- Second-quantized partition function: [[dmvv-formula|DMVV]] (1996).
- Finite-$N$ chiral-primary spectrum reconstructed from the bulk in [[2511.00636|Lee-Li 2025]].
