# E3 — Foundations exemplars (code review)

Golden drills for the **Foundations** tier of module E3. Each is a **diff/function to review**
with **one clear planted bug** (no decoys): **catch it and explain *why* it's wrong.** Code
review is rubric-graded (`drill-generation.md` §3), but every planted bug below was **confirmed
to misbehave by running it through the runner** (`drill-generation.md` §2) — the gold's catch is
anchored to real output, never guessed:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Foundations bug-class space: an off-by-one boundary, a wrong comparison
operator, and a wrong slice. Each gold gives the **prioritized issue** (trivial here — one
issue) and a **model review comment** (precise · references the line · states impact · suggests
a fix · kind). Per `coaching-loop.md`, the coach poses one drill, then **hard-stops and waits**
— the gold is for *grading*, never shown before the learner attempts. **How to grade:** if the
learner disputes the bug, *run it* and show the evidence; score on D1 (catch) + D3 (precise,
actionable phrasing) per the module §7 rubric.

---

## F1 — Off-by-one: the excluded upper bound

**Spec.** `sum_inclusive(a, b)` should return `a + (a+1) + ... + b`, with **`b` inclusive**.

```python
def sum_inclusive(a, b):
    total = 0
    for n in range(a, b):
        total += n
    return total
```

> **Your turn:** Review this. Is it correct against the spec? If not, what's the bug, what's
> the impact, and how would you fix it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the planted bug is real)

```
sum_inclusive(1, 5)  -> 10   (spec wants 15)
sum_inclusive(3, 3)  -> 0    (spec wants 3)
sum_inclusive(0, 0)  -> 0    (spec wants 0 — passes by luck)
# reference sum(range(a, b+1)): 1..5 = 15, 3..3 = 3
status: ok
```

**Prioritized issue list.** One issue, blocking (correctness):
1. `range(a, b)` excludes `b`, so the loop sums `a..b-1`, not `a..b`.

**Model review comment (the gold).**

> **`for n in range(a, b)` (line 3) — blocking.** `range(a, b)` stops at `b-1`, so the upper
> bound `b` is never added — but the spec says `b` is inclusive. `sum_inclusive(1, 5)` returns
> `10` instead of `15`, and the degenerate `sum_inclusive(3, 3)` returns `0` instead of `3`.
> Fix: iterate `range(a, b + 1)`. Worth a test on the single-element case (`a == b`) since
> that's where it's most visibly wrong.

**Diagnoses.** A learner who approves this ("LGTM, sums the range") **rubber-stamped** — they
read the intent ("it sums a range") without checking the boundary against the contract (§5c,
rubber-stamping). A learner who says "something's off with the range" but can't name the
impact has a weak **D3** (vague feedback) — push for the exact input that breaks (`a == b`).
The bug class is the classic **off-by-one** (Catalog §5c; A1 boundary/edge intuition).

---

## F2 — Wrong boundary operator: the excluded lower bound

**Spec.** `valid_percent(p)` returns `True` iff `p` is in the **inclusive** range `0` to `100`.

```python
def valid_percent(p):
    return 0 < p <= 100
```

> **Your turn:** Review this against the spec. Correct? If not — the bug, its impact, and a fix.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence**

```
valid_percent(0)   -> False   (spec wants True)   <-- bug
valid_percent(1)   -> True
valid_percent(50)  -> True
valid_percent(100) -> True
valid_percent(101) -> False
valid_percent(-1)  -> False
status: ok
```

**Prioritized issue list.** One issue, blocking (correctness):
1. `0 < p` uses a strict `<`, excluding the lower boundary `0`, which the spec says is valid.

**Model review comment (the gold).**

> **`return 0 < p <= 100` (line 2) — blocking.** The left comparison is strict (`0 < p`), so
> `p == 0` is rejected even though `0` is a valid percentage per the spec — `valid_percent(0)`
> returns `False` when it should be `True`. The upper bound is correctly inclusive (`<= 100`);
> only the lower one is wrong. Fix: `return 0 <= p <= 100`. A boundary test at `0` and `100`
> would have caught this.

**Diagnoses.** Predicting "correct" reveals the reviewer didn't probe the **boundary** — the
exact value (`0`) the operator mishandles (§5c, did-not-trace; the boundary is where the bug
lives). A correct catch phrased as "the `<` is wrong" without naming `p == 0` as the failing
input is a partial **D3**. Bug class: **wrong comparison operator on a boundary** (Catalog §5c).

---

## F3 — Wrong slice: "last n" that returns the wrong end

**Spec.** `last_n(items, n)` returns the **last** `n` items, in original order.
`last_n([1, 2, 3, 4, 5], 2)` → `[4, 5]`.

```python
def last_n(items, n):
    return items[n:]
```

> **Your turn:** Review this against the spec. Correct? If not — the bug, its impact, and a fix.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence**

```
last_n([1, 2, 3, 4, 5], 2)  -> [3, 4, 5]   (spec wants [4, 5])
last_n(['a', 'b', 'c'], 1)  -> ['b', 'c']  (spec wants ['c'])
status: ok
```

**Prioritized issue list.** One issue, blocking (correctness):
1. `items[n:]` drops the **first** `n` and returns the rest — the opposite end from "last `n`."

**Model review comment (the gold).**

> **`return items[n:]` (line 2) — blocking.** This slices *from* index `n` to the end, so it
> returns everything **after** the first `n` items — not the last `n`. `last_n([1,2,3,4,5], 2)`
> returns `[3, 4, 5]` instead of `[4, 5]`. Fix: `return items[-n:]` (takes the last `n`).
> One edge to watch: `n == 0` — `items[-0:]` is `items[0:]`, i.e. the **whole** list, so if
> `n == 0` should return `[]`, guard it: `return items[-n:] if n > 0 else []`.

**Diagnoses.** A learner who eyeballs `items[n:]` as "takes n items" and approves it confused
the slice's *start* with a *count* (§5c, did-not-trace — running one example exposes it
instantly). Catching the main bug but missing the `n == 0` subtlety in the **fix** is fine at
Foundations (it's a genuine Advanced-flavored wrinkle) — note it as a stretch, don't penalize.
Bug class: **wrong slice / index direction** (Catalog §5c).
