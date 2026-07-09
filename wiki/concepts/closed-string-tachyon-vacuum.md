---
type: concept
title: Closed string tachyon vacuum
aliases: ["nothing state", closed string tachyon condensation]
tags: [string-field-theory, closed-string-tachyon, tachyon-condensation]
prerequisites: [closed-string-field-theory]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The classical solution of [[closed-string-field-theory|closed string field theory]] reached by
condensing the closed string tachyon: the vacuum $\Psi_*$ solving the EOM with the tachyon (and
other fields) turned on. In the bosonic string the proposed endpoint is a **"nothing" state** with
vanishing cosmological constant — the action difference exactly cancels the original vacuum energy,
so spacetime itself is removed rather than merely shifted.

Unlike the open string tachyon — whose condensation is the decay of an unstable D-brane, solved
analytically by the $KBc$ subalgebra — the closed string tachyon couples to the metric and dilaton,
so its condensation restructures spacetime. This is why an analytic construction is prized: it would
give a nonperturbative window on the closed-string landscape and a concrete instance of background
independence.

## Motivation

The zero-momentum bosonic closed string tachyon has $m^2=-4/\alpha'$ ($=-2$ at $\alpha'=2$), an
instability of the 26d vacuum. Where the field rolls, and what sits at the bottom, is a long-standing
question. Level-truncation analysis showed the answer is not a tachyon condensate alone:
[[ghost-dilaton-condensation-tachyon-vacuum|the ghost dilaton must condense with it]]. The recursive
program of [[2603.29926|Kim 2026]] aims to construct the vacuum order by order from the
[[fvm-quadratic-integral-equation|quadratic integral equation]].

## Key formulas

- Zero-momentum tachyon: weight $h=\bar h=-1$, $m^2=-4/\alpha'=-2$ at $\alpha'=2$.
- Yang–Zwiebach level-truncation vacuum: tachyon $t_*\simeq0.416$ at cubic order; with the ghost
  dilaton, $t_*\simeq0.338$, $d_*\simeq0.49$.
- [[seam-graded-expansion|Seam-graded]] grade-0 tachyon seed at the
  [[systolic-threshold|systolic length]]:
  $g_T^{(0)}(L_*)=1/(C_A V_T^{\mathrm{eff}}(L_*,L_*,L_*))\simeq8.10\times10^{-10}$.
- Tachyon-only convergence ratio: $\epsilon_B=|S_1^T(L_*)|/|g_T^{(0)}(L_*)|\simeq2.6\times10^{18}$
  (diverges).

## Relations

- Lives in [[closed-string-field-theory]]; constructed from [[hyperbolic-string-vertices]] via the
  [[fvm-quadratic-integral-equation]].
- Solved perturbatively by the [[seam-graded-expansion]].
- Its defining physical input is [[ghost-dilaton-condensation-tachyon-vacuum|ghost-dilaton condensation]].
- Contrast with the *open* string tachyon vacuum (D-brane decay), solved by the $KBc$ algebra; a
  closed-string analog is [[closed-string-kbc-algebra|sought but not known]].

## Where it appears

- Level-truncation construction and the ghost-dilaton requirement (Yang–Zwiebach 2005).
- Recursive-algebraic construction and the tachyon-only divergence: [[2603.29926|Kim 2026]].
