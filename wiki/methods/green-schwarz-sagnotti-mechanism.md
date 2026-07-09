---
type: method
title: Green-Schwarz-Sagnotti mechanism (6d)
aliases: [Green-Schwarz-Sagnotti mechanism, GSS mechanism, 6d anomaly factorization]
tags: [6d-supergravity, anomaly-cancellation, swampland]
prerequisites: [tensor-charge-lattice]
created: 2026-07-08
updated: 2026-07-08
---

## What it computes

How anomalies are cancelled in a 6d $\mathcal N=(1,0)$ supergravity. The one-loop anomaly
polynomial $I_8$ must **factorize** through the tensor multiplets' Green-Schwarz couplings,
which both determines the allowed gauge/matter spectrum and fixes the anomaly vectors
$b_0,b_i$ in the [[tensor-charge-lattice]]. It is the founding perturbative constraint of
the [[6d-supergravity-swampland|6d landscape]].

## Prerequisites

- The [[tensor-charge-lattice]] $\Gamma$ of signature $(1,T)$ with pairing $\Omega$.
- Group-theory data: the normalization constants $\lambda_i$ and the anomaly coefficients
  $A_{\mathbf r},B_{\mathbf r},C_{\mathbf r}$ of each representation.

## How it works

The anomaly polynomial factorizes as

$$I_8=\tfrac12\,\Omega_{\alpha\beta}\,X_4^\alpha X_4^\beta,\qquad
X_4^\alpha=-\tfrac12 b_0^\alpha\,\mathrm{tr}R^2+\tfrac12\sum_i\frac{b_i^\alpha}{\lambda_i}\,\mathrm{tr}F_i^2,$$

where $b_0$ is the gravitational anomaly vector and $b_i$ the vector for gauge factor
$\mathfrak g_i$ (unsubscripted $\mathrm{tr}$ in the defining representation). Matching
coefficients gives the **Green-Schwarz conditions**, which tie the matter spectrum to
lattice inner products:

$$H-V=273-29T,\qquad b_0\cdot b_0=9-T,$$
$$b_0\cdot b_i=\frac{\lambda_i}{6}\Big(\sum_{\mathbf r}n^i_{\mathbf r}A^i_{\mathbf r}-A^i_{\rm adj}\Big),\qquad
b_i\cdot b_i=\frac{\lambda_i^2}{3}\Big(\sum_{\mathbf r}n^i_{\mathbf r}C^i_{\mathbf r}-C^i_{\rm adj}\Big).$$

The normalization constants are $\lambda_{SU(N)}=1$, $\lambda_{SO(N)}=2$, $\lambda_{Sp(N)}=1$,
$\lambda_{G_2}=2$, $\lambda_{F_4}=6$, $\lambda_{E_6}=6$, $\lambda_{E_7}=12$, $\lambda_{E_8}=60$.
The anomaly sublattice $\mathfrak L=\mathrm{span}(b_0,b_i)$ then has integral Gram matrix
$\mathcal G_{IJ}=b_I\cdot b_J$ with the signature bound $n_+^{\mathfrak L}\le 1$,
$n_-^{\mathfrak L}\le T$ — the seed of the [[supergravity-block]] "one positive eigenvalue"
criterion.

## Regime of validity

6d $\mathcal N=(1,0)$ supergravity (perturbative gauge/gravitational/mixed anomalies). It is
*necessary* but not sufficient for UV completeness — the non-perturbative
[[h-string|$H$-string]] / tensionless-string constraints go beyond it. The main analysis of
[[2607.05496|Hamada-Jeon-Kim 2026]] omits Abelian gauge factors.

## Canonical applications

- Determining un-Higgsable gauge algebras on rigid curves ([[non-higgsable-cluster]]).
- Fixing $b_0,b_i$ and testing candidate tensor bases in the
  [[classification-non-higgsable-gravity-blocks|non-Higgsable gravity block classification]].
- Combined with the blowdown map $Q\to Q+(\mathcal C\cdot Q)\mathcal C$ to reduce a base to
  $\mathbb F_n$/$\mathbb P^2$.
