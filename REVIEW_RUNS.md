# Review Manuscript Runs

This file tracks the review-journal restructuring artifacts. It does not replace `RUNS.md`, which documents the course-paper COMSOL/Python scaffold.

## Current Review Artifacts

- `review_manuscript.md` - English review manuscript scaffold.
- `literature_database.csv` - curated starter literature database with 15 rows.
- `outputs/review/representative_literature_table.md`
- `outputs/review/fom_comparison_pitfalls.csv`
- `outputs/review/fom_comparison_pitfalls.md`
- `outputs/review/display_item_plan.md`

## Relationship To Existing COMSOL Work

The COMSOL qBIC-inspired model remains useful as tutorial or supplementary material. It should not be used as the central evidence chain for a Nanophotonics/JPhys/ACS review. The review's main evidence should come from published literature, comparison of figures of merit, and mechanism-level design rules.

## Process Constraint

No COMSOL process is started, stopped, restarted, or cleaned by the review asset builder. The user may run independent `mph`/COMSOL jobs in parallel.

## Follow-Up Literature Work

The current database is a scoped seed, not a final bibliography. Later work should expand GaSe, InSe, hBN, graphene, metrology, and calibration entries with paper-specific DOI and metric extraction.
