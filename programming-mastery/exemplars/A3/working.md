# A3 — Working exemplars (execution tracing & explain-in-plain-English)

Golden drills for the **Working** tier of module A3: trace a **function with calls** →
produce the **call tree** (arguments + returns) **and** the output; **and/or** "explain this
~10-line function in **one sentence**" at the *purpose* level. Trace/output keys were
obtained by **running the snippet through the runner** (`drill-generation.md` §2); the coach
never guesses. The explain-in-plain-English drill is **rubric-graded** against a **gold
one-sentence answer** plus the relational/multistructural rubric — and the underlying code
was **run** to confirm the gold is accurate:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct regions of the parameter space (call tree on pure functions /
EiPE-purpose / call inside a loop — no repeated structure). Pose one, **hard-stop, wait**
(`coaching-loop.md`). W1 and W3 are **hybrid** (output executable-graded, any explanation
rubric-graded); W2 is the pure **explain-in-plain-English** drill.

---

## W1 — Trace a function with calls: the call tree

```python
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))
```

> **Your turn:** Draw the **call tree** — every call with its argument and what it returns —
> then give the output.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "25\n"
status: ok
```

So the printed line is `25`.

**The call tree (each call, its argument, its return):**

```
sum_of_squares(3, 4)
├─ square(3) → 9
├─ square(4) → 16
└─ returns 9 + 16 = 25
```

**Why.** `sum_of_squares(3, 4)` does **not** compute anything itself until its two
sub-calls finish. `square(3)` runs to completion and hands back `9`; `square(4)` runs and
hands back `16`; *then* the `+` runs on the two returned values → `25`. Each call is its own
sub-computation with its own local `n` (one frame at a time), and the caller waits for the
return before proceeding.

**Diagnoses.** A learner who guesses `square`'s result from its name without tracing into it,
or who mis-orders (tries to add before both calls return), has **no call/return model in the
trace** — treating a call as an inline lookup rather than a sub-computation that must finish
and return first. Drawing the tree, with each node's argument and return, is the fix.
(Catalog §5c — skipping into the call / call-return mis-ordering; Sirkiä & Sorva 2012.)

---

## W2 — Explain in plain English: name the *purpose*, in one sentence

```python
def mystery(items):
    seen = []
    for x in items:
        if x not in seen:
            seen.append(x)
    return seen

print(mystery([3, 1, 3, 2, 1, 3]))
```

> **Your turn:** In **one sentence**, explain the **purpose** of `mystery` — what it would be
> *used for*. (Do not say how it works line by line; say what job it does.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified behavior** (run to confirm the gold is accurate — this drill is
rubric-graded, but the *purpose* must match real behavior):

```
stdout: "[3, 1, 2]\n"
status: ok
```

So `mystery([3, 1, 3, 2, 1, 3])` returns `[3, 1, 2]` — duplicates dropped, and the survivors
appear in the order of their **first** occurrence (`3` before `1` before `2`).

**Gold one-sentence answer (relational):**

> **"It removes duplicate elements from a list while preserving the order of first
> occurrence."**

**Rubric** (`drill-generation.md` §3; A3 §5d) — three binary criteria:

1. **Relational, not multistructural** — names the *purpose* ("removes duplicates, keeping
   order"), not a line-by-line retelling. **PASS** for the gold.
2. **Accurate** — matches the run: duplicates removed, first-occurrence order kept (confirmed
   `[3, 1, 2]`). A sentence that says "sorts the list" or "removes duplicates" *without* the
   order property is **partially inaccurate** (the order is a real, testable behavior).
3. **Appropriately concise** — one sentence a teammate could act on without the code. **PASS.**

**Acceptable variants** (all relational + accurate): "Returns the unique items in first-seen
order," "De-duplicates a list, keeping the earliest copy of each value."

**Weak / failing answers and what they diagnose:**

- *"It makes an empty list `seen`, then loops over `items`, and for each `x` checks if `x` is
  not in `seen`, and if so appends it, then returns `seen`."* → **Multistructural**: a true
  line-by-line retelling that never states the *job*. This is the novice signature on EiPE
  tasks. (Catalog §5c — line-by-line explanation; Whalley et al. 2006; Lister et al. 2006.)
- *"It keeps a list of things it has seen."* → describes a *mechanism*, not the purpose;
  fails to name "removes duplicates."
- *"It filters the list"* → too vague; a teammate cannot reconstruct the dedup-with-order
  job from it.

---

## W3 — Trace a call *inside a loop*: call tree + accumulated output

```python
def tax(price):
    return price * 0.1

def total(cart):
    running = 0
    for price in cart:
        running = running + price + tax(price)
    return running

print(total([100, 50, 30]))
```

> **Your turn:** Draw the call tree (each `tax` call + its return) and trace `running` across
> the loop, then give the output.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "198.0\n"
status: ok
```

So the printed line is `198.0` (a float — `* 0.1` produces a float).

**The call tree + `running` trace:**

```
total([100, 50, 30])
├─ price=100: tax(100) → 10.0 ; running = 0 + 100 + 10.0   = 110.0
├─ price=50 : tax(50)  → 5.0  ; running = 110.0 + 50 + 5.0  = 165.0
├─ price=30 : tax(30)  → 3.0  ; running = 165.0 + 30 + 3.0  = 198.0
└─ returns 198.0
```

**Why.** Each loop pass makes its **own** `tax(price)` call, which runs to completion and
returns a value *before* the addition on that row happens. `running` carries its value
forward across iterations (0 → 110.0 → 165.0 → 198.0). The result is a **float** because
`price * 0.1` is float arithmetic — a detail the run pins down (`198.0`, not `198`).

**Diagnoses.** Predicting `198` (an int) misses that `* 0.1` yields a float — run it to see
`198.0`. A wrong total usually means **losing `running` across iterations** (resetting it, or
dropping a `tax` term), or **not tracing into `tax`** and guessing its return. The combined
call-tree-plus-accumulator trace is the fix; this is the Working-tier merge of "trace the
calls" and "carry the loop state." (Catalog §5c — losing state across iterations + skipping
into the call.)
