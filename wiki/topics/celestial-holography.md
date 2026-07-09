---
type: topic
title: Celestial holography
aliases: [celestial CFT, CCFT]
tags: [celestial-holography, flat-space-holography, asymptotic-symmetries]
prerequisites: ["flat-space-holography"]
created: 2026-07-03
updated: 2026-07-06
---

## Overview

The proposal that quantum gravity in 4d asymptotically flat space is dual to a 2d CFT on the
*celestial sphere*. Amplitudes are recast in a boost (rather than energy) eigenbasis via
Mellin transform in the frequency: $\mathcal S$-matrix elements become
[[celestial-amplitude|celestial amplitudes]], transforming as correlators of 2d conformal
primaries with dimensions $\Delta \in 1 + i\mathbb R$ (principal series). The strength of the
program is symmetry: soft theorems become currents (a $U(1)$ Kac–Moody from the photon, a 2d
stress tensor from the subleading soft graviton), and the tower of soft gravitons generates
the [[lw-infinity-algebra|$Lw_{1+\infty}$ algebra]], transparent on twistor space.

This is one of the two routes to [[flat-space-holography]]; it is equivalent to Carrollian
holography for massless scattering by an invertible integral transform
([[carrollian-celestial-equivalence]], reviewed in [[2602.02644|Ruzziconi 2026]]).

## Historical development

- **2013–17**: [[andrew-strominger|Strominger]]'s IR triangle (soft theorems ↔ asymptotic
  symmetries ↔ memory); Pasterski–Shao–Strominger define celestial amplitudes via Mellin
  transform.
- **2019–21**: conformally soft theorems; celestial OPEs from collinear limits;
  Guevara–Himwich–Pate–Strominger discover $Lw_{1+\infty}$ in the soft-graviton tower.
- **2022–26**: bridge to Carrollian holography ([[2212.12553|Donnay et al. 2022]],
  [[2312.10138|Mason–Ruzziconi–Srikant 2023]]); twistor/self-dual realizations of the
  celestial symmetries.
- **2025–26**: the soft algebras enter AdS$_4$/CFT$_3$: the gauge-theory [[s-algebra]] is
  realized undeformed by [[light-ray-operators|light transforms]] of the boundary current
  ([[2601.00096|Sheta–Strominger–Tropper–Wei 2025]]); every CFT$_3$ carries the
  $\Lambda$-deformed [[lambda-deformed-w-algebra|$\mathcal L_\Lambda w_{1+\infty}$]] from
  ANEC descendants ([[2603.26459|Strominger–Wei 2026]]); and the $S$-algebra is argued
  quantum-exact for the IR-finite hard amplitudes of planar $\mathcal N=4$ SYM
  ([[2606.08582|Alday–Strominger 2026]]).

## Key concepts

- [[celestial-amplitude]] — Mellin-transformed $\mathcal S$-matrix element as 2d correlator.
- [[soft-graviton-theorems]] — origin of the celestial currents ($P = i\bar\partial S_0^+$,
  celestial stress tensor $\bar T$).
- [[lw-infinity-algebra]] — the infinite chiral symmetry of celestial gravity.
- [[s-algebra]] — the soft gluon tower of celestial gauge theory.
- [[lambda-deformed-w-algebra]] — its cosmological-constant deformation, linking to AdS.

## Key results

- [[carrollian-celestial-equivalence]] — equivalence with the Carrollian formulation.
- [[ads4-s-algebra-from-cft3-light-transforms]] — the $S$-algebra exists in AdS$_4$/CFT$_3$.
- [[every-cft3-has-l-lambda-w-symmetry]] — $\mathcal L_\Lambda w_{1+\infty}$ in any CFT$_3$.
- [[undeformed-s-algebra-planar-n4-sym]] — quantum-exact soft algebra in planar
  $\mathcal N=4$ SYM.

## Current status

Structurally rich but analytically awkward as a standalone CFT: low-point functions are
distributional ($\delta(\sum_i\Delta_i - \text{const})$ type supports), the spectrum is
continuous and complex, and OPEs fail associativity in the standard sense — obstructions to
a conventional bootstrap. The Carrollian perspective explains these features as natural
consequences of ultra-locality and bulk translation invariance ([[2602.02644|Ruzziconi 2026]] §8).

## Open questions

- Standalone (non-limit) definition of the celestial CFT; state-operator map.
- Spacetime meaning of $Lw_{1+\infty}$ beyond the self-dual sector.
- Incorporating massive states and loop corrections systematically.
- Bulk AdS$_4$ and de Sitter avatars of the deformed algebras
  ([[soft-algebras-for-gravity-in-ads4]]).
