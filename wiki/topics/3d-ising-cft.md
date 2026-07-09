---
type: topic
title: The 3D Ising CFT
aliases: ["3D Ising transition", "3D Ising universality class", "critical Ising in three dimensions"]
tags: [conformal-field-theory, 3d-ising, critical-phenomena, condensed-matter]
prerequisites: [state-operator-correspondence]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

The 3D Ising CFT is the conformal field theory governing the critical point of the three-dimensional Ising model — equivalently the liquid–vapor critical point, uniaxial magnets, and the $\phi^4$ Wilson–Fisher fixed point in $d=3$. It is the most experimentally relevant and most studied interacting CFT with no known exact solution. Its low-lying spectrum is characterized by two relevant $\mathbb Z_2$-odd/even scalars, $\sigma$ ($\Delta_\sigma\approx0.518$) and $\epsilon$ ($\Delta_\epsilon\approx1.413$), a conserved stress tensor $T_{\mu\nu}$ ($\Delta_T=3$), and a tower of higher primaries.

Its **emergent conformal symmetry** was conjectured by Polyakov in 1970 (see [[emergent-conformal-symmetry-3d-ising]]) but, unlike the 2D case, had never been demonstrated directly — only assumed (numerical [[conformal-bootstrap]]) or probed on non-conformal manifolds (Monte Carlo on tori). The [[fuzzy-sphere-regularization]] program changed this by realizing the transition on $S^2\times\mathbb R$ and exhibiting its [[state-operator-correspondence]] explicitly.

## Historical development

- **Onsager 1944** — exact 2D Ising solution; the 3D case remains unsolved.
- **Polyakov 1970** — conjectured emergent conformal symmetry at critical points.
- **Wilson–Fisher / $\epsilon$-expansion (1970s)** — the Ising fixed point as a perturbative CFT near $d=4$.
- **Numerical conformal bootstrap 2008–2016** — Rychkov et al., El-Showk et al., Kos–Poland–Simmons-Duffin: the sharpest scaling dimensions and OPE data, *assuming* conformal symmetry.
- **Zhu–Han–Huffman–Hofmann–He 2022** — [[2210.13482|fuzzy-sphere realization]]: direct verification of conformal symmetry via the state-operator correspondence, plus two new parity-odd primaries (see [[fuzzy-sphere-ising-spectrum]]).

## Key concepts

- [[state-operator-correspondence]] — the defining CFT structure now checked directly for this theory.
- [[conformal-multiplet]] — the organization of $\sigma$, $\epsilon$, $T_{\mu\nu}$ and higher operators into primaries + descendants.
- [[virial-current]] — whose absence at low $\Delta$ distinguishes conformal from merely scale invariance in this theory.

## Key results

- [[fuzzy-sphere-ising-spectrum]] — 13 parity-even primaries matching bootstrap to $<1.6\%$, and 2 previously unknown parity-odd primaries.

## Current status

An interacting CFT known to very high precision by the [[conformal-bootstrap]], and now with independent, geometry-based confirmation of its conformal symmetry from [[fuzzy-sphere-regularization]]. No exact/analytic solution is known.

## Open questions

- Precise dimensions of the two new parity-odd primaries and their bootstrap confirmation.
- The critical Binder cumulant $U_4^c$ on $S^2\times\mathbb R$ and its bootstrap value.
- An analytic understanding of why the [[virial-current]] is pushed to high dimension.
