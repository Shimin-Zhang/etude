# E2 — Architectural & Technical Judgment `[Practitioner-canon]`

> **Module type.** `[Practitioner-canon]` — **pure craft, and the softest-graded module in
> the curriculum.** Architectural judgment is design *opinion* shaped by hard-won experience,
> not an empirical finding, and a design tradeoff has **no executable ground truth and usually
> no single right answer.** The coach must say this *loudly*: it grades the **reasoning**
> (did you name the real tradeoff? the failure mode? the cost? the thing that breaks first?)
> against a **rubric + golden exemplars**, and surfaces genuine uncertainty rather than
> pretending there is one correct architecture. Where a design choice has a concrete failure
> mode, the coach *runs* it to pin the one thing that **is** decidable — *that the failure is
> real* (a retry double-charges; a cache goes stale; an unbounded wait hangs) — never to
> decide *which design is right*. (The validator badge on this file is `[Practitioner-canon]`;
> the honest prose badge is the same — there is no empirical half to claim.)
>
> **Core idea.** A design choice is a **tradeoff under uncertainty**, not a correctness
> question. The skill is **not** knowing "the right architecture" (there rarely is one) — it
> is reasoning *honestly* about what a choice **buys**, what it **costs**, and **what breaks
> first** when the system grows or something fails. You design for the **change** and the
> **failure** you can actually *name*, and you refuse to build for the ones you can't.

---

## 1. Evidence basis `[Practitioner-canon]`

This module is **canon by design**, and the coach must **never present it as verified
science** (`evidence-base.md` → badge rules). Its substance is respected, widely taught
*engineering judgment* — vetted against the named primary sources during authoring — not an
empirical result. Architectural judgment is, more than any other module here, the kind of
thing where **"research shows…" would be a lie**: there is no controlled study that "the
right architecture" exists, and the practitioners who wrote these sources say plainly they
are offering lenses, not laws. Four pillars, all badged `[Practitioner-canon]`.

**(a) The three concerns + tradeoff framing — Kleppmann, *Designing Data-Intensive
Applications* `[Practitioner-canon]`.** Cite via `evidence-base.md` → reading spine (already
listed: *"Systems/architecture judgment at scale. Staff anchor for E2"*) and the proposed E2
craft-source subsection. **Kleppmann, M. (2017). *Designing Data-Intensive Applications: The
Big Ideas Behind Reliable, Scalable, and Maintainable Systems.* O'Reilly. ISBN
978-1-449-37332-0.** Chapter 1 gives this module its scaffolding and its honesty, confirmed
against the source during authoring:

- The **three concerns** every system is judged against — **reliability** (*"continue to
  work correctly … even in the face of adversity"* — hardware/software faults and human
  error), **scalability** (*"reasonable ways of dealing with growth"* in data, traffic, or
  complexity), and **maintainability** (*"many different people will work on the system …
  and they should all be able to work on it productively"*, via **operability, simplicity,
  and evolvability**).
- The **fault vs. failure** distinction that grounds "design for failure": a **fault** is one
  component deviating from its spec; a **failure** is the system *as a whole* stopping
  service. You **cannot eliminate all faults**, so a reliable system is built to be
  **fault-tolerant** — to stop a fault from becoming a failure — rather than fantasizing that
  faults won't happen. (Kleppmann notes deliberately *inducing* faults, e.g. Netflix's Chaos
  Monkey, to prove the tolerance is real.)
- **Describe before you optimize.** Scalability is not a yes/no property — you **state the
  load** (Kleppmann's *load parameters*) and **describe performance** honestly (e.g. with
  **response-time percentiles and tail latency**, not a misleading average) *before* claiming
  a design "scales." "Will it scale?" is meaningless until you say *scale of what, to what.*
- Above all, the book's *method*: there is **no universally right answer**; you reason about
  **tradeoffs** — what each choice buys, what it costs, and how it behaves under fault and
  load. That tradeoff-analysis stance **is** this module.

**(b) Designing for failure — the Fallacies of Distributed Computing `[Practitioner-canon]`.**
The canonical checklist of false assumptions that make a design fragile the moment it crosses
a process boundary. Originated at **Sun Microsystems**: **L. Peter Deutsch** articulated seven
(c. 1994, incorporating four that **Bill Joy and Dave Lyon** had named), and **James Gosling**
added the eighth (c. 1997). The eight, verbatim: **(1) the network is reliable; (2) latency is
zero; (3) bandwidth is infinite; (4) the network is secure; (5) topology doesn't change;
(6) there is one administrator; (7) transport cost is zero; (8) the network is homogeneous.**
The standard explanatory reference is **Rotem-Gal-Oz, A. (2006). *Fallacies of Distributed
Computing Explained.*** **⚠ Provenance flag:** there is **no single canonical primary
publication** — the list propagated as an internal/oral Sun list, so this is *attributed
folklore*, cited as origin-of-record with Rotem-Gal-Oz as the explanatory essay; the coach
presents it as a respected checklist, not a sourced theorem.

**(c) When *not* to build — YAGNI `[Practitioner-canon]`.** Cite via `evidence-base.md` →
proposed E2 subsection. **"You Aren't Gonna Need It"** is the Extreme Programming maxim
(Beck/Jeffries; the XP practice of *Simple Design*) against building **presumptive features**.
The load-bearing modern statement is **Fowler, M. (2015, 26 May). *Yagni* (bliki,
martinfowler.com)**, confirmed verbatim during authoring: a presumptive feature is *"any code
that supports a feature that isn't yet being made available for use,"* and building it on spec
incurs four costs — **cost of build**, **cost of delay**, **cost of carry** (*"the code for
the presumptive feature adds some complexity … this complexity makes it harder to modify and
debug that software, thus increasing the cost of other features"*), and **cost of repair**.
**The crucial nuance, verbatim:** *"Yagni only applies to capabilities built into the software
to support a presumptive feature; it does not apply to effort to make the software easier to
modify."* So YAGNI is **not** "never abstract" or "never leave a seam" — refactoring and
keeping code malleable are how YAGNI stays *safe*. That distinction (don't build the feature;
*do* keep the change cheap) is exactly E2's "design for the change you can name."

**(d) Strategic vs. tactical programming — Ousterhout `[Practitioner-canon]` (REUSED from D1).**
This module **reuses D1's anchor**, not a new one (`evidence-base.md` → D1a: Ousterhout, *A
Philosophy of Software Design*). **Tactical** = get the feature working as fast as possible
and let complexity accrete; **strategic** = treat working code as *not enough* and invest
continuously in a clean design, because accumulated complexity is what eventually slows you to
a crawl. E2 puts this on the architecture clock: the architectural version of tactical is
*ship the happy path and discover the failure modes in production*; the strategic version is
*name the failure and the change up front and price them in.* **Honesty (per D1):** Ousterhout
says of his own book, *"take the suggestions … with a grain of salt"* — it is one experienced
engineer's philosophy from a course, **not** a study.

**Why these license this module.** Kleppmann gives the **axes** to reason on (reliability,
scalability, maintainability) and the **tradeoff method**; the fallacies give the **failure
checklist** (what breaks when you cross a boundary); YAGNI gives the **"don't build it" half**
(and its nuance — keep the seam, skip the feature); Ousterhout gives the **investment stance**
(price the design in, don't only ship). The combined claim this module teaches: **a good
architectural judgment names what the choice buys, what it costs, and what breaks first under
change and failure — and owns that there is rarely one right answer, only a defensible
tradeoff.**

**Read through the transfer caveat — and then some.** Unlike the `[Verified]` Track-A modules,
E2 has **no program-comprehension experiment behind it at all**: it is four craft sources, two
of them explicitly opinion. The curriculum-wide **transfer caveat** (`evidence-base.md`)
applies in full and bites *hardest here*: that drilling tradeoff-analysis on synthetic systems
*causally* improves a given engineer's real designs is **unproven**, and design judgment is
exactly the kind of skill where the only honest test is the learner's **own real system** (§9).
**AI-era note:** as agents draft most first-draft code *and* propose architectures, the
bottleneck moves to *judging* whether a fluent, confident design is sound or just plausible —
and agents reliably **over-build** (they love to add a queue, a cache, a service). Resisting an
authoritative-sounding over-engineered proposal is the documented AI-era miss
(`evidence-base.md` → AI-era section; ties to F1 calibration and E3 review) — `[Verified-adjacent]`
as a *priority*, not proof.

---

## 2. Soft prerequisites

**D1 (managing complexity / abstraction) recommended.** E2 is D1 one level up: D1 asks "is
*this module* deep or shallow?"; E2 asks "do these *components and boundaries* earn their
keep, and what breaks when the system grows or fails?" The same Parnas move — **hide the
decision likely to change** — is the heart of "design for change," and the YAGNI/"pays for
itself" judgment is D1's "abstraction must pay for itself" applied to whole subsystems (a
queue, a cache, a service). A learner who cannot tell deep from shallow at the module level
will struggle to tell a load-bearing boundary from a speculative one at the system level.

**E1 (you architect what you can comprehend) is the natural sibling.** (E1 may not be built
yet; reference it softly.) The thesis E1 owns — *you cannot soundly design what you cannot
hold in your head* — is why E2 grades the **reasoning**, not a diagram: an architecture you
can't explain the failure modes of is one you can't defend. **A1 (notional machine)** and
**C3 (production & concurrency debugging)** help because several E2 failure modes are
execution-model events at system scale — a retry that double-applies (non-idempotency), an
out-of-order delivery (C3's order-violation), a partial failure across a boundary.
**E3 (code review)** and **F1 (calibration)** are the AI-era siblings: judging an
agent-proposed architecture is a *review under your own overconfidence*.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner reaches for infrastructure reflexively
(the over-build reflex), the coach notes the gap likely traces to D1's "pays for itself" and
*suggests* shoring it up — but does not forbid E2.

---

## 3. The mental model

**A design choice is a tradeoff under uncertainty, not a correctness question. You judge it on
three axes — reliability, scalability, maintainability — by asking the same three questions
every time: what does this BUY, what does it COST, and what BREAKS FIRST when the system grows
or something fails? There is rarely one right answer; there is a defensible tradeoff, named
honestly, or there is hand-waving.**

The model is **three concerns** (Kleppmann), **two failure axes** you reason about, and **one
repeated move**:

| Piece | What it is | The question it forces |
|---|---|---|
| **Concern: reliability** | The system keeps working *under adversity* — faults happen (hardware, software, human), and the design's job is to stop a **fault** becoming a **failure**. | *What breaks first when something fails — a node, a network call, a retry, a bad input? Is that fault contained, or does it take the whole system down?* |
| **Concern: scalability** | Reasonable ways to cope with **growth** in data, traffic, or complexity — *after* you've named the **load parameter** that will actually bite. | *Scale of what, to what? Which parameter grows, where's the cliff, and is the cost worth paying now?* |
| **Concern: maintainability** | Different people can keep working on it productively — **operability, simplicity, evolvability**. | *What does this cost the next person to change it? What change is coming, and is there a seam for it?* |
| **Axis: design for FAILURE** | Assume the fallacies are false — the network *isn't* reliable, latency *isn't* zero, calls fail *partway*, messages arrive *twice* and *out of order*. | *Which fallacy am I assuming? What happens on the unhappy path I'm not testing?* |
| **Axis: design for CHANGE** | Hide the decision likely to change (Parnas/D1); leave a **seam**, but **don't build the feature** (YAGNI). | *What change can I actually name? Is there a cheap seam for it — and am I building the seam, or the speculative feature?* |
| **The move: name the tradeoff** | Every choice **buys** something, **costs** something, and has a **thing that breaks first**. Score all three, on the relevant concern, out loud. | *What does this buy? What does it cost (build / carry / operate / a new failure mode)? What breaks first?* |

**The discipline in one line: *name what the choice buys, what it costs, and what breaks first
— there is rarely one right architecture, only a tradeoff reasoned honestly or a decision
hand-waved.*** The system has no opinion about your design and no controlled study will rank
your options; the **failure modes and the costs** are the judges. Three corollaries the module
drills:

1. **Reason about the unhappy path, not the demo.** A design that works when everything works
   is not "reliable" — it is *untested against failure*. Name the fallacy you're assuming (the
   network is reliable; the call returns; the message arrives once, in order) and ask what
   happens when it's false. A green run is **one sample**, not fault-tolerance (the
   architecture-scale version of C3's heisenbug and F1's overconfidence).
2. **Most components you're tempted to add don't pay for themselves *yet*.** A cache, a queue,
   a service, a plugin layer each **buys** something *and* adds **carry cost** (Fowler) and a
   **new failure mode** (staleness, redelivery, partial failure, an extra thing to operate).
   YAGNI: don't build the presumptive feature. But **do** leave the cheap seam — hiding the
   decision likely to change is *not* a YAGNI violation, it's how YAGNI stays safe.
3. **"It depends" is a real answer — finish it.** The honest output of a tradeoff is often a
   *condition*: "A wins **if** writes dominate and staleness is tolerable; B wins **if** reads
   must be current." A learner who says "it depends" and **states the condition** has the
   skill; one who says "it depends" and stops has dodged it. The coach rewards the *named
   condition*, never a confident cargo-culted pattern.

---

## 4. Worked example — design for failure: is this safe to retry?

*(Foundations depth: the full judgment shown — the choice, the failure mode named, the cost,
the runner-verified proof that the failure is real. This fades by tier; see the table after.)*

The skill is to **judge like a senior engineer**: take a design choice, name which fallacy it
assumes, work out *what breaks first* on the unhappy path, and price the fix. Consider a
payment handler. A client calls `charge(account, amount)`. The network is **not** reliable
(fallacy #1): the client may **time out and retry** even though the first call *already
succeeded* server-side. The design question: *is this operation safe to retry — and if not,
what does it cost to make it safe?*

**Design A — naive.** `charge` just applies the change:

```python
def charge(account, amount):
    balances[account] -= amount      # applies every time it's called
    return balances[account]
```

**Design B — idempotent.** Each logical request carries an id; a retry of the same id is a
no-op that returns the prior result:

```python
def charge(account, amount, request_id):
    if request_id in processed:
        return processed[request_id]      # retry: return prior result, do NOT re-apply
    balances[account] -= amount
    processed[request_id] = balances[account]
    return balances[account]
```

**Step 1 — Name the fallacy and the failure mode.** Both designs are *correct on the happy
path* — one call, one charge. The choice only matters on the **unhappy path** the naive design
ignores: *the network is reliable* is false, so a real client **retries** on timeout. Design A
is **not idempotent** — a retry applies the charge **twice**. Design B records processed
request-ids, so a retry is a no-op.

**Step 2 — Score the tradeoff.** Design B **buys** retry-safety (correctness under the
client's real behavior). It **costs** a little: you must thread a `request_id` through the
call and **store** the processed set (which itself needs bounding/expiry — a maintainability
cost, and arguably a new small failure mode if that store fails). Design A **buys** simplicity
and **costs** *money*: under the failure that *will* happen, it double-charges. **What breaks
first:** A breaks the instant a single client retries a single timed-out request — which at
scale is *constant*, not rare.

**Step 3 — The verdict** (names the tradeoff · the failure mode · the cost · the condition):
*Make the operation idempotent (Design B). The network will retry — that's not an edge case,
it's the contract — so a non-idempotent write is a money bug waiting for the first timeout.
The cost is a request-id and a bounded dedup store; cheap relative to double-charging. The one
condition where A is acceptable: the operation is **naturally idempotent already** (a
set-to-value, not a decrement) or genuinely has no external effect — then there's nothing to
make safe.*

**Verified ground truth** (the coach *runs* both designs to prove the failure is **real** —
that retrying A double-charges and retrying B does not — `drill-generation.md` §2; even though
the *design verdict* is rubric-graded):

```
$ python <skill-dir>/runtime/python/runner.py E2_worked_idempotency.py
naive balance after retry: 40
idempotent balance after retry: 70
naive double-charged? True
idempotent safe? True
status: ok
```

(The snippet starts both accounts at 100 and applies one logical charge of 30 **twice** — the
client's timeout-then-retry. The naive balance lands at **40** (charged 30 *twice*); the
idempotent balance lands at **70** (charged once, the retry a no-op). The runner proves the
failure mode is real — it is not a matter of opinion that A double-charges. What it **cannot**
tell you is whether idempotency is "worth it" for *your* system; that judgment is the
rubric-graded part, and it's why this is a judgment module.)

**What the verdict makes visible** (and a happy-path demo hides): the design difference is
**invisible until something fails**. Run each once and they agree; the *retry* — the failure
the naive design refused to imagine — is where A loses money. Architectural judgment is
exactly this: reasoning about the path you're *not* exercising in the demo.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> judgment helps **novices** (it shows the name-the-failure-then-price-it move) but is
> **redundant load for the more advanced**, who learn more by reasoning it through
> themselves. So the coach fades it:
>
> | Tier | Worked-example depth at E2 |
> |---|---|
> | **Foundations** | **Full** — the choice, the named fallacy/failure mode, the cost, the verdict, and the runner proof, every step shown. |
> | **Working** | **Partial** — coach names *that* the design has a failure mode but leaves **what breaks first, what it costs, and the verdict** to the learner. |
> | **Advanced** | **Skeleton** — coach hands over the design(s) and the rubric only; learner names the tradeoff on both sides, the condition, and the verdict unaided. |
> | **Frontier** | **None** — straight to the design (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for E2. Grading mode is
declared up front: **rubric + golden exemplars** (§5d) — this is the **softest-graded** module
in the curriculum, a pure judgment module. (Where a design choice has a concrete failure mode,
the coach still *runs* it to prove the failure is real — a retry double-applies, a cache goes
stale, an unbounded wait hangs, two designs behave identically *today*; the *design verdict* is
graded against the rubric, never by the runner.)

### 5a. Tier definitions (E2-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Most
drills present a design choice, a small system, or a proposed change, and ask one of: *what
does this buy and cost? · what breaks first under failure/load? · would you build this (YAGNI /
pays for itself)? · where's the seam the coming change needs? · is this the right level (single
process vs distributed)?***

| Tier | E2 criterion | Example shape |
|---|---|---|
| **Foundations** | **One clear, single-axis** call with no genuine tension: a plainly speculative abstraction (build it on spec? — no), a plainly missing failure-handling (a retry that double-applies; a call that crashes on a partial response), or a plainly leaked/hardcoded decision. **Name the tradeoff** in buys/costs/breaks-first terms. The skill is *seeing the failure or the over-build and articulating it.* | A strategy-pattern framework for the *one* channel that exists today; a `plan_price` that `KeyError`s on a degraded response; a tax rate duplicated at two sites. |
| **Working** | A **real but resolvable** tradeoff: a component that *looks* worth adding but whose cost outweighs its benefit at this scale (a cache that buys speed and costs staleness); a "design for the future" call where the answer is *YAGNI-but-leave-the-seam*; a no-timeout call. **Judge it, name what it buys AND costs, name what breaks first, and resist the one-sided answer** ("a cache is always faster"). | "Should we add a read-through cache here?"; "no timeout on this downstream call — fine?"; "split validate+charge into two services?" |
| **Advanced** | A **genuine tension with no clean answer** or a **combined** failure mode: two architectures each winning on a *different* concern (consistency vs availability/latency; build-now vs defer); a failure that needs *two* properties at once (idempotency **and** ordering). **Decide, name the tradeoff on BOTH sides, name what breaks first for each, state the CONDITION under which each wins, and own the cost of your pick.** Plus teach-it-back the principle. | Strong vs eventually-consistent counter; a seam that pays off *iff* a named change is real; at-least-once delivery that's idempotent but order-broken. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations design hides its call behind a real tradeoff (that's
Working/Advanced), or a Working/Advanced design has an *obvious* one-word answer (that's
Foundations). Apply the self-check (`drill-generation.md` §4) and re-level before posing — and
watch the specific E2 trap: a drill that secretly needs **two** judgments (a failure mode *and*
a build/don't-build call) is Advanced, not Foundations.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for E2:

- **Question asked** — *what does this buy/cost?* · *what breaks first under failure/load?* ·
  *would you build this (YAGNI / pays for itself)?* · *where's the seam for the named change?*
  · *is this the right level (single process vs distributed)?* · *defend or refute this design.*
- **Concern stressed** (Kleppmann) — **reliability/failure** · **scalability/load** ·
  **maintainability/change** · the cross-cutting **operability/cost** (who runs it, who pages
  at 3am, what's the carry cost).
- **Failure mode** (the fallacies, made concrete) — **partial failure** (a call fails partway)
  · **retry / non-idempotency** (the network retries) · **redelivery + reordering**
  (at-least-once, out-of-order) · **crash / state loss** (restart loses in-memory state) ·
  **overload / no backpressure / unbounded wait** (no timeout, no eviction) · **staleness /
  consistency** (a cache or replica lags) · **single point of failure**.
- **The temptation / decoy** — **over-build** (add infra: cache/queue/service/framework) ·
  **under-build** (hardcode a decision that will change) · **cargo-cult** a pattern ("we
  should use microservices/event sourcing/CQRS") · **scale the wrong thing** (shard at 100
  users; optimize the cheap stage) · **happy-path green run** treated as fault-tolerance.
- **Surface** — a single function with an architectural assumption · two designs to compare
  (A vs B) · a small system + a proposed change · a "should we add X?" proposal · a design a
  teammate (or an AI) wrote *with its justification* (error-analysis).
- **Format** (`drill-generation.md` §6) — primarily **Generation → Comparison** (learner
  writes the tradeoff verdict / the deciding condition, coach reveals the gold) and
  **Debug-this** cast as *design*-review ("what breaks first here?"); also **Teach-it-back**
  (articulate *why* you design for the failure you can name) and **Error analysis** (here is a
  *one-sided justification someone wrote* — "we should add Kafka so it scales" — what did it
  ignore: the cost, the failure mode, the missing load parameter?).

Keep an in-session log of the `(question, concern/failure-mode, surface, format)` tuples used;
do not repeat a tuple until the others are exercised. Mode-collapse here looks like asking
"should we add infra?" about three caches in a row — vary the concern and the failure mode.

### 5c. Common-error catalog

The *specific* architectural-judgment failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the **named craft sources**
(Kleppmann's concerns + fault/failure; the fallacies of distributed computing; YAGNI;
Ousterhout's strategic/tactical), not in trivia. **The root of most of them is one inversion:
evaluating a design by whether it works on the happy path and serves the feature, instead of
by what it COSTS, what it BUYS, and what BREAKS FIRST under change and failure — and treating
the choice as having one right answer rather than a named tradeoff.**

```
Error: Judges a design by whether it works when everything works; never asks what breaks
       under failure (a retry, a partial response, a crash, a redelivery).
Diagnoses: Happy-path-only reasoning -- assumes the fallacies are TRUE (the network is
           reliable, the call returns, the message arrives once). The unhappy path the
           design ignored is exactly where it fails. (Fallacies of distributed computing;
           Kleppmann fault-vs-failure.)
Example trigger: the naive charge() that double-applies on retry (Worked/Foundations);
                 plan_price() that KeyErrors on a degraded response (F2).

Error: Reaches for infrastructure -- a cache, a queue, a service, a plugin framework --
       for a need that doesn't exist yet, and calls it "scalable" or "future-proof."
Diagnoses: Over-build / resume-driven design; violates YAGNI. Pays cost-of-build and
           cost-of-carry NOW for a benefit that may never arrive, and inherits a new
           failure mode (staleness, redelivery, partial failure). The abstraction doesn't
           pay for itself yet. (Fowler, Yagni; Ousterhout, "different is not better.")
Example trigger: the strategy-pattern Notifier for the one channel that exists (F1);
                 "we should add Kafka so it scales" with 100 users (error-analysis).

Error: Hardcodes a decision that is KNOWN-likely-to-change (a rate, a region, a format) at
       N call sites, so the foreseeable change becomes a shotgun edit / silent inconsistency.
Diagnoses: Under-build -- the dual of over-building. Didn't design for the change you can
           actually NAME; no seam where one was cheap and warranted. (Parnas/D1: hide the
           likely-to-change decision; YAGNI's nuance -- keep the seam.)
Example trigger: a tax rate duplicated at two sites that goes inconsistent on a partial
                 edit (F3); a single-region assumption baked through the code.

Error: Picks an architecture and defends it as "correct" / "best practice" / "scalable"
       with no statement of what it costs or gives up.
Diagnoses: One-right-answer thinking -- treats design as a correctness question and
           cargo-cults a pattern. THE central E2 failure: the module grades the reasoning,
           and "it's just better / it's the standard way" is a non-answer. (Kleppmann: no
           universally right answer; reason about tradeoffs.)
Example trigger: any drill where the learner names a winner but never names its cost or the
                 condition under which the other choice wins.

Error: Counts only what a component BUYS ("a cache makes it fast"), never its COST
       (invalidation, staleness, an extra thing to operate, a new failure mode).
Diagnoses: Cost-blindness -- scores one side of the tradeoff. Every component adds carry
           cost and usually a new failure surface; a benefit named without its cost is half
           a judgment. (Fowler cost-of-carry; Kleppmann operability.)
Example trigger: "add a read-through cache" -- learner says "faster" and stops, missing the
                 stale-read the runner demonstrates (W1).

Error: Optimizes for a scale that isn't real yet (shards at 100 users) OR ignores the load
       parameter that will actually bite; "will it scale?" with no "scale of what, to what."
Diagnoses: Didn't DESCRIBE the load before designing for it (Kleppmann's load parameters);
           guessed the bottleneck (ties D4). Premature or misdirected scaling.
Example trigger: "design this for 1M users" when there are 100 and the real limit is a
                 single-writer DB; optimizing the cheap stage.

Error: Reaches for a distributed system (microservices, a queue, multiple regions) for a
       problem a single process would solve -- inheriting all eight fallacies.
Diagnoses: Distributed-by-default -- takes on partial failure, latency, consistency, and
           operational cost without the problem that requires them. (Fallacies; Kleppmann:
           distribution is a cost you pay only when forced.)
Example trigger: "split validate+charge into two services" -- the split adds a partial-
                 failure gap with no transaction across it (W3).

Error: Treats a single green run / a passing happy-path test as evidence the design handles
       failure ("it works, ship it").
Diagnoses: Conflates a passing SAMPLE with fault-tolerance -- the heisenbug/one-sample
           fallacy at architecture scale, and the F1 overconfidence miss. A design's failure
           modes don't show up in the demo. (Kleppmann: induce faults to prove tolerance;
           C3 heisenbug; F1.)
Example trigger: a design whose failure only appears under retry/partial-failure/reorder --
                 the coach RUNS the failure to show the green demo was a lie (Worked, W1, A3).

Error: Says "it depends" and stops -- names a tension but never states the condition under
       which each choice wins, or never picks.
Diagnoses: Mistakes naming-the-tension for resolving it. "It depends" is the START of an
           Advanced answer; the skill is the CONDITION ("A wins if writes dominate and
           staleness is OK; B wins if reads must be current"). (Kleppmann tradeoff method.)
Example trigger: the strong-vs-eventual counter (A1) or build-now-vs-defer (A2) where the
                 learner sees both sides but won't commit to a condition.
```

### 5d. Grading mode

**Rubric + golden exemplars** (`drill-generation.md` §1d, §3), and the coach states **loudly**
that this is the **softest grading in the curriculum**. E2 has **no executable ground truth for
the design judgment** — "is this the right architecture?" is not a computation, and usually has
more than one defensible answer. The coach grades a learner's verdict like this (the §3
judgment path, made concrete for E2):

1. **Run the failure mode where one exists (the one executable sub-claim).** Although the
   *verdict* is rubric-graded, the coach uses the runner
   (`python <skill-dir>/runtime/python/runner.py snippet.py`, `drill-generation.md` §2) to pin
   the thing that **is** decidable: that the **failure is real**. Most often that means
   demonstrating a **retry double-applies**, a **cache returns stale data**, an **unbounded
   wait hangs** (`status: timeout`), a **partial failure leaves split state**, an
   **out-of-order delivery corrupts**, or that two designs are **behaviorally identical today**
   (so the difference is *speculative complexity*, not behavior). This anchors the gold to real
   behavior, not the coach's guess. If a learner *disputes* a failure ("retrying is fine"), the
   coach **runs it** and shows the double-charge. **The runner never decides which design is
   right** — only that the named failure does or doesn't happen.
2. **Score the verdict against the E2 rubric (§7), criterion by criterion** — *did they name
   the tradeoff on both sides (buys AND costs)? did they name what breaks first under
   failure/load, or the seam the change needs? did they own the uncertainty — state the
   condition under which the other choice wins, and not cargo-cult a pattern?* Each is a
   3-point criterion (§7), graded explicitly, one by one.
3. **Cite the closest golden exemplar.** Compare to the tier's golds in
   `exemplars/E2/<tier>.md` — "your answer is close to the **weak** exemplar: you said the
   cache makes it faster and stopped" vs. "close to the **strong** exemplar: you named the
   staleness cost and the condition under which the cache is still worth it." The golds are the
   calibration anchor.
4. **Name it as soft — louder than any other module.** The coach says out loud: **"this is a
   design judgment graded against the module's rubric + exemplars, not a machine-verifiable
   answer — and architecture has no single right answer, so I'm grading your *reasoning*, not
   matching you to a key."** Do **not** present a plausible verdict as provably correct; rubric
   passes here are the **softest evidence** in the curriculum.

E2 drills are thus **partly hybrid in a narrow way**: any **failure-mode** sub-claim (a retry
double-applies; a wait hangs; two designs are equal today) is executable-graded by the runner;
the **tradeoff verdict** is rubric-graded. Report the verdicts separately — a learner who
correctly *runs* the snippet and sees the failure but reaches a **one-sided verdict** (e.g.
"the cache double-checked out as faster, so use it" — ignoring the stale read the runner just
showed) is a **partial pass**, and the coach flags exactly that, because scoring only one side
of the tradeoff is the central E2 confusion.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one genuine design tension or combined failure mode, judged with the tradeoff
  named on both sides, the condition stated, and the cost of the pick owned.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new dimension
  of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for E2, with step counts:

1. **Subtler / costlier failure mode** (push the failure axis): from a *visible* over-build →
   to a failure that only bites under **partial failure** (Frontier-1) → to one that needs
   **two properties at once** (idempotency *and* ordering; Frontier-2) → to a **consistency /
   distributed-state** hazard where the failure is non-local and intermittent (Frontier-3).
   Each is one increment.

2. **Bigger surface** (push the surface axis): from one component → to a component **plus its
   operators and callers** (who pages at 3am? what's the blast radius?) → to a **multi-service**
   design where the right answer is "the boundary is in the wrong place; here's where it should
   be" (a Parnas/Kleppmann re-decomposition), not a local fix. Each is one increment.

3. **Harder "it depends" / no clean winner** (push the judgment axis): designs where neither
   option wins outright and the answer is a **named condition** — strong vs eventual under a
   *specific* read/write mix; build-now vs defer under a *specific* probability the change
   lands; sync vs async under a *specific* latency budget. The learner must hold the tension
   and **state the condition**, not pick a side reflexively. One increment per added degree of
   genuine ambiguity.

4. **Generate and defend, don't just judge** (push the format axis): from *critiquing* a design
   → to **proposing** the design (write the tradeoff and the seam) → to **defending** it against
   a plausible objection ("but it won't scale!" — to which the honest answer is often "it
   doesn't need to *yet*, and here's the cheap seam for when it does") → to **teaching the
   principle** so it transfers. Proposing is one increment over judging; defending is another.

5. **Judge an AI-proposed architecture → the AI-era frontier.** A design that *reads* fluent,
   confident, and idiomatic (as agent output does) but **over-builds** (a queue and a cache and
   three services for a CRUD app) or **assumes a fallacy** — the spec-§12 apex skill of
   verifying a design you didn't write. One increment for "AI-plausible surface," another for
   "and you must not be talked into the complexity by how authoritative it reads" (ties F1:
   over-trusting fluent output, and agents' documented over-engineering reflex, is the AI-era
   miss).

Track the level as `E2: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the three E2 dimensions. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (reached a defensible judgment *and* named the tradeoff
and what breaks first — a confident "use a queue" with no cost named is a Foundations-level
pass at best, because an architectural verdict without a named tradeoff is a guess), and
**unaided + durable** (a same-session streak is provisional until a delayed re-assessment or
the real-code transfer task confirms it; `assessment.md` Parts 3–5).

**The three scored dimensions** (each 3-point: absent / partial / solid):

- **E-tradeoff — both sides.** Did they name what the choice **buys** *and* what it **costs**
  (build / carry / operate / a new failure mode) — not a one-sided "it's better / it's faster /
  it's the standard"?
- **E-failure/change — what breaks first.** Did they name the **failure mode** (which fallacy
  is assumed; what breaks under retry/partial-failure/reorder/load) and/or the
  **likely-to-change axis** (the seam) — *what breaks first* when the system grows or
  something fails? *(Executable sub-claim where present: the failure mode / behavioral-equality
  is confirmed by the runner; §5d.)*
- **E-honesty — owned the uncertainty.** Did they **own that there's no single right answer** —
  state the **condition** under which the other choice wins, refuse to cargo-cult a pattern,
  and not dress canon as fact? This is the meta-dimension unique to the softest module: the
  coach rewards a well-reasoned "it depends, *and here's the deciding factor*" over a confident
  wrong certainty.

| Tier | Observable bar for E2 |
|---|---|
| **Foundations** | On a **plainly** over-built / failure-ignoring / hardcoded design (no real tension), **names the tradeoff correctly and says why** in buys/costs/breaks-first terms (e.g. "the strategy framework buys nothing today — one channel exists — and costs carry complexity; don't build it, leave a function you can extend"). E-tradeoff solid; E-failure/change at least partial. Allowed *with* the worked example faded to one missing step. |
| **Working** | On a **real but resolvable** tradeoff (cache that buys speed/costs staleness; no-timeout call; split-into-services), **unaided**: names the tradeoff on **both** sides (E-tradeoff), names **what breaks first** (E-failure/change), **and** resists the one-sided answer — and reaches a defensible verdict with at least a gesture at the condition (E-honesty). Names only the benefit (or only the cost) ⇒ partial pass, flagged. On 3 of 4 unseen such drills. |
| **Advanced** | On a **genuine tension or combined failure mode** (consistency vs availability; build-now vs defer; idempotent-but-order-broken), **unaided**: names the tradeoff on both sides, names what breaks first **for each option**, **states the CONDITION under which each wins**, **and** picks one while owning its cost (all three dimensions solid). Articulates the **underlying principle** on a teach-it-back (`drill-generation.md` §6) — "design for the failure and the change you can name; there's no free architecture, only a priced tradeoff" — not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler/combined failure mode → bigger/multi-service surface → harder "it depends" → propose-and-defend → AI-plausible over-built design). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen design drills, never from claimed seniority or "I've
architected big systems." Held-out re-assessment and **real-code transfer** outrank a
same-session streak (`assessment.md` Part 5) — and for the softest judgment module especially,
the real-system signal is weighted heavily (a clean synthetic-drill streak that doesn't show up
when the learner reasons about their *own* architecture is not yet mastery).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Happy-path-only reasoning.** Judging a design by whether it works when everything works,
  and never asking what breaks under failure. The fix: **name the fallacy you're assuming**
  (the network is reliable; the call returns; the message arrives once, in order) and reason
  about the unhappy path — a green demo is one sample, not fault-tolerance.
- **Over-building / resume-driven architecture.** Adding a cache, a queue, a service, or a
  framework for a need that doesn't exist yet, and calling it "scalable." The fix is YAGNI:
  **don't build the presumptive feature** — but **do** leave the cheap seam (hiding a
  likely-to-change decision is not a YAGNI violation). Price the carry cost.
- **Under-building / no seam for the named change.** Hardcoding a decision you *know* will
  change at N sites, so the foreseeable change is a shotgun edit. The fix is the Parnas move
  (D1): **hide the decision likely to change** behind a seam — the dual of over-building, and
  the half YAGNI explicitly *doesn't* forbid.
- **One-right-answer / cargo-culting.** Defending an architecture as "correct" or "best
  practice" with no cost named. The fix: **state the tradeoff** — what it buys, what it costs,
  what breaks first — and the **condition** under which the other choice wins. There is rarely
  one right answer.
- **Cost-blindness.** Counting only what a component buys, never its carry cost or new failure
  mode. The fix: **score both sides** — every interface, cache, and service adds a thing to
  operate and a way to fail.
- **Distributed-by-default / scaling the wrong thing.** Reaching for microservices or sharding
  before the problem requires it, or optimizing a scale that isn't real. The fix: **describe
  the load** (scale of what, to what) before designing for it; distribution is a cost you pay
  only when forced.
- **"It works in the demo" = "it's reliable."** Treating a passing happy-path run as
  fault-tolerance. The fix: **induce the fault** — reason about (or run) the retry, the partial
  failure, the reorder — before believing the design handles it.

**Evidence caveat (this is a `[Practitioner-canon]` module — say so, the loudest of any
module).** E2's grounding is **pure craft**, and it must not be oversold by a single notch:

- The **whole module** is `[Practitioner-canon]`. Kleppmann's three concerns and tradeoff
  method, the fallacies of distributed computing, YAGNI, and Ousterhout's strategic/tactical
  are **respected, widely taught engineering judgment** — vetted against the named sources
  during authoring — **not** empirical findings. Two of the four (Ousterhout, the fallacies)
  are *explicitly* opinion/folklore. The coach says "a respected lens," **never** "research
  shows," and never implies a controlled study ranked these architectures.
- **There is NO empirical half to borrow.** Unlike B3 (a contested TDD layer), D2 (an
  identifier-comprehension layer), or C3 (a concurrency-bug taxonomy), E2 has **no** `[Some
  empirical]` or `[Verified-adjacent]` *content* layer — only craft. The coach must not import
  another module's empirical credibility to dress E2's judgments as science.
- **The fallacies are attributed folklore, not a sourced theorem.** No single canonical primary
  publication exists; the list propagated from Sun Microsystems (Deutsch + Gosling) and is best
  cited via Rotem-Gal-Oz's explanatory essay. The coach presents it as a useful checklist with
  honest provenance, never as a proven law.
- **The runner proves failures, not verdicts.** The one firm thing in this module is that a
  *named failure mode is real* — a retry double-charges, a cache goes stale, an unbounded wait
  hangs. That a given **tradeoff** is the right call is **never** machine-decided; it is the
  rubric-graded judgment, softer than any executable pass in the curriculum.
- **The curriculum-wide transfer caveat applies in full and bites hardest here.** That drilling
  tradeoff-analysis on synthetic systems *causally* improves a given engineer's real designs is
  the open question every module carries — and with no comprehension experiment behind it at
  all, E2 leans entirely on the transfer task (§9), the skill on the learner's **own real
  system**, as the honest individual-level evidence, graded as the soft judgment it is.

No claim in this module is dressed above its badge — and its badge is the most modest in the
curriculum.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real system** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2). For the softest craft module, this is *especially* true — there is no
comprehension experiment standing behind E2, so the learner's real design decision is the
load-bearing evidence.

> **Your turn:** Find a **real design decision** in your own work — one you made recently, one
> a teammate (or an AI assistant) is proposing, or one baked into a system you maintain. Good
> candidates: *should we add a cache / queue / service here? · is this call safe to retry? ·
> should this be one process or two? · should we build this generic now, or hardcode it? · what
> happens to this when the downstream is down?* Pick the smallest decision that actually
> matters.
>
> Now **run the three questions.** **(1) What does it BUY?** Name the concrete benefit, on
> which concern (reliability / scalability / maintainability). **(2) What does it COST?** Name
> the carry cost, the operational cost, and — the one people skip — the **new failure mode** it
> introduces (staleness, redelivery, partial failure, a thing that can now be down). **(3) What
> BREAKS FIRST?** Name the fallacy the current design assumes, and reason about the unhappy
> path: what is the first thing that fails under retry, partial failure, reorder, or load — and
> is that contained, or does it cascade? Then **state your verdict as a tradeoff with a
> condition**: "I'd do X, *because* …; I'd do the opposite *if* …."
>
> Then step back: **was the thing you were tempted to build a presumptive feature?** If you
> can't name a change that is *actually coming*, YAGNI says don't build it — but **do** leave
> the cheap seam. And: **did you reason about the path you're not testing?** If your confidence
> rests on a green demo, you've proven the happy path, not the design.

**Grading is softer and named as such — the softest in the curriculum** (`assessment.md`
Part 4). A real design has no clean answer key; the coach grades against the §7 rubric
(E-tradeoff / E-failure-change / E-honesty) and says: *"this is a design judgment on your real
system, not a machine-verifiable result — and E2 is pure craft, not measured science, so weigh
it accordingly."* Where any sub-claim **is** runnable — the learner claims a call is safe to
retry, or that two shapes behave identically today, or that a wait can hang — the coach still
uses the runner: **reduce the claim to a minimal snippet, run it through `runner.py`, and
confirm the failure is real before the learner leans on it** (the same discipline as §5d, now
on the learner's own design). **Transfer evidence is weighted heavily:** a learner who aces
synthetic tradeoff drills but, on their own system, defends "we added a queue so it scales" with
no cost named and no failure mode reasoned has **not** transferred the skill, and the tracker
notes that gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **rubric + exemplars judgment path**, the executable check on
  failure-mode sub-claims, exercise formats (Generation→Comparison, Debug-this-as-design-review,
  Teach-it-back, Error analysis), Frontier escalation: `references/drill-generation.md` (this
  module instantiates §1 and follows §3, §4, §5; the failure-mode check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder, **surface ground truth** — paste the snippet + output): `references/coaching-loop.md`.
- E2 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-code
  transfer** weighting: `references/assessment.md` (the E2 entry task: a design choice or small
  system + a proposed change — what does it buy, what does it cost, what fails first, would you
  build it; defend the tradeoff, not a "correct" answer).
- Evidence grounding (Kleppmann's *Designing Data-Intensive Applications* on the reading spine
  and in the proposed E2 craft-source subsection; the fallacies of distributed computing —
  Deutsch/Gosling, Rotem-Gal-Oz; YAGNI — Fowler/Beck XP; Ousterhout's strategic-vs-tactical,
  reused from D1a; the worked-examples / expertise-reversal instructional finding):
  `references/evidence-base.md`.
- Soft prerequisite (the module-level version of this judgment): module **D1** (managing
  complexity / abstraction); natural sibling **E1** (you architect what you can comprehend);
  related modules **A1** (execution-model events at system scale), **C3** (partial failure,
  redelivery, order-violation), **E3** (review) and **F1** (calibration — resisting a fluent
  AI-proposed over-build).
- Golden exemplars (~3 per tier, each with a **runner-verified** failure-mode anchor + the
  tradeoff verdict + the named condition): `exemplars/E2/foundations.md`,
  `exemplars/E2/working.md`, `exemplars/E2/advanced.md`.
