---
type: concept
title: Maximal update parameterization (muP)
aliases: ["muP", "μP", "maximal update parametrization"]
tags: [machine-learning, neural-networks, large-n, gradient-descent]
prerequisites: [physics-for-machine-learning, feature-learning, neural-tangent-kernel]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The **unique width-scaling of a network's weights and learning rate that keeps pre-activations,
predictions, and features all $O(1)$ as $N\to\infty$** — the parameterization in which an
infinitely wide network still performs [[feature-learning|feature learning]], unlike the lazy
[[neural-tangent-kernel|NTK]] limit. It is obtained by carrying undetermined $N$-scaling exponents
$(a_\ell,b_\ell,c,d)$ through the pre-activation covariances, feature kernels, and gradient chain
rules, and demanding three conditions:

1. finite pre-activations,
2. predictions evolve in $O_N(1)$ time,
3. features evolve in $O_N(1)$ time.

## Motivation

Naive width-scalings either blow up the pre-activations or collapse the dynamics into the
feature-frozen [[neural-tangent-kernel|NTK]] regime. $\mu P$ is the scaling that survives all three
requirements, giving a well-defined, learning-rate-stable infinite-width limit that *does* learn
features — practically important because it lets hyperparameters tuned on small models transfer to
large ones.

## Key formulas

The scaling constraints are

$$2a_1+b_1=0,\quad 2a_\ell+b_\ell=1,\quad 2a_1+c=0,\quad 2a_\ell+c=1,$$

with the crucial [[feature-learning|feature-learning]] requirement $d=\tfrac12$. Fixing the learning
rate to be $O_N(1)$ gives $c=1$, the unique maximal update parameterization. The learning-rate
scaling is $\eta=\eta_0\gamma_0^2\,N^{2d-c}$; the lazy / NTK regime is instead $d=0$.

## Relations

- The scaling that turns on [[feature-learning]] at infinite width.
- Contrasts with the lazy [[neural-tangent-kernel|NTK]] limit ($d=0$).
- Belongs to the [[physics-for-machine-learning]] topic.

## Where it appears

- Introduced by Yang (2020); connected to self-consistent dynamical mean-field theory by
  Bordelon–Pehlevan (2022).
- Derived through the $N$-scaling analysis in the dynamics section of [[2408.00082|Halverson 2024]].
