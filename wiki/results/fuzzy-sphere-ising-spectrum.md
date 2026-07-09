---
type: result
title: Fuzzy-sphere 3D Ising state-operator correspondence
aliases: ["fuzzy sphere Ising spectrum", "3D Ising primaries from the fuzzy sphere"]
tags: [conformal-field-theory, 3d-ising, fuzzy-sphere, state-operator-correspondence]
status: established
created: 2026-07-07
updated: 2026-07-07
---

## Statement

A microscopic $2+1$D quantum Ising model on the [[fuzzy-sphere|fuzzy sphere]], tuned to its critical point, reproduces the [[state-operator-correspondence]] of the [[3d-ising-cft|3D Ising CFT]]: after fixing a single non-universal scale by $\Delta_T\equiv3$, the low-lying energy spectrum from [[exact-diagonalization|exact diagonalization]] of $N=8$–$16$ spins organizes into complete 3D [[conformal-multiplet|conformal multiplets]], yielding
- **13 parity-even primaries**, with scaling dimensions matching the numerical [[conformal-bootstrap]] to $<1.6\%$ (e.g. $\Delta_\sigma=0.524$ vs. CB $0.518$; $\Delta_\epsilon=1.414$ vs. CB $1.413$; $\epsilon'$ at $3.838$, $\sigma'$ at $5.303$, $T'_{\mu\nu}$ at $5.583$), and
- **2 previously unknown parity-odd primaries**: scalars $\epsilon^{P-}$ at $\Delta\approx10.01$ and $\sigma^{P-}$ at $\Delta\approx11.19$.

No primary appears in the $(\mathbb Z_2{=}{+},P{=}{+},\text{odd }\ell)$ sector below $\Delta=7$, so the [[virial-current]] candidate is pushed far above $\Delta=2$ — evidence that the transition is genuinely conformal, not merely scale-invariant.

## Derivation sketch

1. Build the fuzzy-sphere Ising Hamiltonian by [[lowest-landau-level-projection]]: spinful electrons in the LLL of a monopole sphere with $SO(3)$-invariant density–density interactions plus a transverse field, at half filling ($N=2s+1$ orbitals = spins).
2. Locate the critical point ($V_0=4.75$, $h_c\approx3.16$ with $V_1=1$) by finite-size scaling of the order parameter, $\langle M^2\rangle\sim N^{2-\Delta_\sigma}$, whose rescaled curves cross at $h_c$.
3. Diagonalize (ED for $N\le16$, DMRG for larger $N$), labeling states by exact $(\mathbb Z_2,P,\ell)$.
4. Calibrate energies via $\delta E_n=(v/R)\Delta_n$ with the stress tensor fixed at $\Delta_T=3$.
5. Decompose the spectrum multiplet by multiplet — primary, then its enumerated $\partial/\square/\varepsilon$ descendants — matching the entire low-lying tower with no missing or extra states.

## Assumptions

- The fuzzy-sphere Ising critical point lies in the 3D Ising universality class (supported by the order-parameter scaling and the matched spectrum).
- The single non-universal factor $v/R$ is correctly fixed by identifying the lowest $(\mathbb Z_2{=}{+},P{=}{+},\ell{=}2)$ state as the stress tensor at $\Delta_T=3$.
- Finite-size ($N\le16$–$36$) dimensions approximate the $N\to\infty$ CFT; residual finite-size drift sets the quoted accuracy.

## Status

**Established.** The parity-even dimensions agree with the independently-known [[conformal-bootstrap]] spectrum to sub-percent accuracy, which both validates the method and cross-checks the bootstrap. The two parity-odd primaries are new predictions awaiting independent (e.g. spinning-correlator bootstrap) confirmation.

## Implications

- First direct demonstration of the emergent conformal symmetry of the 3D Ising transition (see [[emergent-conformal-symmetry-3d-ising]]), a 1970 Polyakov conjecture.
- Establishes [[fuzzy-sphere-regularization]] as a general microscopic route to 3D CFT data — spectra, and later OPE coefficients and correlators — competitive with the bootstrap and Monte Carlo.
- Delivers genuinely new spectral data (the parity-odd primaries) beyond what the bootstrap had isolated.

Source: [[2210.13482|Zhu-Han-Huffman-Hofmann-He 2022]].
