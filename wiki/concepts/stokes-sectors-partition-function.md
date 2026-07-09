---
type: concept
title: Stokes Sectors of the Partition Function
aliases: ["Stokes sectors", "contributing pole towers", "fugacity chambers"]
tags: [ads3-cft2, giant-graviton-expansion, complex-analysis, partition-function]
prerequisites: [grand-canonical-residue-expansion, ads3-giant-graviton-expansion]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

When the finite-$N$ partition function is extracted from a grand-canonical generating function by the [[grand-canonical-residue-expansion]], the set of pole towers that actually contribute depends on the fugacities $y,\bar y$ and jumps **discontinuously** as they cross certain lines. The regions of fugacity space with a fixed contributing set are the Stokes sectors; the boundaries are (anti-)Stokes lines. In the bulk this means different infinite subsets of spectrally-flowed orbifold saddles dominate the gravitational path integral in different chambers.

## Motivation

The poles of the [[dmvv-formula|DMVV]] grand-canonical partition function accumulate on an essential-singularity wall $|p|=|y^{-1}\bar y^{-1}|$. Which towers lie inside the deformed contour — hence contribute to $Z_N$ — is decided by the magnitudes of the fugacities, exactly as Stokes phenomenon selects which exponentials contribute to an asymptotic series. The finite answer $Z_N$ is the same in every chamber, but its representation as a sum over geometries is chamber-dependent.

## Key formulas

Contributing set: $\quad \mathcal{S}_{y,\bar y}\subset\{(0,0),(2,0),(0,2),(2,2)\}$ in
$$Z_N(y,\bar y)=\sum_{\mu\in\mathcal{S}_{y,\bar y}}\sum_{k=1}^{\infty}\widehat Z_k^{\,\mu}(y,\bar y).$$
Examples: $\ |\bar y|<|y|\le1:\ \mathcal{S}=\{(0,0),(2,0)\}$; $\ |y|=|\bar y|<1:\ \mathcal{S}=\{(0,0)\}$.

## Relations

- Organizing structure of the [[ads3-giant-graviton-expansion]]; selects which [[tensionless-string-ads3|spectrally-flowed]] orbifold saddles enter.
- Governed by the pole-tower geometry of the [[grand-canonical-residue-expansion]].
- Proposed as a general principle for classifying sums over gravitational saddles by chemical potential.

## Where it appears

- Introduced (with an explicit fugacity phase diagram) in [[2511.00636|Lee-Li 2025]].
