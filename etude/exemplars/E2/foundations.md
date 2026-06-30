# E2 — Foundations exemplars (architectural & technical judgment)

Golden drills for the **Foundations** tier of module E2. Each is a **plainly** over-built,
failure-ignoring, or hardcoded design — *no genuine tension*. The skill is **seeing the failure
or the over-build and naming the tradeoff** in buys/costs/breaks-first terms: *what does this
buy and cost? · what breaks first? · would you build this?* Design judgment is **rubric-graded**
(`drill-generation.md` §3) and **the softest grading in the curriculum** — the coach says so out
loud; where a design has a concrete failure mode, the **failure is proven by running it**
(`drill-generation.md` §2), but the **verdict is never machine-decided**:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct points — **over-build / YAGNI** (F1) · **design-for-failure / a fallacy
assumed** (F2) · **under-build / no seam for the named change** (F3). Pose one, **hard-stop,
wait** (`coaching-loop.md` → Pause for input). **How to grade** against module §7: **E-tradeoff**
= named what it buys *and* costs; **E-failure/change** = named what breaks first / the fallacy /
the seam; **E-honesty** = a defensible verdict, no cargo-cult. **A learner who defends a design
as "scalable / future-proof / the standard way" with no cost named has the inverted model —
flag it** (§5c root: judged by the happy path and the pattern, not by cost and failure).

---

## F1 — Over-build: a framework for a feature that doesn't exist yet

**Context.** A teammate built a pluggable "strategy" framework to send the welcome email, *"so
we can add SMS and push later."* Today there is exactly **one** channel: email.

```python
class Channel:
    def send(self, to, msg): raise NotImplementedError
class EmailChannel(Channel):
    def send(self, to, msg): return f"email->{to}:{msg}"
class Notifier:
    def __init__(self): self._channels = {}
    def register(self, name, ch): self._channels[name] = ch
    def notify(self, name, to, msg): return self._channels[name].send(to, msg)

# vs. the two-liner that does the same job today
def send_email(to, msg): return f"email->{to}:{msg}"
```

> **Your turn:** Does the framework **pay for itself** today? What does it **buy**, what does it
> **cost**, and would you build it now?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the framework and the two-liner are identical *today*)

```
over-built: email->ada:welcome
simple    : email->ada:welcome
same behavior today? True
status: ok
```

**Gold verdict (the design judgment).**

> **Don't build it yet — it's a presumptive feature (YAGNI).** Today the framework **buys
> nothing** the two-liner doesn't: the runner shows identical behavior (`same behavior today?
> True`) for a single channel. What it **costs** is real and immediate — Fowler's **cost of
> carry**: the registry, the base class, and the dispatch are extra complexity to read,
> modify, and debug *now*, paying for a second/third channel that may never arrive (and if it
> does, may not look like this guess). **What breaks first:** nothing breaks, but every future
> change to notification logic is now heavier than it needed to be. **The nuance that keeps
> this honest:** YAGNI forbids the *speculative feature*, **not** a cheap seam — `send_email`
> is *already* an easy place to extend, and if a real second channel is named and imminent,
> generalizing *then* (a small refactor) is cheap and safe. Build the seam when the change is
> real; don't build the framework on spec.

**Why.** This is YAGNI made concrete (§3.2): a presumptive feature pays **cost of build +
carry** now for an uncertain future benefit, and the runner shows the benefit is currently
zero. "Easy to change later" is the point — that's *why* you don't need it now.

**Diagnoses.** A learner who says *"good — it's extensible / future-proof / the right pattern"*
has **over-built** (§5c: reaches for machinery for a need that doesn't exist; cargo-cults a
pattern). A learner who says "build nothing speculative, keep `send_email`, generalize when a
real second channel lands" is solid, and naming the cost-of-carry is the E-tradeoff bar. Push
anyone who says "just delete the abstraction" to notice the *seam* is fine to keep — it's the
*framework* that doesn't pay yet.

---

## F2 — Design for failure: a function that assumes the happy path

**Context.** `plan_price` reads a user's plan from a service **response** and returns the price.

```python
def plan_price(response):
    return {"free": 0, "pro": 20}[response["plan"]]   # assumes "plan" present and known
```

> **Your turn:** This works in every demo. **What breaks first** in production — which
> assumption is it making, and what does that cost?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the happy path passes; a degraded response crashes)

```
happy: 20
[then, on a degraded / partial response — plan_price({}):]
Traceback (most recent call last):
  File "snippet.py", line 5, in <module>
    print("degraded:", plan_price({}))   # a degraded / partial response
                       ~~~~~~~~~~^^^^
  File "snippet.py", line 2, in plan_price
    return {"free": 0, "pro": 20}[response["plan"]]   # assumes "plan" present and known
                                  ~~~~~~~~^^^^^^^^
KeyError: 'plan'
status: error
```

**Gold verdict (the design judgment).**

> It assumes **the network is reliable and the response is always well-formed** — fallacy #1,
> and the happy-path-only reflex. The runner shows the happy case (`20`) and then the failure
> the design ignored: a **degraded or partial response** (a timeout fallback, a new plan value,
> a missing field — all common) makes `response["plan"]` raise `KeyError`, and an *unknown* but
> *present* plan would raise too. **What breaks first:** the first time the upstream is slow,
> mid-deploy, or adds a plan, this line throws — and depending on where it sits, that's a 500
> to the user or a crashed worker. **Cost/fix:** the design needs to **decide what a degraded
> response means** — a default (`response.get("plan", "free")`), an explicit error the caller
> can handle, or a validated contract — *before* indexing. The point isn't the one-liner; it's
> that a reliable design **names the unhappy path** the fallacy hides.

**Why.** Designing for failure (§3, axis 1) starts with naming the fallacy you're assuming.
The coach **runs the failure** rather than asserting it (Surface ground truth) — the green
`happy: 20` is exactly the demo that lulls you; the `KeyError` is the production reality.

**Diagnoses.** A learner who says *"looks fine, it returns the price"* has **happy-path-only
reasoning** (§5c) — they judged the demo, not the design. A learner who names "it assumes the
field is always present / the call always succeeds" and proposes a default-or-explicit-error is
solid (E-failure/change). If a learner *disputes* that it breaks, **run `plan_price({})`** and
show the `KeyError`.

---

## F3 — Under-build: a decision hardcoded where a seam was warranted

**Context.** A sales-tax rule — *7%* — is written directly at **two** call sites, not behind one
interface.

```python
def price_cart(subtotal):
    return subtotal + subtotal * 0.07      # 7% tax -- site 1
def price_quote(subtotal):
    return subtotal + subtotal * 0.07      # 7% tax -- site 2 (same decision, duplicated)
```

> **Your turn:** What design risk is hiding here? Name what it costs when the tax rate changes
> — and is this the *opposite* mistake from over-building?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — a *partial* edit silently diverges)

```
cart : 107.0
quote: 107.0
[business changes the rate to 9%; a dev edits site 1, misses site 2:]
after partial edit -> cart: 109.0   quote: 107.0   (inconsistent!)
status: ok
```

**Gold verdict (the design judgment).**

> The tax rate is a **decision that is *likely to change*** (rates change by law and by region),
> and it's **duplicated** across call sites instead of hidden behind one seam — this is
> **under-building**, the dual of over-building. **What it costs:** when the rate changes to 9%,
> the change is a **shotgun edit** — and the runner shows the failure mode when a dev edits one
> site and misses the other: the system is now **silently inconsistent** (`109.0` vs `107.0`
> for the same input), a correctness bug that scales with the number of call sites. **What
> breaks first:** the next rate change. **Fix (the seam):** put the rate behind one
> function/constant (`apply_tax(subtotal)`), so the change lands in **one place** (Parnas: hide
> the likely-to-change decision). **Note the symmetry with F1:** YAGNI says don't build the
> *speculative framework*, but it explicitly **does** endorse this cheap seam — because the
> change here is *named and certain*, not presumptive.

**Why.** Design-for-change (§3, axis 2): hide the decision you can *name* as likely to change.
This is the half YAGNI does **not** forbid (§3.2, the Fowler nuance) — the runner's silent
inconsistency is the cost of skipping a seam that was warranted.

**Diagnoses.** A learner who says *"just remember to update both / add a comment"* has treated a
**structural** problem as a **discipline** problem (§5c: hardcoded likely-to-change decision) —
the runner's inconsistency shows discipline fails at scale. A learner who names the
likely-to-change decision, the change-amplification cost, and the one-place fix is solid; the
*Advanced* extension is to contrast it with F1 and articulate when a seam pays (named change)
vs. when it's over-build (presumptive feature).
