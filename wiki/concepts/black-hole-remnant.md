---
type: concept
title: Black Hole Remnant
aliases: [remnant, Planck-scale remnant, cornucopion]
tags: [black-holes, entropy, information-paradox, quantum-gravity]
prerequisites: [black-hole-thermodynamics]
created: 2026-07-06
updated: 2026-07-06
---

## Definition

A hypothetical end-state of black hole evaporation: instead of evaporating away completely,
a black hole is proposed to stop shrinking at the Planck mass/size and retain, internally, all
of the information that ever fell in. For remnants "to keep track of all the possible states
that can form an arbitrarily large black hole, the number of distinct species of remnant must
be infinite" — equivalently, from the point of view of entropy, black holes carry an infinite
additional internal entropy $S_R$ above Bekenstein-Hawking, "mass independent if it is not to
modify black hole thermodynamics" ([[hep-th-9501106|Susskind 1995]]). Proposed by Aharonov-Casher-Nussinov
(Phys. Lett. B191 (1987) 51) as a resolution of the [[black-hole-information-paradox]].

Variants (Banks-O'Laughlin-Strominger, Phys. Rev. D47 (1993) 4476) let the remnant look small
from the outside while its interior expands to some enormous size ("cornucopions"),
combined with a proposed mechanism suppressing the *rate* at which such remnants are produced.

## Motivation

Remnants look like an attractive resolution of the information paradox: unitarity is restored
because no information is destroyed, only hidden. The question this concept exists to record
is why this resolution is widely considered pathological rather than viable.

## Key formulas

[[hep-th-9501106|Susskind 1995]]'s thermodynamic argument (not a pair-production-rate
argument, in contrast to earlier objections):

- Import the [[susskind-uglum-low-energy-theorem]]: the entropy of Rindler space, for any
  field content, is exactly reproduced by the renormalized Newton constant,
  $$S/A = 1/(4G).$$
  Any species contributing to $G$'s renormalization must contribute to this entropy in
  lockstep — a statement about the true thermal-equilibrium state (Unruh density matrix
  $\rho_u = e^{-2\pi H_r}/Z$), independent of production dynamics.
- A Planck-mass remnant species is thermally populated in the Rindler wedge at proper distance
  $\rho$ with density $N_i \sim \exp(-2\pi\rho M_p)$ (local Unruh temperature
  $T(\rho)=1/2\pi\rho$). Summing $e^{S_R}$ degenerate species: $N_R \sim \exp[S_R - 2\pi\rho
  M_p]$.
- Demanding this not exceed close-packing forces remnants to saturate out to
  $\rho = S_R/M_p$, giving an entropy per unit area $S/A \sim S_R^2 M_p^2$ — divergent as
  $S_R\to\infty$, which it must be to store information from arbitrarily large black holes.
- Contradiction: the low-energy theorem fixes $S/A=1/(4G)$ exactly with $G$ assumed finite, so
  the divergence forces $1/G\to\infty$, i.e. $G\to0$ — "I can see no way to avoid this without
  giving up remnants."
- Ordinary (non-remnant) black holes do *not* cause this problem: their probability of
  appearing in the thermal atmosphere at distance $\rho$, $P=\exp[-2\pi\rho M+4\pi M^2G]$
  subject to $2MG<\rho$, is dominated by $M=M_p$ and stays exponentially suppressed —
  "black holes are exponentially suppressed in the thermal atmosphere even though their
  entropy is enormous. Remnants, by contrast, would overrun the system": black hole entropy
  grows with mass, while $S_R$ is mass-independent and unbounded.

Two defenses are explicitly neutralized in [[hep-th-9501106|Susskind 1995]]: suppressing
the remnant *production rate* ("it does not matter what mechanisms may or may not exist to
quickly bring these particles to equilibrium" — the theorem relates $G$ to the exact
equilibrium entropy) and cornucopion-style hidden interiors ("for our purposes it is only
important that when seen from outside, the remnant is small").

## Relations

- Cited as the standard "same problems" reference by
  [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]] when motivating the
  [[weak-gravity-conjecture]]: an effectively global $U(1)$ ($g\to0$) lets black holes carry
  arbitrary hidden charge with no light state to radiate it away, leaving the same kind of
  unbounded-degeneracy Planck-scale remnants that [[hep-th-9501106|Susskind 1995]] argues are
  thermodynamically inconsistent.
  > [!warning] Sourcing gap
  > [[hep-th-9501106|Susskind 1995]] itself never discusses global or gauge symmetry — the
  > word "symmetry" does not appear in the paper. The remnant-entropy argument and the
  > global-symmetry argument are logically distinct; AMNV link them by analogy (both produce
  > pathological unbounded degeneracy), not by a shared derivation. A page asserting the
  > direct quantum-gravity-forbids-global-symmetries argument
  > ([[no-global-symmetries-in-quantum-gravity]]) needs an additional primary source (e.g.
  > wormhole-induced global-charge non-conservation, Giddings-Strominger 1988) before that
  > connection is stated as proven rather than heuristic.
- Distinct from ordinary black hole endpoints: an evaporating black hole *without* a remnant
  either radiates all information away (unitary, but requires late-time correlations
  Hawking's original calculation missed) or genuinely destroys it (non-unitary) — remnants are
  the third option this concept's pathology argument rules out.

## Where it appears

- [[hep-th-9501106|Susskind 1995]] — the thermodynamic inconsistency argument (main content of
  this page).
- [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]] — invokes the remnant pathology as
  motivation for the [[weak-gravity-conjecture]].
</content>
