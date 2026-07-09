---
type: concept
title: Local-unitary invariant
aliases: [LU-invariant, multi-invariant, logarithmic multi-invariant, symmetric LU-invariant, coarse-graining, pi-extension, restriction]
tags: [quantum-information, multipartite-entanglement, local-unitary-invariants]
prerequisites: [partition-lattice]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A **local-unitary (LU) invariant** of a $q$-partite pure state is a function
$f:\bigotimes_{a=1}^q\mathcal H_{A_a}\to\mathbb C$ unchanged under local unitaries,
$$|\psi\rangle\longmapsto(U_1\otimes\cdots\otimes U_q)|\psi\rangle.$$
Since local unitaries do not alter entanglement, LU-invariants are the intrinsic entanglement data
of a pure state. An LU-invariant is **additive** (resp. **multiplicative**) if it adds (multiplies)
under [[genuine-multipartite-entanglement|layer decomposition]] $|\psi\rangle=\bigotimes_i|\psi^{(i)}\rangle$.

## Symmetric invariants, restriction, extension

An LU-invariant is **symmetric** if invariant under permuting the parties. Unequal local dimensions
are handled by isometrically embedding each $\mathcal H_{A_a}$ into a common $\mathbb C^d$, after
which parties may be freely permuted. From a symmetric invariant one builds partition-labeled
invariants via two operations tied to the [[partition-lattice]]:

- **Coarse-graining** $\mathrm{grp}_\pi$: group the parties in each block $B$ of $\pi$ into a single
  effective subsystem $\mathcal H_B=\bigotimes_{A_a\in B}\mathcal H_{A_a}$, viewing a $q$-partite
  state as an $|\pi|$-partite one.
- **$\pi$-extension** $f_\pi(|\psi\rangle):=f(\mathrm{grp}_\pi(|\psi\rangle))$ — evaluate an
  $|\pi|$-partite invariant on the coarse-grained state.
- **Restriction** $f|_m(|\psi\rangle):=f(|\psi\rangle\otimes|0\rangle^{\otimes(q-m)})$ — pad an
  $m$-partite state with reference parties; independent of the reference by LU-invariance.

These produce, from a single symmetric invariant, a family of invariants labeled by $\pi\in\Pi_X$ —
the raw material for [[entanglement-signal|signals]].

## Multi-invariants (permutation / edge-colored-graph form)

A large explicit class: writing $|\psi\rangle=\sum\psi_{i_1\dots i_q}|i_1\rangle\cdots|i_q\rangle$, a
**multi-invariant** takes $n$ copies of $\psi$ and $n$ of $\bar\psi$ and contracts all indices in a
pattern set by an $n$-tuple of permutations (equivalently an edge-colored graph):
$$\mathcal Z(\sigma_1,\dots,\sigma_q;|\psi\rangle):=\langle\psi|^{\otimes n}\,
  \sigma_1\otimes\cdots\otimes\sigma_q\,|\psi\rangle^{\otimes n},\qquad \sigma_a\in S_n.$$
It is multiplicative under layer decomposition and bounded, $|\mathcal Z|\le1$ (Cauchy–Schwarz),
with a relabeling redundancy $\mathcal Z(\sigma_a)=\mathcal Z(g\sigma_a)=\mathcal Z(\sigma_a h)$,
$g,h\in S_n$. Reflection-symmetric graphs give positive, real $\mathcal Z$, for which the
**logarithmic multi-invariant**
$$\mathcal E(\sigma_1,\dots,\sigma_q):=-\tfrac1n\log\mathcal Z(\sigma_1,\dots,\sigma_q)$$
is additive. [[multi-entropy|Multi-entropies]] are exactly such logarithmic multi-invariants.

## Key formulas

- LU transformation: $|\psi\rangle\mapsto(U_1\otimes\cdots\otimes U_q)|\psi\rangle$, $f$ invariant.
- $\pi$-extension / restriction: $f_\pi=f\circ\mathrm{grp}_\pi$,
  $f|_m(|\psi\rangle)=f(|\psi\rangle\otimes|0\rangle^{\otimes(q-m)})$.
- Multi-invariant $\mathcal Z(\vec\sigma;|\psi\rangle)=\langle\psi|^{\otimes n}\,\sigma_1\otimes\cdots\otimes\sigma_q\,|\psi\rangle^{\otimes n}$; $\mathcal E=-\tfrac1n\log\mathcal Z$.

## Relations

- Additive symmetric LU-invariants generate [[entanglement-signal|compatible families]] via their
  restrictions $\{f|_m\}$.
- Additive multiplicative structure under layers is what makes [[mobius-inversion]] produce signals.
- Rényi entropy $S^{(n)}_A=\frac1{1-n}\log\mathrm{Tr}\,\rho_A^n$ and [[multi-entropy]] are the
  standard additive seeds.

## Where it appears

- The building blocks of the signal construction in [[2603.07680|Gadde 2026]]; multi-invariant
  enumeration has a long literature (Rains 2000, Grassl–Rötteler–Beth 1998, Vrana, Szalay).
- Belongs to the topic [[multipartite-entanglement]].
