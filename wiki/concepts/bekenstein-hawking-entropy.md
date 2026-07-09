---
type: concept
title: Bekenstein-Hawking entropy
aliases: [Bekenstein-Hawking entropy, black hole entropy, area law of black holes, S_BH]
tags: [black-holes, thermodynamics, holography, general-relativity]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A black hole carries a thermodynamic entropy proportional to the area of its event horizon:
$$S_{\rm BH}=\frac{\mathrm{Area\ of\ horizon}}{4G_N},$$
in units $\hbar=c=k_B=1$. Combined with the Hawking temperature $T_H$, it makes the horizon a
genuine thermodynamic system obeying $dM=T_H\,dS_{\rm BH}$ (the first law) and the area /
generalized second law.

## Motivation

The area law is the sharpest statement that gravity is holographic: the number of degrees of
freedom in a region is bounded by its boundary area, not its volume. Reproducing $S_{\rm BH}$
from a microscopic count is a central test of any quantum-gravity proposal (achieved for BPS
black holes by Strominger-Vafa 1996).

## Key formulas

- $S_{\rm BH}=\dfrac{A}{4G_N}$; the factor $\tfrac14$ is fixed by matching the semiclassical
  Hawking temperature.

## Relations

- Template and normalization anchor for the [[ryu-takayanagi-formula|Ryu-Takayanagi formula]]
  $S_A=\mathrm{Area}(\gamma_A)/4G_N$: entanglement entropy inherits the same Area$/4G_N$ law,
  and in the finite-temperature / large-region limit the RT surface wraps the horizon so
  $S_A\to S_{\rm BH}$.
- Bounded and covariantized by the [[bousso-bound|covariant entropy bound]].
- The renormalization of $G_N$ that makes $A/4G_N$ finite is the subject of the
  [[susskind-uglum-low-energy-theorem|Susskind-Uglum theorem]].

## Where it appears

- Original: Bekenstein 1973, Hawking 1975.
- As the structural template for holographic entanglement entropy:
  [[hep-th-0603001|Ryu-Takayanagi 2006]], [[0705.0016|Hubeny-Rangamani-Takayanagi 2007]].
