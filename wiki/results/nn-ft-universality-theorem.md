---
type: result
title: Universality of NN-FT
aliases: ["NN-FT universality theorem", "universality of neural network field theory"]
tags: [machine-learning, neural-networks, nn-ft, constructive-qft]
status: proven
created: 2026-07-08
updated: 2026-07-08
---

## Statement

Any probability distribution over tempered distributions on $\mathbb R^d$ — in particular any
Euclidean QFT in the constructive sense, whether or not the Osterwalder–Schrader axioms hold — admits
a [[neural-network-field-theory|NN-FT]] description $(\phi_\theta,P(\theta))$ with countably many
parameters. Established in Ferko et al. 2026, presented in [[2607.02905|Halverson 2026]].

## Derivation sketch

A field theory in constructive QFT is a probability distribution $P_\phi$ over field configurations
in $\mathcal S'(\mathbb R^d)$: typical configurations in $d\ge2$ are not functions but tempered
Schwartz distributions, because keeping the kinetic term finite in the continuum limit forces the
roughness $\phi(x+an)-\phi(x)\sim a^{1-d/2}$.

An NN-FT is "two probability spaces and one map": a parameter density $P$ on $\mathbb R^{\mathbb N}$,
the field-configuration density $P_\phi$ on $\mathcal S'(\mathbb R^d)$, and the architecture
$\phi_\theta$ pushing one forward to the other, $(\phi_\theta)_*P=P_\phi$. The universality question is
whether every $P_\phi$ is realized this way.

It is, for a clean reason: both $\mathbb R^{\mathbb N}$ and $\mathcal S'(\mathbb R^d)$ are **standard
Borel spaces**, and the **Borel isomorphism theorem** guarantees a Borel isomorphism
$\phi_\theta:\mathbb R^{\mathbb N}\xrightarrow{\sim}\mathcal S'(\mathbb R^d)$ between any two such
spaces. Given a target $P_\phi$, take $P$ to be its pullback; one may take the architecture to be the
Borel isomorphism itself. The guaranteed architecture is **one-to-one** between parameters and
functions — the case where the neurons form a basis $\varphi_i$ of the function space.

## Assumptions

- The field theory is specified as a probability distribution over $\mathcal S'(\mathbb R^d)$
  (constructive-QFT setting); scalar theories are the case made precise.
- Countably many parameters are allowed; the theorem is an existence statement, silent on whether the
  isomorphism-architecture is a *practical* or *local* network.

## Status

Proven (Borel isomorphism theorem). It is the NN-FT analogue of the
[[universal-approximation-theorem|universal approximation theorem]]: an existence result about what
*can* be represented, not a construction with good properties.

## Implications

- Frames every subsequent NN-FT example ([[liouville-from-neural-networks|Liouville]],
  [[string-amplitudes-from-neural-networks|the bosonic string]],
  [[topological-sectors-nn-ft|BKT]]) as realizing a theory the theorem already guarantees exists.
- Shifts the open problem from "which theories are NN-FTs?" (answer: all of them) to *engineering* —
  building architectures whose ensembles are local, reflection-positive, and cluster-decomposing
  (see [[neural-network-field-theory]] open questions).

## References

- [[2607.02905|Halverson 2026]] §Day 2 (Universality); Ferko et al. 2026.
