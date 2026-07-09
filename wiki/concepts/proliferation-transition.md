---
type: concept
title: Proliferation transition
aliases:
  - proliferation transition
  - anyon proliferation
tags:
  - topological-order
  - tqft
  - anyon-condensation
  - phase-transition
  - 2plus1d
  - strings2026
prerequisites:
  - anyon-condensation
  - one-form-global-symmetry
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A **proliferation transition** is a phase transition out of a $2+1$-dimensional topological phase (TQFT $\mathcal T$) triggered by a single Abelian anyon $a$ becoming light, so that its worldlines proliferate in the path integral across the transition. The name, introduced in [[2603.00245|Cheng–Seiberg 2026]], is a deliberate replacement for the standard term [[anyon-condensation|"anyon condensation"]]: the authors argue nothing actually condenses. Generically no local order parameter acquires a vev, no global symmetry is spontaneously broken, and no particle density becomes macroscopic — only the anyon's worldlines proliferate. Hence *proliferation*, not condensation.

## Motivation

"Condensation" carries the imagery of a Bose–Einstein condensate — a macroscopic occupation of a single mode by a physical particle. For an anyon of a TQFT that picture is misleading: the object going light is a line operator (a worldline), not a local excitation with a conserved number, and the transition changes which lines are genuine versus condensed rather than filling a mode. Renaming the process focuses attention on the correct field-theoretic mechanism — the proliferation of $a$-worldlines, described by giving a mass-squared $\mu^2$ to a scalar $\Phi$ that creates $a$.

## Key formulas

The transition is driven by the [[chern-simons-matter-transition-theory|transition field theory]]
$$\mathcal L=\mathcal L_{\mathcal T'}+\frac1{2\pi}\mathfrak b\,dc+|D_c\Phi|^2-\mu^2|\Phi|^2+\cdots,\qquad D_c\Phi=(d-ic)\Phi,$$
with $\Phi$ creating $a\simeq e^{i\int c}$. For $\mu^2>0$ the IR phase is $\mathcal T$; for $\mu^2<0$ the anyon worldlines proliferate and the IR phase is $\mathcal T'$ (for $p\neq0$) or a gapless theory (for $p=0$).

## Relations

- Reframes [[anyon-condensation]] — same physical process, corrected language.
- Realized by the [[chern-simons-matter-transition-theory|Chern–Simons–matter transition theory]].
- For $p\neq0$ the two phases are related by the [[abelian-hierarchy-construction]]; for $p=0$ by [[gauging-one-form-symmetry|gauging a one-form symmetry]].
- The parameter counting is the result [[proliferation-transition-single-integer-p]].
- Belongs to the topic [[topological-phase-transitions-2plus1d]].

## Where it appears

- [[2603.00245|Cheng–Seiberg 2026]] — introduces the term and the general construction.
