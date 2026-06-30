# A2 — Advanced exemplars (code reading & chunking)

Golden drills for the **Advanced** tier of module A2: a **denser** snippet (multiple
functions / nested structure, or **unhelpful names**). **Chunk it, name the 2 most
important chunks/functions and *why* each is load-bearing,** and **recover intent from
structure** when names don't help. Grading is **mixed** (A2 §5d): the chunk map and "which
2 matter" are **rubric-graded** against the gold answer; "what does this chunk/snippet
compute?" is **runner-verified** — every such key was obtained by **running the snippet**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three Advanced demands: chunk-and-rank a multi-function pipeline, recover
intent from obfuscated names, and read through a memoization wrapper. Pose one,
**hard-stop, wait** (`coaching-loop.md`).

---

## A1 — Chunk a dense pipeline; name the 2 most important chunks and why

```python
def _valid(rec):
    return isinstance(rec.get("amount"), (int, float)) and rec.get("amount") > 0

def settle(batch, fee_rate):
    accepted = []
    rejected = []
    gross = 0
    for rec in batch:
        if not _valid(rec):
            rejected.append(rec.get("ref", "?"))
            continue
        amt = rec["amount"]
        fee = round(amt * fee_rate, 2)
        net = round(amt - fee, 2)
        gross += amt
        accepted.append({"ref": rec["ref"], "net": net, "fee": fee})
    return {
        "accepted": accepted,
        "rejected": rejected,
        "gross": round(gross, 2),
        "count": len(accepted),
    }

batch = [
    {"ref": "A", "amount": 100.0},
    {"ref": "B", "amount": -5},
    {"ref": "C", "amount": 50.0},
    {"ref": "D"},
    {"ref": "E", "amount": 33.33},
]
import json
print(json.dumps(settle(batch, 0.029), sort_keys=True))
```

> **Your turn:** Chunk `settle`. Then name the **2 most important chunks** and say **why**
> each is load-bearing (not incidental). Summarize the function in 1–3 sentences. (Bonus:
> what does it print?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "{\"accepted\": [{\"fee\": 2.9, \"net\": 97.1, \"ref\": \"A\"}, {\"fee\": 1.45, \"net\": 48.55, \"ref\": \"C\"}, {\"fee\": 0.97, \"net\": 32.36, \"ref\": \"E\"}], \"count\": 3, \"gross\": 183.33, \"rejected\": [\"B\", \"D\"]}\n"
status: ok
```

So it accepts A/C/E (computing each net after a 2.9% fee), rejects B (negative) and D
(missing amount), and reports `gross` **183.33** and `count` **3**.

**Gold chunk map + ranking** (rubric-graded)

| Chunk | Lines | Beacon | Name |
|---|---|---|---|
| **A — init accumulators** | `accepted/rejected/gross` | three empty collectors | "buckets for kept, dropped, and a running total" |
| **B — validate-or-reject guard** ⭐ | `if not _valid(rec): rejected.append(...); continue` (+ the `_valid` helper) | the **`continue` guard gated on `_valid`** | "drop invalid records (non-positive / missing amount) and record their refs" |
| **C — fee/net transform** ⭐ | `fee = round(...); net = round(...); gross += amt; accepted.append(...)` | the **`amt - fee` net calc** + `gross += amt` accumulator | "for each valid record, take the fee, compute net, and accumulate gross" |
| **D — assemble result** | the `return {...}` | dict packaging | "package accepted/rejected/gross/count" |

**The 2 most important chunks are B and C**, because they carry the function's *purpose*:
**B decides *which* records count** (the validation policy) and **C computes *the money***
(fee/net/gross). A and D are incidental plumbing — init and packaging. **Summary:**
*"`settle` processes a batch of payment records: it rejects any with a missing or
non-positive amount, and for each valid one computes a fee (`fee_rate` of the amount) and
the net after fee, returning the accepted records, the rejected refs, the gross total, and
the accepted count."*

**Diagnoses.** Ranking chunk D (or the `round()` calls) as "most important" is **chunks not
ranked** — the reader formed chunks but has no model of which is load-bearing vs plumbing,
so the summary buries the validation-and-money point (§5c "not ranked"; the AI-era review
skill of *what matters most*, → E3). Merging B and C into one "the loop does stuff" blob, or
splitting the fee calc from its own loop, is a **boundary error** (§5c).

---

## A2 — Recover intent from structure when names are unhelpful

```python
def g(a, t):
    x = 0
    y = len(a) - 1
    while x <= y:
        m = (x + y) // 2
        if a[m] == t:
            return m
        if a[m] < t:
            x = m + 1
        else:
            y = m - 1
    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(g(arr, 23))
print(g(arr, 10))
print(g(arr, 2))
print(g(arr, 91))
```

> **Your turn:** Every name here is a single letter — they tell you nothing. Recover the
> intent from **structure** alone. What does `g` compute, and what **structural beacons**
> told you? (Bonus: what do the four prints show?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "5\n-1\n0\n9\n"
status: ok
```

So `g(arr, 23) → 5`, `g(arr, 10) → -1` (not present), `g(arr, 2) → 0`, `g(arr, 91) → 9`:
the **index** of the target in the sorted array, or `-1` if absent.

**Gold answer** (rubric-graded)

> **`g` is binary search** — it returns the index of `t` in the **sorted** list `a`, or
> `-1`. **Structural beacons** (no helpful names needed): the **`m = (x + y) // 2`
> midpoint**, the **`while x <= y` two-pointer bracket** that **halves** each step
> (`x = m + 1` / `y = m - 1` discards half), and the three-way `==` / `<` / `else`
> comparison against the midpoint. Those three together are the binary-search plan; the
> precondition (the input `a` must be sorted) is implied by the discard-half logic.

| Chunk | Beacon | Name |
|---|---|---|
| **A — init the bracket** | `x = 0; y = len(a)-1` | "low/high pointers spanning the array" |
| **B — halve toward target** ⭐ | `m = (x+y)//2` midpoint + `x=m+1`/`y=m-1` narrowing | "check the middle; discard the half that can't contain `t`" |
| **C — not-found** | `return -1` | "exhausted the bracket → absent" |

**Diagnoses.** *"It loops over the array and compares elements until it finds `t`"* (calling
it a **linear scan**) is the **unhelpful-names / wrong-plan** error — the reader fell back to
the most generic loop interpretation because the names gave nothing, and **missed the
`(x+y)//2` midpoint + halving** structural beacons that distinguish *binary* search from
linear (§5c "unhelpful names"; Soloway & Ehrlich 1984 — plans are structural). The
consequence-probe ("what must be true of `a` for this to work?" → *it must be sorted*)
separates a reader who *recognized* binary search from one who *guessed* a label.

---

## A3 — Read through a memoization wrapper; identify the recursive chunk

```python
def build(n, _cache={}):
    if n in _cache:
        return _cache[n]
    if n < 2:
        val = n
    else:
        val = build(n - 1) + build(n - 2)
    _cache[n] = val
    return val

print([build(i) for i in range(10)])
print(build(20))
```

> **Your turn:** Chunk `build` and name the **2 most important chunks** and why. What does
> the **recursive chunk** compute? (Bonus: what do the two prints show?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n6765\n"
status: ok
```

So `[build(i) for i in range(10)]` is **`[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`** and
`build(20)` is **`6765`** — the **Fibonacci** sequence.

**Gold chunk map + ranking** (rubric-graded)

| Chunk | Lines | Beacon | Name |
|---|---|---|---|
| **A — cache check** ⭐ | `if n in _cache: return _cache[n]` | the **`if n in _cache: return`** memo-lookup beacon (a mutable default `_cache={}` shared across calls) | "if we've computed `build(n)` before, return the saved answer" |
| **B — recursive combine** ⭐ | `if n < 2: val = n else: val = build(n-1) + build(n-2)` | the **`f(n-1) + f(n-2)`** two-way self-recursion + the `n < 2` base case | "base case `n` for n<2; otherwise sum the two previous values" |
| **C — store & return** | `_cache[n] = val; return val` | write-back to the cache | "save the result before returning" |

**The 2 most important chunks are A and B.** **B is the algorithm** — `build(n-1) +
build(n-2)` with base `n<2` is the **Fibonacci recurrence** (the *what*). **A is the
memoization** — the cache lookup is *why this is fast* (turns exponential recursion into
linear by reusing `_cache`); it's load-bearing because without it `build(20)` would
recompute enormously. C is the plumbing that connects them. **Summary:** *"`build(n)`
returns the nth Fibonacci number, memoized: a cache (the shared `_cache` default) short-
circuits repeat work, and the recurrence `build(n-1) + build(n-2)` (base case `n<2`)
computes new values."*

**Diagnoses.** Naming C ("save the result") as most important, or missing that **A is the
memoization beacon** and treating `_cache` as incidental, is **chunks not ranked** (§5c) —
the reader didn't separate *the algorithm* (B) and *the optimization* (A) from the plumbing.
Reading `build(n-1) + build(n-2)` as anything but the Fibonacci recurrence is **missing the
compound beacon.** (Bonus subtlety, A1 territory: the mutable-default `_cache={}` persists
across *all* calls — which is exactly what makes the memoization work here.)
