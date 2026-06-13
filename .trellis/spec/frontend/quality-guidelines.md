# Frontend Quality Guidelines

## Status

No frontend exists. Frontend quality checks are not applicable to the current project.

## What To Check Instead

- For figures: verify PNG files exist and are non-empty.
- For Markdown papers: verify every image reference resolves.
- For data-driven plots: verify the source CSV exists and has expected columns.

## Forbidden Patterns

- Do not run or invent frontend lint/build commands unless a frontend is added.
- Do not treat static manuscript figures as UI implementation work.
