# Git Workflow Patterns

**Purpose**: Version control patterns and practices for AI-assisted development.

**Value**: Clean commit history, effective collaboration, reduced conflicts, better code review.

---

## Philosophy

**Good git practices**:
- Branch per feature
- Atomic commits
- Clear commit messages
- Small PRs (< 500 lines)
- Test before merge
- Clean history

**Bad git practices**:
- Work directly on main
- Large, mixed commits
- Vague commit messages
- Huge PRs (> 1000 lines)
- Merge without testing
- Force push to shared branches

---

## Pattern Categories

### [Branch Strategies](./branch-strategies.md)
Effective branching for AI-assisted development:
- Feature branch per task
- Worker-specific branches (czarina/*, hopper/*)
- Short-lived branches (< 1 week)
- Branch naming conventions
- AI-generated branch names
- Branch cleanup
- Protection rules
- Experimental branches
- Integration branch strategy

**Key Pattern**: Branch for every feature, merge often, delete quickly

### [Commit Patterns](./commit-patterns.md)
Commit organization and messaging:
- Atomic commits (one logical change)
- Conventional commit format (feat/fix/docs/etc.)
- AI commit message generation
- Commit frequency (natural checkpoints)
- Commit amending (pre-push only)
- Co-authoring with AI
- Documentation sync in commits
- Test inclusion strategies

**Key Pattern**: Commit often, commit atomically, commit clearly

### [PR Workflows](./pr-workflows.md)
Pull request creation and review:
- AI-generated PR descriptions
- PR size management (< 500 lines ideal)
- Self-review before submission
- Draft PRs for work in progress
- PR review checklists
- Automated checks integration
- Merge strategies (merge/squash/rebase)
- Stacked PR dependencies

**Key Pattern**: Small PRs, clear descriptions, passing tests

### [Conflict Resolution](./conflict-resolution.md)
Preventing and resolving merge conflicts:
- Conflict prevention (communication, short branches)
- AI-assisted resolution workflow
- Understanding conflict markers
- Systematic resolution steps
- Testing after resolution
- Abort and retry strategies
- Binary file conflicts
- Refactoring conflict coordination

**Key Pattern**: Prevent through communication, resolve through understanding

---

## Quick Reference

### Starting New Feature
```bash
# 1. Create feature branch
git checkout -b feat/email-verification

# 2. Implement and commit atomically
git commit -m "feat(auth): Add email verification model"
git commit -m "feat(auth): Implement verification email sending"
git commit -m "test(auth): Add email verification tests"

# 3. Keep branch updated
git rebase main  # Daily if branch lives > 1 day

# 4. Create PR when ready
gh pr create --fill

# 5. After merge, cleanup
git branch -d feat/email-verification
```

### Commit Message Format
```bash
<type>(<scope>): <subject>

# Examples:
git commit -m "feat(auth): Add JWT token generation"
git commit -m "fix(payment): Validate refund amounts correctly"
git commit -m "docs(api): Update authentication endpoints"
git commit -m "test(user): Add email verification tests"
```

### PR Checklist
- [ ] < 500 lines changed
- [ ] All tests passing
- [ ] Self-review completed
- [ ] Clear PR description
- [ ] Linked to issue

### Conflict Resolution
```bash
# 1. Identify conflicts
git status

# 2. Resolve each file
# Edit file, remove <<<<<<< ======= >>>>>>> markers
# Combine both changes appropriately

# 3. Test resolution
pytest tests/

# 4. Mark resolved and continue
git add resolved_file.py
git rebase --continue
```

---

## Git Workflow by Task Type

| Task Type | Branch Name | Commit Style | PR Size |
|-----------|-------------|--------------|---------|
| New Feature | feat/feature-name | Atomic, per component | < 500 lines |
| Bug Fix | fix/bug-description | Single commit preferred | < 200 lines |
| Refactoring | refactor/component-name | Per-file or per-component | < 500 lines |
| Documentation | docs/topic | Grouped by topic | < 200 lines |
| Tests | test/component | With implementation | Include in feature PR |

---

## Common Git Problems and Solutions

### Problem: "Branch has conflicts with main"
**Solutions**:
- Rebase on main: `git rebase main`
- Resolve conflicts systematically
- Test after resolution
- See [Conflict Resolution](./conflict-resolution.md)

### Problem: "PR too large to review"
**Solutions**:
- Break into smaller PRs
- Use stacked PRs for dependencies
- See [PR Workflows](./pr-workflows.md)

### Problem: "Accidentally committed to main"
**Solutions**:
- If not pushed: `git reset HEAD~1`
- Create feature branch: `git checkout -b feat/my-feature`
- Cherry-pick commit: `git cherry-pick <commit-sha>`

### Problem: "Forgot to include file in commit"
**Solutions**:
- If not pushed: `git add file.py && git commit --amend --no-edit`
- If pushed: Create new commit (don't amend pushed commits)

---

## Best Practices

### Do
- ✅ Create branch per feature/fix
- ✅ Use conventional commit messages
- ✅ Keep commits atomic
- ✅ Keep PRs small (< 500 lines)
- ✅ Test before creating PR
- ✅ Rebase on main daily for long-lived branches

### Don't
- ❌ Commit directly to main
- ❌ Create vague commit messages
- ❌ Mix unrelated changes in commits
- ❌ Create huge PRs (> 1000 lines)
- ❌ Merge without passing tests
- ❌ Force push to shared branches

---

## Impact Metrics

Based on The Symposium development (v0.4.5):

**Collaboration**:
- Clean git history enables easy code archaeology
- Worker-specific branches (czarina/*, hopper/*) clarified ownership
- Small PRs (avg 250 lines) led to faster reviews

**Quality**:
- Atomic commits enabled precise rollbacks
- Conventional commits improved changelog generation
- PR self-review caught 30-40% of issues before review

**Efficiency**:
- Short-lived branches reduced conflicts by 70-80%
- Conflict prevention strategies saved hours of resolution time
- Automated PR checks caught issues early

---

## Related Patterns

- [Error Recovery](../error-recovery/README.md) - Git-related error patterns
- [Mode Capabilities](../mode-capabilities/README.md) - Which modes can commit
- [Tool Use](../tool-use/README.md) - Efficient git command usage

---

## Related Core Rules

**See Also**:
- [Git Workflows](../../core-rules/workflows/git-workflows.md) - Git standards and requirements

**Note**: This patterns directory focuses on **HOW** to use git effectively (strategies, workflows, examples). The core-rules directory defines **WHAT** is required (standards, policies, requirements). Use both together for best results.

---

**Last Updated**: 2025-12-29
**Patterns**: 4 core patterns (Branch Strategies, Commit Patterns, PR Workflows, Conflict Resolution)
**Source**: The Symposium development (v0.4.5), Czarina multi-worker coordination
**Status**: Complete

*"Version control is collaboration infrastructure - make it clear, clean, and consistent."*
