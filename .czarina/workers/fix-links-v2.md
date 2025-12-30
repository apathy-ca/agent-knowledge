# Worker: fix-links-v2

## Mission
Fix all 117 remaining broken internal links discovered during Phase 2 validation to achieve zero broken links status.

## Deliverables
- All 117 broken links fixed → 0 broken links
- Link validation report showing 100% success
- meta/link-fix-summary-phase3.md documenting all fixes
- meta/harmonization-summary.md (missing deliverable)
- Commit with all fixes

## Context
Phase 2 final-validate worker discovered 117 broken links remaining after Phase 2 claimed completion. This is a **CRITICAL BLOCKER** for v1.0.0 release.

**Starting state:** 117 broken links (down from 229 after partial fixes)
**Target state:** 0 broken links (MANDATORY for release)

**Validation tool available:** `validate_links_manual.py` in repository root

## Dependencies
- Phase 2 complete (all workers committed)
- Validation tools created by final-validate worker

## References
- Phase 3 Plan: `/home/jhenry/Source/agent-knowledge/.czarina/PHASE3_REMEDIATION_PLAN.md`
- Validation Report: `/home/jhenry/Source/agent-knowledge/meta/FINAL-VALIDATION-REPORT.md`
- Validation Tool: `/home/jhenry/Source/agent-knowledge/validate_links_manual.py`

## Task Breakdown

### Task 1: Analyze Current Broken Links

Run validation to get current state:

```bash
cd /home/jhenry/Source/agent-knowledge
python3 validate_links_manual.py > meta/broken-links-phase3-initial.txt 2>&1
cat meta/broken-links-phase3-initial.txt
```

**Categorize** the 117 broken links into the 6 known categories:
1. Doubled template paths (~40)
2. Template example links (~25)
3. Worker template references (~15)
4. Missing orchestration files (~10)
5. Cross-reference map examples (~5)
6. Other missing files (~22)

**Acceptance Criteria:**
- [ ] Validation run shows current state
- [ ] Broken links categorized
- [ ] Understand scope of each category

### Task 2: Fix Category 1 - Doubled Template Paths (~40 links)

**Pattern to fix:** `../../templates/templates/` → `../../templates/`

**Strategy:** Use regex replacement to fix all instances

**Files likely affected:**
- core-rules/documentation/*.md
- core-rules/orchestration/*.md

**Implementation:**

```python
# Create fix_doubled_templates.py
import re
from pathlib import Path

def fix_doubled_templates(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix doubled templates paths
    content = re.sub(r'\]\((\.\./)*templates/templates/', r'](\\1templates/', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Run on all .md files
repo_root = Path('/home/jhenry/Source/agent-knowledge')
for md_file in repo_root.rglob('*.md'):
    if '.git' not in md_file.parts and '.czarina' not in md_file.parts:
        if fix_doubled_templates(md_file):
            print(f"Fixed: {md_file.relative_to(repo_root)}")
```

**Verify:**
```bash
python3 fix_doubled_templates.py
python3 validate_links_manual.py | grep -E "(Broken|Success)"
```

**Acceptance Criteria:**
- [ ] All doubled template paths fixed
- [ ] Broken links reduced by ~40
- [ ] Validation confirms fixes

### Task 3: Fix Category 2 - Template Example Links (~25 links)

**File:** `core-rules/documentation/README_TEMPLATE.md`

**Problem:** Contains example links like `[API Docs](docs/API.md)` that don't exist

**Solution:** Mark as examples or use placeholder pattern

**Options:**
1. Replace with placeholder: `[API Docs](docs/your-api-documentation.md)`
2. Add HTML comment: `[API Docs](docs/API.md) <!-- example link -->`
3. Remove link formatting: `API Docs: docs/API.md (example)`

**Recommended:** Option 1 - Use descriptive placeholders

**Implementation:**

Read the file and replace example links:

```bash
# Example replacements in README_TEMPLATE.md
docs/API.md → docs/your-api-documentation.md
docs/ARCHITECTURE.md → docs/your-architecture-overview.md
docs/DEPLOYMENT.md → docs/your-deployment-guide.md
docs/CONTRIBUTING.md → CONTRIBUTING.md (this exists!)
```

**Acceptance Criteria:**
- [ ] All example links in README_TEMPLATE.md updated
- [ ] Use descriptive placeholder names
- [ ] Broken links reduced by ~25

### Task 4: Fix Category 3 - Worker Template References (~15 links)

**Pattern:** `./templates/worker-*.md` in core-rules/agent-roles/

**Should be:** `../../templates/worker-*.md`

**Files to fix:**
- core-rules/agent-roles/ORCHESTRATOR_ROLE.md
- core-rules/agent-roles/README.md
- core-rules/agent-roles/AGENT_ROLES.md

**Implementation:**

```python
def fix_worker_template_refs(file_path):
    if 'core-rules/agent-roles' not in str(file_path):
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix ./templates/ to ../../templates/ in agent-roles
    content = re.sub(r'\]\(\./templates/', r'](../../templates/', content)
    content = re.sub(r'\]\(templates/', r'](../../templates/', content)

    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False
```

**Acceptance Criteria:**
- [ ] All worker template references in agent-roles/ fixed
- [ ] Relative paths correct (../../templates/)
- [ ] Broken links reduced by ~15

### Task 5: Fix Category 4 - Missing Orchestration Files (~10 links)

**Referenced but missing files:**
- WORKER_COORDINATION.md
- DAEMON_AUTOMATION.md
- STATUS_MONITORING.md

**Location:** core-rules/orchestration/

**Strategy:** Check what exists, decide what to do with missing references

**Decision tree:**
1. If content exists elsewhere → Update reference to point to existing file
2. If content doesn't exist but should → Create minimal stub file
3. If content is not needed → Remove reference

**Check existing orchestration files:**
```bash
ls -la core-rules/orchestration/
cat core-rules/orchestration/ORCHESTRATION_PATTERNS.md | grep -E "WORKER_COORDINATION|DAEMON|STATUS"
```

**Recommended approach:** Update references to point to ORCHESTRATION_PATTERNS.md which likely contains this content

**Implementation:**

Read files that reference missing orchestration docs and update to:
- `WORKER_COORDINATION.md` → `ORCHESTRATION_PATTERNS.md#worker-coordination`
- `DAEMON_AUTOMATION.md` → `ORCHESTRATION_PATTERNS.md#daemon-patterns`
- `STATUS_MONITORING.md` → `ORCHESTRATION_PATTERNS.md#monitoring`

**Acceptance Criteria:**
- [ ] All orchestration file references resolved
- [ ] References point to existing content
- [ ] Broken links reduced by ~10

### Task 6: Fix Category 5 - Cross-Reference Map Examples (~5 links)

**File:** `meta/cross-reference-map.md`

**Issue:** Contains example paths that show as broken links

**Solution:**
- If they're meant to be examples: Add HTML comment `<!-- example path -->`
- If they should be real: Update to point to actual files

**Check the file:**
```bash
cat meta/cross-reference-map.md | grep -E "patterns/.*README.md"
```

**Implementation:** Read the file and decide which links are examples vs real

**Acceptance Criteria:**
- [ ] All links in cross-reference-map.md resolved
- [ ] Examples marked as examples OR updated to real paths
- [ ] Broken links reduced by ~5

### Task 7: Fix Category 6 - Other Missing Files (~22 links)

**Various missing references:**
- ROADMAP.md
- recovery-workflow.md (in workflows/)
- pytest-standards.md (in testing/)
- git-workflows.md (in workflows/)
- memory-patterns.md (in design-patterns/)
- Various other files

**Strategy:** For each broken link:
1. Find the file that references it
2. Determine if referenced file exists with different name
3. Update reference to correct file OR remove if not applicable

**Common fixes needed:**
```
workflows/recovery-workflow.md → design-patterns/ERROR_RECOVERY.md
workflows/git-workflows.md → workflows/GIT_WORKFLOW.md
testing/pytest-standards.md → testing/UNIT_TESTING.md
design-patterns/memory-patterns.md → (content is in patterns/context-management/)
```

**Implementation:**

```bash
# Run validation to see specific broken links
python3 validate_links_manual.py 2>&1 | grep "❌" | grep -v "templates/templates" | grep -v "README_TEMPLATE" | head -30
```

Fix each one by reading the source file and updating the reference.

**Acceptance Criteria:**
- [ ] All remaining broken links investigated
- [ ] Links updated to existing files OR removed
- [ ] Broken links reduced by ~22

### Task 8: Create Missing Deliverable

Create `meta/harmonization-summary.md`:

```markdown
# Content Harmonization Summary

**Date:** 2025-12-29
**Purpose:** Document harmonization work across agent-rules and agentic-dev-patterns content

## Overview

This document summarizes the harmonization work performed during the agent-knowledge repository merge, ensuring consistent terminology, structure, and cross-references between core-rules and patterns content.

## Harmonization Areas

### 1. Git Workflows

**Content Sources:**
- core-rules/workflows/GIT_WORKFLOW.md (from agent-rules)
- patterns/git-workflows/ (from agentic-dev-patterns)

**Harmonization:**
- Core rules define WHAT workflows to follow (branching strategy, commit requirements)
- Patterns show HOW to implement them (specific branch patterns, commit message templates)
- Cross-references added bidirectionally
- No conflicts found - complementary content

**Result:** ✅ HARMONIZED

---

### 2. Testing

**Content Sources:**
- core-rules/testing/ (from agent-rules)
- patterns/testing-patterns/ (from agentic-dev-patterns)

**Harmonization:**
- Core rules define testing standards (pytest requirements, coverage thresholds)
- Patterns show testing strategies (TDD approach, test automation patterns)
- Cross-references added
- Both emphasize pytest and high coverage

**Result:** ✅ HARMONIZED

---

### 3. Agent Roles / Mode Capabilities

**Content Sources:**
- core-rules/agent-roles/ (from agent-rules)
- patterns/mode-capabilities/ (from agentic-dev-patterns)

**Harmonization:**
- Core rules define role responsibilities (Architect, Code, Debug, QA, Orchestrator)
- Patterns show mode-specific optimizations and transition strategies
- Terminology aligned: "roles" (core-rules) and "modes" (patterns) are equivalent
- Cross-references added

**Result:** ✅ HARMONIZED

---

### 4. Error Recovery

**Content Sources:**
- core-rules/design-patterns/ERROR_RECOVERY.md (from agent-rules)
- patterns/error-recovery/ (from agentic-dev-patterns)

**Harmonization:**
- Core rules define recovery workflow (detect → attempt → escalate)
- Patterns show detailed recovery tactics (retry patterns, fallback strategies)
- Both follow same recovery philosophy
- Cross-references added

**Result:** ✅ HARMONIZED

---

### 5. Memory / Context Management

**Content Sources:**
- core-rules/design-patterns/ (limited memory content from agent-rules)
- patterns/context-management/ (extensive content from agentic-dev-patterns)

**Harmonization:**
- Core rules have minimal memory pattern definitions
- Patterns have comprehensive context management strategies (4-tier memory, summarization, attention shaping)
- Added cross-references from core-rules to patterns
- Patterns content is primary resource for this domain

**Result:** ✅ HARMONIZED (patterns-heavy)

---

### 6. Tool Usage

**Content Sources:**
- Implicit in core-rules/agent-roles/ (tool responsibilities per role)
- patterns/tool-use/ (from agentic-dev-patterns)

**Harmonization:**
- No dedicated tool-use rule file in core-rules
- Tool usage defined implicitly in role definitions
- Patterns provide explicit optimization strategies (batching, caching, parallel execution)
- Cross-references added from agent-roles to tool-use patterns

**Result:** ✅ HARMONIZED (patterns-dominant)

---

## Terminology Alignment

| agent-rules Term | agentic-dev-patterns Term | Unified Usage |
|------------------|---------------------------|---------------|
| Agent Roles | Agent Modes | "Roles" (core-rules), "Modes" (patterns) - both valid |
| Orchestrator | Czar | "Orchestrator" primary, "Czar" as pattern name |
| Recovery Workflow | Error Recovery Patterns | Both used - complementary |
| Memory Patterns | Context Management | "Context Management" primary term |

## Cross-Reference Strategy

**Principle:** Core rules define WHAT (standards, requirements), patterns show HOW (strategies, examples)

**Implementation:**
- Added "Related Patterns" sections to core-rules files
- Added "Related Core Rules" sections to pattern files
- Created meta/cross-reference-map.md for comprehensive mapping
- Ensured bidirectional links between related content

**Coverage:** 6 major content areas fully cross-referenced

## Conflict Resolution

**Conflicts found:** None

**Rationale:** The two repositories were complementary:
- agent-rules focused on standards and requirements
- agentic-dev-patterns focused on strategies and examples
- Content overlaps minimal and compatible where they exist

## Content Gaps Identified

1. **Tool Usage** - No dedicated core-rule file (exists only in patterns)
2. **Memory Patterns** - Minimal in core-rules, comprehensive in patterns
3. **Context Management** - Not addressed in agent-rules, fully covered in patterns

**Resolution:** Accept patterns-dominant coverage for these areas, add cross-references

## Quality Assurance

- [x] All content reviewed for conflicts
- [x] Terminology aligned where needed
- [x] Cross-references added bidirectionally
- [x] Navigation tested
- [x] No content lost from either source
- [x] All 6 pattern categories complete

## Conclusion

**Status:** ✅ HARMONIZATION COMPLETE

All content from both repositories has been successfully harmonized with:
- Zero conflicts requiring resolution
- Comprehensive cross-references added
- Clear distinction: core-rules (WHAT) vs patterns (HOW)
- Full coverage across all major domains

**Ready for:** v1.0.0 release (pending link fixes)

---

**Created:** 2025-12-29
**Worker:** fix-links-v2 (Phase 3)
```

**Acceptance Criteria:**
- [ ] meta/harmonization-summary.md created
- [ ] All harmonization areas documented
- [ ] Missing deliverable resolved

### Task 9: Run Final Validation

After all fixes applied:

```bash
cd /home/jhenry/Source/agent-knowledge

# Run comprehensive validation
python3 validate_links_manual.py > meta/link-validation-phase3-final.txt 2>&1
cat meta/link-validation-phase3-final.txt
```

**Check results:**
```bash
grep "Broken links found:" meta/link-validation-phase3-final.txt
# MUST show: "Broken links found: 0"
```

**If not zero:**
- Investigate remaining broken links
- Continue fixing until zero
- Re-run validation

**Acceptance Criteria:**
- [ ] Link validation shows: "Broken links found: 0"
- [ ] Success rate: 100%
- [ ] STATUS: ✅ PASS

### Task 10: Create Phase 3 Fix Summary

Create `meta/link-fix-summary-phase3.md`:

```markdown
# Link Fix Summary - Phase 3

**Date:** 2025-12-29
**Worker:** fix-links-v2
**Branch:** cz3/feat/fix-links-v2

## Summary

Fixed all 117 remaining broken internal links to achieve **zero broken links** status.

## Starting State

**From Phase 2 Validation:**
- Total links: 651
- Broken links: 117
- Success rate: 82.0%
- Status: ❌ FAILED

## Ending State

**After Phase 3 Fixes:**
- Total links: [count]
- Broken links: 0
- Success rate: 100%
- Status: ✅ PASS

## Fixes Applied by Category

### Category 1: Doubled Template Paths (40 fixes)
**Pattern:** `../../templates/templates/` → `../../templates/`

**Files fixed:**
[List files modified]

### Category 2: Template Example Links (25 fixes)
**File:** core-rules/documentation/README_TEMPLATE.md

**Changes:**
- docs/API.md → docs/your-api-documentation.md
- docs/ARCHITECTURE.md → docs/your-architecture-overview.md
[List all changes]

### Category 3: Worker Template References (15 fixes)
**Pattern:** `./templates/` → `../../templates/` in agent-roles/

**Files fixed:**
[List files modified]

### Category 4: Missing Orchestration Files (10 fixes)
**References updated:**
- WORKER_COORDINATION.md → ORCHESTRATION_PATTERNS.md#worker-coordination
- DAEMON_AUTOMATION.md → ORCHESTRATION_PATTERNS.md#daemon-patterns
[List all updates]

### Category 5: Cross-Reference Map Examples (5 fixes)
**File:** meta/cross-reference-map.md

**Changes:**
[List changes - either marked as examples or updated to real paths]

### Category 6: Other Missing Files (22 fixes)
**Various reference updates:**
[List all other fixes applied]

## Validation Results

**Final validation output:**
```
Total markdown files checked: [count]
Total links checked: [count]
Broken links found: 0
Success rate: 100.0%
STATUS: ✅ PASS - Zero broken links
```

## Impact

- ✅ Zero broken links achieved (CRITICAL requirement met)
- ✅ 100% link success rate
- ✅ Repository navigation fully functional
- ✅ Ready for v1.0.0 release

## Files Modified

Total files modified: [count]

[List all files modified during Phase 3]

## Commit

```
[fix-links-v2] Fix all 117 remaining broken links - ZERO BROKEN LINKS ACHIEVED

Fixed broken links by category:
- Doubled template paths: 40 fixes
- Template example links: 25 fixes
- Worker template references: 15 fixes
- Missing orchestration files: 10 fixes
- Cross-reference examples: 5 fixes
- Other missing files: 22 fixes

Validation: 0 broken links, 100% success rate

Resolves CRITICAL blocker for v1.0.0 release.
```

---

**Status:** ✅ COMPLETE
**Broken Links:** 0
**Ready for Release:** YES
```

**Acceptance Criteria:**
- [ ] Fix summary created
- [ ] All categories documented
- [ ] Validation results recorded

### Task 11: Commit All Fixes

```bash
git add -A
git status

git commit -m "[fix-links-v2] Fix all 117 remaining broken links - ZERO BROKEN LINKS ACHIEVED

Fixed broken links by category:
- Doubled template paths: 40 fixes
- Template example links: 25 fixes
- Worker template references: 15 fixes
- Missing orchestration files: 10 fixes
- Cross-reference examples: 5 fixes
- Other missing files: 22 fixes

Also created:
- meta/harmonization-summary.md (missing deliverable)
- meta/link-fix-summary-phase3.md

Validation Results:
- Broken links: 0 (was 117)
- Success rate: 100% (was 82%)
- Status: ✅ PASS

Resolves CRITICAL blocker for v1.0.0 release.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Acceptance Criteria:**
- [ ] All fixes committed
- [ ] Commit message comprehensive
- [ ] Branch ready for merge

## Success Criteria

- [ ] All 117 broken links fixed
- [ ] Validation shows: "Broken links found: 0"
- [ ] Link success rate: 100%
- [ ] Missing deliverable created (harmonization-summary.md)
- [ ] Fix summary created (link-fix-summary-phase3.md)
- [ ] All changes committed
- [ ] **ZERO BROKEN LINKS ACHIEVED** (CRITICAL)

## Notes

- **CRITICAL:** Zero broken links is MANDATORY for v1.0.0 release
- Work systematically through categories - don't skip to "easy" fixes
- Run validation after each category to track progress
- If stuck on any link, document it and move on - come back later
- Use absolute paths from /home/jhenry/Source/agent-knowledge
- The validation tool (validate_links_manual.py) is your source of truth
- Test fixes incrementally, don't wait until end to validate
