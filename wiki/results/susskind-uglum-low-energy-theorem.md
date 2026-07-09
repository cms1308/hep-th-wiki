---
type: result
title: Susskind–Uglum Low-Energy Theorem
aliases: [Susskind-Uglum theorem, entropy renormalization theorem]
tags: [black-holes, entropy, renormalization, quantum-gravity]
prerequisites: [bekenstein-hawking-entropy]
status: proven # per Susskind-Uglum 1994; derivation not yet ingested/verified in this wiki
created: 2026-07-06
updated: 2026-07-06
---

## Statement

The total entropy per unit horizon area of Rindler space, in exact thermal equilibrium
(the Unruh density matrix $\rho_u = e^{-2\pi H_r}/Z$), is given by the Bekenstein–Hawking
formula with the *fully renormalized* Newton constant:
$$\frac{S}{A} = \frac{1}{4G}.$$
Equivalently: "radiative corrections to the coupling constant must be in one to one
correspondence with contributions to the entropy in a consistent theory" — every species
that renormalizes $G$ contributes to the Rindler entropy in lockstep, so the relation holds
with the same $G$ that governs gravity at asymptotic distances
([[hep-th-9501106|Susskind 1995]], quoting the theorem of Susskind–Uglum, Phys. Rev. D50
(1994) 2700 [hep-th/9401070]).

## Derivation sketch

As summarized in [[hep-th-9501106|Susskind 1995]] (the full derivation is in the 1994
Susskind–Uglum paper, not yet ingested): the Rindler entropy is computed from a euclidean
path integral on a cone of deficit angle $2\pi - \beta$ with partition function $Z(\beta)$,
$$S = -\beta^2\, \partial_\beta\!\left[\frac{\log Z(\beta)}{\beta}\right],$$
and the conical path integral, evaluated from the effective gravitational action, depends
only on the fully renormalized Newton coupling $G$.

## Assumptions

- Exact thermal equilibrium: the entropy entering the relation is the full entropy of the
  Unruh state, independent of whatever kinetics would populate it.
- A consistent effective gravitational action whose renormalized $G$ is finite and governs
  asymptotic gravity.

## Status

Stated as a theorem ("a low energy theorem due to the author and Uglum") in
[[hep-th-9501106|Susskind 1995]], citing Susskind–Uglum 1994 for the derivation. The
derivation paper is not yet ingested, so this wiki has not verified the theorem itself —
ingesting hep-th/9401070 would anchor it.

## Implications

- Load-bearing input of the anti-remnant argument of [[hep-th-9501106|Susskind 1995]]: an
  unbounded species degeneracy $e^{S_R}$ makes the equilibrium $S/A$ diverge, and by this
  theorem drives the renormalized $1/G \to \infty$ — the inconsistency that rules out
  information-storing [[black-hole-remnant|remnants]]. Because the theorem refers to exact
  equilibrium, production-rate suppression mechanisms cannot evade the argument.
