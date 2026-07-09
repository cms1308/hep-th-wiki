---
type: concept
title: State-operator correspondence
aliases: ["radial quantization", "operator-state map", "state-operator map"]
tags: [conformal-field-theory, radial-quantization]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

In a conformal field theory, local operators are in one-to-one correspondence with the states of the theory quantized on a sphere. Radially quantizing a CFT on $\mathbb R^d$ and applying the Weyl map $\mathbb R^d\setminus\{0\}\cong S^{d-1}\times\mathbb R$ (with radial time $\tau=\log|x|$) turns the dilatation operator $D$ into the Hamiltonian on $S^{d-1}$. A scaling operator $O$ of dimension $\Delta$ inserted at the origin creates an eigenstate $|O\rangle=O(0)|0\rangle$ with energy
$$\delta E_{O}=E_{O}-E_0=\frac{v}{R}\,\Delta_{O},$$
where $R$ is the sphere radius and $v$ a non-universal speed. Primaries map to lowest-weight states; descendants $\partial_{\mu_1}\!\cdots O$ map to the tower built by the raising generators. This is the diagnostic fingerprint of conformal symmetry.

## Motivation

The correspondence converts an abstract operator spectrum into something directly measurable: the finite-size energy spectrum of a critical quantum Hamiltonian on a sphere. In $d=2$ this is the standard confirmation of conformal invariance for critical spin chains on $S^1$. In $d\ge3$ the obstacle is realizing the theory on the curved sphere $S^{d-1}$ at all — solved for $d=3$ by [[fuzzy-sphere-regularization]].

## Key formulas

- Energy–dimension relation (Cardy): $\delta E_n=\frac{v}{R}\Delta_n$.
- Weyl/radial map: $ds^2_{\mathbb R^d}=r^2\big(\tfrac{dr^2}{r^2}+d\Omega^2\big)$, radial time $\tau=\log r$, $D\to H_{S^{d-1}}$.
- The stress tensor sits at $\Delta_T=d$ (so $\Delta_T=3$ in $d=3$), giving a scale-free way to calibrate $v/R$.

## Relations

- The organizing principle behind [[conformal-multiplet]] decomposition.
- Central diagnostic of [[fuzzy-sphere-regularization]] and the object verified for the [[3d-ising-cft]].
- Underlies radial quantization used throughout CFT and AdS/CFT (bulk states ↔ boundary operators is its holographic cousin — see [[ads-cft-correspondence]]).

## Where it appears

- [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]] — first *direct* verification in a 3D CFT (see [[fuzzy-sphere-ising-spectrum]]).
- Originates with Cardy's finite-size scaling on the cylinder (see [[john-cardy]]).
