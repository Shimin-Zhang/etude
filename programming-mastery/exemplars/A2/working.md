# A2 — Working exemplars (code reading & chunking)

Golden drills for the **Working** tier of module A2: an **unfamiliar 30–50-line** snippet
(or a plan to recognize / a lying name to catch). **Summarize in 1–3 sentences**, and
either **name the plan** or **spot the misleadingly-named** variable/function. Grading is
**mixed** (A2 §5d): the *summary* and *plan/beacon* parts are **rubric-graded** against the
**gold summary** + the **summary rubric** (§5d) given here; any embedded "what does it
return?" is **runner-verified** — every such key below was obtained by **running the
snippet** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct skills (summarize-unfamiliar / recognize-plan /
catch-lying-name). Pose one, **hard-stop, wait** (`coaching-loop.md`).

> **Summary rubric** (A2 §5d), applied to grade every summary below:
> **(1) Purpose, not paraphrase** (required) · **(2) Right chunks/plan named** ·
> **(3) Beacon-justified & behavior-checked.** Pass = ≥2 of 3 **with (1) met**; a
> mechanism-level summary that misses purpose is a **partial pass**.

---

## W1 — Summarize an unfamiliar 30–50-line snippet

```python
def analyze(series, window):
    if window <= 0 or window > len(series):
        return None
    current = sum(series[:window])
    best_sum = current
    best_start = 0
    for i in range(window, len(series)):
        current += series[i]
        current -= series[i - window]
        if current > best_sum:
            best_sum = current
            best_start = i - window + 1
    return {
        "best_sum": best_sum,
        "start": best_start,
        "end": best_start + window - 1,
        "values": series[best_start:best_start + window],
    }

readings = [4, -1, 2, 1, -5, 4, 6, -2, 3, 1]
print(analyze(readings, 3))
print(analyze(readings, 0))
```

> **Your turn:** Read this for structure, then **summarize what `analyze` does in 1–3
> sentences** (purpose, not a line-by-line retelling). Name the **plan** and the **beacon**
> that revealed it.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (for grading any "what does it return?" follow-up)

```
stdout: "{'best_sum': 8, 'start': 5, 'end': 7, 'values': [4, 6, -2]}\nNone\n"
status: ok
```

So `analyze(readings, 3)` returns the window `[4, 6, -2]` at indices 5–7 (sum **8**, the
largest of any length-3 window), and `analyze(readings, 0)` returns **`None`** (invalid
window). *(Brute-forcing all length-3 window sums gives `[5, 2, -2, 0, 5, 8, 7, 2]` →
max 8 at start 5 — confirming the slide is correct.)*

**Gold summary** (the standard to grade against)

> *"`analyze` finds the contiguous block of `window` consecutive elements in `series`
> whose sum is the largest, and returns that block's sum, its start/end indices, and its
> values (or `None` if the window size is invalid). It uses a **sliding window**: it
> computes the first window's sum, then slides one step at a time, adding the entering
> element and subtracting the leaving one, tracking the best sum seen."*

- **Plan:** **sliding-window maximum-sum.** **Beacons:** the paired
  **`current += series[i]; current -= series[i - window]`** (add-one / drop-one = a window
  *sliding*, the compound beacon), the **`if current > best_sum`** running-best guard, and
  the up-front **validity guard** returning `None`.

**Diagnoses.** *"It loops over the series adding and subtracting elements and tracks a best
value"* is a **partial pass** — accurate at the mechanism level but **missing the purpose**
(the *maximum-sum window*); criterion 1 fails (§5c "described the mechanism, not the
intent"). A summary that just re-narrates each line is **reading line-by-line** (§5c,
entry 1). Mistaking the add/subtract pair for "it sums the whole list" is **missing the
sliding-window beacon.**

---

## W2 — Recognize the plan / idiom

```python
def organize(pairs):
    table = {}
    for k, v in pairs:
        if k not in table:
            table[k] = []
        table[k].append(v)
    return table

events = [("err", 1), ("ok", 2), ("err", 3), ("warn", 4), ("ok", 5), ("err", 6)]
print(organize(events))
```

> **Your turn:** What **plan/idiom** is this loop? Name it, cite the beacon, and say in one
> sentence what `organize` produces. (Bonus: what does it return for `events`?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "{'err': [1, 3, 6], 'ok': [2, 5], 'warn': [4]}\n"
status: ok
```

So it returns **`{'err': [1, 3, 6], 'ok': [2, 5], 'warn': [4]}`**.

**Gold answer** (rubric-graded)

> **Plan:** **group-by / bucketing** (accumulate-into-dict-of-lists). **Beacon:** the
> **`if k not in table: table[k] = []`** (lazy-init the bucket) **followed by
> `table[k].append(v)`** (add to the bucket) — the append, not a skip, is what makes it a
> *group-by* rather than a *dedupe*. **Summary:** *"groups the value of each `(key, value)`
> pair into a list under its key, preserving order — i.e. buckets the events by their
> label."*

**Diagnoses.** Calling this *"removes duplicate keys"* is the **wrong-plan** error — the
reader saw `if k not in table` and pattern-matched to *dedupe*, missing that the
**`append`** (not a `continue`/skip) is the **disconfirming beacon** that makes it a
group-by (§5c "wrong plan"; Brooks 1983 — the hypothesis must be confirmed against the
code). The fix is Brooks' verification loop: bind "dedupe" to the lines and the `append`
breaks it.

---

## W3 — Spot the misleadingly-named function/variable (beacon vs reality)

```python
def sort_desc(values):
    total = 0
    for v in values:
        total += 1
    ordered = sorted(values)
    return ordered, total

result, total = sort_desc([4, 1, 3, 2])
print(result)
print(total)
```

> **Your turn:** Two names here **lie**. Read the **behavior** (not the names). What does
> `sort_desc` actually return — and where does the name disagree with what the code does?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[1, 2, 3, 4]\n4\n"
status: ok
```

So `result` is **`[1, 2, 3, 4]`** (sorted **ascending**) and `total` is **`4`**.

**Gold answer** (rubric-graded; behavior confirmed by the runner)

Two **discourse violations** (Soloway & Ehrlich 1984):

1. **`sort_desc` sorts *ascending*, not descending.** The beacon `sorted(values)` with no
   `reverse=True` is plain ascending sort; the `_desc` in the name is a **lying
   name-beacon.** Behavior wins: it returns `[1, 2, 3, 4]`.
2. **`total` holds a *count*, not a sum.** The chunk `total = 0; for v in values: total +=
   1` increments by **1** each pass (ignoring `v`), so it computes `len(values) == 4` — a
   **count**, despite the name `total` suggesting an accumulated sum.

**Summary:** *"`sort_desc` returns `values` sorted **ascending** together with the **count**
of elements — both names misdescribe the behavior."*

**Diagnoses.** Answering *"it returns the list in descending order and the total of the
elements"* is **anchoring on lying beacons** — trusting `sort_desc` and `total` over the
behavior, the exact discourse-violation trap that costs skilled readers most (§5c "lying
name"; Soloway & Ehrlich 1984). The fix is the model's guard rail: when a name and the
behavior conflict, **simulate and let behavior win** (A1). Here the runner settles it —
this is *why* "what does it return?" is run, not guessed.
