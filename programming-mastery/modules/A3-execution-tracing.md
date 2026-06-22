# A3 — Execution Tracing & Explain-in-Plain-English `[Verified]`

> **Module type.** `[Verified]` comprehension module. It teaches the **skill of
> hand-simulating execution** (tracing) and **stating what code does at the level of
> purpose** (explain-in-plain-English / EiPE) — the two intermediate skills that the
> BRACElet studies place *below* code-writing in a developmental hierarchy and that
> together predict a large share of writing ability (`evidence-base.md` → Finding 6).
>
> **Relationship to A1.** A1 teaches the **machine** — the state model (namespace, heap,
> stack, counter) and the transition rule. **A3 teaches the *act of running it by hand,
> on paper, to a recorded answer*, and then *compressing that trace into one sentence of
> intent*.** A1 asks "what is the model?"; A3 asks "can you *operate* it step by step
> without losing state — and can you then say what the whole thing is *for*?" A3
> presupposes A1's model (softly, never as a gate) and points back to it for the
> mechanics; it does not re-teach them.
>
> **Core idea.** Tracing is **keeping an external, written record of state — one row per
> step, in execution order — instead of holding it in your head.** Explaining is the
> inverse compression: having traced the *mechanism*, step back and name the *purpose* in
> one sentence — what the code is *for*, not a line-by-line retelling of how it runs.

---

## 1. Evidence basis `[Verified]`

This module rests on **Finding 6** of `evidence-base.md` — "reading → tracing → writing is
a developmental hierarchy" — which is `[Verified]` there against primary sources, and
draws supporting force from **Finding 4** ("comprehension is active and hypothesis-driven
— *prediction → check*"). Cite via `evidence-base.md`; the anchor sources are the
BRACElet project's reading/tracing/writing studies:

- **Lopez, M., Whalley, J., Robbins, P., & Lister, R. (2008). Relationships between
  reading, tracing and writing skills in introductory programming.** *ICER '08*, 101–112.
  doi:10.1145/1404520.1404531. The keystone result: in combination, **tracing of
  iterative code and "explain in plain English" account for ~46% of the variance in
  code-writing** ability. The study fits a **skill hierarchy** — knowledge of basic
  constructs at the bottom; tracing and explaining as intermediate levels; code-writing
  at the top — via path analysis (polytomous Rasch scaling + stepwise regression) on an
  introductory-Java exam. That is exactly what this module drills: the two intermediate
  skills that gate writing.

- **Lister, R., Fidge, C., & Teague, D. (2009). Further evidence of a relationship
  between explaining, tracing and writing skills in introductory programming.**
  *ITiCSE '09*, 161–165. doi:10.1145/1595496.1562930. A **replication** at a new
  institution, in **Python** (earlier studies used Java), with a **non-parametric**
  analysis. It found that **students who cannot trace code usually cannot explain it**,
  and that students who write reasonably well have *usually* acquired **both** tracing and
  explaining. The contingency data show the relationship is a *soft prerequisite
  ordering*, not a strict gate: among students correct on all tracing tasks, a solid
  fraction wrote well; among students who got *most tracing wrong*, almost none did —
  "most students who scored less than 50% on tracing did poorly on writing." The
  authors are explicit that this supports a *tendency*, not a law (one student wrote
  well despite failing both). This is why A1/A2 are **soft** prerequisites here (§2), not
  gates.

**The Explain-in-Plain-English distinction this module hangs on** is from the same line of
work, framed with the SOLO taxonomy:

- **Whalley, J. L., Lister, R., Thompson, E., Clear, T., Robbins, P., Kumar, P. K. A., &
  Prasad, C. (2006). An Australasian study of reading and comprehension skills in novice
  programmers, using the Bloom and SOLO taxonomies.** *ACE 2006*, CRPIT Vol. 52, 243–252.
  The EiPE task asks the learner to "**in plain English, explain what the following
  segment of code does**." Responses sort on a SOLO scale, and the load-bearing contrast
  for this module is **relational vs. multistructural**: a **relational** answer "provides
  a summary of what the code does in terms of the code's *purpose*"; a **multistructural**
  answer gives "a *line by line* description … of all the code." The sibling study —
  **Lister, Simon, Thompson, Whalley & Prasad (2006), "Not seeing the forest for the
  trees: novice programmers and the SOLO taxonomy," *ITiCSE 2006*** — documents that
  experienced readers summarize at the relational (purpose) level while many novices
  retell line-by-line. **That is the entire thesis of the explain-in-plain-English half of
  this module: a good explanation names the purpose; line-by-line narration is the novice
  signature.** Whalley et al. put the consequence bluntly: "students who cannot read a
  short piece of code and describe it in relational terms are not well equipped
  intellectually to write code of their own."

**Why these license this module.** Finding 6 is confirmed in the evidence base's
fact-checking pass (`evidence-base.md` → Research notes: "Lopez et al. 2008 (BRACElet) —
confirmed"). The verified claim is narrow and exactly what this module teaches: **tracing
and explaining are real, separately-trainable comprehension skills that sit developmentally
below writing and predict it.**

> **Citation precision — one correction, flagged not silently fixed.** Per the standing
> rule (`evidence-base.md` → "cite less, not more; flag, don't inflate"): the evidence
> base's Finding 6 currently notes "R² ≈ 0.66 across the skills" for Lopez et al. 2008.
> The fact-checked primary source supports the **46% combined variance** figure verbatim,
> but **does not state an overall model R² of 0.66** — that value matches the *correlation*
> r = 0.6267 between iterative-tracing and writing in the same paper, which is a different
> quantity. **This module cites only the confirmed 46% figure** and avoids "R² ≈ 0.66."
> See the Report's "new/corrected citations" note. No number is invented here.

**Read through the transfer caveat.** Like all `[Verified]` findings here, the primary
evidence is from **novices in introductory courses** (BRACElet, ~2004–2009, Java/Python).
The *direction* — tracing and explaining are foundations that support writing and
comprehension — is well supported; its causal application to upskilling experienced
engineers is an open question (`evidence-base.md` → transfer caveat). The transfer task
(§9) is the honest test for the individual learner. There is also an **AI-era** reason this
module is in the priority spine: as agents draft most first-pass code, the developer's job
shifts to *verifying code they did not write*, and AI-assisted engineers score measurably
lower on later **unaided** comprehension/debugging (`evidence-base.md` → AI-era impact;
A2/A3 cluster). Tracing by hand is the unaided-comprehension skill that does not atrophy.

---

## 2. Soft prerequisites

**A1 (notional machine) recommended, not required.** Tracing *operates* the state model
A1 teaches — to trace, the learner walks the namespace, heap, call stack, and program
counter that A1 defines. A learner solid on A1 will trace far more easily, and a learner
who traces badly is usually weak on a specific A1 mechanism (most often rebinding-vs-mutation
or the call stack). **A2 (code reading & chunking) is loosely adjacent** — the
*explain-in-plain-English* half is reading *for purpose*, which A2's chunking supports —
but A3 is not gated on A2 either.

Per `assessment.md`, soft prerequisites *inform*, they never *block*: the buffet rule holds
(any learner may open any module at any tier). If a learner is weak on A1, the coach notes
that tracing failures likely trace back to a specific execution-model gap and may pull the
relevant A1 drill — but does **not** forbid them from attempting A3. The BRACElet data
itself (Lister, Fidge & Teague 2009) supports *soft* ordering: tracing tends to precede
writing for most students, but the relationship is a tendency, not a hard prerequisite —
so the coach recommends A1 first, never requires it.

---

## 3. The mental model

**Tracing is hand-simulation with an *external written record*. You do not hold the state
in your head — you write it down, one row per step, in program-counter order, and update
it mechanically. Explaining is the inverse: once the trace shows the mechanism, you step
back and name the *purpose* in one sentence — what the code is *for*, not how each line
moves.**

Two skills, one discipline each.

### 3a. The trace: write the state down, don't hold it

The single highest-value move is **externalizing state onto paper (or a table)** rather
than tracking it mentally. The evidence is direct: students who *sketch a trace* succeed
more on code-reading problems involving loops, arrays, and conditionals, and the sketches
that **track multiple values of the same variable** over time are the ones most correlated
with correct answers (Cunningham, Blanchard, Ericson & Guzdial 2017, replicating the
Leeds Working Group, Lister et al. 2004). The mechanism is **distributed cognition** —
offloading working memory onto the page so it is not the bottleneck.

The trace, concretely:

| For this kind of code | The trace you keep |
|---|---|
| **Straight-line / a loop** | A **state table**: one column per live variable, one **row per statement** in execution order. Each row is the state *after* that statement. (This is A1's §4 state table — A3's contribution is the *discipline of always writing it*.) |
| **A function with calls** | A **call tree** (or call/return list): each call is a node with its **arguments**; each return is the value flowing back **up** to the caller. Trace *into* each call as its own little state table, then bring its return value back to the caller's row. |
| **Recursion** | The **stack of frames** over time: each call **pushes** a frame with its own locals; the base case returns; frames **pop and unwind**, each combining its private locals with the value returned from below. Write the *push* sequence going down and the *return* values coming back up. |
| **A generator** | The **yield sequence with a resume point**: the generator is a **suspended frame**. Each `next()` runs *until the next `yield`*, emits that value, and **freezes** — local state persists across calls. Write what is yielded and where execution paused. |

**The discipline in one line: *write the row, then move the counter.*** The failures in §5
are, almost without exception, failures to *write it down* — the learner tries to hold a
loop's running state in their head and loses a term, or tracks only the *latest* value of a
variable instead of its history, or skips drawing the stack and so cannot say why an inner
call did not clobber an outer one. The fix is never "concentrate harder"; it is "keep the
external record."

### 3b. The explanation: name the purpose, not the lines

Having traced the *mechanism*, the second skill is to **compress it to intent**. A good
explanation is **relational** (SOLO): it states what the code is *for* in a sentence —
"it removes duplicates while keeping first-occurrence order." A weak explanation is
**multistructural**: a line-by-line retelling — "it makes an empty list, then loops, then
checks `if x not in seen`, then appends…" — which re-narrates the trace without ever
saying what the whole thing *accomplishes* (Whalley et al. 2006; Lister et al. 2006).

The test is concrete: **could a teammate who never sees the code reconstruct its job from
your sentence?** "It loops over the list and does stuff with each element" fails (no
purpose). "It returns the running maximum at each position" passes (names the job). The
prompt the coach uses borrows the BRACElet phrasing: *"explain, in plain English, the
**purpose** of this function — do not say how the code works; say what it would be **used
for**."* (Lister, Fidge & Teague 2009.)

**Why both, and in this order.** Tracing without explaining is mechanical bookkeeping that
never abstracts; explaining without tracing is guessing the gist from names (the A1
*superbug* — reading intent instead of executing). The BRACElet hierarchy puts them
*together* below writing precisely because you need the mechanism (trace) **and** the
purpose (explain) before you can reliably *produce* code. Trace first to ground the
explanation in what the machine actually does; explain second to lift it to what the code
is for.

---

## 4. Worked example — a full call-tree trace, then a one-sentence explanation

*(Foundations depth: the complete trace shown, both halves — the call tree **and** the
plain-English compression. This fades by tier — see the note after.)*

The skill is to **trace into the calls** (not skip them), keep the state table, bring each
return value back up, and *then* say what the whole thing is for. Consider:

```python
def double(n):
    return n * 2

def run(xs):
    acc = 0
    for x in xs:
        acc = acc + double(x)
    return acc

print(run([4, 1, 6]))
```

**Step 1 — the call tree (with arguments and returns).** Line 10 calls `run([4, 1, 6])`,
which calls `double` once per loop iteration. Drawn as a tree, each node is a call with its
argument; each `→` is the value returned **up** to the caller:

```
run([4, 1, 6])
├─ double(4) → 8
├─ double(1) → 2
└─ double(6) → 12
   run returns 22
```

**Step 2 — the state table *inside* `run`.** Trace `run`'s frame one row per statement, in
counter order. When the body hits `double(x)`, we **descend** into that call (trivial here
— `return n * 2`), get its return value, and bring it back to this row. Each row is the
state *after* the statement:

| Step | Statement (counter) | `xs` | `x` | `double(x)` returns | `acc` |
|---|---|---|---|---|---|
| 0 | *(frame pushed; arg bound)* | `[4, 1, 6]` | — | — | — |
| 1 | `acc = 0` | `[4, 1, 6]` | — | — | `0` |
| 2 | `for x in xs:` → take `4` | `[4, 1, 6]` | `4` | — | `0` |
| 3 | `acc = acc + double(x)` | `[4, 1, 6]` | `4` | `8` | `8` |
| 4 | `for` → take `1` | `[4, 1, 6]` | `1` | — | `8` |
| 5 | `acc = acc + double(x)` | `[4, 1, 6]` | `1` | `2` | `10` |
| 6 | `for` → take `6` | `[4, 1, 6]` | `6` | — | `10` |
| 7 | `acc = acc + double(x)` | `[4, 1, 6]` | `6` | `12` | `22` |
| 8 | `for` → exhausted | `[4, 1, 6]` | `6` | — | `22` |
| 9 | `return acc` | — | — | — | returns `22`; frame pops |

**Step 3 — verified ground truth** (executable discipline, `drill-generation.md` §2 — the
coach *runs* it, never guesses):

```
stdout: "22\n"
status: ok
```

So the program prints `22`.

**Step 4 — the explanation (relational, one sentence).** Now step back from the rows and
name the *purpose*:

> **"It doubles each number in the list and returns their sum."**

That is a **relational** answer — it states the job. Contrast the **multistructural**
non-answer a line-by-line reading produces: *"it sets `acc` to 0, then for each `x` it
calls `double` and adds the result to `acc`, then returns `acc`."* The second is *true* but
it merely re-narrates the trace; it never says the code computes **the sum of the doubles**.
A teammate can act on the first sentence without seeing the code; they cannot reconstruct
the job from the second.

**What the trace makes visible** (and skipping the calls hides): each `double(x)` is its
**own call** that runs to completion and hands a value back *before* the addition happens —
the loop does not "call double three times in parallel" and it does not inline the
multiplication. Tracking `acc`'s **history** (0 → 8 → 10 → 22), written down, is what keeps
the running sum correct; holding only its *latest* value in your head is exactly the
single-value-tracing error that produces wrong answers on all but the simplest loops (§5).

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a full trace
> *helps novices* (it lowers extraneous load while the schema forms) but becomes
> **redundant load for the more advanced** — they learn more by doing the trace
> themselves. So the coach fades it:
>
> | Tier | Worked-example depth at A3 |
> |---|---|
> | **Foundations** | **Full** — the complete call tree, the complete state table, the verified output, *and* the modeled relational-vs-multistructural explanation, as above. |
> | **Working** | **Partial** — coach draws the call tree and fills the state table through the first call/return, then leaves the remaining rows, the final output, and the one-sentence explanation for the learner. |
> | **Advanced** | **Skeleton** — coach names the columns (the relevant state) or sketches the bare stack/yield shape and hands the learner a blank trace to fill; asks for the final output **and** the purpose sentence with no scaffold. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for A3. Grading mode is
declared up front and is **two-tracked**: traces / outputs / call-trees are **executable
ground truth**; plain-English explanations are **rubric-graded** (§5d).

### 5a. Tier definitions (A3-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. The
A3-specific axis is **what must be traced** and **whether an explanation is also required**.

| Tier | A3 criterion | Example shape |
|---|---|---|
| **Foundations** | Trace **straight-line code or one loop** with a running accumulator (2–3 variables) to the **final state / output**. Keep the state table; report the printed value. No call tree required. | A loop summing a list while tracking the max → final `total, biggest`. The failed-swap-with-temp trace. |
| **Working** | Trace a **function with calls** → produce the **call tree** (arguments + returns) **and** the output; **or** "explain this ~10-line function in **one sentence**" at the *purpose* level. Intermediate state, not just the endpoint. | `sum_of_squares(3,4)` → call tree + `25`. A dedup-preserving-order function → one-sentence purpose. |
| **Advanced** | Trace **recursion or a generator** → produce the **call/stack sequence or yield sequence** **and** the output; **or** explain a **dense** function's intent in one sentence. Combine the trace with naming *why*. | `digit_sum(4821)` → push/return sequence + `15`. A generator consumed by mixed `next()`/`for`. A nested list-comprehension → its purpose. |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success. | — |

A drill is mis-tiered if it requires tracing a structure the tier doesn't include (e.g. a
call tree at Foundations, or recursion at Working); apply the self-check
(`drill-generation.md` §4) and re-level before posing. **Note the deliberate difference
from A1's tiers:** A1 levels by *which execution-model mechanism* is exercised; A3 levels by
*which control structure must be hand-traced* and *whether a purpose-level explanation is
also demanded*. A1 asks "do you know the model?"; A3 asks "can you operate it on paper and
then say what it's for?"

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b,
§4 check 3). The axes for A3:

- **What is traced** — straight-line block · single loop · nested loop · function with one
  call · function calling a helper inside a loop · recursion (linear) · tree recursion ·
  generator / lazy sequence · mutual recursion.
- **Traced artifact (the thing produced)** — final variable value(s) · printed `stdout` ·
  the **call tree** (calls + arguments + returns) · the **stack push/pop sequence** · the
  **yield sequence** (+ resume point) · *whether/where* the trace diverges from a given
  wrong trace.
- **Explanation demand** — none (trace only) · one-sentence purpose (relational) ·
  trace **and** explain · "is this explanation relational or multistructural?" (judge a
  given explanation).
- **Data shape** — short list · string · nested list · numbers feeding arithmetic ·
  generator source.
- **Trap surfaced** — single-value tracing (losing variable history across iterations) ·
  call/return mis-ordering · skipping the stack (recursion) · generator-resume confusion
  (state persists across `next`) · line-by-line (multistructural) explanation where a
  relational one is asked.
- **Format** (`drill-generation.md` §6) — primarily **Trace-the-path** (pause at each step,
  the home format for A3) and **Prediction → Observation → Reflection**; also **Teach-it-back**
  (the EiPE explanation *is* a teach-it-back), **Completion prompts** (hand a partly-filled
  trace table with a gap), and **Error analysis** (give a wrong trace, ask where it
  diverged).

Keep an in-session log of the `(what-is-traced, traced-artifact, explanation-demand,
format)` tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* tracing-and-explaining failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the tracing-pedagogy and SOLO
literature — Lister et al. 2004; Whalley et al. 2006; Lister, Simon et al. 2006; Vainio &
Sajaniemi 2007; Sirkiä & Sorva 2012; Cunningham et al. 2017 — not in trivia. **The root of
the *tracing* errors is one habit: trying to hold state in your head instead of writing it
down, step by step, in execution order. The root of the *explaining* errors is one habit:
re-narrating the lines instead of naming the purpose.**

```
Error: Loses track of a variable's running value across loop iterations — adds into a
       fresh 0 each pass, drops a term, or reports the final value of the wrong variable.
Diagnoses: Not keeping an EXTERNAL state table; trying to hold the accumulator in working
           memory across iterations. The fix is mechanical: one written row per iteration.
           (Cunningham et al. 2017 — blank-paper and incomplete traces have the lowest
           success rate; Lister et al. 2004.)
Example trigger: total=0; biggest=0; for n in [3,8,2,8,5]: total+=n; track the max too —
                 trace BOTH across all five iterations and report total, biggest.

Error: Tracks only the LATEST value a variable has held — keeps one "memory slot" and
       overwrites it — so the trace is right for trivial code but wrong as soon as old
       values are needed.
Diagnoses: "Single-value tracing" — the learner models a variable as one slot showing its
           most recent value and never records its history, so any step that depends on a
           prior state is mis-traced. Low cognitive load, wrong results on all but the
           simplest problems. (Vainio & Sajaniemi 2007; Cunningham et al. 2017.)
Example trigger: a swap via temp (temp=a; a=b; b=temp) — predict a, b. Or any running
                 accumulator where the previous value feeds the next.

Error: When tracing a function with calls, skips INTO the call — guesses what the call
       returns from its name, or mis-orders call and return (uses a return value before the
       call has "finished").
Diagnoses: No call/return model in the trace — treats a call as an inline lookup rather than
           a sub-computation that must run to completion and hand a value BACK before the
           caller's statement proceeds. The trace has no node for the callee. (Sirkiä &
           Sorva 2012 — function-call/parameter simulation is a documented mistake cluster.)
Example trigger: sum_of_squares(a,b) = square(a)+square(b) — draw the call tree with each
                 call's argument and return, then the output.

Error: Cannot produce the frame-by-frame state of a recursive call — assumes one shared set
       of locals across calls, so an inner call appears to clobber the outer call's
       variables; or cannot say why the recursion terminates / how values combine on the
       way back up.
Diagnoses: Skips the STACK — no model of one independent frame per call that pushes on call
           and pops on return, each with its own locals, combining its private value with
           the value returned from the frame below. (A1 §3 call stack; Sirkiä & Sorva 2012.)
Example trigger: digit_sum(n)= n<10 ? n : n%10 + digit_sum(n//10) — write the push sequence
                 down to the base case and the return values coming back up; give the output.

Error: Traces a generator as if it ran to completion at creation, or re-runs it from the
       start on the second consumption, or forgets that local state persists between
       `next()` calls.
Diagnoses: No "suspended frame / resume point" model of a generator — treats it as an eager
           list or a function restarted each call, instead of a frozen frame that runs to the
           next `yield`, emits, and pauses with its locals intact. (A1 §5c generators;
           generator data model.)
Example trigger: g=countdown(3); next(g); next(g); then `for x in g: print(x)` — give the
                 full output (it does NOT restart; it resumes from where it paused).

Error: Asked to "explain what this does," gives a LINE-BY-LINE retelling ("makes an empty
       list, then loops, then checks `if`, then appends…") and never states the purpose.
Diagnoses: A MULTISTRUCTURAL explanation where a RELATIONAL one is required — enumerates the
           parts without relating them to the whole; describes the mechanism, not the job.
           The novice signature on EiPE tasks. (Whalley et al. 2006; Lister, Simon et al.
           2006 — "Not seeing the forest for the trees.")
Example trigger: the dedup-preserving-order function — ask for the purpose in ONE sentence;
                 a relational answer says "removes duplicates, keeping first-occurrence order."

Error: "Explains" by reading the names and intent instead of tracing — reports what the
       code looks like it's "trying to do" without ever simulating it, and so misses
       behavior that diverges from the names.
Diagnoses: Reading for intent instead of executing — the A1 superbug surfacing as a tracing
           failure. The explanation is ungrounded because no trace backs it. (Pea 1986;
           A1 anti-patterns §8.) Trace FIRST, then explain.
Example trigger: any function whose name or surface reading misleads (e.g. a "sort" that
                 actually dedups) — require a trace before the one-sentence explanation.

Error: Gets the FINAL output right but the intermediate states wrong (or unwritten) — backs
       into the endpoint, or pattern-matches the answer, without a correct step-by-step
       trace.
Diagnoses: Endpoint-only "tracing" — tracing and explaining sit below writing precisely
           because the INTERMEDIATE state is the skill; a right endpoint with wrong/absent
           intermediate states is not yet solid (it is often luck or recognition). Record
           which step the trace diverged. (`evidence-base.md` Finding 6; assessment.md A3.)
Example trigger: any loop/recursion drill — require the per-step table, not just the final
                 printed value; grade the row where it first goes wrong.
```

### 5d. Grading mode

**Two-tracked, declared up front** (`drill-generation.md` §1d):

- **Traces, outputs, and call-trees → executable ground truth** (`drill-generation.md` §2).
  Every trace/output/call-tree drill has a computable answer: the coach **runs the snippet**
  via `python <skill-dir>/runtime/python/runner.py snippet.py`, parses the `RunResult`
  JSON, and grades the predicted output against `stdout` (strip the trailing newline before
  comparing to a bare prediction) and/or `status`. For the *intermediate* trace (the
  per-step state table, the call tree, the push/pop or yield sequence), the coach derives
  ground truth from the same run — the printed final value plus, where useful, an
  instrumented version (adding `print` statements at each step, or running sub-expressions)
  to confirm the intermediate rows. The coach **never guesses** the output or the trace.

- **Plain-English explanations → rubric-graded** (`drill-generation.md` §3, and the rubric
  in §7). An EiPE answer has no single machine-checkable string; the coach grades it against
  a small rubric and the golden exemplars (`exemplars/A3/*`). **The rubric (3 binary
  criteria):** (a) **Relational, not multistructural** — names the *purpose* / what the code
  is *for*, rather than retelling it line by line; (b) **Accurate** — the stated purpose
  matches what the code (when run) actually does, with no false implication; (c)
  **Appropriately concise** — one sentence that a teammate could act on without seeing the
  code. The coach states out loud: "this explanation is a judgment call graded against the
  module's rubric, not a machine-verifiable answer." To keep (b) honest, the coach **runs
  the underlying code** before grading the explanation, so the "accurate" criterion is
  checked against real behavior, not the coach's reading.

Most A3 drills are **hybrid** (`drill-generation.md` §3): the *output / trace* is
executable-graded and the *explanation* is rubric-graded. Report the two verdicts
**separately** — a correct output with a multistructural (line-by-line) explanation, or a
correct endpoint with a wrong intermediate trace, is a **partial pass** and is flagged as
such (it commonly reflects recognition or luck, not durable tracing skill;
`evidence-base.md` → illusions of fluency; Finding 6 — the intermediate state *is* the
skill).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = trace one non-trivial structure (single recursion or a generator) in
  isolation, or explain one dense function.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  structural complication to *trace* OR raises one parameter-space dimension one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for A3, with step counts:

1. **Deeper / branching call structure** (push the "what is traced" dimension):
   - Frontier-1: **tree recursion** — trace the full call tree of `fib(5)` (both branches at
     each node, the order they evaluate, the values combining up) — Advanced linear recursion
     + 1 branching increment.
   - Frontier-2: **mutual recursion** (e.g. `is_even`/`is_odd`) — two interleaving frame
     types on the stack (+ 1).
   - Frontier-3: recursion that **also threads an accumulator down** the stack vs. combining
     on the way up — trace both styles of the same function and contrast (+ 1).

2. **Lazy-evaluation pipelines** (push the generator dimension): a generator consumed
   partly by `next()` then finished by a `for`; a chain (`map` over a `filter` over a
   generator) traced for *which element forces which stage*; the difference between a
   generator object and a generator *factory*. Each is one increment over the plain
   generator.

3. **Explanation under load** (push the explanation-demand dimension): explain a function
   whose *name misleads* (a "sort" that dedups) — the learner must trace to discover the
   real purpose, then state it relationally; or compress a 15–20-line function with two
   responsibilities into one sentence that names the *primary* job. One increment each.

4. **Trace divergence / error analysis**: give the learner a *plausible but wrong* trace of
   a snippet and ask them to find the exact row where it first diverges from the real
   execution (run it to confirm). One increment; pushes from *producing* a trace to
   *auditing* one — the AI-era verification move.

5. **Interleavings → hand off to A4.** Tracing a *single* instruction stream is A3. Once
   that is solid, tracing *multiple interleaved* streams (threads, happens-before,
   nondeterministic schedules) is a different machine — escalate into **A4 (concurrency
   mental models)** rather than stretching A3.

Track the level as `A3: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2. Two
cross-cutting requirements apply at every tier above Foundations: **product *and* process**
(the right final value/output *and* a correct **intermediate** trace — and, where an
explanation is asked, a **relational** one; a right endpoint with a wrong/absent
intermediate trace, or a multistructural explanation, is a Foundations-level pass at best),
and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for A3 |
|---|---|
| **Foundations** | Correctly traces a **single loop with a running accumulator** (2–3 variables) and predicts the **final value/output** — *with the per-step state table written out*, not just the endpoint (e.g. `total, biggest` over a 5-element list; or the failed-swap-with-temp). Allowed *with* the worked example faded to one missing row. The signature pass is a **complete intermediate trace**, not a lucky endpoint. |
| **Working** | On **unseen drills**, **unaided**: (a) traces a **function with calls** — produces a correct **call tree** (each call's arguments and return) **and** the output, with correct intermediate `acc`/state rows; **and** (b) explains a ~10-line function's **purpose in one relational sentence** (names the job — e.g. "removes duplicates, keeping first-occurrence order" — not a line-by-line retelling). Distinguishes a relational from a multistructural explanation when shown both. |
| **Advanced** | On a **recursive or generator** snippet, produces the **stack push/return sequence** (or **yield sequence with resume point**) **and** the output, unaided, **and explains why** — names why each recursive frame keeps its own locals and how values combine on unwind, or why a generator resumes rather than restarts. Compresses a **dense** function (nested comprehension, misleading name) to its purpose in one sentence. Articulates the underlying principle on a teach-it-back (`drill-generation.md` §6), not just the instance. |
| **Frontier** | `Frontier-N`: presses one structural step past the last comfortable success per §6 / `drill-generation.md` §5 (e.g. linear recursion → tree recursion → mutual recursion → auditing a wrong trace for the divergence row). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen drills — specifically from the **intermediate trace
and the relational explanation**, not the endpoint alone, and never from claimed seniority.
Held-out re-assessment and real-code transfer outrank a same-session streak
(`assessment.md` Part 5). This product-*and*-process bar is doing real work here: Finding 6's
whole point is that the *intermediate* trace and the *purpose-level* explanation — not the
final answer — are the skills that predict writing.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Tracing in your head.** Holding the running state mentally across iterations instead of
  writing one row per step — the source of lost terms, dropped state, and wrong loop
  results. The fix is not concentration; it is the **external written trace**. Students who
  sketch the trace succeed more, and the sketches tracking *multiple values over time* are
  the ones that correlate with correct answers (Cunningham et al. 2017). *Write the row,
  then move the counter.*
- **Single-value tracing.** Keeping only a variable's *latest* value — one overwritten slot
  — instead of its **history**. Cheap, and wrong on anything past the trivial (Vainio &
  Sajaniemi 2007). A variable's *prior* values are part of the state; record them.
- **Skipping the call / skipping the stack.** Treating a function call as an inline name
  lookup rather than a sub-computation traced to completion, or reasoning about recursion
  as one shared set of locals. Trace **into** each call (a node in the call tree); for
  recursion, draw the **stack of frames** pushing down and the return values coming back up.
- **Explaining line-by-line instead of by purpose.** Re-narrating the statements ("makes a
  list, then loops, then checks…") instead of naming what the code is **for** — a
  *multistructural* answer where a *relational* one is the skill (Whalley et al. 2006;
  Lister et al. 2006). The test: could a teammate act on your sentence without the code?
- **Explaining without tracing (reading intent).** Guessing the purpose from names and
  surface shape without simulating — the A1 *superbug* in tracing clothes (Pea 1986).
  **Trace first, then explain**, so the explanation is grounded in what the machine does,
  not what the names suggest.

**Evidence caveat (minimal — this is a pure `[Verified]` module).** Finding 6 (reading →
tracing → writing) is `[Verified]` and well supported, so this module carries **no inflated
claims to walk back** — with one citation-precision note already made in §1 (the
evidence base's "R² ≈ 0.66" for Lopez et al. 2008 is not in the primary source; this module
cites only the confirmed 46% combined-variance figure). Two honest boundaries remain. First,
the curriculum-wide **transfer caveat** (`evidence-base.md`): the BRACElet evidence is from
*novices in introductory courses* (Java/Python, ~2004–2009); that explicitly drilling
tracing and explaining *causally* improves *experienced* engineers is an open empirical
question — the coach leans on the transfer task (§9). Second, BRACElet establishes a
**correlational hierarchy and a soft prerequisite ordering**, *not* a proof that tracing
*causes* writing ability; Lister, Fidge & Teague (2009) are explicit that the relationship
is a tendency with exceptions. The coach states tracing/explaining as **strongly associated
with, and developmentally prior to, writing** — not as a guaranteed causal lever. No
`[Practitioner-canon]` or extrapolated claims are made in this module.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2).

> **Your turn:** Find a function in **your own codebase** that you *did not write* (or wrote
> long enough ago that it's unfamiliar) — ideally one a coding agent generated, or one you
> reviewed without fully tracing. Pick the smallest non-trivial one with a loop, a call, or
> recursion.
>
> Do **both halves**:
> 1. **Trace it by hand** — keep a written state table (variables per step), draw the call
>    tree or stack if it calls out / recurses, and predict the output for one concrete
>    input. *Then run it* (reduce it to a runnable snippet if needed) and check your trace
>    against reality — **find the row where they diverge**, if any.
> 2. **Explain it in one sentence** — state the function's *purpose*, not its mechanics. Do
>    not say how it works; say what it would be **used for**. Then ask: could a teammate act
>    on that sentence without reading the code?

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean
answer key; the coach grades the trace and the explanation against the §7 rubric and says:
*"this is a judgment call on your real code, not a machine-verifiable result."* Where the
learner's code (or a reduced version) **is runnable**, the coach still uses the runner for
the executable sub-claims — confirm the predicted output, and verify the *purpose* sentence
against actual behavior — before discussing it. **Transfer evidence is weighted heavily:** a
learner who passes generated drills but cannot trace a real function to a verified output,
or cannot state its purpose relationally, has not yet transferred the skill — the tracker
notes that gap as more diagnostic than another passed synthetic drill. This task is also the
**AI-era** move in miniature: tracing and explaining code *you did not write* is precisely
the verification skill that AI-assisted work erodes (`evidence-base.md` → AI-era impact).

---

## Cross-references

- Drill mechanics, exercise formats (esp. **Trace-the-path** and **Teach-it-back**),
  executable ground-truth protocol, Frontier escalation: `references/drill-generation.md`
  (this module instantiates §1 and follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder): `references/coaching-loop.md`.
- Entry task (the A3 trace-and-explain task), per-skill routing, mastery-rubric shape,
  held-out re-assessment, transfer weighting: `references/assessment.md` (A3 entry task — a
  loop/recursion trace **plus** a one-sentence explanation; "a correct 3-iteration loop
  trace → at least Working; a correct recursive call-tree trace → Advanced").
- The **state model A3 operates** (namespace, heap, call stack, program counter; the
  transition rule; the superbug): `modules/A1-notional-machine.md` (A3 traces A1's machine —
  it does not re-teach it). Reading *for purpose* (the explain half) is supported by
  chunking in `modules/A2-*` (loose adjacency).
- Evidence grounding (Finding 6 — reading → tracing → writing; Lopez et al. 2008; Lister,
  Fidge & Teague 2009; Whalley et al. 2006; the SOLO relational/multistructural distinction;
  Finding 4 — comprehension as prediction → check; the transfer caveat; the AI-era
  comprehension-atrophy finding): `references/evidence-base.md`.
- Golden exemplars (~3 per tier, traces runner-verified, explanations with gold + rubric):
  `exemplars/A3/foundations.md`, `exemplars/A3/working.md`, `exemplars/A3/advanced.md`.
