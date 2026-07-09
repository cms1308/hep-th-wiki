---
type: concept
title: Semi-chiral superfield
aliases: [semi-chiral ring, reduced superfield, holomorphic descendant]
tags: [holomorphic-twist, superspace, brst, dolbeault]
prerequisites: [holomorphic-twist]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

In the [[holomorphic-twist|holomorphic twist]] of a 4d $\mathcal N\geq1$ SQFT, a **semi-chiral
superfield** is a *reduced superfield* — one obtained by setting the un-dotted odd coordinates
$\theta^\alpha=0$ and keeping only the anti-holomorphic ones — that is annihilated by the
supercovariant derivative $D_-$:
$$D_-\mathbf O=(\mathbf Q-\bar\partial)\mathbf O=0,\qquad
\mathbf O\equiv e^{-i\,d\bar z^i\,\widetilde{\mathcal Q}_i}\,\mathbf O^{(0)}
=\mathbf O^{(0)}+\mathbf O^{(1)}+\mathbf O^{(2)},$$
where $\bar\partial=d\bar z^i\,\partial_{\bar z^i}$ and the components $\mathbf O^{(k)}$ are
$(0,k)$-forms. Equivalently: its bottom component is a **semi-chiral field**
($\mathbf Q\,\mathbf O^{(0)}=0$) and its higher components obey the **holomorphic descent
equations**
$$\mathbf Q\,\mathbf O^{(k)}=\bar\partial\,\mathbf O^{(k-1)}.$$

Semi-chiral superfields are in **one-to-one correspondence with $\mathbf Q$-closed local
operators**: given a semi-chiral field $O$ one builds the superfield by applying
$e^{-i\,d\bar z^i\widetilde{\mathcal Q}_i}$. The $\mathbf Q$-cohomology classes of these
operators form the **semi-chiral ring** (the holomorphic-twist analogue of the chiral ring),
named by analogy in ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]] following Budzik et al.

## Motivation

Each $\mathcal N=1$ multiplet satisfying an anti-chiral shortening condition contributes exactly
one $\mathbf Q$-closed operator — the bottom component of a semi-chiral superfield. This gives a
uniform bookkeeping device for the protected content of *any* $\mathcal N\geq1$ theory (higher
$\mathcal N$ multiplets are decomposed into $\mathcal N=1$ pieces). Because BPS observables are
insensitive to $\mathbf Q$-exact deformations, the descent structure is sensitive only to
cohomology classes, so semi-chiral superfields package a whole multiplet — operator plus
holomorphic descendants — into the natural variables for the twisted OPE.

## Key formulas

- Reduced superfield with $\bar\theta^i=i\,d\bar z^i$ identified as an anti-holomorphic
  one-form: $\mathbf O=\mathbf O^{(0)}+\mathbf O^{(1)}+\mathbf O^{(2)}$.
- Semi-chirality: $(\mathbf Q-\bar\partial)\mathbf O=0$; descent $\mathbf Q\,\mathbf O^{(k)}=\bar\partial\,\mathbf O^{(k-1)}$.
- A flavor current gives a semi-chiral $\mathbf J$ with $\bar\partial\mathbf J=0$; the
  $R$-symmetry gives a pair $\mathbf S_i$ ($i=1,2$) with $\bar\partial\mathbf S_i=0$ generating
  [[two-virasoro-algebra|$\mathfrak{vir}(2)$]].

## Relations

- Belongs to [[holomorphic-twist]]; the descendants are what carry singular OPE data, accessed
  by the [[holomorphic-lambda-bracket|$\lambda$-brackets]].
- When semi-chirality *fails* (a current is not annihilated by $\mathbf Q$), that failure is an
  anomaly — see [[ac-anomalies-as-central-extensions]].
- The extended-SUSY version deforms to the [[schur-superfield|Schur superfield]] under the
  [[superconformal-deformation-to-voa|superconformal deformation]].

## Where it appears

- Systematized in ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]] as the organizing object of the
  holomorphic-twist framework.
