# C1 — Foundations exemplars (systematic debugging)

Golden drills for the **Foundations** tier of module C1. Each is **one clear bug on a familiar
surface**: the failure is obvious once you *run* it, so the skill is the **loop itself** —
**observe** (run the failing case), **hypothesize** (one specific, falsifiable cause),
**predict** (the fix effect), **test** (re-run). Single mechanism, no camouflage. Every
**buggy output and every fixed output below was obtained by running the snippet through the
runner** (`drill-generation.md` §2) — the coach never guesses output:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct Foundations bug classes: an **off-by-one range** (drops the last
term), an **accumulator reset inside the loop**, and a **wrong logical operator** (`or` where
`and` is meant). Pose one, **hard-stop, wait** (`coaching-loop.md`) — the answer key is for
*grading*, never shown before the learner attempts. **How to grade** against module §7
(executable + hybrid, §5d): the **fix is executable** (apply it, re-run — it works or it
doesn't); the **hypothesis is rubric-graded** (specific? falsifiable? names the mechanism?). A
working fix reached by a vague guess is a **partial pass** — flag it.

---

## F1 — Off-by-one: the range that drops the last term

**Spec.** `sum_to(n)` returns `1 + 2 + ... + n` (inclusive).

```python
def sum_to(n):
    total = 0
    for i in range(1, n):
        total += i
    return total

print(sum_to(5))   # expected 15 (1+2+3+4+5)
```

> **Your turn:** Run this and observe what it prints. Then: what's your hypothesis for the
> cause, what do you predict the *fixed* version prints, and what's the one-line fix?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
buggy  sum_to(5) -> stdout "10\n"   status ok
fixed  sum_to(5) -> stdout "15\n"   status ok   (fix: range(1, n + 1))
```

So the buggy version prints **10**; the fix prints **15**.

**Why.** `range(1, n)` is **half-open** — it yields `1, 2, 3, 4` and **stops before `n`**, so
the final term `5` is never added: `1+2+3+4 = 10`. The fix is `range(1, n + 1)`, which includes
`n`. The discriminating observation: the result is short by exactly `n` (`15 - 10 == 5`), which
points straight at a dropped final term, not a wrong starting value.

**Diagnoses.** A learner who **proposes a fix without running it first** skipped *Observe*
(§5c, fix-before-observe). A learner whose hypothesis is "the loop is wrong" rather than "the
upper bound is exclusive so the last term is dropped" has a **vague/unfalsifiable hypothesis**
(§5c). A learner who predicts the fixed output as `14` or `15` but can't say *why* the original
lost the `5` has the symptom without the mechanism — push for the half-open-range explanation.
Strong attempt: runs it (10), hypothesizes the exclusive upper bound, predicts 15, fixes with
`n + 1`, re-runs to confirm. Bug class: **off-by-one / boundary** (Catalog §5c; an A1 trace of
the loop's `i` values exposes it).

---

## F2 — Accumulator reset *inside* the loop

**Spec.** `total_chars(words)` returns the sum of the lengths of all the words.

```python
def total_chars(words):
    for w in words:
        total = 0
        total += len(w)
    return total

print(total_chars(["ab", "cde", "f"]))   # expected 6 (2 + 3 + 1)
```

> **Your turn:** Run it and observe. What's your hypothesis, what do you predict the fix
> prints, and what's the fix?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
buggy  total_chars(["ab","cde","f"]) -> stdout "1\n"   status ok
fixed  total_chars(["ab","cde","f"]) -> stdout "6\n"   status ok   (fix: move total = 0 above the loop)
```

So the buggy version prints **1**; the fix prints **6**.

**Why.** `total = 0` is **inside** the loop body, so it **re-zeroes `total` on every
iteration** before adding `len(w)`. After the last iteration `total` is just `len("f") == 1` —
the previous additions are thrown away each pass. The result equals the length of the **last
word only**, a strong tell. The fix is to initialize `total = 0` **once, above** the loop, so
it accumulates across iterations.

**Diagnoses.** A learner who guesses "it only counts the last word" *after running it* is on
track; one who can't say *why* (the per-iteration reset) has the symptom, not the cause. A
hypothesis like "the loop doesn't add them up" is **too vague** (§5c) — the precise cause is the
init placement. A learner who "fixes" it by returning `sum(len(w) for w in words)` without
identifying the reset got a working fix but may have **skipped the hypothesis** (§5c, partial
pass) — ask them to name what was wrong with the original. Bug class: **accumulator
init/reset** (Catalog §5c; A1 mental model §3 — the transition rule across iterations).

---

## F3 — Wrong logical operator: `or` where `and` is meant

**Spec.** `is_valid_score(s)` returns `True` if and only if `0 <= s <= 100`.

```python
def is_valid_score(s):
    return s >= 0 or s <= 100

# observed: it calls everything valid
print(is_valid_score(50), is_valid_score(150), is_valid_score(-7))   # expected: True False False
```

> **Your turn:** Run it and observe the three results. What's your hypothesis for why nothing
> is ever rejected, what do you predict the fixed line prints, and what's the fix?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
buggy  -> stdout "True True True\n"    status ok
fixed  -> stdout "True False False\n"  status ok   (fix: `and` instead of `or`)
```

So the buggy version prints **`True True True`**; the fix prints **`True False False`**.

**Why.** With `or`, the result is `True` whenever **either** condition holds. Every real number
satisfies `s >= 0` **or** `s <= 100` (you'd have to be both below 0 *and* above 100 at once to
fail both — impossible), so the function is **always `True`**. The contract is a *conjunction*:
a score is valid only when it's `>= 0` **and** `<= 100`. The fix is `s >= 0 and s <= 100` (or
the chained `0 <= s <= 100`). The discriminating observation: `150` and `-7` — which violate
exactly one bound each — both return `True`, which is impossible under a correct AND.

**Diagnoses.** A learner who predicts the fix flips `150`/`-7` to `False` *and* explains that
`or` is satisfied by either operand has it. A hypothesis of "the comparison is wrong" is **too
vague** (§5c) — the operator, not the comparisons, is the fault. A learner who tries `and` but
**doesn't re-run to confirm** the three outputs has skipped the *Test* stage (§5c, "if you
didn't fix it…") — have them re-run. Bug class: **wrong logical operator** (Catalog §5c; ties
to A1 short-circuit/boolean semantics — `or` returns the first truthy operand).
