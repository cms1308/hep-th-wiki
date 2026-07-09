---
type: concept
title: Entanglement signal and pre-signal
aliases: [signal, pre-signal, GME signal, Möbius vector, compatible family, M_rho]
tags: [quantum-information, multipartite-entanglement, local-unitary-invariants]
prerequisites: [genuine-multipartite-entanglement, local-unitary-invariant, partition-lattice, mobius-inversion]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

Two classes of [[local-unitary-invariant|LU-invariants]] that certify multipartite entanglement by
vanishing on entanglement-free states:

- A **signal** vanishes on all **layerwise-separable** states.
- A **pre-signal** vanishes on all **separable** states.

Since every separable state is [[genuine-multipartite-entanglement|layerwise-separable]] but not
conversely, a signal is the stronger diagnostic. An **additive pre-signal is automatically a
signal**, and more sharply (**Key Lemma**): an additive LU-invariant that vanishes on
$\pi$-separable states of type $(1,q-1)$ is a signal — every layer factorizes into $(1,q-1)$-type
pieces, so the single-party cuts suffice. A nonzero value of a signal certifies
[[genuine-multipartite-entanglement|GME]].

## Compatible families

The construction feeds on **compatible families** $\{f_m\}_{m=1}^q$ of $m$-partite symmetric
LU-invariants, meaning
$$f_\pi(|\psi\rangle_\kappa)=f_{\pi\wedge\kappa}(|\psi\rangle_\kappa)\qquad
  \text{on every }\kappa\text{-separable state},$$
so evaluating the $\pi$-extension on a $\kappa$-separable state only sees the meet $\pi\wedge\kappa$.
The restrictions $\{f|_m\}$ of any symmetric **additive** $q$-partite LU-invariant form a compatible
family, and $\{g(f_m^{(i)})\}$ is compatible for any $g:\mathbb C^r\to\mathbb C$ — an infinite
supply, including non-additive families.

## The Möbius-vector construction

Write the coefficient data as $V=\sum_\pi c_\pi\,\pi\in\mathbb C[\Pi_X]$. The signal/pre-signal
conditions become **meet-vanishing constraints** $V\wedge\kappa=0$, solved (via
[[mobius-inversion]]) by the **Möbius vectors**
$$M_\rho[f]:=\sum_{\pi\le\rho}\mu(\pi,\rho)\,f_\pi,\qquad
  \mu(\pi,\rho)=\prod_{B\in\rho}(-1)^{k_B-1}(k_B-1)!.$$

- **Signals** (Theorem): for an additive compatible family, $\sum_{\rho\in\mathcal N}a_\rho M_\rho[f]$
  with $\mathcal N=\{\rho:\rho\text{ has no size-1 block}\}$ is an additive signal, and these $M_\rho[f]$
  **span the entire additive-signal space** — a free basis.
- **Pre-signals** (Theorem): for any compatible family,
  $M_{\mathbf 1}[\tilde f]=\sum_{\pi\neq\mathbf 1}(-1)^{|\pi|-1}(|\pi|-1)!\,\tilde f_\pi$ is a
  pre-signal, and the **unique** one (up to scale) for a generic non-additive family.

## Examples reproduced from the literature

Choosing the seed $f$ recovers essentially every signal proposed in recent work:

| seed $f$ | resulting signal |
|---|---|
| $\sum_a S^{(n)}_{A_a}$ (single-party Rényi) | $q$-information, $M_{\mathbf 1}[f_1]=\sum_{\varnothing\neq A\subsetneq X}(-1)^{q-|A|}S^{(n)}_A$ ([[q-information-odd-q-vanishing|vanishes for odd $q$]]) |
| $\sum_{a}(\tfrac12 S_{A_aA_a^*}-S_{A_a})$ (reflected entropy) | residual information (non-vanishing at odd $q$) |
| $S^{(n)}_q$ (Rényi [[multi-entropy]]) | genuine multi-entropy $\mathrm{GM}^{(n)}$, now with a free basis |
| $E_p^{(q)}$ (multipartite entanglement of purification) | correlation signals $\Delta_p^{(q)}$ |

**Non-symmetric variant.** From a positive multi-invariant with logarithm $\mathcal E$, any rank-$q$
tensor $T$ with vanishing marginals $\sum_{i_k}T_{i_1\dots i_q}=0$ ($\forall k$) gives a signal
$\sum T_{i_1\dots i_q}\mathcal E(\sigma_{i_1},\dots,\sigma_{i_q})$; the minimal one is
$\mathcal E(\sigma_1-\sigma_2,\sigma_2-\sigma_1,\sigma_3-\sigma_1,\dots,\sigma_q-\sigma_1;\cdot)$.

## Relations

- Signals detect [[genuine-multipartite-entanglement]]; the construction runs on the
  [[partition-lattice]] via [[mobius-inversion]].
- A signal is **not** a GME measure: see [[no-signal-is-gme-measure]]. Pre-signals are the natural
  resource-theoretic objects, and whether they yield measures is [[pre-signals-to-gme-measures|open]].

## Where it appears

- Introduced as a unified class in [[2603.07680|Gadde 2026]].
- Belongs to the topic [[multipartite-entanglement]].
