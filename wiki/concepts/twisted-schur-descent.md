---
type: concept
title: Twisted Schur descent
aliases: [Lorentzian topological descent, twisted descent, descent web]
tags: [n2-scft, extended-operators, cohomology, topological-descent]
prerequisites: [schur-operators, twisted-schur-supercharges]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

**Twisted Schur descent** is a Lorentzian generalization of Witten's topological descent that
builds **extended** operators — lines, surfaces, domain walls — from local
[[schur-operators]] inside the cohomology of the [[twisted-schur-supercharges]] $\mathbb T_\pm$.
Given a $\mathbb T$-closed operator $\mathcal E$ and a $\mathbb T$-exact bosonic generator
$X = \mathbb T\circ\xi$ (so $\xi$ is a fermionic "descent" charge), the descent operator is the
world-volume integral
$$\mathbf D^X[\mathcal E] \doteq \int d\alpha\; \xi\circ e^{\alpha X}\circ\mathcal E,$$
where $\circ$ is the adjoint (super)commutator action and $\alpha$ parameterizes the world-volume
direction. Each application raises the world-volume dimension by one, flips statistics, shifts
the $U(1)_r$ charge by $\pm1$, and preserves the chiral weight $h_{\mathcal O}$.

## Motivation

Topological descent (Witten 1988) turns a local operator of a twisted SUSY theory into a
$p$-form that can be integrated over a $p$-cycle to give a new closed extended operator. Here the
theory is not topological — it is a physical 4d $\mathcal N=2$ SCFT — but the same machine works
inside $\mathbb T_\pm$-cohomology, and the resulting extended operators inherit the meromorphy of
Schur operators. This is what enlarges the Schur VOA into an [[extended-vertex-algebra]].

## Key formulas

- **Non-topological double closedness.** Although $\mathbf D^{N_+}[\mathcal E]$ is built from a
  $\mathbb T_+$-exact generator, it is *also* $\mathbb T_-$-closed:
  $$\mathbb T_-\circ\mathbf D^{N_+}[\mathcal E]
    = -\int d\alpha\;\nu_+\circ e^{\alpha N_+}\circ(\mathbb T_- + \alpha\nu_+)\circ\mathcal E = 0.$$
  For local Schur operators this follows from unitarity; here it follows from the detailed
  superconformal algebra and has **no analog in topological descent**. It is the identity that
  makes descent correlators meromorphic in $z$.
- **The descent web is finite.** Using the twisted conformal group $\widehat{SO}(1,3)$ of the
  VOA plane, the $\mathbb{RP}^3$ of possible generators collapses to **10 inequivalent
  descents** per level:
  $$\mathbf D^{P_\pm},\ \mathbf D^{M_{\pm3}},\ \mathbf D^{K_\pm},\ \mathbf D^{P_\pm+K_\pm},\ \mathbf D^{P_\pm-K_\pm}.$$
  Descent **terminates at world-volume dimension 3** (domain walls) — no 4d volume operators
  arise. The classes are $\mathbf L^\pm$ (lines), $\mathbf S,\widehat{\mathbf S}_{L,R}$
  (surfaces), and $\widehat{\mathbf W}^\pm$ (walls).
- **Hatted vs. unhatted.** Operators reachable only via the rotation descent $M_{\pm3}$ — the
  "hatted" $\widehat{\mathbf S},\widehat{\mathbf W}^\pm$ — have correlators with sign
  discontinuities ("boost" and VOA-plane "intersection" discontinuities), so they behave as
  boundary/line operators rather than genuine vertex operators.

## Relations

- Acts on [[schur-operators]] inside the cohomology of the [[twisted-schur-supercharges]].
- Produces the operators of the [[extended-vertex-algebra]].
- The line operators $\mathbf L^\pm$ are close cousins of [[light-ray-operators]].
- Descent correlators diverge generically and are tamed by
  [[weight-function-regularization]].

## Where it appears

- [[2211.04410|Argyres-Lotito-Weaver 2022]] — introduces the construction; the free
  hypermultiplet $\mathcal O$–$\mathbf L^\pm$–$\mathbf S$ OPEs are in
  [[free-hypermultiplet-extended-va-opes]].
