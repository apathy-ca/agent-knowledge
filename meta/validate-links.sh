#!/bin/bash
# File: /home/jhenry/Source/agent-knowledge/meta/validate-links.sh

echo "Validating internal links..."
cd /home/jhenry/Source/agent-knowledge

broken_links=0
total_links=0

# Find all markdown files
while IFS= read -r file; do
    echo "Checking $file..."

    # Extract all relative markdown links
    grep -oE '\]\([^)]*\.md[^)]*\)' "$file" 2>/dev/null | sed 's/](\(.*\))/\1/' | while read -r link; do
        ((total_links++))

        # Remove any anchors (# fragments)
        link_path="${link%%#*}"

        # Convert relative link to absolute path
        dir=$(dirname "$file")
        target="$dir/$link_path"

        # Normalize path (resolve .. and .)
        if [ -e "$target" ]; then
            target=$(realpath "$target" 2>/dev/null)
        else
            target=$(realpath -m "$target" 2>/dev/null)
        fi

        # Check if file exists
        if [ ! -f "$target" ]; then
            echo "❌ Broken link in $file: $link -> $target"
            ((broken_links++))
        else
            echo "   ✓ Valid: $link"
        fi
    done
done < <(find . -name "*.md" -type f -not -path "./.git/*" -not -path "./.czarina/*")

echo ""
echo "========================================="
echo "Total links checked: $total_links"
echo "Broken links found: $broken_links"
echo "========================================="

if [ $broken_links -eq 0 ]; then
    echo "✅ All links valid!"
    exit 0
else
    echo "❌ Found $broken_links broken links"
    exit 1
fi
