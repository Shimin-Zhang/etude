# D2 — Foundations exemplars (naming)

Golden drills for the **Foundations** tier of module D2. Each has a **single, clear** naming
problem on a familiar surface — no decoys. D2 is **hybrid**: the *lying-name* sub-claim is
**executable** (the coach **runs it; behavior wins**), and the *name-quality* sub-claim is
**rubric** (`drill-generation.md` §3). Every lying-name drill below was **confirmed to misbehave
by running it** (`drill-generation.md` §2) — the gold's catch is anchored to real output, never
guessed:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Foundations space with **different** faults: a **lie about the returned
quantity** (average→sum), a **lie about side effects** (sorted_copy mutates), and a **vague name**
(name-quality, no lie). Per `coaching-loop.md`, the coach poses one drill, then **hard-stops and
waits** — the gold is for *grading*, never shown before the learner attempts. **How to grade
(report the two verdicts separately, module §5d):** **D1 (honest?)** is settled by the run; **D2
(precise?) / D3 (consistent?)** are rubric. If the learner disputes the lie, *run it* and show the
output.

---

## F1 — `get_average` that returns the sum (lie about the returned quantity)

**Spec / promise in the name.** `get_average(nums)` should return the **mean** of the numbers.

```python
def get_average(nums):
    total = 0
    for n in nums:
        total += n
    return total          # returns the SUM, not the average
```

> **Your turn:** Does this function do what its name says? Predict what `get_average([2, 4, 6])`
> returns. Does the name match the behavior — and if not, what's the lie and how would you fix it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_f2.py
{"status": "ok", "stdout": "12\n", ...}

get_average([2, 4, 6])  ->  12        # the AVERAGE is 4; this returns the SUM (2+4+6)
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name lies.** `get_average` returns `12` for
  `[2, 4, 6]`; the average is `4`. The run convicts it.
- **D2 — Precise? (rubric):** the *fix* must make name and behavior agree.

**Model answer (the gold).**

> **The name lies — `get_average` returns the *sum*.** `get_average([2, 4, 6])` returns `12`, but
> the mean is `4`. The body accumulates a total and never divides by `len(nums)`. Two honest fixes:
> rename to `sum_of(nums)` (if the sum is what callers want), **or** — almost certainly the intent
> — keep the name and fix the behavior: `return total / len(nums)` (guarding the empty list:
> `return total / len(nums) if nums else 0`). A caller writing `avg = get_average(scores)` is
> getting a silently wrong number — no exception, just a wrong total masquerading as a mean.

**Diagnoses.** A learner who reads "`get_average` → it averages" and predicts `4` trusted the
**name over the machine** — the A1 superbug, authored-side (§5c, lying name). The bug class is
**lie about the returned quantity**. Catching "it returns the sum" but proposing only `total` as
the rename is a **partial D2** (vague — `total` doesn't say *of what*); push for `sum_of_scores`
or the divide-fix.

---

## F2 — `sorted_copy` that sorts in place (lie about side effects / over-claim)

**Spec / promise in the name.** `sorted_copy(items)` should return a **sorted copy**, leaving the
caller's list **untouched** (that's what "copy" guarantees).

```python
def sorted_copy(items):
    items.sort()          # sorts the caller's list IN PLACE
    return items

original = [3, 1, 2]
result = sorted_copy(original)
```

> **Your turn:** The name promises a *copy*. Does it keep that promise? Predict what `original`
> is after the call, and whether `result` and `original` are the same object. If the name lies,
> name the lie and fix it.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_f3.py
{"status": "ok", "stdout": "result  : [1, 2, 3]\noriginal: [1, 2, 3]\nsame object: True\n", ...}

result        ->  [1, 2, 3]
original      ->  [1, 2, 3]      # the caller's list was MUTATED (was [3, 1, 2])
result is original  ->  True     # it's the SAME object, not a copy
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name lies (over-claims).** `original` was mutated and
  `result is original` is `True`: there is **no copy**. The run convicts it.
- **D3 — Consistent? / D2 — Precise?:** the fix must either make a real copy or rename to the
  honest in-place verb.

**Model answer (the gold).**

> **The name over-claims — `sorted_copy` mutates the caller's list and returns the *same* object,
> not a copy.** After `sorted_copy([3,1,2])`, the original is now `[1,2,3]` and `result is
> original` is `True`. `items.sort()` sorts **in place**; there's no copy anywhere. Two honest
> fixes: (a) keep the name, make it true — `return sorted(items)` (builds a new list, leaves the
> argument alone); or (b) if mutating is intended, rename to `sort_in_place(items)` and (by
> convention) return `None`. A caller relying on "copy" — `s = sorted_copy(data)` expecting `data`
> intact — gets silent mutation-at-a-distance.

**Diagnoses.** This is an A1 mutation-vs-rebind event (`list.sort()` mutates; `sorted()` builds
new) wearing a **lying label** (§5c, over-claiming). A learner who predicts `original` stays
`[3,1,2]` modeled `.sort()` as pure — run it and show the mutation. Catching the mutation but
missing `result is original` (no copy at all) is a **partial D1**; the "same object" line is the
proof that "copy" is a lie, not just "also mutates."

---

## F3 — `tmp` / `p` / `r`: a vague name with no meaning (name-quality, no lie)

**Context.** This helper appears at a call site with no docs. The name tells you nothing.

```python
def tmp(p, r):
    return round(p + p * r, 2)
```

> **Your turn:** What does this function actually compute? (Don't guess from the name — figure it
> out.) Is `tmp` a good name? Are `p` and `r` good names? Propose better ones and say why.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (establishing what the name *should* describe — coach runs it even
to grade a naming judgment, module §5d)

```
$ python3 runtime/python/runner.py /tmp/D2_namequal.py
{"status": "ok", "stdout": "108.0\n59.99\n", ...}

tmp(100, 0.08)    ->  108.0      # 100 plus 8%
tmp(49.99, 0.20)  ->  59.99      # 49.99 plus 20%
```

So it computes **a price plus a tax/markup rate** → `price_with_tax`; `p` = `price`, `r` =
`tax_rate`.

**Two verdicts.**
- **D1 — Honest? (executable):** vacuously honest — `tmp` claims nothing, so it can't *lie*; it
  just *informs nothing*. (No run needed to convict a lie; the run is to learn the *meaning*.)
- **D2 — Precise? (rubric):** **No.** `tmp` names the *lifetime* ("temporary"), not the meaning —
  Ousterhout's #1 naming problem (too generic/vague). `p`/`r` are opaque single letters.

**Model answer (the gold).**

> **`tmp` is maximally vague — it names how long the value lives, not what it *is*.** Running it,
> it computes a price plus a rate: `tmp(100, 0.08)` is `108.0`. A reader at the call site
> (`x = tmp(item.price, region.rate)`) learns nothing from `tmp`. Rename to **`price_with_tax`**
> (or `gross_price`), and the parameters to **`price`** and **`tax_rate`**:
> ```python
> def price_with_tax(price, tax_rate):
>     return round(price + price * tax_rate, 2)
> ```
> Now the call site documents itself — no need to open the function. (`tmp` *can* be fine for a
> genuinely throwaway local whose entire use is visible in two lines; here it's a public helper,
> so it isn't.)

**Diagnoses.** A learner who shrugs "it's just a temp" accepted a name that names the lifetime,
not the meaning (§5c, vague name; Ousterhout Red Flag: Vague Name). Proposing `result` or `value`
as the rename is still a **partial D2** — those are also generic; push for a name that says *price
with tax*. The empirical backdrop: cryptic/single-letter names slow comprehension (Hofmeister
words 19% faster than letters; Lawrie words > single letters) — but note honestly this is
*direction*, not a proof that any one rename is "correct" (Feitelson: ~6.9% name agreement).
</content>
