---
type: concept
title: Large-N ('t Hooft) limit
aliases: ["'t Hooft limit", large-N limit, 1/N expansion]
tags: [gauge-theory, large-n, string-theory]
prerequisites: [quantum-field-theory]
created: 2026-07-03
updated: 2026-07-03
---

## Definition

The limit $N\to\infty$ of a $U(N)$/$SU(N)$ gauge theory with the 't Hooft coupling
$\lambda = g^2_{YM} N$ held fixed. Feynman diagrams organize by topology: genus-$h$ surfaces
are weighted by $N^{2-2h}$, so the expansion in $1/N$ looks like a string genus expansion.

## Motivation

't Hooft (1974) proposed this as a route to solving QCD: the large-$N$ theory should be a
weakly coupled string theory, with the "master field" dominating the path integral. Which
string theory remained unknown until [[hep-th-9711200|Maldacena 1997]] identified it (for
$\mathcal{N}=4$ SYM) as the IIB string on $AdS_5\times S^5$, with the master field being the
AdS supergravity background.

## Key formulas

$$\lambda = g^2_{YM}N \ \text{fixed},\qquad \text{amplitudes} \sim \sum_h N^{2-2h} f_h(\lambda)$$

Under the AdS/CFT dictionary: $g_s \sim g_{YM}^2$, so $1/N$ = string loops, and
$R^4/\alpha'^2 = 4\pi g_s N = \lambda$ (up to convention) — large $\lambda$ = weakly curved
gravity, small $\lambda$ = perturbative gauge theory (strong/weak duality). Quantum-gravity
effects (e.g. Hawking radiation) are $1/N$ effects.

## Relations

Belongs to [[ads-cft-correspondence]]. Person: [[gerard-t-hooft]]. Related:
[[holographic-principle]], [[matrix-theory]].

## Where it appears

[[hep-th-9711200|Maldacena 1997]] §1, where the 't Hooft string is finally identified.
