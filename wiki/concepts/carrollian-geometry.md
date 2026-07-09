---
type: concept
title: Carrollian geometry
aliases: [Carroll structure, Carrollian manifold]
tags: [carrollian-physics, differential-geometry, null-hypersurfaces]
prerequisites: ["carroll-group"]
created: 2026-07-03
updated: 2026-07-03
---

## Definition

A **Carrollian structure** on a $d$-dimensional manifold is a pair $(q_{ab}, n^a)$: a
degenerate metric of signature $(0,+,\cdots,+)$ together with a nowhere-vanishing vector
field spanning its kernel, $q_{ab}n^b = 0$. It is the $c\to0$ degeneration of a Lorentzian
metric, invariant under the [[carroll-group]]. An **Ehresmann connection** $k_a$ (normalized
$k_a n^a = -1$, conventions of [[2602.02644|Ruzziconi 2026]]) fixes a horizontal
distribution; it is defined only up to Carroll boosts $\delta_\lambda k_a = \lambda_a$
($\lambda_a n^a = 0$), so no boost-invariant notion of "constant time slices" exists.

## Motivation

This is precisely the geometry a **null hypersurface** inherits from an ambient Lorentzian
manifold: the induced metric is degenerate, its kernel is the null generator. Black hole
horizons and [[null-infinity]] are therefore Carrollian manifolds — the geometric reason
Carrollian physics enters gravity and [[flat-space-holography]].

## Key formulas

- Projector: $q^a{}_b = \delta^a_b + n^a k_b$.
- Flat Carroll structure (on $\mathbb R_u\times\mathbb C_z$): $n = \partial_u$,
  $q = 2\,dz\,d\bar z$, $k = -du$.
- Extrinsic curvature (expansion tensor): $\theta_{ab} = \tfrac12\mathcal L_n q_{ab}$.
- **Failure of the fundamental theorem of (pseudo-)Riemannian geometry**: a torsion-free
  connection compatible with $(q_{ab}, n^a)$ exists **iff** $\theta_{ab} = 0$. Generically a
  piece of torsion is geometrically fixed, $T_{(I|0|J)} = \theta_{IJ}$ — Carrollian
  connections are naturally torsional whenever the structure "expands" along $n$.
- Conformal Killing equations at level $N$:
  $\mathcal L_\xi q_{ab} = 2\alpha\, q_{ab}$, $\mathcal L_\xi n^a = -\tfrac{2\alpha}{N} n^a$
  (dynamical exponent $z = 2/N$; $N{=}2$ is the [[bms-symmetry|BMS]]-relevant case). On the
  flat structure with $N=2$: $\xi = (\mathcal T + u\,\alpha)\partial_u + \mathcal Y\partial +
  \bar{\mathcal Y}\bar\partial$.
- Symmetry hierarchy: $\mathfrak{Carr}_d \subset \mathfrak{Carriso}_d \subset
  \mathfrak{CCarr}_{d,N} \subset \mathfrak{NU}_d \subset \mathfrak{Carrdiff}_d$.

## Relations

- Isometry algebra: [[carroll-group]]; conformal symmetries:
  [[conformal-carrollian-algebra]] $\simeq$ [[bms-symmetry|BMS]].
- Induced on any null hypersurface via the rigging construction ($\ell^\mu$ with
  $n_\mu\ell^\mu = -1$); the ambient Levi-Civita connection induces exactly the
  geometrically-allowed torsional Carrollian connection.
- The [[null-brown-york-stress-tensor]] is the Carrollian stress tensor of a null boundary;
  its conservation reproduces the Raychaudhuri and Damour equations
  ([[membrane-paradigm]]).
- Newman–Penrose/GHP calculus is adapted Carrollian frame calculus
  ($\text{þ}' = n^aD_a$, $\eth = m^aD_a$).

## Where it appears

[[2602.02644|Ruzziconi 2026]] §3–4 (systematic treatment); Henneaux 1979 and
[[1402.5894|Duval–Gibbons–Horvathy 2014]] (foundations); underlies every page in
[[carrollian-physics]] and the boundary side of [[flat-carrollian-limit-correspondence]].
