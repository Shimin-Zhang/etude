# F2 — Advanced exemplars (designing your own practice)

Golden drills for the **Advanced** tier of module F2: a **subtle hidden flaw** in a
plausible-looking routine (diagnose + redesign + **teach the principle**), and **design from
scratch** for a stated goal (produce a defensible plan **with a held-out measure**, defend it).
These are **judgment-graded against the rubric below** (`drill-generation.md` §3) — there is **no
single correct plan**, and the coach says so. Where a redesign or plan uses a **failing test /
predict-then-check** as its feedback lever, the embedded snippet is **run** to ground it
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans a hidden-flaw critique, a from-scratch design, and the AI-era design. Pose one,
**hard-stop, wait** (`coaching-loop.md`). At Advanced the coach hands over only the routine/brief
and the five levers; the learner diagnoses/designs unaided and **teaches the underlying
principle** (`drill-generation.md` §6). **How to grade**: **D1** diagnose · **D2**
prioritize/redesign or design-from-scratch · **D3** justify the principle (felt-ease anti-signal /
learning ≠ performance / hours ≠ learning / no single correct plan).

---

## A1 — The routine that *looks* rigorous (hidden flaw: no spacing + performance-for-learning)

> *"My practice is dialed in. I do **blank-page solutions to unseen problems** (no peeking), I
> **run each one against a test battery with edge cases** so I get immediate feedback, and I keep
> at one topic **4 hours a day until I've completely mastered it** — until I can solve every
> problem in it without a miss. Then I check the topic off and move to the next one. I never
> needed to come back to arrays once I'd mastered them."*

> **Your turn:** Three of the five levers are genuinely strong here. Find the **hidden flaw**,
> redesign to fix it, and explain *why* it's a flaw even though the routine feels rigorous.
>
> (Take your best guess — wrong attempts are useful data.)

**The trap.** This routine nails **QUALITY (blank-page generation)**, **FEEDBACK (edge-case test
battery)**, and **DESIRABLE DIFFICULTY (unseen problems)** — so a shallow critique praises it.
The hidden flaw is in the **last two levers**, and it's subtle:

- **SPACING ❌ — massed, never revisited.** "4 hours a day on one topic until mastered, then
  never come back" is a **marathon per topic** with **no spaced return**. Arrays mastered in
  March and never revisited will have decayed by June.
- **The deeper flaw — performance mistaken for learning.** "Until I can solve every problem
  *without a miss*, then move on" uses **same-session performance as the promotion signal** —
  the exact thing that is a **poor index of durable learning** (Soderstrom & Bjork 2015). The
  4th hour's flawless streak is *in-session fluency*, not proof it will survive. Promoting off
  that streak is the **learning ≠ performance** error (§5c).

**Redesign** (keep the three strong levers; fix the two):

> - **Space + interleave:** cap a topic session well short of "mastery in one sitting";
>   **interleave** topics within a week; **revisit** each topic on an expanding schedule (a few
>   days, a week, a month) — *especially* the ones already "mastered."
> - **Promote on a delayed, held-out check, not a same-session streak:** consider a topic
>   durable only when you pass **fresh, unseen** problems in it **after a delay** (`assessment.md`
>   Parts 3, 5) — not when you hit a hot streak at hour 4.
> - **Keep:** blank-page generation, the edge-case battery, the unseen difficulty.

**Runner-verified evidence** (what a *delayed, held-out* re-test looks like — a fresh bug in an
"already-mastered" topic, surfaced weeks later, with the real wrong output as the feedback):

```python
def running_max(xs):
    out = []
    m = xs[0]
    for x in xs:
        out.append(m)         # records the max-so-far BEFORE considering x
        if x > m:
            m = x
    return out

print(running_max([3, 1, 4, 1, 5, 9, 2]))   # expected [3,3,4,4,5,9,9]
```

```
stdout: "[3, 3, 3, 4, 4, 5, 9]\n"
status: ok
```

The output **lags one position** (and drops the final `9`) — `[3, 3, 3, 4, 4, 5, 9]`, not
`[3, 3, 4, 4, 5, 9, 9]`. A learner who "mastered arrays in one marathon and never came back"
would miss this on a delayed held-out re-test — which is exactly why the promotion signal must be
the **delayed** check, not the in-session streak.

**Why (the principle to teach back).** Rigor on three levers can hide a fatal gap on the other
two, and the most seductive gap is **mistaking a same-session streak for durable learning** —
because it *feels* like the most rigorous part ("I didn't miss one!"). Spacing and a delayed
held-out check are the unglamorous levers that make the rigor *stick*.

**Rubric** (3-point each: absent / partial / solid):

| # | Criterion | Solid = |
|---|---|---|
| 1 | **Finds the spacing flaw** | Names the per-topic massing **and** the missing spaced *return*, not just "4 hours is long." |
| 2 | **Finds the performance-vs-learning flaw** | Identifies "promote on a same-session no-miss streak" as the deeper error; cites learning ≠ performance. |
| 3 | **Keeps the good levers** | Does **not** "fix" the blank-page generation, the test battery, or the unseen difficulty. |
| 4 | **Redesign closes both gaps** | Adds spacing/interleaving/return **and** a delayed held-out promotion signal. |
| 5 | **Teaches the principle** | Can explain *why* a rigorous-feeling streak is the trap (felt-ease/performance ≠ durable learning). |

- **Advanced pass:** 1, 2, 4, 5 solid with 3 at least partial — found *both* hidden flaws,
  preserved the good levers, taught the principle.
- **Working-level (partial):** finds the spacing flaw but misses the performance-vs-learning one
  (the subtler half), or "fixes" a good lever. Name it and route to more hidden-flaw drills.
- **Diagnoses.** Praising the routine wholesale → fooled by surface rigor (D1 fail). Fixing a good
  lever → over-correction (§5c). Found spacing but not performance≠learning → the subtle-miss gap.

---

## A2 — Design from scratch: 3 weeks of debugging practice, 45 min/day (GOLD RUBRIC)

> **Brief:** *"Design me a 3-week practice plan to get measurably better at **debugging** (the C1
> skill — systematic, hypothesis-driven debugging), given **45 minutes a day**. Tell me what I do
> each session and **how I'll know it worked.**"*

> **Your turn:** Design the plan. Hit the five levers, and define **how progress is measured** —
> defend your choices.
>
> (Take your best guess — wrong attempts are useful data.)

This is **judgment-graded against the rubric below** — **there is no single correct plan.** The
coach grades whether the design *hits the levers and defends them*, not whether it matches a
template.

**Gold plan (one defensible design — the levers, made concrete):**

> - **TARGETING:** Start by finding the *edge*: attempt a handful of failing-test debugging
>   problems cold and note **where** you stall (forming hypotheses? testing them? reading the
>   traceback?). Aim the three weeks at the weakest sub-step (`assessment.md` C1 scores the
>   *hypothesis set*, not just the catch).
> - **QUALITY (generate):** Each session, **before** touching the bug, write down **three ranked,
>   falsifiable hypotheses and the discriminating test for each** (the C1 move) — generation, not
>   reading the fix.
> - **FEEDBACK (ground truth):** Use **real failing tests**; **run** each hypothesis's test
>   through the runner and let the actual output confirm/kill it — never self-grade "I think
>   that's it."
> - **DESIRABLE DIFFICULTY:** Use bugs you haven't seen, slightly above comfort; resist looking up
>   the answer until you've run at least one discriminating test.
> - **SPACING / INTERLEAVING:** 45 min/day **distributed** beats one weekly marathon; **interleave**
>   bug classes (off-by-one, mutation, concurrency) rather than a week each; **revisit** a prior
>   week's bug type on a spaced schedule.
> - **MEASURE (held-out, not hours):** Bank **held-out failing-test problems untouched** at the
>   start; re-attempt fresh ones at the end of week 3. Progress = **the delta in hypothesis
>   quality and time-to-localize on cold bugs**, scored by the C1 rubric — **not** "I did 21
>   sessions."

**Runner-verified evidence** (what one session's *feedback lever* looks like — a real bug whose
failing run is the ground truth, not the learner's guess):

```python
def is_sorted(xs):
    for i in range(len(xs)):
        if xs[i] > xs[i + 1]:      # hypothesis: does i+1 run off the end?
            return False
    return True

print(is_sorted([1, 2, 3]))
```

```
status: error
stderr (last line): IndexError: list index out of range
```

The bug **raises `IndexError`** (on the last iteration `xs[i + 1]` is out of range) — so the
session's discriminating test ("does the loop index run past the end?") is **confirmed by the
runner**, not asserted. Fixing the range to `range(len(xs) - 1)` and re-running yields
`True / False / True / True` on `[1,2,3] / [1,3,2] / [] / [7]` — the feedback the plan is built
around.

**Rubric** (3-point each):

| # | Criterion | Solid = |
|---|---|---|
| 1 | **All five levers present** | Generation, feedback-vs-ground-truth, edge-targeting, desirable difficulty, spacing/interleaving each show up concretely. |
| 2 | **Targets the C1 sub-skill** | Diagnoses *where* in debugging the learner is weak and aims there — not generic "do bugs." |
| 3 | **Feedback is external** | Uses real failing tests + the runner, not self-grading; the hypothesis is *tested*, not believed. |
| 4 | **Held-out measure, not hours** | Defines a cold, delayed re-test scored by the C1 rubric; **rejects** "sessions done" / hours as the metric. |
| 5 | **Defends, doesn't dose** | Justifies choices by the principles; does **not** reach for "just add more time." |

- **Advanced pass:** 1, 3, 4 solid + 2 and 5 at least partial — a plan that hits the levers and
  measures by held-out transfer.
- **Working-level (partial):** a sensible plan that nonetheless measures by **hours/sessions** or
  has **no external feedback** (self-graded) — the two most common design misses. Name which lever
  is open.
- **Diagnoses.** A plan that's a daily *hour budget* with no held-out measure → hour-dosing in
  planning clothes (§5c). A plan with no runner/failing-test feedback → self-grading. A plan that
  blocks the whole 45 min on one bug class all three weeks → massing. Strong design: levers
  concrete, feedback external, measured by a cold delayed delta.

---

## A3 — Design from scratch (AI-era): practice *with* an assistant, without the atrophy (GOLD RUBRIC)

> **Brief:** *"I use an AI assistant all day. Design a practice routine that uses the assistant to
> get better **faster** — without falling into the trap where my own skills quietly **atrophy**
> because the AI does the thinking."*

> **Your turn:** Design it. How do you keep generation, feedback, and unaided skill alive *while*
> using the AI? Defend the design.
>
> (Take your best guess — wrong attempts are useful data.)

**Judgment-graded against the rubric below** — no single correct plan. The tension to resolve:
the assistant is fluent, so naive use maximizes the **fluency illusion** and measurably lowers
**unaided** comprehension (`evidence-base.md` → AI-era impact, ~17% drop; F1 keystone). The design
must put **generation and verification back in front of the AI's fluency.**

**Gold plan (one defensible design):**

> - **Predict before you accept (generation):** before reading the AI's output, **predict what it
>   should return** on a tricky input and **sketch your own approach**; *then* compare. The AI
>   reveals *after* you generate, never before.
> - **Verify, don't trust (feedback):** **run the AI's code on edge cases** (empty/boundary/dupes)
>   and **diff against your prediction** — plausibility is not correctness.
> - **Protect unaided reps (targeting + difficulty):** keep a **no-AI block** each session where
>   you solve from a blank page, so the unaided muscle doesn't atrophy; aim it at your edge.
> - **Space + retrieve:** **revisit** AI-assisted solutions later **without the AI**, from memory,
>   to convert recognition into recall.
> - **Measure (held-out, AI-off):** progress = your **unaided, AI-off** delta on cold problems —
>   not volume shipped with the AI on.

**Runner-verified evidence** (the "verify before you trust" lever — an AI-written function that
looks right and fails an edge case):

```python
# The assistant wrote this for "return the average of a list of numbers":
def average(nums):
    return sum(nums) / len(nums)

print(average([2, 4, 6]))   # predict, then run...
print(average([]))          # the edge case to verify before trusting
```

```
stdout: "4.0\n"
status: error
stderr (last line): ZeroDivisionError: division by zero
```

The function is correct on `[2, 4, 6]` → `4.0`, but `average([])` **raises `ZeroDivisionError`**
— the empty-input case the AI's fluent output silently skipped. Predicting then **running the
edge case** is the verification the design is built to force, *before* the plausible code gets
trusted.

**Rubric** (3-point each):

| # | Criterion | Solid = |
|---|---|---|
| 1 | **Generation before the AI** | The learner predicts/sketches *before* the assistant reveals — not after. |
| 2 | **Verification, not trust** | Plan runs/tests the AI's output on edge cases; treats plausibility as a hypothesis to check. |
| 3 | **Protects unaided skill** | Includes deliberate **AI-off** reps so unaided comprehension doesn't atrophy. |
| 4 | **Spacing/retrieval** | Revisits AI-assisted material later *from memory*, AI-off. |
| 5 | **Measures AI-off transfer** | Progress is the **unaided** held-out delta, not AI-on volume; defends it. |

- **Advanced pass:** 1, 2, 3, 5 solid with 4 at least partial — the design keeps generation,
  verification, and unaided reps alive and measures AI-off.
- **Working-level (partial):** "use the AI, but read its code carefully" — better than nothing but
  still **passive** (no generation-before, no verification, no AI-off measure). Name the open
  levers.
- **Diagnoses.** A plan that's "let the AI teach me, I'll pay attention" → trust-by-plausibility
  as practice (§5c, the keystone AI-era miss). No AI-off block → atrophy unaddressed. Measures
  AI-on throughput → hour-dosing with an AI. Strong design: predict-before-reveal, verify edge
  cases, protect unaided reps, measure AI-off.
</content>
