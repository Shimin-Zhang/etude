# E3 — Advanced exemplars (code review)

Golden drills for the **Advanced** tier of module E3: a **subtle** correctness / security /
concurrency / edge-case bug **hidden among plausible code** that looks correct and survives a
shallow skim (and shallow testing). **Find it, articulate the impact, propose a fix.** Code
review is rubric-graded (`drill-generation.md` §3); every bug below — and every proposed fix —
was **confirmed by running it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three hard bug classes: a broken **search invariant**, a **security** hole
(path traversal), and a **concurrency** race (lost updates). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7: **D1** = found the hidden bug (not a
hallucinated one, and didn't over-report the plausible-but-fine code); **D2** = articulated the
**impact** precisely; **D3** = proposed a **working fix** (the coach re-runs with it to confirm).
At Advanced, also ask for a **teach-it-back** of the principle ("the bug that matters is rarely
the one that's easy to see"). The bugs here pass on the obvious inputs — **a learner who only
tries the obvious inputs will approve them.**

---

## A1 — Binary search: a broken `hi` invariant (passes the extremes, fails the interior)

**Spec.** `search_insert(arr, target)` returns the index where `target` should be inserted to
keep `arr` sorted — i.e. the index of the first element `>= target` (a `bisect_left`).

```python
def search_insert(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo
```

> **Your turn:** Review this. It passes a few quick tests — but is it correct? If not, what's
> the bug, when does it bite, and how would you fix it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the bug is real and *input-dependent* — note the camouflage)

```
search_insert([1, 3, 5, 7], 0)  -> 0   == bisect_left 0   (passes — target before all)
search_insert([1, 3, 5, 7], 8)  -> 4   == bisect_left 4   (passes — target after all)
search_insert([2, 2, 2], 2)     -> 0   == bisect_left 0   (passes)
search_insert([1, 3, 5, 7], 5)  -> 1   != bisect_left 2   <-- WRONG (interior target)
search_insert([1, 3, 5, 7], 4)  -> 1   != bisect_left 2   <-- WRONG
search_insert([1, 2, 3, 4, 5], 3) -> 1 != bisect_left 2   <-- WRONG
# with the fix `hi = mid`: all six cases match bisect_left
status: ok
```

**Prioritized issue list.** One issue, blocking (correctness):
1. `hi = mid - 1` violates the half-open `[lo, hi)` invariant. The `else` branch knows
   `arr[mid] >= target`, so `mid` is still a *candidate* answer and must stay in range
   (`hi = mid`). Subtracting one **skips the correct insertion point**, returning an index one
   too low for interior targets.

**Model review comment (the gold).**

> **`hi = mid - 1` (line 7) — blocking.** This loop uses a half-open range `[lo, hi)`
> (`hi` starts at `len(arr)`). In the `else` branch we've established `arr[mid] >= target`, so
> `mid` is still a *possible* answer — it must remain in the search window, which means
> `hi = mid`, not `hi = mid - 1`. As written it discards a valid candidate and returns an index
> one short for any target that lands in the interior: `search_insert([1, 3, 5, 7], 5)` returns
> `1` but should return `2`. It happens to pass when the target is before or after every element
> (`0` → `0`, `8` → `4`), which is exactly why a couple of quick tests look green. Fix:
> `hi = mid`. Please add tests for an **interior** target and one that **equals** an element —
> that's where the invariant break shows.

**Diagnoses.** A learner who approves it after testing `0` and `8` **rubber-stamped via
insufficient inputs** (§5c, did-not-trace / rubber-stamp) — the bug is invisible unless you test
an interior value. A learner who senses "the boundary update looks off" but can't say *which
inputs fail* has a **D1/D2** gap — have them run the interior case. Strong review: names the
invariant, gives the failing input *and* a passing one (to explain the false-green tests), and
the one-character fix. Bug class: **broken loop/search invariant** (Catalog §5c; an A1
execution-model trace of the loop exposes it).

---

## A2 — "Safe" file fetch: path traversal (a security bug among plausible code)

**Spec.** `read_user_file(name)` resolves a user-supplied filename to a path **inside**
`BASE_DIR` and must **not** let the caller escape `BASE_DIR` (no `../`, no absolute paths).

```python
import os

BASE_DIR = "/srv/app/userfiles"

def read_user_file(name):
    path = os.path.join(BASE_DIR, name)
    return os.path.abspath(path)
```

> **Your turn:** Review this. It joins everything under `BASE_DIR` — is it actually safe? If
> not, what's the bug, what's the impact, and how would you fix it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the security hole is real; run with `BASE_DIR` pointed at a temp
root)

```
read_user_file("notes.txt")        -> <BASE_DIR>/notes.txt        (fine)
read_user_file("../../etc/passwd") -> /etc/passwd                 <-- escapes BASE_DIR via ../
read_user_file("/etc/passwd")      -> /etc/passwd                 <-- os.path.join DROPS BASE_DIR for an absolute arg!
# containment check that SHOULD hold: commonpath([resolved, BASE_DIR]) == BASE_DIR
#   "notes.txt" -> True ;  "../../etc/passwd" -> False ;  "/etc/passwd" -> False
# with the fix (reject when commonpath != BASE_DIR): both attacks REJECTED, "notes.txt" allowed
status: ok
```

**Prioritized issue list.** One issue, blocking (**security**):
1. No containment check after the join, so `name` can escape `BASE_DIR` two ways:
   (a) `../` sequences walk up out of the directory; and
   (b) an **absolute** `name` makes `os.path.join(BASE_DIR, "/etc/passwd")` return
   `"/etc/passwd"` — `join` *discards* `BASE_DIR` entirely when its second argument is absolute.
   This is a classic **path-traversal / arbitrary-file-read** vulnerability.

**Model review comment (the gold).**

> **`os.path.join(BASE_DIR, name)` (line 6) — blocking, security.** Joining doesn't constrain
> the result to `BASE_DIR`. Two escapes: `name = "../../etc/passwd"` walks up and out
> (`read_user_file("../../etc/passwd")` resolves to `/etc/passwd`), and an **absolute** name is
> worse — `os.path.join(BASE_DIR, "/etc/passwd")` returns `/etc/passwd`, because `join` throws
> away everything before an absolute component. Either lets a caller read any file the process
> can. We need to resolve and then **verify containment**:
> ```python
> def read_user_file(name):
>     resolved = os.path.abspath(os.path.join(BASE_DIR, name))
>     if os.path.commonpath([resolved, BASE_DIR]) != BASE_DIR:
>         raise ValueError("path escapes BASE_DIR")
>     return resolved
> ```
> Please add tests for `../` and an absolute path — both should be rejected.

**Diagnoses.** A learner who approves it ("it joins under `BASE_DIR`, looks fine") trusted the
*intent* of the code over its *behavior* (§5c, rubber-stamp; the absolute-path case is genuinely
surprising — many reviewers don't know `join` drops the prefix). A learner who spots `../` but
misses the absolute-path escape has a **partial D1** — show them the `/etc/passwd` line. Strong
review: flags it as **security/blocking**, demonstrates **both** escapes, and gives a containment
check, not a fragile string-blocklist of `..`. Bug class: **security / path traversal** (Catalog
§5c).

---

## A3 — Shared counter: a non-atomic read-modify-write (a concurrency race)

**Spec.** `Counter.increment()` is called from many threads; after all threads finish, `value`
must equal the total number of `increment()` calls.

```python
import threading, time

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        tmp = self.value
        time.sleep(0)
        self.value = tmp + 1
```

> **Your turn:** Review this for use under multiple threads. Is it correct? If not, what's the
> bug, what's the impact, and how would you fix it?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the race is real and **reliably under-counts** when the threads
start together; exact loss varies by scheduler but the under-count is consistent)

```
# 4 threads x 300 increments each, released simultaneously via a Barrier:
final counter = 300    expected = 1200    lost updates = 900   (BUG CONFIRMED — repeated across runs)
# with the fix (guard the read-modify-write with self._lock): final = 1200 == expected, every run
status: ok
```

*(The `time.sleep(0)` and the simultaneous start are just there to make the race show every run
in a drill; the bug is the non-atomic read-modify-write itself, which loses updates under real
contention regardless.)*

**Prioritized issue list.** One issue, blocking (**concurrency**):
1. `tmp = self.value; ...; self.value = tmp + 1` is a **read-modify-write with no lock**. Two
   threads can both read the same `value`, both compute `tmp + 1`, and both store it — one
   increment is **lost**. Under contention the final count is **less** than the number of calls.

**Model review comment (the gold).**

> **`increment()` (the read-modify-write, lines 8–10) — blocking, concurrency.** Reading
> `self.value` into `tmp` and writing `tmp + 1` back is not atomic, so with multiple threads two
> can interleave between the read and the write and one update is lost. It's not hypothetical:
> with 4 threads doing 300 increments each, released together, the counter lands on `300`
> instead of `1200` — 900 lost updates — and it reproduces across runs. (Don't be reassured by a
> single-threaded test; the bug only shows under contention.) Guard the critical section with a
> lock:
> ```python
> def __init__(self):
>     self.value = 0
>     self._lock = threading.Lock()
> def increment(self):
>     with self._lock:
>         self.value += 1
> ```
> With the lock the count is exact every run.

**Diagnoses.** A learner who approves it ("increments a counter, fine") reviewed it as
**single-threaded** and missed that the spec says *many threads* (§5c, no-whole-change-model —
the contract is concurrency; A4 mental model). A learner who says "might have a race" but can't
explain the **interleaving** (both read the same value) or can't show the under-count has a
**D2** gap — have them run the barrier demo. A learner who "fixes" it by making `increment`
*look* shorter without a lock hasn't fixed it (re-run to show it still loses updates). Strong
review: flags **concurrency/blocking**, explains the lost-update interleaving, shows the
under-count, and adds the lock. Bug class: **concurrency / lost update / non-atomic RMW**
(Catalog §5c; extends A1's notional machine to the concurrent one — A4).
