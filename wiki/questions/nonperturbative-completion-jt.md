---
type: question
title: Nonperturbative completion of JT gravity
aliases: [JT nonperturbative completion, JT instability, non-uniqueness of JT]
tags: [jt-gravity, matrix-models, nonperturbative, resurgence]
status: open
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[jt-gravity-matrix-integral-duality|JT/matrix duality]] holds order by order in the genus
expansion, but that series is asymptotic (factorially divergent). Defining JT gravity
nonperturbatively means choosing a convergent definition of the eigenvalue integral behind
$\rho_0(E)\propto\sinh(2\pi\sqrt{2\gamma E})$. Is there a canonical, stable such completion — and
can its "constituents" (the eigenvalues / the matrix itself) be recovered from bulk gravity?

## Why it matters

The nonperturbative sector is where the physics lives: the eigenvalue discreteness that produces the
[[spectral-form-factor|plateau]], and the D-brane (ZZ/FZZT) effects that fix the
[[large-genus-weil-petersson-asymptotics|large-genus volume growth]]. A well-defined completion is
also what a genuine theory of quantum gravity should have — so the ambiguity is a statement about
how much the gravitational path integral alone determines.

## Main attempts

- **Complex eigenvalue contour** [[1903.11115|(Saad–Shenker–Stanford)]]: the effective potential
  $V_{\rm eff}(E)=2e^{S_0}\int_0^{-E}dx\,y(\sqrt x)$ rises to a local maximum at $E=-\tfrac14$ — a
  one-eigenvalue instanton / ZZ brane at $z_{\rm ZZ}=\tfrac12$ — then turns increasingly negative,
  so eigenvalues can leak out. Defining the integral on a complex contour gives a finite but
  **non-unique, metastable** answer with imaginary instanton coefficients.
- **Alternative ensembles / deformed potentials**: modifying the potential or the ensemble (or using
  the airy/topological-gravity truncation) yields different completions with the same perturbative
  expansion.
- **Stable UV completions** of related models (e.g. the Airy / Kontsevich model is well defined; some
  variants of the $\hat p$-deformed density are bounded), suggesting the instability is special to
  the bosonic orientable $\sinh$ curve.

## Current status

**Open.** The genus expansion is unambiguous; the nonperturbative completion is not. The bosonic
orientable JT model is metastable, so it has no unique nonperturbative definition from the matrix
side alone, and no bulk-gravity derivation of the eigenvalue constituents is known. Whether a
preferred, stable completion exists — and what selects it — is unresolved.
