---
type: result
title: Free-hypermultiplet extended-VA OPEs
aliases: [O-L-S subalgebra, free hyper extended operator product expansions]
tags: [n2-scft, vertex-operator-algebra, free-hypermultiplet, ope]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

For the free hypermultiplet SCFT, the operator product expansions of the
$\mathcal O$–$\mathbf L^\pm$–$\mathbf S$ subalgebra of the [[extended-vertex-algebra]] — built from
the weight-$1/2$ symplectic boson $q_I$ (a Schur operator) and its line and surface descents —
are all **meromorphic in the [[extended-vertex-algebra|VOA-plane]] coordinate $z$**, confirming
that the extended operators genuinely enlarge the Schur VOA. Explicit representatives are
$$\mathbf L^+[q_I](z) = -iN\!\int_{L^+}\!\! dx^+\,\tilde\psi_{\dot1 I},\quad
  \mathbf L^-[q_I](z) = -iN\!\int_{L^-}\!\! dx^-\,\psi_{1 I},\quad
  \mathbf S[q_I](z) = -N^2\!\int_S\! dx^+dx^-\,\partial_z\rho^2_I.$$

## Derivation sketch

Descent representatives are obtained from [[twisted-schur-descent]] applied to $q_I$; the raw
integrals diverge and are made finite by [[weight-function-regularization]]. Correlators are then
computed by free-field Wick contraction, reducing to two-point functions of the free scalars and
fermions. Two structural facts emerge:

- **Diagonalization.** Defining $q_\pm \doteq \tfrac12(q \pm \mathbf S[q])$, the combination
  $q_+$ is a **free symplectic boson**, while $q_-$ has **completely regular OPEs with
  everything**. This motivates the conjecture $\mathbf S[q_I] =_{\mathbb T} q_I$ (i.e. $q_-$ is
  trivial in cohomology).
- **A Virasoro operator that is not a stress tensor.** The weight-2 Schur operator $T$ obeys the
  Virasoro OPE
  $$T(z)\,T(0)\sim \frac{-1/2}{z^4} + \frac{2T(0)}{z^2} + \frac{\partial_z T(0)}{z}$$
  with central charge $-1$, yet fails the primary condition on descent operators (e.g.
  $T(z)\,\mathbf S[q](0)$ is non-standard), so it is not the extended algebra's stress-energy
  operator — see [[extended-va-conformal-vertex-algebra]].

## Assumptions

- Free hypermultiplet SCFT (no interactions); computations are exact Wick contractions.
- The descent operators are regularized by an admissible weight function; results assume — but do
  not prove — regulator independence ([[descent-regulator-independence]]).

## Status

Established by explicit computation for the free hypermultiplet
~[[2211.04410|Argyres-Lotito-Weaver 2022]]. The conjecture $\mathbf S[q_I] =_{\mathbb T} q_I$ and
a full generating set of the extended VA (even in the free theory) remain open.

## Implications

- Concrete evidence that [[twisted-schur-descent]] enlarges the Schur VOA into a bona fide
  [[extended-vertex-algebra]] with meromorphic correlators.
- The $q_\pm$ diagonalization suggests the extended free-hyper algebra may collapse back to the
  ordinary symplectic-boson VOA up to cohomologically trivial pieces.
- The Virasoro-but-not-primary structure of $T$ frames the central open structural question about
  whether the extended VA is a *conformal* vertex algebra.
