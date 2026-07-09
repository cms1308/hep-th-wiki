---
type: topic
title: Physics for Machine Learning
aliases: ["physics of machine learning", "field theory of neural networks", "ML theory for physicists"]
tags: [machine-learning, neural-networks, field-theory, nn-ft]
prerequisites: []
created: 2026-07-07
updated: 2026-07-08
---

## Overview

The program of using **theoretical-physics tools — field theory, ensemble statistics, symmetry,
large-$N$ expansions, gradient dynamics — to understand neural networks**. The organizing
observation is that a randomly initialized network is not one function but an *ensemble* of
functions $\phi_\theta$ drawn from a parameter distribution $P(\theta)$, so the objects a network
"predicts" are statistical expectations — correlation functions
$G^{(n)}(x_1,\dots,x_n)=\langle\phi(x_1)\cdots\phi(x_n)\rangle$. That makes an ensemble of networks a
**Euclidean field theory**, computable in two dual ways:

- **parameter space** — $Z[J]=\int d\theta\,P(\theta)\,e^{\int J\phi_\theta}$, always available from
  network data;
- **function space** — $Z[J]=\int\mathcal D\phi\,e^{-S[\phi]+\int J\phi}$, the usual path integral.

The lectures [[2408.00082|Halverson 2024]] organize the subject into three pillars — **expressivity**
(what a network can represent), **statistics** (the ensemble at initialization), and **dynamics**
(evolution under gradient descent) — and then invert the whole picture into an
[[neural-network-field-theory|NN-FT correspondence]] that *defines* field theories from network
ensembles.

This is the vault's first non-holography area. It shares with the rest of the wiki the machinery of
large-$N$ expansions, path integrals, and Osterwalder–Schrader reconstruction, but the physical
objects are neural networks, not gravity. The complementary direction — using ML as a *tool* for
string theory rather than field theory as a lens on networks — is [[machine-learning-in-string-theory]].

## Historical development

- **1957** — Kolmogorov–Arnold representation theorem: any multivariate continuous function is an
  exact superposition of univariate functions and addition. Later the seed of the
  [[kolmogorov-arnold-network|KAN]] architecture.
- **1989–1991** — [[universal-approximation-theorem|universal approximation]]: single-hidden-layer
  networks approximate any continuous function on a compact set (Cybenko; Hornik).
- **1996–1997** — [[nngp-correspondence|NN/Gaussian-process correspondence]]: infinite-width
  single-layer networks are Gaussian processes (Neal), with explicit kernels (Williams). The
  statistics pillar's foundational result.
- **2018–2019** — [[neural-tangent-kernel|neural tangent kernel]]: gradient-descent training of very
  wide networks linearizes and becomes exactly solvable kernel regression (Jacot–Gabriel–Hongler;
  Lee et al.). The dynamics pillar begins.
- **2020–2022** — finite-width / non-Gaussian corrections as an effective field theory (Yaida;
  Roberts–Yaida–Hanin), and [[feature-learning|feature learning]] via
  [[maximal-update-parameterization|$\mu P$]] and dynamical mean-field theory (Yang;
  Bordelon–Pehlevan).
- **2021–2023** — [[neural-network-field-theory|NN-FT / NN-QFT correspondence]]: defining Euclidean
  (and, via Osterwalder–Schrader, quantum) field theories directly from network ensembles, including
  $\phi^4$ built by potential insertion (Halverson–Maiti–Stoner; Demirtas et al.).
- **2024** — [[2408.00082|Halverson's TASI lectures]] synthesize the three pillars and the NN-FT
  inversion for a hep-th audience.
- **2024–2026** — the NN-FT "for-physics" direction expands rapidly: conformal symmetry, defect CFTs,
  worldsheet Virasoro, fermions/SUSY (Grassmann networks), RG flow, and the flagship results of
  [[2607.02905|Halverson's Pre-Strings lectures]] — [[nn-ft-universality-theorem|universality]],
  [[liouville-from-neural-networks|Liouville]],
  [[string-amplitudes-from-neural-networks|string amplitudes]],
  [[topological-sectors-nn-ft|topological sectors / BKT]],
  [[parameter-space-ward-identities|parameter-space anomalies]], and
  [[critical-dimension-from-mode-counting-nn-ft|$D=26$ from mode counting]].

## Key concepts

- [[neural-network-gaussian-process]] — infinite-width networks as generalized free fields.
- [[neural-tangent-kernel]] — the kernel governing gradient-descent dynamics.
- [[feature-learning]] vs the lazy/NTK regime.
- [[maximal-update-parameterization]] — the scaling in which wide networks learn features.
- [[neural-network-field-theory]] — defining field theories from network ensembles.
- [[kolmogorov-arnold-network]] — interpretable edge-activation architecture.
- [[universal-approximation-theorem]] — the expressivity baseline.

## Key results

- [[nngp-correspondence]] — width-$N$ network → Gaussian process (established).
- The frozen-NTK equivalence to kernel regression, and the $\mu P$ scaling constraints for feature
  learning (see [[neural-tangent-kernel]], [[maximal-update-parameterization]]).
- $\phi^4$ and free-scalar field theories realized inside network ensembles (see
  [[neural-network-field-theory]]).

## Current status

An active, physics-flavored corner of ML theory. The statistics and dynamics pillars have
firm large-$N$ results; the NN-FT direction is younger and more open — engineering ensembles that
satisfy the full Osterwalder–Schrader axioms (reflection positivity, cluster decomposition, locality
at finite $N$) is not yet systematic.

## Open questions

- Systematic construction of NN-FTs satisfying reflection positivity and cluster decomposition.
- Building an NN-FT with a prescribed action; realizing locality at finite $N$.
- A unifying theory of statistics + dynamics + architecture (why Transformers work).
- Whether NN-FTs yield genuinely new physics, and whether a theory of sparse networks lets small
  models rival large LLMs.
