# Assessment — Routing, Mastery Rubrics & Measurement

How the coach **routes** a learner to a starting tier per skill, what **observable bar**
defines each named tier, how it **measures improvement** over time, and an **optional**
affective self-report layer. This file is run from `coaching-loop.md` Step 1 (Locate)
for new learners and at fixed checkpoints for returning ones.

Three rules govern everything in this file, and they trace to `evidence-base.md`:

1. **Performance, not tenure.** Years of experience is a weak, inconsistent proxy for
   measured skill (`evidence-base.md` → Finding 7). The coach assigns tiers by what the
   learner *does* on a task, never by claimed seniority, job title, or self-rating.
2. **Recommend, never gate.** Every result here yields a *recommended starting tier* and
   *recommended modules*. It is a buffet (`evidence-base.md` → design; spec §9): the
   learner may sample any module at any tier regardless of what the assessment says. The
   word "route" in this file always means "suggest a starting point."
3. **Within-person progress, not a certified grade.** No validated absolute measure of
   programming expertise exists (`evidence-base.md` → transfer caveat). Everything here
   measures a learner's *delta against their own baseline* on concrete tasks — never an
   absolute expertise score, and never a "can / can't program" verdict (the "two humps"
   aptitude framing is rejected outright; `evidence-base.md` → folklore).

> **Assessment tasks are drills.** An entry task is a drill graded by the exact
> machinery in `drill-generation.md`: executable tasks get **executable ground truth**
> (the coach *runs* the code — never guesses the answer); judgment tasks get
> **rubric + exemplars**. The only thing special about an entry task is *when* it runs
> and *what it's used for* (routing + baseline). Delivery follows `coaching-loop.md` —
> including the **pause / no-spoiler** hard stop after posing each task.

---

## Part 1 — Entry / Routing Assessment

### 1.1 What the battery is and is not

A short **performance battery**: one concrete task per core skill. Each task is built to:

- **(a) Score process AND product.** The product is the answer; the *process* is the
  reasoning the learner produced on the way there. Both are recorded. For several skills
  the *process* is the primary signal — e.g., the debugging task scores the learner's
  *first three hypotheses and how they would test them*, **not** whether they ultimately
  found the bug. A learner who guesses the bug with no method scores *lower* on process
  than one who lays out a clean hypothesis-and-test plan and hasn't found it yet.
- **(b) Map to a recommended tier for *that* skill.** Each task has a per-skill rubric
  (Part 2) that lands the result on Foundations / Working / Advanced. Tiers are assigned
  **per skill**, independently — a learner can be Advanced on tracing and Foundations on
  testing. This is expected, not an anomaly.
- **(c) Never gate.** The result recommends a starting point. The learner can still
  sample anything. The coach says so explicitly when reporting results.

The battery is **not** a certification, **not** pass/fail, and **not** a ranking against
other people. It is a baseline snapshot and a router.

### 1.2 Administration

- **Pick the spine first.** The full battery is ten tasks; that is a lot to ask up front.
  Default to administering the **high-evidence / high-impact spine** first —
  **A1, A2, A3, C1, F1** (Track A comprehension foundation + debugging + calibration;
  these are the verified core and the AI-era verification priority, spec §12) — and offer
  the rest (B1, B2, B3, C2, E3) as the learner reaches for those skills. A learner may
  also ask to do the whole battery at once, or skip straight to a module and be assessed
  in-flow on the first drill.
- **One task at a time, with a hard stop.** Pose a task using the pause markers from
  `coaching-loop.md` (Delivery Disciplines → "Pause for input"), then **end the message
  and wait**. No hints, no "think about…", no worked steps until the learner replies.
  This is the generate-before-reveal condition; an entry task is the learner's *first*
  pre-test on that skill, and a failed attempt is high-value baseline data
  (`evidence-base.md` → pre-testing).
- **Capture the process, not just the answer.** Ask the learner to *show their reasoning*
  as part of the task ("predict the output **and** say why," "list your first three
  hypotheses **and** how you'd test each"). Record the reasoning verbatim in the tracker's
  baseline cell, because it is what the per-skill rubric grades.
- **Ground truth by running, where executable.** For A1/A2/A3/B2/C1/C2 the coach obtains
  truth via the runner (`drill-generation.md` §2), never by predicting output. For
  B1/B3/E3/F1 the coach grades against the rubric + exemplars (`drill-generation.md` §3)
  and says out loud: "this is a judgment call graded against the rubric, not a
  machine-verifiable answer."
- **Record the baseline.** Each task result is written to `progress-template.md` as the
  module's **Baseline (date / score)** plus seed entries in **Recurring errors**. That row
  *is* the measurement instrument; Part 3 re-runs against it.

### 1.3 Partial-knowledge routing boundary (general principle)

When scoring the learner's *process* on any entry task, the answer often falls between
"no idea" and "fully correct." Apply this three-way rule, which holds across all
modules:

| What the learner produces | Route to |
|---|---|
| **Names the right mechanism but inverts its semantics or timing** — e.g., says "closures capture by value / at definition" when the correct model is "by reference / at call time"; or says "the default is re-evaluated each call" when it is evaluated once at definition time. | **Working** — the learner has a partial model that needs correcting, not built from scratch. |
| **No correct mechanism named; cannot engage the state model at all** — vague intent-reading ("it just adds things up"), a blank, or a mechanism that belongs to a different language/paradigm with no relevant contact with the right idea. | **Foundations** — the mental model needs to be built. |
| **Correct semantics AND can articulate the state model** — names the right mechanism and its direction/timing correctly, even if the final prediction is arithmetically off. | **Advanced** (or Working if only one mechanism demonstrated) — promote per the per-module rubric. |

**Why the middle case routes to Working, not Foundations:** a learner who can name the
right mechanism (even inverted) has built a partial schema. Correct-direction teaching is
faster and more effective than schema-building from zero; the Working tier's drills are
designed for exactly this correction. Sending a partial-knowledge learner to Foundations
wastes both time and motivation.

**A1 as the worked example.** On the late-binding closure drill (`make_adders` → prints
`12 12 12`), a learner who predicts `10 11 12` and says "each lambda captures the loop
variable's *current value* when the lambda is *defined*" has the mechanism right
(closure captures the variable) but the timing inverted (definition-time snapshot vs.
call-time read) → **Working**. A learner who says "the loop adds 0, 1, 2 to 10" and
cannot name closures at all → **Foundations**. A learner who predicts `12 12 12` and
explains that all three lambdas share the same variable `i`, read at call time after the
loop ends → **Advanced**.

This boundary applies to every skill's entry rubric; the per-module rubrics in Part 2
instantiate it with module-specific mechanism names.

---

### 1.4 The tasks

Each task below gives its **shape** (what to generate), **what's scored** (process +
product), and **how it routes** (which rubric in Part 2 decides the tier). Two or three
include a **concrete example** the coach can administer as-is or vary along the module's
parameter space. The coach should normally **generate a fresh instance** rather than reuse
the printed example verbatim, so the battery can be re-run later with held-out items
(Part 3).

---

#### A1 — Notional machine / execution model

- **Shape.** Give a short snippet whose behavior hinges on the execution model rather than
  syntax — aliasing, rebinding-vs-mutation, closure capture, mutable default argument,
  or short-circuit evaluation. Ask the learner to **predict the output AND explain the
  state changes** that produce it.
- **Scored.** *Product:* is the predicted output exactly right (graded by running the
  snippet)? *Process:* does the explanation describe the **machine's state transitions**
  (name binding, what each name points to, when defaults are evaluated) rather than the
  code's *intent*? A correct output with a hand-wavy or wrong reason is a partial pass —
  flag it, because it often reflects luck, not model accuracy (`evidence-base.md` →
  illusions of fluency).
- **Routes via** the A1 rubric (Part 2). Mis-predicting simple rebinding → Foundations;
  fluent on rebinding/aliasing but missing definition-time defaults or closure capture →
  Working; correct *and* well-explained on a multi-mechanism snippet → Advanced.
- **Concrete example** (Foundations/Working boundary — closure + aliasing):

  ```python
  def make_adders():
      fns = []
      for i in range(3):
          fns.append(lambda x: x + i)
      return fns

  a, b, c = make_adders()
  print(a(10), b(10), c(10))
  ```

  Ask: "What does this print, and *why*?" Ground truth is obtained by running it
  (it prints `12 12 12`, not `10 11 12`). The discriminating signal is **process**:
  does the learner explain that the lambdas **capture the variable `i`, not its value at
  loop time**, so all three see the final `i == 2`? A learner who predicts `10 11 12`
  has a *copy-at-definition* model of closures — record that exact gap ("late-binding
  closure capture") in the tracker.

---

#### A2 — Code reading & chunking

- **Shape.** Show an unfamiliar function of ~15–30 lines (a recognizable algorithm or a
  small piece of plausible application logic). Give the learner a brief viewing, then ask
  two things: **(1) summarize what it does in 1–3 sentences**, and **(2) name the chunks** —
  what are the 2–4 meaning-bearing parts, and what beacon told them so?
- **Scored.** *Product:* is the summary accurate (does it capture purpose, not just
  restate lines)? *Process:* did the learner read **for structure** — grouping lines into
  semantic units and citing beacons (a `swap` inside nested loops → sort; an accumulator
  init + update + return → reduce) — or did they narrate line-by-line on surface syntax?
  Line-by-line narration with a vague summary is the Foundations signature; fast,
  structure-first chunking with named beacons is the Advanced signature (`evidence-base.md`
  → Findings 2 & 3).
- **Routes via** the A2 rubric. Optionally probe the boundary: ask one consequence
  question ("what changes if line N flips its comparison?") to distinguish a learner who
  *recognized* the structure from one who *guessed* the label.

---

#### A3 — Execution tracing & explain-in-plain-English

- **Shape.** Give a snippet with a loop and a running accumulator, or a small recursive
  function. Ask the learner to **trace the state at each step** (variable values per
  iteration, or the call tree with arguments and returns) **and then explain in one
  sentence what the code computes**. This is the Trace-the-path format
  (`drill-generation.md` §6).
- **Scored.** *Product:* is the final traced value correct (graded by running)? Is the
  plain-English explanation accurate? *Process:* is the **intermediate state** right at
  each step, or only the endpoint? Tracing + explaining sit *below* writing in the skill
  hierarchy and predict writing ability (`evidence-base.md` → Finding 6), so a learner who
  gets the endpoint but botches the intermediate states is **not** yet solid here — record
  which step the trace diverged.
- **Routes via** the A3 rubric. A correct 3-iteration loop trace → at least Working; a
  correct trace through a recursive call tree with accurate frame-by-frame state →
  Advanced.

---

#### B1 — Problem decomposition & planning

- **Shape.** Give a small, ambiguous problem statement (e.g., "design the pieces of a
  function that, given a server log file, returns the three users with the most failed
  logins in the last hour"). Ask the learner to **decompose it into named sub-problems and
  sketch a plan *before* writing any code** — inputs, the sub-steps, the data shape passed
  between them, and the edge cases they'd handle. **No code required.**
- **Scored.** *Product:* is the decomposition complete and at a *consistent level of
  abstraction* (experts keep the parts balanced; novices mix one fully-coded step with
  three vague ones — `evidence-base.md` → Finding 5)? *Process:* did the learner **plan
  top-down** (name the whole shape first, then refine) or **translate linearly** (jump
  straight into the first line of code)? Naming edge cases unprompted (empty file,
  ties, timestamp parsing) is a strong-process signal.
- **Routes via** the B1 rubric. Judgment-graded against exemplars. **Caveat baked in:**
  the coach grades *decomposition and planning*, **not** adherence to any "plan catalog" —
  that idea was refuted (`evidence-base.md` → Refuted; Gilmore & Green 1988). There is no
  single correct decomposition; the rubric rewards completeness, balance, and explicit
  edge-case surfacing, not matching a template.

---

#### B2 — Code writing & composition

- **Shape.** Give a precise spec for a small function (3–8 lines of logic) with at least
  one edge case that a naive version misses. Ask the learner to **write the function**.
- **Scored.** *Product:* run it against a small set of inputs the coach prepares
  (including the edge case) via the runner — executable ground truth. Does it pass? Does
  it handle the edge case? *Process:* did the learner build it up in verified steps or in
  one untested leap; did they state the spec back / name the edge case before coding (the
  writing end of reading→tracing→writing — `evidence-base.md` → Finding 6)?
- **Routes via** the B2 rubric. Correct on the happy path only → Working; correct
  including the edge case, with clean composition → Advanced. *Soft prerequisite signal:*
  if B2 is weak but A3 is also weak, the tracker should note that tracing likely underlies
  the writing gap (do **not** gate — just inform the recommendation).

---

#### B3 — Testing & specifying correctness

- **Shape.** Give a function (correct or with a latent edge-case bug) and ask: **"What
  would you test? Enumerate the cases — and for each, say what property or behavior it
  checks."** Adversarial thinking about code's correctness, not writing a test harness.
- **Scored.** *Product:* did the learner's case list **include the cases that actually
  matter** (boundaries, empty / single / many, the edge case the function mishandles if
  one exists)? *Process:* are the cases organized by **property** ("monotonic," "handles
  empty," "idempotent") rather than a flat list of arbitrary inputs? Does the learner
  reason about *what "correct" means* for this function, or only sample a few values?
- **Routes via** the B3 rubric. Judgment-graded. A handful of happy-path inputs →
  Foundations; systematic boundary + empty/degenerate coverage → Working; property-level
  reasoning and identifying the function's implicit contract → Advanced.

---

#### C1 — Systematic / hypothesis-driven debugging

- **Shape.** Present a **failing test plus the buggy function it exercises** (and the
  observed wrong output / traceback). Ask the learner for their **first three hypotheses
  about the cause, ranked, and exactly how they would test each** to confirm or eliminate
  it. **Do not** ask them to find the bug.
- **Scored — process is the primary signal.** *Process:* are the hypotheses **specific and
  falsifiable** ("the slice on line 4 is off-by-one so the last element is dropped — I'd
  test by printing `len(result)` against `len(input)`"), and does each come with a
  **discriminating test** that would actually narrow the search (bisection, a targeted
  print, a minimal reproducing input)? *Product (secondary):* are the hypotheses
  *plausible* given the evidence in the traceback / failing assertion? A learner who names
  one vague hypothesis and proposes "add print statements everywhere" scores **low on
  process** even if the bug is obvious; a learner who lays out three sharp, testable
  hypotheses scores **high** even without naming the culprit. This mirrors debugging-as-
  science (`evidence-base.md` → Finding 4; C1's method is `[Practitioner-canon]` — the
  *causal* superiority of tracing was refuted, so the rubric rewards method *quality*, not
  a single prescribed technique).
- **Routes via** the C1 rubric.
- **Concrete example** (administer or vary):

  ```python
  # failing test:
  #   assert running_max([3, 1, 4, 1, 5, 9, 2]) == [3, 3, 4, 4, 5, 9, 9]
  # observed: AssertionError — got [3, 3, 3, 4, 4, 5, 9]

  def running_max(xs):
      out = []
      m = xs[0]
      for x in xs:
          out.append(m)        # record the max-so-far ...
          if x > m:            # ... BEFORE considering the current element
              m = x
      return out
  ```

  The coach obtains ground truth by **running** the function (it really does print
  `[3, 3, 3, 4, 4, 5, 9]` — the whole output lags one step, so the new maximum always
  shows up one position too late and the final `9` is dropped off the end). The
  discriminating signal is the **shape of the hypothesis set**, not whether the learner
  spots the line. Strong process reasons from the **evidence already present** — the
  output is right-shifted by one and one element short — and looks like: *"H1: the result
  is lagging the input by one position, so a value is being recorded before it's been
  considered; I'd test by checking whether `out[i]` always equals the max of `xs[:i]`
  rather than `xs[:i+1]`. H2: ordering bug inside the loop — the append happens before the
  comparison/update; I'd swap the two statements and re-run. H3: an off-by-one in
  initialization (`m = xs[0]` plus an early append double-counts the first element); I'd
  print `m` and the appended value each iteration to see where they diverge."* Record
  whether the learner **localized from the symptom** (everything shifted by one → look at
  statement *order*, not the max logic) or jumped to rewriting the function wholesale and
  proposed "add prints everywhere" with no discriminating test.

---

#### C2 — Reading stack traces & error messages

- **Shape.** Show a multi-frame traceback (or a compiler/interpreter error) from code the
  learner can see. Ask: **"Where is the fault, what is the runtime telling you, and what
  single piece of evidence in the trace points there?"**
- **Scored.** *Product:* did they locate the right frame / line? *Process:* did they read
  the trace as **a window into the execution model** — distinguishing the exception *site*
  from the exception *cause*, reading the call chain top-to-bottom, naming the exception
  class meaningfully — or treat it as opaque noise and guess?
- **Routes via** the C2 rubric. Offered alongside C1 because it is cheap to administer and
  high-impact in AI-era verification work (spec §12). `[Practitioner-canon]`.

---

#### E3 — Code review as a skill

- **Shape.** Show a small diff/PR (~20–40 lines) with **one substantive issue** (a missed
  edge case, an abstraction leak, a naming-vs-behavior mismatch, or a correctness bug) and
  a couple of trivial style nits. Ask the learner to **review it: what would you comment,
  what's the *most important* thing, and how would you phrase the feedback?**
- **Scored.** *Product:* did they **catch the substantive issue** (and not drown it under
  bikeshedding the nits)? *Process:* did they **prioritize** what matters, reason about
  consequences, and phrase feedback precisely and non-egoistically (Weinberg's egoless-
  review culture; `evidence-base.md` → reading spine)? Review is reading + judgment +
  communication, and it is the apex AI-era skill (spec §12), so the rubric weights
  *catching what matters* and *communicating it well* over comment volume.
- **Routes via** the E3 rubric. Judgment-graded. `[Some empirical]` (Bacchelli & Bird
  2013) `+ [Canon]`.

---

#### F1 — Metacognition & calibration

- **Shape — predict-then-check.** Before the learner attempts a small drill (reuse any
  A1/A3-style snippet), ask them to **state their confidence that they'll get it right**
  (e.g., 0–100%, or low/medium/high). Then they attempt; the coach grades it. **Calibration
  is the gap between stated confidence and actual outcome**, measured across several such
  predict-then-check trials.
- **Scored.** *Product:* the calibration delta itself — does high confidence track with
  correctness, or is the learner **systematically overconfident** (high confidence,
  frequent misses — the most common and most consequential failure, and worse among more
  AI-literate users per spec §12) or underconfident? *Process:* can the learner **notice
  confusion early** and say "I'm not sure about X" *before* being shown the answer, rather
  than discovering it only on reveal (`evidence-base.md` → metacognition; illusions of
  fluency)?
- **Routes via** the F1 rubric. Requires ≥3 predict-then-check trials to read a pattern;
  a single trial is noise.
- **Concrete example.** Pose three snippets in a row, each preceded by:

  > **Your turn:** Before you answer — how confident are you that you'll get this exactly
  > right (0–100%)? Then: what does it print?
  >
  > (Take your best guess — wrong attempts are useful data.)

  Across the three, the coach records `(confidence, correct?)` pairs. A learner who says
  "95%" three times and is right once is **badly miscalibrated and overconfident** — that
  is the F1 finding to surface, and it is exactly the gap the curriculum's AI-era priority
  targets (spec §12: METR's "19% slower while feeling 20% faster"). A learner whose
  confidence *ordering* matches their outcomes (less sure on the one they missed) is
  well-calibrated even if not always correct.

---

### 1.5 Reporting the result to the learner

After the battery (or the spine), the coach reports per skill:

- the **recommended starting tier** for each assessed skill, with the one-line evidence
  from the rubric ("you traced the 3-iteration loop cleanly but the recursive call tree
  diverged at the second frame → **Working** on A3");
- the **recommended modules to start with** — defaulting newcomers to the high-evidence
  Track A spine and the AI-era verification cluster (A2/A3, C1, F1, B3, E3; spec §12);
- an explicit reminder that **this is a recommendation, not a gate** — "you can open any
  module at any tier; this is just where I'd start you";
- the framing line: **"This is within-person progress on defined skills, not a certified
  expertise score."**

The coach does **not** report a single composite "overall level." Tiers are per skill by
design (`evidence-base.md` → Finding 7; expertise is not one scalar).

---

## Part 2 — Per-Skill Mastery Rubrics

The **observable performance bar** to pass each named tier, per skill. These are the same
rubrics the entry battery routes against (Part 1) and that the coach uses to mark mastery
mid-curriculum (`coaching-loop.md` Step 7). They describe **what the learner must
demonstrably do**, never what they claim or how long they've coded.

### 2.1 Rubric shape (every module follows this)

Each module's mastery rubric is a short, observable ladder:

| Tier | What the learner can demonstrably do | Evidence required |
|---|---|---|
| **Foundations** | Core mechanics on a single concept, familiar surface. | Passes Foundations-tier drills; can do it *with* a worked example faded to one missing step. |
| **Working** | Applies the skill in a context they haven't seen before. | Passes Working-tier drills **unaided**, including one varied-context transfer. |
| **Advanced** | Transfers, adapts, and **combines** the skill with others; explains *why*, not just *what*. | Passes Advanced drills unaided **and** articulates the underlying principle (teach-it-back). |
| **Frontier** | At or past their demonstrated ceiling. | Tracked as `Frontier-N` per `drill-generation.md` §5 — a moving target, not a fixed bar. |

Two cross-cutting requirements apply at **every** tier above Foundations:

1. **Product *and* process.** Passing means the answer is right *and* the reasoning is
   sound. A correct answer with a wrong/absent explanation is a Foundations-level pass at
   best (it may be luck — `evidence-base.md` → illusions of fluency).
2. **Unaided + durable.** A tier is provisionally passed in-session but **confirmed only by
   delayed re-assessment and real-code transfer** (Part 3, Part 4). A same-session streak
   does not by itself promote a tier.

### 2.2 Concrete rubric example — A1 (notional machine)

The shape above, instantiated:

| Tier | Observable bar for A1 |
|---|---|
| **Foundations** | Correctly predicts the result of a single rebinding/aliasing snippet (`x = [1,2,3]; y = x; x = [4,5,6]; print(y)`) **and** explains it in name-binding terms (assignment binds a name to a value; rebinding `x` doesn't touch `y`). |
| **Working** | Correctly predicts **and explains** aliasing-vs-mutation (`y = x; x.append(4); print(y)` → `y` changes, because both names point to the *same* list object) and short-circuit evaluation, unaided. |
| **Advanced** | Correctly predicts **and explains** a multi-mechanism snippet — e.g., a mutable default argument across two calls, or late-binding closure capture in a loop — naming *when* defaults are evaluated (definition time) and *what* a closure captures (the variable, not its value). |
| **Frontier** | `Frontier-N`: presses one mechanism past the last comfortable success per `drill-generation.md` §5 (e.g., mutable default + aliasing across calls → + closure capture → + a wrapping decorator). |

Each module file (`modules/<ID>-*.md`) supplies its own instantiation of this shape in its
**Mastery rubric** section (spec §5, point 7). This file defines the *shape and the
discipline*; the per-module file supplies the *content* for the other 19 modules.

---

## Part 3 — Held-Out Re-Assessment Protocol (the improvement delta)

This is how the skill earns the word **measurable**. Because drills are *generated fresh*
(`drill-generation.md`), held-out re-assessment is essentially free: the coach re-runs the
entry battery later with **brand-new items the learner has never seen**, at fixed
checkpoints, and compares to baseline.

### 3.1 The mechanism

1. **Baseline is already recorded.** Part 1 wrote each skill's entry result into the
   tracker's **Baseline (date / score)** cell.
2. **Re-run with fresh items at a checkpoint.** At a checkpoint (below), regenerate the
   battery for the skills in question — **same task *shape* and tier definitions, new
   instances** drawn from a different region of the module's parameter space
   (`drill-generation.md` §1b). The learner must not have seen these exact items; that is
   what makes them *held-out*. (Teaching-to-the-test is structurally impossible here — the
   coach cannot drill the answer key because it generates a new one each time.)
3. **Score identically.** Same rubrics (Part 2), same executable-ground-truth / rubric
   grading. Same process-and-product scoring.
4. **The delta is the result.** `baseline → now` on held-out items, **per skill**, is the
   measurable-improvement signal. Record the new score as a dated entry in the tracker
   (the cell accumulates: `2026-06-22: 2/5 → 2026-07-20: 4/5`).

### 3.2 Checkpoints (when to re-assess)

Re-assessment is **delayed by design** (Part 5: learning ≠ performance). Fixed checkpoints,
not on-demand same-session re-tests:

- **Per skill:** when the tracker shows a skill has been marked mastered at a tier **and at
  least ~3 sessions (or a spacing interval) have passed** since that mark — re-assess that
  skill with held-out items before treating the tier as durable. (Aligns with the
  spaced-review trigger, `coaching-loop.md` Step 8.)
- **Battery-level:** re-run the **spine** (A1, A2, A3, C1, F1) at a standing cadence — e.g.,
  every ~4–6 weeks of active practice — to produce a periodic baseline-vs-now snapshot
  across the verified core.
- **On request:** the learner may always ask "am I actually getting better at X?" — the
  honest answer is a held-out re-assessment of X, not the coach's impression.

### 3.3 Reporting the delta honestly

- Report the **per-skill delta with its dates**, and state the item count plainly
  (`drill-generation.md` grading is per-item; small batteries are noisy — see Part 6).
- A held-out gain is the **strongest** evidence the skill produces. A flat or negative
  delta is **information, not failure** — it may mean the skill needs different practice,
  the checkpoint was too soon, or the baseline was already high. The coach does not spin a
  flat delta as success, and does not over-read a small gain (Part 6 guardrails apply to
  performance deltas too).

---

## Part 4 — Per-Module Transfer Tasks (real-code transfer)

Held-out re-assessment (Part 3) measures transfer to *fresh generated* items. The **only
honest test of whether a gym drill transferred to the job** is applying the skill to the
learner's **own real code** (`evidence-base.md` → transfer caveat, consequence 2; spec §5
point 9).

- **Every module ends on a transfer task** defined in that module's **Transfer task**
  section (`modules/<ID>-*.md`): the learner runs the skill against a slice of their actual
  codebase — trace a function they wrote (A3), review a real open PR (E3), decompose a
  feature they're about to build (B1), debug a real failing test from their repo (C1),
  state confidence before reading an unfamiliar module of their own system then check it
  (F1).
- **Grading is softer and named as such.** Real code has no clean answer key; the coach
  grades against the module rubric and says "this is a judgment call on your real code, not
  a machine-verifiable result." Where the learner's code *is* runnable, the coach still
  uses the runner for any executable sub-claim.
- **Transfer evidence is weighted heavily.** A learner who passes generated drills but
  cannot apply the skill to their own code **has not transferred it** — the tracker notes
  this gap, and the coach treats it as more diagnostic than another passed synthetic drill.

---

## Part 5 — Learning ≠ Performance (the weighting rule)

> Immediate, same-session performance is a **poor index of durable learning**
> (Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: an integrative
> review. *Perspectives on Psychological Science*, 10(2), 176–199;
> `evidence-base.md` → instructional pillar).

This governs how *all* of the above is weighted:

- **A hot streak is provisional.** A learner passing five drills in a row in one session has
  demonstrated *current performance*, not necessarily *learning*. Do **not** promote a tier
  or mark mastery on a same-session streak alone.
- **Weight delayed re-assessment and real-code transfer over same-session pass rate.** The
  evidentiary hierarchy, strongest first:
  1. **Held-out re-assessment after a delay** (Part 3) — fresh items, time elapsed.
  2. **Real-code transfer** (Part 4) — the skill working on the learner's own code.
  3. **Unaided same-session drills** — current performance; necessary but not sufficient.
  4. **Aided / scaffolded drills** — weakest; shows the skill is reachable, not owned.
- **Desirable difficulty cuts the same way.** Conditions that *slow* same-session
  performance (interleaving, spacing, varied context) often *improve* durable learning
  (`evidence-base.md` → desirable difficulties). So a *dip* in same-session pass rate under
  interleaving is **not** evidence of regression — and a *smooth* same-session streak under
  massed, un-spaced practice is **not** strong evidence of durable learning.
- **The tracker reflects this.** Tier marks carry their evidence basis; a tier confirmed
  only by same-session streak is flagged provisional until a delayed checkpoint (Part 3) or
  a transfer task (Part 4) confirms it.

---

## Part 6 — Optional Affective Self-Report Layer

A **complement** to the performance measures above — a lightweight, optional pre/post
check-in on how the learner *experiences* their practice. It is grounded in validated,
open-access measures from large-scale developer research.

> **OPTIONAL, and NEVER for routing or gating.** This layer does **not** feed tier
> recommendations, mastery marks, or module routing. Those are decided **only** by
> performance (Parts 1–5). The affective layer exists to make the *experience* of learning
> legible — confidence, anxiety about AI, perceived learning culture — as a discussion
> prompt, not a score. A learner may skip it entirely with no effect on anything.

### 6.1 Attribution (CC-BY-SA-4.0)

> **These measures are reproduced verbatim under a CC-BY-SA-4.0 license** and carry a
> share-alike obligation: any adaptation must be credited and licensed alike.
>
> - **AI Skill Threat (PAST) measures and the AI Skill Threat model** —
>   Hicks, C. M., Lee, C. S., & Foster-Marks, K. (2025, March 15). *The New Developer:
>   AI Skill Threat, Identity Change & Developer Thriving in the Transition to AI-Assisted
>   Software Development.* https://doi.org/10.31234/osf.io/2gej5_v2
> - **Developer Thriving (DTS) measures — incl. Learning Culture (DTS-LC) — and the
>   Developer Thriving model** —
>   Hicks, C. M., Lee, C. S., & Ramsey, M. (2024). *Developer Thriving: four sociocognitive
>   factors that create resilient productivity on software teams.* IEEE Software, 41(4),
>   68–77. doi:10.1109/MS.2024.3382957
> - **Coding Self-Efficacy (CSE)** appears in the AI Skill Threat study above.
>
> These items, scales, and the reporting guardrails in §6.4 are adapted from **Cat Hicks'
> *Learning Opportunities* "Measure This" playbook** (CC-BY-SA-4.0). Credit **Cat Hicks**
> for the playbook and measures; **Carol Lee** and **Kristen Foster-Marks** as co-authors
> of the empirical research. If these items are adapted or reshared, keep this attribution
> block and the CC-BY-SA-4.0 license.

Developed from studies of 3,267 and 1,282 professional software developers across 12+
industries; validated in an adult (18+) population, developed in English. Use the items
**verbatim** and keep the response scales exactly as written — do not reword between pre
and post.

### 6.2 The items (verbatim)

**Learning Culture** (DTS-LC)
*Scale: 1 = Strongly Disagree, 2 = Somewhat Disagree, 3 = Neither Agree nor Disagree,
4 = Somewhat Agree, 5 = Strongly Agree*

1. Overall at work, I feel like I am learning new skills and growing as a software engineer.
2. On my team, we often share new things we have learned with each other.

**AI Skill Threat** (PAST; Perceived AI Skill Threat in Software Engineering)
*Scale: 1 = Strongly Disagree, 2 = Somewhat Disagree, 3 = Neither Agree nor Disagree,
4 = Somewhat Agree, 5 = Strongly Agree*

3. When I think about how generative AI will change software development, I feel anxious or uneasy.
4. Because of generative AI tools or AI capabilities, I worry that many of the skills I currently use as a software engineer will become obsolete very quickly.

**Coding Self-Efficacy** (CSE)
*Scale: 1 = Strongly Disagree to 5 = Strongly Agree*

5. Even when I have frustrating or unexpected problems while working with code, I know I will be able to solve them.

> These five core items take about two minutes. The "Measure This" playbook offers further
> optional add-on constructs (AI Behavioral Action, Sense of Belonging, Developer Agency,
> Team Effectiveness); those tap larger psychological affordances, are harder to move on a
> short timescale, and can feel more sensitive — include them only with an anonymized
> administration and over a longer horizon (≥1 month, repeated timepoints). Use them
> verbatim from the source if added.

### 6.3 Timing (pre / post)

- **Pre:** before the learner begins a defined stretch of practice (e.g., the start of a
  multi-session block).
- **Post:** after that stretch (a week is a reasonable lightweight window; the deeper
  add-on constructs want a month+).
- **Use the exact same items and scales both times.** Do not reword. If administered for a
  team, keep it anonymous and do not discuss "expected" results beforehand (otherwise you
  measure social desirability, not the construct).

These are a **momentary sample of how the learner perceives their environment and
themselves**, grounded in psychology about *beliefs and cultures that can change* — not
fixed traits, and not an individual diagnostic.

### 6.4 Reporting guardrails (mandatory whenever the coach summarizes this layer)

The coach must follow these when reporting affective results — they are the playbook's
guardrails, and they bind the same honesty stance as the rest of the skill:

- **Descriptive over inferential.** Report direction of change, the actual numbers, and the
  spread. Do **not** run significance tests on tiny samples (a t-test on n=6 is
  uninterpretable; a non-significant result does **not** mean "nothing happened," and a
  significant one would be unreliable). For an individual learner this is n=1 across time —
  describe the trajectory, never test it.
- **Report variance / spread alongside any average.** Always pair a mean with its range or
  spread. "AI Skill Threat moved 3.5 → 3.2" reads completely differently if everyone
  shifted slightly versus one person dropping 5→1 while others held. Spread is itself a
  finding, not noise to smooth away.
- **No causal overclaiming.** A pre/post with **no control group cannot attribute** change
  to the practice. Never say "the skill reduced AI Skill Threat by 18%." A pre/post can
  *describe* change; it cannot *isolate its cause* — the learner had a whole life around
  the practice (a stressful project ended, the team gelled, the tools themselves changed).
- **Never confabulate norms.** Do **not** tell the learner "a 3.2 means moderate anxiety"
  or "that's within the normal range." The coach does not have the study's distribution,
  and norm interpretation needs measurement context beyond a single number. If the learner
  asks what a score "means," say plainly that the number is a self-report on a 1–5 scale at
  one moment, not a calibrated benchmark.
- **Small-n deltas start conversations, not verdicts.** Use the numbers to prompt reflection
  ("self-efficacy rose — does that match how it felt? what drove it?"), never to render a
  verdict ("the intervention worked"). Absence of measurable change is **not** evidence of
  absence of impact — a short window with one learner is a pilot, and qualitative signal can
  matter as much as the numbers.
- **Keep it separate from performance.** Affective scores and performance tiers are reported
  in *different* parts of any summary, and the coach states that the affective layer
  **does not** influence routing, tiering, or mastery. They answer different questions:
  performance asks *can you do it?*; this layer asks *how does the practice feel?*

---

## Cross-references

- Routing runs from `coaching-loop.md` Step 1 (Locate) for new learners; the pause /
  no-spoiler hard stop after each task is `coaching-loop.md` → Delivery Disciplines.
- Entry/re-assessment tasks are drills graded by `drill-generation.md` — executable ground
  truth (§2), rubric + exemplars (§3), generation self-check (§4), Frontier escalation (§5),
  format catalog (§6, incl. Trace-the-path, Debug-this, predict-then-check).
- The baseline/delta/recurring-errors cells live in `progress-template.md`.
- Evidence for *performance, not tenure* (Finding 7), *learning ≠ performance*
  (Soderstrom & Bjork 2015), illusions of fluency, and the transfer caveat:
  `evidence-base.md`.
- Per-module mastery rubrics (Part 2 shape, instantiated) and transfer tasks (Part 4) live
  in each `modules/<ID>-*.md` (spec §5, points 7 and 9).
