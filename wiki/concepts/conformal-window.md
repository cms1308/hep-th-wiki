---
type: concept
title: Conformal window
aliases: []
tags: [gauge-theory, supersymmetry, rg-flow]
prerequisites: [renormalization-group]
created: 2026-07-03
updated: 2026-07-04
---

## Definition

The range of matter content for which a gauge theory flows to an interacting conformal
fixed point in the IR. For 4d $\mathcal{N}=1$ $SU(N)$ SQCD with $N_f$ flavors
$Q,\tilde Q$, the conformal window is
$$\frac{3}{2}N \;<\; N_f \;<\; 3N$$
(Seiberg, [hep-th/9411149](https://arxiv.org/abs/hep-th/9411149)): above $3N$ asymptotic
freedom is lost; below $\tfrac32 N$ the IR is described by the free magnetic dual rather
than an interacting SCFT.

## Motivation

Conformal-window SCFTs are the simplest large family of interacting non-holographic 4d
SCFTs — strongly coupled, yet with $a$, $c$, $k_F$ exactly computable from anomalies. They
are therefore the natural testing ground for conjectures about "any CFT", such as
WGC-type bounds.

## Key formulas

- At the fixed point the superconformal R-charge of the quarks is fixed by anomaly freedom:
  $R_Q = 1 - N/N_f$, so the baryon $\epsilon Q^N$ has
  $\Delta = \tfrac32 N (1 - N/N_f)$.
- Central charges and $k_B$ (baryon-number flavor central charge) follow from the anomaly
  formulas — see [[flavor-central-charge]].

## Relations

- The IR fixed points come in Seiberg-dual pairs ([[seiberg-duality]]).
- R-charges here are fixed by symmetry; in general theories they require
  [[a-maximization]].

## Where it appears

- [[nakayama-nomura-wgc-bound]] — SQCD at $N_f/N \gtrsim 2.1$ is the original
  counterexample to the AdS WGC bound.
- [[2308.01717|Cho-Choi-Lee-Song 2023]] — the [[modified-ads-wgc-3c-2a|modified bound]]
  is satisfied by the baryon throughout the entire conformal window (also for $SO(N)$,
  $Sp(N)$ SQCD).
- [[2510.19136|Cho-Lee-Song 2025]] — conformal windows determined for every family of
  the simple-gauge-group classification: the upper bound on $N_f$ comes from asymptotic
  freedom, and the lower bound is usually 0 but nonzero for adjoint-SQCD-like Type I
  families (e.g. $SU(N)$ with one adjoint: $1 \le N_f \le 2N$; $Sp(N)$ with one
  antisymmetric: $4 \le N_f < 2N+4$).
