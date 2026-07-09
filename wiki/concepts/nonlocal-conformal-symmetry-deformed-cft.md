---
type: concept
title: Nonlocal conformal symmetry (deformed CFT)
aliases: [nonlocal conformal symmetry, flowed Virasoro, flowed Virasoro-Kac-Moody]
tags: [ttbar, jtbar, nonlocal-symmetry, virasoro, kac-moody, 2d-cft]
prerequisites: [ttbar-deformation, conformal-field-theory]
created: 2026-07-07
updated: 2026-07-07
---

## Definition

A [[ttbar-deformation|$T\bar T$]]- or [[jt-bar-deformation|$J\bar T$]]-deformed CFT still carries
the conformal (or conformal + $U(1)$) symmetry of the seed CFT, but the generators become
**nonlocal**: they are built from the deformed stress tensor through *field-dependent
coordinates* rather than acting geometrically. Writing the deformed left/right energy densities
$\mathcal H_L,\mathcal H_R$, the modes
$$\tilde L_m=i^{m+1}\!\int dy\,\hat u^{\,m+1}\,\mathcal H_L,\qquad
\tilde{\bar L}_m=(-i)^{m+1}\!\int dy\,\hat v^{\,m+1}\,\mathcal H_R$$
use coordinates $\hat u=u+\delta\hat u$, $\hat v=v+\delta\hat v$ whose shifts $\delta\hat u,\delta\hat v$
depend on the fields (on $\mathcal H_R,\mathcal H_L$). This makes the generators nonlocal in the
original coordinates.

## Key formulas

For $T\bar T$ the flowed generators close into two commuting classical Witt/Virasoro algebras,
$$i\{\tilde L_n,\tilde L_m\}=(n-m)\,\tilde L_{n+m},\qquad i\{\tilde{\bar L}_n,\tilde{\bar L}_m\}=(n-m)\,\tilde{\bar L}_{n+m}.$$
For $J\bar T$ the surviving structure is a **Virasoro–Kac–Moody** algebra,
$$i\{\tilde L_n,\tilde L_m\}=(n-m)\tilde L_{n+m},\quad
i\{\tilde{\mathcal J}_n,\tilde{\mathcal J}_m\}=mk\,\delta_{m,-n},\quad
i\{\tilde L_n,\tilde{\mathcal J}_m\}=-m\,\tilde{\mathcal J}_{m+n},$$
plus a barred copy — **local in the left-moving sector, nonlocal in the right**, since $J\bar T$
breaks the right-moving conformal symmetry. The field-dependent coordinate is $\hat v$ with
$\partial\hat v/\partial y=1-\lambda\tilde{\mathcal J}_++\tfrac{\lambda^2 k}{4\pi}\mathcal H_R$.

## Relations

The reason ordinary local operators are awkward in these theories: the symmetry does not act on
them tractably. This motivates the [[dressed-operator-deformed-cft|dressed operators]] (primaries
of this nonlocal symmetry) and the [[physical-operator-deformed-cft|physical operators]] (local,
recovered by smearing). The generators are constructed via the
[[hamiltonian-flow-deformed-cft|Hamiltonian flow]]. Earlier realizations of the same nonlocal
symmetry appear at the Lagrangian and gravity levels (Guica–Monten 2019–2020).

## Where it appears

- [[2507.08588|Chen–Du–Liu–Song 2025]] — two commuting flowed Virasoro algebras for $T\bar T$.
- [[2511.10557|Chen–Du–Song 2025]] — the local-left / nonlocal-right Virasoro–Kac–Moody algebra
  of $J\bar T$.
