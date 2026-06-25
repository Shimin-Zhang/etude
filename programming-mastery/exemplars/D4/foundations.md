# D4 — Foundations exemplars (performance & mechanical sympathy)

Golden drills for the **Foundations** tier of module D4. Each drill exercises **one** cost
mechanism on a familiar surface: name the **Big-O**, predict the **growth** (how the operation
count changes when n grows), or predict **timeout-vs-completes**. The answer is computable.

D4 grades **hybrid** (`drill-generation.md` §5d): the **cost number / timeout status is
machine-verified**; the **"why" (the Big-O reasoning) is rubric-graded**. The executable signals
here are **TIMEOUT status** and **deterministic operation counts** — **not** precise wall-clock
(`duration_s` is noisy in the sandbox; do not grade on it). Every key below is **real runner
output** (re-run from scratch during authoring):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans **three different points** in the parameter space — *(O(n²) nested loop, op-count)*,
*(exponential recursion, timeout + op-count)*, *(per-operation cost of a data structure, growth
ratio)* — no repeated gotcha. Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade**
against module §7: **D1** = correct cost class / count / timeout-prediction; **D2** = points at
*what grows* (at least partial at Foundations); **D3** = not required at Foundations. A correct
number with a hand-wavy "why" is a Foundations pass; flag it and probe the reasoning before
promoting.

---

## F1 — Name the Big-O of a nested loop (and confirm by counting)

The classic all-pairs scan. The skill is to see that an inner loop *inside* an outer loop over the
same n means the body runs ~n² times.

```python
def count_pairs(xs):
    total = 0
    n = len(xs)
    for i in range(n):
        for j in range(i + 1, n):
            total += 1          # one step per unordered pair (i, j)
    return total
```

> **Your turn:** What is the **Big-O** of `count_pairs` in terms of `n = len(xs)`? Roughly how many
> times does the `total += 1` line run when `n = 100`? And if you doubled `n` to 200, roughly how
> would that count change?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** (operation count = the value `count_pairs` returns, which is exactly the
number of times the inner line ran):

```
n=4:   6 pair-ops    (n*(n-1)/2 = 6)
n=8:   28 pair-ops   (n*(n-1)/2 = 28)
n=16:  120 pair-ops  (n*(n-1)/2 = 120)
n=100: 4950 pair-ops (n*(n-1)/2 = 4950)
```

Answer: **O(n²)**. At n=100 the line runs **4,950** times (= n(n−1)/2). Doubling n to 200 makes it
**19,900** — **~4×** the work, the signature of quadratic growth (double the input → quadruple the
work).

**Why.** The outer loop runs n times; for each, the inner loop runs up to n times, so the body
executes on the order of n² times — `n(n−1)/2` precisely, which is **Θ(n²)**. The exact constant
(½) doesn't matter for the *class*: what matters is that the work grows with the **square** of the
input. The doubling test (4,950 → 19,900 ≈ 4×) is how you *recognize* quadratic from data without
deriving the formula.

**Diagnoses.** A learner who says **O(n)** "because there are two loops, n + n" has added the loops
instead of multiplying — they don't yet see that a *nested* loop multiplies (§5c is the parent
inversion: not modeling what grows). A learner who says "O(n²)" but, asked the doubling effect,
says "2×" has the class right but not the *meaning* of quadratic growth (D1 partial; probe before
promoting). Strong answer: O(n²), ~4,950 at n=100, ~4× on doubling, *because* nested loops
multiply.

---

## F2 — Predict timeout vs. completes: naive exponential recursion

The naive Fibonacci. The skill is to see that each call spawns **two** more, so the number of calls
explodes exponentially — and to predict that a large enough n cannot finish in the runner's ~5s.

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(40))
```

> **Your turn:** Roughly how does the *number of calls* to `fib` grow as `n` grows — linearly?
> quadratically? faster? And will `fib(40)` finish within the runner's ~5-second limit, or **time
> out**?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key — the call count grows ~2ⁿ** (instrumented with a counter; deterministic):

```
fib(5):  15 calls
fib(10): 177 calls
fib(20): 21891 calls
fib(30): 2692537 calls
```

**Runner-verified key — `fib(40)` TIMES OUT:**

```
status: "timeout"     (the runner's ~5s limit; returncode: null)
```

(For calibration: this machine ran `fib(32)` in ~0.16s and `fib(35)` in ~0.64s — both *complete*.
The exact n where it crosses ~5s is **machine-dependent**, which is precisely why the deterministic
**op-count** is the primary signal and the **timeout** is the dramatic confirmation at a
large-enough n. `fib(40)` reliably times out here.)

**Why.** Each non-base call makes **two** recursive calls, so the call tree roughly *doubles* in
size every time n grows by one — the call count grows like ~φⁿ ≈ 1.6ⁿ (close enough to "doubles
each step" for the intuition). The counts confirm it: 21,891 at n=20 → 2,692,537 at n=30 (a 10-step
increase multiplies the work by ~123×, not 10× or 100×). That is **exponential, O(2ⁿ)-ish**, and it
overwhelms any fixed time budget for modest n — hence the timeout at 40. (The fix, for later tiers:
memoize, turning the exponential call tree into O(n) — but Foundations only needs to *predict the
explosion*.)

**Diagnoses.** A learner who says "O(n), it just counts down to 0" has missed that the function
calls itself **twice** — modeling it as a single chain, not a branching tree (§5c, no model of what
grows). A learner who says "it'll be slow but finish" underestimates exponential growth — the most
common cost-intuition failure. A learner who predicts the timeout but can't say *why* (the
branching) has D1 without the reasoning (partial). Strong answer: ~2ⁿ / exponential because each
call branches into two; `fib(40)` times out.

---

## F3 — Per-operation cost: building a list at the front vs. the end

Two ways to build a list in a loop. They look equally innocent; one is O(n) total and one is O(n²),
because of the **per-operation** cost of where you insert.

```python
# Version A: append to the end
def build_append(n):
    out = []
    for i in range(n):
        out.append(i)        # amortized O(1) per call
    return out

# Version B: insert at the front
def build_front(n):
    out = []
    for i in range(n):
        out.insert(0, i)     # O(len(out)) per call: every existing element shifts right
    return out
```

> **Your turn:** Both loops run `n` times. Are these two functions the **same** cost, or different?
> Specifically: across the whole loop, how many element-**shifts** does `build_front` cause for
> `n = 1000`, and what is its Big-O? What about `build_append`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — element shifts caused by `insert(0, ...)`, counted (each front-insert
shifts every element already in the list):

```
n=100:  front-insert shifts=4950   (append shifts=0)
n=1000: front-insert shifts=499500 (append shifts=0)
n=5000: front-insert shifts=12497500
```

Answer: **different.** `build_append` is **O(n)** (append is amortized O(1), no shifting).
`build_front` is **O(n²)** — at n=1000 it causes **499,500** element shifts (≈ n²/2), because each
`insert(0, …)` must move every element already present one slot to the right.

**Why.** The number of loop *iterations* is the same (n), so a learner who only counts iterations
sees no difference. The cost hides in the **per-operation** work: `list.insert(0, x)` is O(current
length), so summing 0 + 1 + … + (n−1) over the loop gives ~n²/2 shifts — quadratic. `list.append`
shifts nothing (amortized O(1)), so the total stays linear. Same-looking loops, different cost
*classes*, decided by the cost of one operation. (This is the same n²/2 shape as F1's nested loop —
but here the second "loop" is hidden *inside* `insert`.)

**Diagnoses.** A learner who says "same — both are one loop of n" has counted iterations and missed
the **per-operation** cost (§5c, amortized-vs-worst-case confusion; the canonical "insert(0) is
basically free" error). A learner who senses front-insert is "slower" but says "still O(n), just a
bigger constant" has the right instinct but the wrong class — the shifting makes it genuinely
quadratic, not a constant factor. Strong answer: append O(n), front-insert O(n²) (~499,500 shifts
at n=1000) *because* each front-insert shifts the whole list.
