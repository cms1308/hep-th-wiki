---
type: concept
title: Supergravity block
aliases: [supergravity blocks, gravity block]
tags: [6d-supergravity, swampland, string-landscape, bps-strings]
prerequisites: [tensor-charge-lattice, h-string]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A **supergravity block** is a minimal collection of tensor multiplets in a 6d
$\mathcal N=(1,0)$ supergravity, introduced in [[2607.05496|Hamada-Jeon-Kim 2026]] as the
basic building object of the [[6d-supergravity-swampland|6d landscape]]. It consists of:

- a **single little string theory (LST) sector** whose BPS generators $\{\mathcal C_i^a\}$
  all share the distinguished [[h-string]] charge $f$ (i.e. $\mathcal C_i^a\cdot f=0$), plus
- all **external generators** $\{\mathcal C_l^{\rm ext}\}$ — BPS generators whose charges
  intersect $f$ positively, $\mathcal C_{\rm ext}\cdot f>0$ — together with their charged
  matter.

The defining property: the block's Gram matrix $\mathcal G^a_{\alpha\beta}$ (the Dirac
pairing restricted to the block's charges) has **exactly one positive eigenvalue**. A
generic subset of tensors, or a purely local SCFT/LST sector, instead has a negative
(semi-)definite Gram matrix. The single positive direction is what makes a block
*gravitational*.

## Motivation

Any consistent 6d $(1,0)$ supergravity with $T\ge 1$ (except the exceptional $T=9$,
$b_0=0$ theory) can be assembled by **gluing compatible blocks** and then enhancing gauge
algebras and matter on tensors of non-negative self-intersection. Blocks that belong to the
same theory share the same anomaly vector $b_0$ and the same external generators; generators
of distinct LST sectors do not intersect. The framework thus turns the non-perturbative
$H$-string constraints into a constructive, modular recipe for the whole landscape.

## Key formulas

- Block content: LST generators with $\mathcal C_i^a\cdot f=0$ ⊕ external generators with
  $\mathcal C_l^{\rm ext}\cdot f>0$.
- Gram matrix signature (the block criterion): $n_+^{\mathfrak L}=1$, $n_-^{\mathfrak L}\le T$
  — one positive eigenvalue.
- Consequence: because the Gram matrix has a positive direction, no modulus $J$ (with
  $J\cdot J=1$) can make all of the block's BPS strings tensionless simultaneously — the
  block always contains an intrinsically **gravitational BPS (black) string**.

## Relations

- Built on the [[tensor-charge-lattice]] and the [[h-string]] that all block generators
  share (LST sector orthogonal to $f$; external generators intersecting $f$).
- The special case where every gauge algebra is un-Higgsable is a
  [[non-higgsable-gravity-block]] — the subclass completely classified in the source.
- Assembled via the [[green-schwarz-sagnotti-mechanism]] (anomaly consistency) and the
  blowdown structure of the tensor base.
- Contrast with a 6d SCFT/LST sector: those have negative-(semi)definite Gram matrices
  (no positive direction), so their strings *can* all become tensionless — they are local,
  non-gravitational.

## Where it appears

- [[2607.05496|Hamada-Jeon-Kim 2026]] — introduces supergravity blocks and classifies the
  non-Higgsable ones.
- Central object of the [[6d-supergravity-swampland]] topic.
