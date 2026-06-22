# F1 — Metacognition & Calibration `[Verified-adjacent]`

> **Module type.** The **AI-era keystone** (spec §12). It teaches the skill that decides
> whether a developer can be trusted to *verify code they did not write*: accurately
> judging **what you know vs. don't**, **noticing confusion early**, and **calibrating
> trust** in your own output and the AI's. As coding agents draft most first-draft code,
> the bottleneck moves from *writing* to *verifying* — and verification is bottlenecked by
> calibration (`evidence-base.md` → AI-era impact → calibration gap).
>
> **Core idea.** Your **confidence is itself a measurable quantity**, and it can be **right
> or wrong independent of whether your answer is**. A *well-calibrated* engineer's 90% is
> correct about 90% of the time; an *overconfident* one's 90% is correct 60% of the time
> and they don't feel the difference. The skill is to make confidence **track reality** —
> by predicting, then checking against ground truth, then adjusting — so that "I'm sure"
> and "I'd better verify that" fire at the right moments.

---

## 1. Evidence basis `[Verified-adjacent]`

This module rests on **well-established general learning science** about metacognition and
calibration, plus the curriculum's **AI-era impact** synthesis. Per the badge
(`evidence-base.md` → tiers): the **general** science is solid and replicated; the
**programming-specific** transfer is **thinner and partly extrapolated** — stated honestly
in §8.

**Two layers of grounding.**

**(a) The AI-era priority — cite via `evidence-base.md` (→ AI-era impact; instructional
pillar → Metacognition / Illusions of fluency rows).** These are confirmed *there* against
primary sources; this module does not re-derive them:

- **The perception–reality gap (the single best-evidenced AI-era finding).** In a
  randomized controlled trial, experienced developers were **~19% slower** with early-2025
  AI tools while *forecasting* a 24% speedup and *believing afterward* they'd gotten a ~20%
  speedup — a ~39-point gap between **felt** and **measured** productivity (METR 2025). And
  **more AI-literate users were *more* overconfident**, not less (Fernandes et al. 2025,
  *Computers in Human Behavior*). Calibration does not come free with expertise or with AI
  fluency; it is the thing this module trains.
- **The metacognitive demands of GenAI** (Tankelevitch et al. 2024, *CHI* — already in the
  evidence-base instructional pillar). Working with generative AI *raises* the metacognitive
  load: you must hold a clear goal, decompose the task, and — critically — bring
  **well-adjusted confidence in your own ability to evaluate the output**. Poorly calibrated
  self-confidence is the failure mode the paper names.

**(b) The general calibration science — the metacognition/calibration literature this
module teaches from.** `[Verified-adjacent]`: established cognitive/educational psychology;
**now grounded in `evidence-base.md`** (→ Metacognition & calibration (module F1); see §8):

- **Flavell, J. H. (1979). Metacognition and cognitive monitoring: a new area of
  cognitive–developmental inquiry.** *American Psychologist*, 34(10), 906–911.
  doi:10.1037/0003-066X.34.10.906. The paper that established *metacognition* — "cognition
  about cognitive phenomena" — and split it into **metacognitive knowledge** (what you know
  about your own knowing) and **metacognitive experiences/monitoring** (the in-the-moment
  sense of understanding or confusion). The *monitoring* half is what this module drills.

- **Nelson, T. O., & Narens, L. (1990). Metamemory: a theoretical framework and some new
  findings.** *Psychology of Learning and Motivation*, 26, 125–173. The canonical
  **monitoring ↔ control** framework: a **meta-level** holds a model of the **object-level**
  and two information flows connect them — **monitoring** (object-level state read *upward*:
  "how well do I actually know this?") and **control** (decisions sent *downward*: "re-read
  it / run it / ship it"). This module's mechanism (§3) *is* this loop: monitoring produces
  a confidence; control decides whether to verify.

- **Lichtenstein, S., & Fischhoff, B. (1977). Do those who know more also know more about
  how much they know?** *Organizational Behavior and Human Performance*, 20(2), 159–183.
  Foundational calibration work establishing **systematic overconfidence** and the
  **hard–easy effect**: as tasks get harder, **accuracy falls faster than confidence does**,
  so overconfidence *grows* exactly where the stakes (being wrong) are highest. The
  calibration-trap drill (Working tier) is built on this.

- **Kruger, J., & Dunning, D. (1999). Unskilled and unaware of it: how difficulties in
  recognizing one's own incompetence lead to inflated self-assessments.** *Journal of
  Personality and Social Psychology*, 77(6), 1121–1134.
  doi:10.1037/0022-3514.77.6.1121. The **dual burden**: the skills needed to *do* a task
  well overlap the skills needed to *judge* whether you did it well — so the least skilled
  are also the least able to detect that they're wrong. The direct rationale for measuring
  calibration **separately** from correctness. (The strongest *misreadings* of this paper
  are contested; what we use — that monitoring accuracy is itself a skill that can lag raw
  ability — is the robust core.)

- **Koriat, A., & Bjork, R. A. (2005). Illusions of competence in monitoring one's
  knowledge during study.** *Journal of Experimental Psychology: LMC*, 31(2), 187–194. The
  **fluency/foresight illusion**: information that is *present and easy to process* feels
  *known*, inflating confidence about later **unaided** performance. The programming
  cognate: code that **reads** smoothly feels **understood** — until you must predict its
  output or modify it. This is why the drills demand a *prediction against ground truth*,
  not a self-report of "I get it."

- **Dunlosky, J., & Rawson, K. A. (2012). Overconfidence produces underachievement:
  inaccurate self-evaluations undermine students' learning and retention.** *Learning and
  Instruction*, 22(4), 271–280. doi:10.1016/j.learninstruc.2011.08.003. Calibration is not
  a curiosity — **overconfidence causally degrades learning**: students who overestimate
  their understanding **stop studying too early** and retain less. The engineering cognate:
  overconfidence makes you **stop verifying too early** and ship the bug.

**The instructional pillar already carries this direction.** `evidence-base.md` lists
**Metacognition** ("monitoring and calibration are trainable and predict outcomes
*independent of raw ability*") and **Illusions of fluency / effort** ("fluent reading and
the *feeling* of effort are both mistaken for knowledge; learners are systematically
miscalibrated") as `[Verified-adjacent]` rows that **feed F1**, citing Dunlosky et al.
(2013) and Bjork, Dunlosky & Kornell (2013). This module instantiates those rows with the
primary calibration sources above.

**Why these license this module.** The narrow, well-supported claim they jointly support:
**metacognitive monitoring is a distinct, trainable skill; people are systematically
overconfident; and the gap between felt and actual knowing is largest exactly where it
hurts — on hard problems, on smooth-reading code, and (the AI-era twist) on code one did
not write.** The training move is **predict → check against ground truth → adjust**, which
is the Nelson–Narens loop run with an *external* truth source (the runner) instead of an
internal guess.

**Read through the transfer caveat — and an extra honesty note.** Like every module here,
the general findings come mostly from **lab and classroom calibration studies, not from
professional software engineers** (`evidence-base.md` → transfer caveat). On top of that,
the **programming-specific** calibration evidence is **thin and recent** (METR/Fernandes
are small-N and the productivity *direction* is contested; `evidence-base.md` → AI-era
honesty caveats). The *direction* — calibration is trainable and matters more in the AI era
— is well-motivated; treat this as **priority-steering, not proof**, and lean on the
transfer task (§9) as the honest individual-level evidence.

---

## 2. Soft prerequisites

**Light, and never a gate.** F1 is part of the **high-evidence spine** assessed up front
(`assessment.md` §1.2: A1, A2, A3, C1, **F1**). It is deliberately runnable from near-cold
because its drills *reuse* A1/A3-style snippets — the learner predicts output and **rates
confidence** on them.

- **Softly leans on A1 (notional machine)** — the prediction half of each drill *is* an A1
  execution-model prediction. A learner shaky on A1 will mis-predict; that is fine and
  informative. F1 then has a clean read: **was the wrong answer at least flagged as
  uncertain?** A learner who is wrong *and* knew they might be is calibrated even while
  failing A1. So weakness in A1 does not block F1 — it changes what F1 measures (calibration
  given a shaky model) and the coach notes the A1 gap for routing.
- **Pairs with A3 (tracing)** — confidence is best earned by *tracing*, not vibes; the
  scaffold for an overconfident learner is "trace it, then re-rate" (§7).

Per `assessment.md`, soft prerequisites *inform*, they never *block*: the buffet rule holds
(any learner may open any module at any tier). F1 is in fact the module the coach uses to
**read calibration across all the others** — every hybrid drill in A1/A3/C1 already carries
a confidence signal F1 knows how to score.

---

## 3. The mental model

**Your confidence is a second output you produce alongside every answer — and it has its
own correctness, separate from the answer's.** Calibration is the *match* between the two,
measured over many trials. The skill is to run a **monitor → check → adjust** loop with an
**external ground truth** so that confidence comes to track reality.

Four pieces, and the loop that connects them (the Nelson–Narens meta-level/object-level
framework, run against an external truth source):

| Component | What it is |
|---|---|
| **The answer (object-level)** | Your actual prediction/output — what the code prints, whether it raises, whether the AI's function is correct. Graded against ground truth: **correct or not.** |
| **The confidence (the monitor / meta-level)** | A *number* you attach to the answer **before** you see ground truth — "I'm 85% sure." It is a reading of your own knowing, and it can be too high (overconfident), too low (underconfident), or right. |
| **The check (against ground truth)** | The **external** truth: run the snippet through the runner; read `stdout`/`status`. Calibration is impossible without this — self-graded confidence just re-confirms the illusion (Koriat & Bjork 2005). The runner replaces "it feels right." |
| **The adjustment (control)** | The downward decision: a *miss at high confidence* should **lower** the next similar confidence and **raise** the impulse to verify; a *hit at low confidence* can raise it. Over trials, this is what moves the calibration curve. |

**The calibration rule.** Across a batch of `(confidence, correct?)` pairs, compare your
**average confidence** to your **hit rate**.

- Average confidence **>** hit rate ⇒ **overconfident** (the common, consequential failure;
  Lichtenstein & Fischhoff 1977; Kruger & Dunning 1999; and the AI-era amplification, METR
  2025 / Fernandes 2025).
- Average confidence **<** hit rate ⇒ **underconfident** (real, but usually less costly).
- They **track** (and, finer, your *high*-confidence items are right more often than your
  *low*-confidence ones) ⇒ **well-calibrated**.

Note the two graded quantities are **independent**: you can be *right but uncertain*
(under-confident — fine, slightly wasteful) or, the dangerous one, *wrong but certain*
(over-confident — you ship the bug because nothing told you to look).

**The discipline in one line: *predict the number, then let ground truth move it.*** You do
not get calibrated by *intending* to be humble; you get calibrated by repeatedly attaching
an explicit probability, checking it against a truth you can't argue with, and feeling the
sting when a 95% is wrong. Two refinements follow:

1. **Notice confusion *early* — before the reveal.** The high-value metacognitive act is
   saying "I'm not sure about *this part*" **while** you reason, not discovering it on the
   answer (Flavell 1979's monitoring). A learner who flags the exact sub-step they're unsure
   about — "I know the loop, I'm shaky on whether `+=` rebinds or mutates here" — is
   monitoring well even if the final answer is wrong. The drills reward this explicitly.
2. **Distrust fluency — yours and the AI's.** Code that *reads* smoothly feels *understood*;
   an AI function that *looks* plausible feels *correct*. Both are the fluency illusion
   (Koriat & Bjork 2005). Smoothness is a property of the *prose*, not evidence about the
   *behavior*. The only thing that earns confidence in behavior is a **check** — trace it,
   run it, test the edge case.

Three calibration failures are the usual culprits, and the whole module drills them:

1. **Flat-high confidence ("95% on everything").** Confidence that doesn't *vary* with
   difficulty — the same "I'm sure" on a one-liner and a closure-in-a-loop. The hard–easy
   effect made personal: accuracy drops on the tricky ones but the number doesn't.
2. **The fluency trap.** High confidence bought by *smooth reading* — the
   deceptively-simple-looking snippet (e.g., `0.1 + 0.2 == 0.3`) that *looks* obvious and
   isn't. Looking easy is not being easy.
3. **Trusting AI output by plausibility.** Confidence in code-you-didn't-write that comes
   from "it looks like what I'd write" rather than "I checked the edge cases." The AI-era
   keystone failure.

---

## 4. Worked example — a calibration trace

*(Foundations depth: the full predict → confidence → check → score loop, every step shown.
This fades by tier — see the note after the table.)*

The skill is to attach an explicit number, then score **two things** against ground truth:
the **answer** and the **confidence**. Consider a three-snippet mini-batch (the learner has
written a confidence next to each prediction *before* anything is run):

| # | Snippet (the prediction is the learner's) | Learner predicts | Learner's confidence |
|---|---|---|---|
| 1 | `print(3 * "ab" + "c")` | `abababc` | **95%** |
| 2 | `print(0.1 + 0.2 == 0.3)` | `True` | **90%** |
| 3 | `xs=[1,2,3]; ys=xs; ys.append(4); print(xs)` | `[1, 2, 3]` | **60%** |

**Step 1 — ground truth, by running each (executable-ground-truth discipline,
`drill-generation.md` §2 — the coach *runs* it, never guesses):**

```
#1  python runner.py s1.py  → stdout: "abababc\n"          status: ok
#2  python runner.py s2.py  → stdout: "False\n"             status: ok
#3  python runner.py s3.py  → stdout: "[1, 2, 3, 4]\n"      status: ok
```

**Step 2 — score the answer (object-level):**

| # | Predicted | Actual | Correct? | Confidence |
|---|---|---|---|---|
| 1 | `abababc` | `abababc` | ✅ | 95% |
| 2 | `True` | `False` | ❌ | 90% |
| 3 | `[1, 2, 3]` | `[1, 2, 3, 4]` | ❌ | 60% |

**Step 3 — score the calibration (the F1-specific part).** Hit rate = **1/3 ≈ 33%**.
Average confidence = (95 + 90 + 60)/3 = **~82%**. Confidence (82%) **far exceeds** hit rate
(33%) ⇒ **overconfident** on this batch. But look *within* the batch, because the ordering
carries the real signal:

- **#1 — high confidence, correct → justified.** A 95% that landed. Good. `3 * "ab"` repeats
  the string then `+ "c"` concatenates; the model and the confidence both held.
- **#2 — high confidence, WRONG → the costly miss.** This is the **fluency trap**: the
  snippet *looks* trivial, so it drew a 90% — but `0.1 + 0.2` is `0.30000000000000004` in
  binary floating point, so `== 0.3` is **`False`**. A 90% that's wrong is the
  miscalibration that matters: nothing in the learner told them to check. **This single pair
  is the lesson** — "looks easy" bought confidence that the *behavior* did not earn.
- **#3 — low confidence, wrong → well-flagged.** The answer is wrong (aliasing: `ys = xs`
  binds a second name to the *same* list, so `.append` is seen through `xs` too →
  `[1,2,3,4]`). But the learner *said 60%* — they **flagged their own uncertainty**. A wrong
  answer that was honestly marked uncertain is a **calibration success even though it's an
  accuracy failure**. This is exactly the behavior to reward.

**Verified ground truth recap** (so calibration is measured against real output, never an
asserted answer): `abababc`, `False`, `[1, 2, 3, 4]`.

**What the trace makes visible** (and a bare score hides): the batch's *average*
overconfidence (82% vs 33%) is real, but the **diagnosis lives in the pairs** — #2 is a
fluency-trap overconfidence to *fix*, while #3 is a wrong answer the learner *handled
correctly* by doubting it. A coach who only said "1 of 3, badly overconfident" would miss
that the learner's confidence *ordering was partly right* (they were least sure on one they
missed) and would wrongly lump the well-flagged #3 in with the dangerous #2. **Calibration
is scored on the relationship between the two columns, not on either alone.**

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), the full loop
> *helps novices* (it externalizes a process they can't yet run) but becomes **redundant
> load** for the more advanced, who should run it themselves. So the coach fades it:
>
> | Tier | Worked-example depth at F1 |
> |---|---|
> | **Foundations** | **Full** — the complete predict → confidence → run → score-both loop above, every column shown. |
> | **Working** | **Partial** — coach runs the snippets and reveals the hit rate, then leaves the **over/under-confident verdict and the per-pair diagnosis** for the learner to compute. |
> | **Advanced** | **Skeleton** — coach hands back only the `(confidence, correct?)` pairs and asks the learner to state the calibration verdict, name which pair is the costliest miss, and say *why* their confidence there was unearned. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for F1. Grading mode is
declared up front: **executable ground truth (for the prediction) + metacognitive scoring
(confidence vs. measured correctness)** (§5d).

> **The F1 drill shape.** Every F1 drill **wraps an executable prediction in a confidence
> layer**. The learner (a) states a confidence *before* answering, (b) makes the prediction,
> (c) the coach obtains ground truth via the runner, (d) the coach scores **both**
> correctness *and* calibration. A single trial is noise; calibration is read over **≥3
> trials** (`assessment.md` F1 entry task). This is the **predict-then-check** task from the
> assessment, used here as the drilling engine.

### 5a. Tier definitions (F1-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module:

| Tier | F1 criterion | Example shape |
|---|---|---|
| **Foundations** | **One** predict-the-output snippet on a familiar surface + a confidence rating; run it; score BOTH correctness and whether the confidence was justified. Teach *noticing the gap* and that confidence is gradable. | "Predict the output AND rate confidence 0–100%" on `print(3 * "ab" + "c")`. |
| **Working** | A **short battery** (~3 snippets) of *varied trickiness* — each predict + confidence — then measure **hit-rate vs. average confidence** (over/under-confident?) and read the *ordering*. **Must include ≥1 deceptively-simple-looking-but-tricky case (a calibration trap).** | The `0.1+0.2`, aliasing, `range` step battery; compute over/underconfidence. |
| **Advanced** | Calibrate on **genuinely tricky** code (closures / aliasing / eval-order) **and** an **"AI wrote this function — what would you verify before trusting it, and how confident are you it's correct?"** scenario, graded on the verification plan + calibrated trust. | Late-binding closure comprehension; an AI `median` with a mutation + empty-input bug. |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable calibration. | — |

A drill is mis-tiered if it asks for more (Foundations must be *one* simple snippet; the
*trap* belongs at Working; the *AI-trust* judgment belongs at Advanced). Apply the
self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b,
§4 check 3). The axes for F1:

- **Underlying snippet difficulty** — genuinely-easy · deceptively-easy (a *trap*: looks
  trivial, behaves surprisingly — floats, integer division, operator precedence, chained
  comparison, default `str`/`repr`) · genuinely-hard (closure / aliasing / generator /
  eval-order / `+=`-on-mutable). **Varying this axis is the whole point** — calibration only
  shows up when difficulty varies under the learner.
- **Confidence scale** — numeric 0–100% · coarse low/medium/high · a forced *ranking* of N
  snippets from most- to least-sure (tests *relative* calibration without absolute numbers).
- **Calibration direction the drill probes** — overconfidence (a trap) · underconfidence (a
  snippet that *looks* scary but is simple, e.g. a long-looking but linear trace) · ordering
  (does high confidence land on the ones they got right?).
- **Source of the code to judge** — coach-authored · **AI-attributed** ("an assistant wrote
  this") · the learner's *own* prior wrong prediction (re-rate after error).
- **What's scored as the metacognitive artifact** — average-confidence-vs-hit-rate
  (over/under) · confidence *ordering* vs. outcomes · **pre-reveal confusion flag** (did
  they name the uncertain sub-step *before* the answer?) · a **verification plan** (for AI
  code: *what would you run/check, in what order?*) · calibrated *trust* ("how sure is the AI
  right, and what evidence would change that?").
- **Format** (`drill-generation.md` §6) — primarily **Prediction → Observation →
  Reflection** *with a confidence rating attached* (the home format); also **Teach-it-back**
  ("explain why your confident-but-wrong answer felt right"); **Error analysis** (re-rate a
  past miss); **Debug-this** wrapped in "how sure are you this is the bug?".

Keep an in-session log of the `(difficulty-mix, confidence-scale, probe, source, format)`
tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error (mis-calibration) catalog

The *specific* calibration failures, each with the metacognitive gap it diagnoses
(`drill-generation.md` §1c format). Grounded in the calibration literature — Lichtenstein &
Fischhoff 1977, Kruger & Dunning 1999, Koriat & Bjork 2005, Dunlosky & Rawson 2012,
Flavell 1979 — and the AI-era synthesis (METR 2025; Fernandes 2025; Tankelevitch 2024). The
root of most is one stance: **treating the *feeling* of knowing as evidence of knowing,
instead of as a hypothesis to be checked against ground truth.**

```
Error: Reports high confidence (e.g. 90%+) on nearly every snippet regardless of its
       difficulty; confidence does not vary as the code gets trickier.
Diagnoses: Flat-high / no-discrimination calibration. The learner is not monitoring
           difficulty at all — "I'm sure" is a default, not a reading. Accuracy falls on
           the hard items but confidence doesn't, so overconfidence GROWS exactly where
           being wrong is costliest. (Lichtenstein & Fischhoff 1977, the hard-easy effect.)
Example trigger: a Working battery mixing a one-liner with a closure-in-a-loop; learner
                 rates both 95%.

Error: Gives high confidence to a snippet that LOOKS trivial but behaves surprisingly, and
       is wrong (e.g. 90% that 0.1 + 0.2 == 0.3 is True).
Diagnoses: The fluency trap — confidence bought by smooth reading, not by tracing. Ease of
           PROCESSING the text was mistaken for knowledge of the BEHAVIOR. (Koriat & Bjork
           2005, illusions of competence.)
Example trigger: print(0.1 + 0.2 == 0.3)  → predict + confidence; actual is False.

Error: Discovers uncertainty only AT the reveal — never says "I'm unsure about X" while
       reasoning, then claims "oh, I knew that was the tricky part" after seeing the answer.
Diagnoses: Monitoring failure / hindsight relabeling. The metacognitive act of flagging
           confusion EARLY (during reasoning) isn't happening; "I knew it" is reconstructed
           post hoc. (Flavell 1979, cognitive monitoring; the value is the PRE-reveal flag.)
Example trigger: any trap snippet — check whether the uncertain sub-step is named before
                 the answer or only after ground truth is shown.

Error: Wrong answer delivered with high confidence AND no flag — the learner neither got it
       right nor doubted it.
Diagnoses: The consequential miscalibration (wrong-and-certain). In the AI era this is the
           one that ships the bug: nothing internal fired to say "verify this." Distinct
           from wrong-but-flagged, which is a calibration SUCCESS. (Kruger & Dunning 1999,
           the dual burden — the skill to do it and to judge it overlap.)
Example trigger: the aliasing snippet rated 95% and predicted [1,2,3] (no append seen).

Error: Trusts an AI-written function because it "looks right" / "looks like what I'd write,"
       giving high confidence without naming a single thing to verify.
Diagnoses: Plausibility-as-correctness. Confidence in code-not-written is coming from
           surface fluency of the code, not from checking inputs/edge cases/side effects.
           The AI-era keystone failure; more AI-literate users are MORE prone to it.
           (Fernandes 2025; Tankelevitch 2024 — output evaluation needs well-adjusted
           self-confidence.)
Example trigger: the AI `median` drill — high trust, no mention of empty input or that
                 .sort() mutates the caller's list.

Error: Equally confident the AI function is correct as that it is wrong; cannot say WHAT
       evidence would move that confidence.
Diagnoses: Un-anchored trust — confidence isn't tied to verifiable evidence, so it can't be
           updated. Calibrated trust means "X% it's right, and running case Y would change
           that." (Nelson & Narens 1990 — monitoring must connect to a control decision.)
Example trigger: "how confident are you the AI's function is correct, and what one check
                 would most change that number?"

Error: Systematically LOW confidence on snippets the learner then gets right; treats every
       problem as a coin flip.
Diagnoses: Underconfidence / no credit for real knowledge. Less costly than overconfidence
           but still miscalibration — it wastes verification effort and can stall decisions.
           Often a long-looking-but-linear trace rated scary. (Calibration is two-sided;
           Dunlosky & Rawson 2012.)
Example trigger: a 12-line straight-line trace (no tricks) rated 30%; learner gets it right.

Error: After being shown a confident-but-wrong answer, does not lower confidence on the
       next similar snippet — repeats the same 90% on the same class of trap.
Diagnoses: No adjustment / broken control loop. Monitoring fed back a miss but control
           didn't act on it; calibration can't improve without the downward update.
           (Nelson & Narens 1990 control flow; Dunlosky & Rawson 2012 — overconfidence
           persists and degrades outcomes if uncorrected.)
Example trigger: two float-equality traps in a session; same high confidence on the second.

Error: Confuses being RIGHT with being CALIBRATED (or being WRONG with being miscalibrated)
       — e.g. dismisses a wrong-but-flagged answer as a failure, or counts a lucky
       high-confidence guess as good calibration.
Diagnoses: Conflating the two graded quantities. Correctness is object-level; calibration is
           the confidence↔outcome RELATIONSHIP. A right answer with a hand-wavy 50% is not
           well-calibrated; a wrong answer honestly marked uncertain is. (The core F1
           distinction; see §3 and the worked example #3.)
Example trigger: ask the learner to self-assess after the batch — do they grade their
                 confidence, or just recount how many they got right?
```

### 5d. Grading mode

**Executable ground truth (for the prediction) + metacognitive scoring (confidence vs.
measured correctness)** (`drill-generation.md` §1d, §3 hybrid). Two parts, scored
separately and **both reported**:

1. **The prediction → executable.** The coach **runs the snippet** via
   `python <skill-dir>/runtime/python/runner.py snippet.py`, parses the `RunResult` JSON,
   and grades the prediction against `stdout` (strip the trailing newline before comparing
   to a bare prediction) and/or `status` when the drill is "does it raise?". The coach
   **never guesses** the output — calibration is only meaningful against **real** ground
   truth, never an asserted answer.
2. **The calibration → metacognitive scoring.** Against the *measured* correctness, the
   coach computes, over the batch:
   - **hit rate** (fraction correct) vs. **average confidence** → over/under/well-calibrated
     (the §3 calibration rule);
   - **ordering** — were higher-confidence items right more often than lower-confidence
     ones?
   - **pre-reveal confusion flag** — did the learner name the uncertain sub-step *before*
     the reveal? (a monitoring credit independent of correctness);
   - for AI-code drills, the **verification plan** (rubric, §3 + exemplars) and **calibrated
     trust** (is the trust number tied to evidence that could move it?).

The two verdicts are **independent and both stated** (`drill-generation.md` §3): a *correct*
prediction with a **flat-high** confidence is a *partial* pass (it may be luck — exactly the
fluency illusion this module exists to break); a *wrong* prediction that was **honestly
flagged low** is a **calibration success** even though the answer failed. Report it as such —
do **not** collapse calibration into the accuracy score.

> **Why ≥3 trials.** A single `(confidence, correct?)` pair cannot distinguish luck from
> calibration. The coach reads over/under-confidence and ordering across **at least three**
> trials (`assessment.md` F1 task: "a single trial is noise"). Foundations runs *one* to
> teach the loop; the calibration *verdict* needs the Working battery or an accumulated set.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated calibration ceiling**
and presses **one step** past their last comfortable success along a single axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = calibrated on genuinely-tricky code in isolation, *plus* one AI-trust
  judgment with a verification plan.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  calibration demand OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for F1, with step counts:

1. **Stakes-weighted calibration** (the canonical path): move from "is your confidence
   *accurate*?" to "is it *well-spent*?"
   - Frontier-1: a battery where snippets carry **different costs of being wrong** (a
     read-only print vs. a function that *mutates shared state*); calibrated *and* you
     verified the high-cost ones harder (Advanced + 1: cost-sensitivity).
   - Frontier-2: the above **under a time/effort budget** — you can only run N of the M
     snippets; pick which to verify by where your confidence is *both* low *and* the cost
     high (+1: triage).
   - Frontier-3: the above where **some snippets are AI-written and some yours**, and you
     must allocate scarce verification across both (+1: mixed provenance).

2. **Deeper AI-trust judgments** (push the AI-code dimension): from "what would you verify?"
   to (a) *writing the actual checks* and running them; (b) calibrating trust on an AI
   function whose bug is **subtle and only on one input class** (so plausibility is
   especially seductive); (c) calibrating on an AI *explanation* of code (does the rationale
   match what the runner shows?). Each is one increment over Advanced.

3. **Calibrating the calibration** (meta): predict your **own hit rate** on the next batch
   *before* taking it, then check the meta-prediction against the result — calibrating your
   model of your own calibration. One increment.

4. **Resolution under fluency pressure** (push the trap dimension): batteries built entirely
   of *deceptively-simple-looking* snippets, where every item invites overconfidence — can
   the learner hold *appropriate doubt* across a whole set that "looks easy"? One increment.

5. **Cross-module calibration → hand off in-flow.** F1 is the lens, not a silo: the richest
   Frontier is **calibrating live inside another module** — rate confidence before every A1
   prediction, C1 hypothesis, or E3 review for a session, and read the curve across that
   real work. This isn't a separate F1 drill so much as F1 *instrumenting* the rest of the
   curriculum; track it on the relevant module while F1 holds the calibration history.

Track the level as `F1: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2. Two
cross-cutting requirements apply at every tier above Foundations: **product *and* process**
(here, **correctness *and* calibration** — a correct streak with flat-high confidence is a
Foundations-level pass at best, because it may be luck and shows no monitoring), and
**unaided + durable** (a same-session calibration read is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for F1 |
|---|---|
| **Foundations** | On a **single** predict-the-output snippet with a confidence rating, completes the loop: makes the prediction, and — shown ground truth from the runner — can **say whether the confidence was justified** (high+correct = earned; high+wrong = the gap to notice; low+wrong = well-flagged). Grasps that **confidence is itself gradable**, separate from the answer. Allowed *with* the worked-example loop faded to one missing step. |
| **Working** | On a **battery of ≥3 unseen snippets of varied trickiness — including ≥1 deceptive (trap) case** — predicts + rates confidence on each **unaided**, then **computes the calibration verdict**: average confidence vs. hit rate (over/under-confident), and reads the **ordering** (were the high-confidence ones the right ones?). Correctly identifies the **fluency-trap miss** as the costly one and a **wrong-but-flagged** item as a calibration success — i.e., does **not** conflate being right with being calibrated. |
| **Advanced** | Calibrates on **genuinely tricky** code (a closure/aliasing/eval-order snippet) **and** handles the **AI-trust scenario**: given an "AI-wrote-this" function, produces a **prioritized verification plan** (names the edge cases / side effects / input classes to check, *in order*), states a **calibrated trust** number **tied to evidence that could move it**, and — after the check reveals the bug — explains why plausibility was not correctness. Articulates the underlying principle on a teach-it-back (`drill-generation.md` §6: "why did the confident-but-wrong answer feel right?"), not just the instance. |
| **Frontier** | `Frontier-N`: presses one calibration demand past the last comfortable success per §6 / `drill-generation.md` §5 (stakes-weighted → budgeted triage → mixed provenance; or deeper AI-trust; or meta-calibration). A moving target, not a fixed bar. |

**Scaffolding under struggle is calibration-specific** (`coaching-loop.md` Step 7 — fade the
scaffold, never the challenge): an **overconfident** learner is not *told* the answer; they
are sent to **earn** the confidence — *"trace it as a state table (A3), then re-rate before
I run it."* The difficulty of the setup rises; the answer they must generate stays theirs.

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from the learner's *demonstrated* calibration on unseen batches, never from claimed
seniority or self-rated confidence (self-rating is the very thing under test). Held-out
re-assessment and real-code transfer outrank a same-session calibration read
(`assessment.md` Part 5) — and note the AI-era finding cuts directly here: **more AI-literate
learners may *self-report* better calibration while being worse** (Fernandes 2025), so the
coach trusts the **measured** confidence↔outcome curve, not the learner's account of it.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Confidence as a constant.** Reporting the same high certainty on everything, so the
  number carries no information — the hard–easy effect made personal (Lichtenstein &
  Fischhoff 1977). The fix is to make confidence *vary* with difficulty and *check* it.
- **Mistaking fluency for knowledge.** "It reads clearly, so I understand it" / "the AI code
  looks right, so it's right." Smooth processing is a property of the *text*, not evidence
  about the *behavior* (Koriat & Bjork 2005). The only cure for behavior-confidence is a
  behavior-check (trace / run / test the edge).
- **Discovering doubt only at the reveal.** Not flagging the uncertain sub-step *while*
  reasoning, then claiming "I knew that was the tricky bit" afterward (Flavell 1979
  monitoring; hindsight relabeling). The valued act is the *pre-reveal* flag.
- **Trusting AI output by plausibility.** Granting confidence to code-you-didn't-write
  because it resembles what you'd write, without naming one thing to verify — the keystone
  AI-era failure, *amplified* among the more AI-literate (Fernandes 2025; Tankelevitch
  2024). The fix is a verification plan tied to evidence.
- **Not updating after a miss.** A confident-but-wrong answer that doesn't lower the next
  similar confidence — monitoring fired but control didn't act (Nelson & Narens 1990;
  overconfidence then persists and degrades outcomes, Dunlosky & Rawson 2012).
- **Confusing right with calibrated.** Treating a wrong-but-flagged answer as a failure, or
  a lucky confident guess as good calibration — collapsing the two independent quantities
  this module keeps separate.

**Evidence caveat (this is a `[Verified-adjacent]` module — say so plainly).** Two honest
limits, both surfaced to the learner when relevant:

1. **General vs. programming-specific.** The metacognition/calibration science (Flavell;
   Nelson & Narens; Lichtenstein & Fischhoff; Kruger & Dunning; Koriat & Bjork; Dunlosky &
   Rawson) is **well-established general cognitive/educational psychology** — but it was
   established on **general-knowledge questions, text comprehension, and classroom learning,
   not on professional code**. That calibration training *transfers to* and *causally
   improves* software work is an **extrapolation**, honestly labeled. The coach says: *"this
   is solid learning science in general; the programming-specific evidence is thinner."*
2. **The AI-era evidence is real but young.** The perception–reality gap (METR 2025) and the
   literacy→overconfidence finding (Fernandes 2025) are the **best-evidenced** AI-era
   results and they motivate this module's keystone status — but they are **small-N and
   recent**, and the productivity *direction* is **contested** (METR is revising after
   later data; `evidence-base.md` → AI-era honesty caveats). So this module is
   **priority-steering, not proof**: calibration is *plausibly* the highest-leverage AI-era
   skill, and the **transfer task (§9)** — calibrating on the learner's *own* code and
   *own* AI usage — is the honest individual-level test, not a citation.

No claim in this module is presented as `[Verified]`. The badge is `[Verified-adjacent]`,
and the limits above are part of the teaching, not a footnote.

---

## 9. Transfer task

**The only honest test of whether the calibration drill transferred to the job is applying
it to the learner's own real code — and, in the AI era, their own AI usage**
(`assessment.md` Part 4; `evidence-base.md` → transfer caveat, consequence 2; AI-era
impact).

> **Your turn (two parts, both on *your* work):**
>
> **Part A — calibrate on your own code.** Pick an **unfamiliar module of your own system**
> you haven't touched in a while (or a teammate's you're about to review). *Before* reading
> closely, write down a **confidence (0–100%)** that you can correctly predict what one
> specific function returns on a specific input. Then **predict it, write the confidence
> down, and check** — run it (reduce it to a minimal snippet and use `runner.py` for any
> executable sub-claim), or step through it. Was your confidence earned? Where did *smooth
> reading* buy you confidence the *behavior* didn't?
>
> **Part B — calibrate your trust in AI.** Take a function (or block) **an assistant recently
> wrote for you** and that you *accepted*. *Before* re-examining it, rate **how confident
> you are it's correct (0–100%)** and write down the **two things you'd verify first** and
> *why those two*. Then verify them (run the edge cases; check side effects and shared
> state). Did the AI code do what you assumed? Was your accept-time confidence calibrated —
> or did plausibility stand in for a check?

**Grading is softer and named as such** (`assessment.md` Part 4). Real code and real AI
usage have no clean answer key for *confidence*; the coach grades against the §7 rubric and
says: *"this is a judgment call on your real work, not a machine-verifiable result."* But
the **prediction** half is still pinned to ground truth wherever the code (or a reduced
snippet) is runnable — the coach uses the runner for any executable sub-claim, so
calibration is measured against real output, not assertion. **Transfer evidence is weighted
heavily, and doubly so here:** a learner who calibrates well on synthetic batteries but
**accepts their own AI output on plausibility** has not transferred the skill that this
module exists for — the tracker notes that gap as more diagnostic than another passed
synthetic battery, because *that exact gap* (felt-faster-while-slower, trust-by-plausibility)
is the AI-era failure the curriculum is built to close (spec §12).

---

## Cross-references

- Drill mechanics, exercise formats, executable ground-truth protocol, hybrid grading,
  Frontier escalation: `references/drill-generation.md` (this module instantiates §1 and
  follows §2, §3 hybrid, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  the "trace-then-re-rate" scaffold under overconfidence): `references/coaching-loop.md`.
- **F1 entry task** (predict-then-check confidence calibration; ≥3 trials to read a pattern;
  the "95% three times, right once = overconfident" read), per-skill routing, mastery-rubric
  shape, held-out re-assessment, transfer weighting, the optional affective layer:
  `references/assessment.md`.
- Evidence grounding (AI-era impact: METR 2025 / Fernandes 2025 / Tankelevitch 2024;
  instructional pillar: Metacognition + Illusions-of-fluency rows; transfer caveat; learning
  ≠ performance): `references/evidence-base.md`. The general calibration citations are **now
  grounded in `evidence-base.md`** (→ Metacognition & calibration (module F1)): Flavell 1979;
  Nelson & Narens 1990; Lichtenstein & Fischhoff 1977; Kruger & Dunning 1999; Koriat & Bjork
  2005; Dunlosky & Rawson 2012.
- Golden exemplars (~3 per tier, runner-verified predictions + gold calibration/AI-trust
  rubrics): `exemplars/F1/foundations.md`, `exemplars/F1/working.md`, `exemplars/F1/advanced.md`.
