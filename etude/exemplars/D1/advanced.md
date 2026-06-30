# D1 — Advanced exemplars (managing complexity / abstraction)

Golden drills for the **Advanced** tier of module D1. Each is a **genuine tension or combined
symptom** — judge it, name the symptom(s) precisely, **propose the deepening**, and **state
the trade-off** (including when the shallow/other version is actually right). The skill is
design judgment *with a justified fix*, articulated as a principle. Design judgment is
**rubric-graded** (`drill-generation.md` §3) and **softer than an executable pass**; every
**behavioral** anchor below was **confirmed by running it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct combined symptoms — **change amplification from a leaked decision
across call sites** (A1) · **general-purpose deep interface vs special-purpose shallow ones**
(A2) · **obscurity / unknown-unknowns behind a clean-looking interface** (A3). Pose one,
**hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7: **D-judge** =
the right verdict; **D-locate** = the precise symptom(s); **D-justify** =
interface-vs-implementation + the deepening + the trade-off (incl. when the other choice
wins). Articulating the **principle** (teach-it-back) is the Advanced bar.

---

## A1 — Change amplification: a leaked decision duplicated across call sites

**Context.** A discount rule — *10% off when the price is over $100* — appears at multiple
call sites instead of behind one interface. Compare the **shallow** spread to the **deep**
encapsulation; then watch what happens when the business changes the threshold to $50.

```python
# SHALLOW: each site re-encodes the rule
def price_a(x): return x * 0.9 if x > 100 else x   # site 1
def price_b(x): return x * 0.9 if x > 100 else x   # site 2 (duplicated decision)

# DEEP: the rule lives behind ONE interface; callers don't know the threshold
class Pricing:
    THRESHOLD = 100
    RATE = 0.9
    def discounted(self, x):
        return x * self.RATE if x > self.THRESHOLD else x
```

> **Your turn:** Name the complexity **symptom** the shallow version suffers from, and explain
> what it costs when the discount rule changes. What's the deepening, and is there *any* case
> where the spread-out version is acceptable?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — a *partial* edit produces a real inconsistency)

```
# before any change, all three agree:
shallow a: 135.0   b: 135.0        deep: 135.0

# business changes threshold to 50; developer edits site 1 but MISSES site 2:
after partial edit -> a: 67.5   b: 75   (inconsistent!)
status: ok
```

**Gold verdict (the design judgment).**

> The shallow version suffers **change amplification** (and the dependency that causes it): the
> *design decision* "discount = 10% over $100" is **duplicated** at every call site, so a
> "simple" rule change requires finding and editing **every** site. The runner makes the cost
> concrete — change the threshold to 50, edit `price_a` but miss `price_b`, and the system is
> now **silently inconsistent** (`67.5` vs `75` for the same input). That's not just extra
> typing; it's a **correctness hazard** scaling with the number of call sites, and an
> unknown-unknown for the next reader (which sites encode the *current* rule?). **Deepening:**
> hide the decision behind one interface — `Pricing.discounted` (or a function with the
> constants in one place) — so callers say `pricing.discounted(x)` and **the rule changes in
> exactly one place** (Parnas: hide the likely-to-change decision; a pricing rule is
> *paradigmatically* likely to change). **Trade-off / when the spread is OK:** if the
> expression were a truly **stable, trivial** computation used in two adjacent lines (not a
> business rule that will move), a tiny duplication can be fine — DRY is not absolute. The
> trigger here is that it's a *volatile decision* duplicated across *distant* sites; that's
> what makes the abstraction pay for itself.

**Why.** Change amplification is the headline symptom of a leaked/duplicated decision (§3
table; §8). The drill teaches the Parnas test directly: *is the thing duplicated a decision
likely to change?* If yes, hide it once.

**Diagnoses.** A learner who says *"just be careful to update both / add a comment"* has
treated a **structural** problem as a **discipline** problem (§5c: misses an information leak /
tolerates duplication of a decision) — the runner's inconsistency shows discipline fails. A
learner who names change-amplification, ties it to the volatile decision, gives the
single-source deepening, **and** notes when trivial duplication is acceptable is solid and
hits the Advanced "trade-off" bar.

---

## A2 — General-purpose deep interface vs a pile of special-purpose shallow ones

**Context.** A text buffer. Design **Deep** offers two general primitives; the **Shallow**
sketch would offer one special method per UI action. Each UI action (backspace, delete-word,
paste) is expressible from the two primitives.

```python
class DeepBuffer:
    def __init__(self, s=""): self.s = s
    def insert(self, pos, text): self.s = self.s[:pos] + text + self.s[pos:]
    def delete(self, pos, n):    self.s = self.s[:pos] + self.s[pos+n:]

class ShallowBuffer:                       # the special-purpose alternative (sketch)
    def __init__(self, s=""): self.s = s
    def backspace_at(self, pos): self.s = self.s[:pos-1] + self.s[pos:]    # leaks "pos-1"
    def delete_range(self, a, b): self.s = self.s[:a] + self.s[b:]         # near-dup of delete
    # ...and paste_at, delete_word_at, ... one shallow method per action
```

> **Your turn:** Which interface is **deeper**, and why is "more methods, each tailored to an
> action" the *wrong* instinct here? Is there a case where a special-purpose method earns its
> place?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — both reach the same edited text)

```
# DeepBuffer: backspace+type expressed via the two primitives
DeepBuffer("hello world"): delete(5,6); insert(5,"!")  -> 'hello!'
# ShallowBuffer: a tailored method gets the same result
ShallowBuffer("hello world"): delete_range(5,11) (+ "!") -> 'hello!'
same core? True
status: ok
```

**Gold verdict (the design judgment).**

> **`DeepBuffer` is deeper** — and it's the *smaller* interface that does *more*. Two general
> primitives (`insert`, `delete`) **compose** to express every editing action: backspace is
> `delete(pos-1, 1)`, delete-word is a `delete` over a computed span, paste is `insert`. The
> special-purpose design needs a **new method per action**, each one **shallow** (a thin slice
> manipulation) and each **leaking cursor arithmetic** like `pos-1` into the interface — so the
> interface grows without hiding more, and `backspace_at`/`delete_range` are near-duplicates of
> the same logic. Ousterhout's point exactly: a **general-purpose deep module** beats a pile of
> special-purpose shallow ones; "more methods, each matching a use case" mistakes **surface
> tailoring for depth**. **Trade-off / when a special method earns its place:** if an operation
> is **common and its derivation is non-trivial or error-prone** (e.g. "delete the current
> word respecting Unicode boundaries"), a *named* method built **on top of** the primitives can
> pay for itself — it hides a real decision (the boundary rule) and reads at the call site. The
> rule is: keep the **general core**, and add a thin named convenience only when it hides
> genuine complexity, never as the *primary* interface.

**Why.** "Define errors (and special cases) out of existence" and "general-purpose modules are
deeper" (Ousterhout): a small composable core hides more than many tailored entry points
(§3.1; §5b general-vs-special). The fix direction is *combine*, not *add*.

**Diagnoses.** A learner who says *"the special methods are better — they're convenient and
match exactly what the UI needs"* has chosen **surface tailoring over depth** (§5c: counting
structure / many small pieces; "different is not better"). A learner who picks the two
primitives, notes the leaked `pos-1` and the near-duplication, **and** carves out the
legitimate convenience-method case is solid. Push for the principle (teach-it-back): *a
general interface that composes is deeper than N special ones that each hide little.*

---

## A3 — Obscurity: a clean interface with a hidden, surprising contract

**Context.** A `Service.fetch(key)` looks like a deep, one-call abstraction. But to use it
*correctly* you must know something its interface never tells you.

```python
class Service:
    def __init__(self): self._cache = {}
    def fetch(self, key):
        if key in self._cache:
            return {"key": key, "value": self._cache[key], "ready": True}
        self._cache[key] = key.upper()                      # side effect hidden in a "getter"
        return {"key": key, "value": None, "ready": False}  # first call: value is None!
```

> **Your turn:** `fetch` has a small, simple interface — so is it **deep**? Identify the
> complexity it actually imposes, name the symptom, and say how you'd fix it.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the surprising contract, made visible)

```
s = Service()
s.fetch("a")   -> {'key': 'a', 'value': None, 'ready': False}   # first call: value is None,
                                                                #   and state was mutated
s.fetch("a")   -> {'key': 'a', 'value': 'A', 'ready': True}     # second call: now it's there
status: ok
```

**Gold verdict (the design judgment).**

> **Not deep — a small interface is necessary but not sufficient.** `fetch` hides the lookup
> *mechanics*, but it leaks complexity through **obscurity**: its **contract is hidden and
> surprising**. The runner shows it — the **first** call for a key returns `value=None,
> ready=False` *and silently mutates the cache*, while the **second** returns the real value.
> A caller cannot know any of this from the name `fetch` or its signature; they will write
> `fetch("a")["value"]`, get `None`, and ship a bug. That's an **unknown-unknown** — the worst
> symptom (Ousterhout): you don't even know there's a thing you needed to know. Complexity =
> dependencies + **obscurity**, and a clean-looking interface with an obscure contract is
> still complex. **Fixes:** make the abstraction actually deep by **removing the surprise** —
> populate the cache and return the ready value in **one** call (`return {'value': self._get(key),
> 'ready': True}`), so `fetch` always yields a usable result; or, if laziness is essential,
> make the contract **obvious and honest** (a blocking `get(key) -> value`, or an explicit
> two-step `prime(key)` / `get(key)` whose names *say* the protocol). A "getter" should not
> have a surprising side effect or a cold-cache half-result. **Trade-off:** genuine laziness
> can be worth it, but its cost must be *paid in the interface's honesty*, not hidden.

**Why.** Obscurity is complexity even when the interface is small (§3 table; §5c: misses
obscurity / unknown-unknowns). This drill breaks the over-simple heuristic "small interface ⇒
deep" — depth requires that the interface let you use the code **correctly**, which an obscure
contract defeats.

**Diagnoses.** A learner who says *"deep — one method, simple signature, hides the cache"* has
**equated small-interface with deep** and missed the obscurity (§5c: misses obscurity /
unknown-unknowns). This is the subtle Advanced trap. A learner who runs (or reasons) to the
`value=None`-on-first-call contract, names it an unknown-unknown, and proposes either
single-call readiness or an honest explicit protocol is solid. If a learner *insists* it's fine
("the caller can just call twice"), **show the runner**: nothing in the interface tells them to,
which is the whole point.
