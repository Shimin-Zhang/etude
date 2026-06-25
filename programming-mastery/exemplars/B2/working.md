# B2 — Working exemplars (code writing & composition)

Golden drills for the **Working** tier of module B2: each spec **hides exactly one edge case a
naive version misses**. The learner must **name the edge before coding**, compose in **verified
steps**, and pass the **full battery including the edge**. Two verdicts, reported separately
(B2 §5d):

- **Product (executable):** the coach **runs the learner's function** against the battery —
  every expected value below was obtained by running a reference solution, never guessed:

  ```
  python <skill-dir>/runtime/python/runner.py snippet.py
  ```

- **Process (rubric, softer):** spec/edge named before coding? composed in confirmed steps?
  stopped at the contract? Passing only the happy path, **or** passing the full battery via a
  big-bang write, is a **partial pass — flag the half that fell short.**

Coverage spans **distinct edge classes** — **boundary / don't-append** (truncate) /
**normalization** (is_palindrome) / **remainder / non-divisible** (chunk) — no repeated gotcha.
Each drill also carries a **naive version** whose bug the battery catches. Per
`coaching-loop.md`, pose one drill, **hard-stop and wait**.

---

## WW1 — `truncate(s, n)` (hidden edge: don't append when the string already fits)

> **Your turn:** Write `truncate(s, n)` — if `len(s) <= n`, return `s` unchanged; otherwise
> return the first `n` characters of `s` followed by `"..."`.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
truncate("hello world", 5) = "hello..."   # truncated -> first 5 + "..."
truncate("hi", 5)          = "hi"         # EDGE: len 2 <= 5 -> unchanged, NO "..."
truncate("exact", 5)       = "exact"      # EDGE: len 5 == 5 (boundary) -> unchanged
truncate("exactly7", 5)    = "exact..."   # len 8 > 5 -> truncated
truncate("", 5)            = ""           # empty -> unchanged
status: ok
```

**Gold reference solution:**

```python
def truncate(s, n):
    if len(s) <= n:
        return s
    return s[:n] + "..."
```

**The naive miss (runner-confirmed):**

```python
def truncate_naive(s, n):
    return s[:n] + "..."        # always appends
```
```
truncate_naive("hi", 5) = "hi..."     # WRONG -- appends "..." to a string that fits
```

**Why.** The spec has a **guard the happy path hides**: when the string already fits in `n`,
nothing should be appended. A naive `s[:n] + "..."` "works" on the typical long input
(`"hello world"` → `"hello..."`) and is **wrong** on every short input. The boundary `len(s) ==
n` is the subtle one — `"exact"` is exactly 5 chars and must come back **unchanged**. Composing
in verified steps means running `truncate("hi", 5)` *before* declaring done and seeing `"hi"`,
not `"hi..."`.

**Diagnoses.** A learner who writes the naive one-liner and runs only `truncate("hello world",
5)` has the **happy-path-only** habit (Catalog §5c, entry 2): the long input hides the
don't-append boundary. The fix is to **name the "string already fits" edge in the spec step**
and run a short input. (If the learner *names* the edge but forgets the `==` boundary, that is a
**boundary slip** — Catalog §5c — caught by `truncate("exact", 5)`.)

---

## WW2 — `is_palindrome(s)` (hidden edge: normalize case and non-alphanumeric first)

> **Your turn:** Write `is_palindrome(s)` — return `True` iff `s` reads the same forwards and
> backwards, **ignoring case and any non-alphanumeric characters** (spaces, punctuation).
> Example: `"A man, a plan, a canal: Panama"` → `True`.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
is_palindrome("racecar")                       = True
is_palindrome("A man, a plan, a canal: Panama") = True   # EDGE: punctuation + case ignored
is_palindrome("hello")                          = False
is_palindrome("")                               = True   # empty reads same both ways
is_palindrome("Ab")                             = False  # case-folded "ab" != "ba"
status: ok
```

**Gold reference solution:**

```python
def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]   # normalize FIRST
    return cleaned == cleaned[::-1]
```

**The naive miss (runner-confirmed):**

```python
def is_palindrome_naive(s):
    return s == s[::-1]        # compares raw string, spaces/case/punctuation and all
```
```
is_palindrome_naive("A man, a plan, a canal: Panama") = False   # WRONG (spaces/case/commas)
```

**Why.** The spec's real work is in **two composed pieces**: *normalize* (drop non-alphanumeric,
fold case) **then** *compare to the reverse*. A naive raw `s == s[::-1]` passes the clean cases
(`"racecar"`, `"hello"`) and **fails the moment punctuation or capitals appear** — exactly the
headline example. The normalization step is not optional polish; it is half the spec.

**Diagnoses.** A learner who composes only the `s == s[::-1]` comparison has **missed an edge
class baked into the spec** ("ignoring case and non-alphanumeric") — happy-path-only at the
*spec-reading* level (Catalog §5c, entries 2 & 3). Running the punctuated headline input is the
confirm step that exposes it. A learner who normalizes but forgets `.lower()` fails on `"Ab"` —
a partial normalization, caught by that case.

---

## WW3 — `chunk(xs, k)` (hidden edge: keep the short final remainder)

> **Your turn:** Write `chunk(xs, k)` — split `xs` into consecutive sub-lists of length `k`.
> The **last chunk may be shorter** if `len(xs)` is not a multiple of `k`. Example:
> `chunk([1,2,3,4,5], 2)` → `[[1,2],[3,4],[5]]`.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified battery**

```
chunk([1, 2, 3, 4, 5, 6], 2) = [[1, 2], [3, 4], [5, 6]]   # even split
chunk([1, 2, 3, 4, 5], 2)    = [[1, 2], [3, 4], [5]]      # EDGE: remainder [5] kept
chunk([1, 2, 3], 5)          = [[1, 2, 3]]                # k > len -> one short chunk
chunk([], 2)                 = []                         # empty -> empty
chunk([1, 2, 3, 4], 4)       = [[1, 2, 3, 4]]             # exact one chunk
status: ok
```

**Gold reference solution:**

```python
def chunk(xs, k):
    out = []
    for i in range(0, len(xs), k):
        out.append(xs[i:i + k])      # slice is safe past the end -> short final chunk
    return out
```

**The naive miss (runner-confirmed):**

```python
def chunk_naive(xs, k):
    out = []
    for c in range(len(xs) // k):    # len//k chunks -> DROPS the remainder
        out.append(xs[c * k:c * k + k])
    return out
```
```
chunk_naive([1, 2, 3, 4, 5], 2) = [[1, 2], [3, 4]]    # WRONG -- silently drops [5]
```

**Why.** The edge is the **non-divisible remainder**. `range(0, len(xs), k)` strides to (and
past) the end, and Python's slice `xs[i:i+k]` is **safe past the end**, so the last chunk comes
out short automatically. The naive `range(len(xs) // k)` computes *floor* chunks — `5 // 2 == 2`
— and **silently drops the tail**. Composing in steps: run `chunk([1,2,3,4,5], 2)` and confirm
the `[5]` survives.

**Diagnoses.** A learner whose loop runs `len(xs) // k` times has an **off-by-one / boundary
error in the composed logic** (Catalog §5c — boundary) that *only* shows on non-divisible input.
Running an even split (`[1,2,3,4,5,6]`) hides it; running the remainder case (`[1,2,3,4,5]`)
exposes it. The fix is to **name "len not a multiple of k" as the edge** and confirm it before
finishing.
