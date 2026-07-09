---
type: result
title: Two-point function of deformed-CFT physical operators
aliases: [TTbar two-point function, JTbar two-point function, shifted-weight correlator]
tags: [ttbar, jtbar, correlators, two-point-function, resurgence, 2d-cft]
status: established
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The momentum-space two-point function of a [[physical-operator-deformed-cft|physical operator]]
in a [[ttbar-deformation|$T\bar T$]]- or [[jt-bar-deformation|$J\bar T$]]-deformed CFT keeps the
CFT power-law form but with a **momentum-dependent effective weight** $h_\lambda$:
$$\langle\mathcal O_{h,\bar h}(p,\bar p)\,\mathcal O_{h,\bar h}(-p,-\bar p)\rangle\sim
\frac{\pi\,\Gamma(1-2h_\lambda)}{\Gamma(2h_\lambda)}\Big(\tfrac{|p|}{2}\Big)^{4h_\lambda-2}.$$
For $T\bar T$: $\ h_\lambda=h+\dfrac{\lambda}{\pi}\,p\bar p$. For $J\bar T$ (chiral charge $q$,
$U(1)$ level $k$): $\ h_\lambda=h-\dfrac{i\lambda q\bar p}{2\pi}-\dfrac{\lambda^2 k\,\bar p^2}{8\pi^2}$.
The $T\bar T$ result matches both the worldsheet [[tst-holography|TsT/$T\bar T$]] computation
(Cui–Du–Song 2023) and the field-theory large-momentum computation (Aharony–Barel 2023), and
satisfies Cardy's Callan–Symanzik equation; the $J\bar T$ result matches the TsT/$J\bar T$ string
prediction.

## Derivation sketch

The physical operator is written as a Wilson-line-like dressing of a
[[dressed-operator-deformed-cft|dressed operator]]; its correlator is expanded order by order in
$\lambda$ using undeformed CFT (or Virasoro–Kac–Moody) Ward identities with point-splitting, then
Fourier-transformed. Resumming the **most UV-sensitive (leading-log) terms** to all orders in
$\lambda$ gives the shifted-weight form above; the leading-UV sum has a star-product-like
structure. See [[hamiltonian-flow-deformed-cft]].

## Assumptions

Plane geometry; the classical operator construction lifted to the quantum level with an assumed
normal ordering; only the leading-log tower resummed (subleading logs are dropped, so momentum-
and position-space results are not related by a plain Fourier transform).

## Status

Established at the level of the leading-log resummation, with independent cross-checks against
two string/field-theory computations for $T\bar T$ and against the TsT string for $J\bar T$. The
full (subleading) correlator and a rigorous quantum operator definition remain open
([[quantum-operators-deformed-cft]]).

## Implications

For $J\bar T$ the position-space correlator carries a genuinely **nonperturbative** structure:
the leading-log series is factorially divergent and Borel resummation reveals an instanton term
$\propto e^{-1/4K}$ (with $K=-\tfrac{\lambda^2 k}{4\pi^2}\log|x|^2/(\bar x-\tfrac{\lambda q}{\pi}\log|x|^2)^2$),
setting an effective UV cutoff $\sim\lambda\sqrt{k}$. In the UV the left conformal power law
survives while the right sector softens to logarithmic — a divergence milder than the CFT but
stronger than $T\bar T$.

- [[2507.08588|Chen–Du–Liu–Song 2025]] — the $T\bar T$ two-point function.
- [[2511.10557|Chen–Du–Song 2025]] — the $J\bar T$ two- and $N$-point functions and the instanton.
