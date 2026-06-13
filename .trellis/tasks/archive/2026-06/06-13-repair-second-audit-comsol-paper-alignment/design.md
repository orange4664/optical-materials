# Technical Design

## Scope

This task aligns the existing COMSOL model, generated figures, TCMT analysis, and paper narrative with the second audit. It is not a new topic selection task and not a full experimental reproduction. The final claim remains a teaching-level trend model.

## COMSOL Physics Domain Design

The current model keeps a triangular air-fill prism, which should stay. The immediate fix is to constrain the default `wee1` wave-equation feature to `sel_air`:

```python
configure_wave_equation(ewfd.feature("wee1"), "1", "sel_air")
```

The SiO2 and MoS2 features remain bound to `sel_sio2` and `sel_mos2_checked`. After rebuild, the Java export should show all three features with named selections. This preserves the existing explicit-material-feature pattern while removing overlapping wave equation risk.

## Refined Sweep And Metrics

The refined sweep remains 810-850 nm initially. The scripts should compute:

- `reflectance_R`
- `transmittance_T`
- `R_plus_T`
- MoS2-domain raw `F2`, `F4`, `Emax`
- normalized `F4_norm_to_min`, `F4_norm_to_median`, or equivalent
- peak metadata:
  - `R_peak_wavelength_nm`
  - `F4_peak_wavelength_nm`
  - `low_F4_wavelength_nm`

Absolute F4 values may remain in CSV for traceability but plots and paper should use normalized/log values.

## Near-Field Figure Design

Near-field figures should be regenerated for:

- R peak, currently likely near 849 nm after rerun.
- F4 peak, previously 843 nm.
- Low-F4 point chosen from the refined CSV, not assumed to be 810 nm.

All field maps should use a shared color scale computed from the selected maps, or the figure captions must explicitly say each panel is individually scaled. Preferred output is a multi-panel comparison image, e.g. `qbic_field_comparison.png`, plus optional individual images.

## Side-Length Scan Design

The side scan should not collapse each side length by maximum R only. It should store full sampled grid data and a summarized CSV:

- Full grid: one row per `(tri_side_nm, wavelength_nm)`.
- Summary: best-R and best-F4 points per side length.
- Heatmaps:
  - `tri_side × wavelength → R`
  - `tri_side × wavelength → normalized/log F4`

This supports the paper claim that reflection and F4 optimization are not identical.

## TCMT Design

The left panel can keep the Q-vs-bandwidth illustration. The right panel should use external coupling ratio:

```text
r = gamma_e / gamma_i
field_buildup = gamma_e / (gamma_e + gamma_i)^2
outcoupling = gamma_e / (gamma_e + gamma_i)
proxy = field_buildup^2 * outcoupling
```

Plot `proxy` versus `r` on a log x-axis and mark the optimum ratio. Avoid over-emphasizing the COMSOL Q marker because the audit considers it weak.

## Paper Narrative Design

The paper should consistently use these terms:

- `qBIC-inspired simplified unit cell`
- `teaching-level trend model`
- `linear reflectance peak`
- `MoS2-domain F4 proxy peak`
- `spectral-width proxy Q`

The core analysis point should become:

> The wavelength that maximizes linear reflectance does not necessarily maximize the MoS2-domain F4 proxy, so SHG-oriented design cannot rely on reflectance spectra alone.

## Final Delivery Design

Do not delete source/project files required for traceability. Instead create or update a clean output bundle directory, for example `outputs/final_package/`, excluding:

- `.agents/`, `.claude/`, `.codex/`, `.trellis/`
- `scripts/__pycache__/`
- `hs_err_pid*.log`
- old conflicting refined outputs such as `qbic_refined_800_840nm.*`

The final package should contain the current paper, selected figures/data, scripts, COMSOL model/export, and a README/RUNS file.
