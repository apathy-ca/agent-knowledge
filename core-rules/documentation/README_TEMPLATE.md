# README Template Reference

**Source:** Agent Rules Extraction - Templates Worker
**Version:** 1.0.0
**Last Updated:** 2025-12-26

## Overview

This document provides guidance on using the comprehensive README template. For the full template with all sections and examples, see [README Template](../../templates/templates/agent-project-template.md).

## Quick Reference

The README template is located at: [`../templates/readme-template.md`](../../templates/templates/agent-project-template.md)

It provides comprehensive README structure for different project types:
- Libraries/Packages
- Applications/Services
- Tools/CLI
- Frameworks

## Essential Sections

### Every README Must Have

1. **Title and Tagline**
   - Clear, descriptive project name
   - One-sentence tagline

2. **Overview**
   - 2-3 sentence description
   - Key features (3-5 bullet points)

3. **Quick Start**
   - Prerequisites
   - Installation instructions
   - Minimal working example

4. **Documentation**
   - Links to detailed documentation
   - API reference
   - Guides and tutorials

5. **License**
   - License type
   - Link to LICENSE file

## Customization by Project Type

### For Libraries/Packages

Focus on:
- Installation from package managers
- API reference and usage examples
- Integration examples
- Version compatibility

**Example:**
\`\`\`markdown
## Installation

\`\`\`bash
pip install my-library
\`\`\`

## Usage

\`\`\`python
from my_library import MyClass

client = MyClass(api_key="...")
result = client.do_something()
\`\`\`

## API Reference

See [API Documentation](docs/API.md) <!-- example link --> for complete reference.
\`\`\`

### For Applications/Services

Focus on:
- Features and capabilities
- Configuration options
- Deployment instructions
- Environment setup

**Example:**
\`\`\`markdown
## Features

- Real-time data processing
- Multi-user collaboration
- Advanced reporting

## Configuration

Configure via environment variables or `.env` file:

\`\`\`env
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
\`\`\`

## Deployment

See [Deployment Guide](docs/DEPLOYMENT.md) <!-- example link --> for detailed instructions.
\`\`\`

### For Tools/CLI

Focus on:
- Command-line usage
- Available commands and options
- Common workflows
- Examples

**Example:**
\`\`\`markdown
## Usage

\`\`\`bash
# Basic usage
mytool command [options]

# Common commands
mytool init          # Initialize project
mytool build        # Build project
mytool deploy       # Deploy to production
\`\`\`

## Commands

See [Commands Reference](docs/COMMANDS.md) <!-- example link --> for all available commands.
\`\`\`

### For Frameworks

Focus on:
- Getting started guide
- Core concepts
- Architecture overview
- Extension/plugin system

**Example:**
\`\`\`markdown
## Getting Started

1. Install the framework
2. Create a new project
3. Run the development server

## Core Concepts

- **Concept 1**: Description
- **Concept 2**: Description

## Architecture

See [Architecture Documentation](docs/ARCHITECTURE.md) <!-- example link --> for detailed design.
\`\`\`

## Best Practices

### ✅ Do

- Keep README concise (< 500 lines)
- Use working, tested examples
- Update README with code changes
- Link to detailed documentation
- Include badges (CI, coverage, version)
- Add table of contents for long READMEs

### ❌ Don't

- Put everything in README (use linked docs)
- Include outdated examples
- Forget to test examples
- Use broken links
- Assume prior knowledge
- Make it too technical

## README Checklist

Before releasing:

- [ ] Title and description clear
- [ ] Installation instructions work
- [ ] Examples are tested and work
- [ ] Links all functional
- [ ] Badges up to date
- [ ] License specified
- [ ] Contributing guidelines linked
- [ ] Support/contact information included

## Common Sections

### Badges

\`\`\`markdown
[![CI](https://github.com/org/repo/workflows/CI/badge.svg)](https://github.com/org/repo/actions)
[![Coverage](https://codecov.io/gh/org/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/org/repo)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](VERSION)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
\`\`\`

### Table of Contents

\`\`\`markdown
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
\`\`\`

### Quick Start

\`\`\`markdown
## Quick Start

\`\`\`bash
# Install
pip install my-project

# Run
my-project start
\`\`\`
\`\`\`

### Documentation Links

\`\`\`markdown
## Documentation

- [Getting Started](docs/getting-started.md) <!-- example link -->
- [API Reference](docs/API.md) <!-- example link -->
- [Architecture](docs/ARCHITECTURE.md) <!-- example link -->
- [Contributing](docs/CONTRIBUTING.md) <!-- example link -->
\`\`\`

### Contributing

\`\`\`markdown
## Contributing

Contributions welcome! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) <!-- example link --> for guidelines.
\`\`\`

### License

\`\`\`markdown
## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
\`\`\`

## Examples

### Minimal README (Small Library)

\`\`\`markdown
# My Library

> Simple utility library for X

## Installation

\`\`\`bash
pip install my-library
\`\`\`

## Usage

\`\`\`python
from my_library import function

result = function("input")
\`\`\`

## API

See [API Documentation](API.md).

## License

MIT
\`\`\`

### Comprehensive README (Large Project)

\`\`\`markdown
# My Project

> Complete solution for X, Y, and Z

## Overview

[Detailed description...]

## Features

- Feature 1
- Feature 2

## Quick Start

[Installation and basic usage...]

## Documentation

- [Getting Started](docs/getting-started.md) <!-- example link -->
- [User Guide](docs/guide.md) <!-- example link -->
- [API Reference](docs/API.md) <!-- example link -->
- [Architecture](docs/ARCHITECTURE.md) <!-- example link -->

## Development

[Setup instructions...]

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) <!-- example link -->.

## License

MIT - see [LICENSE](LICENSE).
\`\`\`

## Related Resources

- **Full Template:** [README Template](../../templates/templates/agent-project-template.md)
- **Documentation Standards:** [Documentation Standards](./DOCUMENTATION_STANDARDS.md)
- **API Documentation:** [API Documentation Standards](./API_DOCUMENTATION.md)
- **Documentation Workflow:** [Documentation Workflow](../core-rules/workflows/DOCUMENTATION_WORKFLOW.md)

## References

This guide references:
- [README Template](../../templates/templates/agent-project-template.md) - Complete template
- Workflows Worker: Documentation practices
- All Workers: README structures

---

**For the complete, detailed template with all sections and examples, see:**
**[../templates/readme-template.md](../../templates/templates/agent-project-template.md)**
