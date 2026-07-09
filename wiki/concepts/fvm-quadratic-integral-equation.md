---
type: concept
title: FVM quadratic integral equation
aliases: [Fırat–Valdes-Meller equation, quadratic integral equation]
tags: [string-field-theory, topological-recursion, closed-string-tachyon]
prerequisites: [closed-string-field-theory, hyperbolic-string-vertices, mirzakhani-topological-recursion]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The classical equation of motion of hyperbolic
[[closed-string-field-theory|closed string field theory]], reduced to a single **quadratic integral
equation** for the string field $\Phi(L_1)$ as a function of a border geodesic length. Derived by
Fırat and Valdes-Meller (FVM) by applying the
[[mirzakhani-topological-recursion|topological recursion]] to the
[[hyperbolic-string-vertices|hyperbolic string vertices]]: because the recursion generates every
$V_{0,n}$ from the cubic
$V_{0,3}$, the full nonpolynomial EOM (an infinite sum over vertices) collapses to a self-consistency
condition quadratic in $\Phi$.

Gauge-fixed with the Fenchel–Nielsen $b$-ghost, it has three terms distinguished by how many internal
geodesics are integrated:
$$\Phi(L_1)=C_A\,A_{L_1,L,L}(\mathrm{BG}\Phi(L),\mathrm{BG}\Phi(L))
+C_B\!\int_0^\infty\!\!d\ell\,\hat R\,A_{L_1,L,\ell}(\mathrm{BG}\Phi(L),\mathrm{BG}\Phi(\ell))
+C_C\!\int_0^\infty\!\!\int_0^\infty\!\!d\ell_1 d\ell_2\,\hat D\,A_{L_1,\ell_1,\ell_2}(\mathrm{BG}\Phi(\ell_1),\mathrm{BG}\Phi(\ell_2)),$$
where $A$ is the cubic vertex contracted with two dressed string fields, and $\hat R,\hat D$ are the
[[twisted-mirzakhani-kernels|twisted Mirzakhani kernels]]. The A-term is local (no integral), the
B-term integrates one geodesic, the C-term two — the seam structure exploited by the
[[seam-graded-expansion|seam-graded expansion]].

## Motivation

Solving CSFT directly means handling infinitely many vertices with no closed algebra. The FVM
equation replaces that with one equation whose only vertex input is $V_{0,3}$ and whose kernels are
explicit hyperbolic-geometry objects — a finite, computable starting point for constructing the
[[closed-string-tachyon-vacuum|tachyon vacuum]].

## Key formulas

- Combinatorial coefficients (after $\Phi\to(4/\kappa)\Phi$): $C_A=2$, $C_B=4$, $C_C=2$.
- Twisted kernels (Feynman-region subtractions of the Mirzakhani kernels $R,D$):
  $\hat R_{L_1,L_2,L_3}=R_{L_1,L_2,L_3}-L_1\theta(L-L_3)$, and $\hat D$ the analogous double
  subtraction (see [[twisted-mirzakhani-kernels]]).
- Negative-length convention: $L_i<0$ signals a $\mathrm{BG}$ insertion at puncture $i$ of physical
  length $|L_i|$, folding integration to $[0,\infty)$.

## Relations

- Derived from [[hyperbolic-string-vertices]] via the
  [[mirzakhani-topological-recursion|topological recursion]] on
  [[weil-petersson-volumes|Weil–Petersson volumes]].
- Built from [[twisted-mirzakhani-kernels]] and the cubic hyperbolic vertex.
- Solved perturbatively by the [[seam-graded-expansion]]; its fixed point encodes the genus-0
  recursion.
- FVM solved the analogous *stubbed scalar QFT* version of this equation exactly.

## Where it appears

- Introduced by Fırat–Valdes-Meller (the FVM formulation).
- Solved for the string in the scalar sector by [[2603.29926|Kim 2026]].
