---
type: concept
title: Chiral Primary States
aliases: ["chiral primaries", "(c,c) states", "BPS chiral primaries"]
tags: [ads3-cft2, cft2, supersymmetry, bps, chiral-primary]
prerequisites: [symmetric-orbifold-cft]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

In a 2d $\mathcal{N}=(2,2)$ SCFT, a chiral primary is a superconformal primary annihilated by one supercharge in each sector, saturating the BPS bound so that its conformal weight equals its R-charge, $h=j$ (and $\bar h=\bar j$ for the anti-holomorphic side). The left–right chiral–chiral states, "(c,c)" states, satisfy $h=j$ and $\bar h=\bar j$ simultaneously. They are $\tfrac12$-BPS (or $\tfrac14$-BPS depending on the count of preserved supercharges) and their number is protected — invariant under exactly marginal deformations — which makes them the standard precision-test observable of [[ads3-cft2-correspondence|AdS$_3$/CFT$_2$]].

## Motivation

Because their degeneracies are moduli-independent, chiral primaries computed at the free [[symmetric-orbifold-cft|symmetric-orbifold]] point can be compared directly with bulk supergravity KK modes and string states at any coupling. At large $N$ they reproduce the 6d supergravity KK spectrum; at finite $N$ their number is bounded (the [[stringy-exclusion-principle]]), which is the sharp finite-$N$ observable that [[2511.00636|Lee-Li 2025]] reconstructs from the bulk.

## Key formulas

BPS condition (holomorphic): $\quad h=j$, and unitarity caps the charge at $j\le c/6$.

Chiral-primary partition function (fugacities $y,\bar y$ for $2J_0,2\bar J_0$):
$$Z_N(y,\bar y)=\mathrm{Tr}_{\mathcal{H}_{cc}}\big(y^{2J_0}\bar y^{2\bar J_0}\big)=\lim_{q,\bar q\to0}\mathrm{Tr}\big(q^{L_0-J_0}\bar q^{\bar L_0-\bar J_0}\,y^{2J_0}\bar y^{2\bar J_0}\big).$$

$\mathcal{N}=4$ spectral flow relates R-sector ground states to NS chiral primaries via the automorphism $\sigma^{\eta}$: $L_0\to L_0+\eta J_0+\tfrac{c}{24}\eta^2$, $J_0\to J_0+\tfrac{c}{12}\eta$ (with $\eta=\bar\eta=-1$).

## Relations

- Live in the [[symmetric-orbifold-cft]]; their finite-$N$ bound is the [[stringy-exclusion-principle]].
- Those that decouple at finite $N$ are the [[finite-n-null-states]].
- Their partition function is the target of the [[ads3-giant-graviton-expansion]] and is extracted via the [[grand-canonical-residue-expansion]].
- The chiral-primary black hole (charge $E=N$) sits at the center of the palindrome $Z_N$.

## Where it appears

- Matched to bulk KK modes at large $N$ by Maldacena–Strominger, de Boer et al (1998).
- Their finite-$N$ integer spectrum reproduced from bulk orbifold geometries in [[2511.00636|Lee-Li 2025]].
