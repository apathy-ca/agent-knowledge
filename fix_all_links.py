#!/usr/bin/env python3
"""
Comprehensive link fixer for agent-knowledge repository.
Fixes common broken link patterns.
"""
import os
import re
from pathlib import Path

def fix_file_links(file_path):
    """Fix links in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix python/ -> python-standards/
    content = re.sub(r'\]\((\.\./)*python/', r'](\1python-standards/', content)

    # Fix agents/ -> agent-roles/
    content = re.sub(r'\]\((\.\./)*agents/', r'](\1agent-roles/', content)

    # Fix core-rules/patterns/ -> design-patterns/ (when in core-rules/)
    if 'core-rules' in str(file_path):
        content = re.sub(r'\]\(\.\./(patterns/[^)]+)\)', r'](.././patterns/\1)', content)
        content = re.sub(r'\]\((patterns/[^)]+)\)', r'](design-patterns/\1)', content)

    # Fix core-rules/templates/ -> ../templates/ (when in core-rules/)
    if 'core-rules' in str(file_path):
        content = re.sub(r'\]\((\.\./)*(templates/[^)]+)\)', r'](../../templates/\1)', content)
        # Simplify multiple ../
        content = re.sub(r'\]\((\.\./)+\.\./(templates/)', r'](../\2', content)

    # Remove external .hopper references
    content = re.sub(r'- Read \[.*?\]\(\.\./\.hopper/.*?\).*?\n', '', content)
    content = re.sub(r'- Check \[.*?\]\(\.\./\.hopper/.*?\).*?\n', '', content)
    content = re.sub(r'\[.*?\]\(\.\.?/\.hopper/[^)]+\)', '[external reference removed]', content)

    # Remove external .czarina references
    content = re.sub(r'\[.*?\]\(\.\.?/\.czarina/[^)]+\)', '[external reference removed]', content)

    # Remove external plans/ references
    content = re.sub(r'\[.*?\]\(\.\.?/plans/[^)]+\)', '[external reference removed]', content)

    # Remove LEGACY file broken references
    if 'LEGACY' in str(file_path):
        # These are archive files, just remove the broken links
        content = re.sub(r'\[([^\]]+)\]\([A-Z_]+\.md\)', r'\1 (archived)', content)

    # Remove AGENT_KNOWLEDGE_MERGE_PLAN broken references
    if 'AGENT_KNOWLEDGE_MERGE_PLAN' in str(file_path):
        content = re.sub(r'\[([^\]]+)\]\(\./(docs|templates)/[^)]+\)', r'\1 (reference removed)', content)
        content = re.sub(r'\[([^\]]+)\]\(\.\./\.\./[^)]+\)', r'\1 (reference removed)', content)

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
        if fix_file_links(md_file):
            fixed_count += 1
            print(f"Fixed: {md_file.relative_to(repo_root)}")

    print(f"\n✅ Fixed links in {fixed_count} files")

if __name__ == "__main__":
    main()
