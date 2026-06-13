# Bootstrap Guidelines Completion Record

## Goal

Populate Trellis project specifications so future AI coding sessions use this workspace's actual conventions instead of generic backend/frontend defaults.

## Completed Scope

- Backend specs describe the project as a Python/COMSOL/course-paper workspace rather than a web backend.
- Frontend specs explicitly document that no frontend exists and that static figures and paper outputs should not be treated as UI work.
- Shared thinking guides are present under `.trellis/spec/guides/`.
- Backend and frontend index files now provide pre-development checklists and quality gates.

## Completed Files

### Backend

- `.trellis/spec/backend/directory-structure.md`
- `.trellis/spec/backend/database-guidelines.md`
- `.trellis/spec/backend/error-handling.md`
- `.trellis/spec/backend/logging-guidelines.md`
- `.trellis/spec/backend/quality-guidelines.md`
- `.trellis/spec/backend/index.md`

### Frontend

- `.trellis/spec/frontend/directory-structure.md`
- `.trellis/spec/frontend/component-guidelines.md`
- `.trellis/spec/frontend/hook-guidelines.md`
- `.trellis/spec/frontend/state-management.md`
- `.trellis/spec/frontend/type-safety.md`
- `.trellis/spec/frontend/quality-guidelines.md`
- `.trellis/spec/frontend/index.md`

## Acceptance Criteria

- [x] Backend guidelines are filled with project-specific conventions.
- [x] Frontend guidelines are filled with explicit no-frontend scope.
- [x] Spec index files point future work to the relevant checks.
- [x] No active bootstrap task remains.

## Verification

- `task.json` status is `completed`.
- Task is archived under `.trellis/tasks/archive/2026-06/00-bootstrap-guidelines`.
- `task.py validate` passes for this archived task.
