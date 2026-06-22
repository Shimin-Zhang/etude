# Programming Mastery — Design Spec (v1)

- **Date:** 2026-06-22
- **Status:** Approved for v1 (pending final spec review)
- **Working dir:** `/home/shimin/agents/programming-agent`
- **Skill name (provisional):** `programming-mastery`

## 1. Goal

Build a training scaffolding — **curriculum content wrapped in a Claude Code coaching skill** — that helps working developers of any level get *measurably* better, grounded in what the empirical literature actually supports (not folklore).

The scaffolding teaches **representation and comprehension skills** (the things that actually separate experts from novices in the research), delivers them through an **agent-coached, feedback-rich practice loop**, and **measures within-learner improvement** on concrete performance tasks.

### Success criteria

1. A developer can invoke the skill, be assessed, and be routed to the right tier per skill.
2. Each practice session ends with a *specific, diagnosed* gap and targeted feedback — not a pass/fail score.
3. Improvement is demonstrable as a **baseline → re-assessment delta** on held-out performance tasks, plus transfer evidence on the learner's own code.
4. Every claim the skill makes is traceable to its evidence basis and honestly tier-labeled.

## 2. Evidence base (the grounding)

This is the differentiator: the curriculum is built on fact-checked findings, and it openly distinguishes verified science from practitioner canon from debunked folklore. Full grounding lives in `references/evidence-base.md`. Summary:

### Verified findings we build on (high confidence)

| Finding | Sources | Used by module |
|---|---|---|
| **Notional machine**: the durable barrier is understanding *runtime dynamics of execution*, not syntax; teach it as an explicit objective. *The single most curriculum-actionable finding.* | Sorva 2013 (ACM TOCE 13(2), doi 10.1145/2483710.2483713); du Boulay 1986 | 01 |
| **Expertise = better representation**: experts chunk code into larger semantic units & recognize patterns; novices process line-by-line on surface syntax. Signature evidence: expert recall advantage shrinks on *scrambled* code (the chess-chunking analogue). Advantage shrinks but doesn't vanish. | Shneiderman 1976; McKeithen et al. 1981; SLR arXiv:2212.07763; Sala & Gobet 2017 (r≈.42) | 02 |
| **Beacons & programming plans** are real cues experts exploit. | Soloway & Ehrlich 1984 (IEEE TSE); Brooks 1983; Storey 2006; Crosby et al. 2002 (eye-tracking) | 02 |
| **Comprehension is active & hypothesis-driven**: top-down (Brooks) + bottom-up (Pennington), mode-switching (von Mayrhauser & Vans 1995). | arXiv:2212.07763; Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995 | 03, 04 |
| **Reading → tracing → writing**: code-tracing skill and "explain in plain English" track with code-*writing* ability. | BRACElet project — Lister et al., Lopez et al. 2008; code-tracing→writing study | 03 |
| **Years ≠ expertise**: expertise is poorly operationalized; tenure is a weak/unreliable proxy (r≈.27). Assess by performance. | Bidlake, Aubanel & Voyer 2020 (J. Syst. & Software); Baltes & Diehl 2018; Peitek/Parnin/Apel 2022 | assessment |

### Folklore we explicitly reject

| Myth | Reality | Source |
|---|---|---|
| **"Camel has two humps"** aptitude test sorts born-programmers from the rest | Retracted by its own author; no aptitude test was found; "100% accurate" claim was false and written during an SSRI-induced manic episode; at best a weak predictor | Bornat 2014 retraction; Retraction Watch 2014 |
| **10,000-hour / 10-year rule**; deliberate practice as the dominant cause | Strong thesis is false: DP explains only ~12–14% of variance overall (~1% professions); evidence inflated ~4× by retrospective recall; loses nearly all power at elite levels; time-to-mastery varies ~8×. *Live dispute:* Ericsson contests magnitude; numbers are from music/sports/chess, NOT software. | Macnamara et al. 2014 (Psych Science); Hambrick et al. 2018 (Annals NYAS); Hambrick et al. 2020 (Frontiers Psych); Gobet & Campitelli 2007 |

### Refuted under verification — do NOT author modules asserting these

These *sound* right but did not survive adversarial fact-checking. Module authors must avoid building on them:

- "Teach the catalog of programming plans + discourse rules ⇒ expertise" (clean teachable decomposition) — refuted; partly notation-dependent (Gilmore & Green 1988).
- "Experts use function-based mental models, novices use data-flow" — refuted 0-3.
- "Two-model (program-model / situation-model) theory" — refuted 0-3.
- "Experts search breadth-first, novices depth-first" — refuted 0-3.
- "Systematic control/data-flow tracing *causally* yields better mental models & fewer errors than as-needed reading" — refuted 1-2. → Teach tracing as *a* strategy; do not claim causal superiority.

### The caveat that shapes the whole design

Nearly all this evidence is drawn from **novices** in intro courses, mostly **1976–1995**, in BASIC/Pascal/Fortran. Whether explicitly teaching these skills *causally improves experienced developers* is an **open question**. Our target spans all levels, so the scaffolding is an evidence-*informed hypothesis*. Consequence: **measurement is built in from day one**, and every module ends with a transfer task on the learner's real code.

### Reading spine (book canon)

- *The Programmer's Brain* — Felienne Hermans (operationalizes the chunking/comprehension research) — core.
- *Why Programs Fail* — Andreas Zeller (systematic, hypothesis-driven debugging) — module 04.
- *The Psychology of Computer Programming* — Gerald Weinberg — context.
- *Peak* — Ericsson & Pool (deliberate-practice canon; read critically against the meta-analyses) — module 05.
- *A Philosophy of Software Design* — Ousterhout; *Refactoring* — Fowler — craft modules 06–08 (canon, labeled).

## 3. Scope (v1)

**In:** 8 modules (5 evidence-backed core + 3 craft extensions, evidence-tier-labeled); per-skill tiered routing; entry assessment; coaching loop; progress/mastery tracker; language-agnostic drills with at least one language pack (Python) for v1.

**Out (future):** spaced-repetition scheduling engine; multi-language packs beyond Python; team/cohort dashboards; IDE integration; empirical validation study of transfer.

## 4. Architecture (Approach A + C)

Coach skill + module library (progressive disclosure), borrowing a lightweight structured measurement spine.

```
programming-mastery/                  # built here; installed to ~/.claude/skills/
  SKILL.md                            # the coach: routing + coaching loop + session protocol
  references/
    evidence-base.md                  # §2 expanded: findings, folklore, refuted-list, citations
    assessment.md                     # entry/routing assessment + per-skill mastery rubrics
    coaching-loop.md                  # deliver → attempt → diagnose → feedback → adapt protocol
  modules/
    01-notional-machine.md            # ── core (Verified) ──
    02-code-reading-and-chunking.md
    03-execution-tracing.md
    04-systematic-debugging.md
    05-designing-your-practice.md
    06-managing-complexity.md         # ── craft extensions (Practitioner-canon, labeled) ──
    07-naming.md
    08-refactoring-judgment.md
  drills/
    <module>/<tier>/                  # drill prompts + answer keys / rubrics (language-agnostic core)
    language-packs/python/            # same drills realized in Python (v1 pack)
  progress-template.md                # per-learner mastery tracker (the measurement instrument)
```

- **Progressive disclosure:** `SKILL.md` stays small; the coach loads only the module in play.
- **Dual-use:** a human can read `modules/*.md` directly (the "curriculum"); invoking the skill activates the coach (the "wrapper"). Satisfies "curriculum + skill wrapper."
- **Build vs install:** developed in the working dir; installed by copy/symlink to `~/.claude/skills/programming-mastery/`.

## 5. The module model (anatomy of every `modules/NN-*.md`)

Fixed structure so one coaching protocol drives all modules:

1. **Evidence basis** — finding + citation + tier badge `[Verified]` / `[Practitioner-canon]`. A module may carry a *mixed* badge when its concept and its method differ in evidentiary status (e.g., module 04: verified comprehension model, canon-supported method).
2. **The mental model** — the core concept in plain language.
3. **Worked example** — an expert demonstration to imitate.
4. **Tiered drills** — Foundations / Working / Advanced; each = prompt + answer key or rubric; pointer into `drills/`.
5. **Mastery rubric** — the *observable performance* bar to pass at a tier.
6. **Anti-patterns & evidence caveat** — what the skill is *not*; for craft modules, an explicit "rests on canon, not verified research" note.
7. **Transfer task** — apply the skill to the learner's *own real code*.

## 6. The eight modules

| # | Module | Tier badge | Core idea | Maps to |
|---|---|---|---|---|
| 01 | Notional machine / execution model | `[Verified]` | A program is a machine with state; execution = deterministic state transitions; simulate, don't read intent. | Sorva 2013; du Boulay 1986 |
| 02 | Code reading & chunking | `[Verified]` | Read for structure, not syntax; recognize beacons/patterns; chunk into semantic units; summarize unfamiliar code fast. | Shneiderman 1976; Soloway-Ehrlich 1984; Storey 2006; Hermans |
| 03 | Execution tracing & explain-in-plain-English | `[Verified]` | Hand-simulate execution; produce call trees; explain code's purpose in 1–3 sentences. Reading→tracing→writing. | BRACElet (Lister/Lopez); von Mayrhauser & Vans 1995 |
| 04 | Systematic / hypothesis-driven debugging | `[Verified]` comprehension model + `[Practitioner-canon]` method | Debugging as science: observe → hypothesize → predict → test → narrow (bisection). Not print-spraying. | Brooks 1983; Zeller *Why Programs Fail*. (NB: causal superiority of tracing was refuted — frame as disciplined process, not proven-best.) |
| 05 | Designing your own practice (capstone) | `[Verified]` meta | What well-designed practice actually is: quality + immediate feedback + individualized targeting, NOT hour-dosing. Self-measurement; keep improving after the curriculum. | Macnamara 2014; Hambrick 2018/2020; *Peak* (critically) |
| 06 | Managing complexity / abstraction | `[Practitioner-canon]` | Decomposition, abstraction boundaries, deep vs shallow modules. | Ousterhout |
| 07 | Naming | `[Practitioner-canon]` | Names as the cheapest documentation; precision, consistency, intent. | Martin; Ousterhout |
| 08 | Refactoring judgment | `[Practitioner-canon]` | When (and when not) to refactor; behavior-preserving change under test. | Fowler |

## 7. The coaching loop (`references/coaching-loop.md`, run by `SKILL.md`)

1. **Locate** — read progress file; pick target skill + tier (or run entry assessment if new).
2. **Teach** — present concept + worked example (skip if already mastered).
3. **Drill** — issue one drill at the learner's tier; learner attempts it.
4. **Diagnose** — check against answer key; name the *specific* gap, not just pass/fail.
5. **Feedback** — targeted, specific, immediate; expert solution shown side-by-side. (The active ingredient the DP research supports.)
6. **Adapt** — pass → harder drill / next skill; fail → easier drill / re-teach sub-skill. Update progress file.
7. **Spaced review** — periodically re-surface a mastered skill to check retention.

Each step maps to a verified finding: feedback-rich *individualized* practice, *performance-based* assessment, targeting the *specific* mental-model deficit.

## 8. Tiering, assessment & measurement

No validated absolute measure of expertise exists, so we measure **within-learner deltas on concrete performance tasks** against the learner's own baseline.

- **Tiers:** Foundations / Working / Advanced, assigned **per skill** (a learner may be Advanced at reading, Foundations at debugging).
- **Entry assessment** (`references/assessment.md`): one short *performance* task per core skill, scoring **process and product**, routing each skill to a tier. (e.g., the debugging task scores your first three hypotheses + how you'd test them, not whether you found the bug.)
- **Mastery rubrics:** observable per-tier gates, recorded with evidence.
- **Progress tracker** (`progress-template.md`): per-skill table — current tier, baseline, drills attempted/passed, and a running list of **recurring error patterns** (the diagnostic gold).
- **Headline delta:** re-run the entry battery later with **held-out fresh items**; baseline-vs-now = measurable improvement. Held-out items guard against teaching-to-the-test; per-module transfer tasks track real-code transfer.
- **Honesty:** the skill states out loud that this is within-person progress on defined skills, not a certified expertise grade.

### Progress tracker format (markdown, agent-parseable)

Per learner, a table:

| Skill | Tier | Baseline (date/score) | Drills passed | Recurring errors | Last reviewed |
|---|---|---|---|---|---|
| Notional machine | Working | 2026-06-22: 2/5 | 7/9 | closure capture; aliasing | 2026-06-29 |

## 9. Design principles & guardrails

- **Honesty about evidence** — verified vs canon vs refuted is visible everywhere; never oversell.
- **Performance, not tenure** — all routing/gating is on observed performance.
- **Feedback-rich, individualized practice** — not hour-quotas; quality and specificity over volume.
- **Transfer to real code** — every module ends on the learner's actual codebase.
- **No aptitude gatekeeping** — skill is trainable; reject the "two humps" framing explicitly.
- **Small, well-bounded units** — one module = one skill = one file the coach can hold in context.

## 10. Risks & open questions

1. **Novice-evidence → working-dev transfer is unproven.** Mitigation: transfer tasks + measurement; honest framing.
2. **Teaching-to-the-test.** Mitigation: held-out re-assessment items; transfer on real code.
3. **Modern/AI-assisted revalidation.** Classic findings predate IDEs, large codebases, and LLM-assisted workflows; magnitudes for today's devs are uncertain. Track as an open question; revisit module content as evidence emerges.
4. **Craft modules rest on canon, not verified research.** Mitigation: explicit tier badges and caveats.
5. **Coaching-loop quality depends on the agent's diagnosis.** The drill answer keys must encode *common errors and what they diagnose*, not just correct answers, so the coach can name the specific gap.

## 11. v1 build order

1. `references/evidence-base.md` (grounding — everything else cites it).
2. `SKILL.md` + `references/coaching-loop.md` + `references/assessment.md` (the engine).
3. `progress-template.md` (the measurement instrument).
4. Module 01 (notional machine) end-to-end incl. Python drills + answer keys — the reference implementation of the module model.
5. Modules 02–05 (core), then 06–08 (craft).
6. Smoke-test: run a full coached session against a sample learner on module 01.
