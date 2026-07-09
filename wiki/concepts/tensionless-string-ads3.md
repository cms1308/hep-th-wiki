---
type: concept
title: Tensionless String on AdS$_3$
aliases: ["tensionless string", "psu(1,1|2)_1 string", "k=1 string on AdS3"]
tags: [ads3-cft2, worldsheet, string-theory, tensionless-string]
prerequisites: [ads3-cft2-correspondence, symmetric-orbifold-cft]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The tensionless string is type IIB string theory on $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathbb{T}^4$ at the minimal amount of NS-NS flux, one unit of NS5 charge ($Q_5=1$, i.e. $\ell^2_{\mathrm{AdS}_3}/\alpha'=1$). In the hybrid formalism (Berkovits–Vafa–Witten 1999) the worldsheet theory becomes an exactly solvable WZW-type model based on the affine Lie superalgebra $\mathfrak{psu}(1,1|2)_{\mathsf k}$ at **minimal level** $\mathsf k=1$, admitting a free-field realization. At this point the worldsheet spectrum matches the [[symmetric-orbifold-cft|symmetric orbifold]] $\mathrm{Sym}^N(\mathbb{T}^4)$ essentially state-for-state, making the AdS$_3$/CFT$_2$ dictionary explicit at the level of individual strings.

## Motivation

Generic AdS backgrounds have curvatures of order the string scale, so the worldsheet sigma model is strongly coupled and unsolvable. The $\mathsf k=1$ point is the exception: the free-field $\mathfrak{psu}(1,1|2)_1$ description gives a solvable worldsheet whose physical spectrum reproduces the dual CFT, so bulk string computations can be carried out and matched to the boundary. This is what lets [[2511.00636|Lee-Li 2025]] verify that the terms of its bulk sum coincide with genuine worldsheet partition functions of the orbifold geometries.

## Key formulas

Minimal level fixed by NS5 flux: $\quad \mathsf k=1\ \Leftrightarrow\ \ell^2_{\mathrm{AdS}_3}/\alpha'=Q_5=1$.

Spacetime/worldsheet charge map: $\quad \mathcal{J}^3_0=L_0,\qquad \mathcal{K}^3_0=J_0$.

Worldsheet spectral flow by amount $w$ maps the vacuum module to the $w$-twisted sector; integer $w$ gives AdS$_3$ long strings, while **fractional flow** $w=n/k$ reproduces the $\mathbb{Z}_k$ orbifold geometries and their twisted BPS spectra (used to build the $\widehat Z_k^{\,\mu}$).

## Relations

- Worldsheet dual of the [[symmetric-orbifold-cft]] within the [[ads3-cft2-correspondence]].
- Its fractional spectral flows produce the orbifold saddles summed in the [[ads3-giant-graviton-expansion]].
- Ultra-short $\mathfrak{sl}(2,\mathbb{R})$ representations (worldsheet spin $J^{\mathfrak{sl}(2,\mathbb{R})}=1/2$) carry the [[chiral-primary-states|chiral primaries]].

## Where it appears

- Introduced by Eberhardt–Gaberdiel–Gopakumar (2018); ensemble/grand-canonical interpretation by Eberhardt (2020) and Eberhardt–Gaberdiel (2021).
- Orbifold worldsheet spectra computed by Gaberdiel et al (2023).
- Used to verify the bulk sum-over-geometries proposal in [[2511.00636|Lee-Li 2025]].
