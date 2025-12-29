# Mode Capabilities for AI-Assisted Development

**Purpose**: Define what each operational mode can and cannot do to prevent mistakes and clarify when to switch modes.

**Value**: Clearer boundaries, fewer mode-switching mistakes, better task routing, 30-40% improvement in workflow efficiency.

---

## Philosophy

**Good mode usage**:
- Matches mode to task type
- Switches deliberately with clear reasoning
- Respects mode constraints
- Maximizes tool availability per mode
- Prevents context switching overhead

**Bad mode usage**:
- Starting in wrong mode for task
- Ignoring mode constraints
- Random mode switching
- Forcing tools in restricted modes
- Unclear transition reasoning

---

## Mode Overview

AI-assisted development workflows typically include 5 specialized modes, each with specific capabilities and constraints:

1. **[Architect Mode](./architect-mode.md)** - Planning and design
2. **[Code Mode](./code-mode.md)** - Implementation and modification
3. **[Debug Mode](./debug-mode.md)** - Troubleshooting and investigation
4. **[Ask Mode](./ask-mode.md)** - Explanations and learning
5. **[Orchestrator Mode](./orchestrator-mode.md)** - Multi-task coordination

---

## Pattern Categories

### [Architect Mode](./architect-mode.md)
Planning and design before implementation:
- Create implementation plans
- Design system architecture
- Create technical specifications
- Estimate effort and complexity
- When to use and when to switch

### [Code Mode](./code-mode.md)
Writing and modifying code:
- Full file manipulation capabilities
- Testing and command execution
- Configuration updates
- When to use and when to switch

### [Debug Mode](./debug-mode.md)
Systematic troubleshooting and investigation:
- Investigate errors
- Analyze logs
- Add logging statements
- Trace execution
- When to use and when to switch

### [Ask Mode](./ask-mode.md)
Explanations, documentation, and learning:
- Explain concepts
- Answer questions
- Provide documentation
- Analyze code (read-only)
- When to use and when to switch

### [Orchestrator Mode](./orchestrator-mode.md)
Coordinating complex, multi-step projects:
- Break down large tasks
- Create subtasks
- Coordinate work across modes
- Manage workflows
- Delegation strategies

### [Mode Transitions](./mode-transitions.md)
Decision tree and transition guidelines:
- Decision tree for choosing modes
- When to switch modes
- Transition examples
- Best practices for switching

---

## Decision Tree

```
What do you need to do?
│
├─ Plan or design?
│  └─ Use: Architect Mode
│
├─ Implement or modify code?
│  └─ Use: Code Mode
│
├─ Troubleshoot or investigate?
│  └─ Use: Debug Mode
│
├─ Learn or understand?
│  └─ Use: Ask Mode
│
└─ Coordinate complex project?
   └─ Use: Orchestrator Mode
```

---

## Quick Reference by Task Type

| Task | Best Mode | Why |
|------|-----------|-----|
| Planning features | Architect | Design before implementation saves time |
| Implementing code | Code | Has full tool access |
| Fixing bugs | Debug then Code | Identify root cause, then fix |
| Understanding code | Ask | Read-only analysis, then switch to Code if changes needed |
| Large projects | Orchestrator | Manages complexity and mode coordination |
| Refactoring | Code | Direct implementation with full access |
| Learning new concepts | Ask | Focused explanation without tool distraction |

---

## Best Practices

### 1. Match Task to Mode

**Pattern**: Every task has a natural starting mode
- Complex features → Architect first
- Bug fixes → Debug first, Code second
- Learning → Ask first
- Most development → Code mode

### 2. Switch Modes Deliberately

When you decide to switch:
1. Summarize what the current mode accomplished
2. Explain why you're switching
3. State what the new mode will do
4. Provide any necessary context

**Example**:
```
Switching from Architect to Code mode.

Accomplished: Created detailed implementation plan for the 3-service refactor
(UserService, AuthService, DataService).

Why switching: Architecture is now complete and testable. Ready to implement.

Code mode will: Implement the three services following the design specifications.
```

### 3. Respect Mode Constraints

**Pattern**: Constraints prevent inefficient tool usage

- Don't try to code in Architect mode (use Code mode)
- Don't plan complex architecture in Code mode (use Architect mode first)
- Don't implement in Debug mode (use Code mode)
- Don't modify files in Ask mode (use appropriate mode first)

**If you hit a constraint**:
1. Stop the current operation
2. Identify which mode you need
3. Switch and retry
4. Save context for the next mode

### 4. Use Orchestrator for Complexity

**Pattern**: Large projects need coordination

If a task involves:
- Multiple sub-teams or modes
- Phases that must happen in sequence
- Complex dependencies between tasks
- Progress tracking across days/weeks

→ Use Orchestrator mode to manage the workflow

### 5. Minimize Mode-Switching Overhead

**Pattern**: Batch work within same mode

- Do all planning in Architect mode before switching
- Do all implementation in Code mode before switching
- Do all investigation in Debug mode before switching

Minimize context switches by completing everything possible in one mode.

---

## Kilo Code Specific Notes

These patterns generalize to any AI-assisted development, but Kilo Code has specific mode switching mechanisms (XML tags, mode slugs) and usage statistics from real development:

**From Kilo Code v0.4.5 development** (11.3M tokens):
- Code mode: ~85% of work (implementation, testing, fixes)
- Architect mode: ~10% of work (planning, design docs)
- Debug mode: ~3% of work (troubleshooting)
- Ask mode: ~2% of work (understanding, explanations)
- Orchestrator mode: <1% (complex multi-phase work)

**Insight**: Most work is Code mode, but starting with Architect for complex features saves significant time overall.

---

## Related Patterns

- [Error Recovery Patterns](../error-recovery/README.md) - Handling errors within modes
- [Tool Use Patterns](../tool-use/README.md) - Efficient tool usage per mode
- [Testing Patterns](../testing-patterns/README.md) - Testing strategies
- [Git Workflows](../git-workflows/README.md) - Git discipline across modes

---

**Last Updated**: 2025-12-28
**Patterns**: 5 modes + transitions
**Applicable To**: AI-assisted development (generalizable beyond Kilo Code)
**Source**: MODE_CAPABILITIES.md from agentic-dev-patterns

*"The right mode for the right task makes all the difference."*
