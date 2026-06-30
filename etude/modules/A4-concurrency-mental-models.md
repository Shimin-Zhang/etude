# A4 — Concurrency Mental Models `[Verified-adjacent]`

> **Module type.** Mixed-status by design: **`[Verified-adjacent]` model + `[Practitioner-canon]`
> formalism/facts**. The *concurrent notional machine* extends A1's single-threaded execution
> model (`evidence-base.md` → Finding 1, `[Verified]`) into **N interleaved instruction streams**
> — that extension is `[Verified-adjacent]` (sound CS resting on a verified base, but "drilling it
> improves experienced engineers" is the open transfer question). The *formalism* it teaches — the
> **happens-before** partial order (Lamport 1978) and **sequential consistency** (Lamport 1979) —
> is foundational, rigorously-established CS **theory** (definitions and models by a major figure),
> badged `[Practitioner-canon]` (foundational) because it is exact theory whose use as a
> *reasoning method* is craft, **not** an empirical learning finding. What **CPython's GIL** does
> and does not make atomic is **documented fact** (Python docs), badged `[Practitioner-canon]`
> (documentation). The validator badge on this file is `[Verified-adjacent]`; the honest prose
> badge is the mixed one above.
>
> **Core idea.** With one thread you pick the order: statements run top to bottom and you *are* the
> machine (A1). With **N threads you no longer pick the order** — the **scheduler** interleaves the
> threads' instruction streams, so the *same code over the same inputs has many possible
> executions*. The skill is to stop reasoning about **the one run you got** and start reasoning
> about **the *set* of interleavings**: is there *any* schedule that breaks the intended invariant?
> A4 owns this **model**; sibling **C3** owns *debugging* races and references A4 softly.

---

## 1. Evidence basis `[Verified-adjacent]` model + `[Practitioner-canon]` formalism/facts

This module is **mixed-status** and the coach must never present its canon/theory halves as
verified *learning* science (`evidence-base.md` → badge rules). Four pillars: one extends a
verified finding, two are foundational CS theory + documented fact, and one is reused from C3.

**(a) The concurrent notional machine — extends Finding 1 `[Verified-adjacent]`.** A1's verified
result is that the durable barrier is grasping the **runtime dynamics of execution** — being able
to *simulate the machine* step by step rather than read code for intent (`evidence-base.md` →
Finding 1; Sorva 2013; du Boulay 1986; both `[Verified]`). A4 removes A1's single-machine
assumption: instead of *one* program counter advancing deterministically, there are **N counters**,
and an **interleaving** is one particular merge of their steps, chosen by the OS/runtime scheduler.
This is `[Verified-adjacent]` for the same reason C3's taxonomy half is — it *extends* a
`[Verified]` execution-model finding into the concurrent setting on solid ground, **not** because
"teaching interleaving-reasoning causally improves engineers" has been shown (it has not; that is
the open transfer question every module here carries).

**(b) The happens-before partial order & sequential consistency — Lamport `[Practitioner-canon]`
(foundational CS theory).** Cite via `evidence-base.md` → *Concurrency mental models (module A4)*
(proposed addition). Two definitions, by the field's founding figure, that the whole module reasons
with:

- **Lamport, L. (1978). Time, Clocks, and the Ordering of Events in a Distributed System.**
  *Communications of the ACM*, 21(7), 558–565. doi:10.1145/359545.359563. The origin of the
  **"happened-before" relation** (written `→`), a **partial ordering** of events: within a single
  process events are ordered by program order; a message send is ordered before its receipt; the
  relation is transitive. Two distinct events with **no `→` path either way are *concurrent*** —
  neither can causally influence the other. The shared-memory specialization the module uses
  (program order within a thread; `start`→the thread; the thread→`join`; a lock release→a
  subsequent acquire; an `Event.set()`→a `wait()` that observes it; a queue `put`→its `get`) is the
  standard concurrency adaptation of Lamport's relation. *A mathematical model by a major figure —
  not an empirical learning result.*
- **Lamport, L. (1979). How to Make a Multiprocessor Computer That Correctly Executes Multiprocess
  Programs.** *IEEE Transactions on Computers*, C-28(9), 690–691. doi:10.1109/TC.1979.1675439. The
  canonical definition of **sequential consistency** (the intuitive "there is *some* global
  interleaving" model): *"the result of any execution is the same as if the operations of all the
  processors were executed in some sequential order, and the operations of each individual processor
  appear in this sequence in the order specified by its program."* This is the model A1 silently
  assumes and that A4 makes explicit — and the reason **weaker** real-world memory models are a
  hazard. *A definition/correctness-condition by a major figure — not an empirical result.*

**(c) What CPython's GIL makes atomic — `[Practitioner-canon]` (documentation, factual).** Cite via
the same proposed addition. The **Python docs Programming FAQ**, *"What kinds of global value
mutation are thread-safe?"*, states (verified verbatim during authoring): a **global interpreter
lock (GIL)** "is used internally to ensure that only one thread runs in the Python VM at a time";
"Python offers to switch among threads only between bytecode instructions; how frequently it
switches can be set via `sys.setswitchinterval()`"; and therefore "**each bytecode instruction …
is … atomic from the point of view of a Python program.**" The FAQ then lists operations that
**are** atomic (e.g. `L.append(x)`, `x = L[i]`, `D[x] = y`, `D1.update(D2)`, `x = y`,
`x.field = y`) and ones that are **not** (`i = i+1`, `L.append(L[-1])`, `L[i] = L[j]`,
`D[x] = D[x] + 1`). These are **documented facts about the reference implementation**, *not* a
language guarantee: the GIL is a CPython implementation detail (PyPy/Jython differ; CPython 3.13
ships an experimental **free-threaded / no-GIL build**, PEP 703), so the module teaches the facts
**and** the bound — *never* "Python is thread-safe."

**(d) The concurrency-bug taxonomy — Lu et al. 2008, REUSED from C3 `[Verified-adjacent]`.** A4 does
**not** re-derive this; it is already in the evidence base. Cite via `evidence-base.md` →
*Production & concurrency debugging (module C3)*. The two patterns the classification drills use —
**atomicity violation** ("the desired serializability among multiple memory accesses is violated";
a region meant to be atomic is interleaved) and **order violation** ("the desired order between two
(groups of) memory accesses is flipped") — cover **72 of 74** non-deadlock bugs in Lu, Park, Seo &
Zhou's study of 105 real bugs (MySQL/Apache/Mozilla/OpenOffice; ASPLOS '08). A4 uses this taxonomy
as the **vocabulary for classifying an interleaving**; C3 uses it for *debugging*. (Findings A4
leans on: most bugs are **≤ 2 threads** (101/105) and **one variable** (66%) — so the gym lives at
two threads over one or two shared cells, which is also the runner's practical limit.)

**Why these license this module.** (a) makes the *machine* honest (interleavings extend the verified
notional machine); (b) gives the *reasoning tools* (happens-before to say what is ordered vs
genuinely concurrent; sequential consistency to name the intuitive model and its limits); (c) gives
the *Python-specific facts* (what the GIL really guarantees); (d) gives the *classification
vocabulary* (atomicity vs order). The combined claim the module teaches: **a concurrent program is
correct only if *every* interleaving preserves its invariants; reason about that set using
happens-before, classify the breaks as atomicity or order violations, and never mistake CPython's
GIL for thread-safety.**

**Read through the transfer caveat.** The *model* (a) rests on `[Verified]` Finding 1 but its
*causal* benefit for experienced engineers is unproven; the *formalism* (b) is exact theory, not a
learning study; the *facts* (c) are documentation; the *taxonomy* (d) is descriptive field data
from C/C++ circa 2008, **not** Python and **not** a pedagogy result. The *direction* is well
grounded; that drilling interleaving-reasoning *causally* improves real concurrent-code work is the
open question (`evidence-base.md` → transfer caveat). The transfer task (§9) — a real race in the
learner's own code — is the honest individual-level test. **Sibling note:** *debugging* races under
non-reproducibility, heisenbugs, and production observability are **C3 (production & concurrency
debugging)**; A4 owns the *model* C3 leans on.

---

## 2. Soft prerequisites

**A1 (notional machine) is the load-bearing prerequisite.** A4 *is* A1 with the single-machine
assumption removed. Every concurrency bug here is an A1 event — a read, a rebind, a mutation —
that goes wrong because *another stream's* event landed in between. A learner shaky on
rebinding-vs-mutation or "when does code run" (A1 §3) will not see why a non-atomic `+=` loses an
update, because they do not yet see `+=` as a **read-modify-write of three separable steps**. The
single most important A1 carry-over: *a name is a label bound to an object, and assignment is a
read of the right side then a rebind of the left* — concurrency splits exactly that read from that
write.

**A3 (tracing) helps** — reasoning about an interleaving is **tracing two streams at once**, and
A3's "externalize the state, don't hold it in your head" discipline is what makes an interleaving
table tractable.

**C3 (production & concurrency debugging) is the sibling, not a prerequisite.** C3 *debugs* races
(classify, instrument, hypothesize under non-reproducibility, heisenbugs); A4 owns the *model* C3
references. A learner can take them in either order; they reinforce each other.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any learner
may open any module at any tier). If a learner flails at A4 because they cannot trace a *single*
thread, the coach notes the gap likely traces to A1/A3 and *suggests* shoring those up — but does
not forbid A4. A learner fluent in single-threaded simulation who has simply **never had to give up
choosing the order** is exactly who A4 is for.

---

## 3. The mental model

**With one thread, you choose the order and the machine is deterministic (A1). With N threads, the
*scheduler* chooses the order: it interleaves the threads' instruction streams, so the same code
over the same inputs has *many possible executions*. A concurrent program is correct only if
*every* interleaving preserves its invariants — so you stop reasoning about the one run you got and
start reasoning about the *set* of runs the scheduler is allowed to produce.**

A1's state model, plus exactly what concurrency changes:

| Aspect | Single-threaded (A1) | Concurrent (A4) — what's new |
|---|---|---|
| **Instruction stream** | **One** program counter, advancing top-to-bottom; *you* pick the path. | **N** counters. An **interleaving** is one merge of the threads' steps that preserves each thread's own program order. The **scheduler** picks it — you don't. The same code has a **set** of possible executions. |
| **Atomicity of a "step"** | Treating one statement as one step is fine — nothing interrupts it. | A statement like `x += 1` is **several bytecode steps** — *read, modify, write* — and another thread's steps can land **between** them. **"One source line" ≠ "one atomic step."** This gap is where **atomicity violations** live. |
| **Ordering between events** | A **total** order: everything is "before" or "after" in program order. | A **partial** order — **happens-before** (Lamport 1978). Only *some* pairs are ordered: program order within a thread; `start`→the thread; the thread→`join`; lock release→a later acquire; `Event.set()`→a `wait()` that sees it; queue `put`→its `get`. Pairs with **no** ordering either way are **concurrent**. |
| **Memory visibility** | A write is immediately visible to the next read. | Under **sequential consistency** (Lamport 1979) there is *some* global order consistent with each thread's program order — the intuitive model. Real hardware/compilers use **weaker** models that may reorder unless a happens-before edge forbids it. CPython's **GIL** gives strong, near-SC *bytecode-level* behavior — but it is an **implementation detail**, and it does **not** make a multi-bytecode read-modify-write atomic. |
| **What "correct" means** | Trace the **one** path; that *is* the behavior. | The program is correct **iff every interleaving** preserves the invariant. A green run is **one sample** of the set, not a proof. The bug lives in a schedule you didn't sample. |

**Two distinctions the module forces, because conflating them sends the fix the wrong way:**

- **Data race vs. race condition.** A **data race** is the low-level event: two threads access the
  *same location*, **at least one is a write**, and the accesses are **not ordered by
  happens-before** (genuinely concurrent). A **race condition** is the higher-level fault: program
  **correctness depends on the schedule**. They are *not* the same set. A check-then-act
  (`if k not in cache: cache[k] = compute()`) built from individually-**atomic** dict operations has
  **no data race** on any single access — yet it is a **race condition** (both threads can pass the
  check and both compute). CPython's GIL removes most low-level *data races* (no torn reads of an
  object reference) but does **nothing** about *race conditions* — which is the precise reason
  "the GIL makes Python thread-safe" is false.
- **Atomicity vs. order (Lu et al.).** An **atomicity violation** = a region *meant* to be
  indivisible was interleaved (fix: make the *whole* region atomic — a lock). An **order
  violation** = A was *meant* to precede B and the order flipped (fix: an explicit **happens-before
  edge** — a `join`, an `Event`, a queue). A lock gives **atomicity, not order**: wrapping a
  use-before-init in a lock does not make the initializer run first.

**The discipline in one line: *reason about the set of interleavings, not the run you got.*** The
run you observed is **one sample** of a nondeterministic space the scheduler — not you — chose. A
green local run does not mean "correct"; it means "*this* schedule was fine." On CPython the trap is
sharpest: the GIL makes the bad schedule *rare*, so a racy `+=` loop will very often print the right
total — and look correct while being wrong.

Three corollaries the module drills:

1. **A read-modify-write is several steps; the scheduler may interleave between them.** `x += 1` is
   `read x → add 1 → write x`. Two threads each reading the old `x` before either writes ⇒ one
   update is **lost** (an **atomicity violation** — the largest class in Lu et al., 51/74). The fix
   makes the *whole* read-modify-write atomic, not "adds a lock somewhere."
2. **You only get the orderings you establish.** Anything not connected by a happens-before edge is
   **concurrent** and may interleave (or, under a weak memory model, be reordered). If thread B must
   run *after* A, you need an explicit edge (`join`/`Event`/queue) — a shared lock gives mutual
   exclusion, **not order** (an **order violation** survives a lock).
3. **The GIL is not thread-safety.** It serializes *bytecodes* (so some *single* ops are atomic) but
   a multi-bytecode read-modify-write is **not** atomic, and the GIL is a CPython implementation
   detail (no-GIL builds exist), **not** a language guarantee. Never reason "Python is thread-safe."

---

## 4. Worked example — the *set* of interleavings of two `+1`s

*(Foundations depth: every step shown, with runner-confirmed ground truth. This fades by tier —
see the table after.)*

The A4 move is not "trace the run" — it is **enumerate the set of runs the scheduler may produce and
ask whether *any* breaks the invariant.** Two threads each make a `+1` "deposit" to a shared balance
starting at `0`. Intended invariant: *two deposits ⇒ final balance is `2`.* Each thread does:

```python
def deposit(shared):
    tmp = shared["balance"]        # R: READ shared into a private temp
    shared["balance"] = tmp + 1    # W: WRITE temp+1 back (read-modify-write, NOT atomic)
```

**Step 1 — Confirm the step is not atomic.** "It's one `+=`" is the trap. Disassembled, a dict
read-modify-write is a **read** (`BINARY_SUBSCR`) and a separate **write** (`STORE_SUBSCR`) with a
schedulable gap between — exactly the FAQ's non-atomic `D[x] = D[x] + 1`. **Runner-verified**
(`drill-generation.md` §2 — the coach *runs* it, never asserts bytecode):

```
# /tmp/A4_dis_dict_rmw.py:  def bump(D): D["n"] = D["n"] + 1
  3   LOAD_FAST                0 (D)
      LOAD_CONST               1 ('n')
      BINARY_SUBSCR            ← READ shared D['n']
      LOAD_CONST               2 (1)
      BINARY_OP                0 (+)   ← MODIFY
      LOAD_FAST                0 (D)
      LOAD_CONST               1 ('n')
      STORE_SUBSCR             ← WRITE shared D['n']   (another thread can run between READ and WRITE)
status: ok   (Python 3.13.2)
```

(Contrast: the FAQ-atomic `D['k'] = y` is a *single* `STORE_SUBSCR` with **no** read of the target —
nothing to interleave.)

**Step 2 — Enumerate the set.** Each thread runs `R` then `W`; a valid interleaving merges the four
steps `R1 W1 R2 W2` while preserving `R1<W1` and `R2<W2`. There are `C(4,2)=6` of them. Be the
machine for *each* and record the final balance. **Runner-verified** (a deterministic simulation of
all six schedules):

```
# /tmp/A4_enum_interleavings.py
R1 W1 R2 W2 -> final 2 (OK)
R1 R2 W1 W2 -> final 1 (LOST UPDATE)
R1 R2 W2 W1 -> final 1 (LOST UPDATE)
R2 R1 W1 W2 -> final 1 (LOST UPDATE)
R2 R1 W2 W1 -> final 1 (LOST UPDATE)
R2 W2 R1 W1 -> final 2 (OK)
valid interleavings: 6 | correct: 2 | lose an update: 4
status: ok
```

**The set tells the whole story: 4 of 6 interleavings lose an update.** And look at *which* two are
correct — `R1 W1 R2 W2` and `R2 W2 R1 W1`: exactly the schedules where one thread's read-modify-write
*completes before the other's begins* (a happens-before ordering between the two deposits). The four
broken ones are precisely those where the two reads happen **before** both writes — the
read-modify-writes **overlap**, with no ordering between them. **Overlap with a shared write = the
race.** This is the atomicity violation, seen as a property of the *set*, not of one run.

**Step 3 — Why a naive run hides it (the CPython trap).** If you just launch two threads doing
`counter += 1` in a loop, the GIL makes the bad schedule rare, so you usually get the *correct*
total. **Runner-verified** — two threads, 100 000 increments each, five runs:

```
# /tmp/A4_naive_race.py
expected 200000  actual 200000  no loss (this sample)
expected 200000  actual 200000  no loss (this sample)
expected 200000  actual 200000  no loss (this sample)
expected 200000  actual 200000  no loss (this sample)
expected 200000  actual 200000  no loss (this sample)
status: ok
```

Five green runs — yet the set in Step 2 *proves* 4 of 6 interleavings are wrong. **A green run is one
sample, not a proof.** (This is why the gym **forces** a bad schedule rather than hoping to observe
one.)

**Step 4 — Force one element of the broken subset and confirm.** Pin the schedule to `R1 R2 W1 W2`
(the second row) with `Event`s — a happens-before edge that makes the interleaving deterministic:

```python
import threading
shared = {"balance": 0}
t1_read = threading.Event(); t2_read = threading.Event()

def t1():                                 # deposit +1
    tmp = shared["balance"]               # R1  (reads 0)
    t1_read.set()
    t2_read.wait()                        # pin: T2 must READ before T1 WRITES
    shared["balance"] = tmp + 1           # W1  (writes 0+1 = 1, on a STALE read)

def t2():                                 # deposit +1
    t1_read.wait()                        # pin: T1 has READ
    tmp = shared["balance"]               # R2  (reads 0 -- T1 has not written)
    t2_read.set()
    shared["balance"] = tmp + 1           # W2  (writes 0+1 = 1)

a = threading.Thread(target=t1); b = threading.Thread(target=t2)
a.start(); b.start(); a.join(); b.join()
print("two +1 deposits on 0; correct final = 2")
print("forced interleaving R1 R2 W1 W2 -> final =", shared["balance"])
```

**Runner-verified ground truth** (deterministic across runs — the forced schedule removes the
nondeterminism, so the bug is reproducible every time):

```
stdout: "two +1 deposits on 0; correct final = 2\nforced interleaving R1 R2 W1 W2 -> final = 1\n"
status: ok   (identical on 3/3 runs)
```

**Step 5 — Classify and name the fix.** This is an **atomicity violation** (Lu et al.): R and W were
*meant* to be one indivisible unit, but the atomicity was not enforced, so T2 interleaved between
them. It is **not** an order violation — neither deposit is "supposed to" go first; the fault is the
**overlap**. The fix makes the *whole* read-modify-write atomic (one lock held across R **and** W),
which eliminates the four overlapping interleavings from the set — leaving only the two correct
serial ones. (Adding a lock around *only* the read, or only the write, does not: re-enumerate the
set and the overlap survives.)

**What this makes visible** (and "it just adds two `+1`s" hides): the bug is **not on any single
line** — every line is correct alone. It is a property of the **set of interleavings**, the majority
of which violate the invariant, and it is **invisible in the run you happened to get**. Reasoning
about the set — not the sample — is the whole skill.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), the full
> enumerate-the-set-plus-force-it walkthrough helps **novices** (it shows the move) but is
> **redundant load for the more advanced**, who learn more by enumerating the set themselves. So the
> coach fades it:
>
> | Tier | Worked-example depth at A4 |
> |---|---|
> | **Foundations** | **Full** — the disassembly, the complete six-row interleaving set, the heisenbug warning, the forced repro, and the classification, every step shown. |
> | **Working** | **Partial** — coach gives the snippet and that *an* interleaving loses an update, but leaves the **set** (enumerate the schedules; which overlap?) and the **classification** to the learner. |
> | **Advanced** | **Skeleton** — coach hands over the snippet only; the learner enumerates the set, identifies the breaking subset via happens-before, classifies it per Lu et al., and names the fix that prunes the right interleavings, unaided. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for A4. Grading mode is declared
up front: **hybrid, leaning rubric + exemplars** (§5d). Concurrency nondeterminism resists
single-output executable grading, so the **reasoning** (which interleaving breaks the invariant;
what is ordered by happens-before; atomicity vs order; is the GIL relevant) is rubric-graded against
gold exemplars; the **runner is used for every deterministic sub-claim** — force the interleaving and
show the lost update / order-violation crash / deadlock timeout; disassemble to prove a step is
non-atomic; classify a snippet whose forced misbehavior is runner-confirmed.

### 5a. Tier definitions (A4-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. Every drill is
a **reasoning-about-the-model** drill (enumerate/describe an interleaving; check happens-before;
classify; predict whether the GIL saves it), and any executable sub-claim is **forced and
runner-confirmed**:

| Tier | A4 criterion | Example shape |
|---|---|---|
| **Foundations** | One mechanism on a familiar surface, **named for them**: given a 2-thread non-atomic counter, *predict the final value under a stated interleaving*, or *is there an interleaving that breaks the invariant?* Or: *is this operation atomic per the GIL?* (recall + disassembly). Or: *does `join` make this read safe?* (one happens-before edge). | The lost-update counter under `R1 R2 W1 W2`; "is `D[x]=D[x]+1` atomic?"; "read after `t.join()` — race or not?" |
| **Working** | Apply in an unseen context where the **schedule** matters and intent/execution diverge: **classify** a race as **atomicity vs order** (Lu et al.) and say *why*; distinguish a **data race** from a **race condition** (check-then-act); or judge a **"the GIL makes this safe"** claim. Predict + name the mechanism. | Use-before-init (order); check-then-act double-compute (race condition, no data race); "a lock fixes my counter but the init still flips." |
| **Advanced** | Combine two or more mechanisms, or reason about the **memory model**: a bug needing *both* an atomicity fix *and* an order edge; a **deadlock** from lock-ordering; a publication/flag pattern where **sequential consistency** is the silent assumption ("works on CPython — is that a guarantee?"). Find it, **enumerate/where-needed force** it, classify, propose the fix that targets the right unit, **explain why a lock alone is/ isn't enough**. | Deadlock via opposite lock order (runner times out); flag-publication + weak memory; double-fix (atomicity + ordering). |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations drill secretly needs the learner to *discover* the race class
unaided (that's Working), or an Advanced drill is a single isolated atomicity violation with no
second mechanism, no ordering, and no memory-model wrinkle. Apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for A4:

- **Mechanism** — atomicity violation (lost update / non-atomic read-modify-write) · atomicity
  violation (check-then-act / TOCTOU) · order violation (use-before-init / read-before-write) ·
  order violation (publish-then-consume) · **deadlock** (circular wait / lock ordering) ·
  **happens-before reasoning** (is this pair ordered or concurrent?) · **GIL atomicity** (is this op
  atomic?) · **memory model** (does this rely on sequential consistency?).
- **Reasoning artifact** — *the final value under a stated interleaving* · *whether any interleaving
  breaks the invariant* · *the breaking subset of the interleaving set* · *the classification
  (atomicity / order / deadlock / not-a-race)* · *data race vs race condition* · *whether the GIL
  makes it safe* · *the right-unit fix (atomic region / happens-before edge / lock ordering)*.
- **Scale of the interleaving** — two threads, one variable (the Lu common case) · two threads, two
  variables · two threads, two locks (deadlock). **Keep thread count at two** — real bugs are small
  (Lu Finding 3: 96% ≤ two threads) *and* the runner's 256 MB address-space cap and ~2-thread
  practical limit make many OS threads unreliable.
- **Determinism of the demo** — deterministic-once-forced (`Event`/`Barrier` pins the schedule) ·
  *naively nondeterministic* (the point of the drill is that the green run is a sample) ·
  *GIL-masked* (the bug cannot be observed on CPython at all — reason about the model, don't run).
- **Format** (`drill-generation.md` §6) — primarily **Prediction → Observation → Reflection**
  (predict the value/whether-it-breaks under a schedule; the runner forces it) and **Trace-the-path**
  (step a chosen interleaving). Also **Debug-this** (a racy snippet to classify), **Error analysis**
  ("here's a *fix* someone applied — does it prune the breaking interleavings, or only narrow the
  window?"), and **Teach-it-back** (articulate happens-before, or why the GIL isn't thread-safety).

Keep an in-session log of the `(mechanism, reasoning artifact, scale, determinism, format)` tuples
used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* A4 errors, each with the conceptual gap it diagnoses (`drill-generation.md` §1c
format). Grounded in the concurrency-bug taxonomy (Lu et al. 2008), the happens-before / sequential
-consistency formalism (Lamport 1978/1979), and the documented GIL facts (Python FAQ) — not trivia.
**The root of most of them is one over-extension of A1's single-machine model: "the run I observed
is *the* behavior, and one source line is one step."** The concurrent reality: "the run I observed
is **one sample** of a set the scheduler chose; a source line may be several steps; and only the
orderings I *established* (happens-before) actually hold."

```
Error: Concludes a concurrent program is correct because it ran correctly (locally, a few times,
       on CPython) -- treats one green run as proof.
Diagnoses: "The run I got is THE behavior" -- no model of the schedule as a free variable. Samples
           one interleaving and generalizes; the bug lives in an unsampled (often GIL-rare)
           schedule. (Module §3 corollary 1; §3 "discipline in one line.")
Example trigger: the naive `counter += 1` two-thread snippet that prints the correct total on this
                 CPython -- "is this correct, or just lucky? enumerate the set."

Error: Treats a read-modify-write (`x += 1`, `cache[k] = compute()`, `D[x] = D[x]+1`) as a single
       indivisible step, so cannot see how an update is lost.
Diagnoses: A1 gap surfacing under concurrency -- does not decompose the statement into
           read/modify/write, so the interleaving window between READ and WRITE is invisible. The
           atomicity-violation blind spot. (Lu et al.: 51/74 non-deadlock bugs are atomicity
           violations; the disassembly makes the gap concrete.)
Example trigger: enumerate the six interleavings of two `+1`s; predict how many lose an update.

Error: Believes "the GIL makes Python thread-safe," so concludes a shared `+=` (or check-then-act)
       is safe without synchronization.
Diagnoses: Over-reads the GIL: it serializes BYTECODES (so single ops are atomic) but does NOT make
           a multi-bytecode read-modify-write atomic, and it is a CPython implementation detail, not
           a language guarantee. Confuses "no torn reads" with "no race condition." (Python FAQ; §3
           corollary 3; PEP 703 no-GIL builds.)
Example trigger: "is `i = i + 1` atomic? is `L.append(x)`? does the GIL save my shared counter?" --
                 disassemble and enumerate.

Error: Confuses an atomicity violation with an order violation (or cannot tell them apart), so sends
       the fix the wrong way.
Diagnoses: No working grip on the Lu et al. taxonomy: atomicity = a region meant to be indivisible
           was interleaved (fix: make the region atomic); order = A was meant to precede B and the
           order flipped (fix: a happens-before edge). A lock fixes the first, not the second.
Example trigger: classify check-then-act (atomicity) vs loader/user use-before-init (order), and say
                 which fix each needs.

Error: Adds a lock and assumes order is now guaranteed (or that any lock = thread-safe), e.g. wraps
       a use-before-init in a shared lock and expects the initializer to run first.
Diagnoses: Models "lock = thread-safe spell." Misses that a lock gives MUTUAL EXCLUSION, not
           ORDER -- an order violation survives a lock -- and that the lock must cover the WHOLE
           read-modify-write to give atomicity. (Lu Finding 9: 73% of fixes are NOT just adding/
           changing locks; §3 corollary 2.)
Example trigger: a use-before-init "fixed" by one shared lock -- show (force) the order can still
                 flip; the real fix is a happens-before edge (join/Event/queue).

Error: Cannot say which pairs of events are ordered, so cannot tell a real race from a safe access,
       e.g. thinks a read after `t.join()` is racy, or that two unsynchronized writes are ordered.
Diagnoses: No happens-before model -- does not know the edges (program order; start->thread;
           thread->join; lock release->acquire; Event.set->wait; queue put->get) or that pairs with
           no edge either way are CONCURRENT (and concurrent + shared + a write = a data race).
           (Lamport 1978; §3 ordering row.)
Example trigger: "value written by a thread and read after `t.join()` -- race or not?" (not: join
                 orders it) vs "...read WITHOUT join -- race or not?" (yes).

Error: Conflates a data race with a race condition -- e.g. calls check-then-act "fine, no data race"
       and stops, or calls every race a "data race."
Diagnoses: Misses that the two sets differ: a data race is unsynchronized same-location access with
           a write; a race condition is correctness depending on schedule. Check-then-act over atomic
           ops has NO data race yet IS a race condition; the GIL removes the former, not the latter.
           (§3 "data race vs race condition.")
Example trigger: the check-then-act double-compute (force it: compute runs twice) -- "is there a
                 data race? is there a race condition? which, and why?"

Error: Assumes the publish-then-consume / flag pattern is safe because "it worked," reasoning as if
       memory were sequentially consistent.
Diagnoses: Takes sequential consistency for granted -- no model that real memory models are weaker
           and reorder absent a happens-before edge, and that CPython's GIL HAPPENS to mask this so
           the run is not evidence of portability/correctness. (Lamport 1979; §3 memory-visibility
           row.)
Example trigger: `data = x; ready = True` // `while not ready: pass; use(data)` -- "it completes on
                 CPython; is that a guarantee? what edge would make it one?"

Error: Reaches for a lock-ordering fix that deadlocks, or cannot see why two correct critical
       sections deadlock together.
Diagnoses: No model of circular wait / lock ordering -- two locks acquired in opposite orders on two
           threads, each holding one and waiting for the other. (Lu et al.: deadlock is 31/105 bugs;
           the runner reports this as a TIMEOUT.)
Example trigger: two threads, lock_a then lock_b vs lock_b then lock_a -- predict whether it
                 completes; the runner times out.

Error: Tries to "see" a race by adding a print/sleep and declares it gone when the symptom vanishes.
Diagnoses: No heisenbug model -- the probe perturbs the schedule and can hide the bug; disappearance
           is evidence the schedule moved, not that the bug is fixed. (This is the doorway to C3 --
           A4 names it; C3 debugs it.)
Example trigger: a latent lost-update that a `print` between READ and WRITE "fixes" -- ask what the
                 probe proved. (Hand off to C3 for the debugging workflow.)
```

### 5d. Grading mode

**Hybrid, leaning rubric + exemplars** (`drill-generation.md` §1d, §3). This is **softer than a pure
executable pass, and the coach says so** — concurrency correctness is a property of *all* schedules,
which a single run cannot certify, so the *reasoning about the set* is the graded object. The
procedure, made concrete for A4:

1. **Run every deterministic sub-claim through the runner first** (`drill-generation.md` §2). Force
   the interleaving with an `Event`/`Barrier` and show the **lost update / use-before-init crash /
   check-then-act double-compute / deadlock timeout**; **disassemble** to prove a step is/ isn't
   atomic; **enumerate** the interleaving set with a deterministic simulation. Then apply the
   learner's (or the gold's) **fix** and re-run to confirm it prunes the breaking schedule. A learner
   who *disputes* whether a schedule exists gets the **forced-interleaving run** as evidence.
   Classifications are anchored to runner output, never to the coach's guess. **Honesty note the
   coach states out loud:** a *naive* (unforced) racy snippet may print the *correct* answer on a
   given run — that is the heisenbug/GIL-masking, *not* a refutation; demonstrate the bug via the
   **forced** schedule (or the **enumerated set**) and say the green naive run is one sample.
2. **Score the reasoning against the A4 rubric (§7), criterion by criterion** — *did they reason
   about the set (find a breaking interleaving / enumerate the breaking subset)? did they classify it
   correctly (atomicity vs order vs deadlock vs not-a-race; data race vs race condition)? did they
   target the fix at the right unit (whole read-modify-write atomic / a happens-before edge /
   consistent lock ordering) and not "just add a lock"? did they get the GIL/memory-model status
   right?* Each is a 3-point criterion (§7), graded explicitly.
3. **Cite the closest golden exemplar.** Compare to the tier's golds in `exemplars/A4/<tier>.md` —
   "close to the **weak** exemplar: you saw the lost update but called it an order violation" vs.
   "close to the **strong** exemplar: enumerated the set, classified it as atomicity, made the whole
   RMW atomic, and showed the breaking interleavings are pruned."
4. **Name it as soft — explicitly softer than A1's executable grading.** The coach says: "**this is
   a judgment call graded against the module's rubric + exemplars, and it is softer than a pure
   executable pass: I can force one breaking schedule (or enumerate the set of a tiny example) to
   prove a bug exists, but I cannot run *all* schedules of a real program to prove your fix is
   complete — so I'm grading your reasoning about the schedule space, not just an output**"
   (`drill-generation.md` §3; `assessment.md` §1.2). Do **not** conflate "the forced repro now prints
   the right answer after your fix" with "proven correct under all interleavings."

A4 drills are thus hybrid, and the coach **reports the verdicts separately**: a learner who
*describes a breaking interleaving* (reasoning: good) but *mis-classifies it as an order violation*
(rubric: classification wrong) is a **partial pass**, flagged exactly there, because sending the fix
the wrong way (a lock for an order bug) is the central A4 failure (Lu et al. Finding 2/9; §5c).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses **one
step** past their last comfortable success along a single parameter axis (`drill-generation.md` §5).
Escalating two steps collapses to failure; escalating none loses the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one non-trivial concurrency mechanism handled in isolation — enumerate/force a
  single race, classify it, propose the right-unit fix, and explain why.
- **Frontier-N** = N increments beyond Advanced; **each increment adds exactly one** new interacting
  mechanism OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for A4, with step counts:

1. **Compose mechanisms** (the canonical path): from a single atomicity violation →
   Frontier-1: a bug needing **both** an atomicity fix **and** an order edge (a lock alone is
   insufficient; you must add a happens-before too) → Frontier-2: **+ a deadlock risk** introduced by
   the naive locking fix, so the correct fix must also **order the locks** → Frontier-3: **+** a
   second shared variable so the invariant spans two cells and the interleaving set is larger. Each
   added interacting mechanism is exactly one increment.

2. **Grow the interleaving set** (scale axis): from two threads / one variable / the 6-element set →
   to two variables (a larger set, where the breaking subset is non-obvious) → to a three-step
   critical section (more interleavings to reason about). Each is one increment. (Stay at **two
   threads** — runner limit and Lu's 96%.)

3. **Push the memory model** (visibility axis): from "is this atomic on CPython?" → to "does this
   rely on **sequential consistency**?" → to "this works on CPython (GIL) but would break under a
   **weak memory model** / a no-GIL build — what happens-before edge makes it portable?" Reasoning
   about reorderings you *cannot* reproduce on CPython is one increment beyond reasoning about
   interleavings you can force.

4. **Push toward debugging → hand off to C3.** When the drill stops being "reason about *this*
   interleaving set" and becomes "this is intermittent in CI / production — classify it, decide what
   to instrument, and hypothesize under non-reproducibility (the **heisenbug**)," that is the
   **debugging** skill of sibling module **C3 (production & concurrency debugging)**. Escalate
   *toward* C3 rather than stretching A4; A4 is the *model* C3's debugging runs on.

Track the level as `A4: Frontier-N`. Reset condition: two consecutive failures at the same level →
drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the A4 dimensions. Two cross-cutting requirements apply at every tier above Foundations:
**product *and* process** (reasoned about the set / found the breaking interleaving *and* classified
it correctly and targeted the fix at the right unit — a lucky "add a lock" with no classification is
a Foundations-level pass at best), and **unaided + durable** (a same-session streak is provisional
until a delayed re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

**The scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Reason about the set.** Did they find an interleaving (or enumerate the breaking subset)
  that violates the invariant, rather than trusting one run? Did they correctly use **happens-before**
  to say what is ordered vs concurrent? *(Executable sub-claim: the breaking schedule is confirmed by
  the forced run / enumerated set; §5d.)*
- **D2 — Classify.** Atomicity vs order vs deadlock vs not-a-race (Lu et al.); data race vs race
  condition; and the GIL/memory-model status ("is this atomic / sequentially consistent / a CPython
  detail?").
- **D3 — Fix the right unit.** Whole read-modify-write made atomic / an explicit happens-before edge
  for order / consistent lock ordering for deadlock — **not** a reflexive "add a lock." Fix confirmed
  by re-running the forced repro or re-enumerating the set (necessary, not sufficient — stated as
  such).

| Tier | Observable bar for A4 |
|---|---|
| **Foundations** | On a single named race (e.g. the lost-update counter) or a single happens-before / GIL question, **predicts the value under a stated interleaving** (or *whether any interleaving breaks the invariant*; or *whether the op is atomic*; or *whether a `join` orders the read*) **and** explains it as a state event — "both threads read `0` before either writes, so one `+1` is lost." D1 solid; D2 at least partial (names the read-modify-write window / the edge). Allowed *with* the worked example faded to one missing step. |
| **Working** | On an unseen race, **unaided**: **classifies it** — atomicity vs order, *and* data race vs race condition where relevant — and says *why* (D2), proposes a fix that targets the right unit and not just "a lock" (D3), **and** correctly judges a "the GIL makes this safe" claim. Mis-classifying atomicity as order ⇒ partial pass, flagged. On 3 of 4 such unseen drills. |
| **Advanced** | On a drill **combining mechanisms or invoking the memory model** — a bug needing both atomicity *and* an order edge; a deadlock from lock-ordering; or a flag-publication pattern that relies on sequential consistency — **unaided**: reasons about the set / forces the schedule (D1), classifies it and gets the GIL/SC status right (D2), proposes a fix at the right unit and confirms it prunes the breaking schedule **without introducing a deadlock** (D3). Articulates the **underlying principle** on a teach-it-back ("a lock gives atomicity, not order"; "one run is a sample of a schedule set"; "the GIL serializes bytecodes, it is not thread-safety") — not just the instance. |
| **Frontier** | `Frontier-N`: presses one mechanism/dimension past the last comfortable success per §6 / `drill-generation.md` §5 (compose mechanisms → grow the interleaving set → push the memory model → hand off to C3). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier from
what the learner *does* on unseen drills, never from "I've written threaded code for years."
Held-out re-assessment and **real-code transfer** outrank a same-session streak (`assessment.md`
Part 5) — and for a hybrid module whose grading is explicitly soft, the real-code signal is weighted
heavily.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Trusting the run you got.** "It printed the right total, so it's correct." A green run is **one
  sample** of a schedule set the scheduler — not you — chose, and on CPython the GIL makes the bad
  schedule *rare*, so wrong code routinely looks right. The fix: reason about the **set** — "is there
  *any* interleaving that breaks the invariant?" — and enumerate or force it to confirm.
- **Treating a read-modify-write as one step.** Not seeing that `x += 1` / `D[x]=D[x]+1` /
  check-then-act is *read → modify → write*, with a window another thread can enter. The fix is the
  A1 move at concurrency scale: decompose it (the disassembly makes the gap concrete), and make the
  *whole* unit atomic.
- **"The GIL makes Python thread-safe."** Over-reading a CPython implementation detail. It serializes
  *bytecodes* (single ops are atomic) but a multi-bytecode read-modify-write is **not** atomic, and
  no-GIL builds exist (PEP 703). The fix: learn what the FAQ actually lists as atomic, and synchronize
  the read-modify-writes that aren't.
- **"Add a lock" as a blanket spell.** Assuming any lock makes it safe — missing that the lock must
  cover the *whole* read-modify-write (atomicity) and that a lock gives mutual exclusion, **not
  order**. Lu et al.: 73% of real fixes were *not* just adding/changing locks. The fix: classify first
  (atomicity vs order vs deadlock), then apply the matching remedy (atomic region / happens-before
  edge / consistent lock ordering).
- **Conflating data race with race condition.** Calling check-then-act "fine, no data race" and
  stopping. The fix: separate the low-level event (unsynchronized same-location write = data race)
  from the correctness fault (depends on schedule = race condition); the GIL removes the former, not
  the latter.
- **Assuming sequential consistency.** Trusting a publish-then-consume/flag pattern because "it
  worked," with no model that real memory is weaker and that CPython's GIL merely *masks* the hazard.
  The fix: name the happens-before edge that would make it portable.

**Evidence caveat (this is a `[Verified-adjacent]` model + `[Practitioner-canon]` formalism/facts
module — say so).** The grounding is mixed and must not be oversold:

- The **model** half (the concurrent notional machine; reason about the set of interleavings) is
  `[Verified-adjacent]`: it *extends* A1's `[Verified]` execution-model finding (Finding 1) into the
  concurrent setting on solid CS footing — **not** because "drilling interleaving-reasoning *causally*
  improves engineers" has been demonstrated. State it as "the natural, well-founded extension of the
  verified notional machine," not "research proves teaching this makes you better."
- The **formalism** half (happens-before, sequential consistency — Lamport 1978/1979) is
  **foundational CS theory**: exact, rigorously-established **definitions and models** by the field's
  founding figure — but *theory and definitions*, not an empirical *learning* finding. It is
  `[Practitioner-canon]` (foundational) in the same sense Big-O math or Parnas's information-hiding
  criterion are: the result is exact; its *use as a reasoning method* is craft. The coach must not
  present "happens-before reasoning improves your code" as a measured causal result.
- The **GIL facts** half is **documentation** (Python FAQ): true *of CPython*, an **implementation
  detail**, not a language guarantee — the coach says "this is what CPython does, not what Python
  promises," and never "Python is thread-safe."
- The **taxonomy** (Lu et al. 2008, reused from C3) is a **strong empirical characterization** — but
  **descriptive field data from C/C++ circa 2008**, *not* Python and *not* a causal learning result.
  It is the **best characterization we have** of what real concurrency bugs look like, used here as
  classification vocabulary — not proof that teaching it makes you better.
- The **curriculum-wide transfer caveat** applies in full: that drilling interleaving-reasoning,
  classification, and happens-before puzzles *causally* improves real concurrent-code work is the
  open question. The coach leans on the transfer task (§9) — a **real** race in the learner's system
  — as the honest individual-level evidence, and grades it as the soft judgment it is.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2).

> **Your turn:** Find a **real concurrent (or concurrency-adjacent) piece of your own code** — pick
> whichever you have: a shared counter/cache/flag/dictionary mutated from more than one thread,
> task, or process; a "works on my machine but flaky in CI" test; a piece of code where you added a
> lock and weren't sure it was the right fix; or even an `async`/callback path where two operations
> race on shared state. Pick the smallest concrete instance you can.
>
> Now **run the A4 moves on the *model*, not the run.** **(1) Reason about the set** — identify the
> shared state and the read-modify-writes touching it; name **two threads/streams and a specific
> interleaving** that would break the intended invariant (which read goes stale? which write
> clobbers which? — or which event is *meant* to precede another but isn't ordered?). Where you can,
> **reduce it to a minimal snippet and *force* the schedule** with an `Event`/`Barrier`, or
> **enumerate** the small interleaving set, so the bug is deterministic — then run it. **(2)
> Classify it** — atomicity violation, order violation, or deadlock (Lu et al.)? Is it a **data
> race**, a **race condition**, or both? Are you secretly relying on the **GIL** or on **sequential
> consistency**? **(3) Fix the right unit** — make the whole read-modify-write atomic, add the
> missing **happens-before edge**, or fix the lock ordering — *not* a reflexive lock — and re-run the
> forced repro (or re-enumerate the set) to confirm it prunes *that* schedule.
>
> Then step back: **was the failure something a single local run would ever have shown you — or did
> it only live in a schedule you didn't sample (and that the GIL usually hides)?** If you "fixed" it
> by adding a print and it went away, ask whether you fixed it or just moved the schedule (the
> heisenbug — and the doorway to **C3**).

**Grading is softer and named as such — and softer than A1** (`assessment.md` Part 4; §5d). Real
code has no clean answer key, *and* concurrency correctness is a property of all schedules the runner
cannot exhaust; the coach grades against the §7 rubric (D1 reason about the set · D2 classify · D3
fix the right unit) and says: *"this is a judgment call on your real code, graded against the
module's rubric — and softer than an executable pass, because I can force one breaking schedule (or
enumerate a tiny set) but not prove your fix holds under all interleavings."* Where any sub-claim
**is** runnable — the learner can reduce the race to a minimal snippet — the coach still uses the
runner: **force the interleaving (or enumerate the set), show the bug, apply the fix, re-run** (the
same discipline as the §5d check, now on the learner's real find). **Transfer evidence is weighted
heavily:** a learner who aces forced-interleaving puzzles but, on their own flaky code, reaches
straight for a lock without classifying the race — or trusts a green run as proof — has **not**
transferred the skill, and the tracker notes that gap as more diagnostic than another passed
synthetic drill.

---

## Cross-references

- Drill mechanics, the **hybrid grading path** (runner for the forced-interleaving / enumerated-set /
  disassembly sub-claim; rubric + exemplars for the reasoning), exercise formats (Prediction →
  Observation → Reflection, Trace-the-path, Debug-this, Error analysis, Teach-it-back), Frontier
  escalation: `references/drill-generation.md` (this module instantiates §1 and follows §2, §3, §4,
  §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, **surface ground truth —
  paste the forced run / the enumerated set / the disassembly**, direct feedback, scaffolding
  ladder): `references/coaching-loop.md`.
- A4 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-code
  transfer** weighting: `references/assessment.md` (the A4 entry task: a small 2-thread race — find a
  breaking interleaving, classify it atomicity-vs-order, and target the fix; "Python is thread-safe?"
  baked in as a trap).
- Evidence grounding (the concurrent notional machine extending Finding 1; Lamport 1978
  happens-before; Lamport 1979 sequential consistency; the CPython GIL atomicity facts; the **reused**
  Lu et al. 2008 atomicity/order taxonomy; the worked-examples / expertise-reversal instructional
  finding): `references/evidence-base.md` → *Concurrency mental models (module A4)* and *Production &
  concurrency debugging (module C3)* and Finding 1.
- Soft prerequisites & siblings: **A1** (notional machine — the single-machine model A4 generalizes),
  **A3** (tracing — now of two streams at once); sibling **C3** (production & concurrency debugging —
  *debugging* races, which leans on A4's model and which A4 hands off to for heisenbugs and
  non-reproducibility).
- Golden exemplars (~3 per tier, each with a **runner-confirmed** forced interleaving / enumerated set
  / disassembly + classification + right-unit fix): `exemplars/A4/foundations.md`,
  `exemplars/A4/working.md`, `exemplars/A4/advanced.md`.
