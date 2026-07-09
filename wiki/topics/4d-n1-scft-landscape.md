---
type: topic
title: Landscape of 4d N=1 SCFTs
aliases: [SCFT landscape program, deformation classification of SCFTs]
tags: [scft, classification, supersymmetry, rg-flow]
prerequisites: [conformal-field-theory, supersymmetry-basics]
created: 2026-07-04
updated: 2026-07-04
---

## Overview

A Lagrangian classification program for 4d $\mathcal{N}=1$ SCFTs: start from gauge
theories known to flow to interacting fixed points ("seed theories") and exhaustively
enumerate every fixed point reachable by chains of relevant superpotential deformations
and [[flip-deformation|flip deformations]], using [[a-maximization]] to compute each
fixed point's central charges and the [[superconformal-index|superconformal index]] as
the consistency filter and fingerprint. Unlike string-theoretic classifications (6d
$(1,0)$, class $\mathcal{S}$, rank-1 Coulomb-branch geometry), which cover
high-supersymmetry corners, this attacks the far larger $\mathcal{N}=1$ space directly.

## Historical development

- **2003** — [[a-maximization]] (Intriligator-Wecht,
  [hep-th/0304128](https://arxiv.org/abs/hep-th/0304128)) makes IR central charges of
  $\mathcal{N}=1$ gauge theories computable, with the Kutasov-Parnachev-Sahakyan
  correction ([hep-th/0308071](https://arxiv.org/abs/hep-th/0308071)) handling operators
  that decouple at the unitarity bound.
- **2016–17** — SUSY-enhancing RG flows: deforming $\mathcal{N}=2$ (and even
  $\mathcal{N}=1$) gauge theories with flip fields lands on
  [[argyres-douglas-theories|Argyres-Douglas theories]] (Maruyoshi-Song
  [1606.05632](https://arxiv.org/abs/1606.05632),
  [1607.04281](https://arxiv.org/abs/1607.04281); Agarwal-Maruyoshi-Song
  [1610.05311](https://arxiv.org/abs/1610.05311)) — evidence that simple gauge theories
  reach non-Lagrangian SCFTs.
- **2018** — the pilot landscape: all deformations of $SU(2)$ $N_f=1$ adjoint SQCD
  (Maruyoshi-Nardoni-Song, [1806.08353](https://arxiv.org/abs/1806.08353)).
- **2020–23** — classification of candidate seeds: large-$N$ superconformal gauge
  theories with a [[dense-spectrum-scft|dense spectrum]] (Agarwal-Lee-Song
  [2007.16165](https://arxiv.org/abs/2007.16165);
  [[2308.01717|Cho-Choi-Lee-Song 2023]]).
- **2024** — the large landscape: 7,346 inequivalent fixed-point candidates from ten
  rank-1/rank-2 seeds ($SU(2)$, $SU(3)$, $SO(5)\simeq Sp(2)$, $G_2$), published as a
  searchable database ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]],
  [qft.kaist.ac.kr/landscape](https://qft.kaist.ac.kr/landscape)).
- **2025** — the complete simple-gauge-group large-$N$ classification (20 $SU$ + 6 $SO$
  + 9 $Sp$ families, $W=0$, fixed flavor symmetry) and its
  [[large-n-universality-classes|Type I/II/III universality]]; comprehensive validation
  of the [[modified-ads-wgc-3c-2a|modified AdS WGC]]
  ([[2510.19136|Cho-Lee-Song 2025]]).

## Key concepts

[[flip-deformation]] · [[superconformal-index]] · [[argyres-douglas-theories]] ·
[[non-commuting-rg-flows]] · accidental symmetries (the program's central caveat) ·
dangerously irrelevant operators (why [[a-maximization]] is redone at every step)

## Key results

- [[large-n-universality-classes]] — all simple-gauge-group large-$N$ $\mathcal{N}=1$
  SCFTs ($W=0$) fall into three universality classes keyed to the rank-2 tensor count.
- [[minimal-n1-scft]] — the smallest-known interacting $\mathcal{N}=1$ SCFT now has a
  Lagrangian.
- Record central-charge ratio $a/c = \tfrac{507}{419} \simeq 1.21$ and the conjecture
  $a/c < \tfrac54$ for interacting $\mathcal{N}=1$ SCFTs
  ([[n1-central-charge-bounds]]).
- Statistical correlations across the landscape: $a/c$ vs. lightest-operator gap and
  vs. number of relevant operators ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]).
- New Lagrangian duals for ($\mathcal{N}=1$-deformed) Argyres-Douglas theories,
  including a duality changing the number of flavors.

## Current status

Active. The database rests on two systematic assumptions: deformations are applied one
at a time (fixed points requiring simultaneous multi-operator deformations are missed),
and all accidental symmetries are assumed visible to $a$-maximization plus index checks
— entries could be added or invalidated as tools improve
([[candidate-rank-1-cb-dimension-5-4]] is the sharpest such puzzle).

## Open questions

- [[n1-central-charge-bounds]] — is $a/c < \tfrac54$ a theorem? What is the minimal $c$?
- [[candidate-rank-1-cb-dimension-5-4]] — new $\mathcal{N}=2$ SCFT or accidental
  symmetry?
- Detecting accidental IR symmetries systematically.
- Extending to higher-rank seeds, non-Lagrangian seeds, quivers, and nonzero
  superpotential; completing the truncated landscapes and the
  [[veneziano-limit|Veneziano]]-only classes.
- [[holographic-duals-of-type-ii-iii]] — supergravity duals for the sparse
  universality classes.
