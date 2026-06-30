# A1 — Foundations exemplars (notional machine)

Golden drills for the **Foundations** tier of module A1. Each is a single-mechanism
snippet on a familiar surface: predict the **final value(s) / output** by simulating the
machine. Every answer key below was obtained by **running the snippet through the
runner** (`drill-generation.md` §2) — the coach never guesses output:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Foundations parameter space: straight-line rebinding, sequential
reassignment (no parallelism), and one loop with running accumulators. Used for
few-shot calibration, faded worked examples, and offline fallback. Per
`coaching-loop.md`, the coach poses one drill, then **hard-stops and waits** — the
answer key is for *grading*, never shown before the learner attempts.

---

## F1 — Rebinding is not a link between names

```python
x = 10
y = x
x = x + 1
print(x, y)
```

> **Your turn:** What does this print?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "11 10\n"
status: ok
```

So the printed line is `11 10`.

**Why.** `y = x` binds the name `y` to the *current value* of `x` (the int `10`) at that
instant — it does not create a persistent link. Line 3 **rebinds** `x` to a new int `11`;
`y` is untouched and still labels `10`. Two independent labels after the assignment.

**Diagnoses.** A prediction of `11 11` reveals a **copy-on-assign / "linked names"
model** — the learner believes `y = x` keeps `y` in sync with `x`, instead of the
name-binding model where rebinding one name leaves the other alone. (Catalog §5c, entry
1; du Boulay 1986.)

---

## F2 — One loop, two running accumulators

```python
total = 0
count = 0
for n in [4, 7, 2, 9]:
    total = total + n
    count = count + 1
print(total, count)
```

> **Your turn:** What does this print? (Trace `total` and `count` across all four
> iterations.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "22 4\n"
status: ok
```

So the printed line is `22 4`.

**Why.** Walk the state, one row per iteration. `total`: 0 → 4 → 11 → 13 → 22.
`count`: 0 → 1 → 2 → 3 → 4. Each `= ... + ...` is a **rebind** to a fresh int; the list
`[4, 7, 2, 9]` is only read, never mutated; `n` is rebound each pass.

**Diagnoses.** A wrong `total` usually means the learner did not **carry state across
iterations** (added into a fresh 0 each time, or lost a term) — the "cannot trace code
linearly" gap (Kaczmarczyk et al. 2010). Reporting `4` for `count` but a wrong `total`
shows partial state-tracking. (Catalog §5c; A1 mental model §3 — the transition rule.)

---

## F3 — Statements run one at a time, top to bottom (the failed swap)

```python
a = 3
b = 5
a = b
b = a
print(a, b)
```

> **Your turn:** What does this print? (Many people expect a swap — does it swap?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "5 5\n"
status: ok
```

So the printed line is `5 5` — **not** `5 3`. It does **not** swap.

**Why.** Execution is sequential, one statement at a time. `a = b` rebinds `a` to `5`
(overwriting the old `3` — it is gone). The very next statement `b = a` reads the **new**
`a` (`5`), so `b` is rebound to `5`. There is no hidden temporary holding the old `a`; a
real swap needs `a, b = b, a` (right-hand side fully built first) or an explicit temp.

**Diagnoses.** A prediction of `5 3` reveals the **simultaneous-execution / parallelism
misconception** — the learner imagines both assignments happen "together" off the
original values, instead of one-at-a-time top-to-bottom where the first assignment's
result feeds the second. (Pea 1986, the parallelism bug; A1 mental model §3 — the
program counter.)
