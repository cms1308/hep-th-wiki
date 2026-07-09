---
type: result
title: Every CFT3 has an L_Lambda w(1+infinity) symmetry
aliases: [ANEC descendants generate deformed w-algebra]
tags: [celestial-holography, ads-cft, light-ray-operators, gravity]
status: established
created: 2026-07-06
updated: 2026-07-06
---

## Statement

In any CFT$_3$, the [[anec-operator|ANEC operator]] on the [[einstein-cylinder]] EC$^3$,
its $SO(3,2)$ conformal descendants, and their commutators generate the
[[lambda-deformed-w-algebra|$\mathcal L_\Lambda w_{1+\infty}$ algebra]] at $\Lambda=-1$:
$$\bigl[w^p_{\bar m,m},w^q_{\bar n,n}\bigr]
=\bigl(\bar m(q-1)-\bar n(p-1)\bigr)w^{p+q-2}_{\bar m+\bar n,m+n}
+\bigl(m(q-2)-n(p-2)\bigr)w^{p+q-1}_{\bar m+\bar n,m+n},$$
with exactly one generator per lattice point $(p,\bar m,m)$,
$p\pm m,\,p\pm\bar m\in\mathbb Z$, in the wedge $\bar m+p\ge1$, $m-p\ge-2$ — closed under
commutation, with ANEC modes saturating the boundary
([[2603.26459|Strominger–Wei 2026]]).

## Derivation sketch

1. Map the Córdova–Shao [[light-ray-operators]] $\mathcal E,\mathcal K,\mathcal N$ (with
   their universal CFT commutators) from $M^3$ to EC$^3$, where null lines run between
   antipodal points.
2. Light-transform the ten $SO(3,2)$ conformal-Killing-vector currents
   $j_{A\mu}=T_{\mu\nu}\zeta_A^\nu$; Fourier modes on the $\phi$ circle give the seed
   $w$-generators, with the ANEC modes as $SO(3,2)$ lowest weight (single representation,
   Casimir 6).
3. Raising operators populate the wedge lattice (a constructive argument routes around
   points with vanishing coefficients); Cartan weights fix the commutator's
   $(\bar m+\bar n,m+n)$ labels, eventual annihilation under repeated lowering restricts
   it to $A\,w^{p+q-2}+B\,w^{p+q-1}$, and lowering plus Jacobi identities fix $A,B$ to the
   $\mathcal L_\Lambda w_{1+\infty}$ values.

## Assumptions

Only a conserved stress tensor and the universal light-ray commutators (Córdova–Shao,
valid in any CFT$_3$) — no gravity dual, no weak coupling, no supersymmetry.

## Status

**Established** as an exact operator algebra in any CFT$_3$; extends the tree-level bulk
AdS$_4$ discoveries of the deformed algebra (Taylor–Zhu 2023; Bittleston et al. 2024;
Mago–Ren–Yelleshpur Srikant–Volovich 2023) to the strongly-coupled quantum regime. Operators outside the wedge are not produced by the
construction. The bulk derivation with Dirichlet boundary conditions and the dS case
remain open ([[soft-algebras-for-gravity-in-ads4]]).

## Implications

- Quantum gravity on AdS$_4$ inherits a nonperturbative
  $\mathcal L_\Lambda w_{1+\infty}$ symmetry through its dual — the gravity counterpart of
  [[ads4-s-algebra-from-cft3-light-transforms]], with the conformal non-invariance of
  gravity showing up as the $\Lambda$-deformation.
- A universal infinite-dimensional structure in *every* CFT$_3$, whether or not it is
  holographic; what it constrains dynamically is unexplored.

Source: [[2603.26459|Strominger–Wei 2026]].
