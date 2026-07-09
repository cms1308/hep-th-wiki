---
type: concept
title: Kolmogorov-Arnold Network (KAN)
aliases: ["KAN", "Kolmogorov-Arnold network", "Kolmogorov-Arnold representation theorem", "KART"]
tags: [machine-learning, neural-networks, expressivity, interpretability]
prerequisites: [physics-for-machine-learning, universal-approximation-theorem]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

An architecture with **learned activation functions on the edges** (not fixed activations on the
nodes), motivated by the **Kolmogorov–Arnold representation theorem**: any continuous
$f:[0,1]^n\to\mathbb R$ is *exactly*

$$f(x_1,\dots,x_n)=\sum_{q=0}^{2n}\Phi_q\!\Big(\sum_{p=1}^{n}\phi_{q,p}(x_p)\Big),$$

a finite superposition of univariate functions $\phi_{q,p},\Phi_q$ and addition. In a KAN those
univariate functions are the learnable objects; because each learned edge-function is one-dimensional
it can often be read off as an interpretable symbolic formula.

## Motivation

An expressivity result complementary to the [[universal-approximation-theorem|universal approximation theorem]]:
where UAT is an existence statement about approximation, the
Kolmogorov–Arnold theorem is an *exact* representation with a fixed, finite structure. KANs are cited
in [[physics-for-machine-learning|these lectures]] as a case study in mining classical approximation
theory for architectures — and as a route to interpretability, since the learned pieces are
univariate.

## Key formulas

The representation theorem above (Kolmogorov & Arnold, 1957) is the defining equation; the network
replaces each $\phi_{q,p}$ and $\Phi_q$ with a trainable univariate function.

## Relations

- Complements the [[universal-approximation-theorem]] on the expressivity side of
  [[physics-for-machine-learning]].
- Cited as motivation for the "mine approximation theory for new architectures" open direction.

## Where it appears

- Representation theorem: Kolmogorov & Arnold (1957). KAN architecture: Liu et al. (2024).
- Discussed in the expressivity section of [[2408.00082|Halverson 2024]].
