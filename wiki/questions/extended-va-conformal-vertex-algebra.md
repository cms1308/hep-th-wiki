---
type: question
title: Is the extended vertex algebra a conformal vertex algebra?
aliases: [stress tensor of the extended VA, conformal structure of the extended vertex algebra]
tags: [n2-scft, vertex-operator-algebra, extended-operators, open-problem]
status: open
created: 2026-07-08
updated: 2026-07-08
---

## Statement

Does the [[extended-vertex-algebra]] of a 4d $\mathcal N=2$ SCFT admit a **stress-energy
operator** — a weight-2 element whose modes generate the Virasoro algebra *and* act as
derivations/primary generators on the whole algebra — thereby making it a *conformal* vertex
algebra? Equivalently: is there a genuine stress tensor for the extended operators, or only a
Virasoro-obeying operator that fails to organize the rest of the algebra?

## Why it matters

Conformal structure is what makes an ordinary VOA computable — it gives radial quantization,
highest-weight modules, characters, and modular properties. If the extended VA were conformal,
the whole apparatus of the [[scft-voa-correspondence|SCFT/VOA correspondence]] (characters,
modular data, null-state relations) would extend to line/surface/wall operators. If it is not, a
new organizing principle is needed for the extended sector.

## Main attempts

In the free hypermultiplet ([[free-hypermultiplet-extended-va-opes]]) the weight-2 Schur operator
$T$ satisfies the Virasoro OPE
$$T(z)\,T(0)\sim \frac{-1/2}{z^4} + \frac{2T(0)}{z^2} + \frac{\partial_z T(0)}{z}$$
with central charge $-1$ — so a Virasoro operator exists. But $T$ **fails the primary condition**
on descent operators: e.g. $T(z)\,\mathbf S[q](0)$ is not the standard primary OPE. Hence $T$ is
not a stress tensor of the extended algebra, and whether a genuine one exists (some corrected or
composite weight-2 operator) is left unresolved.

## Current status

Open ~[[2211.04410|Argyres-Lotito-Weaver 2022]]. Tied to the still-unknown generating set of the
extended VA and to whether $\mathbf S[q_I] =_{\mathbb T} q_I$; a resolution likely requires
working out interacting examples (free vector multiplet, conformal gauge theories) beyond the
free hypermultiplet.
