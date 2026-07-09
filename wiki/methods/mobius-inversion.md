---
type: method
title: Möbius inversion (on the partition lattice)
aliases: [Möbius inversion, Möbius inversion formula]
tags: [combinatorics, quantum-information, multipartite-entanglement]
prerequisites: [partition-lattice]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

Given a quantity written as a sum over a poset — $g(\pi)=\sum_{\kappa\le\pi}f(\kappa)$ — Möbius
inversion recovers the summand $f$ from the cumulative $g$. On the [[partition-lattice]] it is the
tool that isolates, from a family of partition-labeled [[local-unitary-invariant|LU-invariants]],
the specific combinations that vanish on all separable states — i.e. the
[[entanglement-signal|signals and pre-signals]].

## Prerequisites

- The [[partition-lattice]] $\Pi_X$: refinement order, meet $\wedge$/join $\vee$, and its
  [[partition-lattice|Möbius function]] $\mu(\kappa,\pi)=\prod_{B\in\pi}(-1)^{k_B-1}(k_B-1)!$.

## How it works

**Inversion formula.** For functions $f,g:\Pi_X\to A$ into an abelian group $A$,
$$g(\pi)=\sum_{\kappa\le\pi}f(\kappa)\quad\Longleftrightarrow\quad
  f(\pi)=\sum_{\kappa\le\pi}\mu(\kappa,\pi)\,g(\kappa),$$
and identically with $\le$ replaced by $\ge$. The relation is the poset generalization of
inclusion–exclusion, and — passing from cumulative sums to their "connected" parts — it is the same
move as **moments $\to$ cumulants** in probability (Speed 1983).

**Solving meet-vanishing constraints.** Encode coefficients as $V=\sum_\pi c_\pi\,\pi$ in the group
algebra $\mathbb C[\Pi_X]$ with $\wedge$ bilinear. To impose $V\wedge\kappa=0$ for all $\kappa$ in a
set $\mathcal K$, define the **Möbius vectors**
$$M_\rho:=\sum_{\pi\le\rho}\mu(\pi,\rho)\,\pi.$$
They satisfy the key eigen-identity
$$M_\rho\wedge\kappa=\begin{cases}M_\rho,&\rho\le\kappa,\\[2pt]0,&\text{otherwise.}\end{cases}$$
Hence the most general solution of $V\wedge\mathcal K=0$ is $V=\sum_{\rho\in\mathcal N}a_\rho M_\rho$,
where $\mathcal N=\Pi_X\setminus\downarrow\!\mathcal K$ is the complement of the downset (refinement
closure) of $\mathcal K$, and the $M_\rho$ are linearly independent.

## Regime of validity

Any locally finite poset admits Möbius inversion. On $\Pi_X$ the block-product formula for $\mu$
makes everything explicit; the meet-vanishing solution requires the target to be a
[[local-unitary-invariant|compatible family]], so that $f_\pi(|\psi\rangle_\kappa)=
f_{\pi\wedge\kappa}(|\psi\rangle_\kappa)$ turns each separability constraint into a linear
meet-vanishing condition on $V$.

## Canonical applications

- **[[entanglement-signal|Signals]]**: with $\mathcal K$ = the singleton cuts of type $(1,q-1)$,
  $\mathcal N$ = partitions with no size-1 block; $\sum_{\rho\in\mathcal N}a_\rho M_\rho[f]$ (where
  $M_\rho[f]=\sum_{\pi\le\rho}\mu(\pi,\rho)f_\pi$) spans the additive-signal space.
- **[[entanglement-signal|Pre-signals]]**: with $\mathcal K=\Pi_X\setminus\{\mathbf 1\}$,
  $\mathcal N=\{\mathbf 1\}$, giving the unique
  $M_{\mathbf 1}[\tilde f]=\sum_{\pi\neq\mathbf 1}(-1)^{|\pi|-1}(|\pi|-1)!\,\tilde f_\pi$.
- Reproduces $q$-information, residual information, genuine [[multi-entropy]], and $\Delta_p^{(q)}$
  correlation signals as special seeds~[[2603.07680|Gadde 2026]].
