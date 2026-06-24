# C2 — Foundations exemplars (reading stack traces & errors)

Golden drills for the **Foundations** tier of module C2. Each is a **shallow** traceback —
single frame or fault-at-the-raise-site — for one common exception. The skill is to **name
the exception class, point at the fault line, and state the cause in one sentence**. Every
traceback below is **real runner output**, obtained by running the buggy snippet through the
runner (`drill-generation.md` §2) — the coach never guesses the traceback:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans the Foundations parameter space across **three different exception classes**
(`TypeError` in an accumulator · `AttributeError` on the wrong object · `NameError` from a
typo) and the three §5c categories they map to (wrong type · wrong object · namespace/scope).
Per `coaching-loop.md`, the coach poses one drill, **pastes the real traceback when grading**
(surface ground truth), then **hard-stops and waits** — the answer key is for *grading*,
never shown before the learner attempts. **How to grade** (§5d, hybrid): **executable** =
correct *class* + *fault line* (verbatim against `stderr`); **rubric** = the *cause* in one
sentence. Report the two separately.

---

## F1 — `TypeError` in an accumulator: a string hiding in a numeric list

**What the code does.** `total_cost(items)` sums a list of prices.

```python
def total_cost(items):
    total = 0
    for price in items:
        total += price
    return total

cart = [9.99, 4.50, "3.00", 1.25]
print(total_cost(cart))
```

> **Your turn:** This raises. What is the **exception class**, **which line** raised it, and
> **what is the cause** (in one sentence)?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`, paths shown as `snippet.py`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 8, in <module>
    print(total_cost(cart))
          ~~~~~~~~~~^^^^^^
  File "snippet.py", line 4, in total_cost
    total += price
TypeError: unsupported operand type(s) for +=: 'float' and 'str'
```

So: **class `TypeError`**; **fault line 4**, `total += price` (in `total_cost`); **cause**:
the fourth list element is the *string* `"3.00"`, and `float += str` is undefined — the data
has a string where the loop expects a number.

**Why.** Read the **bottom line first**: `TypeError: unsupported operand type(s) for +=:
'float' and 'str'` — the *class* says "wrong type for the operation," and the message names
both types (`'float'` and `'str'`). Then the **deepest frame** is line 4 `total += price`.
The line is correct for numbers; the **cause** is the value flowing in — on the third
iteration `price` is `"3.00"`, a string. (Note the trace does *not* say which iteration; the
class + message + the list literal are enough to find the offending element.)

**Diagnoses.** A learner who says "it's a list error" or guesses without naming the class has
**skimmed and guessed from the symptom** (§5c, guessing-from-the-symptom) — grade the
*reading*, not the lucky direction. A learner who names `TypeError` but cannot point at line
4 has a **localization** gap (§5c, names-class-without-frame). Strong read: class + line 4 +
"a string `"3.00"` is in the numeric list."

---

## F2 — `AttributeError`: calling a string method on the wrong object

**What the code does.** `normalize(tags)` trims and lowercases each tag.

```python
def normalize(tags):
    result = []
    for t in tags:
        result.append(t.strip().lower())
    return result

print(normalize(["  Python ", "Rust", 42, "Go"]))
```

> **Your turn:** This raises. What is the **exception class**, **which line** raised it, and
> **what is the cause**?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 7, in <module>
    print(normalize(["  Python ", "Rust", 42, "Go"]))
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "snippet.py", line 4, in normalize
    result.append(t.strip().lower())
                  ^^^^^^^
AttributeError: 'int' object has no attribute 'strip'
```

So: **class `AttributeError`**; **fault line 4**, at `t.strip()` (the caret `^^^^^^^` sits
under `t.strip`); **cause**: the third element is the *int* `42`, and ints have no `.strip()`
method — the list mixes strings with a non-string.

**Why.** Bottom line first: `AttributeError: 'int' object has no attribute 'strip'`. The
class signals "this object doesn't have the attribute/method you asked for," and the message
names the offending type (`'int'`) and the missing attribute (`'strip'`). That is almost
always a **wrong-object** problem — here, an `int` where a `str` was expected. The 3.11+
caret narrows the site to `t.strip` on line 4. The cause is the data: `42` is not a string.

**Diagnoses.** `AttributeError` on a method very often means the object is `None` or the
wrong type — a learner who treats the class as meaningless ("just an error") misses that
free categorization (§5c, ignores-the-class). A learner who says "the strip is broken" and
wants to fix `normalize`'s logic has the **site** but not the **cause** (the input is wrong,
not the line). Strong read: class + line 4 + "the int `42` has no `.strip()`."

---

## F3 — `NameError`: a one-character typo in the namespace

**What the code does.** `greet(name)` builds a greeting string.

```python
def greet(name):
    return "Hello, " + nam

print(greet("Ada"))
```

> **Your turn:** This raises. What is the **exception class**, **which line** raised it, and
> **what is the cause**?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key** (real `stderr`)

```
status: error
Traceback (most recent call last):
  File "snippet.py", line 4, in <module>
    print(greet("Ada"))
          ~~~~~^^^^^^^
  File "snippet.py", line 2, in greet
    return "Hello, " + nam
                       ^^^
NameError: name 'nam' is not defined. Did you mean: 'name'?
```

So: **class `NameError`**; **fault line 2**, at `nam` (caret under `nam`); **cause**: `nam`
is a typo — the parameter is `name`, but line 2 references the undefined name `nam`. (Python
3.11+ even suggests the fix: *"Did you mean: 'name'?"*.)

**Why.** Bottom line first: `NameError: name 'nam' is not defined`. The class signals a
**namespace** problem — a name was read that isn't bound in any reachable scope (A1: names
are labels bound to objects; `nam` was never bound). The deepest frame is line 2; the caret
isolates `nam`. The cause is the typo, and the interpreter's *"Did you mean: 'name'?"* points
straight at it.

**Diagnoses.** A learner who reads the **top** frame (line 4, `print(greet("Ada"))`) as "the
error line" has the **stack order backwards** (§5c, reads-the-stack-upside-down) — "most
recent call last" means the **bottom** frame (line 2) is the failure. A learner who confuses
this with `UnboundLocalError` (a *scope* event — see Working W3) misreads the class. Strong
read: `NameError` + line 2 + "`nam` is an undefined name — typo for `name`."
</content>
</invoke>
