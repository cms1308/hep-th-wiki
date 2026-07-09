---
type: concept
title: Veneziano limit
aliases: []
tags: [large-n, gauge-theory]
prerequisites: []
created: 2026-07-04
updated: 2026-07-04
---

## Definition

The large-$N$ limit of a gauge theory in which the number of flavors grows with the
number of colors at fixed ratio,
$$N, N_f \to \infty\,,\qquad \alpha \equiv \frac{N_f}{N} \ \text{fixed}\,,$$
in contrast to the [[large-n-thooft-limit|'t Hooft limit]], where $N_f$ is held fixed.
Flavor loops then contribute at leading order, and the flavor symmetry grows with $N$.

## Motivation

Many statements about large-$N$ SCFTs depend qualitatively on whether $N_f$ is $O(1)$
or $O(N)$: conformal windows are naturally parameterized by $\alpha$ (SQCD's
[[conformal-window]] $\tfrac32 N < N_f < 3N$ is the fixed-ratio window
$\tfrac32 < \alpha < 3$), and entire families of fixed points exist *only* at fixed
$\alpha$ ([[2510.19136|Cho-Lee-Song 2025]] find classes with
$N_{\text{rank-}2} = 0, \tfrac12, \tfrac32, \tfrac52$ that have no fixed-$N_f$
counterpart).

## Key formulas

In the classification of [[2510.19136|Cho-Lee-Song 2025]], the superconformal
R-charges in the Veneziano limit are universal functions of
$(N_{\text{rank-}2}, \alpha)$ only:
$$r_{\text{rank-}2} = \frac{6N_{\text{rank-}2}^2 - 6N_{\text{rank-}2} - 3\alpha^2
+ \alpha\sqrt{18 + 2N_{\text{rank-}2}^2 - \alpha^2}}
{3(2N_{\text{rank-}2}^2 - \alpha^2)} + O(N^{-1})\,,$$
with an analogous closed form for $r_{\text{fund}}$. For Type I
($N_{\text{rank-}2}=1$), lowering $\alpha$ triggers successive decouplings of $qq'$,
$qXq'$, $qX^2q'$, …, producing an infinite sequence of second-order phase transitions
in the R-charges at $\alpha \simeq 0.177124,\ 0.100506,\ 0.0703675, \ldots$; the
$\alpha \to 0$ limit does not exist for Type I.

## Relations

- Refines the [[large-n-thooft-limit|'t Hooft limit]] (recovered as $\alpha \to 0$
  when that limit exists).
- WGC thresholds are naturally expressed in $\alpha$: the
  [[nakayama-nomura-wgc-bound|Nakayama-Nomura bound]] fails for SQCD at
  $\alpha^{-1} = N_f/N \gtrsim 2.1$ and for other families at family-specific
  $\alpha$ thresholds, while the [[modified-ads-wgc-3c-2a|modified bound]] holds for
  all $\alpha$ ([[2308.01717|Cho-Choi-Lee-Song 2023]],
  [[2510.19136|Cho-Lee-Song 2025]]).

## Where it appears

- [[2510.19136|Cho-Lee-Song 2025]] — Veneziano universality formulas, decoupling
  phase transitions, Veneziano-only universality classes.
- [[2308.01717|Cho-Choi-Lee-Song 2023]] — WGC tests at fixed $\alpha = N_f/N$.
