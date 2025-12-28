# Worker: migrate-patterns

## Mission
Migrate all content from the agentic-dev-patterns repository into the agent-knowledge repository's patterns/ directory, organizing the content into appropriate subdirectories.

## Deliverables
- Error recovery patterns migrated to patterns/error-recovery/
- Tool use patterns migrated to patterns/tool-use/
- Mode capabilities migrated to patterns/mode-capabilities/
- Git workflow patterns migrated to patterns/git-workflows/
- Testing patterns migrated to patterns/testing-patterns/
- Context management migrated to patterns/context-management/

## Context
You are migrating 6 pattern categories from the agentic-dev-patterns repository. These are battle-tested patterns from The Symposium project with proven impact:
- Error Recovery: 30-50% reduction in debugging time
- Tool Use: 40-60% efficiency improvement
- Mode Capabilities: Role-specific patterns
- Context Management: Memory optimization

## Dependencies
- repo-setup (must complete first to have directory structure)

## References
- Implementation Plan: `/home/jhenry/Source/agent-knowledge/AGENT_KNOWLEDGE_MERGE_PLAN.md` (lines 328-339)
- Source Repository: `/home/jhenry/Source/agentic-dev-patterns`
- Target Structure: Plan lines 227-267

## Task Breakdown

### Task 1: Migrate Error Recovery Patterns
```bash
mkdir -p /home/jhenry/Source/agent-knowledge/patterns/error-recovery
cp /home/jhenry/Source/agentic-dev-patterns/ERROR_RECOVERY_PATTERNS.md \
   /home/jhenry/Source/agent-knowledge/patterns/error-recovery/README.md
```

**Content to extract and organize:**
From ERROR_RECOVERY_PATTERNS.md, create separate files for:
- detection-patterns.md (pattern recognition and identification)
- recovery-strategies.md (recovery approaches)
- retry-patterns.md (retry logic and backoff)
- fallback-patterns.md (fallback mechanisms)
- escalation-patterns.md (when to escalate to human)

**Acceptance Criteria:**
- Main README.md created in error-recovery/
- Content organized into focused sub-documents
- All patterns from source preserved
- Impact metrics included (30-50% debugging time reduction)

### Task 2: Migrate Tool Use Patterns
```bash
mkdir -p /home/jhenry/Source/agent-knowledge/patterns/tool-use
cp /home/jhenry/Source/agentic-dev-patterns/TOOL_USE_PATTERNS.md \
   /home/jhenry/Source/agent-knowledge/patterns/tool-use/README.md
```

**Content to extract and organize:**
From TOOL_USE_PATTERNS.md, create separate files for:
- optimization-patterns.md (tool usage optimization)
- batching-patterns.md (batch operations)
- caching-patterns.md (caching strategies)
- parallel-execution.md (parallel tool calls)
- tool-selection.md (choosing the right tool)

**Acceptance Criteria:**
- Main README.md created in tool-use/
- Content organized into focused sub-documents
- All patterns from source preserved
- Impact metrics included (40-60% efficiency improvement)

### Task 3: Migrate Mode Capabilities
```bash
mkdir -p /home/jhenry/Source/agent-knowledge/patterns/mode-capabilities
cp /home/jhenry/Source/agentic-dev-patterns/MODE_CAPABILITIES.md \
   /home/jhenry/Source/agent-knowledge/patterns/mode-capabilities/README.md
```

**Content to extract and organize:**
From MODE_CAPABILITIES.md, create separate files for:
- architect-mode.md (architecture and planning mode)
- code-mode.md (implementation mode)
- debug-mode.md (debugging mode)
- ask-mode.md (clarification and Q&A mode)
- orchestrator-mode.md (coordination mode)
- mode-transitions.md (switching between modes)

**Acceptance Criteria:**
- Main README.md created in mode-capabilities/
- Content organized by mode type
- All mode capabilities documented
- Mode transition patterns included

### Task 4: Migrate Context Management
```bash
mkdir -p /home/jhenry/Source/agent-knowledge/patterns/context-management
cp /home/jhenry/Source/agentic-dev-patterns/CONTEXT_MANAGEMENT.md \
   /home/jhenry/Source/agent-knowledge/patterns/context-management/README.md
```

**Content to extract and organize:**
From CONTEXT_MANAGEMENT.md, create separate files for:
- context-windows.md (managing context limits)
- summarization.md (summarization strategies)
- memory-tiers.md (short-term vs long-term memory)
- attention-shaping.md (focusing attention)

**Acceptance Criteria:**
- Main README.md created in context-management/
- Content organized into focused sub-documents
- All context management strategies documented
- Practical examples included

### Task 5: Migrate Git Workflow Patterns
```bash
mkdir -p /home/jhenry/Source/agent-knowledge/patterns/git-workflows
cp /home/jhenry/Source/agentic-dev-patterns/GIT_WORKFLOW_PATTERNS.md \
   /home/jhenry/Source/agent-knowledge/patterns/git-workflows/README.md
```

**Content to extract and organize:**
From GIT_WORKFLOW_PATTERNS.md, create separate files for:
- branch-strategies.md (branching patterns)
- commit-patterns.md (commit message and organization)
- pr-workflows.md (pull request workflows)
- conflict-resolution.md (handling merge conflicts)

**Acceptance Criteria:**
- Main README.md created in git-workflows/
- Content organized into focused sub-documents
- All git workflow patterns documented
- Note added for harmonization with core-rules/workflows/git-workflows.md

### Task 6: Migrate Testing Patterns
```bash
mkdir -p /home/jhenry/Source/agent-knowledge/patterns/testing-patterns
cp /home/jhenry/Source/agentic-dev-patterns/TESTING_PATTERNS.md \
   /home/jhenry/Source/agent-knowledge/patterns/testing-patterns/README.md
```

**Content to organize:**
From TESTING_PATTERNS.md, create focused documentation on:
- Test-driven development patterns
- Testing automation strategies
- Coverage optimization
- Integration testing approaches

**Acceptance Criteria:**
- Main README.md created in testing-patterns/
- All testing patterns documented
- Note added for harmonization with core-rules/testing/

### Task 7: Preserve Source Documentation
```bash
cp /home/jhenry/Source/agentic-dev-patterns/README.md \
   /home/jhenry/Source/agent-knowledge/AGENTIC_DEV_PATTERNS_LEGACY.md
```

**Acceptance Criteria:**
- Original README preserved as AGENTIC_DEV_PATTERNS_LEGACY.md
- Source attribution maintained
- Historical context preserved

### Task 8: Create Patterns INDEX.md
Create `/home/jhenry/Source/agent-knowledge/patterns/INDEX.md`:

```markdown
# Patterns Index

Battle-tested patterns from real-world AI-assisted development projects.

## Categories

### Error Recovery
**Impact:** 30-50% reduction in debugging time

Patterns for detecting, recovering from, and learning from errors:
- [Overview](./error-recovery/README.md)
- [Detection Patterns](./error-recovery/detection-patterns.md)
- [Recovery Strategies](./error-recovery/recovery-strategies.md)
- [Retry Patterns](./error-recovery/retry-patterns.md)
- [Fallback Patterns](./error-recovery/fallback-patterns.md)
- [Escalation Patterns](./error-recovery/escalation-patterns.md)

### Tool Use
**Impact:** 40-60% efficiency improvement

Patterns for optimizing tool usage and execution:
- [Overview](./tool-use/README.md)
- [Optimization Patterns](./tool-use/optimization-patterns.md)
- [Batching Patterns](./tool-use/batching-patterns.md)
- [Caching Patterns](./tool-use/caching-patterns.md)
- [Parallel Execution](./tool-use/parallel-execution.md)
- [Tool Selection](./tool-use/tool-selection.md)

### Mode Capabilities
**Impact:** Clear role separation and coordination

Patterns for different agent modes and transitions:
- [Overview](./mode-capabilities/README.md)
- [Architect Mode](./mode-capabilities/architect-mode.md)
- [Code Mode](./mode-capabilities/code-mode.md)
- [Debug Mode](./mode-capabilities/debug-mode.md)
- [Ask Mode](./mode-capabilities/ask-mode.md)
- [Orchestrator Mode](./mode-capabilities/orchestrator-mode.md)
- [Mode Transitions](./mode-capabilities/mode-transitions.md)

### Context Management
**Impact:** Optimized memory usage and attention

Patterns for managing context windows and memory:
- [Overview](./context-management/README.md)
- [Context Windows](./context-management/context-windows.md)
- [Summarization](./context-management/summarization.md)
- [Memory Tiers](./context-management/memory-tiers.md)
- [Attention Shaping](./context-management/attention-shaping.md)

### Git Workflows
**Impact:** Consistent version control practices

Patterns for Git operations in AI-assisted development:
- [Overview](./git-workflows/README.md)
- [Branch Strategies](./git-workflows/branch-strategies.md)
- [Commit Patterns](./git-workflows/commit-patterns.md)
- [PR Workflows](./git-workflows/pr-workflows.md)
- [Conflict Resolution](./git-workflows/conflict-resolution.md)

**Note:** See also [Core Rules - Workflows](../core-rules/workflows/) for related content.

### Testing Patterns
**Impact:** Comprehensive test coverage and automation

Patterns for testing in AI-assisted development:
- [Overview](./testing-patterns/README.md)

**Note:** See also [Core Rules - Testing](../core-rules/testing/) for related content.

## Source Attribution

These patterns are derived from:
- **The Symposium Project** - Multi-agent development framework
- **Hopper** - Task routing and orchestration
- **Czarina** - Worker coordination and phase management
- **SARK** - Security and compliance automation

All patterns have been battle-tested in production environments.
```

**Acceptance Criteria:**
- INDEX.md created in patterns/
- All pattern categories listed
- Impact metrics included
- Cross-references to core-rules added
- Source attribution included

### Task 9: Create Migration Summary
Create `/home/jhenry/Source/agent-knowledge/meta/migration-agentic-dev-patterns.md`:

```markdown
# Migration Summary: agentic-dev-patterns

**Date:** [Current Date]
**Source:** /home/jhenry/Source/agentic-dev-patterns (v1.0.0)
**Target:** /home/jhenry/Source/agent-knowledge/patterns/

## Content Migrated

### Error Recovery Patterns
- Source: ERROR_RECOVERY_PATTERNS.md
- Target: patterns/error-recovery/
- Files created: 6 (README + 5 sub-patterns)
- Impact: 30-50% reduction in debugging time

### Tool Use Patterns
- Source: TOOL_USE_PATTERNS.md
- Target: patterns/tool-use/
- Files created: 6 (README + 5 sub-patterns)
- Impact: 40-60% efficiency improvement

### Mode Capabilities
- Source: MODE_CAPABILITIES.md
- Target: patterns/mode-capabilities/
- Files created: 7 (README + 6 mode docs)
- Impact: Clear role separation

### Context Management
- Source: CONTEXT_MANAGEMENT.md
- Target: patterns/context-management/
- Files created: 5 (README + 4 strategies)
- Impact: Optimized memory usage

### Git Workflows
- Source: GIT_WORKFLOW_PATTERNS.md
- Target: patterns/git-workflows/
- Files created: 5 (README + 4 workflow types)
- Note: Will need harmonization with core-rules/workflows/git-workflows.md

### Testing Patterns
- Source: TESTING_PATTERNS.md
- Target: patterns/testing-patterns/
- Files created: 1 (README)
- Note: Will need harmonization with core-rules/testing/

## Changes Made

- Reorganized single-file patterns into multi-file structure
- Created focused sub-documents for easier navigation
- Added INDEX.md for patterns directory
- Preserved original README as AGENTIC_DEV_PATTERNS_LEGACY.md
- Added cross-references to related core-rules

## Verification

- [x] All source files migrated
- [x] Content organized by category
- [x] Impact metrics preserved
- [x] INDEX.md created
- [x] No content lost
```

**Acceptance Criteria:**
- Migration summary created
- Includes all migrated categories
- Documents reorganization decisions
- Notes harmonization needs
- Saved in meta/ directory

### Task 10: Commit Migration
```bash
git add .
git commit -m "[migrate-patterns] Migrate agentic-dev-patterns content to patterns/

- Migrated 6 pattern categories from agentic-dev-patterns v1.0.0
- Organized into focused sub-documents for better navigation
- Created patterns/INDEX.md for navigation
- Preserved impact metrics and source attribution
- Created migration summary

Categories:
- Error Recovery (30-50% debugging time reduction)
- Tool Use (40-60% efficiency improvement)
- Mode Capabilities (clear role separation)
- Context Management (memory optimization)
- Git Workflows
- Testing Patterns"
```

**Acceptance Criteria:**
- Migration committed to git
- Commit message documents impact
- All migrated files staged and committed

## Success Criteria
- [ ] All 6 pattern categories migrated
- [ ] Content organized into focused sub-documents
- [ ] INDEX.md created for patterns/
- [ ] Impact metrics preserved
- [ ] Legacy README preserved
- [ ] Migration summary created
- [ ] Changes committed to git
- [ ] No content lost or corrupted
- [ ] Cross-references to core-rules added

## Notes
- Dependency: repo-setup must be complete before starting
- Can run in parallel with migrate-rules worker
- Use absolute paths: /home/jhenry/Source/agentic-dev-patterns and /home/jhenry/Source/agent-knowledge
- Note overlap with core-rules content for harmonize-content worker
- Keep original files in agentic-dev-patterns repo untouched
