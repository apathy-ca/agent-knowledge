#!/usr/bin/env python3
"""
Clean up nested HTML comments and remaining broken references.
"""

import re
from pathlib import Path

def cleanup_nested_comments(repo_root: Path) -> int:
    """Remove nested HTML comments and clean up broken link references."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            original = ''.join(lines)
            modified = False

            new_lines = []
            for line in lines:
                original_line = line

                # Remove links from within HTML comments
                # Pattern: <!-- text [link](url) more text -->
                if '<!--' in line and '[' in line and '](' in line and '-->' in line:
                    # Remove markdown links within comments
                    line = re.sub(r'(<!--[^>]*)\[([^\]]+)\]\(([^)]+)\)([^>]*-->)', r'\1\2\4', line)

                # Fix nested comments like <!-- <!-- --> -->
                line = re.sub(r'<!-- <!-- ([^>]+) --> ([^>]+) -->', r'<!-- \1 \2 -->', line)

                # Remove dangling link references in comments
                # Convert "Read [link](url) - note" in comments to "Read link - note"
                if '<!--' in line:
                    line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)

                if line != original_line:
                    modified = True

                new_lines.append(line)

            if modified:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                fixes += 1
                print(f"Cleaned up: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("CLEANING UP NESTED COMMENTS")
    print("=" * 80)
    print()

    total_fixes = cleanup_nested_comments(repo_root)

    print()
    print("=" * 80)
    print(f"TOTAL FILES MODIFIED: {total_fixes}")
    print("=" * 80)

if __name__ == '__main__':
    main()
