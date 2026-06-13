# State Management

## Status

No frontend or client-side state exists in this workspace.

## Current State Sources

- Trellis task state lives in `.trellis/tasks/**/task.json`.
- Simulation state is encoded by script parameters and generated CSV/model files.
- Paper state is the editable Markdown draft `course_paper.md`.

## Convention

- Do not add frontend state libraries.
- Keep analysis parameters in scripts or COMSOL model parameters.
- Keep task progress in Trellis task artifacts, not in ad hoc UI state files.
