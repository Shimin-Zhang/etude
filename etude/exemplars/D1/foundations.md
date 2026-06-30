# D1 — Foundations exemplars (managing complexity / abstraction)

Golden drills for the **Foundations** tier of module D1. Each is a **plainly** shallow module
or a **plainly** leaked decision — *no genuine design tension*. The skill is **seeing the
leak and articulating it** in deep/shallow + interface-vs-implementation terms: *is this deep
or shallow? where is the complexity / information leak?* Design judgment is **rubric-graded**
(`drill-generation.md` §3) and explicitly **softer than an executable pass**; where a snippet
has a runnable contract, the **behavior** is confirmed by running it (`drill-generation.md`
§2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct shallowness shapes — **pass-through wrapper** (F1) · **information
leak via a flag** (F2) · **temporal decomposition / leaked ordering** (F3). Pose one,
**hard-stop, wait** (`coaching-loop.md` → Pause for input). **How to grade** against module
§7: **D-judge** = reached the right verdict (shallow / leak present); **D-locate** = put a
finger on the actual cause (the interface hides nothing / the leaked decision), not a decoy;
**D-justify** = argued depth *at the interface* and named the cost (which symptom). **A
learner who calls it "fine because the method is short / because it's a class" has the
inverted model — flag it** (§5c root: depth judged at the implementation, not the interface).

---

## F1 — The pass-through method: does it pay for itself?

**Context.** A `UserStore` wraps a dict of users. Look at `get_user_name`.

```python
class UserStore:
    def __init__(self):
        self._users = {}
    def add(self, uid, name):
        self._users[uid] = name
    def get_user_name(self, uid):          # interface as complex as impl ...
        return self._users.get(uid)        # ... a dict .get with a rename
```

> **Your turn:** Is `get_user_name` a **deep** or **shallow** part of this interface? Does it
> **pay for itself** as an abstraction — and why?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — anchors what the method actually does)

```
s = UserStore(); s.add(1, "Ada")
s.get_user_name(1)   -> Ada
s.get_user_name(99)  -> None        # a miss still leaks None to the caller
status: ok
```

**Gold verdict (the design judgment).**

> **Shallow.** `get_user_name` is a one-line **pass-through**: its interface (`get_user_name(uid)`)
> is essentially as complex as its implementation (`self._users.get(uid)`) — it hides **no
> work** and **no decision**. It buys exactly one thing over `self._users.get(uid)`:
> encapsulation of the `_users` dict (callers don't touch the field directly). That is a
> *small* real benefit, but the method **adds interface cost** (a name to learn, a place to
> look) for almost no complexity removed, and it doesn't even own the missing-key case — a
> miss still returns `None` for the caller to handle. As written it barely pays for itself;
> if it were the *only* method, a plain dict would be simpler. It would become **deep** the
> moment it hid something real — e.g. returning a default, raising a domain error on unknown
> users, or joining first/last names.

**Why.** Depth is measured **at the interface**: how much work and how much "you must know"
does it spare the caller? Here, almost none. The lesson is the "pays for itself" corollary
(§3.3): an abstraction earns its interface cost only by hiding *more* complexity than it adds.

**Diagnoses.** A learner who says *"deep — it's a clean getter / good encapsulation"* has
counted **structure, not hiding** (§5c: pass-through that doesn't pay for itself; depth judged
at the implementation). A learner who says *"shallow, the interface hides nothing"* and notes
the `None` still leaks is solid (D-judge + D-locate). Push anyone who stops at "rename" to say
*what would make it deep* (hide the missing-key decision) — that's the D3/Parnas bridge.

---

## F2 — The flag that leaks an implementation decision

**Spec.** `read_lines(text)` should return the lines of a text file. (A byte-order mark — the
invisible `﻿` some editors prepend — should never end up in the data.)

```python
def read_lines(text, strip_bom):
    # strip_bom is an implementation detail leaked into the signature
    if strip_bom and text.startswith("﻿"):
        text = text[1:]
    return text.split("\n")
```

> **Your turn:** Where is the **information leak** here, and what does it cost a caller?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the leak bites when the caller guesses wrong)

```
read_lines("﻿a\nb", True)   -> ['a', 'b']                 # BOM stripped
read_lines("﻿a\nb", False)  -> ['﻿a', 'b']           # BOM leaks into the data!
status: ok
```

**Gold verdict (the design judgment).**

> The **`strip_bom` parameter is an information leak** (Parnas: the interface should *hide*
> the likely-to-change decision, not surface it). Whether the input has a BOM, and what to do
> about it, is an **implementation detail about text encoding** that the module should own —
> instead it has been pushed into the signature, so **every caller** must (a) know BOMs
> exist, (b) know this function needs to be told about them, and (c) decide correctly every
> time. The runner shows the cost: a caller who passes `False` (or forgets the argument's
> meaning) gets `'﻿a'` silently embedded in their data — a corruption they couldn't have
> predicted from the *name* `read_lines`. **Fix:** drop the flag and always handle the BOM
> internally (`text = text.removeprefix("﻿")`), or decode with a codec that strips it —
> a **simpler interface** (`read_lines(text)`) hiding the decision. That also *pulls the
> complexity down*: the encoding concern lives in one place, not at N call sites.

**Why.** This is the Parnas criterion (§3.2) made concrete: a leaked decision couples every
caller to a detail and turns "use it correctly" into "know its internals." Obscurity +
dependency, both at once.

**Diagnoses.** A learner who says *"the API is flexible — good, callers can choose"* has
**missed the leak** (§5c: misses an information leak); flexibility the caller never wanted is
just leaked complexity. A learner who flags `strip_bom` as the leak and names the corruption
cost is solid. A learner who only says "rename the parameter" has the symptom but not the cure
(D-justify partial) — the parameter shouldn't *exist*, not be renamed.

---

## F3 — Temporal decomposition: a leaked call-order invariant

**Spec.** A `Report` turns a list of rows into a printable string.

```python
class Report:
    def __init__(self):
        self._rows = None
        self._formatted = None
    def load(self, rows):
        self._rows = rows
    def format(self):
        self._formatted = ["* " + r for r in self._rows]
    def emit(self):
        return "\n".join(self._formatted)
```

> **Your turn:** This class is **shallow** in a specific way. What complexity has it pushed
> onto the caller — and what goes wrong because of it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the leaked ordering *bites* when violated)

```
# correct order load -> format -> emit:
r = Report(); r.load(["a","b"]); r.format(); r.emit()
  -> "* a\n* b"                                   status: ok

# emit() before format() -- the leaked invariant bites:
r = Report(); r.load(["a","b"]); r.emit()
  -> TypeError: can only join an iterable         status: error
     (self._formatted is still None)
```

**Gold verdict (the design judgment).**

> This is **temporal decomposition**: one logical job (rows → string) split into three methods
> that **must be called in a fixed order** — `load` → `format` → `emit` — with that ordering
> **leaked to the caller** as an unwritten precondition. The class is shallow because its
> interface (three methods + the hidden rule "call them in this sequence") is *more* complex
> than the job, not less: the caller must now hold the sequence in their head (cognitive
> load) and gets a baffling `TypeError: can only join an iterable` if they get it wrong — an
> **unknown-unknown**, since nothing in `emit`'s signature says "call `format` first." **Fix:**
> collapse it into one deep interface that owns the sequence — e.g. a single
> `Report(rows).render()` (or a function `render_report(rows)`), so the order *can't* be
> gotten wrong and the caller writes one line.

**Why.** A deep module hides a *decision*; a temporally-decomposed one hides nothing and
*exports an invariant*. The failure is the worst symptom (unknown-unknowns) made tangible —
which is exactly why the coach **runs it** to show the traceback rather than asserting "it
breaks."

**Diagnoses.** A learner who says *"deep — good separation of concerns, each method does one
thing"* has mistaken **steps-in-a-sequence for hidden complexity** (§5c: temporal
decomposition; depth judged by method count). "One thing per method" is not the goal —
*hiding* is. A learner who names the leaked ordering and the unknown-unknown failure is solid;
if they dispute that order matters, **run the out-of-order call** and show the `TypeError`.
