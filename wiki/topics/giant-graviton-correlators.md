---
type: topic
title: Giant Graviton Correlators
aliases: ["giant graviton correlators", "defect approach to giant gravitons", "heavy-operator holographic correlators"]
tags: [ads-cft, giant-graviton, defect-cft, holographic-correlators, n4-sym]
prerequisites: ["maldacena-conjecture", "giant-graviton"]
created: 2026-07-08
updated: 2026-07-08
---

## Overview

This topic collects the program that computes correlation functions of **heavy** operators — [[giant-graviton|giant gravitons]], the dimension-$\Delta=N$ determinant operators of $\mathcal{N}=4$ SYM dual to wrapped D3-branes — at strong coupling, by reinterpreting them as **defect** systems. The organizing idea is that a pair of giant gravitons in a four-point function can be traded for a zero-dimensional ([[giant-graviton-defect|$p=0$]]) conformal defect: dividing by the heavy two-point function turns $\langle\mathcal{O}\mathcal{O}\mathcal{D}\mathcal{D}\rangle$ into a two-point function of the light operators in a defect background, $\langle\!\langle\mathcal{O}\mathcal{O}\rangle\!\rangle=\langle\mathcal{O}\mathcal{O}\mathcal{D}\mathcal{D}\rangle/\langle\mathcal{D}\mathcal{D}\rangle$. This imports the mature defect-CFT / Witten-diagram bootstrap and the four-point superconformal kinematics of $\mathcal{N}=4$ SYM into a heavy-operator problem that was previously accessible only in free theory or to a few loops at weak coupling.

This is a distinct thread from the [[giant-graviton-expansion]], which sums giant-graviton branes to reconstruct the *finite-$N$ superconformal index*. Here individual giant gravitons are external heavy operators in a *correlator*, and the physics of interest is the non-planar, "granular" structure of color that light single-trace operators cannot resolve.

## Historical development

- **2000–2002** — Giant gravitons introduced as $S^3\subset S^5$ D3-branes (McGreevy–Susskind–Toumbas; Balasubramanian–Berkooz–Naqvi–Strassler; Hashimoto–Hirano–Itzhaki), with the determinant / Schur-polynomial dictionary (Corley–Jevicki–Ramgoolam) and the fluctuation spectrum (Das–Jevicki–Mathur), all downstream of [[hep-th-9711200|Maldacena 1997]].
- **2016–2018** — Technical prerequisites mature: the Rastelli–Zhou holographic-correlator bootstrap for $AdS_5\times S^5$ supergravitons, and the [[ten-dimensional-hidden-conformal-symmetry|10d hidden conformal symmetry]] of Caron-Huot–Trinh.
- **2019–2024** — Determinant-operator correlators computed at weak coupling and via integrability (three-point functions; four-point functions to three loops), with an integrated-correlator localization prediction (Brown–Wen–Xie 2024) and the $p=-1$/$\mathbb{RP}^4$ defect correlators of Zhou 2024 as the methodological bridge.
- **2025** — [[2503.22987|Chen-Jiang-Zhou 2025]] (letter): the defect reformulation; all strong-coupling two-giant, two-light correlators fixed up to a constant and packaged by a partially broken 10d hidden symmetry, with a weak-coupling integrand conjecture.
- **2026** — [[2602.13570|Chen-Jiang-Zhou 2026]] (long version): all KK levels, parity-odd $p=0$ defect blocks, Mellin space and flat-space limit, the complete [[giant-graviton-defect-anomalous-dimensions|defect double-particle anomalous-dimension spectrum]], the quantum-vs-classical moduli-averaging distinction, and the general [[llhh-correlator|LLHH]] claim that any heavy-pair correlator reduces to a defect two-point function.

## Key concepts

- [[giant-graviton]] — determinant/sub-determinant $\tfrac12$-BPS operators dual to wrapped D3-branes.
- [[giant-graviton-defect]] — the $p=0$ conformal defect from a giant-graviton pair; parity-odd defect blocks.
- [[ten-dimensional-hidden-conformal-symmetry]] — Caron-Huot–Trinh symmetry, partially broken by the defect, generating all correlators from one seed.
- [[llhh-correlator]] — light-light-heavy-heavy correlators and their universal defect description.

## Key results

- [[giant-graviton-defect-correlators]] — all strong-coupling two-giant, two-light correlators and their generating function.
- [[giant-graviton-defect-anomalous-dimensions]] — closed-form tree-level defect double-particle anomalous dimensions.

## Methods

- [[analytic-defect-bootstrap]] — Witten-diagram ansatz + superconformal Ward identity fixing all correlators up to one constant.

## Current status

The two-giant sector is solved at leading order in $1/N$ (all KK levels, with the full anomalous-dimension spectrum) and cross-checked against free theory, direct supergravity, and localization. The framework is established as the natural strong-coupling language for heavy-pair correlators.

## Open questions

- [[four-giant-graviton-correlators]] — four-giant correlators / defect-defect interactions and expected phase transitions; survival of the hidden symmetry for non-maximal and dual giants.
- Loop ($1/N^2$) and stringy ($\alpha'$) corrections via a defect unitarity method and defect flat-space limit.
- Whether integrability reproduces the extracted defect anomalous-dimension spectrum; applications to black hole microstates and ETH.
