---
type: result
title: Large-N universality classes of 4d N=1 SCFTs (Type I/II/III)
aliases: [Type I II III SCFTs, large N universality]
tags: [scft, large-n, classification, central-charges]
status: established
created: 2026-07-04
updated: 2026-07-04
---

Conventions: $a = \tfrac{3}{32}(3\mathrm{Tr}R^3-\mathrm{Tr}R)$, $\Delta = \tfrac32 R$
for chiral operators, Dynkin index $T(\Box_{SU,Sp}) = \tfrac12$, as in
[[2510.19136|Cho-Lee-Song 2025]].

## Statement

Every 4d $\mathcal{N}=1$ gauge theory with simple classical gauge group ($SU(N)$,
$SO(N)$, $Sp(N)$), zero superpotential, and matter admitting a large-$N$ limit with
fixed flavor symmetry that flows to an interacting SCFT — the complete list is 20 $SU$,
6 $SO$, 9 $Sp$ families — falls into one of **three universality classes**, labeled by
the effective number of rank-2 tensor matters
$$N_{\text{rank-}2} = N_{\mathbf{Adj}} + \tfrac12\left(N_S + N_{\bar S} + N_A
+ N_{\bar A}\right) \in \{1, 2, 3\}$$
(for $SO$/$Sp$: $N_S + N_A$; asymptotic freedom forces $N_{\text{rank-}2} \le 3$). At
leading order in $1/N$ the superconformal R-charges are universal — independent of the
gauge group and of the detailed matter content:
$$r_{\text{rank-}2} = 1 - \frac{1}{N_{\text{rank-}2}}\,,\qquad
r_{\text{fund}} = 1 - \sqrt{\frac{1}{18} + \frac{1}{2N_{\text{rank-}2}^2}}\,,$$
up to $O(N^{-1})$ ([[2510.19136|Cho-Lee-Song 2025]]). The three classes:

| | spectrum | central charges | holography |
|---|---|---|---|
| **Type I** ($N_{\text{rank-}2}=1$) | [[dense-spectrum-scft|dense]] ($1/N$ gap, $O(N)$ decoupled free fields) | $a, c = O(N)$, $a \neq c$ | excluded |
| **Type II** ($N_{\text{rank-}2}=2$) | sparse ($O(1)$ gap) | $a \simeq c \simeq \tfrac{27}{128}\dim G$ | candidate (Klebanov-Witten-like) |
| **Type III** ($N_{\text{rank-}2}=3$) | sparse, near-integer dimensions ($r \simeq \tfrac23$) | $a \simeq c \simeq \tfrac14 \dim G$ | candidate ($\mathcal{N}=4$-like) |

In the [[veneziano-limit|Veneziano limit]] $N_f = \alpha N$ the R-charges are universal
functions of $(N_{\text{rank-}2}, \alpha)$ alone; for Type I the decoupling of
$qq'$, $qXq'$, $qX^2q'$, … produces an infinite sequence of second-order phase
transitions in $\alpha$ (first at $\alpha = \tfrac{3-\sqrt7}{2} \simeq 0.1771$).

## Derivation sketch

[[a-maximization]] with a Lagrange multiplier for the anomaly-freedom constraint: at
leading order in $1/N$ the maximization depends on the matter content only through
$\dim(\mathbf{R})/T(\mathbf{R})$, which is $N + O(1)$ for every rank-2 tensor and
$2N + O(1)$ for fundamentals, for all three classical groups — so only
$N_{\text{rank-}2}$ survives. Type I requires iterating
[[flip-deformation|flip-field decoupling]] $O(N)$ times (universality is broken by
model-dependent decoupling at fixed $N_f$, restored in the double-scaling limit
$N \gg N_f \gg 1$: $r_{\text{fund}} = \frac{\sqrt3 - 1}{3}$).

## Assumptions

Interacting IR fixed point; simple classical gauge group; $W = 0$; flavor symmetry
fixed at large $N$ (classes with $N_{\text{rank-}2} = 0, \tfrac12, \tfrac32, \tfrac52$
exist only in the Veneziano limit and are deferred); no accidental symmetries beyond
the treated decouplings. Type II's $\tfrac{27}{128}\dim G$ echoes the Tachikawa-Wecht
$\tfrac{27}{32}$ factor of $\mathcal{N}=2 \to \mathcal{N}=1$ adjoint-mass flows
([0906.0965](https://arxiv.org/abs/0906.0965)).

## Status

Established by exhaustive enumeration and analytic large-$N$ $a$-maximization
([[2510.19136|Cho-Lee-Song 2025]]); the Type I subset was found earlier in
Agarwal-Lee-Song ([2007.16165](https://arxiv.org/abs/2007.16165)).

## Implications

- The classification is the arena in which the [[modified-ads-wgc-3c-2a|modified AdS WGC]] was
  tested with zero counterexamples — including the non-holographic Type I
  theories, which is what makes the test meaningful for "any CFT".
- Types II/III supply new concrete holographic candidates without known supergravity
  duals ([[holographic-duals-of-type-ii-iii]]).
- The realized $a/c$ values ($0.6930 \lesssim a/c \lesssim 1.1332$ within the
  classification) sharpen the empirical central-charge-ratio question
  ([[n1-central-charge-bounds]]).
