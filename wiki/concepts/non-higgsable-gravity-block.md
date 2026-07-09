---
type: concept
title: Non-Higgsable gravity block
aliases: [non-Higgsable supergravity block, non-Higgsable gravity blocks]
tags: [6d-supergravity, swampland, non-higgsable-cluster, string-landscape]
prerequisites: [supergravity-block, non-higgsable-cluster]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A **non-Higgsable gravity block** (or *non-Higgsable supergravity block*) is a
[[supergravity-block]] built entirely from [[non-higgsable-cluster|non-Higgsable clusters]]
— i.e. every tensor multiplet supports only a *minimal, un-Higgsable* gauge algebra, with
no additional Higgsable gauge enhancement or extra charged matter. Introduced in
[[2607.05496|Hamada-Jeon-Kim 2026]] as the first concrete implementation of the block
framework, because the non-Higgsable subclass is finite and completely enumerable.

## Motivation

Non-Higgsable gravity blocks are the "ground floor" of the
[[6d-supergravity-swampland|6d landscape]]: a general 6d $(1,0)$ supergravity is obtained by
gluing blocks and then *enhancing* gauge algebras and adding matter. Every block sits on top
of a non-Higgsable skeleton, so classifying the non-Higgsable blocks first pins down the
allowed tensor bases before enhancement — the combinatorial backbone the rest of the
classification hangs from.

## Key formulas

Complete classification (source, from a ~13,200 CPU-hour scan):

- **12,762** admissible $P$-type LST bases carrying the [[h-string]];
- $N_{\rm tot}=\mathbf{9{,}630{,}606}$ non-Higgsable gravity blocks;
- 34,747 distinct external gauge-algebra patterns; 1,293 distinct external gauge-algebra
  combinations;
- dominant external generator $\mathfrak{su}_2$ on a $-2$ curve (95.33% of blocks), most
  common combination $\mathfrak{su}_2^{\oplus 3}$;
- complete tensor-base lists to $T=9$; agreement with F-theory geometric bases for
  $T\le 6$; new (non-geometric) features from $T=10$.

## Relations

- A subclass of [[supergravity-block]] (only un-Higgsable gauge algebras).
- Built from [[non-higgsable-cluster]] curve configurations.
- Its enumeration is [[classification-non-higgsable-gravity-blocks|the main result]] of
  [[2607.05496|Hamada-Jeon-Kim 2026]].
- Some blocks contain **frozen-singularity** NHCs, giving candidate non-geometric
  supergravities whose UV fate is open ([[uv-completion-frozen-nhc-supergravities]]).

## Where it appears

- [[2607.05496|Hamada-Jeon-Kim 2026]] — defines and completely classifies them.
