# F1 — Advanced exemplars (metacognition & calibration)

Golden drills for the **Advanced** tier of module F1: calibrate on **genuinely tricky** code
(closures / aliasing / eval-order) **and** handle the AI-era keystone scenario — **"an AI
wrote this function; what would you verify before trusting it, and how confident are you it's
correct?"** The first two are runner-verified predict+confidence drills on hard code; the
third (**A3**) is a **gold rubric + answer** for the AI-trust judgment (its prediction half is
still pinned to real runner output).

Executable parts obtained by **running through the runner** (`drill-generation.md` §2);
calibration is measured against **real** output, never assertion:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Pose one, **hard-stop, wait** (`coaching-loop.md`). At Advanced the coach reveals only the
`(confidence, correct?)` pairs and asks the learner to state the calibration verdict, name
the costliest miss, and explain *why* the confidence was unearned (teach-it-back). Two of
these turn on `status` / side effects, not just `stdout`.

---

## A1 — Calibrate on a genuine trap: late-binding closure in a comprehension

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
```

> **Your turn:** First — how confident are you (0–100%) you'll get this exactly right? Then:
> what does it print?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[2, 2, 2]\n"
status: ok
```

So the printed line is `[2, 2, 2]` — **not** `[0, 1, 2]`.

**Why (the answer).** All three lambdas close over the **same variable `i`**, not a
per-iteration snapshot. A closure reads its captured variable **when called**, not when
defined. By the time `[f() for f in funcs]` calls them, the comprehension that built `funcs`
has finished and `i` is at its final value `2`. So every call returns `2` → `[2, 2, 2]`.
(In Python 3 the comprehension variable does **not** leak to the enclosing scope, but it is
still shared by all the closures *within* the comprehension's frame.)

**How to score the calibration.** This is the **deliberately seductive** case: `[0, 1, 2]`
*feels* obviously right, so it draws high confidence — and it's wrong. The Advanced lesson is
that on **genuinely tricky** code, "obvious" is precisely the warning sign. A learner who
rated this **90%+ and predicted `[0, 1, 2]`** is overconfident on a known trap; the
*calibrated* expert response is **lower confidence with a named doubt** — "I think `[0,1,2]`
but I'm only ~50%, because closures-in-loops capture the variable, and I'd **run it** before
trusting that." Reward the **explicit pre-reveal flag of the exact mechanism** even when the
final answer is wrong (Flavell 1979, monitoring).

**Diagnoses.** Confident `[0, 1, 2]` → fluency trap on hard code + late-binding-closure model
gap. The teach-it-back probe ("why did `[0,1,2]` feel so right?") surfaces whether the learner
now *understands* the miscalibration or just memorized the answer. (Catalog §5c; module §3.)

---

## A2 — Calibrate on combined mechanisms: mutable default accumulates across calls

```python
def f(a, b=[]):
    b.append(a)
    return sum(b)

print(f(1), f(2), f(3))
```

> **Your turn:** Rate your confidence (0–100%) first. Then: what does this print?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "1 3 6\n"
status: ok
```

So the printed line is `1 3 6` — **not** `1 2 3`.

**Why (the answer).** The default `b=[]` is evaluated **once at definition time** and that
**one** list lives on the function object (`f.__defaults__`). Each call that omits `b`
appends to the **same shared list**: `f(1)` → `[1]`, `sum` = `1`; `f(2)` → `[1, 2]`, `sum` =
`3`; `f(3)` → `[1, 2, 3]`, `sum` = `6`. The accumulation across calls is the surprise.
(Also note: `print(f(1), f(2), f(3))` evaluates its arguments **left to right** before
printing, so the calls happen in order — an eval-order point folded in.)

**How to score the calibration.** Two mechanisms interact (mutable-default + the running
`sum`), so this is a legitimate Advanced item. The calibration read is the same shape: a
confident `1 2 3` is the overconfident miss; the calibrated answer attaches a **lower number
and a named suspicion** ("`b=[]` as a default is a classic gotcha — I'd verify it persists").
The expert habit being trained is **letting a known-tricky construct *lower* the confidence
automatically** — confidence that *responds* to difficulty (the cure for the hard–easy
effect, Lichtenstein & Fischhoff 1977).

**Diagnoses.** Confident `1 2 3` → "defaults re-initialized each call" model + overconfidence.
A learner who flags "mutable default — not sure it resets" and rates ~50% is **well-calibrated
even if wrong**. (Catalog §5c.)

---

## A3 — The AI-trust scenario (GOLD RUBRIC): "an assistant wrote this — would you trust it?"

> **An assistant produced this function. It was asked for: *"return the median of a list of
> numbers."***
>
> ```python
> def median(xs):
>     xs.sort()
>     n = len(xs)
>     mid = n // 2
>     if n % 2 == 1:
>         return xs[mid]
>     return (xs[mid - 1] + xs[mid]) / 2
> ```
>
> **Your turn:** *Before* you trust it — (1) how confident are you (0–100%) that it is
> **correct**? (2) What are the **first things you would verify**, in priority order, and
> *why those*? (3) After you've named your checks, predict what each reveals.
>
> (Take your best guess — wrong attempts are useful data.)

This drill is **judgment-graded against the rubric below** (`drill-generation.md` §3), with
the **prediction half pinned to real runner output**. The coach states: *"this is a judgment
call graded against the F1 rubric, not a single machine-verifiable answer — but I will run
your checks."*

**Runner-verified ground truth** (so the learner's verification predictions are scored
against reality). Running the function on a battery:

```python
data = [3, 1, 2]
print(median(data))        # -> 2      (odd-length: correct value)
print(data)                # -> [1, 2, 3]   *** mutated the caller's list! ***
print(median([4, 1, 3, 2]))# -> 2.5    (even-length: correct value)
print(median([]))          # -> IndexError: list index out of range
```

```
stdout: "2\n[1, 2, 3]\n2.5\n"
status: error
stderr (last line): IndexError: list index out of range
```

So the function **computes the right median value** on non-empty input **but has two real
defects**: it **mutates the caller's list in place** (`xs.sort()` sorts the argument, a
surprising side effect), and it **crashes on empty input** (`xs[mid - 1]` / `xs[mid]` on
`n == 0`).

**Gold answer (what a well-calibrated reviewer produces).**

- **Calibrated trust, not a vibe.** *"~50–60% it's correct as-specified — the median *math*
  looks right for both parities, but I haven't checked edge cases or side effects, and 'looks
  right' isn't a check. My confidence is **conditional on running it**, and here's exactly
  what would move the number."* (Trust is **tied to evidence that could change it** — Nelson &
  Narens 1990; the AI-era output-evaluation demand, Tankelevitch 2024.)
- **Prioritized verification plan** (highest-value-first):
  1. **Empty input `[]`** — the classic boundary; `mid - 1` indexing screams "what at length
     0/1?" → **predict it raises** (it does: `IndexError`). *Highest priority: most likely to
     break, cheapest to test.*
  2. **Side effects on the argument** — `xs.sort()` mutates in place; does the caller expect
     their list reordered? → **predict the caller's list is mutated** (it is). *A silent
     correctness-of-contract bug even when the return value is right.*
  3. **Single element `[7]`** — boundary for the odd branch → predict `7` (correct).
  4. **Even vs. odd length** with known answers (`[1,2,3]`→2, `[1,2,3,4]`→2.5) → confirm the
     averaging branch.
  5. **Unsorted input** — is sorting actually needed/done? (it is — and that's the source of
     the mutation defect).
- **The calibration point.** The function's **plausibility is exactly the trap**: it returns
  correct values on the obvious cases, so an overconfident reviewer rates it 90% and ships
  the `[]` crash and the mutation bug. The skill is letting **"AI-written + unverified"** cap
  the confidence until the checks run — *not* letting fluency ("it looks like what I'd write")
  stand in for verification (Fernandes 2025: more AI-literate → *more* overconfident; the
  keystone failure).

**Rubric (binary criteria; the coach grades each explicitly, cites the closest exemplar).**

| # | Criterion | Pass = |
|---|---|---|
| 1 | **Calibrated trust number** | Gives a confidence that is **not flat-high** (not 90%+ "looks right") and **conditions it on verification** rather than on plausibility. |
| 2 | **Names the empty-input boundary** | Identifies `[]` (and ideally single-element) as a thing to check, and **predicts a crash/edge failure** there. |
| 3 | **Catches the side effect** | Notes `xs.sort()` **mutates the caller's argument** — a contract bug independent of the return value. |
| 4 | **Prioritizes** | Orders checks by value (boundaries/side-effects first), not a flat or random list — and does **not** drown the real issues under cosmetic nits. |
| 5 | **Ties confidence to evidence** | Can state **what specific check would most move** the trust number (i.e., trust is updatable, not a vibe). |

**Scoring.**
- **Advanced pass:** criteria **1, 2, 3, and 5** met, with **4** (prioritization) at least
  partially — the reviewer is *calibrated* (trust tied to checks) **and** catches both real
  defects through a verification-first stance. Closest to the gold answer above.
- **Working-level (partial):** catches the empty-input crash *or* the mutation but **rates
  the function 90%+ anyway** — found a bug but stayed overconfident; trust not updated. Or
  produces a fine check-list but with a flat-high trust number (criterion 1 fails).
- **Foundations-level / miscalibrated:** *"looks correct, ~90%, I'd maybe test a couple of
  inputs"* with **no** boundary, **no** side-effect, and trust driven by plausibility — the
  **keystone AI-era failure** (catalog §5c, plausibility-as-correctness). Name it bluntly and
  route to the AI-trust drilling.

**Diagnoses.** High trust + "looks right" + no named check → plausibility-as-correctness
(trust-by-fluency on code-not-written). Found-the-bug-but-still-90% → broken adjustment
(monitoring without control, Nelson & Narens 1990). Un-anchored trust ("50/50, dunno") with
no evidence that would move it → un-updatable trust. The gold behavior — **verify-then-trust,
with confidence conditioned on the checks** — is the exact skill the AI era demands
(`evidence-base.md` → AI-era impact; spec §12).
