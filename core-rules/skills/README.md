# Skills — Authoring Framework

**Domain:** Skills  
**Version:** 1.0.0  
**Last Updated:** 2026-03-14

## Overview

Skills are modular, filesystem-based instruction packages that extend an AI agent's capabilities
for recurring, domain-specific workflows. This domain covers the **authoring framework** — how to
design, write, structure, test, and maintain skills. It does not contain any project- or
org-specific skill content.

## Files in This Domain

| File | Description |
|------|-------------|
| [SKILL_AUTHORING.md](SKILL_AUTHORING.md) | Complete skill authoring guide: format, progressive disclosure, descriptions, testing, security |

## What Skills Are (and Aren't)

**Skills are:**
- A `SKILL.md` file (plus optional supporting files) that Claude reads automatically when context matches
- Model-invoked: the agent decides when to activate based on the `description` field
- Scoped to a project (`.claude/skills/`) or a user (`~/.claude/skills/`)
- Composable: skills can reference scripts and reference docs without loading them upfront

**Skills are not:**
- Slash commands (those are user-invoked single markdown files)
- MCP servers (those expose tools at the protocol level)
- AGENTS.md instructions (those are always-on project context)

## Capability Priority Context

Skills sit at position 2 in the capability priority order:

```
1. AGENTS.md     ← always-on project context
2. Skills        ← model-invoked domain expertise   ← this domain
3. APIs          ← external integrations
4. MCP           ← protocol-level tool exposure
```

Use skills when a workflow is recurring, well-understood, and benefits from reusable instructions
that don't need to be re-prompted each session.

## Quick Reference: Skill Directory Layout

```
.claude/skills/<skill-name>/
├── SKILL.md              # Required: frontmatter + instructions
├── references/
│   └── api-reference.md  # Optional: detail loaded on demand
└── scripts/
    └── helper.py         # Optional: executable, output enters context
```

## Related Domains

- `core-rules/mcp/` — MCP servers as an alternative to skill-based tool exposure
- `core-rules/design-patterns/API_INTEGRATION.md` — integrating external APIs inside skills
- `core-rules/workflows/GIT_WORKFLOW.md` — sharing project skills via version control
