#!/usr/bin/env python3
"""
Comprehensive link fixer for agent-knowledge repository.
Fixes all 210 broken links systematically.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def fix_python_directory_references(repo_root: Path) -> int:
    """Fix references from python/ to python-standards/."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        # Skip .czarina and .git directories
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix python/ references to python-standards/
            # Pattern 1: ../python/ -> ../python-standards/
            content = re.sub(r'\]\(\.\./python/', r'](../python-standards/', content)
            # Pattern 2: ../../python/ -> ../../python-standards/
            content = re.sub(r'\]\(\.\./\.\./python/', r'](../../python-standards/', content)
            # Pattern 3: ./python/ -> ./python-standards/
            content = re.sub(r'\]\(\./python/', r'](./python-standards/', content)
            # Pattern 4: python/ (no prefix) -> python-standards/
            content = re.sub(r'\]\(python/', r'](python-standards/', content)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed python/ refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_template_directory_references(repo_root: Path) -> int:
    """Fix template references that point to wrong locations."""
    fixes = 0

    # Files in core-rules/agent-roles/ that reference ./templates/
    # should reference ../../templates/
    agent_roles_dir = repo_root / 'core-rules' / 'agent-roles'

    for md_file in agent_roles_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix ./templates/ -> ../../templates/
            content = re.sub(r'\]\(\./templates/', r'](../../templates/', content)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed template refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    # Also fix in orchestration files
    orch_dir = repo_root / 'core-rules' / 'orchestration'
    for md_file in orch_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix ../templates/worker-* which should be ../../templates/worker-*
            content = re.sub(r'\]\(\.\./templates/worker-', r'](../../templates/worker-', content)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed template refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_testing_directory_references(repo_root: Path) -> int:
    """Fix testing/ references - need to check if they should be testing/ or workflows/."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    # First, check what testing files exist
    testing_dir = repo_root / 'core-rules' / 'testing'
    testing_files = {f.name for f in testing_dir.glob('*.md')} if testing_dir.exists() else set()

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix references to testing files that don't exist
            # MOCKING_STRATEGIES.md doesn't exist, remove or comment these references
            content = re.sub(
                r'\]\(\.\./testing/MOCKING_STRATEGIES\.md\)',
                r'](../testing/README.md#mocking)',
                content
            )
            content = re.sub(
                r'\]\(\.\./\.\./testing/MOCKING_STRATEGIES\.md\)',
                r'](../../testing/README.md#mocking)',
                content
            )

            # TESTING_POLICY.md might need to be TESTING_STANDARDS.md or similar
            if (repo_root / 'core-rules' / 'testing' / 'TESTING_POLICY.md').exists():
                # File exists, fix path
                pass  # Path is correct
            else:
                # Replace with README or main testing doc
                content = re.sub(
                    r'\]\(\.\./testing/TESTING_POLICY\.md\)',
                    r'](../testing/README.md)',
                    content
                )
                content = re.sub(
                    r'\]\(\.\./\.\./testing/TESTING_POLICY\.md\)',
                    r'](../../testing/README.md)',
                    content
                )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed testing refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_agents_directory_references(repo_root: Path) -> int:
    """Fix agents/ references - should be agent-roles/."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix agents/ -> agent-roles/
            content = re.sub(r'\]\(\.\./agents/', r'](../agent-roles/', content)
            content = re.sub(r'\]\(\.\./\.\./agents/', r'](../../agent-roles/', content)
            content = re.sub(r'\]\(\./agents/', r'](./agent-roles/', content)
            content = re.sub(r'\]\(agents/', r'](agent-roles/', content)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed agents/ refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_orchestration_file_references(repo_root: Path) -> int:
    """Fix references to missing orchestration files."""
    fixes = 0
    orch_patterns = repo_root / 'core-rules' / 'orchestration' / 'ORCHESTRATION_PATTERNS.md'

    if orch_patterns.exists():
        try:
            with open(orch_patterns, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Replace references to missing files with anchors in current file
            content = re.sub(
                r'\]\(\./WORKER_COORDINATION\.md\)',
                r'](#worker-coordination)',
                content
            )
            content = re.sub(
                r'\]\(\./DAEMON_AUTOMATION\.md\)',
                r'](#daemon-patterns)',
                content
            )
            content = re.sub(
                r'\]\(\./STATUS_MONITORING\.md\)',
                r'](#status-monitoring)',
                content
            )

            if content != original:
                with open(orch_patterns, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed orchestration file refs in ORCHESTRATION_PATTERNS.md")

        except Exception as e:
            print(f"Error processing orchestration patterns: {e}")

    return fixes

def fix_patterns_directory_references(repo_root: Path) -> int:
    """Fix references to old pattern file names."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix old pattern references
            content = re.sub(
                r'\]\(\.\./patterns/TOOL_USE_PATTERNS\.md\)',
                r'](../patterns/tool-use/README.md)',
                content
            )
            content = re.sub(
                r'\]\(\.\./patterns/ERROR_RECOVERY\.md\)',
                r'](../patterns/error-recovery/README.md)',
                content
            )
            content = re.sub(
                r'\]\(\.\./\.\./patterns/TOOL_USE_PATTERNS\.md\)',
                r'](../../patterns/tool-use/README.md)',
                content
            )
            content = re.sub(
                r'\]\(\.\./\.\./patterns/ERROR_RECOVERY\.md\)',
                r'](../../patterns/error-recovery/README.md)',
                content
            )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed pattern refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_security_directory_references(repo_root: Path) -> int:
    """Fix security/ references."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix ../security/ to point to README or main file
            content = re.sub(
                r'\]\(\.\./security/\)',
                r'](../security/README.md)',
                content
            )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed security refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_index_and_readme_references(repo_root: Path) -> int:
    """Fix core-rules/INDEX.md and README.md references to old structure."""
    fixes = 0

    # Fix INDEX.md
    index_file = repo_root / 'core-rules' / 'INDEX.md'
    if index_file.exists():
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix patterns/ references to design-patterns/
            content = re.sub(r'\]\(patterns/TOOL_USE_PATTERNS\.md\)', r'](design-patterns/TOOL_USE_PATTERNS.md)', content)
            content = re.sub(r'\]\(patterns/STREAMING_PATTERNS\.md\)', r'](design-patterns/STREAMING_PATTERNS.md)', content)
            content = re.sub(r'\]\(patterns/CACHING_PATTERNS\.md\)', r'](design-patterns/CACHING_PATTERNS.md)', content)
            content = re.sub(r'\]\(patterns/BATCH_OPERATIONS\.md\)', r'](design-patterns/BATCH_OPERATIONS.md)', content)
            content = re.sub(r'\]\(patterns/ERROR_RECOVERY\.md\)', r'](design-patterns/ERROR_RECOVERY.md)', content)

            # Fix testing/ references
            content = re.sub(r'\]\(testing/TESTING_POLICY\.md\)', r'](testing/README.md)', content)
            content = re.sub(r'\]\(testing/UNIT_TESTING\.md\)', r'](testing/UNIT_TESTING.md)', content)
            content = re.sub(r'\]\(testing/INTEGRATION_TESTING\.md\)', r'](testing/INTEGRATION_TESTING.md)', content)
            content = re.sub(r'\]\(testing/MOCKING_STRATEGIES\.md\)', r'](testing/README.md#mocking)', content)
            content = re.sub(r'\]\(testing/COVERAGE_REQUIREMENTS\.md\)', r'](testing/README.md#coverage)', content)

            # Fix templates/ references in agent-roles section
            content = re.sub(r'\]\(agent-roles/templates/', r'](../templates/', content)

            # Fix templates/ references that should be ../templates/ (INDEX.md is in core-rules/)
            content = re.sub(r'\]\(templates/', r'](../templates/', content)

            if content != original:
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed INDEX.md references")

        except Exception as e:
            print(f"Error processing INDEX.md: {e}")

    # Fix README.md
    readme_file = repo_root / 'core-rules' / 'README.md'
    if readme_file.exists():
        try:
            with open(readme_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix templates/ references
            content = re.sub(r'\]\(templates/', r'](../templates/', content)

            # Fix patterns/ references to ../patterns/
            content = re.sub(r'\]\(patterns/\)', r'](../patterns/)', content)

            # Fix agent-roles/templates/ to ../templates/
            content = re.sub(r'\]\(agent-roles/templates/', r'](../templates/', content)

            # Fix documentation/ references
            content = re.sub(r'\]\(documentation/', r'](./documentation/', content)

            if content != original:
                with open(readme_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed README.md references")

        except Exception as e:
            print(f"Error processing README.md: {e}")

    return fixes

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("FIXING ALL BROKEN LINKS")
    print("=" * 80)
    print()

    total_fixes = 0

    print("Step 1: Fixing python/ -> python-standards/ references...")
    fixes = fix_python_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 2: Fixing agents/ -> agent-roles/ references...")
    fixes = fix_agents_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 3: Fixing template directory references...")
    fixes = fix_template_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 4: Fixing testing directory references...")
    fixes = fix_testing_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 5: Fixing orchestration file references...")
    fixes = fix_orchestration_file_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 6: Fixing pattern directory references...")
    fixes = fix_patterns_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 7: Fixing security directory references...")
    fixes = fix_security_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 8: Fixing INDEX.md and README.md references...")
    fixes = fix_index_and_readme_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("=" * 80)
    print(f"TOTAL FILES MODIFIED: {total_fixes}")
    print("=" * 80)
    print()
    print("Now run validation to check remaining broken links:")
    print("  python3 validate_links_manual.py")

if __name__ == '__main__':
    main()
