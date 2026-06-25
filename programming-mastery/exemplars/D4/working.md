# D4 — Working exemplars (performance & mechanical sympathy)

Golden drills for the **Working** tier of module D4. Each drill puts the cost in a place where
**intuition and reality diverge**: the slow part is *not* the visibly-complex part. The skill is
**find the hidden super-linear operation, name the level it lives at, and name the fix that changes
the cost class** — not micro-tweak the wrong thing.

D4 grades **hybrid** (`drill-generation.md` §5d): the **op-count is machine-verified**; the
**diagnosis and fix are rubric-graded**. The executable signal is the **deterministic operation
count** at growing sizes — **not** wall-clock (`duration_s` is noisy; do not grade on it). When a
fix is proposed, the coach also runs **both versions for identical output** (correct first, then
fast). Every key is **real runner output** (re-run from scratch during authoring):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans **three different points**: *(hidden O(n²) membership in a multi-stage pipeline —
locate the bottleneck)*, *(exponential recomputation — memoize)*, *(repeated string concatenation —
O(n²) → O(n))*. No repeated gotcha. Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to
grade** against module §7: **D1** = correct cost class of the hidden operation; **D2** = identifies
the real bottleneck / level and *doesn't* chase the decoy; **D3** = names a fix that changes the
class and (if asked) how to confirm + that behavior is preserved. **Catching the cost but
optimizing the decoy is a partial pass — flag the inverted priority** (the central D4 failure:
"intuitive guesses fail").

---

## W1 — Which stage is the bottleneck? (the heavy-looking stage isn't)

A two-stage report builder. Stage B does conspicuous string work and *looks* expensive; stage A
just removes duplicates and *looks* trivial. One of them is O(n²).

```python
def build_report(records):
    # Stage A: drop duplicates, preserve order
    seen = []
    unique = []
    for r in records:
        if r not in seen:          # r in <list>: O(len(seen)) each
            seen.append(r)
            unique.append(r)
    # Stage B: format each record
    lines = []
    for r in unique:
        lines.append(f"record-{r:06d}-formatted-output")   # looks heavy, but O(n)
    return lines
```

> **Your turn:** This is too slow on large inputs. Your teammate wants to optimize **Stage B**
> (the string formatting) because "all that f-string work must be expensive." Are they right?
> Which stage actually dominates, what is its Big-O, and what's the **one-line fix**?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — operations counted per stage (Stage A: list comparisons; Stage B:
format calls), on all-distinct input (n = 2000):

```
n=2000
stage A (dedup, "innocuous"):    1999000 ops
stage B (format, "looks heavy"): 2000 ops
A/B ratio: 999x
```

**Runner-verified behavior check** — the proposed fix (use a `set` for `seen`) must produce the
**same** deduped output:

```
[3,1,3,2,1] -> list=[3, 1, 2]  set=[3, 1, 2]  same=True
[5,5,5]     -> list=[5]        set=[5]        same=True
[0,False,1] -> list=[0, 1]     set=[0, 1]     same=True
status: ok
```

Answer: the teammate is **wrong**. **Stage A** dominates — it's **O(n²)** (`r not in seen` scans a
growing list, ~n²/2 comparisons: **1,999,000** at n=2000), while Stage B is **O(n)** (one format
per record: **2,000**). A is ~**999×** the cost of B. The fix is one line: make `seen` a **set**
(membership O(1) average), turning Stage A into **O(n)**. Optimizing Stage B would speed up the
**0.1%** that isn't the problem.

**Why.** The cost is in the *innocuous-looking* line (`r not in seen`), not the *visibly-complex*
one (the f-string). This is Knuth's "intuitive guesses fail" in miniature — the eye is drawn to the
string work, but the membership scan is what grows quadratically. The op-counts settle it without
any need to trust a wall-clock. And the fix is **algorithmic** (change the data structure so the
inner operation is O(1)), level 1 — no need to touch the formatting at all.

**Diagnoses.** A learner who agrees "optimize Stage B" has **guessed the bottleneck** from surface
complexity (§5c, guesses-the-bottleneck) — the signature failure; mark D2 down even if they can
state Big-O elsewhere. A learner who says "Stage A is slow" but proposes "make the loop faster" /
"use a comprehension" has the location right but the wrong **level** — a comprehension is still
O(n²) here because membership is still a list scan (D3 gap). Strong answer: Stage A, O(n²),
~1,999,000 ops vs B's 2,000; fix = `seen = set()`; confirm same output.

---

## W2 — Exponential recomputation: cache it (don't just "speed up the math")

A function that counts the ways to climb `n` stairs taking 1 or 2 steps at a time (it's the
Fibonacci recurrence in disguise). It's correct, but unusably slow for modest `n`.

```python
def climb_ways(n):
    if n <= 1:
        return 1
    return climb_ways(n - 1) + climb_ways(n - 2)
```

> **Your turn:** `climb_ways(35)` is painfully slow. Someone suggests "the addition is the slow
> part — rewrite it in a tighter form." Is the *arithmetic* the problem? What is actually growing,
> what's its Big-O, and what's the fix that changes the cost class?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — calls to the function, naive vs. memoized (deterministic counts):

```
n=10: naive=177 calls,     memoized=19 calls
n=20: naive=21891 calls,   memoized=39 calls
n=30: naive=2692537 calls, memoized=59 calls
```

(And for the dramatic confirmation: the *naive* recurrence at `n=40` **times out** the runner's ~5s
limit — `status: "timeout"` — while a memoized version returns instantly. The deterministic
**counts** are the primary signal; the timeout is the confirmation at large-enough n.)

Answer: the arithmetic is **not** the problem. The number of **calls** grows ~2ⁿ (exponential):
**2,692,537** calls at n=30, because `climb_ways` recomputes the *same subproblems* over and over.
The fix that changes the class is **memoization** (cache each `climb_ways(k)` the first time it's
computed) — that collapses the exponential call tree to **O(n)**: just **59** calls at n=30. Same
answers, exponentially fewer calls.

**Why.** Each call branches into two, and the two subtrees overlap massively (`climb_ways(n-1)` and
`climb_ways(n-2)` both recompute `climb_ways(n-3)`, etc.), so total work is exponential. "Tightening
the addition" is a **constant-factor** tweak (level 3) on an **exponential** algorithm (level 1) —
it cannot help: 2.6 million slightly-faster additions is still 2.6 million additions. Caching
removes the *recomputation*, dropping the count from millions to ~2n. That's the difference between
a level-3 micro-tweak and a level-1 algorithmic fix.

**Diagnoses.** A learner who proposes to "optimize the `+`" is micro-optimizing the wrong level
(§5c, optimizes-constant-factor-not-class). A learner who says "make it a loop" is *also* right (an
iterative bottom-up version is O(n) too) — credit it: the key insight is **stop recomputing
subproblems**, whether via a cache or a loop. A learner who says "exponential" but can't say *why*
(the overlapping subtrees) has D1 without the mechanism. Strong answer: O(2ⁿ) because subproblems
are recomputed; fix = memoize (or bottom-up loop) → O(n), ~59 calls at n=30; same outputs.

---

## W3 — Building a string in a loop: the `+=` that's secretly O(n²)

A function that joins a list of tokens into one string. It works, but gets slow as the token list
grows.

```python
def render(tokens):
    s = ""
    for t in tokens:
        s += t + " "        # each += builds a NEW string by copying all of s
    return s.strip()
```

> **Your turn:** What is the Big-O of `render` in the number of tokens `n` (assume each token is a
> short fixed-length string)? Where does the cost come from — and what's the idiomatic fix that
> makes it linear?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified key** — characters *copied* by the repeated `+=` (each `+=` copies the
accumulated string) vs. characters *touched* by `"".join` (each piece visited once):

```
n=100:  '+=' chars-copied=4950,    join touches=100
n=1000: '+=' chars-copied=499500,  join touches=1000
n=4000: '+=' chars-copied=7998000, join touches=4000
```

Answer: **O(n²)**. Each `s += …` creates a **new** string and copies the entire current `s` into
it, so the copying work sums to 0 + 1 + … + (n−1) ≈ **n²/2 characters** (**499,500** at n=1000).
The fix is **`" ".join(tokens)`** (or accumulate into a `list` and `join` once at the end), which
visits each piece a single time — **O(n)** (1,000 touches at n=1000).

**Why.** Python strings are **immutable**: `s += t` can't grow `s` in place, so it allocates a new
string the size of `s + t` and copies `s` over. Do that n times on a growing `s` and the copies
pile up quadratically — the same n²/2 shape as a nested loop, but the second "loop" is hidden inside
the string copy. `join` knows the total size up front and copies each character once. (This is the
string cousin of Foundations F3's `insert(0, …)`: an innocent-looking single statement carrying
hidden O(n) work.)

**Diagnoses.** A learner who says "O(n), it's one loop" has counted iterations and missed the
**per-`+=` copy cost** (§5c, amortized-vs-worst-case). A learner who senses it's slow and reaches
for "use a faster loop" or "f-strings" is at the wrong level — the issue is the **repeated copying**,
not the loop or the formatting (D3 gap). A learner who says "use join" but can't explain *why* `+=`
is quadratic (immutability → copy each time) has the fix without the model. Strong answer: O(n²)
because each `+=` copies the whole accumulator (immutable strings); fix = `" ".join(...)` → O(n).
