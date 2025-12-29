# Context Management Patterns

**Purpose**: Strategies for managing context windows, memory, and attention in AI-assisted development.

**Value**: Optimized memory usage, efficient context utilization, enables work on large codebases.

---

## Philosophy

**Good context management**:
- Reads selectively, not speculatively
- Maintains appropriate memory tiers
- Shapes attention deliberately
- Summarizes progressively
- Works within limits gracefully

**Bad context management**:
- Loads everything upfront
- Forgets important context
- Buries critical information
- Ignores context limits
- Repeats context unnecessarily

---

## Pattern Categories

### [Context Windows](./context-windows.md)
Managing context limits and working with large codebases:
- Selective file reading strategies
- Progressive context building
- Context window budgeting
- Context handoff between sessions
- Lazy loading patterns
- Multi-file vs. single-file work

**Key Pattern**: Read what you need, when you need it (70-80% reduction in context usage)

### [Summarization](./summarization.md)
Techniques for condensing information while preserving essential details:
- Investigation summarization (debugging to solution)
- Feature implementation summarization
- Conversation handoff documentation
- Progressive summarization layers
- Error investigation recipes
- Decision records

**Key Pattern**: Summarize the "what" and "why", forget the "how we got there"

### [Memory Tiers](./memory-tiers.md)
Organizing information by access patterns and longevity:
- Tier 1: Working Memory (immediate context, 20-40%)
- Tier 2: Session Memory (task context, 30-40%)
- Tier 3: Project Memory (architectural context, 10-20%)
- Tier 4: Reference Memory (external knowledge, 0-10%)
- Tier promotion and demotion
- Memory checkpointing
- Handoff memory strategies

**Key Pattern**: The right information, in the right place, at the right time

### [Attention Shaping](./attention-shaping.md)
Directing AI focus to the most important information:
- Explicit emphasis (visual markers, formatting)
- Attention anchors (critical warnings)
- Progressive disclosure (reveal as needed)
- Recency emphasis (restate before action)
- Negative attention (DO NOTs)
- Structured attention (priority hierarchies)
- Question-driven attention
- Scope boundaries

**Key Pattern**: Direct attention deliberately, not accidentally (40-50% reduction in errors)

---

## Quick Reference

### Working with Large Codebases
1. **Overview first**: README, architecture docs, directory structure
2. **Progressive loading**: Load files as needed, not all at once
3. **Targeted reading**: Use search before read for discovery
4. **Memory tiers**: Keep only current work in working memory

### Long-Running Tasks
1. **Checkpoint regularly**: Create summaries at phase boundaries
2. **Handoff documents**: Enable seamless session continuation
3. **Progressive summarization**: Tier 1 (detail) → Tier 2 (summary) → Tier 3 (archive)
4. **Context budgeting**: Allocate context across memory tiers

### Critical Operations
1. **Restate constraints**: Repeat important info before action
2. **Explicit emphasis**: Use 🚨 for critical warnings
3. **DO NOTs**: State negatives explicitly
4. **Scope boundaries**: Define what's in/out of scope

---

## Context Management by Task Type

| Task Type | Strategy | Context Budget |
|-----------|----------|----------------|
| Feature Implementation | Progressive loading, session memory | Working 35%, Session 35%, Project 20% |
| Bug Investigation | Focus on error context, working memory heavy | Working 40%, Session 30%, Project 20% |
| Code Review | Load all PR files, structured attention | Working 30%, Session 40%, Project 25% |
| Refactoring | Multi-file context, memory checkpoints | Working 35%, Session 35%, Project 20% |
| Documentation | Reference memory, targeted reading | Working 30%, Session 25%, Project 20%, Reference 25% |

---

## Common Context Problems and Solutions

### Problem: "Context window exhausted mid-task"
**Solutions**:
- Create checkpoint summary (Summarization)
- Demote completed work to lower tier (Memory Tiers)
- Start fresh conversation with handoff (Context Windows)

### Problem: "AI forgot important constraint"
**Solutions**:
- Restate before critical action (Attention Shaping)
- Use explicit emphasis markers (Attention Shaping)
- Keep constraints in working memory (Memory Tiers)

### Problem: "Too much information to process"
**Solutions**:
- Progressive disclosure (Attention Shaping)
- Lazy loading - read just-in-time (Context Windows)
- Structured priority hierarchy (Attention Shaping)

### Problem: "Can't resume work from previous session"
**Solutions**:
- Create handoff document (Summarization)
- Checkpoint with memory tiers (Memory Tiers)
- Include code context in handoff (Context Windows)

---

## Best Practices

### Do
- ✅ Read files selectively based on immediate need
- ✅ Create checkpoints at natural boundaries
- ✅ Organize information into memory tiers
- ✅ Emphasize critical information explicitly
- ✅ Budget context before starting work
- ✅ Summarize progressively (not all at once)

### Don't
- ❌ Load entire codebase upfront
- ❌ Re-read files already in context
- ❌ Bury critical warnings in paragraphs
- ❌ Continue when context limit reached
- ❌ Forget to create handoffs for long tasks
- ❌ Mix all information in working memory

---

## Impact Metrics

Based on The Symposium development (v0.4.5):

**Context Efficiency**:
- 70-80% reduction in context usage (selective reading)
- 60% improvement in context efficiency (memory tiers)
- 80% reduction in context re-loading (handoff documents)

**Error Reduction**:
- 40-50% fewer errors (attention shaping)
- 30% faster bug resolution (focused context)

**Task Continuity**:
- Seamless resumption across sessions (checkpointing)
- Zero context waste on re-exploration (progressive summarization)

---

## Related Patterns

- [Tool Use Patterns](../tool-use/README.md) - Efficient tool usage reduces context needs
- [Error Recovery](../error-recovery/README.md) - Error patterns affect context priority
- [Mode Capabilities](../mode-capabilities/README.md) - Context handoff between modes

---

## Related Core Rules

**See Also**:
- [Memory Patterns](../../core-rules/design-patterns/memory-patterns.md) - Memory architecture standards
- [Agent Handoffs](../../core-rules/orchestration/agent-handoffs.md) - Context transfer between agents

---

**Last Updated**: 2025-12-29
**Patterns**: 4 core patterns (Context Windows, Summarization, Memory Tiers, Attention Shaping)
**Source**: The Symposium development (v0.4.5), Czarina orchestration patterns
**Status**: Complete

*"Manage context like memory: keep working memory lean, organize by tiers, recall on demand."*
