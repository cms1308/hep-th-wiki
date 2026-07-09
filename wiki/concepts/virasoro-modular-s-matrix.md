---
type: concept
title: Virasoro modular S-matrix
aliases: [modular S-matrix, S-transform, Virasoro S-kernel, Racah-Wigner S, character crossing kernel]
tags: [conformal-field-theory, virasoro, modular-invariance, crossing-kernel, virasoro-tqft]
prerequisites: [cardy-density-of-states]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The crossing kernel implementing the modular $S$-transform $\tau\to-1/\tau$ on Virasoro
torus objects. Two versions appear:

- **Character $S$-matrix** (torus one-point with the identity), a plain cosine kernel:
$$S_{P_1P_2} = 2\sqrt2\,\cos(4\pi P_1 P_2).$$
- **Racah-Wigner modular $S$-matrix** (torus one-point with a general operator $P_3$):
$$\widehat{\mathbb S}_{P_1P_2}[P_3]
=\frac{1}{\rho_0(P_2)}\sqrt{\frac{C_0(P_1P_1P_3)}{C_0(P_2P_2P_3)}}\;\mathbb S_{P_1P_2}[P_3],
\qquad \widehat{\mathbb S}_{\id\,P}[\id]=1,$$
with $\rho_0$ the [[cardy-density-of-states|Cardy density]] and $C_0$ the universal OPE data.

## Motivation

Inserting an $\Omega$-loop linked with an edge (an unknot filled with the vacuum projector)
implements $\int dP\,S_{P'P}$ on that edge — a modular $S$-transform, edge by edge. This
"$\Omega$-line / Fourier-transform trick" is the working move behind the
[[chain-mail-formalism|chain-mail]] proof of the
[[ctv-equals-s-transform-of-zvir-squared|CTV main identity]]: replacing external edges by
$\Omega$-linked loops turns $|Z_{\rm Vir}|^2$ into the CTV partition function.

## Key formulas

- Cosine form: $S_{P'P}=2\sqrt2\cos(4\pi P'P)$.
- **Projector property:** $\int_0^\infty dP_2\,\rho_0(P_2)\,S_{P_1P_2}$-type contractions
  collapse to the identity; specifically $\int_0^\infty dP\,S_{P_1P}\,S_{PP_2}$ enforces
  $P_1=P_2$, so $S$ squares to the identity (unitarity of the $S$-transform).
- $\rho_0(P)=\mathbb S_{\id\,P}[\id]$ recovers the [[cardy-density-of-states|Cardy density]]
  as the identity row.

## Relations

- Fourier-conjugate partner of the [[virasoro-6j-symbol|Virasoro $6j$-symbol]]; the two are
  tied by the Post-Tsiares irrational Verlinde formula.
- The kernel in the [[ctv-equals-s-transform-of-zvir-squared|CTV = $S$-transform of $|Z_{\rm Vir}|^2$]] identity, and in the derived $S$-transforms of squared crossing kernels.

## Where it appears

- Integral representation from Teichmüller-space quantization: Teschner and collaborators.
- Racah-Wigner conventions: Collier-Eberhardt-Mühlmann-Zhang 2023, Post-Tsiares 2024,
  Eberhardt 2023.
- As the $S$-transform / Fourier kernel of CTV theory: [[2507.11652|Hartman 2025]].
