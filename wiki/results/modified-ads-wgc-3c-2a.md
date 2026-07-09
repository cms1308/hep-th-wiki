---
type: result
title: Modified AdS Weak Gravity Conjecture (3c−2a bound)
aliases: [modified WGC, 3c-2a WGC bound]
tags: [weak-gravity-conjecture, swampland, ads-cft, supersymmetry, scft]
status: conjectured
created: 2026-07-03
updated: 2026-07-04
---

Conventions: those of [[2308.01717|Cho-Choi-Lee-Song 2023]] — $k_F \equiv -3\,\mathrm{tr}\,RFF$,
chiral operators obey $\Delta = \tfrac32 R$.

## Statement

Any 4d $\mathcal{N}=1$ SCFT with a $U(1)$ non-R flavor symmetry $F$ contains an operator
$\mathcal{O}$ satisfying
$$\left.\frac{\Delta^2}{q^2}\right|_{\mathcal{O}} \;\leq\; \frac{12(3c-2a)}{k_F}\,,$$
where $a$, $c$ are the conformal central charges and $k_F$ the
[[flavor-central-charge|flavor central charge]]
([[2308.01717|Cho-Choi-Lee-Song 2023]]). This replaces $c \to 3c-2a$ in the
[[nakayama-nomura-wgc-bound|Nakayama-Nomura bound]] $\Delta^2/q^2 \le 12c/k_F$. For several
$U(1)$'s the statement is the [[convex-hull-condition|convex hull condition]] with
charge-to-dimension vectors measured in units of $\sqrt{k_F/[12(3c-2a)]}$. The conjecture is
claimed for *any* 4d SCFT, with or without a weakly coupled gravity dual or a large-$N$
limit.

The bound applies only to **non-R** flavor symmetries: chiral operators saturate the
original bound for the R-symmetry itself ($\Delta = \tfrac32 R$ with $k_R$-analog
$\tfrac{16}{3}c$), and would violate the modified one whenever $c<a$.

## Derivation sketch

Not derived — motivated. The combination $3c-2a$ is what governs the Cardy-like limit of
the [[superconformal-index|4d superconformal index]] and hence the entropy of large BPS
black holes in $AdS_5$ ([[supersymmetric-cardy-formula-4d]]):
$\mathrm{Re}(S) = 2^{1/3} 3^{1/2} (3c-2a)^{1/3}\pi J^{2/3} + O(J^{1/3})$. In 2d, modular
invariance — the property behind Cardy's formula — proves the WGC; by analogy, the quantity
controlling the 4d Cardy formula should control the 4d WGC bound. For holographic theories
$a \simeq c$, so $3c-2a \simeq c$ and the bound reduces to Nakayama-Nomura at large $N$.

## Assumptions

- 4d $\mathcal{N}=1$ superconformal symmetry (needed for $a$, $c$, $k_F$ via anomalies and
  for the BPS/chiral-ring structure used in all checks).
- $3c-2a > 0$: guaranteed for SUSY CFTs by the
  [[hofman-maldacena-bound|Hofman-Maldacena bound]] $\tfrac12 < a/c < \tfrac32$. For
  non-SUSY 4d CFTs $a/c \le \tfrac{31}{18}$ allows $3c-2a<0$, where the statement would be
  non-sensical — though no known nontrivial 4d CFT has $\tfrac32 \le a/c \le \tfrac{31}{18}$.
- All checks use chiral-ring operators; "violation" means no chiral-ring operator satisfies
  the bound.

## Status

Conjectured ([[2308.01717|Cho-Choi-Lee-Song 2023]]); now comprehensively tested with
**zero counterexamples**:

- $SU(N)$, $SO(N)$, $Sp(N)$ SQCD in the [[conformal-window|conformal window]] — including
  the regime $N_f/N \gtrsim 2.1$ where the Nakayama-Nomura bound fails
  ([[2308.01717|Cho-Choi-Lee-Song 2023]]).
- An $SO(10)$ theory with $1\,\mathbf{S}+1\,\mathbf{A}+4\,\Box$ saturates the bound
  *exactly* (convex-hull distance exactly 1) — unexplained
  ([[2308.01717|Cho-Choi-Lee-Song 2023]]).
- The complete classification of simple-gauge-group ($SU$/$SO$/$Sp$) theories with a
  large-$N$ limit, $W=0$, and fixed flavor symmetry — 20+6+9 families spanning all
  three [[large-n-universality-classes|universality classes]], including the
  non-holographic [[dense-spectrum-scft|dense-spectrum]] Type I theories: the bound
  holds **at every finite $N$ and in every [[veneziano-limit|Veneziano limit]]**, with
  some saturating examples, while the Nakayama-Nomura bound fails in many newly
  catalogued places ([[2510.19136|Cho-Lee-Song 2025]]).

Untested: theories with superpotentials; no derivation from gravity
([[gravity-derivation-of-modified-wgc]]) or from a CFT principle
([[higher-dimensional-modularity]]) exists.

## Implications

- Rescues the WGC-in-AdS/CFT program from its known counterexamples: the failures of the
  original bound signal the wrong central-charge combination, not a failure of the WGC.
- If it admits a CFT-side derivation, it would be a 4d analog of the 2d
  modularity-implies-WGC theorems — a clue toward higher-dimensional modularity.
- Ties swampland constraints to BPS black hole entropy: the same $3c-2a$ counts black hole
  microstates and bounds the charged spectrum.
