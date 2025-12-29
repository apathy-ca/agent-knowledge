#!/usr/bin/env python3
"""
Final comprehensive link fixer.
"""
import os
import re
from pathlib import Path

def fix_file_final(file_path):
    """Final link fixes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix templates references from core-rules/ subdirectories
    if str(file_path).startswith('/home/jhenry/Source/agent-knowledge/core-rules/') and \
       not str(file_path).endswith('/core-rules/INDEX.md') and \
       not str(file_path).endswith('/core-rules/README.md'):
        # In subdirectories of core-rules, templates are two levels up
        content = re.sub(r'\]\(\.\./(templates/[^)]+)\)', r'](../../templates/\1)', content)
        content = re.sub(r'\]\(\.\./\.\./\.\./templates/', r'](../../templates/', content)

    # Fix workflows references from core-rules/agent-roles
    if 'core-rules/agent-roles' in str(file_path):
        content = re.sub(r'\]\(\.\./\.\./workflows/', r'](../workflows/', content)

    # Remove external references to .czarina and plans
    content = re.sub(r'.*?\[.*?\]\(\.\./\.czarina/[^)]+\).*?\n?', '', content)
    content = re.sub(r'.*?\[.*?\]\(\.\./\.\./\.czarina/[^)]+\).*?\n?', '', content)
    content = re.sub(r'.*?\[.*?\]\(\.\./\.\./plans/[^)]+\).*?\n?', '', content)

    # For LEGACY files, remove broken migration guide references
    if 'LEGACY' in str(file_path):
        content = re.sub(r'.*?\[.*?\]\(\./MIGRATION_GUIDE\.md\).*?\n?', '', content)
        content = re.sub(r'.*?\[.*?\]\(\./CZARINA_ORCHESTRATION_CLOSEOUT\.md\).*?\n?', '', content)

    # For README_TEMPLATE.md, mark example links as examples
    if 'README_TEMPLATE.md' in str(file_path):
        # These are template examples, not real links
        content = re.sub(r'\]\(docs/([A-Z_a-z-]+\.md)\)', r'](docs/\1) <!-- example link -->', content)

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
        if fix_file_final(md_file):
            fixed_count += 1
            print(f"Fixed: {md_file.relative_to(repo_root)}")

    print(f"\n✅ Fixed links in {fixed_count} files")

if __name__ == "__main__":
    main()
