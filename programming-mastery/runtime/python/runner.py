# programming-mastery/runtime/python/runner.py
"""Sandboxed execution of Python snippets for drill ground-truth.

v1 threat model: this runs coach-generated drill snippets and the learner's own
practice code. It is a ROBUSTNESS sandbox (timeout + address-space/CPU limits to
stop runaway loops and memory blowups), NOT a security boundary against
deliberately hostile code. Container-level isolation is future work (spec §10
risk #2).
"""
from __future__ import annotations

import dataclasses
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    import resource  # Unix-only
except ImportError:  # pragma: no cover - non-Unix fallback
    resource = None


@dataclasses.dataclass
class RunResult:
    status: str           # "ok" | "timeout" | "error"
    stdout: str
    stderr: str
    returncode: int | None
    duration_s: float

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))


def _limit_resources(mem_mb: int, cpu_s: int) -> None:
    """preexec_fn run in the child before exec: cap memory and CPU (Unix)."""
    if resource is None:  # pragma: no cover
        return
    mem_bytes = mem_mb * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s))


def run_snippet(code: str, *, timeout_s: float = 5.0, mem_mb: int = 256) -> RunResult:
    """Execute `code` as an isolated Python process and capture its output.

    Ordinary errors in `code` surface as status="error" (never raised); only
    harness misuse raises.
    """
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "snippet.py"
        script.write_text(code)
        preexec = None
        if resource is not None:
            cpu_s = max(1, int(timeout_s) + 1)
            preexec = lambda: _limit_resources(mem_mb, cpu_s)
        start = time.monotonic()
        try:
            proc = subprocess.run(
                [sys.executable, "-I", str(script)],
                capture_output=True,
                text=True,
                timeout=timeout_s,
                cwd=tmp,
                preexec_fn=preexec,
            )
        except subprocess.TimeoutExpired as exc:
            return RunResult(
                "timeout",
                exc.stdout or "",
                exc.stderr or "",
                None,
                time.monotonic() - start,
            )
        return RunResult(
            "ok" if proc.returncode == 0 else "error",
            proc.stdout,
            proc.stderr,
            proc.returncode,
            time.monotonic() - start,
        )


def main(argv: list[str]) -> int:
    """CLI: `python runner.py <script.py>` prints a RunResult as JSON."""
    if len(argv) != 2:
        print("usage: runner.py <script.py>", file=sys.stderr)
        return 2
    code = Path(argv[1]).read_text()
    print(run_snippet(code).to_json())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
