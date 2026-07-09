---
type: concept
title: Electric and magnetic Carrollian theories
aliases: [electric Carroll limit, magnetic Carroll limit, Carrollian contractions]
tags: [carrollian-physics, field-theory, contractions]
prerequisites: ["carroll-group"]
created: 2026-07-03
updated: 2026-07-03
---

## Definition

Every relativistic field theory admits (at least) two inequivalent Carrollian ($c\to0$)
contractions, named by analogy with the electric/magnetic limits of Maxwell theory:

- **Electric limit**: rescale fields to keep the kinetic (time-derivative) term; only
  $\dot\phi$ survives. Ultra-local dynamics, no spatial gradients.
- **Magnetic limit**: no rescaling; spatial gradients survive, time derivatives appear only
  through a constraint. The theory is secretly a *Euclidean* theory in one lower dimension.

## Motivation

The dichotomy is the organizing principle of Carrollian field theory and reappears in the
holographic correlators of [[carrollian-cft]]s, whose Ward identities are solved by a
time-independent *magnetic branch* (lower-dimensional CFT correlators) and distributional
*electric branches* ($\propto\delta^{(2)}(z_{ij})$) — the branch actually populated by
[[carrollian-amplitude|Carrollian amplitudes]]. In the
[[flat-carrollian-limit-correspondence|flat limit of AdS/CFT]] the electric branch carries
the $\mathcal S$-matrix.

## Key formulas

Hamiltonian form makes the two limits transparent (scalar field,
[[2602.02644|Ruzziconi 2026]] §5):

$$S_H = \int \Big[\pi\dot\phi - \tfrac12\partial_A\phi\,\partial^A\phi
- \tfrac{c^2}{2}\pi^2\Big]$$

- **Magnetic** ($c\to0$ directly): $S^M = \int[\pi\dot\phi - \tfrac12(\partial\phi)^2]$;
  $\pi$ is a Lagrange multiplier enforcing $\dot\phi=0$ — correlators are time-independent,
  those of a Euclidean CFT one dimension down.
- **Electric** ($\phi\to c\phi$, $\pi\to\pi/c$, then $c\to0$): $S^E = \tfrac12\int\dot\phi^2$
  — pure ultra-local kinetic term.

Same pattern for Maxwell, Yang–Mills ($g\to g/c$ in the electric limit — couplings must be
scaled along with fields), and ADM gravity: the electric limit of gravity is Henneaux's 1979
zero-signature/strong-coupling limit, relevant to BKL dynamics.

**Quantization obstruction** ([[carrollian-quantization-obstruction]],
[[2407.11971|Cotler et al. 2024]]): lattice-regularized electric theories have flat-band
dispersion $E^2 = m^2$, exhibit UV/IR mixing, and after renormalization all connected
higher-point functions vanish — generalized free fields. Magnetic theories quantize to
time-independent lower-dimensional correlators. Neither gives the interacting,
time-dependent correlators flat holography needs; [[2602.02644|Ruzziconi 2026]] argues $c$
itself may be the correct regulator (define the theory as a limit of the relativistic one).

## Relations

- Realizations of the [[carroll-group]] on fields; contrast the single Galilean limit.
- Branch structure of [[carrollian-cft]] correlators mirrors the dichotomy.
- Related exotica: Carrollian fermions, swiftons (interacting Carroll theories with
  propagating modes), tensionless strings.

## Where it appears

[[2602.02644|Ruzziconi 2026]] §5; [[2109.06708|Henneaux–Salgado-Rebolledo 2021]],
[[2110.02319|de Boer et al. 2021]] (systematic constructions); Duval et al. 2014
(electric/magnetic terminology).
