---
type: question
title: What completes the AdS/CFT dictionary at the boundary?
aliases: [AdS boundary conditions problem]
tags: [ads-cft, holography]
status: resolved
created: 2026-07-03
updated: 2026-07-03
---

## Statement

[[hep-th-9711200|Maldacena 1997]] conjectured the duality but explicitly left open which
boundary conditions (and possible boundary degrees of freedom) at AdS infinity the gauge
theory prescribes — i.e. *how to actually compute* CFT quantities from the bulk.

## Why it matters

Without an observable-level map the duality cannot be checked or used; AdS is not globally
hyperbolic, so boundary data is part of the theory's definition.

## Main attempts

Resolved within months by Gubser–Klebanov–Polyakov (hep-th/9802109) and Witten
(hep-th/9802150) ([[gkp-witten]]): boundary values $\phi_0$ of bulk fields source CFT
operators,
$$Z_{string}\big[\phi\to\phi_0\big] = \Big\langle e^{\int d^4x\,\phi_0(x)\,\mathcal{O}(x)}\Big\rangle_{CFT}.$$

## Current status

Resolved — the GKP–Witten dictionary is the computational backbone of
[[ads-cft-correspondence]]. Kept as a page for the historical flow; successor questions live
in [[black-hole-information-paradox]] (how the *interior* is encoded).
