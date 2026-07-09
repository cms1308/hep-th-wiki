---
type: result
title: TTbar-deformed spectrum
aliases: [TTbar spectrum, Burgers equation spectrum, TTbar energy levels]
tags: [ttbar, irrelevant-deformation, 2d-cft, integrability, spectrum]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The finite-size energy levels of a [[ttbar-deformation|$T\bar T$-deformed]] 2d theory are fixed
in closed form by the undeformed levels. On a cylinder of circumference $R$, the deformed energy
$E_n(R,\lambda)$ of a state that is undeformed a primary of momentum $P_n$ obeys an inviscid
Burgers equation in $(R,\lambda)$, solved by
$$E_n(R,\lambda)=\frac{R}{2\lambda}\left(\sqrt{1+\frac{4\lambda E_n^{(0)}}{R}+\frac{4\lambda^2 P_n^2}{R^2}}-1\right),$$
with $E_n^{(0)}$ the undeformed energy and $P_n$ the (undeformed) momentum. The same √ structure
appears at the level of densities in the Hamiltonian formalism,
$\mathcal H=\tfrac{1}{2\lambda}\big(\sqrt{1+4\lambda\mathcal H^{(0)}+4\lambda^2\mathcal P^2}-1\big)$.

## Derivation sketch

$T\bar T$ is defined so that the composite $\det T_{\mu\nu}$ factorizes on energy eigenstates
(the expectation value is a product of one-point functions up to derivative terms). The Hellmann–
Feynman variation of each level under $\lambda$ then closes on the energy and momentum of the same
state, giving a first-order PDE — the Burgers equation — whose characteristics integrate to the √
formula. See [[hamiltonian-flow-deformed-cft]] for the plane / density version.

## Assumptions

- A local, translation-invariant seed theory with a conserved stress tensor so that $\det T$ and
  its factorization are well defined.
- Real $\lambda$ of the sign for which the square root stays real; for the other sign high levels
  become complex (Hagedorn / complex-energy behavior), signalling the loss of a standard local UV.

## Status

Established (Zamolodchikov 2004; Smirnov–Zamolodchikov and Cavaglià–Negro–Szécsényi–Tateo 2016).
It is the canonical solvability statement of the deformation and a prerequisite for the operator
and correlator constructions built on it.

## Implications

Fixes the deformed spectrum, thermodynamics, and (via the S-matrix CDD factor) the deformed
scattering. It underlies the [[hamiltonian-flow-deformed-cft|Hamiltonian flow]] treatment used to
build [[dressed-operator-deformed-cft|dressed]] and [[physical-operator-deformed-cft|physical]]
operators, and the analogous solvable dressing holds for [[jt-bar-deformation|$J\bar T$]].
