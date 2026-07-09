---
type: topic
title: Swampland program
aliases: [swampland]
tags: [swampland, quantum-gravity, string-landscape]
prerequisites: []
created: 2026-07-04
updated: 2026-07-08
---

## Overview

The program of characterizing which low-energy effective field theories can arise from a
consistent theory of quantum gravity (the *landscape*) and which, despite looking
consistent to an effective field theorist, cannot (the *swampland*). Swampland criteria
are conjectured necessary conditions for a quantum-gravity completion; the string
landscape supplies both the motivating examples and the testing ground.

## Historical development

- Vafa 2005 ([hep-th/0509212](https://arxiv.org/abs/hep-th/0509212)) coined the swampland
  and proposed the first criteria — finiteness properties such as the number of massless
  fields and the volume of moduli space (as summarized in
  [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]).
- [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]] added the
  [[weak-gravity-conjecture|Weak Gravity Conjecture]]: gravity is the weakest force —
  sub-extremal charged states must exist so extremal black holes can decay, with the
  corollary cutoff $\Lambda \lesssim g M_{\rm Pl}$ on any effective $U(1)$ theory. This
  turned the folklore ban on global symmetries
  ([[no-global-symmetries-in-quantum-gravity]]) into a quantitative bound obstructing the
  $g \to 0$ limit.
- The AdS/CFT translation of the WGC — posed as an open direction already in
  [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]] — was formulated as a concrete
  spectral bound by Nakayama-Nomura 2015
  ([1509.01647](https://arxiv.org/abs/1509.01647), [[nakayama-nomura-wgc-bound]]) and
  corrected to the anomaly combination $3c-2a$ by
  [[2308.01717|Cho-Choi-Lee-Song 2023]] ([[modified-ads-wgc-3c-2a]]), then validated
  across the simple-gauge-group SCFT landscape by [[2510.19136|Cho-Lee-Song 2025]].
- A wormhole-based line of 2026 recasts the WGC as a bound on *imaginary* continuation of
  couplings: [[2605.05336|Maldacena-Maloney-McPeak 2026]] introduced the
  [[imaginary-distance-bound|imaginary distance bound]] from
  [[euclidean-axion-wormhole|Euclidean scalar wormholes]], unifying the WGC with the
  [[kontsevich-segal-witten-criterion|Kontsevich-Segal-Witten criterion]]; the companion
  [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] derived the sharp axionic WGC (fixed
  $\mathcal O(1)$ coefficient) from
  [[gravitational-path-integral-positivity|positivity of the gravitational path integral]].
- In the sharply constrained 6d $\mathcal N=(1,0)$ arena, non-perturbative BPS-string data
  refine the landscape/swampland split: [[2607.05496|Hamada-Jeon-Kim 2026]] build 6d
  supergravities from [[supergravity-block|supergravity blocks]] respecting anomaly
  cancellation and the $H$-string constraints, and classify the non-Higgsable ones — see
  the dedicated topic [[6d-supergravity-swampland]].

## Key concepts

- [[weak-gravity-conjecture]] — the flagship criterion; electric, magnetic/cutoff, and
  sharp (I)/(II)/(III) forms.
- [[no-global-symmetries-in-quantum-gravity]] — the folklore principle the WGC
  quantifies.
- Axionic bound $S_{\rm inst} \lesssim M_{\rm Pl}/F$ — obstruction to parametrically
  super-Planckian decay constants, constraining [[extranatural-inflation]]-type models
  ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]).
- [[imaginary-distance-bound]] — limit on imaginary continuation of couplings from
  [[euclidean-axion-wormhole|wormholes]]; generalizes the
  [[kontsevich-segal-witten-criterion|KSW criterion]] and contains the WGC.
- [[gravitational-path-integral-positivity]] — positivity of universe-state inner products as a
  swampland consistency condition.

## Key results

- [[modified-ads-wgc-3c-2a]] — the current best universal AdS-WGC candidate,
  $\Delta^2/q^2 \le 12(3c-2a)/k_F$.
- [[nakayama-nomura-wgc-bound]] — the original AdS translation and its counterexamples.

## Current status

No swampland criterion is proven in $d \ge 3$; the WGC's remnant and monopole arguments
are presented as "Loose conjectures" (the monopole argument as "Another heuristic
argument") in the founding paper itself, while the string-theory evidence
(heterotic spectra, higher-derivative extremality shifts, AdS/CFT tests in
non-holographic SCFTs) keeps sharpening which form survives. In 2d, modular invariance
proves WGC-type bounds ([[higher-dimensional-modularity]]).

## Open questions

- [[wgc-strong-vs-weak-form]] — does the strong form (lightest charged particle
  sub-extremal) hold, or only the weak form?
- [[gravity-derivation-of-modified-wgc]] — derive the $3c-2a$ bound from higher-derivative
  gauged supergravity.
- [[higher-dimensional-modularity]] — a 4d analog of the 2d modular-invariance proof.
