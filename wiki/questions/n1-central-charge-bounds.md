---
type: question
title: Central charge bounds for interacting N=1 SCFTs
aliases: [a/c < 5/4 conjecture, minimal N=1 central charges]
tags: [scft, central-charges, bounds, supersymmetry]
status: open
created: 2026-07-04
updated: 2026-07-04
---

## Statement

Related questions for interacting 4d $\mathcal{N}=1$ SCFTs:

1. Is there an upper bound $a/c < \tfrac54$ — strictly inside the
   [[hofman-maldacena-bound|Hofman-Maldacena window]] $a/c < \tfrac32$?
   [[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]] write it is "tempting to conjecture
   that there is no interacting $\mathcal{N}=1$ SCFT with $a/c \ge 5/4$."
2. Is there a lower bound $a/c > \tfrac35$ for interacting SCFTs, and are the
   empirically unpopulated windows near both Hofman-Maldacena endpoints theorems?
   ([[2510.19136|Cho-Lee-Song 2025]])
3. Is there a rigorous lower bound on $c$ (and $a$), analogous to the proven
   $c \ge \tfrac{11}{30}$ for interacting $\mathcal{N}=2$ SCFTs
   ([1509.00033](https://arxiv.org/abs/1509.00033))? What is the truly minimal
   $\mathcal{N}=1$ SCFT?

## Why it matters

- The whole 7,346-entry [[4d-n1-scft-landscape|landscape]] realizes only
  $0.7228 \lesssim a/c \lesssim 1.2100$ — far inside the unitarity-allowed window. If
  $a/c$ bounds tighter than Hofman-Maldacena exist, they constrain the possible bulk
  duals (since $c-a$ controls higher-derivative corrections) and feed AdS versions of
  swampland conjectures.
- An $\mathcal{N}=1$ bound $a/c < \tfrac32$ strictly (or $<\tfrac54$) also protects the
  positivity of $3c-2a$ underlying the [[modified-ads-wgc-3c-2a|modified AdS WGC]] and
  the [[supersymmetric-cardy-formula-4d|supersymmetric Cardy formula]].

## Main attempts

- Empirical: the landscape maximum $a/c = \tfrac{507}{419} \simeq 1.2100$ ($SO(5)$ with
  $\mathbf{14}+\mathbf{5}$, $W = M_1 S^2 + M_1^2$) is the current record for interacting
  $\mathcal{N}=1$ SCFTs, beating the ISS model's $\tfrac{183}{158} \simeq 1.158$; it
  remains below the $\mathcal{N}=2$ bound $a/c \le \tfrac54$
  ([[2408.02953|Cho-Maruyoshi-Nardoni-Song 2024]]).
- The simple-gauge-group [[large-n-universality-classes|large-$N$ classification]]
  realizes only $0.6930 \lesssim a/c \le \tfrac{417}{368} \simeq 1.1332$; a
  [[veneziano-limit|Veneziano]]-only $Sp(2)$ theory with 10 fundamentals reaches
  $a/c = \tfrac{339}{514} \simeq 0.6595$. Empirically the windows
  $1.25 \lesssim a/c \lesssim 1.5$ **and** $0.5 \lesssim a/c \lesssim 0.6$ are
  unpopulated, and $\tfrac35$ is floated as a conjectural lower bound for interacting
  SCFTs ([[2510.19136|Cho-Lee-Song 2025]]).
- On the minimal side, the smallest known theory is the
  [[minimal-n1-scft|deformed $(A_1,A_4)$ SCFT]] with
  $(a,c) = (\tfrac{633}{2000},\tfrac{683}{2000})$.

## Current status

Open — no derivation of any of the bounds; the evidence is the statistics of the
deformation landscape and of the large-$N$ classification, which populate only
$0.6 \lesssim a/c \lesssim 1.21$ inside the unitarity-allowed
$[\tfrac12, \tfrac32]$.
