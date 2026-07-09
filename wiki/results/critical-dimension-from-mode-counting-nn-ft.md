---
type: result
title: Critical dimension D=26 from mode counting
aliases: ["critical dimension from NN-FT", "D=26 from mode counting", "Weyl anomaly from parameter counting"]
tags: [machine-learning, neural-networks, nn-ft, string-theory, weyl-anomaly, critical-dimension]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

The critical dimension of the bosonic string, $D=26$, follows from demanding Weyl invariance of the
[[string-amplitudes-from-neural-networks|bosonic-string NN-FT]] on $S^2$ — as the zeta-regularized
mismatch between how the bosonic and Grassmann parameter measures respond to a Weyl flow. Established
in Ferko et al. 2026, presented in [[2607.02905|Halverson 2026]]. It is a special case of the
[[parameter-space-ward-identities|parameter-space anomaly formalism]].

## Derivation sketch

Work on the round $S^2$. The free boson is a harmonic random-feature field,
$X^\mu(\hat n)=\sum_{\ell m}a^\mu_{\ell m}Y_{\ell m}(\hat n)$ with $\sigma_\ell^2=2\pi\alpha'/\ell(\ell+1)$;
the $bc$ ghosts expand in spin-weighted spherical harmonics ${}_sY_{\ell m}$ (which exist only for
$\ell\ge|s|$): $b\equiv b_{zz}$ (spin $+2$) starts at $\ell=2$, $c\equiv c^z$ (spin $-1$) at $\ell=1$,
with a Grassmann pair density on the paired modes. The three unpaired $\ell=1$ ghost modes are the
conformal Killing vectors; the antiholomorphic $\bar b,\bar c$ are an independent copy (hence a factor
of two in the ghost count).

A constant Weyl rescaling $g\to e^{2\epsilon}g$ scales the Laplacian spectrum and maps the NN-FT to
one on a different background. Absorbing it into parameters gives linear flows
$\xi^{a^\mu_{\ell m}}=-a^\mu_{\ell m}$, $\xi^{\beta_{\ell m}}=+\beta_{\ell m}$,
$\xi^{\chi_{\ell m}}=-2\chi_{\ell m}$. In the [[parameter-space-ward-identities|breaking function]]
$B=\text{score}+\text{Jacobian}$, the **score contributions cancel sector-by-sector** against the
Weyl shift of the spectrum, leaving **only the Jacobian** — a pure mode count:
$$B^{(X)}_{\rm Jac}=-D\Big[\sum_{\ell=1}^L(2\ell+1)+1\Big],\qquad B^{(bc)}_{\rm Jac}=2\sum_{\ell=2}^L(2\ell+1)+12.$$
The counts diverge as $L\to\infty$; zeta-regularizing with $\zeta_X(0)=-2/3$, $\zeta_{bc}(0)=-5/3$,
$$B^{\rm reg}_{\rm anom}=-D[\zeta_X(0)+1]+2\zeta_{bc}(0)+12=-\frac D3-\frac{10}3+12=-\frac13(D-26).$$
Demanding Weyl invariance of the ensemble, $B^{\rm reg}_{\rm anom}=0$, forces $D=26$.

## Assumptions

- Round $S^2$ (genus-zero) worldsheet, whose Laplacian spectrum is the clean spherical-harmonic tower.
- Zeta-function regularization of the divergent mode counts.
- Grassmann-valued networks for the ghost sector (Berezin measure), whose measure responds to the
  flow oppositely to the bosonic measure — the source of the mismatch.

## Status

Established. Reproduces the standard $D=26$, usually obtained from a normal-ordering constant, the
Polyakov measure, or $c_{\rm matter}+c_{\rm ghost}=0$; here it is the regularized bosonic-vs-Grassmann
measure mismatch under a parameter-space flow.

## Implications

- Turns the Weyl anomaly into a *counting* statement about network modes, giving the
  [[parameter-space-ward-identities|score/Jacobian formalism]] a flagship string-theory application.
- Ties the [[string-amplitudes-from-neural-networks|bosonic-string NN-FT]] together with its own
  consistency condition, entirely inside parameter space.

## References

- [[2607.02905|Halverson 2026]] §Day 2 (The Weyl anomaly and Critical Dimension); Ferko et al. 2026.
