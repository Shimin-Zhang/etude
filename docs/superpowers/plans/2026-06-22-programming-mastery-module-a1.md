# Programming Mastery — Module A1 (Plan 3) Implementation Plan

> **For agentic workers:** Authoring + executable-verification plan (research-as-you-go). Each drill's answer key is **verified by running it through the Plan-1 runner**, never asserted. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Author module **A1 — Notional machine / execution model** end-to-end (teaching file + golden exemplars) as the *reference implementation* of the module model, and prove it with a live coached-session smoke test.

**Architecture:** A1 plugs into the Plan-2 engine. The module file follows the spec §5 9-part anatomy and must pass `tools/validate_modules.py`. Exemplars are tiered, with **runner-verified** outputs. The first real coached session runs against A1.

**Tech Stack:** Markdown; verification via `programming-mastery/runtime/python/runner.py` and pytest (unchanged).

**Spec:** `docs/superpowers/specs/2026-06-22-programming-mastery-skill-design.md` (§5 anatomy, §6 A1 row, §7/§8 engine). Engine refs: `references/{evidence-base,coaching-loop,drill-generation,assessment}.md`.

---

## Method note

Research-as-you-go: the author researches notional-machine pedagogy (Sorva, du Boulay, misconception catalogs) **and** Python execution-model gotchas to build a real common-error catalog and well-leveled drills. **Every drill/exemplar's expected output is verified by actually running it** through the runner (apply our own executable-ground-truth discipline to authoring). A1 is the template for the other 19 modules, so quality and adherence to the anatomy matter more than speed.

## File structure (Plan 3)

- Create: `programming-mastery/modules/A1-notional-machine.md` (the teaching file; 9-part anatomy)
- Create: `programming-mastery/exemplars/A1/foundations.md`, `.../working.md`, `.../advanced.md` (~3 runner-verified drills per tier)

---

### Task 1: Research + author A1 module file and exemplars

- [ ] **Research (first):** mine the notional-machine literature (Sorva 2013, du Boulay 1986, runtime-dynamics misconception catalogs) and Python execution-model gotchas (late-binding closures, mutable default args, aliasing/shared references, name-rebinding vs mutation, scope/`UnboundLocalError`, evaluation order, augmented assignment on mutables, iterator exhaustion, recursion stack). Read the engine refs so A1 plugs in: `references/drill-generation.md` (the generation-spec format A1 must instantiate), `references/coaching-loop.md`, `references/assessment.md` (its A1 entry task — stay consistent), `references/evidence-base.md` (Findings 1, and the A1 grounding), and `runtime/python/runner.py` (the API).
- [ ] **Author `modules/A1-notional-machine.md`** with the spec §5 anatomy — headings must satisfy the validator (section names containing: *evidence basis, soft prerequisites, mental model, worked example, drill-generation spec, frontier band, mastery rubric, anti-patterns, transfer task*); `[Verified]` badge; `# ` title; filename `A1-notional-machine.md`:
  1. **Evidence basis** `[Verified]` — Sorva 2013, du Boulay 1986 (cite via evidence-base).
  2. **Soft prerequisites** — none (foundational).
  3. **The mental model** — a program is a machine with state (variables, call stack, heap, program counter); execution = deterministic state transitions; *simulate, don't read intent*.
  4. **Worked example** — a **state-table** trace of a small function, shown in full (Foundations) with a note on **fading** it at Advanced/Frontier (expertise reversal).
  5. **Drill-generation spec** — instantiate the `drill-generation.md` format for A1: tier definitions (Foundations/Working/Advanced), the **parameter space** to vary, the **common-error catalog** (each error + what it diagnoses), grading mode = **executable ground truth**.
  6. **Frontier band** — escalation beyond Advanced (deep recursion stacks, generators/lazy eval, evaluation order, async/interleavings → links A4).
  7. **Mastery rubric** — observable per-tier bars (e.g., Working = predicts final state+output on 4/5 unseen drills incl. ≥1 aliasing/closure case + can articulate the state model).
  8. **Anti-patterns & evidence caveat** — reading-for-intent instead of simulating; trusting names; skipping the stack. (Pure `[Verified]` module — minimal caveat.)
  9. **Transfer task** — trace a function from the learner's own codebase that once surprised them; explain the surprise as a state-machine event.
- [ ] **Author the exemplars** (`exemplars/A1/{foundations,working,advanced}.md`), ~3 drills per tier. Each drill = prompt (a code snippet + "what does this print / what's the final state?") + **runner-verified** answer key + the common-error(s) it diagnoses. Span the parameter space (don't repeat one gotcha). Suggested coverage: Foundations = straight-line + one loop + 2–3 vars; Working = closures, aliasing, mutable defaults, early-return; Advanced = recursion stack, generators/iterator exhaustion, evaluation order, augmented assignment on mutables.
- [ ] **Verify EVERY snippet** by running it (`python3 programming-mastery/runtime/python/runner.py <file>` or `run_snippet`). Paste the real `stdout`/`status` as the answer key. If a snippet's behavior surprises you, fix the drill or the key to match reality — never assert an unverified output.
- [ ] **Validator must pass:** `python3 tools/validate_modules.py programming-mastery/modules/` → `ok: 1 module file(s) valid`.
- [ ] **Commit:** `feat(module): A1 notional machine — teaching file + runner-verified exemplars`

### Task 2: Review (spec/anatomy + executable verification)

- [ ] **Anatomy + coverage:** the module has all 9 required sections; the drill-generation spec instantiates the engine's format; the common-error catalog entries each say *what they diagnose*; worked example fades by tier; consistent with `assessment.md`'s A1 entry task.
- [ ] **Independent executable check:** re-run EVERY exemplar snippet through the runner and confirm the pasted answer key matches the real output exactly. Flag any mismatch (a fabricated/também stale key).
- [ ] **Consistency:** tier names; runner API/path; `[Verified]` badge; no citations absent from evidence-base.
- [ ] **Validator:** confirm `ok: 1 module file(s) valid`. Fix any findings, then re-verify.

### Task 3: Coached-session smoke test (the milestone)

- [ ] Run a real A1 session end-to-end against the engine + module: (1) entry assessment routes a learner to an A1 tier; (2) Teach presents the mental model + worked example; (3) Generate a fresh drill at that tier; (4) the "learner" makes a prediction; (5) **Diagnose by running the drill through the runner** and comparing; (6) give direct feedback naming the specific gap; (7) a **Frontier escalation** step. Confirm the pause/no-spoiler discipline is followed. Capture a short transcript.
- [ ] **Commit** the smoke-test transcript under `docs/superpowers/` if useful (optional).

---

## Whole-plan acceptance

- [ ] `python3 tools/validate_modules.py programming-mastery/modules/` → `ok: 1 module file(s) valid`.
- [ ] Every A1 exemplar's answer key matches live runner output (zero unverified keys).
- [ ] `python3 -m pytest` still green (no code changed).
- [ ] A coached A1 session runs end-to-end with live execution + a Frontier escalation.

## Self-review

- Anatomy completeness (9 sections, validator green); generation-spec matches `drill-generation.md`; common-error catalog diagnostic; exemplars span the parameter space and are all runner-verified; consistency with `assessment.md` A1 task; `[Verified]` badge only where earned; A1 is a clean template the other 19 modules can copy.
