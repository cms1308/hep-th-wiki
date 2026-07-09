---
type: method
title: Convex hull condition
aliases: [Cheung-Remmen condition]
tags: [weak-gravity-conjecture, swampland]
prerequisites: []
created: 2026-07-03
updated: 2026-07-04
---

## What it computes

Whether a theory with several $U(1)$ gauge symmetries satisfies the
[[weak-gravity-conjecture|Weak Gravity Conjecture]]: with multiple charges, a
super-extremal state must exist in *every* charge direction a black hole can carry, not
just along the basis vectors (Cheung-Remmen,
[1402.2287](https://arxiv.org/abs/1402.2287)). The founding WGC paper had required the
weaker statement that sub-extremal states exist along some *basis* of charge-space
directions ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]).

## Prerequisites

The charge-to-mass (or, in CFT language, charge-to-dimension) vectors of the candidate
states, and the extremality surface of the black holes — i.e. the normalization making
extremal black holes the unit ball.

## How it works

1. For each state, form the vector $\vec z$ of charge-to-mass ratios, normalized so that
   extremal black holes have $|\vec z| = 1$.
2. Take the convex hull of the $\pm\vec z$ of all states (bound states realize convex
   combinations).
3. The WGC holds iff the hull contains the unit ball — equivalently, the minimum distance
   from the origin to the hull's boundary is $\ge 1$.

In the $AdS_5$/CFT$_4$ setting of [[2308.01717|Cho-Choi-Lee-Song 2023]]: the flavor
$U(1)$'s are Gram-Schmidt-orthonormalized so $\mathrm{Tr}\,R F_i F_j = \delta_{ij}$, and
each chiral-ring generator contributes the vector with components
$\sqrt{\tfrac{12(3c-2a)}{k_{F_i}}}\,\tfrac{q_i}{\Delta}$ (the
[[modified-ads-wgc-3c-2a|modified-bound]] unit; use $12c$ for the
[[nakayama-nomura-wgc-bound|original bound]]). Only a generating set of the chiral ring is
needed: composites built from the same field ratios have identical charge-to-dimension
ratios.

## Regime of validity

A statement about the spectrum, valid whenever the extremality normalization is known. In
the CFT application, checks are restricted to the chiral ring; "violation" there means no
chiral-ring operator works.

## Canonical applications

- [[2308.01717|Cho-Choi-Lee-Song 2023]] — multi-flavor tests of the modified WGC,
  including the $SO(10)$ theory with $1\,\mathbf{S}+1\,\mathbf{A}+4\,\Box$ whose hull
  distance is exactly 1 (precise saturation), and a proof that certain theories can never
  satisfy the original bound (the hull of *elementary field* vectors already fails).
- [[2510.19136|Cho-Lee-Song 2025]] — applied numerically to every family of the
  simple-gauge-group classification, per $(N, N_f)$ and per
  [[veneziano-limit|Veneziano ratio]] $\alpha$, in the comprehensive validation of the
  modified WGC.
