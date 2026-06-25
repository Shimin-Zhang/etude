# D1 — Managing Complexity / Abstraction `[Practitioner-canon]`

> **Module type.** `[Practitioner-canon]` (with a `[Some empirical]` counterweight on
> metrics) — a **judgment module**. Its core is a respected practitioner *philosophy*
> (Ousterhout's *A Philosophy of Software Design*) resting on a foundational
> design-principle paper (Parnas 1972, information hiding). There is **no executable
> ground truth for "is this abstraction good?"** — design quality is graded against a
> **rubric + golden exemplars**, not by running the code. Where a snippet has a runnable
> contract, the coach *runs* it to pin the one thing that **is** decidable — that two
> designs are **behaviorally identical**, so any difference between them is a *complexity*
> difference, not a behavior difference. (The validator badge on this file is
> `[Practitioner-canon]`; the honest prose badge is `[Practitioner-canon] + [Some
> empirical, contested]` for the metric caveat.)
>
> **Core idea.** **Complexity is anything about a system's structure that makes it hard to
> understand or change.** It comes from two sources — **dependencies** and **obscurity** —
> and shows up as three symptoms: **change amplification, high cognitive load, and
> unknown-unknowns**. The central craft move is to build **deep modules** (powerful
> functionality behind a simple interface) rather than **shallow** ones (an interface
> nearly as complex as the implementation), and to **pull complexity downward** — let the
> module absorb the hard cases so every caller gets simpler.

---

## 1. Evidence basis `[Practitioner-canon]` (+ `[Some empirical, contested]` on metrics)

This module is **canon by design**, and the coach must **never present it as verified
science** (`evidence-base.md` → badge rules). Its substance is respected, widely taught
*design philosophy* — vetted against the named primary sources during authoring — not an
empirical finding. Three pillars, badged honestly.

**(a) The philosophy — Ousterhout, *A Philosophy of Software Design* `[Practitioner-canon]`.**
Cite via `evidence-base.md` → reading spine (already listed: *"Complexity, deep vs shallow
modules. Craft anchor for D1–D3"*) and the proposed D1 craft-source subsection. The book
(1st ed. 2018; 2nd ed. July 2021) is the source of every load-bearing definition this
module teaches, confirmed against the text during authoring:

- **Complexity** is *"anything related to the structure of a software system that makes it
  hard to understand and modify the system."* It is **incremental** — it accumulates from
  many small chunks, no one of which feels like the problem — which is why it is so hard to
  fight.
- Its **two causes**: **dependencies** ("when a given piece of code cannot be understood
  and modified in isolation") and **obscurity** ("when important information is not
  obvious").
- Its **three symptoms**: **change amplification** ("a seemingly simple change requires code
  modifications in many different places"), **cognitive load** ("how much a developer needs
  to know in order to complete a task"), and **unknown-unknowns** ("it is not obvious which
  pieces of code must be modified to complete a task, or what information a developer must
  have to carry out the task successfully") — which Ousterhout calls the **worst** of the
  three.
- **Deep vs shallow modules.** The best modules are **deep**: they provide *powerful
  functionality through a simple interface*, so the interface hides a lot. **Shallow**
  modules have an interface *nearly as complex as the implementation* and hide little — and
  Ousterhout's most contested claim, **"classitis,"** is that breaking a system into very
  many tiny classes/methods tends to produce shallow modules, raising total complexity.
- **Pull complexity downward.** *"It is more important for a module to have a simple
  interface than a simple implementation."* When there is hard, special-case work to be
  done, the module should absorb it so **every caller** is spared — even if that makes the
  module's *implementation* uglier.
- **Tactical vs strategic programming.** *Tactical* = get this feature working as fast as
  possible (and let complexity accrete); *strategic* = treat working code as not good enough
  — invest continuously in a clean design, because the accumulated complexity is what
  eventually slows you to a crawl.

**HONESTY — this is a philosophy, and its author says so.** Ousterhout opens the book by
asking *"what makes me think I know all the answers about software design? To be honest, I
don't,"* and tells the reader to *"take the suggestions in this book with a grain of salt."*
It distills his Stanford **CS190** software-design course — **classroom experience and
opinion, not a controlled study** — and parts of it (notably *module depth*/"classitis")
are **genuinely contested** among experienced engineers. The coach presents the whole frame
as *"a respected, useful lens — one experienced engineer's hard-won philosophy, not a
measured result."*

**(b) The foundation — Parnas 1972, information hiding `[Practitioner-canon]` (foundational).**
Cite via `evidence-base.md` → proposed D1 subsection. **Parnas, D. L. (1972). "On the
Criteria To Be Used in Decomposing Systems into Modules." *Communications of the ACM*,
15(12), 1053–1058.** doi:10.1145/361598.361623. The origin of **information hiding** and
the answer to *what* a deep module should hide: decompose a system so that **each module
hides a design decision that is likely to change**, behind an interface that does *not*
change when the decision does. Parnas contrasts two decompositions of the same program — a
conventional flowchart-driven split vs. an information-hiding split — and argues the latter
yields modules that can be *"changed independently"* and *"understood independently."* This
is the **classic origin** of the whole deep-module/encapsulation line; Ousterhout's "deep
module" is, in large part, "a module that hides a likely-to-change design decision well."
It is **foundational craft**, a design *criterion* and argument — not an experiment.

**(c) The metric counterweight — complexity metrics are weak/contested `[Some empirical, contested]`.**
This is the one place D1 touches real empirical literature, and it is included **precisely
to keep the module honest**: the famous *number* people reach for to "measure complexity"
does **not** measure what this module is about. **McCabe's cyclomatic complexity** (McCabe,
T. J. (1976). "A Complexity Measure." *IEEE Transactions on Software Engineering*, SE-2(4),
308–320, doi:10.1109/TSE.1976.233837) counts independent paths through a function. As a
**defect predictor**, it is **weak and contested**: it is *strongly correlated with lines
of code*, so most of its apparent predictive power is just program **size** — *"for a large
class of software it is no more than a proxy for, and in many cases is outperformed by,
lines of code"* (Shepperd, M. (1988). "A critique of cyclomatic complexity as a software
metric." *Software Engineering Journal*, 3(2), 30–36, doi:10.1049/sej.1988.0003). And
**"reducing the cyclomatic complexity of code is not proven to reduce the number of errors
or bugs in that code"** (as the metric's own widely-cited summary states; Les Hatton's
finding that it has "the same predictive ability as lines of code" is the standing
critique). **The coach must therefore NEVER say a metric measures "real" complexity.**
Ousterhout's complexity (dependencies + obscurity, felt as change-amplification / cognitive
load / unknown-unknowns) is a **human, structural** property a number cannot capture; D1
trains *judgment*, not a metric.

**Why these license this module.** Parnas gives the *criterion* (hide the
likely-to-change decision); Ousterhout gives the *vocabulary and the moves* (deep vs
shallow, pull complexity down, tactical vs strategic) for spotting and fixing complexity;
the metric literature is the **honest fence** that stops the coach from pretending design
quality is a measurable scalar. The combined claim this module teaches: **a good
abstraction is deep — it hides a real, likely-to-change decision behind a simple interface,
so callers get simpler and a change touches one place; a bad one is shallow, leaks its
internals, or merely relocates complexity without reducing it.**

**Read through the transfer caveat.** Unlike the `[Verified]` Track-A modules, D1 has **no
program-comprehension experiment behind its core**: it is craft (a) + foundational design
argument (b), fenced by a contested metric (c). The curriculum-wide **transfer caveat**
(`evidence-base.md`) applies in full and then some: that drilling "deep vs shallow" on
synthetic snippets *causally* improves a given engineer's real designs is **unproven** —
this is craft, and design judgment is exactly the kind of skill where the only honest test
is the learner's **own real module** (§9). **AI-era note:** as agents draft most
first-draft code, the bottleneck moves to *judging* whether a generated abstraction is deep
or just plausible-looking — over-trusting a fluent, shallow interface is the documented
AI-era miss (`evidence-base.md` → AI-era section; ties to E3/F1) — `[Verified-adjacent]` as
a *priority*, not proof.

---

## 2. Soft prerequisites

**A2 (code reading & chunking) recommended.** Depth and chunkability are two views of the
same thing: a **deep module is one you can chunk** — you can hold "what it does" in one
unit without unpacking its insides; a **shallow module forces you to read its
implementation to use it**, so it never collapses into a clean chunk (`evidence-base.md` →
Finding 2). A learner who can rapidly chunk unfamiliar code can *feel* the cognitive-load
symptom directly. **A1 (notional machine)** helps because several "leaks" in this module
are A1 execution-model events surfacing as design smells (a mutable default shared across
calls leaking state; aliasing the caller's object). **D2 (names)** and **D3 (refactoring
toward depth)** are the natural siblings: a leaky interface often shows up first as a
**lying or implementation-revealing name** (D2), and the *fix* for a shallow module —
deepening it without changing behavior — **is** refactoring (D3).

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner struggles to *see* a complexity leak
because they cannot hold the change in their head, the coach notes the gap likely traces to
A2 and *suggests* shoring it up — but does not forbid D1. Conversely, D1 is itself a soft
prerequisite signal for D3: you cannot refactor *toward* depth if you cannot tell deep from
shallow.

---

## 3. The mental model

**Complexity is anything about a system's structure that makes it hard to understand or
change. It is not "lines of code" and not a metric — it is a human, structural property.
You manage it by hiding the right things behind the right interfaces: deep modules that
absorb hard decisions, so callers stay simple and a change lands in one place.**

The model has two **causes**, three **symptoms**, and one **central move**:

| Piece | What it is | The tell |
|---|---|---|
| **Cause: dependencies** | A piece of code that *cannot be understood or changed in isolation* — it is coupled to others, so touching one forces touching the rest. | Change one thing → must change N others (change amplification). |
| **Cause: obscurity** | Important information that is *not obvious* — a hidden contract, an implied ordering, a side effect a "getter" performs, a magic value duplicated around. | You cannot use the code correctly from its interface; you must read the implementation, or you get bitten by something you couldn't have known. |
| **Symptom: change amplification** | A seemingly simple change requires edits in many places. | One business rule lives at ten call sites; changing it means finding all ten (and missing one). |
| **Symptom: cognitive load** | How much you must hold in your head to do a task. | "To call this you must also know X, Y, Z, and call them in *this* order." |
| **Symptom: unknown-unknowns** | You don't even know what you'd need to know — *the worst symptom*. | A change works in test, breaks a far-away thing you never knew depended on it. |
| **The move: depth** | **Deep** = powerful functionality behind a **simple** interface (hides a lot). **Shallow** = interface ≈ implementation in complexity (hides little). | Cover the interface and ask: *how much work, and how much "you must know," did it save the caller?* A lot → deep. Almost none → shallow. |

**The discipline in one line: *push complexity down behind a simple interface — a good
abstraction makes the caller's life simpler and the change land in one place; a bad one
just moves the complexity around or leaks it back out.*** The machine has no opinion about
your design; *the caller* is the judge — what does this interface spare the people who use
it? Three corollaries the module drills:

1. **Depth is measured at the interface, not the implementation.** A long, hairy
   implementation behind a *tiny, total* interface is **deep and good** (Ousterhout: prefer
   a simple interface over a simple implementation). A three-line method that forces the
   caller to know everything it does is **shallow** no matter how short it is. So "small
   functions" is *not* the goal; **information hidden** is. (This is the corollary that
   collides with naïve "Clean Code" rules — see §8.)
2. **Hide a decision that is likely to change (Parnas).** The thing worth hiding is the
   design decision callers should not depend on and that you expect to revise — a storage
   format, a wire protocol, a special-case rule, a third-party API. If the interface
   *leaks* that decision, every caller is coupled to it and you get change amplification.
3. **An abstraction must *pay for itself*.** Every interface adds a thing to learn and a
   place to look (its own small cost). It earns that cost only by **removing more
   complexity than it adds** — by genuinely hiding work or a decision. A pass-through that
   wraps one call, a "helper" with eight flags, a class that just renames a dict's keys:
   these **move or rename** complexity without reducing it, so they don't pay for
   themselves. *Pulling complexity down* is the version that pays; *moving it sideways* is
   the version that doesn't.

---

## 4. Worked example — deep vs shallow, same behavior

*(Foundations depth: the full judgment shown — the two designs, where the complexity lives,
and why one is deep. This fades by tier; see the table after.)*

The skill is to **judge like a senior designer**: read two designs that do the *same
thing*, locate where the complexity lives, and name which is deep and why. Consider a config
reader. The contract: *given config data, return an integer setting, falling back to a
default when the key is missing.*

**Design A — deep.** The special case (missing key → default, plus the string→int cast)
lives *inside* the module, once:

```python
class Config:
    def __init__(self, data):
        self._data = data
    def get_int(self, key, default):
        if key not in self._data:        # the hard case is handled HERE, for everyone
            return default
        return int(self._data[key])
```

**Design B — shallow.** A thin getter returns the raw value (or `None`), forcing **every
caller** to repeat the missing-key + default + cast dance:

```python
class ShallowConfig:
    def __init__(self, data):
        self._data = data
    def raw(self, key):
        return self._data.get(key)       # returns None on a miss; caller must cope

def caller_get_int(c, key, default):     # this logic now lives at EVERY call site
    v = c.raw(key)
    if v is None:
        return default
    return int(v)
```

**Step 1 — Locate the complexity.** Both designs *can* produce the right answer. The
question is **who carries the load.** In A, the caller writes `cfg.get_int("timeout", 10)` —
one line, no special-casing, nothing to know about how missing keys or string values are
handled. In B, the caller must know that `raw` returns `None` on a miss, must supply the
default itself, and must cast — and must do this *correctly at every call site.* The
missing-key + cast decision **leaked out** of B's interface (obscurity + a dependency every
caller now has).

**Step 2 — Judge depth.** A's interface (`get_int(key, default)`) is **simple** and hides
**real work** (the membership check, the cast, the fallback) → **deep**. B's interface
(`raw(key)`) is simple *only because it does almost nothing*; the work it should have hidden
is now in `caller_get_int`, duplicated → **shallow**. A also *pulls complexity downward*: if
the storage format changes (say values arrive as bytes), A fixes it in one method; B must
fix every caller — **change amplification**.

**Step 3 — The verdict** (precise · names the leak · says what it costs): *Design A is
deeper. Its `get_int` hides the missing-key fallback and the type cast — a decision likely
to change — so callers stay one-liners and a format change lands in one place. Design B's
`raw` leaks that decision: every caller re-implements the same `None`-check and cast, which
is duplicated cognitive load now and change amplification later. Prefer A. (B's `raw` is
only worth keeping if callers genuinely need the uninterpreted value for unrelated reasons —
then it is a *different*, narrower abstraction, not a substitute for `get_int`.)*

**Verified ground truth** (the coach *runs* both designs to confirm they are
**behaviorally identical** — so the difference is purely complexity, not behavior —
`drill-generation.md` §2; even though the *design verdict* is rubric-graded):

```
$ python <skill-dir>/runtime/python/runner.py D1_worked.py
deep timeout: 30
deep missing: 10
shallow timeout: 30
shallow missing: 10
same? True
status: ok
```

(The snippet exercises both designs on the same inputs — present key and missing key — and
asserts the deep and shallow results are equal. They are: `same? True`. The two designs
disagree on **complexity**, not on output — which is exactly why design quality is *not*
something the runner can grade for you, and why this is a judgment module.)

**What the verdict makes visible** (and a line-count or a "small functions" rule hides):
the **shallow** design's methods are individually *tiny* — `raw` is a one-liner — yet the
design is **worse**, because depth is measured by *what the interface spares the caller*,
not by how short its methods are. A reviewer optimizing for "small methods" would *prefer*
B. The deep/shallow lens, and only it, gets this right.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> judgment helps **novices** (it shows the locate-the-complexity move) but is **redundant
> load for the more advanced**, who learn more by judging themselves. So the coach fades it:
>
> | Tier | Worked-example depth at D1 |
> |---|---|
> | **Foundations** | **Full** — both designs, the leak located, depth judged, the verdict written, every step shown. |
> | **Working** | **Partial** — coach shows the two designs and names *that* one leaks, but leaves **which is deeper and why** for the learner. |
> | **Advanced** | **Skeleton** — coach hands over the design(s) and the rubric only; learner locates the complexity, judges depth, and writes the verdict unaided. |
> | **Frontier** | **None** — straight to the design (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for D1. Grading mode is
declared up front: **rubric + golden exemplars** (§5d) — this is a judgment module, not an
executable one. (Where a snippet has a runnable contract, the coach still *runs* it to
confirm behavior — usually to prove two designs are behaviorally identical, or that a leaked
invariant actually bites; the *design verdict* is graded against the rubric.)

### 5a. Tier definitions (D1-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Most
drills present a module/design (or two) and ask one of three questions: *is this deep or
shallow? · where is the complexity / information leak? · does this abstraction pay for
itself, or just move the complexity?***

| Tier | D1 criterion | Example shape |
|---|---|---|
| **Foundations** | **One clear, single-axis** call: a plainly shallow module (pass-through, getter/setter wrapper, temporal-coupling class) **or** a plainly leaked decision. **Name it and say why** in deep/shallow + interface-vs-implementation terms. No genuine tension; the skill is *seeing the leak and articulating it.* | A `get_user_name` method that just renames `dict.get`; a `read_lines(text, strip_bom)` flag that leaks a decision the module should own. |
| **Working** | A design with a **real but resolvable** judgment: a module that *looks* deep (many methods, long file) but is shallow; an "abstraction" that **moved** complexity into 6 kwargs rather than reducing it; a pull-it-down-or-not call. **Judge it, locate the complexity, and justify** — and resist the tempting wrong answer (e.g. "it's deep because it's a class / because the methods are short"). | A 6-method `Account` class that is a thin shell over a dict; a `fmt(...)` helper with six flags; a None-handling rule that should be pulled down. |
| **Advanced** | A **genuine design tension** or **combined** symptom: general-purpose deep interface vs a pile of special-purpose shallow ones; an interface that hides work but **leaks obscurity through its contract/errors** (unknown-unknowns); change-amplification from a leaked decision across call sites. **Decide, name the symptom(s), propose the deepening, and explain the trade-off** (incl. when the shallow version is actually right). | A text buffer: two general primitives vs five special methods; a `fetch()` that secretly returns a half-initialized object on a cold cache; a discount rule duplicated across sites. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations design hides its leak behind a real trade-off (that's
Working/Advanced), or a Working/Advanced design has an *obvious* one-word answer (that's
Foundations). Apply the self-check (`drill-generation.md` §4) and re-level before posing —
and watch the specific D1 trap: a drill that secretly needs **two** judgments (deep/shallow
*and* a Parnas "what should be hidden" call) is Advanced, not Foundations.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for D1:

- **Question asked** — *is this deep or shallow?* · *where is the complexity / information
  leak?* · *does this abstraction pay for itself, or just move complexity?* · *what should be
  hidden here (Parnas)?* · *deepen this shallow module.*
- **Complexity source / symptom** (Ousterhout) — **dependency** (coupling; change
  amplification) · **obscurity** (hidden contract, implied ordering, side-effecting
  "getter," magic value) · **cognitive load** (must-know-N-things to call it) ·
  **unknown-unknowns** (the change that breaks something far away).
- **Shallowness shape** — pass-through / thin wrapper · getter-setter shell over data ·
  **temporal decomposition** (methods that must be called in a fixed, leaked order) ·
  **over-decomposition / "classitis"** (many tiny shallow pieces) · **information leakage**
  (a decision exposed in the signature) · **conjoined twins** (two interfaces that must
  change together).
- **Direction of the fix** — *pull complexity down* (module absorbs the hard case) ·
  *combine* (replace many special methods with one general one) · *hide the decision* (an
  interface that doesn't change when the decision does) · *make the obscure obvious*
  (surface a hidden contract) — vs. the **anti-fix** of *moving* complexity (into kwargs,
  into a new layer, into the caller).
- **Surface** — a single function/method · a class with several methods · two designs to
  compare (A vs B) · a small module + its call sites · a diff that "refactors" (and the
  judgment is whether it deepened or just churned).
- **Format** (`drill-generation.md` §6) — primarily **Generation → Comparison** (learner
  writes the verdict / the deepened interface, coach reveals the gold) and **Debug-this**
  cast as *design*-review ("what's the complexity smell here?"); also **Teach-it-back**
  (articulate *why* depth is measured at the interface) and **Error analysis** (here is a
  *weak design critique someone wrote* — what did it miss or get backwards, e.g. "it's deep
  because the methods are short?").

Keep an in-session log of the `(question, symptom/shape, surface, format)` tuples used; do
not repeat a tuple until the others are exercised. Mode-collapse here looks like asking
"deep or shallow?" about three pass-throughs in a row — vary the symptom and the question.

### 5c. Common-error catalog

The *specific* design-judgment failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the **named craft sources**
(Ousterhout's red flags; Parnas's information-hiding criterion) and the **metric-honesty**
literature, not in trivia. **The root of most of them is one inversion: judging an
abstraction by the size or shape of its *implementation* (short methods! a class! a layer!)
instead of by how much its *interface hides* — how much work and how much "you must know" it
spares the caller.**

```
Error: Calls a module "deep / well-abstracted" because it is a class, has many methods,
       or its methods are short — counts structure, not hiding.
Diagnoses: Depth judged at the implementation, not the interface. The learner equates
           "more/smaller units" or "uses OOP" with abstraction, missing that a tiny
           interface hiding real work is deep while a big interface hiding nothing is
           shallow. (Ousterhout: deep vs shallow; "classitis" — many small classes raise
           complexity. The naive-Clean-Code collision, §8.)
Example trigger: the 6-method Account-over-a-dict (W2) — short methods, zero hiding.

Error: Says a thin wrapper / pass-through "adds an abstraction" and is therefore good.
Diagnoses: Does not require the abstraction to PAY FOR ITSELF. A one-line method that
           just renames or forwards a call adds interface (a name to learn, a place to
           look) without removing complexity — net negative. (Ousterhout: shallow modules;
           "pass-through methods.")
Example trigger: get_user_name() that is dict.get with a rename (F1).

Error: Misses an information leak — treats a flag/param that exposes an implementation
       decision (strip_bom, normalize, use_cache) as a normal part of the interface.
Diagnoses: Does not apply the Parnas criterion — the interface should hide the
           likely-to-change decision, not surface it. Every caller is now coupled to a
           detail the module should own. (Parnas 1972, information hiding; Ousterhout,
           information leakage.)
Example trigger: read_lines(text, strip_bom) (F2) — the BOM decision leaked into the
                 signature, so a caller who passes False corrupts the data.

Error: Calls a refactor an "improvement" because it added a layer / split a function /
       introduced kwargs — when total complexity is unchanged or worse, just relocated.
Diagnoses: Confuses MOVING complexity with REDUCING it. Indirection that doesn't hide a
           decision is not depth; six flags in a signature is the caller's if-ladder
           wearing a disguise. (Ousterhout: pull complexity DOWN, not sideways; deep vs
           shallow.)
Example trigger: fmt(value, *, as_currency, thousands, decimals, prefix, suffix,
                 parens_negative) (W3) — the decision load moved into kwargs, didn't shrink.

Error: Wants to "pull complexity up" / push the hard case onto the caller "to keep the
       module simple," or splits one method into a fixed call-order sequence.
Diagnoses: Optimizes a simple IMPLEMENTATION over a simple INTERFACE, and/or introduces
           temporal decomposition (a leaked ordering invariant). The caller now carries
           the special case or must know the sequence. (Ousterhout: simple interface >
           simple implementation; temporal decomposition red flag.)
Example trigger: the load->format->emit Report class (F3) — leaked ordering; crashes when
                 emit() is called before format().

Error: Reaches for a metric ("cyclomatic complexity is low, so it's simple"; "this
       function is 5 lines, so it's fine") to settle a design question.
Diagnoses: Treats complexity as a measurable scalar. The metric is largely a proxy for
           size and is a weak/contested defect predictor; it cannot see dependencies,
           obscurity, or a leaked contract. (Shepperd 1988; McCabe-as-LOC-proxy; §8
           evidence caveat.) Complexity here is a human, structural judgment.
Example trigger: a short, low-CC function with an obscure contract (A3 fetch()) that the
                 metric would bless.

Error: Misses obscurity / unknown-unknowns — judges only the visible interface shape and
       calls it deep, missing that the CONTRACT is hidden (a side effect, a cold-cache
       half-result, an implied precondition).
Diagnoses: Equates "small interface" with "deep," forgetting that obscurity is itself
           complexity: an interface you cannot use correctly without reading the impl is
           not deep. (Ousterhout: obscurity, unknown-unknowns — the worst symptom.)
Example trigger: fetch() that returns value=None and mutates state on the first call (A3).

Error: Over-deepens / over-engineers — invents a heavy abstraction, config system, or
       plugin layer for a one-off, then calls it "strategic."
Diagnoses: Strategic programming misread as "always add abstraction." Depth must pay for
           itself; speculative generality is complexity with no decision behind it yet.
           (Ousterhout: strategic vs tactical is about investment in DESIGN, not in
           machinery; "different is not better.")
Example trigger: a learner who "fixes" a fine two-line helper by wrapping it in a
                 strategy-pattern class hierarchy.
```

### 5d. Grading mode

**Rubric + golden exemplars** (`drill-generation.md` §1d, §3). D1 has **no executable
ground truth for the design judgment** — "is this abstraction deep / does it pay for itself?"
is a judgment, not a computation. The coach grades a learner's verdict like this (the §3
judgment path, made concrete for D1):

1. **Run the snippet where it has a runnable contract (the one executable sub-claim).**
   Although the *verdict* is rubric-graded, the coach uses the runner
   (`python <skill-dir>/runtime/python/runner.py snippet.py`, `drill-generation.md` §2) to
   pin the thing that **is** decidable — most often that **two designs produce identical
   output** (so the difference is complexity, not behavior; the worked example's `same?
   True`), or that a **leaked invariant actually bites** (the temporal-coupling class
   *raises* when called out of order; F3). This anchors the gold to real behavior, not the
   coach's guess. If a learner *disputes* a behavioral claim ("calling `emit` first is
   fine"), the coach **runs it** and shows the traceback.
2. **Score the verdict against the D1 rubric (§7), criterion by criterion** — *did they
   reach the right judgment (deep/shallow, pays/doesn't)? did they locate the complexity
   correctly (the actual leak/dependency/obscurity, not a decoy)? did they justify it in
   interface-vs-implementation / Parnas terms and name the cost (which symptom)?* Each is a
   3-point criterion (§7), graded explicitly, one by one.
3. **Cite the closest golden exemplar.** Compare to the tier's golds in
   `exemplars/D1/<tier>.md` — "your critique is close to the **weak** exemplar: you called
   it deep because the methods are short" vs. "close to the **strong** exemplar: you saw the
   interface hides nothing and named the change-amplification cost." The golds are the
   calibration anchor.
4. **Name it as soft.** The coach says out loud: **"this is a design judgment graded
   against the module's rubric + exemplars, not a machine-verifiable answer — softer than an
   executable pass"** (`drill-generation.md` §3; `assessment.md` §1.2). Design has more than
   one defensible answer; the rubric rewards a *well-located, well-justified* judgment, not
   a single "correct" design.

D1 drills are thus **partly hybrid**: any **behavioral** sub-claim (two designs equal; an
out-of-order call raises; a partial edit produces inconsistency) is executable-graded by the
runner; the **design verdict** is rubric-graded. Report the verdicts separately — a learner
who correctly *runs* the snippet and sees the behavior but reaches the **wrong design
verdict** (e.g. "they're equal, so the shallow one is just as good") is a **partial pass**,
and the coach flags exactly that, because conflating "same behavior" with "same complexity"
is the central D1 confusion.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one genuine design tension or combined symptom, judged and justified with a
  proposed deepening and the trade-off named.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  dimension of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for D1, with step counts:

1. **Subtler complexity source** (push the symptom axis): from a *visible* shallowness
   (pass-through) → to a **leaked decision** that only bites on change (Frontier-1) → to
   **obscurity / unknown-unknowns** where the interface looks clean but the contract is
   hidden (Frontier-2) → to a **dependency that spans modules** so the change amplification
   is non-local (Frontier-3). Each is one increment.

2. **Bigger surface** (push the surface axis): from one module → to a module **plus its call
   sites** (judge the leak by what callers must repeat) → to a **multi-module** design where
   the right answer is "this boundary is in the wrong place; here is where it should be"
   (a Parnas re-decomposition), not a local tweak. Each is one increment.

3. **Harder trade-off / the right answer is "it depends"** (push the judgment axis): designs
   where deep is **not** obviously better — a genuinely needed escape hatch, a place where
   pulling complexity down would over-couple the module to a caller-specific concern, a
   case where two small modules are correctly separate because they hide *different*
   decisions. The learner must hold the tension and state the **condition** under which each
   choice wins, not pick a side reflexively. One increment per added degree of genuine
   ambiguity.

4. **Generate, don't just judge** (push the format axis): from *critiquing* a design → to
   **redesigning** it (write the deepened interface) → to **defending** the redesign against
   a plausible objection ("but now the implementation is uglier" — yes, and that's the
   trade Ousterhout endorses) → to **teaching the principle** so it transfers. Writing the
   deeper interface is one increment over judging; defending it is another.

5. **Judge an AI-generated abstraction → the AI-era frontier.** A module that *reads* fluent
   and idiomatic (as agent output does) but is **shallow or leaks a decision** — the spec-§12
   apex skill of verifying design you didn't write. One increment for "AI-plausible
   surface," another for "and you must not be talked out of the deep/shallow judgment by how
   confident and clean it reads" (ties to F1: over-trusting fluent output is the documented
   AI-era miss).

Track the level as `D1: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2,
scored against the three D1 dimensions. Two cross-cutting requirements apply at every tier
above Foundations: **product *and* process** (reached the right judgment *and* located the
complexity and justified it — a correct "shallow!" with a wrong or absent reason is a
Foundations-level pass at best, because design judgment without a located cause is a guess),
and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

**The three scored dimensions** (each 3-point: absent / partial / solid):

- **D-judge — the verdict.** Did they reach a defensible judgment — deep vs shallow, pays
  vs doesn't, what should be hidden — *not* the inverted one ("deep because it's a class")?
- **D-locate — the complexity.** Did they put their finger on the *actual* leak /
  dependency / obscurity (the real cause), not a decoy (a naming nit, a style point)?
  *(Executable sub-claim where present: behavioral facts are confirmed by the runner; §5d.)*
- **D-justify — interface-vs-implementation + cost.** Did they argue depth **at the
  interface** (hiding, Parnas's likely-to-change decision) and name **which symptom** it
  costs (change amplification / cognitive load / unknown-unknowns) — rather than counting
  lines or invoking a metric?

| Tier | Observable bar for D1 |
|---|---|
| **Foundations** | On a **plainly** shallow module or leaked decision (no real tension), **names it correctly and says why** in deep/shallow + interface-vs-implementation terms (e.g. "`get_user_name` just renames `dict.get` — the interface hides no work, so it's shallow; it doesn't pay for itself"). D-judge solid; D-locate at least partial. Allowed *with* the worked example faded to one missing step. |
| **Working** | On a design with a **real but resolvable** judgment (looks-deep-but-shallow; complexity-moved-not-reduced), **unaided**: reaches the right verdict (D-judge), locates the actual complexity (D-locate), **and** justifies it at the interface, naming the symptom — *and resists the tempting wrong answer* ("it's deep because the methods are short / because it's a class"). Reaching the right verdict for the wrong reason ⇒ partial pass, flagged. On 3 of 4 unseen such drills. |
| **Advanced** | On a **genuine tension or combined symptom** (general-vs-special; hidden-contract obscurity; cross-site change amplification), **unaided**: judges it (D-judge), names the symptom(s) precisely (D-locate), **proposes the deepening** (the simpler interface / what to hide / how to pull complexity down), **and** states the **trade-off** — including *when the shallow version is actually right*. Articulates the **underlying principle** on a teach-it-back (`drill-generation.md` §6) — "depth is measured at the interface; hide the decision likely to change" — not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler symptom → bigger/multi-module surface → harder "it depends" trade-off → redesign-and-defend → AI-plausible design). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen design drills, never from claimed seniority or "I've
designed systems for years." Held-out re-assessment and **real-code transfer** outrank a
same-session streak (`assessment.md` Part 5) — and for a judgment module especially, the
real-code signal is weighted heavily (a clean synthetic-snippet streak that doesn't show up
when the learner judges their *own* modules is not yet mastery).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Counting structure instead of hiding.** Calling a design deep because it is a class, has
  many methods, or has short methods — "classitis." The fix: judge **at the interface** —
  how much work and how much "you must know" does it spare the caller? A tiny interface over
  real work is deep; a big interface over nothing is shallow.
- **Pass-throughs that don't pay for themselves.** Adding a one-line wrapper that renames or
  forwards a call and calling it "an abstraction." The fix: require every interface to
  **remove more complexity than it adds** — if it hides no decision and saves no work,
  delete it.
- **Tolerating information leaks.** Letting an implementation decision (`strip_bom`,
  `use_cache`, a storage format) surface in the signature, coupling every caller to it. The
  fix is the Parnas move: **hide the decision likely to change** behind an interface that
  doesn't change when the decision does.
- **Moving complexity and calling it reducing it.** "Improving" code by adding a layer,
  splitting a function, or piling six flags into a signature when total complexity is
  unchanged. The fix: **pull complexity down** (the module absorbs the hard case) rather
  than sideways (into kwargs) or up (onto the caller).
- **Temporal decomposition.** Splitting one job into methods that must be called in a fixed,
  *leaked* order (`load` → `format` → `emit`). The fix: a single interface that owns the
  sequence, or a design where order can't be gotten wrong.
- **Reaching for a metric to settle a design call.** "CC is low, so it's simple." The fix:
  treat complexity as the **human, structural** judgment it is (dependencies + obscurity);
  the metric can't see a leaked contract.
- **Over-deepening / speculative generality.** Wrapping a fine two-liner in a plugin
  framework "to be strategic." The fix: depth must **pay for itself now**; strategic
  programming is investment in *clean design*, not in unused machinery — *"different is not
  better."*

**Evidence caveat (this is a `[Practitioner-canon]` module — say so, loudly).** D1's
grounding is **craft, and must not be oversold**:

- The **core** (deep vs shallow, dependencies + obscurity, the three symptoms, pull
  complexity down, tactical vs strategic) is **`[Practitioner-canon]`** — Ousterhout's *A
  Philosophy of Software Design*, a respected, widely taught **philosophy**, vetted against
  the book during authoring. **Its own author calls it opinion** ("take it with a grain of
  salt"), it comes from a **course**, not a study, and parts of it (module depth /
  "classitis") are **genuinely contested** by experienced engineers. State it as "a useful,
  respected lens," never "research shows."
- The **foundation** (information hiding; decompose around decisions likely to change) is
  **`[Practitioner-canon]`, foundational** — Parnas 1972, the classic origin. It is a design
  *criterion* and argument by a major figure, **not** an empirical result.
- **Complexity metrics are NOT a back-door to "verified."** Cyclomatic complexity as a
  defect predictor is **weak and contested** (`[Some empirical, contested]`): largely a
  proxy for lines of code (Shepperd 1988), and **"reducing cyclomatic complexity is not
  proven to reduce errors."** The coach **never** claims a metric measures real complexity,
  and never upgrades the module's craft core to `[Verified]` on the strength of a number.
- A neighboring temptation to refuse: **"good abstractions / refactoring toward depth reduce
  bugs"** is **not an established empirical finding** — it is plausible craft. Likewise
  **mechanical-sympathy / cache-locality** arguments (a cousin of "pull complexity down")
  **matter in systems and HFT but are overstated for typical application code**; D1 does not
  lean on them. Keep the win as **understandability and changeability** (what the craft
  actually claims), not measured defect rates or speed.
- The **curriculum-wide transfer caveat** applies in full: that drilling deep/shallow on
  synthetic snippets *causally* improves a given engineer's real designs is the open
  question every module here carries, and it bites *harder* for a craft module with no
  comprehension experiment behind it. The coach leans on the transfer task (§9) — the skill
  on the learner's **own module** — as the honest individual-level evidence, and grades it as
  the soft judgment it is.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2). For a craft module, this is *especially* true — there is no comprehension
experiment standing behind D1, so the learner's real module is the load-bearing evidence.

> **Your turn:** Find a module, class, or function in **your own codebase** that you (or a
> teammate) have had to **change more than once**, or that you find yourself *re-reading its
> implementation* every time you call it. Pick the smallest such piece.
>
> Now **run the three moves.** **(1) Judge its depth:** cover the implementation and look
> only at the interface — how much work, and how much "you must know," does it spare a
> caller? Is it **deep** (simple interface, real hiding) or **shallow** (interface ≈
> implementation)? **(2) Locate the complexity:** name the *actual* cause — a **dependency**
> (what change forces other changes?), an **obscurity** (what must a caller know that the
> interface doesn't tell them — an implied order, a side effect, a magic value?), or a
> **leaked decision** (what implementation choice shows up in the signature?). Which of the
> three **symptoms** has it cost you — change amplification, cognitive load, or an
> unknown-unknown that bit you? **(3) Propose the deepening:** what would you hide, and what
> would the simpler interface look like — and does that deepening **pay for itself**, or
> would it just move the complexity? Name the trade-off honestly, including the case where
> the current shape is actually fine.
>
> Then step back: **was the thing worth hiding a decision that is *likely to change*** (a
> format, a protocol, a rule, a dependency)? If you can't name a likely-to-change decision
> behind the interface, the abstraction may not be earning its keep.

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean
answer key; the coach grades against the §7 rubric (D-judge / D-locate / D-justify) and
says: *"this is a design judgment on your real code, not a machine-verifiable result — and
D1 is craft, not measured science, so weigh it accordingly."* Where any sub-claim **is**
runnable — the learner claims two shapes behave identically, or that a leaked ordering can be
called wrong — the coach still uses the runner: **reduce the claim to a minimal snippet, run
it through `runner.py`, and confirm the behavior before the learner leans on it** (the same
discipline as §5d, now on the learner's real module). **Transfer evidence is weighted
heavily:** a learner who aces synthetic deep/shallow drills but, on their own code, calls a
leaky 6-method shell "well-abstracted because it's a class" has **not** transferred the
skill, and the tracker notes that gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **rubric + exemplars judgment path**, the executable check on
  behavioral sub-claims, exercise formats (Generation→Comparison, Debug-this-as-design-review,
  Teach-it-back, Error analysis), Frontier escalation: `references/drill-generation.md` (this
  module instantiates §1 and follows §3, §4, §5; the behavioral check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder, **surface ground truth** — paste the snippet + output): `references/coaching-loop.md`.
- D1 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-code
  transfer** weighting: `references/assessment.md` (the D1 entry task: two designs of one
  small utility — judge which is deeper, locate the complexity, justify it).
- Evidence grounding (Ousterhout's *A Philosophy of Software Design* on the reading spine and
  in the proposed D1 craft-source subsection; Parnas 1972 information hiding; the
  contested-metric honesty note — McCabe/Shepperd; the worked-examples / expertise-reversal
  instructional finding): `references/evidence-base.md`.
- Soft prerequisite (chunking the module you must judge): module **A2** (code reading &
  chunking); related modules **A1** (execution-model events surfacing as design smells),
  **D2** (names — a leak often shows up first as a lying name), **D3** (refactoring *toward*
  depth — the fix for a shallow module).
- Golden exemplars (~3 per tier, each with a **runner-verified** behavioral anchor + the
  design verdict + the located complexity): `exemplars/D1/foundations.md`,
  `exemplars/D1/working.md`, `exemplars/D1/advanced.md`.
