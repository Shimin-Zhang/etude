# C1 — Advanced exemplars (systematic debugging)

Golden drills for the **Advanced** tier of module C1: a **subtle** bug whose **first hypothesis
is often wrong** (so a *discriminating test* is needed to falsify it), and where the **obvious
fix may not actually fix it** — forcing a **re-run** ("if you didn't fix it, it ain't fixed").
The learner runs the **full loop** unaided (observe → hypothesize → predict → test → narrow) and
explains *why*. Every **buggy output, every probe, every wrong-fix, and every correct fix below
— and the exception each raises — was obtained by running it through the runner**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three hard points in the parameter space: **mutation while iterating** (the
obvious "wrong-value" hypothesis is wrong — it's index drift), **input minimization /
delta-debugging** (minimizing the failing input exposes a **second** fault), and **generator
exhaustion** (the obvious fix just **moves** the bug). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7 (executable + hybrid, §5d): **fix is
executable** (apply + re-run the *original* failure); **hypothesis/diagnosis is rubric-graded**
(did they falsify a wrong first hypothesis with a discriminating test? catch that an obvious fix
fails on re-run? minimize? explain *why*?). At Advanced, ask for a **teach-it-back** of the
principle. A working fix via a lucky guess is a **partial pass** — flag it.

---

## A1 — Mutating a list while iterating over it

**Spec.** `remove_evens(xs)` removes every even number **in place**, leaving only the odds.

```python
def remove_evens(xs):
    for x in xs:
        if x % 2 == 0:
            xs.remove(x)
    return xs

print(remove_evens([2, 4, 6, 1, 3]))   # spec: [1, 3]
print(remove_evens([1, 2, 2, 3]))      # spec: [1, 3]
```

> **Your turn:** Run it and observe — note that some **even numbers survive**. The tempting
> hypothesis is "`remove()` deletes the wrong element." **Test that hypothesis** (instrument the
> loop), and if it's wrong, say what's *really* happening, then give a fix that re-runs clean.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the obvious hypothesis is *falsified* by the instrumented probe)

```
buggy   remove_evens([2, 4, 6, 1, 3]) -> [4, 1, 3]   <-- the 4 (even!) survived
        remove_evens([1, 2, 2, 3])    -> [1, 2, 3]   <-- a 2 survived

probe   (instrument the loop index/value as it goes):
        visiting index 0 -> value 2;  list now [2, 4, 6, 1, 3]
        visiting index 1 -> value 6;  list now [4, 6, 1, 3]      <-- 4 was SKIPPED
        visiting index 2 -> value 3;  list now [4, 1, 3]
        result: [4, 1, 3]

fixed   remove_evens([2, 4, 6, 1, 3]) -> [1, 3]
        remove_evens([1, 2, 2, 3])    -> [1, 3]     (fix: xs[:] = [x for x in xs if x % 2 != 0])
status: ok
```

**Gold hypothesis + diagnosis.** The tempting hypothesis — "`remove()` removes the wrong
*value*" — is **wrong**, and the probe falsifies it: `remove()` removes the right value each
time, but **deleting during iteration shifts the indices**. After `xs.remove(2)`, the list
becomes `[4, 6, 1, 3]` and the loop's internal cursor advances to **index 1** — which is now
`6`, **skipping the `4`** that slid into index 0. The real cause is **mutating a list while
iterating over it**: the for-loop walks by position, and every deletion left-shifts the unseen
tail. The fix iterates over a *separate* sequence or rebuilds the list:
`xs[:] = [x for x in xs if x % 2 != 0]` (filter into a new list, then assign back in place to
keep the in-place contract).

**A tempting wrong fix — and why it isn't a fix.** "Loop over indices and `del`":

```python
for i in range(len(xs)):
    if xs[i] % 2 == 0:
        del xs[i]
# remove_evens([2, 4, 6, 1, 3]) -> IndexError: list index out of range  (re-run exposes it)
```

The runner shows it **raises `IndexError`** — `range(len(xs))` is computed once at `5`, but
`del` shrinks the list, so `xs[4]` is eventually out of range. *If you didn't fix it, it ain't
fixed* — only the re-run reveals it.

**Model debugging trace (the gold).**

> *Observe:* ran it — `[4, 1, 3]`; an **even** number survived, which contradicts "removes
> evens." *First hypothesis:* `remove()` deletes the wrong value. *Discriminating test:*
> instrument the loop — it shows `remove()` deletes correctly but the loop **jumps from value 2
> to value 6, skipping 4**. *Falsified → re-hypothesize:* deleting during iteration shifts
> indices, so elements get skipped. *Predict the fix:* build a new list of odds (no in-place
> deletion during the walk). *Test:* `xs[:] = [x for x in xs if x % 2 != 0]` → `[1, 3]` for
> both cases. (Also tried the `range(len)`+`del` "fix" — re-ran → `IndexError`, so rejected it.)

**Diagnoses.** A learner who **anchors on "remove() is wrong"** after the probe disproves it is
in a **confirmation tunnel** (§5c). A learner who proposes the `range(len)`+`del` fix and
**doesn't re-run** ships an `IndexError` (§5c, "if you didn't fix it…"). A learner who can't
explain the **index shift** has the symptom, not the mechanism. Strong attempt: falsifies the
obvious hypothesis with instrumentation, names the iterate-while-mutating cause, fixes by
rebuilding, re-runs both cases clean. Bug class: **mutation while iterating** (Catalog §5c; an
A1 execution-model trace of the loop cursor exposes it).

---

## A2 — Input minimization: a parser crash that hides *two* bugs

**Spec.** `parse_config(lines)` parses `"key = value"` lines into a dict, skipping blank lines
and `#` comments.

```python
def parse_config(lines):
    cfg = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, value = line.split("=")
        cfg[key.strip()] = value.strip()
    return cfg

big = [
    "# app config",
    "host = localhost",
    "port = 8080",
    "",
    "feature_flags",            # a line with no '='
    "url = http://x/y?a=1&b=2", # a line with two '='
    "debug = true",
]
print(parse_config(big))
```

> **Your turn:** Run it — it crashes on this real config. **Minimize the input**: find the
> smallest input that still reproduces the crash. (Then keep minimizing — is there more than one
> offending line?) State each cause and give a fix that parses the whole `big` config.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (delta-debugging the input reveals **two** distinct faults, same symptom)

```
full input        -> ValueError: not enough values to unpack (expected 2, got 1)

minimize -> ["feature_flags"]              -> ValueError: not enough values to unpack (expected 2, got 1)
minimize -> ["url = http://x/y?a=1&b=2"]   -> ValueError: too many values to unpack (expected 2)   <-- DIFFERENT error!

fixed   parse_config(big) ->
        {'host': 'localhost', 'port': '8080', 'url': 'http://x/y?a=1&b=2', 'debug': 'true'}
        (fix: skip lines without '=', and split with maxsplit=1)
status: ok  (both bug paths: status error)
```

**Gold hypothesis + diagnosis.** Minimizing the failing input — dropping lines until the crash
disappears, then the smallest set that keeps it — isolates the trigger to a **single line**:
`"feature_flags"`. `line.split("=")` on a line with **no `=`** returns a 1-element list, and
`key, value = [...]` raises *"not enough values to unpack."* But minimization shouldn't stop at
the first trigger: the line `"url = http://x/y?a=1&b=2"` has **two `=`**, so `split("=")` returns
**three** parts and `key, value = [...]` raises *"too many values to unpack"* — a **second,
distinct fault** that the first one masked (the parser died on `feature_flags` before ever
reaching `url`). The fix handles both: skip lines without `=`, and use `split("=", 1)`
(maxsplit) so a `=` in the *value* doesn't over-split.

```python
        if "=" not in line:
            continue            # malformed line: skip (or raise a clear error)
        key, value = line.split("=", 1)
```

**Model debugging trace (the gold).**

> *Observe / make it fail:* ran `parse_config(big)` → `ValueError ... not enough values to
> unpack`. *Narrow by minimization:* removed lines until it stopped crashing, then re-added —
> the smallest failing input is `["feature_flags"]` (a no-`=` line). *Keep minimizing the
> remainder:* the `url` line alone gives a **different** error (*too many values to unpack*) —
> so there are **two** faults: missing `=` and extra `=`. *Predict the fix:* guard `"=" not in
> line` and use `split("=", 1)`. *Test:* re-ran the full `big` → parses to the expected dict, no
> crash. Confirmed both faults addressed.

**Diagnoses.** A learner who fixes only the no-`=` line and **declares done** missed the
second fault because they **stopped at the first reproduction** (§5c, no-minimization-mindset)
— re-running the `url` line shows the second `ValueError`. A learner who uses `split("=")`
without `maxsplit` "fixes" the no-`=` case but the two-`=` line still breaks (§5c, "if you
didn't fix it…") — have them re-run `big`. A learner who reads the traceback as "the parser is
broken" without minimizing scanned instead of narrowing (§5c). Strong attempt: minimizes to the
single trigger line, keeps going to find the second, fixes both, re-runs the whole config. Bug
class: **input minimization / delta-debugging exposing independent triggers** (Catalog §5c;
Zeller & Hildebrandt — ddmin; the traceback ties to C2).

---

## A3 — Generator exhausted on the second pass (the obvious fix just moves the bug)

**Spec.** `summarize(nums)` returns `(count, total)` for a sequence of numbers. Callers may pass
a **generator**, not just a list.

```python
def summarize(nums):
    count = sum(1 for _ in nums)     # first pass: consume to count
    total = sum(nums)                # second pass over the same nums
    return count, total

data = (x for x in [10, 20, 30])
print(summarize(data))               # spec: (3, 60)
print(summarize([10, 20, 30]))       # with a list: (3, 60)
```

> **Your turn:** Run it. With a **generator** it's wrong; with a **list** it's fine — that's a
> clue. Form a hypothesis and **test it** (try iterating the generator twice yourself). Then:
> beware the *obvious* fix — apply your fix and **re-run** to make sure it actually fixes it.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the obvious "reorder" fix *moves* the bug — re-run proves it)

```
buggy   summarize((x for x in [10,20,30])) -> (3, 0)    <-- total is 0 with a generator
        summarize([10, 20, 30])            -> (3, 60)   <-- fine with a list (the camouflage)

probe   data = (x for x in [10,20,30])
        first  list(data) -> [10, 20, 30]
        second list(data) -> []            <-- generator is EXHAUSTED after one pass

wrong fix (swap the two sums):
        summarize((x for x in [10,20,30])) -> (0, 60)   <-- bug just moved to `count`! NOT fixed

fixed   summarize((x for x in [10,20,30])) -> (3, 60)
        summarize([10, 20, 30])            -> (3, 60)    (fix: nums = list(nums) once, then reuse)
status: ok
```

**Gold hypothesis + diagnosis.** A generator is a **one-shot cursor**: iterating it the *first*
time (`sum(1 for _ in nums)`, to count) **consumes** it, so the *second* pass (`sum(nums)`, the
total) sees an **empty** sequence → `total == 0`. The discriminating test confirms it directly:
`list(data)` returns the values once, then `[]`. A **list** survives because it can be iterated
repeatedly — which is why the list call looks fine and masks the bug. The **obvious fix —
reorder so `total` runs first — does NOT work**: re-running shows `(0, 60)`, the bug simply moved
to `count` (whichever pass runs *second* gets the exhausted generator). The real fix
**materializes once**: `nums = list(nums)` at the top, then count and sum the list.

```python
def summarize(nums):
    nums = list(nums)        # one pass over the source; now reusable
    return len(nums), sum(nums)
```

**Model debugging trace (the gold).**

> *Observe:* ran it — `(3, 0)` with a generator, `(3, 60)` with a list. *Hypothesis:* the
> generator is **used up** by the count pass, so the total pass sees nothing. *Discriminating
> test:* `list(data)` twice → `[10,20,30]` then `[]`; confirms one-shot exhaustion. *Beware the
> obvious fix:* reordering the two sums — re-ran → `(0, 60)`; the bug **moved** to `count`, so
> reordering is **not** a fix. *Real fix:* `nums = list(nums)` once, then `len` + `sum`. *Test:*
> re-ran both the generator and list cases → `(3, 60)` for both. Confirmed.

**Diagnoses.** A learner who **reorders the sums and declares victory** without re-running
ships `(0, 60)` (§5c, "if you didn't fix it, it ain't fixed" — the canonical Advanced trap). A
learner who can't explain why the **list** works but the **generator** doesn't missed the
one-shot-cursor mechanism (and the camouflage). A learner who never tries iterating the
generator twice gave a hypothesis with **no discriminating test** (§5c). Strong attempt:
hypothesizes exhaustion, confirms with the double-`list()` probe, *rejects the reorder fix by
re-running*, materializes once, re-verifies both inputs. Bug class: **generator/iterator
exhaustion** (Catalog §5c; A1 — a generator is a stateful cursor, not a re-iterable list).
