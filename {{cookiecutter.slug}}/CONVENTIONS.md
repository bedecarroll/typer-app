# You MUST follow these principles where possible

- Code should be easy to read and understand.

- Keep the code as simple as possible. Avoid unnecessary complexity.

- Use meaningful names for variables, functions, etc. Names should reveal intent.

- Functions should be small and do one thing well.

- Prefer Test Driven Development (TDD)

- Use type hints

- Follow PEP-8

- If this is a standalone script the uv shebang feature MUST be used:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["httpx"]
# ///
import httpx
```
