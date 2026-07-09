---
type: topic
title: AdS/CFT correspondence
aliases: [gauge/gravity duality, holographic duality, AdS/CFT]
tags: [holography, string-theory, quantum-gravity]
prerequisites: [quantum-field-theory, general-relativity, string-theory-basics, conformal-field-theory]
created: 2026-07-03
updated: 2026-07-08
---

## Overview

The conjectured exact equivalence between quantum gravity (string/M-theory) on asymptotically
anti-de Sitter spacetimes and conformal field theories living on the boundary. The flagship
example is $\mathcal{N}=4$ super-Yang-Mills $\leftrightarrow$ IIB strings on $AdS_5\times S^5$
([[maldacena-conjecture]]). It is simultaneously: a realization of the
[[holographic-principle]], a nonperturbative definition of string theory on AdS backgrounds,
and the identification of [[gerard-t-hooft|'t Hooft's]] large-$N$ string.

## Historical development

- **1974** — 't Hooft observes the [[large-n-thooft-limit|large-$N$ genus expansion]] of gauge
  theory looks like string perturbation theory. The dual string is unidentified for 23 years.
- **1991–95** — black $p$-brane supergravity solutions (Horowitz–Strominger); D-branes
  (Polchinski) give the branes a gauge-theory description.
- **1996** — [[strominger-vafa-entropy|Strominger–Vafa]] count black hole microstates with the
  [[d1-d5-system]]; greybody factors and absorption cross-sections keep matching between brane
  gauge theory and supergravity beyond their expected validity.
- **1997** — [[hep-th-9711200|Maldacena 1997]] explains the agreements: the near-horizon limit
  of branes yields an exact duality, $\mathcal{N}=4$ SYM $\leftrightarrow$ $AdS_5\times S^5$,
  plus the M2, M5, and D1–D5 cousins.
- **1998** — [[gkp-witten|GKP and Witten]] supply the boundary dictionary
  ($Z_{bulk}[\phi_0] = \langle e^{\int \phi_0 \mathcal{O}}\rangle$), resolving
  [[ads-boundary-dictionary]] and making the duality computational.
- **Since** — holographic RG, [[ryu-takayanagi-formula|holographic entanglement entropy]],
  applied holography (QCD, condensed matter), and the modern
  [[black-hole-information-paradox|information-paradox]] program
  ([[quantum-extremal-surface|QES]], islands) all grow from this root.
- **2015–25** — since any CFT is dual to *some* AdS quantum gravity, swampland statements
  become CFT statements: the [[weak-gravity-conjecture]] is translated into the
  [[nakayama-nomura-wgc-bound|Nakayama-Nomura bound]] $\Delta^2/q^2 \le 12c/k_F$, whose
  SQCD counterexamples lead to the [[modified-ads-wgc-3c-2a|modified $3c-2a$ bound]]
  ([[2308.01717|Cho-Choi-Lee-Song 2023]]), validated with zero counterexamples across
  the complete simple-gauge-group large-$N$ classification
  ([[2510.19136|Cho-Lee-Song 2025]]).
- **2024–26** — the flat-space limit $\ell\to\infty$ is shown to act on the boundary as a
  Carrollian limit $c\to0$ ([[flat-carrollian-limit-correspondence]]), so
  [[flat-space-holography]] arises as a controlled limit of AdS/CFT — verified via
  [[flat-space-limit-of-witten-diagrams|flat limits of Witten diagrams]] and realized
  top-down in ABJM ([[2602.02644|Ruzziconi 2026]]).
- **2025–26** — the soft symmetry algebras of [[celestial-holography]] are found *inside*
  AdS$_4$/CFT$_3$: the gauge-theory [[s-algebra]] from
  [[light-ray-operators|light transforms]] of boundary currents
  ([[ads4-s-algebra-from-cft3-light-transforms]], [[2601.00096|Sheta et al. 2025]]) and the
  deformed gravitational [[lambda-deformed-w-algebra|$\mathcal L_\Lambda w_{1+\infty}$]]
  from ANEC descendants in every CFT$_3$ ([[2603.26459|Strominger–Wei 2026]]).
- **2025–26** — heavy-operator correlators become tractable: a pair of
  [[giant-graviton|giant gravitons]] is recast as a [[giant-graviton-defect|zero-dimensional defect]], solving all
  strong-coupling [[giant-graviton-correlators|giant graviton correlators]] via a defect
  bootstrap and a partially broken 10d hidden symmetry ([[2503.22987|Chen-Jiang-Zhou 2025]],
  [[2602.13570|Chen-Jiang-Zhou 2026]]).

## Key concepts

[[anti-de-sitter-space]] · [[large-n-thooft-limit]] · [[holographic-radial-coordinate]] ·
[[holographic-principle]] · [[near-horizon-supersymmetry-enhancement]] · [[d1-d5-system]] ·
[[btz-black-hole]] · [[holographic-entanglement-entropy]] · [[ads3-cft2-correspondence]] ·
[[giant-graviton]] · [[giant-graviton-correlators]]

## Key results

[[maldacena-conjecture]] (with its parameter dictionary) · [[strominger-vafa-entropy]] ·
[[gkp-witten|GKP–Witten dictionary]] · [[ryu-takayanagi-formula]]

## Current status

Unproven but supported by an enormous body of checks (symmetries, spectra, localization,
integrability, entropy matches). Universally used as a working definition of quantum gravity
on AdS backgrounds.

## Open questions

- [[ads-boundary-dictionary]] — resolved (GKP–Witten), kept for history.
- How the bulk interior/horizon is encoded in the CFT ([[black-hole-information-paradox]]).
- The $AdS_2$/Reissner–Nordström puzzle raised already in [[hep-th-9711200|Maldacena 1997]].
- A duality for de Sitter or QCD-like theories; the asymptotically flat case is now
  approached via the Carrollian limit ([[flat-space-holography]]).
