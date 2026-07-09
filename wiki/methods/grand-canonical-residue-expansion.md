---
type: method
title: Grand-Canonical Residue Expansion
aliases: ["grand-canonical residues", "residue expansion of the index", "pole-tower expansion"]
tags: [ads3-cft2, giant-graviton-expansion, complex-analysis, partition-function]
prerequisites: [symmetric-orbifold-cft, dmvv-formula]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

The finite-$N$ partition function (or index) from a grand-canonical generating function $\mathcal{Z}(p,\dots)=\sum_N p^N Z_N$, by extracting the $p^N$ coefficient as a contour integral and evaluating it as a sum over residues at the poles of $\mathcal{Z}$. Each pole (or tower of poles) is identified with a bulk gravitational saddle, turning the coefficient extraction into a **sum over geometries**.

## Prerequisites

- A closed-form grand-canonical partition function — e.g. the [[dmvv-formula|DMVV]] product for the [[symmetric-orbifold-cft|symmetric orbifold]].
- Control of the analytic structure of $\mathcal{Z}$ in the fugacity $p$: locations of poles, and any essential-singularity walls where poles accumulate.

## How it works

1. Write $Z_N=\oint\frac{dp}{2\pi i}\,p^{-N-1}\,\mathcal{Z}(p,\dots)$ on a small circle around $p=0$.
2. Deform the contour outward; each pole crossed contributes $-\mathrm{Res}\,[p^{-N-1}\mathcal{Z}]$.
3. When poles form infinite towers accumulating on a wall $|p|=|p_*|$ (essential singularity), the naive residue theorem fails. Regularize with a cutoff $M$ (e.g. $n\le M$ in the DMVV product), apply the residue theorem, then take $M\to\infty$. Which towers survive depends on the fugacities — the [[stokes-sectors-partition-function|Stokes sectors]].
4. Group each tower's residues by its $\mathbb{Z}_k$ images: $\widehat Z_k^{\,\mu}=-\sum_{m=0}^{k-1}\mathrm{Res}_{p=\mu_k^m}p^{-N-1}\mathcal{Z}$. These are the bulk saddle partition functions.

## Regime of validity

- Requires a meromorphic (or controlled-essential-singularity) $\mathcal{Z}$; the fugacity domain determines the contributing pole set, so results are chamber-dependent (Stokes phenomenon).
- The bulk-saddle identification is sharp when the residue terms independently match known geometry partition functions (as verified with the [[tensionless-string-ads3|tensionless string]]).

## Canonical applications

- The [[giant-graviton-expansion]] in AdS$_5$/CFT$_4$ (contour rotation past giant-graviton poles).
- The [[ads3-giant-graviton-expansion]] in [[2511.00636|Lee-Li 2025]]: residues of the DMVV partition function at four pole towers give the $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ orbifold saddles with alternating signs, collapsing to the finite $Z_N$.
- Earlier grand-canonical-residue analyses of finite-$N$ chiral primaries in AdS$_3$ ([[jan-de-boer|de Boer]] 1998).
