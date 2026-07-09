---
type: result
title: Hofman-Maldacena bound
aliases: [a/c bounds, collider bounds on central charges]
tags: [cft, central-charges, positivity]
status: proven
created: 2026-07-03
updated: 2026-07-04
---

## Statement

Bounds on the ratio of 4d conformal central charges from positivity of energy flux in
collider-type experiments ([Hofman-Maldacena 2008](https://arxiv.org/abs/0803.1467)):

- non-supersymmetric 4d CFT: $\;\tfrac{1}{3} \le \tfrac{a}{c} \le \tfrac{31}{18}$,
- $\mathcal{N}=1$ superconformal: $\;\tfrac{1}{2} < \tfrac{a}{c} < \tfrac{3}{2}$
  (strict for interacting theories, as used in
  [[2308.01717|Cho-Choi-Lee-Song 2023]]).

## Derivation sketch

Demand positivity of the integrated energy flux $\langle \mathcal{E}(\theta)\rangle$
measured at infinity in a state created by a stress-tensor insertion; the flux depends on
the three-point structure of $T_{\mu\nu}$, parameterized by $a$ and $c$ (and, with SUSY,
constrained further by the superconformal algebra). Originally conjectural positivity,
since proven from causality/ANEC arguments.

## Assumptions

Unitary, interacting 4d CFT; SUSY versions assume the corresponding superconformal algebra.

## Status

Proven.

## Implications

- For any interacting $\mathcal{N}=1$ SCFT, $a/c < \tfrac32$ implies $3c-2a > 0$ — the
  positivity that makes the [[supersymmetric-cardy-formula-4d|supersymmetric Cardy entropy]]
  $\mathrm{Re}(S) \propto (3c-2a)^{1/3} J^{2/3}$ real and the
  [[modified-ads-wgc-3c-2a|modified AdS WGC bound]] well-defined
  ([[2308.01717|Cho-Choi-Lee-Song 2023]]).
- For non-SUSY CFTs, $a/c \le \tfrac{31}{18}$ still allows $3c-2a < 0$; whether any
  nontrivial 4d CFT realizes $\tfrac32 \le a/c \le \tfrac{31}{18}$ is unknown. The
  largest known interacting $\mathcal{N}=1$ value was $a/c = \tfrac{183}{158} \simeq
  1.158$ (ISS model, quoted in [[2308.01717|Cho-Choi-Lee-Song 2023]]), superseded by
  $a/c = \tfrac{507}{419} \simeq 1.2100$ from the
  [[4d-n1-scft-landscape|SCFT landscape]]
  ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]).
- Empirically, known interacting $\mathcal{N}=1$ theories fill only a narrow slice of
  the window: the 7,346-entry landscape realizes
  $0.7228 \lesssim a/c \lesssim 1.2100$, prompting the conjecture $a/c < \tfrac54$ for
  interacting $\mathcal{N}=1$ SCFTs ([[n1-central-charge-bounds]]).
