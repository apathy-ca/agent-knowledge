#!/usr/bin/env python3
"""
Fix incorrect relative paths that have too many ../ references.
"""

import re
from pathlib import Path

def fix_agent_roles_paths(repo_root: Path) -> int:
    """Fix paths in agent-roles/ that incorrectly use ../../."""
    fixes = 0
    agent_roles_dir = repo_root / 'core-rules' / 'agent-roles'

    for md_file in agent_roles_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Files in core-rules/agent-roles/ should use ../ to reference other core-rules/ subdirs
            # Not ../../

            # Fix ../../python-standards/ -> ../python-standards/
            content = re.sub(r'\]\(\.\./\.\./python-standards/', r'](../python-standards/', content)

            # Fix ../../testing/ -> ../testing/
            content = re.sub(r'\]\(\.\./\.\./testing/', r'](../testing/', content)

            # Fix ../../workflows/ -> ../workflows/
            content = re.sub(r'\]\(\.\./\.\./workflows/', r'](../workflows/', content)

            # Fix ../../design-patterns/ -> ../design-patterns/
            content = re.sub(r'\]\(\.\./\.\./design-patterns/', r'](../design-patterns/', content)

            # Fix ../../orchestration/ -> ../orchestration/
            content = re.sub(r'\]\(\.\./\.\./orchestration/', r'](../orchestration/', content)

            # Fix ../../documentation/ -> ../documentation/
            content = re.sub(r'\]\(\.\./\.\./documentation/', r'](../documentation/', content)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed relative paths in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_readme_patterns_reference(repo_root: Path) -> int:
    """Fix specific patterns/ references in README.md."""
    fixes = 0
    readme = repo_root / 'core-rules' / 'README.md'

    if readme.exists():
        try:
            with open(readme, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix patterns/TOOL_USE_PATTERNS.md -> ../patterns/tool-use/README.md
            content = re.sub(
                r'\]\(patterns/TOOL_USE_PATTERNS\.md\)',
                r'](../patterns/tool-use/README.md)',
                content
            )

            # Fix patterns/ERROR_RECOVERY.md -> ../patterns/error-recovery/README.md
            content = re.sub(
                r'\]\(patterns/ERROR_RECOVERY\.md\)',
                r'](../patterns/error-recovery/README.md)',
                content
            )

            if content != original:
                with open(readme, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed patterns references in README.md")

        except Exception as e:
            print(f"Error processing README.md: {e}")

    return fixes

def remove_missing_directory_references(repo_root: Path) -> int:
    """Remove or comment out references to directories that don't exist (.hopper, plans, etc)."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Replace references to .hopper/ with a comment
            content = re.sub(
                r'\[([^\]]+)\]\(\.\./\.hopper/([^)]+)\)',
                r'<!-- [\1](../.hopper/\2) - .hopper directory not included in this repository -->',
                content
            )

            # Replace references to plans/
            content = re.sub(
                r'\[([^\]]+)\]\(\.\./\.\./plans/([^)]+)\)',
                r'<!-- [\1](../../plans/\2) - plans directory not included in this repository -->',
                content
            )

            # Replace references to .czarina/README.md (not in repo, only worktrees)
            content = re.sub(
                r'\[([^\]]+)\]\(\.\./\.\./\.czarina/README\.md\)',
                r'<!-- [\1](../../.czarina/README.md) - internal orchestration directory -->',
                content
            )

            # Replace references to .czarina/archive/
            content = re.sub(
                r'\[([^\]]+)\]\(\.\./\.\./\.czarina/archive/\)',
                r'<!-- [\1](../../.czarina/archive/) - internal archive directory -->',
                content
            )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Removed missing dir refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_documentation_template_references(repo_root: Path) -> int:
    """Fix template references in core-rules/documentation/."""
    fixes = 0
    doc_dir = repo_root / 'core-rules' / 'documentation'

    for md_file in doc_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # From core-rules/documentation/ to templates/ is ../../templates/
            # Fix ../templates/ -> ../../templates/
            content = re.sub(r'\]\(\.\./templates/', r'](../../templates/', content)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed template refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_more_missing_refs(repo_root: Path) -> int:
    """Fix remaining missing directory references that weren't caught."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix patterns/CACHING_PATTERNS.md etc in README.md
            # These should be ../patterns/design-patterns/ or fixed appropriately
            content = re.sub(
                r'\]\(patterns/CACHING_PATTERNS\.md\)',
                r'](../patterns/README.md#caching)',
                content
            )
            content = re.sub(
                r'\]\(patterns/BATCH_OPERATIONS\.md\)',
                r'](../patterns/tool-use/batching-patterns.md)',
                content
            )
            content = re.sub(
                r'\]\(patterns/STREAMING_PATTERNS\.md\)',
                r'](../patterns/README.md#streaming)',
                content
            )

            # Fix .czarina/workers/ references
            content = re.sub(
                r'\[([^\]]+)\]\(\.\./\.\./\.czarina/workers/([^)]+)\)',
                r'<!-- [\1](../../.czarina/workers/\2) - internal worker definition -->',
                content
            )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed remaining refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("FIXING RELATIVE PATHS")
    print("=" * 80)
    print()

    total_fixes = 0

    print("Step 1: Fixing agent-roles/ relative paths...")
    fixes = fix_agent_roles_paths(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 2: Fixing README patterns references...")
    fixes = fix_readme_patterns_reference(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 3: Fixing documentation/ template references...")
    fixes = fix_documentation_template_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 4: Removing references to missing directories...")
    fixes = remove_missing_directory_references(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 5: Fixing remaining missing references...")
    fixes = fix_more_missing_refs(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("=" * 80)
    print(f"TOTAL FILES MODIFIED: {total_fixes}")
    print("=" * 80)

if __name__ == '__main__':
    main()
