# Agent Rules Library - LEGACY

> **Historical Document**
> This is the original README from the `agent-rules` repository (v1.0.0).
> Content has been migrated to `core-rules/` and `templates/` directories in this repository.
> Preserved for historical reference and attribution.

**Source Repository:** https://github.com/apathy-ca/agent-rules
**Original Version:** 1.0.0
**Migration Date:** 2025-12-27
**Migrated To:** `/home/jhenry/Source/agent-knowledge/core-rules/` and `/home/jhenry/Source/agent-knowledge/templates/`

---

**Comprehensive agent development rules extracted from production systems**

A curated library of rules, patterns, and standards for AI agent development, extracted from thesymposium, czarina, and SARK production codebases.

---

## Overview

This repository contains 69 markdown files documenting agent development best practices across 9 domains:

- **Python Standards** (7 files) - Modern Python coding standards
- **Agent Roles** (10 files) - Agent role definitions and orchestration patterns
- **Workflows** (7 files) - Development workflow patterns
- **Design Patterns** (6 files) - Tool use, streaming, caching, batch operations, error recovery
- **Testing Standards** (6 files) - Testing policy, unit/integration testing, mocking, coverage
- **Security Practices** (6 files) - Authentication, authorization, secrets, injection prevention, auditing
- **Templates** (13 files) - Project templates for quick starts
- **Documentation Standards** (6 files) - API docs, architecture docs, changelogs
- **Orchestration Patterns** (2 files) - Multi-agent coordination

**Total:** 43,873 lines of production-ready documentation

---

## Quick Start

### Browse by Domain

```bash
# Python coding standards
cat agent-rules/python/README.md

# Agent roles and orchestration
cat agent-rules/agents/README.md

# Security best practices
cat agent-rules/security/README.md

# Complete index of all rules
cat agent-rules/INDEX.md
```

### Use Templates

```bash
# List available templates
ls agent-rules/templates/

# Create a new Python project
cp agent-rules/templates/python-project-template.md my-project/

# Use worker definition template
cp agent-rules/agents/templates/worker-definition-template.md .czarina/workers/
```

### Integration with Hopper

 for complete Hopper integration instructions.

Quick setup:
```bash
# In your Hopper project
ln -s ~/Source/agent-rules/agent-rules ./agent-rules
ln -s ~/Source/agent-rules/.hopper ./.hopper
```

---

## Repository Structure

```
agent-rules/
├── README.md                 ← You are here
├── agent-rules/
│   ├── INDEX.md              ← Complete index of all 53+ rules
│   ├── README.md             ← Library overview
│   ├── USAGE_GUIDE.md        ← Practical usage scenarios
│   │
│   ├── python/               ← Python coding standards (7 files)
│   ├── agents/               ← Agent roles & templates (10 files)
│   ├── workflows/            ← Development workflows (7 files)
│   ├── patterns/             ← Design patterns (6 files)
│   ├── testing/              ← Testing standards (6 files)
│   ├── security/             ← Security practices (6 files)
│   ├── templates/            ← Project templates (13 files)
│   ├── documentation/        ← Doc standards (6 files)
│   └── orchestration/        ← Orchestration patterns (2 files)
│
├── .hopper/                  ← Hopper integration
│   ├── README.md
│   └── modes/
│       ├── research.md
│       └── implementation.md
│
├── CLOSEOUT.md               ← Project closeout report
├── PROJECT_COMPLETE.md       ← Completion summary
├── CZARINA_ORCHESTRATION_CLOSEOUT.md  ← Orchestration report
└── MIGRATION_GUIDE.md        ← Hopper integration guide
```

---

## Usage

### For Developers

**Learn best practices:**
```bash
# Python async patterns
cat agent-rules/python/ASYNC_PATTERNS.md

# Error handling strategies
cat agent-rules/patterns/ERROR_RECOVERY.md

# Testing patterns
cat agent-rules/testing/UNIT_TESTING.md
```

**Use templates:**
```bash
# Start a new project
cp agent-rules/templates/python-project-template.md myproject/README.md

# Create API documentation
cp agent-rules/templates/api-documentation-template.md docs/API.md
```

### For Agent Systems

**Configure Hopper:**
- See `.hopper/` directory for mode-specific rules
- Use `MIGRATION_GUIDE.md` for integration steps

**Orchestration with Czarina:**
- See `agent-rules/orchestration/` for patterns
- Use `agent-rules/agents/` for worker definitions

---

## Domains

### 1. Python Standards
Modern Python coding standards extracted from SARK production codebase.

**Files:** CODING_STANDARDS.md, ASYNC_PATTERNS.md, ERROR_HANDLING.md, DEPENDENCY_INJECTION.md, TESTING_PATTERNS.md, SECURITY_PATTERNS.md

**Use for:** Python project setup, code reviews, team standards

### 2. Agent Roles
Agent role definitions and orchestration patterns from Czarina.

**Files:** AGENT_ROLES.md, ARCHITECT_ROLE.md, CODE_ROLE.md, DEBUG_ROLE.md, QA_ROLE.md, ORCHESTRATOR_ROLE.md, worker templates

**Use for:** Multi-agent systems, role assignment, worker coordination

### 3. Workflows
Git workflow, PR requirements, documentation, phase-based development.

**Files:** GIT_WORKFLOW.md, PR_REQUIREMENTS.md, PHASE_DEVELOPMENT.md, DOCUMENTATION_WORKFLOW.md, TOKEN_PLANNING.md, CLOSEOUT_PROCESS.md

**Use for:** Team processes, project planning, documentation standards

### 4. Design Patterns
Tool use, streaming, caching, batch operations, error recovery.

**Files:** TOOL_USE_PATTERNS.md, STREAMING_PATTERNS.md, CACHING_PATTERNS.md, BATCH_OPERATIONS.md, ERROR_RECOVERY.md

**Use for:** System architecture, performance optimization, reliability

### 5. Testing Standards
Testing policy, unit/integration testing, mocking, coverage standards.

**Files:** TESTING_POLICY.md, UNIT_TESTING.md, INTEGRATION_TESTING.md, MOCKING_STRATEGIES.md, COVERAGE_STANDARDS.md

**Use for:** Test strategy, CI/CD, quality assurance

### 6. Security Practices
Authentication, authorization, secret management, injection prevention, auditing.

**Files:** AUTHENTICATION.md, AUTHORIZATION.md, SECRET_MANAGEMENT.md, INJECTION_PREVENTION.md, AUDIT_LOGGING.md

**Use for:** Security reviews, compliance, production readiness

### 7. Templates
Ready-to-use templates for projects, documentation, testing.

**13 templates** for Python projects, API docs, architecture docs, tests, workers

**Use for:** Project initialization, consistency, quick starts

### 8. Documentation Standards
API documentation, architecture docs, changelogs, README templates.

**Files:** DOCUMENTATION_STANDARDS.md, API_DOCUMENTATION.md, ARCHITECTURE_DOCS.md, CHANGELOG_STANDARDS.md, README_TEMPLATE.md

**Use for:** Documentation strategy, technical writing, onboarding

### 9. Orchestration Patterns
Multi-agent coordination patterns from Czarina.

**Files:** ORCHESTRATION_PATTERNS.md

**Use for:** Multi-agent systems, worker coordination, parallel execution

---

## Project History

**Created:** 2025-12-26
**Completed:** 2025-12-27
**Method:** Czarina multi-agent orchestration (7 workers)
**Source:** thesymposium, czarina, SARK production codebases

**Orchestration:**
- 7 workers (6 content + 1 QA)
- 3-week scope completed in 2 days through parallel execution
- 100% worker success rate
- 3.4x speedup vs sequential execution

 for complete orchestration report.

---

## Contributing

This library is extracted from production systems and represents battle-tested patterns. Updates should:

1. Come from production usage
2. Include real examples with file references
3. Follow existing structure and formatting
4. Be validated against actual codebases

---

## License

Extracted from production systems for internal use and education.

---

## Related Projects

- **Hopper** - AI agent framework (uses this library)
- **Czarina** - Multi-agent orchestration (documented in this library)
- **SARK** - Symposium Agent Rules and Knowledge (source of Python/security patterns)
- **thesymposium** - Source of workflow and documentation patterns

---

## Support

For questions about specific rules or patterns, see the domain READMEs:
- `agent-rules/python/README.md`
- `agent-rules/agents/README.md`
- `agent-rules/workflows/README.md`
- etc.

For Hopper integration: See `MIGRATION_GUIDE.md`

---

**Production-ready agent development rules. Battle-tested. Comprehensive. Ready to use.**
