---
type: result
title: Flat space limit = boundary Carrollian limit
aliases: [flat/Carrollian correspondence, c = 1/ell correspondence]
tags: [flat-space-holography, ads-cft, carrollian-physics]
status: established
created: 2026-07-03
updated: 2026-07-03
---

## Statement

The flat-space limit $\ell\to\infty$ of the AdS bulk is implemented on the boundary CFT as a
Carrollian limit $c\to0$, with the identification

$$c_{\text{boundary}} \equiv \ell^{-1}_{\text{bulk}} .$$

In Bondi coordinates, $ds^2_{\text{AdS}_4} = -\tfrac{r^2}{\ell^2}du^2 - 2dudr + 2r^2dzd\bar z$
induces the boundary metric $ds^2_\partial = -\tfrac{1}{\ell^2}du^2 + 2dzd\bar z$, which
degenerates to the flat Carroll structure as $\ell\to\infty$. The diagram commutes at the
level of observables: flat limits of holographic correlators are
[[carrollian-amplitude|Carrollian amplitudes]] of the flat bulk theory. Consequently,
[[flat-space-holography]] arises as a controlled limiting procedure applied to *both sides*
of the [[ads-cft-correspondence]] rather than an independent conjecture.

## Derivation sketch

Verified two independent ways that agree diagram by diagram
([[flat-space-limit-of-witten-diagrams]]):

1. AdS propagators → flat propagators; each Witten diagram limits, in position space, to the
   corresponding Feynman diagram at $\mathscr I$ computing a Carrollian amplitude.
2. Intrinsically in the CFT: analytic continuation, restore $c$, electric scaling
   $\Phi_\Delta \sim c^{\Delta-1}\mathcal O_\Delta$, extract the leading electric branch —
   the $\delta^{(2)}(z_{ij})$ support arising from the bulk-point singularity of
   $\bar D$-functions at $Z\to\bar Z$. The branch-splitting mechanism on a 2-point function:
   $$\frac{\mathcal N_2}{(-c^2u_{12}^2 + 2|z_{12}|^2+i\varepsilon)^\Delta}
   \xrightarrow{c\to0} c^0(\text{magnetic, 2d CFT}) + c^{2-2\Delta}(\text{electric,}
   \;\propto\delta^{(2)}(z_{12})) .$$

## Assumptions

Massless bulk states; tree level; verified at 2-, 3-, 4-point (contact and exchange) in
AdS$_4$/CFT$_3$; equivalence of extrapolate and GKP/W dictionaries established via the
Arefeva–Faddeev–Slavnov path integral.

## Status

**Established** at the level checked (tree-level massless correlators, AdS$_4$), including a
top-down realization: [[carrollian-abjm-correspondence]] (Carrollian limit of ABJM half-BPS
correlators = 11d supergravity Carrollian amplitudes with kinematics restricted to
$\mathbb R^{1,3}$, [[2504.10291|Lipstein et al. 2025]]). Loops, massive states, and the
$S^7$ decompactification ([[internal-space-decompactification]]) remain open.

## Implications

- Flat holography inherits AdS/CFT's credibility: the dual of flat space can be *derived*
  as a limit, giving a working definition while
  [[intrinsic-definition-of-carrollian-cft|an intrinsic one]] is lacking.
- Explains the branch structure of [[carrollian-cft]] correlators from the bulk.
- Sources: [[2406.19343|Alday–Nocchi–Ruzziconi–Yelleshpur Srikant 2024]];
  reviewed in [[2602.02644|Ruzziconi 2026]] §9.
