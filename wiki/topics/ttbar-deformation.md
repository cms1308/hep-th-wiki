---
type: topic
title: TTbar and current-stress deformations
aliases: [TTbar deformation, T-Tbar, TTbar-deformed CFT, irrelevant solvable deformations]
tags: [ttbar, jtbar, irrelevant-deformation, 2d-cft, holography, non-ads-holography]
prerequisites: [conformal-field-theory]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

The $T\bar T$ deformation is an irrelevant deformation of a 2d QFT by the composite operator
$\det(T_{\mu\nu})$ built from the stress tensor. Despite being irrelevant (dimension 4 at the
UV point), it is *solvable*: the deformed finite-size spectrum, thermodynamics, and S-matrix
are fixed by the undeformed data through a flow equation. Starting from a 2d CFT, the
deformation deletes locality at short distances while preserving integrability and a
(now nonlocal) conformal symmetry, so a $T\bar T$-deformed CFT sits between a local QFT and a
theory of quantum gravity / non-critical string.

A family of relatives is defined the same way — by a bilinear $\epsilon^{ab}\epsilon^{\mu\nu}
J_{\mu a}J_{\nu b}$ in conserved currents. Replacing one stress-tensor factor with a $U(1)$
current gives the $J\bar T$ deformation ([[jt-bar-deformation]]), which breaks Lorentz
invariance and half of the conformal symmetry while remaining solvable. These deformations are
the field-theory face of several "holography beyond AdS" programs: finite radial cutoff in
AdS$_3$, single-trace $T\bar T/J\bar T$ via [[tst-holography|TsT]], and warped-AdS$_3$/Kerr-CFT.

## Historical development

- **2004** — $T\bar T$ introduced as a solvable irrelevant deformation, with the factorization
  of $\langle T\bar T\rangle$ making $\det T$ well defined (Zamolodchikov).
- **2016** — the deformed energy levels on the cylinder are shown to obey an inviscid Burgers
  equation, giving a closed-form spectrum (Smirnov–Zamolodchikov; Cavaglià–Negro–Szécsényi–Tateo).
  See [[ttbar-deformed-spectrum]].
- **2016–2018** — holographic and gravitational reformulations: finite radial cutoff in
  AdS$_3$ (McGough–Mezei–Verlinde); coupling to flat "JT"/topological 2d gravity
  (Dubovsky–Gorbenko–Mirbabayi; Dubovsky–Gorbenko–Hernández-Chifflet); random-geometry /
  field-dependent coordinate change (Cardy).
- **2017** — $J\bar T$ deformation introduced as a solvable $(1,2)$ deformation preserving the
  left-moving conformal symmetry (Guica); single-trace $T\bar T/J\bar T$ and long-string
  holography (Giveon–Itzhaki–Kutasov; Apolo–Song).
- **2019–2024** — the surviving conformal symmetry is made explicit and *nonlocal*: mixed
  boundary conditions in AdS$_3$ gravity (Guica–Monten), flowed/nonlocal Virasoro at the
  Lagrangian and Hamiltonian levels (Guica; Kruthoff–Parrikar; Georgescu–Guica). See
  [[nonlocal-conformal-symmetry-deformed-cft]] and [[hamiltonian-flow-deformed-cft]].
- **2023** — two independent nonperturbative two-point functions agree: worldsheet via
  [[tst-holography|TsT/$T\bar T$]] (Cui–Du–Song) and a field-theory large-momentum computation
  (Aharony–Barel), both solving Cardy's Callan–Symanzik equation. See
  [[deformed-cft-two-point-function]].
- **2025** — a symmetry-organized operator dictionary for the plane:
  [[2507.08588|Chen–Du–Liu–Song 2025]] constructs the dressed and physical operators of
  $T\bar T$-deformed CFTs and reproduces the nonperturbative two-point function;
  [[2511.10557|Chen–Du–Song 2025]] extends the whole construction to $J\bar T$, finding a
  Virasoro–Kac–Moody symmetry and an instanton contribution to the position-space correlator.

## Key concepts

- [[jt-bar-deformation]] — the $(1,2)$ current-stress relative that keeps left conformal symmetry.
- [[nonlocal-conformal-symmetry-deformed-cft]] — the flowed Virasoro (and Kac–Moody) generators.
- [[dressed-operator-deformed-cft]] — nonlocal primaries of the flowed symmetry.
- [[physical-operator-deformed-cft]] — the local operators built from them.
- [[tst-holography]] — TsT / single-trace holographic realization.

## Key results

- [[ttbar-deformed-spectrum]] — the Burgers/√ formula for the deformed spectrum.
- [[deformed-cft-two-point-function]] — nonperturbative UV two-point function with a
  momentum-dependent effective weight $h_\lambda$.

## Current status

The deformed spectrum, torus partition function, and S-matrix are under good control. Since
2019 the surviving nonlocal conformal symmetry has been made explicit in several formalisms;
since 2025 it has been turned into a working tool for computing correlators of local operators
on the plane, with results matching string-theory (TsT) predictions. The quantum definition of
these operators, finite-size (cylinder) correlators, and cases with a classical central charge
remain open.

## Open questions

- [[quantum-operators-deformed-cft]] — a fully quantum definition of the physical operators
  (normal ordering, exact correlators) beyond the classical/leading-log construction.
- Finite-size (cylinder) correlators, where the spectrum-deforming term reappears.
- The physical meaning of the nonperturbative/instanton structure in $J\bar T$ correlators and
  its relation to nonperturbative effects in $T\bar T$ partition functions.
