# Programming Mastery — Verification Cluster (Plan 4a) Implementation Plan

> **For agentic workers:** Authoring plan (research-as-you-go). Runner-verify executable drills; golden exemplars for judgment drills. Modules follow the **A1 reference template** (`modules/A1-notional-machine.md`).

**Goal:** Author the 5 AI-era verification-cluster modules — **A2, A3, B3, E3, F1** — on the A1 template. Highest-impact subset (spec §12), and it deliberately exercises **both grading paths**: executable ground truth (A2/A3 + parts of B3/F1) and **rubric + exemplars** (E3 + parts of B3/F1) — the latter not yet validated by A1.

**Architecture:** each module = `modules/<ID>-*.md` (spec §5 nine-part anatomy; passes the validator) + `exemplars/<ID>/{foundations,working,advanced}.md`. Plugs into the Plan-2 engine; stays consistent with each module's existing entry task in `references/assessment.md`.

**Tech Stack:** Markdown; executable drills verified via `programming-mastery/runtime/python/runner.py`; `tools/validate_modules.py` must end at `ok: 6 module file(s) valid`; pytest stays green.

**Spec/refs:** design spec §5/§6/§12; engine `references/*`; **template = `modules/A1-notional-machine.md`**.

---

## Method

5 research-author subagents (one per module, dispatched **in parallel** — modules touch disjoint files). Each subagent **researches the topic against primary sources**, authors the module + exemplars on the A1 template, and **verifies**:
- executable drills → run through the runner, paste real output as the key;
- judgment drills → provide gold-standard exemplars, AND run any embedded code (e.g. confirm a code-review drill's *planted bug* really is a bug).

Subagents **write files but do not commit** (avoids git races in parallel); the controller integrates, runs the validator + pytest, then dispatches **per-module review** (re-verify) before merge.

### Per-module foci

| Mod | Badge | Research foci | Grading mode | Verify |
|---|---|---|---|---|
| **A2** Code reading & chunking | `[Verified]` | chunking, beacons, programming plans (Shneiderman, McKeithen, Soloway & Ehrlich, Hermans *Programmer's Brain*) | mixed | runner for "trace this chunk"; gold rubric for summaries/beacon-ID |
| **A3** Execution tracing & explain | `[Verified]` | BRACElet reading→tracing→writing (Lister, Lopez); tracing pedagogy | executable + rubric | runner for traces/output/call-trees; gold for plain-English explanations |
| **B3** Testing & specifying correctness | `[Canon + some empirical]` | edge cases, properties, equivalence classes, TDD/property-based-testing evidence | mixed | runner: run the learner's tests against buggy vs correct impls |
| **E3** Code review | `[Some empirical] + [Canon]` | Bacchelli & Bird 2013 (modern code review); effective-review practices | rubric + exemplars | run each drill's **planted bug** to confirm it is real; gold review = the issue list |
| **F1** Metacognition & calibration | `[Verified-adjacent]` | confidence calibration & overconfidence (Tankelevitch 2024; METR/Fernandes from evidence-base AI-era section) | executable + metacog | runner to check prediction accuracy; calibration = confidence vs measured correctness |

---

### Task 1: Research-author the 5 modules (parallel, no-commit)

- [ ] Dispatch one research-author subagent per module (A2, A3, B3, E3, F1). Each: read the **A1 template** + the engine refs + its own entry task in `assessment.md`; research its foci; author `modules/<ID>-*.md` (9-part anatomy, `# ` title, correct badge, filename) + `exemplars/<ID>/{foundations,working,advanced}.md` (~3 drills/tier); verify per the table (unique temp paths like `/tmp/<ID>_d.py`); **do not git commit**; report.

### Task 2: Integrate

- [ ] Commit the 5 modules + exemplars. `python3 tools/validate_modules.py programming-mastery/modules/` → `ok: 6 module file(s) valid`. `python3 -m pytest -q` → 14 passed.

### Task 3: Per-module review (re-verify)

- [ ] One review subagent per module: independently re-run every executable drill through the runner (confirm keys match); for judgment modules, confirm planted bugs are real and the gold answers are sound; check the 9-section anatomy, the grading-mode declaration, consistency with the engine + the `assessment.md` entry task + the A1 template; validator stays `ok: 6`. Fix findings.

### Task 4: Merge to master.

---

## Whole-plan acceptance

- [ ] `validate_modules` → `ok: 6 module file(s) valid`.
- [ ] Every executable drill key is runner-verified; every judgment drill's embedded code is verified (planted bugs are real bugs).
- [ ] Each module is consistent with its `assessment.md` entry task and matches the A1 template's anatomy/quality.
- [ ] `pytest` green; the rubric+exemplar grading path (E3/F1) is now demonstrated.

## Self-review

- All 5 modules pass the validator; grading modes declared correctly (executable vs rubric); exemplars span the parameter space; executable keys runner-verified; judgment golds sound; citations trace to `evidence-base.md`; no module drifts from the A1 template structure.
