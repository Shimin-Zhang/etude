# B2 — Foundations exemplars (code writing & composition)

Golden drills for the **Foundations** tier of module B2: write a function for a spec with a
**single, clear behavior** on a familiar surface, built in at least one **confirmed step**
(not a guess pasted whole), passing the **happy-path battery**. Each drill is graded **two
ways, reported separately** (`drill-generation.md` §1d; B2 §5d):

- **Product (executable):** the coach **runs the learner's function** against the battery
  below — every expected value here was obtained by running a reference solution, the coach
  never guesses:

  ```
  python <skill-dir>/runtime/python/runner.py snippet.py
  ```

- **Process (rubric, softer):** did the learner state the spec, write the smallest runnable
  piece and **confirm it before extending**, and stop at the contract?

Coverage spans distinct parameter-space points — **numeric scalar** (clamp) / **list → int
count** (count_evens) / **string → string** (initials) — no repeated surface. Per
`coaching-loop.md`, pose one drill, then **hard-stop and wait**; the battery and gold are for
*grading*, never shown before the learner attempts.

---

## FF1 — `clamp(x, lo, hi)` (numeric scalar; the boundary surface)

> **Your turn:** Write `clamp(x, lo, hi)` — return `x` unchanged if it lies in `[lo, hi]`;
> if `x` is below `lo` return `lo`; if above `hi` return `hi`. (Assume `lo <= hi`.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery** (the grading key — coach runs the learner's `clamp` on these):

```
clamp(5, 0, 10)   = 5     # inside (typical)
clamp(-3, 0, 10)  = 0     # below lo -> lo
clamp(99, 0, 10)  = 10    # above hi -> hi
clamp(0, 0, 10)   = 0     # boundary x == lo
clamp(10, 0, 10)  = 10    # boundary x == hi
status: ok
```

**Gold reference solution:**

```python
def clamp(x, lo, hi):
    if x < lo:
        return lo
    if x > hi:
        return hi
    return x
```

**Why.** The whole behavior is three cases. Running the **boundary** inputs (`clamp(0, 0,
10)`, `clamp(10, 0, 10)`) confirms an in-range value on a bound comes back **unchanged** —
though note clamp is *robust* to a `<` vs `<=` slip here, since when `x == lo` the function
returns `lo == x` either way (runner-confirmed: a `<=`/`>=` version still gives
`clamp(0,0,10) == 0` and `clamp(10,0,10) == 10`). The bug a confirmed step **actually**
catches is a **wrong comparison direction**: `if x > lo: return lo` makes `clamp(5, 0, 10)`
return `0`, not `5` — so predicting-then-running the *typical* case (predict `5`, see `5`)
catches the most common clamp slip immediately.

**Diagnoses.** A learner who writes the comparison in the **wrong direction** (`x > lo` / `x
< hi`) returns the bound for in-range inputs — runner-confirmed: such a version gives
`clamp(5,0,10) == 0` when the spec wants `5` — a **comparison-direction construction error**
caught by the predict-then-run step on the typical case (Catalog §5c — boundary/comparison
error). A learner who writes all three branches in one block and runs nothing until the end
shows the **big-bang** habit even on easy code — the fix is to confirm the typical case first,
then the bounds.

---

## FF2 — `count_evens(xs)` (list → int; the empty case is gentle here)

> **Your turn:** Write `count_evens(xs)` — return how many numbers in the list `xs` are even.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
count_evens([1, 2, 3, 4, 5, 6]) = 3    # typical
count_evens([])                 = 0    # empty -> 0 (falls out naturally)
count_evens([1, 3, 5])          = 0    # all odd
count_evens([0])                = 1    # 0 IS even
count_evens([-2, -4])           = 2    # negatives are even too
status: ok
```

**Gold reference solution:**

```python
def count_evens(xs):
    c = 0
    for x in xs:
        if x % 2 == 0:
            c += 1
    return c
```

**Why.** This is the **accumulator composition** — initialize, update inside the loop, return.
The edges here are *gentle*: the empty list returns `0` for free (the loop body never runs),
which is why this is Foundations, not Working. But two real cases catch a hasty writer:
**`0` is even** (`0 % 2 == 0`) and **negative evens count** (`-2 % 2 == 0` in Python). Running
`count_evens([0])` and `count_evens([-2, -4])` confirms the `% 2 == 0` test, rather than an
`x > 0 and x % 2 == 0` over-restriction.

**Diagnoses.** A learner who writes `if x % 2 == 0 and x > 0` has **over-engineered past the
spec** (excluding `0` and negatives the spec never excluded — Catalog §5c, over-engineering).
A learner who initializes `c` *inside* the loop, resetting it each pass, has the **losing-state**
construction bug (runner-confirmed: such a version returns `1` on `[1,2,3,4,5,6]` — only the last
element's contribution survives); the per-step confirm — run on `[1,2,3,4,5,6]`, expect `3` —
surfaces it immediately.

---

## FF3 — `initials(full_name)` (string → string; compose split → first-char → join)

> **Your turn:** Write `initials(full_name)` — return the uppercase initials of a name, e.g.
> `initials("ada lovelace")` → `"AL"`. Names are separated by spaces.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
initials("ada lovelace")        = "AL"    # typical
initials("grace hopper")        = "GH"
initials("  ada   lovelace  ")  = "AL"    # extra/leading/trailing spaces
initials("plato")               = "P"     # single name
initials("")                    = ""      # empty string -> empty
status: ok
```

**Gold reference solution:**

```python
def initials(full_name):
    parts = full_name.split()                      # split() collapses runs of whitespace
    return "".join(p[0].upper() for p in parts)
```

**Why.** The composition is three pieces — **split into words → take each first char → join**.
The verified-steps payoff is the **whitespace edge**: the gold uses `full_name.split()` (no
argument), which collapses runs of whitespace and drops empties. The naive `full_name.split(" ")`
(splitting on a single literal space) turns `"  ada   lovelace  "` into a list with **empty
strings**, and `p[0]` on `""` raises:

```
# initials_naive("  ada   lovelace  ")  using split(" ")
status: error    # IndexError: string index out of range
```

A learner who composes in confirmed steps runs the *extra-spaces* input early and either sees
the `IndexError` (with `split(" ")`) or the clean `"AL"` (with `split()`) — they do not ship the
crash.

**Diagnoses.** A learner who uses `split(" ")` and runs only `initials("ada lovelace")` has the
**happy-path-only** habit (Catalog §5c, entry 2): the typical input hides the whitespace edge,
and the crash surfaces only on messy real input. The fix is to **name the whitespace edge in the
spec step** and run it before declaring done. (Foundations-gentle: the coach may accept a working
`split(" ")` here *if* the learner names the whitespace risk — the edge is the teaching moment,
not a hard fail at this tier.)
