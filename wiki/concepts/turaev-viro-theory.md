---
type: concept
title: Turaev-Viro theory
aliases: [Turaev-Viro invariant, TV theory, TV state sum]
tags: [tqft, 3-manifolds, quantum-invariants, virasoro-tqft]
prerequisites: []
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A state-sum construction of a 3-manifold invariant from a modular (or spherical fusion)
category. Triangulate the 3-manifold with tetrahedra, label edges by simple objects (spins)
$j$, assign each tetrahedron a quantum $6j$-symbol, and sum over internal labels weighted by
quantum dimensions:
$$Z_{\rm TV}(M) = \mathcal D^{-2V}\sum_{\{j\}}\prod_{\text{edges}} d_{j}\prod_{\text{tetrahedra}}
\begin{Bmatrix} j_1 & j_2 & j_3\\ j_4 & j_5 & j_6\end{Bmatrix},$$
with $d_j$ the quantum dimension, $\mathcal D$ the total quantum dimension, and $V$ the number
of vertices. The result is independent of the triangulation because the $6j$-symbols satisfy
the pentagon identity, which is exactly the invariance under the 2-3 and 1-4 Pachner moves.

## Motivation

It gives a manifestly combinatorial, triangulation-based 3-manifold invariant, dual to the
surgery-based Reshetikhin-Turaev/Chern-Simons construction. The two are related by
$$Z_{\rm TV}(M) = \big|Z_{\rm RT}(M)\big|^2,$$
established for spin networks by the [[chain-mail-formalism|chain-mail formalism]].

## Key formulas

- Roberts' theorem (closed manifold): $Z_{\rm TV}(M) = |Z_{\rm RT}(M)|^2$.
- Extension to a manifold with an embedded graph $\Gamma$ (spin-network invariant
  $\langle\Gamma\rangle$): $Z_{\rm TV}(M,\Gamma) = |\langle\Gamma\rangle|^2$ up to a
  modular $S$-transform on the external edges (Barrett-García-Islas-Martins), the discrete
  analog of the [[ctv-equals-s-transform-of-zvir-squared|CTV main identity]].
- Self-duality of squared spin-network invariants under the $S$-transform (Barrett).

## Relations

- Continuous / irrational generalization: [[conformal-turaev-viro-theory]], where the finite
  fusion category is replaced by the Virasoro modular data (continuous weights $P$,
  [[virasoro-6j-symbol|Virasoro $6j$-symbols]], and the [[cardy-density-of-states|Cardy density]] in place of quantum dimensions).
- Surgery dual: [[virasoro-tqft|Virasoro TQFT]] plays the role of Reshetikhin-Turaev in the
  Virasoro setting.
- Shadow-world reformulation: phase-free evaluation via shaded planar regions (Turaev-Viro
  shadows), extended to the Virasoro case in [[2507.11652|Hartman 2025]].

## Where it appears

- Original construction and shadow world: Turaev-Viro 1992, 1994.
- Chain-mail proof $Z_{\rm TV}=|Z_{\rm RT}|^2$: Roberts 1995.
- External edges / squared spin-network self-duality: Barrett-García-Islas-Martins 2004,
  Barrett 2002 — the discrete templates that [[2507.11652|Hartman 2025]] lifts to Virasoro.
