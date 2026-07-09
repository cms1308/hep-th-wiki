---
type: result
title: Classification of non-Higgsable gravity blocks
aliases: [non-Higgsable gravity block classification]
tags: [6d-supergravity, swampland, string-landscape, non-higgsable-cluster]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

[[2607.05496|Hamada-Jeon-Kim 2026]] give a **complete classification** of the
[[non-higgsable-gravity-block|non-Higgsable gravity blocks]] — the
[[supergravity-block|supergravity blocks]] built entirely from
[[non-higgsable-cluster|non-Higgsable clusters]] — of 6d $\mathcal N=(1,0)$ supergravity:

- **12,762** admissible $P$-type LST bases carrying the [[h-string|$H$-string]];
- $N_{\rm tot}=\mathbf{9{,}630{,}606}$ non-Higgsable gravity blocks;
- **34,747** distinct external gauge-algebra patterns; **1,293** distinct external
  gauge-algebra combinations;
- dominant external generator $\mathfrak{su}_2$ on a $-2$ curve (**95.33%** of blocks), most
  common combination $\mathfrak{su}_2^{\oplus 3}$;
- **complete tensor-base lists up to $T=9$**, with new (non-geometric) features appearing
  from $T=10$.

## Derivation sketch

A C++/OpenMP pipeline (~13,200 CPU-hours) enumerates: (1) $P$-type LST sectors sharing an
$H$-string charge $f$; (2) all external generators with $\mathcal C_{\rm ext}\cdot f>0$
attached via the gluing rules $p\overset{n}{-}[q]$; (3) filters each candidate by
[[green-schwarz-sagnotti-mechanism|anomaly cancellation]], worldsheet central-charge bounds
($\sum_i c_{\mathfrak g_i}\le 16$ for $T>1$, $\le 8$ for E-strings), the Gram-matrix
signature condition ($n_+^{\mathfrak L}\le 1$), and the blowdown test (base must reduce to
$\mathbb F_n$/$\mathbb P^2$). Weyl/duality equivalence relations remove redundant bases.

## Assumptions

- Only non-Higgsable gauge algebras (no Higgsable enhancement, no extra charged matter).
- No Abelian gauge factors.
- Practical cutoffs on intersection numbers (single-target $\mathfrak{su}_2,\mathfrak{su}_3$
  capped at 2; leg count $\le 4$; $\le 9$ external sectors) — expected but not proven to be
  complete.

## Status

**Established** as a computational classification. Cross-checked against F-theory geometric
base classifications, with which it **agrees for $T\le 6$**; conjectured to give the
complete tensor-base list for all $T\le 9$. Data released on Zenodo with a Python toolkit.

## Implications

- Provides the combinatorial backbone (allowed tensor bases before gauge/matter
  enhancement) for the full [[6d-supergravity-swampland|6d $(1,0)$ landscape]].
- Produces candidate **non-geometric** supergravities (frozen-singularity NHCs at $T=10,11$)
  whose quantum-gravity UV completion is open
  ([[uv-completion-frozen-nhc-supergravities]]).
- Reduces general-theory construction to gluing blocks and enhancing on non-negative-
  self-intersection tensors.
