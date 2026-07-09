---
type: method
title: Holomorphic a-maximization
aliases: [holomorphic a-maximization, a-maximization in the holomorphic twist, spectral flow a-extremization]
tags: [holomorphic-twist, a-maximization, r-symmetry, anomaly, central-charge]
prerequisites: [holomorphic-twist, two-virasoro-algebra, a-maximization]
created: 2026-07-08
updated: 2026-07-08
---

## What it computes

The exact superconformal $R$-symmetry — hence the IR central charges $a$ and $c$ — of a
holomorphically twisted $\mathcal N=1$ theory, by adapting the standard
[[a-maximization]] algorithm (Intriligator–Wecht) to the twist. In the twist, choosing the
correct $R$-symmetry is choosing the correct **twisting homomorphism**, and the extremization
principle is realized algebraically through the higher currents.

## Prerequisites

- A twisted theory with its [[two-virasoro-algebra|2-Virasoro]] stress-tensor superfields
  $\mathbf S_i$ and flavor currents $\mathbf J_f$.
- Anomaly data as ternary [[holomorphic-lambda-bracket|$\lambda$-brackets]] — see
  [[ac-anomalies-as-central-extensions]].

## How it works

1. **Spectral flow.** Mixing the $R$-current with flavor currents,
   $\mathbf S^\epsilon_i=\mathbf S_i+\epsilon^f\partial_i\mathbf J_f$, defines a one-parameter
   family of candidate stress tensors — the twist analogue of trial $R$-symmetries $R_t$.
2. **Uniqueness of the tensor structure.** The superconformal stress tensor is the one whose
   $\langle SSJ\rangle$ correlator has a **single** invariant tensor structure (Osborn),
   $$\{\!\{\mathbf S^{\rm sc}_i\,\mathbf S^{\rm sc}_j\,\mathbf J_f\}\!\}
   \propto k_f\,[\lambda_1\lambda_2]\big(\lambda_{1i}\lambda_{2j}-3\lambda_{1j}\lambda_{2i}\big).$$
3. **Extremization condition.** Requiring this single structure forces
   $$k_f=9\,k_{RRf},$$
   which is exactly the $a$-extremization condition of the untwisted theory.
4. **Maximum, not just extremum.** Unitarity of the parent SCFT gives $k_{Rfg}<0$, selecting the
   maximum; the extremal central charges are read off as
   $c^{\rm hol}=-\tfrac{k_{RRR}}{48}$, $a^{\rm hol}=\tfrac{k_R}{24}$.

## Regime of validity

Holomorphically twisted $\mathcal N=1$ SCFTs (and $\mathcal N\geq1$ theories treated as such).
The construction is **not yet fully intrinsic**: the single tensor structure and the unitarity
input are imported from the untwisted physical theory — see
[[intrinsic-holomorphic-a-maximization]].

## Canonical applications

- Extracting $a,c$ of a twisted theory directly from its higher-current brackets
  ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]].
- A sharper diagnostic of IR (super)symmetry enhancement along RG flows than the index alone,
  earmarked for twisted Argyres–Douglas theories.
