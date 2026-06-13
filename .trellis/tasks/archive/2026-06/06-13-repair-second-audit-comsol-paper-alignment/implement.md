# Implementation Plan

## Step Order

1. Inspect current scripts, Java export, refined CSV, field figures, TCMT output, paper, and second audit report.
2. Patch COMSOL build script:
   - bind `wee1` to `sel_air`;
   - keep air-hole fix intact;
   - rebuild `.mph` and `.java`.
3. Patch refined sweep/metrics scripts:
   - compute normalized/log F4 columns;
   - identify R peak, F4 peak, and low-F4 wavelengths;
   - generate normalized refined spectrum plot.
4. Patch field-map export:
   - generate R-peak, F4-peak, and low-F4 maps;
   - enforce common color scale or document individual scaling;
   - write a multi-panel comparison figure.
5. Patch side-length scan:
   - write full grid CSV;
   - write summary CSV with best-R and best-F4 fields;
   - generate R and F4_norm heatmaps.
6. Patch TCMT:
   - replace right panel with `gamma_e/gamma_i` coupling-ratio optimum;
   - update CSV summary for optimum ratio.
7. Update paper:
   - soften qBIC/replication/Q language;
   - add reflection-vs-F4 mismatch analysis;
   - use new normalized figures and field comparison;
   - add course link and final-format metadata/cover placeholders;
   - update limitations.
8. Add/update `RUNS.md` and clean final delivery directory/list.
9. Validate scripts, outputs, images, DOCX/PDF export status, and Trellis acceptance criteria.
10. Archive task with `--no-commit` if root remains non-git.

## Validation Commands

```powershell
python -m py_compile scripts\build_qbic_model.py scripts\qbic_metrics.py scripts\refine_qbic_peak.py scripts\export_qbic_field_maps.py scripts\qbic_sensitivity_scan.py scripts\tcmt_analysis.py
python scripts\build_qbic_model.py
python scripts\run_qbic_model.py
python scripts\evaluate_qbic_model.py
python scripts\refine_qbic_peak.py
python scripts\export_qbic_field_maps.py
python scripts\qbic_sensitivity_scan.py
python scripts\tcmt_analysis.py
pandoc course_paper.md -o outputs\paper\course_paper.docx --resource-path='.;outputs;outputs\comsol;outputs\python'
```

If the side scan is too slow, run a reduced grid only after recording the exact reduction and keeping the full-grid script.

## Review Gates

- Do not start long COMSOL reruns until `wee1` domain binding is verified in the Java export.
- Do not update paper claims until the new refined CSV identifies both R and F4 peaks.
- Do not cite a field comparison unless all referenced image files exist and are non-empty.
- Do not claim PDF export if Pandoc/LaTeX cannot produce it.

## Rollback Points

- If binding `wee1` to `sel_air` breaks solve, inspect generated Java selections before changing geometry.
- If field maps remain visually misleading, use normalized/log multi-panel plots and describe them as sampled qualitative diagnostics.
- If COMSOL runtime is prohibitive, keep code changes, document skipped commands, and adjust paper to avoid unsupported claims.
