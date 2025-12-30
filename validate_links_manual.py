#!/usr/bin/env python3
"""
Manual link validation script for agent-knowledge repository.
Checks all internal markdown links and reports broken ones.
"""

import os
import re
from pathlib import Path
from typing import List, Tuple, Set

def find_markdown_files(root_dir: Path) -> List[Path]:
    """Find all markdown files in the repository."""
    md_files = []
    for md_file in root_dir.rglob('*.md'):
        # Skip .git and .czarina directories
        if '.git' in md_file.parts or '.czarina' in md_file.parts:
            continue
        md_files.append(md_file)
    return md_files

def extract_links(file_path: Path) -> List[Tuple[str, int]]:
    """Extract all markdown links from a file, excluding code blocks."""
    links = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            in_code_block = False
            for line_num, line in enumerate(f, 1):
                # Track code blocks
                if line.strip().startswith('```'):
                    in_code_block = not in_code_block
                    continue

                # Skip lines inside code blocks
                if in_code_block:
                    continue

                # Find markdown links: [text](path)
                # Must have text in brackets followed immediately by parentheses
                matches = re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', line)
                for match in matches:
                    link = match.group(2)
                    # Skip external links, anchors only, and mailto
                    if link.startswith(('http://', 'https://', 'mailto:', '#')):
                        continue
                    # Skip if link looks like a placeholder (e.g., [text](self))
                    # Valid links usually contain / or .md
                    if '/' not in link and not link.endswith('.md'):
                        continue
                    links.append((link, line_num))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return links

def resolve_link(source_file: Path, link: str) -> Path:
    """Resolve a relative link to an absolute path."""
    # Remove anchor if present
    link_path = link.split('#')[0]

    # Resolve relative to source file's directory
    source_dir = source_file.parent
    resolved = (source_dir / link_path).resolve()

    return resolved

def validate_links(root_dir: Path) -> Tuple[int, int, List[Tuple[Path, str, int, Path]]]:
    """Validate all links in markdown files."""
    md_files = find_markdown_files(root_dir)
    total_links = 0
    broken_links = []

    for md_file in md_files:
        links = extract_links(md_file)

        for link, line_num in links:
            total_links += 1

            # Skip wildcards
            if '*' in link:
                continue

            resolved = resolve_link(md_file, link)

            # Check if target exists
            if not resolved.exists():
                broken_links.append((md_file, link, line_num, resolved))

    return total_links, len(broken_links), broken_links

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("LINK VALIDATION REPORT")
    print("=" * 80)
    print()

    total_links, broken_count, broken_links = validate_links(repo_root)

    if broken_count == 0:
        print("✅ STATUS: PASS - Zero broken links")
        print()
        print(f"Total links checked: {total_links}")
        print(f"Broken links found: 0")
        print(f"Success rate: 100.0%")
        return 0

    # Group broken links by category
    doubled_templates = []
    template_examples = []
    worker_templates = []
    missing_orchestration = []
    cross_ref_examples = []
    other_missing = []

    for source, link, line_num, target in broken_links:
        link_lower = link.lower()

        if 'templates/templates' in link:
            doubled_templates.append((source, link, line_num, target))
        elif 'README_TEMPLATE.md' in str(source):
            template_examples.append((source, link, line_num, target))
        elif 'agent-roles' in str(source) and 'templates/worker' in link:
            worker_templates.append((source, link, line_num, target))
        elif any(x in link for x in ['WORKER_COORDINATION', 'DAEMON_AUTOMATION', 'STATUS_MONITORING']):
            missing_orchestration.append((source, link, line_num, target))
        elif 'cross-reference-map.md' in str(source):
            cross_ref_examples.append((source, link, line_num, target))
        else:
            other_missing.append((source, link, line_num, target))

    print("❌ STATUS: FAILED")
    print()
    print(f"Total links checked: {total_links}")
    print(f"Broken links found: {broken_count}")
    print(f"Success rate: {((total_links - broken_count) / total_links * 100):.1f}%")
    print()

    # Print categorized results
    print("BROKEN LINKS BY CATEGORY:")
    print()

    if doubled_templates:
        print(f"Category 1: Doubled Template Paths ({len(doubled_templates)} links)")
        print("-" * 80)
        for source, link, line_num, target in doubled_templates[:5]:
            print(f"  File: {source.relative_to(repo_root)}")
            print(f"  Line: {line_num}")
            print(f"  Link: {link}")
            print()
        if len(doubled_templates) > 5:
            print(f"  ... and {len(doubled_templates) - 5} more")
        print()

    if template_examples:
        print(f"Category 2: Template Example Links ({len(template_examples)} links)")
        print("-" * 80)
        for source, link, line_num, target in template_examples[:5]:
            print(f"  File: {source.relative_to(repo_root)}")
            print(f"  Line: {line_num}")
            print(f"  Link: {link}")
            print()
        if len(template_examples) > 5:
            print(f"  ... and {len(template_examples) - 5} more")
        print()

    if worker_templates:
        print(f"Category 3: Worker Template References ({len(worker_templates)} links)")
        print("-" * 80)
        for source, link, line_num, target in worker_templates[:5]:
            print(f"  File: {source.relative_to(repo_root)}")
            print(f"  Line: {line_num}")
            print(f"  Link: {link}")
            print()
        if len(worker_templates) > 5:
            print(f"  ... and {len(worker_templates) - 5} more")
        print()

    if missing_orchestration:
        print(f"Category 4: Missing Orchestration Files ({len(missing_orchestration)} links)")
        print("-" * 80)
        for source, link, line_num, target in missing_orchestration:
            print(f"  File: {source.relative_to(repo_root)}")
            print(f"  Line: {line_num}")
            print(f"  Link: {link}")
            print()

    if cross_ref_examples:
        print(f"Category 5: Cross-Reference Examples ({len(cross_ref_examples)} links)")
        print("-" * 80)
        for source, link, line_num, target in cross_ref_examples:
            print(f"  File: {source.relative_to(repo_root)}")
            print(f"  Line: {line_num}")
            print(f"  Link: {link}")
            print()

    if other_missing:
        print(f"Category 6: Other Missing Files ({len(other_missing)} links)")
        print("-" * 80)
        # Group by file
        by_file = {}
        for source, link, line_num, target in other_missing:
            file_key = source.relative_to(repo_root)
            if file_key not in by_file:
                by_file[file_key] = []
            by_file[file_key].append((link, line_num, target))

        for file_path, links in sorted(by_file.items()):
            print(f"  File: {file_path} ({len(links)} broken links)")
            for link, line_num, target in links[:3]:
                print(f"    Line {line_num}: {link}")
            if len(links) > 3:
                print(f"    ... and {len(links) - 3} more")
            print()
        print()

    return 1

if __name__ == '__main__':
    exit(main())
