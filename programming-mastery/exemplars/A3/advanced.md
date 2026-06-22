# A3 — Advanced exemplars (execution tracing & explain-in-plain-English)

Golden drills for the **Advanced** tier of module A3: trace **recursion or a generator** →
produce the **call/stack push-return sequence** or the **yield sequence (with resume
point)** **and** the output; **and/or** explain a **dense** function's intent in one
sentence. Trace/output keys were obtained by **running the snippet through the runner**
(`drill-generation.md` §2) — including *instrumented* runs (printing each push/return) to
confirm the intermediate sequence, not just the endpoint. The explain drill is
**rubric-graded** against a gold sentence, with the underlying code **run** to confirm
accuracy:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct structures (linear recursion / generator with interleaved
consumption / dense comprehension). Pose one, **hard-stop, wait** (`coaching-loop.md`). All
three demand **product *and* process** — the correct sequence *and* an explanation of *why*
(why each frame keeps its own locals; why a generator resumes rather than restarts; what the
dense expression is *for*).

---

## A1 — Recursion: the stack pushes down, returns combine on the way up

```python
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(4821))
```

> **Your turn:** Write the **push sequence** down to the base case and the **return values**
> coming back up, then give the output. *Why* doesn't an inner call clobber the outer call's
> `n`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "15\n"
status: ok
```

So the printed line is `15`.

**The stack over time (push down, then unwind — confirmed by an instrumented run):**

```
push   digit_sum(4821)   n%10 = 1, waits on digit_sum(482)
push     digit_sum(482)  n%10 = 2, waits on digit_sum(48)
push       digit_sum(48) n%10 = 8, waits on digit_sum(4)
push         digit_sum(4)   4 < 10  → returns 4        (base case)
return     digit_sum(48)  = 8 + 4  = 12
return   digit_sum(482)   = 2 + 12 = 14
return digit_sum(4821)    = 1 + 14 = 15
```

**Why.** Each call **pushes its own frame** with a **private `n`** (4821, then 482, 48, 4);
the caller's frame is *suspended*, not overwritten, waiting for the value from below. The
base case `digit_sum(4)` returns `4`; then frames **pop and unwind**, each adding its private
`n % 10` to what the frame below returned: `12`, `14`, `15`. The per-frame `n` is exactly why
`digit_sum(48)`'s `n` (48) is untouched while `digit_sum(4)` runs — they are different frames
with different locals.

**Diagnoses.** A learner who computes one running value (mutating a single `n`), or who
cannot say why the inner call doesn't clobber the outer `n`, has **no stack-of-frames model**
— assumes one shared set of locals across calls. The same gap predicts surprise at
`RecursionError` for unbounded recursion (Python keeps real frames, no tail-call
optimization). Writing the push-down / return-up sequence is the fix. (Catalog §5c — skips
the stack; Sirkiä & Sorva 2012; A1 §3 call stack.)

---

## A2 — Generator: a suspended frame that *resumes*, not restarts

```python
def countdown(n):
    while n > 0:
        yield n
        n = n - 1

g = countdown(3)
print(next(g))
print(next(g))
for x in g:
    print(x)
```

> **Your turn:** What is the full output? Track **where execution pauses** after each
> `next()` and what `n` is when the `for` loop takes over.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "3\n2\n1\n"
status: ok
```

So the output is `3`, then `2`, then `1` — each on its own line.

**The yield sequence (with resume point):**

| Action | Runs until… | Yields | Frozen state (`n`) |
|---|---|---|---|
| `g = countdown(3)` | *(nothing yet — frame created, suspended at top)* | — | `n = 3`, paused before loop |
| `next(g)` | first `yield n` | **3** | paused *after* `yield`, `n` still `3` |
| `next(g)` | `n = n - 1` (→ 2), loop, `yield n` | **2** | paused after `yield`, `n = 2` |
| `for x in g` → 1st | `n = n - 1` (→ 1), loop, `yield n` | **1** | paused after `yield`, `n = 1` |
| `for x in g` → 2nd | `n = n - 1` (→ 0), `while 0 > 0` false → **StopIteration** | — | exhausted; loop ends |

**Why.** A generator is a **suspended frame**, not an eager list and not a function restarted
each call. Each `next()` runs from where it last paused **until the next `yield`**, emits that
value, and **freezes with its locals intact** — `n` persists across calls. The `for` loop
simply keeps calling `next()` from the *same* paused point: it does **not** restart the
countdown, so it picks up at `1` (not back at `3`), then stops on `StopIteration`. The whole
output is `3 2 1`, each printed once.

**Diagnoses.** Predicting `3 3 2 1` or `3 2 3 2 1` (the `for` restarting from the top) reveals
the **"generator restarts / is a re-iterable list" model**. Predicting the `for` prints
nothing reveals not knowing state persists across `next()`. Both miss the **suspended-frame /
resume-point** model. (Catalog §5c — generator resume confusion; A1 §5c generators; generator
data model.)

---

## A3 — Explain a *dense* function in one sentence

```python
def f(xs):
    return [x for i, x in enumerate(xs) if x not in xs[:i]]

print(f([4, 4, 2, 7, 2, 4, 9]))
```

> **Your turn:** In **one sentence**, explain the **purpose** of `f` — what it would be *used
> for*. (Trace it first if you need to; then say the job, not the mechanics.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified behavior** (run to confirm the gold — this drill is rubric-graded, but the
*purpose* must match real behavior):

```
stdout: "[4, 2, 7, 9]\n"
status: ok
```

So `f([4, 4, 2, 7, 2, 4, 9])` returns `[4, 2, 7, 9]` — each value kept only at its **first**
appearance, in original order.

**What the trace reveals** (needed to *find* the purpose under the dense syntax): for each
element, `xs[:i]` is "everything **before** position `i`"; `x not in xs[:i]` is true only the
**first** time `x` appears. So the comprehension keeps each value's first occurrence and drops
later repeats: position 0 `4` (none before → keep), position 1 `4` (`4` is before → drop),
`2` keep, `7` keep, `2` drop, `4` drop, `9` keep → `[4, 2, 7, 9]`.

**Gold one-sentence answer (relational):**

> **"It removes duplicate elements from a list, keeping each value's first occurrence and the
> original order."**

**Rubric** (`drill-generation.md` §3; A3 §5d):

1. **Relational, not multistructural** — states the *job* (dedup, order-preserving), not "it
   enumerates `xs`, and for each `i, x` checks `x not in xs[:i]`…". **PASS** for the gold.
2. **Accurate** — matches the run `[4, 2, 7, 9]`: first occurrences kept, order preserved. A
   sentence omitting the order property is partially inaccurate; "removes duplicates" alone is
   close but under-specifies.
3. **Appropriately concise** — one actionable sentence. **PASS.**

**Acceptable variants:** "Returns the list's unique values in first-seen order"; "Order-
preserving de-duplication of a list." (Note this is the *same purpose* as Working W2's
`mystery` — a deliberate **varied-context** pairing: same job, denser surface. A learner who
named W2's purpose but stalls here is pattern-matching surface syntax, not reading for
purpose.)

**Weak / failing answers and what they diagnose:**

- *"It builds a list comprehension that enumerates `xs` and includes `x` when `x` is not in
  `xs[:i]`."* → **Multistructural**: restates the mechanism, never names dedup. (Catalog §5c —
  line-by-line; Whalley et al. 2006.)
- *"It checks each element against the earlier part of the list."* → describes a *step*, not
  the purpose; a teammate can't reconstruct "order-preserving dedup" from it.
- *"It filters out elements that appear earlier"* — borderline: it *implies* dedup and order
  but doesn't name the job outright; coach probes ("so what is the function *for*?") before
  crediting it as relational. **Trace first, then explain** — an answer guessed from the
  syntax without the trace tends to land here. (Catalog §5c — explaining without tracing.)
