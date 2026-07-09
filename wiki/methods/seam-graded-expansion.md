---
type: method
title: Seam-graded expansion
aliases: [seam grading, seam-graded algebra]
tags: [string-field-theory, closed-string-tachyon, topological-recursion]
prerequisites: [closed-string-field-theory, fvm-quadratic-integral-equation, hyperbolic-string-vertices]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

A perturbative solution of the classical
[[closed-string-tachyon-vacuum|closed string tachyon vacuum]] equation of motion, order by order,
such that **each order is purely algebraic** — a single
matrix inversion rather than a Fredholm integral equation. Introduced in~[[2603.29926|Kim 2026]] for
the [[fvm-quadratic-integral-equation|FVM quadratic integral equation]] in the sector of
zero-momentum Lorentz-scalar states.

## Prerequisites

- The [[fvm-quadratic-integral-equation|quadratic integral equation]] with its three terms A (local,
  no integral), B (one geodesic integral), C (two geodesic integrals), built from
  [[twisted-mirzakhani-kernels|twisted Mirzakhani kernels]] and the cubic
  [[hyperbolic-string-vertices|hyperbolic vertex]].
- The Fock-space projection with $b$-ghost dressing, evaluated at the
  [[systolic-threshold|systolic length]] $L_*$.

## How it works

The string field is expanded by **seam grade** — the number of integrated internal geodesics
("seams", i.e. pairs of pants beyond the initial 3-punctured sphere) in a contribution:
$$\Phi(L_1)=\sum_{n\ge0}\Phi_n(L_1).$$
Two facts make the expansion algebraic:

1. **Intrinsic seam cost.** In the [[fvm-quadratic-integral-equation|quadratic equation]] the A-term
   opens no seam (cost $0$), the B-term one (cost $1$), the C-term two (cost $2$). Grades add: a term
   with operator seam cost $c$ acting on $\Phi_j, \Phi_k$ has grade $c+j+k$.

2. **Point evaluation of the highest grade.** Because B and C open new seams, the grade-$n$ unknown
   $\Phi_n$ can appear on the right-hand side of the grade-$n$ equation **only through the A-term**,
   which is local and evaluates the string field at the single systolic point $L$. Everything else
   at grade $n$ is a *source* $S_n$ built from strictly lower grades $\Phi_{<n}$.

Hence the grade-$n$ equation is
$$\Phi_n(L_1)=S_n(L_1)+M(L_1)\,\Phi_n(L),$$
which is closed by setting $L_1=L$: $(I-M(L))\Phi_n(L)=S_n(L)$, a finite matrix inversion in the
truncated Fock space. The full-argument solution is then
$$\Phi_n(L_1)=S_n(L_1)+M(L_1)\,(I-M(L))^{-1}S_n(L).$$

The linearized operator is **grade-independent**: $M(L)=2J\,B(L)$ with
$J^{\alpha\beta}=C_A\sum_\gamma V^{\alpha\beta\gamma}(L,L,L)\,\tilde g_\gamma^{(0)}$ symmetric and $B$
the $b$-ghost matrix, so the same inversion is reused at every order. The dressed grade-0 seed is an
eigenvector of $M$ with eigenvalue $2$; in the tachyon-only projection $M_T(L)=2$ exactly (the
linearization of $x=ax^2$ at its nontrivial root), giving $g_T^{(n)}(L)=-S_n^T(L)$.

Evaluated at the solution, the seam iteration reproduces the genus-0
[[mirzakhani-topological-recursion|Mirzakhani/FVM recursion]]: B-terms build $V_{0,n+3}$ through the
R-channel, C-terms through the D-channel, while the A-term back-reaction (absent in the linear
recursion) enforces the nonlinear self-consistency of the vacuum.

## Regime of validity

- Requires a sector **closed under the EOM**; the zero-momentum Lorentz-scalar sector qualifies (a
  scalar cannot source non-scalars through the cubic vertex). Spacetime-derivative terms drop there,
  so the component vertex equation applies directly.
- Formal/perturbative: the grade expansion is defined order by order; **convergence is not
  guaranteed**. In the tachyon-only truncation it diverges badly
  ($\epsilon_B=|S_1^T|/|g_T^{(0)}|\simeq2.6\times10^{18}$), consistent with the requirement of
  [[ghost-dilaton-condensation-tachyon-vacuum|ghost-dilaton condensation]]. Whether the full
  multi-level expansion converges is [[closed-string-tachyon-vacuum-convergence|open]].
- The linearized recursion is unobstructed only if $M(L_*)$ has no eigenvalue near $1$; numerically
  its spectrum is $\lambda_{\max}=2$ with all others $<10^{-4}$.

## Canonical applications

- The [[closed-string-tachyon-vacuum|closed string tachyon vacuum]] of the bosonic string
  ([[2603.29926|Kim 2026]]) — the sole application to date.
