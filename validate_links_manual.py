#!/usr/bin/env python3
import os
import re
from pathlib import Path

def find_md_links(file_path):
    """Extract markdown links from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all markdown links: [text](path)
    pattern = r'\]\(([^)]*\.md[^)]*)\)'
    return re.findall(pattern, content)

def check_link(source_file, link):
    """Check if a relative markdown link exists."""
    # Remove anchor
    link_path = link.split('#')[0]

    # Resolve relative path
    source_dir = Path(source_file).parent
    target_path = (source_dir / link_path).resolve()

    return target_path.exists(), str(target_path)

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')
    os.chdir(repo_root)

    # Find all markdown files (excluding .git and .czarina)
    md_files = []
    for md_file in repo_root.rglob('*.md'):
        if '.git' not in md_file.parts and '.czarina' not in md_file.parts:
            md_files.append(md_file)

    total_links = 0
    broken_links = 0
    broken_details = []

    for md_file in sorted(md_files):
        relative_path = md_file.relative_to(repo_root)
        links = find_md_links(md_file)

        for link in links:
            total_links += 1
            exists, target = check_link(md_file, link)

            if not exists:
                broken_links += 1
                broken_details.append(f"  ❌ {relative_path}: {link} -> {target}")

    # Print summary
    print("=" * 60)
    print("LINK VALIDATION REPORT")
    print("=" * 60)
    print(f"Total markdown files checked: {len(md_files)}")
    print(f"Total links checked: {total_links}")
    print(f"Broken links found: {broken_links}")
    print(f"Success rate: {((total_links - broken_links) / total_links * 100):.1f}%")
    print("=" * 60)

    if broken_links > 0:
        print(f"\n❌ VALIDATION FAILED - {broken_links} broken links:")
        for detail in broken_details[:50]:  # Show first 50
            print(detail)
        if len(broken_details) > 50:
            print(f"\n... and {len(broken_details) - 50} more broken links")
        print("\n" + "=" * 60)
        print(f"STATUS: ❌ FAIL - {broken_links} broken links")
        print("=" * 60)
    else:
        print("\n✅ ALL LINKS VALID!")
        print("=" * 60)
        print("STATUS: ✅ PASS - Zero broken links")
        print("=" * 60)

if __name__ == "__main__":
    main()
