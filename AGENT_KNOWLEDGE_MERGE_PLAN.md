# Agent-Knowledge Repository Merge Plan

**Version:** 1.0.0
**Date:** 2025-12-28
**Purpose:** Plan for merging agent-rules and agentic-dev-patterns into unified agent-knowledge repository

---

## Executive Summary

This document outlines the plan to merge two related repositories into a single `agent-knowledge` repository:

- **agent-rules** (53+ rules, 9 domains, templates, 43,873 lines)
- **agentic-dev-patterns** (proven patterns from The Symposium development)

The merged repository will serve as the canonical knowledge base for AI-assisted development across the entire ecosystem (Hopper, Czarina, The Symposium, SARK).

## Current State Analysis

### agent-rules Repository

**Location:** `/home/jhenry/Source/agent-rules`

**Structure:**
```
agent-rules/
├── README.md (2,505 lines)
├── agent-rules/
│   ├── INDEX.md
│   ├── README.md
│   ├── 01-python-standards/ (7 files, 1,827 lines)
│   ├── 02-agent-roles/ (10 files, 11,485 lines)
│   ├── 03-workflows/ (7 files, 3,062 lines)
│   ├── 04-design-patterns/ (6 files, 1,926 lines)
│   ├── 05-testing/ (6 files, 1,799 lines)
│   ├── 06-security/ (5 files, 4,155 lines)
│   ├── 07-templates/ (13 files, 12,041 lines)
│   ├── 08-documentation/ (6 files, 1,959 lines)
│   └── 09-orchestration/ (2 files, 1,098 lines)
└── examples/ (configuration examples)
```

**Key Content:**
- Production-tested rules extracted from real projects
- Role-based patterns (Architect, Code, Debug, QA, Orchestrator)
- Templates for rapid project setup
- Comprehensive index and navigation

**Version:** v1.0.0 Complete

### agentic-dev-patterns Repository

**Location:** `/home/jhenry/Source/agentic-dev-patterns`

**Structure:**
```
agentic-dev-patterns/
├── README.md
├── ERROR_RECOVERY_PATTERNS.md
├── TOOL_USE_PATTERNS.md
├── MODE_CAPABILITIES.md
├── GIT_WORKFLOW_PATTERNS.md
├── TESTING_PATTERNS.md
└── CONTEXT_MANAGEMENT.md
```

**Key Content:**
- Error recovery patterns (30-50% reduction in debugging time)
- Tool use optimization (40-60% efficiency improvement)
- Mode capabilities (Architect, Code, Debug, Ask, Orchestrator)
- Git workflow patterns
- Testing strategies
- Battle-tested from The Symposium project

**Version:** v1.0.0 Initial Release

### Overlap Analysis

**Common topics:**
- Testing patterns (both repos)
- Git workflows (both repos)
- Agent roles/modes (both repos)
- Error handling (both repos)

**Unique to agent-rules:**
- Python standards
- Security patterns
- Templates
- Documentation standards
- Orchestration patterns

**Unique to agentic-dev-patterns:**
- Detailed error recovery scenarios
- Tool use optimization specifics
- Context management strategies

## Merge Strategy

### Option A: Full Merge (Recommended)

**Create new repository with combined content**

**Pros:**
- Single source of truth
- Unified navigation
- Easy to discover related content
- Simpler dependency management

**Cons:**
- Larger repository
- More migration work upfront

### Option B: Submodules

**Keep separate repos, link via git submodules**

**Pros:**
- Preserve independent history
- Can evolve separately

**Cons:**
- Complexity (submodule management)
- Harder to discover content
- Dependency management issues

### Option C: Monorepo with Workspaces

**Single repo, separate packages**

**Pros:**
- Shared tooling
- Can version independently
- Clear boundaries

**Cons:**
- Overhead for simple markdown files

**Decision: Option A (Full Merge)** - Best for discoverability and ecosystem usage

## Repository Structure

### Proposed Structure

```
agent-knowledge/
├── README.md                    # Unified overview and navigation
├── CONTRIBUTING.md              # How to add patterns/rules
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT or Apache 2.0
│
├── core-rules/                  # From agent-rules
│   ├── INDEX.md                 # Navigation for rules
│   ├── python-standards/
│   │   ├── README.md
│   │   ├── imports.md
│   │   ├── type-annotations.md
│   │   ├── async-await.md
│   │   ├── error-handling.md
│   │   ├── logging.md
│   │   ├── testing.md
│   │   └── packaging.md
│   │
│   ├── agent-roles/
│   │   ├── README.md
│   │   ├── architect-role.md
│   │   ├── code-role.md
│   │   ├── debug-role.md
│   │   ├── qa-role.md
│   │   ├── orchestrator-role.md
│   │   ├── ask-role.md
│   │   ├── ops-role.md
│   │   ├── security-role.md
│   │   ├── docs-role.md
│   │   └── roles-coordination.md
│   │
│   ├── workflows/
│   │   ├── README.md
│   │   ├── feature-workflow.md
│   │   ├── bugfix-workflow.md
│   │   ├── refactor-workflow.md
│   │   ├── investigation-workflow.md
│   │   ├── handoff-workflow.md
│   │   ├── recovery-workflow.md
│   │   └── git-workflows.md         # Merged from agentic-dev-patterns
│   │
│   ├── design-patterns/
│   │   ├── README.md
│   │   ├── layer-based-architecture.md
│   │   ├── modular-design.md
│   │   ├── configuration-over-code.md
│   │   ├── progressive-complexity.md
│   │   ├── comprehensive-testing.md
│   │   └── memory-patterns.md
│   │
│   ├── testing/
│   │   ├── README.md
│   │   ├── testing-philosophy.md
│   │   ├── pytest-standards.md
│   │   ├── test-organization.md
│   │   ├── fixtures-and-mocks.md
│   │   ├── integration-testing.md
│   │   ├── coverage-requirements.md
│   │   └── testing-patterns.md      # Merged from agentic-dev-patterns
│   │
│   ├── security/
│   │   ├── README.md
│   │   ├── authentication.md
│   │   ├── authorization.md
│   │   ├── secrets-management.md
│   │   ├── input-validation.md
│   │   └── audit-logging.md
│   │
│   ├── documentation/
│   │   ├── README.md
│   │   ├── docstring-standards.md
│   │   ├── readme-structure.md
│   │   ├── api-documentation.md
│   │   ├── architecture-docs.md
│   │   ├── changelog-standards.md
│   │   └── inline-comments.md
│   │
│   └── orchestration/
│       ├── README.md
│       ├── task-coordination.md
│       └── agent-handoffs.md
│
├── patterns/                    # From agentic-dev-patterns (enhanced)
│   ├── INDEX.md                 # Navigation for patterns
│   │
│   ├── error-recovery/
│   │   ├── README.md
│   │   ├── detection-patterns.md
│   │   ├── recovery-strategies.md
│   │   ├── retry-patterns.md
│   │   ├── fallback-patterns.md
│   │   └── escalation-patterns.md
│   │
│   ├── tool-use/
│   │   ├── README.md
│   │   ├── optimization-patterns.md
│   │   ├── batching-patterns.md
│   │   ├── caching-patterns.md
│   │   ├── parallel-execution.md
│   │   └── tool-selection.md
│   │
│   ├── mode-capabilities/
│   │   ├── README.md
│   │   ├── architect-mode.md
│   │   ├── code-mode.md
│   │   ├── debug-mode.md
│   │   ├── ask-mode.md
│   │   ├── orchestrator-mode.md
│   │   └── mode-transitions.md
│   │
│   ├── context-management/
│   │   ├── README.md
│   │   ├── context-windows.md
│   │   ├── summarization.md
│   │   ├── memory-tiers.md
│   │   └── attention-shaping.md
│   │
│   └── git-workflows/           # Enhanced from both sources
│       ├── README.md
│       ├── branch-strategies.md
│       ├── commit-patterns.md
│       ├── pr-workflows.md
│       └── conflict-resolution.md
│
├── templates/                   # From agent-rules
│   ├── INDEX.md
│   ├── README.md
│   ├── project-init/
│   ├── python-service/
│   ├── fastapi-api/
│   ├── cli-tool/
│   ├── library/
│   └── agent-project/
│
├── examples/                    # Real-world examples
│   ├── hopper/                  # Hopper project examples
│   ├── czarina/                 # Czarina project examples
│   ├── thesymposium/            # The Symposium examples
│   └── sark/                    # SARK examples
│
└── meta/                        # Meta-documentation
    ├── versioning.md            # Version strategy
    ├── contributing.md          # How to contribute
    ├── pattern-template.md      # Template for new patterns
    └── learning-extraction.md   # How learnings become patterns
```

## Migration Steps

### Step 1: Create New Repository

```bash
cd ~/Source
mkdir agent-knowledge
cd agent-knowledge
git init
git branch -M main
```

### Step 2: Copy agent-rules Content

```bash
# Copy core rules structure
cp -r ../agent-rules/agent-rules ./core-rules

# Reorganize to match new structure
mv core-rules/01-python-standards core-rules/python-standards
mv core-rules/02-agent-roles core-rules/agent-roles
mv core-rules/03-workflows core-rules/workflows
mv core-rules/04-design-patterns core-rules/design-patterns
mv core-rules/05-testing core-rules/testing
mv core-rules/06-security core-rules/security
mv core-rules/07-templates ../templates
mv core-rules/08-documentation core-rules/documentation
mv core-rules/09-orchestration core-rules/orchestration

# Copy README and supporting files
cp ../agent-rules/README.md ./AGENT_RULES_LEGACY.md  # Preserve for reference
cp ../agent-rules/examples ./examples/agent-rules-legacy
```

### Step 3: Copy agentic-dev-patterns Content

```bash
# Create patterns directory
mkdir -p patterns

# Copy and reorganize pattern files
cp ../agentic-dev-patterns/ERROR_RECOVERY_PATTERNS.md patterns/error-recovery/README.md
cp ../agentic-dev-patterns/TOOL_USE_PATTERNS.md patterns/tool-use/README.md
cp ../agentic-dev-patterns/MODE_CAPABILITIES.md patterns/mode-capabilities/README.md
cp ../agentic-dev-patterns/GIT_WORKFLOW_PATTERNS.md patterns/git-workflows/README.md
cp ../agentic-dev-patterns/TESTING_PATTERNS.md patterns/testing-patterns/README.md
cp ../agentic-dev-patterns/CONTEXT_MANAGEMENT.md patterns/context-management/README.md
```

### Step 4: Create Unified Index

**Create `README.md`:**

```markdown
# Agent Knowledge

**Unified Knowledge Base for AI-Assisted Development**

This repository combines production-tested rules and patterns from:
- **agent-rules** - 53+ rules across 9 domains
- **agentic-dev-patterns** - Battle-tested patterns from The Symposium

## Quick Start

- **New to AI development?** Start with [Getting Started Guide](./docs/getting-started.md)
- **Looking for specific patterns?** Browse [Patterns Index](./patterns/INDEX.md)
- **Setting up a project?** Check [Templates](./templates/INDEX.md)
- **Contributing?** Read [Contributing Guide](./CONTRIBUTING.md)

## Structure

### Core Rules
Production-tested rules extracted from real projects:
- [Python Standards](./core-rules/python-standards/) - 7 rules
- [Agent Roles](./core-rules/agent-roles/) - 10 roles
- [Workflows](./core-rules/workflows/) - 7 workflows
- [Design Patterns](./core-rules/design-patterns/) - 6 patterns
- [Testing](./core-rules/testing/) - 6 rules
- [Security](./core-rules/security/) - 5 rules
- [Documentation](./core-rules/documentation/) - 6 rules
- [Orchestration](./core-rules/orchestration/) - 2 patterns

### Patterns
Battle-tested patterns with quantified impact:
- [Error Recovery](./patterns/error-recovery/) - 30-50% reduction in debugging time
- [Tool Use](./patterns/tool-use/) - 40-60% efficiency improvement
- [Mode Capabilities](./patterns/mode-capabilities/) - Role-specific patterns
- [Context Management](./patterns/context-management/) - Memory optimization
- [Git Workflows](./patterns/git-workflows/) - Branch and commit strategies

### Templates
Quick-start templates for common project types:
- [Project Templates](./templates/INDEX.md)

## Usage

### In Hopper
```yaml
# hopper-config.yaml
knowledge:
  agent_knowledge_path: "../agent-knowledge"
  auto_sync: true
```

### In Czarina
```yaml
# .czarina/config.yaml
knowledge:
  agent_knowledge_path: "../agent-knowledge"
  load_on_startup: true
```

### In The Symposium
```yaml
# Sage configuration
knowledge:
  base_path: "../agent-knowledge"
  index_patterns: true
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- How to submit new patterns
- Pattern review process
- Documentation standards
- Continuous learning integration

## Continuous Improvement

This knowledge base is continuously updated via:
- **Czarina closeout learnings** - What did workers discover?
- **Hopper routing feedback** - What routing decisions worked?
- **Symposium Sage wisdom** - What patterns emerged?

See [Learning Extraction](./meta/learning-extraction.md) for details.

## License

MIT License - See [LICENSE](./LICENSE)

## Version

Current version: v1.0.0

See [CHANGELOG.md](./CHANGELOG.md) for version history.
```

### Step 5: Create Cross-References

**Link related content:**

```markdown
# In core-rules/workflows/git-workflows.md

## Related Patterns

For detailed git workflow patterns, see:
- [Git Workflows Patterns](../../patterns/git-workflows/README.md)
- [Branch Strategies](../../patterns/git-workflows/branch-strategies.md)
- [Commit Patterns](../../patterns/git-workflows/commit-patterns.md)

## Related Templates

For git workflow templates:
- [Feature Branch Template](../../templates/git/feature-branch.md)
```

### Step 6: Deduplication

**Identify duplicate content:**
```bash
# Find files with similar names
find . -name "*git*workflow*" -o -name "*testing*"

# Manual review and merge
# If agent-rules/workflows/git-workflows.md overlaps with
# agentic-dev-patterns/GIT_WORKFLOW_PATTERNS.md:
# - Keep most comprehensive version
# - Add unique content from other
# - Cross-reference
```

### Step 7: Create Contributing Guide

**`CONTRIBUTING.md`:**

```markdown
# Contributing to Agent Knowledge

## How to Add a New Pattern

1. **Identify the pattern category**:
   - Error recovery?
   - Tool use optimization?
   - Workflow improvement?
   - Testing strategy?

2. **Use the template**:
   ```bash
   cp meta/pattern-template.md patterns/<category>/<pattern-name>.md
   ```

3. **Fill in the template**:
   - Name and description
   - Problem it solves
   - Solution (step-by-step)
   - Examples
   - Evidence (where was it tested?)
   - Impact (quantified if possible)

4. **Submit for review**:
   - Create PR
   - Link to evidence (session logs, commits, issues)
   - Tag reviewers

## Continuous Learning Integration

Patterns can be submitted:
- **Manually** (via PR)
- **Automatically** (via Symposium Learnings Processor)

### Automatic Submission

When Czarina closes a phase or Hopper completes a task:
1. Learnings extracted to JSON
2. Sent to Symposium Learnings Processor
3. LLM analyzes and proposes patterns
4. Human reviews and approves
5. Merged to agent-knowledge

## Review Process

**All patterns require:**
- Evidence from real usage
- Clear problem statement
- Step-by-step solution
- Examples
- Impact statement (qualitative or quantitative)

**Reviewers check:**
- Does this generalize beyond one case?
- Is it actionable?
- Is it documented clearly?
- Does it conflict with existing patterns?

## Pattern Quality Standards

**Good pattern:**
- Specific and actionable
- Backed by evidence
- Generalizable
- Measurable impact

**Bad pattern:**
- Vague or theoretical
- No evidence
- One-off solution
- Unmaintainable

## Versioning

**Semantic versioning:**
- Major version: Breaking changes (rare)
- Minor version: New patterns or rules
- Patch version: Clarifications, fixes

**Changelog:**
- Document all changes in `CHANGELOG.md`
- Link to PRs and issues
- Credit contributors
```

### Step 8: Initial Commit

```bash
git add .
git commit -m "Initial commit: Merge agent-rules and agentic-dev-patterns

- Merged agent-rules v1.0.0 (53+ rules, 9 domains)
- Merged agentic-dev-patterns v1.0.0 (6 pattern categories)
- Created unified structure with core-rules/ and patterns/
- Added cross-references and navigation
- Created CONTRIBUTING.md and meta-documentation

See CHANGELOG.md for details."
```

### Step 9: Create GitHub Repository

```bash
# Create on GitHub
gh repo create agent-knowledge --public --source=. --remote=origin

# Push
git push -u origin main
```

### Step 10: Update Dependent Projects

**Hopper:**
```bash
cd ~/Source/hopper
# Add as submodule or direct dependency
git submodule add https://github.com/user/agent-knowledge.git ../agent-knowledge
```

**Czarina:**
```bash
cd ~/Source/czarina
git submodule add https://github.com/user/agent-knowledge.git ../agent-knowledge
```

**The Symposium:**
```bash
cd ~/Source/thesymposium
git submodule add https://github.com/user/agent-knowledge.git ../agent-knowledge
```

**SARK:**
```bash
cd ~/Source/sark
git submodule add https://github.com/user/agent-knowledge.git ../agent-knowledge
```

## Content Harmonization

### Overlapping Topics

**Git Workflows:**
- `agent-rules/workflows/git-workflows.md` (general workflow)
- `agentic-dev-patterns/GIT_WORKFLOW_PATTERNS.md` (specific patterns)

**Resolution:**
- Keep general workflow in `core-rules/workflows/git-workflows.md`
- Keep specific patterns in `patterns/git-workflows/`
- Cross-reference both

**Testing:**
- `agent-rules/testing/` (standards and organization)
- `agentic-dev-patterns/TESTING_PATTERNS.md` (specific patterns)

**Resolution:**
- Keep standards in `core-rules/testing/`
- Keep patterns in `patterns/testing-patterns/`
- Cross-reference

### Unique Content

**From agent-rules only:**
- Python standards (keep in `core-rules/python-standards/`)
- Security patterns (keep in `core-rules/security/`)
- Templates (keep in `templates/`)

**From agentic-dev-patterns only:**
- Error recovery patterns (keep in `patterns/error-recovery/`)
- Tool use optimization (keep in `patterns/tool-use/`)
- Context management (keep in `patterns/context-management/`)

## Navigation Strategy

### Two Entry Points

**1. By Topic (INDEX.md)**
```markdown
# Agent Knowledge Index

## By Topic

### Python Development
- [Python Standards](./core-rules/python-standards/)
- [Testing](./core-rules/testing/)
- [Security](./core-rules/security/)

### Agent Development
- [Agent Roles](./core-rules/agent-roles/)
- [Mode Capabilities](./patterns/mode-capabilities/)
- [Orchestration](./core-rules/orchestration/)

### Development Patterns
- [Error Recovery](./patterns/error-recovery/)
- [Tool Use](./patterns/tool-use/)
- [Git Workflows](./patterns/git-workflows/)
```

**2. By Use Case (README.md)**
```markdown
# I want to...

## Set up a new project
→ [Templates](./templates/)

## Improve error handling
→ [Error Recovery Patterns](./patterns/error-recovery/)

## Optimize tool usage
→ [Tool Use Patterns](./patterns/tool-use/)

## Define agent roles
→ [Agent Roles](./core-rules/agent-roles/)
```

## Versioning Strategy

### Version Numbers

**Major version (2.0.0):**
- Breaking changes to structure
- Removed deprecated patterns
- Major reorganization

**Minor version (1.1.0):**
- New patterns added
- New rules added
- Significant enhancements

**Patch version (1.0.1):**
- Typo fixes
- Clarifications
- Cross-reference updates

### Changelog Format

```markdown
# Changelog

## [1.1.0] - 2025-02-15

### Added
- Error recovery pattern: Circuit breaker (#23)
- Tool use pattern: Adaptive batching (#24)
- Template: MCP server project (#25)

### Changed
- Enhanced git workflow patterns with rebase strategies (#26)

### Fixed
- Typo in architect role documentation (#27)

### Deprecated
- (none)

## [1.0.0] - 2025-01-01

### Added
- Initial merge of agent-rules and agentic-dev-patterns
- 53+ rules across 9 domains
- 6 pattern categories
- 13 project templates
```

## Success Metrics

### Quantitative

- [ ] All content from both repos migrated
- [ ] Zero broken internal links
- [ ] All 4 projects (Hopper, Czarina, Symposium, SARK) using agent-knowledge within 1 month
- [ ] 10+ new patterns added in first 3 months (via learnings processor)

### Qualitative

- [ ] Easy to navigate
- [ ] Clear cross-references
- [ ] Discoverable patterns
- [ ] Actionable guidance

## Timeline

**Week 1:**
- Create repository
- Migrate agent-rules content
- Migrate agentic-dev-patterns content
- Create README and navigation

**Week 2:**
- Harmonize overlapping content
- Create CONTRIBUTING.md
- Add cross-references
- Initial commit and push

**Week 3:**
- Update dependent projects
- Test integration with Hopper
- Test integration with Czarina
- Documentation review

**Week 4:**
- Polish navigation
- Add examples
- Learnings processor integration
- v1.0.0 release

---

**Next Steps:**
1. Review and approve this plan
2. Create agent-knowledge repository
3. Execute migration steps 1-10
4. Integrate with ecosystem projects
