# Database Guidelines

## Overview

This project currently has no database, ORM, migration system, backend service, or persistent application state. Do not introduce database abstractions unless a future task explicitly requires them.

## Current Data Sources

- Word source document: `低维材料论文方向审计与结论.docx`.
- Trellis planning artifacts: `.trellis/tasks/**`.
- Generated simulation data: `outputs/comsol/*.csv`, `outputs/python/*.txt`.
- Main paper draft: `course_paper.md`.

## Contracts

- CSV files are the current structured data format for numerical outputs.
- Scripts that generate CSV files must write headers.
- Numeric sweep CSVs should include units in column names when practical, for example `wavelength_nm` or `max_normE_V_per_m`.

## Forbidden Patterns

- Do not add SQLite, SQLAlchemy, migrations, or service-layer persistence for course-paper work.
- Do not store generated data inside `.trellis/spec/`.
- Do not hard-code analysis conclusions without linking them to generated CSV/figure outputs or literature sources.

## Validation

- For generated spectra, validate row count and simple invariants such as `R_plus_T ≈ 1` when the model is a lossless proxy.
- For paper claims based on data, verify the referenced CSV/figure exists.
