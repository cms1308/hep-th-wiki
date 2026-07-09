---
type: concept
title: ANEC operator
aliases: [averaged null energy operator, averaged null energy condition]
tags: [conformal-field-theory, light-ray-operators, energy-conditions]
prerequisites: ["light-ray-operators"]
created: 2026-07-06
updated: 2026-07-06
---

## Definition

The averaged null energy operator: the stress tensor integrated along a complete null
geodesic,
$$\mathcal E=\int_{-\infty}^{\infty} dy^+\,T_{++}(y^+),$$
the simplest [[light-ray-operators|light-ray operator]]. The averaged null energy
*condition* (ANEC) is the statement $\langle\psi|\mathcal E|\psi\rangle\ge0$ in any state —
proven for unitary QFTs both information-theoretically
(Faulkner–Leigh–Parrikar–Wang 2016) and from causality (Hartman–Kundu–Tajdini 2016).

## Motivation

ANEC expectation values are the energy fluxes measured in conformal collider experiments,
whose positivity yields the [[hofman-maldacena-bound]]. Beyond positivity, the ANEC
operator generates symmetry: on the [[einstein-cylinder]] its Fourier modes and their
conformal descendants close into infinite-dimensional algebras.

## Key formulas

- On the Einstein cylinder EC$^3$ (null lines between antipodal points,
  [[2603.26459|Strominger–Wei 2026]] conventions):
  $\mathcal E(\phi)=\tfrac12\int_0^\pi d\tau^+\,\sin^3\tau^+\,T_{++}$, Fourier modes
  $\mathcal E_k=\int_0^{2\pi}d\phi\,e^{ik\phi}\mathcal E(\phi)$.
- The ANEC modes are $SO(3,2)$ *lowest weight*: annihilated by the conformal lowering
  operators, with all descendants assembling into a single representation of quadratic
  Casimir 6. In $w$-generator labels, $\mathcal E_k=-i^k\,w^{\frac{3+k}{2}}_{-\frac{k+1}{2},\frac{k-1}{2}}$,
  saturating the wedge boundary of the
  [[lambda-deformed-w-algebra|$\mathcal L_\Lambda w_{1+\infty}$ algebra]].

## Relations

- Member of the Córdova–Shao triple $\mathcal E,\mathcal K,\mathcal N$ with universal
  commutators ([[light-ray-operators]]).
- Seed of the $\mathcal L_\Lambda w_{1+\infty}$ symmetry of every CFT$_3$
  ([[every-cft3-has-l-lambda-w-symmetry]]); anticipated as the gravitational analogue of
  the conserved-current light transform that seeds the [[s-algebra]] in AdS$_4$
  ([[2601.00096|Sheta et al. 2025]]).

## Where it appears

[[2603.26459|Strominger–Wei 2026]] (central) · [[2601.00096|Sheta et al. 2025]]
(conjectured role, realized in the sequel) · [[hofman-maldacena-bound]].
