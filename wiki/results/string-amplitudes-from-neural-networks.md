---
type: result
title: String amplitudes from neural networks
aliases: ["bosonic string as NN-FT", "Virasoro-Shapiro from neural networks", "Veneziano from neural networks"]
tags: [machine-learning, neural-networks, nn-ft, string-theory, amplitudes]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

The gauge-fixed bosonic string is a [[neural-network-field-theory|NN-FT]]: ensembles of
infinite-width networks realize the worldsheet boson and the $bc$ ghosts, and the four-tachyon
amplitude comes out as an analytic integral over network parameters, equal to the Virasoro–Shapiro
amplitude (Veneziano for the open string). Established in Frank et al. 2026, presented in
[[2607.02905|Halverson 2026]].

## Derivation sketch

**Free boson.** Give the embedding fields $X^\mu(z,\bar z)$ the random-Fourier-feature architecture
$$X^\mu(z)=\frac{C}{\sqrt N}\sum_{i=1}^N\frac{a_i^\mu}{|W_i|}\cos\!\Big(\tfrac12(W_iz+\bar W_i\bar z)+c_i\Big),$$
with $a_i^\mu\sim\mathcal N(0,\sigma_a^2)$, $c_i\sim\mathrm{Unif}[-\pi,\pi]$, and complex hidden weights
$W_i$ uniform on a momentum-space annulus $B^2_\Lambda\setminus B^2_\epsilon$ ($\Lambda$ UV cutoff,
$\epsilon$ IR cutoff). The spectrum-shaping factor $1/|W_i|$ lands the two-point function on the
free-boson logarithm
$$\langle X^\mu(z)X^\nu(w)\rangle=\alpha'\delta^{\mu\nu}\big[-\log r+\cdots\big],\qquad G^{(2)}(p)=2\pi\alpha'\delta^{\mu\nu}/p^2,$$
so by the CLT the $N\to\infty$ ensemble *is* the gauge-fixed Polyakov boson — defined by its
statistics, no worldsheet action written down. Matching gives
$$\alpha'=\frac{\sigma_a^2}{\Lambda^2-\epsilon^2},$$
with the annulus radii mere regulators and $\sigma_a$ the only physical dial.

**Ghosts.** The same architecture with **Grassmann-valued** output weights $\beta_k,\chi_k$ and a
Grassmann Gaussian density $P\propto\exp(\beta_k\chi_k/\sigma^2)$; Berezin integration gives
$\langle\beta_k\chi_l\rangle=\sigma^2\delta_{kl}$ and, with phases arranged, the ghost propagator
$\langle b(z)c(w)\rangle=1/(z-w)+\cdots$.

**Amplitude in parameter space.** The four-tachyon sphere amplitude is a *parameter-space*
correlator, an honest finite-dimensional integral over the network parameters. The Gaussian integral
over the output weights $a_i^\mu$ is exact; the remaining i.i.d. $W,c$ integrals exponentiate at large
$N$ into single-neuron expectations, whose cross terms assemble precisely into the Koba–Nielsen factor
$\prod_{r<s}|z_r-z_s|^{\alpha'p_r\cdot p_s}$ (self-contractions absorbed into the vertex
renormalization $\mathcal Z(p)$). The zero-mode Gaussian gives $\delta^D(\sum_r p_r)$ in the
decompactification limit. The result is
$$\mathcal A^{(4)}=\frac{g_s^2\,\delta^D(\sum_r p_r)}{\mathrm{Vol}(SL(2,\mathbb C))}\int\Big(\prod_{\alpha=1}^4 d^2z_\alpha\Big)\prod_{r<s}|z_r-z_s|^{\alpha'p_r\cdot p_s},$$
the standard Virasoro–Shapiro amplitude, obtained as a correlator in network parameter space. The
computation is analytic — no path integral and no Monte Carlo.

**Open strings.** Put the worldsheet on the upper half plane and enforce the Neumann condition by the
image trick *at the architecture level*, $X_N^\mu(z,\bar z)=\tfrac1{\sqrt2}[X^\mu(z,\bar z)+X^\mu(\bar z,z)]$,
which doubles the boundary propagator; the same steps give the Veneziano amplitude.

## Assumptions

- Infinite width ($N\to\infty$): the amplitude is the Gaussian (GP) result. Different architectures
  with a $1/p^2$ neuron spectrum give the same GP, so $\sigma_a$ always plays the role of $\alpha'$;
  they differ at finite $N$, where $1/N$ non-Gaussianities would correct the amplitudes.
- Momentum conservation emerges as $\delta^D(\sum p_r)$ from translation invariance of the network
  density (zero-mode decompactification limit).

## Status

Established: the exact Virasoro–Shapiro (and Veneziano) amplitude, with its crossing symmetry, Regge
behavior, and soft UV, reproduced analytically as a parameter-space integral.

## Implications

- Puts the most famous string amplitudes inside the NN-FT program, complementing the worldsheet
  Virasoro symmetry developed separately (Robinson et al. 2025).
- Positions finite-width $1/N$ corrections as a concrete handle on *interacting* deformations of
  string amplitudes (open question in [[neural-network-field-theory]]).
- Uses [[topological-sectors-nn-ft|Grassmann-valued networks]] for the ghost sector — the same
  machinery reused in the [[critical-dimension-from-mode-counting-nn-ft|$D=26$ derivation]].

## References

- [[2607.02905|Halverson 2026]] §Day 2 (The Bosonic String); Frank et al. 2026 (string), Frank et al.
  2025 (Grassmann/SUSY networks), Robinson et al. 2025 (worldsheet Virasoro).
