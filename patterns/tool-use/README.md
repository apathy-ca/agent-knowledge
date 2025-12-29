# Tool Use Patterns for AI Coding Assistants

**Purpose**: Efficient strategies for using AI coding assistant tools effectively.

**Value**: 40-60% improvement in development efficiency through optimized tool usage.

---

## Core Principle

**Efficient tool use means**:
- Reading multiple related files at once
- Using the right tool for the job
- Minimizing round trips
- Batching operations
- Caching results when appropriate
- Executing operations in parallel

---

## Pattern Categories

### [Optimization Patterns](./optimization-patterns.md)
General strategies for optimizing tool usage:
- Minimizing round trips
- Choosing the right tool for the task
- Understanding tool capabilities
- Avoiding redundant operations

### [Batching Patterns](./batching-patterns.md)
Combining multiple operations for efficiency:
- Parallel file reading
- Batch modifications
- Grouped searches
- Combined operations

### [Caching Patterns](./caching-patterns.md)
Strategies for caching and reusing results:
- When to cache
- Cache invalidation
- Context retention
- Avoiding redundant reads

### [Parallel Execution](./parallel-execution.md)
Executing independent operations simultaneously:
- Parallel file reads
- Concurrent searches
- Independent command execution
- Dependency management

### [Tool Selection](./tool-selection.md)
Choosing the appropriate tool for each task:
- File reading vs. search
- Different file modification approaches
- Command execution strategies
- Navigation vs. direct access

---

## Quick Reference

### File Operations
- **Read known files**: Batch read up to 5 related files
- **Search for files**: Use search when location unknown
- **Small changes**: Use targeted edits
- **Large changes**: Rewrite entire sections
- **New files**: Write complete file at once

### Command Execution
- **Control scripts**: Prefer project control scripts
- **Raw commands**: Only when no wrapper exists
- **Batching**: Chain related commands
- **Error handling**: Check status before proceeding

### Search Operations
- **Specific patterns**: Use precise regex
- **Broad exploration**: Start general, then narrow
- **File type filtering**: Specify extensions
- **Context**: Request surrounding lines

---

## Related Patterns

- [Error Recovery](../error-recovery/README.md) - Handling tool failures
- [Context Management](../context-management/README.md) - Managing tool output
- [Testing Patterns](../testing-patterns/README.md) - Testing tool integrations

---

**Last Updated**: 2025-11-29
**Source**: The Symposium development

*"Efficient tools make efficient development."*
