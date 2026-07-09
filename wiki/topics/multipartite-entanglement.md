---
type: topic
title: Multipartite entanglement
aliases: [GME, genuine multipartite entanglement, multipartite entanglement measures]
tags: [quantum-information, multipartite-entanglement, entanglement]
prerequisites: [entanglement-entropy]
created: 2026-07-07
updated: 2026-07-07
---

## Overview

How does one characterize the entanglement of a state shared among **many** parties, when the
information is genuinely spread across all of them rather than merely shared pairwise? A $q$-partite
pure state $|\psi\rangle\in\mathcal H_{A_1}\otimes\cdots\otimes\mathcal H_{A_q}$ is **separable**
if it factorizes across some nontrivial partition of the parties, and
[[genuine-multipartite-entanglement|genuinely multipartite entangled (GME)]] if it does not
factorize across *any* partition. The field builds quantities that detect and quantify the GME
content:

- **[[local-unitary-invariant|Local-unitary (LU) invariants]]** — functions unchanged by local
  basis changes $U_1\otimes\cdots\otimes U_q$; the only intrinsic entanglement data of a pure state.
- **[[entanglement-signal|Signals]]** — LU-invariants that *vanish* on separable (or
  layerwise-separable) states, so a nonzero value certifies GME.
- **GME measures** — signals promoted to positive, LOCC-monotone quantities (entanglement
  monotones), the resource-theoretic gold standard.

The unifying combinatorial backbone is the [[partition-lattice]] $\Pi_X$: separability types are
its elements, and [[mobius-inversion]] on it isolates the combinations that vanish on every
nontrivially separable state. This topic is the wiki's entry point into quantum information; it
connects to holography through [[multi-entropy]] and its use as a GME diagnostic of holographic
states.

## Historical development

- **Foundations (combinatorics).** Möbius inversion on the partition lattice — Rota (1964),
  Stanley — with the moments-to-cumulants reading (Speed 1983). LU-invariant enumeration for
  qubits/qudits: Rains (2000), Grassl–Rötteler–Beth (1998), Vrana, Szalay.
- **Multi-entropy program.** A permutation/edge-colored-graph formulation of
  [[local-unitary-invariant|multi-invariants]] and the resulting [[multi-entropy]] / Rényi
  multi-entropy (Gadde and collaborators, 2022–2025).
- **Holographic GME diagnostics.** "Genuine multi-entropy" $\mathrm{GM}^{(n)}$ (Iizuka–Nishida,
  Iizuka–Lin–Nishida 2025), the **$q$-information** and **residual information**
  (Balasubramanian–Kang–Murdia–Ross 2024), and correlation signals $\Delta_p^{(q)}$ from the
  multipartite entanglement of purification (Bao–Furuya–Naskar 2025) — each proposed independently.
- **Unification.** A general construction showing that (almost) all of these are Möbius vectors on
  the partition lattice, built from *compatible families* of lower-partite symmetric LU-invariants,
  with a matching no-go theorem for turning signals into measures~[[2603.07680|Gadde 2026]].
- **Application.** Signals used to read off the low-energy topological quantum field theory from a
  gapped ground-state wavefunction (Del Zotto–Gadde–Putrov 2026).

## Key concepts

- [[genuine-multipartite-entanglement]] — the target: states not separable across any partition;
  layer decomposition and layerwise separability.
- [[local-unitary-invariant]] — the raw material: LU-invariant functions, symmetric restriction /
  $\pi$-extension, and multiplicative permutation multi-invariants $\mathcal Z,\mathcal E$.
- [[partition-lattice]] — the bookkeeping poset; meet/join, Möbius function.
- [[entanglement-signal]] — signals, pre-signals, compatible families, and the Möbius-vector basis.
- [[multi-entropy]] — the multipartite generalization of entanglement entropy that seeds the most
  studied signals.

## Key results

- [[no-signal-is-gme-measure]] — no signal can be a GME measure; pre-signals are the natural
  resource-theoretic objects.
- [[q-information-odd-q-vanishing]] — the sum-of-Rényi signal ($q$-information) vanishes for odd $q$
  on pure states, motivating the reflected-entropy "residual information".

## Current status

The signal side is well understood: for a compatible family the additive-signal space is freely
spanned by Möbius vectors $M_\rho[f]$ ($\rho$ with no singleton block), and there is a unique
pre-signal $M_{\mathbf 1}[\tilde f]$ for a generic non-additive family. Turning these into bona
fide **GME measures** (positive and LOCC-monotone, ideally for mixed states) is open.

## Open questions

- [[pre-signals-to-gme-measures]] — can positive, LOCC-monotone pre-signals (hence GME measures),
  computable on mixed states via convex roof, be constructed?
- [[structural-characterization-compatibility]] — what is the full class of compatible LU-invariant
  families, structurally?
- Relation to the hypergraph/Sperner-state organization of multipartite entanglement
  (Ju–Sun–Zhao 2026).
