---
type: result
title: High-Temperature Entropic Superconductivity
aliases: [entropic superconductivity, high-Tc from entropic order]
tags: [entropic-order, superconductivity, bcs, large-n, quantum-field-theory]
status: conjectured
created: 2026-07-07
updated: 2026-07-07
---

## Statement

Coupling BCS fermions to $N$ near-critical bosons (a [[high-temperature-order-in-qft|critical $O(N)$ sector]]) makes the effective Cooper attraction *grow* with temperature,

$$g_{\rm eff}(\sigma) = \frac{g}{1 - \tfrac12 g\, t\, \sigma},$$

so the superconducting gap equation retains a nonzero solution

$$\Delta^2(T) \sim t^{-1}\, T^{d-1} \neq 0$$

for all temperatures up to $T \lesssim \omega_*$ (the pairing cutoff). Superconductivity persists to arbitrarily high temperature — an exponential enhancement over the standard $T_c \sim \omega_*\, e^{-1/g\nu}$ — as a realization of [[entropic-order]]. Here $t > 0$ is a **dangerously irrelevant** coupling (mass dimension $d - 3$).

## Derivation sketch

Hubbard–Stratonovich the attractive interaction into a Cooper field $\Delta$ and integrate out the fermions ($\mathrm{tr}\log$ of the Nambu operator). Coupling the pairing channel to the critical boson field $\sigma$ (whose thermal expectation grows with $T$, as in the entropically ordered QFT) shifts the coupling to $g_{\rm eff}(\sigma)$. Solving the coupled $\sigma, \phi, \Delta$ gap equations with Matsubara sums, the growth of $\sigma$ with $T$ compensates the usual thermal suppression of the BCS kernel

$$\frac{1}{g_{\rm eff}} = \nu\int_0^{\beta\omega_*}\!dx\;\frac{\tanh\!\big(\tfrac12\sqrt{x^2 + (\beta\Delta)^2}\big)}{\sqrt{x^2 + (\beta\Delta)^2}},$$

whose right-hand side would otherwise vanish as $\beta \to 0$ and kill ordinary superconductivity.

## Assumptions

- Large $N$ of critical bosons; leading-order saddle-point (gap-equation) analysis.
- The pairing cutoff $\omega_*$ (Debye-like) and a coupling $t > 0$ to the critical sector.
- Robustness to dynamical $U(1)$ gauge fluctuations is only partially argued.

## Status

Conjectural toy model — a proof of principle within large-$N$ field theory, not a claim about a specific material. Whether any real system (e.g. many-band superconductors with near-critical phonons) realizes it, versus a mere zero-temperature enhancement of the coupling, is open.

## Implications

- Shows entropic order is not a curiosity of solids and magnets: it can in principle drive high-$T_c$ superconductivity.
- Recasts the search for high-$T_c$ pairing as a search for a temperature-growing effective attraction sourced by a near-critical sector.

## Where it appears

- Introduced in [[2503.22789|Han et al. 2025]] (Entropic Order).
