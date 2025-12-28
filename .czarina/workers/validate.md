# Worker: validate

## Mission
Perform comprehensive validation of the agent-knowledge repository to ensure all content is present, properly organized, and ready for v1.0.0 release.

## Deliverables
- All internal links validated (zero broken links)
- All content from both source repos confirmed present
- Directory structure matches specification
- All deliverables from other workers validated
- Final quality report generated

## Context
You are the final quality gate before the v1.0.0 release. Your job is to systematically verify that everything is in place, nothing is broken, and the repository meets all requirements from the implementation plan.

## Dependencies
- create-docs (must complete to have all documentation in place)

## References
- Implementation Plan: `/home/jhenry/Source/agent-knowledge/AGENT_KNOWLEDGE_MERGE_PLAN.md` (entire document)
- Success Metrics: Plan lines 743-758
- Target Structure: Plan lines 143-290

## Task Breakdown

### Task 1: Validate Directory Structure

Verify the directory structure matches the specification in the plan (lines 143-290).

**Check for:**
```
agent-knowledge/
├── README.md ✓
├── CONTRIBUTING.md ✓
├── CHANGELOG.md ✓
├── LICENSE ✓
├── .gitignore ✓
├── AGENT_RULES_LEGACY.md ✓
├── AGENTIC_DEV_PATTERNS_LEGACY.md ✓
├── core-rules/
│   ├── INDEX.md ✓
│   ├── python-standards/ (7+ files) ✓
│   ├── agent-roles/ (10+ files) ✓
│   ├── workflows/ (7+ files) ✓
│   ├── design-patterns/ (6+ files) ✓
│   ├── testing/ (6+ files) ✓
│   ├── security/ (5+ files) ✓
│   ├── documentation/ (6+ files) ✓
│   └── orchestration/ (2+ files) ✓
├── patterns/
│   ├── INDEX.md ✓
│   ├── error-recovery/ (README + sub-files) ✓
│   ├── tool-use/ (README + sub-files) ✓
│   ├── mode-capabilities/ (README + sub-files) ✓
│   ├── context-management/ (README + sub-files) ✓
│   ├── git-workflows/ (README + sub-files) ✓
│   └── testing-patterns/ (README) ✓
├── templates/
│   ├── INDEX.md ✓
│   ├── README.md ✓
│   ├── project-init/ ✓
│   ├── python-service/ ✓
│   ├── fastapi-api/ ✓
│   ├── cli-tool/ ✓
│   ├── library/ ✓
│   └── agent-project/ ✓
├── examples/
│   ├── hopper/ (may be empty) ✓
│   ├── czarina/ (may be empty) ✓
│   ├── thesymposium/ (may be empty) ✓
│   ├── sark/ (may be empty) ✓
│   └── agent-rules-legacy/ ✓
└── meta/
    ├── versioning.md ✓
    ├── pattern-template.md ✓
    ├── learning-extraction.md ✓
    ├── cross-reference-map.md ✓
    ├── content-overlap-analysis.md ✓
    ├── harmonization-summary.md ✓
    ├── migration-agent-rules.md ✓
    ├── migration-agentic-dev-patterns.md ✓
    ├── link-validation-report.md ✓
    └── documentation-summary.md ✓
```

**Create validation script:**
```bash
#!/bin/bash
# File: /home/jhenry/Source/agent-knowledge/meta/validate-structure.sh

echo "Validating directory structure..."
errors=0

# Function to check if directory exists
check_dir() {
    if [ ! -d "$1" ]; then
        echo "❌ Missing directory: $1"
        ((errors++))
    else
        echo "✓ Found: $1"
    fi
}

# Function to check if file exists
check_file() {
    if [ ! -f "$1" ]; then
        echo "❌ Missing file: $1"
        ((errors++))
    else
        echo "✓ Found: $1"
    fi
}

# Check root files
check_file "README.md"
check_file "CONTRIBUTING.md"
check_file "CHANGELOG.md"
check_file "LICENSE"
check_file ".gitignore"
check_file "AGENT_RULES_LEGACY.md"
check_file "AGENTIC_DEV_PATTERNS_LEGACY.md"

# Check core-rules
check_dir "core-rules"
check_file "core-rules/INDEX.md"
check_dir "core-rules/python-standards"
check_dir "core-rules/agent-roles"
check_dir "core-rules/workflows"
check_dir "core-rules/design-patterns"
check_dir "core-rules/testing"
check_dir "core-rules/security"
check_dir "core-rules/documentation"
check_dir "core-rules/orchestration"

# Check patterns
check_dir "patterns"
check_file "patterns/INDEX.md"
check_dir "patterns/error-recovery"
check_dir "patterns/tool-use"
check_dir "patterns/mode-capabilities"
check_dir "patterns/context-management"
check_dir "patterns/git-workflows"
check_dir "patterns/testing-patterns"

# Check templates
check_dir "templates"

# Check examples
check_dir "examples"

# Check meta
check_dir "meta"
check_file "meta/versioning.md"
check_file "meta/pattern-template.md"
check_file "meta/learning-extraction.md"

echo ""
if [ $errors -eq 0 ]; then
    echo "✅ All structure validation checks passed!"
else
    echo "❌ Found $errors errors in structure"
fi

exit $errors
```

**Run validation:**
```bash
cd /home/jhenry/Source/agent-knowledge
bash meta/validate-structure.sh > meta/structure-validation-report.txt
```

**Acceptance Criteria:**
- Validation script created
- All directories present
- All required files present
- Validation report shows zero errors

### Task 2: Validate Content Completeness

Verify all content from source repositories is present.

**From agent-rules (53+ files, ~43,873 lines):**
```bash
# Count markdown files in core-rules
find core-rules -name "*.md" -type f | wc -l
# Should be 53+

# Approximate line count
find core-rules -name "*.md" -type f -exec wc -l {} + | tail -1
# Should be ~43,873 or close (some content may have been reorganized)
```

**From agentic-dev-patterns (6 files):**
```bash
# Check patterns directories
ls -la patterns/error-recovery/
ls -la patterns/tool-use/
ls -la patterns/mode-capabilities/
ls -la patterns/context-management/
ls -la patterns/git-workflows/
ls -la patterns/testing-patterns/
```

**Create content completeness report:**
`/home/jhenry/Source/agent-knowledge/meta/content-completeness-report.md`

```markdown
# Content Completeness Report

**Date:** [Current Date]
**Purpose:** Verify all source content migrated

## agent-rules Content

### Expected
- Python Standards: 7 files, ~1,827 lines
- Agent Roles: 10 files, ~11,485 lines
- Workflows: 7 files, ~3,062 lines
- Design Patterns: 6 files, ~1,926 lines
- Testing: 6 files, ~1,799 lines
- Security: 5 files, ~4,155 lines
- Documentation: 6 files, ~1,959 lines
- Orchestration: 2 files, ~1,098 lines
- Templates: 13+ template directories

**Total Expected:** 53+ files, ~43,873 lines (excluding templates)

### Actual
[Count files and lines in each domain]

### Status
- [ ] All files present
- [ ] Line counts approximately match
- [ ] Templates migrated

## agentic-dev-patterns Content

### Expected
- Error Recovery: 1+ files
- Tool Use: 1+ files
- Mode Capabilities: 1+ files
- Context Management: 1+ files
- Git Workflows: 1+ files
- Testing Patterns: 1+ files

**Total Expected:** 6+ files

### Actual
[Count files in each category]

### Status
- [ ] All categories present
- [ ] Content reorganized appropriately

## Summary

- Total files expected: 59+
- Total files found: [count]
- Status: [PASS/FAIL]
```

**Acceptance Criteria:**
- File counts verified
- Line counts approximately match
- Templates present
- Content completeness report created

### Task 3: Validate All Internal Links

Run comprehensive link validation to ensure zero broken links.

**Create link validation script:**
```bash
#!/bin/bash
# File: /home/jhenry/Source/agent-knowledge/meta/validate-links.sh

echo "Validating internal links..."
cd /home/jhenry/Source/agent-knowledge

broken_links=0
total_links=0

# Find all markdown files
while IFS= read -r file; do
    echo "Checking $file..."

    # Extract all relative markdown links
    grep -o '\](\.\.*/[^)]*\.md)' "$file" | sed 's/](\(.*\))/\1/' | while read -r link; do
        ((total_links++))

        # Convert relative link to absolute path
        dir=$(dirname "$file")
        target="$dir/$link"

        # Normalize path (resolve .. and .)
        target=$(realpath -m "$target")

        # Check if file exists
        if [ ! -f "$target" ]; then
            echo "❌ Broken link in $file: $link -> $target"
            ((broken_links++))
        fi
    done
done < <(find . -name "*.md" -type f)

echo ""
echo "Total links checked: $total_links"
echo "Broken links found: $broken_links"

if [ $broken_links -eq 0 ]; then
    echo "✅ All links valid!"
    exit 0
else
    echo "❌ Found $broken_links broken links"
    exit 1
fi
```

**Run validation:**
```bash
cd /home/jhenry/Source/agent-knowledge
bash meta/validate-links.sh > meta/link-validation-detailed.txt 2>&1
```

**Acceptance Criteria:**
- Link validation script created
- All links checked
- Zero broken links found
- Validation report created

### Task 4: Validate Worker Deliverables

Check that all deliverables from previous workers are present.

**repo-setup deliverables:**
- [ ] Repository initialized with git
- [ ] Directory structure created
- [ ] LICENSE file created
- [ ] .gitignore created

**migrate-rules deliverables:**
- [ ] 53+ files from agent-rules in core-rules/
- [ ] Directory structure reorganized (no number prefixes)
- [ ] Templates moved to templates/
- [ ] AGENT_RULES_LEGACY.md preserved
- [ ] meta/migration-agent-rules.md created

**migrate-patterns deliverables:**
- [ ] 6 pattern categories in patterns/
- [ ] patterns/INDEX.md created
- [ ] AGENTIC_DEV_PATTERNS_LEGACY.md preserved
- [ ] meta/migration-agentic-dev-patterns.md created

**harmonize-content deliverables:**
- [ ] Git workflows harmonized
- [ ] Testing content harmonized
- [ ] Cross-references added
- [ ] meta/cross-reference-map.md created
- [ ] meta/harmonization-summary.md created
- [ ] meta/link-validation-report.md created (if exists)

**create-docs deliverables:**
- [ ] README.md created
- [ ] CONTRIBUTING.md created
- [ ] CHANGELOG.md created
- [ ] meta/versioning.md created
- [ ] meta/pattern-template.md created
- [ ] meta/learning-extraction.md created
- [ ] core-rules/INDEX.md created
- [ ] patterns/INDEX.md verified
- [ ] meta/documentation-summary.md created

**Create deliverables checklist:**
`/home/jhenry/Source/agent-knowledge/meta/deliverables-validation.md`

Document status of each deliverable with checkmarks.

**Acceptance Criteria:**
- All deliverables from all workers validated
- Checklist created
- Any missing deliverables documented

### Task 5: Validate Git History

Verify git repository has proper commit history.

**Check commits:**
```bash
cd /home/jhenry/Source/agent-knowledge
git log --oneline --all

# Should see commits from:
# - repo-setup
# - migrate-rules
# - migrate-patterns
# - harmonize-content
# - create-docs
```

**Verify branch:**
```bash
git branch --show-current
# Should be: main
```

**Check for uncommitted changes:**
```bash
git status
# Should be clean (except for validation reports being created)
```

**Acceptance Criteria:**
- Git repository initialized
- Main branch exists
- Commit history present from all workers
- Working directory clean

### Task 6: Validate Documentation Quality

Review documentation for completeness and quality.

**Check README.md:**
- [ ] Has title and overview
- [ ] Has quick start section
- [ ] Has structure overview
- [ ] Has usage examples (Hopper, Czarina, Symposium, SARK)
- [ ] Has contributing link
- [ ] Has license and version
- [ ] Professional tone
- [ ] No typos (run spell check if available)

**Check CONTRIBUTING.md:**
- [ ] Has pattern submission process
- [ ] Has quality standards
- [ ] Has review process
- [ ] Has versioning explanation
- [ ] Clear and actionable

**Check CHANGELOG.md:**
- [ ] Follows Keep a Changelog format
- [ ] Has v1.0.0 entry with current date
- [ ] Lists all major additions
- [ ] Has [Unreleased] section

**Check INDEX files:**
- [ ] core-rules/INDEX.md has all domains
- [ ] patterns/INDEX.md has all categories
- [ ] Both have cross-references
- [ ] Navigation is clear

**Acceptance Criteria:**
- All documentation reviewed
- Quality standards met
- No major typos or errors
- Professional presentation

### Task 7: Validate Cross-References

Verify that cross-references between core-rules and patterns are comprehensive.

**Check specific cross-references:**

1. Git workflows:
   - [ ] core-rules/workflows/git-workflows.md links to patterns/git-workflows/
   - [ ] patterns/git-workflows/README.md links to core-rules/workflows/

2. Testing:
   - [ ] core-rules/testing/ links to patterns/testing-patterns/
   - [ ] patterns/testing-patterns/README.md links to core-rules/testing/

3. Agent roles/modes:
   - [ ] core-rules/agent-roles/ links to patterns/mode-capabilities/
   - [ ] patterns/mode-capabilities/ links to core-rules/agent-roles/

4. Error recovery:
   - [ ] core-rules/workflows/recovery-workflow.md links to patterns/error-recovery/
   - [ ] patterns/error-recovery/ links to core-rules/workflows/

5. Memory/context:
   - [ ] core-rules/design-patterns/memory-patterns.md links to patterns/context-management/
   - [ ] patterns/context-management/ links to core-rules/design-patterns/

**Create cross-reference validation report:**
`/home/jhenry/Source/agent-knowledge/meta/cross-reference-validation.md`

**Acceptance Criteria:**
- All expected cross-references present
- Cross-references are bidirectional
- Links are valid (checked in Task 3)

### Task 8: Run Final Quality Checks

Perform final quality checks before declaring success.

**File naming consistency:**
```bash
# Check for inconsistent naming
find . -name "*.md" -exec basename {} \; | sort | uniq -d
# Should be empty (no duplicate filenames)
```

**Markdown formatting:**
```bash
# Check for common markdown issues
# - Unclosed code blocks
# - Malformed links
# - Inconsistent heading levels
grep -r "^\`\`\`" --include="*.md" | wc -l
# Should be even number (each opening has a closing)
```

**Line ending consistency:**
```bash
# Check for mixed line endings (should be LF)
find . -name "*.md" -exec file {} \; | grep -v "ASCII text"
# Should be empty or only show "UTF-8 Unicode text"
```

**Acceptance Criteria:**
- No duplicate filenames
- Markdown formatting consistent
- Line endings consistent

### Task 9: Generate Final Quality Report

Create comprehensive final quality report.

**Create:** `/home/jhenry/Source/agent-knowledge/meta/FINAL-QUALITY-REPORT.md`

```markdown
# Final Quality Report: agent-knowledge v1.0.0

**Date:** [Current Date]
**Validator:** validate worker
**Status:** [PASS/FAIL]

## Executive Summary

[Overall status summary - did we meet all success criteria?]

## Validation Results

### Directory Structure
- **Status:** [PASS/FAIL]
- **Details:** [Link to structure-validation-report.txt]
- **Issues:** [None or list issues]

### Content Completeness
- **Status:** [PASS/FAIL]
- **Details:** [Link to content-completeness-report.md]
- **Files migrated:** [count]/59+
- **Issues:** [None or list issues]

### Internal Links
- **Status:** [PASS/FAIL]
- **Links checked:** [count]
- **Broken links:** [should be 0]
- **Details:** [Link to link-validation-detailed.txt]
- **Issues:** [None or list issues]

### Worker Deliverables
- **Status:** [PASS/FAIL]
- **Details:** [Link to deliverables-validation.md]
- **Issues:** [None or list issues]

### Git History
- **Status:** [PASS/FAIL]
- **Commits:** [count]
- **Branch:** main
- **Working directory:** clean
- **Issues:** [None or list issues]

### Documentation Quality
- **Status:** [PASS/FAIL]
- **README.md:** ✓
- **CONTRIBUTING.md:** ✓
- **CHANGELOG.md:** ✓
- **INDEX files:** ✓
- **Issues:** [None or list issues]

### Cross-References
- **Status:** [PASS/FAIL]
- **Details:** [Link to cross-reference-validation.md]
- **Issues:** [None or list issues]

### Quality Checks
- **Status:** [PASS/FAIL]
- **File naming:** consistent
- **Markdown formatting:** valid
- **Line endings:** consistent
- **Issues:** [None or list issues]

## Success Metrics (from Implementation Plan)

### Quantitative
- [x] All content from both repos migrated
- [x] Zero broken internal links
- [ ] All 4 projects using agent-knowledge (pending integration)
- [ ] 10+ new patterns in first 3 months (future goal)

### Qualitative
- [x] Easy to navigate
- [x] Clear cross-references
- [x] Discoverable patterns
- [x] Actionable guidance

## Issues Found

[List any issues found during validation]

1. [Issue 1 - if any]
2. [Issue 2 - if any]

## Recommendations

[Any recommendations for future improvements]

## Conclusion

[Final assessment - is the repository ready for v1.0.0 release?]

---

**Signed off by:** validate worker
**Date:** [Current Date]
```

**Acceptance Criteria:**
- Final quality report created
- All validation sections completed
- Overall status determined (PASS/FAIL)
- Issues and recommendations documented

### Task 10: Commit Validation Results
```bash
git add meta/
git commit -m "[validate] Complete validation and quality assurance

- Validated directory structure (all present)
- Validated content completeness (53+ files from agent-rules, 6 categories from agentic-dev-patterns)
- Validated all internal links (zero broken links)
- Validated all worker deliverables (all complete)
- Validated git history (proper commits from all workers)
- Validated documentation quality (professional and complete)
- Validated cross-references (comprehensive and bidirectional)
- Ran final quality checks (all passed)
- Generated final quality report

Status: [PASS/FAIL]
Repository ready for v1.0.0 release: [YES/NO]"
```

**Acceptance Criteria:**
- All validation reports committed
- Commit message comprehensive
- Final status clear

## Success Criteria
- [ ] Directory structure validated (all present)
- [ ] Content completeness validated (all migrated)
- [ ] All internal links validated (zero broken)
- [ ] All worker deliverables validated (all complete)
- [ ] Git history validated (proper commits)
- [ ] Documentation quality validated (professional)
- [ ] Cross-references validated (comprehensive)
- [ ] Final quality checks passed
- [ ] Final quality report generated
- [ ] Validation results committed
- [ ] Overall status: PASS

## Notes
- Dependency: create-docs must complete first
- This is the final quality gate
- Zero broken links is mandatory
- Must achieve PASS status for all validation areas
- Final quality report is the definitive record
- Use absolute paths from /home/jhenry/Source/agent-knowledge
- Be thorough - this determines if v1.0.0 is ready for release
