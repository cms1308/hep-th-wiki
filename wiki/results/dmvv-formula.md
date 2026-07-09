---
type: result
title: DMVV Formula (symmetric-orbifold partition function)
aliases: ["DMVV", "Dijkgraaf-Moore-Verlinde-Verlinde formula", "second-quantized string formula"]
tags: [ads3-cft2, symmetric-orbifold, cft2, elliptic-genus]
status: proven
created: 2026-07-07
updated: 2026-07-07
---

## Statement

The generating function of partition functions (or elliptic genera) of symmetric orbifolds $\mathrm{Sym}^N(\mathcal{M})$, summed over $N$ with a fugacity $p$, is an **infinite product** over the seed-CFT degeneracies — a "second-quantized string" partition function:
$$\sum_{N\ge0}p^N\,Z_{\mathrm{Sym}^N(\mathcal{M})}(q,\bar q,\dots)=\prod_{n\ge1}\ \prod_{h,\bar h,\dots}\big(1-p^{\,n}q^{h}\bar q^{\bar h}\cdots\big)^{-c(n h,\dots)},$$
where the exponents $c(\cdot)$ are the seed degeneracies. The single index $n$ counts the winding (twist length) of a long string, so the product realizes the Fock space of a second-quantized string.

## Derivation sketch

Twisted sectors of $\mathrm{Sym}^N(\mathcal{M})=\mathcal{M}^{\otimes N}/S_N$ are labelled by conjugacy classes of $S_N$, i.e. partitions of $N$ into cycles; a length-$w$ cycle is a single copy of $\mathcal{M}$ on a circle $w$ times as long, with fractionally moded ($1/w$) oscillators. Summing over all partitions and all $N$ with weight $p^N$ exponentiates the single-cycle (single long-string) contribution into the infinite product above — the orbifold analog of the free-string second-quantization formula.

## Assumptions

- Seed CFT with a well-defined (super)character / elliptic genus; convergence in the appropriate fugacity domain.
- For the AdS$_3$/CFT$_2$ application, $\mathcal{M}=\mathcal{M}_4$ with $c_{\text{seed}}=6$.

## Status

Established (Dijkgraaf–Moore–Verlinde–Verlinde 1996). Standard tool for [[symmetric-orbifold-cft|symmetric-orbifold]] partition functions and elliptic genera.

## Implications

- Supplies the grand-canonical partition function $\mathcal{Z}(p,y,\bar y)=\sum_N p^N Z_N$ whose poles and residues are read off in the [[grand-canonical-residue-expansion]] and identified with bulk saddles in the [[ads3-giant-graviton-expansion]].
- Interprets multi-wound CFT sectors as a second-quantized bulk string Fock space, matching the [[tensionless-string-ads3|tensionless string]] spectrum.
