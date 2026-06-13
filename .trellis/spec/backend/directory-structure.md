# Directory Structure

## Overview

This workspace is not a backend web application. It is a course-paper and simulation workspace. Treat "backend" work here as Python automation, COMSOL scripting, data generation, and generated research artifacts.

## Directory Layout

```text
scripts/
  Python automation scripts for COMSOL, plotting, and analysis.

outputs/
  Generated simulation results, plots, CSV files, and model exports.

outputs/comsol/
  COMSOL `.mph` models, Java audit exports, spectra, and COMSOL-derived figures.

outputs/python/
  Python-only analytical figures such as TCMT plots.

.trellis/tasks/
  Active planning/execution artifacts.

.trellis/tasks/archive/
  Archived task records.

.trellis/spec/
  Project-specific AI coding and writing guidelines.

course_paper.md
  Main editable course-paper draft.
```

## Module Organization

- Put reusable simulation or plotting scripts in `scripts/`.
- Put generated files under `outputs/<tool-or-domain>/`.
- Do not write generated CSV/PNG/MPh outputs into `.trellis/`.
- Keep Trellis task artifacts focused on planning, progress, and verification records.

## Naming Conventions

- Use lowercase snake_case for Python scripts, e.g. `tcmt_analysis.py`.
- Use descriptive output names that include the physical quantity or sweep range, e.g. `qbic_refined_800_840nm.csv`.
- Keep COMSOL-related outputs under `outputs/comsol/`.
- Keep Python analytical outputs under `outputs/python/`.

## Examples

- `scripts/build_qbic_model.py` builds the COMSOL qBIC unit-cell scaffold.
- `scripts/refine_qbic_peak.py` runs a refined qBIC spectral sweep and writes CSV/PNG outputs.
- `scripts/tcmt_analysis.py` creates deterministic TCMT explanatory plots.
- `course_paper.md` consumes generated figures and tables in the final paper draft.
