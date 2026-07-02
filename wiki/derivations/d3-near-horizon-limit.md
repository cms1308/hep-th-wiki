---
type: derivation
title: "D3-brane near-horizon limit: emergence of AdS5×S5"
aliases: [near-horizon limit of D3-branes]
tags: [ads-cft, string-theory, supergravity]
prerequisites: [anti-de-sitter-space, brane-decoupling-limit]
status: verified
source: sources/arxiv/hep-th-9711200
created: 2026-07-03
updated: 2026-07-03
---

## Goal

Show that in the decoupling limit, the geometry sourced by $N$ coincident D3-branes becomes
$AdS_5 \times S^5$ with common radius $R^4/\alpha'^2 = 4\pi g N$ — the gravity side of the
[[maldacena-conjecture]]. Follows [[hep-th-9711200|Maldacena 1997]] §2 (eqs. 2.1–2.4).

## Setup and conventions

- Type IIB string theory, string frame, signature $(-,+,\dots,+)$; string coupling $g$
  fixed, $\alpha' = l_s^2$. Conventions such that $g \to 1/g$ under S-duality.
- $x_{||}$: the four worldvolume coordinates; $r$: transverse radial distance;
  $d\Omega_5^2$: unit round $S^5$.
- **Input taken from the source (not re-derived here):** the extremal black 3-brane
  solution of IIB supergravity (Horowitz–Strominger 1991),
  $$ds^2 = f^{-1/2}\, dx_{||}^2 + f^{1/2}\left(dr^2 + r^2 d\Omega_5^2\right),
  \qquad f = 1 + \frac{R^4}{r^4},$$
  with $N$ units of self-dual five-form flux through the $S^5$. Flux quantization fixes
  the coefficient: $R^4 = 4\pi g N \alpha'^2$.

## Derivation

1. **Decoupling limit.** Take
   $$\alpha' \to 0, \qquad U \equiv \frac{r}{\alpha'} = \text{fixed},$$
   with $g, N$ fixed ([[brane-decoupling-limit]]). Physical meaning: $U$ is the mass of a
   string stretched between separated branes (the Higgs vev / W-boson mass in the gauge
   theory), held fixed so the field-theory data survives the limit.

2. **The limit lands you deep in the throat.** With $U$ fixed,
   $$\frac{r}{R} = \frac{\alpha' U}{(4\pi g N)^{1/4}\sqrt{\alpha'}}
   = \frac{\sqrt{\alpha'}\, U}{(4\pi g N)^{1/4}} \;\longrightarrow\; 0,$$
   so the limit automatically probes $r \ll R$: "decoupling limit" and "near-horizon
   region" coincide. Equivalently, in the harmonic function
   $$f = 1 + \frac{4\pi g N \alpha'^2}{r^4} = 1 + \frac{4\pi g N}{\alpha'^2 U^4}
   = \frac{4\pi g N}{\alpha'^2 U^4}\left[1 + O\!\left(\frac{\alpha'^2 U^4}{4\pi gN}\right)\right],$$
   the $1$ is negligible as $\alpha' \to 0$: **drop the 1 in $f$**.

3. **Substitute** $r = \alpha' U$, $dr = \alpha'\,dU$, $f^{1/2} = \frac{\sqrt{4\pi gN}}{\alpha' U^2}$
   term by term:
   - longitudinal: $f^{-1/2} dx_{||}^2 = \alpha' \frac{U^2}{\sqrt{4\pi gN}}\, dx_{||}^2$
   - radial: $f^{1/2} dr^2 = \frac{\sqrt{4\pi gN}}{\alpha' U^2}\,\alpha'^2 dU^2
     = \alpha' \sqrt{4\pi gN}\, \frac{dU^2}{U^2}$
   - sphere: $f^{1/2} r^2 d\Omega_5^2 = \frac{\sqrt{4\pi gN}}{\alpha' U^2}\,\alpha'^2 U^2\, d\Omega_5^2
     = \alpha' \sqrt{4\pi gN}\, d\Omega_5^2$

   Collecting:
   $$\boxed{\;ds^2 = \alpha' \left[ \frac{U^2}{\sqrt{4\pi gN}}\, dx_{||}^2
   + \sqrt{4\pi gN}\, \frac{dU^2}{U^2}
   + \sqrt{4\pi gN}\, d\Omega_5^2 \right]\;}$$
   — exactly eq. (2.3) of the source.

4. **Identify the geometry.** The first two terms are the Poincaré-patch metric of
   [[anti-de-sitter-space|$AdS_5$]],
   $ds^2_{AdS} = \frac{U^2}{\tilde R^2} dx^2 + \tilde R^2 \frac{dU^2}{U^2}$
   with radius $\tilde R^2 = \sqrt{4\pi gN}$ (in units of $\alpha'$); the third term is a
   round $S^5$ of the **same** radius. Hence
   $$AdS_5 \times S^5, \qquad \frac{R^2_{AdS}}{\alpha'} = \frac{R^2_{sph}}{\alpha'} = \sqrt{4\pi g N}.$$
   The radius is quantized because the $F_5$ flux through $S^5$ is the integer $N$.

5. **Why the overall $\alpha'$ is harmless.** Naively the metric shrinks to zero size as
   $\alpha'\to 0$. But the metric is constant in string units, and the overall $\alpha'$
   cancels against the $\alpha'$ dependence of Newton's constant
   ($G_{10} \sim g^2 \alpha'^4$), so curvatures in string units, proper energies of bulk
   modes, and the supergravity action stay finite: bulk dynamics on $AdS_5\times S^5$
   survives the limit. (See the redshift relation
   $E_{proper} = \frac{\omega (4\pi gN)^{1/4}}{\sqrt{\alpha'} U}$ on
   [[holographic-radial-coordinate]].)

6. **Regime of validity.** Supergravity requires curvature small in string units:
   $R^2/\alpha' = \sqrt{4\pi gN} \gg 1$, i.e.
   $$gN \gg 1 \quad (g \le 1; \text{ for } g>1 \text{ S-duality gives } N/g \gg 1),$$
   complementary to gauge-theory perturbation theory ($gN \ll 1$). In ten-dimensional
   Planck units ($l_p = g^{1/4}\sqrt{\alpha'}$), $R/l_p = (4\pi N)^{1/4}$ — large-radius
   spacetime is controlled by $N$ alone.

## Checks

- **Dimensions**: $[\alpha'] = L^2$, $[U] = L^{-1}$, $4\pi gN$ dimensionless. Each bracket
  term is dimensionless ($U^2 dx^2$, $dU^2/U^2$, $d\Omega_5^2$), so $ds^2 \sim L^2$. ✓
- **Source agreement**: step 3 reproduces eq. `\nh` and step 6 reproduces eq. `\sugra` of
  the TeX verbatim. ✓
- **Opposite limit**: keeping the $1$ in $f$, $r \gg R$ gives $f \to 1$, flat
  $\mathbb{R}^{9,1}$ — the solution interpolates between flat space and the AdS throat,
  as expected. ✓
- **Symmetry**: isometries $SO(2,4) \times SO(6)$ of $AdS_5 \times S^5$ = conformal group
  × R-symmetry of $\mathcal{N}=4$ SYM; equal radii are required by the self-duality of
  $F_5$ (Freund–Rubin), consistent with 32 supercharges. ✓

## References

- [[hep-th-9711200|Maldacena 1997]] §2 — followed directly; gaps filled here: the explicit
  $r/R \to 0$ estimate (step 2) and the term-by-term substitution (step 3), which the paper
  states without intermediate steps.
- Extremal 3-brane solution: Horowitz–Strominger 1991 (taken as input).
- Used by: [[maldacena-conjecture]] · [[brane-decoupling-limit]] · [[near-horizon-limit]]
