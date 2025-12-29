# Worker: fix-links

## Mission
Fix all 222 broken internal links to achieve "zero broken links" status required for v1.0.0 release.

## Deliverables
- core-rules/INDEX.md updated with correct paths
- All broken links fixed or removed
- Link validation report showing zero failures
- Commit with all link fixes

## Context
The validation report identified 222 broken links (45% failure rate) as a CRITICAL RELEASE BLOCKER. This violates the v1.0.0 success criteria of "zero broken internal links."

**Primary Issues:**
- core-rules/INDEX.md contains majority of broken links
- Path mismatches: `python/` vs `python-standards/`, `agents/` vs `agent-roles/`
- Structure mismatches: `core-rules/patterns/` vs `../patterns/`
- Missing template files
- Missing documentation files

## Dependencies
- None (can start immediately)

## References
- Validation Report: `/home/jhenry/Source/agent-knowledge/meta/FINAL-QUALITY-REPORT.md`
- Link Validation: `/home/jhenry/Source/agent-knowledge/meta/link-validation-detailed.txt`
- Link Validation Script: `/home/jhenry/Source/agent-knowledge/meta/validate-links.sh`

## Task Breakdown

### Task 1: Analyze Broken Links

Review the validation reports to understand the full scope:

```bash
# Review detailed link validation
cat /home/jhenry/Source/agent-knowledge/meta/link-validation-detailed.txt | grep "Broken link"

# Identify patterns in failures
grep "Broken link" /home/jhenry/Source/agent-knowledge/meta/link-validation-detailed.txt | cut -d: -f2 | sort | uniq -c | sort -rn
```

**Acceptance Criteria:**
- Full list of broken links reviewed
- Common patterns identified
- Strategy for fixes determined

### Task 2: Fix core-rules/INDEX.md Path References

The INDEX file contains most broken links. Update all path references:

**Changes needed:**

1. **Python directory:**
   - Find: `./python/`
   - Replace: `./python-standards/`

2. **Agent roles directory:**
   - Find: `./agents/`
   - Replace: `./agent-roles/`

3. **Patterns directory:**
   - Find: `./core-rules/patterns/`
   - Replace: `../patterns/`
   - Also find: `(../../core-rules/patterns/` → `(../../patterns/`

4. **Templates directory:**
   - Find: `./core-rules/templates/`
   - Replace: `../templates/`
   - Also find: `(../../core-rules/templates/` → `(../../templates/`

**Example fixes:**
```markdown
# Before
- [Python Standards](./python/README.md)
- [Agent Roles](./agents/README.md)
- [Error Recovery](../../core-rules/patterns/error-recovery/)
- [Templates](./core-rules/templates/)

# After
- [Python Standards](./python-standards/README.md)
- [Agent Roles](./agent-roles/README.md)
- [Error Recovery](../../patterns/error-recovery/)
- [Templates](../templates/)
```

**Acceptance Criteria:**
- All path references in core-rules/INDEX.md corrected
- Links point to actual directories
- Relative paths correct from INDEX.md location

### Task 3: Fix or Remove Template References

Some links reference template files that don't exist. Options:

1. **Create placeholder files** in templates/ directories
2. **Remove links** to non-existent templates
3. **Update links** to point to existing templates

**Recommended:** Create minimal placeholder README.md files in template directories that are empty.

**Example placeholder:**
```markdown
# [Template Name]

**Status:** Template structure in progress

This template directory is reserved for future template content.

## Planned Content

- Template files
- Configuration examples
- Usage documentation

**Contributing:** See [CONTRIBUTING.md](../../CONTRIBUTING.md) for how to add template content.
```

**Acceptance Criteria:**
- All template references either:
  - Point to existing files, OR
  - Have placeholder files created, OR
  - Are removed from documentation
- No broken template links remain

### Task 4: Fix Documentation References

Fix links to documentation files that may be misnamed or in wrong locations.

**Common issues:**
- Links to files in wrong subdirectories
- Links using old naming conventions
- Links to files that were consolidated

**Strategy:**
1. Identify target of each broken doc link
2. Find where file actually exists (if it does)
3. Update link or create missing file
4. Or remove link if content no longer relevant

**Acceptance Criteria:**
- All documentation links valid
- Cross-references work
- No broken doc links

### Task 5: Remove External References

Remove references to paths outside the repository (e.g., `.hopper/`, `.czarina/` in other projects).

**Example removals:**
```markdown
# Remove lines like:
- See `.hopper/config.yaml` for configuration
```

Replace with:
```markdown
# Replace with:
- See usage examples in [README.md](../../README.md#usage)
```

**Acceptance Criteria:**
- No links to external project directories
- No broken references to `.hopper/`, `.czarina/`, etc.
- Alternative references provided where needed

### Task 6: Validate All Links - First Pass

Run validation to see progress:

```bash
cd /home/jhenry/Source/agent-knowledge
bash meta/validate-links.sh > meta/link-validation-pass1.txt 2>&1

# Check results
grep "Broken links found:" meta/link-validation-pass1.txt
```

**Acceptance Criteria:**
- Significant reduction in broken links
- Remaining issues identified
- Progress documented

### Task 7: Fix Remaining Broken Links

Address any remaining broken links found in validation:

1. Review meta/link-validation-pass1.txt
2. Fix each remaining broken link
3. Verify fix works
4. Document resolution

**Acceptance Criteria:**
- All remaining broken links addressed
- Strategy documented for each fix

### Task 8: Final Link Validation

Run final validation to confirm ZERO broken links:

```bash
cd /home/jhenry/Source/agent-knowledge
bash meta/validate-links.sh > meta/link-validation-final.txt 2>&1

# Verify zero broken links
grep "Broken links found: 0" meta/link-validation-final.txt || echo "FAILED - still have broken links"
```

**Acceptance Criteria:**
- **CRITICAL:** Zero broken links
- Validation report shows 100% success
- meta/link-validation-final.txt shows "Broken links found: 0"

### Task 9: Create Fix Summary

Document all fixes made:

Create `/home/jhenry/Source/agent-knowledge/meta/link-fix-summary.md`:

```markdown
# Link Fix Summary

**Date:** [Current Date]
**Worker:** fix-links
**Status:** COMPLETE

## Summary

Fixed 222 broken internal links to achieve "zero broken links" status.

## Fixes Applied

### 1. core-rules/INDEX.md Path Corrections
- Updated X references from `./python/` → `./python-standards/`
- Updated X references from `./agents/` → `./agent-roles/`
- Updated X references from `./core-rules/patterns/` → `../patterns/`
- Updated X references from `./core-rules/templates/` → `../templates/`

### 2. Template References
- Created X placeholder README files in template directories
- Removed X links to non-existent templates
- Updated X links to point to existing templates

### 3. Documentation References
- Fixed X broken documentation links
- Updated X cross-references
- Removed X obsolete references

### 4. External References
- Removed X references to external project paths

## Validation Results

**Before:**
- Broken links: 222
- Success rate: 55%

**After:**
- Broken links: 0
- Success rate: 100%

## Files Modified

[List all files modified with link fixes]

## Verification

- [x] Ran meta/validate-links.sh
- [x] Zero broken links confirmed
- [x] All navigation tested
- [x] Success criteria met
```

**Acceptance Criteria:**
- Fix summary created
- All changes documented
- Verification checklist complete

### Task 10: Commit Link Fixes

```bash
git add .
git commit -m "[fix-links] Fix all 222 broken internal links

- Updated core-rules/INDEX.md path references
  - python/ → python-standards/
  - agents/ → agent-roles/
  - core-rules/patterns/ → ../patterns/
  - core-rules/templates/ → ../templates/
- Created placeholder README files in template directories
- Fixed documentation cross-references
- Removed external path references
- Validated: ZERO broken links (100% success rate)

Resolves critical blocker for v1.0.0 release"
```

**Acceptance Criteria:**
- All changes committed
- Commit message comprehensive
- Link fix summary included in commit

## Success Criteria
- [ ] All 222 broken links fixed
- [ ] core-rules/INDEX.md paths corrected
- [ ] Template references valid or removed
- [ ] Documentation cross-references working
- [ ] External references removed
- [ ] **ZERO broken links** (run meta/validate-links.sh)
- [ ] Link fix summary created
- [ ] Changes committed to git
- [ ] Validation passes with 100% success rate

## Notes
- **CRITICAL:** Must achieve zero broken links - this is a release blocker
- Use systematic approach: fix by category, validate frequently
- Document all changes in link-fix-summary.md
- Test navigation after fixes to ensure usability
- Use absolute paths from /home/jhenry/Source/agent-knowledge
