---
type: result
title: Undeformed S-algebra in planar N=4 SYM
aliases: [quantum-exact soft algebra for N=4 SYM]
tags: [celestial-holography, soft-theorems, n4-sym, scattering-amplitudes]
status: conjectured
created: 2026-07-06
updated: 2026-07-06
---

## Statement

The IR-finite *hard* amplitudes of planar $\mathcal N=4$ super Yang–Mills, defined by the
all-orders factorization
$$\mathcal A_n=\mathcal A^{\rm soft}_n(\epsilon)\,\mathcal A^{\rm hard}_n,\qquad
\mathcal A^{\rm soft}_n=e^{G_n(\epsilon)},\qquad
\mathcal A^{\rm hard}_n=\mathcal A^{\rm tree}_{n,\rm MHV}\,e^{R_n}\,\mathcal P_n,$$
obey the uncorrected tree-level leading soft theorem and have tree-exact half-collinear
poles at finite 't Hooft coupling. Their conformally soft gluon modes therefore represent
the **undeformed tree-level [[s-algebra]]**,
$[\mathsf S^{p,a}_{\bar m,m},\mathsf S^{q,b}_{\bar n,n}]
=-if^{ab}{}_c\,\mathsf S^{p+q-1,c}_{\bar m+\bar n,m+n}$ — a quantum-exact soft algebra in a
standard, IR-divergent 4d gauge theory ([[2606.08582|Alday–Strominger 2026]]).

## Derivation sketch

1. Split $\log M_n$ into the exponentiated IR divergence, the BDS piece, and the
   dual-conformal [[remainder-function|remainder]] $R_n$; put all IR divergences (and
   loop-level collinear divergences) into $e^{G_n}$.
2. Show $R_n\to R_{n-1}$ smoothly in the soft limit (no additive constant) using the
   [[wilson-loop-ope|Wilson-loop OPE]]: soft is a degenerate endpoint of collinear, and
   absence of endpoint growth of the flux-tube Fourier integrals prevents enhancement.
3. Half-collinear nonrenormalization: each flux-tube exchange contributes
   $\bigl(\frac{\bar z_{s2}}{z_{s2}}\bigr)^{m/2}\bigl(\omega_s^{1/2}|z_{s2}|\bigr)^{E_k(0)f(\eta)}$-type
   corrections, and $E_k(0)-|m|>0$ strictly at finite coupling (Basso's GKP spectrum), so
   perturbative logs essentially resum to nonnegative powers $(p_1\cdot p_2)^c$ — the
   leading pole, i.e. the celestial OPE coefficient, is tree-exact.
4. Mellin-transform: the tree-exact holomorphic pole gives the tree-level celestial OPE and
   hence the undeformed algebra of soft insertions; the *divergent* Bern–Davies–Nohle
   one-loop subleading soft correction of the full amplitude is reproduced by
   $S^{(1)}_{\rm full}=e^{G_n}S^{(1)}_{\rm hard}e^{-G_{n-1}}$.

## Assumptions

Planar limit; Assumptions 1–4 of the paper: [[amplitude-wilson-loop-duality]]
(Assumption 1; dual superconformal symmetry as Assumption 1′), universal collinear
factorization, BDS exponentiation of the splitting function, and uniform convergence of
the Wilson-loop OPE in the Euclidean region. The
half-collinear limit requires complexified momenta or Klein space. The special-conformal
route to the tower ([[2601.00096|Sheta et al. 2025]]) is unavailable in flat space —
special conformal transformations are anomalous — so the argument is amplitude-level.

## Status

**Conjectured/argued**: rests on the stated (standard but unproven) assumptions; the
smooth soft limit is verified explicitly on the two-loop hexagon remainder and at one loop
for NMHV ratio functions. Evidence for an uncorrected quantum $S$-algebra in a standard,
IR-divergent flat-space 4d gauge theory — it had been speculated that an uncorrected
quantum $S$-algebra could exist only in twistorial theories without IR divergences (the
AdS$_4$/CFT$_3$ realization being the other known non-twistorial case).

## Implications

- IR-finite observables of a confining-free, interacting 4d gauge theory carry the full
  celestial symmetry tower: a milestone for making [[celestial-holography]] quantum-exact.
- The flat-space counterpart of the AdS$_4$/CFT$_3$ statement
  ([[ads4-s-algebra-from-cft3-light-transforms]]); answers (affirmatively, for hard
  amplitudes) the question raised in [[2601.00096|Sheta et al. 2025]] of whether the
  $S$-algebra acts on IR-finite $\mathcal N=4$ observables.
- Loop corrections to soft-theorem *operators* are constrained by $S$-algebra
  integrability conditions; the leading-log corrections are computed to all orders
  (Narayana polynomials).

Source: [[2606.08582|Alday–Strominger 2026]].
