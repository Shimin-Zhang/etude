# A3 — Foundations exemplars (execution tracing)

Golden drills for the **Foundations** tier of module A3: trace **straight-line code or one
loop** with a running accumulator (2–3 variables) and predict the **final state / output**
by keeping a written state table — *one row per step, in execution order*. The skill at this
tier is the **intermediate trace**, not just the endpoint. Every answer key below was
obtained by **running the snippet through the runner** (`drill-generation.md` §2) — the
coach never guesses output:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Foundations parameter space: a swap-via-temp (variable *history*
matters), a loop tracking two accumulators (sum + max), and a loop building a string while
counting (state across iterations). Used for few-shot calibration, faded worked examples,
and offline fallback. Per `coaching-loop.md`, the coach poses one drill, then **hard-stops
and waits** — the answer key is for *grading*, never shown before the learner attempts.
**Grading mode: executable** (the trace/output is run, not guessed); the per-step table is
graded for the **row where it first diverges**.

---

## F1 — Swap via temp: a variable's *history* is part of the state

```python
a = 5
b = 3
temp = a
a = b
b = temp
print(a, b)
```

> **Your turn:** What does this print? (Trace `a`, `b`, and `temp` after each line.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "3 5\n"
status: ok
```

So the printed line is `3 5` — the values **are** swapped.

**The trace (one row per statement, the state *after* it):**

| Step | Statement | `a` | `b` | `temp` |
|---|---|---|---|---|
| 1 | `a = 5` | `5` | — | — |
| 2 | `b = 3` | `5` | `3` | — |
| 3 | `temp = a` | `5` | `3` | `5` |
| 4 | `a = b` | `3` | `3` | `5` |
| 5 | `b = temp` | `3` | `5` | `5` |

**Why.** `temp` **records the old value of `a` (`5`) before it is overwritten**. Line 4
rebinds `a` to `3` (the old `5` would be lost — but `temp` is holding it). Line 5 rebinds
`b` to `temp`'s `5`. The temp is the whole point: it preserves a *prior* value the swap
needs.

**Diagnoses.** A learner who only tracks each variable's *latest* value, without writing
`temp`'s row, often predicts `3 3` (they let `a = b` destroy the `5` with nothing holding
it) — that is **single-value tracing**: keeping one overwritten slot per name instead of
recording history. The fix is the written table above. (Catalog §5c — single-value tracing;
Vainio & Sajaniemi 2007.)

---

## F2 — One loop, two running accumulators (sum and max)

```python
total = 0
biggest = 0
for n in [3, 8, 2, 8, 5]:
    total = total + n
    if n > biggest:
        biggest = n
print(total, biggest)
```

> **Your turn:** What does this print? (Trace `total` **and** `biggest` across all five
> iterations.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "26 8\n"
status: ok
```

So the printed line is `26 8`.

**The trace (one row per iteration):**

| `n` | `total` after | `biggest` after |
|---|---|---|
| 3 | 3 | 3 |
| 8 | 11 | 8 |
| 2 | 13 | 8 |
| 8 | 21 | 8 (`8 > 8` is false — no change) |
| 5 | 26 | 8 |

**Why.** `total` carries its running value forward each pass (0 → 3 → 11 → 13 → 21 → 26).
`biggest` only updates when `n` *strictly exceeds* it — note the **second `8` does not
update it** (`8 > 8` is false), a detail a written trace catches and an in-head trace often
misses.

**Diagnoses.** A wrong `total` usually means the learner did not **carry state across
iterations** (added into a fresh 0, or dropped a term) — the lost-state gap. A `biggest`
that ends as `5` (the last `n`) reveals confusing "track the maximum" with "keep the latest"
— again single-value thinking. Both are fixed by the written per-row table. (Catalog §5c;
A3 mental model §3a — write the row, then move the counter.)

---

## F3 — Loop building a string while counting (two kinds of accumulator)

```python
s = ""
vowels = 0
for ch in "trace":
    if ch in "aeiou":
        vowels = vowels + 1
    else:
        s = s + ch
print(s, vowels)
```

> **Your turn:** What does this print? (Trace `s` and `vowels` letter by letter.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "trc 2\n"
status: ok
```

So the printed line is `trc 2`.

**The trace (one row per character of `"trace"`):**

| `ch` | vowel? | `s` after | `vowels` after |
|---|---|---|---|
| `t` | no | `"t"` | 0 |
| `r` | no | `"tr"` | 0 |
| `a` | yes | `"tr"` | 1 |
| `c` | no | `"trc"` | 1 |
| `e` | yes | `"trc"` | 2 |

**Why.** Each character takes **exactly one branch**: vowels (`a`, `e`) increment the counter
and leave `s` alone; consonants (`t`, `r`, `c`) append to `s` and leave the counter alone.
`s` accumulates `"trc"`; `vowels` accumulates `2`. The branch means the two accumulators
update on *disjoint* steps — visible immediately in the table.

**Diagnoses.** Predicting `"trace" 2` (the whole string in `s`) reveals not modeling the
`if/else` as **mutually exclusive** — the learner appended *every* char and *also* counted
vowels. Predicting `vowels = 0` or losing a character shows in-head state loss. The written
row-per-char trace is the fix. (Catalog §5c — losing state across iterations; A3 §3a.)
