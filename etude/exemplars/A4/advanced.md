# A4 — Advanced exemplars (concurrency mental models)

Golden drills for the **Advanced** tier of module A4: combine two or more mechanisms, or reason about
the **memory model** itself. Find/enumerate/force the breaking schedule, **classify** it, and propose
the fix that targets the **right unit** — explaining *why a lock alone is or isn't enough*. Every
executable sub-claim was obtained by **running it through the runner** (`drill-generation.md` §2):
forced `Event` interleavings, a deadlock that the runner reports as a **timeout**, and a
publication pattern whose CPython result is explicitly *not* a correctness proof. The coach never
guesses:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct mechanisms (deadlock / lock-ordering · sequential-consistency &
the memory model · atomicity-**and**-order double fix) — no repeated gotcha. Grading is **hybrid,
leaning rubric** (§5d) and **softer than A1's executable grading** — the coach says so, because the
runner can force *one* schedule (or time out *one* deadlock) but cannot certify a fix over *all*
interleavings. Two of these turn on `status` (a `timeout`) or on a result the coach must explicitly
**refuse to read as proof**. Pose one, **hard-stop, wait** (`coaching-loop.md`).

---

## A4-A1 — Two correct critical sections that deadlock (lock ordering)

Two threads each need **both** locks. Each grabs them in its own "natural" order:

```python
import threading
lock_a = threading.Lock(); lock_b = threading.Lock()
def t1():
    with lock_a:
        with lock_b:        # A then B
            ...
def t2():
    with lock_b:
        with lock_a:        # B then A
            ...
```

> **Your turn:** Each function on its own is correct. Run together, they sometimes hang forever.
> (1) What is the failure, and what is the precise condition that causes it? (2) Is "use more
> locking / a bigger lock" the fix? Give the fix that is. (3) What `status` would the runner report
> for a hang?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — the deadly embrace is *forced* (each thread takes its first lock,
then waits on an `Event` until the other holds *its* first lock, then reaches for the second):

```
# /tmp/A4_deadlock.py  (forced circular wait)
status: timeout   (duration_s ≈ 5.0, stdout empty — "completed" is never printed)
```

The program never finishes — the runner's timeout is the deterministic signal of the deadlock.

**Why.** This is a **deadlock by circular wait / lock ordering**. T1 holds `lock_a` and waits for
`lock_b`; T2 holds `lock_b` and waits for `lock_a` — a cycle, so neither can proceed. "More locking"
or "a bigger lock" makes it *worse* or merely hides it; the real fix is a **consistent global lock
order** — every thread acquires `lock_a` *before* `lock_b` (or use a single lock for both resources,
or `acquire(timeout=...)` with back-off). Note this is **not** an atomicity or order *violation* of
the Lu non-deadlock taxonomy — it is the **deadlock** class (31/105 bugs in Lu et al.), and its fix
is ordering *the locks*, not the data.

**Diagnoses.** Reaching for "add/enlarge a lock" is the **lock-ordering blind spot** (Catalog §5c:
"reaches for a lock-ordering fix that deadlocks, or cannot see why two correct critical sections
deadlock"). Predicting "error/exception" rather than **timeout** reveals no model that a deadlock
*hangs* (no thread raises — they wait). Solid: names circular wait and prescribes a consistent
acquisition order.

---

## A4-A2 — "It works on CPython" is not a memory-model guarantee (sequential consistency)

A producer publishes data via a flag; a consumer spins until the flag is set, then reads the data:

```python
import threading
state = {"data": None, "ready": False}
def producer():
    state["data"] = 42                # (1) write data
    state["ready"] = True             # (2) publish
def consumer():
    while not state["ready"]:          # spin until published
        pass
    print("consumer read data =", state["data"])
```

> **Your turn:** On CPython this prints `consumer read data = 42` and completes. (1) Does that *run*
> prove the pattern is correct/portable? (2) What is the silent assumption that makes "set the flag
> last" safe, and where could it fail? (3) What would make it correct **by construction**?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — *and the explicit refusal to over-read it*:

```
# /tmp/A4_publication.py
stdout: "consumer read data = 42\ncompleted\n"
status: ok
```

The run **completes on CPython** — but that is **not** a proof of correctness. (This is the rare A4
sub-claim the runner *cannot* settle: CPython's GIL **masks** the very hazard the drill is about, so
a green run is evidence of *nothing* about portability. The coach states this out loud — the grade is
rubric reasoning, not the output.)

**Why.** The pattern relies on **sequential consistency** (Lamport 1979): the assumption that there
is *some* global order of operations consistent with each thread's program order — so if the producer
writes `data` *before* `ready`, every thread that sees `ready == True` also sees `data == 42`. Real
hardware and optimizing compilers use **weaker** memory models that may **reorder** the two writes
(or let the consumer's `data` read be hoisted) **unless a happens-before edge forbids it** — so on a
weak-memory platform (or a future no-GIL build, PEP 703) the consumer could see `ready == True` but
stale `data`. CPython's GIL happens to serialize bytecodes, which is *why it works here* — an
**implementation detail**, not a Python guarantee. The fix is to **stop hand-rolling publication over
a plain flag** and use a primitive that *is* a happens-before edge: a `threading.Event`
(`set()`→`wait()`), a `queue.Queue` (`put`→`get`), or a `Lock`/`Condition` around both the write and
the read. Then the ordering holds **by construction**, on any memory model.

**Why this is graded as reasoning, not a run.** There is **no executable ground truth** for the bug
on CPython — the runner can only show "it happens to work." So the coach grades the *argument* (D2:
names sequential consistency as the assumption; identifies reordering under a weak model; recognizes
the GIL as the masker) against the rubric and the gold above, and **says it is soft** (§5d). This is
the honest shape of a memory-model drill: the model is exact, but you cannot demonstrate its
violation on this interpreter.

**Diagnoses.** "The run proves it's fine" is **assuming sequential consistency** + **one-green-run-
as-proof** (Catalog §5c). Not naming the producer/consumer *ordering* assumption, or "fixing" it with
a lock that gives mutual exclusion but no publication edge, is the **happens-before gap**. Solid:
names SC, names the reordering risk, and reaches for an edge-providing primitive.

---

## A4-A3 — Both an atomicity fix *and* an order edge (compose two mechanisms)

Two workers each increment a shared counter; a reporter prints the total. All three run as threads:

```python
import threading
counter = {"n": 0}
def worker():
    counter["n"] += 1                 # ① non-atomic read-modify-write
def report():
    print("total:", counter["n"])     # ② may read before the workers have incremented
w1 = threading.Thread(target=worker); w2 = threading.Thread(target=worker)
r  = threading.Thread(target=report)
w1.start(); w2.start(); r.start(); w1.join(); w2.join(); r.join()
```

> **Your turn:** This has **two** distinct concurrency bugs, needing **two different** fixes.
> Identify and **classify each** (atomicity vs order), and give the specific fix for each. Would a
> single `Lock` around the increment fix both? Why or why not?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — each bug forced/shown separately, then the combined fix confirmed:

```
# Bug ② (order), forced: reporter reads before either worker increments
# /tmp/A4_adv_order.py
stdout: "reporter saw 0 (invariant wanted 2 after both increments)\nfinal counter: 2\n"

# Bug ① (atomicity) is the lost update: forcing R1 R2 W1 W2 on the two increments -> final 1
# (same mechanism as /tmp/A4_forced_lost_update.py, runner-verified -> final = 1)

# The combined fix: lock around the WHOLE += (atomicity) AND join the workers before the read (order)
# /tmp/A4_adv_fixed.py
stdout: "total: 2\n"
status: ok   (reliably 2 on 3/3 runs)
```

**Why.** **Bug ① is an atomicity violation:** `counter["n"] += 1` is a read-modify-write, so two
workers can lose an update (forced → `1`, not `2`). **Bug ② is an order violation:** the reporter is
*meant* to run after both workers, but nothing orders it, so it can read `0` or `1` (forced →
`reporter saw 0`). The two bugs need **two different tools**: ① a **`Lock` held across the whole
`+=`** (atomicity); ② a **happens-before edge** — `w1.join(); w2.join()` *before* the read (order).
A single lock around the increment fixes **only ①**: it makes the increments not overlap, but does
**nothing** to force the reporter *after* the workers — the report can still run first. The combined
fix (lock **and** join) prunes both failure classes and prints `2` reliably. (This is the canonical
"a lock gives atomicity, not order" lesson, with both halves present at once.)

**Diagnoses.** Finding only one bug — or "one lock fixes it" — is the **atomicity/order conflation**
plus the **lock-as-blanket-spell** (Catalog §5c). The Advanced bar is seeing that the snippet sits in
**two** parts of the taxonomy at once and that each needs its matching remedy (atomic region *and*
happens-before edge), then confirming the combined fix prunes both — while stating that a green
forced repro is **necessary, not sufficient** over all schedules (§5d).

---

### Grading note (all Advanced drills)

Run the forced repro / deadlock-timeout first and **paste it** (`coaching-loop.md` → surface ground
truth); for A4-A2, **paste the run and then explicitly refuse to read it as proof**. Grade **D1
(reason about the set / force the schedule) · D2 (classify + GIL/SC status) · D3 (fix the right unit,
no new deadlock)** separately (§7, §5d), and **say it is softer than A1** — the runner forces *one*
schedule (or times out *one* deadlock) but cannot exhaust the interleaving space. A learner who fixes
the atomicity but misses the order edge (A4-A3), "fixes" the publication with a bare lock (A4-A2), or
predicts "exception" for a deadlock (A4-A1) is a **partial pass** — flag exactly which dimension fell
short. Promotion needs the **teach-it-back** principle ("a lock gives atomicity, not order"; "one run
is a sample of a schedule set"; "the GIL serializes bytecodes, it is not thread-safety"), not just
the instance.
