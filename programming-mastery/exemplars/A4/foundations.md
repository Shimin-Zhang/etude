# A4 — Foundations exemplars (concurrency mental models)

Golden drills for the **Foundations** tier of module A4: one mechanism on a familiar surface,
**named for the learner**. Predict the value under a *stated* interleaving, or answer a single
happens-before / GIL-atomicity question. Every executable sub-claim was obtained by **running it
through the runner** (`drill-generation.md` §2) — forced `Event` interleavings, deterministic
interleaving-set enumeration, and `dis` disassembly; the coach never guesses:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct mechanisms (atomicity / lost-update · GIL atomicity · happens-before
via `join`) — no repeated gotcha. Grading is **hybrid, leaning rubric** (§5d): the forced run /
enumeration / disassembly is executable ground truth; the *reasoning* is rubric-graded and the coach
**says so**. Pose one, **hard-stop, wait** (`coaching-loop.md`).

---

## A4-F1 — Lost update under a *stated* interleaving (atomicity)

Two threads each make a `+1` "deposit" to a shared balance starting at `0`. Each does
`tmp = shared["balance"]` (READ) then `shared["balance"] = tmp + 1` (WRITE). The scheduler runs the
four steps in this order: **`R1, R2, W1, W2`** (T1 reads, T2 reads, T1 writes, T2 writes).

> **Your turn:** After both threads finish under that interleaving, what is `shared["balance"]` —
> and is that the intended result of "two `+1` deposits on `0`"?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — the schedule is *forced* with `Event`s so it is deterministic:

```
# /tmp/A4_forced_lost_update.py  (interleaving pinned to R1 R2 W1 W2)
stdout: "two +1 deposits on 0; correct final = 2\nforced interleaving R1 R2 W1 W2 -> final = 1\n"
status: ok   (identical on 3/3 runs)
```

So the balance is **`1`**, not `2` — **one deposit is lost**. (And the full set: of the 6 valid
interleavings, **4 lose an update**, only 2 are correct — runner-verified in the worked example §4.)

**Why.** `shared["balance"] = tmp + 1` is a **read-modify-write**, not one atomic step. Under
`R1 R2 W1 W2` both threads READ `0` into their private `tmp` *before* either WRITES. T1 writes
`0+1=1`; T2 writes `0+1=1` on its **stale** `tmp` — T2's write clobbers nothing new and T1's update
is the one effectively lost. The two reads **overlap** the two writes, with no ordering between the
deposits.

**Diagnoses.** Predicting `2` reveals the **read-modify-write-as-one-step** blind spot — not seeing
the schedulable window between READ and WRITE (Catalog §5c: "treats a read-modify-write as a single
indivisible step"). If the learner says "but it would print 2 if you just ran it," that is the
**one-green-run-as-proof** error (§5c) — true on CPython most of the time, and still wrong: the set
has 4 losing schedules. Name the window; classify it as an **atomicity** violation (Lu et al.).

---

## A4-F2 — Which of these are atomic? (the GIL, precisely)

A teammate says "the GIL makes Python thread-safe, so I don't need locks." Consider four shared-state
updates:

```python
D[x] = y                # (a)
D[x] = D[x] + 1         # (b)
L.append(x)             # (c)
i = i + 1               # (d)
```

> **Your turn:** Per CPython's actual guarantee, which of (a)–(d) are **atomic** (cannot be
> interrupted partway by another thread), and which are **not**? State the rule you used.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** — the Python docs FAQ (*"What kinds of global value mutation are
thread-safe?"*) lists **(a)** and **(c)** as atomic and **(b)** and **(d)** as *not*; the
disassembly shows *why*:

```
# /tmp/A4_dis_dict_rmw.py :  D["n"] = D["n"] + 1   (NOT atomic)
      BINARY_SUBSCR     ← READ shared D['n']
      BINARY_OP   0 (+) ← MODIFY
      STORE_SUBSCR      ← WRITE shared D['n']    (another thread can run between READ and WRITE)

# /tmp/A4_dis_atomic_store.py :  D["k"] = y        (atomic)
      LOAD_FAST_LOAD_FAST (y, D)
      LOAD_CONST  'k'
      STORE_SUBSCR      ← a single WRITE; no read-of-target to interleave
status: ok   (Python 3.13.2)
```

So: **(a) `D[x]=y` atomic** (one `STORE_SUBSCR`), **(b) `D[x]=D[x]+1` NOT** (read then write),
**(c) `L.append(x)` atomic** (the mutation is one `CALL` into C that doesn't release the GIL),
**(d) `i=i+1` NOT** (read then write).

**Why.** The GIL "ensure[s] that only one thread runs in the Python VM at a time" and switches
"only between bytecode instructions," so **each single bytecode is atomic from a Python program's
point of view**. An op that touches the shared location in **one** bytecode (or one C call behind one
bytecode) is atomic; a **read-modify-write** is several bytecodes — a READ, then a separate WRITE —
with a schedulable gap. The teammate is wrong: the GIL prevents *torn* low-level reads, not *lost
updates*, and it is a **CPython implementation detail** (PyPy differs; 3.13 ships an experimental
no-GIL build, PEP 703), not a language guarantee.

**Diagnoses.** Marking (b) or (d) atomic — or "all of them, because GIL" — is the
**"GIL = thread-safe"** misconception (Catalog §5c). The fix is the rule, not the vibe: *atomic iff
the shared access is a single bytecode; a read-modify-write never is.* Never "Python is thread-safe."

---

## A4-F3 — Is this read a race? (happens-before via `join`)

A worker thread writes a result; the main thread reads it **after `t.join()`**:

```python
import threading
result = {}
def worker():
    result["v"] = 99             # the thread's write
t = threading.Thread(target=worker)
t.start()
t.join()
print("after join, main reads:", result["v"])
```

> **Your turn:** Is the main thread's read of `result["v"]` a **race** (could it see a missing or
> half-written value), or is it **safe**? Say which ordering rule decides it.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
stdout: "after join, main reads: 99\n"
status: ok   (identical on 3/3 runs)
```

It is **safe** — reliably `99`, no race.

**Why.** `t.join()` establishes a **happens-before edge**: *everything the worker did* is ordered
**before** *everything after `join` in the main thread*. So the write `result["v"] = 99` is ordered
before the read — they are **not concurrent**, so there is no data race. (Contrast: delete the
`t.join()` and read immediately after `start()`, and the read and the write become **concurrent** —
no ordering edge either way — which *is* a race; the main thread could read before the worker writes
and raise `KeyError`.) `join` is one of the standard happens-before edges, alongside program order
within a thread, `start`→the thread, lock release→acquire, `Event.set()`→`wait()`, and queue
`put`→`get`.

**Diagnoses.** Calling the **post-join** read racy reveals **no happens-before model** — not knowing
`join` orders the thread's writes before the continuation (Catalog §5c: "cannot say which pairs of
events are ordered"). Calling the **no-join** version safe reveals the same gap from the other side
(treating concurrent accesses as if ordered). The skill is naming the *edge* (or its absence), per
Lamport's partial order.

---

### Grading note (all Foundations drills)

Run the forced interleaving / enumeration / disassembly first and **paste it** (`coaching-loop.md` →
surface ground truth). Then grade the *reasoning* against §7 (D1 reason about the set · D2 classify ·
D3 right-unit fix) and **say it is softer than an executable pass** (§5d): the runner proves a bug
exists on *one* forced schedule (or across a tiny enumerated set), but cannot certify correctness
over *all* schedules. A correct value with a hand-wavy "why" is a **partial pass** — flag it
(`evidence-base.md` → illusions of fluency).
