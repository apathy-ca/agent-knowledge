#!/usr/bin/env python3
"""
Fixed link fixer that handles templates/ correctly.
"""
import os
import re
from pathlib import Path

def fix_file_links_v2(file_path):
    """Fix links in a single file - version 2."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix mangled templates paths like ../templates/../
    content = re.sub(r'\]\(\.\./templates/\.\./\)', r'](../templates/agent-project-template.md)', content)
    content = re.sub(r'\]\(\.\./templates/\.\./', r'](../templates/', content)

    # Fix patterns/INDEX.md references to non-existent files
    if 'patterns/INDEX.md' in str(file_path):
        # These files don't exist, use correct paths
        content = re.sub(r'\.\./(core-rules/workflows/recovery-workflow\.md)', r'error-recovery/README.md', content)
        content = re.sub(r'\.\./(core-rules/workflows/git-workflows\.md)', r'git-workflows/README.md', content)
        content = re.sub(r'\.\./(core-rules/python-standards/error-handling\.md)', r'../core-rules/python-standards/ERROR_HANDLING.md', content)
        content = re.sub(r'\.\./(core-rules/design-patterns/memory-patterns\.md)', r'context-management/memory-tiers.md', content)
        content = re.sub(r'\.\./(core-rules/orchestration/agent-handoffs\.md)', r'../core-rules/orchestration/ORCHESTRATION_PATTERNS.md', content)
        content = re.sub(r'\.\./(core-rules/testing/pytest-standards\.md)', r'testing-patterns/README.md', content)

    # Fix patterns/git-workflows/README.md
    if 'patterns/git-workflows/README.md' in str(file_path):
        content = re.sub(r'\.\./\.\./core-rules/workflows/git-workflows\.md', r'../../core-rules/workflows/GIT_WORKFLOW.md', content)

    # Fix patterns/testing-patterns/README.md
    if 'patterns/testing-patterns/README.md' in str(file_path):
        content = re.sub(r'\.\./\.\./core-rules/testing/pytest-standards\.md', r'../../core-rules/testing/UNIT_TESTING.md', content)

    # Fix patterns/context-management/README.md
    if 'patterns/context-management/README.md' in str(file_path):
        content = re.sub(r'\.\./\.\./core-rules/design-patterns/memory-patterns\.md', r'memory-tiers.md', content)
        content = re.sub(r'\.\./\.\./core-rules/orchestration/agent-handoffs\.md', r'../../core-rules/orchestration/ORCHESTRATION_PATTERNS.md', content)

    # Fix patterns/error-recovery/README.md
    if 'patterns/error-recovery/README.md' in str(file_path):
        content = re.sub(r'\.\./\.\./core-rules/python-standards/error-handling\.md', r'../../core-rules/python-standards/ERROR_HANDLING.md', content)
        content = re.sub(r'\.\./\.\./core-rules/workflows/recovery-workflow\.md', r'recovery-strategies.md', content)

    # Fix patterns/mode-capabilities/README.md
    if 'patterns/mode-capabilities/README.md' in str(file_path):
        content = re.sub(r'\.\./\.\./core-rules/agent-roles/code-role\.md', r'../../core-rules/agent-roles/CODE_ROLE.md', content)
        content = re.sub(r'\.\./\.\./core-rules/agent-roles/orchestrator-role\.md', r'../../core-rules/agent-roles/ORCHESTRATOR_ROLE.md', content)
        content = re.sub(r'\.\./\.\./core-rules/orchestration/orchestration-patterns\.md', r'../../core-rules/orchestration/ORCHESTRATION_PATTERNS.md', content)

    # Write back if changed
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')
    os.chdir(repo_root)

    # Find all markdown files
    md_files = []
    for md_file in repo_root.rglob('*.md'):
        if '.git' not in md_file.parts and '.czarina' not in md_file.parts:
            md_files.append(md_file)

    fixed_count = 0
    for md_file in sorted(md_files):
        if fix_file_links_v2(md_file):
            fixed_count += 1
            print(f"Fixed: {md_file.relative_to(repo_root)}")

    print(f"\n✅ Fixed links in {fixed_count} files")

if __name__ == "__main__":
    main()
