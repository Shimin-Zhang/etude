# C3 — Working exemplars (production & concurrency debugging)

Golden drills for the **Working** tier of module C3. Each asks the learner to apply the model in a
context not seen before, **unaided**: **classify** a race (atomicity vs order — Lu et al. 2008) and
say *why*; spot a **heisenbug** (will observing it hide it?); or localize from a metric trail where
the loudest signal is a **decoy**. Grading is **hybrid, leaning rubric + exemplars, and softer than
a pure executable pass** (`drill-generation.md` §3; module §5d) — the coach scores the *reasoning*,
but every deterministic sub-claim was **confirmed by running it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Concurrency races are **forced** into a deterministic schedule (`Event`/`Barrier`) so the bug and
its fix are reproducible. Coverage spans distinct points: **atomicity violation (check-then-act)** ·
**heisenbug / non-reproducibility** · **production metric trail with a decoy**. Pose one,
**hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7: **D1** =
found/localized; **D2** = classified correctly (atomicity vs order) or named the discriminating
signal and reasoned about non-reproducibility; **D3** = targeted the fix at the right unit, not a
reflexive lock. **A learner who finds the race but mis-classifies it (atomicity called order, or
vice versa) is a partial pass — flag it, because it sends the fix the wrong way** (Lu et al. Finding
2/9; the central C3 failure).

---

## W1 — Build it once, built it twice (classify: atomicity or order?)

**Spec.** `get_or_create` should create an expensive shared resource **exactly once** — the classic
lazy-init / cache-fill. Two threads call it concurrently. The check (`"key" not in cache`) and the
act (create + store) are **not** wrapped together. The schedule is **forced** (a `Barrier`) so both
threads finish the check before either acts.

```python
import threading
cache = {}
created = []                            # log of how many times the resource was "created"
both_checked = threading.Barrier(2)     # both rendezvous AFTER the check, BEFORE the act

def get_or_create(tag):
    missing = "key" not in cache        # CHECK (both see True: cache empty)
    both_checked.wait()                 # force both to finish the check before any act
    if missing:
        created.append(tag)             # ACT: create the "expensive" resource
        cache["key"] = tag

a = threading.Thread(target=get_or_create, args=("T1",))
b = threading.Thread(target=get_or_create, args=("T2",))
a.start(); b.start(); a.join(); b.join()
print("resource created", len(created), "times; correct is 1")
print("creators:", sorted(created))
```

> **Your turn:** What does this print? **Classify the bug** — is it an *atomicity* violation or an
> *order* violation, and **why**? What's the fix, and would a single lock around just the
> `created.append(...)` line be enough?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the bug is real and deterministic)

```
stdout: "resource created 2 times; correct is 1\ncreators: ['T1', 'T2']\n"
status: ok
# with the suggested fix (check AND act under one lock): "resource created 1 times; correct is 1"
```

**Classification + why.** This is an **atomicity violation** (Lu et al. 2008): the check and the
act were *meant* to be one indivisible unit ("if it's missing, create it"), but the two operations
are separable, so both threads pass the check (both see `missing == True`) before either acts, and
the resource is created **twice**. It is *not* an order violation — there is no "A must precede B"
that got flipped; the bug is the **interleaving inside a region that should have been atomic**
(this exact shape is *check-then-act* / TOCTOU). **Fix:** make the **check and the act atomic
together** under one lock:

```python
lock = threading.Lock()
def get_or_create(tag):
    with lock:
        if "key" not in cache:
            created.append(tag); cache["key"] = tag
```

A lock around **only** `created.append(...)` is **not** enough — the two threads have already both
passed the check by then, so they both append (serialized, but still twice). The lock must span the
*whole* check-modify-write.

**Diagnoses.** A learner who calls this an **order violation** has the **atomicity-vs-order
confusion** (§5c) — push them: nothing here is "supposed to go first"; the fault is the overlap.
A learner who proposes locking only the `append` has missed that the **check** is part of the
atomic unit (§5c, add-a-lock-without-checking-what-must-be-atomic). A learner who never runs it may
not believe it creates twice. Strong answer: created `2`; atomicity violation (check-then-act);
fix = whole check-and-act under one lock; locking only the append is insufficient. (Catalog §5c;
module §3 corollaries 1–2.)

---

## W2 — It only breaks when you're not looking (the heisenbug)

A non-atomic increment, modeled with explicit shared state so the interleaving is controllable.
The code is run twice: once *latent* (the bad schedule is allowed), once *observed* (an extra
synchronized re-read — standing in for an added `print`/log/breakpoint — perturbs the timing).

```python
import threading

def run(observe):
    shared = {"balance": 0}
    t1_has_read = threading.Event()
    t2_has_written = threading.Event()
    reg = {"t1": None}                       # T1's local copy of its read (a "register")

    def t1():
        reg["t1"] = shared["balance"]        # READ -> 0
        t1_has_read.set()
        t2_has_written.wait()                # race window held open deterministically
        if observe:
            reg["t1"] = shared["balance"]    # PROBE: observation forces a fresh re-read -> 1
        shared["balance"] = reg["t1"] + 1    # WRITE

    def t2():
        t1_has_read.wait()
        shared["balance"] = shared["balance"] + 1   # 0 -> 1
        t2_has_written.set()

    a = threading.Thread(target=t1); b = threading.Thread(target=t2)
    a.start(); b.start(); a.join(); b.join()
    return shared["balance"]

print("two concurrent +1 on 0; correct = 2")
print("latent run (no probe):", run(observe=False))
print("observed  (w/ probe):", run(observe=True))
```

> **Your turn:** Two `+1`s on `0`; the correct result is `2`. What does each line print — and
> **what does the probe actually prove**? If a teammate added that probe, watched the result become
> `2`, and closed the ticket, were they right?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (deterministic across runs)

```
stdout: "two concurrent +1 on 0; correct = 2\nlatent run (no probe): 1\nobserved  (w/ probe): 2\n"
status: ok
```

So: **latent run = `1`** (an update is lost), **observed run = `2`** (looks correct).

**Why.** Without the probe, T1 writes back its **stale** read (`0 + 1 = 1`), clobbering T2's
write — a lost update (atomicity violation). The probe is an *observation*: it forces T1 to re-read
the freshest value right before writing, which changes the effective schedule so T1 no longer uses
a stale value, and the symptom vanishes. **This is a heisenbug:** observing the bug changed the
timing and *hid* it. The teammate was **wrong** — the probe didn't fix the race; it perturbed the
schedule so this run didn't hit it. The underlying read-modify-write is still non-atomic; a
different schedule (or removing the probe) brings the loss back. The real fix is to make the RMW
atomic (a lock), not to add an observation.

**Diagnoses.** A learner who says "the probe fixed it — output is `2`" has **no heisenbug model**
(§5c, debugging-a-heisenbug-by-observing-it): they read disappearance-under-observation as a fix.
A learner who predicts both as `2` is still trusting intended semantics over the interleaving
(§5c, treats-RMW-as-one-step). Strong answer: latent `1` / observed `2`; the probe only perturbed
timing and hid the bug; closing the ticket is wrong; fix the atomicity. (Catalog §5c; module §3
corollary 3.)

---

## W3 — High CPU is the loudest, not the cause (metric trail + decoy)

An incident. You have a minute-by-minute metric snapshot — CPU utilization, the downstream
dependency's p99 latency, and the error rate. CPU is high the **whole** time. Errors spike at
minutes 3–4. You cannot reproduce it; reason from the trail.

```python
# (minute, cpu_pct, dep_p99_ms, error_rate_pct)
rows = [
    (1, 88,  40, 0.1),
    (2, 90,  42, 0.1),
    (3, 89, 850, 7.4),
    (4, 91, 870, 8.1),
    (5, 90,  41, 0.2),
    (6, 88,  39, 0.1),
]
print("min cpu% dep_p99ms err%")
for m, cpu, dep, err in rows:
    print(f"{m:3d} {cpu:4d} {dep:7d} {err:5.1f}")
```

> **Your turn:** Errors spiked at minutes 3–4. CPU is ~90% throughout. **Which signal actually
> localizes the fault**, and which is a decoy? State your top hypothesis and the **one** piece of
> evidence that supports it over "the box is CPU-bound."
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the metric trail)

```
stdout:
    min cpu% dep_p99ms err%
      1   88      40   0.1
      2   90      42   0.1
      3   89     850   7.4
      4   91     870   8.1
      5   90      41   0.2
      6   88      39   0.1
status: ok
```

**Why.** The discriminating signal is **`dep_p99ms`** (the downstream dependency's latency), not
CPU. CPU is high *the whole time* — including minutes 1–2 and 5–6 when the error rate is ~0.1% — so
it **does not correlate** with the failure and cannot be the cause (it's a steady-state decoy;
maybe the service just runs hot). `dep_p99ms` is the only signal that **moves in lockstep with the
error rate**: it jumps from ~40 ms to ~850–870 ms exactly at minutes 3–4 and returns to baseline at
minute 5, tracking the error spike precisely. Top hypothesis: the downstream dependency degraded
(timeouts/slow responses) during minutes 3–4. The one piece of evidence over "CPU-bound": the error
spike is **time-aligned with the latency spike and not with CPU**, which is flat-high across both
healthy and failing minutes.

**Diagnoses.** A learner who says "CPU is at 90%, scale up the box" anchored on the **loudest**
signal instead of the **discriminating** one (§5c, fixating-on-a-signal-that-doesn't-discriminate).
A learner who says "errors went up" restated the symptom without localizing. A learner who reasons
purely from CPU never asked "does this signal differ between healthy and failing minutes?" — the
core narrowing move (Zeller). Strong answer: the dependency latency localizes it; CPU is a decoy
because it's flat-high regardless of errors; the latency/error time-alignment is the evidence.
(Catalog §5c; module §1c, observability canon + Zeller's narrowing.)
