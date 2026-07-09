---
type: concept
title: Partition lattice
aliases: [set partition lattice, Pi_X, Möbius function, partition poset]
tags: [combinatorics, quantum-information, multipartite-entanglement]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

For a finite set $X$, a **partition** $\pi$ is a collection of nonempty, disjoint **blocks**
covering $X$; $\Pi_X$ denotes the set of all partitions. Write $|\pi|$ for the number of blocks and
$\lambda(\pi)$ (the **type**) for the sorted list of block sizes.

$\Pi_X$ is ordered by **refinement**: $\kappa\le\pi$ means $\kappa$ is *finer* than $\pi$ (each
block of $\pi$ is a union of blocks of $\kappa$). This makes $\Pi_X$ a **lattice**:

- **meet** $\pi\wedge\kappa$ — the finest partition coarser-or-equal to both = common refinement's
  coarsening; concretely, two elements share a block of $\pi\wedge\kappa$ iff they are together in
  *both* $\pi$ and $\kappa$;
- **join** $\pi\vee\kappa$ — the coarsest partition finer-or-equal to nothing above both = transitive
  closure of "together in $\pi$ or in $\kappa$";
- bottom $\mathbf 0$ = all singletons ($|\pi|=|X|$); top $\mathbf 1$ = single block ($|\pi|=1$).

For example on $\{A,B,C\}$ with $\pi=\{AB,C\}$, $\kappa=\{AC,B\}$: $\pi\vee\kappa=\{ABC\}=\mathbf 1$,
$\pi\wedge\kappa=\{A,B,C\}=\mathbf 0$. General identities: $\pi\vee\mathbf 0=\pi$,
$\pi\vee\mathbf 1=\mathbf 1$, $\pi\wedge\mathbf 0=\mathbf 0$, $\pi\wedge\mathbf 1=\pi$.

## Motivation

The partition lattice is the natural bookkeeping device for **multipartite separability**: a
$q$-partite state's separability type is exactly an element $\pi\in\Pi_X$ (it factorizes across the
blocks of $\pi$). Order, meet, and join then translate directly into statements about
[[genuine-multipartite-entanglement|separable and GME states]], and [[mobius-inversion]] on the
lattice produces the [[entanglement-signal|signals]] that vanish on separable states.

## Key formulas

**Möbius function.** For $\kappa\le\pi$, $\mu(\kappa,\pi)$ is the unique function with
$\sum_{\kappa\le\tau\le\pi}\mu(\kappa,\tau)=\delta_{\kappa,\pi}$. On the partition lattice it factors
over the blocks of $\pi$:
$$\mu(\kappa,\pi)=\prod_{B\in\pi}(-1)^{k_B-1}(k_B-1)!,$$
where $k_B$ is the number of $\kappa$-blocks inside the block $B$ of $\pi$. The special case toward
the top is
$$\mu(\kappa,\mathbf 1)=(-1)^{|\kappa|-1}(|\kappa|-1)!.$$

**Group algebra $\mathbb C[\Pi_X]$.** The free complex vector space on $\Pi_X$, with $\wedge$ (and
$\vee$) extended bilinearly. Formal vectors $V=\sum_\pi c_\pi\,\pi$ let separability constraints be
written as linear **meet-vanishing** conditions $V\wedge\kappa=0$; their solution space is spanned
by the [[entanglement-signal|Möbius vectors]] $M_\rho=\sum_{\pi\le\rho}\mu(\pi,\rho)\,\pi$.

## Relations

- Underlies [[mobius-inversion]] (the inversion formula and moments-to-cumulants analogy).
- Bookkeeps [[genuine-multipartite-entanglement|multipartite separability]] and the
  [[entanglement-signal|signal]] construction.

## Where it appears

- The organizing structure of [[2603.07680|Gadde 2026]]; classical background is Rota (1964) and
  Stanley's *Enumerative Combinatorics*.
- Belongs to the topic [[multipartite-entanglement]].
