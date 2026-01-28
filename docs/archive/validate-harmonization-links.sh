#!/usr/bin/env bash
# validate-harmonization-links.sh
# Validate all internal markdown links added during harmonization

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "=== Link Validation Report (Harmonization Worker) ==="
echo "Date: $(date)"
echo "Repository: $REPO_ROOT"
echo ""

TOTAL_LINKS=0
BROKEN_LINKS=0
VALID_LINKS=0

# Files modified/created by harmonization worker
HARMONIZED_FILES=(
    "core-rules/workflows/GIT_WORKFLOW.md"
    "patterns/git-workflows/README.md"
    "core-rules/testing/README.md"
    "patterns/testing-patterns/README.md"
    "core-rules/agent-roles/README.md"
    "patterns/mode-capabilities/README.md"
    "core-rules/design-patterns/ERROR_RECOVERY.md"
    "patterns/error-recovery/README.md"
    "patterns/context-management/README.md"
    "meta/cross-reference-map.md"
)

echo "Checking ${#HARMONIZED_FILES[@]} harmonized files..."
echo ""

for FILE in "${HARMONIZED_FILES[@]}"; do
    if [[ ! -f "$FILE" ]]; then
        echo "⚠️  File not found: $FILE"
        continue
    fi

    echo "Checking: $FILE"

    # Extract markdown links: [text](path)
    # Match relative links only (starting with ./ or ../)
    grep -oP '\[([^\]]+)\]\((\.\./[^\)]+\.md|\./[^\)]+\.md)\)' "$FILE" | while read -r LINK; do
        ((TOTAL_LINKS++)) || true

        # Extract the path from [text](path)
        PATH_PART=$(echo "$LINK" | sed -n 's/.*(\(.*\)).*/\1/p')

        # Remove any anchor (#section)
        PATH_NO_ANCHOR="${PATH_PART%%#*}"

        # Resolve relative path
        FILE_DIR="$(dirname "$FILE")"
        RESOLVED_PATH="$(cd "$FILE_DIR" && realpath --relative-to="$REPO_ROOT" "$PATH_NO_ANCHOR" 2>/dev/null || echo "INVALID")"

        if [[ "$RESOLVED_PATH" == "INVALID" ]] || [[ ! -f "$RESOLVED_PATH" ]]; then
            echo "  ❌ BROKEN: $PATH_PART"
            ((BROKEN_LINKS++)) || true
        else
            echo "  ✅ Valid: $PATH_PART -> $RESOLVED_PATH"
            ((VALID_LINKS++)) || true
        fi
    done

    echo ""
done

echo "=== Summary ==="
echo "Total links checked: $TOTAL_LINKS"
echo "Valid links: $VALID_LINKS"
echo "Broken links: $BROKEN_LINKS"
echo ""

if [[ $BROKEN_LINKS -eq 0 ]]; then
    echo "✅ All links are valid!"
    exit 0
else
    echo "❌ Found $BROKEN_LINKS broken links!"
    exit 1
fi
