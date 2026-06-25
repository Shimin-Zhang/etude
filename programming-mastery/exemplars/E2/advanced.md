# E2 — Advanced exemplars (architectural & technical judgment)

Golden drills for the **Advanced** tier of module E2. Each is a **genuine tension with no clean
answer** or a **combined failure mode** — name the tradeoff on **both** sides, name what breaks
first **for each option**, **state the condition** under which each wins, pick one and **own its
cost**, and articulate the **principle** (teach-it-back). Design judgment is **rubric-graded**
(`drill-generation.md` §3) and **the softest grading in the curriculum** — the coach says so;
every **failure-mode / behavioral** anchor below is **confirmed by running it**
(`drill-generation.md` §2), but the **verdict is never machine-decided**:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct points — **consistency vs availability/latency** (A1) · **build-now vs
defer, with a named change** (A2) · **a combined failure mode: idempotent but order-broken**
(A3). Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7:
**E-tradeoff** = both sides; **E-failure/change** = what breaks first for *each* option;
**E-honesty** = the stated condition + owning the cost of the pick (no cargo-cult). Articulating
the **principle** is the Advanced bar. **A learner who says "it depends" and stops, or who
cargo-cults a pattern ("just use CAP / event sourcing"), has not resolved the tension — flag
it** (§5c: "it depends" with no condition; one-right-answer).

---

## A1 — Strong vs eventual consistency: there is no free lunch

**Context.** A view counter. Design **Strong**: one authoritative counter — every read reflects
every prior write. Design **Eventual**: per-replica local counters, merged later — fast and
available, but a read **before** the merge sees a stale value.

```python
class Strong:                       # every op through one synchronous path
    def __init__(self): self.n = 0
    def incr(self): self.n += 1
    def read(self): return self.n

class Eventual:                     # two replicas accumulate locally; merge later
    def __init__(self): self.r1 = 0; self.r2 = 0
    def incr_r1(self): self.r1 += 1
    def incr_r2(self): self.r2 += 1
    def read_r1(self): return self.r1          # local, fast, possibly stale
    def merged(self): return self.r1 + self.r2 # after anti-entropy sync
```

> **Your turn:** Neither is "correct" in the abstract. Name what each **buys** and **costs**,
> **what breaks first** for each, and **the condition** under which each wins. Then pick one for
> a *view counter* and own the cost.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the eventual design has a real **stale window**)

```
strong read (always current): 3
eventual local read (stale):  2        # missed r2's write
eventual merged read (later): 3        # converges after sync
stale window real? True
status: ok
```

**Gold verdict (the design judgment).**

> **Strong** buys **correctness on every read** (the count is always current) and costs
> **availability and latency**: every op funnels through one synchronous path, so that path is
> a **bottleneck and a single point of failure** — *what breaks first* is throughput and
> uptime under load or partition. **Eventual** buys **availability and low latency** (replicas
> serve reads locally, survive partitions) and costs **consistency**: the runner shows the
> **stale window** — three writes across two replicas, but a local read returns `2`, not `3`,
> until the merge (`stale window real? True`). *What breaks first* is correctness-of-the-moment:
> a reader can see a value that's behind. **Condition:** Strong wins when a stale read is
> *unacceptable* — balances, inventory you'll oversell, a uniqueness check. Eventual wins when
> staleness is *tolerable for a bounded window* and availability/latency matter more. **Pick for
> a view counter:** **Eventual.** A view count that's briefly off by a few is fine; nobody is
> harmed by `2` vs `3` for a second, and you get availability and speed cheaply. **Owned cost:**
> the count is approximate in the short term and only *converges* — if anyone ever needs an
> exact, point-in-time count (billing on views), this choice is wrong and you'd revisit.

> **Principle (teach-it-back):** consistency and availability/latency trade against each other;
> there is no design that maximizes both. The skill isn't picking the "consistent" one because
> it sounds safer — it's matching the **tolerance for staleness** to the **cost of
> unavailability** for *this specific data*.

**Why.** This is the honest version of the consistency/availability tradeoff — reasoned from the
**data's tolerance**, not cargo-culted as "CAP says…" (which is widely misapplied). The runner
proves the stale window is real, so the tradeoff is concrete, not theoretical.

**Diagnoses.** A learner who says *"use strong, it's correct"* has **ignored the
availability/latency cost** (§5c: one-sided / cost-blindness) and missed that "correct" has a
price. A learner who says *"it depends on consistency vs availability"* and stops has **named the
tension but not resolved it** (§5c: "it depends" with no condition). A learner who states the
staleness-tolerance condition, picks Eventual for a *view counter* specifically, and owns the
approximate-count cost is solid and hits the Advanced bar.

---

## A2 — Build the abstraction now, or defer it? (YAGNI meets a named change)

**Context.** A report exporter. Today: **CSV only.** Two designs behave **identically today** —
**(H)** hardcoded CSV, **(P)** parameterized by a formatter "seam." The question is *not* "which
is cleaner" — it's **does the seam pay for itself?**

```python
def export_hardcoded(rows):                       # H
    return "\n".join(",".join(map(str, r)) for r in rows)

def export_seam(rows, fmt):                        # P -- a formatter is passed in
    return fmt(rows)
def csv_fmt(rows):
    return "\n".join(",".join(map(str, r)) for r in rows)
```

> **Your turn:** They produce the same output today. So is the seam **over-build (YAGNI)** or a
> **warranted seam**? What's the deciding factor, and what's the cost of guessing wrong in each
> direction?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — identical today; the seam absorbs a *named* new format)

```
hardcoded: '1,a\n2,b'
seam(csv): '1,a\n2,b'
same today?  True
[a NAMED change arrives -- add TSV -- the seam absorbs it with no edit to the core:]
seam(tsv) new format: '1\ta\n2\tb'
status: ok
```

**Gold verdict (the design judgment).**

> **The runner shows the seam buys *nothing* today** (`same today? True`) — so on a pure YAGNI
> read, it's a presumptive feature and you shouldn't build it on spec. **But YAGNI's deciding
> factor is whether the change is *named and real*.** If a second format (TSV, JSON, XLSX) is
> **actually on the roadmap / requested**, the seam **pays for itself**: the runner shows it
> absorbs TSV **with zero change to the export core** (`seam(tsv) new format: ...`), whereas the
> hardcoded version would need surgery at the call site. **The two ways to be wrong, and their
> costs:** build the seam for a format that **never comes** → you paid cost-of-build + carry for
> nothing (over-build). *Don't* build it and the format **does** come → you pay a refactor
> *later* — but that's cheap **if you kept the code malleable** (Fowler's nuance: refactoring is
> *not* a YAGNI violation; it's what makes deferring safe). **Verdict (condition):** if no second
> format is named, **defer** — ship `export_hardcoded`, keep it easy to change. If a second
> format is named and imminent, **build the seam now** — the change is real, so the seam isn't
> presumptive. The asymmetry matters: deferring is cheap to reverse; over-building carries
> indefinitely.

> **Principle (teach-it-back):** YAGNI is about *presumptive* features. A seam pays for itself
> exactly when the change it anticipates is **named and likely**, not imagined. The safe default
> is defer-and-keep-malleable, because a missing seam is a cheap refactor while a speculative one
> is permanent carry cost.

**Why.** This is YAGNI's real subtlety (§3.2 + the Fowler refactoring nuance): the runner shows
the abstraction is *behaviorally free today*, which is precisely why you don't build it on spec —
**unless** the change is real, in which case the same runner shows it earns its keep.

**Diagnoses.** A learner who says *"always parameterize, it's more flexible"* has **over-built**
(§5c: presumptive abstraction). A learner who says *"hardcode it, YAGNI"* with no regard for a
named change has applied YAGNI **mechanically** (missed the nuance — a *named* change warrants
the seam). A learner who makes the verdict **conditional on whether a second format is named**,
and notes the cost-asymmetry (defer is cheap to reverse), is solid and hits the Advanced bar.

---

## A3 — Idempotency is not enough: a combined failure mode

**Context.** A message-driven handler. Delivery is **at-least-once** (messages can be
**redelivered**) *and* messages can arrive **out of order**. A teammate made the handler
**idempotent** by deduping on event id — *"so retries are safe."* Two events for one account:
set balance to 100, then to 50.

```python
def apply_events(events):
    state = {"balance": None}
    seen = set()
    for eid, value in events:
        if eid in seen:            # idempotent: ignore a redelivered event
            continue
        seen.add(eid)
        state["balance"] = value   # last-writer-wins on ARRIVAL order
    return state["balance"]
```

> **Your turn:** Idempotency handles redelivery — so is this handler correct under at-least-once
> delivery? Name the failure it **still** has, what breaks first, and what property it needs that
> idempotency doesn't give.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — idempotent against dupes, but **order-broken**)

```
in order      : 50         # e1=100 then e2=50  -> correct final state
out of order  : 100        # e2=50 then e1=100  -> WRONG (order flipped)
redelivered   : 50         # e1,e2,e1 (dup)     -> idempotent: dup ignored, correct
idempotent but order-broken? True
status: ok
```

**Gold verdict (the design judgment).**

> **Idempotency is necessary but not sufficient** — this handler has a **second, independent
> failure mode**: it's **order-sensitive**, and the network reorders. The runner shows both
> truths: redelivery is handled (`redelivered -> 50`, the dup ignored), **but** out-of-order
> delivery corrupts the state (`out of order -> 100` instead of `50`). The bug is
> `last-writer-wins on *arrival* order` — fine if arrival order equals causal order, which
> **at-least-once delivery does not guarantee.** **What breaks first:** the first time the
> broker redelivers or reorders under load/partition, the account lands on the *wrong* final
> value — silently. **What it needs that idempotency doesn't give:** an **ordering property** —
> a version/sequence number or timestamp so the handler applies *last-by-version*, not
> *last-by-arrival* (a happens-before edge; ties C3's order-violation). e.g. drop an event whose
> version is older than the current state. **Verdict:** make it idempotent **and**
> order-resolving — both, because at-least-once delivery breaks **both** assumptions at once.
> **Owned cost:** you now must carry a version per event and per state, and define the
> conflict-resolution rule — real complexity, but it's the price of correctness over an
> unreliable, unordered channel.

> **Principle (teach-it-back):** "the network is reliable" fails in *more than one way at once* —
> messages can duplicate **and** reorder **and** be lost. Designing for one (idempotency for
> duplicates) and assuming the others away is the trap; reason about *each* fallacy the channel
> violates, not just the one you fixed.

**Why.** This is a **combined** failure mode (§5a Advanced): two of the fallacies bite together,
and fixing one leaves the other. The runner proves idempotency alone is insufficient — the
out-of-order case really does land on `100`.

**Diagnoses.** A learner who says *"it's idempotent, so it's safe under at-least-once"* has
**fixed one fallacy and assumed the rest away** (§5c: happy-path-only at the protocol level) —
the runner's `out of order: 100` refutes it. A learner who names the *separate* ordering failure,
ties it to a version/sequence number (happens-before), **and** owns the added cost is solid and
hits the Advanced "combined symptom + principle" bar. If a learner disputes that order matters,
**run the out-of-order case** and show `100`.
