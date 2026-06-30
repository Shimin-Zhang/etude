# C2 — Advanced exemplars (reading stack traces & errors)

Golden drills for the **Advanced** tier of module C2. Each **combines two or more** reading
skills: the **site is far from the cause** (≥2 frames up), the deepest frame is a **library**,
or the trace is **chained**. The skill is to name type + site + cause **and explain *why* the
raise site is not the fix site** — and, for chains, **which traceback holds the original
cause**. Every traceback below is **real runner output** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Advanced parameter space across **three distinct wrinkles**: a
`ZeroDivisionError` whose cause is empty data **two frames up**; a **chained** traceback
where an over-broad `except` masks the real `KeyError`; and a `JSONDecodeError` whose
**deepest frames are the stdlib** (walk up to your code). Pose one, **paste the real
traceback when grading**, **hard-stop, wait** (`coaching-loop.md`). **How to grade** (§5d,
hybrid): **executable** = correct *class* + *deepest your-code frame* (+ for chains, which
traceback is the original); **rubric** = the cause walk + *why site ≠ fix*. Report
separately, and at this tier also ask for a **teach-it-back** of the four-move procedure.

---

## A1 — `ZeroDivisionError`: a correct line, an empty list two frames up

**What the code does.** `per_group` maps each group name to the `average` of its values;
`average` divides the sum by the count.

```python
def average(nums):
    return sum(nums) / len(nums)

def per_group(groups):
    return {name: average(vals) for name, vals in groups.items()}

report = {
    "north": [10, 20, 30],
    "south": [],
    "east": [5, 15],
}
print(per_group(report))
```

> **Your turn:** This raises. Name the **class**, the **line** it raised on, and **the
> cause** — and explain why the line the trace points at is **not** the line to fix.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`, paths shown as `snippet.py`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 12, in <module>
    print(per_group(report))
          ~~~~~~~~~^^^^^^^^
  File "snippet.py", line 5, in per_group
    return {name: average(vals) for name, vals in groups.items()}
                  ~~~~~~~^^^^^^
  File "snippet.py", line 2, in average
    return sum(nums) / len(nums)
           ~~~~~~~~~~^~~~~~~~~~~
ZeroDivisionError: division by zero
```

So: **class `ZeroDivisionError`**; **raise site line 2**, at `sum(nums) / len(nums)` (the
caret `~~~~~~~~~~^~~~~~~~~~~` sits on the `/`); **cause**: `len(nums) == 0` because `nums` is
the empty list — and walking up, that empty list is `"south": []` in `report`, passed through
the dict-comprehension frame (line 5) from line 12. **Why the site is not the fix:** line 2's
division is correct for any non-empty list; the bug is that an **empty group** reaches
`average` at all. The fix is upstream — guard `average` (`if not nums: return 0.0`) or filter
empty groups in `per_group` — *not* at the division.

**Why.** Bottom line first: `ZeroDivisionError: division by zero` — a `/` (or `%`) had a zero
denominator. The deepest frame (line 2) and the caret on `/` tell you `len(nums)` is `0`. But
the **cause** is *which* call passed an empty list: read **up** through the dict-comprehension
frame (line 5) to the data at line 12, where `"south": []` lives. Two frames separate the
**site** (line 2) from the **cause** (the empty-list datum). This is the Advanced move:
the trace points at a *correct* line, and the fault is the data flowing into it.

**Diagnoses.** A learner who proposes "add a check on line 2" is on the right track only if
they realize they're fixing the *contract* (`average` of empty), not the division operator. A
learner who can't say *which* group is empty hasn't walked the chain up to the data (§5c,
site≠cause). A learner who stops at "ZeroDivisionError, line 2" without the cause has the
executable half but not the rubric half — **partial pass**, flag it. Strong read:
`ZeroDivisionError` + line 2 site + "`"south": []` is empty; fix the empty-group contract,
not the `/`."

---

## A2 — A **chained** traceback: an over-broad `except` masking the real cause

**What the code does.** `enrich` looks up each id via `fetch_row`; on *any* exception it
re-raises a friendly `ValueError`.

```python
def fetch_row(table, rid):
    return table[rid]

def enrich(table, ids):
    results = []
    for rid in ids:
        try:
            results.append(fetch_row(table, rid))
        except Exception:
            raise ValueError(f"could not process id {rid}")
    return results

rows = {1: "Ada", 2: "Linus", 3: "Grace"}
print(enrich(rows, [1, 2, 5]))
```

> **Your turn:** This raises a **chained** traceback. There are two exceptions — **which is
> the original cause**, which is the wrapper, and **what is the real fault**? (And: was the
> second raised *while handling* the first, or *because of* it?)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 8, in enrich
    results.append(fetch_row(table, rid))
                   ~~~~~~~~~^^^^^^^^^^^^
  File "snippet.py", line 2, in fetch_row
    return table[rid]
           ~~~~~^^^^^
KeyError: 5

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "snippet.py", line 14, in <module>
    print(enrich(rows, [1, 2, 5]))
          ~~~~~~^^^^^^^^^^^^^^^^^
  File "snippet.py", line 10, in enrich
    raise ValueError(f"could not process id {rid}")
ValueError: could not process id 5
```

So: **two linked exceptions.** The **original cause is the `KeyError: 5`** in the **first
(top) traceback** — `fetch_row` indexed `table[5]` and `rows` has no key `5` (only `1, 2,
3`). The **wrapper is the `ValueError`** in the second (bottom) traceback, raised by the
over-broad `except Exception` on line 10. The chaining line **"During handling of the above
exception, another exception occurred"** means the second was raised **while handling** the
first (implicit `__context__`, PEP 3134) — *not* an explicit `raise … from`. **The real
fault**: id `5` is not in `rows` (a missing-key / data problem); the `ValueError` is just a
relabel that *hides* the precise `KeyError`.

**Why.** With a chained traceback you must read **both** sections and the **banner** between
them. The bottom error (`ValueError: could not process id 5`) is what propagated to the top
level, but it is a **wrapper** — the `except Exception: raise ValueError(...)` on line 10
caught something and re-raised. The banner tells you which: "During handling…" = the wrapper
was raised *while handling* the original, so the original is in the **first** traceback:
`KeyError: 5` at line 2. That `KeyError` is the actionable fault. (Had the code said `raise
ValueError(...) from exc`, the banner would instead read "The above exception was the **direct
cause**…" — same idea, explicit `__cause__`.)

**Diagnoses.** A learner who reports only "ValueError, line 10" has **ignored the chaining
banner** and missed the original cause (§5c, ignores-the-chaining-banner) — the single most
common chained-trace miss. A learner who reads both but can't say *which* is the cause hasn't
parsed "most recent call last" + the banner. A learner who can't distinguish "during
handling" (`__context__`) from "direct cause" (`raise … from`) has a partial PEP-3134 model.
Strong read: "original cause = `KeyError: 5` (first traceback, line 2 — id `5` missing); the
`ValueError` is a wrapper from the over-broad `except`; banner says it was raised *while
handling*, so look at the first traceback to fix it."

---

## A3 — A library deepest frame: walk *up* to the code you wrote

**What the code does.** `parse_payload` JSON-decodes each incoming line.

```python
import json

def parse_payload(raw_lines):
    return [json.loads(line) for line in raw_lines]

incoming = ['{"id": 1}', '{"id": 2}', "{id: 3}"]
print(parse_payload(incoming))
```

> **Your turn:** This raises, and the **deepest frames are inside the `json` library**.
> What's the **class**, **which frame is the deepest one *you* wrote**, and **what is the
> cause**? (Don't try to fix the library.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`; the stdlib path is shown by the runner as the
absolute install path — elided here to `<python>/…/json/…` since it varies by machine, but the
**frames and the exception are verbatim**)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 7, in <module>
    print(parse_payload(incoming))
          ~~~~~~~~~~~~~^^^^^^^^^^
  File "snippet.py", line 4, in parse_payload
    return [json.loads(line) for line in raw_lines]
            ~~~~~~~~~~^^^^^^
  File "<python>/lib/python3.13/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "<python>/lib/python3.13/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "<python>/lib/python3.13/json/decoder.py", line 361, in raw_decode
    obj, end = self.scan_once(s, idx)
               ~~~~~~~~~~~~~~^^^^^^^^
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

So: **class `json.decoder.JSONDecodeError`**; **deepest frame overall is `json/decoder.py`
(library)** — but the **deepest frame *you wrote* is line 4** in `parse_payload`, at
`json.loads(line)`; **cause**: the third element of `incoming`, `"{id: 3}"`, is **not valid
JSON** — its key `id` is not wrapped in double quotes (the message even pinpoints "line 1
column 2 (char 1)"). The fix is at *your* boundary (line 4 / the input), not in the `json`
package.

**Why.** Bottom line first: `JSONDecodeError: Expecting property name enclosed in double
quotes` — the parser hit malformed JSON, and the message gives the exact position. The
**deepest frames** (`json/__init__.py`, `json/decoder.py` ×2) are **library internals** — you
can tell because their paths are under the Python install (`<python>/lib/python3.13/json/…`),
not your file. Mature libraries like `json` are not where the bug is; **walk up** past them to
the deepest frame *you* wrote: line 4, `json.loads(line)`. That is the boundary where your
code fed bad input to the library. The cause is the input `"{id: 3}"` (unquoted key). Fix:
correct the data, or validate/`try` around `json.loads` and handle the malformed line.

**Diagnoses.** A learner who points at `json/decoder.py` as "the bug" has **tried to fix
library internals** (§5c, library-frames-as-the-bug) — the defining Advanced-frame error. A
learner who names the class but stops at the deepest (library) frame hasn't done the
walk-up-to-your-code move. A learner who doesn't recognize the install path as "not my code"
lacks the your-code/library boundary distinction. Strong read: `JSONDecodeError` + "deepest
*my* frame is line 4 `json.loads(line)`" + "the cause is the unquoted-key string `"{id: 3}"`
in the input; fix it at my boundary, not in `json`."
</content>
</invoke>
