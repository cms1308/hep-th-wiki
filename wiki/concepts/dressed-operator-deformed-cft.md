---
type: concept
title: Dressed operator (deformed CFT)
aliases: [dressed operator, flowed operator, flowed primary]
tags: [ttbar, jtbar, nonlocal-symmetry, operators, 2d-cft]
prerequisites: [ttbar-deformation, nonlocal-conformal-symmetry-deformed-cft, hamiltonian-flow-deformed-cft]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

In a [[ttbar-deformation|$T\bar T$]]- or [[jt-bar-deformation|$J\bar T$]]-deformed CFT, a
**dressed** (or *flowed*) operator is the solution of the flow equation that transforms as a
primary under the deformed, *nonlocal* conformal symmetry
([[nonlocal-conformal-symmetry-deformed-cft]]). It is a covariant constant of the
[[hamiltonian-flow-deformed-cft|Hamiltonian flow]]:
$$\mathcal D_\lambda\,\tilde{\mathcal O}\equiv\big(\partial_\lambda-i[\mathcal X,\cdot]\big)\tilde{\mathcal O}=0,$$
where $\mathcal X$ is the bilocal generator of the deformation. Because the flowed Virasoro
generators are nonlocal, the dressed operator is itself **nonlocal** — but it carries exactly
the undeformed conformal weight $(h,\bar h)$ and has undeformed-CFT correlation functions.

This is the operator class needed to bring conformal symmetry to bear on the deformed theory:
correlators of dressed operators are computed with ordinary CFT Ward identities.

## Key formulas

For $T\bar T$, a weight-$(h,\bar h)$ primary dresses (in the field-dependent coordinates
$\hat u,\hat v$) to
$$\tilde{\mathcal O}_{h,\bar h}(\hat u,\hat v)=\frac{\mathcal O_{h,\bar h}(u,v)}{1+\lambda^2\mathcal O_{T\bar T}},$$
equivalently the closed double sum
$\tilde{\mathcal O}_{h,\bar h}=\sum_{n,m}\tfrac{(-1)^n}{(n-m)!\,m!}\partial_u^m\partial_v^{\,n-m}\big((\delta\hat u)^m(\delta\hat v)^{n-m}\mathcal O_{h,\bar h}\big)$.
For $J\bar T$ the dressing is local only in the left null direction,
$\tilde{\mathcal O}_{h,\bar h,q}=\sum_n\tfrac{1}{n!}\partial_v^n\big((-\delta\hat v)^n e^{i\lambda q\bar\eta_0}\mathcal O_{h,\bar h,q}\big)$.

## Relations

Contrast with two other operator classes in the same theories:
- **Undeformed operator** — the local operator obtained by evolving an initial CFT operator with
  the deformed Hamiltonian; local but *not* organized by the symmetry.
- [[physical-operator-deformed-cft|Physical operator]] — a *local* operator recovered from the
  dressed operator by smearing it over a field-dependent delta function; local *and*
  symmetry-organized.

Dressed and physical operators are two solutions of the same flow equation with different
locality/primary properties; the physical operator is the observable one, the dressed operator
the symmetry-covariant intermediary.

## Where it appears

- [[2507.08588|Chen–Du–Liu–Song 2025]] — closed-form dressed stress tensor and dressed primaries
  for $T\bar T$.
- [[2511.10557|Chen–Du–Song 2025]] — dressed currents and operators for $J\bar T$.
- Earlier flowed-operator constructions: Kruthoff–Parrikar 2020; Guica 2021.
