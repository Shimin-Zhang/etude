# B3 — Advanced exemplars (testing & correctness)

Golden drills for the **Advanced** tier of module B3: **property/invariant thinking** (what
must *always* hold regardless of input) and **finding the subtle correctness gap a naive
(even green, high-coverage) test suite misses**. Grading is **mixed** (`drill-generation.md`
§1d, §3): the property/case statement is rubric-graded, **then** executable-verified — the
coach encodes the property as an assertion and **runs it against a correct and a
deliberately-wrong implementation** to confirm it **accepts the right one and rejects the
wrong one** (a property that admits the bug is too weak; a property that rejects correct
code is false). Every check below was **runner-verified during authoring**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct moves (property strength / metamorphic relation / the gap a
covered suite misses). Pose one, **hard-stop, wait** (`coaching-loop.md`).

---

## A1 — What property must always hold? (and why one property is too weak)

```python
def my_sort(xs):
    """Return the elements of xs in non-decreasing order."""
    # implementation hidden — reason about the CONTRACT, not the code
```

> **Your turn:** Write down the **property/properties** that must hold for *any* correct
> `my_sort`, for **every** input. Then: is a single "the output is in order" property
> enough to catch a wrong sort? Why or why not?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold answer + runner verification**

A correct sort needs **two** properties, and **neither alone is sufficient**:

1. **Ordered (postcondition):** `all(out[i] <= out[i+1] for i in range(len(out)-1))`.
2. **Same multiset (invariant):** `Counter(out) == Counter(xs)` — the output is a
   *permutation* of the input (no element added, dropped, or duplicated).

**Why "ordered" alone is too weak** — demonstrated by running both properties against a
buggy sort that returns `sorted(set(xs))` (ordered, but **drops duplicates**), on
`xs = [3, 1, 2, 1]`:

```
ordered   on buggy sorted(set):  True     # the weak property is FOOLED
multiset  on buggy sorted(set):  False    # the strong property CATCHES the bug
ordered   on a correct sort:     True     # both accept correct code
multiset  on a correct sort:     True
```

So a suite that only checks orderedness passes a sort that silently discards duplicates.
You need the multiset property to pin "every element survives." (A third common property —
**idempotence**, `my_sort(my_sort(xs)) == my_sort(xs)` — is also true but, like ordered,
*too weak alone*: `sorted(set(...))` is idempotent too.)

**Rubric (binary):** (a) states **orderedness**? (b) states **multiset/permutation
preservation** (not just "same length" — same length is even weaker and passes
`[0,0,0,0]`)? (c) recognizes that **one property is insufficient** and can name an input
where a weak property is fooled? **Then executable-verify** the learner's property against
the planted `sorted(set(...))` impl.

**Diagnoses.** Stating only "it's sorted," or "same length," is the **too-weak property**
gap (Catalog §5c, "property that is too weak"). A property must hold the **same
falsifiability bar as a case**: reject wrong implementations *and* accept the right one
(Hughes 2019). "Same length" is the classic trap — it admits `[0,0,0,0]` for any
4-element input. (Claessen & Hughes 2000; the §3 transition rule applied to properties.)

---

## A2 — A metamorphic relation when there is no easy exact oracle

```python
def median(xs):
    """Return the median of the non-empty list of numbers xs."""
    # implementation hidden
```

> **Your turn:** You don't always want to hand-compute the expected median for every input.
> Name a **relation between different inputs/outputs** that must hold for *any* correct
> `median` — one you can check **without** knowing the exact answer in advance.
>
> (Take your best guess — wrong attempts are useful data.)

**Gold answer + runner verification**

The median is **invariant under permutation** of its input — reordering the elements must
not change the median. This is a **metamorphic relation** (Segura et al. 2016): a necessary
property linking two executions, checkable with no exact oracle:

```
median(xs) == median(any_permutation_of_xs)
```

Verified by running it on a buggy `median` that takes the middle *element* without sorting
(it assumes the input is pre-sorted) vs. a correct one, with `xs = [5,1,9,3,7]` and the
permutation `[9,3,1,7,5]`:

```
buggy: median([5,1,9,3,7]) = 9,  median([9,3,1,7,5]) = 1   -> relation holds: False  (bug CAUGHT)
good:  median([5,1,9,3,7]) = 5,  median([9,3,1,7,5]) = 5   -> relation holds: True   (correct OK)
```

The metamorphic relation catches the "assumes sorted input" bug **without** the test ever
needing to state that the true median is `5` — which is exactly the point of metamorphic
testing for functions where writing the exact oracle is tedious or hard (Barr et al. 2015,
the oracle problem). Other valid relations: adding a constant `c` to every element shifts
the median by `c`; scaling by a positive constant scales the median.

**Rubric (binary):** (a) names a relation that is **actually invariant** for a correct
median (permutation / shift / scale)? (b) the relation is checkable **without the exact
answer**? (c) it **rejects** a plausible wrong impl? **Then executable-verify** against the
no-sort buggy median.

**Diagnoses.** A learner who insists on asserting an exact value for every input has
**one-oracle tunnel vision** (Catalog §5c, "insists on exact-output"); they stall on
functions where the oracle is expensive. The fix is the metamorphic-relation tool. A
learner who proposes a *false* relation (e.g. "median of the concatenation equals the sum
of medians") fails rubric (a) — the coach runs it and shows it breaks on correct code.
(Segura et al. 2016; Hughes 2019.)

---

## A3 — Find the gap a naive (green, full-coverage) suite misses

```python
def first_repeated(xs):
    """Return the first element of xs that has ALREADY appeared earlier
    (i.e., the element at the first position that is a second occurrence),
    or None if every element is unique."""
    for i, x in enumerate(xs):
        if x in xs[i+1:]:          # BUG: 'does x appear LATER?' — not 'has x appeared BEFORE?'
            return x
    return None
```

And here is a suite someone wrote. It is **all green** and it **executes every line** of
the function (both the `return x` branch and the `return None` branch):

```python
assert first_repeated([1, 2, 3]) is None     # no repeat  -> covers 'return None'
assert first_repeated([1, 1, 2]) == 1         # repeat at front -> covers 'return x'
assert first_repeated([]) is None             # empty
# all pass; coverage looks complete
```

> **Your turn:** The suite is green and covers every line — but the function is **wrong**.
> Find an input that exposes the bug (and the suite misses), and say what the correct
> output is.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

A discriminating input is one where the first element **also recurs later**, so the buggy
"appears later?" check fires on it *before* reaching the element that is the true first
*second-occurrence*. For `xs = [1, 3, 3, 1]`:

```
good  first_repeated([1, 3, 3, 1]) = 3    # 3 (index 2) is the first value to repeat
buggy first_repeated([1, 3, 3, 1]) = 1    # 1 appears again later, so the bug returns it first
```

The correct answer is **`3`** (occurrences in order: `1@0, 3@1, 3@2` → the first *second
occurrence* is the `3` at index 2). The buggy version returns **`1`**, because `1` *does*
appear later (at index 3), so its forward-looking test matches the very first element. The
naive suite missed this because every one of its inputs had the first repeat at the front,
where "appears later" and "appeared before" happen to coincide.

**Why coverage didn't save it.** The suite achieves **100% line coverage and is green**,
yet says nothing about *ordering among multiple repeats* — the equivalence class it never
exercised. **Coverage measures what ran, not what was checked** (Inozemtseva & Holmes 2014):
once you've covered both branches, more of the same input shape adds no fault-detection
power. The gap is an *unexercised behavior class*, not an unexecuted line.

**Diagnoses.** A learner who concludes "the suite is green and full-coverage, so the code
is tested" has the **coverage-as-correctness** gap (Catalog §5c, "equates high coverage
with a good suite"; Inozemtseva & Holmes 2014) — *and* the meta-error of confusing "passes
my tests" with "correct" (Dijkstra). The coach grades by **running the learner's proposed
input** against the buggy impl to confirm it actually produces the wrong value; a proposed
input on which buggy and correct agree has not found the gap. Articulating *why* the gap
exists ("the suite never tested two repeats in a row") is the Advanced teach-it-back bar.
