# AGENTS.md — Agent Knowledge Library

This file provides guidance to AI coding agents (OpenCode, Claude Code, Cursor, Cline, Roo, etc.)
when working with this repository.

## Repository Purpose

**agent-knowledge** is a canonical, tool-agnostic library of rules, patterns, and standards for
AI-assisted software development. It is consumed by other projects via `opencode.json` instructions
references and direct file inclusion. It is **not** a runnable application.

## Capability Priority Order

Four layers, four jobs. Start at the top. Move down only when the layer above cannot do the job.

1. **Project instructions (AGENTS.md / CLAUDE.md)** — Zero tool overhead. The model reads this
   file on every message with no tool call, no schema, no external dependency. Put API
   conventions, version requirements, doc links, and project constraints here. This layer solves
   most problems people reach for MCP to fix. Cost: free.

2. **Skills** — Load on demand. Skills are listed in context as one-line triggers (~100 tokens
   total when dormant). When invoked, the full instructions expand. When not needed, nearly
   invisible. Use skills for recurring workflows that need detailed, reusable instructions.
   See `core-rules/skills/SKILL_AUTHORING.md`.

3. **Direct tools (Bash / shell)** — One schema, unlimited reach. A single Bash tool definition
   gives the model access to every CLI, every API via curl, every file operation. The model
   constructs the right flags and filters itself. This is the right layer for any environment
   where the agent has shell access — which is most agentic development contexts.
   See `core-rules/design-patterns/API_INTEGRATION.md`.

4. **MCP (Model Context Protocol)** — Structured discovery for sandboxed environments. MCP earns
   its overhead when the model has **no shell** — a web chat, a mobile app, an enterprise copilot
   in a locked-down container. It gives the model a typed menu of capabilities when there is no
   shorter path. Do not use MCP in shell-accessible agentic environments; layers 1–3 are cheaper
   and simpler. See `core-rules/mcp/MCP_PATTERNS.md`.

## Repository Structure

```
agent-knowledge/
├── AGENTS.md                    # This file — agent entrypoint
├── core-rules/                  # Canonical rules library (10 domains)
│   ├── INDEX.md                 # Master index of all rules
│   ├── README.md                # Library overview
│   ├── agent-roles/             # Role definitions: Architect, Code, Debug, QA, Orchestrator
│   ├── design-patterns/         # Tool use, streaming, caching, batch, error recovery, API integration
│   ├── documentation/           # Documentation standards and templates
│   ├── mcp/                     # Model Context Protocol patterns (NEW)
│   ├── orchestration/           # Multi-agent coordination (Czarina pattern)
│   ├── python-standards/        # Python coding, async, DI, testing, security
│   ├── security/                # Auth, authz, secrets, injection, audit logging
│   ├── skills/                  # Skill authoring framework (NEW)
│   ├── testing/                 # Testing policy, unit, integration, coverage, mocking
│   └── workflows/               # Git, PRs, documentation, phases, token planning, closeout
├── patterns/                    # Practical how-to pattern library
├── templates/                   # 13 reusable project/doc/test/worker templates
├── meta/                        # Library maintenance metadata
└── scripts/                     # Maintenance scripts
```

## Working with This Repo

### Adding a New Rule or Domain

1. Create a directory under `core-rules/<domain>/`
2. Write the rule file following `core-rules/documentation/DOCUMENTATION_STANDARDS.md`
3. Add a `README.md` to the domain directory
4. Update `core-rules/INDEX.md` with the new entry
5. Submit a PR per `core-rules/workflows/PR_REQUIREMENTS.md`

### Adding a Skill (Framework)

Skills belong in `.claude/skills/<name>/` in the **consuming project**, not here. This library
contains the **authoring framework** only. See `core-rules/skills/SKILL_AUTHORING.md`.

### Language Coverage

Currently Python-focused. TypeScript/Go standards are planned but not yet authored.

## Key Conventions

- All rule files use `SCREAMING_SNAKE_CASE.md` naming
- Domain READMEs summarize their domain — don't duplicate rule content in them
- Cross-references use relative paths from the file making the reference
- No TELUS-specific content belongs here — this library is tool- and org-agnostic
- The `.hopper/` integration is intentionally excluded from this repo

## Related Resources

- Global agent rules: `~/.config/opencode/AGENTS.md`
- Project-specific rules: each consuming repo's own `AGENTS.md`
- TELUS skill registry: `~/Source/ai-dev/skills/` (TELUS-specific, not this repo)
