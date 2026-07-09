---
type: topic
title: Carrollian physics
aliases: [Carroll physics, ultra-relativistic limit]
tags: [carrollian-physics, non-lorentzian, null-hypersurfaces]
prerequisites: []
created: 2026-07-03
updated: 2026-07-03
---

## Overview

Carrollian physics is the physics of the $c\to 0$ contraction of relativistic symmetry — the
"other" non-relativistic limit, mirror to the Galilean $c\to\infty$ one. Light cones collapse
to lines: space becomes absolute, time relative, and dynamics ultra-local (no energy
transport between spatial points). Long a curiosity, it became load-bearing when Carrollian
structures were recognized as the intrinsic geometry of *null hypersurfaces* — black hole
horizons and, crucially, [[null-infinity]] — and when conformal Carroll symmetry was shown to
be isomorphic to the [[bms-symmetry|BMS group]] of asymptotically flat gravity. It is now the
kinematic backbone of one of the two main approaches to [[flat-space-holography]].

Main source: [[2602.02644|Ruzziconi 2026]] (review; its conventions are adopted as
wiki-canonical for this topic — see its Conventions section).

## Conventions

Wiki-canonical for this topic, following [[2602.02644|Ruzziconi 2026]]: Lorentzian signature
$(-,+,\cdots,+)$; Carrollian contraction $x^0 = cu$, $c\to0$; Carroll structure
$(q_{ab}, n^a)$ with $q_{ab}n^b = 0$, Ehresmann connection normalized $k_a n^a = -1$; flat
Carroll background $n=\partial_u$, $q = 2dzd\bar z$, $k = -du$; conformal Carroll level
$N=2$.

## Historical development

- **1965–67 — the contraction**: Lévy-Leblond and Sen Gupta contract Poincaré with $c\to0$,
  obtaining the [[carroll-group]] (named for Lewis Carroll's motionless-yet-moving world).
  Vogel, Jankiewicz, Dautcourt study degenerate-metric geometry.
- **1977–79 — null surfaces**: Geroch's treatment of [[null-infinity]] and
  [[marc-henneaux|Henneaux 1979]]'s intrinsic description of null hypersurfaces identify
  Carrollian structures in gravity; Henneaux's zero-signature gravity anticipates the
  electric Carroll limit (BKL-relevant).
- **2014 — the isomorphism**: Duval–Gibbons–Horvathy ([[1402.5894|DGH 2014]]) formalize
  Carrollian (and conformal Carrollian) geometry and prove
  $\mathfrak{CCarr}_d \simeq \mathfrak{bms}_{d+1}$ — BMS *is* conformal Carroll.
- **2014–21 — field theories**: electric vs magnetic contractions of relativistic actions
  (Duval et al.; [[2109.06708|Henneaux–Salgado-Rebolledo 2021]];
  [[2110.02319|de Boer et al. 2021]]) → [[electric-magnetic-carrollian-theories]]; Carroll
  fermions, swiftons, tensionless strings; Carroll symmetry appears in cosmology (dark
  energy, inflation) and condensed matter (flat bands, fractons).
- **2022–26 — holography**: Carrollian CFT correlators proposed as the flat-space dual
  ([[2212.12553|Donnay–Fiorucci–Herfray–Ruzziconi 2022]], [[2202.08438|Bagchi et al. 2022]]);
  [[carrollian-amplitude|Carrollian amplitudes]] ([[2312.10138|Mason–Ruzziconi–Srikant 2023]]);
  equivalence with celestial amplitudes; flat limit of AdS/CFT as a boundary
  Carrollian limit ([[2406.19343|Alday et al. 2024]]); top-down ABJM realization
  ([[2504.10291|Lipstein et al. 2025]]). Consolidated in [[2602.02644|Ruzziconi 2026]].

## Key concepts

- [[carroll-group]] — the $c\to0$ contraction; ultra-locality, collapsed light cones.
- [[carrollian-geometry]] — degenerate metric + kernel vector + Ehresmann connection; the
  intrinsic geometry of null hypersurfaces; torsion generically forced.
- [[conformal-carrollian-algebra]] — level-$N$ conformal extensions;
  $\mathfrak{CCarr}^{\text{glob}}_d\simeq\mathfrak{iso}(d,1)$.
- [[bms-symmetry]] — asymptotic symmetries of flat gravity = conformal Carroll at $\mathscr I$.
- [[electric-magnetic-carrollian-theories]] — the two inequivalent $c\to0$ contractions of
  any relativistic theory.
- [[carrollian-cft]] — QFT with conformal Carroll symmetry; electric/magnetic correlator
  branches.
- [[null-brown-york-stress-tensor]] — Carrollian stress tensor of null hypersurfaces;
  conservation = Raychaudhuri + Damour ([[membrane-paradigm]]).

## Key results

- [[bms-conformal-carroll-isomorphism|BMS ≅ conformal Carroll]]
  ($\mathfrak{bms}_{d+1}\simeq\mathfrak{CCarr}_d$, proven).
- [[carrollian-celestial-equivalence]] — Carrollian and celestial holography are equivalent
  for massless scattering.
- [[flat-carrollian-limit-correspondence]] — bulk $\ell\to\infty$ ⇔ boundary $c\to0$
  ($c_{\text{bdy}} = \ell^{-1}$), verified at correlator level.
- [[carrollian-quantization-obstruction|Quantization obstruction]] — lattice-regularized
  electric Carroll theories are generalized free fields ([[2407.11971|Cotler et al. 2024]]).

## Current status

Kinematics and geometry are settled; classical Carrollian field theories are well charted.
The frontier is quantum: no Lagrangian quantization yields the interacting, time-dependent
Carrollian correlators that flat holography requires — the working definition of the
holographic Carrollian CFT is currently *the limit of AdS/CFT correlators*, not an intrinsic
theory. See [[flat-space-holography]] for the holographic program built on this topic.

## Open questions

- [[intrinsic-definition-of-carrollian-cft]] — does a standalone holographic Carrollian CFT
  exist?
- Quantization of electric Carrollian theories (regulator preserving interactions).
- [[massive-states-in-carrollian-holography]] — massive scattering at null infinity.
- State-operator correspondence, conformal blocks, and a Carrollian bootstrap.
