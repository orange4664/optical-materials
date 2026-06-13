# Technical Design

## Scope

This task creates the first review-manuscript layer on top of the existing course-paper project. It should not overwrite or delete the course-paper deliverables. The new artifacts should live in review-specific files and folders, while the existing COMSOL/Python scaffold remains available as a supporting Box/Supplementary workflow.

## Target Artifact Boundaries

Primary new artifacts:

- `review_manuscript.md` or `manuscripts/review_manuscript.md`: English review scaffold with title, abstract, section outline, initial prose blocks, Box placement, and figure/table callouts.
- `literature_database.csv`: structured starter literature database covering the required conceptual routes. It does not need to be exhaustive in this task.
- `review_figures/` or `outputs/review/`: generated or drafted review display items, tables, and figure plans.
- `REVIEW_RUNS.md`: explains how the review manuscript relates to the original course-paper COMSOL workflow and which files are main-text vs Box/Supplementary.

Existing artifacts preserved:

- `course_paper.md`
- `RUNS.md`
- `outputs/comsol/**`
- `outputs/python/**`
- `outputs/final_package/**`

## Manuscript Design

Working title:

> Resonant Nonlinear Nanophotonics in van der Waals Metasurfaces

Alternative title to keep in the scaffold:

> Beyond High-Q Resonances: Design Rules for Nonlinear van der Waals Metasurfaces

Main thesis:

> Useful SHG in vdW metasurfaces is governed by nonlinear-source symmetry, source-mode overlap, outcoupling at the harmonic frequency, excitonic absorption, bandwidth, and fabrication tolerance, not by maximum Q alone.

Review structure:

1. Introduction: why vdW nonlinear metasurfaces now?
2. Nonlinear sources in layered crystals.
3. Resonant enhancement mechanisms.
4. Material platforms and representative progress.
5. Figures of merit and comparison pitfalls.
6. Design rules for useful SHG.
7. Box: minimal modelling of resonant SHG.
8. Outlook.

The COMSOL qBIC-inspired model should be referenced only in Section 7 or Supplementary planning. It must not appear as a main evidence chain for the review's central claim.

## Literature Database Contract

CSV columns:

- `id`
- `year`
- `authors`
- `title`
- `venue`
- `material_platform`
- `dimensionality_or_source_type`
- `resonance_mechanism`
- `nonlinear_process`
- `metric_reported`
- `baseline_or_reference`
- `pump_condition_note`
- `device_geometry`
- `key_message`
- `role_in_review`
- `doi_or_url`

Starter coverage:

- monolayer TMD + external metasurface
- all-TMD resonators/metasurfaces
- 3R-MoS2 nanodisks/anapole
- 3R-MoS2 qBIC and non-local metasurfaces
- WS2/MoS2 interface SHG
- broader vdW nonlinear platforms including GaSe, InSe, NbOCl, hBN, graphene/chi3
- mechanisms and methods papers for Mie/anapole/qBIC/nonlocal/exciton-cavity coupling
- FoM/metrology/calibration and review/context papers

The user explicitly relaxed the literature-count requirement: use only the papers needed for the current scaffold, and leave broader bibliography expansion as follow-up work.

## Figure/Table Design

Review display items should be mostly schematic/table based, not dependent on COMSOL.

Required display items:

1. Roadmap schematic/table: monolayer-on-metasurface -> hybrid vdW nanoantenna -> all-TMD resonator -> 3R/non-local vdW metasurface.
2. Nonlinear-source taxonomy: bulk, surface, interface, exciton-enhanced, chi3.
3. Resonance-mechanism taxonomy: Mie, anapole, qBIC, non-local, exciton/cavity hybridization.
4. Representative literature table generated from `literature_database.csv`.
5. FoM/comparison pitfalls table.
6. Design-rule summary figure/table.

Optional:

- A literature scatter plot if enough numeric metrics are available with trustworthy definitions.
- Clean English TCMT figure regenerated from existing `scripts/tcmt_analysis.py` or a new review plotting script.

## Journal-Target Notes

Nanophotonics is the primary target. The review should be selective and critical rather than encyclopedic. JPhys Photonics is the fallback if reproducible workflow and tutorial framing remain prominent. ACS Photonics Perspective/Review is the stretch target if the article becomes sharper and more opinionated.

## Operational Constraints

- Do not stop, restart, or clean any `python` or `comsolmphserver` process. The user is running their own COMSOL jobs.
- Avoid long COMSOL runs in this task. The immediate implementation can work from existing outputs and literature.
- If process inspection is needed, use read-only commands only.
- Root is not a git repository; Trellis archive must use `--no-commit`.

## Validation Strategy

- Validate Trellis planning with `task.py validate`.
- Validate new CSV shape and required columns.
- Validate review manuscript contains English title, abstract, required section headings, and no course metadata.
- Validate all Markdown image/table paths exist when used.
- Validate any new Python plotting/literature scripts with `python -m py_compile`.
- Validate no implementation step stops COMSOL/Python processes.
