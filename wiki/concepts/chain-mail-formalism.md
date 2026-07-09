---
type: concept
title: Chain-mail formalism
aliases: [chain mail, chain-mail link, Roberts chain mail, Virasoro chain mail]
tags: [tqft, 3-manifolds, virasoro-tqft, quantum-invariants]
prerequisites: [turaev-viro-theory]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A method (Roberts 1995) that proves the surgery invariant and the state-sum invariant of a
3-manifold agree, by rewriting a triangulation as a single link diagram. Each edge, crossing,
and vertex of the graph $\Gamma$ is replaced by an $\Omega$-loop (an unknot carrying the
vacuum/identity projector $\Omega=\sum_j d_j\,\ell_j$, continuous version
$\Omega=\int dP\,\rho_0(P)$), producing the **chain-mail link** $\Gamma_{CH}$. Evaluating the
same link two ways gives, on one side, the Reshetikhin-Turaev amplitude squared and, on the
other, the [[turaev-viro-theory|Turaev-Viro]] state sum:
$$\langle \Gamma_{CH}\rangle \;=\; Z_{\rm TV}(M)\;=\;|Z_{\rm RT}(M)|^2.$$

## Motivation

An $\Omega$-loop linked with a strand projects that strand onto the vacuum and implements
Dehn surgery / a handle attachment. Threading the whole triangulation with $\Omega$-loops
therefore encodes the surgery presentation and the state sum in one diagram, so evaluating it
by two different reduction orders equates the two invariants.

## How it works (Virasoro adaptation)

[[2507.11652|Hartman 2025]] adapts this to the continuous Virasoro spectrum to prove the
[[ctv-equals-s-transform-of-zvir-squared|CTV main identity]]:

- $\Omega$-loops are integrated with the [[cardy-density-of-states|Cardy measure]]
  $\int dP\,\rho_0(P)$ instead of summing $\sum_j d_j$.
- The **perimeter loop is deleted** (a departure from the discrete Barrett-García-Islas-Martins
  prescription): this removes the divergent total-quantum-dimension factor $\mathcal D$ that
  has no finite Virasoro analog.
- A **marked Heegaard-diagram** picture gives $\Gamma_{CH}$ a geometric definition
  (handlebody = thickened dual complex; internal/external edges become OPE-channel cycles).
- The **vertex-join identity** collapses each tetrahedron of the diagram to a single
  [[virasoro-6j-symbol|Virasoro $6j$-symbol]]; a phase-free reading via the (extended)
  shadow formalism identifies the product of $6j$'s with $|Z_{\rm Vir}|^2$.

## Relations

- Proves [[turaev-viro-theory]] $=|Z_{\rm RT}|^2$ (discrete) and its Virasoro lift, the
  [[ctv-equals-s-transform-of-zvir-squared|CTV = $S$-transform of $|Z_{\rm Vir}|^2$]] identity.
- Uses the [[virasoro-modular-s-matrix|modular $S$-matrix]] $\Omega$-line trick to implement
  the edge-by-edge Fourier transform.

## Where it appears

- Original: Roberts 1995; external edges: Barrett-García-Islas-Martins 2004.
- Virasoro adaptation: [[2507.11652|Hartman 2025]].
