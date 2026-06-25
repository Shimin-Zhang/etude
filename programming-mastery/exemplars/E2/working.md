# E2 — Working exemplars (architectural & technical judgment)

Golden drills for the **Working** tier of module E2. Each is a **real but resolvable** tradeoff
— a component that *looks* worth adding, a call that *looks* fine, a split that *looks* clean.
The skill is to **name the tradeoff on both sides, name what breaks first, and resist the
one-sided answer** ("a cache is always faster"). Design judgment is **rubric-graded**
(`drill-generation.md` §3) and **softer than any executable pass** — the coach says so; every
**failure-mode** anchor below is **confirmed by running it** (`drill-generation.md` §2), but the
**verdict is never machine-decided**:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct points — **a cache's hidden cost / staleness** (W1) · **no bounded wait
/ overload** (W2) · **distribute-or-not / partial failure** (W3). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7: **E-tradeoff** = both sides (buys AND
costs); **E-failure/change** = what breaks first / the new failure mode; **E-honesty** = a
defensible verdict with at least a gesture at the condition. **A learner who names only the
benefit (or only the cost) is a partial pass — flag it** (§5c: cost-blindness / one-sided
tradeoff).

---

## W1 — Should we add a cache? (buys speed, costs staleness)

**Context.** Reads of a price are "slow"; a teammate proposes a **read-through cache** over the
source of truth. The source can change.

```python
source = {"price": 100}
cache = {}
def get_price_cached(key):
    if key not in cache:
        cache[key] = source[key]     # populate once, never invalidate
    return cache[key]
```

> **Your turn:** A cache makes reads faster — so is this a clear win? Name what it **buys**, what
> it **costs**, and **what breaks first**. Would you ship it as written?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the cache returns **stale** data after the source moves)

```
first read : 100        # from source
source now : 130        # the source of truth changes
cached read: 100        # STILL 100 -- stale!
stale? True
status: ok
```

**Gold verdict (the design judgment).**

> **Not a clear win — and not as written.** The cache **buys** read speed (a real benefit *if*
> reads are hot and the source is slow). It **costs** the thing people skip: a **new failure
> mode — staleness**. The runner shows it bluntly — the source moves to `130`, and the cache
> still serves `100` (`stale? True`). It also adds **carry/operational cost**: invalidation
> logic, a TTL to tune, memory to bound, another thing to reason about. **What breaks first:**
> the first time the underlying price changes, every reader gets a wrong number until something
> invalidates — a correctness bug, not just a latency one. **Verdict (tradeoff + condition):**
> a cache here is worth it **only if** stale reads are *tolerable for a bounded window* (then
> add a TTL and accept the staleness budget) **or** you can invalidate on write. If reads must
> be current, the cache is the wrong tool — fix the read path instead. "Cache = faster" is half
> the judgment; the other half is "stale = wrong, for how long, and is that OK?"

**Why.** Cost-blindness is the headline Working failure (§5c): a component's benefit is easy to
see, its new failure mode is not. The runner makes the invisible cost visible — caching is the
canonical "famous as a speedup, infamous for invalidation" tradeoff.

**Diagnoses.** A learner who says *"yes, caching makes it faster"* and stops has **scored one
side** (§5c: cost-blindness). A learner who names the staleness failure mode, the invalidation
cost, **and** states the condition (tolerable staleness window → TTL; else don't) hits the
E-tradeoff + E-honesty bars. If a learner insists "the cache is fine," **run it** and show
`cached read: 100` against `source now: 130`.

---

## W2 — No timeout on a downstream call (bound your waits)

**Context.** A synchronous call to a downstream service. There is **no timeout** — *"the
downstream is fast, it's fine."*

```python
def call_downstream():
    while True:          # downstream never returns (hung peer / deadlock / GC pause)
        pass

print("calling downstream with no timeout...", flush=True)  # flush: the kill discards buffered stdout
call_downstream()        # the caller waits... forever
```

> **Your turn:** Which fallacy is this assuming, and **what breaks first** when it's false? What
> would you add, and what does *that* cost?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — with no bound, the caller hangs; the sandbox kills it)

```
calling downstream with no timeout...
status: timeout        (returncode: null, duration ~5.0s -- the process never returned)
```

**Gold verdict (the design judgment).**

> It assumes **latency is zero and the network is reliable** (fallacies #1, #2): that the
> downstream always responds promptly. When it doesn't — a hung peer, a deadlock, a GC pause, a
> dropped connection — **the caller hangs with it.** The runner makes it literal: the process
> never returns and is killed at the limit (`status: timeout`). **What breaks first:** under any
> downstream slowness, caller threads/connections **pile up waiting**, and one slow dependency
> **cascades** into the caller's own exhaustion — a classic failure amplification. **Fix and its
> cost:** add a **bounded timeout** (and usually a retry-with-backoff *if the call is
> idempotent*, plus a circuit breaker under sustained failure). The cost: you must now **handle
> the timeout** — decide the fallback (error, default, degraded mode), which is real work and a
> real decision. But a bounded failure you handle beats an unbounded wait that takes you down.
> **Condition:** the only time "no timeout" is defensible is a genuinely in-process,
> can't-block call — the moment it crosses a boundary, bound the wait.

**Why.** Designing for failure (§3, axis 1): an unbounded wait turns *someone else's* failure
into *your* outage. The runner's `status: timeout` is the design's failure mode made
executable — the caller really does hang.

**Diagnoses.** A learner who says *"fine, the downstream is fast"* has **assumed a fallacy**
(§5c: happy-path-only). A learner who names the cascade ("slow dependency → caller exhaustion"),
adds a bounded timeout, **and** notes the fallback decision is the new cost is solid. Push for
the **idempotency** link: a retry is only safe if the call is idempotent (ties the worked
example) — that's the Advanced bridge.

---

## W3 — Split into two services, or keep one process? (partial failure)

**Context.** An order flow does `validate` then `charge`. A teammate proposes splitting them
into **two services** (separate processes over a network) "for independent scaling and deploys."

```python
# In-process: validate+charge happen together; either both run or neither.
def in_process(order):
    if order["amount"] <= 0:
        return "rejected"
    order["charged"] = True
    return "charged"

# "Distributed" sketch: charge is a REMOTE call that can fail AFTER validate committed state.
def distributed(order, remote_ok):
    order["validated"] = True            # committed in service 1
    if not remote_ok:                    # the network call to service 2 fails
        return "validated-but-not-charged"
    order["charged"] = True
    return "charged"
```

> **Your turn:** What does the split **buy**, what does it **cost**, and **what breaks first**
> that the single process didn't have to worry about?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (behavior — the split introduces a **partial-failure** gap)

```
in-process     : charged                  {'amount': 30, 'charged': True}
distributed ok : charged                  {'amount': 30, 'validated': True, 'charged': True}
distributed bad: validated-but-not-charged {'amount': 30, 'validated': True}   <- inconsistent
status: ok
```

**Gold verdict (the design judgment).**

> The split **buys** independent scaling, independent deploys, and team/ownership boundaries —
> real benefits **at the scale and org size that need them.** It **costs** the eight fallacies:
> the call between services can **fail partway**, and there's **no transaction across the wire**.
> The runner shows the new failure mode the single process never had — when the remote charge
> fails *after* validate committed local state, the order is left
> **`validated-but-not-charged`**: **inconsistent state split across the gap.** **What breaks
> first:** the first network blip between the two services leaves orders half-done, and now you
> need sagas / compensating actions / idempotency / retries to repair what one process got for
> free. **Verdict (tradeoff + condition):** keep it **one process** unless you can name the
> pressure that forces the split — independent scaling of one half, separate deploy cadence, a
> team boundary. If you *do* split, the cost is **designing for partial failure explicitly**
> (idempotent charge keyed by order id, a saga or outbox to reconcile). Distribution is a cost
> you pay when *forced*, not a default.

**Why.** Distributed-by-default is a core Working/Advanced trap (§5c): a boundary you didn't
need buys you every fallacy. The runner's `validated-but-not-charged` is the partial failure the
in-process version structurally cannot have.

**Diagnoses.** A learner who says *"yes, microservices scale better"* has **gone distributed by
default** (§5c) — named a benefit, ignored the partial-failure cost. A learner who names the
partial-failure gap, the reconciliation cost, **and** the condition that justifies a split
(named scaling/deploy/team pressure) is solid and reaches the Working bar. The Advanced
extension: *what makes the charge safe to retry across that gap?* → idempotency + ordering (see
`advanced.md` A3).
