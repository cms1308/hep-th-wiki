---
type: result
title: Liouville theory as an NN-FT
aliases: ["Liouville from neural networks", "NN-FT Liouville", "DOZZ from neural networks"]
tags: [machine-learning, neural-networks, nn-ft, liouville, cft, dozz]
status: established
created: 2026-07-08
updated: 2026-07-08
---

## Statement

The probabilistic construction of Liouville CFT is effectively a
[[neural-network-field-theory|NN-FT]], and Monte Carlo in parameter space reproduces the DOZZ
structure constant. Established in Ferko et al. 2026, presented in [[2607.02905|Halverson 2026]].

Liouville is an interacting 2d CFT with action
$$S=\int_\Sigma d^2x\,\sqrt g\Big(\tfrac1{4\pi}\partial^\mu\phi\,\partial_\mu\phi+\tfrac{Q}{4\pi}R\,\phi+\mu\,e^{2b\phi}\Big),$$
background charge $Q=b+1/b$, central charge $c_L=1+6Q^2$, primaries $V_\alpha={:}e^{2\alpha\phi}{:}$
with $\Delta_\alpha=\alpha(Q-\alpha)$. Its three-point structure constants are the DOZZ formula
$$C=\big(\pi\mu\,\gamma(b^2)\,b^{2-2b^2}\big)^{-s}\frac{\Upsilon_b'(0)\prod_{i}\Upsilon_b(2\alpha_i)}{\Upsilon_b(\sum_i\alpha_i-Q)\prod_i\Upsilon_b(\sum_j\alpha_j-2\alpha_i)},$$
$\gamma(x)=\Gamma(x)/\Gamma(1-x)$, $s=(\alpha_1+\alpha_2+\alpha_3-Q)/b$, and $\Upsilon_b$ Zamolodchikov's
special function — the irrational-$c$ target.

## Derivation sketch

**Architecture.** A zero mode plus real spherical harmonics on $S^2$,
$$\phi_\theta=c+\sum_{\ell=1}^L\sum_{m=-\ell}^\ell a_{\ell m}Y_{\ell m},$$
with the free field on the sphere obtained from Gaussian parameters
$a_{\ell m}\sim\mathcal N(0,4\pi/\ell(\ell+1))$.

**Interaction on the zero mode.** On the round sphere $R$ is constant, so the curvature coupling
integrates against fluctuations to zero ($\int_{S^2}\sqrt g\,R\,Y_{\ell m}=0$ for $\ell\ge1$), leaving
$2Qc$; and $e^{2b\phi}=e^{2bc}e^{2bX}$ factorizes. Both interaction terms therefore live entirely in
the zero mode. Writing $t=e^{2bc}$, the density factorizes $P(\theta)=P(t\mid a_{\ell m})P(a_{\ell m})$
with
$$P(t\mid a_{\ell m})\propto t^{s-1}\exp\!\big(-M_X(a_{\ell m})\,t\big),\qquad s=\frac{\sum_i\alpha_i-Q}{b},$$
where $M_X=\mu\int_{S^2}d^2x\sqrt g\,{:}e^{2b\sum a_{\ell m}Y_{\ell m}}{:}$ is the **Gaussian
multiplicative chaos**. The non-zero modes stay independent Gaussians: all statistical dependence,
all interaction, lives in how the zero mode is conditioned on them.

**Computation.** Honest Monte Carlo in parameter space — sample the $a_{\ell m}$, normal-order via
mollified ensemble variances, pixelate the sphere to evaluate $M_X$, sample $t$ from its conditional
density, average.

## Assumptions

- Round $S^2$ worldsheet (constant $R$), which is what localizes both interaction terms onto the
  zero mode.
- Finite harmonic cutoff $L$; the reported run is $L=30$.

## Status

Established numerically. At $L=30$ (10 experiments of 50,000 runs, sphere pixelated at $100\times200$)
the NN structure constant agrees with DOZZ at the few-percent level across a range of $b$ and
$\alpha_3$, error bars smaller than the plot markers, degrading (as expected) near the Seiberg bound
$\alpha\le Q/2$ where DOZZ develops zeros.

## Implications

- A first interacting *CFT with irrational central charge* realized as a network ensemble — the DOZZ
  formula becomes a target hit by parameter-space sampling.
- Shows the [[neural-network-field-theory|density-deformation]] mechanism ("interactions = broken
  independence") realizing a nontrivial, rigorously-defined interacting theory, not just $\phi^4$.

## References

- [[2607.02905|Halverson 2026]] §Day 2 (Liouville Theory); Ferko et al. 2026; David–Kupiainen–
  Rhodes–Vargas 2016 (probabilistic Liouville); Dorn–Otto 1994, Zamolodchikov–Zamolodchikov 1995 (DOZZ).
