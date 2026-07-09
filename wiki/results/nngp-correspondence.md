---
type: result
title: NNGP correspondence (infinite-width networks are Gaussian processes)
aliases: ["NNGP correspondence", "Neal's theorem", "NN-GP theorem"]
tags: [machine-learning, neural-networks, field-theory, large-n]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

In the infinite-width limit, a randomly initialized feedforward neural network converges to a
**Gaussian process** — a generalized free field with quadratic action, fully specified by its mean
and its two-point kernel $G^{(2)}$. All connected correlators above second order vanish. The result
holds for width in fully-connected networks, channels in CNNs, and heads in attention networks.

## Derivation sketch

A biasless single-hidden-layer network
$\phi(x)=\frac1{\sqrt N}\sum_i w_i^{(1)}\sigma(w^{(0)}_{ij}x_j)$ is a sum of $N$ i.i.d. neuron
functions. A functional central limit theorem then gives a Gaussian limit. Concretely, the cumulants
of the width-$N$ sum scale as $\kappa_r^\phi=\kappa_r^{X}/N^{r/2-1}$, so every $\kappa_{r>2}\to0$ as
$N\to\infty$. The surviving second cumulant is the exact-in-$N$ kernel

$$G^{(2)}(x,y)=\mu_2\,\big\langle\sigma(w^{(0)}_{ij}x_j)\,\sigma(w^{(0)}_{il}y_l)\big\rangle\quad
(\text{no sum on }i).$$

See [[neural-network-gaussian-process]] for the concept page.

## Assumptions

- Neuron functions are independent and identically distributed with finite second moments.
- Width (or channels / heads) taken strictly to infinity — finite $N$ or broken independence
  violate the CLT and reinstate connected correlators.

## Status

**Established.** Proven by Neal (1996), with the explicit parameter-space kernel computation by
Williams (1997); subsequently extended to deep, convolutional, and attention architectures.

## Implications

- Identifies the exactly solvable **free-field** point of
  [[physics-for-machine-learning|neural-network field theory]]; the free action is the inverted
  kernel $S[\phi]=\int\phi\,G^{(2)-1}\phi$.
- Finite-width $1/N$ corrections and independence-breaking are the two knobs that turn on
  interactions (see [[neural-network-field-theory]]).
- Combined with a frozen [[neural-tangent-kernel]], gradient descent at this point becomes exactly
  solvable kernel regression.
