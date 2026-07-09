---
type: concept
title: Physical operator (deformed CFT)
aliases: [physical operator, local physical operator]
tags: [ttbar, jtbar, operators, 2d-cft, correlators]
prerequisites: [ttbar-deformation, dressed-operator-deformed-cft]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A **physical operator** is a *local* operator in a [[ttbar-deformation|$T\bar T$]]- or
[[jt-bar-deformation|$J\bar T$]]-deformed CFT, introduced in
[[2507.08588|Chen–Du–Liu–Song 2025]], built from an undeformed primary $\mathcal O^{(0)}_{h,\bar h}$
multiplied by stress-tensor / current factors. It combines the two properties that the other
operator classes have only one of each: it is local (unlike the
[[dressed-operator-deformed-cft|dressed operator]]) and organized by the deformed conformal
symmetry (unlike the undeformed operator). It is fixed uniquely, up to the dressing ansatz, by
demanding that the extra field-dependent weight-shift terms in the flow / Ward identity cancel.

## Key formulas

For $T\bar T$:
$$\mathcal O_{h,\bar h}=\frac{1+\lambda^2\mathcal O_{T\bar T}}{(1+2\lambda\mathcal H_R)^h\,(1+2\lambda\mathcal H_L)^{\bar h}}\,\mathcal O^{(0)}_{h,\bar h}.$$
For $J\bar T$, with chiral charge $q$:
$$\mathcal O_{h,\bar h,q}=\frac{\mathcal O^{(0)}_{h,\bar h,q}}{(1-\lambda\tilde{\mathcal J}_+)\big(1-\lambda\tilde{\mathcal J}_++\tfrac{\lambda^2 k}{4\pi}\mathcal H_R\big)^{\bar h-1}}.$$
Either way, the physical operator equals a dressed operator smeared over a field-dependent
(nonlocal) delta function onto the field-dependent coordinates $U,V$:
$$\mathcal O_{h,\bar h}(u,v)=\int d^2\sigma\,\delta\big(U(\sigma)-u,\,V(\sigma)-v\big)\,\tilde{\mathcal O}_{h,\bar h}(\sigma).$$
Classically the $T\bar T$ physical operator coincides with the local operator of the
topological-gravity (Aharony–Barel) formulation.

## Relations

The observable endpoint of the [[dressed-operator-deformed-cft|dressed]]/undeformed/physical
trichotomy. Its two-point function — computed by resumming the leading logs of the smeared
dressed correlator — is the [[deformed-cft-two-point-function]] with a momentum-dependent
effective weight $h_\lambda$. Its position-space flow equation is a *total* derivative,
distinguishing it from the undeformed operators of Kruthoff–Parrikar and Cardy. A fully quantum
definition (normal ordering, exact correlators) is open — see
[[quantum-operators-deformed-cft]].

## Where it appears

- [[2507.08588|Chen–Du–Liu–Song 2025]] — introduces physical operators for $T\bar T$; equivalence
  with the Aharony–Barel operator; two-point function.
- [[2511.10557|Chen–Du–Song 2025]] — physical operators for $J\bar T$; left-primary with shifted
  charge; two- and $N$-point functions.
