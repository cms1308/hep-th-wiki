---
type: result
title: AdS$_3$ Giant-Graviton Expansion (finite-$N$ chiral primaries)
aliases: ["sum over orbifold geometries", "AdS3 giant graviton expansion", "finite-N chiral primary sum"]
tags: [ads3-cft2, symmetric-orbifold, stringy-exclusion-principle, giant-graviton-expansion]
status: conjectured
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The exact finite-$N$ chiral-primary partition function of $\mathrm{Sym}^N(\mathcal{M}_4)$ ($\mathcal{M}_4=\mathbb{T}^4$ or K3) equals an infinite alternating sum of one-loop supersymmetric partition functions of $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ orbifold geometries and their $\mathcal{N}=4$ spectral flows:
$$Z_N(y,\bar y)=\sum_{\mu\in\mathcal{S}_{y,\bar y}}\ \sum_{k=1}^{\infty}\widehat{Z}_k^{\,\mu}(y,\bar y),\qquad \mathcal{S}_{y,\bar y}\subset\{(0,0),(2,0),(0,2),(2,2)\}.$$
Here $\widehat Z_k^{(0,0)}$ is the one-loop partition function of IIB strings on $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k\times\mathcal{M}_4$; the other $\mu$ are its asymmetric spectral-flow generalizations. The $k=1$ term is the large-$N$ KK spectrum $Z_\infty$; the $k\ge2$ terms carry alternating signs $(-1)^{k-1}$ and subtract the [[finite-n-null-states|finite-$N$ null states]], collapsing the infinite sum to the finite polynomial $Z_N$. This is the AdS$_3$/CFT$_2$ analog of the [[giant-graviton-expansion]] and provides a bulk realization of the [[stringy-exclusion-principle]].

## Derivation sketch

1. Write the grand-canonical partition function $\mathcal{Z}(p,y,\bar y)=\sum_N p^N Z_N$ using the [[dmvv-formula|DMVV]] product; its NS form is
$$\mathcal{Z}^{\rm NS}(p;y,\bar y)=\prod_{n\ge1}\prod_{r,s=0}^{2}\Big(1-(-\varepsilon)^{r+s}p^n y^{n+r-1}\bar y^{n+s-1}\Big)^{-(-1)^{r+s}h^{r,s}}.$$
2. Extract $Z_N=\oint\frac{dp}{2\pi i}p^{-N-1}\mathcal{Z}$ via the [[grand-canonical-residue-expansion]]. The simple poles form four towers $(0/2,0/2)_k^m$ at $p=e^{2\pi i m/k}y^{-(1\mp1/k)}\bar y^{-(1\mp1/k)}$, accumulating on an essential-singularity wall $|p|=|y^{-1}\bar y^{-1}|$.
3. Each tower's residue sum is (minus) an orbifold partition function: $\widehat Z_k^{\,\mu}=-\sum_{m=0}^{k-1}\mathrm{Res}_{p=\mu_k^m}\,p^{-N-1}\mathcal{Z}$.
4. The K3 orbifold determinant has bosonic negative modes ($n<k$) of negative $h,j$; the identity
$$\frac{1}{\prod_{n=1}^{k-1}(1-y^{\frac nk-1}\bar y^{\frac nk-1})}=\frac{(-1)^{k-1}y^{\frac{k-1}{2}}\bar y^{\frac{k-1}{2}}}{\prod_{n=1}^{k-1}(1-y^{1-\frac nk}\bar y^{1-\frac nk})}$$
produces the $(-1)^{k-1}$ sign. The alternating sum cancels down to $Z_N$.
5. The one-loop ground-state charge is staggered to $h=\bar h=j=\bar j=\tfrac N2(1-\tfrac1k)+\tfrac14(k-1)$, resolving the $k\to\infty$ accumulation and pushing $k\gtrsim\sqrt{2N}$ orbifolds past the black-hole charge.

## Assumptions

- Orbifold-point (free symmetric-orbifold) description of the D1–D5 CFT; protected quantities extend across moduli space.
- The tensionless $\mathfrak{psu}(1,1|2)_1$ worldsheet ([[tensionless-string-ads3]]) computes the $\widehat Z_k^{\,\mu}$; verified to coincide with the residue terms.
- One-loop (quadratic-fluctuation) truncation of the bulk saddles, with Wick-rotated contours for the negative modes.
- Matching the null states requires an extra $\mathbb{Z}_k$ Gauss constraint beyond the worldsheet orbifold projection.

## Status

Conjectured bulk prescription, checked in detail: the integer spectrum is reproduced at any $N$, the $\widehat Z_k^{\,\mu}$ match tensionless worldsheet partition functions of the orbifold geometries, and the $N=1$ null states are matched operator-by-operator. A first-principles Euclidean gravitational-path-integral derivation is not yet available.

## Implications

- Gives a **bulk mechanism** for the [[stringy-exclusion-principle]]: large cancellations among orbifold saddles, not a hard cutoff.
- Identifies the bulk objects populating the "wedge" $N/2<E<N$ between KK modes and black holes as (flowed) $\mathbb{Z}_k$ orbifold geometries dual to [[finite-n-null-states]].
- Establishes the analytic structure ([[stokes-sectors-partition-function|Stokes sectors]]) of grand-canonical partition functions as an organizing principle for sums over gravitational saddles.
