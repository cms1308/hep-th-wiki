---
type: topic
title: Holographic entanglement entropy
aliases: [holographic entanglement entropy, HEE, RT/HRT]
tags: [holography, entanglement, ads-cft, quantum-information]
prerequisites: [ads-cft-correspondence, anti-de-sitter-space]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

Holographic entanglement entropy (HEE) computes the [[entanglement-entropy|entanglement entropy]] of a region $A$ in a holographic CFT from bulk geometry: it is the area, in Planck
units, of a codimension-two [[extremal-surface|bulk surface]] anchored on the entangling
surface $\partial A$. In static spacetimes the surface is minimal ([[ryu-takayanagi-formula|Ryu-Takayanagi]]);
in general time-dependent spacetimes it is extremal ([[hrt-formula|HRT]]). The single formula
$$S_A=\frac{\mathrm{Area}(\gamma_A)}{4G_N}$$
recasts a notoriously hard field-theory quantity as a classical geometry problem, and turns
[[bekenstein-hawking-entropy|Bekenstein-Hawking]]'s Area$/4G_N$ into a statement about
entanglement. This launched the "entanglement builds spacetime" program and, downstream, the
quantum extremal surface and island resolutions of the black-hole information problem.

## Historical development

- **Pre-history.** Black-hole entropy as entanglement / the area-law intuition
  (Bombelli-Koul-Lee-Sorkin 1986, Srednicki 1993); 2d CFT entanglement entropy
  $S=\frac c3\log(\ell/a)$ (Holzhey-Larsen-Wilczek 1994, Calabrese-Cardy 2004).
- **The RT formula (2006).** [[hep-th-0603001|Ryu-Takayanagi]] propose $S_A=\mathrm{Area}(\gamma_A)/4G_N$
  with $\gamma_A$ a static minimal surface, checked exactly in AdS$_3$/CFT$_2$ and applied to
  higher dimensions, finite temperature, and the area law.
- **Covariant generalization (2007).** [[0705.0016|Hubeny-Rangamani-Takayanagi]] replace the
  minimal surface by a Lorentzian extremal surface ($\theta_+=\theta_-=0$), motivated by the
  [[bousso-bound|covariant entropy bound]]; verified on rotating BTZ and monotonic growth in
  Vaidya-AdS collapse.
- **Proofs and refinements (later).** Bulk-replica derivation (Lewkowycz-Maldacena 2013;
  covariant version Dong-Lewkowycz-Rangamani); $1/N$ quantum corrections (Faulkner-Lewkowycz-Maldacena)
  and the quantum extremal surface (Engelhardt-Wall), leading to the island formula.

## Key concepts

- [[entanglement-entropy]] — the boundary quantity being computed.
- [[extremal-surface]] — the RT (minimal) / HRT (extremal) bulk surface.
- [[bousso-bound]] — covariant entropy bound / light-sheets, the covariant engine.
- [[bekenstein-hawking-entropy]] — the Area$/4G_N$ template and normalization.

## Key results

- [[ryu-takayanagi-formula]] — static minimal-surface HEE; exact AdS$_3$/CFT$_2$ check.
- [[hrt-formula]] — covariant extremal-surface HEE for time-dependent backgrounds.

## Current status

The RT/HRT prescriptions are established and derived from AdS/CFT, with a well-developed
quantum (island) extension. HEE is now a standard tool for characterizing holographic states,
proving entropy inequalities (strong subadditivity, monogamy), reconstructing bulk geometry,
and analyzing black-hole information.

## Open questions

- First-principles selection among competing extremal surfaces and the full space of
  holographic entropy inequalities.
- Reconstructing the bulk metric from the entanglement entropies of all subregions
  (entanglement-geometry inversion).
- The precise reason entanglement entropy saturates the thermodynamic (Bousso) bound.
