---
type: result
title: Large-genus asymptotics of Weil–Petersson volumes
aliases: [Zograf conjecture, large-genus WP volumes]
tags: [jt-gravity, weil-petersson-volumes, resurgence, matrix-models]
status: conjectured
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[weil-petersson-volumes|Weil–Petersson volumes]] $V_{g,n}(b)$ grow factorially with genus,
and their leading large-$g$ asymptotics are fixed by the nearest singularity of the Borel transform
of the JT genus expansion. For no boundaries,
$$V_{g,0}\approx\frac{(4\pi^2)^{2g-5/2}}{\sqrt2\,\pi^{3/2}}\,\Gamma\!\big(2g-\tfrac52\big),$$
and for one geodesic boundary of length $b$,
$$V_{g,1}(b)\approx\frac{\Gamma(2g-1)}{\pi i}\int_{\mathcal C}\frac{dz}{2\pi}\,\frac{\sinh(bz)}{bz}\,\frac{1}{t(z)^{2g-1}},\qquad
t(z)=\frac{\sin 2\pi z-2\pi z\cos 2\pi z}{4\pi^3}.$$
Derived from JT gravity by [[1903.11115|Saad–Shenker–Stanford 2019]].

## Derivation sketch

The genus expansion is an asymptotic series with $(2g)!$-type growth. Its Borel transform has a
branch point at $t=1/(4\pi^2)$, set by the one-eigenvalue instanton — the extremum of the
effective potential $V_{\rm eff}$ at $E=-\tfrac14$ (the ZZ brane at $z_{\rm ZZ}=\tfrac12$). The
exponentially small density in the classically forbidden region $E<0$ controls this singularity,
and standard resurgence relates the singularity's location and strength to the large-order growth
of the $V_{g,n}$. The $b$-dependence enters through the trumpet Laplace kernel $\sinh(bz)/bz$.

## Assumptions

- The dominant Borel singularity is the leading one-instanton (nearest-brane) contribution;
  subleading branch points give $1/g$ corrections.
- The forbidden-region density and spectral curve of orientable bosonic JT gravity.

## Status

**Conjectured, strongly checked.** The $V_{g,0}$ formula reproduces Zograf's (2008) conjecture,
and $V_{g,1}(b\ll g)$ matches; the general-$b/g$ formula is new and was verified against Zograf's
exact volume data up to $g=20$. A gravitational prediction of a purely mathematical asymptotic —
one direction of the [[jt-gravity-matrix-integral-duality|JT/matrix duality]] paying off in number
theory / geometry.

## Implications

- Concrete illustration that the JT genus sum is asymptotic and requires a nonperturbative
  completion (the very instanton that sets the growth also drives the
  [[nonperturbative-completion-jt|instability]]).
- Provides high-genus data to test resurgence and the trans-series structure of 2d gravity.
