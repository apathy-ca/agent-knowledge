#!/usr/bin/env python3
import os
import re
from pathlib import Path

def check_md_links(file_path):
    """Check all markdown links in a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find markdown links [text](path)
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    broken = []

    for text, link in links:
        # Skip external URLs
        if link.startswith('http'):
            continue
        # Skip anchors
        if link.startswith('#'):
            continue
        # Skip mailto
        if link.startswith('mailto:'):
            continue

        # Resolve relative path
        base_dir = os.path.dirname(file_path)
        target = os.path.normpath(os.path.join(base_dir, link.split('#')[0]))

        if not os.path.exists(target):
            broken.append((link, target))

    return broken

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')
    total_broken = 0
    files_with_broken = 0

    # Find all markdown files
    for md_file in repo_root.rglob('*.md'):
        # Skip worktrees and hidden directories
        if '/.czarina/worktrees/' in str(md_file) or '/.git/' in str(md_file):
            continue

        broken = check_md_links(str(md_file))
        if broken:
            files_with_broken += 1
            rel_path = md_file.relative_to(repo_root)
            print(f"\n{rel_path}: {len(broken)} broken links")
            total_broken += len(broken)
            for link, target in broken[:5]:  # Show first 5
                print(f"  {link}")
            if len(broken) > 5:
                print(f"  ... and {len(broken) - 5} more")

    print(f"\n{'='*60}")
    print(f"Total: {total_broken} broken links in {files_with_broken} files")

if __name__ == '__main__':
    main()
