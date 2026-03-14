# MCP Patterns — Model Context Protocol

**Source:** Claude Code MCP documentation, production MCP integration patterns  
**Version:** 1.0.0  
**Last Updated:** 2026-03-14

## Overview

The Model Context Protocol (MCP) lets AI agents connect to external processes that expose:

- **Tools** — callable functions (search, query, execute)
- **Resources** — readable data sources (files, database rows, API responses)
- **Prompts** — reusable prompt templates surfaced as slash commands

### When MCP Is the Right Choice

MCP earns its overhead in one specific context: **when the model has no shell**.

A web chat interface, a mobile app, an enterprise copilot running in a locked-down container — in
these environments the model cannot run `curl`, `gh`, or `python`. MCP gives it a typed menu of
capabilities when there is genuinely no shorter path. A support agent that needs to hit Zendesk,
pull Stripe history, and file a Jira ticket in one turn — that is three auth models and three APIs
with no shell available. MCP is the right design there.

### When MCP Is the Wrong Choice

**In any shell-accessible environment — local development, CI, server-side agents — do not use
MCP.** A single Bash tool definition covers every CLI, every API via `curl`, every file operation.
The model constructs the right flags itself. That is cheaper, simpler, and has no server to
maintain.

Before reaching for MCP in a shell environment, exhaust:
1. A line in AGENTS.md — for static context and conventions
2. A skill — for recurring workflows with load-on-demand instructions
3. Bash + CLI tools or `curl` — for any API call the shell can reach

---

## Transport Types

### stdio (Standard I/O)

The agent spawns the server as a subprocess and communicates over stdin/stdout.

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "env": {
        "API_KEY": "${MY_API_KEY}"
      }
    }
  }
}
```

**Use when:** Local tools, CLI wrappers, database clients, anything you control.  
**Lifecycle:** Server starts when agent starts; terminates with agent.

### SSE (Server-Sent Events)

The agent connects to a running HTTP server over SSE.

```json
{
  "mcpServers": {
    "remote-server": {
      "url": "https://mcp.example.com/sse",
      "headers": {
        "Authorization": "Bearer ${API_TOKEN}"
      }
    }
  }
}
```

**Use when:** Remote servers, shared team infrastructure, servers that need to persist between
agent sessions.  
**Lifecycle:** Server is independent of the agent; must be running before the agent connects.

### HTTP (Streamable HTTP)

Similar to SSE but uses a single endpoint for bidirectional communication.

```json
{
  "mcpServers": {
    "http-server": {
      "url": "https://mcp.example.com/mcp",
      "type": "http"
    }
  }
}
```

---

## Configuration Scopes

| Scope | File | Visibility | Use for |
|-------|------|-----------|---------|
| **Local** | `.mcp.json` (gitignored) | Your machine only | Personal auth tokens, local servers |
| **Project** | `.mcp.json` (committed) | Whole team via git | Shared team servers, project tools |
| **User** | `~/.config/<tool>/mcp.json` | All your projects | Personal cross-project servers |

**Priority:** Local > Project > User. Local settings override project settings.

### Project `.mcp.json` Example

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

Always use environment variable references (`${VAR_NAME}`) for secrets — never hardcode credentials
in `.mcp.json`, even in the local-only file.

---

## Tool Schema Design

MCP tools declare their interface via JSON Schema. Good schema design is critical: the agent uses
the description and parameter schemas to decide when and how to call a tool.

### Tool Definition Structure

```python
{
    "name": "search_documents",           # snake_case, descriptive verb+noun
    "description": (                       # THE activation trigger — be specific
        "Search the knowledge base for documents matching a query. "
        "Returns ranked results with title, snippet, and relevance score. "
        "Use when the user asks to find, look up, or search for information."
    ),
    "inputSchema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Natural language search query"
            },
            "limit": {
                "type": "integer",
                "description": "Maximum number of results to return (default: 10)",
                "default": 10,
                "minimum": 1,
                "maximum": 100
            },
            "filters": {
                "type": "object",
                "description": "Optional metadata filters (e.g. {\"author\": \"alice\"})",
                "additionalProperties": {"type": "string"}
            }
        },
        "required": ["query"]
    }
}
```

### Schema Design Rules

1. **Name tools with verb+noun** — `search_documents`, `create_issue`, `get_user`, not `docs` or `search`
2. **Write descriptions as activation triggers** — include "Use when..." and the user's vocabulary
3. **Mark required fields explicitly** — don't make everything optional
4. **Provide defaults** for optional fields in the schema, not just in code
5. **Include examples** in parameter descriptions for non-obvious inputs
6. **Keep tools focused** — one tool, one responsibility; avoid "do everything" tools

---

## Authoring MCP Servers

### Python Server (using `mcp` SDK)

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import json

server = Server("my-server")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_status",
            description=(
                "Get the current status of the system. "
                "Use when the user asks about system health, uptime, or status."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "component": {
                        "type": "string",
                        "description": "Specific component to check (optional)",
                        "enum": ["api", "database", "cache", "all"]
                    }
                },
                "required": []
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "get_status":
        component = arguments.get("component", "all")
        status = await check_system_status(component)
        return [TextContent(type="text", text=json.dumps(status, indent=2))]

    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Node.js/TypeScript Server (using `@modelcontextprotocol/sdk`)

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  { name: "my-server", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "get_status",
      description: "Get system status. Use when the user asks about health or uptime.",
      inputSchema: {
        type: "object" as const,
        properties: {
          component: { type: "string", enum: ["api", "database", "all"] }
        }
      }
    }
  ]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "get_status") {
    const status = await checkSystemStatus(args?.component ?? "all");
    return { content: [{ type: "text", text: JSON.stringify(status, null, 2) }] };
  }

  throw new Error(`Unknown tool: ${name}`);
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

---

## Error Handling in MCP Servers

Return structured errors that help the agent recover:

```python
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    try:
        result = await perform_operation(arguments)
        return [TextContent(type="text", text=json.dumps(result))]

    except ValidationError as e:
        # Return user-facing error — agent will surface this
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "invalid_input",
                "message": str(e),
                "hint": "Check that required fields are present and correctly typed"
            })
        )]

    except ConnectionError as e:
        return [TextContent(
            type="text",
            text=json.dumps({
                "error": "connection_failed",
                "message": str(e),
                "retryable": True
            })
        )]
```

**Key principle:** Don't raise exceptions from tool handlers — return structured error objects that
the agent can reason about and potentially recover from.

---

## Resources

Resources let agents read data without a tool call:

```python
@server.list_resources()
async def list_resources():
    return [
        Resource(
            uri="config://app/settings",
            name="Application Settings",
            description="Current application configuration",
            mimeType="application/json"
        )
    ]

@server.read_resource()
async def read_resource(uri: str) -> str:
    if uri == "config://app/settings":
        return json.dumps(load_settings(), indent=2)
    raise ValueError(f"Unknown resource: {uri}")
```

Agents reference resources with `@server:config://app/settings` syntax in conversation.

---

## Prompts

Prompts are reusable templates surfaced as slash commands:

```python
@server.list_prompts()
async def list_prompts():
    return [
        Prompt(
            name="review_code",
            description="Review code for quality and security issues",
            arguments=[
                PromptArgument(name="language", description="Programming language", required=False)
            ]
        )
    ]

@server.get_prompt()
async def get_prompt(name: str, arguments: dict) -> GetPromptResult:
    if name == "review_code":
        lang = arguments.get("language", "any language")
        return GetPromptResult(
            messages=[{
                "role": "user",
                "content": f"Please review the following {lang} code for correctness, "
                           f"security vulnerabilities, and adherence to best practices..."
            }]
        )
```

Prompts appear as `/mcp__servername__review_code` slash commands in Claude Code.

---

## Security

### Authentication

- Always use environment variables for tokens — never hardcode in `.mcp.json`
- For remote SSE servers, use short-lived tokens rotated via OAuth 2.0 where possible
- For local stdio servers, filesystem permissions provide implicit auth

### Access Scoping

- Scope tokens to the minimum required permissions
- Prefer read-only tokens when a tool only reads data
- Log all tool invocations with enough context to audit what the agent did

### Input Validation

```python
async def call_tool(name: str, arguments: dict):
    # Always validate before operating on arguments
    if name == "query_database":
        table = arguments.get("table")
        if not table or not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', table):
            return [TextContent(type="text", text=json.dumps({
                "error": "invalid_table_name",
                "message": "Table name must be alphanumeric with underscores"
            }))]
        # Safe to proceed
```

Never pass raw agent input directly to shell commands, SQL queries, or file paths.

---

## Common MCP Servers

These are well-maintained servers from the MCP ecosystem:

| Server | Transport | Use Case |
|--------|-----------|---------|
| `@modelcontextprotocol/server-github` | stdio | GitHub issues, PRs, repos |
| `@modelcontextprotocol/server-gitlab` | stdio | GitLab projects, MRs, issues |
| `@modelcontextprotocol/server-postgres` | stdio | PostgreSQL queries |
| `@modelcontextprotocol/server-sqlite` | stdio | SQLite databases |
| `@modelcontextprotocol/server-filesystem` | stdio | Scoped filesystem access |
| `@modelcontextprotocol/server-fetch` | stdio | HTTP fetch with filtering |
| `@modelcontextprotocol/server-brave-search` | stdio | Web search via Brave |

Install pattern (npx, no global install required):

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}
```

---

## When to Use MCP vs. Skills vs. Direct Tools

The primary decision axis is **shell access**, not complexity or statefulness.

| Environment | Right approach |
|-------------|---------------|
| Shell available (local dev, CI, server-side agent) | AGENTS.md → Skills → Bash/curl. Do not use MCP. |
| No shell (web chat, mobile app, locked-down enterprise container) | MCP is appropriate here. |

Within shell-accessible environments:

| Situation | Use |
|-----------|-----|
| Static project conventions, version pins, doc links | AGENTS.md instruction |
| Recurring workflow with detailed reusable instructions | Skill |
| One-off or infrequent API call | Bash + curl / CLI tool |
| External API called repeatedly inside a workflow | Skill with a script in `scripts/` |
| Any of the above but no shell available | MCP tool exposing the same capability |

**Default: AGENTS.md or a skill.** If it can be expressed as a shell command, it should be.
Only design an MCP server when there is no shell and no other path.

---

## Anti-Patterns

### Hardcoding Credentials
```json
// Bad
{ "env": { "API_KEY": "sk-abc123" } }

// Good
{ "env": { "API_KEY": "${MY_API_KEY}" } }
```

### God Tools
```python
# Bad — one tool that does everything based on an "action" argument
Tool(name="manage_data", description="Manage data. Actions: create, read, update, delete, search, export...")

# Good — separate focused tools
Tool(name="search_data", description="Search data by query...")
Tool(name="create_record", description="Create a new record...")
```

### Silent Failures
```python
# Bad
async def call_tool(name, arguments):
    try:
        return [TextContent(type="text", text=do_thing())]
    except:
        return []  # Silent failure — agent has no idea what happened

# Good
    except Exception as e:
        return [TextContent(type="text", text=json.dumps({
            "error": type(e).__name__, "message": str(e)
        }))]
```

### Vague Tool Descriptions
```python
# Bad — won't be selected reliably
Tool(name="helper", description="Helps with various tasks.")

# Good — specific trigger language
Tool(name="search_issues", description=(
    "Search GitHub issues by keyword, label, or assignee. "
    "Use when the user wants to find, list, or filter issues."
))
```

---

## Related Patterns

- `core-rules/skills/SKILL_AUTHORING.md` — lighter-weight alternative for project-specific workflows
- `core-rules/design-patterns/TOOL_USE_PATTERNS.md` — tool registry, health checks, composition
- `core-rules/design-patterns/API_INTEGRATION.md` — direct API integration patterns
- `core-rules/security/SECRET_MANAGEMENT.md` — managing credentials for MCP server config
