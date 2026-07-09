---
type: concept
title: Universal Approximation Theorem
aliases: ["UAT", "universal approximation", "Cybenko theorem"]
tags: [machine-learning, neural-networks, expressivity]
prerequisites: [physics-for-machine-learning]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A single-hidden-layer feedforward network with a non-polynomial nonlinearity $\sigma$,

$$\phi(x)=\sum_{i=1}^{N}\sum_{j=1}^{d} w_i^{(1)}\,\sigma\!\big(w^{(0)}_{ij}x_j+b^{(0)}_i\big)+b^{(1)},$$

can approximate any continuous function $f$ on a compact set $K$ to any accuracy:

$$\sup_{x\in K}\,|f(x)-\phi(x)|<\epsilon .$$

## Motivation

The baseline expressivity guarantee of [[physics-for-machine-learning|neural network theory]]:
networks are, in principle, universal function approximators. Its **limitation** is the crucial
caveat for a theory of learning — it is an *existence* statement about a good parameter set
$\theta^\ast$, saying nothing about how many neurons are needed or whether gradient descent can
*find* $\theta^\ast$. Trainability is the province of the dynamics pillar
([[neural-tangent-kernel]], [[feature-learning]]).

## Key formulas

The approximation statement above; the architecture is the same single-hidden-layer form whose
infinite-width ensemble gives the [[neural-network-gaussian-process|NNGP]].

## Relations

- Expressivity counterpart to the exact [[kolmogorov-arnold-network|Kolmogorov–Arnold representation]].
- Silent on trainability, which is addressed by [[neural-tangent-kernel]] and
  [[feature-learning]].
- Belongs to the [[physics-for-machine-learning]] topic.

## Where it appears

- Cybenko (1989) for sigmoid activations; Hornik (1991) for the multi-layer / general-activation
  generalization.
- Opens the expressivity section of [[2408.00082|Halverson 2024]].
