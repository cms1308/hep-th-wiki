---
type: method
title: Superconformal deformation of the holomorphic twist (VOA recovery)
aliases: [superconformal deformation, VOA from holomorphic twist, z^2 G-tilde deformation]
tags: [holomorphic-twist, vertex-operator-algebra, n2-scft, twisted-qft]
prerequisites: [holomorphic-twist, higher-super-virasoro-algebra, schur-superfield]
created: 2026-07-08
updated: 2026-07-08
---

## What it computes

It recovers the 2d [[scft-voa-correspondence|vertex operator algebra]] of a 4d $\mathcal N=2$
SCFT as a **deformation of the holomorphic twist**, and gives an explicit rule expressing the
2d VOA $\lambda$-brackets in terms of the 4d holomorphic
[[holomorphic-lambda-bracket|$\lambda$-brackets]]. This makes precise how the higher algebraic
structures of the holomorphic twist give rise to ordinary vertex-algebra structure.

## Prerequisites

- A holomorphically twisted $\mathcal N\geq2$ theory with its
  [[higher-super-virasoro-algebra|$\mathfrak{svir}(2|\mathcal N-1)$]] currents, in particular
  the extra generator $\widetilde{\mathbf G}$.
- The [[schur-superfield|Schur superfields]] $\mathbb O=\mathbf O+dz^2\Psi_{\mathbf O}$.

## How it works

1. **Deform.** Add $\int z^2\,\widetilde{\mathbf G}$ to the action. In the twist the differential
   *is* the BV/BRST operator $\{S_{\rm BV},-\}$, so deforming the action deforms the differential
   by $\{\int z^2\widetilde{\mathbf G},-\}$; since $z^2\widetilde{\mathbf G}$ is the Hamiltonian for
   $z^2\partial_\theta\sim z^2\iota_{\partial_2}$, the Dolbeault differential is replaced by
   $\mathbb Q=\bar\partial+\iota_{z^2\partial_2}$, whose fixed locus is the plane $z^2=0$: the 4d
   holomorphic theory **localizes** to a genuine 2d holomorphic theory. (Deforming instead by
   $\int\mathbf G_2$ — Hamiltonian for $\theta\partial_2\sim dz^2\partial_2$ — gives the THF
   differential $\bar\partial+dz^2\partial_2$, i.e. the holomorphic–topological twist.)
2. **Identify survivors.** The operators closed under $\mathbb Q$ are the Schur superfields; a
   spectral-sequence / Cartan-homotopy argument shows the 4d $S^3$ configuration integrals are
   cohomologous to 2d $S^1$ VOA integrals.
3. **Extract 2d brackets.** The 2d $\lambda$-bracket is a perturbative series in the 4d ones:
   $$\{\!\{\mathbb O_1{}_\lambda\mathbb O_2\}\!\}
   =\{\{\widetilde{\mathbf G}{}_{(0,0)}\mathbf O_1\}{}_{(\lambda,0)}\mathbf O_2\}
   +\sum_{n>0}\frac{(-\pi^2)^n}{n!}\,\partial_{\mu^2_1}\!\cdots\partial_{\mu^2_n}\{\widetilde{\mathbf G}\cdots\}.$$
4. **Read off dictionaries.** The stress tensor
   $\mathbb T=\mathbf G_1+dz^2(\mathbf S_1-\tfrac13\partial_1\mathbf R)$ gives $c_{2d}=-12c$; the
   currents $\mathbb J_a=\boldsymbol\mu_a+dz^2\mathbf J_a$ give level $k_{2d}=-\tfrac12 k_F$.

## Regime of validity

Any $\mathcal N\geq2$ theory in the holomorphic twist. Worked out fully for the free
hypermultiplet (giving the **symplectic boson VOA**); interacting examples (free vector
multiplet, conformal gauge theories) are in principle accessible by the same rule but not
computed there.

## Canonical applications

- Free hypermultiplet → symplectic bosons, with 2d stress tensor and affine currents at the
  Beem-et-al levels — ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]].
- Provides a holomorphic-twist derivation of the
  [[scft-voa-correspondence|SCFT/VOA correspondence]], complementing Saberi–Williams 2019.
