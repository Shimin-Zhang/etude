# C2 — Reading Stack Traces & Error Messages `[Practitioner-canon]`

> **Module type.** `[Practitioner-canon] technique grounded by [Verified] principle` — a
> mostly **executable** comprehension/debugging module. The *technique* it teaches —
> a disciplined procedure for reading a traceback — is practitioner craft (it has no
> single controlled-experiment behind it), but it is **grounded by the verified principle
> that comprehension and debugging are evidence-driven, prediction-then-check activities**
> (`evidence-base.md` → Finding 4) and by the verified fact that the **execution model** is
> the durable barrier (Finding 1) — a traceback is just that model made visible. The
> *answer* in every drill is executable: the runner returns the **real** traceback in
> `stderr` with `status: "error"`, and the learner must name the exception type, the fault
> line, and the cause. (The file badge is `[Practitioner-canon]`; the honest prose badge is
> `[Practitioner-canon] technique on a [Verified] foundation`.)
>
> **Core idea.** A stack trace is **a snapshot of the call stack at the instant of
> failure** — a window straight into the notional machine (A1) and the call tree (A3). You
> read it like a machine, not like prose: **bottom line first** (the exception type +
> message says *what* went wrong), then **walk the frames** to the deepest one that is
> *your* code (that is *where* the machine was), then separate the **site** the error
> *surfaced* from the **cause** that *put it there*.

---

## 1. Evidence basis `[Practitioner-canon]` (technique) on a `[Verified]` foundation

This module is **mixed-status by design**, and the coach must never present the
trace-reading *procedure* as an empirical finding. Two layers:

**(a) The verified foundation — what a traceback *is* `[Verified]`.** A Python traceback is
a literal rendering of the **call stack** (the frames model of A1 §3 and the call tree of
A3) at the moment an exception propagated to the top. Reading it is therefore an exercise
in the **execution model**, which `evidence-base.md` establishes as the durable barrier:

- **Finding 1 — the notional machine is the durable barrier (`[Verified]`).** Sorva (2013,
  *ACM TOCE* 13(2), Article 8, doi:10.1145/2483710.2483713) and du Boulay (1986, *J. Ed.
  Computing Research* 2(1), 57–73) — both confirmed in the evidence base's fact-checking
  pass. The verified claim is narrow: *reasoning about program execution is the central
  difficulty, and it improves when the learner simulates state transitions rather than
  reads for intent.* A traceback **is** the machine's state (its live stack of frames)
  printed for you; reading it well is the execution-model skill applied to a real failure.

- **Finding 4 — comprehension/debugging is active, hypothesis-driven, prediction→check
  (`[Verified]`).** Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995 (all confirmed
  in the evidence base). The licensed claim: *experts read and debug as a cycle of forming
  hypotheses and checking them against the text/runtime, not by reading until it "clicks."*
  The whole point of this module is that **the traceback is the cheapest piece of evidence
  you will ever get** — it names the exception class, the failing line, and the exact call
  chain — and the skill is to *use* that evidence to form a sharp hypothesis, not to skim
  past it to a guess.

**(b) The practitioner-canon layer — the reading *procedure* `[Practitioner-canon]`.** The
specific step-by-step technique (bottom line first → exception type → walk to the deepest
*your-code* frame → site-vs-cause → map onto the machine) is **respected, widely taught
craft**, vetted during authoring against the named primary sources below — **not** a
controlled finding. The coach says: *"this is respected practice — not a verified research
result."* Grounding sources (all verifiable, primary):

- **The Python Tutorial, §8 "Errors and Exceptions," and the Python Language Reference,
  §"Exceptions" (docs.python.org).** The authoritative description of what a traceback is
  (§8.2: the error message "contains a stack traceback listing source lines; however, it
  will not display lines read from standard input") and the **definition of each built-in
  exception class** (Library Reference → Built-in Exceptions) — what
  `NameError`, `UnboundLocalError`, `TypeError`, `AttributeError`, `KeyError`,
  `IndexError`, `ValueError`, `RecursionError`, etc. each *signal*. This is the
  origin-of-record for "the bottom line names the failure" and for the exception-class
  catalog in §5c.
- **PEP 3134 — "Exception Chaining and Embedded Tracebacks" (Ka-Ping Yee, 12 May 2005;
  targets Python 3.0).** The spec that defines the two chaining messages the learner must
  distinguish: **"During handling of the above exception, another exception occurred"**
  (implicit chaining via `__context__` — a *second* exception was raised while handling the
  first) versus **"The above exception was the direct cause of the following exception"**
  (explicit `raise … from …` via `__cause__`). Confirmed against the PEP itself
  (peps.python.org/pep-3134 — author, date, the `__context__`/`__cause__` attributes, the
  `raise … from` syntax, and both message strings verbatim) and rendered live by the runner
  in this module's worked drills.
- **Practitioner canon on the *reading order*** — the consistent, widely-taught advice to
  **read the traceback from the bottom up**: start at the exception type and message, then
  walk *up* the frames to your own code. The load-bearing, verifiable anchor is the Python
  docs' own framing: the header literally reads **"Traceback (most recent call last)"**, so
  by construction the **last** line is the failure (the exception type/message) and the
  **bottom** frame is where it raised — the docs order the trace precisely so you read it
  bottom-first. The further "walk up to the deepest frame that's *yours*" step is craft
  consensus among Python practitioners, not a measured result. It is technique, not
  causation — badged `[Practitioner-canon]` accordingly.

**Why these license this module.** Findings 1 and 4 license the *frame*: a traceback is the
execution model made visible, and debugging is evidence-driven prediction→check, so a
learner who can *read the machine's own report of its state* has a verified-grounded
advantage. The Python docs + PEP 3134 license the *content*: what each exception class
means and what the chaining lines mean are facts, pinned to primary sources. The combined
skill this module teaches: **read the traceback as a stack snapshot — type, then site, then
cause — and turn it into one sharp hypothesis about the fault.**

**Read through the transfer caveat.** The verified foundation (Findings 1, 4) is, like all
`[Verified]` findings here, drawn from **novices in introductory courses, 1976–1995**
(`evidence-base.md` → transfer caveat); the *direction* is well supported but its causal
application to experienced engineers is open. The reading *procedure* is craft, not
science. The honest individual-level test is the transfer task (§9) — reading a real
traceback from the learner's own failing code. **AI-era note:** as agents draft most
first-draft code, the human job shifts to *verifying* code one did not write — and the
first artifact you get when generated code fails is a traceback. Reading it fast and
correctly is squarely in the AI-era "verification cluster" (`evidence-base.md` → AI-era
impact; spec §12) — `[Verified-adjacent]` as a *priority*, not proof.

---

## 2. Soft prerequisites

**A1 (notional machine) and A3 (execution tracing) inform this module most directly.** A
traceback is the **call stack** (A1 §3: one frame per active call, pushed on call, popped
on return) and the **call tree** (A3) frozen at the failure point. The reading skill *is*
the execution-model skill turned on a real crash: to locate the fault you reconstruct,
from the frames, what the machine was doing. Several exception classes here are A1 events
surfacing as errors — **`UnboundLocalError`** is the A1 scope rule (any binding in a
function makes the name local for the *whole* function, so a pre-assignment read is an
unbound local, not a global fallback); **`RecursionError`** is the A1 finite call stack
overflowing. A learner who cannot trace a call tree (A3) will struggle to walk frames.

**C1 (systematic debugging) is the sibling skill.** C2 is the *first move* of C1: the
traceback is the opening evidence from which the first hypothesis is formed. C1 is what you
do *after* you have read the trace; C2 is reading it. **E3 (code review)** leans on C2
whenever a review includes a failing test (read its traceback to find the planted bug).

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at C2 because they cannot
reconstruct the call chain, the coach notes the gap likely traces to A1/A3 and *suggests*
shoring those up — but does **not** forbid C2. Conversely, a learner fluent at A1/A3 who
still freezes at a traceback is exactly who C2 is for: the skill of *reading the report* is
separable from the skill of *simulating the machine*.

---

## 3. The mental model

**A stack trace is a snapshot of the call stack at the instant of failure.** It is not an
error log to skim — it is the notional machine handing you its own state: the chain of
active frames from the top-level call down to the exact line where an exception was raised,
plus the exception's type and message. To use it, you read it like the machine produced it,
in a fixed order, and you separate *what* failed from *where* it surfaced from *what put it
there*.

A Python traceback has four parts. Learn to find each one **by where it sits**, not by
reading top-to-bottom like prose:

| Part | Where it is | What it tells you | Maps onto |
|---|---|---|---|
| **The exception type + message** | The **very last line** (`KeyError: 'threshold'`, `TypeError: 'NoneType' object is not subscriptable`). | **What** went wrong — the *class* names the *category* of fault; the message gives the specifics. **Read this FIRST.** | The kind of state violation (A1: wrong object, missing key, name unbound…). |
| **The deepest frame** | The frame **just above** the exception line (the bottom `File … line N, in <fn>` block). | **Where** the machine was when it raised — the exact line and function. With Python 3.11+ **fine-grained markers** (`^^^` / `~~~~`) it points at the exact *sub-expression*. | A1: the program counter at the moment of failure. |
| **The call chain** | Every `File … line N, in <fn>` block, **top = outermost call, bottom = the failure** ("most recent call **last**"). | **How** execution got there — the live stack of frames, each calling the next. | A1 §3 frames / A3 call tree: push on call, the bottom is the deepest. |
| **The header / chaining lines** | `Traceback (most recent call last):` at the top; and, if present, **"During handling of the above exception, another exception occurred"** or **"The above exception was the direct cause…"** between two tracebacks. | Whether there is **one** failure or a **chain** of them — and if chained, which traceback holds the *original* cause (the **first/top** one). | A1: a second exception raised while the first was being handled (PEP 3134). |

**The procedure (four moves, in this order).** It is a pipeline; skipping the first move
poisons the rest.

1. **Read the bottom line — name the exception type and message.** The class tells you the
   *category* before you look at any code (`KeyError` → a dict/lookup was missing the key;
   `AttributeError` → an object didn't have the attribute, very often because it was `None`
   or the wrong type). Say it out loud: *"This is a `TypeError` — something was the wrong
   type for the operation."*
2. **Find the deepest frame — the fault *site*.** Read *up* from the bottom to the last
   `File … line N` block. That line, in that function, is where the machine actually raised.
   The 3.11+ caret markers narrow it to the exact operand.
3. **Walk up to the deepest frame that is *your* code.** If the deepest frame is inside a
   **library** (a path under `site-packages/`, the stdlib, `json/decoder.py`, …), keep
   walking *up* until you reach the deepest frame *you wrote*. Library internals rarely have
   the bug; **the boundary where your code called the library with bad input usually does.**
4. **Separate the site from the cause.** The line the trace points at is where the error
   *surfaced* — not always where the bug *lives*. `average(vals)` raising
   `ZeroDivisionError` on `sum(nums) / len(nums)` is a correct line; the **cause** is the
   empty list passed two frames up. Ask: *given the message, what value/state made this line
   fail, and where did that value come from?* That question, answered against the frames, is
   the hypothesis C1 then tests.

**The discipline in one line: *read the bottom line first, then walk the frames to your
code — name the type, the site, and the cause as three separate things.*** The novice
failure is to treat the traceback as opaque red noise and guess from the symptom; the skill
is to read it as the machine's own state report.

Three corollaries the module drills:

1. **The exception *class* is information before you read any code.** Each built-in class
   signals a *category* of fault (§5c). Naming it correctly is half the diagnosis —
   `NameError`/`UnboundLocalError` point at the **namespace/scope** (A1); `TypeError`/
   `AttributeError` at a **wrong object (often `None`)**; `KeyError`/`IndexError` at a
   **data-shape** mismatch; `RecursionError` at the **call stack** (A1).
2. **Site ≠ cause.** The deepest frame is where it *surfaced*. The cause is often the value
   that flowed in from a frame above. Reading the chain *up* is how you find it.
3. **"Most recent call last" + chaining.** The **bottom** frame is the failure; the **top**
   frame is where you started. In a *chained* traceback, the **first** (top) traceback holds
   the *original* cause, and the chaining line tells you whether the second error was raised
   *while handling* the first (`__context__`) or *because of* it (`raise … from`,
   `__cause__`).

---

## 4. Worked example — reading a real multi-frame traceback

*(Foundations depth: every step shown, with the **real** runner traceback pasted in. This
fades by tier — see the table after.)*

The skill is to **read the machine's own crash report** in the fixed order above. Consider
this code — a `summarize` helper that pulls a threshold out of a config dict and filters
rows by it:

```python
def load_config(records, key):
    return records[key]

def summarize(rows):
    cfg = load_config(rows, "threshold")
    return [r for r in rows if r > cfg]

data = {"limit": 10, "ceiling": 99}
print(summarize(data))
```

**Runner-verified ground truth** (executable-ground-truth discipline,
`drill-generation.md` §2 — the coach *runs* it and reads the real `stderr`, never guesses):

```
status: error
stderr:
Traceback (most recent call last):
  File "snippet.py", line 9, in <module>
    print(summarize(data))
          ~~~~~~~~~^^^^^^
  File "snippet.py", line 5, in summarize
    cfg = load_config(rows, "threshold")
  File "snippet.py", line 2, in load_config
    return records[key]
           ~~~~~~~^^^^^
KeyError: 'threshold'
```

*(Verified by running `/tmp/C2_worked_keyerror.py` through
`runtime/python/runner.py`. The runner reports temp paths like
`/tmp/…/snippet.py`; shown here as `snippet.py`. The 3.11+ caret markers — `~~~~^^^` — are
real runner output.)*

**Now run the four moves:**

1. **Bottom line — type + message.** `KeyError: 'threshold'`. A `KeyError` means a
   **mapping lookup asked for a key that wasn't there**. The message names the missing key:
   `'threshold'`. Before reading a single line of code, we already know: *some dict was
   indexed with `'threshold'` and didn't have it.*
2. **Deepest frame — the site.** Read up to the last `File … line N` block: **line 2, in
   `load_config`**, at `return records[key]`. The `~~~~~~~^^^^^` caret sits under
   `records[key]` — that subscription is exactly where the machine raised.
3. **Walk to your code.** Every frame here is *your* code (no library frames), so the
   deepest *your-code* frame is the site itself: `load_config`, line 2.
4. **Site vs. cause.** Line 2 is correct in isolation — indexing a dict by a key is fine.
   The **cause** is *which* dict and *which* key. Walk the chain **up**: line 5 in
   `summarize` called `load_config(rows, "threshold")`, and line 9 called `summarize(data)`
   where `data = {"limit": 10, "ceiling": 99}`. So `records` *is* `data`, and `data` has no
   `"threshold"` key (it has `"limit"` and `"ceiling"`). **The fault:** `summarize` assumes
   the config carries a `"threshold"` entry, but the caller passed a dict that uses
   different key names. The fix is **upstream of the raise site** — the caller's data (or
   `summarize`'s contract about what keys it requires) is what's wrong, not the `records[key]`
   line. Editing `load_config` to swallow the missing key would only hide the real mismatch.

**What the trace makes visible** (and a guess from the symptom hides): the *type* told us
the category (missing key) for free; the *deepest frame* gave the exact line; and the
*chain*, read upward, gave the **cause** (the caller's dict shape) — which is **not** at the
raise site. A reader who saw "KeyError" and started editing `load_config` would be fixing
the wrong frame. *Read the bottom line, walk the frames, separate site from cause.*

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully read-out
> traceback *helps novices* (it models the reading order while the schema forms) but becomes
> **redundant load for the more advanced**, who learn more by reading it themselves. So the
> coach fades it:
>
> | Tier | Worked-example depth at C2 |
> |---|---|
> | **Foundations** | **Full** — the complete four-move read above, every part of the trace pointed at and explained. |
> | **Working** | **Partial** — coach names the exception type and the deepest frame, then leaves the **site-vs-cause** walk (which frame holds the fault, and why) for the learner. |
> | **Advanced** | **Skeleton** — coach hands over the raw traceback only; learner names the type, the fault frame, and the cause unaided, and (for chained traces) says which traceback holds the original cause. |
> | **Frontier** | **None** — straight to the traceback (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for C2. Grading mode is
declared up front: **executable** for the type + fault-line (the runner returns the real
traceback), **hybrid** for the cause/fix reasoning (rubric) (§5d).

### 5a. Tier definitions (C2-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Every
drill is a buggy snippet that raises**; the coach runs it, gets the **real** traceback, and
the learner reads it. The learner must always produce **(type, fault line, cause)**; the
tiers differ in how far the cause is from the raise site and how many frames/wrinkles are
involved.

| Tier | C2 criterion | Example shape |
|---|---|---|
| **Foundations** | A **single-frame or shallow** trace, one common exception, where the **fault is at (or one obvious step from) the raise site**. Name the **exception type** and the **fault line**, and state the cause in one sentence. | A `TypeError` in an accumulator loop (a string in a numeric list); an `AttributeError` (`'int' object has no attribute 'strip'`). |
| **Working** | A **multi-frame** trace (2–4 frames) where intent and execution diverge and the **cause is one frame above the raise site** — a `None` from a missing `return`, a missing dict key, a bad unpack. Name type + the deepest *your-code* frame **and** walk up to the cause. | `'NoneType' object is not subscriptable` because a lookup returned `None` one frame up; a `KeyError` through a genexpr + nested dict. |
| **Advanced** | **Combine two or more** reading skills: the **site is far from the cause** (≥2 frames up), the deepest frame is a **library**, the trace is **chained** ("during handling…" / "direct cause"), or it is a **`RecursionError`**. Name type + site + cause **and explain why** the raise site is not the fix site. | `ZeroDivisionError` whose cause is an empty list 2 frames up; a chained traceback where an over-broad `except` masks the real `KeyError`; a `JSONDecodeError` whose deepest frame is stdlib. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a "Foundations" trace actually needs a 3-frame site-vs-cause walk,
or an "Advanced" trace's bug sits right at the raise site with no chaining/library/depth
wrinkle. Apply the self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for C2:

- **Exception class** — `NameError` · `UnboundLocalError` · `TypeError` · `AttributeError`
  · `KeyError` · `IndexError` · `ValueError` (incl. unpack) · `ZeroDivisionError` ·
  `RecursionError` · a **stdlib** exception (`JSONDecodeError`, etc.) · `AssertionError`
  (failing-test surface). *(Each class maps to a §5c diagnosis category.)*
- **Trace depth** — single frame · 2–3 frames · deep (recursion / `[Previous line repeated
  N more times]`) · includes a **comprehension/`<genexpr>`/`<lambda>`** frame.
- **Site-vs-cause distance** — fault **at** the raise site · **one** frame up · **two-plus**
  frames up · cause is the **caller's data**, not any code line.
- **Frame ownership** — all frames are *your* code · deepest frame is **library/stdlib**
  (must walk up to the your-code boundary).
- **Chaining** — none · **implicit** ("During handling of the above exception, another
  exception occurred") · **explicit** ("The above exception was the direct cause…",
  `raise … from`).
- **What the learner must produce** — *type + line* (Foundations) · *type + line + cause
  walk* (Working) · *type + site + cause + why-site-≠-fix* and, for chains, *which traceback
  holds the original cause* (Advanced) · *plus a teach-it-back of the reading procedure*
  (Advanced/Frontier).
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (read the real trace of a
  buggy snippet); also **Prediction → Observation → Reflection** (predict *whether and how*
  it raises, then read the trace), **Error analysis** (here is a *wrong reading someone
  gave* — what did they miss?), and **Teach-it-back** (articulate the four-move procedure).

Keep an in-session log of the `(exception class, depth, site-vs-cause distance, frame
ownership, chaining, format)` tuples used; do not repeat a tuple until the others are
exercised. In particular, **do not pose three `KeyError`s in a row** — vary the class.

### 5c. Common-error catalog

The *specific* trace-reading errors, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the execution-model misconception
literature (Pea 1986; du Boulay 1986; Kaczmarczyk et al. 2010 — all in `evidence-base.md`
Finding 1) and the Python docs' exception semantics (PEP 3134; the tutorial's exception
chapter), not in trivia. **The root of most of them is one inversion: treating the traceback
as opaque noise to skim past on the way to a guess, instead of reading it as the notional
machine's own state report — type first, then the frames as a stack, then site-vs-cause.**

```
Error: Reads the traceback top-to-bottom like prose and fixates on the FIRST "File…line"
       (the outermost frame, usually the top-level call or a test harness) as "where the
       error is," instead of the deepest frame.
Diagnoses: Has the stack order backwards — does not know "most recent call last" means the
           BOTTOM frame is the failure and the TOP is where execution started. No
           frames-as-a-stack model. (A1 §3 call stack; Python tutorial §8.)
Example trigger: any 3-frame trace; ask "which line actually raised?" — a learner who
                 names the top-level `print(...)` line has read it upside down.

Error: Names the exception type wrong or treats the class as meaningless ("it's just an
       error"), reading only the message, so cannot use the class to categorize the fault.
Diagnoses: Does not know what the built-in classes SIGNAL — that KeyError vs IndexError vs
           TypeError each name a different CATEGORY of state violation before you read any
           code. Exception class carries information; the learner discards it. (Python
           Library Reference, built-in exceptions.)
Example trigger: an AttributeError on None ('NoneType' object has no attribute 'x'); ask
                 "what does that class tell you before you look at the code?"

Error: Confuses the exception SITE with the CAUSE — starts editing the deepest frame even
       when that line is correct and the bad value came from a frame above.
Diagnoses: No site-vs-cause distinction; assumes "where it raised" == "where the bug is."
           Does not read the chain UPWARD to find where the offending value entered.
           (Finding 4: debugging is tracing the evidence to its source, not patching the
           symptom.)
Example trigger: ZeroDivisionError on `sum(nums)/len(nums)` whose cause is an empty list
                 passed two frames up; the division line is fine — the input is wrong.

Error: Treats library/stdlib frames as "the bug" — tries to fix json/decoder.py or a
       frame deep inside a package, instead of the boundary where their own code called the
       library with bad input.
Diagnoses: Does not distinguish YOUR code from library internals in the frame list; no
           notion of "walk up to the deepest frame I wrote." (Practitioner canon: the bug
           is almost always at the your-code/library boundary, not inside mature libraries.)
Example trigger: a JSONDecodeError whose deepest frames are json/__init__.py and
                 json/decoder.py; the fault is the malformed string YOUR code passed to
                 json.loads.

Error: Ignores the chaining banner — reads only the SECOND (bottom) traceback of a chained
       error and reports the re-raised wrapper exception, missing the original cause in the
       FIRST traceback.
Diagnoses: Does not parse "During handling of the above exception, another exception
           occurred" / "The above exception was the direct cause": that there are TWO
           linked failures and the ORIGINAL cause is in the first/top traceback. (PEP 3134.)
Example trigger: an over-broad `except Exception: raise ValueError(...)` that masks a
                 KeyError; the learner reports "ValueError" and stops, missing the KeyError
                 that the first traceback names as the real cause.

Error: Reads UnboundLocalError as "the variable doesn't exist / NameError" and looks for a
       typo, missing that it is a SCOPE event — the name is local (because it's assigned
       somewhere in the function) but read before being bound.
Diagnoses: No static-scope model — does not know that any binding anywhere in a function
           makes the name local for the WHOLE function, so a pre-assignment read is an
           unbound LOCAL, not a missing global. (A1 §5c scope entry; Python FAQ.)
Example trigger: a function that does `count = count + 1` where `count` is also a global —
                 raises UnboundLocalError, not NameError; the fix is `global`/`nonlocal` or
                 a parameter, not spelling.

Error: Reads RecursionError as "the function is broken / infinite loop" without recognizing
       the repeated identical frame and "[Previous line repeated N more times]" as a missing
       or never-reached BASE CASE.
Diagnoses: Does not map the deep repeated frame to A1's FINITE call stack overflowing —
           each call pushes a frame, the base case never fires, the stack hits the limit.
           (A1 §5c recursion entry; A1 finite-stack model.)
Example trigger: a recursive `depth(node)` that recurses on the same node (never advances
                 to a child) → the trace shows the same line repeated ~996 times then
                 RecursionError.

Error: Guesses the fault from the symptom / the function's NAME or apparent intent without
       reading the trace at all ("it's a list thing, probably the loop").
Diagnoses: The superbug applied to errors — reading for intent instead of reading the
           machine's actual report. The traceback is the cheapest evidence available and the
           learner skips it. The root meta-error this module targets. (Pea 1986; Finding 4.)
Example trigger: any drill where the learner answers before pointing at a specific line and
                 a specific exception class — grade the READING, not the lucky guess.

Error: Stops at "it raised an error" without naming the line, so cannot act — reports the
       category vaguely ("some type error somewhere") with no frame.
Diagnoses: Communication/localization failure: the read is not actionable. Naming the
           class without the frame (or vice versa) is half a read. (Mirrors the A3
           "endpoint without intermediate state" gap and the E3 "vague feedback" gap.)
Example trigger: a learner who says "TypeError" but cannot point at the deepest your-code
                 frame and line where it raised.
```

### 5d. Grading mode

**Executable for the read; hybrid for the reasoning** (`drill-generation.md` §1d, §2, §3).
Every C2 drill has executable ground truth: the coach **runs the buggy snippet** via
`python <skill-dir>/runtime/python/runner.py snippet.py`, gets `status: "error"` and the
**real traceback in `stderr`**, and grades against it. **Surface the run** in the reply —
paste the exact snippet and the exact `stderr` traceback (`coaching-loop.md` → Surface
ground truth) so the learner sees the evidence; an unseen run reads as a guessed key.

The grading is **hybrid**, and the two verdicts are reported **separately**:

1. **Executable part (hard).** Did the learner name the correct **exception class** (matches
   the last line of the real `stderr`) and the correct **fault line / deepest your-code
   frame** (matches the bottom `File … line N` block, or the deepest non-library block)?
   This is checkable against the runner output verbatim. For chained traces, "which
   traceback holds the original cause" is also executable (it is the first/top traceback).
2. **Rubric part (soft) — the cause / how-to-fix.** *Why* did the line fail, what value/state
   caused it, where did that value come from, and what is the fix? This is graded against the
   per-tier bar in §7 and the catalog in §5c (it is a judgment about the *cause*, not a
   single computable string — though any proposed *fix* can be made executable: apply it and
   re-run to confirm `status: "ok"`). The coach says out loud: *"naming the type and line is
   machine-checked; the cause/fix is a judgment graded against the rubric — softer than the
   executable part."*

Report the verdicts separately: a learner who **names the type and line** (executable: yes)
but **points at the wrong frame as the cause** — e.g., wants to fix the library frame, or
the raise site when the bug is two frames up (rubric: poor) — is a **partial pass**, and the
coach flags exactly that, because **site≠cause** confusion is the central C2 failure (§5c).
A correct type + line with a hand-wavy "something's wrong with the data" cause is also a
partial pass (it often reflects pattern-matching on the class name, not a real read).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one non-trivial reading skill exercised in isolation (site far from cause,
  *or* a library frame, *or* a chain, *or* a `RecursionError`).
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  interacting wrinkle OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for C2, with step counts:

1. **Combine reading wrinkles** (the canonical path from `drill-generation.md` §5):
   - Frontier-1: a **chained** traceback **and** the original cause is in a **library** frame
     of the first traceback (Advanced chaining + 1 extra wrinkle: read past the wrapper *and*
     up to your-code/library boundary).
   - Frontier-2: the above **and** the cause is **≥2 frames up** from where the original
     exception raised (+1: a deep site-vs-cause walk inside the first traceback).
   - Frontier-3: the above **and** a **comprehension/`<genexpr>`** frame sits between the
     caller and the raise site, obscuring the data path (+1).
   Each additional interacting wrinkle is exactly one Frontier increment.

2. **Deeper / messier stacks** (push the depth dimension): a `RecursionError` where the base
   case *exists* but is **never reached** because an argument is mutated wrong each call
   (read the repeated frame *and* the one differing frame); a deep stack mixing your code and
   several library layers (find the *one* your-code frame among them). One increment each.

3. **Subtler exception classes / messages** (push the class dimension): from the common
   classes → to ones whose message is easy to misread (`TypeError: 'X' object is not
   callable` from shadowing a function with a value; `RecursionError` masquerading as a
   hang; a `KeyError` whose key is itself computed). One increment each.

4. **The cause is *not in the trace at all*** (push site-vs-cause to its limit): the
   traceback is correct and complete, but the real fault is **upstream state** — a value set
   far earlier, a config loaded elsewhere, a mutation by a *different* call. The trace tells
   you *where it surfaced*; the learner must reason that the cause is *outside* the printed
   frames and say where to look next (hand off to **C1** for the hypothesis-and-test loop).
   One increment for "cause is upstream of the trace," another for "and you must name the
   next place to look."

5. **Real AI-generated failures → the AI-era frontier.** A traceback from fluent,
   plausible-looking generated code where the message *suggests* one fault but the cause is
   another (the spec-§12 verification skill). Reading a confident-looking program's crash
   without trusting its surface is one increment for "AI-plausible code," another for "and
   the trace's obvious reading is a decoy." (Ties to F1 calibration — over-trusting the first
   plausible reading is the documented AI-era miss.)

Track the level as `C2: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2. Two
cross-cutting requirements apply at every tier above Foundations: **product *and* process**
(the right type+line *and* a sound site-vs-cause read — a correct class with a wrong/absent
cause is a Foundations-level pass at best, and may be pattern-matching on the class name),
and **unaided + durable** (a same-session streak is provisional until a delayed re-assessment
or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for C2 |
|---|---|
| **Foundations** | On a shallow trace (single frame or fault-at-site), **names the exception class correctly and points at the fault line** — e.g., reads `TypeError: unsupported operand type(s) for +=: 'float' and 'str'` and identifies line 4 `total += price` with the offending `"3.00"` string. States the cause in one sentence. D1 (type+line) solid; cause at least partially right. Allowed *with* the worked example faded to one missing step. |
| **Working** | On a **multi-frame** trace, **unaided**: names the type, finds the **deepest *your-code* frame**, **and walks up to the cause** when it is one frame above the raise site — e.g., reads `'NoneType' object is not subscriptable`, points at `user["name"]`, and explains that `find_user` returned `None` (the not-found path) one frame up. Distinguishes **site** (where it raised) from **cause** (the `None` from the missing return). On **4 of 5** unseen drills, including at least one where the cause is one frame above the site. |
| **Advanced** | On a trace **combining** wrinkles — site **≥2 frames** from cause, a **library** deepest frame, a **chained** traceback, or a **`RecursionError`** — **unaided**: names type + site + cause **and explains *why* the raise site is not the fix site**. For a chain, says **which traceback holds the original cause** ("`KeyError: 5` in the *first* traceback is the real fault; the `ValueError` is a wrapper from an over-broad `except`"). For a library frame, walks up to the your-code boundary. Articulates the **four-move reading procedure** on a teach-it-back (`drill-generation.md` §6), not just the instance. |
| **Frontier** | `Frontier-N`: presses one wrinkle past the last comfortable success per §6 / `drill-generation.md` §5 (chained + library cause → + deep site-vs-cause → + comprehension frame; or cause-outside-the-trace; or AI-plausible decoy). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen tracebacks, never from claimed seniority or "I read
stack traces all day." Held-out re-assessment and real-code transfer outrank a same-session
streak (`assessment.md` Part 5).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Skimming the trace and guessing from the symptom.** Treating the traceback as opaque red
  noise and jumping to a fix from the function name or apparent intent. This is Pea's
  *superbug* turned on errors — reading for intent instead of reading the machine's actual
  report. The fix is mechanical: **read the bottom line first** (type + message), then walk
  the frames. The traceback is the cheapest evidence you will ever get; use it.
- **Reading the stack upside down.** Fixating on the *first* `File … line` (the outermost
  call / test harness) as "where the bug is." "Most recent call last" means the **bottom**
  frame is the failure. The fix: read up from the bottom.
- **Confusing the site with the cause.** Editing the deepest frame when its line is correct
  and the bad value arrived from above. The fix: read the chain **upward** and ask *where did
  the offending value come from?*
- **Trying to fix library internals.** Patching `json/decoder.py` or a deep package frame
  instead of the boundary where *your* code passed bad input. The fix: **walk up to the
  deepest frame you wrote.**
- **Reporting the wrapper, missing the cause.** On a chained traceback, reading only the
  second (bottom) error and stopping. The fix: parse the chaining banner; the **first/top**
  traceback holds the original cause (PEP 3134).
- **Misreading scope/recursion errors as typos/hangs.** Treating `UnboundLocalError` as a
  missing-name typo (it is an A1 *scope* event) or `RecursionError` as a vague "broken
  function" (it is the A1 *finite stack* overflowing on a missing/never-reached base case).
  The fix: recognize the class as the A1 event it is.

**Evidence caveat (this is a `[Practitioner-canon]` module — say so).** The trace-reading
*procedure* is **respected, widely taught craft, vetted against the Python docs and PEP 3134
during authoring — not a controlled empirical finding.** The coach must not present "read the
bottom line first, walk to your code" as "research shows." What *is* `[Verified]` is the
**foundation** the technique rests on: that the execution model is the durable barrier
(Finding 1) and that comprehension/debugging is evidence-driven prediction→check (Finding 4)
— and, like all `[Verified]` findings here, that evidence is from **novices in introductory
courses, 1976–1995**, with the curriculum-wide **transfer caveat** (`evidence-base.md`): its
causal application to experienced engineers is open. What each exception class *signals* and
what the chaining lines *mean* are **facts** pinned to the Python documentation and PEP 3134,
not empirical claims. The **AI-era priority** that makes fast trace-reading part of the
verification cluster (spec §12) is `[Verified-adjacent]` — **priority-steering, not proof**;
the supporting productivity data is partly contested and vendor-sourced (`evidence-base.md` →
AI-era honesty caveats). The honest individual-level test is the transfer task (§9). **No
claim in this module is dressed above its badge** — the technique is craft on a verified
foundation, and it is labeled exactly that.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is reading a real
traceback from the learner's own failing code** (`assessment.md` Part 4; `evidence-base.md`
→ transfer caveat, consequence 2).

> **Your turn:** Find a **real traceback** — one from your own code that bit you recently
> (a failing test, a crashed script, an exception in a log, a stack trace an agent's
> generated code threw). Pick the smallest reproducible one you can; if you can reduce it to
> a snippet that still raises, do.
>
> Now **run the four moves on it.** **(1) Bottom line:** name the exception *class* and what
> that class signals as a category, and read the message. **(2) Deepest frame:** find the
> exact line and function where it raised. **(3) Walk to your code:** if the deepest frame is
> a library, walk up to the deepest frame *you* wrote. **(4) Site vs. cause:** name where it
> *surfaced* and, by reading the chain upward, where the fault actually *lives* — and what
> value/state caused it. If it is a *chained* traceback, say which traceback holds the
> original cause and whether the second was raised *while handling* the first or *because of*
> it.
>
> Then step back: **was the line the trace pointed at the line you needed to fix, or did the
> cause live somewhere up the chain?** If you found yourself reaching to edit the raise site
> before reading the frames above it, that is the exact trap this module targets — re-read.

**Grading is softer and named as such** (`assessment.md` Part 4). A real traceback's *cause*
has no clean answer key; the coach grades the **read** against the §7 rubric and says: *"the
type and line are machine-checkable; the cause and fix are a judgment call on your real code,
not a machine-verifiable result."* Where the failure **is** reproducible, the coach still
uses the runner: **reduce it to a minimal snippet, run it through `runner.py` to get the real
traceback, and grade the learner's read against that real `stderr`** — and to grade a
proposed fix, apply it and re-run to confirm `status: "ok"` (the same discipline as the §5d
executable check, now on the learner's real failure). **Transfer evidence is weighted
heavily:** a learner who aces synthetic tracebacks but, on their own failing code, edits the
raise site without reading the chain — or guesses from the symptom — has **not** transferred
the skill, and the tracker notes that gap as more diagnostic than another passed synthetic
drill.

---

## Cross-references

- Drill mechanics, the **executable ground-truth protocol** (run the snippet, read the real
  `stderr`), the **hybrid** grading path (type+line executable, cause rubric), exercise
  formats (Debug-this, Prediction→Observation→Reflection, Error analysis, Teach-it-back),
  Frontier escalation: `references/drill-generation.md` (this module instantiates §1 and
  follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, **surface ground
  truth** — paste the real traceback, direct feedback, scaffolding ladder):
  `references/coaching-loop.md`.
- C2 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, real-code
  transfer weighting: `references/assessment.md` (the C2 entry task: show a multi-frame
  traceback — "where is the fault, what is the runtime telling you, and what single piece of
  evidence in the trace points there?").
- Evidence grounding (Finding 1 — the notional machine as the durable barrier, Sorva 2013 /
  du Boulay 1986; Finding 4 — comprehension/debugging is hypothesis-driven prediction→check;
  the C2 craft sources — Python tutorial §8 + Library Reference exceptions, PEP 3134
  exception chaining, the read-bottom-up practitioner canon; the worked-examples /
  expertise-reversal instructional finding; the AI-era verification cluster):
  `references/evidence-base.md`.
- Soft-prerequisite / sibling modules: **A1** (notional machine — the call stack a trace
  renders; the scope rule behind `UnboundLocalError`; the finite stack behind
  `RecursionError`), **A3** (execution tracing — the call tree a trace freezes), **C1**
  (systematic debugging — what you do *after* reading the trace), **E3** (code review — read
  the traceback when a review includes a failing test).
- Golden exemplars (~3 per tier, each with a **runner-verified** real traceback + the read):
  `exemplars/C2/foundations.md`, `exemplars/C2/working.md`, `exemplars/C2/advanced.md`.
</content>
</invoke>
