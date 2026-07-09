---
type: topic
title: AdS$_3$/CFT$_2$ Correspondence
aliases: ["AdS3/CFT2", "D1-D5 CFT", "AdS3 holography"]
tags: [ads3-cft2, holography, symmetric-orbifold, string-theory]
prerequisites: [ads-cft-correspondence, anti-de-sitter-space]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

The AdS$_3$/CFT$_2$ correspondence is the lowest-dimensional and most tractable member of the [[ads-cft-correspondence|AdS/CFT]] family. Its cleanest realization is type IIB string theory on $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathcal{M}_4$ (with $\mathcal{M}_4=\mathbb{T}^4$ or K3), dual to a 2d $\mathcal{N}=(4,4)$ SCFT on the moduli space of the D1–D5 system. At a special point of that moduli space the dual is the [[symmetric-orbifold-cft|symmetric orbifold]] $\mathrm{Sym}^N(\mathcal{M}_4)$, with central charge $c=6N$ and $N=Q_1Q_5$ ($\mathbb{T}^4$) or $Q_1Q_5+1$ (K3).

Two features make this duality special. First, the boundary being 2d means the full infinite-dimensional Virasoro (indeed $\mathcal{N}=4$ superconformal) symmetry is available on both sides. Second, at one unit of NS5 flux the worldsheet theory becomes the exactly solvable [[tensionless-string-ads3|tensionless string]], so bulk string amplitudes can be computed and matched to the symmetric orbifold. This makes AdS$_3$/CFT$_2$ the setting where holography is understood in the most microscopic detail.

## Historical development

- **1997** — The D1–D5 near-horizon geometry $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathcal{M}_4$ and its CFT dual are identified as part of the original AdS/CFT proposal, [[hep-th-9711200|Maldacena 1997]].
- **1998** — Chiral primaries of the symmetric orbifold are matched with 6d supergravity KK modes at large $N$ (Maldacena–Strominger; de Boer; Larsen; Deger et al). [[jan-de-boer|de Boer]] extracts the finite-$N$ structure from grand-canonical residues. The [[stringy-exclusion-principle]] (finite chiral-primary Hilbert space at finite $N$) is formulated.
- **1996** — The [[dmvv-formula|DMVV formula]] recasts symmetric-orbifold partition functions as second-quantized strings.
- **2000–2005** — Conical-defect / $\mathbb{Z}_k$ orbifold and Lunin–Mathur fuzzball geometries are constructed (Martinec; Maldacena–Maoz; Balasubramanian et al; Lunin–Mathur); their BPS states are geometrically quantized (Rychkov; Krishnan–Raju).
- **2018–2021** — The tensionless string on $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathbb{T}^4$ at $k=1$ NS5 flux is solved as a $\mathfrak{psu}(1,1|2)_1$ free-field theory (Eberhardt–Gaberdiel–Gopakumar), and its grand-canonical/ensemble interpretation is developed (Eberhardt; Eberhardt–Gaberdiel; Aharony et al).
- **2023** — Tensionless worldsheet spectra of the $\mathbb{Z}_k$ orbifold geometries are computed (Gaberdiel et al).
- **2025** — A bulk sum-over-geometries prescription reproduces the exact finite-$N$ chiral-primary spectrum, giving a bulk stringy exclusion principle, [[2511.00636|Lee-Li 2025]] — the AdS$_3$ analog of the [[giant-graviton-expansion]].

## Key concepts

- [[symmetric-orbifold-cft]] — the boundary CFT at the orbifold point.
- [[chiral-primary-states]] — the protected $\tfrac12$-BPS spectrum used for precision tests.
- [[stringy-exclusion-principle]] — the finite-$N$ bound on the spectrum.
- [[tensionless-string-ads3]] — the exactly solvable worldsheet at $k=1$.
- [[stokes-sectors-partition-function]], [[finite-n-null-states]] — features of the finite-$N$ bulk description.

## Key results

- [[dmvv-formula]] — grand-canonical partition function of the symmetric orbifold.
- [[ads3-giant-graviton-expansion]] — finite-$N$ chiral-primary spectrum as an alternating sum over $\mathbb{Z}_k$ orbifold saddles.

## Current status

The BPS/chiral-primary sector of AdS$_3$/CFT$_2$ is now understood at finite $N$: [[2511.00636|Lee-Li 2025]] reproduces the exact integer spectrum from a bulk sum over orbifold geometries and identifies the states in the "wedge" $N/2<E<N$ that are neither KK modes nor black holes. Open frontiers concern the $\tfrac14$-BPS sector, a first-principles gravitational-path-integral derivation of the orbifold partition functions, and the large-$\mathcal{N}=4$ setting $\mathrm{AdS}_3\times\mathrm{S}^3\times\mathrm{S}^3\times\mathrm{S}^1$.

## Open questions

- Derive the orbifold one-loop partition functions $\widehat Z_k^{\,\mu}$ directly from the Euclidean gravitational path integral, including the contour treatment of negative modes.
- Extend the sum-over-geometries picture to $\tfrac14$-BPS states above the black-hole threshold (elliptic genus of $\mathrm{Sym}^N$K3) and to the Farey-tail / Rademacher expansion.
- Realize the orbifold partition functions as genuine giant-graviton branes in $\mathrm{AdS}_3\times\mathrm{S}^3$.
