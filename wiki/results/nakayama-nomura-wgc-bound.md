---
type: result
title: Nakayama-Nomura WGC bound
aliases: [NN-WGC, AdS WGC bound]
tags: [weak-gravity-conjecture, swampland, ads-cft]
status: disputed
created: 2026-07-03
updated: 2026-07-04
---

Conventions: those of [[2308.01717|Cho-Choi-Lee-Song 2023]] — $C_T = \frac{40}{\pi^4}c$,
$C_F = \frac{3}{4\pi^4}k_F$, $k_F \equiv -3\,\mathrm{tr}\,RFF$ for the SUSY case.

## Statement

The CFT translation of the [[weak-gravity-conjecture|Weak Gravity Conjecture]] in
$AdS_5$/CFT$_4$ ([Nakayama-Nomura 2015](https://arxiv.org/abs/1509.01647)): a CFT$_4$ with a
$U(1)$ flavor symmetry should contain an operator with
$$\frac{\Delta^2}{q^2} \;\le\; \frac{9}{40}\frac{C_T}{C_F} \;=\; \frac{12c}{k_F}\,.$$
An AdS version of the WGC had been posed as an open direction already in the founding
paper ([[hep-th-0601001|Arkani-Hamed-Motl-Nicolis-Vafa 2006]]).

## Derivation sketch

Extremal black hole decay kinematics in semi-classical Einstein-Maxwell theory in $AdS_5$:
demanding $M_{\text{ext}}(Q) - m \ge M_{\text{ext}}(Q-q)$ for some particle, the strongest
condition arises in the $Q\to 0$ (flat-space) limit, giving $m^2/q^2 \le 3g^2/2G_N$ — the
same as 5d flat-space extremality $M_{\text{ext}}/Q = \sqrt{3g^2/2G_N}$. Translating with
$C_T = \frac{40 L^3}{\pi^2 G_N}$, $C_F = \frac{6L}{\pi^2 g^2}$, $\Delta \simeq Lm$ yields
the bound ([[2308.01717|Cho-Choi-Lee-Song 2023]], review of
[1509.01647](https://arxiv.org/abs/1509.01647)).

## Assumptions

Semi-classical Einstein-Maxwell gravity in the bulk — i.e. a holographic CFT with
$a \simeq c \sim N^2$. Applying it to arbitrary CFTs is an extrapolation beyond the
derivation's regime.

## Status

Fails as a universal statement: 4d $\mathcal{N}=1$ $SU(N)$ SQCD in the
[[conformal-window|conformal window]] has no chiral-ring operator satisfying it when
$N_f/N \gtrsim 2.1$ (already noted in [1509.01647](https://arxiv.org/abs/1509.01647)), and
[[2308.01717|Cho-Choi-Lee-Song 2023]] exhibit further families (e.g. $SU(N)$ with
$2\,\mathbf{S}+2\,\overline{\mathbf{S}}+N_f(\Box+\overline{\Box})$ at $N_f/N \gtrsim 0.6$)
where *no* chiral-ring operator can ever satisfy it. Some
[[dense-spectrum-scft|dense-spectrum]] SCFTs do obey it
([1912.12881](https://arxiv.org/abs/1912.12881),
[2007.16165](https://arxiv.org/abs/2007.16165)). The full simple-gauge-group
classification catalogues many more violations: most Type I/II $SU$ families above
family-specific [[veneziano-limit|Veneziano]] thresholds, sparse large-$N$ Type III
theories at fixed $N_f$ (e.g. $SU(N)$ with $3\,\mathbf{A}+3\,\overline{\mathbf{A}}$ at
$N_f = 3,4,5$ for *any* $N$), and isolated finite-$(N_f, N)$ points
([[2510.19136|Cho-Lee-Song 2025]]). The fix is
[[modified-ads-wgc-3c-2a]]: replace $c \to 3c-2a$, which agrees with this bound at large
$N$ (where $a\simeq c$) and repairs every known counterexample.

## Implications

The counterexamples show that bounds derived from two-derivative Einstein-Maxwell theory
need not extend to CFTs far from the holographic regime — the correct universal
combination is selected by the [[supersymmetric-cardy-formula-4d|supersymmetric Cardy formula]],
not by $C_T$ alone.
