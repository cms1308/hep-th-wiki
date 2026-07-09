---
type: concept
title: Feature learning
aliases: ["feature learning", "lazy vs rich regime", "rich regime"]
tags: [machine-learning, neural-networks, gradient-descent]
prerequisites: [physics-for-machine-learning, neural-tangent-kernel]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The **nontrivial evolution of hidden-layer pre-activations (internal representations) during
training** — the network learning useful intermediate features rather than merely fitting a fixed
representation. It is the property that the lazy / [[neural-tangent-kernel|NTK]] regime *lacks*: in
the frozen-NTK limit the network reduces to kernel regression in a fixed feature space and hidden
layers do not move, so there is no feature learning.

## Motivation

Feature learning is widely believed to be what makes deep networks powerful in practice, so a theory
of the infinite-width limit that *excludes* it (the NTK/lazy regime) is missing the interesting
physics. The question becomes: what $N$-scaling of weights and learning rate keeps a wide network in
the "rich," feature-learning regime? The answer is
[[maximal-update-parameterization|$\mu P$]].

## Key formulas

Feature learning is diagnosed through the layerwise **feature kernel**

$$\Phi^{(\ell)}_{\alpha\beta}=\frac1N\,\sigma\!\big(z^{(\ell)}_{m\alpha}\big)\,
\sigma\!\big(z^{(\ell)}_{m\beta}\big),$$

whose evolution under training must be $O(1)$ for genuine feature learning. Carrying scaling
exponents through the pre-activations and gradients yields the constraint $d=\tfrac12$ for the
feature-learning solution; feature learning fails for $d<\tfrac12$, and the NTK regime sits at
$d=0$ (see [[maximal-update-parameterization]]).

## Relations

- The opposite regime to the lazy [[neural-tangent-kernel|NTK]] limit.
- Realized at infinite width only in [[maximal-update-parameterization|$\mu P$]].
- A deformation away from the free [[neural-network-gaussian-process|NNGP]] point.
- Belongs to the [[physics-for-machine-learning]] topic.

## Where it appears

- Developed via dynamical mean-field theory (Yang 2020; Bordelon–Pehlevan 2022).
- Presented in the dynamics section of [[2408.00082|Halverson 2024]], following Pehlevan–Bordelon.
