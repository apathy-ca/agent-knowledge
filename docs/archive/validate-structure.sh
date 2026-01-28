#!/bin/bash
# File: /home/jhenry/Source/agent-knowledge/meta/validate-structure.sh

echo "Validating directory structure..."
errors=0

# Function to check if directory exists
check_dir() {
    if [ ! -d "$1" ]; then
        echo "❌ Missing directory: $1"
        ((errors++))
    else
        echo "✓ Found: $1"
    fi
}

# Function to check if file exists
check_file() {
    if [ ! -f "$1" ]; then
        echo "❌ Missing file: $1"
        ((errors++))
    else
        echo "✓ Found: $1"
    fi
}

# Check root files
check_file "README.md"
check_file "CONTRIBUTING.md"
check_file "CHANGELOG.md"
check_file "LICENSE"
check_file ".gitignore"
check_file "AGENT_RULES_LEGACY.md"
check_file "AGENTIC_DEV_PATTERNS_LEGACY.md"

# Check core-rules
check_dir "core-rules"
check_file "core-rules/INDEX.md"
check_dir "core-rules/python-standards"
check_dir "core-rules/agent-roles"
check_dir "core-rules/workflows"
check_dir "core-rules/design-patterns"
check_dir "core-rules/testing"
check_dir "core-rules/security"
check_dir "core-rules/documentation"
check_dir "core-rules/orchestration"

# Check patterns
check_dir "patterns"
check_file "patterns/INDEX.md"
check_dir "patterns/error-recovery"
check_dir "patterns/tool-use"
check_dir "patterns/mode-capabilities"
check_dir "patterns/context-management"
check_dir "patterns/git-workflows"
check_dir "patterns/testing-patterns"

# Check templates
check_dir "templates"

# Check examples
check_dir "examples"

# Check meta
check_dir "meta"
check_file "meta/versioning.md"
check_file "meta/pattern-template.md"
check_file "meta/learning-extraction.md"

echo ""
if [ $errors -eq 0 ]; then
    echo "✅ All structure validation checks passed!"
else
    echo "❌ Found $errors errors in structure"
fi

exit $errors
