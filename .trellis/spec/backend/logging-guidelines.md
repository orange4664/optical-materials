# Logging Guidelines

## Overview

This workspace uses simple command-line scripts, not a long-running service. Prefer concise `print()` progress lines over configuring application logging.

## Required Output

Scripts that generate artifacts should print:

- Input stage or sweep point, for example `solving_wavelength_nm=830`.
- Output paths, for example `saved_png=outputs/...`.
- Important scalar results, for example `R=... T=... maxE=...`.

## What To Avoid

- Do not add verbose debug logs to final scripts unless they help reproduce a COMSOL issue.
- Do not print entire field arrays in production analysis scripts; reserve that for discovery scripts.
- Do not log sensitive local paths unless needed for locating generated artifacts. Existing output path prints are acceptable in this local workspace.

## Examples

- `scripts/sweep_qbic_spectrum.py` prints each wavelength and the resulting `R`, `T`, and `R_plus_T`.
- `scripts/tcmt_analysis.py` prints the saved figure paths.
