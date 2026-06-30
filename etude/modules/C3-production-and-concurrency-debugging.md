# C3 — Production & Concurrency Debugging `[Verified-adjacent]`

> **Module type.** Mixed-status by design: **`[Verified-adjacent]` model + `[Practitioner-canon]`
> method**. The *concurrency notional machine* extends A1's single-threaded execution model to
> **multiple interleaved instruction streams**, and rests on an empirical taxonomy of real-world
> concurrency bugs (Lu et al. 2008, ASPLOS — `[Verified-adjacent]`: a strong empirical
> characterization, but it is *descriptive* field data, not a causal learning result). The
> *production-debugging method* — reasoning about a live system from the evidence it leaves
> (logs, metrics, traces) under non-reproducibility — is **`[Practitioner-canon]`** (Zeller's
> systematic debugging; the observability canon). The validator badge on this file is
> `[Verified-adjacent]`; the honest prose badge is the mixed one above. The coach must keep the
> two halves apart and never sell the method as verified science.
>
> **Core idea.** At systems and concurrency scale, two things from A1/C1 break down. (1) You can
> no longer **be the single machine**: many instruction streams interleave, the *schedule* is
> chosen by the runtime not by you, so the same code produces different outcomes on different
> runs — and **observing it changes it** (a heisenbug). (2) You can no longer **attach a debugger
> and step**: the fault is in production, intermittent, and gone by the time you look — so you
> reason from the **evidence the runtime already left behind**. The skill is to debug *under
> uncertainty and non-reproducibility*: classify the race, decide what to instrument, and form
> falsifiable hypotheses about a system you cannot pause.

---

## 1. Evidence basis `[Verified-adjacent]` model + `[Practitioner-canon]` method

This module is **mixed-status** and the coach must never present its canon half as verified
science (`evidence-base.md` → badge rules). Three pillars; the first is empirical, the other two
are craft.

**(a) The concurrency taxonomy — Lu, Park, Seo & Zhou 2008 `[Verified-adjacent]`.** Cite via
`evidence-base.md` → *Production & concurrency debugging (module C3)* (proposed addition). The
paper is *Learning from Mistakes: A Comprehensive Study on Real-World Concurrency Bug
Characteristics* (ASPLOS '08; doi:10.1145/1346281.1346323; ASPLOS Influential Paper Award 2022).
The authors examined **105 randomly selected real-world concurrency bugs** from four large mature
open-source applications — **MySQL, Apache, Mozilla, OpenOffice** — split into **74 non-deadlock
and 31 deadlock** bugs. The findings that ground this module's whole stance (numbers and wording
verified against the primary PDF during authoring):

- **Most non-deadlock concurrency bugs are one of two simple patterns.** *Finding (1), verbatim:*
  "**Most (72 out of 74) of the examined non-deadlock concurrency bugs are covered by two simple
  patterns: atomicity-violation and order-violation.**" The paper's own definitions:
  an **atomicity violation** is when "the desired serializability among multiple memory accesses
  is violated (i.e., a code region is intended to be atomic, but the atomicity is not enforced
  during execution)"; an **order violation** is when "the desired order between two (groups of)
  memory accesses is flipped (i.e., A should always be executed before B, but the order is not
  enforced during execution)." Table 4 of the paper: **51 atomicity, 24 order, 2 other** (with 3
  bugs counted as both). *This is the taxonomy the module's classification drills teach.*
- **Order violations are common and under-served.** *Finding (2), verbatim:* "**A significant
  number (24 out of 74) of the examined non-deadlock concurrency bugs are order bugs**" — and the
  paper stresses these "may not be easily expressed via synchronization primitives like locks."
  (A lock makes a region *atomic*; it does **not** by itself impose an *order*.)
- **The bug is small even though the system is large.** *Finding (3), verbatim:* "**The
  manifestation of most (101 out of 105) examined concurrency bugs involves no more than two
  threads**" (96%); and *Finding (5):* "**Many (66%) of the examined non-deadlock concurrency
  bugs['] manifestation involves concurrent accesses to only one variable**" (34% involve
  multiple variables). So the productive place to look is a *small* interleaving of *two* threads
  over *one or two* shared variables — not the whole thread pool.
- **Locks are not the universal fix.** *Finding (9), verbatim:* "**Three quarters (73%) of the
  examined non-deadlock bugs are fixed by techniques other than adding/changing locks**" — and
  many fixes "were not correct at the first try, indicating the difficulty of reasoning concurrent
  execution by programmers." This is the empirical backstop for the module's "don't reflexively
  slap a lock on it" anti-pattern.

**(b) Systematic debugging under non-reproducibility — Zeller, *Why Programs Fail* (2nd ed., 2009)
`[Practitioner-canon]`.** Already on the curriculum reading spine (`evidence-base.md` → reading
spine; "anchors C1 and C3"). Zeller's frame is debugging as **the scientific method run against a
program**: from an observed failure, form a **hypothesis** about the cause, **predict** a
consequence you can check, **observe**, and **refine** — narrowing systematically rather than
guessing. C3 inherits C1's hypothesis-driven loop and stresses the parts that bite hardest in
production: **reproduction** (a failure you cannot reproduce on demand is the hardest case;
Zeller treats controlling and isolating the conditions of failure as central), and the discipline
of **reasoning from recorded evidence** when you cannot re-run at will. *Craft, vetted against the
named source — not an effectiveness experiment.* (And per `evidence-base.md` → Refuted: that
*systematic tracing causally* beats skilled as-needed reading was **not** established; the method
is taught as disciplined practice, not proven superiority — exactly as for C1.)

**(c) Observability-driven debugging — the observability canon `[Practitioner-canon]`.** Cite via
`evidence-base.md` → *Production & concurrency debugging (module C3)* (proposed addition). The
anchor is Majors, Fong-Jones & Miranda, *Observability Engineering* (O'Reilly, 2022). Its core
stance, made operational here: in production you **cannot attach a debugger and step** — the
system is remote, concurrent, serving traffic, and the failure is often gone by the time you look.
So you debug from the **evidence the running system emits** — structured **logs**, **metrics**
(rates, latencies, error counts), and **distributed traces** — and the engineering goal is to
emit *enough* of the right evidence that you can ask new questions of past behavior **without
shipping new code to reproduce it**. Respected, widely taught practice — **not** a measured
result; the coach says "respected practice, not a verified research finding."

**Why these license this module.** Lu et al. is the empirical anchor for the *what* of
concurrency bugs (the atomicity/order taxonomy; bugs are small — two threads, one variable;
locks aren't the universal fix). Zeller + the observability canon are the canon anchors for the
*how* of debugging a system you cannot pause (hypothesis-driven reasoning under
non-reproducibility; reason from emitted evidence). The combined claim the module teaches:
**at scale you classify the race, instrument to surface the evidence, and hypothesize under
uncertainty — because you can neither be the machine nor step it.**

**Read through the transfer caveat.** Lu et al. is a **descriptive characterization of 105 bugs
in four C/C++ applications circa 2008** — it tells you what real concurrency bugs *looked like*,
not that teaching this taxonomy *causally* makes a given engineer better (and the language mix is
not Python). The canon sources are **craft wisdom, not measured causation**. The *direction* is
well grounded; that drilling forced-interleaving puzzles *causally* improves real-incident
debugging is the open question every module here carries (`evidence-base.md` → transfer caveat).
The transfer task (§9) — a real concurrency or production bug from the learner's own system — is
the honest individual-level test. **A4 note:** the *concurrent notional machine itself*
(interleavings, happens-before, memory models) is the subject of sibling module **A4 (concurrency
mental models)**, which is **not yet built**; C3 leans on the slice of that model it needs and
references A4 softly.

---

## 2. Soft prerequisites

**A1 (notional machine) is the load-bearing prerequisite.** C3 is A1's execution model with the
single-machine assumption removed: instead of one program counter walking statements top to
bottom, there are **N counters interleaving**, and the *transition rule* now has to account for
which stream runs next. Every concurrency bug here is an A1 event — a read, a rebind, a mutation —
that goes wrong because *another stream's* event landed in between. A learner shaky on
rebinding-vs-mutation or "when code runs" (A1 §3) will not see why a non-atomic `+=` loses
updates, because they do not yet see `+=` as a *read-modify-write* of three separable steps.

**C1 (systematic debugging) is the method this extends.** C3 is C1's observe → hypothesize →
predict → test → narrow loop, run against a system you **cannot reproduce on demand and cannot
attach to**. A learner who debugs by print-spraying a reproducible local script (the C1
anti-pattern) will be helpless when the failure is intermittent and in production — the C3 skill
is doing C1's loop from *recorded* evidence under *uncertainty*.

**C2 (reading stack traces) and A3 (tracing) help.** A production exception still arrives as a
traceback (C2); reasoning about an interleaving is tracing two streams at once (A3). **A4
(concurrency mental models)** is the natural sibling — when it exists it will own the happens-before
/ memory-model machinery this module only uses in passing.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any learner
may open any module at any tier). If a learner flails at C3 because they cannot trace a single
thread, the coach notes the gap likely traces to A1/A3 and *suggests* shoring those up — but does
not forbid C3. A learner strong on single-threaded debugging (C1) but who has never reasoned about
*nondeterminism* or *production-only* failure is exactly who C3 is for.

---

## 3. The mental model

**Two assumptions from A1/C1 break at scale, and the whole module is about debugging once they
do.** (1) **You are no longer the only machine.** Multiple instruction streams interleave; the
*schedule* — which stream's next step runs when — is chosen by the OS/runtime, not by you. So the
same code over the same inputs can produce **different outcomes on different runs**
(nondeterminism), and **adding an observation** (a print, a log, a breakpoint, a sleep) perturbs
the timing and can **change or hide** the very bug you are chasing (a **heisenbug**). (2) **You can
no longer step the machine.** The failure is in production — remote, concurrent, intermittent, and
usually gone by the time you look. So you debug from the **evidence the runtime already emitted**:
logs, metrics, traces. The runtime is still the ground truth; you just read it *after the fact*
instead of stepping it live.

The concurrency state model — A1's state, plus what's new:

| State component | What's new at concurrency / production scale |
|---|---|
| **Shared state (the heap, shared)** | The same heap object is now reachable from **multiple threads at once**. A read-modify-write (`x += 1`, `cache[k] = compute()`, check-then-act) is **not one step** — it is *read → compute → write*, and another thread's writes can land **in between**. That gap is where atomicity violations live. |
| **Per-thread state (frames × N)** | Each thread has its **own** call stack and locals (A1's frames, replicated). A thread's local copy of a shared value (`tmp = balance`) can go **stale** the instant another thread writes the shared original — and the stale write **clobbers** the other's update (a **lost update**). |
| **The schedule (was: the program counter)** | A1 had *one* counter advancing deterministically. Now there are **N counters**, and an **interleaving** is one particular merge of their steps. The runtime picks it; you do not. **Nondeterminism** = the outcome depends on the interleaving. **Happens-before** = the (few) orderings you *can* rely on (a `join`, a lock release→acquire, a thread's own program order); everything else may be reordered. |
| **The evidence channel (new)** | At scale you don't read the live state — you read what the program **chose to emit**: a log line, a counter, a latency histogram, a trace span. **You can only debug what you instrumented.** Absent evidence is not "no problem"; it is *no data*. |

**The transition rule, generalized.** A1: each statement maps the current state to the next,
deterministically. Concurrency: at each step the **scheduler picks one ready thread** and advances
*its* next step; the result is deterministic *given the interleaving*, but the interleaving is not
under your control. To predict what *can* happen, you do not trace one path — you ask **"is there
an interleaving that breaks the intended invariant?"** A correct concurrent program gives the same
answer under **every** schedule; a buggy one has at least one schedule that doesn't.

**The discipline in one line: *find the interleaving (or the missing evidence) — don't trust the
run you happened to get.*** The run you observed is **one sample** of a nondeterministic space. A
green local run does not mean "correct"; it means "this schedule was fine." The bug lives in a
schedule you didn't sample — and the instant you add a print to look for it, you've changed the
schedule. So you reason about the *space* of interleavings and instrument to *capture* evidence,
rather than trusting any single execution.

Three corollaries the module drills:

1. **A non-atomic read-modify-write is three steps, and another thread can interleave between
   them.** `x += 1` is `tmp = x; tmp = tmp + 1; x = tmp`. Two threads each reading the old `x`
   before either writes → one update is **lost**. (Lu et al.: atomicity violations are the single
   largest class — 51 of 74 non-deadlock bugs.) The fix makes the *whole* read-modify-write
   atomic (a lock), not just adds a lock somewhere.
2. **A lock gives atomicity, not order.** If thread B must run *after* thread A (B reads what A
   initializes), wrapping both in the *same* lock does **not** guarantee A goes first — it only
   stops them overlapping. Order requires an explicit **happens-before** edge (a `join`, an
   `Event`/condition, a queue). (Lu et al. Finding 2: order violations are a distinct, common,
   under-served class.) Conflating the two is why "I added a lock and it still breaks."
3. **Observation changes the system; absent evidence is not absence of the bug.** Adding a probe
   perturbs timing (heisenbug); a clean log is not proof of correctness, only proof that *this
   schedule* logged clean. You debug the *space*, from *emitted evidence*, under the assumption
   that the next schedule may differ.

---

## 4. Worked example — a lost update, forced into the open

*(Foundations depth: every step shown, with runner-confirmed ground truth. This fades by tier —
see the table after.)*

The skill is to stop trusting "the run I got" and instead **find the interleaving that breaks the
invariant**, then confirm it deterministically. Consider two threads each making a `+1` "deposit"
to a shared balance that starts at `0`. The intended invariant: *two deposits ⇒ final balance is
`2`.*

```python
shared = {"balance": 0}

def deposit():
    tmp = shared["balance"]        # READ
    shared["balance"] = tmp + 1    # WRITE  (read-modify-write, NOT atomic)

# (two threads each run deposit() once)
```

**Step 1 — Be the machine, but for *two* streams.** A1 says trace the statements; here we trace
*an interleaving* of two threads, T1 and T2, each doing `READ` then `WRITE`. The benign schedule
is `T1.READ, T1.WRITE, T2.READ, T2.WRITE` → `0→1→1→2`, final `2`. But the scheduler is free to
interleave. Consider the schedule `T1.READ, T2.READ, T2.WRITE, T1.WRITE`:

| Step | Thread / action | `tmp` (T1) | `tmp` (T2) | `shared["balance"]` |
|---|---|---|---|---|
| 0 | *(start)* | — | — | `0` |
| 1 | T1 READ | `0` | — | `0` |
| 2 | T2 READ | `0` | `0` | `0` |
| 3 | T2 WRITE `tmp+1` | `0` | `0` | `1` |
| 4 | T1 WRITE `tmp+1` | `0` | `0` | **`1`** ← T1's stale `tmp=0` clobbers T2's `1` |

Both threads read `0`; T1's write overwrites T2's. **One deposit is lost** — final `1`, not `2`.

**Step 2 — Why a naive run usually won't show it (the heisenbug warning).** If you just launch two
threads doing `counter += 1` in a tight loop, on CPython you will very often get the *correct*
total — because the GIL serializes the short bytecode window and the scheduler rarely preempts
mid-`+=`. **Verified — the race does NOT reliably manifest naively** (two threads, 200 000
increments each, run five times):

```
# /tmp/C3_naive_tight.py: two threads each do `counter += 1` 200000 times
expected 400000 actual 400000 no-loss
expected 400000 actual 400000 no-loss
expected 400000 actual 400000 no-loss
expected 400000 actual 400000 no-loss
expected 400000 actual 400000 no-loss
status: ok   (Python 3.13.2)
```

This is the trap: a green run is **one sample**, not a proof. The bug is real and latent; the
schedule just didn't hit it. To study it in the gym we **force** the bad interleaving with an
`Event` (a happens-before edge that pins the schedule), so the lost update is deterministic.

**Step 3 — Force the interleaving and confirm.** The forced version pauses T1 *after* its read and
*before* its write until T2 has committed — exactly the schedule from the table:

```python
import threading
shared = {"balance": 0}
t1_read = threading.Event()
t2_wrote = threading.Event()

def t1():                          # deposit +1
    tmp = shared["balance"]        # READ 0
    t1_read.set()
    t2_wrote.wait()                # force T2 to interleave between read and write
    shared["balance"] = tmp + 1    # WRITE 1 (stale)

def t2():                          # deposit +1
    t1_read.wait()
    shared["balance"] = shared["balance"] + 1   # 0 -> 1
    t2_wrote.set()

a = threading.Thread(target=t1); b = threading.Thread(target=t2)
a.start(); b.start(); a.join(); b.join()
print("two +1 deposits on 0; correct final = 2")
print("actual final =", shared["balance"])
```

**Runner-verified ground truth** (executable-ground-truth discipline — the coach *runs* it, never
guesses; confirmed deterministic across **10/10** runs):

```
stdout: "two +1 deposits on 0; correct final = 2\nactual final = 1\n"
status: ok
```

**Step 4 — Classify it (Lu et al. taxonomy).** This is an **atomicity violation**: the read and
the write were *intended* to be one atomic unit, but the atomicity was not enforced, so T2's
accesses interleaved between them. (It is *not* an order violation — neither deposit is "supposed
to" go first; the bug is the *overlap*, not the *order*.)

**Step 5 — Fix the right thing, and confirm the fix.** The fix makes the **whole read-modify-write
atomic** with a lock — not just "add a lock somewhere." With both critical sections under one
lock, T2 cannot enter between T1's read and write:

```python
import threading
shared = {"balance": 0}
lock = threading.Lock()
t1_read = threading.Event(); t2_wrote = threading.Event()

def t1():
    with lock:                              # the WHOLE read-modify-write is atomic
        tmp = shared["balance"]
        t1_read.set()
        shared["balance"] = tmp + 1
def t2():
    t1_read.wait()
    with lock:
        shared["balance"] = shared["balance"] + 1
    t2_wrote.set()

a = threading.Thread(target=t1); b = threading.Thread(target=t2)
a.start(); b.start(); a.join(); b.join()
print("actual final =", shared["balance"])
```

**Runner-verified — the fix resolves it** (correct `2` across runs; the same discipline as a
review drill — confirm the bug, then confirm the fix):

```
stdout: "actual final = 2\n"
status: ok
```

**What this makes visible** (and "it just adds two deposits" hides): the bug is **not on any single
line** — every line is correct in isolation. It is in the *interleaving* of two correct lines, and
it is **invisible in the run you happened to get**. Trusting the green naive run is the exact
failure this module breaks; finding the interleaving (and forcing it to confirm) is the skill.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), the full
> interleaving-table-plus-fix helps **novices** (it shows the move) but is **redundant load for
> the more advanced**, who learn more by finding the interleaving themselves. So the coach fades
> it:
>
> | Tier | Worked-example depth at C3 |
> |---|---|
> | **Foundations** | **Full** — the complete interleaving table, the heisenbug warning, the forced repro, the classification, and the confirmed fix, every step shown. |
> | **Working** | **Partial** — coach shows the racy snippet and names that *an* interleaving loses an update, but leaves the **interleaving table** (which schedule? which value goes stale?) and the **classification** for the learner. |
> | **Advanced** | **Skeleton** — coach hands over the snippet (or a log/metric trail) only; the learner finds the breaking interleaving (or localizes from evidence), classifies it per Lu et al., and proposes a fix that targets the right unit, unaided. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for C3. Grading mode is
declared up front: **hybrid, leaning rubric + exemplars** (§5d). Concurrency nondeterminism is
hard to grade by a single executable output, so the **reasoning** (which interleaving breaks it,
what to instrument, how to classify, the hypothesis set) is rubric-graded against gold exemplars;
the **runner is used for every deterministic sub-claim** (force the interleaving and show the lost
update; run the planted bug and its fix; classify a snippet whose misbehavior is runner-confirmed).

### 5a. Tier definitions (C3-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. Every drill
is either a **concurrency reasoning** drill (find/classify the race; the misbehavior is forced and
runner-confirmed) or a **production-reasoning** drill (localize a fault from an emitted
log/metric/trace trail and hypothesize under non-reproducibility):

| Tier | C3 criterion | Example shape |
|---|---|---|
| **Foundations** | One race on a familiar surface, **named for them**: given a 2-thread non-atomic counter (or a use-before-init), *predict whether there is an interleaving that breaks the invariant, and describe it*. Or: read a clean log trail and name where the fault is. The runner forces the interleaving to confirm. | The lost-update counter (worked example); the use-before-init order violation; the 504-cluster log trail. |
| **Working** | Apply in a context not seen before, where the **schedule** matters and intent/execution diverge: classify a race as **atomicity vs order** violation (Lu et al.) and say *why*; or identify the **heisenbug** risk (will adding this print hide the bug?); or read a metric trail where the obvious culprit is a decoy. Predict + name the mechanism. | Check-then-act (TOCTOU); a lock that fixes atomicity but not order; "we added logging and it went away." |
| **Advanced** | Combine two or more mechanisms or reason about **non-reproducibility**: a bug that needs *both* an atomicity fix *and* an order edge; a deadlock from lock-ordering; "this passes in CI and fails in prod — what's different about the schedule/load, and what one piece of evidence would discriminate your top two hypotheses?" Find it, classify it, propose the fix that targets the right unit, **explain why a lock alone is/ isn't enough**. | Deadlock via opposite lock order; double-fix (atomicity + ordering); incident triage from a partial trace. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations drill secretly needs the learner to *discover* the race
class unaided (that's Working), or an Advanced drill is a single isolated atomicity violation with
no second mechanism, no non-reproducibility, and no instrumentation decision. Apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for C3:

- **Bug class** — atomicity violation (lost update / non-atomic read-modify-write) · atomicity
  violation (check-then-act / TOCTOU) · order violation (use-before-init / read-before-write) ·
  order violation (write-write, last-writer-wins) · deadlock (lock-ordering / circular wait) ·
  *not-a-concurrency-bug* (a plain logic bug surfacing only under load — the decoy class) ·
  observability gap (the evidence needed to localize was never emitted).
- **Scale of the interleaving** — two threads, one variable (the Lu-et-al. common case) · two
  threads, two variables · two locks (deadlock). *Keep thread count low* — both because real bugs
  are small (Lu Finding 3: 96% ≤ two threads) and because the runner's address-space cap blocks
  spawning many OS threads.
- **Evidence surface (production half)** — a structured **log** trail · a **metric** series
  (latency / error-rate / count) · a multi-span **trace** sketch · a stack trace from an
  intermittent crash · *missing* evidence (the answer is "instrument X first").
- **Reproducibility** — deterministic-once-forced (gym) · intermittent (the run you got was a
  lucky/unlucky sample) · prod-only (passes in CI, fails under prod load/concurrency).
- **What the learner must produce** — *describe the breaking interleaving* (Foundations) ·
  *classify atomicity-vs-order + why* (Working) · *predict the heisenbug* (will the probe hide
  it?) · *localize from evidence + name the one discriminating signal* · *propose the fix that
  targets the right unit* (atomicity? order edge? lock-ordering discipline?) · *a teach-it-back of
  the principle*.
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (a racy/planted-bug snippet or
  an evidence trail) and **Trace-the-path** (step a chosen interleaving). Also **Error analysis**
  ("here's a *fix* someone applied — does it actually close the race, or only narrow the window?"),
  **Teach-it-back** (articulate atomicity-vs-order, or why observation perturbs), and
  **Generation → Comparison** (learner proposes the instrumentation/repro plan; coach reveals the
  gold).

Keep an in-session log of the `(bug class, scale, evidence surface, reproducibility, format)`
tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* C3 errors, each with the conceptual gap it diagnoses (`drill-generation.md` §1c
format). Grounded in the concurrency-bug taxonomy (Lu et al. 2008), systematic-debugging canon
(Zeller), and the observability canon — not trivia. **The root of most of them is one
over-extension of A1's single-machine model: "the run I observed is *the* behavior."** The
concurrent reality is "the run I observed is **one sample** of a nondeterministic space chosen by
the scheduler; observing it can change it; and at scale I see only what I emitted." Most errors
below are a refusal to give up the single-deterministic-run assumption.

```
Error: Concludes a concurrent program is correct because it ran correctly (locally, in CI, a
       few times) -- treats one green run as proof.
Diagnoses: "The run I got is THE behavior" -- no model of the schedule as a free variable. The
           learner samples one interleaving and generalizes; the bug lives in an unsampled
           schedule. (Lu et al.: real bugs are intermittent; module §3 corollary 3.)
Example trigger: the naive `counter += 1` two-thread snippet that prints the correct total on
                 this CPython but is still racy -- ask "is this correct, or just lucky?"

Error: Treats a read-modify-write (`x += 1`, `cache[k] = compute()`, append-after-check) as a
       single indivisible step, so cannot see how an update is lost.
Diagnoses: A1 gap surfacing under concurrency -- does not decompose `+=` into read/compute/write,
           so the interleaving window between read and write is invisible. The atomicity-violation
           blind spot. (Lu et al.: 51/74 non-deadlock bugs are atomicity violations.)
Example trigger: the lost-update worked example; predict the final balance under T1.READ,
                 T2.READ, T2.WRITE, T1.WRITE.

Error: Adds a lock and assumes the bug is fixed, without checking WHAT must be atomic or whether
       the problem was order, not atomicity.
Diagnoses: Models "lock = thread-safe" as a blanket spell. Misses that (a) the lock must cover
           the WHOLE read-modify-write to give atomicity, and (b) a lock gives mutual exclusion,
           NOT ordering -- an order violation survives a lock. (Lu Finding 9: 73% of fixes are
           NOT just adding/changing locks; §3 corollary 2.)
Example trigger: a use-before-init order violation "fixed" by wrapping both threads in one lock --
                 run it and show the order can still flip.

Error: Confuses an atomicity violation with an order violation (or cannot tell them apart).
Diagnoses: No working grip on the Lu et al. taxonomy: atomicity = a region meant to be
           indivisible was interleaved; order = A was meant to precede B and the order flipped.
           Conflating them sends the fix the wrong way (a lock vs a happens-before edge).
Example trigger: classify check-then-act (atomicity) vs loader/user use-before-init (order),
                 and say which fix each needs.

Error: Adds a print / log / breakpoint / sleep to "see" a concurrency bug and concludes it is
       gone when the symptom disappears.
Diagnoses: No heisenbug model -- does not see that observation perturbs timing and can hide (or
           move) the bug. The disappearance is evidence the probe changed the schedule, not that
           the bug is fixed. (Zeller; §3 corollary 3.)
Example trigger: the heisenbug snippet -- latent run loses an update (final 1); the same code with
                 an observation probe prints the "correct" 2. Ask what the probe proved.

Error: Tries to debug a production failure by attaching a debugger / re-running locally, and is
       stuck when it won't reproduce.
Diagnoses: Carrying the C1 "reproduce locally then step" assumption into a setting where you
           cannot pause or re-run the system. The shift to reasoning from EMITTED evidence
           (logs/metrics/traces) hasn't happened. (Observability canon.)
Example trigger: an intermittent prod 500 with only a log/metric trail -- "you can't repro it
                 locally; what do you reason from, and what's your first hypothesis?"

Error: Reads "no error in the logs" as "no problem here," or fixates on the loudest signal.
Diagnoses: Treats absent evidence as evidence of absence -- forgets you can only see what was
           instrumented; or anchors on the most salient metric (a decoy) instead of the one that
           discriminates hypotheses. (Observability canon; Zeller's narrowing.)
Example trigger: a metric trail where CPU is high (decoy) but the latency cluster lines up with a
                 downstream dependency -- which signal actually localizes the fault?

Error: Print-sprays / changes many things at once / "just adds a lock everywhere" instead of
       forming a falsifiable hypothesis and a discriminating test.
Diagnoses: Non-systematic debugging carried to scale -- no hypothesis, no prediction, no single
           discriminating observation. At scale this is worse: each probe perturbs timing and
           costs a deploy. (Zeller; C1 method; §3.)
Example trigger: "passes in CI, fails in prod" -- ask for two ranked hypotheses and the ONE piece
                 of evidence that would tell them apart, not a list of changes to try.

Error: Reaches for a lock-ordering fix that introduces a deadlock, or cannot see why two
       correct critical sections deadlock together.
Diagnoses: No model of circular wait / lock ordering -- acquires two locks in opposite orders on
           two threads, each holding one and waiting for the other. (Lu et al.: deadlock is 31/105
           bugs; the runner reports this as a TIMEOUT.)
Example trigger: two threads, lock_a then lock_b vs lock_b then lock_a -- predict whether it
                 completes; the runner times out.
```

### 5d. Grading mode

**Hybrid, leaning rubric + exemplars** (`drill-generation.md` §1d, §3). This is **softer than a
pure executable pass, and the coach says so to the learner** — concurrency correctness is a
property of *all* schedules, which a single run cannot certify, so the *reasoning* is the graded
object. The procedure, made concrete for C3:

1. **Run every deterministic sub-claim through the runner first.** Although the *reasoning* is
   rubric-graded, the **planted behavior is verified by running it** via
   `python <skill-dir>/runtime/python/runner.py snippet.py` (`drill-generation.md` §2): force the
   breaking interleaving (with an `Event`/`Barrier`) and show the **lost update / duplicate
   creation / use-before-init crash / deadlock timeout**; then apply the learner's (or the gold's)
   **fix** and re-run to confirm it closes the race. A learner who *disputes* whether a schedule
   exists gets the **forced-interleaving run** as evidence. The classification drills are anchored
   to runner output, never to the coach's guess. **Honesty note the coach states out loud:** a
   *naive* (unforced) racy snippet may print the *correct* answer on a given run — that is the
   heisenbug, not a refutation; the coach demonstrates the bug via the **forced** schedule and
   says explicitly that the green naive run is one sample, not a proof.
2. **Score the reasoning against the C3 rubric (§7), criterion by criterion** — *did they find an
   interleaving that breaks the invariant (or localize from the evidence)? did they classify it
   correctly (atomicity vs order vs deadlock vs not-a-race)? did they target the fix at the right
   unit (whole read-modify-write atomic / a happens-before edge / consistent lock ordering), and
   not "just add a lock"? did they reason about non-reproducibility and the heisenbug risk?* Each
   is a 3-point criterion (§7), graded explicitly.
3. **Cite the closest golden exemplar.** Compare to the tier's golds in `exemplars/C3/<tier>.md` —
   "close to the **weak** exemplar: you saw the lost update but called the fix done by adding a
   lock to one side" vs. "close to the **strong** exemplar: forced the interleaving, classified it
   as atomicity, made the whole RMW atomic, and confirmed the fix."
4. **Name it as soft — explicitly softer than A1/C1's executable grading.** The coach says: "**this
   is a judgment call graded against the module's rubric + exemplars, and it is softer than a
   pure executable pass: I can run the *forced* schedule to prove a bug exists, but I cannot run
   *all* schedules to prove your fix is complete — so I'm grading your reasoning about the schedule
   space, not just an output**" (`drill-generation.md` §3; `assessment.md` §1.2). Do **not**
   conflate "the forced repro now prints the right answer after your fix" with "proven correct
   under all interleavings"; rubric passes here are softer evidence than A1's executable passes.

C3 drills are thus hybrid, and the coach **reports the verdicts separately**: a learner who
*describes the interleaving* (reasoning: good) but *mis-classifies it as an order violation*
(rubric: classification wrong) is a **partial pass**, flagged exactly there, because sending the
fix the wrong way (a lock for an order bug) is the central C3 failure (Lu et al. Finding 2/9; §5c).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses **one
step** past their last comfortable success along a single parameter axis (`drill-generation.md`
§5). Escalating two steps collapses to failure; escalating none loses the desirable-difficulty
benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one non-trivial concurrency/production mechanism handled in isolation — find and
  classify a single race (or localize a single fault from evidence), propose the right-unit fix,
  and explain why.
- **Frontier-N** = N increments beyond Advanced; **each increment adds exactly one** new
  interacting mechanism OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for C3, with step counts:

1. **Compose bug classes** (the canonical path): from a single atomicity violation →
   Frontier-1: a bug needing **both** an atomicity fix **and** an order edge (lock alone is
   insufficient; you must add a happens-before too) → Frontier-2: **+ a deadlock risk** introduced
   by the naive locking fix, so the correct fix must also order the locks → Frontier-3: **+** the
   whole thing is **prod-only / intermittent**, so it must be reasoned from a partial evidence
   trail rather than a snippet. Each added interacting mechanism is exactly one increment.

2. **Push the evidence surface** (production axis): from a clean single-service log → to a
   **multi-span distributed trace** where the fault is in a *downstream* span → to a trail with a
   **decoy** loud signal (high CPU) that does not localize the fault → to **missing** evidence
   where the right answer is "instrument X and wait for it to recur." Each is one increment.

3. **Push reproducibility** (uncertainty axis): from deterministic-once-forced → to **intermittent**
   (the learner must reason that the green run was a sample) → to **"works in CI, fails in prod"**
   (reason about what differs in the schedule/load) → to a **heisenbug** where every probe they'd
   add perturbs the timing and they must design an *observation that doesn't move the bug*. Each is
   one increment.

4. **Push the fix's subtlety**: from "make the RMW atomic" → to a fix that must not **serialize**
   the hot path (correctness *and* not killing throughput) → to a lock-free / single-owner
   redesign (hand the shared state to one thread / a queue) where the right answer is "remove the
   sharing, not guard it." Each is one increment.

5. **Hand off the model to A4.** When the drill stops being "debug this race" and becomes "reason
   about the **memory model / happens-before** in the abstract" (reorderings the hardware/runtime
   permits, why a benign-looking read needs a barrier), that is the **concurrent notional machine**
   itself — sibling module **A4 (concurrency mental models)**, not yet built. Escalate *toward* A4
   rather than stretching C3; C3 is the *debugging* skill that A4's model will underwrite.

Track the level as `C3: Frontier-N`. Reset condition: two consecutive failures at the same level →
drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the C3 dimensions. Two cross-cutting requirements apply at every tier above Foundations:
**product *and* process** (found/localized the issue *and* classified it correctly and targeted
the fix at the right unit — a lucky "add a lock" with no classification is a Foundations-level pass
at best), and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

**The scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Find / localize.** Did they find an interleaving that breaks the invariant (concurrency),
  or localize the fault from the emitted evidence (production)? *(Executable sub-claim: the
  breaking schedule is confirmed by the forced run; §5d.)*
- **D2 — Classify & reason.** Atomicity vs order vs deadlock vs not-a-race (Lu et al.); for
  production, the *one discriminating signal* and a falsifiable hypothesis (Zeller). Did they
  reason about **non-reproducibility** and the **heisenbug** risk rather than trusting one run?
- **D3 — Fix the right unit.** Whole read-modify-write made atomic / an explicit happens-before
  edge for order / consistent lock ordering for deadlock — **not** a reflexive "add a lock." Fix
  confirmed by re-running the forced repro (necessary, not sufficient — stated as such).

| Tier | Observable bar for C3 |
|---|---|
| **Foundations** | On a single named race (e.g. the lost-update counter) or a clean evidence trail, **describes a breaking interleaving** (or names where the fault is) **and** explains it as a state event — "both threads read `0` before either writes, so one `+1` is lost." D1 solid; D2 at least partial (names the read-modify-write window). Allowed *with* the worked example faded to one missing step. |
| **Working** | On an unseen race, **unaided**: **classifies it as atomicity vs order** and says *why* (D2), proposes a fix that targets the right unit and not just "a lock" (D3), **and** recognizes the **heisenbug** risk where relevant ("adding that print may hide it"). Mis-classifying atomicity as order ⇒ partial pass, flagged. On 3 of 4 such unseen drills. |
| **Advanced** | On a drill **combining mechanisms or under non-reproducibility** — a bug needing both atomicity *and* an order edge; a deadlock from lock-ordering; or "passes in CI, fails in prod" from a partial trace — **unaided**: finds/localizes it (D1), classifies and gives a **falsifiable hypothesis + the one discriminating signal** (D2), proposes a fix at the right unit and confirms it on the forced repro **and does not introduce a deadlock** (D3). Articulates the **underlying principle** on a teach-it-back ("a lock gives atomicity, not order"; "one run is a sample of a schedule space"; "you can only debug what you instrumented") — not just the instance. |
| **Frontier** | `Frontier-N`: presses one mechanism/dimension past the last comfortable success per §6 / `drill-generation.md` §5 (compose bug classes → push the evidence surface → push reproducibility → subtler fix). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier from
what the learner *does* on unseen drills, never from "I've run production systems for years."
Held-out re-assessment and **real-incident transfer** outrank a same-session streak
(`assessment.md` Part 5) — and for a hybrid module whose grading is explicitly soft, the real-code
signal is weighted heavily.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Trusting the run you got.** "It passed locally / in CI a few times, so it's correct." A green
  run is **one sample** of a schedule space the runtime, not you, chose. The fix: reason about the
  *space* of interleavings — ask "is there a schedule that breaks the invariant?" — and force that
  schedule to confirm.
- **Treating a read-modify-write as one step.** Not seeing that `x += 1` / check-then-act /
  `cache[k] = compute()` is read → compute → write, with a window another thread can enter. The
  fix is the A1 move at concurrency scale: decompose it, and make the *whole* unit atomic.
- **"Add a lock" as a blanket spell.** Assuming any lock makes it thread-safe — missing that the
  lock must cover the *whole* read-modify-write (atomicity) and that a lock gives mutual exclusion,
  **not order**. Lu et al.: 73% of real fixes were *not* just adding/changing locks. The fix:
  classify first (atomicity vs order vs deadlock), then apply the matching remedy (atomic region /
  happens-before edge / consistent lock ordering).
- **Debugging a heisenbug by observing it.** Adding a print/breakpoint/sleep, watching the symptom
  vanish, and declaring victory — when the probe changed the timing. The fix: treat disappearance
  under observation as *evidence the probe moved the schedule*, and design observations that don't
  perturb the bug (or reason about the space instead of poking it).
- **Carrying "reproduce-and-step" into production.** Trying to attach a debugger / re-run locally a
  failure that is intermittent and prod-only, then stalling. The fix: reason from **emitted
  evidence** (logs/metrics/traces); remember **absent evidence is not absence** — you see only what
  you instrumented; instrument the gap and wait for recurrence.
- **Print-spraying / changing many things at once.** No hypothesis, no discriminating test — worse
  at scale, where each probe perturbs timing and costs a deploy. The fix is Zeller's loop:
  hypothesize, predict a consequence, make the *one* observation that discriminates.

**Evidence caveat (this is a `[Verified-adjacent]` model + `[Practitioner-canon]` method module —
say so).** The grounding is mixed and must not be oversold:

- The **concurrency taxonomy** half (Lu et al. 2008) is a **strong empirical characterization** —
  105 real bugs, careful classification, an award-winning study — but it is **descriptive field
  data**, and from **C/C++ server/client apps circa 2008**, *not* Python and *not* a causal
  learning result. State it as "the best characterization we have of what real concurrency bugs
  look like," not "research proves teaching this makes you better." It is `[Verified-adjacent]`
  because it *extends* A1's verified execution-model finding into the concurrent setting on solid
  empirical footing — not because the *pedagogy* is proven.
- The **method** half (systematic debugging under non-reproducibility; observability-driven
  reasoning) is **`[Practitioner-canon]`** — Zeller and the observability canon: respected, widely
  taught **craft**, vetted against the named sources during authoring, **not** an effectiveness
  experiment. Per `evidence-base.md` → Refuted, the claim that *systematic tracing causally* beats
  skilled as-needed reading was **not** established; the method is taught as disciplined practice,
  exactly as C1's is. The coach must never present it as verified science.
- The **runner cannot certify concurrency correctness.** It can *prove a bug exists* (force the
  breaking schedule) and *demonstrate a fix closes that schedule*, but it **cannot enumerate all
  interleavings** — so a passing forced repro after a fix is **necessary, not sufficient**. The
  coach states this whenever it grades a fix.
- The **curriculum-wide transfer caveat** applies in full: that drilling forced-interleaving
  puzzles and evidence-trail localization *causally* improves real-incident debugging is the open
  question. The coach leans on the transfer task (§9) — a **real** concurrency/production bug from
  the learner's system — as the honest individual-level evidence, and grades it as the soft
  judgment it is.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real system** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2).

> **Your turn:** Find a **real concurrency or production bug** you have lived through — pick
> whichever you have: (a) a concurrency bug in your own code (a counter/cache/flag that was
> occasionally wrong, a "works on my machine but flaky in CI" test, a data structure mutated from
> two places), **or** (b) a production incident you debugged from logs/metrics/traces because you
> couldn't reproduce it locally. Pick the smallest concrete instance you can.
>
> Now **run the C3 moves.** For a **concurrency** bug: **(1) Find the interleaving** — name the two
> threads/streams and the exact schedule that breaks the intended invariant (which read goes
> stale? which write clobbers which?). Where you can, **reduce it to a minimal snippet and force
> the schedule** (an `Event`/`Barrier`) so the bug is deterministic — then run it. **(2) Classify
> it** — atomicity violation, order violation, or deadlock (Lu et al.)? **(3) Fix the right unit** —
> make the whole read-modify-write atomic, add the missing happens-before edge, or fix the lock
> ordering — *not* a reflexive lock — and re-run the forced repro to confirm it closes *that*
> schedule. For a **production** bug: **(1) Localize from the evidence** — what log line / metric /
> trace span actually pointed at the fault, and what was the *loudest decoy* you had to ignore?
> **(2) Hypothesize** — what was your top hypothesis, and the *one* piece of evidence that
> discriminated it from the runner-up? **(3) Name the observability gap** — what evidence did you
> *wish* you'd instrumented, that would have localized it faster?
>
> Then step back: **was the failure something a single local run would ever have shown you — or
> did it only live in a schedule/load you didn't sample?** If you "fixed" it by adding a print and
> it went away, ask whether you fixed it or just moved the schedule (the heisenbug).

**Grading is softer and named as such — and softer than A1/C1** (`assessment.md` Part 4; §5d). A
real incident has no clean answer key, *and* concurrency correctness is a property of all schedules
the runner cannot exhaust; the coach grades against the §7 rubric (D1 find/localize · D2
classify & reason · D3 fix the right unit) and says: *"this is a judgment call on your real system,
graded against the module's rubric — and softer than an executable pass, because I can force one
breaking schedule but not prove your fix holds under all of them."* Where any sub-claim **is**
runnable — the learner can reduce the race to a minimal snippet — the coach still uses the runner:
**force the interleaving, show the bug, apply the fix, re-run** (the same discipline as the §5d
planted-bug check, now on the learner's real find). **Transfer evidence is weighted heavily:** a
learner who aces forced-interleaving puzzles but, on their own flaky test, reaches straight for a
lock without classifying the race — or "fixes" a prod bug by adding a log and calling the
disappearance a fix — has **not** transferred the skill, and the tracker notes that gap as more
diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **hybrid grading path** (runner for the forced-interleaving / planted-bug
  sub-claim; rubric + exemplars for the reasoning), exercise formats (Debug-this, Trace-the-path,
  Error analysis, Teach-it-back, Generation→Comparison), Frontier escalation:
  `references/drill-generation.md` (this module instantiates §1 and follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, **surface ground truth
  — paste the forced run**, direct feedback, scaffolding ladder): `references/coaching-loop.md`.
- C3 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-incident
  transfer** weighting: `references/assessment.md` (the C3 entry task: a small concurrency bug or
  an evidence trail — find the interleaving / localize the fault, classify it, target the fix).
- Evidence grounding (Lu et al. 2008 concurrency taxonomy; Zeller's systematic debugging;
  *Observability Engineering*; the worked-examples / expertise-reversal instructional finding; the
  Refuted "tracing is causally superior" constraint): `references/evidence-base.md` →
  *Production & concurrency debugging (module C3)* and the reading spine.
- Soft prerequisites: **A1** (notional machine — the single-machine model C3 generalizes), **C1**
  (systematic debugging — the method C3 extends to non-reproducibility), **C2** (stack traces),
  **A3** (tracing); sibling **A4** (concurrency mental models — the concurrent notional machine
  itself; *not yet built*, referenced softly).
- Golden exemplars (~3 per tier, each with a **runner-confirmed** forced interleaving / planted bug
  + classification + right-unit fix): `exemplars/C3/foundations.md`, `exemplars/C3/working.md`,
  `exemplars/C3/advanced.md`.
