# D2 — Working exemplars (naming)

Golden drills for the **Working** tier of module D2. Each name is **plausible-but-wrong** — the
mismatch is subtle enough to survive a skim, often "looking right" on the obvious input and
breaking on another. The skill is **catch the mismatch via the run, state the impact at the call
site, and propose a precise + honest fix.** D2 is **hybrid**: the lie is **executable** (run it;
behavior wins), the name quality is **rubric** — report the two verdicts separately (module §5d).
Every lie below was **confirmed by running it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans **distinct lie classes**: a **wrong return type** for a noun-count name
(`count_items`→bool), a **silent no-op** under an action verb (`save_user` drops falsy input), and
a **predicate returning a length** (`is_empty`→int). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade (module §7):** **D1** = caught the mismatch and the run
proves it; **D2/D3** = precise, honest rename or behavior fix, impact named. **Catching the lie but
proposing a vague rename is a partial pass — flag it.**

---

## W1 — `count_items` that returns a bool (wrong return type for the name's word-class)

**Spec / promise in the name.** `count_items(seq, target)` should return **how many times**
`target` appears — an **int count**.

```python
def count_items(seq, target):
    for x in seq:
        if x == target:
            return True       # returns a bool on first match
    return False
```

> **Your turn:** The name says "count." Does it return a count? Predict what
> `count_items([1, 2, 2, 3, 2], 2)` returns and its type. Then: does the name match the behavior,
> and what would a caller doing `n = count_items(...) ` then `n + 1` get?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_w1.py
{"status": "ok", "stdout": "returned: True\ntype: bool\nn + 1 = 2\n", ...}

count_items([1, 2, 2, 3, 2], 2)  ->  True   (type: bool)   # a "count" should be 3
n + 1                            ->  2       # True + 1 == 2  (silently wrong, no error)
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name lies.** It returns `True`, a **bool**, not the
  count `3`. And because `bool` is an `int` subclass, `n + 1` is `2` — **silently wrong, no
  exception.** The run convicts it.
- **D2 — Precise? (rubric):** the fix must reconcile the name's word-class ("count" → int) with the
  behavior.

**Model answer (the gold).**

> **The name lies — `count_items` returns a *bool*, not a count.** For `[1,2,2,3,2]` and target
> `2` it returns `True` (the value `2` occurs), not `3`. The word "count" promises an int; the body
> is actually a *membership test* that short-circuits on the first match. The danger is silent:
> `n = count_items(...)` then `n + 1` gives `2` (since `True == 1`), with **no error** to flag it.
> Two honest fixes: (a) if a count is wanted, make the behavior match — `return seq.count(target)`;
> (b) if a membership test is wanted, rename to the honest predicate — `def contains(seq, target):
> return target in seq`. Don't keep a "count" name on a bool.

**Diagnoses.** §5c **wrong return type for the name's word-class** ("count"/"num" implies int).
A learner who predicts `3` trusted the name; one who predicts `True` but says "that's basically a
count" missed that `bool` ≠ `int count` — run `n + 1` to show the silent-wrongness. The
"looks-right-by-luck" trap is real: callers only doing `if count_items(...)` never notice.

---

## W2 — `save_user` that silently saves nothing on falsy input (silent no-op)

**Spec / promise in the name.** `save_user(name)` should **persist** the user. The name promises
the postcondition "the user is saved."

```python
saved = []

def save_user(name):
    if not name:                 # silent guard
        return                   # returns None and saves NOTHING, no error
    saved.append(name)
    return name
```

> **Your turn:** A caller does `save_user(name)` for each name in a form. The name promises the
> user is persisted. Is that always true? Predict `saved` after `save_user("ada")` then
> `save_user("")`, and what each call returns.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies on one path; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_w2.py
{"status": "ok", "stdout": "returns: ada None\nsaved: ['ada']\n", ...}

save_user("ada")  ->  'ada'          # saved
save_user("")     ->  None           # NOT saved — and no error raised
saved             ->  ['ada']        # the empty name silently vanished
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name over-promises on a path.** `save_user("")` returns
  `None` and **saves nothing**, with no exception. The run shows `""` missing from `saved`. The
  caller believes the postcondition holds; it doesn't.
- **D2 — Precise? (rubric):** the fix must make the name honest about *when* it saves (and signal
  the skip).

**Model answer (the gold).**

> **The name lies on the empty-input path — `save_user` silently saves nothing when `name` is
> falsy.** `save_user("")` returns `None` and leaves `saved` as `['ada']`; the empty name just
> disappears with **no error**. The name promises persistence unconditionally, but a guarded path
> drops the input silently. The honest fix is to make the contract explicit: either **validate and
> signal** — `if not name: raise ValueError("name required")` (the caller learns the save didn't
> happen), or **document and return a status** the caller checks (`return False`/`return None`
> *with a name that admits it*, e.g. `try_save_user`). Silently returning `None` from a function
> named `save_user` is the trap — the caller has no way to know.

**Diagnoses.** §5c **silent no-op under an action verb**. A learner who says "it just skips empty
names, fine" missed that *the name promises it won't skip* and *the caller gets no signal* — the
gap is between the name's unconditional promise and the conditional behavior. Catching "it returns
None on empty" but not naming the **caller's false belief** is a **partial D2** — the impact (a
user the form thinks it saved) is the point.

---

## W3 — `is_empty` that returns a length (predicate returning a non-bool)

**Spec / promise in the name.** `is_empty(c)` is a **predicate** — it should return a **bool**:
`True` iff `c` is empty.

```python
def is_empty(c):
    return len(c)            # returns an int length, not a bool
```

> **Your turn:** `is_empty` looks fine — `is_empty([])` is falsy, `is_empty([1,2,3])` is truthy.
> But it's a predicate; does it return a *bool*? Predict `is_empty([1,2]) == True`. Does the name
> match the behavior?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies about its type; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_w3.py
{"status": "ok", "stdout": "is_empty([]): 0\nis_empty([1,2,3]): 3\nis_empty([1]) == True: True\nis_empty([1,2]) == True: False\n", ...}

is_empty([])          ->  0      # falsy, "looks" right
is_empty([1,2,3])     ->  3      # truthy, "looks" right
is_empty([1]) == True ->  True   # 1 == True -> True  (right by LUCK)
is_empty([1,2]) == True -> False # 2 == True -> False (!) the lie surfaces
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name lies about its type.** A predicate must return a
  `bool`; this returns an `int` length. It *looks* right in a plain `if`, and even
  `is_empty([1]) == True` is `True` **by luck** (`1 == True`), but `is_empty([1,2]) == True` is
  **`False`** — the run convicts it.
- **D2 — Precise? (rubric):** trivial honest fix.

**Model answer (the gold).**

> **The name lies about its type — `is_empty` returns a *length*, not a *bool*.** It rides on
> truthiness so it *looks* correct in `if is_empty(c):`, but it returns `len(c)` (an int). That
> bites the moment anyone compares to a bool: `is_empty([1]) == True` is `True` only because
> `1 == True`, while `is_empty([1,2]) == True` is `False` (`2 != True`). Predicates must return
> booleans (Ousterhout: "names of boolean variables should always be predicates"). Fix: `return
> len(c) == 0` (or `return not c`). One character of intent, and the name stops lying.

**Diagnoses.** §5c **wrong return type for a predicate**. The instructive part is the
**looks-right-by-luck** failure: a learner who tests only `[]` and `[1]` "confirms" the bug-free
illusion; the `[1,2] == True` case is what exposes the lie. This is why **behavior wins via the
run, not a skim** — the module's central executable lesson. Catching "it returns an int" earns D1;
the strong answer also shows the comparison that breaks.
</content>
