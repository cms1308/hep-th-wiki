---
type: concept
title: Holomorphic λ-brackets (higher secondary products)
aliases: [lambda-bracket, holomorphic lambda-bracket, secondary product, higher secondary operation]
tags: [holomorphic-twist, l-infinity, ope, dolbeault, configuration-space]
prerequisites: [holomorphic-twist, semi-chiral-superfield]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

**$\lambda$-brackets** are generating functions for the higher modes of the currents of a
[[holomorphic-twist|holomorphically twisted]] theory — the $L_\infty$ analogue of the
$\lambda$-bracket of a 2d Lie conformal algebra. They are the **secondary products** that access
the (singular, physical) OPE data hidden by Hartogs' lemma: while the OPE of $\mathbf Q$-closed
operators is non-singular, singularities reappear in multi-operator configurations probed by
integrating descendants over compact cycles in configuration space.

The $(n{+}1)$-ary bracket of semi-chiral superfields is
$$\{\mathbf O_1{}_{\lambda_1}\cdots{}_{\lambda_n}\mathbf O_{n+1}\}
=\int_{\mathrm{Conf}^0_{n+1}}\prod_{k}\frac{d^2z_k}{(2\pi i)^2}\,
e^{\lambda_k\cdot z_k}\,\mathbf Q\!\left[\mathbf O_1\cdots\mathbf O_{n+1}\right],$$
the binary case reducing to an $S^3$ integral of $\mathbf O_1$ around $\mathbf O_2$ weighted by a
Dolbeault representative $\rho(z)\in\Omega^{0,\bullet}(\mathbb C^2\setminus\{0\})$. The class of
the result depends only on $[\rho]\in H^{0,\bullet}(\mathbb C^2\setminus\{0\})$: it is
$\mathbf Q$-exact when $\rho=\bar\partial\tilde\rho$.

## Motivation

In one complex dimension singular OPE data sits in the poles of meromorphic functions. In two
complex dimensions Hartogs' lemma forbids isolated singularities of holomorphic functions, so
the data migrates into higher Dolbeault cohomology: $H^{0,\bullet}(\mathbb C^2\setminus\{0\})$ is
concentrated in degrees $0$ and $1$. The degree-1 (Bochner–Martinelli) classes are exactly the
"negative modes" that make the brackets a **derived**, homotopy-Lie structure rather than an
ordinary Lie algebra — this is why anomalies show up as ternary brackets.

## Key formulas

- Basis of Dolbeault representatives:
  $\rho_{m,n}=(z^1)^m(z^2)^n\in\Omega^{0,0}$ for $m,n\geq0$ (positive/singular modes), and
  $\rho_{m,n}=\partial_{z^1}^{-m-1}\partial_{z^2}^{-n-1}\omega_{\rm BM}\in\Omega^{0,1}$ for
  $m,n<0$ (negative/regularized modes), with the Bochner–Martinelli kernel
  $\omega_{\rm BM}=\frac{1}{(2\pi i)^2}\frac{\bar z^1 d\bar z^2-\bar z^2 d\bar z^1}{|z|^4}$.
- 2-Virasoro binary bracket:
  $\{\mathbf S_i{}_\lambda\mathbf S_j\}=\partial_i\mathbf S_j+\lambda_i\mathbf S_j+\lambda_j\mathbf S_i$.
- Anomalies are **ternary** brackets, e.g.
  $\{\!\{\mathbf S_i\,\mathbf S_j\,\mathbf S_k\}\!\}=16(a-c)\mathcal I^{\rm vec}_{ijk}+\tfrac43(3c-2a)\mathcal I^{\mathcal N=4}_{ijk}$.

## Relations

- The organizing algebra of [[two-virasoro-algebra]], [[higher-kac-moody-algebra]] and
  [[higher-super-virasoro-algebra]]; the 4d brackets reduce to 2d VOA $\lambda$-brackets under
  the [[superconformal-deformation-to-voa|superconformal deformation]].
- Perturbatively computed from 2-Laman graphs and Wick contractions (Budzik–Gaiotto et al.;
  Gaiotto–Kulp–Wu 2024).

## Where it appears

- Central computational tool of ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]].
