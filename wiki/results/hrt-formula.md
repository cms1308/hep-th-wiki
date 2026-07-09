---
type: result
title: HRT formula (covariant holographic entanglement entropy)
aliases: [HRT formula, HRT proposal, covariant holographic entanglement entropy, Hubeny-Rangamani-Takayanagi formula]
tags: [holography, entanglement, ads-cft, holographic-entanglement-entropy, time-dependent]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The covariant generalization of the [[ryu-takayanagi-formula|Ryu-Takayanagi formula]] to
general, possibly time-dependent, asymptotically AdS$_{d+1}$ spacetimes. The
[[entanglement-entropy|entanglement entropy]] of a boundary region $A$ is
$$S_A=\frac{\mathrm{Area}(\gamma_A^{\rm ext})}{4G_N^{(d+1)}},$$
where $\gamma_A^{\rm ext}$ is a bulk codimension-two spacelike **extremal surface** anchored on
$\partial A$, characterized covariantly by vanishing of both null expansions
$\theta_+=\theta_-=0$ (a saddle of the Lorentzian area functional). When several extremal
surfaces qualify, the one of **minimum area among those homologous to $A$** is chosen.

## Derivation sketch

A minimal spacelike surface is ill-defined in Lorentzian signature (deforming in the time
direction lowers the area without bound), and a generic time-dependent bulk has no preferred
constant-time slice — so RT's "minimal surface on the $t=$const slice" is not covariant. The
fix uses the [[bousso-bound|covariant entropy bound]]: minimize the area over surfaces that
support both a future and a past light-sheet ($\theta_{\hat+}\le0$, $\theta_{\hat-}\le0$);
deforming toward the boundary drives the area down until $\theta_+=\theta_-=0$, i.e. to the
extremal surface, which saturates the bound. Checked against exact 2d CFT answers.

## Assumptions

- Classical (supergravity) bulk; the entangling surface bounds a spacelike region on the
  boundary.
- Selection rule: minimum area among homologous extremal surfaces (stated, not derived here).
- Reduces to [[ryu-takayanagi-formula|RT]] when the bulk is static (extremal surface lies on
  the constant-$t$ slice and extremality becomes minimality).

## Status

**Established** as the correct covariant prescription; later proven from AdS/CFT (covariant
replica, Dong-Lewkowycz-Rangamani) and refined by the quantum extremal surface prescription
(Engelhardt-Wall). Checks in the paper:

- **Rotating BTZ** (stationary, non-static): the extremal geodesic is *not* confined to any
  constant-$t$ slice and gives
  $S_A=\frac{c}{6}\log\!\big[\frac{\beta_+\beta_-}{\pi^2\epsilon^2}\sinh\frac{\pi\Delta l}{\beta_+}\sinh\frac{\pi\Delta l}{\beta_-}\big]$,
  $\beta_\pm=\beta(1\pm\Omega)$, matching the CFT twist-operator result in the ensemble
  $\rho=e^{-\beta H+\beta\Omega P}$ and factorizing into left/right movers.
- **Vaidya-AdS collapse** (genuinely time-dependent): $S_A(v)$ grows monotonically during
  thermalization, proven perturbatively under the null energy condition.

## Key formulas

- **Covariant HEE:** $S_A=\mathrm{Area}(\gamma_A^{\rm ext})/4G_N^{(d+1)}$, $\theta_+=\theta_-=0$.
- **Light-sheet form:** $S_A=\min_\Sigma\mathrm{Area}(\Sigma_t)/4G_N$ over surfaces supporting
  future/past light-sheets, $\Sigma_t=L_t^+\cap L_t^-$.
- **Area variation:** $\delta(\mathrm{Area})\propto\int(\theta_+N_+^\mu+\theta_-N_-^\mu)\delta X_\mu$.

## Implications

- Makes holographic entanglement entropy a fully covariant, time-dependent observable;
  necessary for thermalization, quantum quenches, and the eternal black hole.
- The extremal-surface framework is the classical seed of the quantum extremal surface
  prescription and the island formula for black-hole information.
- A surprising fact flagged here — entanglement entropy saturating the thermodynamic Bousso
  bound — foreshadows the deep entanglement/geometry connection.

## References

- [[0705.0016|Hubeny-Rangamani-Takayanagi 2007]] (the extremal-surface proposal, BTZ and
  Vaidya checks).
- Static special case: [[ryu-takayanagi-formula|Ryu-Takayanagi]] /
  [[hep-th-0603001|Ryu-Takayanagi 2006]].
