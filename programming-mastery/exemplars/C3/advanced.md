# C3 — Advanced exemplars (production & concurrency debugging)

Golden drills for the **Advanced** tier of module C3. Each **combines mechanisms** or forces the
learner to reason about **non-reproducibility**, **unaided**: a deadlock from lock-ordering; a bug
that needs **both** an atomicity fix **and** an order edge (a lock alone is insufficient); a
"passes in CI, fails in prod" incident. Grading is **hybrid, leaning rubric + exemplars, and softer
than a pure executable pass** (`drill-generation.md` §3; module §5d) — the coach scores the
*reasoning*, but every deterministic sub-claim was **confirmed by running it**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Buggy schedules are **forced** (`Event`/`Barrier`/`sleep`) so the bug is deterministic; each fix
was **re-run to confirm it closes the forced schedule** — *necessary, not sufficient*: the runner
proves a bug exists and that a fix closes *that* schedule, but it cannot enumerate *all*
interleavings, so the coach grades the reasoning about the schedule space, not just the output.
Coverage spans distinct points: **deadlock (lock-ordering)** · **atomicity + order combined** ·
**non-reproducibility (CI vs prod)**. Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to
grade** against module §7: **D1** found/localized · **D2** classified + falsifiable hypothesis +
non-reproducibility reasoning · **D3** fixed the right unit and **did not introduce a deadlock**;
plus a **teach-it-back** of the principle.

---

## A1 — Two locks, opposite order (deadlock from a circular wait)

Two threads each need both `lock_a` and `lock_b`. T1 takes `a` then `b`; T2 takes `b` then `a`. A
`Barrier` **forces** the interleaving where each holds one lock and reaches for the other.

```python
import threading
lock_a = threading.Lock()
lock_b = threading.Lock()
gate = threading.Barrier(2)

def t1():
    with lock_a:
        gate.wait()           # ensure T2 has grabbed lock_b before we reach for it
        with lock_b:          # waits for lock_b, which T2 holds
            pass

def t2():
    with lock_b:
        gate.wait()
        with lock_a:          # waits for lock_a, which T1 holds
            pass

a = threading.Thread(target=t1); b = threading.Thread(target=t2)
a.start(); b.start(); a.join(); b.join()
print("reached the end (no deadlock)")
```

> **Your turn:** What happens when you run this? **Classify it** and explain the exact condition.
> What's the fix — and be careful: would adding a *third* lock around everything help or hurt?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (it deadlocks; the runner reports a timeout)

```
stdout: ""
status: timeout      (the program hangs; runner kills it at the 5s limit, returncode null)
```

So it **never prints** — it **deadlocks**, and the runner surfaces that as `status: timeout`.

**Classification + why.** This is a **deadlock** via **circular wait** (Lu et al. 2008: 31/105
bugs). The four classic conditions all hold; the one the code creates is **inconsistent lock
ordering**: T1 holds `a` and waits for `b` while T2 holds `b` and waits for `a`, so neither can
proceed. The `Barrier` is just the forcing device that guarantees this overlap every run.
**Fix:** impose a **consistent global lock order** — every thread acquires `a` *before* `b`. Then a
circular wait is impossible and no forcing can reproduce it:

```python
def t2():
    with lock_a:          # was lock_b first -> acquire a then b, matching t1
        with lock_b:
            pass
```

**Runner-verified — the fix resolves it** (consistent ordering, looped 1000×, no barrier needed,
3/3 runs):

```
stdout: "both threads completed 1000x; no deadlock\n"
status: ok
```

A *third* "big lock" around everything would **also** remove the deadlock (it serializes the two
critical sections) — but it's the heavier hammer: it kills any concurrency between the two regions,
whereas consistent ordering keeps them concurrent except for the genuinely-shared moment. Adding it
*on top of* the existing two locks without care can itself create a new ordering hazard. Prefer the
ordering fix.

**Diagnoses.** A learner who predicts `reached the end` did not see the circular wait (§5c,
lock-ordering/deadlock). A learner who "fixes" it by adding *another* lock without removing the
opposite-order acquisition has the **reach-for-a-lock reflex** that can introduce *more* deadlock
(§5c). A learner who reports "it timed out" but can't name *circular wait / lock ordering* has the
symptom, not the class. Strong answer: deadlock via inconsistent lock order; fix = consistent global
ordering; a big lock works but over-serializes. (Catalog §5c; module §6 escalation 1.)

---

## A2 — A lock isn't enough: atomicity *and* order (combine two mechanisms)

**Spec.** A producer fills a shared `items` list; a consumer reads the final count. The consumer
must see all 5 items. A teammate "made it thread-safe" by guarding every list access with a lock —
and it *still* reports the wrong count. The buggy order (consumer ahead of producer) is forced with
a `sleep`.

```python
import threading
items = []
lock = threading.Lock()
# NOTE: the only synchronization is the lock. There is NO happens-before edge
# between the producer finishing and the consumer reading.

def producer():
    for i in range(5):
        with lock:                 # access is guarded (no torn state) ...
            items.append(i)

def consumer():
    with lock:                     # ... guarded read, but nothing orders it after the producer
        count = len(items)
    print("consumer saw", count, "items (expected 5)")

c = threading.Thread(target=consumer)
p = threading.Thread(target=producer)
c.start()
import time; time.sleep(0.02)      # consumer reads before the producer has appended
p.start()
c.join(); p.join()
```

> **Your turn:** The lock guards every access, yet the count is wrong. What does it print, **why
> didn't the lock fix it**, and what's the *complete* fix? Name the two distinct mechanisms at play.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (lock-guarded but still wrong — deterministic)

```
stdout: "consumer saw 0 items (expected 5)\n"
status: ok
```

So it prints **`consumer saw 0 items`** even though every access is locked.

**Why the lock didn't fix it.** Two distinct mechanisms are needed, and the lock only supplies one:
- **Atomicity** (what the lock *does* give): it prevents the consumer from reading a *torn*
  intermediate state while the producer mutates. Fine — but not the bug here.
- **Order** (what the lock does **not** give): nothing forces the consumer to read *after* the
  producer finishes. A lock provides **mutual exclusion, not ordering** (Lu et al. Finding 2). The
  consumer wins the race, takes the lock first, reads an **empty** list (`0`), releases — all
  perfectly "thread-safe," and completely wrong. This is an **order violation layered on a region
  that also needs atomicity**.

**Complete fix** — keep the lock (atomicity) **and** add a **happens-before edge** (order), e.g. an
`Event`:

```python
done = threading.Event()
def producer():
    for i in range(5):
        with lock: items.append(i)
    done.set()                     # ORDER: signal completion
def consumer():
    done.wait()                    # ORDER: don't read until producer is done
    with lock: count = len(items)  # ATOMICITY: still guard the shared read
    print("consumer saw", count, "items (expected 5)")
```

**Runner-verified — the complete fix resolves it** (2/2 runs):

```
stdout: "consumer saw 5 items (expected 5)\n"
status: ok
```

**Diagnoses.** A learner who says "the lock makes it thread-safe, so the `0` must be something else"
has **conflated atomicity with order** (§5c) — the central C3 trap; show that the lock-guarded code
still reads `0`. A learner who adds *another* lock, or a bigger lock, never gets to `5` because the
problem was never overlap — it was sequencing (§5c, add-a-lock-as-a-spell). A learner who only fixes
the order (drops the lock) is right *here* but should still name that the shared read wants guarding
under genuine concurrency. Strong answer: prints `0`; the lock gives atomicity not order; complete
fix = lock **plus** a happens-before edge; the two mechanisms are atomicity and ordering.
(Catalog §5c; module §3 corollary 2; §6 escalation 1.)

---

## A3 — Green in CI, red in prod (non-reproducibility)

A per-request counter is incremented with a non-atomic `+=`. The test suite drives it with **one
worker** and passes every time; in production, **many workers** hit it concurrently and the count
drifts low. Below, "CI" is modeled as a single worker (no contention) and "prod" as a **forced
overlapping interleaving** of two workers, so both outcomes are deterministic and you can see the
difference.

```python
import threading

def ci_run():                          # low contention: effectively serial (one worker)
    count = {"n": 0}
    for _ in range(3):                 # 3 requests, one at a time
        tmp = count["n"]; count["n"] = tmp + 1
    return count["n"]

def prod_run():                        # high contention: two workers, forced to overlap
    count = {"n": 0}
    read = threading.Event(); wrote = threading.Event()
    def w1():
        tmp = count["n"]; read.set(); wrote.wait(); count["n"] = tmp + 1
    def w2():
        read.wait(); count["n"] = count["n"] + 1; wrote.set()
    a = threading.Thread(target=w1); b = threading.Thread(target=w2)
    a.start(); b.start(); a.join(); b.join()
    return count["n"]

print("CI (1 worker, 3 requests):  count =", ci_run(), "(expected 3)")
print("prod (2 workers overlap):   count =", prod_run(), "(expected 2)")
```

> **Your turn:** The test passes; prod is wrong. What does this print? **Why does the same code
> pass in CI and fail in prod** — what is different, and is it the *code* or the *schedule*? Give
> your top hypothesis and the **one** thing you'd add to prove it, knowing you *cannot reproduce it
> locally* by just re-running.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (deterministic across runs)

```
stdout: "CI (1 worker, 3 requests):  count = 3 (expected 3)\nprod (2 workers overlap):   count = 1 (expected 2)\n"
status: ok
```

So **CI = `3` (correct)**, **prod = `1` (a lost update)**.

**Why.** The code is **identical**; only the **schedule** differs. In CI there is *one* worker, so
the read-modify-write never overlaps — every `+=` completes before the next starts, and the latent
atomicity violation is never exercised. In prod, *concurrent* workers interleave: both read the
same value before either writes, and one update is lost (here, the forced overlap drops one of two
deposits → `1`). The bug was always there; **low contention in CI never sampled the breaking
interleaving.** Re-running the test won't help — it has the same low-contention schedule every time
(and even high-contention re-runs are a *heisenbug*: they may or may not hit the window). **Top
hypothesis:** a non-atomic read-modify-write on the shared counter loses updates under concurrency.
**The one thing to add to prove it without "just re-running":** instrument the invariant directly —
emit/assert *expected increments vs. actual count* under load (or add a contention/lost-update
metric), and/or run the counter under a **deterministic interleaving** (force the overlap, as above)
rather than hoping a re-run trips it. **Fix:** make the increment atomic (a lock or an atomic
counter).

**Diagnoses.** A learner who says "CI passes, so the code is fine; prod must be a different bug"
has **trusted the green run** and missed that correctness is schedule-dependent (§5c,
trusting-the-run; treats-RMW-as-one-step). A learner who proposes "just re-run the test until it
fails" has no model of *why* CI's schedule differs and is courting a heisenbug (§5c). A learner who
reaches for a debugger to step prod is carrying the C1 reproduce-and-step assumption into a setting
where it doesn't apply (§5c, reproduce-and-step-in-prod). Strong answer: same code, different
schedule (low vs high contention); non-atomic RMW; prove it by instrumenting the invariant or
forcing the interleaving, not by re-running; fix = make the increment atomic. **Teach-it-back to
require:** "a green run is one sample of a schedule space; CI sampled a benign schedule, prod
sampled a breaking one." (Catalog §5c; module §3 corollary 3; §6 escalation 3.)
