# Programming Mastery — Design Spec (v1)

- **Date:** 2026-06-22
- **Status:** Approved in principle; revised for dynamic drill generation + comprehensive/staff scope (pending final spec review)
- **Working dir:** `/home/shimin/agents/programming-agent`
- **Skill name (provisional):** `programming-mastery`

## 1. Goal

Build a training scaffolding — **curriculum content wrapped in a Claude Code coaching skill** — that helps working developers from junior through **staff** get *measurably* better, grounded in what the empirical literature actually supports (not folklore).

It teaches **representation and comprehension skills** (what actually separates experts from novices in the research), delivers them through an **agent-coached, feedback-rich practice loop with dynamically generated drills**, supports **unbounded depth** so even senior engineers keep being challenged, and **measures within-learner improvement** on concrete performance tasks.

### Success criteria

1. A developer invokes the skill, is assessed, and is routed to the right tier *per skill*.
2. Each session ends with a *specific, diagnosed* gap and targeted feedback — not a pass/fail score.
3. Improvement is demonstrable as a **baseline → re-assessment delta** on freshly generated performance tasks, plus transfer evidence on the learner's own code.
4. The ceiling is high enough that a staff engineer keeps hitting their edge (the **Frontier band**).
5. Every claim the skill makes is traceable to its evidence basis and honestly tier-labeled.

## 2. Evidence base (the grounding)

The differentiator: the curriculum is built on fact-checked findings and openly distinguishes **verified science** from **practitioner canon** from **debunked folklore**. Full grounding lives in `references/evidence-base.md`. Summary:

### Verified findings we build on (high confidence — from the fact-checked research pass)

| Finding | Sources | Module |
|---|---|---|
| **Notional machine**: the durable barrier is understanding *runtime dynamics of execution*, not syntax; teach it as an explicit objective. *The single most curriculum-actionable finding.* | Sorva 2013 (ACM TOCE 13(2), doi 10.1145/2483710.2483713); du Boulay 1986 | 01 |
| **Expertise = better representation**: experts chunk code into larger semantic units & recognize patterns; novices process line-by-line on surface syntax. Signature evidence: expert recall advantage shrinks on *scrambled* code (chess-chunking analogue). Shrinks but doesn't vanish. | Shneiderman 1976; McKeithen et al. 1981; SLR arXiv:2212.07763; Sala & Gobet 2017 (r≈.42) | 02 |
| **Beacons & programming plans** are real cues experts exploit. | Soloway & Ehrlich 1984 (IEEE TSE); Brooks 1983; Storey 2006; Crosby et al. 2002 | 02 |
| **Comprehension is active & hypothesis-driven**: top-down (Brooks) + bottom-up (Pennington), mode-switching (von Mayrhauser & Vans 1995). | arXiv:2212.07763; Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995 | 03, 04 |
| **Reading → tracing → writing**: code-tracing skill and "explain in plain English" track with code-*writing* ability. | BRACElet — Lister et al., Lopez et al. 2008 | 03 |
| **Years ≠ expertise**: expertise is poorly operationalized; tenure is a weak/unreliable proxy (r≈.27). Assess by performance. | Bidlake, Aubanel & Voyer 2020; Baltes & Diehl 2018; Peitek/Parnin/Apel 2022 | assessment |

### Folklore we explicitly reject

| Myth | Reality | Source |
|---|---|---|
| **"Camel has two humps"** aptitude test sorts born-programmers from the rest | Retracted by its own author; no aptitude test found; "100% accurate" claim was false and written during an SSRI-induced manic episode; at best a weak predictor | Bornat 2014 retraction; Retraction Watch 2014 |
| **10,000-hour / 10-year rule**; deliberate practice as the dominant cause | Strong thesis is false: DP explains only ~12–14% of variance overall (~1% professions); evidence inflated ~4× by retrospective recall; loses nearly all power at elite levels; time-to-mastery varies ~8×. *Live dispute:* Ericsson contests magnitude; numbers are from music/sports/chess, NOT software. | Macnamara et al. 2014; Hambrick et al. 2018, 2020; Gobet & Campitelli 2007 |

### Refuted under verification — do NOT author modules asserting these

Sound right, did not survive adversarial fact-checking:

- "Teach the catalog of programming plans + discourse rules ⇒ expertise" (clean teachable decomposition) — refuted; partly notation-dependent (Gilmore & Green 1988).
- "Experts use function-based mental models, novices use data-flow" — refuted 0-3.
- "Two-model (program-model / situation-model) theory" — refuted 0-3.
- "Experts search breadth-first, novices depth-first" — refuted 0-3.
- "Systematic control/data-flow tracing *causally* yields better mental models & fewer errors than as-needed reading" — refuted 1-2. → Teach tracing as *a* strategy; don't claim causal superiority.

### Evidence honesty for craft & staff modules (06–12)

Modules 06–12 rest on **practitioner canon and extrapolation**, NOT the fact-checked research pass. Their grounding must be assembled and verified *during authoring*, and each carries a `[Practitioner-canon]` badge with caveats. Candidate sources (to be verified, not yet vetted): Ousterhout *A Philosophy of Software Design*; Fowler *Refactoring*; Feathers *Working Effectively with Legacy Code*; Tornhill *Your Code as a Crime Scene*; Kleppmann *Designing Data-Intensive Applications*; Agans *Debugging*; Bacchelli & Bird 2013 (*Modern Code Review*, ICSE — module 12 has *some* genuine empirical support). The skill must not present these as "verified."

### The caveat that shapes the whole design

Nearly all the *verified* evidence is drawn from **novices** in intro courses, mostly **1976–1995**, in BASIC/Pascal/Fortran. Whether teaching these skills *causally improves experienced developers* is an **open question**, and staff-level depth is largely extrapolation. Consequences: **measurement is built in from day one**; every module ends with a **transfer task on the learner's real code**; depth beyond the evidence is honestly labeled.

### Reading spine (book canon)

*The Programmer's Brain* (Hermans) — core; *Why Programs Fail* (Zeller) — 04/10; *The Psychology of Computer Programming* (Weinberg) — context; *Peak* (Ericsson & Pool) — 05, read critically; *A Philosophy of Software Design* (Ousterhout) & *Refactoring* (Fowler) — craft 06–08; *Working Effectively with Legacy Code* (Feathers) & *Designing Data-Intensive Applications* (Kleppmann) — staff 09–11.

## 3. Scope (v1)

**In:** 12 modules (5 verified-core + 3 craft + 4 staff, all tier-labeled); per-skill tiered routing **plus an unbounded Frontier band**; entry assessment; **dynamic drill generation** anchored by golden exemplars; **executable ground truth** for verifiable drills via a Python runtime; coaching loop; progress/mastery tracker; a module-authoring template so the curriculum is extensible.

**Out (future):** non-Python execution runtimes; spaced-repetition scheduling engine; team/cohort dashboards; IDE integration; an empirical transfer-validation study; backlog modules (performance/mechanical-sympathy; distributed-execution as its own module; communication/mentoring).

## 4. Architecture (coach skill + module library + generation engine)

Progressive disclosure, dynamic drills anchored by curated exemplars, executable grading where possible.

```
programming-mastery/                  # built here; installed to ~/.claude/skills/
  SKILL.md                            # the coach: routing + coaching loop + session protocol
  references/
    evidence-base.md                  # §2 expanded: findings, folklore, refuted-list, citations, tiers
    assessment.md                     # entry/routing assessment + per-skill mastery rubrics
    coaching-loop.md                  # locate → teach → generate → attempt → diagnose → feedback → adapt
    drill-generation.md               # generation spec format; executable-ground-truth; self-check; Frontier escalation
    authoring-new-modules.md          # template + process for adding modules (extensibility)
  modules/
    01-notional-machine.md            # ── core (Verified) ──
    02-code-reading-and-chunking.md
    03-execution-tracing.md
    04-systematic-debugging.md
    05-designing-your-practice.md     #     meta-capstone; revisited throughout
    06-managing-complexity.md         # ── craft (Practitioner-canon, labeled) ──
    07-naming.md
    08-refactoring-judgment.md
    09-large-codebase-comprehension.md  # ── staff (mixed / canon, labeled) ──
    10-production-and-concurrency-debugging.md
    11-architectural-judgment.md
    12-code-review.md
  exemplars/
    <module>/<tier>/                  # ~3 golden drills/tier: generator few-shot calibration + worked examples + offline fallback
  runtime/
    python/                           # sandboxed runner so the coach can EXECUTE code drills for ground truth (v1: Python)
  progress-template.md                # per-learner mastery tracker (the measurement instrument)
```

- **Progressive disclosure:** `SKILL.md` stays lean; the coach loads only the module + tier in play.
- **Dual-use:** a human reads `modules/*.md` directly (the curriculum); invoking the skill activates the coach (the wrapper).
- **Drills are generated, not banked:** each module ships a *generation spec* + a *small golden exemplar set*; the coach generates fresh drills per session. This makes teaching-to-the-test structurally impossible and removes the authoring bottleneck.
- **Build vs install:** developed here; installed by copy/symlink to `~/.claude/skills/programming-mastery/`.

## 5. The module model (anatomy of every `modules/NN-*.md`)

Fixed structure so one coaching protocol drives all modules:

1. **Evidence basis** — finding + citation + tier badge `[Verified]` / `[Practitioner-canon]`. A module may carry a *mixed* badge when its concept and method differ in evidentiary status (e.g., 04, 10: verified comprehension model, canon-supported method).
2. **The mental model** — the core concept in plain language.
3. **Worked example** — an expert demonstration to imitate.
4. **Drill-generation spec** — tier definitions (the difficulty model), the parameter space to vary, the **common-error catalog** to target, and the **grading mode**: *executable ground truth* (coach runs the code) vs *rubric + exemplars* (judgment skills). Points into `exemplars/`.
5. **Frontier band** — how difficulty escalates *beyond* Advanced (what knobs increase, what staff-level looks like).
6. **Mastery rubric** — the *observable performance* bar to pass at each named tier.
7. **Anti-patterns & evidence caveat** — what the skill is *not*; for craft/staff modules, the explicit "rests on canon, not verified research" note.
8. **Transfer task** — apply the skill to the learner's *own real code*.

## 6. The twelve modules

| # | Module | Tier badge | Core idea |
|---|---|---|---|
| 01 | Notional machine / execution model | `[Verified]` | A program is a machine with state; execution = deterministic state transitions; simulate, don't read intent. |
| 02 | Code reading & chunking | `[Verified]` | Read for structure not syntax; recognize beacons/patterns; chunk into semantic units; summarize unfamiliar code fast. |
| 03 | Execution tracing & explain-in-plain-English | `[Verified]` | Hand-simulate execution; produce call trees; explain purpose in 1–3 sentences. Reading→tracing→writing. |
| 04 | Systematic / hypothesis-driven debugging | `[Verified]` model + `[Canon]` method | Debugging as science: observe → hypothesize → predict → test → narrow (bisection). Not print-spraying. (Causal superiority of tracing was refuted — frame as disciplined process.) |
| 05 | Designing your own practice *(meta-capstone)* | `[Verified]` meta | What well-designed practice actually is: quality + immediate feedback + individualized targeting, NOT hour-dosing. Self-measurement. Revisited throughout. |
| 06 | Managing complexity / abstraction | `[Practitioner-canon]` | Decomposition, abstraction boundaries, deep vs shallow modules. |
| 07 | Naming | `[Practitioner-canon]` | Names as cheapest documentation; precision, consistency, intent. |
| 08 | Refactoring judgment | `[Practitioner-canon]` | When (and when not) to refactor; behavior-preserving change under test. |
| 09 | Large-codebase comprehension | `[Verified]` core + `[Canon]` scale | Orient in a big unfamiliar repo fast: entry points, architecture reconstruction, mental map under time pressure. Extends 02/03 to repo scale. |
| 10 | Production & concurrency debugging | `[Verified]` model + `[Canon]` method | Heisenbugs, races, observability-driven debugging, reasoning about live-system incidents. Extends 01/04 to systems scale. |
| 11 | Architectural & technical judgment | `[Practitioner-canon]` | Designing for change & failure; tradeoff analysis under uncertainty; when NOT to build. |
| 12 | Code review as a skill | `[Some empirical]` + `[Canon]` | Reading + judgment + communication; reviewing others' code well; precise feedback; catching what matters. |

## 7. The coaching loop (`references/coaching-loop.md`, run by `SKILL.md`)

1. **Locate** — read progress file; pick target skill + tier (or run entry assessment if new).
2. **Teach** — present concept + worked example (skip if already mastered).
3. **Generate** — produce a *fresh* drill at the learner's tier from the module's generation spec + golden exemplars; in the **Frontier band**, escalate difficulty against the demonstrated ceiling.
4. **Attempt** — learner does the drill (writes the trace / plain-English explanation / bug hypothesis / review).
5. **Diagnose** — obtain ground truth: **run the code** for executable drills; apply **rubric + exemplars** for judgment drills. Name the *specific* gap, not just pass/fail.
6. **Feedback** — targeted, specific, immediate; expert solution side-by-side. (The active ingredient the DP research supports.)
7. **Adapt** — pass → harder drill / next skill / push into Frontier; fail → easier drill / re-teach sub-skill. Update progress file.
8. **Spaced review** — periodically re-surface a mastered skill to check retention.

## 8. Tiering, assessment & measurement

No validated absolute measure of expertise exists, so we measure **within-learner deltas on concrete performance tasks** against the learner's own baseline.

- **Tiers:** Foundations / Working / Advanced as **named checkpoints**, assigned **per skill**, plus an open-ended **Frontier band** above Advanced where the generator presses until failure. The Frontier gives advanced/staff learners a moving "current ceiling" metric (e.g., "Frontier level 7 on tracing").
- **Entry assessment** (`references/assessment.md`): one short *performance* task per core skill, scoring **process and product**, routing each skill to a tier. (The debugging task scores your first three hypotheses + how you'd test them, not whether you found the bug.)
- **Mastery rubrics:** observable per-tier gates, recorded with evidence.
- **Progress tracker** (`progress-template.md`): per-skill table — tier, baseline, drills passed, current Frontier level, and a running list of **recurring error patterns** (the diagnostic gold).
- **Headline delta:** because drills are generated fresh, held-out re-assessment is free — re-run the entry battery later with new items at fixed checkpoints; baseline-vs-now = measurable improvement. Per-module transfer tasks track real-code transfer.
- **Honesty:** the skill states out loud that this is within-person progress on defined skills, not a certified expertise grade.

### Progress tracker format (markdown, agent-parseable)

| Skill | Tier | Frontier | Baseline (date/score) | Drills passed | Recurring errors | Last reviewed |
|---|---|---|---|---|---|---|
| Notional machine | Working | — | 2026-06-22: 2/5 | 7/9 | closure capture; aliasing | 2026-06-29 |
| Execution tracing | Advanced | L4 | 2026-06-22: 4/5 | 15/16 | deep-recursion stack | 2026-06-30 |

## 9. Design principles & guardrails

- **Honesty about evidence** — verified vs canon vs refuted is visible everywhere; never oversell.
- **Performance, not tenure** — all routing/gating is on observed performance.
- **Executable ground truth** — for verifiable drills the coach *runs the code*; it never grades against a guessed answer key.
- **Generation anchored by golden exemplars** — drills are generated for volume/freshness but calibrated by curated gold standards; not free-form.
- **Feedback-rich, individualized practice** — quality and specificity over volume; no hour-quotas.
- **Unbounded depth** — the Frontier band means the ceiling fits staff engineers.
- **Transfer to real code** — every module ends on the learner's actual codebase.
- **No aptitude gatekeeping** — skill is trainable; reject the "two humps" framing explicitly.
- **Extensible by design** — adding a module is a documented, repeatable operation (`authoring-new-modules.md`), not a rewrite.
- **Small, well-bounded units** — one module = one skill = one file the coach can hold in context (teaching files ≤ ~200 lines).

## 10. Risks & open questions

1. **Generated drills can be mis-leveled or have wrong answer keys.** Mitigations: executable ground truth where possible; golden-exemplar calibration; a generation **self-check** pass; a learner "this looks wrong" escape hatch; rubric+exemplar grading for judgment drills (acknowledged softer).
2. **Executing generated/learner code is a safety risk.** Mitigation: a sandboxed runtime (resource-limited subprocess/container); never execute untrusted code outside the sandbox. v1 supports Python only.
3. **Judgment modules (06, 07, 08, 11, parts of 12) lack executable ground truth** — grading is inherently softer. Mitigation: stronger rubrics + more exemplars; surface uncertainty to the learner.
4. **Novice-evidence → working/staff-dev transfer is unproven; staff depth is extrapolation.** Mitigation: transfer tasks + measurement; explicit tier badges; honest framing.
5. **Teaching-to-the-test** — largely solved by fresh generation, but watch generator mode-collapse (repetitive drills). Mitigation: parameter-space coverage tracking.
6. **Modern/AI-assisted revalidation.** Classic findings predate IDEs, large codebases, and LLM-assisted workflows; magnitudes for today's devs are uncertain. Track as an open question.
7. **Coaching quality depends on the generation spec encoding common errors + what they diagnose**, not just correct answers — so the coach can name the specific gap.

## 11. v1 build order

1. `references/evidence-base.md` (grounding — everything cites it).
2. `SKILL.md` + `references/coaching-loop.md` + `references/assessment.md` + `references/drill-generation.md` (the engine, incl. executable-ground-truth + self-check + Frontier escalation).
3. `runtime/python/` sandboxed runner + `progress-template.md` (execution + measurement instruments).
4. **Module 01 end-to-end** — mental model + worked example + generation spec + golden exemplars + executable grading + Frontier band. The reference implementation of the module model.
5. Core 02–05, then craft 06–08, then staff 09–12.
6. `references/authoring-new-modules.md` — extract the template from how 01–12 were actually built.
7. Smoke-test: a full coached session on module 01, including live code execution for ground truth and a Frontier escalation.
