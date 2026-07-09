---
type: concept
title: Neural Network / Gaussian Process (NNGP) correspondence
aliases: ["NNGP", "NN-GP correspondence", "infinite-width Gaussian process"]
tags: [machine-learning, neural-networks, field-theory, large-n]
prerequisites: [physics-for-machine-learning]
created: 2026-07-07
updated: 2026-07-08
---

## Definition

At infinite width, a randomly initialized feedforward neural network is a **Gaussian process** — in
field-theory language, a **generalized free field** with purely quadratic action. Take a biasless
single-hidden-layer network

$$\phi(x)=\frac{1}{\sqrt N}\sum_{i=1}^{N} w_i^{(1)}\,\sigma\!\big(w^{(0)}_{ij}x_j\big),$$

with i.i.d. (independent and identically distributed) weights. It is a sum of $N$ i.i.d. neuron
functions, so by a functional central limit
theorem the $N\to\infty$ ensemble over initializations is Gaussian: $\phi\sim\mathcal N(\mu,K)$,
fully specified by its mean and its two-point kernel. All higher connected correlators vanish, so the
theory is free.

## Motivation

It identifies the exactly solvable point of the [[physics-for-machine-learning|NN field-theory]]:
the infinite-width network is a free field, and everything interesting (finite-width corrections,
[[feature-learning|feature learning]]) is a deformation away from it. It is the statistics-pillar
analog of a Gaussian fixed point.

## Key formulas

Exact-in-$N$ two-point kernel (no sum on $i$):

$$G^{(2)}(x,y)=\mu_2\,\big\langle\sigma(w^{(0)}_{ij}x_j)\,\sigma(w^{(0)}_{il}y_l)\big\rangle,$$

with $\mu_2$ the second moment of the last-layer weights. The corresponding free action is obtained
by inverting the kernel,

$$S[\phi]=\int d^dx\,d^dy\;\phi(x)\,G^{(2)}(x,y)^{-1}\,\phi(y),\qquad
\int d^dy\;G^{(2)-1}(x,y)\,G^{(2)}(y,z)=\delta^{(d)}(x-z).$$

Cumulant scaling behind the CLT: a width-$N$ sum of i.i.d. neurons has
$\kappa_r^{\phi}=\kappa_r^{X}/N^{r/2-1}$, so every $\kappa_{r>2}\to0$ as $N\to\infty$.

## Relations

- The free/Gaussian limit of [[neural-network-field-theory]]; interactions are the $1/N$ and
  independence-breaking corrections away from it.
- Frozen at this Gaussian point, gradient descent becomes kernel regression via the
  [[neural-tangent-kernel]].
- Deviations from Gaussianity are the subject of [[feature-learning]] and finite-width effective
  field theory.
- Belongs to the [[physics-for-machine-learning]] topic.

## Where it appears

- Established by Neal (1996) and Williams (1997); generalized to deep, convolutional, and attention
  architectures (width → channels → heads).
- Reviewed as the statistics pillar in [[2408.00082|Halverson 2024]]; the formal statement is
  [[nngp-correspondence]].
