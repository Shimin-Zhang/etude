# D4 — Advanced exemplars (performance & mechanical sympathy)

Golden drills for the **Advanced** tier of module D4. Each **combines** two or more of: cost
reasoning + measurement strategy + the level hierarchy + behavior-preservation + the
*premature-optimization* judgment. Given slow (or allegedly-slow) code, the learner must decide
**which level dominates**, justify **why a fix does or doesn't change the cost class**, say **how
they'd confirm it without trusting a wall-clock**, and call out a **premature** optimization or a
**fast-but-wrong** "optimization."

D4 grades **hybrid** (`drill-generation.md` §5d): **op-counts / behavior-divergence are
machine-verified**; the **judgment (level, why, premature-or-not, tradeoff) is rubric-graded**, and
the coach says so. The executable signals are **operation counts**, **`cProfile` call counts
(deterministic `ncalls`)**, and **behavior-preservation** — **not** wall-clock (`duration_s` is
noisy; never grade on it). Every key is **real runner output** (re-run from scratch during
authoring):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans **three different points**: *(two proposed fixes — which actually changes the class,
and why)*, *(measure, don't guess — the profiled hot path is the innocuous line, and judging
premature reaches)*, *(a "fast" optimization that is secretly wrong — behavior-preservation + the
caching tradeoff)*. No repeated gotcha. Pose one, **hard-stop, wait** (`coaching-loop.md`).
**How to grade** against module §7: **D1** = cost class right; **D2** = right level + resists the
decoy/premature reach; **D3** = fix changes the class, says how to confirm, preserves behavior;
plus the **teach-it-back** of the level hierarchy. Report executable and rubric verdicts
**separately**.

---

## A1 — Two proposed optimizations: which one actually helps, and why?

A duplicate-remover that's too slow. Two engineers each submit a "faster" version.

```python
def dedupe(items):
    seen = []
    out = []
    for x in items:
        if x not in seen:        # O(len(seen)) per element -> O(n^2) total
            seen.append(x)
            out.append(x)
    return out
```

- **Fix P (micro):** "I tightened the inner membership scan — local variable for `seen`, manual
  index loop with early exit instead of `x not in seen`."
- **Fix Q (algorithmic):** "I replaced `seen` (a list) with a `set`."

> **Your turn:** Both compile and pass the tests. **Which fix actually makes this scale, and which
> is a waste of effort — and why?** State the Big-O of the original and of each fix. How would you
> *confirm* your answer without relying on a single stopwatch reading? (And: does either fix risk
> changing the output?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — dominant-operation counts at n=3000 (all-distinct, worst case), plus a
behavior check that both fixes preserve order-preserving dedup:

```
n=3000:
  micro-optimized quadratic (Fix P): 4498500 ops
  algorithm-change to set   (Fix Q): 3000 ops

behavior (both fixes vs the original):
  [3,1,3,2,1] -> [3, 1, 2]   same=True
  [5,5,5]     -> [5]         same=True
  [0,False,1] -> [0, 1]      same=True
```

Answer: **Fix Q helps; Fix P is wasted effort.** The original is **O(n²)** (`x not in seen` scans a
growing list). **Fix P keeps it O(n²)** — tightening the inner loop is a *constant-factor* change
(level 3); the op-count is still ~n²/2 (**4,498,500** at n=3000). **Fix Q changes the class to
O(n)** — set membership is O(1) average, so the dominant-op count drops to **3,000** (linear). To
confirm without a stopwatch: **count the dominant operation at two or three sizes** and look at the
*growth* — Fix P quadruples when n doubles (still quadratic); Fix Q doubles (linear). Both fixes
preserve the output (verified), so the win is real, not a fast-wrong answer.

**Why.** This is corollary 1 made concrete: **asymptotic class, not the inner-loop micro-detail,
governs scaling.** Fix P optimizes *within* the wrong cost class — at n=3000 it does 4.5 million
slightly-faster comparisons; at n=30,000 it'd do 450 million. Fix Q removes the scan entirely. The
measurement that distinguishes them is the **growth ratio**, not one timing — a single wall-clock at
one size could even make P look fine on small input and is noisy in this sandbox anyway. The
**teach-it-back**: "a micro-optimization rarely changes the cost class; reach for the algorithm /
data structure first."

**Diagnoses.** A learner who picks **Fix P** (or rates both as helping) has confused
constant-factor tuning with algorithmic change (§5c, optimizes-constant-factor-not-class) — the core
Advanced miss; mark D2/D1 down. A learner who picks Q but "confirms" with one timing has the right
fix but the wrong *verification* (D3 partial) — push for the growth ratio across sizes. A learner
who picks Q *and* explains the class change *and* says "count ops at two sizes; confirm same output"
is solid. Strong answer: Q (O(n²)→O(n)); P stays O(n²); confirm via growth ratio; behavior
preserved.

---

## A2 — Measure, don't guess: the profiled hot path is the line you'd never suspect

A routine that builds a derived list. It has a helper, `score`, that *looks* expensive (it does
arithmetic in a little loop), and an innocuous-looking result-building line.

```python
def score(x):
    acc = 0
    for k in range(5):           # fixed 5 iterations -> O(1) per call
        acc += (x * k + 7) % 13
    return acc

def build(n):
    out = []
    for i in range(n):
        v = score(i)             # called n times
        out.insert(0, v)         # newest first
    return out
```

> **Your turn:** `build` is slow for large `n`. Your instinct says "`score` is the hot spot — it's
> doing all that modular arithmetic in a loop." Before you optimize it: **how would you find the
> real bottleneck**, and what do you predict it is? Give the Big-O of the whole function and the
> fix. Is optimizing `score` justified or premature?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — `cProfile` deterministic call counts (`ncalls`) plus an explicit count of
the element-shifts caused by `insert(0, …)`:

```
cProfile (n=1500):  score: ncalls=1500    build: ncalls=1

operation counts:
  n=500:  score calls=500  (O(n)),  front-insert shifts=124750   (O(n^2))
  n=1500: score calls=1500 (O(n)),  front-insert shifts=1124250  (O(n^2))
  n=3000: score calls=3000 (O(n)),  front-insert shifts=4498500  (O(n^2))
```

Answer: the bottleneck is **`out.insert(0, v)`**, not `score`. **How to find it:** run a profiler
(`cProfile`) or count operations at two or three sizes — don't guess. The profile shows `score` is
called exactly **n** times (O(n) total, each call O(1) — it's bounded 5-iteration arithmetic), while
`insert(0, …)` causes **~n²/2 element shifts** (**4,498,500** at n=3000) because each front-insert
moves every existing element. The whole function is **O(n²)**, and the fix is **append then reverse
once** (`out.append(v)` in the loop, `out.reverse()` or `out[::-1]` at the end) → **O(n)**.
Optimizing `score` would be **premature**: it's O(n) total and cheap; speeding it up can't fix a
quadratic function.

**Why.** This is corollary 2 (don't guess — profile) plus the level hierarchy. The eye is drawn to
`score` (visible arithmetic in a loop), but its loop is **fixed at 5** — bounded work, O(1) per
call. The cost is in the *innocuous* `insert(0, …)`, whose hidden O(n) shift makes the total
quadratic. The deterministic profile (`ncalls`) and the shift count locate it unambiguously; a
*guess* sends you to optimize the wrong line — exactly Knuth's "intuitive guesses fail." Reaching
for `score` (or worse, `__slots__` / numpy / a C rewrite) before measuring is the premature move the
module warns against.

**Diagnoses.** A learner who optimizes `score` on instinct has **guessed the bottleneck** (§5c,
guesses-the-bottleneck) — and if they reach for a hardware/`numpy` trick, that's also the *premature
mechanical sympathy* error (§5c). A learner who says "profile it" but then can't name what the
profile would show, or trusts a single timing, has the discipline without the model (D3 partial). A
learner who profiles, names `insert(0, …)` as O(n²), gives the append-then-reverse fix, and says
optimizing `score` is premature is solid. Strong answer: measure (profile/op-count) → `insert(0)` is
the O(n²) cost → append+reverse → O(n); `score` is O(n) and optimizing it is premature.

---

## A3 — A "10× faster" optimization that's secretly wrong (and the tradeoff)

A cart-pricing function is called a lot with repeating carts, so an engineer **adds a cache** to
speed up repeated calls.

```python
prices = {"apple": 10, "banana": 5}      # loaded from a store that can update prices

def total_uncached(cart):
    return sum(prices[item] * qty for item, qty in cart.items())

_cache = {}
def total_cached(cart):
    key = tuple(sorted(cart.items()))
    if key in _cache:
        return _cache[key]               # "fast path"
    val = sum(prices[item] * qty for item, qty in cart.items())
    _cache[key] = val
    return val
```

> **Your turn:** The cache makes repeated calls O(1) instead of O(items) — a real speedup. **But is
> `total_cached` a safe optimization?** What must be true for it to be correct, and what breaks if
> it isn't? More broadly: when is adding a cache the right call, and what does it cost you besides
> memory?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — the cached version returns a **stale, wrong** answer once the underlying
prices change (behavior is **not** preserved):

```
before price change:
  uncached=25  cached=25  same=True
after apple price 10 -> 20:
  uncached=45  cached=25  same=False      <-- cached is WRONG (stale)
status: ok
```

Answer: `total_cached` is **only correct if the inputs to the computation never change** — and here
`prices` *can* change (it's loaded from a store that updates). The cache keys on the **cart** but
the result also depends on **`prices`**, which isn't in the key, so after a price update the cache
returns the **old** total: `cached=25` when the correct answer is **45**. That's a **fast-but-wrong**
"optimization" — a correctness regression (corollary 3: correct first, then fast). A cache is the
right call when (a) the same inputs recur often (real reuse), (b) the computation is genuinely
expensive *and measured to be hot*, and (c) you can **invalidate** it when its dependencies change
(or key on *all* of them). Its costs beyond memory: **invalidation complexity** and the risk of
**staleness bugs** — "there are only two hard things in computer science…"

**Why.** Performance work is **behavior-preserving change under a cost constraint** (ties B3/D3). A
speedup that changes outputs isn't an optimization; it's a bug with better latency. The
behavior-preservation check catches it immediately: same call, different answer after the world
changes. This is also a **tradeoff-under-tension** case (Frontier-adjacent): the cache trades memory
and *correctness-maintenance burden* for speed — worth it only when the reuse is real, the path is
measured-hot, and invalidation is handled. Adding it speculatively (no measured hotness, no
invalidation plan) is premature *and* dangerous.

**Diagnoses.** A learner who says "great, it's faster" and stops has missed **behavior-preservation
under changing inputs** (§5c, optimizes-by-changing-behavior) — the central correctness trap; the
executable check (cached=25 vs uncached=45) settles it. A learner who spots the staleness but frames
it as "just add invalidation" without acknowledging that invalidation is the *hard part* and that
the cache should be justified by *measurement* has D2 partial. A learner who says "is this even a
measured hot path? if not, the cache is premature complexity *and* a staleness risk; if yes, key on
prices too or invalidate on update" is solid — they hold cost, correctness, *and* the tradeoff at
once. Strong answer: unsafe — result depends on `prices` (not in the key) → stale/wrong after an
update (45 vs 25); cache only with real reuse + measured hotness + invalidation; it costs
invalidation complexity and staleness risk, not just memory.
