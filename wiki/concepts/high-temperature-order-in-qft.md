---
type: concept
title: High-Temperature Order in QFT
aliases: [high-temperature order in QFT, persistent symmetry breaking, inverse symmetry breaking]
tags: [entropic-order, quantum-field-theory, large-n, cft, spontaneous-symmetry-breaking]
prerequisites: [large-n-thooft-limit, entropic-order]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

**High-temperature order in QFT** refers to relativistic field theories whose symmetry stays *broken* at all temperatures, including $T\to\infty$ — the field-theory face of [[entropic-order|entropic order]]. The representative construction is the multicritical large-$N$ Lagrangian

$$\mathcal{L} = \tfrac12(\partial\psi)^2 + \tfrac12(\partial\vec\phi)^2 + \tfrac{\lambda}{4N}(\vec\phi^2 - \psi^2)^2, \qquad 2 < d < 3,$$

whose large-$N$ free energy is minimized at $\bar\phi^2 = 0$, $\bar\psi^2 = c_3 T^{d-1} > 0$. The discrete $\mathbb{Z}_2$ symmetry $\psi \to -\psi$ is therefore broken at *every* $T > 0$, and the entropy is *larger* in the ordered ($\bar\psi \neq 0$) state — the same entropic logic as the lattice models.

## Motivation

A relativistic QFT has neither a finite nor a factorizable Hilbert space, so the finite-dimensional no-go theorems on high-$T$ order never applied to it. These multicritical models were the first clean examples that a symmetry can stay broken up to $T\to\infty$; the [[entropic-order]] program later explained the shared mechanism (an unbounded local Hilbert space carrying the ordering entropy) and reproduced it in simple local lattice models.

## Key formulas

- Large-$N$ free-energy density:
$$\frac{\mathcal F}{N} \approx -c_1 T^{d+1} + c_2\, T^{-\frac{2}{d-2}}\big(c_3 T^{d-1} + \phi^2 - \psi^2\big)^{\frac{d}{d-2}} + \cdots,$$
minimized at $\phi^2 = 0$, $\psi^2 = c_3 T^{d-1}$: the condensate *grows* with temperature.
- The onset requires $N$ above an $O(1)$ value (claimed $\gtrsim 3$, unreliable at leading large-$N$).

## Relations

- The QFT realization within the [[entropic-order]] topic; parallel to the lattice [[arithmetic-ising-model]].
- Provides the critical-boson sector coupled to fermions in [[high-temperature-entropic-superconductivity]].
- Analyzed by Hubbard–Stratonovich + large-$N$ thermal field theory (see [[large-n-thooft-limit]] for the general large-$N$ framing).

## Where it appears

- The multicritical $O(N)$-type constructions (Chai, Komargodski et al. 2020) and a local unitary $d=2$ model (Hawashin–Komargodski 2024) predate and motivate the program.
- Worked into the entropic-order framework in [[2503.22789|Han et al. 2025]]; cited as the QFT context in [[2512.07980|Huang et al. 2025]].
