# Quality Guidelines

> Code quality standards for backend development.

---

## Overview

Quality in this project means reproducible Python/COMSOL analysis, traceable generated figures, and paper claims that are supported by either local outputs or cited literature. There is no backend service, API, or database.

---

## Forbidden Patterns

- Do not claim quantitative reproduction from simplified proxy simulations.
- Do not reference figures that do not exist on disk.
- Do not put generated simulation outputs under `.trellis/spec/`.
- Do not introduce backend frameworks or databases for paper-writing tasks.
- Do not use COMSOL GUI when a task explicitly requires script-only execution.

---

## Required Patterns

### COMSOL/MPh Scripted Simulation Pattern

#### 1. Scope / Trigger

- Trigger: Python scripts create, solve, or export COMSOL `.mph` simulation models.
- Applies to scripts under `scripts/` that use the `mph` package.
- User constraint for this project: COMSOL GUI may be disallowed; scripts must be able to build and verify models directly.

#### 2. Signatures

- Smoke test command:
  - `python scripts/comsol_smoke.py`
- Build model command:
  - `python scripts/build_qbic_model.py`
- Mesh/solve command:
  - `python scripts/run_qbic_model.py`
- Sweep/export command:
  - `python scripts/sweep_qbic_spectrum.py`
- Plot command:
  - `python scripts/plot_qbic_spectrum.py`

#### 3. Contracts

- Scripts must write generated simulation artifacts under `outputs/comsol/`.
- A build script must save both:
  - `.mph` model for reuse.
  - `.java` export for audit/debugging of COMSOL node properties.
- COMSOL scripts should call:
  - `mph.option("session", "stand-alone")` before `mph.start(...)` on Windows.
  - `mph.start(cores=<small integer>)` to avoid uncontrolled CPU use.
- Model parameters must include units in COMSOL string form, for example `"500[nm]"`.
- If material-property mapping through COMSOL materials is unreliable, use explicit physics features selected by domain and set the needed properties directly on each feature.
- For COMSOL EWFD models, do not stack extra wave-equation features on top of the default `wee1` unless every feature selection is verified editable and mutually exclusive. If COMSOL reports that `wee1` selection is not editable, keep a single material-controlled all-domain `wee1` and bind permittivity through material selections instead.
- If a geometry subtracts a physical void that should contain air, keep or recreate an explicit air-fill domain and include it in the air material/physics selection. A Boolean difference alone can turn the void into a non-physical outside boundary.
- For domain-restricted SHG proxies, define COMSOL coupling operators on the material selection, for example `aveop_mos2`, `intop_mos2`, and `maxop_mos2`, instead of using full-domain sampled maxima.
- Scripts that import `matplotlib.pyplot` in a COMSOL/JVM workflow should set `matplotlib.use("Agg")` before importing pyplot. On Windows, GUI/Tk cleanup can crash after a long COMSOL solve even when outputs were written.

#### 4. Validation & Error Matrix

- `import mph` fails -> stop and report missing Python dependency.
- `mph.start()` fails -> stop and report COMSOL startup/licensing issue.
- `client.modules()` lacks Wave Optics -> do not attempt EWFD model solve.
- Geometry build fails -> fix feature tags/properties before meshing.
- Mesh fails with automatic mesh sizing -> switch to user-controlled mesh size features.
- Solve fails with undefined material property such as `n`, `mur`, or `sigma` -> either provide that material property or set it directly on the selected physics feature.
- Periodic port solve fails due to incomplete periodic boundary selection -> inspect source/target boundary selections and exported Java before changing physics assumptions.

#### 5. Good/Base/Bad Cases

- Good: build, mesh, single-wavelength solve, sweep, and exported figure all pass from scripts.
- Base: build and mesh pass; solve failure is captured with the COMSOL message and the `.java` export exists for debugging.
- Bad: manual GUI-only edits are required but not documented in scripts.

#### 6. Tests Required

- Run `python -m py_compile scripts/*.py` or the explicit script list.
- Run the COMSOL smoke test after environment changes.
- For generated spectra, verify output CSV row count and basic physical consistency such as `R + T` within tolerance for lossless proxy models.
- For corrected air-hole models, verify the Java export contains the air-hole geometry domain in the air selection, e.g. `sel_air` includes the triangular-prism domain and the MoS2 material/physics uses the checked MoS2 selection.
- Confirm generated PNG/PDF files exist and are non-empty before using them in writing.

#### 7. Wrong vs Correct

Wrong:

```python
model = client.create("model")
model.solve()
```

This hides whether geometry, mesh, materials, and studies were configured correctly.

Correct:

```python
mph.option("session", "stand-alone")
client = mph.start(cores=2)
model = client.create("qbic_3r_mos2_unitcell")
# Create geometry, selections, materials, physics, mesh, and study.
model.build()
model.mesh()
model.solve("Wavelength sweep")
model.save("outputs/comsol/qbic_3r_mos2_unitcell.mph")
model.save("outputs/comsol/qbic_3r_mos2_unitcell.java", format="java")
```

---

## Testing Requirements

### Paper and Figure Validation

- Before reporting a paper task complete, verify every Markdown image path exists.
- Verify the paper contains required section headings from the task PRD.
- Verify generated CSV files have expected row counts and core invariants.
- If references are used, include enough metadata to locate the source: author, title, venue, year, and URL or DOI.

### Simulation Validation

- For COMSOL outputs, at minimum validate build, mesh, solve, and artifact generation.
- For lossless proxy optical models, check `R + T` is close to 1 when using port S-parameters.
- Store caveats near the output, for example in `outputs/comsol/README.md`.

### Script Validation

- Run Python syntax checks on all modified scripts:

```bash
python -m py_compile scripts/<script>.py
```

---

## Code Review Checklist

- Are generated files under `outputs/` rather than `.trellis/`?
- Are simplified physics assumptions explicitly stated?
- Does every paper figure reference resolve to an existing file?
- Are source claims backed by either generated data or cited literature?
- Are Trellis task artifacts updated before archiving?
