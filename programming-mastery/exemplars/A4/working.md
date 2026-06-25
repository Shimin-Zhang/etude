# A4 — Working exemplars (concurrency mental models)

Golden drills for the **Working** tier of module A4: apply the model in an unseen context where the
**schedule** matters and intent/execution diverge. The skill is **classification** — atomicity vs
order, data race vs race condition, and judging a "the GIL saves this" claim — *and saying why*, not
just spotting that something is wrong. Every executable sub-claim was obtained by **running it
through the runner** (`drill-generation.md` §2); forced `Event` interleavings make each bug
deterministic, and the coach never guesses:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct mechanisms (order violation · race-condition-without-a-data-race ·
GIL-misconception) — no repeated gotcha, and a genuine classification *decision* in each. Grading is
**hybrid, leaning rubric** (§5d): the forced misbehavior is executable ground truth; the
**classification + fix-direction** is rubric-graded and the coach **says so**. Pose one, **hard-stop,
wait** (`coaching-loop.md`).

---

## A4-W1 — Classify this race, and say why a lock won't fix it (order)

A loader thread initializes config; a consumer thread reads it. There is no ordering between them:

```python
import threading
data = {}
def producer():
    data["config"] = "LOADED"        # initialize
def consumer():
    use(data["config"])              # read the config
# both started; no edge forces the producer first
```

> **Your turn:** This sometimes crashes. (1) Classify it: **atomicity violation** or **order
> violation** (Lu et al.)? (2) Your teammate's fix is "wrap both functions in one shared `Lock`."
> Does that fix it? Say why or why not, and give the fix that does.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — the breaking schedule (consumer reads first) is *forced* with an
`Event` so the crash is deterministic (the consumer catches and reports it so the process exits
cleanly):

```
# /tmp/A4_order_violation2.py  (consumer's read pinned before the producer's write)
stdout: "consumer result: {'error': \"KeyError('config')\"}\ndata after both threads: {'config': 'LOADED'}\n"
status: ok
```

The consumer's read ran **before** the producer's write → `KeyError('config')`.

**Why.** This is an **order violation**: A (`data["config"] = ...`) was *meant* to precede B
(`use(data["config"])`), but nothing orders them, so the order can flip. The teammate's shared
`Lock` is the **wrong tool**: a lock gives **mutual exclusion (atomicity)**, not **order** — it stops
the two from *overlapping*, but does **not** make the producer go first, so the consumer can still
acquire the lock first and read missing config. The right fix is an explicit **happens-before edge**:
a `producer.join()` before the consumer reads, an `Event` the producer `set()`s and the consumer
`wait()`s on, or a `queue.Queue` (`put`→`get`). (Lu et al. Finding 9: 73% of real fixes are *not*
just adding/changing locks.)

**Diagnoses.** Classifying it as **atomicity** (or "just add a lock") is the central A4 failure —
**sending the fix the wrong way** (Catalog §5c: "confuses an atomicity violation with an order
violation"; "adds a lock and assumes order is now guaranteed"). The tell that the model is right:
the learner names that a lock gives mutual exclusion *not order*, and reaches for a happens-before
edge.

---

## A4-W2 — Data race, race condition, or both? (check-then-act)

A cache memoizes an expensive `compute()`. Two workers run the classic check-then-act:

```python
if "k" not in cache:                 # CHECK   (a dict membership test)
    cache["k"] = compute()           # ACT     (a dict store)
```

Both `in` and `cache[...] = ...` are on the Python-FAQ list of **atomic** dict operations.

> **Your turn:** Under concurrency this sometimes runs `compute()` **twice**. (1) Is there a **data
> race** here? (2) Is there a **race condition**? (3) Reconcile your answers with "but every dict
> operation is atomic."
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — both workers are *forced* to pass the check before either writes;
`compute` is instrumented to record each call:

```
# /tmp/A4_check_then_act.py
stdout: "computed 2 times: ['w2', 'w1'] -- expected exactly 1\nfinal cache['k'] = w1\n"
status: ok
```

`compute()` ran **twice** — the memo failed — even though no single dict operation was interrupted.

**Why.** **No data race, yet a race condition.** A *data race* is two threads touching the **same
location** unsynchronized with at least one **write**; here each `in` and each store is individually
**atomic** (the GIL guarantees it), so no single access is torn — there is **no data race**. But
**correctness depends on the schedule**: both threads can run the atomic CHECK (both see "absent")
*before* either runs the atomic ACT, so both compute and both store (last-writer-wins). That is a
**race condition** (specifically a TOCTOU atomicity violation: the *check-then-act region* was meant
to be indivisible). The lesson: **the GIL removes data races, not race conditions** — which is why
"the GIL makes it thread-safe" is false. The fix makes the **whole** check-then-act atomic (hold a
lock across both), or uses a structure with an atomic "compute-if-absent" (`dict.setdefault`, a lock,
`functools.lru_cache`).

**Diagnoses.** Answering "no data race, so it's fine" is the **data-race/race-condition conflation**
(Catalog §5c) — the exact trap the GIL sets. Calling it a "data race" is the same gap from the other
side. Solid: names that the *combination* of atomic ops is non-atomic, and fixes the *region*.

---

## A4-W3 — "It printed the right total, so the GIL saved me" (error analysis)

A teammate ships this and says "I ran it five times and always got 200000, so the GIL makes `+=`
safe — no lock needed":

```python
import threading
counter = 0
def work():
    global counter
    for _ in range(100_000):
        counter += 1
t1 = threading.Thread(target=work); t2 = threading.Thread(target=work)
t1.start(); t2.start(); t1.join(); t2.join()
print(counter)          # teammate: "always 200000"
```

> **Your turn:** Is the teammate's reasoning sound? What, exactly, does "always 200000 on five runs"
> prove — and what would you show them to settle it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — the teammate's observation reproduces (five green runs), **and** the
interleaving *set* of a single pair of `+=`s proves the code is still wrong:

```
# /tmp/A4_naive_race.py  (their snippet, 5 runs)
expected 200000  actual 200000  no loss (this sample)   ... ×5

# /tmp/A4_enum_interleavings.py  (all interleavings of just TWO +1s on 0)
valid interleavings: 6 | correct: 2 | lose an update: 4
status: ok
```

**Why.** The reasoning is **unsound**: five green runs prove only that **five sampled schedules were
fine**, not that the code is correct. `counter += 1` is a non-atomic read-modify-write
(`LOAD`/`BINARY_OP`/`STORE` — runner-verified), so two threads *can* lose updates — and the
enumeration shows **4 of 6** interleavings of even a single pair of increments lose one. CPython's
GIL makes the losing schedule **rare** for a tight loop (it rarely preempts mid-`+=`), so the bug is
**latent**, not absent — a heisenbug. What settles it is the **set**, not another run: enumerate (or
force) a losing interleaving. The fix is a `Lock` around the whole `+=` (or `itertools.count` /
`threading` primitives designed for it). "Always 200000" is the illusion of fluency, not a proof.

**Diagnoses.** Accepting "five runs ⇒ correct" is **one-green-run-as-proof** (Catalog §5c); accepting
"GIL ⇒ `+=` safe" is the **GIL-misconception** (§5c). The skill is to answer a *sampling* claim with
a *set* argument — reason about the interleavings the scheduler is *allowed* to produce, not the ones
you happened to observe.

---

### Grading note (all Working drills)

Force the breaking schedule (or enumerate the set) and **paste it** (`coaching-loop.md` → surface
ground truth) — especially when the learner disputes that a bug exists ("it works for me"). Then
grade **D1 (reason about the set) · D2 (classify: atomicity/order, data-race/race-condition,
GIL-status) · D3 (right-unit fix)** separately (§5d), and **say it is softer than an executable
pass**: the runner proves the bug on a forced schedule but cannot certify a fix over *all* schedules.
A learner who *describes the breaking interleaving* but *mis-classifies it* (e.g. order-as-atomicity)
is a **partial pass** — flag exactly that, because the misclassification sends the fix the wrong way
(Lu et al. Finding 2/9).
