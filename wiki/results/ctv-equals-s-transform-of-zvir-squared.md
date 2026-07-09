---
type: result
title: CTV = modular S-transform of |Z_Vir|²
aliases: [CTV main identity, chain-mail identity for Virasoro, Fourier transform of |Z_Vir|^2]
tags: [tqft, 3d-gravity, virasoro-tqft, crossing-kernel]
status: conjectured
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[conformal-turaev-viro-theory|CTV]] partition function on a closed 3-manifold $M_E$ with
an embedded framed trivalent graph $\Gamma(\mathsf P')$ equals the modular $S$-transform, on
every external edge, of the squared [[virasoro-tqft|Virasoro TQFT]] amplitude:
$$Z_{\rm CTV}(M_E,\Gamma(\mathsf P'))
=\int_{\mathbb R_+^{n}} d\mathsf P\,\Big(\prod_{i=1}^{n} S_{P_i'P_i}\Big)
\big|Z_{\rm Vir}(M_E,\Gamma(\mathsf P))\big|^2,\qquad
S_{P'P}=2\sqrt2\cos(4\pi P'P).$$
It is the Virasoro (continuous, irrational) analog of Barrett's discrete
$Z_{\rm TV}(M,\Gamma)$-from-$|\langle\Gamma\rangle|^2$ result.

Two corollaries are new closed-form $S$-transforms of squared
[[virasoro-6j-symbol|Virasoro crossing kernels]]:

- **Squared $6j$ is self-dual** (tetrahedron graph in $S^3$, two tetrahedra):
$$\begin{Bmatrix}P_4'&P_5'&P_6'\\ P_1'&P_2'&P_3'\end{Bmatrix}^{2}
=\int_0^\infty\Big(\prod_{i=1}^{6}dP_i\,S_{P_i'P_i}\Big)
\begin{Bmatrix}P_1&P_2&P_3\\ P_4&P_5&P_6\end{Bmatrix}^{2}.$$
- **$S$-transform of the squared modular $S$-matrix** (knotted handcuff graph, one
  tetrahedron):
$$\begin{Bmatrix}P_3'&P_3'&P_1'\\ P_3'&P_3'&P_2'\end{Bmatrix}
=\int_0^\infty\Big(\prod_{i=1}^{3}dP_i\,S_{P_i'P_i}\Big)\,
\big|\widehat{\mathbb S}_{P_1P_2}[P_3]\big|^{2}.$$

## Derivation sketch

Adapt Roberts' [[chain-mail-formalism|chain-mail formalism]] to Virasoro. Build the chain-mail
link $\Gamma_{CH}$ from $\Gamma$ (edges/crossings/vertices $\to$ $\Omega$-loops integrated with
the [[cardy-density-of-states|Cardy measure]]; perimeter loop deleted to drop the divergent
total-quantum-dimension factor). Evaluate $\langle\Gamma_{CH}\rangle=Z_{\rm Vir}(M_E,\Gamma_{CH})$
two ways: collapsing each tetrahedron via the vertex-join identity gives the product of
$6j$-symbols, i.e. $Z_{\rm CTV}$; expanding the external $\Omega$-loops via the
[[virasoro-modular-s-matrix|modular $S$-matrix]] $\Omega$-line trick gives $\int d\mathsf P
\prod_i S_{P_i'P_i}|Z_{\rm Vir}|^2$. A phase-free reading through the (Virasoro-extended)
shadow formalism matches the two. Both example corollaries are checked by computing each side
independently (triangulation vs. Fourier transform of $|Z_{\rm Vir}|^2$).

## Assumptions

- Restricted to **large triangulations** ($H_2(M_E-V_{\rm int})=0$) and graphs $\Gamma$ that
  are finite in Virasoro TQFT; then $Z_{\rm CTV}$ is finite and triangulation-independent.
- Invariance under 2-3/3-2 Pachner moves follows from the pentagon identity; 1-4 moves are
  excluded (interior vertices give divergent contractible $\Omega$-loops).

## Status

Established by explicit chain-mail derivation and confirmed on worked examples (tetrahedron
and knotted-handcuff graphs). The accompanying **finiteness / triangulation-independence for
all large triangulations** is stated as a conjecture, supported by examples, together with the
conjecture that a large triangulation exists whenever $M=M_E-N(\Gamma)$ is hyperbolic.

## Implications

- Turns squared Virasoro crossing kernels into computable modular-$S$ transforms — new CFT
  identities for the $6j$-symbol and modular $S$-matrix.
- Provides the topological foundation for computing the exact AdS$_3$ pure-gravity path
  integral by triangulation: $Z_{\rm CTV}(M_E,\Gamma(\mathsf P))$ is identified with the
  gravitational path integral at fixed dihedral angles $\psi_i=2\pi i b P_i$.

## References

- [[2507.11652|Hartman 2025]] (main identity eq. 1.1/4.1; corollaries eqs. 4.7, 4.16).
