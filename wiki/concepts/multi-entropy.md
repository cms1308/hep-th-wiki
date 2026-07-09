---
type: concept
title: Multi-entropy
aliases: [Rényi multi-entropy, genuine multi-entropy, GM(n), multipartite entropy]
tags: [quantum-information, multipartite-entanglement, entanglement, holography]
prerequisites: [entanglement-entropy, local-unitary-invariant]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

**Multi-entropy** is a multipartite generalization of [[entanglement-entropy]] designed to capture
correlations shared among $q>2$ parties at once, rather than across a single bipartition. Its
Rényi version $S^{(n)}_q$ is (proportional to the logarithm of) a positive
[[local-unitary-invariant|multi-invariant]] — an index contraction of $n$ copies of the state
against a permutation tuple — and reduces to the multi-entropy at $n=1$. Because multi-invariants
are multiplicative under [[genuine-multipartite-entanglement|layer decomposition]], their
logarithms (the multi-entropies) are **additive**, which is precisely the property that makes them
usable as seeds in the [[entanglement-signal|signal]] construction.

## Genuine multi-entropy

The bare multi-entropy does not vanish on all separable states, so it is not itself a GME
diagnostic. **Genuine multi-entropy** $\mathrm{GM}^{(n)}$ is the [[entanglement-signal|Möbius-vector]]
combination of Rényi multi-entropies that *does* vanish on separable states — i.e. the signal
obtained by taking $f_3=S^{(n)}_q$ as the additive seed and applying [[mobius-inversion]] on the
[[partition-lattice]]. Small cases (using $S^{(n)}_1=0$ on pure states):

- $q=2$: $s=-S^{(n)}_2(A,B)$.
- $q=3$: $s=-\big(S^{(n)}_2(AB,C)+\cdots\big)+2\,S^{(n)}_3(A,B,C)$.
- $q=4$: the signal space is spanned by the three pair-partition vectors $M_{AB|CD},M_{AC|BD},M_{AD|BC}$
  together with $M_{\mathbf 1}$ — e.g. $M_{AB|CD}=-S^{(n)}_3(A,B,CD)-S^{(n)}_3(AB,C,D)+S^{(n)}_4(A,B,C,D)$.

The signal reformulation supplies a **free parametrization** of the whole space of such GME
combinations, rather than a single ad hoc quantity.

## Key formulas

- Rényi entropy (bipartite reference point): $S^{(n)}_A=\frac1{1-n}\log\mathrm{Tr}\,\rho_A^n$.
- Rényi multi-entropy $S^{(n)}_q$ = $-\tfrac1n\log$ of a positive $q$-party multi-invariant;
  additive under layers.
- Genuine multi-entropy $\mathrm{GM}^{(n)}=M_\rho[S^{(n)}]$, a Möbius vector on $\Pi_X$.

## Relations

- A specific additive seed in the general [[entanglement-signal|signal]] framework.
- Generalizes [[entanglement-entropy]]; used as a GME diagnostic of holographic states, connecting
  to [[holographic-entanglement-entropy]].
- Related multipartite quantities that also appear as signal seeds: reflected entropy (residual
  information), $q$-information, and the multipartite entanglement of purification $E_p^{(q)}$.

## Where it appears

- Genuine multi-entropy was introduced as a holographic GME diagnostic (Iizuka–Nishida,
  Iizuka–Lin–Nishida 2025); shown to be a Möbius-vector signal in [[2603.07680|Gadde 2026]].
- Belongs to the topic [[multipartite-entanglement]].
