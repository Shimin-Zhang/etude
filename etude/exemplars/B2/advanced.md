# B2 — Advanced exemplars (code writing & composition)

Golden drills for the **Advanced** tier of module B2: each spec requires **composing two or
more sub-behaviors** (or a **contract decision** on edge inputs). The learner composes in
**verified steps**, passes the **full battery**, **justifies the contract**, does **not**
over-engineer, **and explains the composition** on a teach-it-back (`drill-generation.md` §6).
Two verdicts, reported separately (B2 §5d):

- **Product (executable):** the coach **runs the learner's function** against the battery —
  every expected value below was obtained by running a reference solution, never guessed:

  ```
  python <skill-dir>/runtime/python/runner.py snippet.py
  ```

- **Process (rubric, softer):** composed in confirmed steps? contract for the edge inputs
  named and justified? composition explained (why each piece, why this contract)?

Coverage spans **distinct composition shapes** — **parse → filter → build a dict, with a
malformed-line contract** (parse_kv) / **two-pointer merge with a remainder drain**
(merge_sorted) / **group → aggregate → format** (summarize_scores) — no repeated structure. Per
`coaching-loop.md`, pose one drill, **hard-stop and wait**.

---

## AA1 — `parse_kv(text)` (compose: split lines → parse each → build dict; contract on malformed)

> **Your turn:** Write `parse_kv(text)` — parse newline-separated `key=value` lines into a dict.
> **Skip blank lines.** **Strip surrounding whitespace** from keys and values. If a key repeats,
> the **last** value wins. A line with **no `=`** is malformed — decide and state what you do
> with it.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery** (gold contract: malformed lines are **skipped**; split on the
**first** `=` so values may contain `=`)

```
parse_kv("a=1\nb=2")           = {'a': '1', 'b': '2'}    # basic
parse_kv("a=1\n\nb=2")         = {'a': '1', 'b': '2'}    # blank line skipped
parse_kv("a=1\na=2")           = {'a': '2'}              # duplicate key -> last wins
parse_kv("a=1\ngarbage\nb=2")  = {'a': '1', 'b': '2'}    # malformed line skipped
parse_kv("")                   = {}                      # empty input -> empty dict
parse_kv("x = 5")              = {'x': '5'}              # whitespace stripped
parse_kv("k=a=b")              = {'k': 'a=b'}            # split on FIRST '=' -> value keeps '='
status: ok
```

**Gold reference solution:**

```python
def parse_kv(text):
    result = {}
    for line in text.splitlines():     # (1) split into lines
        line = line.strip()
        if not line:                   # (2) skip blanks
            continue
        if "=" not in line:            # (3) contract: skip malformed
            continue
        key, _, value = line.partition("=")   # (4) split on the FIRST "="
        result[key.strip()] = value.strip()   # (5) build dict, last write wins
    return result
```

**Why.** This is genuine composition — **five pieces** (split lines, skip blanks, handle
malformed, split each line on the *first* `=`, build the dict) — and **three contract decisions**
the spec forces: blanks (skip), malformed lines (skip vs raise), and `=`-in-value (`partition`
keeps the first split, so `"k=a=b"` → `{'k': 'a=b'}`). Building in verified steps means
confirming each piece: run on `"a=1\nb=2"` first, then add the blank-line input, then the
malformed input, then the `=`-in-value input — each a confirmed point before the next.

**Diagnoses.** A learner who uses `line.split("=")` and unpacks into exactly two names
**crashes** on `"k=a=b"` (too many values) — a composition bug surfaced by the `=`-in-value case;
`partition` (or `split("=", 1)`) is the fix. A learner who never decides the malformed-line
contract has **left a hole in the spec** (Catalog §5c, entry 2 — the contract is part of the
spec). **Teach-it-back check:** can the learner say *why* `partition` over `split`, and *why*
skip-vs-raise on malformed? Naming the contract is the Advanced bar; a working function with an
unjustified contract is a partial pass.

---

## AA2 — `merge_sorted(a, b)` (compose: two-pointer walk + drain BOTH remainders)

> **Your turn:** Write `merge_sorted(a, b)` — given two already-sorted lists, return one sorted
> list containing all their elements (the merge step of mergesort). Do **not** call `sorted()`.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
merge_sorted([1, 3, 5], [2, 4, 6]) = [1, 2, 3, 4, 5, 6]   # interleave
merge_sorted([], [1, 2])           = [1, 2]               # one side empty
merge_sorted([1, 2], [])           = [1, 2]
merge_sorted([1, 1], [1])          = [1, 1, 1]            # duplicates across both
merge_sorted([1, 5, 9], [2, 3])    = [1, 2, 3, 5, 9]      # EDGE: a's tail [5,9] must drain
merge_sorted([], [])               = []
status: ok
```

**Gold reference solution:**

```python
def merge_sorted(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):   # (1) two-pointer interleave
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:])                  # (2) drain whatever is left of a
    out.extend(b[j:])                  # (3) drain whatever is left of b
    return out
```

**The naive miss (runner-confirmed):**

```python
def merge_naive(a, b):
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out                          # FORGOT to drain the remainders
```
```
merge_naive([1, 5, 9], [2, 3]) = [1, 2, 3]    # WRONG -- drops a's tail [5, 9]
```

**Why.** The `while` loop stops the instant **either** list is exhausted — so the **other
list's tail is left behind.** The two `extend` lines that drain the remainders are not optional;
they are pieces 2 and 3 of the composition. This is the canonical case where **building in
verified steps catches the forgotten piece**: run the unequal-length input `([1,5,9], [2,3])`
and you *see* `[1, 2, 3]` from the naive version — the missing tail is obvious. Writing the loop
and the drains together and running only at the end (big-bang) is exactly how the remainder bug
ships.

**Diagnoses.** A learner who writes only the `while` loop has **stopped composing before the
contract is met** (Catalog §5c, entry 1 — big-bang / not building on confirmed pieces) — the
loop is a confirmed *piece*, but the *function* is unfinished. The unequal-length case is the
discriminating input; an equal-length test (`[1,3,5]`/`[2,4,6]`) hides the bug. **Teach-it-back
check:** can the learner explain *why* the loop alone is insufficient (it terminates on the
first exhausted list)? Using `sorted(a + b)` is a non-answer — it ignores the "don't call
sorted / this is the merge step" spec and discards the linear-merge skill (over-/wrong-
composition).

---

## AA3 — `summarize_scores(rows)` (compose: group → average → round; contract on empty)

> **Your turn:** Write `summarize_scores(rows)` — given a list of `{"name": str, "score":
> number}` dicts, return `{name: average_score}` where each average is **rounded to 1 decimal
> place**. A name may appear **multiple times** (average all of that name's scores).
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
summarize_scores([{"name": "a", "score": 10}, {"name": "b", "score": 20}]) = {'a': 10.0, 'b': 20.0}
summarize_scores([{"name": "a", "score": 10}, {"name": "a", "score": 20}]) = {'a': 15.0}   # EDGE: averaged
summarize_scores([])                                                       = {}            # empty -> {}
summarize_scores([{"name": "a", "score": 0}])                              = {'a': 0.0}    # score 0 kept
summarize_scores([{"name": "a", "score": 1}, {"name": "a", "score": 1},
                  {"name": "a", "score": 2}])                              = {'a': 1.3}    # 4/3 -> 1.3
status: ok
```

**Gold reference solution:**

```python
def summarize_scores(rows):
    totals = {}
    counts = {}
    for row in rows:                           # (1) group: accumulate per name
        name = row["name"]
        totals[name] = totals.get(name, 0) + row["score"]
        counts[name] = counts.get(name, 0) + 1
    result = {}
    for name in totals:                        # (2) aggregate + (3) format
        result[name] = round(totals[name] / counts[name], 1)
    return result
```

**Why.** Three composed pieces — **group** (accumulate a running total *and* count per name),
**aggregate** (total / count), **format** (round to 1 decimal). The **multi-row-per-name** case
is the edge a naive `{row["name"]: row["score"] for row in rows}` misses — that dict-comprehension
**overwrites** earlier scores instead of averaging, returning `{'a': 20}` for the repeat case.
The empty-input contract (`{}`) falls out naturally. Building in steps: confirm the grouping on
the two-distinct case first, then add the **repeat** input and confirm `{'a': 15.0}`, then the
rounding input (`4/3 → 1.3`, the runner pins it — don't guess banker's-rounding behavior).

**Diagnoses.** A learner who writes the dict-comprehension has **happy-path-only composition**
(Catalog §5c, entry 2): the all-distinct-names input passes, the duplicate-name input is wrong.
A learner who keeps a running average instead of total+count usually mis-handles the third score
(an incremental-mean bug) — the `4/3 → 1.3` case discriminates. **Teach-it-back check:** can the
learner explain *why* total+count beats overwriting, and confirm the rounding by running rather
than asserting `round(4/3, 1)`? Reasoning from the run (not from a guess about `round`) is the
Advanced process bar.
