# F3 — Advanced exemplars (learning new languages & frameworks fast)

Golden drills for the **Advanced** tier of module F3: a **genuinely-new** construct (no clean
analogy) or a false friend that **combines two mechanisms**. The learner builds/ports the
sub-model, predicts, the coach **runs it**, and the learner **explains why** and names the
analogy **and its limit** — and can teach back the general *port-and-verify* principle.
Grading is **hybrid**: the prediction is **executable** (run, never guess); the mapping +
execution-model explanation is **rubric-graded** and softer. Every prediction key was obtained
by **running the snippet through the runner**:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct construct families (generator laziness / context-manager
exception control / class-vs-instance attributes), three source analogies ("a function that
returns a list" · C++ RAII or Java try-with-resources or `try/finally` · Java field
declaration), and three artifacts (the **order** of side effects / **whether it raises** /
shared mutation across instances) — no repeated gotcha. Two of these turn on more than
`stdout` (one on the **order** of prints, one on **`status`**). Pose one, **hard-stop, wait**
(`coaching-loop.md`).

---

## Adv-1 — Generators are lazy & one-shot (genuinely-new construct; "returns a list" is a false analogy)

> You know functions that **build and return a list**. The natural analogy: `gen()` runs the
> body, collects the values, and hands them back.

```python
def gen():
    print("start")
    for i in range(3):
        print("yield", i)
        yield i

g = gen()
print("created")
first = next(g)
print("got", first)
```

> **Your turn:** Map `gen()` onto "a function that returns its values" and predict the
> **order** of the printed lines. Then: when does the body of `gen` actually run?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "created\nstart\nyield 0\ngot 0\n"
status: ok
```

So the order is `created` → `start` → `yield 0` → `got 0`. Under the "returns a list" analogy
you would have predicted `start`, `yield 0`, `yield 1`, `yield 2` **all at the `gen()` call**,
*then* `created`. Wrong order, wrong eagerness — the analogy is a false one.

**Gold mapping.** *Analogy:* a function that builds and returns a list. *Classify:*
**genuinely-new construct** — forcing the list analogy makes the prediction worse. *Why
(execution model):* a function containing `yield` is a **generator function**; calling it runs
**none** of the body — it returns a paused **generator object** (hence `created` prints
*before* any body line). Each `next(g)` **resumes the frame** until the next `yield`, returns
that value, and **pauses again**. So the first `next(g)` prints `start`, `yield 0`, yields `0`;
the body is **lazy** (runs on demand) and **one-shot** (a consumed generator yields nothing
more, and is not re-iterable). *Nearest partial analogy, with its limit:* it's like a Ruby/C#
**iterator** or a coroutine — *not* like a list; the value is a **suspended computation**, not
a materialized container. *Teach-back principle:* when no analogy holds, **build the notional-
machine sub-model directly** (a generator is a resumable frame), then reach for the nearest
partial analogy knowing where it stops.

**Why.** The whole point is *eagerness vs. laziness*, which the surface (`def`, a call,
`yield`) does not reveal. Only by running and watching the **order** of side effects can you
see that `gen()` did nothing until `next`. This is corollary 3 (stop forcing an analogy; build
the sub-model) made concrete.

**Diagnoses.** Predicting the body runs at `gen()` reveals **forcing a list analogy onto a
genuinely-new construct** — no "lazy cursor / resumable frame" sub-model, so the eager,
materialized "returns a list" picture is imported wholesale. (Catalog §5c, "forces an analogy
onto a genuinely-new construct" + "maps to the wrong analogy.")

---

## Adv-2 — `with` / `__exit__` can *suppress* the exception (false friend from RAII / `try/finally`)

> You know **C++ RAII** / **Java try-with-resources** / **`try/finally`**: a cleanup action
> runs deterministically when the block exits, **whether or not** an exception was thrown — but
> the exception still **propagates** after cleanup.

```python
class Ctx:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, *a):
        print("exit")
        return True  # truthy return value

with Ctx() as c:
    print("body")
    raise ValueError("boom")
print("after")
```

> **Your turn:** Map `with` onto try/finally and predict: does `after` print? Does the
> `ValueError` propagate out (does the program end with an error)?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "enter\nbody\nexit\nafter\n"
status: ok
```

So it prints `enter` → `body` → `exit` → **`after`**, and the program exits **cleanly**
(`status: ok`) — the `ValueError` **does not propagate**. Under the try/finally analogy you
would have predicted `enter`, `body`, `exit`, then the `ValueError` **raised** (and `after`
**never** printed). False friend.

For contrast, the genuine try/finally — *runner-verified* — does **not** suppress:

```python
try:
    print("body")
    raise ValueError("boom")
finally:
    print("cleanup")
print("after")
```
```
stdout: "body\ncleanup\n"
status: error   ->  ValueError: boom    ("after" never prints)
```

**Gold mapping.** *Analogy:* `with` ≈ RAII / try-with-resources / `try/finally` for
deterministic cleanup. *Classify:* **mostly true friend, with a sharp false-friend twist.**
*Why (execution model):* `with` runs the object's `__enter__`, then the body, then
**`__exit__(exc_type, exc, tb)`** on the way out. The true-friend part: `__exit__` always runs,
like `finally`. The twist: if the body raised, **`__exit__`'s return value decides whether the
exception is suppressed** — a **truthy** return *swallows* it (so `after` prints and `status`
is `ok`); a falsy/`None` return *re-raises* it (like `finally`). *Repaired mapping:* `with` is
`try/finally` **plus an opt-in `except` that the context manager controls via its `__exit__`
return**. *Same/different line:* "deterministic cleanup at block exit" transfers; "the exception
always propagates" does **not** — `__exit__` can suppress it, which `finally` cannot.

**Why.** This is an Advanced false friend because it **combines** a new protocol (`__enter__`/
`__exit__`) with **exception control flow**, and the difference is invisible on the happy path
(no exception → `with` and `try/finally` look identical). You only see it by running the
**raising** case and checking `status` — *whether it raised* is the artifact, not `stdout`.

**Diagnoses.** Predicting the `ValueError` propagates reveals **mistaking one model for
universal** (try/finally semantics assumed for `with`) and **no sub-model of `__exit__`'s
return-value contract** — the suppression mechanism was never ported. (Catalog §5c,
"over-generalizes one language's model" + "memorizes syntax instead of porting the execution
model.")

---

## Adv-3 — A mutable **class attribute** is shared across instances (false friend from Java fields)

> You know **Java / C++**: a field written in the class body (`List items = ...`) is
> **per-instance** — each object gets its own.

```python
class Bag:
    items = []          # looks like a field declaration
    def add(self, x):
        self.items.append(x)

a = Bag()
b = Bag()
a.add(1)
b.add(2)
print("a.items:", a.items)
print("b.items:", b.items)
print("same object:", a.items is b.items)
```

> **Your turn:** Map `items = []` onto a per-instance field and predict `a.items` and
> `b.items`. Then: is there one list here, or two?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "a.items: [1, 2]\nb.items: [1, 2]\nsame object: True\n"
status: ok
```

So **both** `a.items` and `b.items` are `[1, 2]`, and they are the **same object**. Under the
"per-instance field" analogy you would have predicted `a.items == [1]` and `b.items == [2]`,
two separate lists. False friend.

**Gold mapping.** *Analogy:* a class-body assignment declares a per-instance field. *Classify:*
**false friend**, combining attribute resolution + aliasing. *Why (execution model):* `items =
[]` in the class body creates **one class attribute** on `Bag` itself — not a per-instance
slot. `self.items.append(x)` does an attribute **lookup** for `items` (finds it on the class,
since no instance attribute shadows it) and then **mutates that shared list in place** — it
never *rebinds* `self.items`, so no instance attribute is ever created. Both instances resolve
`items` to the **same** class-level list → `a.items is b.items` is `True`. *Repaired mapping:*
the per-instance idiom is to assign in `__init__`: `def __init__(self): self.items = []` —
**that** rebind, on `self`, creates a distinct instance attribute per object. *Same/different
line:* "declare a collection on the class" transfers as a concept; **where the assignment lives
(class body vs `__init__`) and rebind-vs-mutate** do not.

**Why.** This is Advanced because the prediction needs **two** ported mechanisms at once —
class-vs-instance attribute **lookup** *and* mutate-vs-rebind **aliasing** (A1) — and it is a
real, common production bug. A learner who mutates (`.append`) but never rebinds (`self.items =
...`) keeps hitting the shared object; the `is` check makes the single-object truth undeniable
(which is why the drill prints it).

**Diagnoses.** Predicting two separate lists reveals **mistaking the Java field model for
universal** (class body ⇒ per-instance) plus **no rebind-vs-mutate model** (the shared class
list is mutated, never shadowed). (Catalog §5c, "over-generalizes one language's model" +
false-friend over-trust; A1 aliasing.)
</content>
