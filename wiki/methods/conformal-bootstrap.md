---
type: method
title: Conformal bootstrap
aliases: ["numerical conformal bootstrap"]
tags: [conformal-field-theory, numerics, bootstrap]
prerequisites: [conformal-multiplet]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

Rigorous bounds — and, in favorable cases, sharp determinations — of CFT data (scaling dimensions and OPE coefficients) using only conformal symmetry, unitarity, and crossing symmetry of four-point functions, with no reference to a Lagrangian. For the [[3d-ising-cft|3D Ising CFT]] it produces the benchmark spectrum ($\Delta_\sigma\approx0.518$, $\Delta_\epsilon\approx1.413$, …) against which the [[fuzzy-sphere-regularization]] results are compared.

## Prerequisites

- The [[conformal-multiplet]] / operator-product-expansion structure of a CFT.
- Crossing symmetry of a four-point function, expanded in conformal blocks.
- Unitarity (positivity of OPE coefficient squares) and semidefinite-programming solvers.

## How it works

1. Expand a four-point function in conformal blocks in two channels.
2. Impose crossing symmetry: the two expansions must agree.
3. Treat this as a linear functional problem — search for functionals that are positive on all allowed operators, which excludes hypothetical spectra and carves out the space of consistent CFTs.
4. Numerically, solve the resulting semidefinite program; isolated theories (like 3D Ising) appear as kinks/islands in the allowed region.

## Regime of validity

- Assumes conformal symmetry as an *input* — it tests consistency and pins data, but does not by itself prove that a given lattice model flows to a CFT. This is exactly the gap the direct [[state-operator-correspondence]] check on the fuzzy sphere fills.
- Sharpest for theories with few relevant operators; sensitivity to high-dimension and parity-odd operators is limited.

## Canonical applications

- 3D Ising: Rychkov et al. 2008, El-Showk et al. 2012, Kos–Poland–Simmons-Duffin 2016 — the high-precision spectrum used as the benchmark in [[fuzzy-sphere-ising-spectrum]].
- Comparison standard for [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]], whose parity-even dimensions match it to $<1.6\%$ and whose two new parity-odd primaries were beyond its reach.
