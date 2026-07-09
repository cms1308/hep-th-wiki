---
type: question
title: Does the seam-graded closed string tachyon vacuum expansion converge?
aliases: [seam-graded convergence]
tags: [string-field-theory, closed-string-tachyon, convergence]
status: open
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[seam-graded-expansion|seam-graded expansion]] solves the
[[fvm-quadratic-integral-equation|FVM quadratic integral equation]] for the
[[closed-string-tachyon-vacuum|closed string tachyon vacuum]] order by order, each grade a matrix
inversion. But the expansion is defined formally. **Does it converge, and if so on what field
content?** In the tachyon-only truncation it diverges spectacularly
($\epsilon_B=|S_1^T|/|g_T^{(0)}|\simeq2.6\times10^{18}$). The open question is whether the full
multi-level system — including the ghost dilaton and higher-level states — has convergence ratio below
$1$, or whether the series is only asymptotic and must be Borel/otherwise resummed.

## Why it matters

Convergence is what separates a formal recursion from an actual construction of the vacuum. If the
multi-level expansion converges, it yields an analytic, nonperturbative closed string tachyon vacuum —
a concrete instance of background independence and a window on the closed-string landscape. If it is
only asymptotic, the vacuum still exists but requires a resummation scheme, and the "nothing" state is
reached only after nonperturbative input.

## Main attempts

- **Tachyon-only sector** ([[2603.29926|Kim 2026]]): diverges. This is expected, since
  [[ghost-dilaton-condensation-tachyon-vacuum|the ghost dilaton must condense]] — the tachyon
  component alone is not the vacuum.
- **Multi-level truncations**: at level $(0{+}2{+}4)$ the linearized operator $M(L_*)$ has a clean
  spectrum (largest eigenvalue $2$, all others $<10^{-4}$), so the recursion is *unobstructed* even
  though the tachyon-only series diverges. Whether adding levels drives $\epsilon_B<1$ is the decisive
  test not yet completed.
- The large-$n$ growth of the source norms $\|S_n\|$ (set by the moduli-space geometry of
  $V_{0,n+3}$) is the quantity that ultimately controls convergence and has not been characterized.

## Current status

Open. The linearized recursion is unobstructed and the machinery is algebraic at every order, but
convergence of the multi-level expansion — the decisive test — is the stated subject of ongoing work.
