---
type: concept
title: Virial current
aliases: ["virial operator", "scale vs conformal invariance"]
tags: [conformal-field-theory, scale-invariance]
prerequisites: [conformal-multiplet]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The virial current $V_\mu$ is the operator that measures the failure of a scale-invariant theory to be conformally invariant. Scale invariance requires a conserved dilatation current, which can be written as $D_\mu = x^\nu T_{\mu\nu} + V_\mu$; the theory is fully *conformal* precisely when the virial current is itself a total derivative, $V_\mu=\partial_\nu L_{\mu\nu}$, so that the stress tensor can be improved to be traceless. A non-trivial $V_\mu$ that is *not* a derivative is a spin-1 primary of dimension $\Delta=d-1$ (i.e. $\Delta=2$ in $d=3$); its existence would signal scale-without-conformal invariance.

## Motivation

Emergent symmetry at a critical point is a priori only scale invariance; the stronger statement of full conformal invariance requires the absence of a genuine virial current. In the [[state-operator-correspondence]] this becomes a concrete spectral question: is there a spin-1 ($\ell=1$), $\mathbb Z_2$-even, parity-even primary at low dimension? If the lowest such primary sits well above $\Delta=d-1$, no virial current exists and the transition is conformal.

## Key formulas

- Dilatation current decomposition: $D_\mu=x^\nu T_{\mu\nu}+V_\mu$.
- Conformal iff $V_\mu=\partial_\nu L_{\mu\nu}$ (a total derivative / redundant operator).
- Dangerous virial-current channel in $d=3$: a genuine spin-1 primary at $\Delta=2$ in the $(\mathbb Z_2{=}{+},P{=}{+},\ell{=}1)$ sector.

## Relations

- A specific type of [[conformal-multiplet]] (spin-1 primary) whose absence certifies conformal symmetry.
- Its non-existence is what promotes scale invariance to the full conformal symmetry of the [[3d-ising-cft]].

## Where it appears

- [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]] — finds no primary in the $(\mathbb Z_2{=}{+},P{=}{+},\text{odd }\ell)$ sector below $\Delta=7$, so the $\ell=1$ virial candidate lies far above $\Delta=2$, structurally explaining why the 3D Ising transition is conformal (see [[fuzzy-sphere-ising-spectrum]]).
- Prior arguments (Meneses–Penedones et al. 2019) that the 3D Ising virial current does not exist are consistent with this finding.
