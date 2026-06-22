# A1 — Advanced exemplars (notional machine)

Golden drills for the **Advanced** tier of module A1: combine mechanisms, or a mechanism
whose runtime behavior is non-obvious — the recursion call stack, generator/iterator
exhaustion, left-to-right evaluation order + short-circuit, augmented assignment on a
mutable inside a tuple. Predict output (or whether it **raises**) **and explain why**.
Every answer key was obtained by **running the snippet through the runner**
(`drill-generation.md` §2); the coach never guesses:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans four distinct mechanisms (stack / lazy-eval / eval-order / aug-assign).
Pose one, **hard-stop, wait** (`coaching-loop.md`). Two of these turn on `status`
(whether an exception is raised), not just `stdout`.

---

## A1 — Recursion: the call stack unwinds

```python
def fact(n):
    if n == 0:
        return 1
    sub = fact(n - 1)
    return n * sub

print(fact(4))
```

> **Your turn:** What does this print? Trace the stack of frames and how it unwinds.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "24\n"
status: ok
```

So the printed line is `24`.

**Why.** Each call **pushes a new frame** with its **own** local `n` and `sub`; the
caller's frame is suspended, not overwritten. The stack grows to
`fact(4) → fact(3) → fact(2) → fact(1) → fact(0)`. The base case `fact(0)` returns `1`,
then frames **pop and unwind**, each multiplying by its private `n`:
`fact(1)=1*1=1`, `fact(2)=2*1=2`, `fact(3)=3*2=6`, `fact(4)=4*6=24`. The per-frame `n` is
exactly why an inner call doesn't clobber the outer call's `n`.

**Diagnoses.** A learner who cannot say why each call keeps its own `n`, or who computes
a single mutated running value, has **no stack-of-frames model** (assumes one shared set
of locals across calls). The same gap predicts surprise at `RecursionError` for
unbounded recursion — Python keeps real frames and does no tail-call optimization.
(Catalog §5c; Ned Batchelder; A1 mental model §3 — the call stack.)

---

## A2 — Generator exhaustion: a one-shot cursor, not a list

```python
nums = (n * n for n in range(4))
first = list(nums)
second = list(nums)
print(first)
print(second)
print(sum(nums))
```

> **Your turn:** What do the three `print` lines show?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[0, 1, 4, 9]\n[]\n0\n"
status: ok
```

So the three lines are `[0, 1, 4, 9]`, then `[]`, then `0`.

**Why.** `nums` is a **generator** — a one-shot, stateful **cursor**, not a re-iterable
list. `list(nums)` drives it to exhaustion → `[0, 1, 4, 9]`, and the cursor is now at the
end. The second `list(nums)` finds it **already exhausted** → `[]`. `sum(nums)` over the
exhausted generator sums nothing → `0`. A generator's `__iter__` returns *itself*, so
there is no rewind; only a *fresh* generator (or a materialized `list`) can be iterated
again.

**Diagnoses.** Predicting `[0, 1, 4, 9]` for `second` (and `14` for the sum) reveals the
**"generator is a re-iterable lazy list" model** — treating a consumed cursor as a
container. The same gap causes the real bug where a debug `print(list(g))` silently
drains a generator before the production loop runs. (Catalog §5c; Python data model.)

---

## A3 — Evaluation order + short-circuit: operands, not bools; RHS may never run

```python
calls = []
def log(name, value):
    calls.append(name)
    return value

result = log("a", 0) or log("b", 7) or log("c", 1 // 0)
print(result)
print(calls)
```

> **Your turn:** What does this print? Watch for whether `1 // 0` ever runs.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "7\n['a', 'b']\n"
status: ok
```

So the two lines are `7`, then `['a', 'b']`. It does **not** raise `ZeroDivisionError`.

**Why.** `or` evaluates **left to right** and **short-circuits**, returning the **first
truthy operand unchanged** (an operand, not `True`/`False`). `log("a", 0)` runs (records
`"a"`) and returns `0` — falsy, so evaluation continues. `log("b", 7)` runs (records
`"b"`) and returns `7` — truthy, so `or` returns `7` **and stops**. The third operand
`log("c", 1 // 0)` is **never evaluated**, so `1 // 0` never executes and no exception is
raised, and `"c"` is never appended. Hence `result == 7` and `calls == ['a', 'b']`.

**Diagnoses.** Predicting a `ZeroDivisionError`, or `result == True`, or `'c'` in
`calls`, reveals the **"both operands always evaluate / `and`/`or` return bools" model**
— instead of operand-returning short-circuit operators where the deciding operand is
returned and the rest never runs. (Catalog §5c; Python FAQ; mathspp Pydon't.)

---

## A4 — Augmented assignment on a mutable inside a tuple ("fails *and* succeeds")

```python
t = ([1], [10])
try:
    t[0] += [2]
except TypeError as e:
    print("TypeError:", e)
print(t)
```

> **Your turn:** Does this raise? And what is `t` afterward?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "TypeError: 'tuple' object does not support item assignment\n([1, 2], [10])\n"
status: ok
```

So it prints `TypeError: 'tuple' object does not support item assignment`, then
`([1, 2], [10])`. (The whole snippet exits cleanly — `status: ok` — because the
`TypeError` is caught.)

**Why.** `t[0] += [2]` is **two phases**, not atomic. It desugars to roughly
`t[0] = t[0].__iadd__([2])`. **Phase 1:** `t[0].__iadd__([2])` runs first — the inner
list is mutable, so it is **mutated in place** to `[1, 2]` and returns itself. This
**commits**. **Phase 2:** Python then attempts the rebind `t[0] = <that list>`, which is
item assignment on a **tuple** → `TypeError`. The exception aborts phase 2 *after* phase
1 already happened. So the statement **both mutates the list and raises** — the list is
`[1, 2]` even though an exception fired. The tuple's immutability protects *which object*
slot 0 points at, not the mutability of that object.

**Diagnoses.** Predicting that the list is left as `[1]` because the statement raised
reveals the **"augmented assignment is atomic / all-or-nothing" model**, missing the
mutate-then-rebind two-phase reality. Predicting no error reveals the belief that tuple
immutability is "deep" (protects contents). (Catalog §5c; Python Morsels; PEP 203.)
