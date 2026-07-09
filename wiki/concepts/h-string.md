---
type: concept
title: H-string
aliases: [H-string, supergravity string, Kim-Vafa-Xu H-string]
tags: [6d-supergravity, bps-strings, swampland, little-string-theory]
prerequisites: [tensor-charge-lattice]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

The **$H$-string** is a distinguished BPS string in a 6d $\mathcal N=(1,0)$ supergravity,
identified by Kim-Vafa-Xu (2024) and central to the
[[supergravity-block|supergravity-block]] framework of
[[2607.05496|Hamada-Jeon-Kim 2026]]. Its charge $f$ in the
[[tensor-charge-lattice|tensor charge lattice]] satisfies

$$f^2=0,\qquad b_0\cdot f=2,$$

where $b_0$ is the gravitational anomaly vector. It is a critical (heterotic-like)
supergravity string with worldsheet central charges $c_L=20$, $c_R=6$.

## Motivation

Every 6d $(1,0)$ supergravity with $T\ge 1$ — except the exceptional $T=9$, $b_0=0$ theory
— contains an $H$-string. It organizes the entire tensor base: for $T>1$ the $H$-string is
not itself a primitive generator but is *shared* by the $P$-type-endpoint little string
theories,

$$f=\sum_i n_i\,\mathcal C_i,\qquad n_i>0,\qquad \mathcal C_i\cdot f=0,$$

and any generator orthogonal to $f$ must belong to an LST carrying $f$ (a **containment
relation**). This shared $H$-string is exactly what glues the
[[supergravity-block|blocks]] of a theory together: all blocks in one theory share the same
$f$ and the same external generators.

## Key formulas

- Charge: $f^2=0$, $b_0\cdot f=2$.
- Worldsheet central charges: $c_L=20$, $c_R=6$.
- Central-charge bound on gauge algebras it carries:
  $\sum_i c_{\mathfrak g_i}\le 20$ (and $\le 16$ for $T>1$), with
  $c_{\mathfrak g}=k\,\dim\mathfrak g/(k+h^\vee)$ for level $k=f\cdot\mathcal C_i$.
- Existence fails only for $T=9$, $b_0=0$, where the lattice is
  $\Gamma^{1,9}\simeq U\oplus E_8(-1)$ and no $f$ with $b_0\cdot f=2$ exists.

## Relations

- Lives in the [[tensor-charge-lattice]]; its multiples and the orthogonal LST generators
  define a [[supergravity-block]].
- The **external generators** of a block are precisely those with
  $\mathcal C_{\rm ext}\cdot f>0$.
- Distinguishes gravitational from local physics: because a block containing $f$ has a Gram
  matrix with one positive eigenvalue, its BPS strings cannot all become tensionless.

## Where it appears

- Kim-Vafa-Xu 2024 (`Kim:2024eoa`) — identifies the $H$-string and proves finiteness of the
  6d $(1,0)$ spectrum (not yet ingested).
- [[2607.05496|Hamada-Jeon-Kim 2026]] — uses it as the organizing charge of the
  supergravity-block construction.
