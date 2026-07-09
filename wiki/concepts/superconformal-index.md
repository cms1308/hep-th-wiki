---
type: concept
title: Superconformal index (4d)
aliases: [4d superconformal index, index]
tags: [supersymmetry, scft, protected-quantities]
prerequisites: [conformal-field-theory, supersymmetry-basics]
created: 2026-07-03
updated: 2026-07-04
---

Conventions here follow [[2308.01717|Cho-Choi-Lee-Song 2023]]; the equivalent
$(t,y)$ convention of [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]] and its dictionary
are given under Key formulas.

## Definition

A Witten-type index of a 4d $\mathcal{N}=1$ SCFT counting (with sign) short multiplets on
$S^3 \times \mathbb{R}$:
$$\mathcal{I}(\omega_1,\omega_2; z_I) \;=\;
\mathrm{Tr}_{\mathcal{H}}\Big[(-1)^F\, e^{-\omega_1 (J_1 + \frac{R}{2})}\,
e^{-\omega_2 (J_2 + \frac{R}{2})} \prod_I z_I^{f_I}\Big]\,,$$
where the trace is over radially quantized states on $S^3$, $J_{1,2}$ are the Cartans of
the $SO(4)$ rotation group, $R$ is the $U(1)_R$ charge, and $z_I$ are fugacities for flavor
symmetries $f_I$. Only states with
$$\Delta - J_1 - J_2 - \tfrac{3}{2}R \;=\; 0$$
contribute; the index is protected — independent of continuous couplings. Introduced in
[hep-th/0510251](https://arxiv.org/abs/hep-th/0510251) (Kinney-Maldacena-Minwalla-Raju) and
[hep-th/0510060](https://arxiv.org/abs/hep-th/0510060) (Romelsberger).

## Motivation

The index is the main exactly computable partition function of a 4d SCFT: it tests
dualities, detects protected operators, and — through its high-temperature (Cardy-like)
asymptotics — counts the microstates of BPS black holes in $AdS_5$.

## Key formulas

- Cardy-like limit $\omega_{1,2} \to 0$ (after the shift $\omega_1 \to \omega_1 - 2\pi i$,
  which turns $(-1)^F$ into $e^{\pi i R}$ and obstructs boson/fermion cancellation):
  $\log \mathcal{I}$ is fixed by the anomaly coefficients $\mathrm{Tr}R^3$ and
  $\mathrm{Tr}R$, i.e. by $a$ and $c$ — see [[supersymmetric-cardy-formula-4d]].
- The shift matters because $\mathcal{N}=1$ R-charges are not integer-quantized, so
  $\mathcal{I}$ is not $2\pi i$-periodic in $\omega_{1,2}$.
- Equivalent $(t,y)$ convention
  ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]):
  $\mathcal{I}(t,y;x) = \mathrm{Tr}\,(-1)^F t^{3(R+2j_1)} y^{2j_2} x^f$ with $(j_1,j_2)$
  the half-integer $SU(2)_1\times SU(2)_2$ spins. Dictionary:
  $e^{-\omega_1} = t^3 y$, $e^{-\omega_2} = t^3 y^{-1}$, $J_{1,2} = j_1 \pm j_2$
  (the BPS condition becomes $\Delta - 2j_1 - \tfrac32 R = 0$, matching the $t$-grading).
- **Reduced index**: $\mathcal{I}_{\rm red} = (1-t^3 y)(1-t^3/y)\,(\mathcal{I}-1)$ strips
  descendant contributions; its $t^6$ coefficient equals
  $\#(\text{marginal operators}) - \#(\text{conserved currents})$, diagnosing conformal
  manifolds ($>0$) and symmetry enhancement ($<0$).

## Relations

- Contributing states are the $\tfrac14$-BPS sector; chiral operators
  ($\Delta = \tfrac32 R$) are the states used to test WGC-type bounds
  ([[modified-ads-wgc-3c-2a]]).
- Its Cardy-like limit is the 4d analog of the 2d Cardy formula
  ([[supersymmetric-cardy-formula-4d]], [[higher-dimensional-modularity]]).
- For holographic theories, its large-charge asymptotics reproduces BPS black hole entropy
  in $AdS_5$.

## Where it appears

- [[2308.01717|Cho-Choi-Lee-Song 2023]] — its Cardy-like limit motivates the modified AdS
  WGC bound.
- [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]] — used as the fingerprint
  distinguishing the 7,346 fixed points of the [[4d-n1-scft-landscape|landscape]] and as
  the consistency filter (unitarity conditions, free-field detection, SUSY-enhancement
  criteria).
