---
type: concept
title: JT spectral curve
aliases: [spectral curve of JT gravity, sinh spectral curve]
tags: [jt-gravity, matrix-models, topological-recursion]
prerequisites: [jt-gravity, weil-petersson-volumes]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The spectral curve is the single piece of data that, fed into
[[eynard-orantin-topological-recursion|topological recursion]], generates every amplitude of
[[jt-gravity|JT gravity]]. For JT it is
$$y(z)=\frac{\gamma}{2\pi}\sin\!\big(2\pi\sqrt{2\gamma}\,z\big)\ \xrightarrow{\ \gamma=1/2\ }\ \frac{\sin(2\pi z)}{4\pi},\qquad x=z^2=-E,$$
equivalent to the genus-zero density of states
$$\rho_0(E)=\frac{\gamma}{2\pi^2}\sinh\!\big(2\pi\sqrt{2\gamma E}\big).$$
The coordinate $z$ satisfies $z^2=-E$, so real $z$ probes the classically forbidden region $E<0$;
$y=-\pi i\,\rho_0(E)$ under continuation through the upper half-plane.

## Motivation

A double-scaled matrix model is specified entirely by its leading eigenvalue density (equivalently
its spectral curve $y(x)$); all connected multi-resolvent correlators follow by loop equations.
[[1903.11115|Saad–Shenker–Stanford]] read $\rho_0$ off the [[schwarzian-theory|Schwarzian]] disk
partition function, showed the resulting $y$ is exactly the curve for which the Eynard–Orantin
recursion reproduces Mirzakhani's [[weil-petersson-volumes|Weil–Petersson volume]] recursion, and
thereby identified the whole of JT gravity with this one curve.

## Key formulas

- $y=\frac{\sin 2\pi z}{4\pi}$ — the curve (for $\gamma=\tfrac12$).
- $\rho_0(E)=\frac{1}{4\pi^2}\sinh(2\pi\sqrt{E})$ — density of states at $\gamma=\tfrac12$.
- Recursion inputs $W_{0,1}=2z\,y(z)$, $W_{0,2}=\frac{1}{(z_1-z_2)^2}$.
- The curve's oscillatory continuation to $E<0$ sets the
  [[nonperturbative-completion-jt|one-eigenvalue instanton]] at $E=-\tfrac14$.

## Relations

- Distinguished from the $\sqrt E$ Airy curve of topological gravity: JT's $\sinh$ makes it the
  $p\to\infty$ limit of the $(2,p)$ [[minimal-string|minimal string]], whose curve is
  $y\propto\sin(p\cdot\mathrm{arccos})$.
- Input to [[eynard-orantin-topological-recursion]]; output is $Z_{g,n}$ / $V_{g,n}$.

## Where it appears

- [[1903.11115|Saad–Shenker–Stanford 2019]] — derives the curve from the disk and shows it
  reproduces all Weil–Petersson volumes.
