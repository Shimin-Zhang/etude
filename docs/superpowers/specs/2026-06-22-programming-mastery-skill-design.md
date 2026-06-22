# Programming Mastery — Design Spec (v1)

- **Date:** 2026-06-22
- **Status:** Approved in principle; revised to a 20-module sampleable "buffet" with dynamic drill generation, track-stable IDs, staff ceiling; integrated learning-science **delivery techniques** borrowed from Cat Hicks' *Learning Opportunities* project (§13) (pending final spec review)
- **Working dir:** `/home/shimin/agents/programming-agent`
- **Skill name (provisional):** `programming-mastery`

## 1. Goal

Build a training scaffolding — **curriculum content wrapped in a Claude Code coaching skill** — that helps working developers from junior through **staff** get *measurably* better, grounded in what the empirical literature actually supports (not folklore).

It is a **buffet**: an extensive set of fine-grained, self-contained skill modules a developer samples as they wish. It teaches **representation, construction, and comprehension skills** (what actually separates experts from novices in the research), delivers them through an **agent-coached, feedback-rich practice loop with dynamically generated drills**, supports **unbounded depth** so even senior engineers keep being challenged, and **measures within-learner improvement** on concrete performance tasks.

### Success criteria

1. A developer invokes the skill, is assessed, and is *recommended* a tier and starting modules per skill — but can freely sample any module.
2. Each session ends with a *specific, diagnosed* gap and targeted feedback — not a pass/fail score.
3. Improvement is demonstrable as a **baseline → re-assessment delta** on freshly generated tasks, plus transfer evidence on the learner's own code.
4. The ceiling is high enough that a staff engineer keeps hitting their edge (the **Frontier band**).
5. Every claim the skill makes is traceable to its evidence basis and honestly tier-labeled.

## 2. Evidence base (the grounding)

The differentiator: the curriculum is built on fact-checked findings and openly distinguishes **verified science** from **practitioner canon** from **debunked folklore**. Full grounding lives in `references/evidence-base.md`. Summary:

### Verified findings we build on (high confidence — from the fact-checked research pass)

| Finding | Sources | Module |
|---|---|---|
| **Notional machine**: the durable barrier is understanding *runtime dynamics of execution*, not syntax; teach it as an explicit objective. *The single most curriculum-actionable finding.* | Sorva 2013 (ACM TOCE 13(2), doi 10.1145/2483710.2483713); du Boulay 1986 | A1 |
| **Expertise = better representation**: experts chunk code into larger semantic units & recognize patterns; novices process line-by-line on surface syntax. Signature: expert recall advantage shrinks on *scrambled* code (chess-chunking analogue). Shrinks but doesn't vanish. | Shneiderman 1976; McKeithen et al. 1981; SLR arXiv:2212.07763; Sala & Gobet 2017 (r≈.42) | A2 |
| **Beacons & programming plans** are real cues experts exploit. | Soloway & Ehrlich 1984 (IEEE TSE); Brooks 1983; Storey 2006; Crosby et al. 2002 | A2 |
| **Comprehension is active & hypothesis-driven**: top-down (Brooks) + bottom-up (Pennington), mode-switching (von Mayrhauser & Vans 1995). | arXiv:2212.07763; Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995 | A3, C1 |
| **Experts plan top-down before coding**: form an *abstract, complete representation* of the solution; novices translate step-by-step. (Teach plan-before-code/decompose — NOT the refuted "plan catalog.") | Adelson 1985; Soloway; Hoc 1977; Rist 1991; Koubek & Salvendy 1988/91 | B1 |
| **Reading → tracing → writing**: tracing and "explain in plain English" track with code-*writing* ability — a developmental hierarchy. | BRACElet — Lister et al., Lopez et al. 2008 | A3, B2 |
| **Years ≠ expertise**: expertise is poorly operationalized; tenure is a weak/unreliable proxy (r≈.27). Assess by performance. | Bidlake, Aubanel & Voyer 2020; Baltes & Diehl 2018; Peitek/Parnin/Apel 2022 | assessment |

### Learning-science delivery techniques (the instructional pillar)

The findings above are about *what* separates experts. This pillar is about *how to teach* — well-established cognitive/educational-psychology results that govern drill delivery (§7) and generation. Surfaced via Cat Hicks' *Learning Opportunities* project (§13), whose independently-assembled bibliography overlaps ours (Hermans, Storey, Ericsson, Tankelevitch) — cross-validating the foundation. These are robust in general learning science; programming-specific transfer carries the same open-question caveat as the rest.

| Technique | Finding | Applied in |
|---|---|---|
| **Generation & testing effect** | Producing/retrieving beats passively consuming, even when immediate performance is worse. | generate-before-reveal; teach-it-back (Roediger & Karpicke 2006; Murphy 2023) |
| **Pre-testing** | Attempting *before* being shown helps encoding even when the attempt fails — shown for novice programmers. | predict/sketch before reveal (Giebl 2021) |
| **Spacing** | Distributed practice beats massing; feels worse, works better. | spaced review + retrieval check-ins (Kornell 2009; Kang 2016) |
| **Worked examples + expertise reversal** | Worked examples help novices but become redundant load for experts. | fade examples by tier (Sweller & Cooper 1985; Kalyuga 2007) |
| **Desirable difficulties** | Conditions that slow short-term performance improve long-term retention/transfer. | don't simplify under struggle; scaffold the *setup* (Bjork) |
| **Learning ≠ performance** | Immediate performance is a poor index of durable learning. | weight delayed re-assessment + transfer over same-session streaks (Soderstrom & Bjork 2015) |
| **Illusions of fluency/effort** | Fluent reading and felt effort are mistaken for knowledge. | feeds F1 calibration (Bjork; Dunlosky 2013) |
| **Metacognition** | Monitoring/calibration is trainable and predicts outcomes independent of ability. | F1; reflection prompts (Tankelevitch 2024; Dunlosky 2013) |

### Folklore we explicitly reject

| Myth | Reality | Source |
|---|---|---|
| **"Camel has two humps"** aptitude test sorts born-programmers from the rest | Retracted by its own author; no aptitude test found; "100% accurate" claim was false and written during an SSRI-induced manic episode; at best a weak predictor | Bornat 2014 retraction; Retraction Watch 2014 |
| **10,000-hour / 10-year rule**; deliberate practice as the dominant cause | Strong thesis is false: DP explains only ~12–14% of variance overall (~1% professions); evidence inflated ~4× by retrospective recall; loses nearly all power at elite levels; time-to-mastery varies ~8×. *Live dispute:* Ericsson contests magnitude; numbers are from music/sports/chess, NOT software. | Macnamara et al. 2014; Hambrick et al. 2018, 2020; Gobet & Campitelli 2007 |

### Refuted under verification — do NOT author modules asserting these

Sound right, did not survive adversarial fact-checking:

- "Teach the catalog of programming plans + discourse rules ⇒ expertise" (clean teachable decomposition) — refuted; partly notation-dependent (Gilmore & Green 1988). *(Constrains B1: teach planning/decomposition, not a plan catalog.)*
- "Experts use function-based mental models, novices use data-flow" — refuted 0-3.
- "Two-model (program-model / situation-model) theory" — refuted 0-3.
- "Experts search breadth-first, novices depth-first" — refuted 0-3.
- "Systematic control/data-flow tracing *causally* yields better mental models & fewer errors than as-needed reading" — refuted 1-2. → Teach tracing as *a* strategy; don't claim causal superiority.

### Evidence honesty for verified-adjacent, craft & staff modules

Many modules rest on **practitioner canon, general learning science, or extrapolation** rather than the programming-specific fact-checked pass. Badges are honest:
- `[Verified]` — confirmed in our research pass.
- `[Verified-adjacent]` — extends a verified finding or rests on well-established *general* science (e.g., metacognition/transfer), but the programming-specific evidence is thin.
- `[Practitioner-canon]` — respected practice, not empirically established; grounded & vetted during authoring.

Candidate sources (to be vetted): Ousterhout *A Philosophy of Software Design*; Fowler *Refactoring*; Feathers *Working Effectively with Legacy Code*; Tornhill *Your Code as a Crime Scene*; Kleppmann *Designing Data-Intensive Applications*; Agans *Debugging*; Bacchelli & Bird 2013 (*Modern Code Review*, ICSE — E3 has *some* empirical support); property-based-testing/TDD literature (mixed — B3); metacognition/self-regulated-learning literature (Flavell; calibration research — F1). The skill must not present canon as "verified."

### The caveat that shapes the whole design

Nearly all the *verified* evidence is drawn from **novices** in intro courses, mostly **1976–1995**, in BASIC/Pascal/Fortran. Whether teaching these skills *causally improves experienced developers* is an **open question**, and staff-level depth is largely extrapolation. Consequences: **measurement is built in from day one**; every module ends with a **transfer task on the learner's real code**; depth beyond the evidence is honestly labeled.

### Reading spine (book canon)

*The Programmer's Brain* (Hermans) — comprehension core; *Why Programs Fail* (Zeller) — C1/C3; *The Psychology of Computer Programming* (Weinberg) — context; *Peak* (Ericsson & Pool) — F2, read critically; *A Philosophy of Software Design* (Ousterhout) & *Refactoring* (Fowler) — craft D1–D3; *Working Effectively with Legacy Code* (Feathers) & *Designing Data-Intensive Applications* (Kleppmann) — staff E1–E2.

## 3. Scope (v1)

**In:** 20 modules across 6 tracks (all tier-labeled by evidence); per-skill tiered routing **plus an unbounded Frontier band**; entry assessment that *recommends* (never gates); free sampling; **dynamic drill generation** anchored by golden exemplars; **executable ground truth** for verifiable drills via a Python runtime; coaching loop with the **learning-science delivery disciplines** (pause/no-spoiler, pre-test, fading scaffolding, direct feedback); progress/mastery tracker; an **optional affective self-report layer** (validated open-access measures, §13); a module-authoring template for extensibility.

**Out (future):** non-Python execution runtimes; spaced-repetition scheduling engine; team/cohort dashboards; IDE integration; an empirical transfer-validation study; backlog modules (technical communication & design docs; mentoring/teaching; type-driven reasoning; distributed-execution as its own module). Also future: an **in-flow delivery mode** — run exercises on the learner's *own* just-written/committed code (with an optional post-commit trigger hook), as an alternative to the synthetic-drill "gym" (the *Learning Opportunities* model, §13).

## 4. Architecture (coach skill + module buffet + generation engine)

Progressive disclosure, dynamic drills anchored by curated exemplars, executable grading where possible. **Track-prefixed IDs are stable** — adding a module appends within its track and never renumbers the others.

```
programming-mastery/                  # built here; installed to ~/.claude/skills/
  SKILL.md                            # the coach: routing + coaching loop + session protocol + module index
  references/
    evidence-base.md                  # §2 expanded: findings, folklore, refuted-list, citations, tiers
    assessment.md                     # entry/routing assessment + per-skill mastery rubrics
    coaching-loop.md                  # locate → teach → generate → attempt → diagnose → feedback → adapt
    drill-generation.md               # generation spec format; executable-ground-truth; self-check; Frontier escalation
    authoring-new-modules.md          # template + process for adding modules (extensibility)
  modules/
    # ── Track A · Comprehension (intake) [Verified] ──
    A1-notional-machine.md
    A2-code-reading-and-chunking.md
    A3-execution-tracing.md
    A4-concurrency-mental-models.md
    # ── Track B · Construction (generate) [Verified-adjacent / Canon] ──
    B1-decomposition-and-planning.md
    B2-code-writing-and-composition.md
    B3-testing-and-correctness.md
    # ── Track C · Debugging [Verified model + Canon method] ──
    C1-systematic-debugging.md
    C2-reading-stack-traces-and-errors.md
    C3-production-and-concurrency-debugging.md
    # ── Track D · Quality & craft [Practitioner-canon] ──
    D1-managing-complexity.md
    D2-naming.md
    D3-refactoring-judgment.md
    D4-performance-and-mechanical-sympathy.md
    # ── Track E · Scale & collaboration / staff [Mixed / Canon] ──
    E1-large-codebase-comprehension.md
    E2-architectural-judgment.md
    E3-code-review.md
    # ── Track F · Meta & learning [Verified-adjacent / Verified meta] ──
    F1-metacognition-and-calibration.md
    F2-designing-your-practice.md       # meta-capstone; revisited throughout
    F3-learning-new-languages-and-frameworks.md
  exemplars/
    <module-id>/<tier>/               # ~3 golden drills/tier: generator few-shot calibration + worked examples + offline fallback
  runtime/
    python/                           # sandboxed runner so the coach can EXECUTE code drills for ground truth (v1: Python)
  progress-template.md                # per-learner mastery tracker (the measurement instrument)
```

- **Buffet, not a track sequence:** tracks group related skills and imply a *recommended* order; the entry assessment routes and recommends, but a learner can sample any module anytime. Modules declare **soft** prerequisites only.
- **Progressive disclosure:** `SKILL.md` stays lean; the coach loads only the module + tier in play.
- **Dual-use:** a human reads `modules/*.md` directly (the curriculum); invoking the skill activates the coach (the wrapper).
- **Drills are generated, not banked:** each module ships a *generation spec* + a *small golden exemplar set*; the coach generates fresh drills per session. Teaching-to-the-test becomes structurally impossible; no authoring bottleneck.
- **Build vs install:** developed here; installed by copy/symlink to `~/.claude/skills/programming-mastery/`.

## 5. The module model (anatomy of every `modules/<ID>-*.md`)

Fixed structure so one coaching protocol drives all modules:

1. **Evidence basis** — finding + citation + tier badge `[Verified]` / `[Verified-adjacent]` / `[Practitioner-canon]`. A module may carry a *mixed* badge when concept and method differ in status (e.g., C1, C3: verified comprehension model, canon-supported method).
2. **Soft prerequisites** — recommended prior modules, explicitly *not required* (buffet model). Each module is usable standalone.
3. **The mental model** — the core concept in plain language.
4. **Worked example** — an expert demonstration to imitate. *Fade by tier* (worked-example effect + expertise reversal, Kalyuga 2007): full at Foundations, progressively removed at Advanced/Frontier where shown steps become redundant cognitive load.
5. **Drill-generation spec** — tier definitions (the difficulty model), parameter space to vary, the **common-error catalog** to target, and the **grading mode**: *executable ground truth* (coach runs the code) vs *rubric + exemplars* (judgment skills). Points into `exemplars/`.
6. **Frontier band** — how difficulty escalates *beyond* Advanced (which knobs increase; what staff-level looks like).
7. **Mastery rubric** — the *observable performance* bar to pass at each named tier.
8. **Anti-patterns & evidence caveat** — what the skill is *not*; for canon modules, the explicit "rests on canon, not verified research" note.
9. **Transfer task** — apply the skill to the learner's *own real code*.

## 6. The twenty modules

A sampleable buffet. Tracks map onto the build lifecycle so the generative front half (Track B) is no longer thin:

| ID | Module | Track | Tier badge | Core idea |
|---|---|---|---|---|
| A1 | Notional machine / execution model | A | `[Verified]` | A program is a machine with state; execution = deterministic state transitions; simulate, don't read intent. |
| A2 | Code reading & chunking | A | `[Verified]` | Read for structure not syntax; recognize beacons/patterns; chunk into semantic units; summarize unfamiliar code fast. |
| A3 | Execution tracing & explain-in-plain-English | A | `[Verified]` | Hand-simulate execution; produce call trees; explain purpose in 1–3 sentences. |
| A4 | Concurrency mental models | A | `[Verified-adjacent]` + `[Canon]` | The notional machine for concurrency: interleavings, happens-before, memory models, reasoning about nondeterminism. |
| B1 | Problem decomposition & planning | B | `[Verified-adjacent]` | Understand → represent → plan top-down before coding. Decompose; don't translate line-by-line. (Not the refuted plan catalog.) |
| B2 | Code writing & composition | B | `[Verified-adjacent]` | The writing end of reading→tracing→writing: compose correct code from intent, built up in verified steps. |
| B3 | Testing & specifying correctness | B | `[Canon + some empirical]` | Adversarial thinking about your own code: edge cases, properties, what "correct" means. |
| C1 | Systematic / hypothesis-driven debugging | C | `[Verified]` model + `[Canon]` method | Debugging as science: observe → hypothesize → predict → test → narrow (bisection). Not print-spraying. (Causal superiority of tracing was refuted.) |
| C2 | Reading stack traces & error messages | C | `[Practitioner-canon]` | Decode a trace as a window into the execution model; locate fault from the evidence the runtime already gives you. |
| C3 | Production & concurrency debugging | C | `[Verified]` model + `[Canon]` method | Heisenbugs, races, observability-driven debugging, live-system incident reasoning. Extends A1/C1 to systems scale. |
| D1 | Managing complexity / abstraction | D | `[Practitioner-canon]` | Decomposition, abstraction boundaries, deep vs shallow modules. |
| D2 | Naming | D | `[Practitioner-canon]` | Names as cheapest documentation; precision, consistency, intent. |
| D3 | Refactoring judgment | D | `[Practitioner-canon]` | When (and when not) to refactor; behavior-preserving change under test. |
| D4 | Performance & mechanical sympathy | D | `[Canon / extrapolation]` | Cost models; what operations actually cost; measure-before-optimize. Extends the notional machine down to hardware. |
| E1 | Large-codebase comprehension | E | `[Verified]` core + `[Canon]` scale | Orient in a big unfamiliar repo fast: entry points, architecture reconstruction, mental map under time pressure. Extends A2/A3 to repo scale. |
| E2 | Architectural & technical judgment | E | `[Practitioner-canon]` | Designing for change & failure; tradeoff analysis under uncertainty; when NOT to build. |
| E3 | Code review as a skill | E | `[Some empirical]` + `[Canon]` | Reading + judgment + communication; reviewing others' code well; precise feedback; catching what matters. |
| F1 | Metacognition & calibration | F | `[Verified-adjacent]` | Knowing what you don't know: calibrate confidence, notice confusion early, monitor your own understanding. (General learning science; programming-specific evidence thin.) |
| F2 | Designing your own practice *(meta-capstone)* | F | `[Verified]` meta | What well-designed practice actually is: quality + immediate feedback + individualized targeting, NOT hour-dosing. Revisited throughout. |
| F3 | Learning new languages & frameworks fast | F | `[Verified-adjacent]` | Transfer: acquire a new notional machine + idioms quickly; map the unfamiliar onto what you know. |

**E1 reuses the `orient` methodology** (Mullarkey/Hicks, §13): expert codebase orientation is *strategic, not exhaustive* — README → directory-tree-as-table-of-contents → entry points → **tests-as-executable-spec** → core modules → **git-churn-as-core-finder** — plus the *gateway artifact* concept (Dagenais 2010). That procedure + its bibliography (Spinellis *Code Reading*, Hermans, Storey, Spolsky) drops nearly whole into E1.

## 7. The coaching loop (`references/coaching-loop.md`, run by `SKILL.md`)

1. **Locate** — read progress file; pick the learner's chosen module + tier (or run entry assessment / recommend if new). For returning learners, open with a **retrieval check-in** ("what do you remember about …?") before new work.
2. **Teach** — present concept + **tier-faded** worked example (skip if already mastered).
3. **Generate** — produce a *fresh* drill at the learner's tier from the module's generation spec + golden exemplars; in the **Frontier band**, escalate difficulty against the demonstrated ceiling.
4. **Attempt (pre-test, then hard stop)** — pose the drill, then **end the message and wait**. Generate no answer, hints, "think about…", suggested responses, or teaching content until the learner replies. Prefer *generate-before-reveal* (predict/sketch first). The learner produces the trace / explanation / plan / code / bug hypothesis / review.
5. **Diagnose** — obtain ground truth: **run the code** for executable drills; apply **rubric + exemplars** for judgment drills. Name the *specific* gap, not just pass/fail.
6. **Feedback (direct, no false credit)** — targeted, specific, immediate; expert solution side-by-side. Be blunt about what's wrong — don't soften errors into ambiguity, and don't credit the learner with insight they didn't actually express. Wrong predictions are high-value data.
7. **Adapt (fade the scaffold, not the challenge)** — pass → harder drill / next skill / push into Frontier; struggling → move *up* the scaffolding ladder (a more specific *question setup*), never hint at the answer or simplify the challenge itself. Update progress file.
8. **Spaced review** — periodically re-surface a mastered skill to check retention.

### Delivery disciplines (borrowed learning science — see §13)

These govern *how* the coach runs every step; they counteract the LLM's default to spoil its own questions and the learner's pull toward fluent passivity:
- **Pause for input / no-spoiler:** after posing a question, the message ends. No answer, hints, leading "consider…", suggested responses, or italic clues — only a content-free nudge ("best guess — wrong is useful data") or an escape hatch.
- **Pre-test before reveal:** have the learner attempt before being shown, even if it fails (Giebl 2021).
- **Fading scaffolding:** adjust the difficulty of the *question setup*, never the answer ("open file X line N" → "find where we handle X" → "where would you look?"). Stuck → move *up* (more specific setup), don't hint.
- **Direct error feedback:** blunt about wrong, then explore the gap; clear feedback is what makes errors productive.
- **Desirable difficulty:** don't simplify because the learner struggles — productive struggle is the mechanism.
- **Prefer directing to files over showing code:** have the learner *locate* code themselves (stronger memory traces); show snippets only when short or when they're blocked.
- **Session restraint:** don't nag — cap unsolicited drill offers and stop when the learner declines.

## 8. Tiering, assessment & measurement

No validated absolute measure of expertise exists, so we measure **within-learner deltas on concrete performance tasks** against the learner's own baseline.

- **Tiers:** Foundations / Working / Advanced as **named checkpoints**, assigned **per skill**, plus an open-ended **Frontier band** above Advanced where the generator presses until failure. The Frontier gives a moving "current ceiling" metric (e.g., "Frontier level 7 on tracing").
- **Entry assessment** (`references/assessment.md`): one short *performance* task per core skill, scoring **process and product**, *recommending* a tier and starting modules per skill — never blocking sampling.
- **Mastery rubrics:** observable per-tier gates, recorded with evidence.
- **Progress tracker** (`progress-template.md`): per-skill table — track, tier, baseline, drills passed, current Frontier level, and a running list of **recurring error patterns** (the diagnostic gold).
- **Headline delta:** because drills are generated fresh, held-out re-assessment is free — re-run the entry battery later with new items at fixed checkpoints; baseline-vs-now = measurable improvement. Per-module transfer tasks track real-code transfer.
- **Honesty:** the skill states out loud that this is within-person progress on defined skills, not a certified expertise grade.
- **Learning ≠ performance** (Soderstrom & Bjork 2015): same-session drill pass-rate is a weak index of *durable* learning — so weight **delayed** re-assessment and real-code transfer over hot streaks; treat a same-session run as provisional.
- **Optional affective layer** (self-report; validated, open-access; Hicks et al., CC-BY-SA — §13): track **Learning Culture**, **AI Skill Threat**, and **Coding Self-Efficacy** pre/post as a *complement* to performance measures — never as routing or gating.
- **Reporting guardrails** (when the skill summarizes progress): descriptive over inferential; report variance/spread alongside any average; no causal overclaiming from pre/post (no control group); never confabulate norms ("a 3.2 means moderate…"). Small-n deltas start conversations, they don't render verdicts.

### Progress tracker format (markdown, agent-parseable)

| Module | Tier | Frontier | Baseline (date/score) | Drills passed | Recurring errors | Last reviewed |
|---|---|---|---|---|---|---|
| A1 Notional machine | Working | — | 2026-06-22: 2/5 | 7/9 | closure capture; aliasing | 2026-06-29 |
| A3 Execution tracing | Advanced | L4 | 2026-06-22: 4/5 | 15/16 | deep-recursion stack | 2026-06-30 |

## 9. Design principles & guardrails

- **Honesty about evidence** — verified vs verified-adjacent vs canon vs refuted is visible everywhere; never oversell.
- **Buffet, not a forced track** — modules are self-contained samplers with *soft* prerequisites; the assessment recommends but never gates.
- **Performance, not tenure** — all routing/recommendation is on observed performance.
- **Executable ground truth** — for verifiable drills the coach *runs the code*; it never grades against a guessed answer key.
- **Generation anchored by golden exemplars** — drills are generated for volume/freshness but calibrated by curated gold standards; not free-form.
- **Feedback-rich, individualized practice** — quality and specificity over volume; no hour-quotas.
- **Pause for input (no-spoiler)** — after posing a drill the coach stops; it never answers its own questions or leaks hints. The single most important delivery discipline.
- **Desirable difficulty over fluency** — keep productive struggle; fade the scaffold's *setup*, not the challenge; optimize durable learning over the feeling of fluency.
- **Unbounded depth** — the Frontier band means the ceiling fits staff engineers.
- **Transfer to real code** — every module ends on the learner's actual codebase.
- **No aptitude gatekeeping** — skill is trainable; reject the "two humps" framing explicitly.
- **Extensible by design** — adding a module is a documented, repeatable operation (`authoring-new-modules.md`), slotting into a track under a stable ID.
- **Small, well-bounded units** — one module = one skill = one file the coach can hold in context (teaching files ≤ ~200 lines).

## 10. Risks & open questions

1. **Generated drills can be mis-leveled or have wrong answer keys.** Mitigations: executable ground truth where possible; golden-exemplar calibration; a generation **self-check** pass; a learner "this looks wrong" escape hatch; rubric+exemplar grading for judgment drills (acknowledged softer).
2. **Executing generated/learner code is a safety risk.** Mitigation: a sandboxed runtime (resource-limited subprocess/container); never execute untrusted code outside the sandbox. v1 supports Python only.
3. **Judgment modules (B3, D1–D3, E2, F1, parts of E3) lack executable ground truth** — grading is inherently softer. Mitigation: stronger rubrics + more exemplars; surface uncertainty to the learner.
4. **Novice-evidence → working/staff-dev transfer is unproven; staff & verified-adjacent depth is extrapolation.** Mitigation: transfer tasks + measurement; explicit tier badges; honest framing.
5. **Teaching-to-the-test** — largely solved by fresh generation, but watch generator mode-collapse (repetitive drills). Mitigation: parameter-space coverage tracking.
6. **Buffet sprawl** — 20 modules of uneven evidentiary quality risk diluting the verified core. Mitigation: badges everywhere; the assessment steers newcomers to the high-evidence Track A/B spine first.
7. **Modern/AI-assisted revalidation.** Classic findings predate IDEs, large codebases, and LLM-assisted workflows; magnitudes for today's devs are uncertain. Track as an open question.
8. **Coaching quality depends on the generation spec encoding common errors + what they diagnose**, not just correct answers — so the coach can name the specific gap.

## 11. v1 build order

1. `references/evidence-base.md` (grounding — everything cites it; incl. the §2 learning-science instructional pillar).
2. `SKILL.md` + `references/coaching-loop.md` + `references/assessment.md` + `references/drill-generation.md` (the engine, incl. executable-ground-truth + self-check + Frontier escalation; **`coaching-loop.md` encodes the §7 delivery disciplines**; **`drill-generation.md` encodes the exercise-format catalog**, §13).
3. `runtime/python/` sandboxed runner + `progress-template.md` (execution + measurement instruments).
4. **Module A1 (notional machine) end-to-end** — mental model + worked example + generation spec + golden exemplars + executable grading + Frontier band. The reference implementation of the module model.
5. Build by track: rest of A (A2–A4) → B (B1–B3) → C (C1–C3) → D (D1–D4) → E (E1–E3) → F (F1–F3). (E1 adapts the `orient` procedure + bibliography, §13; F1 leans on the §2 instructional pillar.)
6. `references/authoring-new-modules.md` — extract the template from how the modules were actually built.
7. Smoke-test: a full coached session on A1, including live code execution for ground truth and a Frontier escalation.

## 12. AI-era impact priority (2026–27, research-informed)

A five-angle subagent research pass (productivity RCTs, practitioner commentary, code-quality data, agentic-role analysis, deskilling/learning studies) converged on one shift: **as agents draft most code, developer value moves from *writing* code to *verifying* code they didn't write.** All five angles independently ranked the same cluster highest.

**Highest-impact cluster — the "verification" modules:**
- **E3 Code review** — the apex skill; where the measured bottleneck moved (Faros telemetry: review time +91%, PR volume +98%; DORA 2025: "AI doesn't replace code review; it makes it more critical").
- **F1 Metacognition & calibration** — the upstream gate and the single best-evidenced finding (METR RCT: experienced devs 19% slower while feeling 20% faster; Fernandes et al. 2025: more AI-literate users were *more* overconfident).
- **A2/A3 Code reading & tracing** — the verified foundation review stands on, and what atrophies first (Anthropic RCT, N=52: −17% on later unaided comprehension/debugging).
- **B3 Testing & specifying correctness** — the automated arm of verification (Veracode 2025: 45% of AI-generated code carried vulnerabilities; NUS/Google CS-ed consensus: precise specification + verification is "arguably the most durable technical skill a graduate can possess").
- Supporting: **C1/C2 systematic debugging & stack traces**, **E1/E2 large-codebase comprehension & architectural judgment**.

**Decision:** v1 build order stays **track-based** (§11) for dependency/pedagogy reasons (A1 remains the reference implementation; reading precedes review). This cluster is flagged as the **priority for real-world impact** — it should steer sequencing latitude within the plan, and the entry assessment should surface these modules prominently to newcomers.

**Evidence caveats:** the productivity *direction* is contested (METR is revising its slowdown finding after late-2025/2026 data showed an ~18% speedup); much "AI degrades quality" data is vendor-sourced (GitClear was independently rebutted); the RCTs (METR, Anthropic, Stanford CCS'23) are the load-bearing evidence; coding-specific *causal* evidence is thin and small-N. Treat this as priority-steering, not proof — consistent with the §2 evidence-honesty stance.

## 13. Borrowed techniques & attribution

**Source:** Cat Hicks' *Learning Opportunities* skill + Michael Mullarkey's *orient* companion — `github.com/DrCatHicks/learning-opportunities`. A sibling project by a psychological scientist who studies developer learning/thriving. It is **complementary**: it specializes in *delivery discipline*, *affective measurement*, and *codebase orientation*, where our project specializes in the skill taxonomy + the generation/executable-grading engine.

**License & attribution.** Their principles/skill are **CC-BY-4.0**; their survey measures are **CC-BY-SA-4.0** (share-alike). Findings, citations, and techniques aren't copyrightable and we use them with credit. If we ship their *survey items* or *principle prose* verbatim, we attribute (Hicks, Lee, Foster-Marks / Ramsey) and CC-BY-SA binds that derivative. Credit **Cat Hicks** for the delivery techniques and measures; **Michael Mullarkey** for `orient`.

**What we borrowed and where it lives:**

| # | Borrowed | Folded into |
|---|---|---|
| 1 | **Delivery disciplines** — pause/no-spoiler, pre-test, fading scaffolding, direct feedback, desirable difficulty, direct-to-files, session restraint | §7 + `coaching-loop.md`; principle in §9 |
| 2 | **Exercise-format catalog** — Prediction→Observation→Reflection · Generation→Comparison · Trace-the-path · Debug-this · Teach-it-back · Retrieval check-in · + elaborative interrogation, interleaving, varied-context, concrete→abstract transfer, error analysis, example-problem pairs, completion prompts | `drill-generation.md` (formats are orthogonal to modules — any generator may draw from them) |
| 3 | **Learning-science instructional pillar** (citations: Roediger & Karpicke, Giebl, Kornell/Kang, Sweller, Kalyuga, Bjork, Soderstrom & Bjork, Dunlosky, Murphy, Tankelevitch) | §2 instructional-pillar table + `evidence-base.md` |
| 4 | **Worked-example fading / expertise reversal** | §5 module anatomy (point 4) + tier model |
| 5 | **`orient` codebase-orientation procedure + bibliography** (Spinellis, Hermans, Storey, Spolsky, Dagenais "gateway artifact") | E1 module (near-complete) |
| 6 | **Measurement**: learning≠performance caveat; optional affective measures (DTS Learning Culture, AI Skill Threat, Coding Self-Efficacy); AI-analysis statistical guardrails | §8 + `assessment.md` |
| 7 | *(future)* **In-flow delivery mode** + post-commit trigger hook (their PostToolUse model) | §3 Out (future) |

**Cross-validation:** their independently-assembled bibliography overlaps ours (Hermans, Storey, Ericsson, Tankelevitch), strengthening confidence in the shared foundation. Their delivery emphasis also *reinforces* our highest-evidence AI-era priority (§12): F1 calibration and the verification cluster are exactly what their fluency/effort-illusion and metacognition work targets.
