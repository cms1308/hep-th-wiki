---
type: concept
title: Dense-spectrum SCFTs
aliases: [dense spectrum]
tags: [scft, large-n, holography]
prerequisites: [conformal-field-theory]
created: 2026-07-04
updated: 2026-07-04
---

## Definition

Large-$N$ SCFTs whose low-lying BPS operator spectrum forms a band with gap of order
$1/N$: as $N \to \infty$ the dimensions of the light chiral operators (e.g.
$\mathrm{Tr}\,X^m$, $q X^n q$ in a theory with a rank-2 tensor $X$) become dense, and
$O(N)$ of them cross the unitarity bound and decouple as free fields. Identified and
classified in Agarwal-Song ([1912.12881](https://arxiv.org/abs/1912.12881)) and
Agarwal-Lee-Song ([2007.16165](https://arxiv.org/abs/2007.16165)).

## Motivation

A CFT with a weakly coupled Einstein-gravity dual must have a *sparse* low-lying
spectrum (and $a \simeq c$); dense-spectrum theories are systematically generated
counterpoints — genuine strongly coupled large-$N$ SCFTs that **cannot** be holographic
in the usual sense. They make broad conjecture-testing meaningful: a bound that holds
only for holographic CFTs would be expected to fail here.

## Key formulas

- Gap between successive light chiral operators: $O(1/N)$; number of decoupled free
  fields: $O(N)$.
- Central charges scale as $a, c = O(N)$ (not $O(N^2)$), with $a \neq c$ at leading
  order — these are the **Type I** theories ($N_{\text{rank-}2}=1$) of the
  [[large-n-universality-classes|universality classification]]
  ([[2510.19136|Cho-Lee-Song 2025]]).

## Relations

- Complement of the sparse Type II/III classes ($a \simeq c$, gap $O(1)$), the
  holographic candidates of the classification.
- The large-$N$ superconformal index of Type I theories lacks the Hawking-Page-like
  saddle transition present for Type II/III ([[2510.19136|Cho-Lee-Song 2025]]).
- Dense-spectrum SQCD-like theories were early test cases for the
  [[nakayama-nomura-wgc-bound|Nakayama-Nomura WGC bound]]
  ([1912.12881](https://arxiv.org/abs/1912.12881),
  [2007.16165](https://arxiv.org/abs/2007.16165)).

## Where it appears

- [[2510.19136|Cho-Lee-Song 2025]] — Type I universality class; what its bulk dual
  could be is posed as an open question.
- [[2308.01717|Cho-Choi-Lee-Song 2023]] — dense-spectrum theories among the WGC test
  set.
