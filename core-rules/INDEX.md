# Core Rules Index

Production-tested rules extracted from real projects.

**What are Core Rules?** Standards, requirements, and definitions that establish **what** you must do.

**How do they relate to Patterns?** Core Rules define requirements; [Patterns](../patterns/INDEX.md) show how to implement them effectively.

---

## Navigation by Domain

### Python Standards (7 rules, ~1,827 lines)

Foundation for Python development:
- [README](./python-standards/README.md) - Overview and philosophy
- [Imports](./python-standards/imports.md) - Import organization and standards
- [Type Annotations](./python-standards/type-annotations.md) - Type hints and mypy
- [Async/Await](./python-standards/async-await.md) - Asynchronous programming patterns
- [Error Handling](./python-standards/error-handling.md) - Exception handling standards
- [Logging](./python-standards/logging.md) - Structured logging requirements
- [Testing](./python-standards/testing.md) - Python testing standards
- [Packaging](./python-standards/packaging.md) - Distribution and dependency management

**Related Patterns:** [Error Recovery](../patterns/error-recovery/), [Testing Patterns](../patterns/testing-patterns/)

---

### Agent Roles (10 roles, ~11,485 lines)

Definitions and responsibilities for different agent roles:
- [README](./agent-roles/README.md) - Overview of agent role system
- [Architect Role](./agent-roles/architect-role.md) - System design and planning
- [Code Role](./agent-roles/code-role.md) - Implementation and coding
- [Debug Role](./agent-roles/debug-role.md) - Debugging and troubleshooting
- [QA Role](./agent-roles/qa-role.md) - Quality assurance and testing
- [Orchestrator Role](./agent-roles/orchestrator-role.md) - Task coordination
- [Ask Role](./agent-roles/ask-role.md) - Information gathering and clarification
- [Ops Role](./agent-roles/ops-role.md) - Operations and deployment
- [Security Role](./agent-roles/security-role.md) - Security validation
- [Docs Role](./agent-roles/docs-role.md) - Documentation creation
- [Roles Coordination](./agent-roles/roles-coordination.md) - Multi-role collaboration

**Related Patterns:** [Mode Capabilities](../patterns/mode-capabilities/)

---

### Workflows (7 workflows, ~3,062 lines)

Standard workflows for common development tasks:
- [README](./workflows/README.md) - Workflow system overview
- [Feature Workflow](./workflows/feature-workflow.md) - Adding new features
- [Bugfix Workflow](./workflows/bugfix-workflow.md) - Fixing bugs
- [Refactor Workflow](./workflows/refactor-workflow.md) - Code refactoring
- [Investigation Workflow](./workflows/investigation-workflow.md) - Research and exploration
- [Handoff Workflow](./workflows/handoff-workflow.md) - Transferring context between agents
- [Recovery Workflow](./workflows/recovery-workflow.md) - Recovering from errors
- [Git Workflows](./workflows/git-workflows.md) - Version control practices

**Related Patterns:** [Error Recovery](../patterns/error-recovery/), [Git Workflows](../patterns/git-workflows/)

---

### Design Patterns (6 patterns, ~1,926 lines)

Architectural and design patterns:
- [README](./design-patterns/README.md) - Design philosophy
- [Layer-Based Architecture](./design-patterns/layer-based-architecture.md) - Separation of concerns
- [Modular Design](./design-patterns/modular-design.md) - Component organization
- [Configuration Over Code](./design-patterns/configuration-over-code.md) - Externalized configuration
- [Progressive Complexity](./design-patterns/progressive-complexity.md) - Incremental sophistication
- [Comprehensive Testing](./design-patterns/comprehensive-testing.md) - Testing strategy
- [Memory Patterns](./design-patterns/memory-patterns.md) - State management

**Related Patterns:** [Context Management](../patterns/context-management/)

---

### Testing (6 rules, ~1,799 lines)

Testing standards and requirements:
- [README](./testing/README.md) - Testing philosophy
- [Testing Philosophy](./testing/testing-philosophy.md) - Why and how we test
- [Pytest Standards](./testing/pytest-standards.md) - Pytest conventions
- [Test Organization](./testing/test-organization.md) - Test structure
- [Fixtures and Mocks](./testing/fixtures-and-mocks.md) - Test helpers
- [Integration Testing](./testing/integration-testing.md) - End-to-end tests
- [Coverage Requirements](./testing/coverage-requirements.md) - Coverage targets

**Related Patterns:** [Testing Patterns](../patterns/testing-patterns/)

---

### Security (5 rules, ~4,155 lines)

Security best practices and requirements:
- [README](./security/README.md) - Security overview
- [Authentication](./security/authentication.md) - User authentication
- [Authorization](./security/authorization.md) - Access control
- [Secrets Management](./security/secrets-management.md) - Credential handling
- [Input Validation](./security/input-validation.md) - Data validation
- [Audit Logging](./security/audit-logging.md) - Security event logging

**Used by:** SARK for security validation

---

### Documentation (6 rules, ~1,959 lines)

Documentation standards and best practices:
- [README](./documentation/README.md) - Documentation philosophy
- [Docstring Standards](./documentation/docstring-standards.md) - Code documentation
- [README Structure](./documentation/readme-structure.md) - Project README format
- [API Documentation](./documentation/api-documentation.md) - API reference docs
- [Architecture Docs](./documentation/architecture-docs.md) - System design docs
- [Changelog Standards](./documentation/changelog-standards.md) - Version history
- [Inline Comments](./documentation/inline-comments.md) - Code comments

---

### Orchestration (2 patterns, ~1,098 lines)

Patterns for task coordination and agent orchestration:
- [README](./orchestration/README.md) - Orchestration overview
- [Task Coordination](./orchestration/task-coordination.md) - Multi-task management
- [Agent Handoffs](./orchestration/agent-handoffs.md) - Context transfer between agents

**Related Patterns:** [Mode Capabilities](../patterns/mode-capabilities/)

**Used by:** Czarina for worker coordination, Hopper for task routing

---

## Navigation by Use Case

### I want to set up a new Python project
**Relevant domains:**
- [Python Standards](./python-standards/) - Language fundamentals
- [Testing](./testing/) - Test setup and standards
- [Documentation](./documentation/) - Project documentation
- [Design Patterns](./design-patterns/) - Architecture guidance

**Quick-start templates:**
- See [Templates](../templates/) for project scaffolding

---

### I want to define agent roles for my project
**Relevant domains:**
- [Agent Roles](./agent-roles/) - Role definitions and responsibilities
- [Orchestration](./orchestration/) - Coordination patterns

**Related patterns:**
- [Mode Capabilities](../patterns/mode-capabilities/) - Role-specific strategies

**Example systems:**
- Hopper (task routing)
- The Symposium (multi-agent collaboration)

---

### I want to establish development workflows
**Relevant domains:**
- [Workflows](./workflows/) - Standard development workflows
- [Agent Roles](./agent-roles/) - Role-specific workflows

**Related patterns:**
- [Git Workflows](../patterns/git-workflows/) - Version control strategies
- [Error Recovery](../patterns/error-recovery/) - Recovery workflows

---

### I want to implement comprehensive testing
**Relevant domains:**
- [Testing](./testing/) - Testing standards
- [Python Standards](./python-standards/) - Language-level testing
- [Design Patterns](./design-patterns/) - Testable architecture

**Related patterns:**
- [Testing Patterns](../patterns/testing-patterns/) - Advanced testing strategies

---

### I want to secure my application
**Relevant domains:**
- [Security](./security/) - Security requirements and best practices

**Example systems:**
- SARK (security validation)

---

### I want to document my code properly
**Relevant domains:**
- [Documentation](./documentation/) - Documentation standards

**Example outputs:**
- This repository's documentation (meta-documentation)

---

### I want to coordinate multiple agents
**Relevant domains:**
- [Orchestration](./orchestration/) - Task and agent coordination
- [Agent Roles](./agent-roles/) - Role definitions

**Related patterns:**
- [Mode Capabilities](../patterns/mode-capabilities/) - Role-specific patterns

**Example systems:**
- Czarina (worker orchestration)
- The Symposium (multi-agent dialogue)
- Hopper (task routing)

---

## Relationship to Patterns

### Core Rules vs. Patterns

**Core Rules** define **WHAT**:
- Standards you must follow
- Requirements you must meet
- Definitions of roles and concepts
- Quality criteria

**Patterns** show **HOW**:
- Proven strategies for implementation
- Real-world examples
- Impact metrics and evidence
- Trade-offs and alternatives

### Example: Error Handling

**Core Rule:** [Python Standards - Error Handling](./python-standards/error-handling.md)
- Defines WHAT: Use specific exceptions, log errors, don't swallow exceptions

**Pattern:** [Error Recovery](../patterns/error-recovery/)
- Shows HOW: Retry patterns, fallback strategies, circuit breakers
- Provides evidence: 30-50% reduction in debugging time

### Cross-Reference Map

For detailed relationships between core rules and patterns, see:
- [Cross-Reference Map](../meta/cross-reference-map.md)
- [Patterns Index](../patterns/INDEX.md)

---

## Statistics

**Total Content:**
- 9 domains
- 53+ individual rules
- ~43,873 lines of content
- Production-tested in real projects

**Most Referenced:**
- Agent Roles (used by Hopper, Czarina, The Symposium)
- Python Standards (foundation for Python projects)
- Workflows (standard development processes)

**Coverage:**
- Python development ✓
- Multi-agent systems ✓
- Security and compliance ✓
- Documentation ✓
- Testing ✓
- Orchestration ✓

---

## Contributing

**Found a gap?** See [CONTRIBUTING.md](../CONTRIBUTING.md)

**Want to add a rule?** Follow the same process as adding patterns:
1. Use appropriate template
2. Provide evidence from real projects
3. Submit PR
4. Human review

**Questions?** Open an issue with the `question` label

---

## Related Documentation

- [Main README](../README.md) - Repository overview
- [Patterns Index](../patterns/INDEX.md) - Implementation patterns
- [Templates](../templates/) - Project templates
- [Examples](../examples/) - Real-world examples
- [CONTRIBUTING](../CONTRIBUTING.md) - How to contribute
- [CHANGELOG](../CHANGELOG.md) - Version history

---

**Last Updated:** 2025-12-28
**Version:** 1.0.0
