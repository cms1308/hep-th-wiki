---
type: concept
title: Giant Graviton as a Zero-Dimensional Defect
aliases: ["giant graviton defect", "zero-dimensional defect", "p=0 defect", "giant-graviton defect"]
tags: [defect-cft, giant-graviton, ads-cft, n4-sym, conformal-defect]
prerequisites: ["giant-graviton", "maldacena-conjecture"]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

A pair of [[giant-graviton|giant gravitons]] (determinant operators $\mathcal{D}$) inserted in a correlator can be traded for a **zero-dimensional ($p=0$) conformal defect**: dividing the four-point function by the giant-graviton two-point function turns it into a two-point function of the remaining light operators in a defect background,
$$\langle\!\langle\mathcal{O}_{k_1}\mathcal{O}_{k_2}\rangle\!\rangle=\frac{\langle\mathcal{O}_{k_1}\mathcal{O}_{k_2}\mathcal{D}\mathcal{D}\rangle}{\langle\mathcal{D}\mathcal{D}\rangle}.$$
Geometrically the two heavy operators trace a geodesic in $AdS_5$; its boundary anchor is the $p=0$ defect. The defect breaks the conformal group $SO(5,1)\to SO(1,1)\times SO(4)$ and the R-symmetry $SO(6)\to SO(2)\times SO(4)$, preserving $SU(2|2)\times SU(2|2)\subset PSU(2,2|4)$. It is encoded by embedding-space projectors
$$\mathbb{N}_{AB}=\frac{P_{3,A}P_{4,B}+P_{4,A}P_{3,B}}{P_3\cdot P_4},\qquad \mathbb{M}_{IJ}=\delta_{IJ}-\frac{t_{3,I}t_{4,J}+t_{4,I}t_{3,J}}{t_3\cdot t_4},$$
onto the broken spacetime and R-symmetry directions, together with their antisymmetric "square roots" $\mathbb{n},\mathbb{m}$ (needed because only the simultaneous $3\leftrightarrow4$ exchange, not each separately, is a symmetry).

## Motivation

The reformulation imports two mature toolkits into a heavy-operator problem: the four-point superconformal kinematics of $\mathcal{N}=4$ SYM and the defect-CFT / Witten-diagram bootstrap. It also makes the physics transparent — the heavy pair is a background, and the light operators simply propagate in it.

## Key formulas

- Parity-even/odd defect-channel blocks (a feature unique to $p=0$):
$$\widehat{g}_{\widehat{\Delta},s}^\pm=C_s^{(1)}\!\big(\tfrac{\chi}{2}\big)\times\begin{cases}V^{\widehat{\Delta}/2}, & 0<V<1,\\ \pm\,V^{-\widehat{\Delta}/2}, & V\ge1.\end{cases}$$
Parity-odd ($-$) blocks exist only for zero-dimensional defects; higher-$p$ defect two-point functions are necessarily parity-even.
- Defect cross ratios: $\xi=U/\sqrt V$, $\chi=(1-U+V)/\sqrt V$, $\Sigma=1/\sqrt{\sigma\tau}$, $\bar\Sigma=(\sigma+\tau)/\sqrt{\sigma\tau}$.
- Mass–dimension relation on the $p=0$ defect uses $d=0$: $m^2=\Delta(\Delta-d)\to\Delta^2$.

## Relations

- A $p=0$ member of the [[llhh-correlator|light-light-heavy-heavy]] family; the $p=-1$ analogue is $\mathcal{N}=4$ on $\mathbb{RP}^4$ (Zhou 2024).
- Solved by the [[analytic-defect-bootstrap]]; its correlators are organized by the [[ten-dimensional-hidden-conformal-symmetry|partially broken 10d hidden symmetry]].
- Belongs to [[giant-graviton-correlators]]; part of [[ads-cft-correspondence]].

## Where it appears

- Introduced in [[2503.22987|Chen-Jiang-Zhou 2025]] and developed in detail (parity-odd blocks, Casimir construction, quantum moduli averaging) in [[2602.13570|Chen-Jiang-Zhou 2026]].
