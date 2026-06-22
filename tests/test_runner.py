# tests/test_runner.py
import json
import sys

import pytest

from runner import run_snippet


def test_normal_output_is_ok():
    r = run_snippet("print(2 + 2)")
    assert r.status == "ok"
    assert r.stdout.strip() == "4"
    assert r.returncode == 0


def test_runtime_error_is_captured_not_raised():
    r = run_snippet("raise ValueError('boom')")
    assert r.status == "error"
    assert "ValueError" in r.stderr
    assert "boom" in r.stderr
    assert r.returncode != 0


def test_timeout_on_infinite_loop():
    r = run_snippet("while True:\n    pass\n", timeout_s=1.0)
    assert r.status == "timeout"
    assert r.returncode is None


def test_stdout_and_stderr_are_separated():
    r = run_snippet("import sys\nprint('out')\nprint('err', file=sys.stderr)\n")
    assert "out" in r.stdout and "err" not in r.stdout
    assert "err" in r.stderr


def test_to_json_roundtrips_fields():
    r = run_snippet("print('hi')")
    data = json.loads(r.to_json())
    assert data["status"] == "ok"
    assert "hi" in data["stdout"]


@pytest.mark.skipif(sys.platform == "win32", reason="resource limits are Unix-only")
def test_memory_limit_triggers_error():
    # ~1 GiB allocation under a 128 MB cap should fail (MemoryError / nonzero exit).
    r = run_snippet("x = bytearray(1024 * 1024 * 1024)\n", mem_mb=128, timeout_s=5.0)
    assert r.status == "error"


def test_timeout_with_partial_output():
    # Snippet prints before spinning -> exercises the bytes-decode path on POSIX.
    r = run_snippet(
        "import sys; print('partial', flush=True)\nwhile True: pass\n",
        timeout_s=1.0,
    )
    assert r.status == "timeout"
    assert isinstance(r.stdout, str)   # decoded, not bytes
    assert "partial" in r.stdout
    r.to_json()  # must not raise


def test_duration_s_is_positive():
    r = run_snippet("pass")
    assert isinstance(r.duration_s, float)
    assert 0.0 < r.duration_s < 5.0
