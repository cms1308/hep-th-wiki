---
type: concept
title: Weak Gravity Conjecture
aliases: [WGC]
tags: [swampland, quantum-gravity, black-holes]
prerequisites: [black-hole-thermodynamics]
created: 2026-07-03
updated: 2026-07-07
---

## Definition

The conjecture that in any consistent theory of quantum gravity with a $U(1)$ gauge field,
there exists a state whose charge exceeds its mass in extremal-black-hole units — "gravity
is the weakest force" ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]). The
operational statement is that extremal black holes can decay, which requires a state with
$m/q < (M/Q)\big|_{\text{ext}}$ (the sharp conjecture forms use $\le$, with BPS saturation
as the limiting case). In units $M_{\rm Pl}=1$ with charge normalized so large
extremal black holes have $M/Q = 1$, the founding paper distinguishes three sharp forms:

- **(I)** the state of *minimal charge* has $M/q \le 1$ — refuted there by stable heavy
  states (the $SO(32)$ heterotic spinors, Wen-Witten fractionally charged winding states);
- **(II)** the *lightest charged particle* has $M/q \le 1$ — the strongest surviving form;
- **(III)** *some* state has $M/q \le 1$ — the weak form, which most of the string-theory
  evidence supports ([[wgc-strong-vs-weak-form]]).

## Motivation

Kinematic: an extremal black hole can only shed its charge if a state with
charge-to-mass ratio exceeding the extremal value exists; otherwise an unbounded number of
stable charged [[black-hole-remnant|remnants]] survives — the same kind of thermodynamically
pathological unbounded degeneracy that [[hep-th-9501106|Susskind 1995]] shows drives the
renormalized Newton constant to zero — the heuristic behind
[[no-global-symmetries-in-quantum-gravity]], of which the WGC is the quantitative
$g \to 0$ obstruction: as $g \to 0$ a gauge symmetry becomes effectively global, and the
conjectured cutoff $\Lambda \lesssim g M_{\rm Pl}$ removes the would-be limit. The WGC is
a flagship constraint of the [[swampland-program]] — separating effective field theories
that can arise from quantum gravity from those that cannot.

## Key formulas

- Electric form: a charged particle with $m \lesssim g\, M_{\rm Pl}$.
- Magnetic form: a monopole with $m_{\rm mag} \lesssim M_{\rm Pl}/g$; since a minimal
  monopole has $m_{\rm mag} \sim \Lambda/g^2$, this bounds the cutoff of the effective
  $U(1)$ theory:
  $$\Lambda \;\lesssim\; g\, M_{\rm Pl}$$
  ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]] — the "magnetic WGC" of later
  literature, there derived from the monopole bound).
- Decay condition, as used in the AdS analysis of
  [[2308.01717|Cho-Choi-Lee-Song 2023]]: $M_{\text{ext}}(Q) - m \ge M_{\text{ext}}(Q-q)$
  for some state $(m, q)$.
- $p$-form generalization in $D$ dimensions: charged branes with
  $T_{\rm el} \lesssim (g^2/G_N)^{1/2}$, $T_{\rm mag} \lesssim (1/(g^2 G_N))^{1/2}$; the
  axion case ($D=4$, $p=0$, $g \sim 1/F$) gives $S_{\rm inst} \lesssim M_{\rm Pl}/F$,
  obstructing parametrically super-Planckian axion decay constants (and hence
  [[extranatural-inflation]]-type models).
- Multiple $U(1)$'s: sub-extremal states along a basis of charge-space directions
  ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]), sharpened to the
  [[convex-hull-condition|convex hull condition]] — the convex hull of charge-to-mass
  vectors $\vec z = \vec q\, M_{\text{Pl}}/m$ must contain the extremal black hole region
  ([1402.2287](https://arxiv.org/abs/1402.2287)).
- $AdS_5$: extremality is strongest in the $Q \to 0$ limit, giving
  $m^2/q^2 \le 3g^2/2G_N$, which translates via AdS/CFT into a bound on the boundary
  spectrum — the [[nakayama-nomura-wgc-bound|Nakayama-Nomura bound]]
  $\Delta^2/q^2 \le 12c/k_F$, modified by
  [[2308.01717|Cho-Choi-Lee-Song 2023]] to $\Delta^2/q^2 \le 12(3c-2a)/k_F$
  ([[modified-ads-wgc-3c-2a]]).

## Evidence

- Heterotic on $T^6$: the perturbative spectrum always contains, in non-BPS charge
  directions, a state strictly below Sen's extremal black hole mass
  ($M^2 = \tfrac12 Q_L^2 - 1$ vs. $\tfrac12 Q_L^2$); BPS directions saturate the bound.
  Extended, for any integral $U(1)$ coming from the left-movers, to any perturbative
  heterotic compactification by spectral flow / completeness of the worldsheet CFT
  spectrum ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]).
- Higher-derivative corrections: with
  $\mathcal L = -F_{\mu\nu}^2 + a(F^2)^2 + b(F\tilde F)^2$, the extremal mass shifts to
  $M^2_{\rm extr} = Q^2 - \tfrac{2a}{5}$ (purely electric/magnetic), so the
  causality-preferred sign $a>0$ makes large extremal black holes themselves sub-extremal
  ([[f4-corrected-extremality-bound]]).
- Parametric checks across string constructions (heterotic, KK/winding, type I, D-brane
  $U(1)$'s); the many-$U(1)$ Higgsing loophole is closed by the species problem.

## Relations

- In [[ads-cft-correspondence|AdS/CFT]], the WGC becomes a statement about the
  dimension-to-charge spectrum of the boundary CFT — testable in non-holographic CFTs,
  where "quantum gravity in AdS" exists but is not Einstein-like. An AdS version was
  already posed as an open direction in
  [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]].
- In 2d CFT, modular invariance *proves* a WGC-type bound
  ([1603.09745](https://arxiv.org/abs/1603.09745),
  [1606.08438](https://arxiv.org/abs/1606.08438),
  [1811.00976](https://arxiv.org/abs/1811.00976)) — the model for a hoped-for 4d
  derivation ([[higher-dimensional-modularity]]).
- Part of the broader [[swampland-program]]; the founding paper proposes that the weak
  form (III) follows from finiteness of the number of exactly stable states per direction
  in charge space.
- **As a special case of the [[imaginary-distance-bound|imaginary distance bound]]**: reducing
  Einstein-Maxwell on $S^1$, a wrapped charged particle's action vanishes on the extremal lines
  exactly when it saturates the WGC bound, so demanding a superextremal state to spoil the
  [[euclidean-axion-wormhole|scalar wormhole]] reproduces the WGC (and, with several gauge
  fields, the [[convex-hull-condition]]) — [[2605.05336|Maldacena-Maloney-McPeak 2026]].
- **Axionic WGC from path-integral positivity**: requiring
  [[gravitational-path-integral-positivity|positivity of the gravitational path integral]] to
  survive the divergence of axion wormhole amplitudes forces shift-symmetry-breaking instantons
  with $S_{\rm inst}\le\tfrac12|\mathrm{Im}\,\Delta a_{\rm crit}|$ — the axionic WGC with a fixed
  $\mathcal O(1)$ coefficient ([[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]]). For type IIB on
  AdS$_5\times S^5$ the required $\beta_{\rm crit}=\sqrt{8/3}<\beta_{\rm IIB}=2$, so it passes.

## Where it appears

- [[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]] — the founding paper: forms
  (I)/(II)/(III), magnetic/cutoff form, $p$-form and axion generalizations, heterotic
  evidence.
- [[2308.01717|Cho-Choi-Lee-Song 2023]] — modified $3c-2a$ bound in $AdS_5$/CFT$_4$ and
  systematic tests in $\mathcal{N}=1$ gauge theories.
- [[2605.05336|Maldacena-Maloney-McPeak 2026]] — WGC as a special case of the imaginary
  distance bound (via $S^1$ reduction of Einstein-Maxwell).
- [[2605.05305|Di Ubaldo-Iliesiu-Lin-Yan 2026]] — sharp axionic WGC derived from
  gravitational-path-integral positivity.
- Review: [Harlow-Heidenreich-Reece-Rudelius 2022](https://arxiv.org/abs/2201.08380).
