# AGENTS.md

This repository aims for high-quality, readable Python. Favor clarity, small diffs, and strong tests over cleverness.

## Prime directives (in order)

1. **Correctness first** (tests + types + clear behavior).
2. **Readability over cleverness** (optimize for the median maintainer).
3. **Smallest change that works** (minimal diff; avoid unrelated refactors).
4. **Consistency with existing code** (follow local patterns unless improving them is the task).
5. **Performance only when justified** (measure, document, and constrain it).

---

## How to run things (default)

Prefer modern tooling. If the repo differs, follow the repo’s existing commands.

### Setup

- Create/sync env: `uv sync`
- Run a command in the env: `uv run <cmd>`

### Format + lint

- Format: `uv run ruff format .`
- Lint + autofix: `uv run ruff check . --fix`

### Type check

- Type check: `uv run ty check`

### Tests

- Run tests: `uv run pytest`
- Fast subset (if configured): `uv run pytest -q`
- Specific test(s): `uv run pytest path/to/test_file.py -k name_fragment`

> If any command fails, fix the underlying issue instead of working around the tool.

---

## Coding style

- Prefer modern Python (3.12+). Use modern typing syntax (`list[str]`, `X | Y`, etc.).
- Keep the “cleverness ceiling” around **list comprehensions**.
  - Avoid dense generator pipelines, heavy functional patterns, and non-obvious lambdas.
  - If you use a more advanced construct, add clarity (naming, intermediate variables).
- Prefer small functions with descriptive names.
- Avoid deep nesting; use guard clauses and early returns.
- Prefer stdlib when reasonable; keep dependencies minimal.

---

## Comments, TODOs, and docs

### Comments

- Add comments only when they explain **why**, not **what**.
- Don’t restate code in English.

### TODO/FIXME conventions

Use explicit tags and actionable context:

- `TODO(<owner or issue>): <what> — <why> (optional)`
- `FIXME(<owner or issue>): <what is broken> — <impact>`

Avoid vague TODOs like “cleanup later”.

### Docstrings

- Public functions/classes/modules should have docstrings.
- Prefer describing behavior, constraints, and edge cases.
- If performance constraints exist, document them in the docstring and (if relevant) link to benchmarks/profiling notes.

---

## Project structure

- Files should have a **single purpose**.
- Group related files by domain (e.g. `models/devices.py` over `device_models.py`).
- Keep imports simple; avoid circular imports.
- Avoid side effects at import time.
  - Do not execute code in `__init__.py` beyond defining exports.
- Prefer a `src/` layout for packages when applicable.

---

## Abstractions & reuse

- A little repetition is fine.
- Use the **rule of three**:
  - First time: implement simply.
  - Second time: repeat (if still small).
  - Third time: extract a shared helper with a clear name and tests.
- Don’t create “frameworks” or generic abstractions without at least 2–3 real call sites.

---

## Error handling

- Raise specific exceptions with clear messages.
- Avoid `except Exception:` unless you re-raise with context or are at a boundary (CLI, job runner).
- Never silently swallow exceptions.
- Use `raise ... from e` when wrapping to preserve causal context.

---

## Async guidelines

- Use async **only** in async codebases.
- Don’t introduce async purely for speculative performance.
- Avoid mixing sync and async APIs in the same module unless unavoidable and clearly documented.

---

## Performance rules

- Do not optimize blindly.
- If performance matters:
  - Measure first (benchmark/profile).
  - Constrain the optimization to the smallest scope.
  - Add documentation explaining **why this is special** and what trade-offs exist.
  - Add a test that protects the critical behavior (and a benchmark if appropriate).

---

## Testing rules (TDD-friendly)

- Prefer TDD: write the failing test first when adding/changing behavior.
- Tests should be deterministic and isolated.
- Test behavior, not implementation details.
- Use parametrization/fixtures to reduce duplication.
- Add property-based tests for “rule-like” logic when it improves coverage.

---

## Anti-patterns to avoid (slop list)

- Mutable default args.
- Hidden I/O at import time.
- Code execution in `__init__.py`.
- Overly clever one-liners.
- Broad exception catching without re-raise/context.
- Excessive mocking / testing internals instead of behavior.
- Premature abstraction and “manager” god-objects.
- Adding dependencies for trivial utilities.

---

## Definition of done (before considering a change complete)

- `ruff format` and `ruff check` pass.
- `ty check` passes (or types are intentionally omitted with a clear reason).
- `pytest` passes.
- New/changed behavior has tests.
- Docs/comments updated where behavior or constraints changed.
- No unrelated refactors or drive-by style changes.

---

## Scripts

For single-file scripts, prefer uv script mode / inline dependencies when appropriate. This is an example:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
import httpx
```

Keep scripts small, explicit, and safe to run.
