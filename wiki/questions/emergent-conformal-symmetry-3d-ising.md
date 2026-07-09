---
type: question
title: Does the 3D Ising transition have emergent conformal symmetry?
aliases: ["Polyakov conjecture 3D Ising", "emergent conformal symmetry in 3D"]
tags: [conformal-field-theory, 3d-ising, scale-invariance]
status: resolved
created: 2026-07-07
updated: 2026-07-07
---

## Statement

At the critical point, the 3D Ising model becomes scale invariant. Polyakov (1970) conjectured the far stronger statement that it becomes *conformally* invariant — invariant under the full $SO(4,1)$ conformal group, not just dilatations. The question is whether this emergent conformal symmetry can be demonstrated *directly*, and whether the transition might instead be only scale- (not conformally-) invariant.

## Why it matters

Conformal invariance is what makes the [[3d-ising-cft|3D Ising CFT]] a well-defined object with a [[state-operator-correspondence]], a bootstrappable operator algebra, and universal data shared across liquid–vapor criticality, magnets, and $\phi^4$ theory. In $d=2$ conformal symmetry is proven via critical spin chains on $S^1$, but in $d=3$ no lattice tiles the sphere $S^2$, so the direct check was unavailable for half a century. Scale-invariant-but-not-conformal fixed points do exist in principle, so the stronger symmetry could not simply be assumed.

## Main attempts

- **Numerical [[conformal-bootstrap]] (2008–2016)** — pins down the spectrum to high precision but *assumes* conformal symmetry as an input; it tests consistency, not emergence.
- **Monte Carlo** — accurate critical exponents, but on non-conformal manifolds ($T^3$, $T^2\times\mathbb R$), so it cannot exhibit the state-operator correspondence.
- **Virial-current arguments** — Meneses–Penedones et al. (2019) argued the 3D Ising [[virial-current]] does not exist, indirect evidence for conformal (not merely scale) invariance.
- **[[fuzzy-sphere-regularization|Fuzzy-sphere regularization]] (2022)** — [[2210.13482|Zhu-Han-Huffman-Hofmann-He]] realized the transition on $S^2\times\mathbb R$ and read the state-operator correspondence directly off the spectrum.

## Current status

**Resolved in the affirmative** for practical purposes. The fuzzy-sphere spectrum organizes into complete 3D [[conformal-multiplet|conformal multiplets]] with no missing or extra states, matches bootstrap dimensions to $<1.6\%$, and shows no low-lying [[virial-current]] — direct evidence of full conformal invariance (see [[fuzzy-sphere-ising-spectrum]]). An analytic proof of emergence remains absent, and the same direct demonstration for other 3D universality classes (gauge theories, deconfined criticality) is the open frontier.
