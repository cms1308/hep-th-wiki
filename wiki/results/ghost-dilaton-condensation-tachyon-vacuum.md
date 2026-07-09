---
type: result
title: Ghost-dilaton condensation in the closed string tachyon vacuum
aliases: [ghost dilaton condensation, Yang–Zwiebach mechanism]
tags: [string-field-theory, closed-string-tachyon, tachyon-condensation]
status: established
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The bosonic [[closed-string-tachyon-vacuum|closed string tachyon vacuum]] is **not** a tachyon
condensate alone: reaching the vacuum requires the **ghost dilaton** to condense together with the
tachyon. A tachyon-only ansatz cannot solve the equation of motion consistently; the ghost dilaton
(the BRST-nontrivial dilaton mode) must acquire a vacuum expectation value.

## Derivation sketch

- **Level truncation** (Yang–Zwiebach 2005). Truncating the CSFT action and extremizing gives a
  tachyon-only cubic vacuum at $t_*\simeq0.416$, but including the ghost dilaton shifts this to
  $t_*\simeq0.338$ with $d_*\simeq0.49$, and only the dilaton-inclusive extremum is stable/consistent
  as the truncation level increases. The endpoint is a "nothing" state with vanishing cosmological
  constant.
- **Recursive-algebraic confirmation** ([[2603.29926|Kim 2026]]). In the
  [[seam-graded-expansion|seam-graded]] solution restricted to the tachyon component, the linearized
  operator is clean ($M_T(L_*)=2$, no eigenvalue near $1$), yet the grade-1 source overwhelms the
  seed: the convergence ratio
  $$\epsilon_B=\frac{|S_1^T(L_*)|}{|g_T^{(0)}(L_*)|}\simeq2.6\times10^{18},$$
  computed from $S_1^T(L_*)=(2.08\pm0.05)\times10^9$ via three independent continuation methods
  (Padé–Borel, conformal Padé, contour deformation). The tachyon-only expansion diverges — the
  self-consistent vacuum cannot live in the tachyon component alone, matching the requirement that the
  ghost dilaton condense.

## Assumptions

- Bosonic closed string; zero-momentum sector.
- Level truncation / the truncated Fock space is a faithful guide to the full theory (standard SFT
  assumption).
- The recursive confirmation is within the zero-momentum Lorentz-scalar sector; the divergence is of
  the tachyon-only projection, not a proof that the full multi-level expansion converges (that remains
  [[closed-string-tachyon-vacuum-convergence|open]]).

## Status

Established as the standard picture since Yang–Zwiebach 2005, and independently re-confirmed from the
divergence of the tachyon-only recursive expansion in [[2603.29926|Kim 2026]].

## Implications

- Any analytic construction of the [[closed-string-tachyon-vacuum]] must carry the ghost dilaton from
  the start; a tachyon-only truncation is not merely inaccurate but divergent.
- Sets the next target for the [[seam-graded-expansion]]: test whether inter-level cancellations,
  including the ghost dilaton and higher states, bring the convergence ratio below $1$.
