# F1 — Foundations exemplars (metacognition & calibration)

Golden drills for the **Foundations** tier of module F1. Each wraps a **single** predict-the-output
snippet (familiar surface) in a **confidence layer**: the learner rates confidence 0–100%
*before* answering, predicts, then the coach runs it and scores **BOTH** the answer and
whether the confidence was justified. The teaching goal is *noticing the gap* and grasping
that **confidence is itself gradable**, separate from correctness.

Every answer key below was obtained by **running the snippet through the runner**
(`drill-generation.md` §2) — calibration is only meaningful against **real** ground truth,
never an asserted answer:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Per `coaching-loop.md`, the coach poses one drill, then **hard-stops and waits** — the
answer key and the calibration read are for *grading*, never shown before the learner
attempts. One trial teaches the *loop*; the over/under-confidence **verdict** needs the
Working battery (`assessment.md` F1 task: a single trial is noise).

---

## F1 — High confidence, correct: confidence that was *earned*

```python
print(3 * "ab" + "c")
```

> **Your turn:** Before you answer — how confident are you that you'll get this exactly
> right (0–100%)? Then: what does it print?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "abababc\n"
status: ok
```

So the printed line is `abababc`.

**Why (the answer).** `*` binds tighter than `+`: `3 * "ab"` repeats the string to
`"ababab"`, then `+ "c"` concatenates → `abababc`.

**How to score the calibration.** This snippet is **genuinely easy**, so a **high
confidence (90%+) that lands** is *justified* — the model and the number agreed. Reward it:
"your 95% was earned — correct *and* confidently so." The calibration lesson here is the
**positive anchor**: this is what high-confidence-correct *should* feel like, so the learner
can later contrast it with the fluency trap (Working tier) where the same 95% is *unearned*.

**Diagnoses.** A *wrong* answer here (e.g. `ababab c` with a stray space, or `abcabcabc`
from misreading the operands) **rated high** is an early over-confidence signal — the
snippet is easy, so a confident miss means the learner isn't actually tracing. A *correct*
answer rated **low** (e.g. 40%) is mild **under-confidence** — real knowledge given no
credit. (Catalog §5c; the positive-anchor case.)

---

## F2 — High confidence, WRONG: the fluency trap (looks trivial, isn't)

```python
print(0.1 + 0.2 == 0.3)
```

> **Your turn:** First — how confident are you (0–100%) you'll get this exactly right?
> Then: what does it print, `True` or `False`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "False\n"
status: ok
```

So the printed line is `False` — **not** `True`.

**Why (the answer).** Binary floating point can't represent `0.1`, `0.2`, or `0.3` exactly.
`0.1 + 0.2` evaluates to `0.30000000000000004` (confirmed by running `print(0.1 + 0.2)`),
which is **not** equal to the stored `0.3`. So `==` is `False`.

**How to score the calibration.** This is the **fluency trap** and the central Foundations
lesson: the snippet *looks* trivial, so it reliably draws a 90%+ — and that confidence is
bought by **smooth reading**, not by knowing the *behavior*. A **high-confidence miss here
is the gap to notice**: nothing in the learner fired to say "floats — better check." Name it
exactly: "your 90% came from how *simple it looked*; looking easy is not being easy. The
cure is a check — trace or run, don't trust the smoothness." (Koriat & Bjork 2005, illusions
of competence.)

**Diagnoses.** Predicting `True` at high confidence reveals the **fluency trap**
(processing-ease mistaken for behavior-knowledge). The valuable variant: a learner who
predicts `True` **but rated only 55%** — wrong answer, but they *flagged the doubt* — is a
**calibration success** even while failing the prediction; that is the behavior to reward.
(Catalog §5c, the fluency-trap and wrong-but-flagged entries.)

---

## F3 — Aliasing: the costly wrong-and-certain vs. the healthy wrong-and-flagged

```python
xs = [1, 2, 3]
ys = xs
ys.append(4)
print(xs)
```

> **Your turn:** Rate your confidence (0–100%) first. Then: what does this print — does
> `xs` change when we append to `ys`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[1, 2, 3, 4]\n"
status: ok
```

So the printed line is `[1, 2, 3, 4]` — `xs` **does** change.

**Why (the answer).** `ys = xs` does **not** copy; it binds a **second name to the same list
object**. `ys.append(4)` **mutates that shared object in place**, and `xs` labels the very
same object — so the append is seen through `xs` too. (This is the A1 aliasing mechanism;
F1's job is the *confidence* layer on top of it.)

**How to score the calibration.** This snippet separates the **two faces of a wrong answer**
— the whole point of F1:

- Predicting `[1, 2, 3]` (append not seen) at **95% with no doubt** is the **consequential
  miscalibration**: wrong *and* certain, nothing said "verify." In the AI era this is the
  one that ships the bug. Name it bluntly (Kruger & Dunning 1999, the dual burden — the
  skill to get aliasing right and the skill to *doubt* your aliasing answer are the same
  skill).
- Predicting `[1, 2, 3]` but rating **50–60%** — *the same wrong answer* — is a **calibration
  success**: the learner flagged exactly the uncertainty that mattered. Credit it explicitly:
  "wrong answer, but you *handled it right* — you doubted it, which is what tells you to
  check." (This is worked-example #3 in the module §4.)

**Diagnoses.** The grade is on the **(confidence, correct?) relationship**, not the answer
alone: a confident `[1,2,3]` → flat-high / wrong-and-certain (catalog §5c); a flagged
`[1,2,3]` → well-flagged miss (a *pass* on calibration). A confident `[1,2,3,4]` → earned.
Reward the **pre-reveal flag** ("I'm unsure whether `ys` is a copy or the same list") over a
post-reveal "oh, I knew that." (Flavell 1979, monitoring before the reveal.)
