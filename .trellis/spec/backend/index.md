# Backend Development Guidelines

> Project-specific conventions for Python automation, COMSOL scripting, data outputs, and paper-validation work.

---

## Overview

This workspace is a course-paper and simulation project, not a backend service. Treat backend work as scripted analysis under `scripts/`, generated data under `outputs/`, and validation of paper/simulation artifacts.

---

## Guidelines Index

| Guide | Description | Status |
|-------|-------------|--------|
| [Directory Structure](./directory-structure.md) | Python scripts, outputs, Trellis artifact layout | Filled |
| [Database Guidelines](./database-guidelines.md) | No database; CSV/data-output contracts | Filled |
| [Error Handling](./error-handling.md) | COMSOL/Python script error handling | Filled |
| [Quality Guidelines](./quality-guidelines.md) | Simulation, paper, and script quality checks | Filled |
| [Logging Guidelines](./logging-guidelines.md) | CLI progress output for local scripts | Filled |

---

## Pre-Development Checklist

Before changing scripts, outputs, or paper-generation logic:

1. Read [Directory Structure](./directory-structure.md) for where files belong.
2. Read [Database Guidelines](./database-guidelines.md) for CSV/data-output contracts.
3. Read [Error Handling](./error-handling.md) before changing COMSOL or diagnostic scripts.
4. Read [Quality Guidelines](./quality-guidelines.md) before running or reporting simulation results.
5. Read [Logging Guidelines](./logging-guidelines.md) before adding command-line script output.

## Quality Gate

- Run syntax checks for modified Python scripts.
- Verify COMSOL outputs exist and are non-empty before citing them.
- Verify Markdown image paths resolve before exporting the paper.
- State simplified-material and proxy-metric limitations in paper text and output README files.
