---
type: concept
title: Topological sectors in NN-FT (discrete latents and the BKT transition)
aliases: ["discrete latents NN-FT", "vortices in NN-FT", "BKT from neural networks", "topological defects NN-FT"]
tags: [machine-learning, neural-networks, nn-ft, topological-defects, bkt, xy-model]
prerequisites: [neural-network-field-theory]
created: 2026-07-08
updated: 2026-07-08
---

## Definition

The mechanism that puts **topological sectors** into a [[neural-network-field-theory|NN-FT]] by
enlarging the latent space with *discrete* parameters $Q$ labeling the topological quantum numbers:
$$\langle\mathcal O\rangle=\sum_Q\int d\theta\,P(\theta,Q)\,\mathcal O[\phi_{\theta,Q}].$$
Introduced in Ferko et al. 2026, presented in [[2607.02905|Halverson 2026]]. Its flagship application
is the Berezinskii–Kosterlitz–Thouless (BKT) transition of the 2d compact boson / XY model.

## Motivation

A Gaussian random-feature field is smooth, single-valued, and real: winding modes and vortices are
simply not in the ensemble, no matter how the spectrum is shaped. This mirrors the path integral,
where topological sectors enter through the choice of field space and measure, not through Gaussian
fluctuations. The resolution is structural — **the sum over topological sectors is a sum over discrete
latent variables of the network ensemble** (discrete latents are standard ML, as in Gaussian mixture
models or mixture-of-experts).

## Key formulas

For the XY model $S[\theta]=\tfrac{K_0}2\int d^2x(\nabla\theta)^2$, $K_0=\rho_{s,0}/T$, split the
architecture into a smooth spin-wave part and a singular winding part,
$$\theta(x)=b\,\theta_{\rm sw}(x)+\theta_v(x).$$
The spin waves are random Fourier features
$\theta_{\rm sw}(x)=\tfrac{A}{\sqrt N}\sum_j\cos(k_j\cdot x+\gamma_j)$ ($k_j=2\pi n_j/L$,
$n_j\propto1/|n_j|^2$); the vortices are the **discrete sector** $\{(x_a,m_a)\}$, $m_a=\pm1$,
$\sum_a m_a=0$, entering through $\theta_v(x)=\sum_a m_a\arg(x-x_a)$ with a neutral-Coulomb-gas density
$$P_{\rm vort}\propto y^{N_v}\exp\!\Big[2\pi K_0\sum_{a<b}m_a m_b\log(r_{ab}+a_c)\Big],$$
$y$ the vortex fugacity, $a_c$ a core regulator. The two sectors are statistically independent; the
spin wave is sampled exactly, the vortices by a Markov chain (displace a vortex, insert/delete a
neutral pair).

**BKT phenomenology reproduced.** At $N\to\infty$ the spin-wave two-point function is
$\langle e^{ib\theta_{\rm sw}(x)}e^{-ib\theta_{\rm sw}(0)}\rangle\sim|x|^{-\eta}$, $\eta=b^2$. The BKT
dictionary ($K_0=1/2\pi b^2$, $T=2\pi b^2$) and the universal $\eta_c=\tfrac14$ locate the transition
(units $\rho_{s,0}=1$):
$$b_c=\tfrac12,\qquad T_c=\tfrac\pi2.$$
The numerics then confirm the full picture: $\eta=b^2$ below $T_c$ (to $<1\%$); spin waves alone never
transition; above $T_c$ exponential decay $G_2(r)\propto e^{-r/\xi}$ with the essential singularity
$\xi(b)\sim\exp(c/\sqrt{b^2-b_c^2})$; vortex proliferation rising steeply above $b_c$; and the
universal Nelson–Kosterlitz stiffness jump $\Upsilon_R(T_c^-)=\tfrac2\pi T_c$.

## Relations

- Uses the same [[neural-network-field-theory|density-deformation]] and random-Fourier-feature
  spectrum-shaping as the [[string-amplitudes-from-neural-networks|bosonic-string NN-FT]], but adds
  the discrete latent $Q$ that continuous parameters cannot supply.
- The vortex sector is precisely the winding configurations $\oint\nabla\theta\cdot d\ell=2\pi m$ that
  no smooth Gaussian field reaches.

## Where it appears

- Introduced in [[2607.02905|Halverson 2026]] §Day 2 (Topological Defects and the BKT Transition),
  from Ferko et al. 2026; belongs to the [[physics-for-machine-learning]] topic.
