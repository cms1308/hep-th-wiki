---
type: method
title: Analytic Defect Bootstrap
aliases: ["analytic defect bootstrap", "holographic defect bootstrap", "Witten-diagram defect bootstrap"]
tags: [defect-cft, holographic-correlators, bootstrap, witten-diagrams, n4-sym]
prerequisites: ["giant-graviton-defect", "conformal-bootstrap"]
created: 2026-07-08
updated: 2026-07-08
---

## What it computes

Strong-coupling (tree-level in $1/N$) two-point functions of light operators in the presence of a holographic conformal defect — for [[giant-graviton-defect|giant graviton]] defects, all correlators $\langle\!\langle\mathcal{O}_{k_1}\mathcal{O}_{k_2}\rangle\!\rangle$ — without evaluating any bulk integral in full, by fixing a finite Witten-diagram ansatz with symmetry.

## Prerequisites

- Embedding-space defect kinematics: projectors $\mathbb{N},\mathbb{M}$ (and square roots $\mathbb{n},\mathbb{m}$) and defect cross ratios.
- Defect conformal blocks from the projected quadratic Casimir equations (the $p=0$ specialization of Billò–Gonçalves–Lauria–Meineri blocks, including the parity-odd branches).
- The bulk fluctuation spectrum, from expanding the D3-brane DBI+WZ action about the giant-graviton solution.

## How it works

1. **Ansatz**: write the correlator as a sum of bulk-channel exchange, defect-channel exchange, and contact Witten diagrams, each multiplied by the appropriate R-symmetry polynomial,
$$\mathcal{G}^{\rm ansatz}_{k_1k_2}=\mathcal{G}^{\rm bulk}+\mathcal{G}^{\rm defect}+\mathcal{G}^{\rm contact}.$$
2. **Truncate** the exchanged fields with R-symmetry selection rules and non-extremality cutoffs: $\Delta_\mathcal{X}-\ell_\mathcal{X}<k_1+k_2$ (bulk) and $\widehat\Delta-s\le\min\{k_1,k_2\}$ (defect). Exchange diagrams reduce to finitely many contact diagrams, so the ansatz has finitely many unknowns.
3. **Impose the superconformal Ward identity** $(z\partial_z-\alpha\partial_\alpha)\mathcal{F}|_{\alpha=1/z}=0$ (equivalently $\bar\alpha=1/\bar z$ independence). This fixes all coefficients up to a single overall constant.
4. **Fix the constant** from a protected one-point function / the D3-brane action normalization.

Coefficients across different KK levels are further tied together by the shared single-particle CFT data $\lambda_{k_1k_2k}=\sqrt{k_1k_2k}/N$, and the whole family is then repackaged by the [[ten-dimensional-hidden-conformal-symmetry|partially broken 10d hidden symmetry]].

## Regime of validity

Leading order in $1/N$ (tree-level supergravity) for $\tfrac12$-BPS external operators; requires enough supersymmetry for the Ward identity to be constraining. Loop ($1/N^2$) and stringy ($\alpha'$) corrections need, respectively, a defect unitarity method and a defect flat-space limit (not carried out here).

## Canonical applications

- All maximal-giant-graviton two-point functions at strong coupling — [[2503.22987|Chen-Jiang-Zhou 2025]], [[2602.13570|Chen-Jiang-Zhou 2026]].
- Adapts the $AdS_5\times S^5$ holographic bootstrap (Rastelli–Zhou) and the holographic-defect bootstrap (Giménez-Grau et al.; Zhou's $p=-1$ case) to $p=0$ defects.
