# E3 — Working exemplars (code review)

Golden drills for the **Working** tier of module E3. Each diff is a **mix**: one real
**correctness bug**, one **style nit**, and one **design smell**. The skill is **triage +
communication** — **catch the correctness bug, prioritize it above the nit and smell**, mark
nits as `Nit:`, and write precise/kind feedback on each. Code review is rubric-graded
(`drill-generation.md` §3); every **correctness bug** below was **confirmed to misbehave by
running it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct correctness-bug classes (empty-case / truthiness-drop / mutable-default)
with genuinely-tempting decoys. Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to
grade** against module §7: **D1** = caught the correctness bug (not just the nits); **D2** =
ranked it above the nit/smell and didn't gate on the smell; **D3** = comment names the line,
gives impact, suggests a fix, kind tone, `Nit:` separation. **A review that catches the bug but
leads with the naming nit is a partial pass — flag the inverted priority** (the central E3
failure: Bacchelli & Bird's "commented on formatting while missing the real issue").

---

## W1 — Average rating: the empty-list edge case (bug) + a nit + a smell

**Spec.** `average_rating(ratings)` returns the mean of a list of integer ratings, **or `0.0`
for an empty list**.

```python
def average_rating(ratings):
    s = 0
    for r in ratings:
        s += r
    return s / len(ratings)
```

> **Your turn:** Review this diff. What would you comment? What's the **most important** thing,
> and how would you phrase the feedback?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the correctness bug is real)

```
average_rating([5, 4, 3]) -> 4.0   (correct on the happy path)
average_rating([])        -> ZeroDivisionError: division by zero   (spec wants 0.0)
# with the suggested fix: average_rating([]) -> 0.0, average_rating([5,4,3]) -> 4.0
status: ok  (bug path: status error)
```

**Prioritized issue list** (rank by consequence):
1. **Blocking (correctness):** empty `ratings` → `len(ratings) == 0` → `ZeroDivisionError`, but
   the spec says return `0.0`. The function crashes on a documented input.
2. **Design smell:** the empty-case contract isn't handled, and the manual accumulator loop
   reimplements `sum()`. Not a blocker, but worth raising.
3. **Nit:** `s` and `r` are terse; `total` reads clearer. Cosmetic only.

**Model review comment (the gold).** Lead with the bug; nits last, marked:

> **`return s / len(ratings)` (line 5) — blocking.** On an empty list this divides by zero and
> raises, but the spec says `average_rating([])` should return `0.0`. Add an early guard:
> `if not ratings: return 0.0`. While you're there, the loop can be `sum(ratings) / len(ratings)`.
>
> **Nit:** `s`/`r` → `total`/`rating` would read a bit clearer. Non-blocking.
>
> The happy-path math is correct — `[5, 4, 3]` gives `4.0` as expected.

**Diagnoses.** A learner who files the **naming nit first** (or *only*) and misses the empty-list
crash has **inverted priority** (§5c, nitpicking-while-missing-the-issue) — the canonical E3
failure; mark D2 down even if D1 caught the bug elsewhere. A learner who says "doesn't handle
empty input" but doesn't realize it *raises* (vs. returns a wrong number) has a **D1** gap — run
it and show the traceback. Strong review: blocking on the crash, names the input, gives the
guard, demotes naming to `Nit:`.

---

## W2 — Dedupe: the truthiness filter that swallows falsy values (bug) + a nit + a smell

**Spec.** `dedupe(items)` removes duplicates, **preserving first-seen order**. It must keep
falsy values that aren't duplicates — `0`, `""`, `None`, `False`.

```python
def dedupe(items):
    seen = []
    out = []
    for x in items:
        if x and x not in seen:
            seen.append(x)
            out.append(x)
    return out
```

> **Your turn:** Review this. What's the **most important** issue, and how would you phrase the
> feedback?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the correctness bug is real)

```
dedupe([1, 0, 1, 2, 0, ''])  -> [1, 2]        (spec wants [1, 0, 2, ''])
dedupe([0, False, None])     -> []            (spec wants the falsy values kept)
# with the suggested fix (drop `x and`, use a set): dedupe([1,0,1,2,0,'']) -> [1, 0, 2, '']
status: ok
```

**Prioritized issue list** (rank by consequence):
1. **Blocking (correctness):** the `x and ...` guard means any **falsy** element (`0`, `""`,
   `None`, `False`) is silently skipped. `dedupe([1, 0, 1, 2, 0, ''])` returns `[1, 2]`,
   dropping the `0` and `''` the spec requires.
2. **Design smell:** `seen` is a **list**, so `x not in seen` is O(n) per element → O(n²)
   overall. A `set` makes membership O(1). Matters for large inputs; not a blocker for small.
3. **Nit:** none material here — the structure is otherwise clean. (Don't manufacture one;
   §5c, over-reporting.)

**Model review comment (the gold).**

> **`if x and x not in seen:` (line 5) — blocking.** The `x and` test filters on *truthiness*,
> so it silently drops falsy-but-valid values: `0`, `""`, `None`, `False`. For
> `dedupe([1, 0, 1, 2, 0, ''])` this returns `[1, 2]` instead of `[1, 0, 2, '']` — real data
> loss. The membership check alone is what you want: `if x not in seen:`.
>
> While you're in here: `seen` as a list makes this O(n²); a `set` for `seen` makes membership
> O(1). Worth it if these lists can get large — your call.
>
> Order preservation and the overall shape look right.

**Diagnoses.** A learner who flags the **O(n²)** smell but not the truthiness bug has prioritized
performance over **correctness** — wrong order (§5c, priority inversion); the function is *wrong*,
not just slow. A learner who never runs it may not see the falsy-drop at all (§5c, did-not-trace)
— the `0`/`''` case is invisible on a skim. Strong review: blocking on the data loss with the
exact dropped values, smell demoted to optional.

---

## W3 — Merge defaults: the shared mutable default (bug) + a nit + a smell

**Spec.** `merge(overrides, defaults)` returns a **new** dict — `defaults` overlaid with
`overrides`. The caller's dicts must **not** be mutated, and repeated calls must be independent.

```python
def merge(overrides, defaults={}):
    for k in overrides:
        defaults[k] = overrides[k]
    return defaults
```

> **Your turn:** Review this. What's the **most important** issue, what's the impact, and how
> would you phrase the feedback?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the correctness bug is real)

```
a = merge({"x": 1})        # -> {'x': 1}
b = merge({"y": 2})        # -> {'x': 1, 'y': 2}   (spec wants {'y': 2}; leaked x from the prior call)
base = {"color": "red"}
merge({"color": "blue", "size": "L"}, base)
base                       # -> {'color': 'blue', 'size': 'L'}   (spec wants base UNCHANGED)
# with the suggested fix: independent calls, caller's base untouched
status: ok
```

**Prioritized issue list** (rank by consequence):
1. **Blocking (correctness):** two faults from one root —
   (a) the mutable default `{}` is created **once** and **shared across calls**, so state leaks
   between calls (`merge({"y": 2})` returns `{'x': 1, 'y': 2}`); and
   (b) when a real `defaults` dict is passed, the loop **mutates the caller's object** in place,
   violating "returns a new dict."
2. **Design smell:** the manual `for k in overrides` loop is just `dict.update`.
3. **Nit:** parameter naming is fine; no material nit. (Don't invent one.)

**Model review comment (the gold).**

> **`def merge(overrides, defaults={})` + the in-place writes (lines 1–3) — blocking.** Two
> problems, same root: (1) the default `{}` is evaluated **once at definition time** and shared
> by every call that omits `defaults`, so state leaks between calls — after `merge({"x": 1})`,
> `merge({"y": 2})` returns `{'x': 1, 'y': 2}`, not `{'y': 2}`. (2) When a caller *does* pass a
> dict, the loop mutates **their** object — `merge({...}, base)` changes `base` in place, but the
> contract says return a new dict. Fix both with a sentinel default and a copy:
> ```python
> def merge(overrides, defaults=None):
>     result = dict(defaults or {})
>     result.update(overrides)
>     return result
> ```
> That also replaces the manual loop with `update`.

**Diagnoses.** This is an **A1 notional-machine event** (mutable default evaluated once;
aliasing the caller's object) seen inside a review — a learner weak on A1 may not recognize it
(§2 soft-prereq; §5c, no-whole-change-model: the bug spans *calls*, invisible from one line). A
learner who flags `defaults={}` as "a style thing" has the symptom but not the **impact** (D3
partial) — push them to state the cross-call leak. Strong review: blocking, both manifestations
named, the sentinel-and-copy fix given.
