---
type: concept
title: Neural network field theory (NN-FT / NN-QFT)
aliases: ["NN-FT", "NN-QFT", "neural network field theory", "neural network quantum field theory"]
tags: [machine-learning, neural-networks, field-theory, osterwalder-schrader]
prerequisites: [physics-for-machine-learning, neural-network-gaussian-process]
created: 2026-07-07
updated: 2026-07-08
---

## Definition

Defining a **field theory directly from a neural-network ensemble**. Taking "field theory = an
ensemble of functions with computable correlators," the pair $(\phi_\theta,P(\theta))$ — a network
architecture together with its parameter distribution — *is* a Euclidean field theory, with
correlators

$$G^{(n)}(x_1,\dots,x_n)=\big\langle\phi_\theta(x_1)\cdots\phi_\theta(x_n)\big\rangle_{\theta\sim P}.$$

If the ensemble additionally satisfies the **Osterwalder–Schrader axioms** (Euclidean invariance,
permutation invariance, reflection positivity, cluster decomposition), it defines a genuine
**quantum** field theory (NN-QFT) with a Lorentzian continuation.

## Motivation

It inverts the [[physics-for-machine-learning|NN field-theory]] dictionary: instead of asking what
field theory a given network realizes, it uses networks as a *constructive* handle on field theories
— free fields at infinite width, interactions by controlled deformation. The infinite-width network
is a free field ([[neural-network-gaussian-process|NNGP]]); interactions come from the two knobs
$1/N$ and broken statistical independence.

## Key formulas

Inserting a local potential into a free (NNGP) partition function builds an interacting theory:

$$Z[J]=\int d\theta\,P(\theta)\,e^{\int d^dx\,V(\phi_\theta)}\,e^{\int J\phi_\theta}
=\int d\theta\,\tilde P(\theta)\,e^{\int J\phi_\theta},$$

so **interactions = broken statistical independence** encoded in the deformed density
$\tilde P(\theta)$. Worked examples:

- **Scalar-net** reproduces the free scalar propagator $G^{(2)}(p)=1/(p^2+m^2)$;
- adding $V=\phi^4$ to the Scalar-net builds **$\phi^4$ theory** inside an ensemble of
  infinite-width networks;
- **Cos-net** is Euclidean-invariant at all $N$, via input layers such as
  $\ell_i(x)=F(\mathbf w^{(0)}_i)\cos(w^{(0)}_{ij}x_j+b^{(0)}_i)$ with $b\sim\mathrm{Unif}[-\pi,\pi]$.

## Relations

- Free limit is the [[neural-network-gaussian-process|NNGP correspondence]]; the free action is the
  inverted kernel $S[\phi]=\int\phi\,G^{(2)-1}\phi$.
- Global symmetries follow from an invariant $P(\theta)$ (e.g. even $P(w)\Rightarrow\mathbb Z_2$,
  killing odd correlators).
- Realizes [[phi4-from-neural-networks|$\phi^4$ theory]] by potential insertion.
- Symmetries, conservation laws, and anomalies come from a change of variables in the parameter
  integral — the [[parameter-space-ward-identities|score/breaking-function formalism]].
- Discrete latent parameters add [[topological-sectors-nn-ft|topological sectors]] (vortices,
  winding) that no continuous Gaussian ensemble can reach.
- Belongs to the [[physics-for-machine-learning]] topic.

## Recent results (2024–2026)

The framework has been carried well beyond $\phi^4$, surveyed in [[2607.02905|Halverson 2026]]:

- **[[nn-ft-universality-theorem|Universality]]** — every distribution over tempered distributions
  (hence any constructive Euclidean QFT) is an NN-FT, by the Borel isomorphism theorem.
- **[[liouville-from-neural-networks|Liouville theory]]** — an interacting irrational-$c$ 2d CFT
  realized by conditioning the zero mode via Gaussian multiplicative chaos; parameter-space Monte
  Carlo matches the DOZZ structure constant to the percent level.
- **[[string-amplitudes-from-neural-networks|The bosonic string]]** — the gauge-fixed worldsheet boson
  (random Fourier features) plus $bc$ ghosts (Grassmann-valued output weights) give the
  Virasoro–Shapiro and Veneziano amplitudes as analytic parameter integrals.
- **[[critical-dimension-from-mode-counting-nn-ft|$D=26$]]** — Weyl invariance of the string ensemble,
  via the parameter-space anomaly, is a zeta-regularized mode count.
- **[[topological-sectors-nn-ft|Topological sectors / BKT]]** — discrete latents reproduce the full
  BKT transition of the 2d XY model.
- Also: conformal symmetry, defect CFTs, worldsheet Virasoro, fermions/SUSY (Grassmann networks), and
  RG flow — the growing "for-physics" direction.

## Where it appears

- Developed by Halverson–Maiti–Stoner (2021) and Halverson (2021), with the Osterwalder–Schrader
  axioms (1973) as the continuation criterion; independence-breaking and NN actions systematized in
  Demirtas et al. (2023).
- The synthesis pillar of [[2408.00082|Halverson 2024]] and the central framework of Day 2 of
  [[2607.02905|Halverson 2026]].
