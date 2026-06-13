# Reproduction Runs

This project uses scripted Python/COMSOL runs only. COMSOL GUI edits are not part of the workflow.

## Current Script Order

Run from the project root:

```powershell
python scripts\build_qbic_model.py
python scripts\run_qbic_model.py
python scripts\evaluate_qbic_model.py
python scripts\refine_qbic_peak.py
python scripts\export_qbic_field_maps.py
python scripts\qbic_sensitivity_scan.py
python scripts\tcmt_analysis.py
```

## Current Outputs Used By The Paper

- `outputs/comsol/qbic_3r_mos2_unitcell.mph`
- `outputs/comsol/qbic_3r_mos2_unitcell.java`
- `outputs/comsol/qbic_spectrum_780_900nm.png`
- `outputs/comsol/qbic_refined_810_850nm.csv`
- `outputs/comsol/qbic_refined_810_850nm.png`
- `outputs/comsol/qbic_peak_summary.txt`
- `outputs/comsol/qbic_field_comparison.png`
- `outputs/comsol/qbic_tri_side_grid.csv`
- `outputs/comsol/qbic_tri_side_sensitivity.csv`
- `outputs/comsol/qbic_tri_side_sensitivity.png`
- `outputs/comsol/qbic_tri_side_R_heatmap.png`
- `outputs/comsol/qbic_tri_side_F4_norm_heatmap.png`
- `outputs/python/tcmt_q_tradeoff.png`
- `outputs/python/tcmt_detuning_map.png`
- `outputs/python/tcmt_qbic_asymmetry.png`

## Key Numerical Markers

From `outputs/comsol/qbic_peak_summary.txt`:

- Reflectance peak: 849 nm, `R = 0.9971797801526613`.
- MoS2-domain F4 proxy peak: 843 nm.
- Low-F4 reference point: 811 nm.
- Reflectance spectral-width proxy: `Q = 30.596087239711714`.

From `outputs/python/tcmt_q_tradeoff_optimum.csv`:

- Useful-SHG proxy optimum: `gamma_e/gamma_i ≈ 1.49`.

## Historical Outputs

The following outputs are historical and are kept for traceability, but they are not used in the final paper or final package:

- `outputs/comsol/qbic_refined_800_840nm.*`
- `outputs/comsol/qbic_field_resonance.png`
- `outputs/comsol/qbic_field_off_resonance.png`

## Final Package Exclusions

The clean package should exclude development traces and stale conflict outputs:

- `.agents/`, `.claude/`, `.codex/`, `.trellis/`
- `scripts/__pycache__/`
- `hs_err_pid*.log`
- historical files listed above

## Interpretation Limits

The COMSOL model is a qBIC-inspired teaching-level trend model. It uses simplified, lossless, wavelength-independent optical constants. The MoS2-domain F4 quantity is a linear-field source-strength proxy, not a full SHG conversion efficiency. The reported Q is a reflectance spectral-width proxy, not a fitted qBIC modal Q.
