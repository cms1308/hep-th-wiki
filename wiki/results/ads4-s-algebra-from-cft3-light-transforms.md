---
type: result
title: S-algebra in AdS4 from CFT3 light-ray operators
aliases: [soft algebras in AdS4]
tags: [celestial-holography, ads-cft, light-ray-operators, soft-theorems]
status: established
created: 2026-07-06
updated: 2026-07-06
---

## Statement

In any CFT$_3$ with a nonabelian conserved global symmetry current $J^a_i$ (in particular
the boundary dual of an unconfined bulk gauge theory in AdS$_4$), the light transform of the
current
along antipodally-terminating null geodesics of the [[einstein-cylinder]] EC$^3$,
$$\mathcal L^a(\phi)=\int_0^\pi dt^+\,\sin t^+\,J^a_+(t^+,t^-{=}0,\phi),$$
together with its $SO(3,2)$ conformal descendants
$\mathcal L^{p,a}_{\bar m,m}$, generates the complete [[s-algebra]]:
$$\bigl[\mathcal L^{p,a}_{\bar m,m},\,\mathcal L^{q,b}_{\bar n,n}\bigr]
=-\frac{i}{2\pi}f^{abc}\,\mathcal L^{p+q-1,c}_{\bar m+\bar n,\,m+n}.$$
Under the conformal embedding of $M^4$ and AdS$_4$ into the shared Einstein cylinder (with
$i^0$ placed in $\partial\mathrm{AdS}_4$), these light-ray operators are the images of the
linearly polarized combinations
$\mathcal L^{p,a}_{\bar n,m}=\tfrac{1}{4\pi}(S^{p,a}_{\bar n,m}+\bar S^{p,a}_{-\bar m,-n})$
of the flat-space soft gluon generators, satisfying an isomorphic algebra — soft algebras
exist in AdS$_4$, undeformed ([[2601.00096|Sheta–Strominger–Tropper–Wei 2025]]).

## Derivation sketch

1. In flat space, define the subleading soft tower as special-conformal descendants of the
   leading soft generator; $SO(4,2)$ plus the leading soft theorem imply the full
   $S$-algebra via Jacobi identities.
2. Map $M^4$ and AdS$_4$ into EC$^4$; a family of null generators of $\mathscr I^+$ lies in
   both $\mathscr I^+$ and $\partial\mathrm{AdS}_4$.
3. Dirichlet boundary conditions ($n\wedge F^a|_\partial=0$) reflect helicity, so only the
   linearly polarized combinations
   $T^{p,a}_{\bar n,m}\propto S^{p,a}_{\bar n,m}+\bar S^{p,a}_{-\bar m,-n}$ (note the
   reflected indices) survive at the boundary; they satisfy an isomorphic algebra.
4. The surviving leading generator equals $2\pi\times$ the light transform of the boundary
   current; its commutator is the Córdova–Shao current algebra
   $[\mathcal L^a(\phi_1),\mathcal L^b(\phi_2)]=-if^{abc}\delta(\phi_{12})\mathcal L^c$,
   computed purely in CFT$_3$; descendants close the full tower.

## Assumptions

Conformally invariant bulk gauge theory (undeformed leading soft theorem); standard
Dirichlet boundary conditions; the CFT$_3$ has the corresponding conserved current. "Soft"
means boost weight, not global energy — hence no conflict with the AdS energy gap.

## Status

**Established** at the leading ($p=1$) level, where the commutator is the Córdova–Shao
current algebra, valid in any CFT$_3$. For the full tower the paper is more guarded: the
light-ray $S$-algebras appearing in the conformal map to AdS are "potentially well-defined
at the quantum level".

## Implications

- A direct bridge between the holographic symmetry algebras of flat space
  ([[celestial-holography]]) and AdS$_4$/CFT$_3$ ([[ads-cft-correspondence]]); could
  enable importing CFT light-ray technology into flat holography.
- Template for gravity: the [[lambda-deformed-w-algebra]] from ANEC descendants
  ([[every-cft3-has-l-lambda-w-symmetry]]).
- Motivated the planar $\mathcal N=4$ analysis ([[undeformed-s-algebra-planar-n4-sym]]),
  where the special-conformal route fails due to the anomaly.

Source: [[2601.00096|Sheta–Strominger–Tropper–Wei 2025]].
