---
type: concept
title: Carroll group
aliases: [Carroll algebra, Carrollian limit, ultra-relativistic limit]
tags: [carrollian-physics, kinematics, group-contraction]
prerequisites: []
created: 2026-07-03
updated: 2026-07-03
---

## Definition

The İnönü–Wigner contraction of the Poincaré group obtained by sending the speed of light to
zero. Rescale $x^0 = cu$, boost parameters $\vec\beta = c\vec v$, and take $c\to0$: Lorentz
boosts degenerate into **Carroll boosts**

$$u' = u + \vec v\cdot R\vec x, \qquad \vec x' = R\vec x ,$$

which shift time by a position-dependent amount while leaving space untouched. Space becomes
absolute, time relative — the exact mirror of the Galilean $c\to\infty$ contraction. Light
cones collapse onto the time axis: nothing propagates, and dynamics is **ultra-local**.
Named by [[jean-marc-levy-leblond|Lévy-Leblond]] (1965; independently Sen Gupta 1966) after
Lewis Carroll's Red Queen ("it takes all the running you can do, to keep in the same place").

## Motivation

Originally a curiosity, the Carroll group matters because it is the isometry group of the
degenerate geometry intrinsic to *null hypersurfaces* ([[carrollian-geometry]]) — black hole
horizons and [[null-infinity]] — and because its conformal extension is the
[[bms-symmetry|BMS group]] of asymptotically flat gravity
([[bms-conformal-carroll-isomorphism]]). It thereby underlies [[flat-space-holography]].

## Key formulas

Conventions of [[2602.02644|Ruzziconi 2026]] (topic-canonical). Carroll algebra
$\mathfrak{Carr}_d$ = $\{$rotations $J_{AB}$, Carroll boosts $B_A$, spatial translations
$P_A$, time translation $H\}$ with the non-Lorentzian brackets

$$[B_A, B_B] = 0,\qquad [B_A, P_B] = i\,\delta_{AB} H,\qquad [B_A, H] = 0 ,$$

so $H$ is **central**. Contraction of generators: $B_A \to B_A/c$, $H \to H/c$ as $c\to0$.
The conformal extension at level $N$ ([[conformal-carrollian-algebra]]) satisfies

$$\mathfrak{CCarr}^{\text{glob}}_d \simeq \mathfrak{iso}(d,1)$$

— global conformal Carroll in $d$ dimensions is Poincaré in $d{+}1$ — and admits an
infinite-dimensional supertranslation ideal $M_{\mathcal T} = -i\,\mathcal T(\vec x)\partial_u$.

## Relations

- Mirror contraction to the Galilei group ($c\to\infty$); both sit inside the classification
  of kinematical algebras.
- Isometries of the flat Carroll structure in [[carrollian-geometry]].
- Conformal extension = [[bms-symmetry]] via [[bms-conformal-carroll-isomorphism]].
- Field theories realizing it: [[electric-magnetic-carrollian-theories]], [[carrollian-cft]].

## Where it appears

Foundational for the [[carrollian-physics]] topic; reviewed in depth in
[[2602.02644|Ruzziconi 2026]] §2. Original papers: Lévy-Leblond 1965, Sen Gupta 1966.
