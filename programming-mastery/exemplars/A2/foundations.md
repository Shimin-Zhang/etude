# A2 — Foundations exemplars (code reading & chunking)

Golden drills for the **Foundations** tier of module A2. Each is a **small** (≤ ~12-line)
function on a familiar plan: **identify the 2–3 chunks and the beacon for each**, then
answer **"what does this chunk compute?"** for a named chunk. The chunk-computation key is
**executable** — every such key below was obtained by **running the snippet through the
runner** (`drill-generation.md` §2); the coach never guesses output:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

The chunk/beacon *identification* part is **rubric-graded** (`drill-generation.md` §3) —
a gold answer is given to grade against. Grading is **mixed** per A2 §5d. Coverage spans
distinct Foundations plans: find-extreme, filter/clean, and sort (compound swap beacon).
Pose one, **hard-stop, wait** (`coaching-loop.md`).

---

## F1 — Chunk a max-finder; compute the loop chunk

```python
def f(nums):
    best = nums[0]
    for n in nums:
        if n > best:
            best = n
    return best

print(f([3, 7, 2, 9, 4]))
```

> **Your turn:** (1) Name the chunks and the beacon for each. (2) What does the **loop
> chunk** compute for the input `[3, 7, 2, 9, 4]`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (the "what does it compute" part)

```
stdout: "9\n"
status: ok
```

So `f([3, 7, 2, 9, 4])` returns **9** — the loop chunk computes the **maximum** of the
list.

**Gold chunk/beacon identification** (rubric-graded)

| Chunk | Lines | Beacon | Name |
|---|---|---|---|
| **A — seed** | `best = nums[0]` | initialize a tracker from the first element | "start `best` at the first value" |
| **B — scan & keep larger** | the `for` body | the **`if n > best: best = n`** idiom — a `>` comparison that *replaces* the tracker | "keep the largest seen so far" |
| **C — return** | `return best` | — | "hand back the max" |

Whole-function summary: ***"returns the largest element of `nums`"*** — the **find-extreme**
plan.

**Diagnoses.** Naming chunk B "adds up the numbers" reveals **missing the beacon** — the
reader saw a `for` loop and assumed accumulation, never noticing the `>`/replace idiom that
makes it a *max*, not a *sum* (Crosby et al. 2002; §5c "missing the beacon"). A learner who
narrates "best is nums[0], then for n in nums, then if n greater than best…" with no chunk
names is **reading line-by-line** (§5c, entry 1; Shneiderman 1976).

---

## F2 — Chunk a clean/filter loop; compute the guard chunk

```python
def clean(items):
    result = []
    for s in items:
        s = s.strip()
        if not s:
            continue
        result.append(s.lower())
    return result

print(clean(["  Hello ", "", "  WORLD", "   ", "Foo  "]))
```

> **Your turn:** (1) Name the chunks and beacons. (2) What does `clean([...])` return for
> the given input?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "['hello', 'world', 'foo']\n"
status: ok
```

So it returns **`['hello', 'world', 'foo']`**.

**Gold chunk/beacon identification** (rubric-graded)

| Chunk | Lines | Beacon | Name |
|---|---|---|---|
| **A — setup** | `result = []` | empty collector list | "a list to collect kept strings" |
| **B — normalize + drop-empty guard** | `s = s.strip()` … `if not s: continue` … `result.append(s.lower())` | the **`if not s: continue`** guard (skip-empties beacon) + `strip`/`lower` (normalize beacon) | "strip each string, **skip the empties**, lowercase and keep the rest" |
| **C — return** | `return result` | — | "hand back the cleaned list" |

Whole-function summary: ***"trims whitespace, drops blank entries, and lowercases the
rest"*** — a **filter/clean** plan.

**Diagnoses.** Predicting four elements (forgetting the `"   "` whitespace-only string is
dropped) reveals not tracing the **guard chunk** — `strip()` turns `"   "` into `""`, which
the `if not s: continue` then skips. Missing that the **`continue`** is the load-bearing
beacon (calling this "just lowercases the list") is **missing the beacon** (§5c).

---

## F3 — Chunk a sort; name the swap beacon, compute the result

```python
def mystery(xs):
    a = list(xs)
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

print(mystery([5, 1, 4, 2, 8]))
```

> **Your turn:** The name `mystery` tells you nothing. (1) What **structural beacon** tells
> you what this is? (2) What does `mystery([5, 1, 4, 2, 8])` return?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[1, 2, 4, 5, 8]\n"
status: ok
```

So it returns **`[1, 2, 4, 5, 8]`** — the input **sorted ascending**.

**Gold chunk/beacon identification** (rubric-graded)

| Chunk | Lines | Beacon | Name |
|---|---|---|---|
| **A — copy input** | `a = list(xs)` | defensive copy | "work on a copy, don't mutate the caller's list" |
| **B — nested-loop bubble** | the two `for`s + the `if`/swap | the **`a[j], a[j+1] = a[j+1], a[j]` swap inside nested loops**, comparing **adjacent** elements with `>` | "repeatedly swap out-of-order adjacent pairs" |
| **C — return** | `return a` | — | "hand back the sorted copy" |

Whole-function summary: ***"returns `xs` sorted in ascending order (a bubble sort)"*** — the
**sort** plan. The swap beacon is the giveaway even though the function is named `mystery`.

**Diagnoses.** Failing to name *any* structure ("it loops over the list twice and swaps
some things") with no "sort" conclusion is **over-reliance on name-beacons** — with
`mystery` giving nothing, the reader couldn't fall back to the **structural** swap beacon to
recover intent (§5c "unhelpful names"; Soloway & Ehrlich 1984 — plans are structural, not
just lexical). This previews the Advanced skill of reading through stripped names.
