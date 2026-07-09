---
type: concept
title: Schur superfield
aliases: [Schur superfield, Schur multiplet superfield]
tags: [holomorphic-twist, vertex-operator-algebra, n2-scft, superconformal-deformation]
prerequisites: [holomorphic-twist, semi-chiral-superfield, higher-super-virasoro-algebra]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A **Schur superfield** is the object that survives the
[[superconformal-deformation-to-voa|superconformal deformation]] of the
[[holomorphic-twist|holomorphic twist]] and generates the associated
[[scft-voa-correspondence|vertex operator algebra]]. It extends a
[[semi-chiral-superfield|semi-chiral superfield]] $\mathbf O$ by one extra component along the
localizing plane,
$$\mathbb O=\mathbf O+dz^2\,\Psi_{\mathbf O},\qquad
\Psi_{\mathbf O}=\{\widetilde{\mathbf G}{}_{(0,0)}\mathbf O\},$$
and is closed under the deformed differential
$$\mathbb Q\,\mathbb O=(\bar\partial+\iota_{z^2\partial_2})\,\mathbb O.$$
The deformation by $\int z^2\widetilde{\mathbf G}$ (with $\widetilde{\mathbf G}$ the extra
generator of $\mathfrak{svir}(2|1)$) localizes the 4d holomorphic theory to the plane $z^2=0$,
turning it into a genuine 2d holomorphic theory — the VOA — whose generators are the Schur
superfields.

## Motivation

The Beem-et-al SCFT/VOA correspondence was originally a separate construction. Recasting it as a
deformation of the holomorphic twist requires an object that interpolates between the 4d
semi-chiral superfield and the 2d VOA generator: the Schur superfield is exactly that
interpolant, and its extra component $\Psi_{\mathbf O}$ is what the deformation "switches on".

## Key formulas

- Stress tensor: $\mathbb T=\mathbf G_1+dz^2\big(\mathbf S_1-\tfrac13\partial_1\mathbf R\big)$
  yields the 2d stress tensor with
  $\{\!\{\mathbb T{}_\lambda\mathbb T\}\!\}=\partial_1\mathbb T+2\lambda\mathbb T-c\,\lambda^3$,
  i.e. $c_{2d}=-12c$.
- Affine currents: $\mathbb J_a=\boldsymbol\mu_a+dz^2\,\mathbf J_a$ at level $k_{2d}=-\tfrac12 k_F$.
- Free hypermultiplet: the Schur superfields generate the **symplectic boson VOA**.

## Relations

- Deformation partner of the [[semi-chiral-superfield]]; generated using the extra current of
  [[higher-super-virasoro-algebra|$\mathfrak{svir}(2|1)$]].
- Its brackets are computed from the 4d [[holomorphic-lambda-bracket|$\lambda$-brackets]] via the
  extraction rule of [[superconformal-deformation-to-voa]].
- Realizes the local content of [[scft-voa-correspondence]] inside the holomorphic-twist framework.

## Where it appears

- Introduced in ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]].
