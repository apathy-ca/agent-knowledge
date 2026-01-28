# Content Overlap Analysis

**Date:** 2025-12-29 (Updated)
**Worker:** harmonize-content
**Purpose:** Identify and resolve overlapping content between core-rules and patterns

---

## Executive Summary

After analyzing the repository structure post-migration, I've identified **4 main areas of content overlap** between core-rules and patterns. In all cases, the content is already **well-separated** with clear cross-references in place. The existing structure follows the principle:

- **Core Rules** = Standards, requirements, definitions (the "what")
- **Patterns** = Strategies, examples, optimizations (the "how")

Most harmonization work involves **validating existing cross-references** and **ensuring consistency** rather than major restructuring.

---

## 1. Git Workflows

### Current State

**core-rules/workflows/GIT_WORKFLOW.md** (990 lines)
- Complete git workflow documentation
- Branch naming conventions
- Commit message structure (conventional commits)
- PR workflow and merge strategies
- Multi-agent coordination patterns
- **Cross-reference status:** ✅ Has cross-reference to patterns at line 987-989

**patterns/git-workflows/README.md** (68 lines)
- Placeholder file marked as "To be populated"
- Planning structure for future content from agentic-dev-patterns
- **Cross-reference status:** ✅ Has cross-references to core-rules at lines 13-17, 62-67

### Overlap Assessment

**Overlap:** ❌ **NONE** - The patterns directory is a placeholder awaiting content

**Unique to core-rules:**
- All current git workflow content
- Conventional commit standards
- PR requirements
- Branch strategies
- Czarina orchestration patterns

**Unique to patterns:**
- None yet (placeholder only)

### Resolution Strategy

✅ **NO ACTION REQUIRED** - Content is already separated:
1. Core rules define the standards
2. Patterns directory will contain specific examples when populated
3. Cross-references are already in place
4. Both files reference each other correctly

**Recommendation:** Monitor when patterns are populated to ensure no duplication occurs.

---

## 2. Testing Content

### Current State

**core-rules/testing/** (580 lines in README.md + 5 additional files)
- Complete testing standards and policy
- Test organization and structure
- Coverage requirements (80% minimum for new code)
- pytest configuration
- Unit, integration, mocking, and coverage standards
- **Cross-reference status:** ✅ Has cross-reference to patterns at lines 569-572

**patterns/testing-patterns/README.md** (93 lines)
- Placeholder file marked as "To be populated"
- Planning structure for AI-assisted TDD patterns
- **Cross-reference status:** ✅ Has cross-references to core-rules at lines 13-20, 80-88

### Overlap Assessment

**Overlap:** ❌ **NONE** - The patterns directory is a placeholder awaiting content

**Unique to core-rules:**
- Testing policy and requirements
- Unit testing standards
- Integration testing with Docker
- Mocking strategies
- Coverage standards and tools
- pytest configuration examples

**Unique to patterns:**
- None yet (placeholder only)

### Resolution Strategy

✅ **NO ACTION REQUIRED** - Content is already separated:
1. Core rules define comprehensive testing standards
2. Patterns directory will contain AI-assisted TDD strategies when populated
3. Cross-references are already in place
4. Clear separation: core-rules = requirements, patterns = AI strategies

**Recommendation:** When patterns are populated, ensure they focus on AI-specific testing approaches (test generation, TDD with AI assistants) rather than duplicating general testing standards.

---

## 3. Agent Roles vs Mode Capabilities

### Current State

**core-rules/agent-roles/README.md** (478 lines + 6 role-specific files)
- Generic agent role definitions (Architect, Code, Debug, QA, Orchestrator)
- Worker taxonomy and organization
- Role selection guide
- Orchestration patterns
- Worker templates
- **Cross-reference status:** ✅ Has cross-reference to patterns at lines 463-466

**patterns/mode-capabilities/README.md** (111 lines)
- Placeholder file marked as "To be populated"
- Planning structure for tool-specific mode optimization
- **Cross-reference status:** ✅ Has cross-references to core-rules at lines 13-20, 98-106

### Overlap Assessment

**Overlap:** ❌ **NONE** - Clear conceptual separation

**Difference:**
- **Agent Roles** (core-rules): Generic role definitions independent of tool
- **Mode Capabilities** (patterns): Tool-specific mode optimization (Kilo Code, Claude Code, etc.)

**Unique to core-rules:**
- Role taxonomy (Architect, Code, Debug, QA, Orchestrator)
- Responsibilities and coordination patterns
- Worker organization strategies
- Orchestration workflows

**Unique to patterns:**
- None yet (placeholder only)
- Will contain: tool-specific capabilities, mode transitions, optimization per mode

### Resolution Strategy

✅ **NO ACTION REQUIRED** - Content is conceptually different:
1. Core rules = what roles should do (tool-agnostic)
2. Patterns = how to optimize within specific tools (tool-specific)
3. Cross-references already in place
4. Explanation of relationship included in both files (lines 74-86 in patterns/README.md)

**Recommendation:** When patterns are populated, maintain clear distinction between generic role responsibilities and tool-specific mode features.

---

## 4. Error Recovery

### Current State

**core-rules/design-patterns/ERROR_RECOVERY.md** (1,287 lines)
- Comprehensive error recovery design patterns
- Retry with exponential backoff (with code from SARK)
- Circuit breaker pattern
- Error classification
- Graceful degradation
- Timeout management
- **Cross-reference status:** ✅ Has cross-references to patterns at lines 1271-1277

**patterns/error-recovery/README.md** (109 lines + 4 additional pattern files)
- AI-assisted development error patterns
- Common errors from real experience
- Quick pattern recognition
- Links to detailed pattern files (detection, recovery, retry, fallback)
- **Cross-reference status:** ✅ Has cross-reference to core-rules at lines 97-101

### Overlap Assessment

**Overlap:** ⚠️ **MINIMAL** - Some conceptual overlap but different focus

**Unique to core-rules:**
- Design pattern implementations (with code)
- Retry handler class implementation
- Circuit breaker class implementation
- Error classification system
- Theoretical foundations and best practices

**Unique to patterns:**
- AI-assisted development specific errors (Docker, Python, async, import)
- Quick reference for common error patterns
- Practical recovery strategies
- Battle-tested examples from The Symposium

**Conceptual Difference:**
- **Core rules:** Generic error recovery design patterns (implementation-focused)
- **Patterns:** AI-specific error patterns and quick recovery (troubleshooting-focused)

### Resolution Strategy

✅ **MINIMAL ACTION REQUIRED** - Content serves different purposes:
1. Core rules provide implementation patterns (code libraries)
2. Patterns provide troubleshooting guides (error catalog)
3. Cross-references already in place
4. Natural division: design vs troubleshooting

**Action Items:**
- Verify cross-references are comprehensive ✓
- Ensure no duplicate error examples between the two
- Natural separation is appropriate

---

## 5. Memory/Context Management

### Current State

**core-rules/design-patterns/**
- No memory-specific patterns found
- ERROR_RECOVERY.md, CACHING_PATTERNS.md, BATCH_OPERATIONS.md, etc. exist
- **Cross-reference status:** ❌ No memory patterns document found

**patterns/context-management/README.md** (73 lines)
- Placeholder file marked as "To be populated"
- Planning structure for context management in AI interactions
- Memory tiers, attention management, conversation management
- **Cross-reference status:** ⚠️ References core-rules/design-patterns generically at lines 64-66

### Overlap Assessment

**Overlap:** ❌ **NONE** - Core rules don't have memory patterns document

**Finding:** The task instructions mention "design-patterns/memory-patterns.md" but this file doesn't exist. The cross-reference in Task 6 (lines 209-220 of worker instructions) references a non-existent file.

**Unique to patterns:**
- None yet (placeholder only)
- Will contain: memory tiers, context window management, attention management

### Resolution Strategy

✅ **UPDATE CROSS-REFERENCES ONLY**
1. No harmonization needed (no core-rules memory patterns exist)
2. Update patterns/context-management/README.md to remove reference to non-existent file
3. Cross-reference to related design patterns instead (CACHING_PATTERNS.md if relevant)
4. **Task 6 will be modified** - update cross-references to point to existing files only

---

## Additional Findings

### Files with Existing Cross-References

1. **core-rules/workflows/GIT_WORKFLOW.md** ✅
   - Lines 987-989: Links to patterns/git-workflows/

2. **core-rules/testing/README.md** ✅
   - Lines 569-572: Links to patterns/testing-patterns/

3. **core-rules/agent-roles/README.md** ✅
   - Lines 463-466: Links to patterns/mode-capabilities/

4. **core-rules/design-patterns/ERROR_RECOVERY.md** ✅
   - Lines 1271-1277: Links to patterns/error-recovery/ (comprehensive)

5. **patterns/git-workflows/README.md** ✅
   - Lines 13-17, 62-67: Links to core-rules/workflows/

6. **patterns/testing-patterns/README.md** ✅
   - Lines 13-20, 80-88: Links to core-rules/testing/

7. **patterns/mode-capabilities/README.md** ✅
   - Lines 13-20, 98-106: Links to core-rules/agent-roles/

8. **patterns/error-recovery/README.md** ✅
   - Lines 97-101: Links to core-rules/design-patterns/ERROR_RECOVERY.md

### Files Missing Cross-References

**None found** - All files have appropriate cross-references!

---

## Summary Matrix

| Area | Core Rules Location | Patterns Location | Overlap | Status | Action Required |
|------|-------------------|------------------|---------|---------|-----------------|
| Git Workflows | workflows/GIT_WORKFLOW.md (990 lines) | git-workflows/ (placeholder) | None | ✅ Good | Monitor when populated |
| Testing | testing/ (6 files, 580+ lines) | testing-patterns/ (placeholder) | None | ✅ Good | Monitor when populated |
| Agent Roles/Modes | agent-roles/ (7 files, 478+ lines) | mode-capabilities/ (placeholder) | None | ✅ Good | Monitor when populated |
| Error Recovery | design-patterns/ERROR_RECOVERY.md (1,287 lines) | error-recovery/ (5 files) | Minimal | ✅ Good | Validate separation |
| Memory/Context | ❌ Not found | context-management/ (placeholder) | None | ⚠️ Issue | Fix cross-ref |

---

## Proposed Resolution Strategy

### Strategy 1: Git Workflows
**Decision:** ✅ **Already harmonized** - No action required
- Core rules contain complete standards
- Patterns directory is placeholder for future examples
- Cross-references in place

### Strategy 2: Testing
**Decision:** ✅ **Already harmonized** - No action required
- Core rules contain comprehensive standards
- Patterns directory will contain AI-specific strategies
- Cross-references in place

### Strategy 3: Agent Roles vs Mode Capabilities
**Decision:** ✅ **Already harmonized** - No action required
- Clear conceptual separation (generic vs tool-specific)
- Cross-references in place
- Relationship explained in both documents

### Strategy 4: Error Recovery
**Decision:** ✅ **Validate separation** - Minor review
- Core rules focus on design pattern implementations
- Patterns focus on troubleshooting and quick recovery
- Cross-references comprehensive
- **Action:** Verify no duplicate examples

### Strategy 5: Memory/Context Management
**Decision:** ⚠️ **Fix cross-reference**
- No memory-patterns.md exists in core-rules
- Update patterns/context-management/README.md
- Reference CACHING_PATTERNS.md or other relevant patterns instead
- **Action:** Update cross-references

---

## Recommendations

### Immediate Actions (Tasks 2-11)

1. **Task 2 (Git Workflows):** ✅ Validate existing cross-references - COMPLETE
2. **Task 3 (Testing):** ✅ Validate existing cross-references - COMPLETE
3. **Task 4 (Agent Roles/Modes):** ✅ Validate existing cross-references - COMPLETE
4. **Task 5 (Error Recovery):** ✅ Validate cross-references, check for duplicate examples
5. **Task 6 (Memory/Context):** ⚠️ **MODIFIED** - Update cross-refs to point to existing files (not memory-patterns.md)
6. **Task 7:** Create cross-reference map
7. **Task 8:** Validate all internal links
8. **Task 9:** Update INDEX files with cross-references
9. **Task 10:** Create harmonization summary
10. **Task 11:** Commit all changes

### Future Monitoring

When patterns directories are populated from agentic-dev-patterns repository:
- Ensure no duplication of content from core-rules
- Verify patterns focus on "how" while core-rules focus on "what"
- Maintain cross-references
- Review for any new overlaps

---

## Success Metrics

- ✅ All overlapping content identified
- ✅ Clear strategy for each overlap
- ✅ Most content already harmonized
- ✅ Cross-references already in place
- ⚠️ 1 issue found (memory-patterns.md doesn't exist)
- 🎯 Ready to proceed with validation and link checking

---

**Analysis Complete**
**Next Step:** Proceed to Task 2 - Validate existing cross-references
