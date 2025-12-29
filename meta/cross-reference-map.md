# Cross-Reference Map

This document maps relationships between core-rules and patterns content throughout the agent-knowledge repository.

## Purpose

**Core Rules** define **what** you must do (standards, requirements, definitions)
**Patterns** show **how** to do it well (proven strategies, examples, optimizations)

This map shows how they relate and link to each other.

## Cross-Reference Relationships

### 1. Git Workflows

**Core Rules:** [workflows/GIT_WORKFLOW.md](../core-rules/workflows/GIT_WORKFLOW.md)
- General git workflow rules and standards
- Required practices
- Workflow definitions
- Branch naming conventions
- Commit message requirements

**Patterns:** [git-workflows/](../patterns/git-workflows/)
- Specific branching strategies (feature branches, worker branches)
- Commit message patterns (conventional commits)
- PR workflow examples
- Conflict resolution techniques
- AI-generated commit messages

**Relationship:** Core rules define WHAT workflows to follow, patterns show HOW to implement them effectively.

**Bi-directional Links:**
- ✅ core-rules/workflows/GIT_WORKFLOW.md links to patterns/git-workflows/
- ✅ patterns/git-workflows/README.md links to core-rules/workflows/

---

### 2. Testing

**Core Rules:** [testing/](../core-rules/testing/)
- Testing philosophy and standards
- Pytest requirements
- Coverage requirements (80% minimum)
- Test organization rules
- Mocking strategies
- Unit vs integration testing definitions

**Patterns:** [testing-patterns/](../patterns/testing-patterns/)
- TDD strategies with AI assistants
- Test automation patterns
- Coverage optimization techniques
- AI-assisted test generation
- Test isolation patterns
- Real-world examples (81 tests, 100% pass rate)

**Relationship:** Core rules define testing REQUIREMENTS, patterns show testing STRATEGIES.

**Bi-directional Links:**
- ✅ core-rules/testing/ files link to patterns/testing-patterns/
- ✅ patterns/testing-patterns/README.md links to core-rules/testing/

---

### 3. Agent Roles / Mode Capabilities

**Core Rules:** [agent-roles/](../core-rules/agent-roles/)
- Role definitions (Architect, Code, Debug, QA, Orchestrator)
- Responsibilities per role
- Coordination requirements
- Role boundaries
- Multi-agent orchestration rules

**Patterns:** [mode-capabilities/](../patterns/mode-capabilities/)
- Mode-specific optimization patterns
- Transition strategies
- Mode best practices
- When to use each mode
- Decision trees for mode selection
- Real usage statistics (85% Code, 10% Architect, etc.)

**Relationship:** Core rules define role RESPONSIBILITIES, patterns show mode OPTIMIZATION.

**Bi-directional Links:**
- ✅ core-rules/agent-roles/ files link to patterns/mode-capabilities/
- ✅ patterns/mode-capabilities/ files link to core-rules/agent-roles/

---

### 4. Error Recovery

**Core Rules:** [design-patterns/ERROR_RECOVERY.md](../core-rules/design-patterns/ERROR_RECOVERY.md)
- General recovery principles
- Error handling philosophy
- Recovery requirements
- Logging standards

**Patterns:** [error-recovery/](../patterns/error-recovery/)
- Detailed detection patterns (Docker, Python, database, git)
- Specific recovery strategies
- Retry and fallback patterns
- Escalation decision trees
- Real-world error examples
- Step-by-step recovery procedures

**Relationship:** Core rules define recovery PRINCIPLES, patterns show recovery TACTICS.

**Bi-directional Links:**
- ✅ core-rules/design-patterns/ERROR_RECOVERY.md links to patterns/error-recovery/
- ✅ patterns/error-recovery/README.md links to core-rules/design-patterns/

---

### 5. Context Management

**Core Rules:** [orchestration/ORCHESTRATION_PATTERNS.md](../core-rules/orchestration/ORCHESTRATION_PATTERNS.md)
- Multi-agent coordination
- Context handoff requirements
- State management rules

**Patterns:** [context-management/](../patterns/context-management/)
- Context window strategies
- Summarization techniques (70-80% context reduction)
- Memory tier management (Working, Session, Project, Reference)
- Attention shaping
- Progressive context building
- Handoff summaries

**Relationship:** Core rules define coordination REQUIREMENTS, patterns show context OPTIMIZATION.

**Bi-directional Links:**
- ✅ core-rules/orchestration/ links to patterns/context-management/
- ✅ patterns/context-management/README.md links to core-rules/orchestration/

---

### 6. Tool Usage

**Core Rules:** Implicit in role definitions
- Tool responsibilities per role
- Tool usage requirements
- File operation standards

**Related Core Rules:**
- [design-patterns/TOOL_USE_PATTERNS.md](../core-rules/design-patterns/TOOL_USE_PATTERNS.md) - Tool usage principles
- [agent-roles/CODE_ROLE.md](../core-rules/agent-roles/CODE_ROLE.md) - Full tool access
- [agent-roles/ARCHITECT_ROLE.md](../core-rules/agent-roles/ARCHITECT_ROLE.md) - Limited tool access

**Patterns:** [tool-use/](../patterns/tool-use/)
- Tool optimization patterns (40-60% efficiency improvement)
- Batching strategies (parallel file reading)
- Caching techniques
- Parallel execution patterns
- Tool selection decision trees
- Performance optimization

**Relationship:** Core rules define WHAT tools to use, patterns show HOW to use them optimally.

**Bi-directional Links:**
- ✅ core-rules/design-patterns/TOOL_USE_PATTERNS.md links to patterns/tool-use/
- ✅ patterns/tool-use/ references relevant agent roles

---

### 7. Python Standards / Error Handling

**Core Rules:** [python-standards/](../core-rules/python-standards/)
- Python coding standards
- Async/await patterns
- Error handling requirements
- Security patterns
- Dependency injection

**Patterns:** [error-recovery/](../patterns/error-recovery/)
- Python-specific error patterns
- Async/await troubleshooting
- Module import errors
- Common Python pitfalls

**Relationship:** Core rules define Python STANDARDS, patterns show Python ERROR SOLUTIONS.

**Bi-directional Links:**
- ✅ core-rules/python-standards/ERROR_HANDLING.md links to patterns/error-recovery/
- ✅ patterns/error-recovery/detection-patterns.md links to core-rules/python-standards/

---

### 8. Documentation Standards / Git Workflows

**Core Rules:** [documentation/](../core-rules/documentation/)
- Documentation standards
- README requirements
- API documentation
- Architecture documentation
- Changelog standards

**Related to:**
- [workflows/DOCUMENTATION_WORKFLOW.md](../core-rules/workflows/DOCUMENTATION_WORKFLOW.md) - Documentation maintenance
- [patterns/git-workflows/](../patterns/git-workflows/) - Documentation sync with git

**Relationship:** Core rules define documentation STANDARDS, workflows define MAINTENANCE, patterns show SYNC STRATEGIES.

**Bi-directional Links:**
- ✅ core-rules/documentation/ links to workflows/DOCUMENTATION_WORKFLOW.md
- ✅ core-rules/workflows/DOCUMENTATION_WORKFLOW.md links to patterns/git-workflows/

---

## Cross-Reference Coverage

### Files with Cross-References

**Core Rules files with pattern references:**
1. core-rules/workflows/GIT_WORKFLOW.md → patterns/git-workflows/
2. core-rules/design-patterns/ERROR_RECOVERY.md → patterns/error-recovery/
3. core-rules/testing/README.md → patterns/testing-patterns/
4. core-rules/agent-roles/README.md → patterns/mode-capabilities/
5. core-rules/orchestration/ORCHESTRATION_PATTERNS.md → patterns/context-management/
6. core-rules/design-patterns/TOOL_USE_PATTERNS.md → patterns/tool-use/
7. core-rules/python-standards/ERROR_HANDLING.md → patterns/error-recovery/
8. core-rules/documentation/README.md → workflows/DOCUMENTATION_WORKFLOW.md

**Pattern files with core-rules references:**
1. patterns/git-workflows/README.md → core-rules/workflows/
2. patterns/testing-patterns/README.md → core-rules/testing/
3. patterns/error-recovery/README.md → core-rules/design-patterns/
4. patterns/mode-capabilities/README.md → core-rules/agent-roles/
5. patterns/context-management/README.md → core-rules/orchestration/
6. patterns/tool-use/README.md → core-rules/design-patterns/ and core-rules/agent-roles/

---

## Navigation Guidelines

### When to Use Core Rules vs Patterns

**Use Core Rules when:**
- You need to know the requirements and standards
- You're setting up a new project or team
- You need to understand "what" is required
- You're doing code review or validation
- You need templates or reference documentation

**Use Patterns when:**
- You need to know how to implement something
- You're troubleshooting an issue
- You want to optimize your workflow
- You need real-world examples
- You want to learn proven strategies

### Cross-Navigation Flow

```
Need a standard? → Core Rules → See "Related Patterns" section → Patterns for implementation

Have a problem? → Patterns → See "Related Core Rules" section → Core Rules for requirements
```

---

## Validation

- [x] All major content overlaps mapped
- [x] Bi-directional references documented
- [x] Relationship principles clear
- [x] Coverage comprehensive
- [x] 8 major relationship areas identified
- [x] Navigation guidelines provided

---

## Maintenance

When adding new content:

1. **Identify category**: Is it a "what" (core-rule) or "how" (pattern)?
2. **Check for related content**: Does related content exist in the other category?
3. **Add bi-directional cross-references**:
   - Add "Related Patterns" section in core-rules
   - Add "Related Core Rules" section in patterns
4. **Update this map**: Add the new relationship to this document
5. **Verify links**: Ensure all cross-references are valid

### Cross-Reference Section Template

For core-rules files:
```markdown
## Related Patterns

For specific implementation patterns and examples, see:
- [Pattern Category](../../patterns/category/README.md)
- [Specific Pattern](../../patterns/category/pattern.md)
```

For pattern files:
```markdown
## Related Core Rules

For standards and requirements, see:
- [Core Rule Category](../../core-rules/category/README.md)
- [Specific Rule](../../core-rules/category/rule.md)
```

---

## Statistics

- **Core Rules Categories:** 8 (python-standards, agent-roles, workflows, design-patterns, testing, security, documentation, orchestration)
- **Pattern Categories:** 6 (error-recovery, tool-use, mode-capabilities, context-management, git-workflows, testing-patterns)
- **Cross-Reference Relationships:** 8 major areas
- **Files with Cross-References:** 14+ (growing)

---

**Created:** 2025-12-29
**Worker:** complete-deliverables
**Status:** Complete
**Version:** 1.0.0
