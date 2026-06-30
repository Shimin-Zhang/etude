# C2 — Working exemplars (reading stack traces & errors)

Golden drills for the **Working** tier of module C2. Each is a **multi-frame** traceback
(2–4 frames) where intent and execution diverge and the **cause sits one frame above the
raise site**. The skill is to name the type, find the **deepest *your-code* frame**, **and
walk up to the cause** — distinguishing where the error *surfaced* (the site) from what *put
it there* (the cause). Every traceback below is **real runner output**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Working parameter space across **three exception classes and three
site-vs-cause shapes**: a `KeyError` whose cause is the caller's data (through a `<genexpr>`
frame); a `TypeError` on `None` from a missing `return` one frame up; and an
`UnboundLocalError` that is an **A1 scope** event, not a typo. Pose one, **paste the real
traceback when grading**, **hard-stop, wait** (`coaching-loop.md`). **How to grade** (§5d,
hybrid): **executable** = correct *class* + *deepest your-code frame*; **rubric** = the
**cause walk** (which frame holds the fault and why). Report separately. **A learner who
names the type and line but wants to fix the raise site when the cause is a frame up is a
partial pass — flag the site≠cause confusion** (the central C2 failure).

---

## W1 — `KeyError` through a generator expression: the cause is the caller's data

**What the code does.** `checkout` sums `price_for(catalog, s)` over a list of SKUs;
`price_for` looks up a nested dict.

```python
def price_for(catalog, sku):
    return catalog[sku]["price"]

def checkout(catalog, skus):
    return sum(price_for(catalog, s) for s in skus)

inventory = {
    "A1": {"price": 10, "qty": 3},
    "B2": {"price": 25, "qty": 1},
}
print(checkout(inventory, ["A1", "B2", "C3"]))
```

> **Your turn:** This raises. Name the **exception class**, the **deepest frame that is your
> code**, and **walk up to the cause** — which value, from which frame, is the real fault?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`, paths shown as `snippet.py`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 11, in <module>
    print(checkout(inventory, ["A1", "B2", "C3"]))
          ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "snippet.py", line 5, in checkout
    return sum(price_for(catalog, s) for s in skus)
  File "snippet.py", line 5, in <genexpr>
    return sum(price_for(catalog, s) for s in skus)
               ~~~~~~~~~^^^^^^^^^^^^
  File "snippet.py", line 2, in price_for
    return catalog[sku]["price"]
           ~~~~~~~^^^^^
KeyError: 'C3'
```

So: **class `KeyError`** (key `'C3'`); **deepest your-code frame: line 2** in `price_for`,
at `catalog[sku]` (the caret is under `catalog[sku]`, not `["price"]` — the *first*
subscription is what's missing); **cause**: walking up — line 5 `<genexpr>` passed `s ==
"C3"`, line 5 `checkout` iterated `skus == ["A1", "B2", "C3"]`, and line 11 passed
`["A1", "B2", "C3"]` while `inventory` only has keys `"A1"` and `"B2"`. **The fault is the
caller's data**: `"C3"` is requested but not stocked.

**Why.** Bottom line first: `KeyError: 'C3'` — a mapping lookup missed the key `'C3'`. The
deepest frame (line 2) is where it raised, and the caret tells you it's `catalog[sku]` (the
SKU lookup) that failed, *not* the inner `["price"]`. But line 2 is correct in isolation;
the **cause** is the value `sku == "C3"`, which you find by reading **up**: the `<genexpr>`
frame and `checkout` frame are just plumbing, and line 11 is where the unstocked `"C3"`
enters. The fix is upstream — validate SKUs, or use `catalog.get(sku)`.

**Note the `<genexpr>` frame.** `sum(... for s in skus)` runs the generator expression in
its **own frame** (`in <genexpr>`), so it appears in the stack between `checkout` and
`price_for`. That is normal — comprehensions and generator expressions get their own frames.

**Diagnoses.** A learner who points at line 11 (the top frame) as "the error" has the
**stack upside down** (§5c). A learner who wants to fix `price_for`'s line 2 has the **site**
but not the **cause** — the lookup line is fine; the data is wrong (§5c, site≠cause). A
learner thrown by the `<genexpr>` frame doesn't yet model comprehension frames. Strong read:
`KeyError 'C3'` + line 2 deepest + "the cause is the unstocked `"C3"` passed from line 11."

---

## W2 — `TypeError` on `None`: a missing `return` one frame up

**What the code does.** `find_user` returns the matching user or — implicitly — `None` when
none matches; `display` uppercases the found user's name.

```python
def find_user(users, uid):
    for u in users:
        if u["id"] == uid:
            return u
    # no explicit return -> None when not found

def display(users, uid):
    user = find_user(users, uid)
    return user["name"].upper()

people = [{"id": 1, "name": "Ada"}, {"id": 2, "name": "Linus"}]
print(display(people, 7))
```

> **Your turn:** This raises. Name the **exception class**, the **line** it raised on, and
> **the cause** — where did the offending value come from?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 12, in <module>
    print(display(people, 7))
          ~~~~~~~^^^^^^^^^^^
  File "snippet.py", line 9, in display
    return user["name"].upper()
           ~~~~^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
```

So: **class `TypeError`** (`'NoneType' object is not subscriptable`); **fault line 9**, at
`user["name"]` (caret under `user["name"]`); **cause**: `user` is `None`, because `display`
called `find_user(people, 7)` and **no user has `id == 7`**, so `find_user` fell off the end
of the loop and **returned `None`** (the implicit no-`return` path). The fault is the missing
not-found handling **one frame up**, not line 9.

**Why.** Bottom line first: `'NoneType' object is not subscriptable` — you tried to index
(`[...]`) something that is `None`. `None` showing up where an object was expected almost
always means **a function returned `None`** — either an explicit `return None`, or (here) a
function that *fell off the end* without returning. The deepest frame is line 9; the caret
says `user["name"]` is the operation. The **cause** is `user`, and walking up one frame:
`find_user(people, 7)` found no match (`id == 7` exists for nobody) and returned `None`. Fix:
handle the not-found case (`if user is None: ...`) or make `find_user`'s contract explicit.

**Diagnoses.** This is the canonical "`None` from a missing `return`" trap — an A1 event (a
function with no `return` yields `None`) surfacing as a `TypeError`. A learner who tries to
fix line 9 has the **site** but not the **cause** (§5c, site≠cause); the indexing is fine —
`user` should never have been `None`. A learner who names `TypeError` but not *why* it's
`None` has a partial cause read — push them to the missing-return frame. Strong read:
`TypeError` + line 9 + "`find_user` returned `None` for the unmatched `uid=7`."

---

## W3 — `UnboundLocalError`: a scope event, not a typo

**What the code does.** `tally` tries to count events, incrementing a module-level `count`.

```python
count = 0

def tally(events):
    for e in events:
        count = count + 1
    return count

print(tally(["a", "b", "c"]))
```

> **Your turn:** This raises (even though `count` is defined at the top!). Name the
> **exception class**, the **line**, and **the cause** — why doesn't it just use the global
> `count`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 8, in <module>
    print(tally(["a", "b", "c"]))
          ~~~~~^^^^^^^^^^^^^^^^^
  File "snippet.py", line 5, in tally
    count = count + 1
            ^^^^^
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

So: **class `UnboundLocalError`**; **fault line 5**, at the `count` on the *right-hand side*
(caret under `count`); **cause**: because `tally` **assigns** to `count` (line 5), `count` is
a **local** variable for the *entire* function — so the read `count + 1` on the first
iteration accesses a local that hasn't been bound yet. The module-level `count = 0` is a
*different*, global `count` that line 5 never consults. Fix: `global count` (rarely good), or
pass/return the count, or initialize a local before the loop.

**Why.** Bottom line first: `UnboundLocalError: cannot access local variable 'count' where it
is not associated with a value`. This is **not** a `NameError` (a typo / truly-undefined
name) — it is a **scope** event (A1 §5c): Python decides a name's scope *statically for the
whole function*. Any binding of `count` anywhere in `tally` (line 5's `count = ...`) makes
`count` local *everywhere* in `tally`, including the read on the same line. So the read
happens *before* the local is ever assigned → unbound local. The deepest frame (line 5) and
the caret (under the right-hand `count`) point exactly at the premature read.

**Diagnoses.** A learner who reads this as a `NameError` and hunts for a typo has misread the
**class** — it is the A1 scope rule, not a spelling mistake (§5c, UnboundLocal-as-NameError).
A learner who expects the function to "fall back to the global `count`" holds the **dynamic /
positional scope** misconception A1 targets ("local only after the assignment line") instead
of static-whole-function scope. Strong read: `UnboundLocalError` + line 5 + "assigning
`count` in the function makes it local for the whole function, so the read precedes its
binding; the global `count` is never used."
</content>
</invoke>
