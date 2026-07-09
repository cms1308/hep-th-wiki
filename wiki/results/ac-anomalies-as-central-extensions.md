---
type: result
title: Anomalies as central extensions of holomorphic symmetry algebras
aliases: [a,c as central extensions, anomaly as ternary bracket, anomaly multiplet]
tags: [holomorphic-twist, anomaly, central-charge, l-infinity, a-equals-c, abj-anomaly]
status: proven
created: 2026-07-08
updated: 2026-07-08
---

## Statement

In the [[holomorphic-twist|holomorphic twist]] of a 4d $\mathcal N\geq1$ theory, **anomalies are
central extensions (3-cocycles / ternary $\lambda$-brackets) of the higher symmetry algebras**:

- The two conformal anomalies $a,c$ are the two $L_\infty$ central extensions of the
  [[two-virasoro-algebra|2-Witt algebra]], packaged as
  $$\{\!\{\mathbf S_i\,\mathbf S_j\,\mathbf S_k\}\!\}
  =16(a-c)\,\mathcal I^{\rm vec}_{ijk}+\tfrac43(3c-2a)\,\mathcal I^{\mathcal N=4}_{ijk}.$$
- The cubic flavor 't Hooft anomaly $k_{FFF}$ is the central extension of the
  [[higher-kac-moody-algebra|higher Kac–Moody algebra]]; mixed anomalies $k_F,k_{RRf}$ are
  further ternary brackets.
- An **ABJ (broken) symmetry** shows up as the failure of a current to be semi-chiral, e.g.
  $$\mathbf Q\,\mathbf J=\bar\partial\mathbf J-\tfrac{\hbar k}{2\pi^2}\partial\mathbf A\,\partial\mathbf A,$$
  reinterpreted as the conservation law of an **enlarged** symmetry algebra carrying an internal
  differential that maps $\mathbf J$ to the instanton density $\partial\mathbf c\,\partial\mathbf c$.
- For $\mathcal N\geq3$ the relevant space of 3-cocycles is one-dimensional (Fuks 1986), forcing
  $$a=c.$$

## Derivation sketch

Couple the twisted theory to background fields (a Beltrami differential $\mu$ for spacetime, a
connection $\mathbf A$ for flavor) and impose the **equivariant quantum BV master equation**. Its
failure is the anomaly, computed from triangle/Feynman diagrams and organized by a
**holomorphic anomaly polynomial** built from degree-three characteristic classes ($c_3=\mathrm{tr}\,F^3$
for flavor; $(c_1^3,c_1c_2)$ for spacetime). A descent construction ties the resulting central
extension of the current algebra to the ordinary 4d 't Hooft anomaly via the specialization
$p_1\mapsto c_1^2-2c_2$, $c_{1,r}\mapsto-\tfrac12 c_1$. For extended SUSY, the anomaly appears as
the unique 3-cocycle of [[higher-super-virasoro-algebra|$\mathfrak{svir}(2|\mathcal N-1)$]]; its
uniqueness for $\mathcal N\geq3$ is the algebraic origin of $a=c$.

## Assumptions

- Standard holomorphic-twist setup (nilpotent $\mathbf Q=\mathcal Q_-$, BV/BRST framework).
- Only 't Hooft / ABJ anomalies are considered; genuine **gauge** anomalies are excluded (they
  spoil the quantum theory).
- The ABJ "anomaly multiplet" $(\mathbf N,\mathbf M,\mathbf L_i)$ organizes the internal differential.

## Status

**Proven** within the framework (component-level 3-cocycles are given explicitly at the level of
the twist). The identification of $a,c$ with the two central extensions was established in paper I
~[[2509.16737|Bomans-Garner-Williams-Wu 2023]]; the full anomaly dictionary, the ABJ
reinterpretation, and $a=c$ for $\mathcal N\geq3$ are ~[[2509.16737|Bomans-Garner-Williams-Wu 2025]].
Explicit **supergeometric** representatives of the extended-SUSY 3-cocycles remain incomplete —
[[supergeometric-3-cocycles-svir]].

## Implications

- Feeds [[holomorphic-a-maximization]]: the $a$-extremization condition $k_f=9k_{RRf}$ is a
  statement about these ternary brackets.
- Recovers the classic $a=c$ for $\mathcal N\geq3$ SCFTs (Sohnius; Aharony–Evtikhiev 2015) from
  cocycle uniqueness.
- Gives a categorified, algebraic home for anomaly data that the [[superconformal-index]] (a
  number) cannot see.
