# Worker: repo-setup

## Mission
Create the foundational repository structure for the unified agent-knowledge repository, including directory scaffolding, git initialization, and basic configuration files.

## Deliverables
- New repository initialized with git
- Core directory structure created (core-rules/, patterns/, templates/, examples/, meta/)
- LICENSE file created (MIT)
- Basic .gitignore configured

## Context
This is the first worker in the agent-knowledge merge project. You are setting up the foundation that all other workers will build upon. The repository will merge content from two existing repositories:
- agent-rules (53+ rules, 9 domains)
- agentic-dev-patterns (proven patterns from The Symposium)

## References
- Implementation Plan: `/home/jhenry/Source/agent-knowledge/AGENT_KNOWLEDGE_MERGE_PLAN.md` (lines 143-290 for structure)
- Source Repository 1: `/home/jhenry/Source/agent-rules`
- Source Repository 2: `/home/jhenry/Source/agentic-dev-patterns`

## Task Breakdown

### Task 1: Initialize Git Repository
```bash
cd /home/jhenry/Source/agent-knowledge
git init
git branch -M main
```

**Acceptance Criteria:**
- `.git` directory exists
- Default branch is `main`
- Git repository is ready for commits

### Task 2: Create Directory Structure
Create the following directory structure:
```
agent-knowledge/
├── core-rules/
│   ├── python-standards/
│   ├── agent-roles/
│   ├── workflows/
│   ├── design-patterns/
│   ├── testing/
│   ├── security/
│   ├── documentation/
│   └── orchestration/
├── patterns/
│   ├── error-recovery/
│   ├── tool-use/
│   ├── mode-capabilities/
│   ├── context-management/
│   └── git-workflows/
├── templates/
│   ├── project-init/
│   ├── python-service/
│   ├── fastapi-api/
│   ├── cli-tool/
│   ├── library/
│   └── agent-project/
├── examples/
│   ├── hopper/
│   ├── czarina/
│   ├── thesymposium/
│   └── sark/
└── meta/
```

**Acceptance Criteria:**
- All directories created
- Directory structure matches specification in plan (lines 143-290)
- Directories are empty and ready for content

### Task 3: Create LICENSE File
Create an MIT License file with the following:
- Copyright year: 2025
- Copyright holder: "Agent Knowledge Contributors"

**Acceptance Criteria:**
- `LICENSE` file exists at repository root
- Contains valid MIT license text
- Copyright information is correct

### Task 4: Create .gitignore
Create a `.gitignore` file with common exclusions:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
*.egg-info/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Czarina
.czarina/state/
.czarina/logs/

# Testing
.pytest_cache/
.coverage
htmlcov/

# Build
dist/
build/
```

**Acceptance Criteria:**
- `.gitignore` file exists at repository root
- Contains appropriate exclusions
- Covers Python, IDEs, OS files, and Czarina state

### Task 5: Create Initial Commit
```bash
git add .
git commit -m "Initial commit: Repository foundation

- Initialized git repository
- Created directory structure for core-rules, patterns, templates, examples, and meta
- Added MIT LICENSE
- Added .gitignore

Part of agent-knowledge merge project (czarina phase 1)"
```

**Acceptance Criteria:**
- Initial commit exists
- Commit message follows conventions
- All foundation files are committed

## Success Criteria
- [ ] Git repository initialized with main branch
- [ ] Complete directory structure created matching specification
- [ ] MIT LICENSE file present
- [ ] Comprehensive .gitignore configured
- [ ] Initial commit completed
- [ ] Repository ready for content migration

## Notes
- This worker has no dependencies and can start immediately
- Follow the exact directory structure from the plan document
- Do not create any content files yet - only the structure
- Ensure all paths are absolute references from /home/jhenry/Source/agent-knowledge
