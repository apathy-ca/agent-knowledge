#!/usr/bin/env python3
"""
Fix references from templates/ directory to core-rules/.
"""

import re
from pathlib import Path

def fix_templates_directory_refs(repo_root: Path) -> int:
    """Fix references in templates/ to core-rules/ subdirectories."""
    fixes = 0
    templates_dir = repo_root / 'templates'

    for md_file in templates_dir.rglob('*.md'):
        # Skip subdirectories that are project templates
        if md_file.parent != templates_dir:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # From templates/ to core-rules/python-standards/ is ../core-rules/python-standards/
            content = re.sub(r'\]\(\.\./python-standards/', r'](../core-rules/python-standards/', content)

            # From templates/ to core-rules/testing/ is ../core-rules/testing/
            content = re.sub(r'\]\(\.\./testing/', r'](../core-rules/testing/', content)

            # From templates/ to core-rules/workflows/ is ../core-rules/workflows/
            content = re.sub(r'\]\(\.\./workflows/', r'](../core-rules/workflows/', content)

            # From templates/ to core-rules/agent-roles/ is ../core-rules/agent-roles/
            content = re.sub(r'\]\(\.\./agent-roles/', r'](../core-rules/agent-roles/', content)

            # From templates/ to core-rules/security/ is ../core-rules/security/
            content = re.sub(r'\]\(\.\./security/', r'](../core-rules/security/', content)

            # From templates/ to patterns/ is ../patterns/
            # This is already correct, no change needed

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("FIXING TEMPLATES DIRECTORY REFERENCES")
    print("=" * 80)
    print()

    total_fixes = 0

    print("Fixing templates/ directory references to core-rules/...")
    fixes = fix_templates_directory_refs(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("=" * 80)
    print(f"TOTAL FILES MODIFIED: {total_fixes}")
    print("=" * 80)

if __name__ == '__main__':
    main()
