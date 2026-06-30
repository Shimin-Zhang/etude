# A1 — Working exemplars (notional machine)

Golden drills for the **Working** tier of module A1: apply the execution model in a
context where **intent and execution diverge** — late-binding closures, aliasing vs.
rebinding, mutable default arguments, early return. Predict output **and** name the
state change. Every answer key was obtained by **running the snippet through the
runner** (`drill-generation.md` §2); the coach never guesses:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct regions of the parameter space (closure / aliasing /
mutable-default — no repeated gotcha). Pose one, **hard-stop, wait** (`coaching-loop.md`).
The W1 closure drill is the one in `assessment.md`'s A1 entry task — it prints
`12 12 12`.

---

## W1 — Late-binding closure capture (the `12 12 12` drill)

```python
def make_adders():
    fns = []
    for i in range(3):
        fns.append(lambda x: x + i)
    return fns

a, b, c = make_adders()
print(a(10), b(10), c(10))
```

> **Your turn:** What does this print, and *why*?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "12 12 12\n"
status: ok
```

So the printed line is `12 12 12` — **not** `10 11 12`.

**Why.** The three lambdas all close over the **same variable `i`**, not a per-iteration
snapshot of its value. A closure reads its captured variable **when it is called**, not
when it is defined. By the time any of `a`, `b`, `c` runs, `make_adders` has finished and
the loop has left `i` at its final value `2`. So every call computes `x + 2`:
`10 + 2 = 12`, three times. (The fix `lambda x, i=i: x + i` works because **default
arguments are evaluated at definition time** — capturing the *current* `i` per lambda.)

**Diagnoses.** A prediction of `10 11 12` reveals a **"copy-at-definition / snapshot"
model of closures** — the learner thinks defining the lambda photographs `i`'s value at
that moment, instead of capturing the variable and reading it at call time. Record the
exact gap as **"late-binding closure capture."** (Catalog §5c; `assessment.md` A1 entry
task; Python FAQ.)

---

## W2 — Aliasing vs. rebinding in one snippet

```python
a = [1, 2, 3]
b = a
a.append(4)
c = a + [5]
a = a + [6]
print(b, c, a)
```

> **Your turn:** What are `b`, `c`, and `a` at the end? Track which names point at which
> list object.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[1, 2, 3, 4] [1, 2, 3, 4, 5] [1, 2, 3, 4, 6]\n"
status: ok
```

So the printed line is `[1, 2, 3, 4] [1, 2, 3, 4, 5] [1, 2, 3, 4, 6]`.

**Why.** `b = a` makes `b` a **second label on the same list** — no copy. `a.append(4)`
**mutates that shared object in place**, so `b` sees it too → both are `[1, 2, 3, 4]`.
Then `c = a + [5]` and `a = a + [6]` each **build a new list and rebind** (`+` does not
mutate): `c` is a fresh `[1, 2, 3, 4, 5]`, and `a` is rebound to a fresh `[1, 2, 3, 4, 6]`.
Crucially, rebinding `a` does **not** drag `b` along — `b` still labels the original
(now `[1, 2, 3, 4]`) object.

**Diagnoses.** Predicting `b == [1, 2, 3]` reveals **no aliasing model** (thinks `b`
copied the data). Predicting `b` ends as `[1, 2, 3, 4, 6]` reveals the **"linked names"**
error — assuming rebinding `a` also moves `b`. Both stem from "names are boxes that hold
copied values" instead of "labels on shared objects; mutation is seen by all, rebinding
moves only one." (Catalog §5c, entries 2 & 3; Python FAQ.)

---

## W3 — Mutable default argument across calls + early return

```python
def collect(item, bin=[]):
    if item is None:
        return bin
    bin.append(item)
    return bin

print(collect(1))
print(collect(2))
print(collect(None))
```

> **Your turn:** What do the three `print` lines show?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "[1]\n[1, 2]\n[1, 2]\n"
status: ok
```

So the three lines are `[1]`, then `[1, 2]`, then `[1, 2]`.

**Why.** The default `bin=[]` is evaluated **once, at definition time**, and that single
list lives on the function object (`collect.__defaults__`). Every call that omits `bin`
rebinds the parameter to that **same shared list**. `collect(1)` appends → `[1]`.
`collect(2)` appends to the *same* list → `[1, 2]`. `collect(None)` takes the early
`return bin` without appending, but returns that same accumulated list → `[1, 2]`. The
early return changes *control flow*, not *which object* `bin` is.

**Diagnoses.** Predicting `[1]`, `[2]`, `[]` reveals the **"defaults re-initialized each
call" model** — the learner thinks `bin=[]` runs fresh on every call, instead of once at
definition time with the object shared across calls. (Catalog §5c; Python FAQ;
Hitchhiker's Guide.)
