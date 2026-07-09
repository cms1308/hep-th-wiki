---
type: concept
title: Abelian hierarchy construction
aliases: [hierarchy construction, FQH hierarchy, stack and condense]
tags: [topological-order, fractional-quantum-hall, tqft, chern-simons, K-matrix]
prerequisites: [chern-simons-theory, one-form-global-symmetry]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

The **Abelian hierarchy construction** builds new Abelian topological orders from old ones by a "stack and condense" step: stack the TQFT $\mathcal T$ with an auxiliary Abelian Chern–Simons theory and condense a diagonal anyon. Originating as the Haldane–Halperin hierarchy of fractional quantum Hall plateaux (1983–1984), it is formulated with $K$-matrices (Blok–Wen 1990; Read 1990; Wen–Zee 1992) and, in modern language, is a TQFT-to-TQFT map $\mathcal T\to\mathcal T'$ (Lan–Wang–Wen 2017) equivalent to a gauging/enrichment sequence.

## Motivation

The FQH hierarchy explains the observed sequence of fractional filling fractions as daughters condensed from parent states. Abstracted from Hall physics, it is the general way one Abelian topological order sits next to another, and it is exactly the relation between the two phases of a [[proliferation-transition|proliferation transition]] when the driving anyon is anomalous ($p\neq0$).

## Key formulas

In [[2603.00245|Cheng–Seiberg 2026]] the far-side theory of the transition is the hierarchy image
$$\mathcal T'=\frac{\mathcal T\boxtimes\mathrm U(1)_{-pn}}{(a,p)}.$$
For a general Abelian $\mathcal T$ with $K$-matrix $K$, coupling vector $q$, and anomaly integer $p$,
$$K'=\begin{pmatrix}0&-q^{\mathrm T}\\-q&K\end{pmatrix},\qquad \det K'=-\frac pn\det K.$$
The map is invertible: $\mathcal T$ is the hierarchy construction of $\mathcal T'$ with $\tilde a=(\mathbf 1,n)$, $\tilde n=p$, $\tilde p=-n$.

## Relations

- Produces the $p\neq0$ far side of a [[proliferation-transition]].
- The $p=0$ degenerate case reduces to [[gauging-one-form-symmetry|gauging a one-form symmetry]] rather than a TQFT-to-TQFT map.
- Built on [[chern-simons-theory|Chern–Simons TQFT]] / $K$-matrices.
- Belongs to [[topological-phase-transitions-2plus1d]].

## Where it appears

- [[2603.00245|Cheng–Seiberg 2026]] — the two phases of the transition are hierarchy constructions of each other; the $K'$ formula and Jain-series examples.
