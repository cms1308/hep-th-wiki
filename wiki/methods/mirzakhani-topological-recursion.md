---
type: method
title: Mirzakhani topological recursion
aliases: [Mirzakhani recursion, Weil–Petersson volume recursion]
tags: [hyperbolic-geometry, moduli-space, weil-petersson, topological-recursion]
prerequisites: [weil-petersson-volumes]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

A recursion generating the [[weil-petersson-volumes|Weil–Petersson volumes]] $V_{g,n}(b_1,\dots,b_n)$
of moduli spaces of bordered hyperbolic Riemann surfaces from lower-complexity data, ultimately from
the pair of pants $V_{0,3}=1$. Mirzakhani (2006) derived it from an identity that unfolds the length
spectrum of simple closed geodesics over the mapping class group. Eynard and Orantin (2007) showed it
is a special case of their [[eynard-orantin-topological-recursion|topological recursion]] on the
spectral curve $x=\tfrac12 z^2$, $y=-\tfrac{z}{2\pi}\sin(2\pi z)$.

In [[closed-string-field-theory|closed string field theory]] the same recursion, applied to the
[[hyperbolic-string-vertices|hyperbolic string vertices]], generates every closed-string vertex
$V_{0,n}$ from the cubic $V_{0,3}$ — the step that reduces the nonpolynomial EOM to the
[[fvm-quadratic-integral-equation|FVM quadratic integral equation]].

## Prerequisites

- Hyperbolic surfaces with geodesic borders of length $b_i$; the [[weil-petersson-volumes|WP volume]]
  as the integrand.
- The two Mirzakhani integration kernels $R$ (border-splitting, a pair of pants attached to two
  lower surfaces via one internal geodesic) and $D$ (non-separating, one internal pair of geodesics).

## How it works

The recursion writes a derivative of $V_{g,n}$ as an integral, over one border length, of kernels
against lower volumes:
- the **$R$-kernel** term glues a pair of pants along a single internal geodesic $\ell$, joining two
  lower-complexity surfaces (the separating / R-channel);
- the **$D$-kernel** term removes a handle or joins a self-gluing along a pair $(\ell_1,\ell_2)$ (the
  non-separating / D-channel).

For string vertices the vertex region is restricted to systole $\ge L$; subtracting the
Feynman-diagram region (systole $<L$) from the standard kernels produces the
[[twisted-mirzakhani-kernels|twisted kernels $\hat R,\hat D$]], which act as scalar multiplicative
weights on the cubic vertex $V_{0,3}$. The [[seam-graded-expansion|seam-graded]] iteration of the
tachyon-vacuum equation, evaluated at its solution, reproduces exactly this genus-0 recursion: B-terms
are the R-channel, C-terms the D-channel.

## Regime of validity

- Genus-0 (classical string vertices) is the case used for the tachyon vacuum; the recursion extends
  to all $(g,n)$, so the quantum (higher-genus) closed SFT vertices, e.g. $V_{1,1}(L_1)$, are in
  principle accessible the same way.
- For string vertices the border lengths sit at/relative to the [[systolic-threshold|systolic length]]
  $L_*$.

## Canonical applications

- Weil–Petersson volumes and, through the [[jt-gravity-matrix-integral-duality|JT/matrix duality]],
  the genus expansion of [[jt-gravity]].
- Generating all closed-string vertices $V_{0,n}$ from $V_{0,3}$ in hyperbolic CSFT
  ([[fvm-quadratic-integral-equation|FVM]]; [[2603.29926|Kim 2026]]).
