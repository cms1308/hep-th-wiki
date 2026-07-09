---
type: result
title: q-information vanishes for odd q
aliases: [q-information, odd-q vanishing, residual information motivation]
tags: [quantum-information, multipartite-entanglement, renyi-entropy]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The **$q$-information** is the [[entanglement-signal|signal]] obtained from the additive seed
$f_1=\sum_{a=1}^q S^{(n)}_{A_a}$ (the sum of single-party $n$th Rényi entropies). Its coarsest
Möbius vector evaluates, on a pure $q$-partite state, to
$$M_{\mathbf 1}[f_1]=\sum_{\varnothing\neq A\subsetneq X}(-1)^{q-|A|}\,S^{(n)}_A .$$
For **odd $q$** this signal — and in fact every Möbius vector $M_\rho[f_1]$ — **vanishes**
identically; for **even $q$** all $M_\rho[f_1]$ vanish except $\rho=\mathbf 1$.

## Derivation sketch

Purity of $|\psi\rangle$ gives $S^{(n)}_A=S^{(n)}_{A^c}$, pairing each subset with its complement.
Combined with the Möbius coefficients $(-1)^{q-|A|}$ this reduces the sum to a Stirling-number
identity $\sum_{r=0}^m(-1)^r r!\,S(m,r)=(-1)^m$, which forces cancellation for odd $q$. (Detailed in
the Appendix "Vanishing signals" of the source.)

## Assumptions

- Pure $q$-partite state; seed = sum of single-party Rényi entropies $S^{(n)}_{A_a}$.
- Purity is used through $S^{(n)}_A=S^{(n)}_{A^c}$.

## Status

**Proven** in [[2603.07680|Gadde 2026]]. The $q$-information itself was introduced by
Balasubramanian–Kang–Murdia–Ross (2024).

## Implications

Because the sum-of-Rényi signal is blind to odd-party GME, a different seed is needed there: tracing
out one party, canonically purifying, and using a reflected-entropy seed
$f_2=\sum_a(\tfrac12 S_{A_aA_a^*}-S_{A_a})$ gives the **residual information**, whose Möbius vector
$M_{\mathbf 1}[f_2]$ is non-vanishing for odd $q$ and reduces to the $q$-information for even $q$.
This is a concrete illustration of choosing the seed within the general
[[entanglement-signal|signal]] framework.
