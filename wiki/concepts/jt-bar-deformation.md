---
type: concept
title: JTbar deformation
aliases: [JTbar, J-Tbar, JTbar deformation, (1,2) deformation]
tags: [jtbar, irrelevant-deformation, 2d-cft, warped-ads3, non-ads-holography]
prerequisites: [conformal-field-theory, ttbar-deformation]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

The $J\bar T$ deformation is an irrelevant deformation of a 2d CFT with a chiral $U(1)$ current
$J$, driven by the Lorentz-scalar bilinear of the $U(1)$ current and the right-moving component
of the stress tensor:
$$\partial_\lambda S=\int d^2x\,\mathcal O_{J\bar T},\qquad
\mathcal O_{J\bar T}=\epsilon^{\alpha\beta}\mathcal J_{+\alpha}\,T_{v\beta}\;\big(\propto J\bar T\ \text{at the CFT point}\big).$$
Like the [[ttbar-deformation|$T\bar T$ deformation]] it is built from a
$\epsilon^{ab}\epsilon^{\mu\nu}J_{\mu a}J_{\nu b}$ current bilinear, but replacing one
stress-tensor factor by a $U(1)$ current makes it a $(1,2)$ operator: it breaks Lorentz
invariance and the right-moving conformal symmetry while *preserving the full left-moving
Virasoro–Kac–Moody symmetry*. It is solvable — the deformed spectrum, charge flow, and torus
partition function are fixed by the undeformed data.

## Motivation

The deformation was introduced (Guica 2017) as the simplest solvable relative of $T\bar T$ that
keeps one chiral half of the conformal symmetry. That asymmetric structure is exactly what
holography beyond AdS wants: Kerr/CFT and warped-AdS$_3$ carry a reduced
$SL(2,\mathbb R)_L\times U(1)_R$ symmetry, and the $(1,2)$ irrelevant deformation is the
field-theory operator identified in that supergravity analysis. Single-trace $J\bar T$ provides
a concrete string dual via [[tst-holography|TsT]] of AdS$_3$.

## Key formulas

Under $J\bar T$ the right-moving energy density is dressed (Hamiltonian formalism, plane):
$$\mathcal H_R=\frac{2\pi}{\lambda^2 k}\Big(1-\lambda\mathcal J^{(0)}_+-\sqrt{(1-\lambda\mathcal J^{(0)}_+)^2-\tfrac{\lambda^2 k}{\pi}\mathcal H^{(0)}_R}\Big),$$
with $k$ the $U(1)$ level. The combination $\tilde{\mathcal J}_+=\mathcal J^{(0)}_++\tfrac{\lambda k}{2\pi}\mathcal H_R$
stays chiral and flow-invariant, and the left $U(1)$ charge flows as
$Q_L=\tilde{\mathcal J}_0-\tfrac{\lambda k}{2\pi}H_R$. The surviving symmetry is a
Virasoro–Kac–Moody algebra, local on the left and nonlocal on the right — see
[[nonlocal-conformal-symmetry-deformed-cft]].

## Relations

Sibling of the [[ttbar-deformation|$T\bar T$ deformation]] within the same family of solvable
current-bilinear deformations; shares its [[hamiltonian-flow-deformed-cft|Hamiltonian flow]],
[[dressed-operator-deformed-cft|dressed]] and [[physical-operator-deformed-cft|physical]]
operators, and [[deformed-cft-two-point-function|two-point function structure]]. Its
holographic realization is [[tst-holography|single-trace $J\bar T$ / TsT]], connecting to
[[ads-cft-correspondence]] and warped AdS$_3$.

## Where it appears

- [[2511.10557|Chen–Du–Song 2025]] — symmetry algebra, dressed/physical operators, and
  correlators (including a nonperturbative instanton) of $J\bar T$-deformed CFTs.
- Original definition and solvable spectrum: Guica 2017; Chakraborty–Giveon–Kutasov 2018.
