---
type: topic
title: 4d N=2 SCFT / VOA correspondence
aliases: [SCFT-VOA correspondence, Beem-Rastelli VOA, chiral algebra of N=2 SCFTs, Schur sector]
tags: [n2-scft, vertex-operator-algebra, superconformal, protected-sector, chiral-algebra]
prerequisites: [superconformal-index]
created: 2026-07-08
updated: 2026-07-08
---

## Overview

Every 4d $\mathcal N=2$ superconformal field theory contains a protected subsector of local
operators — the **Schur operators** — whose correlation functions, restricted to a plane and
passed to the cohomology of a nilpotent supercharge, are those of a **2d chiral algebra**, i.e.
a [[vertex-operator-algebra|vertex operator algebra]] (VOA). This is the **4d $\mathcal N=2$
SCFT/VOA correspondence** of Beem, Lemos, Liendo, Peelaers, Rastelli and van Rees (2015). It
turns hard 4d superconformal data (a subset of the OPE coefficients, the Schur limit of the
[[superconformal-index]]) into 2d chiral-algebra data — characters, null vectors, modular
properties — that can often be computed exactly, even for strongly coupled, non-Lagrangian
theories where no other tool exists.

The map sends the 4d central charge $c_{4d}$ to the 2d Virasoro central charge via
$c_{2d} = -12\,c_{4d}$ (negative, so the VOA is non-unitary), and flavor symmetries to affine
Kac–Moody subalgebras at level $k_{2d} = -\tfrac12 k_{4d}$. The Higgs branch of the SCFT is
recovered as the associated variety of the VOA.

The correspondence, as originally formulated, is a statement about **local** operators. This
topic tracks its extension to **extended** (line, surface, domain-wall) operators via
[[twisted-schur-descent]], which enlarges the VOA into an [[extended-vertex-algebra]]
~[[2211.04410|Argyres-Lotito-Weaver 2022]].

## Historical development

- **2013–2015 — the correspondence.** The chiral algebra of the Schur sector of a 4d
  $\mathcal N=2$ SCFT is defined by twist-translating Schur operators and passing to the
  cohomology of a nilpotent supercharge; correlators become meromorphic in a single plane
  coordinate, realizing a 2d VOA (Beem–Lemos–Liendo–Peelaers–Rastelli–van Rees). Central-charge
  and flavor-level dictionaries $c_{2d}=-12c_{4d}$, $k_{2d}=-\tfrac12 k_{4d}$ follow.
- **2019–2025 — VOA twist as a deformation of the holomorphic twist.** The Schur/VOA twist is
  recognized as a [[superconformal-deformation-to-voa|superconformal deformation]] of the more
  general [[holomorphic-twist|holomorphic (minimal) twist]] (Saberi–Williams 2019). The
  systematic recovery — extracting the 2d VOA $\lambda$-brackets from the 4d holomorphic ones via
  the [[schur-superfield|Schur superfields]] $\mathbb O=\mathbf O+dz^2\Psi_{\mathbf O}$, with
  $c_{2d}=-12c$ and $k_{2d}=-\tfrac12 k_F$ reproduced — is worked out (free hypermultiplet →
  symplectic bosons) in ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]].
- **2016–2020 — structure and conventions.** Multiplet and R-symmetry conventions systematized
  ~[[2211.04410|Córdova-Dumitrescu-Intriligator 2016]] (red link); the marginal-coupling
  independence of the Schur VOA rests on a non-renormalization theorem (Baggio–de Boer–
  Papadodimas 2012). Lecture treatments (Lemos 2020) fix the twisted-supercharge conventions
  used downstream.
- **2017–2019 — first extended operators in the sector.** Surface operators in twisted-Schur
  cohomology were studied (Cordova–Gaiotto–Shao 2017; Beem 2018; Bianchi–Lemos 2019).
- **2022 — extended vertex algebra.** A systematic **Lorentzian topological descent** builds
  line, surface, and domain-wall operators from Schur operators inside the same cohomology,
  enlarging the VOA of local operators to a vertex algebra including nonlocal operators, with
  explicit free-hypermultiplet OPEs ~[[2211.04410|Argyres-Lotito-Weaver 2022]].

## Key concepts

- [[schur-operators]] — the local BPS operators of the protected sector.
- [[twisted-schur-supercharges]] — the nilpotent pair $\mathbb T_\pm$ whose cohomology is the VOA.
- [[twisted-schur-descent]] — Lorentzian descent producing extended operators in cohomology.
- [[extended-vertex-algebra]] — the enlargement of the Schur VOA by line/surface/wall operators.
- [[holomorphic-twist]] — the broader $\mathcal N\geq1$ twist of which the VOA twist is a
  deformation; the VOA generators are its [[schur-superfield|Schur superfields]].
- [[voa-plane|VOA plane]] — the spatial 2-plane on which protected correlators are meromorphic
  (introduced under [[extended-vertex-algebra]]).
- [[light-ray-operators]] — null-integrated conformal operators; cousins of the descent lines.

## Key results

- [[free-hypermultiplet-extended-va-opes]] — explicit $\mathcal O$–$\mathbf L^\pm$–$\mathbf S$
  extended-algebra OPEs in the free hypermultiplet, including the $q_\pm$ diagonalization and a
  Virasoro operator of central charge $-1$.

## Current status

The local correspondence is well established and widely used; the extended/vertex-algebra
enlargement is new and worked out in detail only for the free hypermultiplet. Whether the
extended algebra is a *conformal* vertex algebra (has a genuine stress tensor) is open — see
[[extended-va-conformal-vertex-algebra]]. Interacting examples (free vector multiplet,
conformal gauge theories, genuine Wilson–'t Hooft lines) remain to be computed.

## Open questions

- [[extended-va-conformal-vertex-algebra]] — does the extended VA have a stress-energy operator?
- Regulator-independence of descent cohomology classes (see
  [[weight-function-regularization]]).
- Does the marginal-coupling independence of the Schur VOA survive the extension?
