# C3 — Foundations exemplars (production & concurrency debugging)

Golden drills for the **Foundations** tier of module C3. Each presents **one race, named for the
learner** (describe the breaking interleaving), or **one clean evidence trail** (localize the
fault) — no requirement to *discover* the bug class unaided (that's Working). Grading is **hybrid,
leaning rubric + exemplars and softer than a pure executable pass** (`drill-generation.md` §3;
module §5d): the coach scores the *reasoning*, but every deterministic sub-claim below was
**confirmed by running it** through the runner (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Concurrency races are forced into a **deterministic** schedule with an `Event`/`Barrier` so the
bug manifests every run — a *naive* (unforced) racy snippet often prints the *correct* answer on
CPython (the heisenbug), which is itself the lesson, not a refutation. Coverage spans the
Foundations parameter space: **atomicity violation** (lost update) · **order violation**
(use-before-init) · **observability** (localize from a log trail). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7: **D1** = described a breaking
interleaving / located the fault; **D2** = named the read-modify-write window or the discriminating
signal; **D3** is exercised more at Working/Advanced. The answer key is for *grading*, never shown
before the learner attempts.

---

## F1 — Two deposits, one lost (atomicity violation; 2 threads, 1 variable)

Two threads each make a single `+1` "deposit" to a shared balance that starts at `0`. The intended
invariant: *two deposits ⇒ final balance is `2`*. The schedule is **forced** so the race is
deterministic.

```python
import threading
shared = {"balance": 0}
t1_read = threading.Event()
t2_wrote = threading.Event()

def t1():                          # deposit +1
    tmp = shared["balance"]        # READ 0
    t1_read.set()
    t2_wrote.wait()                # force T2 to interleave between this read and the write
    shared["balance"] = tmp + 1    # WRITE 1 (using the stale tmp)

def t2():                          # deposit +1
    t1_read.wait()
    shared["balance"] = shared["balance"] + 1   # 0 -> 1
    t2_wrote.set()

a = threading.Thread(target=t1); b = threading.Thread(target=t2)
a.start(); b.start(); a.join(); b.join()
print("two +1 deposits on 0; correct final = 2")
print("actual final =", shared["balance"])
```

> **Your turn:** The correct final balance is `2`. What does this actually print, and **describe
> the interleaving** that produces it — which read goes stale, and which write clobbers which?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (deterministic — confirmed `1` on 10/10 runs)

```
stdout: "two +1 deposits on 0; correct final = 2\nactual final = 1\n"
status: ok
```

So the printed final is `actual final = 1` — one deposit is **lost**.

**Why.** `shared["balance"] = tmp + 1` is the *write* half of a read-modify-write; the *read*
(`tmp = ...`) happened earlier. The forced schedule is: T1 reads `0` → T2 reads `0`, computes `1`,
writes `1` → T1 now writes `tmp + 1` where `tmp` is its **stale `0`**, so it writes `1`, clobbering
T2's update. Both deposits ran; only one survived. This is an **atomicity violation** (Lu et al.
2008): the read and write were *meant* to be one indivisible unit, but T2's accesses interleaved
between them.

**Diagnoses.** A learner who says "it prints `2`, the deposits just add up" has **trusted the
intended semantics over the interleaving** — and is treating `+= 1`/`= tmp + 1` as one step
(§5c, read-modify-write-as-one-step; the atomicity blind spot). Run it and show the `1`. A learner
who predicts `1` but can't say *why* (which read is stale) has the symptom, not the mechanism — push
for the interleaving. Strong answer: `1`, because both threads read `0` before either writes, and
T1's stale write overwrites T2's. (Catalog §5c; module §3 corollary 1.)

---

## F2 — Use before init (order violation; the reader races ahead of the loader)

A loader thread initializes `config`; a user thread reads it. Nothing enforces that the loader runs
first. The loader is "slow" (a realistic init latency), so the user races ahead.

```python
import threading, time

config = None     # will be initialized by the loader thread

def loader():
    global config
    time.sleep(0.05)            # loader is slow (simulates real init latency)
    config = {"timeout": 30}

def user():
    # BUG: assumes loader has finished. Nothing creates a happens-before edge to guarantee it.
    print("timeout is", config["timeout"])

t_load = threading.Thread(target=loader)
t_use  = threading.Thread(target=user)
t_load.start()
t_use.start()                  # user races ahead of loader
t_load.join(); t_use.join()
```

> **Your turn:** Does this print the timeout cleanly, or does something go wrong? If it goes wrong,
> say **exactly what** and **why** — what ordering was assumed but not enforced?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (the user thread raises)

```
stdout: ""
status: ok        (the main thread exits 0; the exception is in the child thread)
stderr (the trace):
    Exception in thread Thread-2 (user):
    ...
        print("timeout is", config["timeout"])
                            ~~~~~~^^^^^^^^^^^
    TypeError: 'NoneType' object is not subscriptable
```

So `user` crashes with `TypeError: 'NoneType' object is not subscriptable` — it read `config` while
it was still `None`.

**Why.** The user thread dereferences `config["timeout"]` before the loader has assigned `config`.
There is **no happens-before edge** forcing the loader to run first — `start()` does not guarantee
ordering between two sibling threads, and the loader's `sleep` makes the user reliably win the race.
This is an **order violation** (Lu et al. 2008): operation A (initialize) was *meant* to precede B
(read), but the order is not enforced. Note this is **not** an atomicity bug — the fix is a
**happens-before edge** (have the user `wait()` on an `Event` the loader `set()`s, or `join()` the
loader first), *not* a lock. A lock here would not help: it prevents *overlap*, not *order*.

**Diagnoses.** A learner who says "it prints `timeout is 30`" assumed the loader runs first
(intent-reading the order; §5c, atomicity-vs-order / trusting-the-run). A learner who spots the
crash but proposes "wrap both in a lock" has the **order-vs-atomicity confusion** (§5c) — a lock
gives mutual exclusion, not ordering; run a lock-wrapped version and show the order can still flip.
Strong answer: crashes with `TypeError` because the read can happen before the init; it's an order
violation; fix with a happens-before edge, not a lock. (Catalog §5c; module §3 corollary 2.)

---

## F3 — Read the trail (observability; localize the fault from logs, no debugger)

You cannot attach a debugger to this service — it's in production. Each request emits one structured
log line with per-stage timings and a status. Six requests came through; some returned `504`
(gateway timeout). Reason from the **evidence the runtime emitted**.

```python
# Per-request log line: authMs / dbMs / depMs (downstream dependency) / totalMs / status.
def handle(req_id, slow_dep):
    a = 2                                    # auth (fast, constant)
    b = 5                                    # db lookup (fast, constant)
    c = 200 if slow_dep else 8               # downstream dependency call (the variable one)
    total = a + b + c
    status = 504 if total > 100 else 200     # gateway timeout if too slow
    print(f"req={req_id} authMs={a} dbMs={b} depMs={c} totalMs={total} status={status}")

for i in range(1, 7):
    handle(i, slow_dep=(i in (3, 4)))
```

> **Your turn:** Here is the log trail (below). Two requests returned `504`. **Which stage is the
> fault in**, and **what single piece of evidence in the logs points there**?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (the emitted trail)

```
stdout:
    req=1 authMs=2 dbMs=5 depMs=8 totalMs=15 status=200
    req=2 authMs=2 dbMs=5 depMs=8 totalMs=15 status=200
    req=3 authMs=2 dbMs=5 depMs=200 totalMs=207 status=504
    req=4 authMs=2 dbMs=5 depMs=200 totalMs=207 status=504
    req=5 authMs=2 dbMs=5 depMs=8 totalMs=15 status=200
    req=6 authMs=2 dbMs=5 depMs=8 totalMs=15 status=200
status: ok
```

**Why.** The fault is in the **downstream dependency** (the `depMs` stage). The discriminating
evidence: on the two `504` requests, `authMs` and `dbMs` are **unchanged** (`2` and `5`, exactly as
on the healthy requests) while **`depMs` jumps from `8` to `200`** — and `totalMs` (`207`) crosses
the timeout threshold *entirely* because of that one stage. You localize by *comparing the failing
requests to the healthy ones* and finding the **one stage that differs**. This is the production
move: no debugger, no re-run — you read the trail and narrow to the stage whose evidence changed.

**Diagnoses.** A learner who says "the requests timed out" has restated the symptom (`status=504`)
without localizing — push them to the *stage*. A learner who blames `auth` or `db` ignored that
those numbers are *identical* on good and bad requests (§5c, fixating on a signal that doesn't
discriminate). A learner who says "there's no error logged so it's fine" misread `504` as benign or
treated absent stack traces as absence of a fault (§5c, absent-evidence). Strong answer: the
downstream dependency, because `depMs` is the only stage that differs between the `200`s and the
`504`s, and it alone pushes `totalMs` past the threshold. (Catalog §5c; module §1c, observability
canon.)
