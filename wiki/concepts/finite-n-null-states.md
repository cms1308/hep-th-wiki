---
type: concept
title: Finite-$N$ Null States
aliases: ["finite-N null states", "finite-N trace relations", "null chiral primaries"]
tags: [ads3-cft2, symmetric-orbifold, chiral-primary, giant-graviton-expansion]
prerequisites: [chiral-primary-states, symmetric-orbifold-cft, stringy-exclusion-principle]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

Finite-$N$ null states are candidate [[chiral-primary-states|chiral primary]] operators of $\mathrm{Sym}^N(\mathcal{M}_4)$ that exist as formal expressions in the large-$N$ (KK / multi-graviton) spectrum but **decouple at finite $N$** — they become null (zero-norm) once the number of copies is finite. They are the 2d analog of trace relations in a matrix theory: a product of single-particle operators that would be independent at $N=\infty$ but is not an independent state once $N$ is small. Their removal is exactly what turns the infinite bulk KK spectrum $Z_\infty$ into the finite polynomial $Z_N$ — i.e. they implement the [[stringy-exclusion-principle]].

## Motivation

The [[stringy-exclusion-principle]] says the chiral-primary Hilbert space is finite at finite $N$, but leaves open which bulk objects account for the missing states. [[2511.00636|Lee-Li 2025]] identifies them: the finite-$N$ null states are holographically dual to BPS fluctuations of the $(\mathrm{AdS}_3\times\mathrm{S}^3)/\mathbb{Z}_k$ orbifold saddles ($k\ge2$), the AdS$_3$ analog of giant-graviton branes. Summing these saddles with their alternating signs subtracts exactly the null states from $Z_\infty$.

## Key formulas

Term-by-term matching (verified explicitly at $N=1$): the null states appearing at order $k$ are the $S_N$-invariant combinations of chiral-primary oscillators $\psi^{(i)+A}_{-1/2}$, $\bar\psi^{(i)+A}_{-1/2}$ and twist operators $|\sigma_2^{--}|$ counted by $\sum_{k\ge2}\widehat Z_k^{(0,0)}$.

Illustrative subtraction ($\mathbb{T}^4$, $\bar y=0$): the $k=1$ flowed saddle supplies
$$\widehat Z_1^{(2,0)}(y,0)=-\,y^{2N}\,\frac{(1+\varepsilon y)^2}{1-y^2},$$
which (with the negative sign) removes the would-be states beyond the finite palindrome.

## Relations

- The states subtracted in the [[ads3-giant-graviton-expansion]] to enforce the [[stringy-exclusion-principle]].
- Carried by [[ads3-z-k-orbifold-geometry|$\mathbb{Z}_k$ orbifold saddles]] via [[negative-modes-contour-rotation|negative-mode contour rotation]] (giving the $(-1)^{k-1}$ signs).
- 2d analog of the trace relations encoded by giant-graviton branes in the [[giant-graviton-expansion]].
- Matching them requires an extra $\mathbb{Z}_k$ **Gauss constraint** on the worldsheet orbifold projection.

## Where it appears

- Introduced and matched operator-by-operator in [[2511.00636|Lee-Li 2025]].
