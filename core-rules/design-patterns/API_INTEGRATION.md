# API Integration Patterns

**Source:** Production agent integration patterns  
**Version:** 1.0.0  
**Last Updated:** 2026-03-14

## Overview

Direct tool use (Bash, CLI tools, `curl`, SDK scripts) is position 3 in the capability priority
order. In any shell-accessible environment this single layer reaches every API, every service,
every file operation — with one schema and no server to maintain.

```
1. AGENTS.md        ← zero-overhead project context
2. Skills           ← load-on-demand domain expertise
3. Direct tools     ← Bash / curl / CLI: one schema, unlimited reach    ← this document
4. MCP              ← sandboxed/no-shell environments only
```

This document covers patterns for calling external APIs from within layer 3 — whether directly
from an agent's Bash tool or from a script inside a skill's `scripts/` directory.

**Use this layer when:**
- The agent has shell access (local dev, CI, server-side agent)
- The capability is reachable via a CLI tool, `curl`, or a Python/Node script
- You don't need MCP's typed discovery (because the model can construct shell commands itself)

---

## Authentication Patterns

### API Key (Bearer Token)

```python
import httpx
import os

def get_client() -> httpx.Client:
    """Build a pre-authenticated client from environment."""
    api_key = os.environ.get("MY_API_KEY")
    if not api_key:
        raise EnvironmentError("MY_API_KEY is not set")
    return httpx.Client(
        base_url="https://api.example.com/v1",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=30.0,
    )
```

### OAuth 2.0 Client Credentials

```python
import httpx
import os
from datetime import datetime, timedelta

_token_cache: dict = {}

def get_access_token() -> str:
    """Fetch and cache an OAuth 2.0 client-credentials token."""
    now = datetime.utcnow()
    if _token_cache.get("expires_at", now) > now:
        return _token_cache["access_token"]

    resp = httpx.post(
        "https://auth.example.com/oauth/token",
        data={
            "grant_type": "client_credentials",
            "client_id": os.environ["CLIENT_ID"],
            "client_secret": os.environ["CLIENT_SECRET"],
            "scope": "read write",
        },
        timeout=10.0,
    )
    resp.raise_for_status()
    token_data = resp.json()

    _token_cache["access_token"] = token_data["access_token"]
    _token_cache["expires_at"] = now + timedelta(seconds=token_data["expires_in"] - 60)
    return _token_cache["access_token"]
```

### Key Rules for Auth

- Always load credentials from environment variables — never hardcode
- Cache tokens with a safety margin before expiry (60 seconds is typical)
- Fail fast with a clear error when credentials are missing
- Use short-lived tokens wherever the API supports them

---

## HTTP Client Patterns

### Always Set Timeouts

```python
# Good — explicit timeouts prevent hangs
client = httpx.Client(timeout=httpx.Timeout(connect=5.0, read=30.0, write=10.0))

# Bad — no timeout, can hang indefinitely
client = httpx.Client()
```

### Structured Response Handling

Return a consistent shape regardless of success or failure so callers can reason about the result:

```python
from typing import Any

def api_call(endpoint: str, params: dict | None = None) -> dict[str, Any]:
    """
    Call the API and return a structured result.

    Returns:
        {"success": True, "data": ...}          on success
        {"success": False, "error": ..., "status_code": ...}  on failure
    """
    try:
        resp = client.get(endpoint, params=params)
        if resp.status_code == 200:
            return {"success": True, "data": resp.json()}
        return {
            "success": False,
            "error": f"HTTP {resp.status_code}",
            "status_code": resp.status_code,
            "body": resp.text[:500],          # truncate large error bodies
        }
    except httpx.TimeoutException:
        return {"success": False, "error": "Request timed out", "retryable": True}
    except httpx.RequestError as e:
        return {"success": False, "error": str(e), "retryable": True}
```

---

## Pagination

Never assume a single response contains all results.

### Offset / Limit

```python
def get_all_items(endpoint: str, page_size: int = 100) -> list[dict]:
    items = []
    offset = 0
    while True:
        result = api_call(endpoint, params={"limit": page_size, "offset": offset})
        if not result["success"]:
            raise RuntimeError(result["error"])
        batch = result["data"].get("items", [])
        items.extend(batch)
        if len(batch) < page_size:
            break                             # last page
        offset += page_size
    return items
```

### Cursor / Next-Page Token

```python
def get_all_items_cursor(endpoint: str) -> list[dict]:
    items = []
    cursor = None
    while True:
        params = {"cursor": cursor} if cursor else {}
        result = api_call(endpoint, params=params)
        if not result["success"]:
            raise RuntimeError(result["error"])
        data = result["data"]
        items.extend(data.get("items", []))
        cursor = data.get("next_cursor")
        if not cursor:
            break
    return items
```

---

## Retry with Exponential Backoff

```python
import time
import random

def api_call_with_retry(
    endpoint: str,
    params: dict | None = None,
    max_attempts: int = 3,
    base_delay: float = 1.0,
) -> dict[str, Any]:
    last_result = {}
    for attempt in range(max_attempts):
        result = api_call(endpoint, params)
        if result["success"]:
            return result

        # Only retry on transient errors
        status = result.get("status_code", 0)
        retryable = result.get("retryable", False) or status in (429, 500, 502, 503, 504)
        if not retryable:
            return result

        if attempt < max_attempts - 1:
            delay = base_delay * (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(delay)
        last_result = result

    return last_result
```

**Retry on:** network errors, timeouts, 429 (rate limit), 5xx server errors.  
**Do not retry on:** 4xx client errors (400, 401, 403, 404) — these won't succeed on retry.

---

## Rate Limiting

Respect API rate limits to avoid bans and degraded service:

```python
import time
from collections import deque

class RateLimiter:
    """Simple sliding-window rate limiter."""

    def __init__(self, calls_per_second: float):
        self.min_interval = 1.0 / calls_per_second
        self._last_call = 0.0

    def wait(self) -> None:
        elapsed = time.monotonic() - self._last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_call = time.monotonic()

# Usage
limiter = RateLimiter(calls_per_second=5)

def rate_limited_call(endpoint: str) -> dict:
    limiter.wait()
    return api_call(endpoint)
```

When you receive a `429` response, check for a `Retry-After` header before falling back to
exponential backoff:

```python
if resp.status_code == 429:
    retry_after = float(resp.headers.get("Retry-After", base_delay))
    time.sleep(retry_after)
```

---

## Async Patterns

For agents that need to call multiple APIs concurrently:

```python
import asyncio
import httpx

async def fetch_many(urls: list[str], headers: dict) -> list[dict]:
    async with httpx.AsyncClient(headers=headers, timeout=30.0) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)

    results = []
    for url, resp in zip(urls, responses):
        if isinstance(resp, Exception):
            results.append({"success": False, "url": url, "error": str(resp)})
        elif resp.status_code == 200:
            results.append({"success": True, "url": url, "data": resp.json()})
        else:
            results.append({"success": False, "url": url, "status_code": resp.status_code})
    return results
```

---

## Calling APIs from Inside Skills

When a skill needs to call an external API, put the logic in a script under `scripts/` and
reference it from `SKILL.md`. This keeps the skill body concise and the API code testable
independently:

```
.claude/skills/my-integration/
├── SKILL.md
└── scripts/
    ├── fetch_data.py       # API call logic
    └── requirements.txt    # Dependencies
```

**SKILL.md:**
```markdown
## Fetch latest data

Run the fetch script — it handles auth, pagination, and retries automatically:

```bash
python scripts/fetch_data.py --output data.json
```

If the script exits non-zero, read the error output and report the problem to the user.
```

**scripts/fetch_data.py:**
```python
#!/usr/bin/env python3
"""Fetch data from the API with auth, pagination, and retry."""
import os, json, sys
# ... full implementation using patterns above
```

This pattern:
- Keeps `SKILL.md` under 500 lines
- Makes the API code testable with `pytest` independently of the agent
- Ensures consistent behavior — the same code runs every time, not generated code

---

## Security

- **Never log full request/response bodies** in production — they may contain credentials or PII
- **Validate and sanitize** any user-provided values before including in API requests
- **Use HTTPS only** — reject or warn on HTTP URLs
- **Check `Content-Type`** on responses before calling `.json()` — malformed responses can panic
- **Scope API tokens** to the minimum permissions the integration requires

---

## Anti-Patterns

### No Timeout
```python
# Bad — hangs forever on slow APIs
requests.get("https://api.example.com/data")

# Good
httpx.get("https://api.example.com/data", timeout=30.0)
```

### Hardcoded Credentials
```python
# Bad
API_KEY = "sk-abc123realkey"

# Good
API_KEY = os.environ["MY_API_KEY"]
```

### Ignoring Status Codes
```python
# Bad — assumes success
data = requests.get(url).json()

# Good
resp = httpx.get(url)
resp.raise_for_status()   # or check manually and return structured error
data = resp.json()
```

### Fetching All Pages Upfront When Only First Is Needed
Only paginate when you actually need all results. Fetching all pages for a query that only needs
the top 10 results wastes time and API quota.

### Reaching for MCP in a Shell Environment
If the agent has shell access, `curl` or a CLI tool reaches the same API with less overhead and no
server to maintain. MCP belongs in sandboxed/no-shell contexts — not here.

---

## Related Patterns

- `core-rules/skills/SKILL_AUTHORING.md` — embedding API scripts in skills
- `core-rules/mcp/MCP_PATTERNS.md` — when MCP is genuinely necessary over a direct API call
- `core-rules/design-patterns/ERROR_RECOVERY.md` — broader error recovery strategies
- `core-rules/security/SECRET_MANAGEMENT.md` — credential storage and rotation
- `core-rules/python-standards/ASYNC_PATTERNS.md` — async patterns for concurrent API calls
