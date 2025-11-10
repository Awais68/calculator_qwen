<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- List of modified principles:
  - [PRINCIPLE_1_NAME] → Test-Driven Development
  - [PRINCIPLE_2_NAME] → Modern Python with Type Hints
  - [PRINCIPLE_3_NAME] → Clean and Readable Code
  - [PRINCIPLE_4_NAME] → Architectural Decision Records
  - [PRINCIPLE_5_NAME] → Git for Version Control
- Added sections:
  - Technology Stack
  - Quality Requirements
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
Keep code clean and easy to read. Follow essential OOP principles: SOLID, DRY, KISS.

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

**Version**: 1.0.0 | **Ratified**: 2025-11-10 | **Last Amended**: 2025-11-10