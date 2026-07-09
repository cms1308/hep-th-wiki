---
type: topic
title: Holomorphic twist of 4d SQFTs
aliases: [holomorphic twist, minimal twist, holomorphically twisted SQFT, higher holomorphic field theory]
tags: [holomorphic-twist, twisted-qft, higher-symmetry, l-infinity, vertex-operator-algebra, protected-sector]
prerequisites: [superconformal-index]
created: 2026-07-08
updated: 2026-07-08
---

## Overview

The **holomorphic (minimal) twist** is the least restrictive twist of a 4d $\mathcal N\geq1$
supersymmetric field theory: one picks a translation-invariant square-zero supercharge
$\mathbf Q$ whose image on the translations is as small as possible (two-dimensional in 4d),
adds it to the BV/BRST differential, and passes to $\mathbf Q$-cohomology. The result is a
**holomorphic field theory on $\mathbb C^2$**: anti-holomorphic translations act trivially and
the operator product is meromorphic. Because it only requires $\mathcal N\geq1$, the holomorphic
twist is more general than the [[scft-voa-correspondence|Schur/VOA twist]] (which needs
$\mathcal N\geq2$) — and it retains **all** operators that contribute to the superconformal
index, making it a categorification of the [[superconformal-index]]: an operator algebra rather
than a number.

The distinctive feature relative to 2d chiral CFT is that the configuration space of points in
$\mathbb C^2$ is not affine, so it has **higher Dolbeault cohomology**. By Hartogs' lemma there
are no meromorphic functions on $\mathbb C^2$ with isolated singularities, so singular OPE data
is carried by $(0,1)$-forms rather than poles. The infinite-dimensional symmetry algebras — the
higher analogues of Virasoro and Kac–Moody — are therefore genuinely **derived**: homotopy Lie
($L_\infty$) algebras rather than ordinary Lie algebras, with anomalies appearing as **ternary
brackets / 3-cocycles** (central extensions) rather than 2-cocycles.

## Historical development

- **1994–2013 — foundations.** Holomorphic twists of 4d gauge theory introduced (Johansen 1994)
  and developed in the factorization-algebra framework (Costello 2011; Costello–Li 2013). The
  space of square-zero supercharges — the [[nilpotence-variety|nilpotence variety]] — is
  classified (Eager–Saberi–Walcher 2018; Elliott–Safronov–Williams 2020).
- **2013–2019 — higher current algebras.** The Schur-sector VOA twist of $\mathcal N\geq2$
  SCFTs (Beem et al. 2013) is recognized as a **deformation of the holomorphic twist**
  (Saberi–Williams 2019). Higher Kac–Moody and Virasoro algebras of holomorphic field theory in
  complex dimension $>1$ are constructed (Faonte–Hennion–Kapranov 2019; Gwilliam–Williams).
- **2022–2024 — perturbative brackets and anomalies.** Secondary products and
  [[holomorphic-lambda-bracket|$\lambda$-brackets]] computed from Feynman/Laman graphs
  (Budzik–Gaiotto et al.; Gaiotto–Kulp–Wu 2024). The central charges $a,c$ are identified as
  the two central extensions of the 4d "2-Witt/Virasoro" algebra
  (paper I ~[[2509.16737|Bomans-Garner-Williams-Wu 2023]]; Williams 2024).
- **2025 — unified framework (installment II).** A single complex-geometric + algebraic
  treatment of symmetries and anomalies ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]]:
  anomalies as ternary brackets, [[holomorphic-a-maximization|holomorphic $a$-maximization]],
  the extended-SUSY algebras $\mathfrak{svir}(2|\mathcal N-1)$ (forcing $a=c$ for
  $\mathcal N\geq3$), and the recovery of the Beem-et-al VOA via a
  [[superconformal-deformation-to-voa|superconformal deformation]].

## Key concepts

- [[semi-chiral-superfield]] — the basic object: a reduced superfield with $D_-\mathbf O=0$,
  in bijection with $\mathbf Q$-closed local operators; its higher form components are the
  holomorphic descendants.
- [[holomorphic-lambda-bracket]] — generating functions for the higher current modes, defined
  by configuration-space ($S^3$) integrals; the $L_\infty$ analogue of a Lie conformal algebra.
- [[two-virasoro-algebra]] — $\mathfrak{vir}(2)_{a,c}$: the holomorphic enhancement of spacetime
  symmetry, with $a,c$ as its two central extensions.
- [[higher-kac-moody-algebra]] — the holomorphic enhancement of a flavor symmetry, with the
  flavor level as its central extension.
- [[higher-super-virasoro-algebra]] — $\mathfrak{svir}(2|\mathcal N-1)$ for extended SUSY.
- [[schur-superfield]] — the object surviving the superconformal deformation that generates the
  associated VOA.

## Key results

- [[ac-anomalies-as-central-extensions]] — the conformal anomalies $a,c$ and the 't Hooft/ABJ
  anomalies are central extensions (3-cocycles / ternary brackets) of the higher symmetry
  algebras; $a=c$ for $\mathcal N\geq3$ follows from cocycle uniqueness.
- The [[scft-voa-correspondence|Beem-et-al VOA]] is reproduced by deforming the holomorphic
  twist by $\int z^2\widetilde{\mathbf G}$ (see [[superconformal-deformation-to-voa]]).

## Current status

The $\mathcal N=1$ framework — semi-chiral superfields, higher symmetry algebras, anomalies as
central extensions, and holomorphic $a$-maximization — is worked out in detail. The extended-SUSY
algebras are constructed for $\mathcal N=2,3,4$, though explicit supergeometric formulas for the
3-cocycles are known only in part. The VOA-from-deformation prescription is fully explicit for
the free hypermultiplet (symplectic bosons); interacting examples remain to be computed.

## Open questions

- [[intrinsic-holomorphic-a-maximization]] — an intrinsically holomorphic proof of
  $a$-extremization, requiring a notion of unitarity ("graded unitarity") in the twist.
- [[supergeometric-3-cocycles-svir]] — explicit representatives of the $\mathfrak{svir}$ 3-cocycles.
- Twisted Argyres–Douglas theories and IR $\mathcal N=2$ enhancement of $\mathcal N=1$ Lagrangians
  (announced follow-up).
