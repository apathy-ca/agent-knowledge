# Agent-Knowledge Phase 2 Remediation Launch Guide

**Purpose:** Complete remaining 30-40% of work to achieve v1.0.0 release

## Phase 2 Overview

**Critical Blockers to Resolve:**
1. Fix 222 broken internal links (RELEASE BLOCKER)
2. Complete pattern migration from 17% to 100%
3. Create all missing deliverables (61% missing)

**Workers:** 4 (2 parallel, 2 sequential)
**Estimated Duration:** 4-6 hours
**Success Criteria:** Zero broken links, 100% pattern migration, all deliverables present

---

## Pre-Flight Checklist

Before launching Phase 2, verify:

- [ ] Phase 1 work is committed to main branch
- [ ] Source repositories available:
  - `/home/jhenry/Source/agent-rules`
  - `/home/jhenry/Source/agentic-dev-patterns`
- [ ] Current directory: `/home/jhenry/Source/agent-knowledge`
- [ ] Git status clean (or known state)
- [ ] Remediation plan reviewed: `REMEDIATION_PLAN.md`

---

## Worker Execution Plan

### Phase 2A: Parallel Execution (Critical Priority)

**Worker 1: fix-links**
- Mission: Fix all 222 broken internal links
- Priority: CRITICAL
- Dependencies: None
- Branch: cz2/fix/links
- Estimated: 2-3 hours

**Worker 2: complete-patterns**
- Mission: Complete pattern migration (5 empty categories)
- Priority: CRITICAL
- Dependencies: None
- Branch: cz2/fix/patterns
- Estimated: 2-3 hours

**Run in parallel** - Both workers can work simultaneously

---

### Phase 2B: Sequential Execution (High Priority)

**Worker 3: complete-deliverables**
- Mission: Create all missing deliverables
- Priority: HIGH
- Dependencies: fix-links, complete-patterns
- Branch: cz2/fix/deliverables
- Estimated: 1-2 hours

**Waits for Phase 2A to complete**

---

### Phase 2C: Final Validation (Release Gate)

**Worker 4: final-validate**
- Mission: Re-validate and approve v1.0.0 release
- Priority: HIGH
- Dependencies: complete-deliverables
- Branch: cz2/fix/validate
- Estimated: 1 hour

**Waits for Phase 2B to complete**

---

## Launch Commands

### Option 1: Czarina Auto-Launch (Recommended)

```bash
cd /home/jhenry/Source/agent-knowledge

# Launch Phase 2 with czarina
czarina launch \
  --project "Agent Knowledge Remediation - Phase 2" \
  --plan REMEDIATION_PLAN.md \
  --workers fix-links,complete-patterns,complete-deliverables,final-validate \
  --parallel "fix-links,complete-patterns" \
  --branch-prefix "cz2/fix"
```

### Option 2: Manual Worker Launch

If czarina auto-launch is not available, launch workers manually in tmux:

**Step 1: Create tmux session**
```bash
tmux new-session -d -s agent-knowledge-phase2
```

**Step 2: Launch Phase 2A workers (parallel)**
```bash
# Window 0: fix-links
tmux send-keys -t agent-knowledge-phase2:0 "cd /home/jhenry/Source/agent-knowledge" Enter
tmux send-keys -t agent-knowledge-phase2:0 "git checkout -b cz2/fix/links" Enter
tmux send-keys -t agent-knowledge-phase2:0 "claude --permission-mode bypassPermissions 'Read .czarina/workers/fix-links.md and begin Task 1'" Enter

# Window 1: complete-patterns
tmux new-window -t agent-knowledge-phase2:1
tmux send-keys -t agent-knowledge-phase2:1 "cd /home/jhenry/Source/agent-knowledge" Enter
tmux send-keys -t agent-knowledge-phase2:1 "git checkout -b cz2/fix/patterns" Enter
tmux send-keys -t agent-knowledge-phase2:1 "claude --permission-mode bypassPermissions 'Read .czarina/workers/complete-patterns.md and begin Task 1'" Enter
```

**Step 3: Wait for Phase 2A to complete, then launch Phase 2B**
```bash
# Window 2: complete-deliverables (wait for 2A)
tmux new-window -t agent-knowledge-phase2:2
tmux send-keys -t agent-knowledge-phase2:2 "cd /home/jhenry/Source/agent-knowledge" Enter
tmux send-keys -t agent-knowledge-phase2:2 "git checkout main && git merge cz2/fix/links cz2/fix/patterns" Enter
tmux send-keys -t agent-knowledge-phase2:2 "git checkout -b cz2/fix/deliverables" Enter
tmux send-keys -t agent-knowledge-phase2:2 "claude --permission-mode bypassPermissions 'Read .czarina/workers/complete-deliverables.md and begin Task 1'" Enter
```

**Step 4: Wait for Phase 2B to complete, then launch Phase 2C**
```bash
# Window 3: final-validate (wait for 2B)
tmux new-window -t agent-knowledge-phase2:3
tmux send-keys -t agent-knowledge-phase2:3 "cd /home/jhenry/Source/agent-knowledge" Enter
tmux send-keys -t agent-knowledge-phase2:3 "git checkout main && git merge cz2/fix/deliverables" Enter
tmux send-keys -t agent-knowledge-phase2:3 "git checkout -b cz2/fix/validate" Enter
tmux send-keys -t agent-knowledge-phase2:3 "claude --permission-mode bypassPermissions 'Read .czarina/workers/final-validate.md and begin Task 1'" Enter
```

**Step 5: Attach to session**
```bash
tmux attach -t agent-knowledge-phase2
```

---

## Monitoring Progress

### Czar Dashboard (if available)
```bash
# Switch to czar window to monitor
tmux attach -t czarina-agent-knowledge-merge
# Press Ctrl+b 0 to go to czar window
```

### Check Worker Status
```bash
# View worker branches
git branch -a | grep cz2

# Check commits on worker branches
git log --oneline --all --graph --decorate

# View worker logs (if using czarina logging)
tail -f .czarina/logs/*.log
```

### Validation Checkpoints

**After Phase 2A completes:**
- Check: Are links fixed? Run `bash meta/validate-links.sh`
- Check: Are patterns complete? `ls -la patterns/*/`

**After Phase 2B completes:**
- Check: Are deliverables present? Review checklist in complete-deliverables worker

**After Phase 2C completes:**
- Check: Final quality report status
- Look for: `meta/FINAL-QUALITY-REPORT.md` should say "✅ READY FOR RELEASE"

---

## Success Indicators

**Phase 2A Success:**
- ✅ `meta/validate-links.sh` shows "Broken links found: 0"
- ✅ All 6 pattern directories have content files
- ✅ Commits on cz2/fix/links and cz2/fix/patterns branches

**Phase 2B Success:**
- ✅ All LEGACY files verified
- ✅ meta/cross-reference-map.md created
- ✅ Cross-references added to content files
- ✅ Commit on cz2/fix/deliverables branch

**Phase 2C Success:**
- ✅ meta/FINAL-QUALITY-REPORT.md shows PASS
- ✅ Zero broken links confirmed
- ✅ v1.0.0 release APPROVED
- ✅ Commit on cz2/fix/validate branch

---

## Post-Phase 2 Actions

### If Validation Passes ✅

1. **Merge all worker branches to main:**
   ```bash
   git checkout main
   git merge cz2/fix/links
   git merge cz2/fix/patterns
   git merge cz2/fix/deliverables
   git merge cz2/fix/validate
   ```

2. **Tag v1.0.0 release:**
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0: Unified agent knowledge repository

   Merged agent-rules and agentic-dev-patterns into single repository.

   - 53+ rules across 9 domains (~43,873 lines)
   - 6 pattern categories with battle-tested patterns
   - Comprehensive cross-references and navigation
   - Zero broken links
   - Professional documentation

   Ready for use by Hopper, Czarina, The Symposium, and SARK."

   git push origin main
   git push origin v1.0.0
   ```

3. **Create GitHub release** (if applicable)

4. **Update dependent projects:**
   - Hopper
   - Czarina
   - The Symposium
   - SARK

### If Validation Fails ❌

1. **Review validation report:**
   ```bash
   cat meta/FINAL-QUALITY-REPORT.md
   ```

2. **Identify remaining issues**

3. **Create Phase 3 remediation** (if needed)

4. **Escalate to user** for guidance

---

## Troubleshooting

### Worker Stuck or Failed

**Check worker status:**
```bash
# View worker session
tmux attach -t agent-knowledge-phase2
# Navigate to worker window (Ctrl+b [window-number])
```

**Common issues:**
- Missing source repository files
- Permission issues
- Git conflicts

**Solutions:**
- Restart worker: Kill and relaunch claude process
- Check dependencies: Ensure prior workers completed
- Review worker definition: `.czarina/workers/[worker-name].md`

### Links Still Broken After fix-links

**Diagnose:**
```bash
bash meta/validate-links.sh | grep "Broken link" | head -20
```

**Common causes:**
- New broken links introduced by other workers
- External references not removed
- Path case sensitivity issues

**Fix:**
- Re-run fix-links worker
- Manual fixes if needed
- Re-validate

### Pattern Migration Incomplete

**Check:**
```bash
for dir in patterns/*/; do
  echo "$dir: $(find $dir -name "*.md" | wc -l) files"
done
```

**If any show 0 or 1 file:**
- complete-patterns worker didn't finish
- Source files missing from agentic-dev-patterns
- Restart worker or escalate

---

## Emergency Abort

If you need to stop Phase 2:

```bash
# Kill all claude processes
pkill -f "claude.*agent-knowledge"

# Delete worker branches (if needed)
git branch -D cz2/fix/links cz2/fix/patterns cz2/fix/deliverables cz2/fix/validate

# Return to clean main
git checkout main
git reset --hard origin/main  # CAUTION: Loses uncommitted work
```

---

## Files Created for Phase 2

**Planning:**
- `REMEDIATION_PLAN.md` - Overall Phase 2 plan
- `.czarina/PHASE2_LAUNCH.md` - This file

**Worker Definitions:**
- `.czarina/workers/fix-links.md`
- `.czarina/workers/complete-patterns.md`
- `.czarina/workers/complete-deliverables.md`
- `.czarina/workers/final-validate.md`

**Expected Outputs:**
- `meta/link-fix-summary.md`
- `meta/phase2-completion-summary.md`
- `meta/FINAL-QUALITY-REPORT.md` (updated)
- All pattern content files
- All missing deliverables

---

## Ready to Launch?

**Checklist:**
- [ ] Pre-flight checklist complete
- [ ] Worker definitions reviewed
- [ ] Source repositories available
- [ ] Remediation plan understood
- [ ] Ready to commit 4-6 hours to completion

**Launch command:**
```bash
cd /home/jhenry/Source/agent-knowledge
# Use czarina auto-launch or manual tmux launch above
```

**Good luck! 🎯**

---

**Prepared by:** Czar orchestrator
**Date:** 2025-12-28
**Status:** Ready for launch
