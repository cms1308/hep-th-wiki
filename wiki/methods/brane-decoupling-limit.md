---
type: method
title: Brane decoupling (near-horizon) limit
aliases: [decoupling limit, Maldacena limit]
tags: [string-theory, d-branes, ads-cft]
prerequisites: [d-branes, black-brane-solutions]
created: 2026-07-03
updated: 2026-07-03
---

## What it computes

Derives a gauge/gravity duality from a brane configuration: it simultaneously isolates the
brane worldvolume field theory (open-string side) and the near-horizon geometry
(closed-string side), so the two must describe the same physics.

## Prerequisites

[[d-branes]] and their worldvolume gauge theories; black $p$-brane supergravity solutions
([[near-horizon-limit]]).

## How it works

Take $\alpha'\to 0$ holding fixed the energies and the Higgs-vev scale
$$U \equiv \frac{r}{\alpha'} = \text{fixed}$$
(for D3-branes; $U^2 = r/l_p^3$ for M5, $U^{1/2} = r/l_p^{3/2}$ for M2). Bulk gravity
decouples ($G_N\to 0$), the brane theory flows to its conformal point, and in the supergravity
solution the "1" in the harmonic function $f = 1 + \frac{4\pi gN\alpha'^2}{r^4}$ drops,
leaving $AdS\times$(sphere). The overall $\alpha'$ in the metric cancels against Newton's
constant, so bulk dynamics on AdS survives.

## Regime of validity

The derivation uses supergravity, valid when curvature is small: $gN \gg 1$ (D3 case), i.e.
large 't Hooft coupling — complementary to gauge perturbation theory ($gN\ll1$). The duality
itself is conjectured exact.

## Canonical applications

[[hep-th-9711200|Maldacena 1997]]: D3 → [[maldacena-conjecture]] (worked out step by step in
[[d3-near-horizon-limit]]); M2, M5 → $AdS_4\times S^7$, $AdS_7\times S^4$;
[[d1-d5-system]] → $AdS_3\times S^3$. Template: Maldacena–Strominger's NS5-brane analysis
(little strings).
