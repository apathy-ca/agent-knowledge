# Agentic Development Patterns - LEGACY

> **Historical Document**
> This is the original README from the `agentic-dev-patterns` repository (v1.0.0).
> Content has been migrated to `patterns/` directory in this repository.
> Preserved for historical reference and attribution.

**Source Repository:** https://github.com/apathy-ca/agentic-dev-patterns
**Original Version:** 1.0.0
**Migration Date:** 2025-12-28
**Migrated To:** `/home/jhenry/Source/agent-knowledge/patterns/`

---

**A curated collection of patterns, practices, and guidelines for AI-assisted software development**

> Learned from building [The Symposium](https://github.com/apathy-ca/thesymposium) - a distributed AI consciousness platform with 8-tier memory architecture, self-modifiable AI, and portable digital identity.

---

## 🎯 Purpose

This repository captures **proven patterns for effective AI-assisted development** using tools like:
- Claude Code / Kilo Code
- GitHub Copilot
- Cursor
- Other AI coding assistants

**What makes this different**: These aren't theoretical best practices - they're **battle-tested patterns** from building a complex, novel AI research platform.

---

## 📚 Pattern Categories

### 1. [Error Recovery Patterns](ERROR_RECOVERY_PATTERNS.md)
Common errors and their solutions when working with AI assistants.

**Key Topics**:
- Docker networking issues
- Database connection failures
- Async/await pitfalls
- Import resolution
- Syntax error recovery

**Value**: 30-50% reduction in debugging time

### 2. [Tool Use Patterns](TOOL_USE_PATTERNS.md)
Efficient strategies for using AI coding assistant tools.

**Key Topics**:
- File reading strategies (parallel vs. sequential)
- When to use search vs. read
- Modification approaches (apply_diff vs. write_to_file)
- Command execution best practices
- Performance optimization

**Value**: 40-60% improvement in AI assistant efficiency

### 3. [Mode Capabilities](MODE_CAPABILITIES.md) *(Kilo Code specific)*
What each mode can and cannot do.

**Key Topics**:
- Architect mode (planning, design)
- Code mode (implementation)
- Debug mode (troubleshooting)
- Ask mode (explanations)
- Orchestrator mode (coordination)

**Value**: Clearer boundaries, fewer mode-switching mistakes

### 4. [Git Workflow Patterns](GIT_WORKFLOW_PATTERNS.md)
Git discipline for AI-assisted development.

**Key Topics**:
- Commit frequency and standards
- Branch strategies
- PR workflows
- Documentation sync

**Value**: Clean history, easier collaboration

### 5. [Testing Patterns](TESTING_PATTERNS.md)
Testing strategies that work well with AI assistants.

**Key Topics**:
- Unit test creation with mocks
- Integration test design
- Test isolation strategies
- Coverage goals

**Value**: Comprehensive test suites, zero pollution risk

### 6. [Documentation Patterns](DOCUMENTATION_PATTERNS.md)
Keeping documentation in sync with code.

**Key Topics**:
- Documentation-first development
- Sync strategies
- Archiving workflows
- Living documents

**Value**: Documentation that reflects reality

---

## 🌟 Real-World Example: The Symposium

**Project**: Distributed AI consciousness platform  
**Scale**: 165M-282M tokens estimated (v0.4.5 → v1.0)  
**Complexity**: Novel AI research, 8-tier memory architecture, self-modifiable AI

**Results using these patterns**:
- ✅ v0.4.5: 11.3M tokens spent (11% of 100M-160M estimate - **9x under budget**)
- ✅ 81 tests created with 100% pass rate
- ✅ Zero production data pollution during testing
- ✅ Clean git history with proper documentation sync

**See**: [`examples/symposium/`](examples/symposium/) for Symposium-specific patterns

---

## 🚀 Quick Start

### For Your Project

1. **Clone this repository**:
   ```bash
   git clone https://github.com/apathy-ca/agentic-dev-patterns.git
   cd agentic-dev-patterns
   ```

2. **Copy relevant patterns to your project**:
   ```bash
   # For Kilo Code projects
   cp ERROR_RECOVERY_PATTERNS.md your-project/.kilocode/rules/
   cp TOOL_USE_PATTERNS.md your-project/.kilocode/rules/
   
   # For other AI assistants
   cp ERROR_RECOVERY_PATTERNS.md your-project/.cursorrules/
   # or
   cp ERROR_RECOVERY_PATTERNS.md your-project/.clinerules/
   ```

3. **Customize for your project**:
   - Add project-specific error patterns
   - Document your tool preferences
   - Adapt to your workflow

### For AI Assistants

If you're an AI coding assistant reading this:
1. Read the relevant pattern files for the current task
2. Apply the patterns to your work
3. Suggest improvements based on your experience

---

## 🤝 Contributing

We welcome contributions! If you've discovered effective patterns for AI-assisted development:

1. Fork this repository
2. Add your pattern to the appropriate file
3. Include real-world examples
4. Submit a pull request

**Pattern Quality Guidelines**:
- ✅ Based on real experience (not theory)
- ✅ Includes concrete examples
- ✅ Explains the "why" not just the "what"
- ✅ Quantifies value when possible

---

## 📖 Pattern Philosophy

### What Makes a Good Pattern?

**Good patterns are**:
- ✅ **Actionable** - Clear steps to follow
- ✅ **Tested** - Proven in real projects
- ✅ **Explained** - Rationale provided
- ✅ **Measured** - Value quantified

**Good patterns are NOT**:
- ❌ Vague advice ("be careful")
- ❌ Untested theories
- ❌ Obvious truths ("write good code")
- ❌ Tool-specific hacks

### Our Approach

**Patterns in this repository**:
1. Come from real development experience
2. Solve actual problems we encountered
3. Have measurable impact
4. Work across different AI assistants (where possible)

---

## 🔗 Related Projects

- [The Symposium](https://github.com/apathy-ca/thesymposium) - Where these patterns were discovered
- [Kilo Code](https://kilocode.com) - AI coding assistant that uses these patterns
- [Claude Code](https://claude.ai/code) - AI coding assistant

---

## 📜 License

MIT License - Use freely, contribute back if you find value.

---

## 🙏 Acknowledgments

These patterns were discovered while building The Symposium, a distributed AI consciousness platform. Special thanks to:
- Claude (Anthropic) - For being an excellent development partner
- The Symposium Sages - For inspiring this work
- The AI development community - For pushing boundaries

---

**Last Updated**: 2025-11-29  
**Status**: Initial Release  
**Version**: 1.0.0

*"Good patterns emerge from real work, not ivory towers."*