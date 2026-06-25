# D1 — Working exemplars (managing complexity / abstraction)

Golden drills for the **Working** tier of module D1. Each has a **real but resolvable**
judgment with a **tempting wrong answer** (the kind a reviewer optimizing for "short methods"
or "use a class" would fall for). The skill is **triage of design**: reach the right verdict,
**locate the actual complexity**, justify it at the interface, and **resist the decoy**.
Design judgment is **rubric-graded** (`drill-generation.md` §3) and **softer than an
executable pass**; every **behavioral** claim below was **confirmed by running it**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct shapes — **pull-complexity-down vs leave-it-up** (W1) ·
**looks-deep-but-shallow** (W2) · **complexity-moved-not-reduced** (W3). Pose one,
**hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7: **D-judge** =
the right verdict; **D-locate** = the actual complexity, not a decoy; **D-justify** =
interface-vs-implementation + which symptom. **Reaching the right verdict for the wrong reason
is a partial pass — flag it** (e.g. "it's deep because the methods are short").

---

## W1 — Pull the complexity down, or leave it to the caller?

**Spec.** `line_total(qty, price)` returns the cost of a cart line. **`price` may be `None`**
(an unpriced item), which must count as `0`.

Two designs, same behavior. **A** leaves the `None`-handling to the caller; **B** pulls it
into the function:

```python
def line_total_A(qty, price):
    return qty * price                                   # caller must guard None

def line_total_B(qty, price):
    return qty * (price if price is not None else 0)     # module owns the None case
```

> **Your turn:** Which design is **deeper**, and why? (Consider what each caller has to write,
> and what happens on a cart that contains an unpriced item.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — both reach the same total when callers cope)

```
cart = [(2, 5.0), (1, None), (3, 2.0)]
# caller of A must repeat the guard at the call site, then:
total_A -> 16.0
# caller of B just sums:
total_B -> 16.0
same? True
status: ok
```

**Gold verdict (the design judgment).**

> **B is deeper — prefer it.** The contract explicitly includes the unpriced-item case
> (`price is None → 0`), so handling it is *part of this function's job*, not the caller's. B
> **pulls that complexity down**: it absorbs the special case once, so every caller writes the
> obvious `sum(line_total_B(q, p) for q, p in cart)`. A leaves the special case **up**: every
> caller must remember to guard `None` (the evidence shows the A-caller doing exactly that
> extra `price if price is not None else 0` at the call site) — and a caller who forgets gets
> a `TypeError` on the first unpriced item. Same output, but A's missing-case decision is
> **leaked and duplicated** across call sites (cognitive load now, change amplification if the
> rule changes). This is Ousterhout's "simple interface > simple implementation": B's body is
> marginally less pretty; B's *interface* is strictly kinder.

**Why.** "Pull complexity downward" (§3, corollary 2 of the mental model; §8 anti-pattern
"moving complexity"). When a special case belongs to the contract, the module should own it —
the win is every caller getting simpler, paid for by a slightly busier implementation.

**Diagnoses.** A learner who says *"A is cleaner — the function stays simple and callers can
decide"* has **optimized a simple implementation over a simple interface** (§5c: wants to pull
complexity up). "Callers can decide" is the leak: they must decide, every time. A learner who
picks B and names the duplicated guard / change-amplification cost is solid. If they argue
"they're behaviorally identical so it doesn't matter," **show the runner** — identical output,
**different complexity** (the central D1 point; §5d partial-pass).

---

## W2 — Looks deep (it's a class!), is shallow

**Context.** An `Account` "model." It has six methods and reads like a real abstraction.

```python
class Account:
    def __init__(self):
        self._d = {}
    def set_name(self, v): self._d["name"] = v
    def get_name(self): return self._d["name"]
    def set_email(self, v): self._d["email"] = v
    def get_email(self): return self._d["email"]
    def set_balance(self, v): self._d["balance"] = v
    def get_balance(self): return self._d["balance"]
```

> **Your turn:** Is `Account` a **deep** abstraction? Does it **pay for itself** over a plain
> dict — and why?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the "abstraction" doesn't even guard its own contract)

```
a = Account(); a.set_name("Ada"); a.set_balance(100)
a.get_name(), a.get_balance()  -> Ada 100
a.get_email()                  -> KeyError: 'email'     # before set_email; same as a bare dict
status: ok  (the KeyError path is caught in the demo)
```

**Gold verdict (the design judgment).**

> **Shallow — it does not pay for itself.** Being a class with six methods is **structure, not
> depth**: every method is a one-line pass-through to `self._d`, so the interface surface
> (`set_name/get_name/set_email/get_email/set_balance/get_balance`) is **as large as the data
> it hides** and hides **no work and no decision**. A caller must still know every field
> exists, in what order to set them, and — as the runner shows — `get_email()` raises
> `KeyError` before `set_email()`, *exactly* as a bare `dict` would. So the twelve lines of
> interface buy almost nothing over `account = {"name": ..., "balance": ...}`. This is
> Ousterhout's **"classitis"**: splitting into many tiny members *raises* total complexity
> (more names, more places to look) without hiding anything. It would earn its keep if it hid
> a real decision — validation (reject a malformed email), an invariant (balance never
> negative), a computed field, or a storage format behind the getters. As written, delete it
> or deepen it.

**Why.** Depth is measured **at the interface** (§3.1; §8 "counting structure instead of
hiding"). "It's a class / it has methods / the methods are short" are the exact decoys this
drill plants — none of them is hiding.

**Diagnoses.** A learner who says *"deep — it's a proper class, encapsulates the fields, each
method does one thing"* has the **root inversion** (§5c: deep because it's a class / methods
are short). This is the single most common D1 error and the one that collides with naïve
"Clean Code." A learner who says "shallow — every method is a pass-through, the interface
hides nothing the dict didn't" is solid; bonus for naming *what* would deepen it (validation /
invariant / hidden format = a likely-to-change decision, Parnas).

---

## W3 — The helper that moved the complexity into kwargs

**Context.** Someone "extracted a helper" to centralize number formatting.

```python
def fmt(value, *, as_currency, thousands, decimals, prefix, suffix, parens_negative):
    s = f"{abs(value):,.{decimals}f}" if thousands else f"{abs(value):.{decimals}f}"
    if as_currency: s = "$" + s
    s = prefix + s + suffix
    if parens_negative and value < 0: s = "(" + s + ")"
    return s
```

> **Your turn:** Did this helper **reduce** complexity, or just **move** it? Is `fmt` a deep
> abstraction — and why?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — it works; the question is the design, not correctness)

```
fmt(-1234.5, as_currency=True, thousands=True, decimals=2,
    prefix="", suffix="", parens_negative=True)            -> ($1,234.50)
fmt(99.0, as_currency=False, thousands=False, decimals=0,
    prefix="~", suffix=" units", parens_negative=False)    -> ~99 units
status: ok
```

**Gold verdict (the design judgment).**

> It **moved** complexity, it didn't reduce it — so `fmt` is **shallow** despite hiding the
> formatting *mechanics*. Six required keyword arguments mean every caller must understand and
> supply **six independent decisions** every single time (look at the evidence: each call is a
> wall of `as_currency=..., thousands=..., decimals=..., prefix=..., suffix=...,
> parens_negative=...`). The caller's old if-ladder didn't disappear; it **relocated into the
> signature**. The interface is nearly as complex as the work it does — the tell of a shallow
> module. **Deepen it** by hiding the *decisions*, not just the string ops: offer a few
> **named, intention-revealing** entry points that each bundle a coherent decision set —
> `money(value)` → `"($1,234.50)"`, `count(value, unit)` → `"~99 units"` — built on a private
> core. Now a caller writes `money(-1234.5)`: one decision, the common cases hidden. (This is
> *pull complexity down*, not *move it sideways into kwargs*; §3.3, §8.)

**Why.** An abstraction pays for itself only by removing **more** complexity than it adds
(§3.3). A pile of flags is the caller's decision load wearing a function's clothes — the
indirection is real, the hiding is not.

**Diagnoses.** A learner who says *"deep — one reusable function, DRY, handles every case"*
has **confused configurability with depth** (§5c: moving complexity, not reducing it; "added a
layer / kwargs ⇒ improvement"). DRY at the implementation can still be a shallow, high-load
interface. A learner who sees the six-decision load on every caller and proposes named
intention-revealing wrappers is solid (D-judge + D-justify + the deepening). Watch for the
*over-correction* (§5c over-engineering): inventing a formatter-strategy class hierarchy is
swapping one shallow shape for a heavier one — the fix is a couple of named functions, not a
framework.
