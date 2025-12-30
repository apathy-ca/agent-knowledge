#!/usr/bin/env python3
"""
Final link fixes for remaining broken links.
"""

import re
from pathlib import Path

def fix_readme_template_docs_links(repo_root: Path) -> int:
    """Fix docs/ links in README_TEMPLATE.md - these are examples, not real links."""
    fixes = 0
    readme_template = repo_root / 'core-rules' / 'documentation' / 'README_TEMPLATE.md'

    if readme_template.exists():
        try:
            with open(readme_template, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # These are example links showing what users SHOULD create
            # Change them to be more clearly placeholders
            content = re.sub(
                r'See \[API Documentation\]\(docs/API\.md\)',
                r'See [API Documentation](docs/YOUR-API-DOCS.md)',
                content
            )
            content = re.sub(
                r'See \[Deployment Guide\]\(docs/DEPLOYMENT\.md\)',
                r'See [Deployment Guide](docs/YOUR-DEPLOYMENT-GUIDE.md)',
                content
            )
            content = re.sub(
                r'See \[Commands Reference\]\(docs/COMMANDS\.md\)',
                r'See [Commands Reference](docs/YOUR-COMMANDS-REFERENCE.md)',
                content
            )
            content = re.sub(
                r'See \[Architecture Documentation\]\(docs/ARCHITECTURE\.md\)',
                r'See [Architecture Documentation](docs/YOUR-ARCHITECTURE-DOCS.md)',
                content
            )
            content = re.sub(
                r'\[Getting Started\]\(docs/getting-started\.md\)',
                r'[Getting Started](docs/YOUR-GETTING-STARTED.md)',
                content
            )
            content = re.sub(
                r'\[User Guide\]\(docs/guide\.md\)',
                r'[User Guide](docs/YOUR-USER-GUIDE.md)',
                content
            )
            content = re.sub(
                r'\[API Reference\]\(docs/API\.md\)',
                r'[API Reference](docs/YOUR-API-REFERENCE.md)',
                content
            )
            content = re.sub(
                r'\[Architecture\]\(docs/ARCHITECTURE\.md\)',
                r'[Architecture](docs/YOUR-ARCHITECTURE.md)',
                content
            )
            content = re.sub(
                r'\[Contributing\]\(docs/CONTRIBUTING\.md\)',
                r'[Contributing](CONTRIBUTING.md)',
                content
            )

            if content != original:
                with open(readme_template, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed docs/ example links in README_TEMPLATE.md")

        except Exception as e:
            print(f"Error processing README_TEMPLATE.md: {e}")

    return fixes

def fix_template_readme_links(repo_root: Path) -> int:
    """Fix docs/ links in templates/readme-template.md."""
    fixes = 0
    readme_template = repo_root / 'templates' / 'readme-template.md'

    if readme_template.exists():
        try:
            with open(readme_template, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Similar fixes for the templates directory version
            content = re.sub(
                r'\]\(docs/getting-started\.md\)',
                r'](docs/YOUR-GETTING-STARTED.md)',
                content
            )
            content = re.sub(
                r'\]\(docs/API\.md\)',
                r'](docs/YOUR-API-DOCS.md)',
                content
            )
            content = re.sub(
                r'\]\(docs/ARCHITECTURE\.md\)',
                r'](docs/YOUR-ARCHITECTURE.md)',
                content
            )
            content = re.sub(
                r'\]\(docs/CONTRIBUTING\.md\)',
                r'](CONTRIBUTING.md)',
                content
            )

            if content != original:
                with open(readme_template, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed docs/ example links in templates/readme-template.md")

        except Exception as e:
            print(f"Error processing templates/readme-template.md: {e}")

    return fixes

def fix_double_comments(repo_root: Path) -> int:
    """Fix double-commented links."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Fix double HTML comments
            content = re.sub(
                r'<!-- <!-- \[([^\]]+)\]\(([^)]+)\) - ([^-]+) --> - \3 -->',
                r'<!-- [\1](\2) - \3 -->',
                content
            )

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed double comments in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_remaining_hopper_refs(repo_root: Path) -> int:
    """Fix remaining .hopper references that weren't commented."""
    fixes = 0
    md_files = list(repo_root.rglob('*.md'))

    for md_file in md_files:
        if '.czarina' in md_file.parts or '.git' in md_file.parts:
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            original = content

            # Don't re-comment already commented links
            # Only comment links that are still active
            lines = content.split('\n')
            new_lines = []
            for line in lines:
                # Skip if already in HTML comment
                if '<!-- [' in line and '.hopper' in line:
                    new_lines.append(line)
                    continue

                # Comment active .hopper links
                line = re.sub(
                    r'\[([^\]]+)\]\(\.\./(\.hopper[^)]*)\)',
                    r'<!-- [\1](../\2) - .hopper directory not included in this repository -->',
                    line
                )
                new_lines.append(line)

            content = '\n'.join(new_lines)

            if content != original:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixes += 1
                print(f"Fixed remaining .hopper refs in: {md_file.relative_to(repo_root)}")

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return fixes

def fix_patterns_readme_anchors(repo_root: Path) -> int:
    """Fix broken anchor links to patterns README."""
    fixes = 0

    # Check if ../patterns/README.md has a #caching section
    patterns_readme = repo_root / 'patterns' / 'README.md'
    if patterns_readme.exists():
        with open(patterns_readme, 'r', encoding='utf-8') as f:
            patterns_content = f.read()

        # If there's no #caching anchor, we should link to the actual files
        if '#caching' not in patterns_content.lower() and '## caching' not in patterns_content.lower():
            # Fix the links to point to actual pattern files
            md_files = list(repo_root.rglob('*.md'))

            for md_file in md_files:
                if '.czarina' in md_file.parts or '.git' in md_file.parts:
                    continue

                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    original = content

                    # Fix the caching link - there's no caching in patterns/, so comment it out
                    content = re.sub(
                        r'\]\(\.\./patterns/README\.md#caching\)',
                        r'](../patterns/tool-use/caching-patterns.md)',
                        content
                    )

                    # Fix streaming similarly
                    content = re.sub(
                        r'\]\(\.\./patterns/README\.md#streaming\)',
                        r'](../patterns/README.md) <!-- Note: streaming patterns not yet documented -->',
                        content
                    )

                    if content != original:
                        with open(md_file, 'w', encoding='utf-8') as f:
                            f.write(content)
                        fixes += 1
                        print(f"Fixed patterns anchor refs in: {md_file.relative_to(repo_root)}")

                except Exception as e:
                    print(f"Error processing {md_file}: {e}")

    return fixes

def main():
    repo_root = Path('/home/jhenry/Source/agent-knowledge')

    print("=" * 80)
    print("FINAL LINK FIXES")
    print("=" * 80)
    print()

    total_fixes = 0

    print("Step 1: Fixing README_TEMPLATE.md docs/ example links...")
    fixes = fix_readme_template_docs_links(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 2: Fixing templates/readme-template.md docs/ links...")
    fixes = fix_template_readme_links(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 3: Fixing double HTML comments...")
    fixes = fix_double_comments(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 4: Fixing remaining .hopper references...")
    fixes = fix_remaining_hopper_refs(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("Step 5: Fixing patterns README anchor links...")
    fixes = fix_patterns_readme_anchors(repo_root)
    total_fixes += fixes
    print(f"  Fixed {fixes} files\n")

    print("=" * 80)
    print(f"TOTAL FILES MODIFIED: {total_fixes}")
    print("=" * 80)

if __name__ == '__main__':
    main()
