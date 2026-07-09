---
type: concept
title: Genuine multipartite entanglement (GME)
aliases: [GME, genuinely multipartite entangled, layerwise-separable, layer decomposition]
tags: [quantum-information, multipartite-entanglement, entanglement]
prerequisites: [entanglement-entropy, partition-lattice]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

Let $|\psi\rangle\in\mathcal H_{A_1}\otimes\cdots\otimes\mathcal H_{A_q}$ be a pure $q$-partite
state, with parties $X=\{A_1,\dots,A_q\}$. Separability is classified by the
[[partition-lattice|partitions]] $\pi\in\Pi_X$: the state is **$\pi$-separable** if it factorizes
across the blocks of $\pi$,
$$|\psi\rangle=\bigotimes_{B\in\pi}|\psi_B\rangle,\qquad
  |\psi_B\rangle\in\bigotimes_{A_a\in B}\mathcal H_{A_a}.$$
The state is **separable** if it is $\pi$-separable for some $\pi$ with $|\pi|\ge2$ (at least two
blocks), and **completely separable** if it is $\mathbf 0$-separable (a product over all parties).
It is **genuinely multipartite entangled (GME)** if it is *not* separable across any partition —
no cut factorizes it.

**Layer decomposition.** Refine each local space $\mathcal H_{A_a}=\bigotimes_{i=1}^n\mathcal
H_{A_a^{(i)}}$. The state *admits a layer decomposition* if
$|\psi\rangle=\bigotimes_{i=1}^n|\psi^{(i)}\rangle$ with each layer
$|\psi^{(i)}\rangle\in\bigotimes_a\mathcal H_{A_a^{(i)}}$. It is **layerwise-separable** if some such
decomposition has every layer $|\psi^{(i)}\rangle$ separable. Every separable state is
layerwise-separable (take $n=1$); the converse fails. The non-separable layers carry the GME part,
so layerwise separability — not mere separability — is the sharp notion a GHZ-detecting quantity
should vanish on.

## Motivation

Bipartite entanglement across *some* cut is not genuinely multipartite: a state can be highly
entangled across every single bipartition yet be a product of independent pieces (layers). GME
isolates the entanglement that cannot be built from lower-party resources. Detecting it requires
[[local-unitary-invariant|LU-invariants]] that vanish exactly on layerwise-separable states — the
[[entanglement-signal|signals]].

## Key formulas

- $\pi$-separable: $|\psi\rangle=\bigotimes_{B\in\pi}|\psi_B\rangle$.
- Separability hierarchy on the [[partition-lattice]]: completely separable $=\mathbf 0$-separable
  $\Rightarrow\;\pi$-separable ($|\pi|\ge2$) $\Rightarrow$ GME (no such $\pi$).
- Layerwise-separable: $|\psi\rangle=\bigotimes_i|\psi^{(i)}\rangle$ with each layer separable.

## Relations

- Detected by [[entanglement-signal|signals and pre-signals]] built via [[mobius-inversion]] on the
  [[partition-lattice]].
- The most-studied quantitative diagnostics are [[multi-entropy|multi-entropies]] and their
  Möbius-vector combinations (genuine multi-entropy, $q$-information).
- A **GME measure** is a signal/pre-signal additionally satisfying positivity and LOCC monotonicity;
  see [[no-signal-is-gme-measure]] for why signals cannot be measures.

## Where it appears

- Central object of [[2603.07680|Gadde 2026]], which constructs the full space of LU-invariants
  vanishing on layerwise-separable states.
- The parent topic is [[multipartite-entanglement]].
