---
type: result
title: Carrollian–celestial equivalence
aliases: [Carrollian/celestial correspondence]
tags: [flat-space-holography, celestial-holography, carrollian-physics]
status: established
created: 2026-07-03
updated: 2026-07-03
---

## Statement

For massless scattering, Carrollian and celestial holography are *equivalent*: celestial
primaries are an invertible integral transform of Carrollian ones,

$$\mathbb O^\epsilon_{(\Delta,J)}(z,\bar z) = \kappa^\epsilon_\Delta
\int_{-\infty}^{+\infty}\frac{du}{(u+i\epsilon\varepsilon)^\Delta}\,
\Phi^\epsilon_J(u,z,\bar z), \qquad
\kappa^\epsilon_\Delta = 4\pi(i\epsilon)^{\Delta+1}\Gamma(\Delta),$$

so every [[celestial-amplitude]] is a transform of a [[carrollian-amplitude]] and vice versa.
The two bottom-up formulations of [[flat-space-holography]] are one framework in two bases:
Fourier ($\omega\leftrightarrow u$, Carrollian) vs Mellin ($\omega\leftrightarrow\Delta$,
celestial) transforms of the same $\mathcal S$-matrix.

## Derivation sketch

Compose the defining transforms: the $u$-integral of the Carrollian (Fourier) representation
against $(u+i\epsilon\varepsilon)^{-\Delta}$ produces the Mellin transform in $\omega$.
Checks ([[2602.02644|Ruzziconi 2026]] §8): celestial 2-/3-/4-point functions with their
characteristic $\delta(\sum_i\Delta_i - \text{const})$ supports are recovered from the
$u_i\to0$ behavior; conformally soft theorems (Kac–Moody current $P = i\bar\partial S_0^+$,
celestial stress tensor $\bar T(\bar z)$) and the celestial OPE formula are rederived from
Carrollian stress-tensor Ward identities and Carrollian OPEs.

## Assumptions

Massless external states (massive states have no boundary primaries at $\mathscr I$ in
either formulation yet — see [[massive-states-in-carrollian-holography]]); the transform's
invertibility requires the principal-series contour for $\Delta$.

## Status

**Established** ([[2312.10138|Mason–Ruzziconi–Srikant 2023]],
[[2212.12553|Donnay–Fiorucci–Herfray–Ruzziconi 2022]]; reviewed in
[[2602.02644|Ruzziconi 2026]] §8).

## Implications

- The celestial "pathologies" (distributional correlators, continuous complex spectrum,
  non-associative OPEs) are images of natural Carrollian ultra-locality — arguments about
  which formulation is "the" dual dissolve.
- Celestial symmetry structures ($S$-algebra, [[lw-infinity-algebra]]) can be imported into
  the Carrollian frame and vice versa.
- Effectively merges the two research communities of [[flat-space-holography]].
