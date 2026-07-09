---
type: concept
title: Neural Tangent Kernel (NTK)
aliases: ["NTK", "tangent kernel", "lazy training"]
tags: [machine-learning, neural-networks, gradient-descent, large-n]
prerequisites: [physics-for-machine-learning, neural-network-gaussian-process]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The kernel that controls a network's evolution under gradient descent. For network output
$\phi(x)$ and parameters $\theta_i$,

$$\Theta(x,x')=\partial_{\theta_i}\phi(x)\,\partial_{\theta_i}\phi(x')$$

(summed over parameters). Under gradient descent with learning rate $\eta$ on a dataset
$\mathcal D$, the output flows as

$$\frac{d\phi(x)}{dt}=\frac{\eta}{|\mathcal D|}\sum_\alpha \Delta(x_\alpha)\,\Theta(x,x_\alpha),$$

where $\Delta(x_\alpha)$ is the residual on training point $x_\alpha$. In the infinite-width
**"lazy" regime** the parameters barely move, $|\theta(t)-\theta(0)|\ll1$, the network is linear in
its parameters, and the NTK **freezes** at its deterministic initialization value $\bar\Theta$.

## Motivation

It makes the dynamics pillar of [[physics-for-machine-learning|NN field theory]] exactly solvable at
infinite width: with a frozen, deterministic kernel the training ODE is linear, and training reduces
to kernel regression. It is the dynamical companion of the
[[neural-network-gaussian-process|NNGP]] Gaussian point.

## Key formulas

With frozen $\bar\Theta$ and MSE loss, training to infinite time gives kernel regression:

$$\phi_\infty(x)=\phi_0(x)+\bar\Theta(x,x_\alpha)\,\bar\Theta_{\alpha\beta}^{-1}
\big(y_\beta-\phi_0(x_\beta)\big),$$

exact memorization on training points ($\phi_\infty(x_\alpha)=y_\alpha$) and interpolation
elsewhere. The ensemble mean prediction is

$$\mu_\infty(x)=\bar\Theta(x,x_\alpha)\,\bar\Theta_{\alpha\beta}^{-1}\,y_\beta$$

— the mean of infinitely many infinitely-wide networks trained to infinite time.

## Relations

- Freezes at the [[neural-network-gaussian-process|NNGP]] Gaussian point; the frozen-NTK solution is
  the [[nngp-correspondence|kernel-regression]] result.
- Its central limitation — **no [[feature-learning|feature learning]]**, since hidden layers do not
  move — motivates [[maximal-update-parameterization|$\mu P$]]. In the $\mu P$ scaling language the
  lazy/NTK regime is the point $d=0$.
- Belongs to the [[physics-for-machine-learning]] topic.

## Where it appears

- Introduced by Jacot–Gabriel–Hongler (2018); the wide-network linearization and exact-training
  solution by Lee et al. (2019).
- Presented as the dynamics pillar in [[2408.00082|Halverson 2024]].
