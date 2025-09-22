# Contributing to this Ansible Collection

Thank you for your interest in contributing to the Proxmox Management Ansible collection! This document provides guidelines and steps for contributing.

## Core Principles

1. **Single Responsibility**: Keep roles targeted at doing a specific thing well and idempotently. Each role should have a clear, focused purpose.

2. **Idempotency**: Ensure all tasks can be run multiple times without causing issues or unwanted changes.

## Development Process

### 1. Making Changes

Before submitting your contribution:

1. Create a new branch for your changes
2. Write clear, focused code that follows basic Ansible principles
3. Add appropriate examples in the `examples/` directory
4. Update all relevant documentation
5. Update the changelog following the Keep a Changelog format:

```markdown
## [Unreleased]

### Added
- New feature X

### Changed
- Modified behavior Y

### Fixed
- Bug fix Z
```

### 2. Testing and Validation

1. Run linting checks:
```bash
ansible-lint
```

2. Test your changes thoroughly:
   - Ensure idempotency (running twice should not change anything the second time)
   - Test edge cases
   - Verify error handling

### 3. Documentation

Ensure you've updated all relevant documentation:

1. Role documentation (README.md in each role directory)
2. Examples in the `examples/` directory
3. Main README.md (if adding new features)
4. CHANGELOG.md (following the Keep a Changelog format)

### 4. Pull Request Process

1. Push your changes to your fork
2. Create a Pull Request with a clear title and description
3. Link any relevant issues
4. Respond to review feedback

## Code Style

- Follow Ansible best practices
- Use clear, descriptive variable names
- Comment complex logic
- Keep functions focused and manageable
- Use consistent indentation (2 spaces)

## Examples

Always include examples for new features or significant changes. Examples should be:

- Clear and easy to understand
- Demonstrating practical use cases
- Showing both basic and advanced usage (when applicable)
- Located in the appropriate `examples/` directory

## Need Help?

If you have questions or need help with your contribution:

1. Open an issue for discussion
2. Ask in the pull request
3. Reference existing similar contributions

Thank you for contributing!