---
type: concept
title: Stringy Exclusion Principle
aliases: ["stringy exclusion", "SEP"]
tags: [ads3-cft2, symmetric-orbifold, chiral-primary, holography]
prerequisites: [chiral-primary-states, symmetric-orbifold-cft, ads3-cft2-correspondence]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The stringy exclusion principle is the statement that the Hilbert space of [[chiral-primary-states|chiral primary]] states in the boundary CFT of $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathcal{M}_4$ is **finite-dimensional at finite $N$**, even though the bulk Kaluza–Klein spectrum of supergravity is infinite. It is the boundary imprint of a non-perturbative bulk cutoff: naive multi-particle KK states in AdS$_3$ cannot be piled up indefinitely.

## Motivation

In any 2d $\mathcal{N}=(2,2)$ SCFT, unitarity of the $\mathcal{N}=2$ superconformal algebra bounds the R-charge and dimension of chiral primaries by the central charge:
$$h,\ \bar h,\ j,\ \bar j\ \le\ \frac{c}{6}.$$
For the $\mathcal{N}=(4,4)$ [[symmetric-orbifold-cft|symmetric orbifold]] $\mathrm{Sym}^N(\mathcal{M}_4)$ one has $c=6N$, so every chiral-primary charge is capped at $N$. The chiral-primary Hilbert space $\mathcal{H}_{cc}$ is therefore finite-dimensional, and its partition function $Z_N(y,\bar y)$ is a **polynomial** in the fugacities (palindromic, reflecting the $c/6$ symmetry about $E=N$). As $N\to\infty$ the bound recedes and $Z_N\to Z_\infty$, the infinite KK/supergravity spectrum.

## Key formulas

Unitarity bound (2d $\mathcal{N}=2$): $\quad h,\bar h,j,\bar j\le c/6=N$.

Finite-$N$ chiral-primary partition function (K3, low $N$):
$$Z_1=1+22y^2+y^4,\qquad Z_2=1+23y^2+276y^4+23y^6+y^8.$$
Each is a finite palindrome; the large-$N$ limit $Z_\infty$ is instead an infinite product (see [[ads3-giant-graviton-expansion]]).

## Relations

- Bounds the spectrum of [[chiral-primary-states]] in the [[symmetric-orbifold-cft]].
- Given a bulk explanation in [[ads3-giant-graviton-expansion]]: the excess KK states beyond the finite count are cancelled by [[finite-n-null-states|finite-$N$ null states]] carried by $\mathbb{Z}_k$ orbifold saddles with alternating signs.
- The 4d/higher-dimensional analog is the truncation of the BPS spectrum realized by the [[giant-graviton-expansion]].
- Belongs to the [[ads3-cft2-correspondence]] topic.

## Where it appears

- Formulated by Maldacena–Strominger (1998); rooted in the $c/6$ unitarity bound (Boucher–Dean–Zumino 1986; Lerche–Vafa–Warner 1989).
- Given a bulk, finite-$N$ realization in [[2511.00636|Lee-Li 2025]], where the infinite alternating sum over orbifold geometries collapses to the finite polynomial $Z_N$.
