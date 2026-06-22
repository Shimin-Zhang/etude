# B3 — Working exemplars (testing & correctness)

Golden drills for the **Working** tier of module B3: a function where the **happy path
passes but a boundary/degenerate case fails**. Two drill types: **write a test that catches
the bug** (executable — the coach runs the learner's test against the **buggy** impl, which
must **fail** with `status: error`, and against the **fixed** impl, which must **pass** with
`status: ok`), and **state the contract** (rubric — pre/post/invariants in behavior terms).
The runner is the ground truth (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

A test that **passes on the buggy implementation is vacuous** and is graded a fail no
matter how it reads (§5c "test that cannot fail"; the operational form of Dijkstra). Both
implementations and both verdicts below were **runner-verified during authoring**. Coverage
spans distinct parameter-space regions (order bug / boundary bug / contract). Pose one,
**hard-stop, wait** (`coaching-loop.md`).

---

## W1 — Write a test that catches the bug (order not preserved)

**Buggy implementation** (the learner is shown this):

```python
def dedupe(xs):
    """Return the elements of xs with duplicates removed,
    PRESERVING first-seen order."""
    return list(set(xs))        # BUG: set() loses order
```

**Fixed implementation** (held by the coach for grading):

```python
def dedupe(xs):
    seen = set()
    out = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
```

> **Your turn:** Write a single assertion (a test) that **fails** on the buggy version
> above but **passes** once the bug is fixed. What input exposes it?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold test + runner verification**

The contract promises **order preservation**, so the test must use an input whose
de-duplicated order differs from `set()` ordering:

```python
got = dedupe([3, 1, 3, 2, 1])
assert got == [3, 1, 2], f"order not preserved: got {got}"
```

- **Against the buggy impl** → `status: error`,
  `AssertionError: order not preserved: got [1, 2, 3]` (the test **catches the bug** ✓).
  *(The `got [1, 2, 3]` value comes from the learner's own assertion message; a **bare**
  `assert dedupe(...) == [...]` would emit only `AssertionError` with no value — the
  message form is what surfaces the actual output.)*
- **Against the fixed impl** → `status: ok`, `"test passed"` (the test **passes** ✓).

**Why it must target order.** A weak test like `assert sorted(dedupe([1, 2, 3])) == [1, 2, 3]`
checks only the *set of elements*, not the order — and it **passes on the buggy impl**
(runner-verified `status: ok`). That is a **vacuous** test for this contract: it cannot
fail on the actual bug. The discriminating input must have its first-seen order *differ*
from numeric/set order (e.g. start with the larger value).

**Diagnoses.** A test that asserts only membership / sortedness reveals the learner is
testing a *weaker* contract than the function promises — the "asserts something trivially
true / too loose" gap (Catalog §5c, "test that cannot fail"). The coach **runs the
learner's test against the buggy impl**: if it passes, the test is vacuous, full stop —
"green on the buggy version means it specifies nothing." (Dijkstra EWD249.)

---

## W2 — Write a test that catches the bug (boundary off-by-one)

**Buggy implementation** (shown to the learner):

```python
def count_in_range(xs, lo, hi):
    """Count how many elements of xs are in the CLOSED interval [lo, hi]
    — both ends inclusive."""
    return sum(1 for x in xs if lo <= x < hi)    # BUG: hi excluded (should be <=)
```

**Fixed implementation** (held by the coach):

```python
def count_in_range(xs, lo, hi):
    return sum(1 for x in xs if lo <= x <= hi)   # closed interval, hi inclusive
```

> **Your turn:** Write one assertion that **fails** on the buggy version and **passes** on
> the fix. Which input exposes the off-by-one?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold test + runner verification**

The bug only bites when an element sits **exactly on the `hi` boundary**, so the test must
put a value there:

```python
got = count_in_range([1, 5, 10], 1, 10)
assert got == 3, f"hi boundary excluded: got {got}"
```

- **Against the buggy impl** → `status: error`,
  `AssertionError: hi boundary excluded: got 2` (the element `10` on the `hi` boundary is
  wrongly excluded — bug **caught** ✓). *(As in W1, the `got 2` value comes from the
  learner's own assertion message; a bare `assert` would print only `AssertionError`.)*
- **Against the fixed impl** → `status: ok`, `"test passed"` ✓.

**Why it must hit the boundary.** A test whose values avoid the `hi` edge —
`assert count_in_range([2, 5, 8], 1, 10) == 3` — **passes on the buggy impl**
(runner-verified): nothing equals `10`, so the half-open bug is invisible. Boundary-value
analysis says put a representative **at** the boundary, exactly where `<` vs `<=` flips.

**Diagnoses.** Choosing interior-only test values is the **missed-boundary** gap (Catalog
§5c, entries 1 & "missing boundary"; Myers BVA). The coach grades by **running the test on
both impls** — a test that doesn't fail on the buggy version has not caught the off-by-one,
regardless of intent.

---

## W3 — State the contract (precondition, postcondition, invariants)

```python
def binary_search(xs, target):
    """xs is a list sorted in non-decreasing order. Return an index i such that
    xs[i] == target, or -1 if target is not present."""
    lo, hi = 0, len(xs) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if xs[mid] == target:
            return mid
        elif xs[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

> **Your turn:** State this function's **contract** — its precondition, its postcondition,
> and any invariant it relies on. (Describe what it *promises*, not how the loop works.)
>
> (Take your best guess — wrong attempts are useful data.)

**Gold contract (rubric grading — `drill-generation.md` §3)**

- **Precondition:** `xs` is sorted in **non-decreasing** order. (The function is *wrong* —
  not just slow — on unsorted input; sortedness is a caller obligation it does not check.)
- **Postcondition:** returns an index `i` with `xs[i] == target` when `target` is present;
  returns `-1` when it is absent. (Note the contract does **not** promise *which* index is
  returned when there are duplicate `target` values — that is left unspecified.)
- **Invariant (internal):** at every loop step, if `target` is in `xs` at all, its index is
  within `[lo, hi]`; the window `[lo, hi]` only ever shrinks. This is *why* it terminates
  and is correct — but it is the *mechanism*, secondary to the pre/post promise.

**Rubric (binary, score each):** (a) names the **sortedness precondition** (the load-bearing
one — most-missed)? (b) states **both** halves of the postcondition (found → valid index;
absent → `-1`)? (c) describes the promise in **behavior** terms, not by narrating the loop?
(d) *bonus:* notes the **duplicate** case is unspecified?

**Diagnoses.** A learner who describes *how the loop narrows the window* but never states
the **sorted-input precondition** is **testing/▸specifying the implementation, not the
contract** (Catalog §5c, "asserts on implementation"). Missing the precondition is the
highest-value gap: it is exactly the input class (unsorted list) where a happy-path suite
of pre-sorted inputs would *pass* while the function silently returns `-1` for present
values. This is a **judgment call graded against the rubric, not a machine-verifiable
answer** (`drill-generation.md` §3). (Contract/oracle thinking; Barr et al. 2015.)
