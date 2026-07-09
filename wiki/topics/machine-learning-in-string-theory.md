---
type: topic
title: Machine learning in string theory
aliases: ["applied AI for strings", "ML for string theory", "AI for string theory", "string data"]
tags: [machine-learning, string-theory, landscape, reinforcement-learning, calabi-yau]
prerequisites: []
created: 2026-07-08
updated: 2026-07-08
---

## Overview

The program of applying **machine learning as a practical tool for string theory**: searching the
landscape, approximating geometric objects, and mining trained models for mathematical structure.
This is distinct from [[physics-for-machine-learning]] (which uses field theory to understand
networks): here networks are the instrument, string theory the object of study. The techniques in
current use are **supervised learning** (regression/classification on string data), **reinforcement
learning and search** (flux vacua, brane models, knots), **physics-informed neural networks** (PDE
solvers, notably numerical Calabi–Yau metrics), and **conjecture generation** (interpreting trained
models into provable statements). The community meets annually at *String Data*, in its tenth edition
in 2026.

A recurring theme, emphasized in [[2607.02905|Halverson 2026]], is that **agentic reasoning models**
now wrap around all of these techniques as a force multiplier — outsourcing the "plumbing" (datasets,
environments, hyperparameters, plots) and lowering the implementation barrier by roughly an order of
magnitude, with the physicist owning correctness.

## Historical development

- **2017** — the field opens: gauge theory / landscape ML (He; Krefl–Seong; Ruehle;
  Carifio–Halverson–Krioukov–Nelson), the last introducing
  [[machine-learning-in-string-theory|conjecture generation]] over an F-theory ensemble.
- **2019** — reinforcement learning set loose on the landscape: deep RL (A3C) on type IIA
  intersecting-D6-brane orientifolds finds consistent, SM-like vacua up to $O(200)\times$ faster than
  random search (Halverson–Nakajima–Ruehle); genetic-algorithm search in parallel.
- **2020** — neural networks take over as the ansatz for **numerical Calabi–Yau metrics**
  (Anderson et al.; Douglas et al.; Jejjala et al.), the current state of the art; RL/rigorous ML on
  knots begins (Gukov et al.).
- **2021** — DeepMind's guided-intuition result: a network points mathematicians to the natural-slope
  invariant, yielding a new knot-signature theorem (Davies et al.).
- **2022** — `cymetric` (Larfors–Lukas–Ruehle–Schneider): Kähler-potential-correction PINNs for CICY
  and Kreuzer–Skarke metrics anywhere in moduli space.
- **2024–2026** — agentic reasoning models (OpenAI o1; DeepSeek R1) enter the workflow; the
  Get Physics Done pipeline; RL/Bayesian optimization applied to SPC4 candidate counterexamples
  (Gukov 2025); several [[neural-network-field-theory|NN-FT]] results produced with AI-assisted
  workflows, surveyed in [[2607.02905|Halverson 2026]].

## Key concepts

- **Agentic AI physicist** — a reasoning model in a think–act–observe loop (context → reason → act on
  an environment through tools → fold observations back), terminating in an artifact (code, plot,
  derivation, draft). Get Physics Done (GPD) is a concrete physics-research instantiation. Warnings:
  plausible $\ne$ correct; verify results (unit tests, limits, dimensions, closed-form cross-checks);
  hallucinated scholarship (require INSPIRE-sourced BibTeX); "you are the physicist."
- **Numerical Calabi–Yau metrics** — no compact full-$SU(3)$-holonomy CY metric is known in closed
  form (Yau's theorem gives existence, not an expression). A PINN models the Kähler potential
  correction $J_{\rm CY}=J_{\rm ref}+\partial\bar\partial\phi_\theta$ (building in Kählerity and fixing
  the class), trained on a Monge–Ampère surrogate loss with Shiffman–Zelditch sampling; this unlocks
  the genuinely metric-dependent quantities (canonically normalized Yukawas, KK modes,
  Hermitian–Yang–Mills connections). Topological/calibrated-geometry data (intersection numbers,
  Hodge numbers, BPS volumes via $\mathrm{Vol}(C)=\int_C J$) come without the metric.
- **NN metric flow / Ricci flow** — training a metric-network induces a flow in the space of metrics
  governed by a metric NTK $\Theta_{ijkl}$; **Ricci flow is the special corner** reached by infinite
  width (frozen kernel), locality (kernel $\propto\delta$), and choosing minus Perelman's functional
  as the loss. CY metric flows succeed precisely because they use feature learning, unlike frozen
  Ricci flow.
- **Reinforcement learning** — an MDP $(\mathcal S,\mathcal A,P,r,\gamma)$ with a policy
  $\pi_\theta(a|s)$; the policy-gradient theorem and log-derivative trick let RL train on
  non-differentiable rewards (black-box scorers, discrete correctness checks). Families: value-based
  (deep $Q$-learning), policy-based (REINFORCE, TRPO), actor-critic (A3C); GRPO post-trains reasoning
  models. RL beats blind search when the problem has *learnable structure*.
- **Conjecture generation** — the data → model → interpret → conjecture → proof loop. Interpretation
  tools: interpretable model classes (linear/logistic regression, decision trees), gradient saliency,
  interpretable-by-design architectures ([[kolmogorov-arnold-network|KANs]], symbolic regression),
  and program search (FunSearch, AlphaEvolve).

## Key results

- **RL on the landscape** — deep RL finds consistent, SM-like type IIA orientifold vacua up to
  $O(200)\times$ faster than random, *rediscovering* human model-building strategies (filler branes
  saturating tadpoles) and *inventing* new ones (Halverson–Nakajima–Ruehle 2019). The consistency
  conditions are RR tadpole cancellation in homology, K-theory constraints, and a special-Lagrangian
  (calibration) SUSY condition; SM-like chirality is fixed by intersection numbers $I_{ab}=\pm3$.
- **Learning to unknot** — UNKNOT recast as braid-word sequence classification; TRPO agents learn to
  *simplify* braid words, producing human-checkable unknotting certificates where random walkers and
  other RL fail (Gukov et al. 2020). The "search hard, verify trivially" certificate pattern is the
  template for rigorously acceptable ML results.
- **SPC4** — RL/Bayesian optimization applied to a family of 3375 candidate counterexample pairs to
  the smooth 4d Poincaré conjecture eliminated all but two, ruling out many proposed counterexamples
  (Gukov 2025). SPC4 itself remains open.
- **Conjecture generation** — a logistic-regression model produced (and Gukov et al. later proved) a
  conjecture for when an $E_6$ sector arises in the F-theory ensemble; DeepMind's network yielded the
  knot-signature/natural-slope theorem $|2\sigma(K)-\mathrm{slope}(K)|\le c\,\mathrm{vol}(K)/\mathrm{inj}(K)^3$;
  unknot-classifying networks spontaneously encode the Jones-polynomial degree.

## Current status

An active, decade-old field, now accelerating as agentic reasoning models lower the cost of
implementation. Numerical CY metrics are state-of-the-art but approximate; verified-numerics
certificates (pairing a network solution with a rigorous existence proof) are a growing but partial
answer to the "wrong local minimum" failure mode. RL and conjecture generation have produced results
mathematicians accept at full rigor via the certificate pattern.

## Open questions

- No compact full-$SU(3)$-holonomy Calabi–Yau metric in closed form; how far can numerical metrics
  and their downstream observables be trusted, and certified?
- Can program-search agents rediscover (or generalize) landscape structures that were painstakingly
  found by hand?
- How reliably can agentic pipelines be made to self-verify (formal/numerical checks in the loop)?
- SPC4 — resolve the two surviving candidate counterexample pairs.

## Related

- [[physics-for-machine-learning]] — the complementary "field theory of networks" direction; both are
  developed in [[2607.02905|Halverson 2026]].
- People: [[jim-halverson]], [[fabian-ruehle]], [[sergei-gukov]].
