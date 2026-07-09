---
type: topic
title: Closed String Field Theory
aliases: [CSFT, closed SFT, nonpolynomial string field theory]
tags: [string-field-theory, closed-string, tachyon-condensation, hyperbolic-vertices]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Overview

Closed string field theory (CSFT) is a spacetime-covariant, off-shell formulation of closed string
theory: a classical action $S[\Psi]$ on the closed-string Hilbert space whose equation of motion
reproduces the S-matrix and whose solutions are string backgrounds. Its defining feature is that it
is **nonpolynomial** — there is no associative star product and no consistent covariant *cubic*
action; the action needs an infinite tower of higher vertices $V_{0,n}$ ($n=3,4,5,\dots$), organized
by a geometric Batalin–Vilkovisky master equation into a quantum $L_\infty$ algebra. The vertices
are integrals over regions of the moduli space of punctured spheres, with the string-field
constraints $b_0^-|\Psi\rangle=0$, $L_0^-|\Psi\rangle=0$ imposed.

The nonpolynomial structure is the central technical obstacle. In *open* SFT the star product makes
the action cubic, and tachyon condensation (D-brane decay) was solved analytically via the $KBc$
subalgebra. Closed SFT has no such algebra, so classical solutions — in particular the
[[closed-string-tachyon-vacuum|closed string tachyon vacuum]] — have historically been accessible
only by level truncation.

Two developments changed the computational landscape:
[[hyperbolic-string-vertices|hyperbolic string vertices]] (constant curvature $K=-1$, systole
$\ge L$) gave the vertices explicit, computable local
coordinates, and the [[mirzakhani-topological-recursion|topological recursion]] for those vertices
generated all $V_{0,n}$ from the cubic $V_{0,3}$ and reduced the classical EOM to a single
[[fvm-quadratic-integral-equation|quadratic integral equation]].

## Historical development

- **1989–1992 — nonpolynomial action.** No consistent covariant cubic closed SFT exists
  (Sonoda–Zwiebach, Kugo–Suehiro); the full nonpolynomial action from minimal-area metrics, with the
  geometric BV master equation and quantum $L_\infty$ structure, is Zwiebach 1992.
- **1994–2006 — numerical vertices.** Minimal-area four/five-string vertices computed numerically
  (Belopolsky, Moeller); quartic tachyon coupling $\kappa^2 V_0^{(4)}=-3.0172\,t^4$.
- **2005 — tachyon vacuum by level truncation** (Yang–Zwiebach): the bosonic closed string tachyon
  vacuum requires [[ghost-dilaton-condensation-tachyon-vacuum|ghost-dilaton condensation]] alongside
  the tachyon; endpoint a "nothing" state with vanishing cosmological constant.
- **2017–2019 — hyperbolic vertices** with systole $\ge L$ and $K=-1$ (Moosavian–Pius,
  Costello–Zwiebach), fixing the [[systolic-threshold|systolic threshold]]
  $L_*=2\,\mathrm{arcsinh}(1)$.
- **2021 — explicit cubic vertex** (Fırat): closed-form local coordinates / mapping radii for the
  hyperbolic cubic vertex from the Fuchsian equation and hypergeometric functions.
- **2024 — topological recursion for string vertices** ([[fvm-quadratic-integral-equation|FVM]],
  Fırat–Valdes-Meller): all $V_{0,n}$ from $V_{0,3}$ via
  [[mirzakhani-topological-recursion|Mirzakhani recursion]]; the classical EOM collapses to one
  quadratic integral equation, solved exactly for the analogous stubbed scalar QFT.
- **2026 — recursive-algebraic solution** ([[2603.29926|Kim 2026]]): a
  [[seam-graded-expansion|seam-graded expansion]] makes the string equation algebraic at every
  order; the tachyon-only expansion diverges, re-confirming that ghost-dilaton condensation is
  essential.

## Key concepts

- [[hyperbolic-string-vertices]] — constant-curvature vertices with computable local coordinates.
- [[systolic-threshold]] — $L_*=2\,\mathrm{arcsinh}(1)=1.7627\ldots$, the maximal vertex length
  consistent with the BV master equation.
- [[fvm-quadratic-integral-equation]] — the classical EOM reduced to a quadratic self-consistency
  condition.
- [[twisted-mirzakhani-kernels]] — Mirzakhani $R/D$ kernels with Feynman-region subtractions.
- [[closed-string-tachyon-vacuum]] — the "nothing" state; the main solution being sought.

## Key results

- [[ghost-dilaton-condensation-tachyon-vacuum]] — the bosonic tachyon vacuum is not tachyon-only;
  the ghost dilaton must condense.
- [[seam-graded-expansion]] as a method: each grade is a matrix inversion, not a Fredholm equation.

## Current status

The vertices and the classical EOM are now computable in closed form via hyperbolic geometry and
topological recursion. The [[seam-graded-expansion|seam-graded]] solution of the
[[closed-string-tachyon-vacuum|tachyon vacuum]] is an active program: the linearized recursion is
unobstructed (clean spectrum), but the tachyon-only truncation diverges, and whether the full
multi-level expansion (including the ghost dilaton) converges is open. The quantum (higher-genus)
extension and a possible closed-string analog of the $KBc$ algebra remain to be developed.

## Open questions

- [[closed-string-tachyon-vacuum-convergence]] — does the multi-level seam-graded expansion
  converge, or is it asymptotic?
- [[closed-string-kbc-algebra]] — is there a hyperbolic-vertex analog of the $KBc$ algebra giving an
  analytic seed?
