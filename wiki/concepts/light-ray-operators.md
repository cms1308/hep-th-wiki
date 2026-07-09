---
type: concept
title: Light-ray operators
aliases: [light ray operators, light transform]
tags: [conformal-field-theory, light-ray-operators, celestial-holography]
prerequisites: ["conformal-field-theory"]
created: 2026-07-06
updated: 2026-07-06
---

## Definition

Nonlocal CFT operators obtained by integrating a local operator along a complete null
geodesic. The basic example is the *light transform* of a conserved current: on the
Lorentzian cylinder (where null geodesics run from a point $x_i$ to its antipode) a
conserved global symmetry current $J_\mu$ (dimension 2, spin 1 in $d=3$) is smeared as

$$\mathcal L(\phi)=\int_0^\pi d\tau^+\,\sin\tau^+\,J_+(\tau^+,\tau^-{=}0,\phi),$$

one operator per null geodesic, labeled by the angle $\phi$; the weight in the integrand
depends on the operator's dimension and spin (for the stress tensor the ANEC weight is
$\tfrac12\sin^3\tau^+$, see [[anec-operator]]). Light-ray
operators are the natural home of the [[anec-operator|ANEC operator]] and of conformal
collider physics (Hofman–Maldacena 2008); the general theory is due to
Kravchuk–Simmons-Duffin 2018.

## Key formulas

Córdova–Shao (2018) triple in CFT$_3$ on $M^3$ ($ds^2=-dy^+dy^-+dy^2$):
$$\mathcal E(y)=\int dy^+\,T_{++},\qquad \mathcal K(y)=\int dy^+\,y^+T_{++},\qquad
\mathcal N(y)=\int dy^+\,T_{+y},$$
with universal commutators valid in any CFT$_3$ — in Fourier modes on the
[[einstein-cylinder]] circle ([[2603.26459|Strominger–Wei 2026]] eqs. 12–13):
$$[\mathcal E_k,\mathcal E_l]=0,\quad [\mathcal K_k,\mathcal K_l]=0,\quad
[\mathcal K_k,\mathcal E_l]=-i\mathcal E_{k+l},$$
$$[\mathcal N_k,\mathcal E_l]=-l\,\mathcal E_{k+l},\quad
[\mathcal N_k,\mathcal K_l]=-l\,\mathcal K_{k+l},\quad
[\mathcal N_k,\mathcal N_l]=(k-l)\,\mathcal N_{k+l}.$$

For a global symmetry current $J^a_i$, the light transforms obey
$[\mathcal L^a(\phi_1),\mathcal L^b(\phi_2)]=-if^{abc}\delta(\phi_{12})\mathcal L^c(\phi_2)$
(Córdova–Shao) — a $\delta$-function current algebra on the $\phi$ circle.

## Relations

- [[anec-operator]] — the averaged-null-energy member $\mathcal E$; positivity of its
  expectation values is the engine of conformal collider bounds
  ([[hofman-maldacena-bound]]).
- [[s-algebra]] — realized in any CFT$_3$ with a nonabelian conserved current by the light
  transform of $J^a_i$ and its $SO(3,2)$ descendants
  ([[ads4-s-algebra-from-cft3-light-transforms]]).
- [[lambda-deformed-w-algebra]] — realized in any CFT$_3$ by the ANEC operator and its
  $SO(3,2)$ descendants ([[every-cft3-has-l-lambda-w-symmetry]]).
- Under conformal maps, light-ray operators transform with the rules worked out in
  conformal collider physics (Hofman–Maldacena 2008) — used to move between $M^3$ and the
  Einstein cylinder.

## Where it appears

[[2601.00096|Sheta–Strominger–Tropper–Wei 2025]] · [[2603.26459|Strominger–Wei 2026]] ·
conformal collider physics and the [[hofman-maldacena-bound]] · ANEC proofs
(Faulkner–Leigh–Parrikar–Wang 2016; Hartman–Kundu–Tajdini 2016).
