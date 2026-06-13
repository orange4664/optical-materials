# Frontend Development Guidelines

> Project-specific guidance for the current no-frontend workspace.

---

## Overview

This workspace currently has no web UI, frontend build system, routes, components, hooks, or browser state. Frontend guidance is therefore mostly negative scope: do not add frontend infrastructure for course-paper, COMSOL, or static-figure work unless a future task explicitly asks for it.

---

## Guidelines Index

| Guide | Description | Status |
|-------|-------------|--------|
| [Directory Structure](./directory-structure.md) | No frontend; static figures and paper outputs only | Not applicable / Filled |
| [Component Guidelines](./component-guidelines.md) | No components in this project | Not applicable / Filled |
| [Hook Guidelines](./hook-guidelines.md) | No frontend hooks in this project | Not applicable / Filled |
| [State Management](./state-management.md) | No frontend state; task/script state locations | Not applicable / Filled |
| [Quality Guidelines](./quality-guidelines.md) | Figure and Markdown checks instead of frontend checks | Not applicable / Filled |
| [Type Safety](./type-safety.md) | No TypeScript; Python/CSV naming conventions | Not applicable / Filled |

---

## Pre-Development Checklist

Before doing anything that looks like frontend work:

1. Confirm the user explicitly asked for a UI, website, dashboard, or frontend deliverable.
2. If not, use Python/COMSOL scripts for figures and `course_paper.md` plus document exports for writing.
3. Read [Directory Structure](./directory-structure.md), [Quality Guidelines](./quality-guidelines.md), and [Type Safety](./type-safety.md) for static-figure and paper-output checks.
4. If a real frontend is requested later, create a new Trellis task and update these specs with the chosen framework and conventions.

## Quality Gate

- Do not invent frontend lint/build commands while no frontend exists.
- Verify static figures and Markdown paths instead of running UI checks.
- Keep scientific plots under `outputs/`, not frontend asset directories.
