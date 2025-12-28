# Worker: harmonize-content

## Mission
Resolve overlapping content between core-rules and patterns, create comprehensive cross-references, and ensure unified navigation throughout the repository.

## Deliverables
- Git workflow content harmonized between core-rules and patterns
- Testing content harmonized between core-rules and patterns
- Cross-references added to all related documents
- Duplicate content removed or consolidated
- Navigation links validated

## Context
After migrating content from both source repositories, there is overlap in several areas:
- Git workflows (in both core-rules/workflows and patterns/git-workflows)
- Testing (in both core-rules/testing and patterns/testing-patterns)
- Agent roles/modes (in core-rules/agent-roles and patterns/mode-capabilities)

Your job is to harmonize this content, ensuring each piece has a clear purpose and creating cross-references so users can navigate between related content.

## Dependencies
- migrate-rules (must complete to have core-rules content)
- migrate-patterns (must complete to have patterns content)

## References
- Implementation Plan: `/home/jhenry/Source/agent-knowledge/AGENT_KNOWLEDGE_MERGE_PLAN.md` (lines 617-650)
- Deduplication Strategy: Plan lines 461-473
- Cross-Reference Examples: Plan lines 441-458

## Task Breakdown

### Task 1: Analyze Overlapping Content

**Identify overlap in:**
1. Git Workflows
   - core-rules/workflows/git-workflows.md
   - patterns/git-workflows/

2. Testing
   - core-rules/testing/
   - patterns/testing-patterns/

3. Agent Roles vs Mode Capabilities
   - core-rules/agent-roles/
   - patterns/mode-capabilities/

**Create analysis document:**
`/home/jhenry/Source/agent-knowledge/meta/content-overlap-analysis.md`

Document:
- What content overlaps
- What is unique to each location
- Proposed resolution strategy for each

**Acceptance Criteria:**
- All overlapping content identified
- Analysis document created
- Clear strategy for each overlap

### Task 2: Harmonize Git Workflow Content

**Strategy:**
- **core-rules/workflows/git-workflows.md** = General workflow rules and standards
- **patterns/git-workflows/** = Specific patterns and examples

**Actions:**

1. Review core-rules/workflows/git-workflows.md
   - Keep general workflow guidance
   - Keep rules and standards
   - Add cross-reference to patterns/git-workflows/

2. Review patterns/git-workflows/README.md
   - Keep specific patterns and examples
   - Keep battle-tested strategies from The Symposium
   - Add cross-reference to core-rules/workflows/

3. Add cross-references to both:
   ```markdown
   ## Related Content

   For general git workflow rules and standards, see:
   - [Git Workflows (Core Rules)](../../core-rules/workflows/git-workflows.md)

   For specific git workflow patterns and examples, see:
   - [Git Workflow Patterns](../../patterns/git-workflows/README.md)
   - [Branch Strategies](../../patterns/git-workflows/branch-strategies.md)
   - [Commit Patterns](../../patterns/git-workflows/commit-patterns.md)
   ```

**Acceptance Criteria:**
- Clear separation: rules in core-rules, patterns in patterns
- No duplicate content
- Comprehensive cross-references in both locations
- Both documents updated

### Task 3: Harmonize Testing Content

**Strategy:**
- **core-rules/testing/** = Testing standards, organization, and requirements
- **patterns/testing-patterns/** = Specific testing patterns and strategies

**Actions:**

1. Review core-rules/testing/
   - Keep testing philosophy and standards
   - Keep pytest standards and requirements
   - Keep coverage requirements
   - Add cross-reference to patterns/testing-patterns/

2. Review patterns/testing-patterns/README.md
   - Keep specific testing patterns
   - Keep TDD strategies
   - Keep automation patterns
   - Add cross-reference to core-rules/testing/

3. Add cross-references to both:
   ```markdown
   ## Related Content

   For testing standards and requirements, see:
   - [Testing (Core Rules)](../../core-rules/testing/README.md)
   - [Pytest Standards](../../core-rules/testing/pytest-standards.md)
   - [Coverage Requirements](../../core-rules/testing/coverage-requirements.md)

   For specific testing patterns, see:
   - [Testing Patterns](../../patterns/testing-patterns/README.md)
   ```

**Acceptance Criteria:**
- Clear separation: standards in core-rules, patterns in patterns
- No duplicate content
- Comprehensive cross-references in both locations
- Both locations updated

### Task 4: Harmonize Agent Roles and Mode Capabilities

**Strategy:**
- **core-rules/agent-roles/** = Role definitions, responsibilities, and coordination
- **patterns/mode-capabilities/** = Mode-specific patterns and transition strategies

**Actions:**

1. Review core-rules/agent-roles/
   - Keep role definitions
   - Keep responsibilities and expectations
   - Keep coordination patterns
   - Add cross-reference to patterns/mode-capabilities/

2. Review patterns/mode-capabilities/
   - Keep mode-specific patterns
   - Keep transition strategies
   - Keep optimization techniques
   - Add cross-reference to core-rules/agent-roles/

3. Add cross-references to both:
   ```markdown
   ## Related Content

   For role definitions and responsibilities, see:
   - [Agent Roles (Core Rules)](../../core-rules/agent-roles/README.md)
   - [Architect Role](../../core-rules/agent-roles/architect-role.md)
   - [Code Role](../../core-rules/agent-roles/code-role.md)

   For mode-specific patterns and transitions, see:
   - [Mode Capabilities](../../patterns/mode-capabilities/README.md)
   - [Mode Transitions](../../patterns/mode-capabilities/mode-transitions.md)
   ```

**Acceptance Criteria:**
- Clear separation: definitions in core-rules, patterns in patterns
- No duplicate content
- Comprehensive cross-references
- Both locations updated

### Task 5: Add Cross-References to Error Recovery

Error recovery appears in multiple places. Add cross-references:

1. In core-rules/workflows/recovery-workflow.md:
   ```markdown
   ## Related Patterns

   For detailed error recovery patterns, see:
   - [Error Recovery Patterns](../../patterns/error-recovery/README.md)
   - [Detection Patterns](../../patterns/error-recovery/detection-patterns.md)
   - [Recovery Strategies](../../patterns/error-recovery/recovery-strategies.md)
   ```

2. In patterns/error-recovery/README.md:
   ```markdown
   ## Related Workflows

   For error recovery workflow guidance, see:
   - [Recovery Workflow](../../core-rules/workflows/recovery-workflow.md)
   ```

**Acceptance Criteria:**
- Cross-references added to both locations
- Links validated

### Task 6: Add Cross-References to Design Patterns and Context Management

1. In core-rules/design-patterns/memory-patterns.md:
   ```markdown
   ## Related Patterns

   For context management strategies, see:
   - [Context Management](../../patterns/context-management/README.md)
   - [Memory Tiers](../../patterns/context-management/memory-tiers.md)
   ```

2. In patterns/context-management/README.md:
   ```markdown
   ## Related Design Patterns

   For memory design patterns, see:
   - [Memory Patterns](../../core-rules/design-patterns/memory-patterns.md)
   ```

**Acceptance Criteria:**
- Cross-references added to both locations
- Links validated

### Task 7: Create Cross-Reference Map

Create `/home/jhenry/Source/agent-knowledge/meta/cross-reference-map.md`:

```markdown
# Cross-Reference Map

This document maps relationships between core-rules and patterns content.

## Git Workflows
- **Core Rules:** [workflows/git-workflows.md](../core-rules/workflows/git-workflows.md) - General rules and standards
- **Patterns:** [git-workflows/](../patterns/git-workflows/) - Specific patterns and examples
- **Relationship:** Core rules define standards, patterns show implementation

## Testing
- **Core Rules:** [testing/](../core-rules/testing/) - Standards, organization, requirements
- **Patterns:** [testing-patterns/](../patterns/testing-patterns/) - TDD, automation strategies
- **Relationship:** Core rules define requirements, patterns show strategies

## Agent Roles / Mode Capabilities
- **Core Rules:** [agent-roles/](../core-rules/agent-roles/) - Role definitions and coordination
- **Patterns:** [mode-capabilities/](../patterns/mode-capabilities/) - Mode-specific patterns and transitions
- **Relationship:** Core rules define roles, patterns show mode optimization

## Error Recovery
- **Core Rules:** [workflows/recovery-workflow.md](../core-rules/workflows/recovery-workflow.md) - Recovery workflow
- **Patterns:** [error-recovery/](../patterns/error-recovery/) - Detailed recovery patterns
- **Relationship:** Core rules define workflow, patterns show specific strategies

## Memory Management
- **Core Rules:** [design-patterns/memory-patterns.md](../core-rules/design-patterns/memory-patterns.md) - Memory design patterns
- **Patterns:** [context-management/](../patterns/context-management/) - Context and attention strategies
- **Relationship:** Core rules define patterns, patterns show context-specific strategies

## Tool Usage
- **Core Rules:** Implicit in role definitions
- **Patterns:** [tool-use/](../patterns/tool-use/) - Tool optimization patterns
- **Relationship:** Patterns extend role capabilities with specific tool strategies

## General Principle

**Core Rules** = What you must do (standards, requirements, definitions)
**Patterns** = How to do it well (proven strategies, examples, optimizations)
```

**Acceptance Criteria:**
- Cross-reference map created
- All major overlaps documented
- Relationship principles clear

### Task 8: Validate All Internal Links

Create a script or use grep to find all internal links and validate them:

```bash
cd /home/jhenry/Source/agent-knowledge

# Find all markdown links
grep -r "\](\.\./" --include="*.md" > /tmp/links.txt

# TODO: Validate each link exists
# Check for:
# - Broken relative paths
# - Missing files
# - Incorrect directory references
```

Create validation report: `/home/jhenry/Source/agent-knowledge/meta/link-validation-report.md`

**Acceptance Criteria:**
- All internal links found
- All links validated
- Broken links fixed or removed
- Validation report created with zero broken links

### Task 9: Update INDEX Files

Ensure INDEX.md files in core-rules/ and patterns/ have comprehensive cross-references:

1. In `core-rules/INDEX.md`:
   - Add section "Related Patterns" at bottom
   - Link to relevant patterns for each core rule category

2. In `patterns/INDEX.md`:
   - Add section "Related Core Rules" at bottom
   - Link to relevant core rules for each pattern category

**Acceptance Criteria:**
- Both INDEX.md files updated
- Cross-references comprehensive
- Navigation improved

### Task 10: Create Harmonization Summary

Create `/home/jhenry/Source/agent-knowledge/meta/harmonization-summary.md`:

```markdown
# Content Harmonization Summary

**Date:** [Current Date]
**Purpose:** Resolve overlapping content and create cross-references

## Overlaps Resolved

### Git Workflows
- **Decision:** Core rules for standards, patterns for examples
- **Changes:**
  - Reviewed and deduped content
  - Added cross-references in both locations
- **Result:** Clear separation, no duplication

### Testing
- **Decision:** Core rules for requirements, patterns for strategies
- **Changes:**
  - Reviewed and deduped content
  - Added cross-references in both locations
- **Result:** Clear separation, no duplication

### Agent Roles / Mode Capabilities
- **Decision:** Core rules for definitions, patterns for optimization
- **Changes:**
  - Reviewed and deduped content
  - Added cross-references in both locations
- **Result:** Clear separation, no duplication

## Cross-References Added

- Git Workflows: 2 locations
- Testing: 2 locations
- Agent Roles/Modes: 2 locations
- Error Recovery: 2 locations
- Memory/Context: 2 locations

**Total:** 10+ cross-reference sets

## Link Validation

- Links checked: [count]
- Broken links found: 0
- Links fixed: [count]

## Navigation Improvements

- INDEX.md files updated with cross-references
- Cross-reference map created
- Clear navigation between core-rules and patterns

## Principle Established

**Core Rules** = Standards, requirements, definitions (the "what")
**Patterns** = Strategies, examples, optimizations (the "how")
```

**Acceptance Criteria:**
- Harmonization summary created
- All resolutions documented
- Link validation results included
- Saved in meta/ directory

### Task 11: Commit Harmonization
```bash
git add .
git commit -m "[harmonize-content] Harmonize overlapping content and add cross-references

- Resolved git workflow overlap (core-rules vs patterns)
- Resolved testing overlap (core-rules vs patterns)
- Resolved agent roles/mode capabilities overlap
- Added comprehensive cross-references throughout
- Validated all internal links (zero broken links)
- Created cross-reference map and harmonization summary

Principle: Core rules = standards/requirements, Patterns = strategies/examples"
```

**Acceptance Criteria:**
- All changes committed
- Commit message describes harmonization
- No broken links in repository

## Success Criteria
- [ ] All overlapping content analyzed and resolved
- [ ] Git workflows harmonized (core-rules + patterns)
- [ ] Testing content harmonized (core-rules + patterns)
- [ ] Agent roles/modes harmonized (core-rules + patterns)
- [ ] Cross-references added to all related content
- [ ] All internal links validated (zero broken)
- [ ] Cross-reference map created
- [ ] Harmonization summary created
- [ ] Changes committed to git
- [ ] Clear navigation between core-rules and patterns

## Notes
- Dependencies: Both migrate-rules and migrate-patterns must complete first
- This is critical for usability - users must be able to navigate related content
- Use absolute paths from /home/jhenry/Source/agent-knowledge
- Principle: core-rules = "what", patterns = "how"
- Zero broken links is mandatory
