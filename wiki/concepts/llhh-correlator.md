---
type: concept
title: Light-Light-Heavy-Heavy (LLHH) Correlator
aliases: ["LLHH correlator", "light-light-heavy-heavy correlator", "heavy-heavy-light-light correlator"]
tags: [cft, defect-cft, ads-cft, heavy-operators, conformal-blocks]
prerequisites: ["giant-graviton-defect"]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

An **LLHH correlator** is a four-point function $\langle\mathcal{O}_{\Delta_1}\mathcal{O}_{\Delta_2}\mathcal{O}_Q\mathcal{O}_Q\rangle$ of two light operators (fixed dimension) and two identical heavy operators (dimension $Q\to\infty$). The central claim is that any such correlator is universally described by a two-point function of the two light operators in the presence of a [[giant-graviton-defect|conformal defect]] created by the heavy pair: in the heavy limit the four-point conformal blocks collapse onto defect two-point blocks. Concretely, the s-channel becomes the defect bulk channel, and the *union* of t- and u-channel blocks becomes the parity-even defect-channel block $\widehat g^+_{\widehat\Delta,s}$ with the background dimension subtracted ($\widehat\Delta=\Delta-Q$).

## Motivation

Because conformal blocks form a complete basis, the reduction holds **nonperturbatively and without supersymmetry** — so the defect language is not a special feature of BPS giant gravitons but the natural kinematics of any heavy-pair correlator. This reframes heavy-operator dynamics (black hole microstates, ETH, large-charge states) as defect CFT.

## Key formulas

- Block reduction in the heavy limit:
$$g_{\Delta,\ell}=\tilde g_{\Delta,\ell}\big|_{Q\to\infty},\qquad \widehat g^+_{\widehat\Delta,s}=\big\{\widehat{\tilde g}_{\widehat\Delta+Q,s}\ (V<1);\ \widehat{\tilde g}\,'_{\widehat\Delta+Q,s}\ (V\ge1)\big\}\big|_{Q\to\infty}.$$
- Confirmed at the Witten-diagram level by a large-$Q$ saddle point: heavy propagators exponentiate and the AdS integral localizes onto the boundary-anchored geodesic.

## Relations

- The [[giant-graviton|giant graviton]] correlators are the supersymmetric, exactly solvable instance; the LLHH statement is the general kinematic backbone.
- Motivates a nonperturbative analytic-functional (Polyakov–Mellin-type) bootstrap program for heavy-operator correlators.
- Belongs to [[giant-graviton-correlators]]; part of [[ads-cft-correspondence]].

## Where it appears

- Argued and demonstrated in [[2602.13570|Chen-Jiang-Zhou 2026]].
