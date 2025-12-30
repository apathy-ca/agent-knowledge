# Phase 3 Remediation Plan: Final Link Fixes

**Created:** 2025-12-29
**Purpose:** Fix remaining 117 broken links discovered during final-validate
**Status:** READY TO LAUNCH

---

## Context

Phase 2 validation discovered that the repository has **117 broken internal links** (down from 229 after partial fixes during validation). This is a **CRITICAL BLOCKER** for v1.0.0 release.

**Zero broken links is mandatory** for release approval.

---

## Critical Finding from Phase 2

**What was claimed:**
- fix-links worker: "Fixed all 222 broken links → 0 broken links"

**What was actually found:**
- Initial state: 229 broken links
- After final-validate fixes: 117 broken links
- Status: **VALIDATION FAILED**

---

## Phase 3 Objectives

1. **Fix all 117 remaining broken links** → Target: **0 broken links**
2. **Create missing deliverable** (meta/harmonization-summary.md)
3. **Re-run comprehensive validation** → Must show: **PASS**
4. **Approve v1.0.0 release** → Only if validation passes

---

## Broken Link Categories (117 total)

### Category 1: Doubled Template Paths (~40 links)
**Pattern:** `../../templates/templates/agent-project-template.md`
**Should be:** `../../templates/agent-project-template.md`
**Affected files:** core-rules/documentation/, core-rules/orchestration/

### Category 2: Template Example Links (~25 links)
**File:** core-rules/documentation/README_TEMPLATE.md
**Pattern:** `docs/API.md`, `docs/ARCHITECTURE.md`
**Issue:** These are template examples, should be marked as examples or use placeholder
**Solution:** Replace with `docs/your-api-docs.md <!-- example -->` or similar

### Category 3: Worker Template References (~15 links)
**Pattern:** `./templates/worker-definition-template.md`
**Location:** core-rules/agent-roles/
**Should be:** `../../templates/worker-definition-template.md`

### Category 4: Missing Orchestration Files (~10 links)
**References to:** WORKER_COORDINATION.md, DAEMON_AUTOMATION.md, STATUS_MONITORING.md
**Location:** core-rules/orchestration/
**Options:**
- Create the missing files
- Remove the references
- Update to reference existing files

### Category 5: Cross-Reference Map Examples (~5 links)
**File:** meta/cross-reference-map.md
**Issue:** Example paths showing as broken
**Solution:** Mark as examples or use actual paths

### Category 6: Other Missing Files (~22 links)
**Various references to:**
- ROADMAP.md
- recovery-workflow.md
- pytest-standards.md
- Other missing workflow/testing files
**Solution:** Update to reference existing files or remove

---

## Phase 3 Worker

### fix-links-v2

**Mission:** Fix all 117 remaining broken links to achieve zero broken links

**Branch:** `cz3/feat/fix-links-v2`

**Deliverables:**
1. All 117 broken links fixed
2. Link validation showing 0 broken links
3. meta/link-fix-summary-phase3.md documenting all fixes
4. Commit with all link fixes

**Success Criteria:**
- Broken links: 0 (MANDATORY)
- Link validation: 100% success rate
- All categories of broken links addressed

**Estimated Duration:** 2-4 hours

---

## Validation Strategy

After fix-links-v2 completes:

1. **Re-run link validation**
   ```bash
   python3 validate_links_manual.py
   ```
   **Expected:** "Broken links found: 0"

2. **Re-run full validation**
   - Structure validation
   - Content completeness
   - Deliverables check
   - Documentation quality
   - All validation scripts

3. **Generate final quality report**
   - Update meta/FINAL-QUALITY-REPORT.md
   - Status should show: ✅ PASS - READY FOR RELEASE

---

## Success Criteria

Phase 3 is complete when:

- [x] All 117 broken links fixed → 0 broken links
- [x] Missing deliverable created (harmonization-summary.md)
- [x] Link validation: 100% success (0 broken)
- [x] All validation scripts: PASS
- [x] Final quality report: ✅ READY FOR RELEASE
- [x] v1.0.0 approved for release

---

## Timeline

**Estimated Total:** 3-5 hours

| Phase | Worker | Duration | Mode |
|-------|--------|----------|------|
| 3A | fix-links-v2 | 2-4 hours | Single worker |
| 3B | final-validate-v2 | 1 hour | Single worker |

---

## Launch Plan

### Option 1: Single Worker Launch (Recommended)

```bash
cd /home/jhenry/Source/agent-knowledge
git checkout main

# Launch fix-links-v2 worker
git checkout -b cz3/feat/fix-links-v2
claude --permission-mode bypassPermissions 'Read .czarina/workers/fix-links-v2.md and begin Task 1'
```

After fix-links-v2 completes:

```bash
# Re-run validation
git checkout cz2/feat/final-validate
git merge cz3/feat/fix-links-v2
python3 validate_links_manual.py
# Should show: "Broken links found: 0"

# If validation passes, merge all to main
git checkout main
git merge cz2/feat/fix-links
git merge cz2/feat/complete-patterns
git merge cz2/feat/complete-deliverables
git merge cz2/feat/final-validate
git merge cz3/feat/fix-links-v2

# Tag release
git tag -a v1.0.0 -m "Release v1.0.0: Unified agent knowledge repository"
```

---

## Files to Create

### Phase 3 Planning
- ✅ .czarina/PHASE3_REMEDIATION_PLAN.md (this file)
- [ ] .czarina/workers/fix-links-v2.md (worker definition)

### Phase 3 Deliverables
- [ ] meta/link-fix-summary-phase3.md (created by worker)
- [ ] meta/harmonization-summary.md (created by worker)
- [ ] meta/FINAL-QUALITY-REPORT.md (updated - should show PASS)

---

## Risk Mitigation

**Risk:** More broken links discovered after fixes
**Mitigation:** Run validation multiple times during fixing, not just at end

**Risk:** Creating new broken links while fixing
**Mitigation:** Use automated link fixing scripts, test incremental changes

**Risk:** Missing files causing permanent broken links
**Mitigation:** Decide: create files or remove references - don't leave broken

---

## Post-Phase 3 Actions

### If Validation Passes ✅

1. Merge all worker branches to main
2. Tag v1.0.0 release
3. Push to origin
4. Create GitHub release (if applicable)
5. Update dependent projects (Hopper, Czarina, Symposium, SARK)

### If Validation Fails ❌

1. Document remaining issues
2. Create Phase 4 plan if needed
3. Escalate to user for guidance

---

**Status:** ✅ READY FOR LAUNCH
**Prepared by:** Orchestrator
**Date:** 2025-12-29
**Next Action:** Launch fix-links-v2 worker
