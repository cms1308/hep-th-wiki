---
type: result
title: Ryu-Takayanagi formula
aliases: [RT formula, Ryu-Takayanagi, holographic entanglement entropy formula, RT proposal]
tags: [holography, entanglement, ads-cft, holographic-entanglement-entropy]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The [[entanglement-entropy|entanglement entropy]] of a spatial region $A$ in a $d+1$
dimensional CFT with an AdS$_{d+2}$ dual equals the area of a bulk static
[[extremal-surface|minimal surface]] $\gamma_A$ anchored on the entangling surface
($\partial\gamma_A=\partial A$, and $\gamma_A$ homologous to $A$), in Planck units:
$$S_A=\frac{\mathrm{Area}(\gamma_A)}{4G_N^{(d+2)}}.$$
It reproduces the structure of the [[bekenstein-hawking-entropy|Bekenstein-Hawking]] area law,
manifestly gives $S_A=S_B$ for a pure state, and satisfies subadditivity
$S_{A_1}+S_{A_2}\ge S_{A_1\cup A_2}$.

## Derivation sketch

Proposed by analogy with black-hole entropy and checked against known CFT results. The
sharpest check is AdS$_3$/CFT$_2$: the bulk object is a geodesic, and with the Brown-Henneaux
relation $c=\frac{3R}{2G_N^{(3)}}$ and the holographic UV cutoff $e^{\rho_0}\sim L/a$ the
geodesic length reproduces the 2d CFT interval entropy exactly. Originally a conjecture; later
derived from AdS/CFT by a bulk replica computation (Lewkowycz-Maldacena 2013) and generalized
covariantly by [[hrt-formula|HRT]].

## Assumptions

- Static (time-independent) bulk, so a preferred constant-time slice exists; $\gamma_A$ is
  minimal on that slice. Time-dependent backgrounds require the covariant
  [[hrt-formula|HRT]] extremal-surface prescription.
- Classical (large $N$, strong coupling / supergravity) bulk; $1/N$ quantum corrections are
  not included (later: the FLM quantum term and quantum extremal surfaces).
- Homology constraint: $\gamma_A$ must be homologous to $A$.

## Status

**Established.** Verified exactly in AdS$_3$/CFT$_2$ (single interval, multiple intervals,
finite temperature via BTZ) and consistent with the entanglement area law in higher $d$;
subsequently proven from AdS/CFT. The higher-dimensional strong-coupling comparison to free
$\mathcal N=4$ SYM agrees only up to an $O(1)$ factor $\sim\tfrac32$, paralleling the known
thermal-entropy strong/weak mismatch — not a failure of the formula.

## Key formulas

- **RT formula:** $S_A=\mathrm{Area}(\gamma_A)/4G_N^{(d+2)}$.
- **AdS$_3$ single interval (reproduces Calabrese-Cardy):**
  $S_A=\frac{c}{3}\log\!\left(\frac{L}{\pi a}\sin\frac{\pi l}{L}\right)$, $c=\frac{3R}{2G_N^{(3)}}$.
- **Finite temperature (2d, BTZ dual):**
  $S_A=\frac{c}{3}\log\!\left(\frac{\beta}{\pi a}\sinh\frac{\pi l}{\beta}\right)$.
- **Higher $d$:** leading UV term $\propto \mathrm{Area}(\partial A)/a^{d-1}$ (area law) plus a
  universal cutoff-independent term (a finite constant for even $d$, a $\log$ coefficient for
  odd $d$).

## Implications

- Turns a hard field-theory quantity into a classical geometry problem, launching
  [[holographic-entanglement-entropy|holographic entanglement entropy]] and the
  "entanglement/geometry" program.
- The finite-temperature, large-region limit has $\gamma_A$ wrap the horizon and
  $S_A\to S_{\rm BH}$, fixing the $1/4G_N$ normalization and connecting entanglement to
  black-hole entropy.

## References

- [[hep-th-0603001|Ryu-Takayanagi 2006]] (the formula and the AdS$_3$/higher-$d$ checks).
- Covariant generalization: [[0705.0016|Hubeny-Rangamani-Takayanagi 2007]].
