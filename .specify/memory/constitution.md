<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- List of modified principles:
  - Clean and Readable Code
- Added sections:
  - Object-Oriented Programming
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# sp-calc-online Constitution

## Core Principles

### Test-Driven Development
Write tests first (TDD approach). Red-Green-Refactor cycle strictly enforced.

### Modern Python with Type Hints
Use Python 3.12+ with type hints everywhere.

### Clean and Readable Code
Keep code clean and easy to read.

### Object-Oriented Programming
Follow essential OOP principles: SOLID, DRY, KISS.

### Architectural Decision Records
Document important decisions with ADRs.

### Git for Version Control
Keep all project files in git.

## Technology Stack
- Python 3.12+ with UV package manager
- pytest for testing

## Quality Requirements
- All tests must pass
- At least 80% code coverage
- Use dataclasses for data structures

## Governance
Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance.

**Version**: 1.1.0 | **Ratified**: 2025-11-10 | **Last Amended**: 2025-11-11