# Programming Mastery — Engine Content (Plan 2) Implementation Plan

> **For agentic workers:** This is an **authoring** plan (prose, not code — no TDD). Execute each task by authoring the file from the cited spec sections. Acceptance per task = the listed required content is present, internally consistent, and free of fabricated citations. Steps use checkbox (`- [ ]`) syntax.

**Goal:** Author the coaching engine's reference content so an agent can run a coached session end-to-end. (The first *live* session — with real code execution — lands in Plan 3, which adds module A1.)

**Architecture:** Four `references/*.md` files plus an expanded `SKILL.md`, all derived from the design spec. These are instructions the coach (the agent) follows; the only code (runner, validator) already shipped in Plan 1.

**Tech Stack:** Markdown. No code changes. `python3 -m pytest` must stay green (sanity only).

**Spec:** `docs/superpowers/specs/2026-06-22-programming-mastery-skill-design.md` (the authoring source of record — §2, §5, §7, §8, §12, §13).

---

## Method note (why no TDD)

This plan authors prose. "Tests" are: (a) the existing pytest suite stays green (no code touched); (b) `SKILL.md`'s references all resolve to real files; (c) a **tabletop dry-run** — an agent can follow `SKILL.md → assessment.md → coaching-loop.md → drill-generation.md` without hitting an undefined reference or gap. A full *live* coached session requires module A1 (Plan 3).

## Per-task protocol: research → author (go deep, as you go)

Each task is executed by a **research-capable subagent that researches the topic deeply *before* authoring** — web search/fetch for primary sources, plus the cloned sibling repo at `/tmp/learning-opportunities`, plus the spec. The subagent **verifies and deepens** the spec's claims/citations (find the real paper, confirm the finding's direction/magnitude, add precise detail), and **flags anything that doesn't check out** — it never fabricates a citation or overstates evidence. Research foci:

- **evidence-base.md** — verify each verified-finding and instructional-pillar citation against primary sources; confirm effect directions (and magnitudes where claimed); keep the strongest 1–2 sources per claim; preserve the verified/canon/refuted honesty.
- **coaching-loop.md** — research the learning-science *delivery* techniques (generation effect, desirable difficulties, fading, retrieval/pre-testing) to write authoritative, correctly-hedged instructions; mine `learning-opportunities` SKILL.md / PRINCIPLES.md for proven phrasings of the pause/no-spoiler discipline.
- **drill-generation.md** — research worked-example / assessment-item / drill design and executable-grading patterns; confirm the Plan-1 runner interface exactly.
- **assessment.md** — research programming-skill assessment design; locate the **exact** validated measure items + scales (Developer Thriving / Learning Culture, AI Skill Threat, Coding Self-Efficacy) from the open-access supplements; cite and attribute (CC-BY-SA).
- **SKILL.md** — lighter research; primarily integrates the above into a lean entry point.

**Invariants every subagent must honor:** runner path is skill-relative (`runtime/python/runner.py`); `RunResult` fields = `status | stdout | stderr | returncode | duration_s`; tier names = Foundations / Working / Advanced + Frontier; the 20 module IDs/badges match spec §6; cite only verified sources; honor CC-BY / CC-BY-SA attribution.

## Licensing

`evidence-base.md` and `assessment.md` incorporate material surfaced by Cat Hicks' *Learning Opportunities* (spec §13). Findings/citations are used freely **with credit (CC-BY)**. The affective survey items in `assessment.md` are reproduced from CC-BY-SA-4.0 measures, so that section carries an explicit attribution block (Hicks, Lee, Foster-Marks / Ramsey) and a share-alike note.

## File structure (Plan 2)

- Create: `programming-mastery/references/evidence-base.md`
- Create: `programming-mastery/references/coaching-loop.md`
- Create: `programming-mastery/references/drill-generation.md`
- Create: `programming-mastery/references/assessment.md`
- Modify: `programming-mastery/SKILL.md` (expand the skeleton body)

---

### Task 1: `references/evidence-base.md`

**Author from spec §2 (+ §12 priority, §13 attribution).**

- [ ] **Required content:**
  - Verified-findings table with citations (notional machine, chunking/beacons, active comprehension, plan-before-code, reading→tracing→writing, years≠expertise).
  - The **learning-science instructional-pillar** table (generation/testing, pre-testing, spacing, worked-example fading + expertise reversal, desirable difficulty, learning≠performance, fluency/effort illusions, metacognition) with citations.
  - **Folklore rejected** (camel two-humps; strong 10k-hour) and the **refuted-list** ("do NOT author modules asserting these").
  - Evidence-tier definitions: `[Verified]` / `[Verified-adjacent]` / `[Practitioner-canon]`.
  - The novice→working/staff **transfer caveat**; the **reading spine**; a full reference list.
  - An **attribution note** crediting *Learning Opportunities* (Cat Hicks) for the instructional pillar (CC-BY).
- [ ] **Acceptance:** every evidence badge and citation used by other engine files / modules is traceable here; use ONLY citations that appear in the spec (no fabrication).
- [ ] **Commit:** `feat(content): evidence-base.md grounding for programming-mastery`

### Task 2: `references/coaching-loop.md`

**Author from spec §7.**

- [ ] **Required content:**
  - The 8 loop steps (locate → teach → generate → attempt → diagnose → feedback → adapt → spaced-review) with concrete coach instructions.
  - The **Delivery Disciplines** section: **pause/no-spoiler** (explicit: *end the message after the question; generate no answer, hints, "consider…", suggested responses, or teaching content*; allow only a content-free nudge / escape hatch), pre-test-before-reveal, fading scaffolding (the setup ladder; move *up* when stuck), direct error feedback / no false credit, desirable difficulty, prefer-directing-to-files, session restraint (cap unsolicited offers; stop on decline).
  - The exact pause-point markers + one worked example of a pause.
- [ ] **Acceptance:** an agent can run a session step-by-step from this file alone; the no-spoiler rule is unambiguous and un-rationalizable.
- [ ] **Commit:** `feat(content): coaching-loop.md with delivery disciplines`

### Task 3: `references/drill-generation.md`

**Author from spec §5 (point 5), §7, §13.**

- [ ] **Required content:**
  - The **generation-spec format** each module supplies (tier definitions, parameter space, common-error catalog, grading mode).
  - The **executable-ground-truth protocol**: write the snippet → call the runner (skill-relative `runtime/python/runner.py`) → parse `RunResult` JSON (`status`/`stdout`/`stderr`/`returncode`/`duration_s`) → grade the learner's prediction against the *real* output; never guess.
  - The **rubric + exemplar** path for judgment drills.
  - The **generation self-check** (known answer? well-leveled? parameter-space coverage to avoid mode-collapse).
  - **Frontier escalation** rules.
  - The **exercise-format catalog** (Prediction→Observation→Reflection, Generation→Comparison, Trace-the-path, Debug-this, Teach-it-back, Retrieval check-in + elaborative interrogation, interleaving, varied-context, concrete→abstract, error analysis, example-problem pairs, completion prompts) as reusable formats.
- [ ] **Acceptance:** a coach can generate AND grade one executable drill and one judgment drill from this file; the runner path + interface match Plan 1 exactly.
- [ ] **Commit:** `feat(content): drill-generation.md (executable ground truth + format catalog)`

### Task 4: `references/assessment.md`

**Author from spec §8.**

- [ ] **Required content:**
  - The **entry/routing assessment**: one *performance* task per core skill (at least the Track A/B spine + C1, E3, F1), each scoring **process AND product**, mapping result → **recommended tier per skill** (Foundations/Working/Advanced); **never gates** sampling.
  - The **per-skill mastery rubrics** (observable bars).
  - The **held-out re-assessment** protocol (fresh items at fixed checkpoints → baseline-vs-now delta).
  - The **learning≠performance** caveat (weight delayed re-assessment + transfer over same-session streaks).
  - The **optional affective self-report layer** (Learning Culture, AI Skill Threat, Coding Self-Efficacy) with the **CC-BY-SA attribution block** (Hicks et al.) and pre/post + **reporting guardrails** (descriptive over inferential; variance alongside means; no causal overclaiming; no confabulated norms).
- [ ] **Acceptance:** a coach can run entry assessment for a new learner and emit a recommended per-skill tier + a baseline row for the progress tracker.
- [ ] **Commit:** `feat(content): assessment.md (routing + rubrics + affective layer)`

### Task 5: `SKILL.md` (expand from skeleton)

**Author from spec §4 + §6 module index.**

- [ ] **Required content:** replace the skeleton body with the real coach: role; how to start (load `coaching-loop.md`; run `assessment.md` for new learners; create the tracker from `progress-template.md`); the **20-module index table** (ID · module · track · tier badge · one-line) so the coach can route; pointers to `references/*` and `modules/<ID>` + `exemplars/<ID>/<tier>/`; honesty rules (respect badges; executable ground truth via the **skill-relative** runner path from the Plan-1 fix; within-person, not certified); session restraint.
- [ ] **Acceptance:** `SKILL.md` alone tells the coach how to run a session and where everything is; keep ≤ ~150 lines (progressive disclosure — depth lives in `references/`); runner path stays skill-relative.
- [ ] **Commit:** `feat(content): expand SKILL.md into the full coach entry point`

---

## Whole-plan acceptance

- [ ] `python3 -m pytest` still green (no code changed).
- [ ] All 5 files present; every reference in `SKILL.md` resolves to a real file.
- [ ] **Tabletop dry-run:** an agent can follow `SKILL.md → assessment → coaching-loop → drill-generation` without an undefined reference. (Live session with real execution = Plan 3.)

## Self-review

- Coverage vs spec §2 / §5 / §7 / §8 / §13 — each required item maps to authored content.
- Consistency: runner path + `RunResult` interface match Plan 1; tier names (Foundations/Working/Advanced/Frontier) consistent; the 20 module IDs match spec §6; tier badges match.
- No fabricated citations (only those in the spec). Attribution blocks present where CC-BY-SA material is reproduced.
