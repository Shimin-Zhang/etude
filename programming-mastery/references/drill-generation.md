# Drill Generation — Mechanics & Format Catalog

How the coach generates fresh drills, obtains ground truth, grades attempts, and
escalates difficulty. Delivery discipline (pause rules, scaffolding ladder, feedback
tone) lives in `coaching-loop.md` — this file does not duplicate those rules; it
references them.

> **Attribution.** The exercise-format catalog in §6 is adapted from Cat Hicks'
> *Learning Opportunities* (CC-BY 4.0, <https://drcathicks.com>), which also informs
> several technique names and descriptions throughout. Adapted, not reproduced verbatim.

---

## §1 — Generation-spec format (what every module must supply)

Each module file must contain a **drill-generation spec** block that gives the coach
everything needed to produce a fresh, correctly leveled drill without rereading the
entire module on every turn. The spec has four required parts:

### 1a. Tier definitions

For this module, what separates a Foundations drill from a Working drill from an
Advanced drill? The tier names are fixed curriculum-wide:

| Tier | Cognitive demand | Default worked-example depth |
|---|---|---|
| **Foundations** | Core mechanics, single concept, familiar surface | Full: every step shown and explained |
| **Working** | Apply in a context the learner hasn't seen before | Partial: one step left for learner to predict |
| **Advanced** | Transfer, adapt, combine two or more concepts | Skeleton: learner fills in the reasoning |
| **Frontier** | At or past the learner's demonstrated ceiling | None: go straight to the problem |

Each module spec translates these into *module-specific* criteria. For example, in
module A1 (notional machine / execution model):

- **Foundations** — single variable, one assignment, predict the final value.
- **Working** — a loop with a running accumulator; trace the state across three
  iterations.
- **Advanced** — a function call with mutable default argument; predict both the
  return value and the side effect on subsequent calls.
- **Frontier** — see §5 (Frontier escalation).

### 1b. Parameter space

The dimensions the coach varies to produce non-repeating drills. Every module spec
enumerates the axes it controls; the coach must pick different points on each axis
across successive drills to avoid mode-collapse.

Typical axes (module-specific content will differ):

- **Construct** — which language feature is exercised (e.g., slice, list-comp,
  generator, decorator).
- **Context** — how the construct appears (standalone, inside a function, inside a
  class, in a callback).
- **Data shape** — empty, single-element, nested, large.
- **Error type** — off-by-one, name collision, mutable default, wrong operator.
- **Format** — which exercise type from §6 (Prediction → Observation → Reflection vs.
  Debug-this vs. Teach-it-back, etc.).

The coach keeps a short in-session log of which (construct, context, data shape,
format) tuples have been used and avoids repeating a combination until all others
have been exercised.

### 1c. Common-error catalog

A catalog of the *specific* conceptual errors learners make in this module, each
paired with a diagnosis label. This is what lets the coach name the gap precisely in
Step 5 (Diagnose) rather than saying "incorrect."

Format per entry:

```
Error: <what the learner does / predicts incorrectly>
Diagnoses: <what conceptual gap this reveals>
Example trigger: <a drill that surfaces it>
```

Example entries for module A1 (notional machine):

```
Error: Predicts that reassigning a variable changes all names that previously
       pointed to it.
Diagnoses: Learner has a "copy-on-assign" model rather than a name-binding model;
           does not distinguish rebinding from mutation.
Example trigger: x = [1,2,3]; y = x; x = [4,5,6]; predict y.

Error: Does not account for short-circuit evaluation in a compound boolean.
Diagnoses: Learner models boolean expressions as always evaluating both operands;
           has not internalized Python's left-to-right short-circuit rule.
Example trigger: def f(): ... ; True or f() — predict how many times f runs.

Error: Predicts that a mutable default argument is re-initialized each call.
Diagnoses: Learner models default arguments as evaluated at call time rather than
           definition time; misunderstands where default values live.
Example trigger: def append_to(x, lst=[]): lst.append(x); return lst
                 — predict append_to(1) then append_to(2).
```

### 1d. Grading mode

Each module spec declares whether its drills have an **executable ground truth** or
require a **rubric judgment**. Most drills in Tracks A–C (notional machine, code
reading, tracing, debugging) are executable. Most drills in Tracks D–F (design,
naming, review, calibration) require rubric judgment.

A single drill may be **hybrid**: its output prediction is executable-graded; its
explanation of *why* is rubric-graded.

---

## §2 — Executable ground-truth protocol

For any drill whose answer is computable, the coach **never guesses** the output.
The protocol is:

1. Write the snippet.
2. Run it via the runner.
3. Parse the `RunResult` JSON.
4. Grade the learner's prediction against `stdout` (and/or `status`, if the drill is
   about whether an error occurs).

### Runner API

```python
# programming-mastery/runtime/python/runner.py

def run_snippet(code: str, *, timeout_s: float = 5.0, mem_mb: int = 256) -> RunResult:
    ...

@dataclasses.dataclass
class RunResult:
    status: str        # "ok" | "timeout" | "error"
    stdout: str
    stderr: str
    returncode: int | None
    duration_s: float
```

**Programmatic use** (from within the skill's Python code):

```python
from runtime.python.runner import run_snippet

result = run_snippet(code, timeout_s=5.0, mem_mb=256)
# result.status  → "ok" | "timeout" | "error"
# result.stdout  → captured standard output (string)
# result.stderr  → captured standard error (string)
# result.returncode → process exit code, or None on timeout
# result.duration_s → wall time in seconds
```

**CLI use** (the coach's primary grading path):

```
python <skill-dir>/runtime/python/runner.py <script.py>
```

Prints a single-line JSON object matching `RunResult` fields. The skill-relative path
is key: resolve `runner.py` against the directory containing `SKILL.md`, not the
learner's working directory. From `SKILL.md`:

> *"Resolve `runtime/python/runner.py` against THIS skill's own directory (the folder
> containing this SKILL.md), not the learner's working directory."*

Example if the skill is installed at `~/.claude/skills/programming-mastery/`:

```bash
python ~/.claude/skills/programming-mastery/runtime/python/runner.py snippet.py
```

**Security note.** The runner is a robustness sandbox (timeout + address-space/CPU
limits), not a security boundary against deliberately hostile code. It catches
runaway loops and memory blowups; it does not isolate against crafted exploits.
Container-level isolation is planned future work.

### Worked example end-to-end

**Module A1, Foundations — "what does this print?" notional-machine drill.**

**Step 1 — Coach writes the snippet.**

```python
x = 10
y = x
x = x + 1
print(y)
```

**Step 2 — Coach poses the drill (generate-before-reveal; see `coaching-loop.md`
Step 4 for the hard-stop rule).**

> **Your turn:** What does this snippet print?
>
> (Take your best guess — wrong attempts are useful data.)

*[Message ends. Coach waits.]*

**Step 3 — Learner responds.** Suppose the learner says: `11`.

**Step 4 — Coach runs the snippet to obtain ground truth.**

The coach writes `snippet.py` with the above code, then runs:

```bash
python ~/.claude/skills/programming-mastery/runtime/python/runner.py snippet.py
```

Runner output (JSON on stdout):

```json
{
  "status": "ok",
  "stdout": "10\n",
  "stderr": "",
  "returncode": 0,
  "duration_s": 0.031
}
```

**Step 5 — Coach parses and grades.**

`result.status == "ok"` and `result.stdout == "10\n"`.
Learner predicted `11`; actual output is `10`.

**Step 6 — Coach names the specific gap (not "incorrect").**

From the common-error catalog:

> *Error:* predicts that reassigning `x` changes `y`.
> *Diagnoses:* learner has not built the name-binding model; they believe `y = x`
> creates a persistent link between the two names rather than copying the *current
> value* of `x` into `y` at the moment of assignment.

Coach feedback (following `coaching-loop.md` Step 6 — blunt, no false credit):

> "That's wrong. The output is `10`, not `11`.
>
> In Python, `y = x` copies the *current value* of `x` (which is `10`) into `y` at
> that instant. When line 3 rebinds `x` to `11`, `y` is unaffected — it still holds
> `10`. The two names are independent after the assignment; there is no persistent
> link. This is the name-binding model: assignment binds a name to a value, not to
> another name."

### RunResult field usage guide

| Field | Use in grading |
|---|---|
| `status` | Primary gate: if `"error"` when the learner predicted normal output, or `"ok"` when the learner predicted an exception, that *itself* is a finding. |
| `stdout` | Compare against the learner's predicted output. Strip trailing newline from `stdout` before comparing to a bare learner prediction (e.g., `"10\n"` vs `"10"`). |
| `stderr` | Examine when `status == "error"` — the traceback names the exception class and line. Use this to produce a precise diagnosis. |
| `returncode` | Secondary signal; `0` on clean exit, nonzero on error (Python exits with `1` on unhandled exception). |
| `duration_s` | Flag to the learner if notably slow (e.g., >1 s on a tiny snippet) — a teaching moment about complexity or accidental O(n²) behavior. |
| `"timeout"` status | Diagnoses infinite loops, unbounded recursion, or unexpectedly large input. Use as a teaching moment about termination conditions. |

### Grading a "will this raise?" drill

Some drills ask the learner to predict whether a snippet raises an exception (and if
so, which one). Grade by:

1. Check `result.status`:
   - `"ok"` → no exception raised.
   - `"error"` → an exception raised; read `result.stderr` for the type and message.
2. Compare `result.status` and exception type (if applicable) to learner's prediction.
3. Diagnosis is in the common-error catalog under the relevant error class.

---

## §3 — Rubric + exemplars path (judgment drills)

Drills in Tracks D–F and many Advanced/Frontier drills in other tracks have no
executable ground truth. Examples: naming a function, reviewing a design for
abstraction quality, assessing whether a refactor is behavior-preserving, rating
one's own confidence level.

**Grading path:**

1. Each module supplies a **rubric** — a small set of binary or 3-point criteria.
   Example for a naming drill: (a) does the name reveal intent without implementation
   detail? (b) is it accurate — no false implication? (c) is it appropriately
   concise?
2. Each module supplies **golden exemplars** — at least one strong and one weak
   example per tier, stored in `exemplars/<ID>/<tier>/`. The coach compares the
   learner's response to these.
3. The coach grades the rubric criteria explicitly, one by one, and cites which
   exemplar the learner's response is closest to.
4. This is explicitly softer than executable grading. The coach states:
   "This is a judgment call graded against the module's rubric — not a
   machine-verifiable answer."

**Do not conflate rubric quality with executable correctness.** A learner can pass a
rubric drill by producing a plausible answer; that is different from being provably
right. Treat rubric passes as softer evidence; executable passes as harder evidence.

**Hybrid drills.** When a drill has both a computable part and a judgment part (e.g.,
"what does this print AND why does it work that way?"), grade the computable part via
the runner first. Then apply the rubric to the explanation. Report both verdicts
separately.

---

## §4 — Generation self-check

Before showing a drill to the learner, the coach runs this four-question check:

1. **Known/derivable answer?**
   - For executable drills: can the runner be run on this snippet without error?
     If the snippet itself has a syntax error or depends on unavailable imports, fix
     it before posing it.
   - For judgment drills: does the rubric have criteria that apply to this exact
     prompt? If not, refine the prompt until it fits the rubric.

2. **Correctly tier-leveled?**
   - Does the cognitive demand match the learner's current tier per the module's
     tier definitions (§1a)?
   - A Foundations drill that accidentally requires two-concept transfer is mislabeled
     Working or Advanced. Adjust or discard it.

3. **New region of the parameter space?**
   - Compare to the in-session log of (construct, context, data shape, format) tuples
     already used.
   - If this drill is a minor rewording of a recent one, choose a different axis to
     vary. Repetition within a session does not produce the interleaving benefit.
   - Exception: a deliberate *retrieval check-in* at session start intentionally
     repeats a prior topic from a *previous* session (spaced review).

4. **Single main question?**
   - Each drill should have exactly one primary thing to predict, generate, or judge.
     If you find yourself asking two things, split into two drills.

If the drill fails any check, revise it before posing it.

---

## §5 — Frontier escalation

Frontier is not a fixed tier — it is a *moving target* tracking the learner's
demonstrated ceiling.

**Tracking the ceiling.** After each drill, record:

- Did the learner pass on the first attempt? (ceiling not yet found)
- Did the learner fail, then pass after one retry? (ceiling found; escalate one step)
- Did the learner fail on retry? (ceiling found; hold here and scaffold the setup per
  `coaching-loop.md` Step 7)

**Escalation mechanics.** At Frontier, the coach picks a drill that presses *one
step* past the last comfortable success along one parameter axis. Not two steps —
one. Escalating too fast collapses to failure; escalating too slowly loses the
desirable-difficulty benefit (`evidence-base.md` → desirable difficulties).

Example escalation path in module A1 (notional machine):

1. Advanced ceiling: mutable default argument (one function call).
2. Frontier +1: mutable default argument + aliasing across two function calls.
3. Frontier +2: mutable default + aliasing + closure capture in the same snippet.
4. Frontier +3: the above, but with a decorator that wraps the function.

**Tracking.** Record the frontier level in the learner's tracker as:
`Frontier-N` where N is the step above Advanced. Example: `A1: Frontier-2`.

**Reset condition.** If the learner fails two consecutive Frontier drills at the same
level, move back to Advanced for one drill, then re-approach. The demonstrated ceiling
is not a permanent verdict — it shifts with practice and spacing.

---

## §6 — Exercise-format catalog

These formats are **orthogonal to modules** — any format can be applied to any
module's content. The coach varies format across drills to produce the interleaving
benefit and avoid overtraining a single response type.

> **Attribution.** The six named formats below are adapted from Cat Hicks' *Learning
> Opportunities* (CC-BY 4.0, <https://drcathicks.com>). The additional techniques
> section draws on the same source for nomenclature; all are adapted, not verbatim.

### 6.1 — Named exercise formats

**Prediction → Observation → Reflection**
- What it is: Learner predicts what code will do; the runner reveals actual behavior;
  learner reflects on what matched or surprised them.
- When to use: Any executable drill where the interesting learning is in the *gap*
  between mental model and reality. The primary format for notional-machine drills
  (module A1). Most generative for wrong predictions — they expose the exact model
  boundary.

**Generation → Comparison**
- What it is: Learner sketches or writes a solution before seeing any implementation;
  coach reveals the canonical answer; learner compares and reasons about divergences.
- When to use: Working and Advanced tiers, especially for code-writing and design
  drills (modules B1, B2, D1). Drives the generation effect even when the learner's
  attempt is partially wrong.

**Trace-the-path**
- What it is: Coach sets up a concrete scenario with specific values; at each
  execution step, coach pauses and asks what the state is now (stack frame, variable
  value, branch taken). The learner steps through the execution manually.
- When to use: Tracing drills (module A3), debugging drills (module C1). The pause
  at each step (not just the final output) is what builds a step-by-step execution
  model. Particularly valuable for loops and recursive calls.

**Debug-this**
- What it is: Coach presents a snippet with a plausible bug or edge-case failure.
  Learner identifies what would go wrong and why, then proposes a fix.
- When to use: Debugging modules (C1, C3), code-review modules (D4). Graded as
  hybrid: the "what goes wrong" part is executable-graded (run the buggy snippet,
  compare to learner's prediction); the fix is rubric-graded or executable-verified
  by running the corrected snippet.

**Teach-it-back**
- What it is: Learner explains a concept, component, or execution sequence as if
  explaining to a new team member with less context. Coach gives targeted feedback:
  what was precise, what was vague, what was wrong.
- When to use: After a learner has passed an executable drill on a concept — checks
  whether the conceptual model is articulate, not just whether the prediction was
  right. Also useful as a spaced-review format (module F1). Rubric-graded.

**Retrieval check-in**
- What it is: A short (one or two questions) recall exercise on a concept or module
  covered in a prior session, posed at the start of the current session before any
  new material.
- When to use: Every returning session, per `coaching-loop.md` Step 1. Not a full
  drill; a warm-up. If the learner fails the check-in on a previously mastered skill,
  run one full drill before reconsidering the mastery mark.

### 6.2 — Techniques to weave into drills

These are not standalone formats but modifications that deepen any drill type.

**Elaborative interrogation**
- What it is: After a prediction or answer, ask "why," "how," or "when else" — require
  the learner to reason about the mechanism, not just report the result.
- When to use: Any format, especially after a correct first answer — a correct
  prediction without an explanation of *why* may reflect luck rather than model
  accuracy. (`evidence-base.md` → illusions of fluency.)

**Interleaving**
- What it is: Within a session, mix drills across two or more constructs or modules
  rather than drilling one concept repeatedly until mastery, then moving to the next.
- When to use: Once a learner is past Foundations on two or more modules. Interleaving
  slows same-session performance but improves long-term retention and transfer.
  (`evidence-base.md` → desirable difficulties.)

**Varied-context practice**
- What it is: Apply the same underlying concept in a context different from the one
  where it was first taught. "We drilled this in a standalone function — now the same
  concept appears inside a class method."
- When to use: Working → Advanced transition. Prevents the learner from pattern-
  matching to surface context rather than the underlying mechanism.

**Concrete-to-abstract transfer**
- What it is: After the learner has worked through a specific drill, coach steps back
  and asks them to name the general principle. "That was an example of X — where else
  might you encounter X?"
- When to use: After any drill at Working or above where the specific example
  illustrates a general pattern. Helps build the chunked, semantic representation
  that distinguishes expert from novice readers (`evidence-base.md` → Finding 2).

**Error analysis**
- What it is: Present a plausible mistake someone might make (or that the learner
  themselves made in a previous session) and ask the learner to explain what is wrong
  and why.
- When to use: After a learner has failed a drill — flip the failing attempt into the
  subject of analysis. Also useful proactively: "here's a bug someone might introduce;
  what goes wrong?"

**Example-problem pairs**
- What it is: After examining one instance of a pattern (or the coach solving one
  worked example), have the learner find or solve a parallel case themselves.
- When to use: Foundations → Working transition. The worked example reduces cognitive
  load during initial schema-building; the parallel problem activates the generation
  effect immediately after. (`evidence-base.md` → worked examples + expertise reversal.)

**Completion prompts**
- What it is: Coach provides a partial snippet with a gap — a missing line, a missing
  condition, a missing return — and asks the learner to fill in what belongs there.
- When to use: Foundations and early Working tiers. Lowers the generation demand
  compared to full-from-scratch writing, while still requiring active output. The gap
  should be at the exact point of the drill's teaching objective.

---

## Cross-references

- Pause and hard-stop rules after posing a drill: `coaching-loop.md` §Delivery
  Disciplines → "Pause for input."
- Scaffolding ladder when learner is stuck: `coaching-loop.md` Step 7.
- Tier assignment and worked-example depth: `coaching-loop.md` Step 2 and
  §Tier quick-reference.
- Evidence citations for instructional techniques (generation effect, pre-testing,
  desirable difficulties, spacing, worked examples + expertise reversal):
  `evidence-base.md` §Learning-science instructional pillar.
- Evidence citations for what the drills are teaching (notional machine, chunking,
  tracing, expertise gaps): `evidence-base.md` §Verified findings.
