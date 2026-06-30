# F3 — Working exemplars (learning new languages & frameworks fast)

Golden drills for the **Working** tier of module F3: one construct in a context the learner
hasn't seen, where the analogy is **more tempting** and **survives a shallow look** (intent
and execution diverge). The learner predicts under the analogy, the coach **runs it**, and
the learner must then **articulate the execution-model reason** the analogy broke — not just
"it's different." Grading is **hybrid**: the prediction is **executable** (run, never guess);
the *mapping + execution-model reason* is **rubric-graded** and softer. Every prediction key
was obtained by **running the snippet through the runner**:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct construct families (default-argument binding / identity vs
equality / slice-copy depth), three source analogies (C++/Java "fresh locals" · Java `==`
reference · value-semantics or JS spread), and three artifacts (stdout across calls /
identity bools / mutation seen through an alias) — no repeated gotcha. Pose one,
**hard-stop, wait** (`coaching-loop.md`).

---

## Wkg-1 — Mutable default argument (false friend from "fresh locals each call")

> You know **C++ / Java / JavaScript**. There, a function's locals (and any default you'd
> set up) are **fresh on every call** — `acc` starts empty each time.

```python
def add(x, acc=[]):
    acc.append(x)
    return acc

print(add(1))
print(add(2))
```

> **Your turn:** Map `acc=[]` onto "a fresh empty list each call" and predict both lines.
> Then say *when* `acc=[]` actually runs.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "[1]\n[1, 2]\n"
status: ok
```

So `add(1)` is `[1]` and `add(2)` is `[1, 2]` — the list **persists** across calls. Under the
"fresh each call" analogy you would have predicted `[1]` then `[2]`. False friend.

**Gold mapping.** *Analogy:* a default/local is re-initialized per call. *Classify:*
**false friend** — same "default parameter" surface, different timing. *Why (execution
model):* the default expression `[]` is evaluated **once, at function-definition time**, and
that single list is stored on the function object (`add.__defaults__`) and **shared** by every
call that omits `acc`. So each call appends to the *same* list. *Repaired mapping:* the
"fresh container per call" idiom is `def add(x, acc=None): acc = [] if acc is None else acc`.
*The same/different line:* "default parameter" transfers as a concept; **when the default is
evaluated** does not.

**Why.** This passes a shallow look — `add(1)` alone returns `[1]`, exactly as expected. The
divergence only appears on the **second** call, which is why the drill needs two calls to
surface it (and why "it worked once" is not verification; corollary 1, §5c last entry). This
is also an A1 mechanism (mutable defaults) seen here as a **cross-language** false friend.

**Diagnoses.** Predicting `[1]` then `[2]` reveals modeling the default as **evaluated at
call time, fresh each call** — the imported "fresh locals" model — instead of once at
definition time with the object shared. (Catalog §5c, false-friend over-trust + "memorizes
syntax instead of porting the execution model.")

---

## Wkg-2 — `is` vs `==` and the small-int cache (false friend from Java `==`)

> You know **Java**. There, `==` compares **references** and you use `.equals()` for value
> equality — so for "are these the same value?" you reach for the operator that checks the
> objects themselves.

```python
x = 256
y = 256
print("256 is:", x is y)
a = int("257")
b = int("257")
print("257 is:", a is b)
print("257 ==:", a == b)
```

> **Your turn:** A Java developer maps "check the objects with `is`, like a reference
> `==`" and uses `is` to test value equality. Predict all three lines. Then: is `is` a safe
> way to compare two integers for equality?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "256 is: True\n257 is: False\n257 ==: True\n"
status: ok
```

So `256 is 256` → **`True`**, but `257 is 257` (built via `int("257")`) → **`False`**, while
`257 == 257` → `True`. Using `is` for equality "works" for `256` and then **silently fails**
for `257`. False friend.

**Gold mapping.** *Analogy:* Java `==` compares references; mapped onto Python `is`.
*Classify:* **false friend**, with a second-order trap. *Why (execution model):* Python's
`is` is **identity** (same object), not value. CPython **caches** the small integers
`-5..256`, so `x` and `y` both point at the *one cached* `256` object → `is` is `True` by an
implementation accident. `257` is outside the cache, and building it with `int("257")` forces
**two distinct objects**, so `is` is `False` even though `==` (value equality) is `True`.
*Repaired mapping:* use **`==`** for value equality; reserve **`is`** for identity and for the
singletons `None` / `True` / `False`. *The same/different line:* "compare two things" transfers;
**which operator means *value*** does not — and the cache makes the wrong choice *look* right.

**Why.** This is the worst kind of false friend: it **passes shallow testing** (small numbers)
and fails only on larger values, exactly where a quick REPL check with `5 is 5` would have
*confirmed* the wrong model. The boundary at 256/257 is an implementation detail — which is
why the coach **runs** it rather than asserting it (the cache edge is precisely a "verify,
don't trust" case; §5c last entry). *(Note: `257 is 257` written as bare literals in one line
can be `True` via compiler constant-folding; the drill uses `int("257")` to force distinct
objects and make the identity contrast unambiguous — itself a lesson in constructing a clean
test.)*

**Diagnoses.** Predicting `True` for all three reveals **mapping to the wrong analogy**
(`is`↦value-equality by surface similarity to a reference `==`) plus **one-green-run
over-trust** (the cached small int confirms a wrong model). (Catalog §5c, "maps to the wrong
analogy" + "treats a single green run as proof.")

---

## Wkg-3 — `b = a[:]` is a *shallow* copy (re-notated idiom + false friend)

> You know languages with **value semantics** (or JS, where `[...a]` / `a.slice()` copies an
> array). You've learned that **`a[:]` is the Python idiom for "copy a list"** — a genuine
> re-notation of "make a copy."

```python
a = [[1, 2], [3, 4]]
b = a[:]
b.append([5, 6])
b[0].append(99)
print("a:", a)
print("b:", b)
```

> **Your turn:** You "copied" `a` into `b` with `a[:]`. Predict `a` and `b` after the two
> mutations of `b`. Then: how deep does `a[:]` copy?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "a: [[1, 2, 99], [3, 4]]\nb: [[1, 2, 99], [3, 4], [5, 6]]\n"
status: ok
```

So `b.append([5, 6])` left `a` unchanged (`a` did **not** grow), but `b[0].append(99)`
**also changed `a[0]`** → `a` is `[[1, 2, 99], [3, 4]]`. The "copy" was only skin-deep.

**Gold mapping.** *Analogy:* `a[:]` (or `list(a)`, `[...a]`) copies the list. *Classify:*
**correct re-notated idiom *with* a false-friend depth limit.** *Why (execution model):*
`a[:]` builds a **new outer list** whose elements are the **same inner objects** (a *shallow*
copy). So rebinding/extending `b` itself (`b.append`) does not touch `a`, but **mutating a
shared inner list** (`b[0].append(99)`) is visible through `a[0]` — the inner lists are
aliased. *Repaired mapping:* for an independent nested structure use `copy.deepcopy(a)`; `a[:]`
/ `list(a)` are right only when the elements are immutable or sharing them is intended.
*The same/different line:* the *idiom* "`a[:]` copies a list" transfers; the **depth** of that
copy is the part you must verify.

**Why.** Half the idiom is a **true** friend (the outer copy works — `a` didn't grow) and half
is a **false** friend (the inner sharing). That mix is exactly why you run the **nested**
case, not the flat one: a flat-list test would have "confirmed" a deep-copy model that isn't
there. This is an A1 aliasing mechanism surfacing as a cross-language idiom limit.

**Diagnoses.** Predicting `a == [[1, 2], [3, 4]]` (unchanged) reveals **transliterating the
idiom** ("`[:]` = copy") without porting the execution model of *how deep* the copy goes — the
shared inner objects (aliasing) were not modeled. (Catalog §5c, "transliterates an idiom" +
"treats a single green run as proof.")
</content>
