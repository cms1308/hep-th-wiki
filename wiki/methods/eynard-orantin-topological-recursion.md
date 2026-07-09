---
type: method
title: Eynard–Orantin topological recursion
aliases: [topological recursion, Eynard-Orantin recursion, loop equations]
tags: [matrix-models, jt-gravity, topological-recursion]
prerequisites: [jt-spectral-curve]
created: 2026-07-07
updated: 2026-07-07
---

## What it computes

Given a spectral curve — a plane curve $y(z)$ with a marked branch point and the trivial two-point
function $W_{0,2}=1/(z_1-z_2)^2$ — topological recursion generates all higher connected
correlators (multi-resolvents) $W_{g,n}(z_1,\dots,z_n)$ of the associated matrix model, order by
order in the genus. For [[jt-gravity|JT gravity]] with the [[jt-spectral-curve|spectral curve]]
$y=\frac{\sin 2\pi z}{4\pi}$, the outputs are the Laplace-transformed
[[weil-petersson-volumes|Weil–Petersson volumes]], hence all JT amplitudes $Z_{g,n}$.

## Prerequisites

- A spectral curve $y(z)$ and $W_{0,1}=2z\,y(z)$, $W_{0,2}=1/(z_1-z_2)^2$.
- Coordinate near the branch point (for JT, $x=z^2=-E$, branch point at $z=0$).

## How it works

The recursion is a residue at the branch point:
$$W_{g,n}(z_1,J)=\mathop{\mathrm{Res}}_{z\to0}\frac{1}{z_1^2-z^2}\,\frac{1}{4y(z)}\Big[W_{g-1,n+1}(z,-z,J)+\!\!\sum_{\substack{h+h'=g\\ I\sqcup I'=J}}'\!\!W_{h,1+|I|}(z,I)\,W_{h',1+|I'|}(-z,I')\Big],$$
where $J=\{z_2,\dots,z_n\}$ and the primed sum omits the two $W_{0,1}$ terms. Each step raises
$2g+n$ by one, so all correlators follow from $W_{0,1}$ and $W_{0,2}$. Eynard and Orantin proved
that for $y=\frac{\sin 2\pi z}{4\pi}$ this recursion reproduces
[[mirzakhani-topological-recursion|Mirzakhani's recursion]] for Weil–Petersson volumes — the
mathematical heart of the [[jt-gravity-matrix-integral-duality|JT/matrix duality]].

## Regime of validity

- Perturbative (all-orders genus) statement; the resulting series is asymptotic and needs a
  [[nonperturbative-completion-jt|nonperturbative completion]].
- Orientable, Hermitian ($\beta=2$) ensembles. Other symmetry classes need generalized recursions.

## Canonical applications

- All $(p,q)$ [[minimal-string|minimal-string]] amplitudes and Weil–Petersson volumes.
- [[1903.11115|Saad–Shenker–Stanford 2019]] — generating the full genus expansion of JT gravity
  from its spectral curve; reproducing the RMT ramp resolvent $R_{0,2}$ and predicting
  [[large-genus-weil-petersson-asymptotics|large-genus volume asymptotics]].
- The same [[mirzakhani-topological-recursion|Mirzakhani recursion]] generates the
  [[hyperbolic-string-vertices|hyperbolic string vertices]] of [[closed-string-field-theory]]
  ([[2603.29926|Kim 2026]]).
