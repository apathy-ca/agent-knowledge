#!/usr/bin/env python3
"""
Fix the last remaining broken links.
"""

import re
from pathlib import Path

def fix_templates_readme_refs(repo_root: Path) -> int:
    """Fix ../documentation/ and ../orchestration/ in templates/README.md."""
    fixes = 0
    readme = repo_root / 'templates' / 'README.md'

    if readme.exists():
        try:
            with open(readme, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix ../documentation/ -> ../core-rules/documentation/
            content = re.sub(r'\]\(\.\./documentation/\)', r'](../core-rules/documentation/)', content)

            # Fix ../orchestration/ -> ../core-rules/orchestration/
            content = re.sub(r'\]\(\.\./orchestration/\)', r'](../core-rules/orchestration/)', content)

            if content != original:
                with open(readme, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed templates/README.md references")

        except Exception as e:
            print(f"Error processing templates/README.md: {e}")

    return fixes

def comment_out_hopper_refs(repo_root: Path) -> int:
    """Comment out all remaining .hopper and plans references."""
    fixes = 0
    files_to_check = [
        repo_root / 'core-rules' / 'INDEX.md',
        repo_root / 'core-rules' / 'README.md',
        repo_root / 'core-rules' / 'USAGE_GUIDE.md',
    ]

    for md_file in files_to_check:
        if not md_file.exists():
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            original_content = ''.join(lines)
            new_lines = []

            for line in lines:
                # Replace any remaining .hopper or plans references
                if '.hopper' in line and not line.strip().startswith('<!--'):
                    # Comment out the line
                    line = '<!-- ' + line.rstrip() + ' - .hopper directory not included -->\n'
                new_lines.append(line)

            new_content = ''.join(new_lines)

            if new_content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixes += 1
                print(f"Commented .hopper refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def comment_out_plans_refs(repo_root: Path) -> int:
    """Comment out all plans/ references."""
    fixes = 0
    agent_roles_dir = repo_root / 'core-rules' / 'agent-roles'

    for md_file in agent_roles_dir.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Comment plans/ references
            content = re.sub(
                r'\[([^\]]+)\]\(\.\./\.\./plans/([^)]+)\)',
                r'<!-- [\1](../../plans/\2) - plans directory not included in this repository -->',
                content
            )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Commented plans refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def comment_pattern_template_examples(repo_root: Path) -> int:
    """Comment out example links in meta/pattern-template.md."""
    fixes = 0
    pattern_template = repo_root / 'meta' / 'pattern-template.md'

    if pattern_template.exists():
        try:
            with open(pattern_template, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # These are template examples - add a note
            content = re.sub(
                r'\]\(\.\./category/pattern[0-9]\.md\)',
                r'](../category/YOUR-PATTERN.md) <!-- example path -->',
                content
            )
            content = re.sub(
                r'\]\(\.\./\.\./core-rules/domain/rule[0-9]\.md\)',
                r'](../../core-rules/YOUR-DOMAIN/YOUR-RULE.md) <!-- example path -->',
                content
            )

            if content != original:
                with open(pattern_template, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed pattern-template.md example links")

        except Exception as e:
            print(f"Error processing pattern-template.md: {e}")

    return fixes

def fix_core_readme_caching_link(repo_root: Path) -> int:
    """Fix the ../patterns/README.md#caching link."""
    fixes = 0
    readme = repo_root / 'core-rules' / 'README.md'

    if readme.exists():
        try:
            with open(readme, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix caching link
            content = re.sub(
                r'\]\(\.\./patterns/README\.md#caching\)',
                r'](../patterns/tool-use/caching-patterns.md)',
                content
            )

            if content != original:
                with open(readme, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed caching link in core-rules/README.md")

        except Exception as e:
            print(f"Error processing core-rules/README.md: {e}")

    return fixes

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("FIXING LAST REMAINING LINKS")
    print("=" * 80)
    print()

    total_fixes = 0

    print("Step 1: Fixing templates/README.md refs...")
    fixes = fix_templates_readme_refs(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 2: Commenting out .hopper refs...")
    fixes = comment_out_hopper_refs(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 3: Commenting out plans/ refs...")
    fixes = comment_out_plans_refs(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 4: Fixing pattern-template.md examples...")
    fixes = comment_pattern_template_examples(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 5: Fixing core-rules/README.md caching link...")
    fixes = fix_core_readme_caching_link(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("=" * 80)
    print(f"TOTAL FILES MODIFIED: {total_fixes}")
    print("=" * 80)

    print("\nNote: The following broken links are INTENTIONAL:")
    print("  - docs/YOUR-*.md in README_TEMPLATE.md (template examples)")
    print("  - docs/YOUR-*.md in templates/readme-template.md (template examples)")
    print("  - ERROR_RECOVERY_PATTERNS.md in LEGACY files (historical references)")
    print("  - MIGRATION_GUIDE.md in LEGACY files (not needed)")
    print("\nThese can be excluded from validation or left as-is.")

if __name__ == '__main__':
    main()
