# MCP — Model Context Protocol Patterns

**Domain:** MCP  
**Version:** 1.0.0  
**Last Updated:** 2026-03-14

## Overview

The Model Context Protocol (MCP) is an open standard for exposing **tools**, **resources**, and
**prompts** to AI agents at runtime. MCP gives the model a typed menu of capabilities with
structured inputs and predictable outputs.

This domain covers how to configure and author MCP servers for the one context where they make
sense. For all other contexts, use layers 1–3 instead.

## Files in This Domain

| File | Description |
|------|-------------|
| [MCP_PATTERNS.md](MCP_PATTERNS.md) | Transport types, configuration, tool schema design, server authoring, security, when-to-use guidance |

## Capability Priority Context

MCP is position 4 — and only appropriate in a specific environment:

```
1. AGENTS.md     ← zero-overhead project context
2. Skills        ← load-on-demand domain expertise
3. Direct tools  ← Bash / shell: one schema, unlimited reach
4. MCP           ← sandboxed/no-shell environments only    ← this domain
```

**MCP earns its overhead when the model has no shell** — a web chat interface, a mobile app, an
enterprise copilot running in a locked-down container. In those environments, there is no shorter
path to a typed API call than MCP.

**In any shell-accessible agentic environment (local dev, CI, server-side agents), use layers 1–3.**
A Bash tool with `curl` or the GitHub CLI reaches everything MCP exposes, with less overhead and
no server to maintain.

## Related Domains

- `core-rules/skills/` — lighter-weight model-invoked extension mechanism
- `core-rules/design-patterns/API_INTEGRATION.md` — calling APIs directly vs. via MCP
- `core-rules/design-patterns/TOOL_USE_PATTERNS.md` — general tool-calling patterns (includes MCP section)
