---
type: topic
title: Virasoro TQFT and 3d gravity
aliases: [Virasoro TQFT, VTQFT, 3d gravity as TQFT, pure AdS3 gravity path integral]
tags: [3d-gravity, virasoro-tqft, tqft, conformal-field-theory, holography]
prerequisites: [anti-de-sitter-space]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

Pure three-dimensional gravity with a negative cosmological constant has no local degrees of
freedom, so on a fixed spacetime topology its path integral is a topological object. **Virasoro
TQFT** (VTQFT) makes this precise: it is a topological quantum field theory whose states are
non-degenerate Virasoro conformal blocks and whose amplitudes $Z_{\rm Vir}(M_E,\Gamma(\mathsf
P))$ are built from a diagrammatic calculus of framed trivalent graphs $\Gamma$ carrying
continuous conformal weights $P$. The gravitational partition function on a hyperbolic
3-manifold is $|Z_{\rm Vir}|^2$ (holomorphic $\times$ antiholomorphic). This topic collects the
machinery that turns that statement into concrete computations — and, via
[[conformal-turaev-viro-theory|Conformal Turaev-Viro theory]], into an actual triangulated
path integral.

The Virasoro modular data are the **irrational / continuous** analog of a rational modular
tensor category: the [[cardy-density-of-states|Cardy density]] $\rho_0(P)$ replaces quantum
dimensions, the [[virasoro-6j-symbol|Virasoro $6j$-symbol]] replaces the fusion $6j$, and the
[[virasoro-modular-s-matrix|modular $S$-matrix]] $S_{P'P}=2\sqrt2\cos(4\pi P'P)$ replaces the
finite $S$-matrix.

## Historical development

- **$SL(2,\mathbb R)\times SL(2,\mathbb R)$ Chern-Simons.** 3d gravity as a gauge theory
  (Achúcarro-Townsend 1986, Witten 1988), with subtleties about the correct contour and
  functional measure emphasized later (Witten 2007).
- **Teichmüller-space quantization.** Virasoro conformal blocks as states of a TQFT: Verlinde
  1989; the modular kernels and their integral representations from quantizing Teichmüller
  space (Teschner and collaborators, 2001-2014).
- **Rigorous Teichmüller TQFT from triangulations.** Andersen-Kashaev (2011, 2013); a
  Turaev-Viro-type dual (Kashaev 2012) — the discrete-geometry ancestor of CTV.
- **Virasoro TQFT as a working calculus.** A self-contained diagrammatic framework for
  $|Z_{\rm Vir}|^2$: Collier-Eberhardt-Mühlmann-Zhang 2023, 2024; further identities
  (irrational Verlinde formula) Post-Tsiares 2024.
- **Conformal Turaev-Viro theory.** [[2507.11652|Hartman 2025]] defines the
  triangulation-based dual of VTQFT and proves
  [[ctv-equals-s-transform-of-zvir-squared|$Z_{\rm CTV}$ = modular $S$-transform of $|Z_{\rm Vir}|^2$]], laying the topological foundation for the exact AdS$_3$ path integral.

## Key concepts

- [[conformal-turaev-viro-theory]] — the triangulation-based state sum dual to VTQFT.
- [[turaev-viro-theory]] — the discrete predecessor (finite fusion categories).
- [[virasoro-6j-symbol]] — tetrahedron weight / four-point crossing kernel.
- [[cardy-density-of-states]] — $\rho_0(P)$, the internal-edge measure.
- [[virasoro-modular-s-matrix]] — the $S$-transform / Fourier kernel.
- [[chain-mail-formalism]] — the link-diagram method proving the state-sum/surgery equivalence.

## Key results

- [[ctv-equals-s-transform-of-zvir-squared]] — CTV partition function = modular $S$-transform
  of $|Z_{\rm Vir}|^2$; new $S$-transforms of the squared $6j$-symbol and squared modular
  $S$-matrix.

## Current status

The VTQFT calculus is established and the CTV dual is defined, with the central identity
proved by chain mail and checked on examples. Whether $Z_{\rm CTV}$ is finite and
triangulation-independent for *all* large triangulations is conjectural (supported by
examples), as is the claim that a large triangulation exists whenever the complement
$M=M_E-N(\Gamma)$ is hyperbolic. The gravitational application — computing exact AdS$_3$ path
integrals from triangulated hyperbolic geometries — is developed in companion work.

## Open questions

- Prove the [[conformal-turaev-viro-theory|large-triangulation]] finiteness /
  triangulation-independence conjecture, and characterize which $(M_E,\Gamma)$ admit a
  well-defined CTV partition function beyond $S^3$.
- Establish the expected equivalence with Kashaev's Turaev-Viro-type dual of Teichmüller
  TQFT (ideal vs. ordinary tetrahedra).
- Clarify the relation to other Virasoro-$6j$ state-sum constructions (stated to be
  inequivalent).
