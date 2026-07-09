---
type: topic
title: 6d (1,0) supergravity landscape
aliases: [6d supergravity landscape, 6d N=(1,0) swampland, six-dimensional supergravity]
tags: [6d-supergravity, swampland, string-landscape, anomaly-cancellation, f-theory, little-string-theory]
prerequisites: [swampland-program]
created: 2026-07-08
updated: 2026-07-08
---

## Overview

Six-dimensional $\mathcal N=(1,0)$ supergravity — eight supercharges in $d=6$ — is one of
the sharpest testing grounds for the [[swampland-program|Swampland program]]. The
combination of supersymmetry, unitarity and anomaly cancellation is so constraining that
the set of theories consistent at the level of local physics is nearly discrete, and much
of it is realized geometrically in [[f-theory|F-theory]]. But perturbative consistency does
not fully separate the landscape from the swampland: the extra, non-perturbative data live
in the **BPS strings** that become tensionless at boundaries of tensor moduli space
(associated with 6d SCFTs, little string theories, or critical strings). The modern program
turns those strings into concrete constraints and constructive building blocks for the
whole landscape.

The bosonic data of a 6d $(1,0)$ supergravity are $T$ tensor multiplets, vector multiplets
with gauge algebra $\bigoplus_i\mathfrak g_i$, and charged hypermultiplets. String/tensor
charges live in a [[tensor-charge-lattice|unimodular Lorentzian lattice]] $\Gamma$ of
signature $(1,T)$; the [[green-schwarz-sagnotti-mechanism|Green-Schwarz-Sagnotti mechanism]]
factorizes the anomaly polynomial and ties the spectrum to lattice vectors $b_0,b_i$.

## Historical development

- **Anomaly cancellation and finiteness (1984–2021).** Green-Schwarz-Sagnotti
  factorization in 6d and the gravitational-anomaly relation $H-V=273-29T$ set the founding
  constraints; the broader landscape/finiteness program grew from Vafa 2005 onward.
- **F-theory construction (1996–).** Most consistent 6d $(1,0)$ theories are realized by
  F-theory on elliptically fibered Calabi-Yau threefolds; the tensor branch is the base
  surface, gauge algebras sit on curves, and matter comes from singular fibers.
- **Non-Higgsable clusters (Morrison-Taylor 2012).** The complete list of minimal
  un-Higgsable gauge algebras carried by rigid curves — the
  [[non-higgsable-cluster|NHC catalogue]] that seeds the building-block program.
- **6d SCFT / LST classification (2013–2019).** F-theoretic classification of 6d
  superconformal and little string theories (Heckman-Morrison-Vafa; Bhardwaj et al.),
  including endpoint configurations and frozen singularities.
- **BPS strings as swampland probes (2019–).** Central-charge bounds on supergravity
  strings (Kim-Tarazi-Vafa) and the Emergent String Conjecture (Lee-Lerche-Weigand) recast
  infinite-distance limits and tensionless strings as consistency diagnostics.
- **$H$-string constraints and finiteness proof (Kim-Vafa-Xu 2024).** Every tensor-moduli
  boundary hosts a tensionless BPS string; a distinguished $H$-string
  ([[h-string]], $f^2=0$, $b_0\cdot f=2$) exists for $T\ge 1$; the massless spectrum is
  finite ($T\le 193$, $r(V)\le 480$).
- **Supergravity blocks (Hamada-Jeon-Kim 2026, [[2607.05496|Hamada-Jeon-Kim 2026]]).**
  A constructive EFT framework: assemble theories from [[supergravity-block|supergravity blocks]]
  — one $H$-string LST plus external generators, each with a Gram matrix of exactly one
  positive eigenvalue — and completely classify the
  [[non-higgsable-gravity-block|non-Higgsable gravity blocks]]
  ([[classification-non-higgsable-gravity-blocks|9,630,606 blocks]], tensor bases to $T=9$).

## Key concepts

- [[tensor-charge-lattice]] — unimodular Lorentzian $\Gamma$ of signature $(1,T)$; the Dirac
  pairing of BPS string charges.
- [[supergravity-block]] — the minimal intrinsically-gravitational building block: one
  $H$-string LST sector plus its external generators.
- [[non-higgsable-gravity-block]] — a block supporting only non-Higgsable gauge algebras.
- [[h-string]] — the distinguished BPS string ($f^2=0$, $b_0\cdot f=2$) shared across a
  theory's tensor base.
- [[non-higgsable-cluster]] — minimal curve configurations with rigid, un-Higgsable gauge
  algebras.

## Key results

- [[classification-non-higgsable-gravity-blocks]] — 12,762 $P$-type LST bases, 9,630,606
  non-Higgsable gravity blocks, tensor bases complete to $T=9$, agreeing with F-theory to
  $T\le 6$.

## Current status

The block framework reduces the construction of 6d $(1,0)$ supergravities to (i)
enumerating $H$-string-sharing LST sectors, (ii) attaching external generators, and (iii)
enhancing gauge/matter on non-negative-self-intersection tensors. The non-Higgsable
subclass is fully classified; the general case (gauge enhancements, extra matter, Abelian
sectors, $T\ge 10$) is open. The framework produces candidate **non-geometric** theories
(frozen-singularity NHCs) whose UV completion is unknown.

## Open questions

- [[uv-completion-frozen-nhc-supergravities]] — do the frozen-NHC / non-geometric candidate
  supergravities admit genuine quantum-gravity UV completions?
- Is the non-Higgsable list already the complete tensor-base list for $T\le 9$? (checked
  geometrically to $T\le 6$)
- Sharp, physically motivated bounds on intersection numbers to replace the practical
  scan cutoffs.
