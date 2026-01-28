#!/bin/bash
# File: /home/jhenry/Source/agent-knowledge/meta/validate-links.sh

echo "Validating internal links..."
cd /home/jhenry/Source/agent-knowledge

broken_links_file=$(mktemp)
total_links_file=$(mktemp)
echo "0" > "$broken_links_file"
echo "0" > "$total_links_file"

# Find all markdown files
find . -name "*.md" -type f -not -path "./.git/*" -not -path "./.czarina/*" | while IFS= read -r file; do
    echo "Checking $file..."

    # Extract all relative markdown links
    grep -oE '\]\([^)]*\.md[^)]*\)' "$file" 2>/dev/null | sed 's/](\(.*\))/\1/' | while read -r link; do
        total=$(cat "$total_links_file")
        echo $((total + 1)) > "$total_links_file"

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
            broken=$(cat "$broken_links_file")
            echo $((broken + 1)) > "$broken_links_file"
        else
            echo "   ✓ Valid: $link"
        fi
    done
done

broken_links=$(cat "$broken_links_file")
total_links=$(cat "$total_links_file")

rm -f "$broken_links_file" "$total_links_file"

echo ""
echo "========================================="
echo "Total links checked: $total_links"
echo "Broken links found: $broken_links"
echo "========================================="

if [ "$broken_links" -eq 0 ]; then
    echo "✅ All links valid!"
    exit 0
else
    echo "❌ Found $broken_links broken links"
    exit 1
fi
