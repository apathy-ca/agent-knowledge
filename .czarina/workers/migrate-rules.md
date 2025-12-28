# Worker: migrate-rules

## Mission
Migrate all content from the agent-rules repository into the agent-knowledge repository's core-rules/ directory, reorganizing the structure and preserving the templates separately.

## Deliverables
- All agent-rules content copied to core-rules/
- Directory structure reorganized (removed numbered prefixes)
- Templates moved to templates/ directory
- Legacy README preserved as AGENT_RULES_LEGACY.md

## Context
You are migrating 53+ rules across 9 domains from the agent-rules repository (43,873 lines). This content represents production-tested rules extracted from real projects including Hopper, Czarina, The Symposium, and SARK.

## Dependencies
- repo-setup (must complete first to have directory structure)

## References
- Implementation Plan: `/home/jhenry/Source/agent-knowledge/AGENT_KNOWLEDGE_MERGE_PLAN.md` (lines 306-324)
- Source Repository: `/home/jhenry/Source/agent-rules`
- Target Structure: Plan lines 143-290

## Task Breakdown

### Task 1: Copy Core Rules Content
Copy the main agent-rules content directories:
```bash
cp -r /home/jhenry/Source/agent-rules/agent-rules/* /home/jhenry/Source/agent-knowledge/core-rules/
```

**Acceptance Criteria:**
- All content from agent-rules/agent-rules/ copied to core-rules/
- File integrity verified (line counts match)
- All markdown files present

### Task 2: Reorganize Directory Structure
Remove numbered prefixes from directories:
```bash
cd /home/jhenry/Source/agent-knowledge/core-rules
mv 01-python-standards python-standards
mv 02-agent-roles agent-roles
mv 03-workflows workflows
mv 04-design-patterns design-patterns
mv 05-testing testing
mv 06-security security
mv 07-templates ../templates
mv 08-documentation documentation
mv 09-orchestration orchestration
```

**Acceptance Criteria:**
- All directories renamed to remove number prefixes
- Templates moved to repository root templates/ directory
- Directory names match target structure
- No numbered directories remain in core-rules/

### Task 3: Verify Content Migration
For each domain, verify content is complete:

**Python Standards (7 files, ~1,827 lines):**
- imports.md
- type-annotations.md
- async-await.md
- error-handling.md
- logging.md
- testing.md
- packaging.md

**Agent Roles (10 files, ~11,485 lines):**
- architect-role.md
- code-role.md
- debug-role.md
- qa-role.md
- orchestrator-role.md
- ask-role.md
- ops-role.md
- security-role.md
- docs-role.md
- roles-coordination.md

**Workflows (7 files, ~3,062 lines):**
- feature-workflow.md
- bugfix-workflow.md
- refactor-workflow.md
- investigation-workflow.md
- handoff-workflow.md
- recovery-workflow.md
- git-workflows.md

**Design Patterns (6 files, ~1,926 lines):**
- layer-based-architecture.md
- modular-design.md
- configuration-over-code.md
- progressive-complexity.md
- comprehensive-testing.md
- memory-patterns.md

**Testing (6 files, ~1,799 lines):**
- testing-philosophy.md
- pytest-standards.md
- test-organization.md
- fixtures-and-mocks.md
- integration-testing.md
- coverage-requirements.md

**Security (5 files, ~4,155 lines):**
- authentication.md
- authorization.md
- secrets-management.md
- input-validation.md
- audit-logging.md

**Documentation (6 files, ~1,959 lines):**
- docstring-standards.md
- readme-structure.md
- api-documentation.md
- architecture-docs.md
- changelog-standards.md
- inline-comments.md

**Orchestration (2 files, ~1,098 lines):**
- task-coordination.md
- agent-handoffs.md

**Templates (13 files, ~12,041 lines):**
- Verify all template directories moved to templates/

**Acceptance Criteria:**
- All expected files present in each directory
- Line counts approximately match source
- README.md files present in each domain
- INDEX.md preserved

### Task 4: Preserve Legacy Documentation
```bash
cp /home/jhenry/Source/agent-rules/README.md /home/jhenry/Source/agent-knowledge/AGENT_RULES_LEGACY.md
cp -r /home/jhenry/Source/agent-rules/examples /home/jhenry/Source/agent-knowledge/examples/agent-rules-legacy
```

**Acceptance Criteria:**
- Original README preserved as AGENT_RULES_LEGACY.md
- Examples preserved in examples/agent-rules-legacy/
- Historical context maintained

### Task 5: Clean Up Temporary Files
Remove any temporary or build files that shouldn't be migrated:
```bash
cd /home/jhenry/Source/agent-knowledge
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete
find . -name ".DS_Store" -delete
```

**Acceptance Criteria:**
- No Python cache files
- No OS temporary files
- Only source markdown and documentation present

### Task 6: Create Migration Summary
Create a file documenting what was migrated:
```markdown
# Migration Summary: agent-rules

**Date:** [Current Date]
**Source:** /home/jhenry/Source/agent-rules (v1.0.0)
**Target:** /home/jhenry/Source/agent-knowledge/core-rules/

## Content Migrated

- Python Standards: 7 files, ~1,827 lines
- Agent Roles: 10 files, ~11,485 lines
- Workflows: 7 files, ~3,062 lines
- Design Patterns: 6 files, ~1,926 lines
- Testing: 6 files, ~1,799 lines
- Security: 5 files, ~4,155 lines
- Documentation: 6 files, ~1,959 lines
- Orchestration: 2 files, ~1,098 lines
- Templates: 13 files, ~12,041 lines

**Total:** 53+ files, ~43,873 lines

## Changes Made

- Removed numbered directory prefixes (01-, 02-, etc.)
- Moved templates from core-rules/07-templates to templates/
- Preserved original README as AGENT_RULES_LEGACY.md
- Preserved examples in examples/agent-rules-legacy/

## Verification

- [x] All source files copied
- [x] Directory structure matches specification
- [x] Line counts verified
- [x] No content lost
```

Save to: `/home/jhenry/Source/agent-knowledge/meta/migration-agent-rules.md`

**Acceptance Criteria:**
- Migration summary created
- Includes file counts and line counts
- Documents all changes made
- Saved in meta/ directory

### Task 7: Commit Migration
```bash
git add .
git commit -m "[migrate-rules] Migrate agent-rules content to core-rules/

- Copied 53+ rules across 9 domains (~43,873 lines)
- Reorganized directory structure (removed number prefixes)
- Moved templates to templates/ directory
- Preserved legacy README and examples
- Created migration summary

Source: agent-rules v1.0.0"
```

**Acceptance Criteria:**
- Migration committed to git
- Commit message documents changes
- All migrated files staged and committed

## Success Criteria
- [ ] All 53+ files from agent-rules migrated
- [ ] Directory structure reorganized per specification
- [ ] Templates separated to templates/ directory
- [ ] Legacy documentation preserved
- [ ] Migration summary created
- [ ] Changes committed to git
- [ ] No content lost or corrupted
- [ ] Line counts verified against source

## Notes
- Dependency: repo-setup must be complete before starting
- Use absolute paths: /home/jhenry/Source/agent-rules and /home/jhenry/Source/agent-knowledge
- Verify line counts using `wc -l` to ensure no content loss
- Keep original files in agent-rules repo untouched
