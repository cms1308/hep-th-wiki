---
type: concept
title: Positivity of the gravitational path integral
aliases: [GPI positivity, baby-universe Hilbert space, Stieltjes moment positivity]
tags: [gravitational-path-integral, baby-universes, wormholes, ensemble-averaging, hilbert-space]
prerequisites: [factorization-vs-wormholes]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The requirement that the inner products of universe states computed by the gravitational path
integral be positive semi-definite, as they must be in any Hilbert space. In the baby-universe
formalism (Marolf-Maxfield 2020) an asymptotic boundary $\mathcal J$ prepares a state
$|\mathcal J\rangle$, and gluing two boundaries with a CPT reflection $\Theta$ gives the inner
product
$$\langle\mathcal J_1|\mathcal J_2\rangle=Z\big(\mathcal J_1^\Theta\cup\mathcal J_2\big).$$
Positivity of every Gram matrix built from these states is equivalent to the existence of a
positive ensemble measure $P(\alpha)\ge0$ with non-negative densities of states
$\rho^\alpha_J(E)\ge0$ — i.e. gravity computes moments of a genuine probability distribution
over boundary theories.

## Motivation

Connected wormhole geometries make partition functions non-factorize
([[factorization-vs-wormholes]]), which is naturally read as the variance of an ensemble. But an
ensemble is only consistent if its measure is positive. Positivity is therefore a sharp,
model-independent consistency condition on the low-energy theory: any EFT whose wormhole moments
cannot come from a non-negative measure is in the swampland.
[[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] turn this into a derivation of the axionic
[[weak-gravity-conjecture|WGC]].

## Key formulas

- Inner products from gluing: $\langle\mathcal J_1|\mathcal J_2\rangle=Z(\mathcal J_1^\Theta\cup\mathcal J_2)$.
- Positive ensemble decomposition:
  $\overline{\rho_J(E_1)\cdots\rho_J(E_n)}=\int d\alpha\,P(\alpha)\prod_i\rho^\alpha_J(E_i)$,
  with $P(\alpha)\ge0$, $\rho^\alpha_J\ge0$.
- **Stieltjes moment problem**: for non-negative partition functions the moments
  $m_n=\overline{Z^n}$ must give PSD Hankel and shifted-Hankel matrices; in cumulants
  $\kappa_1\ge0$, $\kappa_2\ge0$, and $\kappa_1\kappa_3\ge\kappa_2(\kappa_2-\kappa_1^2)$.
- Violation mechanism: an [[euclidean-axion-wormhole|axion wormhole]] makes the connected
  two-boundary amplitude $\kappa_2$ diverge while the mean $\kappa_1$ stays finite, so a
  (near-Gaussian) $Z$ is negative with probability $\to50\%$ — the third inequality fails.

## Relations

- Sharpens the ensemble resolution of [[factorization-vs-wormholes]]: it is not enough that a
  measure exist; it must be *positive*, which fails for an exactly-shift-symmetric axion.
- Restoring positivity forces shift-symmetry-breaking instantons to proliferate before the
  wormhole divergence, giving the axionic WGC $S_{\rm inst}\le\tfrac12|\mathrm{Im}\,\Delta a_{\rm crit}|$
  with a fixed coefficient (see [[imaginary-distance-bound]]).
- Whether the instanton-corrected amplitudes satisfy *all* Stieltjes constraints — a
  "wormhole bootstrap" — is left open by [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]].

## Where it appears

- [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] — casts GPI positivity as a Stieltjes moment
  problem, shows axion wormholes violate it, and derives the sharp axionic WGC.
- [[1903.11115|Saad-Shenker-Stanford 2019]] — the ensemble/matrix-integral context in which
  wormhole moments are computed.
