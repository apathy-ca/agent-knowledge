# Patterns Index

Battle-tested patterns with quantified impact from real projects.

**What are Patterns?** Proven strategies that show **how** to implement requirements effectively.

**How do they relate to Core Rules?** [Core Rules](../core-rules/INDEX.md) define what you must do; Patterns show how to do it well.

---

## Navigation by Category

### Error Recovery

**Impact:** 30-50% reduction in debugging time

Strategies for handling failures gracefully and recovering from errors:
- Retry patterns with exponential backoff
- Fallback strategies and graceful degradation
- Circuit breaker patterns
- Error context preservation
- Recovery workflows

**Related Core Rules:** [Error Handling](../core-rules/python-standards/error-handling.md), [Recovery Workflow](../core-rules/workflows/recovery-workflow.md)

**Directory:** [error-recovery/](./error-recovery/)

---

### Tool Use

**Impact:** 40-60% efficiency improvement

Optimization strategies for effective tool usage:
- Parallel tool calls for independent operations
- Tool selection strategies
- Error handling in tool calls
- Tool call batching and optimization
- Context-aware tool usage

**Related Core Rules:** [Agent Roles](../core-rules/agent-roles/), [Workflows](../core-rules/workflows/)

**Directory:** [tool-use/](./tool-use/)

---

### Mode Capabilities

**Impact:** Clear role separation and improved collaboration

Role-specific patterns for different agent modes:
- Code mode patterns (implementation strategies)
- Ask mode patterns (information gathering)
- Orchestrator patterns (coordination)
- Debug mode patterns (troubleshooting)
- Architect mode patterns (design)

**Related Core Rules:** [Agent Roles](../core-rules/agent-roles/), [Orchestration](../core-rules/orchestration/)

**Directory:** [mode-capabilities/](./mode-capabilities/)

---

### Context Management

**Impact:** Memory optimization and efficient context usage

Strategies for managing context windows and memory:
- Context window optimization
- Summarization patterns
- Context handoff between agents
- Memory management strategies
- Selective context inclusion

**Related Core Rules:** [Memory Patterns](../core-rules/design-patterns/memory-patterns.md), [Agent Handoffs](../core-rules/orchestration/agent-handoffs.md)

**Directory:** [context-management/](./context-management/)

---

### Git Workflows

**Impact:** Consistent version control and collaboration

Branch strategies, commit patterns, and PR workflows:
- Branch naming conventions
- Commit message patterns
- PR workflow strategies
- Conflict resolution patterns
- Version control best practices

**Related Core Rules:** [Git Workflows](../core-rules/workflows/git-workflows.md)

**Directory:** [git-workflows/](./git-workflows/)

---

### Testing Patterns

**Impact:** Comprehensive coverage and test quality

Advanced testing strategies and organization:
- Test organization patterns
- Mocking and fixture strategies
- Integration testing approaches
- Coverage optimization
- Test maintenance patterns

**Related Core Rules:** [Testing](../core-rules/testing/), [Pytest Standards](../core-rules/testing/pytest-standards.md)

**Directory:** [testing-patterns/](./testing-patterns/) (if exists)

---

## Navigation by Impact

### Highest Efficiency Gains
1. **Tool Use** (40-60% improvement) - Parallel execution, optimization
2. **Error Recovery** (30-50% reduction) - Faster debugging, resilient systems
3. **Context Management** - Reduced token usage, faster operations

### Best for Collaboration
1. **Mode Capabilities** - Clear roles, effective coordination
2. **Git Workflows** - Consistent version control
3. **Context Management** - Smooth agent handoffs

### Best for Quality
1. **Testing Patterns** - Comprehensive coverage
2. **Error Recovery** - Resilient systems
3. **Tool Use** - Correct and efficient operations

---

## Navigation by Use Case

### I want to build more resilient systems
**Recommended patterns:**
- [Error Recovery](./error-recovery/) - Handle failures gracefully
- **Related core rules:** [Recovery Workflow](../core-rules/workflows/recovery-workflow.md)

---

### I want to work more efficiently
**Recommended patterns:**
- [Tool Use](./tool-use/) - Optimize tool calls
- [Context Management](./context-management/) - Manage memory effectively
- **Related core rules:** [Workflows](../core-rules/workflows/)

---

### I want to coordinate multiple agents
**Recommended patterns:**
- [Mode Capabilities](./mode-capabilities/) - Role-specific strategies
- [Context Management](./context-management/) - Context handoff
- **Related core rules:** [Orchestration](../core-rules/orchestration/), [Agent Roles](../core-rules/agent-roles/)

---

### I want to improve my version control
**Recommended patterns:**
- [Git Workflows](./git-workflows/) - Branch and commit strategies
- **Related core rules:** [Git Workflows](../core-rules/workflows/git-workflows.md)

---

### I want to write better tests
**Recommended patterns:**
- [Testing Patterns](./testing-patterns/) - Advanced testing strategies (if exists)
- **Related core rules:** [Testing](../core-rules/testing/)

---

## Relationship to Core Rules

### Patterns vs. Core Rules

**Patterns** show **HOW**:
- Proven strategies from real projects
- Real-world examples with code
- Quantified impact metrics
- Trade-offs and alternatives

**Core Rules** define **WHAT**:
- Standards and requirements
- Role definitions
- Quality criteria
- Workflow structures

### Example: Error Handling

**Core Rule:** [Error Handling](../core-rules/python-standards/error-handling.md)
- Defines WHAT: Use specific exceptions, log errors, handle failures properly

**Pattern:** [Error Recovery](./error-recovery/)
- Shows HOW: Retry with exponential backoff, circuit breakers, fallback strategies
- Provides evidence: 30-50% reduction in debugging time

### Cross-Reference Map

For detailed relationships between patterns and core rules, see:
- [Cross-Reference Map](../meta/cross-reference-map.md)
- [Core Rules Index](../core-rules/INDEX.md)

---

## Pattern Quality Levels

### Proven
- Used successfully in 3+ projects
- Quantified impact from multiple sources
- Recommended for general use

### Accepted
- Reviewed and approved
- Evidence from at least one project
- Documented impact

### Proposed
- New pattern, not yet battle-tested
- Requires additional validation
- Under review

See [Pattern Template](../meta/pattern-template.md) for submission guidelines.

---

## Statistics

**Total Categories:** 6

**Migration Status (2025-12-28):**
- ✅ Error Recovery: **COMPLETE** (6 documents) - Migrated from agentic-dev-patterns
- ✅ Tool Use: **COMPLETE** (6 documents) - Migrated from agentic-dev-patterns
- ✅ Mode Capabilities: **COMPLETE** (7 documents) - Migrated from agentic-dev-patterns
- 🚧 Context Management: **PLACEHOLDER** - Content to be developed
- 🚧 Git Workflows: **PLACEHOLDER** - Content to be developed (harmonization needed with core-rules)
- 🚧 Testing Patterns: **PLACEHOLDER** - Content to be developed (harmonization needed with core-rules)

**Impact Metrics:**
- Error Recovery: 30-50% reduction in debugging time
- Tool Use: 40-60% efficiency improvement
- Mode Capabilities: Clear role separation
- Context Management: Memory optimization (to be developed)
- Git Workflows: Consistent version control (to be developed)
- Testing Patterns: Comprehensive coverage (to be developed)

**Source Projects:**
- The Symposium (multi-agent collaboration platform - v0.4.5)
- Agentic-dev-patterns repository (v1.0.0)
- Hopper (task routing)
- Czarina (orchestration)
- SARK (security validation)

**Documentation Status:**
- Error handling and recovery ✅ (Complete with 6 focused sub-documents)
- Tool usage optimization ✅ (Complete with 6 focused sub-documents)
- Multi-agent coordination ✅ (Complete with 7 mode-specific documents)
- Context management 🚧 (Placeholder - needs development)
- Version control 🚧 (Placeholder - needs development + harmonization)
- Testing strategies 🚧 (Placeholder - needs development + harmonization)

---

## Contributing

**Have a pattern to share?** See [CONTRIBUTING.md](../CONTRIBUTING.md)

**Pattern submission process:**
1. Use the [Pattern Template](../meta/pattern-template.md)
2. Provide evidence from real projects
3. Document impact (quantified or qualitative)
4. Submit PR for review
5. Human review and approval

**Questions?** Open an issue with the `pattern` label

---

## Continuous Improvement

Patterns are continuously extracted from:
- **Czarina closeout learnings** - Worker insights and observations
- **Hopper task feedback** - Routing and execution patterns
- **Symposium Sage wisdom** - Multi-agent collaboration patterns
- **SARK security learnings** - Security pattern effectiveness

See [Learning Extraction](../meta/learning-extraction.md) for the full workflow.

---

## Related Documentation

- [Main README](../README.md) - Repository overview
- [Core Rules Index](../core-rules/INDEX.md) - Standards and requirements
- [Pattern Template](../meta/pattern-template.md) - Template for new patterns
- [Learning Extraction](../meta/learning-extraction.md) - How patterns are captured
- [CONTRIBUTING](../CONTRIBUTING.md) - How to contribute
- [CHANGELOG](../CHANGELOG.md) - Version history

---

**Last Updated:** 2025-12-28
**Version:** 1.0.0
