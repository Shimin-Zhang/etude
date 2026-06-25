# F2 — Designing Your Own Practice `[Verified-adjacent]`

> **Module type.** The **meta-capstone** — a **judgment module** that turns the
> curriculum's own design principles back on the learner. Its job is to make the learner
> able to **design and critique their own practice**: not "how do I solve this problem?"
> but "how do I *practice* so that I actually get better?" There is **no executable ground
> truth for "is this practice well-designed?"** — that is a judgment, graded against a
> **rubric + golden exemplars**, surfaced as soft.
>
> **Honest prose badge.** `[Verified-adjacent]` — the design principles are **verified
> *general* learning science** (`[Verified]` *as general cognitive psychology*: the
> testing/generation effect, spacing, desirable difficulties, worked examples + expertise
> reversal, learning ≠ performance, metacognition — among the most replicated findings in
> the field), but their **programming-specific** transfer is thin, so the module badge is
> `[Verified-adjacent]`, **not** `[Verified]` — matching F1 and the evidence base's own
> `[Verified-adjacent]` badging of the instructional pillar this module rests on. Two honesty
> fences keep it from overclaiming: (1) the **deliberate-practice-dominance / "10,000-hour"
> folklore is explicitly REJECTED** (it is refuted, and disputed on top of that); and (2)
> the **programming-specific causal transfer is the open question** the whole curriculum
> carries.
>
> **Core idea.** Well-designed practice is **QUALITY + immediate FEEDBACK + individualized
> TARGETING + desirable DIFFICULTY + SPACING** — *not hours logged*. Hours are an input;
> learning is the outcome, and the conditions that produce durable learning often feel
> *harder and slower* than the comfortable ones that feel productive. The skill is to
> **design practice for the learning, not the clock.**

---

## 1. Evidence basis `[Verified-adjacent]`

This module is unusual: its subject *is* the evidence base. It teaches the learner to apply
the curriculum's instructional science to their own practice. So §1 has three parts — what
is **verified** (and licenses the module), what is **REJECTED** (and the module exists in
part to debunk), and the **caveat** that keeps even the verified half honest.

### (a) The verified half — the learning-science instructional pillar

The five design levers this module teaches are each grounded in the **learning-science
instructional pillar** already in `evidence-base.md` (→ *Learning-science instructional
pillar*). **Cite the pillar; this module does not re-derive it.** These effects are
**`[Verified]` as general cognitive/educational psychology** — the testing effect and the
spacing effect in particular are among the most replicated results in the whole field:

| Design lever (what F2 teaches) | Verified finding it rests on (instructional pillar) |
|---|---|
| **QUALITY — generate, don't re-consume** | **Generation & testing effect** (Roediger & Karpicke 2006) and **pre-testing** (Giebl et al. 2021, shown with people learning *programming* concepts): producing/retrieving beats passively re-reading, and the benefit shows up on *delayed* tests even when immediate performance is worse. |
| **FEEDBACK — check against external ground truth** | The pillar's **dynamic-testing** stance (`coaching-loop.md` Step 6) and the curriculum's **surface-ground-truth** rule (`drill-generation.md` §2): errors followed by clear correction enhance retention; the cure for the fluency illusion is an external check. |
| **TARGETING — aim at *your* current edge** | **Worked examples + expertise reversal** (Sweller & Cooper 1985; Kalyuga 2007): the right level of support is *individual* and *changes with skill* — full support helps a novice and becomes redundant load for an expert. Knowing your edge is **metacognition** (Dunlosky et al. 2013), the F1 skill. |
| **DESIRABLE DIFFICULTY — choose productive struggle** | **Desirable difficulties** (Bjork; Bjork, Dunlosky & Kornell 2013) and **learning ≠ performance** (Soderstrom & Bjork 2015): conditions that *slow* short-term performance often *improve* long-term retention and transfer, so felt ease is a poor — often *inverted* — signal of learning. |
| **SPACING — distribute and interleave** | **Spacing** (Kornell 2009; Kang 2016): distributed practice beats massing for retention, even though massing *feels* more efficient and is *judged* more effective by learners. |

The narrow, well-supported claim these jointly license — and all this module teaches as
verified *general science* — is: **practice is a design problem, and these five conditions reliably produce
more durable learning per unit time than their comfortable opposites (re-reading,
self-grading, grinding the easy, cramming).** This is exactly the science the *rest of the
curriculum* is built on; F2 just makes the learner the designer.

### (b) The REJECTED half — the deliberate-practice-dominance / "10,000-hour" folklore

The defining honesty move of this module. The popular thesis — that **~10,000 hours of
deliberate practice is the dominant cause of expert performance** — is **REJECTED folklore**
(`evidence-base.md` → *Folklore we explicitly reject* → "The strong 10,000-hour / 10-year
rule"). It is on the **refuted/folklore list, and it bites here**: F2 must teach the
good-practice principles **while explicitly rejecting hour-counting**.

What the meta-analytic evidence actually shows:

- Deliberate practice explained **~12% of the variance in performance overall** (pooled
  across domains) — and only **~1% in professions**, ~4% in education, ~18% in sports, ~21%
  in music, ~26% in games (Macnamara, Hambrick & Oswald 2014). **Most of the variance is
  *other* factors.** The effect **loses most of its power at elite levels**, and
  retrospective recall of practice hours tends to **inflate** the estimate (Hambrick et al.
  2014).
- **Time-to-mastery varies enormously between people**: in chess, the slower player needed
  **~8× as much practice** as the faster one to reach master level (Gobet & Campitelli
  2007). A single hour target cannot be "the answer."
- **The numbers above come from music, sports, chess, and games — NOT software.** There is
  no "10,000 hours to senior engineer" finding; the figure was never measured in
  programming.
- **And it is a *live* scientific dispute**: K. Anders Ericsson and colleagues contested
  the magnitude and the definition used in these meta-analyses. So the honest conclusion is
  carefully hedged, not triumphant.

**How the coach states it** (verbatim discipline from the evidence base): *"the strong
10,000-hour claim is not supported; practice matters but is far from the whole story; the
precise numbers aren't from programming; and the magnitude is itself disputed."* Ericsson &
Pool's **_Peak_** is on the curriculum's reading spine **to be read critically** — use it
for the **quality-of-practice** ideas (which overlap the verified pillar above), **not** for
the hour-dosing thesis the meta-analyses dispute (`evidence-base.md` → reading spine).

### (c) The caveat that keeps the verified half honest

Two honesty bounds, both taught out loud (see §8):

1. **General vs. programming-specific (the curriculum-wide transfer caveat).** The five
   levers are verified *general* learning science — established mostly on **general-knowledge
   questions, classroom learning, and lab tasks, not professional code**
   (`evidence-base.md` → transfer caveat). That redesigning your *programming* practice this
   way *causally* makes you a better engineer is the **same open question** the entire
   curriculum carries. The module teaches the principles and the **measurement stance**; the
   proof for an individual is their **own held-out deltas over time** (§9; `assessment.md`
   Part 3), not a citation.
2. **No "correct" regimen — F2 is not a plan catalog.** Just as B1 teaches decomposition but
   **not** a memorizable "plan catalog" (refuted — Gilmore & Green 1988), and D2 teaches
   precise naming but concedes there is **no single correct name** (Feitelson 2022), F2
   teaches the **principles that constrain** good practice — it does **not** prescribe one
   schedule. The levers tell you what a good design must *do*; the specific regimen is
   **individual** to the learner's edge, goal, and life. Copying an influencer's "12 hours a
   day" routine is itself an anti-pattern (it ignores targeting).

**Why these license this module.** The principles are verified; the hour-thesis is refuted;
the programming-specific causal promise is honestly withheld. That is exactly the posture a
*reflexive* module must take: F2 is subject to its own standard of evidence, and it says so.

---

## 2. Soft prerequisites

**Light, and never a gate. F2 is the meta-capstone — the *whole curriculum* informs it**,
because the practice the learner is learning to design *is* practice on the other nineteen
skills.

- **F1 (metacognition & calibration) is the closest tie.** You cannot **target** practice at
  your edge if you cannot tell where your edge *is* — and calibration is the F1 skill
  ("knowing what to practice next"). An overconfident learner targets the wrong things
  (grinds what they already do, skips what they're shaky on) and cannot read whether a
  practice change worked. F1 is the instrument F2's *targeting* and *measurement* levers run
  on.
- **The executable spine (A1/A3/C1/B2 …) supplies the *feedback* lever.** A core mark of
  well-designed *programming* practice is that, where possible, it has an **external ground
  truth** (the runner) instead of self-grading — which is exactly the predict-then-check
  discipline those modules drill. F2 designs practice that *uses* that ground truth.
- **The judgment modules (E3, D1–D4, B1) are where F2's "no single correct answer" stance
  comes from** — and where practice must get its feedback from rubrics, exemplars, and peer
  review rather than a runner.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). A learner can profitably design their practice
before mastering every skill they'll practice; indeed, doing F2 *early* improves how they
run all the others. If a learner flails at F2 because they can't tell their edge, the coach
notes the gap likely traces to F1 and *suggests* shoring it up — but does not forbid F2.

---

## 3. The mental model

**Practice is a design problem with five levers. The goal is to maximize *durable learning
per unit time*, not to maximize the time.** A running tally of hours measures the **input**;
it tells you nothing about the **output**. Worse, the practice that *feels* most productive
— smooth re-reading, cramming one topic, redoing what you can already do — is systematically
*among the worst* for durable learning, because **felt ease is a poor and often inverted
signal** (Soderstrom & Bjork 2015). Designing practice well means deliberately choosing the
conditions that feel harder now and pay off later.

The five levers, each defined by **what well-designed practice does** and **the anti-pattern
it replaces**:

| Lever | What well-designed practice does | The comfortable anti-pattern it replaces |
|---|---|---|
| **QUALITY (generate)** | **Produce or retrieve before you look** — predict the output, write from a blank page, explain it back — so the act of practice is *generative*, not receptive. | **Re-reading** solved solutions / editorials / tutorials until they feel familiar. Feels productive; builds a *fluency illusion*, not skill. |
| **FEEDBACK (ground truth)** | **Check against an external truth immediately** — run it, test the edge case, diff against the rubric — so an error gets corrected while it's fresh. | **Self-grading** ("yeah, I get it"). Confidence with no check just re-confirms the illusion. |
| **TARGETING (individualized)** | **Aim at *your* current failure boundary** — the class of problem you actually get wrong — and fade the support as you improve (expertise reversal). | **Grinding the comfortable** — redoing the easy/solved because it *feels good to get through*. Near-useless: no edge, no difficulty. |
| **DESIRABLE DIFFICULTY** | **Choose productive struggle** — unseen problems, blank pages, interleaving — accepting that it feels slower because that struggle is what builds durable, transferable skill. | **Staying comfortable** and reading felt-ease as learning. The desirable-difficulty inversion. |
| **SPACING (distribute + interleave)** | **Spread practice over time and mix problem types**, returning to old material on a schedule. | **Massing / cramming** — one topic in a marathon block, or a week before a deadline then nothing. Feels efficient; poor for retention. |

**The discipline in one line: *design practice for the learning, not the clock — quality,
feedback, targeting, difficulty, and spacing, measured by what you can do, not by hours
logged.*** Three corollaries the module drills:

1. **Felt ease is an anti-signal.** The conditions that make a session feel smooth and
   productive (massed, fluent, re-reading the solved) are the ones that produce the *least*
   durable learning; the conditions that feel effortful and halting (spaced, interleaved,
   blank-page, unseen) produce the *most* (Soderstrom & Bjork 2015; Bjork desirable
   difficulties). So **"that session flowed, I learned a lot" is evidence you should
   distrust.** Conversely, struggling is not failing — it's often the practice working.
2. **Hours are an input, not a result.** "I practiced two hours" / "I'm on a 40-day streak"
   / "I'm aiming for 10,000 hours" all measure **dose**, not **learning**. The 10,000-hour
   framing is **refuted folklore** (Macnamara 2014 — DP ≈ 12% of variance, and not from
   software; §1b). Measure **within-person deltas on held-out tasks** — "can I now solve a
   *cold, unseen* problem of a kind I used to fail?" — the curriculum's own measurement
   stance (`assessment.md` Part 3), never the clock.
3. **You can't target what you can't see — practice needs calibration (F1).** Aiming at your
   edge presupposes you know where it is. Overconfidence sends you to grind what you already
   do; underconfidence wastes effort re-verifying the solid. So good practice design has a
   **calibration loop** built in: predict your performance, check it, and let the miss
   retarget the next session.

---

## 4. Worked example — critique and redesign a practice routine

*(Foundations depth: the full lever-by-lever critique **and** the redesign shown, with the
one executable sub-claim run. This fades by tier — see the table after.)*

The skill is to **read a described routine, diagnose it against the five levers, prioritize
the highest-leverage fix, and redesign it** — the same shape as the entry task
(`assessment.md` → F2). Consider this routine (every sentence carries an anti-pattern):

> *"I want to get better at Python before my interview. My routine: every evening I spend
> **2 hours**. I open my notebook of **solved** problems and **re-read** my solutions and the
> editorial, one after another — maybe 15 a night. I stick to the **easy ones I've already
> solved** because it feels good to get through them. I do this **every night for the week
> before the interview, then stop**. I track progress by **the number of hours I've put in** —
> I'm aiming for the **10,000 hours** everyone talks about."*

**Step 1 — Diagnose, lever by lever** (name the anti-pattern *and* the principle it
violates):

| Lever | What the routine does | Verdict |
|---|---|---|
| **QUALITY** | Re-reads solved solutions + editorials. | ❌ **Passive consumption, zero generation.** Re-reading produces a *fluency illusion* — it *feels* learned because the text reads smoothly, but nothing was retrieved or produced (Roediger & Karpicke 2006; Koriat & Bjork 2005). |
| **FEEDBACK** | Reads the editorial and nods. | ❌ **Self-grading, no external truth.** "I get it" is not a check. The cheapest real feedback — *run it, test an edge case* — is skipped entirely. |
| **TARGETING** | Grinds the easy, already-solved problems "because it feels good." | ❌ **No targeting at the edge.** Redoing the solved is comfort, not practice. The *feeling-good* is the tell. |
| **DESIRABLE DIFFICULTY** | Maximally comfortable: known, easy, solved, re-read. | ❌ **The desirable-difficulty inversion.** All ease, no struggle ⇒ minimal durable learning (Soderstrom & Bjork 2015). |
| **SPACING** | Every night for one week, then stop. | ❌ **Massed cram, then zero.** Distributed practice beats cramming (Kornell 2009; Kang 2016); a one-week block before a deadline is the textbook *worst* schedule for retention. |
| **(Meta) MEASUREMENT** | Tracks hours; aims at 10,000. | ❌ **Hour-dosing folklore.** Hours are an input; "10,000" is refuted (Macnamara 2014 — DP ≈ 12% of variance, ~1% in professions, and *not from software*). Measures dose, not learning. |

**Step 2 — Prioritize.** Every lever is broken, but the highest-leverage single change is to
**make the practice generative with external feedback** (QUALITY + FEEDBACK together): stop
re-reading solved code; instead *predict-then-check on unseen problems*. That one change
converts the most worthless activity (re-reading) into the most valuable (retrieval +
ground-truth correction), and it's the change that most exposes the targeting and difficulty
gaps underneath.

**Step 3 — Redesign** (flip every lever; this is the gold):

> - **QUALITY:** Don't re-read solutions. **Cover the solution, attempt the problem from a
>   blank page**, or at minimum **predict the output before running**. Generate, then look.
> - **FEEDBACK:** **Run every attempt against a small battery including edge cases** (empty,
>   single, duplicate, boundary). The failing case *is* the feedback — far more than "the
>   editorial looks right."
> - **TARGETING:** Stop grinding the solved easy ones. **Practice the class you actually
>   fail** (use F1: predict your success rate per topic, check it, and aim where confidence
>   and correctness diverge).
> - **DESIRABLE DIFFICULTY:** Prefer **unseen, slightly-too-hard** problems and blank pages.
>   Expect it to feel worse than re-reading — that discomfort is the signal it's working.
> - **SPACING:** **Distribute over weeks, not one cram week**; **interleave** problem types
>   in a session; **revisit** older problems on a spaced schedule (a few days, then a week).
> - **MEASUREMENT:** Replace the hour counter with a **held-out check** — a small set of
>   *cold, unseen* problems you attempt before and after, scored by whether they pass a test
>   battery. That delta, not hours, is "getting better" (`assessment.md` Part 3).

**The one executable sub-claim — what "generative + ground truth" actually buys.** Take one
"solved problem" the learner would otherwise *re-read*:

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []

print(two_sum([3, 2, 4], 6))
```

**Re-reading it** yields "yep, hash map, I get it" — a self-graded fluency illusion. The
**redesigned** practice instead has the learner *cover the body, predict the output, then
run it* — and then **escalate to edge cases the re-reading never surfaces** (duplicate
values, no solution, empty input). The coach obtains the ground truth by **running it**
(`drill-generation.md` §2 — never guessed):

```
two_sum([3, 2, 4], 6)   -> [1, 2]     # the happy path the learner predicted
two_sum([3, 3], 6)      -> [0, 1]     # duplicate values — does the dict clobber? (no: it returns before overwriting)
two_sum([1, 2], 100)    -> []         # no solution — handled
two_sum([], 5)          -> []         # empty input — handled
status: ok
```

The point is **about the practice design, not the algorithm**: re-reading produces a feeling
about `two_sum`; the redesigned drill produces *checked predictions against real output*,
including the duplicate-values case (`[0, 1]`) that "I get it" would never have tested. The
redesign now *has the external feedback the original lacked* — and that, not the hours, is
what makes it good practice.

**What the critique makes visible** (and an "is this enough hours?" question hides): the
routine wasn't *too short* — it was **wrong on every lever**. Adding hours to it would
multiply the worthless re-reading. The fix isn't *more*; it's a **different design**. That is
the whole module in one example.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> critique helps **novices** (it shows the lever-by-lever move) but is **redundant load for
> the more advanced**, who learn more by diagnosing themselves. So the coach fades it:
>
> | Tier | Worked-example depth at F2 |
> |---|---|
> | **Foundations** | **Full** — the complete lever-by-lever critique *and* the redesign above, every step shown. |
> | **Working** | **Partial** — coach names the anti-patterns present but leaves the **redesign** (and *which* lever each fix serves) for the learner to produce. |
> | **Advanced** | **Skeleton** — coach hands over the routine and the five levers only; the learner diagnoses, prioritizes, redesigns, and justifies unaided. |
> | **Frontier** | **None** — straight to the problem (§6: a subtle routine, or design-from-scratch). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for F2. Grading mode is
declared up front: **rubric + golden exemplars** (§5d) — this is a **judgment** module, **not**
an executable one. "Is this practice well-designed?" is a judgment with **no single correct
answer**; the coach says so out loud. (The *one* executable sub-claim — running a snippet a
redesigned drill would predict-then-check — is graded by the runner; the *design verdict* is
not.)

### 5a. Tier definitions (F2-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Every
drill is a described practice routine to critique, or a practice plan to design** (an
*Error-analysis* / *Generation→Comparison* format, `drill-generation.md` §6):

| Tier | F2 criterion | Example shape |
|---|---|---|
| **Foundations** | A routine with **one clear anti-pattern** on a familiar surface. **Name the anti-pattern, the principle it violates, and the one fix.** No decoys. | "I learn by re-reading my old solutions until they feel familiar." → name passive/no-generation; fix = predict-then-check. |
| **Working** | A routine with a **mix** (2–4 anti-patterns, possibly one *already-good* element that must **not** be "fixed"). **Critique against all five levers, prioritize the highest-leverage fix, redesign** — and catch the **hours/comfort framing**. | The full 2-hours-re-reading-cram-10,000-hours routine; or a "marathon-read the docs" routine with one good targeting choice baked in. |
| **Advanced** | A **subtle** case: a routine that **looks rigorous** but has a hidden flaw (generation + difficulty but **no spacing**; or hard problems but **no feedback**; or confuses same-session performance with durable learning) — **diagnose the hidden flaw, redesign, and explain *why*** — **OR** **design a practice plan from scratch** for a stated goal and defend it. | "I do 20 hard unseen problems a day but 'it ran' counts as done, and I never revisit." → generation without feedback or spacing. Or: "design 3 weeks of debugging practice, 45 min/day." |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations routine hides its flaw among decoys, or a Working
routine has no genuinely-good element to *de*-prioritize, or an Advanced routine's flaw is
obvious on a skim. Apply the self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for F2:

- **Lever stressed** — QUALITY/generation · FEEDBACK/ground-truth · TARGETING/individualization
  · DESIRABLE-DIFFICULTY · SPACING/interleaving · the **meta** lever (hours-dosing /
  performance-vs-learning / no-single-correct-plan).
- **Anti-pattern present** — re-reading-passive · self-grading-no-truth · grinding-the-
  comfortable · massing/cramming · hour-dosing/streak-chasing · felt-ease-as-signal ·
  generation-without-feedback · performance-mistaken-for-learning · copying-one-regimen ·
  **AI-trust-by-plausibility-as-practice**.
- **Routine shape** — a described daily routine · a weekly/pre-deadline plan · "how I learn a
  new library/framework" · an **AI-assisted** workflow (accept-what-looks-right) · a
  *design-from-scratch* brief for a stated goal · a critique of *someone else's* posted plan.
- **Decoy mix** (the judgment axis) — none (Foundations) · a genuinely-**good** element that
  must **not** be flagged (e.g., spaced review mistaken for "inefficient"; blank-page
  generation that is *correct*) · a **plausible-but-wrong fix** to reject ("just add more
  hours") · the **hours/streak framing** buried in an otherwise-okay plan.
- **What the critique must produce** — *name + fix* (Foundations) · *critique-all-levers +
  prioritize + redesign* (Working) · *diagnose the hidden flaw + redesign + teach the
  principle*, **or** *design-from-scratch + defend + define a held-out measure* (Advanced).
- **Format** (`drill-generation.md` §6) — primarily **Error-analysis** (critique a described
  routine) and **Generation → Comparison** (redesign, then compare to the gold); also
  **Teach-it-back** (articulate *why* felt-ease is an anti-signal, or why hours ≠ learning),
  and **Debug-this** ("here is a practice plan — what breaks, and what's the highest-leverage
  fix?").

Keep an in-session log of the `(lever, anti-pattern, routine shape, decoy mix, format)`
tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* failures a learner makes when critiquing or designing practice, each with the
conceptual gap it diagnoses (`drill-generation.md` §1c format). Grounded in the instructional
pillar and the folklore section of `evidence-base.md`, not in trivia. **The root of almost
all of them is one misconception: "practice = time-on-task, and what *feels* productive *is*
productive." The corrective model: practice is a *design* problem; the learning-effective
conditions usually feel harder and slower, and learning is measured by *durable transfer*,
not by hours or by the fluency of the moment.**

```
Error: Counts hours / chases a streak / aims at a total ("I just need to hit 10,000 hours").
       Treats more time as the goal and as the measure of progress.
Diagnoses: Hour-dosing / deliberate-practice-dominance folklore. Conflates the INPUT (time)
           with the OUTCOME (learning). The strong 10,000-hour thesis is REFUTED — DP explains
           ~12% of variance overall, ~1% in professions, and the numbers are from
           music/sports/chess, not software. (Macnamara et al. 2014; evidence-base Folklore.)
Example trigger: any routine whose stated progress metric is hours or a day-streak.

Error: Re-reads solved solutions / editorials, re-watches tutorials, highlights the docs —
       and calls it studying because it feels productive.
Diagnoses: Passive consumption, no generation. The generation/testing effect: producing or
           retrieving beats re-reading, whose smoothness is a FLUENCY ILLUSION (feels learned,
           isn't). (Roediger & Karpicke 2006; Koriat & Bjork 2005.)
Example trigger: "I re-read my old solutions until they feel familiar."

Error: Self-grades ("yeah, I get it") with no external check; never runs the code, never
       tests an edge case, never diffs against a rubric.
Diagnoses: No feedback against ground truth. Confidence without a check just re-confirms the
           illusion; the cure is an EXTERNAL truth (run it / test the edge / rubric).
           (Curriculum surface-ground-truth rule; F1 calibration.)
Example trigger: a routine that reads the editorial and moves on, or "if it runs, it's done."

Error: Grinds problems/topics already mastered because it feels good and keeps a streak alive.
Diagnoses: No targeting at the edge + comfort-seeking. Redoing the solved is near-useless;
           practice must aim at the current FAILURE boundary, which requires calibration to
           locate. (Expertise reversal — Kalyuga 2007; targeting needs F1.)
Example trigger: "I stick to the easy ones I've already solved" / "only my strongest topic."

Error: Reads felt-ease/smoothness as evidence the practice worked ("that session flowed, I
       learned a ton").
Diagnoses: Learning != performance + the desirable-difficulty inversion. The conditions that
           feel best (massed, fluent, re-reading) are often WORST for durable learning; felt
           ease is an anti-signal, struggle is often the work. (Soderstrom & Bjork 2015; Bjork.)
Example trigger: a learner who defends a re-reading routine with "but it feels really
                 productive."

Error: Masses practice — crams one topic in a marathon block, or one week before a deadline
       then stops; never spaces or interleaves.
Diagnoses: Massing over spacing. Distributed + interleaved practice beats cramming for
           retention even though cramming FEELS more efficient. (Kornell 2009; Kang 2016.)
Example trigger: "I do all of recursion in one 6-hour Sunday, then never come back."

Error: Does lots of hard, generative work but never checks answers / never revisits —
       generation and difficulty present, but the loop is open.
Diagnoses: A PARTIAL design. The five levers are a system; difficulty + generation WITHOUT
           feedback is just unguided struggle, and without spacing it doesn't consolidate.
           Missing one lever breaks the design even when the others are right.
Example trigger: "20 blank-page hard problems a day; if it runs I count it done; I never redo
                 old ones."

Error: Mistakes same-session improvement for durable learning; promotes themselves off a hot
       streak ("nailed five in a row, I've got this").
Diagnoses: Performance-for-learning. Same-session gains are a poor index of durable learning;
           weight DELAYED held-out re-assessment and real-code transfer over a streak.
           (Soderstrom & Bjork 2015; assessment Part 5.)
Example trigger: a plan that ends practice on a topic the moment a same-session streak appears.

Error: Copies someone else's exact regimen wholesale (the influencer's "12 hours a day"),
       or insists there is one correct practice schedule.
Diagnoses: There is NO single correct plan (parallel to B1's no-plan-catalog, D2's
           no-single-correct-name). The principles constrain; the regimen must be
           individualized to THIS learner's edge, goal, and life. Copying ignores targeting.
           (Gilmore & Green 1988 analogue; transfer caveat.)
Example trigger: "I'm following X's exact routine because it made them a 10x engineer."

Error: "Fixes" an element that was actually GOOD — flags spaced review as "inefficient,"
       interleaving as "distracting," or blank-page struggle as "wasting time."
Diagnoses: Over-correction / the desirable-difficulty inversion in reverse. The slower-FEELING
           element (spacing, interleaving, struggle) is the FEATURE, not a bug; flagging it is
           the same mistake as trusting felt-ease. Don't manufacture a fix. (Parallels E3
           over-reporting; Bjork desirable difficulties.)
Example trigger: a Working routine containing one good lever (spaced review) the learner
                 "corrects" into massing.

Error: (AI-era) Practices by accepting AI output that "looks right" — no prediction, no
       verification — and counts the volume as practice ("did 30 problems with the AI").
Diagnoses: Trust-by-plausibility as practice. Reading fluent AI code/explanations is the
           re-reading anti-pattern in AI clothing: no generation, no feedback, pure fluency
           illusion — and it ATROPHIES unaided comprehension. (F1 keystone; AI-era impact —
           ~17% lower unaided comprehension after AI assistance, Anthropic RCT.)
Example trigger: "I let the AI write it, read it, and if it looks right I move on."
```

### 5d. Grading mode

**Rubric + golden exemplars** (`drill-generation.md` §1d, §3) — a **judgment** module. There
is **no executable ground truth for "is this practice well-designed?"** and **no single
correct plan**. The coach grades like this (the §3 judgment path, made concrete for F2):

1. **Score the critique/design against the three F2 dimensions, criterion by criterion**
   (§7): **D1 — Diagnose** (named the real anti-patterns and the principle each violates — not
   a decoy, not a good element); **D2 — Prioritize & redesign** (targeted the highest-leverage
   fix and produced a redesign that flips the levers — *not* "add more hours"); **D3 — Justify**
   (can explain *why*: felt-ease is an anti-signal, hours ≠ learning, no single correct plan —
   not just parrot a rule). Each is a 3-point criterion (absent / partial / solid).
2. **Run the *one* executable sub-claim, where present.** When a redesign turns a passive
   element into a **predict-then-check** drill, the coach **runs the embedded snippet** via
   `python <skill-dir>/runtime/python/runner.py snippet.py` and **pastes the real output**
   (`drill-generation.md` §2). This does two honest things: it **demonstrates the redesigned
   practice now *has* external ground truth** (the thing the original lacked), and it
   **grounds any claim about what the snippet does**. The *design verdict* stays rubric-graded;
   only the snippet's behavior is executable. (This is the same surface-ground-truth discipline
   the redesign is *teaching*.)
3. **Cite the closest golden exemplar** in `exemplars/F2/<tier>.md` — "your critique is close
   to the **weak** exemplar: you spotted the cramming but missed that re-reading is the bigger
   miss" vs. "close to the **strong** exemplar: you led with QUALITY+FEEDBACK and demoted the
   hours framing."
4. **Name it as soft, and name the genuine uncertainty.** The coach says out loud: *"this is a
   judgment call graded against the module's rubric + exemplars, not a machine-verifiable
   answer — and there is no single correct practice plan."* And the deeper uncertainty
   (§1c, §8): the **principles are verified general science, but the programming-specific
   causal payoff is the open question**, and **the DP magnitude is itself disputed** — so the
   coach grades the learner's **reasoning against the principles**, never against a promise
   that "this plan will make you X% better."

F2 drills are thus **rubric-graded with one optional executable sub-claim**, reported
separately: a learner who **diagnoses** the anti-patterns well (rubric: solid) but whose
redesign's embedded snippet, when run, reveals they misread what the code *does* (executable:
no) is told exactly that — the design reasoning can be sound while a specific code claim is
wrong, and conflating the two is itself the fluency illusion the module targets.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single axis (`drill-generation.md`
§5). Escalating two steps collapses to failure; escalating none loses the desirable-difficulty
benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = diagnose a subtle hidden flaw in a plausible-looking routine (redesign +
  teach the principle), **or** design a defensible practice plan from scratch for a goal.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new dimension
  of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for F2, with step counts:

1. **Subtler / more-camouflaged flaw** (push the decoy & difficulty axes): from a routine with
   **one** subtle missing lever (Frontier-1) → to one with a **second-order** flaw, where the
   levers are each individually fine but *interact* badly — interleaving so aggressive no
   single skill ever reaches its edge, or spacing so wide nothing consolidates (Frontier-2) →
   to a routine that is textbook-correct *in general* but **mis-targeted for THIS learner's
   actual goal/edge** (e.g., grinding algorithm puzzles when the goal is shipping
   maintainable services) (Frontier-3). Each is one increment.

2. **Design under constraint** (push the design axis): design a plan for a real goal
   (Frontier-1) → **under a tight time budget** where the learner must *triage which levers to
   spend on* and justify the trade-off (Frontier-2) → for a skill with **no executable ground
   truth** (design, naming, review), where the *feedback* lever must come from rubrics,
   exemplars, and peer review rather than a runner — designing good feedback *without* an
   oracle (Frontier-3). Each is one increment.

3. **AI-era practice design** (push the AI-trust axis): design a regimen that **uses an AI
   assistant to learn *faster* without the comprehension-atrophy / trust-by-plausibility
   trap** — building generation (predict before accepting), verification (run/test the
   output), and unaided-retrieval back in (`evidence-base.md` → AI-era impact, the ~17%
   unaided-comprehension drop). One increment for "uses AI," another for "and provably avoids
   the atrophy trap."

4. **Meta-calibration of one's own practice** (the reflexive push): instrument the learner's
   *real* practice, **predict their own held-out delta before a stretch, then measure it** and
   reconcile the gap — calibrating their model of their own learning (ties to F1 and
   `assessment.md` Part 3). One increment.

5. **Coach-the-coach → the fully reflexive frontier.** Critique *this curriculum's* design
   against the five levers, or **design a practice curriculum for someone else** (a junior, a
   teammate) given their goal and edge. This is F2 turned all the way around — the learner is
   now the instructional designer. Track it as the terminal Frontier band.

Track the level as `F2: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the three F2 dimensions. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (diagnosed the right anti-patterns *and* can justify the
principle — a correct critique with a hand-wavy or rule-parroting "why" is a Foundations-level
pass at best), and **unaided + durable** (a same-session critique streak is provisional until a
delayed re-assessment or the **real-practice** transfer task confirms it; `assessment.md` Parts
3–5 — and for F2 the durable signal is unusually heavily weighted, see below).

**The three scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Diagnose.** Did the learner name the *actual* anti-patterns and the principle each
  violates — not a decoy, not a good element flagged as bad, not a vague "needs more"?
- **D2 — Prioritize & redesign.** Did they target the **highest-leverage** fix and produce a
  redesign that **flips the levers** (generative, ground-truth-checked, edge-targeted, spaced)
  — rather than "do more hours / try harder"?
- **D3 — Justify.** Can they explain *why* — felt-ease is an anti-signal, hours ≠ learning,
  the design is individual (no single correct plan) — grounded in the principle, not parroted?

| Tier | Observable bar for F2 |
|---|---|
| **Foundations** | On a **single-anti-pattern** routine (no decoys), **names the anti-pattern, the principle it violates, and the one fix** — e.g., "re-reading is passive/no-generation; switch to predict-then-check." D1 solid; D3 at least partial (states the principle, not just the fix). Allowed *with* the worked example faded to one missing step. |
| **Working** | On a **mixed** routine, **unaided**: catches **all the material anti-patterns including the hours/comfort framing** (D1), **prioritizes the highest-leverage fix and redesigns flipping the levers** (D2), **does not "fix" a genuinely-good element**, **and** explains *felt-ease-is-an-anti-signal* / *hours ≠ learning* (D3). Buries the big miss under a minor one, or "fixes" a good lever ⇒ partial pass, flagged. On **3 of 4** unseen routines. |
| **Advanced** | On a **subtle** routine (looks rigorous, hidden flaw) **or** a **design-from-scratch** brief, **unaided**: diagnoses the hidden flaw / produces a **defensible from-scratch design with a held-out measure** (D1+D2), and **teaches the principle** on a teach-it-back (`drill-generation.md` §6) — including naming that there is **no single correct plan** and **why the verified science does not license hour-counting** (the DP-dominance refutation, *and* that the magnitude is disputed) — not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler/second-order flaw → mis-targeted-for-this-goal → budgeted design → no-oracle feedback → AI-era → meta-calibration → coach-the-coach). A moving target, not a fixed bar. |

**Scaffolding under struggle is F2-specific** (`coaching-loop.md` Step 7 — fade the scaffold,
never the challenge): a learner stuck on a critique is **not handed the diagnosis**; the setup
is sharpened — *"walk it against each of the five levers in turn: is the practice generative?
is there external feedback? is it aimed at your edge? is it desirably hard? is it spaced?"* The
difficulty of the setup rises; the diagnosis they must generate stays theirs.

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen routines, never from claimed seniority or "I've been
practicing for years" (years are exactly the hour-dosing proxy this module rejects — Finding 7
*and* the DP folklore). **Held-out re-assessment and real-practice transfer outrank a
same-session streak (`assessment.md` Part 5) — and for F2 this is the whole point reflexively:**
the honest test of whether F2 transferred is whether the learner's **own practice** improves
their **held-out deltas over weeks** (§9). A learner who critiques synthetic routines flawlessly
but whose real practice is still hour-dosing and re-reading has **not** mastered F2.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Hour-dosing / streak-chasing.** Counting time or days as the goal and the measure — "I'm
  aiming for 10,000 hours," "I'm on day 40." The fix: measure **held-out deltas** on cold,
  unseen tasks, not the clock. *Hours are an input, not a result.*
- **Re-reading / passive consumption.** Re-reading solved solutions, re-watching tutorials,
  highlighting the docs — and feeling productive. The fix: **generate** (predict, blank-page,
  explain-back) *before* you look.
- **Self-grading with no ground truth.** "Yeah, I get it." The fix: **check against an external
  truth** — run it, test the edge case, diff against the rubric — immediately.
- **Grinding the comfortable.** Redoing the easy/solved because it feels good. The fix: **target
  your edge** (use F1 to locate it).
- **Trusting felt-ease.** Reading a smooth session as a learned session. The fix: treat **felt
  ease as an anti-signal**; expect good practice to feel harder and slower.
- **Massing / cramming.** One marathon block, or a pre-deadline week then nothing. The fix:
  **space and interleave**, and **revisit** on a schedule.
- **Generation without feedback (or without spacing).** Hard blank-page work that's never
  checked or never revisited. The fix: **close the loop** — the five levers are a *system*.
- **Mistaking performance for learning.** Promoting yourself off a same-session streak. The fix:
  weight **delayed** and **real-code** transfer (`assessment.md` Part 5).
- **Copying one regimen / seeking the one true schedule.** The fix: **individualize** — the
  principles constrain; the plan is yours. *There is no plan catalog.*
- **AI-trust-by-plausibility as practice.** "The AI wrote it, it looks right, next." The fix:
  build **generation + verification** back in — predict before accepting, run the edge cases.

**Evidence caveat (this is a `[Verified-adjacent]`-badged module — verified *general* learning
science, thin *programming-specific* transfer — and a *reflexive* one, so it must be unusually
careful about its own claims):**

1. **The principles are verified *general* science; the *programming-specific* causal payoff
   is not.** The five levers rest on the instructional pillar (testing/generation, spacing,
   desirable difficulties, worked examples + expertise reversal, learning ≠ performance,
   metacognition) — among the most replicated findings in cognitive psychology, and genuinely
   `[Verified]` *as general learning science*. But that body of work was built on
   **general-knowledge questions, classroom learning, and lab tasks, not professional code**,
   and the evidence base badges the pillar's *programming transfer* one tier down for exactly
   this reason. So the coach says: **"this is solid learning science in general; that designing
   your *programming* practice this way *causally* makes you a better engineer is the same open
   question the whole curriculum carries."** The honest individual-level test is §9.

2. **The deliberate-practice-dominance / "10,000-hour" thesis is REJECTED — and the rejection
   is itself carefully bounded.** DP explains **~12% of variance overall** and **~1% in
   professions** (Macnamara et al. 2014); time-to-mastery varies **~8×** between people (Gobet
   & Campitelli 2007); and **the numbers are from music/sports/chess/games, not software.**
   *On top of that* there is a **live scientific dispute** — Ericsson and colleagues contested
   the magnitude and definition. So the coach does **not** swing to the opposite overclaim
   ("practice doesn't matter"); the bounded truth is: **"the strong 10,000-hour claim is not
   supported; practice matters but is far from the whole story; the precise numbers aren't from
   programming; and the magnitude is disputed."** _Peak_ is read **critically** — mined for the
   quality-of-practice ideas, not the hour thesis (`evidence-base.md` → reading spine).

3. **F2 is subject to its own standard.** Because this module *is* the evidence base applied
   reflexively, it cannot promise "design your practice this way and you'll improve by X" —
   that would be the very overclaim it teaches learners to reject. It teaches the **principles**
   and the **measurement stance**; the proof for any individual is their **own held-out deltas
   over time** (§9; `assessment.md` Part 3), reported with the same honesty guardrails as the
   rest of the curriculum (small-n, within-person, no causal overclaiming).

No claim in this module is presented as `[Verified]`; the badge is `[Verified-adjacent]`,
hedged in prose exactly where the verified *general* science stops and the *programming-specific*
promise would begin — mirroring F1, and the evidence base's `[Verified-adjacent]` badging of the
instructional pillar this module rests on.

---

## 9. Transfer task

**The only honest test of whether the meta-skill transferred is the learner redesigning — and
then *running* — their own real practice** (`assessment.md` Part 4; `evidence-base.md` →
transfer caveat, consequence 2). For F2 this is doubly true: the module *is* about the
learner's practice, so the transfer task is not a sidecar — it is the actual deliverable.

> **Your turn (two parts, both on *your own* practice):**
>
> **Part A — audit what you actually do.** Write down, honestly, what you did to get better at
> programming in the **last month** — what activities, how often, and *how you knew it was
> working*. Now **critique it against the five levers**: which are present, which are missing?
> Is it generative or re-reading? Is there external feedback or self-grading? Is it aimed at
> your edge or your comfort? Is it desirably hard or smooth? Is it spaced or massed? And the
> meta-check: is your "how I knew it was working" a **held-out delta**, or **hours / a streak /
> a feeling**? Name the **single highest-leverage change**.
>
> **Part B — redesign, then measure (don't just plan).** Redesign **one week** of practice that
> flips your **weakest** lever. Then — and this is the part that makes it real — **define a
> held-out measure**: a small set of *cold, unseen* problems (or a kind of task you currently
> fail) that you'll attempt **before and after**, scored by a **test battery you run through the
> runner**, not by hours logged or by how the week felt. Run the *before* battery now. (Reduce
> any check to a minimal snippet and use `runner.py` for the executable sub-claim — the point of
> the redesign is that it *has* external ground truth.)

**Grading is softer and named as such** (`assessment.md` Part 4). A real practice plan has no
clean answer key, and **there is no single correct design**; the coach grades against the §7
rubric (D1 diagnose / D2 prioritize+redesign / D3 justify) and says: *"this is a judgment call
on your real practice, not a machine-verifiable result."* But the **measurement half is pinned
to ground truth**: wherever the held-out check is runnable, the coach uses the runner, so the
*delta* is measured against real output, not a feeling. **Transfer evidence is weighted
heavily, and for F2 most heavily of all:** a learner who critiques synthetic routines perfectly
but, on their *own* practice, still **dose-counts hours and re-reads solved code** has **not**
transferred the one skill this module exists to install — and the tracker notes that gap as far
more diagnostic than another flawless synthetic critique. The slow, spaced, held-out delta on
the learner's *own* practice (`assessment.md` Part 3) is the honest measure of whether F2 — and,
reflexively, the whole curriculum — actually worked.

---

## Cross-references

- Drill mechanics, the **rubric + exemplars judgment path**, the one executable sub-claim
  (running a snippet the redesign would predict-then-check), exercise formats (Error-analysis,
  Generation→Comparison, Teach-it-back, Debug-this), Frontier escalation:
  `references/drill-generation.md` (this module instantiates §1 and follows §3, §4, §5; the
  snippet check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback, the
  "walk it against the five levers" scaffold under struggle): `references/coaching-loop.md`.
- **F2 entry task** (a described practice routine with anti-patterns baked in — critique it
  against the five levers and redesign it; the AI-assisted "looks-right" routine as the
  concrete example), per-skill routing, mastery-rubric shape, held-out re-assessment as the
  reflexive measure, transfer weighting, the optional affective layer: `references/assessment.md`.
- Evidence grounding — the **verified** half: `evidence-base.md` → *Learning-science
  instructional pillar* (generation/testing — Roediger & Karpicke; pre-testing — Giebl; spacing
  — Kornell/Kang; worked examples + expertise reversal — Sweller/Kalyuga; desirable difficulties
  — Bjork; learning ≠ performance — Soderstrom & Bjork; metacognition — Dunlosky). The
  **REJECTED** half: `evidence-base.md` → *Folklore we explicitly reject* → the strong
  10,000-hour / deliberate-practice-dominance thesis (Macnamara et al. 2014; Hambrick et al.
  2014; Gobet & Campitelli 2007), and the reading spine's "read _Peak_ critically." The
  **caveat**: the curriculum-wide transfer caveat.
- Closest tie: module **F1** (metacognition & calibration — knowing your edge, the targeting and
  measurement instrument); and the **whole curriculum**, whose practice F2 teaches the learner to
  design. Soft-prereq feedback lever leans on the executable spine (**A1/A3/C1/B2**).
- Golden exemplars (~3 per tier, each a described routine to critique or a plan to design, with
  the gold critique/redesign + rubric note, and the runner-verified snippet where the redesign
  predicts-then-checks): `exemplars/F2/foundations.md`, `exemplars/F2/working.md`,
  `exemplars/F2/advanced.md`.
</content>
</invoke>
