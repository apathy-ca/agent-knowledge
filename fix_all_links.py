#!/usr/bin/env python3
"""Fix all broken internal links in markdown files."""
import os
import re
from pathlib import Path

def fix_links_in_file(file_path):
    """Fix all broken links in a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern replacements - order matters!
    replacements = [
        # Fix paths that should point to core-rules
        (r'\(\.\./python/', '(../core-rules/python-standards/'),
        (r'\(\./python/', '(./python-standards/'),
        (r'\(python/', '(python-standards/'),

        (r'\(\.\./agents/', '(../core-rules/agent-roles/'),
        (r'\(\./agents/', '(./agent-roles/'),
        (r'\(agents/', '(agent-roles/'),

        (r'\(\.\./patterns/([A-Z])', r'(../core-rules/design-patterns/\1'),
        (r'\(\./patterns/([A-Z])', r'(./design-patterns/\1'),
        (r'\(patterns/([A-Z])', r'(design-patterns/\1'),

        (r'\(\.\./workflows/', '(../core-rules/workflows/'),
        (r'\(workflows/', '(workflows/'),

        (r'\(\.\./testing/', '(../core-rules/testing/'),
        (r'\(testing/', '(testing/'),

        (r'\(\.\./security/', '(../core-rules/security/'),
        (r'\(security/', '(security/'),

        (r'\(\.\./orchestration/', '(../core-rules/orchestration/'),
        (r'\(orchestration/', '(orchestration/'),

        (r'\(\.\./documentation/', '(../core-rules/documentation/'),
        (r'\(documentation/', '(documentation/'),

        # Fix templates references
        (r'\(templates/', '(../templates/'),
        (r'\(\./templates/', '(../templates/'),

        # Remove .hopper references
        (r'- .*\.\.\/\.hopper\/.*\n', ''),
        (r'\[.*\]\(\.\.\/\.hopper\/.*\)', ''),
    ]

    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    # Write back if changed
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')
    fixed_count = 0

    # Process all markdown files in core-rules
    for md_file in repo_root.glob('core-rules/**/*.md'):
        if fix_links_in_file(str(md_file)):
            print(f"Fixed: {md_file.relative_to(repo_root)}")
            fixed_count += 1

    # Also process patterns and templates
    for directory in ['patterns', 'templates']:
        for md_file in (repo_root / directory).glob('**/*.md'):
            if fix_links_in_file(str(md_file)):
                print(f"Fixed: {md_file.relative_to(repo_root)}")
                fixed_count += 1

    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
