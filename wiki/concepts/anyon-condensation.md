---
type: concept
title: Anyon condensation
aliases: [anyon condensation]
tags: [topological-order, tqft, anyon, phase-transition, 2plus1d]
prerequisites: [one-form-global-symmetry, chern-simons-theory]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

**Anyon condensation** is the standard name for the operation that takes a $2+1$-dimensional topological phase $\mathcal T$ to a new phase $\mathcal T'$ by making a chosen (Abelian) anyon $a$ "trivial." Categorically (Bais–Slingerland 2008; Moore–Seiberg 1989) one restricts to anyons that braid trivially with $a$, identifies those differing by fusion with $a$, and keeps the resulting consistent set — producing a smaller anyon theory $\mathcal T'$. In modern language, condensing an Abelian anyon of order $n$ is [[gauging-one-form-symmetry|gauging]] the [[one-form-global-symmetry|$\mathbb Z_n^{(1)}$ one-form symmetry]] it generates (when that symmetry is anomaly-free).

## Motivation

Anyon condensation is the workhorse for relating topological orders: fractional quantum Hall hierarchies, gapped boundaries and interfaces, and phase transitions between spin liquids are all organized by which anyon condenses. It gives a purely algebraic (modular-tensor-category) recipe for $\mathcal T'$ from $\mathcal T$ and $a$.

> [!note] Terminology
> [[2603.00245|Cheng–Seiberg 2026]] argues "condensation" is a misnomer for the associated *dynamical phase transition*: nothing condenses in the Bose–Einstein sense — the anyon's worldlines proliferate. They call the transition a [[proliferation-transition|proliferation transition]]. "Anyon condensation" remains standard for the categorical $\mathcal T\to\mathcal T'$ operation; the two names describe the algebraic map and the field-theoretic transition respectively.

## Key formulas

For an Abelian anyon $a$ of order $n$ with spin $h(a)=\frac{p}{2n}\bmod 1$, the condensed theory is
$$\mathcal T'=\frac{\mathcal T\boxtimes\mathrm U(1)_{-pn}}{(a,p)}\quad(p\neq0),\qquad \mathcal T/\mathbb Z_n=\mathcal T/(a)\quad(p=0,\ \text{anomaly-free}).$$

## Relations

- Its dynamical realization is the [[proliferation-transition]].
- The $p=0$ anomaly-free case is exactly [[gauging-one-form-symmetry|gauging the one-form symmetry]] $\mathbb Z_n^{(1)}$.
- The $p\neq0$ case is an [[abelian-hierarchy-construction|Abelian hierarchy construction]].
- Belongs to [[topological-phase-transitions-2plus1d]].

## Where it appears

- [[2603.00245|Cheng–Seiberg 2026]] — reframes it as a proliferation transition and gives the continuum theory.
