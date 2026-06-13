# Error Handling

## Overview

Python scripts in this project primarily orchestrate COMSOL, plotting, and paper-output validation. Errors should fail fast with enough context to identify the failing model stage, expression, or output file.

## Required Patterns

- Use explicit script stages in printed output, such as `building_geometry`, `meshing`, `solving`, or `saved_csv=...`.
- Let unrecoverable errors raise normally so the command exits non-zero.
- For exploratory expression discovery, catch broad COMSOL exceptions only to report which expression failed, as in `scripts/evaluate_qbic_model.py`.
- Use assertions for local validation scripts when checking generated CSV row counts, image paths, or paper completeness.

## COMSOL-Specific Handling

- Treat COMSOL exceptions as authoritative. Do not hide the COMSOL error message.
- If solve fails with undefined material properties such as `n`, `mur`, or `sigma`, either define those material properties or set them explicitly on selected physics features.
- If automatic meshing fails, switch to user-controlled mesh settings rather than retrying the same automatic mesh.

## Forbidden Patterns

- Do not swallow COMSOL solve/build errors and continue as if results are valid.
- Do not write a paper figure reference until the corresponding file exists.
- Do not claim quantitative reproduction when scripts use simplified material constants or proxy metrics.

## Examples

- `scripts/run_qbic_model.py` prints stage markers before build, mesh, and solve.
- `scripts/evaluate_qbic_model.py` catches expression-evaluation errors while continuing to test other expressions.
