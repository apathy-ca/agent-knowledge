# Content Overlap Analysis

**Date**: 2025-12-28
**Worker**: harmonize-content
**Purpose**: Analyze overlapping content between agent-rules and agentic-dev-patterns repositories

## Executive Summary

After examining both source repositories, the actual overlap is **less than initially expected**. The agentic-dev-patterns repository is smaller and more focused than anticipated, containing only 4 core markdown files. Many patterns mentioned in its README (GIT_WORKFLOW_PATTERNS.md, TESTING_PATTERNS.md, DOCUMENTATION_PATTERNS.md) do not actually exist as separate files yet.

## Overlapping Content Areas

### 1. Git Workflows

**Source Files**:
- **agent-rules**: `/agent-rules/workflows/GIT_WORKFLOW.md` (23,752 bytes)
  - Comprehensive git workflow for AI agent development
  - Branch naming conventions (feature/, fix/, etc.)
  - PR-based development requirements
  - Conventional commits
  - Documentation synchronization
  - Production-tested from The Symposium

- **agentic-dev-patterns**: `GIT_WORKFLOW_PATTERNS.md` (DOES NOT EXIST)
  - Referenced in README but file doesn't exist
  - README mentions: commit frequency, branch strategies, PR workflows, documentation sync

**Overlap Assessment**: **MINIMAL**
- Only one actual file exists (from agent-rules)
- The agentic-dev-patterns file is referenced but not created yet

**Resolution Strategy**:
1. Migrate agent-rules GIT_WORKFLOW.md to `core-rules/workflows/git-workflows.md` as the primary source
2. If migrate-patterns worker creates git-workflows content, place in `patterns/git-workflows/`
3. Add cross-references between locations
4. Ensure core-rules has standards/requirements, patterns has examples

### 2. Testing

**Source Files**:
- **agent-rules**: `/agent-rules/testing/` (6 files, ~111K total)
  - COVERAGE_STANDARDS.md (14,216 bytes)
  - INTEGRATION_TESTING.md (28,531 bytes)
  - MOCKING_STRATEGIES.md (19,699 bytes)
  - README.md (14,107 bytes)
  - TESTING_POLICY.md (12,919 bytes)
  - UNIT_TESTING.md (22,227 bytes)

- **agentic-dev-patterns**: `TESTING_PATTERNS.md` (DOES NOT EXIST)
  - Referenced in README but file doesn't exist
  - README mentions: unit test creation, integration test design, test isolation, coverage goals

**Overlap Assessment**: **MINIMAL**
- Comprehensive content exists only in agent-rules
- The agentic-dev-patterns file is referenced but not created yet

**Resolution Strategy**:
1. Migrate all agent-rules testing content to `core-rules/testing/`
2. If migrate-patterns creates testing-patterns content, place in `patterns/testing-patterns/`
3. Add cross-references
4. Core-rules = standards and requirements, patterns = strategies and examples

### 3. Agent Roles vs Mode Capabilities

**Source Files**:
- **agent-rules**: `/agent-rules/agents/` (7 files, ~120K total)
  - AGENT_ROLES.md (12,690 bytes)
  - ARCHITECT_ROLE.md (13,681 bytes)
  - CODE_ROLE.md (16,400 bytes)
  - DEBUG_ROLE.md (18,459 bytes)
  - ORCHESTRATOR_ROLE.md (27,372 bytes)
  - QA_ROLE.md (20,081 bytes)
  - README.md (12,514 bytes)

- **agentic-dev-patterns**: `MODE_CAPABILITIES.md` (6,825 bytes)
  - Defines 5 modes for Kilo Code: Architect, Code, Debug, Ask, Orchestrator
  - Specific capabilities and constraints per mode
  - File patterns allowed per mode

**Overlap Assessment**: **MODERATE**
- Both define role-based capabilities
- agent-rules is more generic (agent roles for any system)
- agentic-dev-patterns is Kilo Code-specific (mode capabilities)
- Different perspectives on similar concepts

**Resolution Strategy**:
1. Migrate agent-rules content to `core-rules/agent-roles/` - generic role definitions
2. Migrate MODE_CAPABILITIES.md to `patterns/mode-capabilities/` - specific mode optimization
3. Add cross-references showing relationship
4. Core-rules = role definitions and responsibilities (generic)
5. Patterns = mode-specific optimization and transitions (tool-specific)

### 4. Error Recovery

**Source Files**:
- **agent-rules**: No dedicated error recovery content
  - Some error handling in workflows/

- **agentic-dev-patterns**: `ERROR_RECOVERY_PATTERNS.md` (8,150 bytes)
  - Docker networking issues
  - Database connection failures
  - Async/await pitfalls
  - Import resolution
  - Syntax error recovery

**Overlap Assessment**: **NONE**
- Unique to agentic-dev-patterns
- No equivalent in agent-rules

**Resolution Strategy**:
1. Migrate ERROR_RECOVERY_PATTERNS.md to `patterns/error-recovery/`
2. No harmonization needed (unique content)
3. If any workflow error recovery exists in agent-rules, add cross-reference

### 5. Tool Use

**Source Files**:
- **agent-rules**: No dedicated tool use content
  - Some tool guidance in role definitions

- **agentic-dev-patterns**: `TOOL_USE_PATTERNS.md` (1,524 bytes)
  - File reading strategies
  - Search vs read decisions
  - Modification approaches
  - Command execution
  - Performance optimization

**Overlap Assessment**: **NONE**
- Unique to agentic-dev-patterns
- No equivalent in agent-rules

**Resolution Strategy**:
1. Migrate TOOL_USE_PATTERNS.md to `patterns/tool-use/`
2. No harmonization needed (unique content)

### 6. Documentation Workflows

**Source Files**:
- **agent-rules**: `/agent-rules/workflows/DOCUMENTATION_WORKFLOW.md` (28,087 bytes)
  - Documentation-first development
  - Sync strategies
  - Archiving workflows
  - Living documents

- **agentic-dev-patterns**: `DOCUMENTATION_PATTERNS.md` (DOES NOT EXIST)
  - Referenced in README but file doesn't exist

**Overlap Assessment**: **NONE**
- Only exists in agent-rules
- agentic-dev-patterns reference is placeholder

**Resolution Strategy**:
1. Migrate DOCUMENTATION_WORKFLOW.md to `core-rules/workflows/documentation-workflow.md`
2. No harmonization needed

## Unique Content

### From agent-rules Only
- Python standards
- Security patterns
- PR requirements (workflows/PR_REQUIREMENTS.md)
- Phase development (workflows/PHASE_DEVELOPMENT.md)
- Token planning (workflows/TOKEN_PLANNING.md)
- Closeout process (workflows/CLOSEOUT_PROCESS.md)
- Comprehensive testing standards
- Agent role definitions

### From agentic-dev-patterns Only
- Error recovery patterns (actual file)
- Tool use patterns (actual file)
- Mode capabilities (actual file)

### Referenced But Not Existing in agentic-dev-patterns
- GIT_WORKFLOW_PATTERNS.md
- TESTING_PATTERNS.md
- DOCUMENTATION_PATTERNS.md

## Overall Assessment

**Actual Overlap**: **Much less than expected**

The agentic-dev-patterns repository is a lean, focused collection of 4 markdown files:
1. README.md
2. ERROR_RECOVERY_PATTERNS.md
3. MODE_CAPABILITIES.md
4. TOOL_USE_PATTERNS.md

Many patterns referenced in the README don't exist as separate files yet. This means:
- Less deduplication work needed
- More straightforward migration
- Clearer separation of concerns
- Focus on cross-referencing rather than merging

## Harmonization Priority

### High Priority (Actual Overlap)
1. **Agent Roles / Mode Capabilities** - Moderate overlap, different perspectives
   - Requires thoughtful cross-referencing
   - Clear separation: generic roles vs mode-specific optimization

### Low Priority (Minimal Overlap)
2. **Git Workflows** - Only one file exists
   - Straightforward migration
   - Add placeholder cross-references

3. **Testing** - Only comprehensive content in agent-rules
   - Straightforward migration
   - Add placeholder cross-references

### No Priority (No Overlap)
4. **Error Recovery** - Unique to patterns
5. **Tool Use** - Unique to patterns
6. **Documentation** - Unique to core-rules

## Success Criteria

- [ ] Clear separation established: core-rules = standards/definitions, patterns = strategies/examples
- [ ] All actual overlaps identified and resolved
- [ ] Cross-references added for related content
- [ ] No duplicate content in repository
- [ ] Navigation clear between related topics

## Next Steps

1. Wait for migrate-rules and migrate-patterns workers to complete
2. Examine actual migrated content in core-rules/ and patterns/
3. Execute harmonization tasks based on actual content (not assumptions)
4. Focus on Agent Roles/Mode Capabilities as primary overlap
5. Add comprehensive cross-references throughout

## Notes

- The implementation plan may have been based on assumptions about agentic-dev-patterns content
- Actual content is leaner than expected
- This is good news - less work, clearer structure
- Focus should be on excellent cross-referencing rather than complex deduplication
