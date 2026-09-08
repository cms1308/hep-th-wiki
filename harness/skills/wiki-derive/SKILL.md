---
name: wiki-derive
description: Derive a physics result step by step, verify it, and record it as a wiki derivation page. Use when the user asks how a result is derived, wants a derivation worked out, or asks to fill in the steps of a paper's argument.
---

# Derive and record

Input: what to derive (a result, formula, or a step in a paper the user wants expanded).

## 1. Ground it

- Read `Index.md`; open the relevant result/concept/paper pages.
- If a source paper contains (or sketches) the derivation, **read the TeX in `sources/`** and
  follow it — the wiki's derivation must be anchored to sources where they exist, not
  reconstructed from memory. Note explicitly where you deviate, simplify, or fill gaps.
- If no source gives the full argument, an original derivation may start from premises
  supported by ingested sources: cite those premises and mark the new steps as your own.
  If even the premises lack ingested support, explain the gap in chat; do not file an
  unsourced knowledge page ({{SCHEMA}} → No page without a source).
- If a derivation page for it already exists, extend/refine that page instead.

## 2. Derive

Write the full derivation:
- Fix notation and conventions up front (metric signature, units, normalizations).
- Numbered steps; justify every nontrivial step. No "it can be shown".
- Preserve source file/section/equation locators, assumptions, and convention conversions
  for the premises and the final result; distinguish source claims from added deductions.
- Standard LaTeX (`$...$`, `$$...$$`), self-contained — expand source macros.
- Keep the level matched to the wiki's prerequisites structure: link
  [[concepts]]/[[methods]] used instead of re-deriving them inline.

## 3. Verify

Before recording, check the result:
- dimensional analysis; known limits and special cases; symmetry consistency;
  agreement with the cited source's equations.
- For a long or subtle derivation, spawn a general-purpose agent to independently check the
  steps (give it the derivation and the source TeX; ask it to find errors, not to praise).
- Record the outcome honestly: `status: verified` only if the checks pass; otherwise
  `status: unverified` with the unresolved point stated in the Checks section.

## 4. Record

- Write `wiki/derivations/<kebab-slug>.md` from `templates/derivation.md`.
- Link it from the relevant pages: the result page's "Derivation sketch" section gets
  `Full derivation: [[<slug>]]`; concept/paper pages link where natural.
- Update `Index.md` (Derivations section); append to `Log.md`:
  `## [YYYY-MM-DD] derive | <slug> | <what was derived>` + status + pages linked.

## 5. Report

Present the derivation to the user (this is the answer to their question, not just a filing
job), state the verification outcome, and note anything left unverified.
