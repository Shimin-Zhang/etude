# B1 — Advanced exemplars (decomposition & planning)

Golden drills for the **Advanced** tier of module B1. Each problem **combines two or more
interacting sub-systems**, *or* the **decomposition choice itself changes the difficulty** (a
good split makes the hard part tractable; a bad one creates an intractable interface or solves
the wrong problem). The learner must **justify why this decomposition and sequence**, name the
**load-bearing uncertainty**, **and teach-back the principle** — unaided. B1 plans are
**rubric-graded** (`drill-generation.md` §3); the gold's **composition check** was confirmed by
running the implemented pieces (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct Advanced lessons (an **order-dependent state machine** / an
**interface/IR is the whole design** / a decomposition that **composes but solves the wrong
problem**). Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against module
§7: all four dimensions **solid and unaided**, plus the **teach-it-back** of the principle. A
plan that composes but can't justify *why this split* is a partial pass — flag it.

---

## A1 — Replay a bank ledger (an order-dependent state machine)

**Problem.** Plan `replay(ops)`: given a list of operations applied **in order** —
`('deposit', acct, amt)`, `('withdraw', acct, amt)`, `('transfer', src, dst, amt)` — compute the
final balances and the **count of rejected operations**. A withdraw/transfer is **rejected**
(does nothing) if the source can't cover it; accounts start at `0`. No code — decompose it,
name the hard part, and tell me **why** you'd structure it this way.

> **Your turn:** Decompose this. What's the load-bearing property of the problem, what's the
> hard sub-problem, and how do you sequence it?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold decomposition.**
- **Understand:** input an **ordered** `list[op]`; output `(balances: dict, rejected: int)`. The
  **load-bearing property: this is a sequential state machine — the ops are order-dependent and
  cannot be reordered or parallelized.** A later deposit **cannot rescue** an earlier
  withdraw that was already rejected. This insight reframes the whole plan: it's a *fold over a
  mutable state*, not a set of independent calculations.
- **The hard sub-problem — the per-op transition, especially `transfer`:** `transfer` is **two
  coupled updates** (debit src, credit dst) that must happen **together and only if the guard
  passes**; the overdraft **guard** is the policy decision (reject-and-continue, not raise).
- **Sub-problems (one altitude):**
  1. `apply(state, op)` → new state + a `rejected` increment, dispatching on op kind. *(the hard
     box: the guarded transition, incl. the coupled transfer)*
  2. `fold(ops)` → thread the state through the ops **in order**, summing rejections.
  3. `summarize(state)` → `(balances, rejected)`.
- **Why this split:** isolating `apply` as a pure transition makes the **order-dependence
  explicit** (it's the thing `fold` threads) and makes each op kind **independently testable**.
- **Edge cases:** overdraft withdraw (rejected, balance unchanged); **order matters**
  (`withdraw` then `deposit` ≠ `deposit` then `withdraw`); transfer that overdrafts (rejected,
  *neither* account moves); withdraw from an unknown account (balance `0` → rejected).

**Composition check (runner-verified — the pieces compose):**

```
replay([('deposit','a',100),('withdraw','a',30),('transfer','a','b',50)]) -> ({'a': 20, 'b': 50}, 0)
replay([('withdraw','a',50),('deposit','a',100)])                         -> ({'a': 100}, 1)   (order: deposit can't rescue the rejected withdraw)
replay([('deposit','a',10),('transfer','a','b',50)])                      -> ({'a': 10}, 1)    (transfer overdraft -> neither account moves)
replay([('withdraw','z',5)])                                              -> ({}, 1)           (unknown acct -> 0 -> rejected)
status: ok
```

**Why.** The Advanced insight is naming the **shape** of the problem — a sequential state machine
— which dictates the decomposition (fold a guarded transition over ordered ops). The
`('withdraw','a',50),('deposit','a',100)` case is the proof: the answer **depends on order**, so
any plan that treats the ops as independent is wrong regardless of how cleanly it composes.

**Teach-it-back (the principle).** *"First identify the problem's shape. Order-dependence means
it's a state machine — a fold over mutable state — not a bag of independent computations, and the
hard box is the guarded transition. Get the shape wrong and a tidy plan computes a confidently
wrong answer."*

**Diagnoses.** A plan that computes each account's net independently has **missed the
order-dependence** (§5c, solving-the-wrong-problem) — it can't model "rejected then rescued." A
plan that treats `transfer` as two unrelated steps has a **broken interface** (§5c) — the debit
and credit must be coupled under one guard. Strong plan: names the state-machine shape, isolates
the guarded transition (with transfer coupled), threads it in order, surfaces the
order-dependence edge case.

---

## A2 — Evaluate `+ - * ( )` expressions (the interface *is* the design)

**Problem.** Plan `evaluate(s)`: evaluate an arithmetic string over non-negative integers with
`+`, `-`, `*`, and parentheses, honoring precedence and left-associativity — e.g. `"2+3*4"` →
`14`, `"(2+3)*4"` → `20`. No code — decompose it, and tell me where the **real** difficulty lives.

> **Your turn:** Decompose this. What are the pieces, and — crucially — what **data flows between
> them**? Where's the hard part?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold decomposition.**
- **Understand:** input a `str`; output an `int`. Precedence: `*` binds tighter than `+`/`-`;
  parentheses override; `-` and `+` are left-associative.
- **The hard part — the intermediate representations (the interfaces between pieces *are* the
  problem).** You **cannot** evaluate the string directly (precedence and nesting make a
  left-to-right pass wrong). The design decision is the **two interfaces**: `str` → **token
  stream** → **value via a precedence-aware parse**. Choosing those data shapes *is* solving the
  problem; the code in each box is then routine.
- **Sub-problems (one altitude):**
  1. `tokenize(s)` → `list[str]` (numbers and the operators/parens as separate tokens).
  2. `parse_expr` / `parse_term` / `parse_factor` → a **recursive-descent** walk of the token
     stream that **encodes precedence in the call structure** (`expr` handles `+`/`-` over
     `term`s; `term` handles `*` over `factor`s; `factor` is a number or a parenthesized `expr`).
     *(the load-bearing box — precedence lives here)*
- **Why this split:** the **grammar layering** (expr→term→factor) is what makes precedence fall
  out *for free* — a flat "scan and compute" decomposition would have to special-case precedence
  and nesting and becomes intractable. The decomposition choice changes the difficulty.
- **Edge cases:** precedence `"2+3*4"` (=14, not 20); parens `"(2+3)*4"`; left-assoc `"10-2-3"`
  (=5, not 11); mixed `"2*3+4*5"`; nested/redundant parens `"((1+2))*3"`.

**Composition check (runner-verified — the pieces compose):**

```
evaluate('2+3*4')     -> 14    (precedence: * before +)
evaluate('(2+3)*4')   -> 20    (parens override)
evaluate('10-2-3')    -> 5     (left-associative, not 11)
evaluate('2*3+4*5')   -> 26
evaluate('((1+2))*3') -> 9     (nested parens)
status: ok
```

**Why.** This is the canonical "**the decomposition is the solution**" problem: once you commit
to `str → tokens → precedence-aware parse`, every box is easy; without those interfaces the
problem is a thicket of special cases. Naming the **data shapes between pieces** is the entire
Advanced skill here.

**Teach-it-back (the principle).** *"When a flat pass is intractable, the design is the **choice
of intermediate representations**. Layering the grammar (expr→term→factor) encodes precedence in
the structure, so the hard requirement is handled by the *shape* of the decomposition, not by
special cases."*

**Diagnoses.** A plan of "scan left to right and compute as you go" has the **wrong shape** — it
will get precedence and nesting wrong (§5c, solving-the-wrong-problem / template-matching a
left-fold). A plan that says "tokenize then evaluate" without naming the **token-stream → value**
contract or how precedence is encoded has an **undefined interface** (§5c) — the omitted contract
is the whole problem. Strong plan: the two interfaces named, precedence located in the layered
parse, left-associativity surfaced as a deciding edge case.

---

## A3 — Critique a decomposition that *composes but solves the wrong problem*

**Problem.** A teammate needs `is_balanced(s)` — are the parentheses in `s` balanced? They
decomposed it as:

```
1. count_open(s)  -> number of '('
2. count_close(s) -> number of ')'
3. compare        -> balanced iff the two counts are equal
```

> **Your turn:** This decomposition is balanced, composes cleanly, and runs without error. Is it
> **correct**? If not, give the exact input that breaks it, the right decomposition, and the
> principle this illustrates.
>
> (Take your best guess — wrong attempts are useful data.)

**Gold answer.** The decomposition is **well-formed but encodes the wrong model.** "Balanced"
is **not** "equal counts" — it also requires that **at no prefix do the closes exceed the opens**
(a `)` must never come before its matching `(`). So `")("` has **equal counts** and is
**unbalanced**. The plan composes and runs; it answers a **different question** than the contract.
- **Right decomposition — a single left-to-right scan with a running `depth`:**
  1. `scan(s)` → walk the string, `+1` on `(`, `-1` on `)`; **fail immediately if `depth` ever
     goes negative** (a close with no open).
  2. `result` → balanced iff `scan` never went negative **and** ends at `depth == 0`.
- The load-bearing insight: the problem needs **order/structure** (a stack/depth), which a
  **count** throws away.

**Composition check (runner-verified — counting vs the correct scan):**

```
'(())' : count== -> True   stack/scan -> True
')('   : count== -> True   stack/scan -> False   <-- equal counts, but UNBALANCED
'(()'  : count== -> False  stack/scan -> False
''     : count== -> True   stack/scan -> True
'())(' : count== -> True   stack/scan -> False   <-- equal counts, but UNBALANCED
status: ok
```

The counting plan calls `")("` and `"())("` **balanced** — the exact inputs that expose that
"equal counts" is the wrong contract.

**Why.** This is the module's headline lesson at full strength: **a decomposition can be balanced,
compose cleanly, and run — and still be wrong**, because *fit between pieces* is a different
question from *fidelity to the contract* (§5d — "a clean run doesn't prove the plan is good").
The fix isn't structural tidiness; it's choosing a decomposition whose pieces preserve the
**ordering information** the problem actually needs.

**Teach-it-back (the principle).** *"Verify a decomposition against the **contract**, not just
that the pieces fit. 'Equal counts' is a lossy model — it discards order — so it composes
perfectly and answers the wrong question. When the problem cares about structure, the
decomposition must carry that structure (a depth/stack), not summarize it away."*

**Diagnoses.** A learner who says "the boxes fit, looks right" judged by **composition, not
contract** (§5c, solving-the-wrong-problem) — and the runner convicts the plan on `")("`. A
learner who senses it's wrong but can't produce the **deciding input** has the intuition without
the **edge-case discipline** (§5c, happy-path-only). Strong answer: names `")("` as the deciding
input, re-decomposes to a depth-scan with the fail-on-negative rule, and states the principle —
*check the decomposition against the contract; a lossy model composes and lies.*
