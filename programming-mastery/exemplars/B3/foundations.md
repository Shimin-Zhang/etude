# B3 — Foundations exemplars (testing & correctness)

Golden drills for the **Foundations** tier of module B3. Each gives a function with an
*obvious* contract on a familiar surface and asks the learner to **enumerate the edge
cases it must handle** (graded against the gold list — judgment) or to name **which single
input makes it wrong** (graded by **running** that input through the runner — the coach
never guesses which input breaks it):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Foundations parameter space: boundary (`<` vs `<=`), the empty/degenerate
case, and one "which input breaks it" with a planted boundary bug. Grading is **mixed**
(`drill-generation.md` §1d): enumerate-cases is rubric/gold; "which input breaks it" is
executable. Per `coaching-loop.md`, the coach poses one drill, then **hard-stops and
waits** — the gold list / answer key is for *grading*, never shown before the learner
attempts.

---

## F1 — Enumerate the edge cases (closed-interval membership)

```python
def in_range(x, lo, hi):
    """True iff x lies in the CLOSED interval [lo, hi] — both ends included.
    Precondition: lo <= hi."""
    return lo <= x <= hi
```

> **Your turn:** What cases would you test? List them — and for **each**, say what
> behavior or boundary it checks.
>
> (Take your best guess — wrong attempts are useful data.)

**Gold case list (rubric grading — `drill-generation.md` §3)**

A strong answer is **organized by equivalence class and boundary**, not a flat list of
arbitrary numbers. It must cover the three behavior classes **and** both boundaries:

| Case | Class / boundary | Expected |
|---|---|---|
| `in_range(5, 0, 10)` | inside (typical) | `True` |
| `in_range(-3, 0, 10)` | below `lo` | `False` |
| `in_range(99, 0, 10)` | above `hi` | `False` |
| `in_range(0, 0, 10)` | **boundary** `x == lo` | `True` |
| `in_range(10, 0, 10)` | **boundary** `x == hi` | `True` |
| `in_range(11, 0, 10)` | just above `hi` | `False` |
| `in_range(5, 5, 5)` | **degenerate** `lo == hi`, `x` on it | `True` |
| `in_range(4, 5, 5)` | degenerate, `x` just below | `False` |

(All eight expected values runner-verified.) A *bonus* answer raises the **contract
question**: what should happen when `lo > hi` (precondition violated)? The contract is
silent; naming that gap is Advanced-flavored.

**Rubric (binary, score each):** (a) covers all **three classes** (below / inside / above)?
(b) tests **both boundaries** `x == lo` *and* `x == hi`? (c) includes the **degenerate**
`lo == hi`? (d) organized **by class/boundary**, not arbitrary values?

**Diagnoses.** A list of only interior values (`3, 5, 7`) with no boundary is the
**happy-path / confirmation-testing** signature — the learner samples the comfortable
middle and misses the `<`/`<=` edge where bugs live. Hitting `x == lo` but not `x == hi`
is partial boundary coverage. (Catalog §5c, entries 1 & 3; Myers 1979 boundary-value
analysis; A1 transfer caveat — this is a judgment call, not a machine verdict.)

---

## F2 — Which single input makes this wrong? (planted boundary bug)

```python
def running_max(xs):
    """Return a list where out[i] == max(xs[:i+1]) — the max seen so far at each step."""
    out = []
    m = xs[0]
    for x in xs:
        out.append(m)        # records the max-so-far BEFORE considering the current element
        if x > m:
            m = x
    return out
```

> **Your turn:** This passes on some inputs and is wrong on others. Give **one** input
> that makes it produce the wrong result — and say what the right answer is.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

A discriminating input is any list where a **later element is a new maximum** (so the lag
shows). For `xs = [1, 3, 2]`:

```
# buggy running_max([1, 3, 2]):
stdout: "[1, 1, 3]\n"     # status: ok  — but WRONG
# contract (reference max(xs[:i+1])):
[1, 3, 3]
```

So `running_max([1, 3, 2])` returns `[1, 1, 3]`; the contract requires `[1, 3, 3]`. The
new max `3` shows up **one position too late** because the append happens *before* the
update.

**Why this input.** A *non-increasing* or front-loaded input does **not** discriminate:
`running_max([3, 1, 2])` gives `[3, 3, 3]` under both the buggy and a correct
implementation (runner-verified) — the bug is invisible there. The learner must pick an
input where the maximum *changes after the first element*. Naming `[3, 1, 2]` (a
non-discriminating happy-path input) is the error to catch.

**Diagnoses.** A learner who says "it looks right" or offers a front-loaded input that
hides the bug has the **happy-path** reflex (Catalog §5c, entry 1). The coach grades by
**running the named input** — if the learner's input does not actually produce a wrong
result, that itself is the teaching moment: a breaking input must *break* it. (Mirrors the
`assessment.md` C1 `running_max` example, here pointed at *test-input selection* rather
than hypothesis-forming.)

---

## F3 — Which single input makes this wrong? (the empty case)

```python
def average(xs):
    """Return the arithmetic mean of the numbers in xs."""
    return sum(xs) / len(xs)
```

> **Your turn:** Give **one** input on which this function fails (raises or misbehaves),
> and say what happens.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

The breaking input is the **empty list**, `xs = []`:

```
# average([]):
status: error
stderr: "... ZeroDivisionError: division by zero"
```

`len([]) == 0`, so `sum([]) / len([])` is `0 / 0` → `ZeroDivisionError`. The function has
no precondition guard and no defined behavior for the empty input.

**Why this input.** Every *non-empty* list works fine, so happy-path testing
(`average([1, 2, 3]) == 2.0`) never reveals it. The empty collection is its **own
equivalence class** — `{empty}` vs `{non-empty}` — and the single most commonly missed
boundary. A single element (`average([4]) == 4.0`) is fine; the cliff is at zero elements.

**Diagnoses.** A learner who only proposes non-empty inputs has not partitioned the input
domain to include the **degenerate empty case** (Catalog §5c, entry 3). The graded signal:
the coach **runs** `average([])` and confirms `status: error`. The fix is also a *contract*
decision — should empty raise a clear error, return `0`, or return `None`? — which previews
the Working-tier "state the contract" drill. (Myers 1979 equivalence partitioning;
Dijkstra — passing on non-empty inputs never shows the absence of the empty-input bug.)
