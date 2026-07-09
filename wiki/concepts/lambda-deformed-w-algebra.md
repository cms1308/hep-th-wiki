---
type: concept
title: Lambda-deformed w(1+infinity) algebra
aliases: [L_Lambda w_{1+infinity}, deformed w-algebra]
tags: [celestial-holography, ads-cft, soft-theorems, gravity]
prerequisites: ["lw-infinity-algebra"]
created: 2026-07-06
updated: 2026-07-06
---

## Definition

The one-parameter (cosmological-constant) deformation of the flat-space
[[lw-infinity-algebra|$\mathcal Lw_{1+\infty}$]] soft algebra
([[2603.26459|Strominger–Wei 2026]] eq. 1):

$$\bigl[w^p_{\bar m,m},\,w^q_{\bar n,n}\bigr]
=\bigl(\bar m(q-1)-\bar n(p-1)\bigr)\,w^{p+q-2}_{\bar m+\bar n,\,m+n}
\;-\;\Lambda\,\bigl(m(q-2)-n(p-2)\bigr)\,w^{p+q-1}_{\bar m+\bar n,\,m+n}.$$

At $\Lambda=0$ the loop index $m$ is inert and the algebra is $\mathcal Lw_{1+\infty}$; at
$\Lambda\neq0$ a second structure constant turns on, raising $p+q-2\to p+q-1$ with
loop-index-dependent coefficients. The deformation is Jacobi-consistent and preserves a
global $SO(3,2)$ subalgebra.

## Motivation

Gravity — unlike 4d Yang–Mills — is not conformally invariant, so its flat-space soft
algebra cannot simply be transported to AdS$_4$: the cosmological constant *deforms* it
rather than leaving it intact. The algebra was discovered by perturbing flat-space
celestial OPEs with a cosmological-constant interaction (Taylor–Zhu 2023) and via a
twistor deformation of self-dual gravity to negative curvature
(Bittleston–Bogna–Heuveline–Kmec–Mason–Skinner 2024); related deformations appeared in
Mago–Ren–Yelleshpur Srikant–Volovich 2023.

## Key formulas

- **CFT$_3$ realization at $\Lambda=-1$**: the [[anec-operator|ANEC]]
  Fourier modes are $\mathcal E_k=-i^k\,w^{\frac{3+k}{2}}_{-\frac{k+1}{2},\frac{k-1}{2}}$,
  and light transforms of the ten $SO(3,2)$ conformal-Killing-vector currents supply the
  remaining seed generators ([[2603.26459|Strominger–Wei 2026]] eq. 37).
- **Wedge subalgebra**: the construction produces exactly one generator for each
  $(p,\bar m,m)$ with $p\pm m,\,p\pm\bar m\in\mathbb Z$ in the wedge
  $$\bar m+p\ge 1,\qquad m-p\ge -2,$$
  closed under commutation, with ANEC modes saturating the boundary. A generator
  redefinition maps it to the "plane-model" wedge algebra of Bittleston et al. and
  Heuveline.

## Relations

- $\Lambda\to0$: [[lw-infinity-algebra]]. Gauge-theory analogue: the [[s-algebra]], which
  is *undeformed* in AdS$_4$ because Yang–Mills is conformally invariant
  ([[2601.00096|Sheta et al. 2025]]).
- Realized nonperturbatively in every CFT$_3$ by [[light-ray-operators]]
  ([[every-cft3-has-l-lambda-w-symmetry]]); previously seen only at tree level in bulk
  AdS$_4$ gravity.
- The dS ($\Lambda>0$) interpretation is open ([[soft-algebras-for-gravity-in-ads4]]).

## Where it appears

[[2603.26459|Strominger–Wei 2026]] (CFT$_3$ realization) ·
[[2601.00096|Sheta et al. 2025]] (anticipated gravity analogue) ·
[[2606.08582|Alday–Strominger 2026]] (context for the flat-space planar question).
