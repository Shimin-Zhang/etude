# D4 — Performance & Mechanical Sympathy `[Practitioner-canon]`

> **Module type.** Mixed-status by design, and **the most extrapolation-heavy module in the
> curriculum**. The honest prose badge is **`[Some empirical]` (the cost-of-guessing /
> measure-first observation) + `[Practitioner-canon]` (Big-O cost models, "profile before you
> optimize") + extrapolation (the hardware / mechanical-sympathy layer)**. There is a real
> empirical core — Knuth's own report that *programmers' intuitive guesses about where the time
> goes fail* — and a large body of respected craft (asymptotic cost models; "measure, don't
> guess"); but the cache-line / branch-prediction / memory-hierarchy material, while genuinely
> load-bearing in systems / HFT / game-engine work, is **overstated for typical application
> code** and is flagged as extrapolation throughout. The validator badge on this file is
> `[Practitioner-canon]`; the coach must never present the canon or the extrapolation as verified
> science.
>
> **Core idea.** *Reason about cost before you change anything, then measure before you optimize.*
> The first-order model of "what will scale" is **asymptotic complexity (Big-O)** — it tells you
> which work *grows* with the input and which is a constant you can ignore. The first-order rule
> of "what to actually speed up" is **profile, don't guess** — developer intuition about the
> hotspot is documented (by Knuth himself) to be unreliable. Everything below that — what an
> individual operation costs on real hardware ("mechanical sympathy") — matters *sometimes*, but
> for most code the **algorithm and the I/O dominate**, and cache-level reasoning is usually
> premature.

---

## 1. Evidence basis `[Some empirical]` + `[Practitioner-canon]` + extrapolation

This module is **mixed-status** and **heavily extrapolated**, and saying so plainly is the whole
job (`evidence-base.md` → badge rules; transfer caveat). Four pillars, in descending order of
evidential strength.

**(a) The empirical core — programmers' intuition about the bottleneck is unreliable; measure.
`[Some empirical]`.** Cite via `evidence-base.md` → *Performance & mechanical sympathy (module
D4)* (proposed addition). The primary source is the same 1974 Knuth paper that gave us the famous
aphorism, and the *measurement* claim is the part most people forget. In **Knuth, D. E. (1974),
"Structured Programming with `go to` Statements," *ACM Computing Surveys* 6(4):261–301, on
p. 268** — in the same passage as "premature optimization is the root of all evil," a few
sentences later (just past the "critical 3%" qualifier; see the full passage in (b)) — Knuth
writes (verified verbatim against the primary source during authoring):

> "It is often a mistake to make *a priori* judgments about what parts of a program are really
> critical, since the universal experience of programmers who have been using measurement tools
> has been that their intuitive guesses fail."

This is not folklore restated — it is the originator's **report of the universal experience with
measurement tools**: guesses about the hot path are wrong often enough that you must *measure*.
It is badged `[Some empirical]` rather than `[Verified]` because it is one expert's reported
experience from 1974, not a controlled replicated study — but it is a genuine empirical
observation, not a prescription, and it is the empirical anchor for this module's "profile, don't
guess" discipline.

**(b) The famous quote, IN CONTEXT — `[Practitioner-canon]`, and routinely misquoted.** The
single most-abused sentence in our field. The full passage (Knuth 1974, p. 268, verified verbatim
against the primary source):

> "Programmers waste enormous amounts of time thinking about, or worrying about, the speed of
> *noncritical* parts of their programs … We should forget about small efficiencies, say about
> 97% of the time: **premature optimization is the root of all evil.** Yet **we should not pass
> up our opportunities in that critical 3%.** A good programmer will not be lulled into
> complacency by such reasoning, he will be wise to look carefully at the critical code; but only
> after that code has been identified."

Three things the popular misquote drops, all of which this module restores:
- The quote **preserves the critical 3%.** It does **not** mean "never optimize." It means
  *don't* optimize the 97% that doesn't matter, *and do* optimize the 3% that does — **once it's
  been identified** (by measurement; see (a)).
- The sentence Knuth wrote *just before* this passage is an argument **against** blanket
  "ignore efficiency" advice: "a 12% improvement, easily obtained, is never considered marginal
  [in established engineering disciplines]." Knuth is not anti-optimization; he is anti-*premature*
  optimization, which is a precise and different thing.
- It is sometimes called **"Hoare's dictum"** — Knuth himself attributed it to C. A. R. Hoare in
  1989 ("The Errors of TeX"), but that attribution is **doubtful** and the verifiable
  origin-of-record is Knuth 1974. (A variant of the aphorism — "premature optimization is the root
  of all evil (or at least most of it) in programming" — also appears in Knuth's 1974 Turing Award
  lecture, "Computer Programming as an Art," *CACM* 17(12):667–673, on p. 670.) Cite Knuth 1974 as
  origin; do not assert the Hoare attribution as fact.

**(c) Big-O cost models — math + canon `[Practitioner-canon]`.** Asymptotic complexity is
**mathematics**, not an empirical finding about programmers — `O(n log n)` *is* the worst-case
comparison count of a comparison sort, by proof, not by survey. What is *canon* (respected
practice, not measured causation) is the **engineering doctrine built on top of it**: that
asymptotic class is the right first-order model of "what scales," that you should know the cost of
the data-structure operations you use (list-membership is O(n), set-membership is O(1) average,
list-front-insert is O(n), `dict`/`set` lookup is O(1) average), and that an **algorithmic** change
usually dwarfs any **micro**-optimization. The math is exact; the doctrine of *how to apply it in
practice* is craft. Grounded against the standard algorithms canon during authoring (CLRS for the
asymptotic definitions; the CPython time-complexity reference for the per-operation costs —
`evidence-base.md` → proposed D4 addition).

**(d) Mechanical sympathy — `[Practitioner-canon]` + EXTRAPOLATION; the honesty fault line.** The
term comes from racing (the driver's feel for the car) and was **popularized for software by
Martin Thompson** (the *Mechanical Sympathy* blog; the LMAX Disruptor). The idea: code that works
*with* the machine — cache lines, the memory hierarchy, branch prediction, allocation cost,
contiguous vs. pointer-chasing layout — can be dramatically faster than code that fights it.
**This is real** — in high-frequency trading, game engines, database internals, and tight
numerical kernels it is decisive (the Disruptor's reported latency advantage over a queue — from
its authors and practitioner write-ups, *not* an independent controlled study — is the canonical
demonstration). **But for typical application code it is overstated**, and this module
says so in every section: the dominant costs in ordinary code are **algorithmic complexity** (the
O(n²) you didn't notice) and **I/O** (network, disk, database round-trips, serialization), each of
which is *orders of magnitude* larger than a cache miss. Reaching for cache-line reasoning before
you have (i) fixed the algorithm and (ii) *measured* that you are CPU- and memory-bound on a hot
path is itself a form of premature optimization. The hardware layer is taught here as **a real
thing that is usually the wrong first move** — `[Practitioner-canon]` for the systems contexts
where it bites, **extrapolation** for the claim that it matters to the median program.

**Why these license this module.** (a) grounds *measure, don't guess*; (b) grounds *don't optimize
the 97%, do optimize the identified 3%*; (c) grounds *reason about asymptotic cost first, and
prefer algorithmic fixes*; (d) grounds *the hardware matters in specific domains and is usually
premature elsewhere*. The combined discipline: **reason about cost (Big-O) before you change
anything; measure to find the real 3%; fix the algorithm or the I/O first; and treat
cache-level mechanical sympathy as a specialist tool, not a default.**

**Read through the transfer caveat.** Knuth 1974 is a single expert's report, not a replicated
study; Big-O is exact math whose *practical application* is craft; mechanical sympathy is craft
that is genuinely domain-dependent and extrapolated for general code. None of this is the
`[Verified]` novice-comprehension literature. The *directions* are well grounded; that drilling
cost-reasoning and measurement discipline *causally* improves a given engineer's real
performance work is the open question every module here carries (`evidence-base.md` → transfer
caveat). The transfer task (§9) — a real slow path in the learner's own system — is the honest
individual-level test.

---

## 2. Soft prerequisites

**A1 (notional machine) is the load-bearing prerequisite — this module extends it *downward*.**
A1 teaches *what the machine does* to program state, step by step; D4 attaches a **cost** to each
of those steps and asks *how the total grows with the input*. A `+=` on a list is an A1 event
(in-place mutate then rebind); D4 adds that `list.insert(0, x)` is that event repeated with an
**O(n) shift** hidden inside it. A learner who cannot yet trace *what* a loop does (A1/A3) cannot
reason about *how much* it costs, because the cost is a function of the trace. Concretely: the
"count the operations" discipline below **is** A1 tracing with a counter attached.

**B3 (testing & correctness) and the curriculum-wide rule "correct first, then fast" tie in
directly.** Performance work is **behavior-preserving change under a cost constraint** — the same
shape as refactoring (D3), but the invariant is "same outputs, fewer operations." A faster
function that returns wrong answers is not an optimization; it is a regression. So D4 assumes you
can *say what correct means* (B3) and *confirm behavior is preserved* across the change. The
worked example and several drills check the optimized version against the naive one for **identical
output** before crediting any speedup — a fast wrong answer is the most common self-inflicted
performance "win."

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at D4 because they can't trace the
loop, the coach notes the gap likely traces to A1/A3 and *suggests* shoring those up — but does
not forbid D4. Related: **C1/C3** (debugging) share D4's "measure / instrument before you act"
stance; a profiler is to performance what a hypothesis-and-test loop is to a bug.

---

## 3. The mental model

**Performance is a cost question, answered in two passes. First pass — *asymptotics*: of all the
work this code does, which part *grows with the input*? That's the only part that scales; constants
and one-off costs are noise at large n. Second pass — *measurement*: once you have a candidate hot
path, do not trust your intuition about it — measure, because the universal experience is that the
guess is wrong. Optimize only the part that is both (a) growing and (b) measured to dominate.**

Four levels of cost, coarsest first. The discipline is to work them **in order** and stop as soon
as you've solved the problem — most problems are solved at level 1 or 2.

| Level | What it is | When it dominates | Typical magnitude |
|---|---|---|---|
| **1. Algorithmic complexity (Big-O)** | How the operation count *grows* with input size: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ). The first-order model of "what scales." | Almost always the first thing that matters at scale. An O(n²) where O(n) was possible is the single most common real performance bug. | An O(n²)→O(n) fix at n=10⁴ is a ~10,000× reduction in operations. |
| **2. I/O and external work** | Network round-trips, disk, database queries, serialization, process/lock contention. Often *not visible* in the CPU profile of your function. | Dominates most *application* code. One avoidable database round-trip in a loop (the "N+1 query") swamps any in-process optimization. | A network call is ~10⁵–10⁶× a memory access; an avoided round-trip beats any cache tuning. |
| **3. Constant factors / interpreter overhead** | The fixed cost per operation: Python-level loop overhead vs. a C-implemented builtin (`sum`, `set`, `str.join`), attribute lookups, allocation churn. | After the algorithm and I/O are right, on a hot path that is genuinely CPU-bound. | Using `set` membership or `''.join` vs. a Python loop: often 2–50×, **but it does not change the cost class.** |
| **4. Mechanical sympathy (hardware)** | Cache lines, memory hierarchy, branch prediction, contiguous vs. pointer-chasing layout, allocation locality. | Systems / HFT / game / numeric kernels. **Usually premature for ordinary application code** (and largely invisible in interpreted Python). | Decisive in the right domain (the Disruptor); typically a rounding error next to levels 1–2 for typical code. |

**The transition rule for *deciding*** (not for executing — that's A1): given slow code, ask the
levels in order. *Is the algorithm super-linear when it needn't be? (level 1) → Is it doing
avoidable I/O? (level 2) → Is the hot path measured and CPU-bound, with a cheaper constant-factor
form? (level 3) → Only then, in a domain where it matters, is it fighting the hardware? (level 4).*
Most real wins are level 1 and level 2. **Skipping to level 3 or 4 before measuring is exactly the
premature optimization Knuth warned about.**

**The discipline in one line: *reason about cost before you change anything; measure before you
optimize; fix the biggest-growing thing first.*** The machine has no "make it fast" button and your
intuition about the hot path is, per Knuth's own report, probably wrong — so you *reason* about
what grows, then *measure* to confirm where the time actually goes, then change the **one** thing
that dominates.

Three corollaries the module drills:

1. **Asymptotic class beats constant factors, and a micro-optimization rarely changes the class.**
   "Tightening the inner loop" of an O(n²) algorithm leaves it O(n²); switching the data structure
   to make the inner operation O(1) is what changes the class. Reach for the *algorithm* before the
   *micro-tweak*. (Worked example; drills throughout.)
2. **Don't guess the bottleneck — profile it.** The visibly-complex code (the string formatting,
   the math) is usually *not* the cost; the innocuous-looking line (the membership scan, the
   front-insert, the N+1 query) usually is. Knuth's "intuitive guesses fail." Use a profiler /
   operation count, not a hunch.
3. **Correct first, then fast — and prove the speedup preserved behavior.** Optimization is
   behavior-preserving change under a cost constraint (ties B3, D3). Confirm the fast version
   produces the *same outputs* as the correct one; a fast wrong answer is a regression dressed as
   a win.

---

## 4. Worked example — same task, two cost classes (and how we know)

*(Foundations depth: every step shown, with runner-verified operation counts. This fades by tier —
see the note after.)*

The skill is to **reason about cost, then confirm by measuring** rather than eyeballing speed.
Consider a function that detects whether a list has any duplicate — written the "obvious" way:

```python
def has_dupes(items):
    seen = []
    for x in items:
        if x in seen:        # <-- x in <list> scans seen: O(len(seen))
            return True
        seen.append(x)
    return False
```

**Step 1 — Reason about the cost (level 1, before touching anything).** The outer loop runs n
times. The line `if x in seen` is the trap: membership in a **list** is a linear scan, so on the
k-th iteration it does up to k comparisons. Summing 0 + 1 + 2 + … + (n−1) gives **≈ n²/2
comparisons** in the worst case (all-distinct input). That is **O(n²)**. The fix is not to tighten
the loop — it is to change `seen` to a **set**, whose membership is O(1) average, making the whole
thing **O(n)**:

```python
def has_dupes_fast(items):
    seen = set()
    for x in items:
        if x in seen:        # x in <set>: O(1) average
            return True
        seen.add(x)
    return False
```

**Step 2 — Confirm by counting operations (don't trust the eyeball).** We instrument each version
to count the dominant operation — list comparisons vs. set probes — and run it across growing n.
This is the operation-counting discipline: a deterministic stdout number, not a noisy wall-clock.

**Verified ground truth** (the coach *runs* it — `drill-generation.md` §2 — never guesses). Counts
of list comparisons for the O(n²) version, on all-distinct input (worst case):

```
n=10:   45 comparisons
n=100:  4950 comparisons
n=1000: 499500 comparisons
```

Counts of set probes for the O(n) version, same inputs:

```
n=10:   10 set-probes
n=100:  100 set-probes
n=1000: 1000 set-probes
```

**Step 3 — Read the growth, not the absolute number.** From n=100 to n=1000 (10× the input): the
list version went 4,950 → 499,500, a **~100× jump** — that's the quadratic signature (10× input →
100× work). The set version went 100 → 1,000, a **10× jump** — linear (10× input → 10× work). At
n=1000 the list version does **499,500** comparisons to the set version's **1,000** — a ~500×
gap, and it *widens* with n. The fix was a one-line data-structure change, and it changed the cost
*class*, not just a constant.

**Step 4 — Confirm behavior is preserved (correct first, then fast).** Both versions must return
the *same* answer on every input, or the "speedup" is a bug. The coach re-runs both on the same
inputs (with and without a duplicate) and confirms identical output before crediting the change —
verified:

```
has_dupes([1,2,3,2])      -> True    has_dupes_fast([1,2,3,2])      -> True
has_dupes([1,2,3,4])      -> False   has_dupes_fast([1,2,3,4])      -> False
status: ok (both)
```

**What the example makes visible** (and an eyeball-the-code skim hides): the cost lived in an
*innocuous-looking* line (`x in seen`), not in anything that reads as "expensive." Reasoning about
*what grows* found it; the operation count *confirmed* it without trusting a wall-clock; and the
fix was algorithmic (change the structure), not a micro-tweak. Note what we did **not** do: we did
not reach for `__slots__`, cache-line packing, or rewriting in C — those are levels 3–4, and the
problem was solved at level 1.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> cost analysis helps **novices** (it shows the two-pass move) but is **redundant load for the
> more advanced**, who learn more by doing the analysis themselves. So the coach fades it:
>
> | Tier | Worked-example depth at D4 |
> |---|---|
> | **Foundations** | **Full** — the complete cost reasoning + the runner-verified operation counts + the growth read + the behavior check, every step shown. |
> | **Working** | **Partial** — coach states the cost class of the naive version and shows *one* version's counts, leaving the learner to predict the other's growth and name the fix. |
> | **Advanced** | **Skeleton** — coach hands over the slow function only; learner identifies the dominating level, predicts the growth, proposes the fix, and says how they'd confirm it (op-count / profile) and that behavior is preserved. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for D4. Grading mode is
declared up front: **hybrid** (§5d) — the *cost/scaling claim* is executable via **TIMEOUT status**
and **operation counts** (deterministic), the *Big-O reasoning and the "which level / what to do"
judgment* is rubric-graded. Precise wall-clock (`duration_s`) is **noisy in the sandbox and is not
used as ground truth** — only timeout-status and op-counts are.

### 5a. Tier definitions (D4-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module:

| Tier | D4 criterion | Example shape |
|---|---|---|
| **Foundations** | One cost mechanism on a familiar surface: name the **Big-O** of a single loop / nested loop / single data-structure operation, OR predict the **growth** (how op-count changes when n doubles), OR predict that a naive snippet will **time out** vs. complete. One concept, computable answer. | Nested loop over n → predict O(n²); predict the all-pairs op-count doubles to ~4× when n doubles; predict naive `fib(40)` times out. |
| **Working** | Apply cost reasoning in a context the learner hasn't seen, where the cost is **non-obvious**: spot the hidden super-linear operation (list-membership in a loop, `insert(0,...)`, repeated `list += ` / string `+=`, an N+1-shaped pattern), name the level it lives at, and name the fix. Intuition and reality diverge. | A pipeline whose "heavy-looking" stage is O(n) and whose innocuous stage is O(n²); identify the real cost and the one-line fix. |
| **Advanced** | **Combine** two or more of: cost reasoning + measurement strategy + behavior-preservation + the level hierarchy. Given slow code, decide *which level* dominates, justify *why* a proposed optimization does or doesn't change the cost class, and say how you'd *confirm* it without trusting a wall-clock. Includes recognizing when an optimization is **premature** (level 3/4 before measuring). | "Here are two proposed fixes (a micro-tweak and an algorithm change) — which actually helps, why, and how would you prove it?"; or "is reaching for `__slots__` here justified or premature?" |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations drill secretly needs the level-hierarchy judgment (that's
Working/Advanced), or a Working drill's hidden cost is actually obvious on a skim (that's
Foundations). Apply the self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for D4:

- **Cost class in play** — O(1) · O(log n) · O(n) · O(n log n) · O(n²) · O(2ⁿ)/exponential ·
  amortized-O(1)-with-a-trap (e.g. `list.insert(0,...)` is O(n)).
- **Where the cost hides** — a visible nested loop · membership-in-a-list inside a loop ·
  front-insert / repeated concatenation building a result · a recomputation that could be cached ·
  an exponential recursion without memoization · an I/O-shaped pattern (N+1 / per-item round-trip,
  posed as reading) · a "looks expensive but is O(n)" decoy stage.
- **The level it lives at** (the judgment axis) — level 1 algorithmic · level 2 I/O · level 3
  constant-factor/interpreter · level 4 hardware (and recognizing when 3/4 is *premature*).
- **Executable signal used** — **TIMEOUT status** (naive snippet blows the ~5s limit) ·
  **operation count** (instrumented counter → deterministic stdout) · **growth ratio** (count at
  n vs. 2n) · **behavior-preservation** (naive vs. optimized produce identical output).
- **What the learner must produce** — name the Big-O · predict the growth/ratio · predict
  timeout-vs-completes · spot the hidden cost + name the fix · decide which proposed fix helps and
  *why* · judge premature-vs-justified · teach-back the level hierarchy.
- **Format** (`drill-generation.md` §6) — **Debug-this** ("this is too slow — why, and what's the
  fix?") as the home format; also **Prediction → Observation → Reflection** (predict the op-count
  / timeout, then run), **Generation → Comparison** (propose an optimization, compare to the
  gold), **Error analysis** ("someone optimized this — did it help?"), and **Teach-it-back** (the
  level hierarchy / why premature optimization is a trap).

Keep an in-session log of the `(cost class, where-it-hides, level, executable signal, format)`
tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* cost-reasoning errors, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). Grounded in the cost-model canon and Knuth's measurement
observation (`evidence-base.md` → proposed D4 addition), not trivia. **The root of most of them is
one inversion: optimizing what is *easy to see or fun to tweak* (the inner-loop micro-detail, the
clever bit-trick) instead of what *grows or dominates* (the asymptotic class, the I/O) — and doing
it *before measuring*, on a hunch the originator of the aphorism told us is usually wrong.**

```
Error: Optimizes a constant factor while leaving the cost class unchanged — "tightens" the
       inner loop, inlines a call, swaps a method, but the algorithm stays O(n^2).
Diagnoses: Confuses constant-factor tuning (level 3) with algorithmic change (level 1). Does not
           see that asymptotic class, not the micro-detail, governs scaling. (Big-O canon;
           corollary 1.)
Example trigger: a quadratic dup-check "optimized" with a local-variable inner loop vs. switched
                 to a set — op-counts show the micro version is still ~n^2/2, the set is n.

Error: Guesses the bottleneck from reading the code and optimizes the visibly-complex part —
       rewrites the string formatting / the math, ignores the innocuous membership scan or
       front-insert that actually dominates.
Diagnoses: Trusts intuition about the hot path instead of measuring. The exact failure Knuth
           reported: "intuitive guesses fail." Did not profile / count. (Knuth 1974; corollary 2.)
Example trigger: a two-stage pipeline where the "heavy-looking" format stage is O(n) and the
                 "innocuous" dedup stage is O(n^2); op-counts settle it (~999x in favor of dedup).

Error: Reads "premature optimization is the root of all evil" as "never optimize / optimization
       is bad," and refuses to fix even an identified, measured, hot O(n^2).
Diagnoses: Dropped the "critical 3%." Took the aphorism as anti-optimization rather than
           anti-PREMATURE-optimization. (Knuth 1974, in context — the quote PRESERVES the 3%.)
Example trigger: a learner who, shown a profiled hot quadratic, says "optimizing is premature"
                 even though it's been identified by measurement — the precise case Knuth says to fix.

Error: Reaches for hardware / mechanical-sympathy reasoning (cache lines, __slots__, struct
       packing, rewrite-in-C) before checking the algorithm or measuring.
Diagnoses: Jumped to level 4/3 before level 1/2. Mechanical sympathy is real in its domains but
           is premature here; the algorithm or the I/O is almost certainly the lever. (Level
           hierarchy; honesty fault line in §1d.)
Example trigger: "make this Python loop faster with __slots__/numpy" when the loop is O(n^2) and
                 the real fix is a set / a better algorithm.

Error: Ignores I/O — micro-optimizes in-process CPU while the function makes a network/DB call
       per item (an N+1 pattern), which dominates by orders of magnitude.
Diagnoses: Missed level 2. Optimized the cheap thing (CPU) and left the expensive thing (round
           trips) untouched. (Level hierarchy; corollary 2.)
Example trigger: a loop that does one lookup per item described as "slow" — the fix is to batch
                 the I/O, not to speed up the loop body.

Error: Confuses an amortized- or average-case cost with the per-operation worst case — assumes
       list.insert(0, x), "x in list", or building a string with += is "basically free."
Diagnoses: No model of the per-operation cost of the data structure. insert(0,...) and
           list-membership are O(n); repeated str += is O(n^2) overall. (CPython complexity
           reference; corollary 1.)
Example trigger: build a list with insert(0, x) in a loop -> op-count of element shifts is ~n^2/2;
                 compare to append (amortized O(1)).

Error: Asserts a speedup with no measurement, or "confirms" it by a single wall-clock run.
Diagnoses: Used a noisy, one-sample wall-clock as proof (especially unreliable in the sandbox),
           instead of an operation count / growth ratio / a profile across sizes. (Measurement
           discipline; corollary 2; runner constraint.)
Example trigger: "I made it faster" claimed from one timing; the coach shows the op-count is
                 unchanged (the class didn't change) and the timing was noise.

Error: "Optimizes" by changing behavior — drops a case, loosens a check, returns an approximation
       — and counts it as a performance win.
Diagnoses: Broke "correct first, then fast." A faster function that returns different outputs is
           a regression, not an optimization. (Ties B3/D3; corollary 3.)
Example trigger: a "fast" dedup that uses a set but loses first-seen order the spec requires —
                 faster AND wrong; behavior-preservation check catches it.

Error: Picks the asymptotically-better algorithm for tiny, fixed, or rarely-run inputs where the
       constant factor or simplicity matters more.
Diagnoses: Over-applies Big-O where n is small/bounded — asymptotics describe LARGE n; for n=5 the
           simpler O(n^2) may be faster and clearer. (Big-O is a large-n model; nuance, not a
           license to ignore it.)
Example trigger: replacing a 5-element linear scan with a heavyweight indexed structure "for
                 performance" — premature complexity for no scaling benefit.
```

### 5d. Grading mode

**Hybrid** (`drill-generation.md` §1d, §3) — and the executable half must be used **carefully**,
per the runner constraints. The coach grades a D4 drill like this:

1. **Cost/scaling claim — executable, via timeout-status and operation counts (NOT wall-clock).**
   - For "does this scale / is it pathological?" drills: the coach **runs** the naive snippet via
     `python <skill-dir>/runtime/python/runner.py snippet.py` and uses the **`status`** field — a
     naive exponential (e.g. `fib(40)`) returns `status: "timeout"`, which *is* the demonstration
     of pathological cost. (Respect the sandbox: ~5s timeout, 256 MB RLIMIT_AS — design drills so
     the naive version times out or so the counts are modest; avoid huge allocations / many
     threads.)
   - For "how much does it cost / how does it grow?" drills: the coach runs an **instrumented**
     version that prints a **deterministic operation count** (a counter incremented in the hot
     line), at two or three input sizes, and grades the learner's predicted count / growth ratio
     against the real stdout.
   - **Do not use `duration_s` as ground truth.** Wall-clock is noisy in the sandbox (cross-run
     jitter; the runner itself reports it as indicative). The coach may *mention* a duration as a
     qualitative aside ("it visibly hung, then timed out") but grades on **status** and **counts**.
   - **Surface the run** (`coaching-loop.md` → surface ground truth): paste the snippet and its
     real `status` / counted stdout into the reply — an unseen run reads as a guessed key.
2. **Behavior-preservation — executable.** When a drill proposes an optimization, the coach runs
   **both** the naive and the optimized version on the same inputs and confirms **identical
   output** before crediting the speedup. If the "optimization" changes output, that is the
   finding (corollary 3) — show it.
3. **Big-O reasoning and the level/what-to-do judgment — rubric + exemplars (§7).** *Did they name
   the right cost class? Identify the level that dominates? Justify why a fix does/doesn't change
   the class? Recognize premature optimization? Insist on measurement?* Each is a 3-point
   criterion (§7), graded explicitly. Compare to the tier golds in `exemplars/D4/<tier>.md`.
4. **Name it as partly soft.** The coach says out loud: "the **cost number / timeout is
   machine-verified**; the **Big-O reasoning and the call about what to do are a judgment graded
   against the rubric + exemplars**, not a single machine-checkable answer" (`drill-generation.md`
   §3). Report the verdicts **separately**: a learner who correctly predicts the op-count
   (executable: yes) but **micro-optimizes instead of fixing the class** (rubric: wrong level) is a
   **partial pass**, and the coach flags exactly that — predicting-the-cost without
   knowing-what-to-do is the central D4 gap.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses the
desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = given slow code, identify the dominating level, justify why a fix changes (or
  doesn't change) the cost class, and say how you'd confirm it — one such combination in isolation.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new dimension of
  difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for D4, with step counts:

1. **Subtler / more-hidden cost** (push the where-it-hides axis): from a hidden O(n²) membership →
   to a recomputation that wants memoization (Frontier-1) → to an exponential recursion that needs
   restructuring, not just caching (Frontier-2) → to a cost that only appears at a *specific input
   distribution* (e.g. quadratic only on sorted / adversarial input; hash collisions degrading
   O(1) to O(n)) (Frontier-3). Each is one increment.

2. **Up the level hierarchy** (push the level axis): from a level-1 algorithmic fix → to a level-2
   I/O fix (recognize the N+1 / per-item round-trip and batch it; reason about why one round-trip
   dwarfs the loop) → to a level-3 constant-factor call that is *justified because measured* (and
   articulating why it's not premature) → to a level-4 mechanical-sympathy case **with the honesty
   judgment attached**: is cache/layout reasoning warranted *here*, or premature? Each is one
   increment; the level-4 step is two (one for the hardware reasoning, one for "and you must judge
   whether it's premature").

3. **Measurement under noise** (push the executable-signal axis): from "predict the op-count" → to
   "design the measurement" (what would you count / profile, at what sizes, to distinguish two
   hypotheses about the bottleneck?) → to reasoning about why a single wall-clock is untrustworthy
   and what a *growth ratio* or a *profile across sizes* shows that one timing can't. Each is one
   increment.

4. **Tradeoff under tension** (push the what-to-produce axis): the asymptotically-better option is
   *not* obviously the right call — small/bounded n where the constant factor wins; a
   memory-vs-time tradeoff (a cache that speeds reads but risks staleness / unbounded growth); a
   readability-vs-speed tradeoff on a path that *isn't* hot. The learner must hold "fix the
   biggest-growing thing" **and** "don't add complexity the measurement doesn't justify" at once.
   One increment.

5. **Optimize AI-generated code → the AI-era frontier.** A function an agent produced that *reads*
   fluently and idiomatically but carries a plausible-surface cost bug — a hidden O(n²), an N+1, a
   needless recomputation — exactly the kind of defect that survives a skim of confident-looking
   code (ties E3 review and F1 calibration). One increment for "AI-plausible surface," another for
   "and you must measure rather than trust the fluency."

Track the level as `D4: Frontier-N`. Reset condition: two consecutive failures at the same level →
drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the three D4 dimensions. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (named the right cost *and* reasoned about it correctly — a
right Big-O with a hand-wavy or wrong "why," or a correct op-count with the wrong call about what
to do, is a Foundations-level pass at best), and **unaided + durable** (a same-session streak is
provisional until a delayed re-assessment or the real-code transfer task confirms it;
`assessment.md` Parts 3–5).

**The three scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Cost (did they get the asymptotic / measured cost right?).** Correct Big-O class, or
  correct predicted op-count / growth ratio / timeout-vs-completes. *(Executable sub-claim: the
  count/timeout is machine-verified; §5d.)*
- **D2 — Diagnosis (judgment).** Did they identify the **level** that dominates and the **hidden**
  cost — not a decoy, not the visibly-complex-but-cheap part — and resist optimizing what doesn't
  matter (premature level 3/4; tiny-n over-engineering)?
- **D3 — Action + verification (judgment).** Did they propose a fix that actually changes the
  dominating cost (usually algorithmic / I/O), say how they'd **confirm** it (op-count / profile,
  not a single wall-clock), and ensure **behavior is preserved**?

| Tier | Observable bar for D4 |
|---|---|
| **Foundations** | On a single-mechanism snippet, **names the Big-O correctly and says why** — e.g. "nested loop over n → O(n²) because the inner loop runs n times for each of n outer iterations," or predicts that naive `fib(40)` **times out** because each call spawns two, so calls grow ~2ⁿ. D1 solid; D2 at least partial (points at *what* grows). Allowed *with* the worked example faded to one missing step. |
| **Working** | On a snippet with a **non-obvious** cost, **unaided**: finds the hidden super-linear operation (D1 — names its class), identifies the **level** it lives at and that the visibly-complex part is *not* the cost (D2), **and** names the fix that changes the class (D3). On 3 of 4 unseen drills. Optimizes the decoy / micro-tweaks the wrong thing ⇒ partial pass, flagged. |
| **Advanced** | On slow code, **unaided**: decides which **level** dominates and justifies it (D2), **justifies why** a proposed fix does or doesn't change the cost class (D1+D3), says how they'd **confirm** without trusting a wall-clock and that **behavior is preserved** (D3), **and** correctly calls out a **premature** optimization (reaching for level 3/4 before measuring, or Big-O for tiny n). Articulates the **level hierarchy** on a teach-it-back (`drill-generation.md` §6) — "reason about what grows, measure, fix the biggest thing first; the easy-to-tweak detail is rarely the one that matters" — not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler hidden cost → up the level hierarchy → measurement under noise → tradeoff under tension → AI-generated code). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier from
what the learner *does* on unseen drills, never from "I optimize code all the time." Held-out
re-assessment and **real-code transfer** outrank a same-session streak (`assessment.md` Part 5) —
and because the executable half here is deliberately limited (timeout + counts, not precise
timing), the real-code signal (a profiled real slow path) is weighted heavily: a clean
synthetic-drill streak that doesn't show up when the learner profiles their own system is not yet
mastery.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Micro-optimizing the cost class away.** Tightening the inner loop, swapping a method, inlining
  — while the algorithm stays O(n²). The fix: change the *algorithm / data structure* so the
  dominating operation gets cheaper (the inner op O(n)→O(1)); the class is what scales, not the
  constant.
- **Guessing the bottleneck.** Optimizing the visibly-complex part on a hunch. The fix is the
  measurement Knuth prescribed: **profile / count operations** — the innocuous line (membership
  scan, front-insert, N+1 query) is usually the real cost, and "intuitive guesses fail."
- **"Never optimize."** Reading the aphorism as anti-optimization and refusing to fix even an
  identified, measured hot path. The fix: restore the **critical 3%** — *don't* optimize the 97%,
  *do* optimize the 3% once measurement identifies it.
- **Premature mechanical sympathy.** Reaching for cache lines / `__slots__` / a C rewrite before
  checking the algorithm or measuring. The fix: work the levels in order — algorithm, I/O, then
  (only if measured CPU-bound on a hot path, in a domain where it bites) the hardware.
- **Ignoring I/O.** Micro-optimizing CPU while the function does a round-trip per item. The fix:
  find level 2 first — batch the I/O; one avoided round-trip beats any in-process tuning.
- **"Faster" without measuring or without preserving behavior.** Claiming a win from one noisy
  wall-clock, or "optimizing" by quietly dropping a case. The fix: confirm with an op-count /
  growth ratio across sizes, and confirm the outputs are **identical** to the correct version.

**Evidence caveat (this is the most extrapolation-heavy module — say so loudly).** D4 mixes four
evidential statuses and the coach must keep them apart:

- The **measure-don't-guess** core is **`[Some empirical]`** — Knuth's *reported universal
  experience* that intuitive guesses about the bottleneck fail (Knuth 1974, p. 268). A genuine
  empirical observation, but **one expert's report from 1974, not a replicated controlled study**.
  State it as "Knuth reported, and it's widely echoed," not "studies prove."
- **Big-O** is **exact mathematics**; the **engineering doctrine** built on it ("asymptotic class
  is the right first model," "prefer algorithmic fixes," "know your data-structure costs") is
  **`[Practitioner-canon]`** — respected, near-universal craft, vetted against the algorithms
  canon, **not** a measured causal result about programmers. The coach says "respected practice on
  an exact mathematical foundation," not "research shows."
- **Mechanical sympathy** (level 4) is **`[Practitioner-canon]` in its domains + EXTRAPOLATION for
  general code.** It is *real and decisive* in HFT / game engines / DB internals / numeric kernels
  (the Disruptor is the canonical demonstration), and **overstated for typical application code**,
  where the algorithm and I/O dominate and cache reasoning is usually premature (and largely
  invisible in interpreted Python). The coach must say plainly: *for most code, fix the algorithm
  and the I/O; cache-line reasoning is a specialist tool, not a default.* Never present level-4
  reasoning as the first move or as generally-applicable verified fact.
- The **curriculum-wide transfer caveat** applies in full: that drilling cost-reasoning and
  measurement on synthetic snippets *causally* improves a given engineer's real performance work
  is the open question. The coach leans on the transfer task (§9) — a **real** slow path — as the
  honest individual-level evidence, and grades it as the soft judgment it is.

Nothing in this module is dressed above its badge; in particular, the hardware layer is never sold
as more than the domain-specific, frequently-premature tool it is.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to a real
slow path** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat, consequence 2).

> **Your turn:** Find a piece of **your own code** that is — or that you suspect is — too slow: a
> request that lags, a script that crawls on big inputs, a job that grew with the data. Pick the
> smallest such piece you can isolate.
>
> Now **run the two passes.** **(1) Reason about cost first:** before changing anything, write down
> what work *grows with the input* and your best guess at the dominating **level** (algorithm? an
> I/O round-trip? a constant factor? — almost never the hardware). **(2) Then measure — do not
> trust the guess.** Profile it (`cProfile`, a timer around the suspected region, or an operation
> count on the hot line) at **two or more input sizes**, so you see the *growth*, not one number.
> Compare what the measurement says to what you guessed. **Was the bottleneck the part you
> expected, or the innocuous line?** (If they differ, you've just lived Knuth's "intuitive guesses
> fail.") Then make **one** change at the dominating level, re-measure to confirm the cost actually
> dropped, and confirm the output is **identical** to before — correct first, then fast.
>
> Finally, step back: did you fix what *grows* (the algorithm / the I/O), or did you reach for a
> micro-tweak or a hardware trick? If the latter, and you hadn't measured it as the bottleneck,
> that was premature — re-aim at the biggest-growing thing.

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean answer
key; the coach grades against the §7 rubric (D1 cost / D2 diagnosis / D3 action+verification) and
says: *"this is a judgment call on your real code, not a machine-verifiable result."* Where any
sub-claim **is** runnable — the learner suspects a hot path — the coach still uses the runner:
**reduce the suspected slow operation to a minimal snippet, count its operations at two sizes (or
show it times out), and confirm the growth before the learner asserts it** (the same discipline as
the §5d op-count check, now on the learner's real find), and confirm the optimized version's output
matches the original. **Transfer evidence is weighted heavily:** a learner who aces synthetic
op-count drills but, on real code, micro-optimizes a cold path, "confirms" a speedup from one noisy
timing, or breaks behavior chasing speed has **not** transferred the skill, and the tracker notes
that gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **hybrid grading path** (executable timeout/op-count + rubric reasoning),
  the behavior-preservation check, exercise formats (Debug-this, Prediction→Observation→Reflection,
  Error analysis, Teach-it-back), Frontier escalation: `references/drill-generation.md` (this
  module instantiates §1 and follows §2, §3, §4, §5; the executable checks use §2 with the
  timeout/op-count discipline of §5d).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, **surface the run** so
  the op-count/timeout is visible, direct feedback, scaffolding ladder): `references/coaching-loop.md`.
- D4 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-code
  transfer** weighting: `references/assessment.md` (the D4 entry task: a slow snippet — name the
  cost class, locate the real bottleneck, say what you'd change and how you'd measure it).
- Evidence grounding (Knuth 1974 "premature optimization" *in context* + the measurement
  observation; Big-O cost-model canon; mechanical sympathy / Martin Thompson, badged as
  canon-plus-extrapolation): `references/evidence-base.md` → *Performance & mechanical sympathy
  (module D4)* (proposed addition).
- Soft prerequisites (the execution model the cost attaches to; correct-before-fast): modules
  **A1** (notional machine), **B3** (testing & correctness); related measurement-discipline
  modules **C1/C3** (systematic / production debugging).
- Golden exemplars (~3 per tier, each with a **runner-verified** timeout-or-op-count key +
  behavior check + reasoning gold): `exemplars/D4/foundations.md`, `exemplars/D4/working.md`,
  `exemplars/D4/advanced.md`.
