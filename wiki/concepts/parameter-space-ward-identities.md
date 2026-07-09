---
type: concept
title: Parameter-space Ward identities and anomalies
aliases: ["breaking function", "score-based Ward identities", "NN-FT anomalies", "parameter-space Schwinger-Dyson"]
tags: [machine-learning, neural-networks, nn-ft, ward-identity, anomaly, symmetry]
prerequisites: [neural-network-field-theory]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

The formalism that reproduces Ward identities, conservation laws, Schwinger–Dyson equations, and
anomalies for a [[neural-network-field-theory|NN-FT]] by a **change of variables in the parameter
integral** rather than the path integral. Introduced in Ferko et al. 2026, presented in
[[2607.02905|Halverson 2026]]. It applies at any width and architecture, even finite width and even
for non-local ensembles.

## Motivation

In the path integral, Ward identities and anomalies follow from acting with a symmetry on the field
and asking whether the integral and its measure are invariant. NN-FT has *its own* integral, over
parameters, so the same change-of-variables logic applied there generates analogous machinery — with
the score playing the role the equation of motion plays in field space.

## Key formulas

**Score.** For a parameter density $p(\theta)>0$, $s_a(\theta)=\partial_a\log p(\theta)$ (the object
learned by score-based generative models).

**Master identity.** For any smooth observable $\mathcal O$, integrating a total derivative in
parameter space (boundary terms dropped) gives one identity per parameter,
$\langle\partial_a\mathcal O\rangle=-\langle s_a\mathcal O\rangle$, and contracting against a smooth
vector field $\xi=\xi^a\partial_a$ promotes it to
$$\Big\langle\sum_a\xi^a\partial_a\mathcal O\Big\rangle=-\langle B(\theta)\,\mathcal O\rangle+(\text{boundary}),\qquad
B(\theta)=\underbrace{\sum_a\xi^a s_a}_{\text{score}}+\underbrace{\sum_a\partial_a\xi^a}_{\text{Jacobian}},$$
with $B$ the **breaking function** of the flow $\xi$. No symmetry is assumed — every flow has one.
Field variations are induced by parameter flows, $\delta_\xi\phi(x)=\sum_a\xi^a\partial_a\phi(x)$;
taking $\mathcal O$ a product of fields turns this into $n$-point Schwinger–Dyson equations.

**Conservation.** Since $pB=\sum_a\partial_a(\xi^a p)$,
$$B=0\iff\partial_a j^a=0,\qquad j^a=\xi^a p,$$
a divergence-free current on *parameter space* (not a local spacetime current). When a local
Lagrangian exists, the spacetime current is recovered by fiber-averaging $B$ over parameters mapping
to a fixed field, then invoking locality.

**Score vs Jacobian.** The score term carries *explicit* breaking (it vanishes when the density is
invariant along the flow); the Jacobian term is density-independent and measures the failure of the
flat measure $d\theta$ to be invariant — a finite-dimensional avatar of the **Fujikawa anomaly**.

## Relations

- The **general case** of the [[neural-network-gaussian-process|NNGP]]/[[neural-network-field-theory|NN-FT]]
  symmetry story: it subsumes the "absorption mechanism" (realize a symmetry by absorbing the group
  action into a parameter reparameterization and checking measure invariance).
- Sanity checks: input rotations of a Gaussian-initialized net give the unbroken rotational Ward
  identity (both score and Jacobian vanish); the query/key rotation of attention returns a *gauge*
  redundancy with a trivial Ward identity.
- Reproduces the massless $4d$ $\phi^4$ scale anomaly — a Gaussian integration by parts converts the
  score insertion into the connected four-point function, giving the one-loop
  $\beta(\lambda)=3\lambda^2/16\pi^2+O(\lambda^3)$.
- Directly powers the [[critical-dimension-from-mode-counting-nn-ft|$D=26$ derivation]], where a Weyl
  flow leaves only the Jacobian mode count.

## Where it appears

- Introduced in [[2607.02905|Halverson 2026]] §Day 2 (Anomalies and Ward Identities), from Ferko et
  al. 2026; belongs to the [[physics-for-machine-learning]] topic.
