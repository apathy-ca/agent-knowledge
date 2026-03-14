# Skill Authoring Guide

**Source:** Distilled from Claude Code skills specification and production skill patterns  
**Version:** 1.0.0  
**Last Updated:** 2026-03-14

## Overview

A **skill** is a directory containing a `SKILL.md` file (plus optional supporting resources) that
gives an AI agent reusable, domain-specific expertise. Skills use **progressive disclosure** — only
metadata loads at startup, full instructions load when triggered, and reference files load only when
needed. This lets you install many skills with minimal context cost.

---

## How Skills Work: Progressive Disclosure

Skills load in three stages:

| Level | Content | When Loaded | Token Cost |
|-------|---------|------------|------------|
| **1 — Metadata** | YAML frontmatter (`name`, `description`) | Always, at agent startup | ~100 tokens per skill |
| **2 — Instructions** | Full `SKILL.md` body | When user request matches description | Typically <5k tokens |
| **3 — Resources** | `references/`, `scripts/`, templates | Only when referenced or executed | Scripts run without loading into context |

With progressive disclosure, 100+ skills can be installed with minimal context penalty — only
metadata loads by default.

### Skills vs. Other Extension Mechanisms

| Feature | Skills | Slash Commands | AGENTS.md | MCP Servers |
|---------|--------|---------------|-----------|-------------|
| **Invocation** | Model-invoked (automatic) | User-invoked | Always-on | Tool-call (protocol) |
| **Loading** | Progressive (3 levels) | All at once | All at once | On demand |
| **Structure** | Multi-file with scripts | Single markdown | Single markdown | Server process |
| **Best for** | Recurring domain workflows | Quick prompts | Project context | Runtime tool access |

---

## Skill File Format

### Required: SKILL.md Frontmatter

Every skill must start with YAML frontmatter. The only fields the agent runtime requires are
`name` and `description`. All others are conventions that improve discoverability and safety.

```yaml
---
name: my-skill                           # Required. Kebab-case, max 64 chars.
description: >                           # Required. Max 1024 chars. THE activation trigger.
  Use when the user wants to [trigger].
  Does [what] by [how].
allowed-tools: "Bash, Read, Write"       # Recommended. Comma-separated tool names.
metadata:                                # Recommended. Registry/discovery metadata.
  author: your-name
  version: "1.0.0"
  category: integration                  # e.g. git, integration, code-quality, tutorial
  tags: [example, my-domain]
compatibility: [python3]                 # Optional. System dependencies required.
argument-hint: "[start | next]"          # Optional. Hint shown when skill is invoked as command.
---
```

### `allowed-tools` Values

Use canonical tool names. Constraining tools limits what the agent can do when the skill is active
without prompting for permission:

```
Read        Write       Edit        Glob        Grep
Bash        Task        WebFetch    WebSearch   AskUserQuestion
```

You can restrict `Bash` further with patterns: `"Bash(python:*)"` limits to python commands only.

### Directory Structure

**Single-file skill** (minimal):
```
.claude/skills/my-skill/
└── SKILL.md
```

**Multi-file skill** (preferred for complex workflows):
```
.claude/skills/my-skill/
├── SKILL.md                # Main instructions (Level 2) — keep under 500 lines
├── references/
│   ├── api-reference.md    # Detail loaded on demand (Level 3)
│   └── examples.md         # Extended examples (Level 3)
└── scripts/
    ├── validate.py         # Executable — only output enters context (Level 3)
    └── process.py
```

---

## Writing Effective Descriptions

The `description` field is the most important line in a skill. The agent reads every installed
skill's description at startup to decide which to activate. Write it as a **trigger**, not as
documentation.

### Rules

1. **Lead with "Use when"** — forces trigger-first phrasing
2. **Include the words users actually say** — "create a ticket", "review the PR", "push to prod"
3. **Name the systems involved** — "via the GitHub CLI", "using the Sheets API"
4. **Stay under 1024 characters** — 2–3 sentences is the target
5. **Use third person** — "Processes files" not "I process files"
6. **Mention prerequisites that affect activation** — "Requires Python 3.8+ and `jq` installed"

### Examples

```yaml
# Good — trigger-first, user-vocabulary, names the tool
description: >
  Use when the user wants to create, update, or search issues, manage sprints,
  or check board status. Wraps the project's issue-tracking CLI.

# Bad — describes the skill instead of triggering on user intent
description: >
  A comprehensive issue-tracking integration providing full lifecycle management
  capabilities for enterprise project tracking systems.
```

---

## Writing Skill Instructions

### Keep SKILL.md Concise

Aim for under 500 lines. The agent is capable — only write what it doesn't already know:

- **Assume** common programming concepts, standard library APIs, general best practices
- **Include** project-specific patterns, non-obvious workflows, critical gotchas, domain secrets

### Use Progressive Disclosure in the Body

Split long skills into a high-level guide in `SKILL.md` that references detail files:

```markdown
## Quick start
[Basic 3-step workflow here]

## Advanced usage
For edge cases, see [references/advanced.md](references/advanced.md).
For the full API reference, see [references/api-reference.md](references/api-reference.md).
```

### Provide Executable Scripts When Possible

Scripts are more reliable than generated code, save tokens, and ensure consistency:

```markdown
## Validate output
Run the provided validation script:
```bash
python scripts/validate.py output.json
```

Output format:
```json
{"status": "ok", "issues": []}
```
```

### Use Checklists for Complex Workflows

```markdown
## Deployment workflow
Track progress:
- [ ] Step 1: Run pre-flight checks (`python scripts/preflight.py`)
- [ ] Step 2: Build artifact (`make build`)
- [ ] Step 3: Upload to staging (`python scripts/upload.py staging`)
- [ ] Step 4: Smoke test staging
- [ ] Step 5: Promote to production
```

### Build in Feedback Loops

```markdown
## After each edit
1. Run validation immediately:
   ```bash
   python scripts/validate.py
   ```
2. If validation fails: fix the issue, re-run.
3. Only proceed when validation passes.
```

### Include Concrete Examples

```markdown
## Commit message format
**Feature example:**
Input: Added JWT authentication
Output:
```
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware.
```
```

---

## Skill Locations

| Scope | Path | Shared via |
|-------|------|-----------|
| Personal (all projects) | `~/.claude/skills/<name>/` | Not shared |
| Project (team) | `.claude/skills/<name>/` | Git |
| Plugin-bundled | Plugin directory `skills/` | Plugin install |

Project skills (`.claude/skills/`) are the standard way to share skills with a team — they're
committed to the repository and automatically available to everyone who clones it.

---

## Testing and Debugging

### Test a Skill

Skills are model-invoked — the agent decides when to use them. Test by sending a natural language
query that should match your description:

```
User: "Can you help me review this PR?"
```

If the skill has a matching description, the agent will activate it automatically.

Enable debug mode to see skill loading and activation:

```bash
claude --debug
```

### Debug: Skill Not Activating

1. **Check description specificity** — is it trigger-first? Does it use the words the user said?
2. **Verify file path** — `ls .claude/skills/my-skill/SKILL.md`
3. **Check YAML syntax** — opening `---` must be line 1; no tabs; only supported fields
4. **Verify `name` and `description` are present** — they're the only required fields

### Evaluation-Driven Development

Build skills iteratively:

1. Run Claude without the skill — document where it falls short
2. Write 3+ realistic test scenarios
3. Write minimal instructions that pass those scenarios
4. Test with real-world queries
5. Iterate: observe failures, refine instructions, re-test

### Two-Agent Development Pattern

Use two agent instances:

- **Agent A** (author): helps design and refine the skill
- **Agent B** (user): uses the skill for real tasks

Process:
1. Complete a task with Agent A using normal prompting
2. Identify which patterns are reusable
3. Ask Agent A to extract a skill from those patterns
4. Test with Agent B on similar tasks
5. Return observations to Agent A and iterate

---

## Security

**Only install skills from sources you trust.** A malicious skill can:
- Direct the agent to invoke tools inappropriately
- Exfiltrate data via network calls
- Access files outside the intended scope

### Before Installing a Third-Party Skill

1. Read `SKILL.md` completely — understand every instruction
2. Review all scripts for unexpected network calls or file access
3. Check `allowed-tools` — does it need more access than the task requires?
4. Test in an isolated environment before using on real data
5. Treat skill installation like installing software — verify source and reputation

### Writing Secure Skills

- Use `allowed-tools` to constrain to the minimum necessary tools
- Never hardcode credentials or API keys in skill files
- Reference secrets via environment variables only
- Avoid `Bash` without restrictions when `Read`/`Write`/`Edit` are sufficient

---

## Anti-Patterns

### Vague Description
```yaml
# Bad — won't activate reliably
description: Helps with things.

# Good — trigger-first, specific
description: Use when the user wants to [specific action] using [specific tool].
```

### Overloaded SKILL.md
Keep the main file under 500 lines. Move detail into `references/` files and link to them.

### No Feedback Loop
Skills that ask Claude to perform actions without validation steps are fragile. Always include
a way to verify each step succeeded before proceeding.

### Generating Code That Should Be a Script
If the same code will be run repeatedly, put it in `scripts/` and reference it. Generated code
varies; scripts are consistent and don't consume context tokens.

### Missing `allowed-tools`
Without `allowed-tools`, the agent may request permissions for any tool. Constrain to what the
skill actually needs.

---

## Skill Creation Checklist

**Before sharing a skill:**

- [ ] Description is trigger-first with user-vocabulary terms
- [ ] Description uses third person and stays under 1024 characters
- [ ] `SKILL.md` body is under 500 lines
- [ ] `allowed-tools` is set to the minimum necessary
- [ ] Complex detail is split into `references/` files
- [ ] Repeated operations use `scripts/` rather than generated code
- [ ] Validation/feedback steps are included in workflows
- [ ] 3+ test scenarios have been run against real queries
- [ ] No credentials, secrets, or org-specific URLs are hardcoded
- [ ] Works correctly from both `~/.claude/skills/` and `.claude/skills/`

---

## Related Patterns

- `core-rules/mcp/MCP_PATTERNS.md` — when MCP is a better choice than a skill
- `core-rules/design-patterns/API_INTEGRATION.md` — calling APIs from inside skill scripts
- `core-rules/workflows/GIT_WORKFLOW.md` — committing and sharing project skills
- `core-rules/agent-roles/AGENT_ROLES.md` — how skills relate to agent role specialization
