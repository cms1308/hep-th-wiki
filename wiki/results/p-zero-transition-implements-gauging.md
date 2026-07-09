---
type: result
title: p=0 proliferation transition implements gauging a one-form symmetry
aliases: [gauging as a Higgs transition]
tags: [topological-order, tqft, one-form-symmetry, gauging, phase-transition, 2plus1d]
status: proven
created: 2026-07-08
updated: 2026-07-08
---

## Statement

When the driving Abelian anyon $a$ generates an **anomaly-free** [[one-form-global-symmetry|$\mathbb Z_n^{(1)}$]] — i.e. the anomaly integer $p=0$ — the [[proliferation-transition|proliferation transition]] out of the topological phase $\mathcal T$ realizes, as a Higgs transition, the [[gauging-one-form-symmetry|gauging]] of that one-form symmetry:
$$\mathcal T\ \longrightarrow\ \mathcal T/\mathbb Z_n=\mathcal T/(a).$$

## Derivation sketch

At $p=0$ the far-side object $\mathcal T'$ is not a TQFT; the $\mu^2<0$ phase of the transition theory is gapless, with a Goldstone boson $\alpha$ for the spontaneously broken emergent magnetic $\mathrm U(1)_{\mathcal B}$. Adding the minimal-charge local operator $\mathcal O=\Phi^n$ (Eq. 4.5 of [[2603.00245|Cheng–Seiberg 2026]]) explicitly breaks $\mathrm U(1)_{\mathcal B}$ and gaps the Goldstone. The theory then decouples (up to a $\mathbb Z_n$ gauge field $\mathbf c^{(1)}$) into $\mathcal T/\mathbb Z_n$ and an XY model for $\Phi$. Tuning $\mu^2$ through zero drives a transition of BKT type: the winding ($\mathrm U(1)_{\mathcal B}$) symmetry is emergent on one side and explicitly broken on the other.

## Assumptions

- $p=0$ (anomaly-free $\mathbb Z_n^{(1)}$); single light Abelian anyon $a$.
- The gapping deformation $\mathcal O=\Phi^n$ is added (without it the far phase stays gapless).
- No obstructing enrichment: if $\mathcal T$ is enriched by an ordinary $\mathrm U(1)_A$ under which $a$ carries fractional charge ($n_v\neq0\bmod n$), the gauging transition is incompatible and the system is forced into a phase with spontaneously broken $\mathrm U(1)_A$ instead.

## Status

Established in [[2603.00245|Cheng–Seiberg 2026]], generalizing an earlier unpublished $p=0$ recipe (attributed to work with S. Todadri) to all $p$.

## Implications

- Gives a concrete lattice-motivated field theory for "condensing an anyon = gauging a one-form symmetry," with the transition itself (not just the endpoints) described.
- The incompatibility with fractional-charge $\mathrm U(1)_A$ enrichment is a sharp obstruction to symmetry-preserving gauging transitions — a candidate for its own page, [[enrichment-incompatibility-fractional-charge]].
- Contrasts with $p\neq0$, where the transition is a TQFT-to-TQFT [[abelian-hierarchy-construction]] rather than a gauging.
