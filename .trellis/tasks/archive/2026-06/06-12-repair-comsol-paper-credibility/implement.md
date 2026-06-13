# Implementation Plan

## Ordered Steps

1. Read current Word audit, Markdown draft, COMSOL scripts, generated CSV/PNG outputs, and Trellis/backend specs.
2. Patch `scripts/build_qbic_model.py`:
   - add triangular air-fill domain,
   - split/union air selections,
   - add MoS2 field coupling operators where possible,
   - save `.mph` and `.java` exports.
3. Patch COMSOL analysis scripts:
   - replace full-domain `max |E|^4` claims with MoS2-domain or sampled film proxies,
   - refine wavelength sweep and Q summary,
   - generate field maps from sampled `|E|^2`,
   - extend triangle-side scan to at least 7 points.
4. Run build/mesh/solve/sweep scripts as far as the local COMSOL environment permits.
5. Regenerate TCMT figure/data if needed to mark the simplified COMSOL Q on the explanatory plot.
6. Update `course_paper.md`:
   - formalize academic structure,
   - update figure references and captions,
   - add simplified-model limitations,
   - avoid overclaiming quantitative reproduction.
7. Validate:
   - `python -m py_compile` on modified scripts,
   - expected output files exist and are non-empty,
   - Markdown image paths resolve,
   - generated CSV headers contain units/proxy naming,
   - paper language does not claim true SHG efficiency reproduction.
8. Record final verification and known limitations in this task.

## Validation Commands

```powershell
python -m py_compile scripts\build_qbic_model.py scripts\refine_qbic_peak.py scripts\qbic_sensitivity_scan.py scripts\tcmt_analysis.py
python scripts\build_qbic_model.py
python scripts\run_qbic_model.py
python scripts\refine_qbic_peak.py
python scripts\qbic_sensitivity_scan.py
python scripts\tcmt_analysis.py
```

If COMSOL solve time is too high, run at minimum:

```powershell
python scripts\build_qbic_model.py
python scripts\run_qbic_model.py
python scripts\evaluate_qbic_model.py
```

## Rollback Points

- If the repaired geometry fails to build, inspect the Java export and revert only the geometry changes made in this task.
- If COMSOL coupling operators are unsupported, keep the corrected geometry and switch only the proxy-evaluation path to sampled film points.
- If the local COMSOL environment blocks solving, keep scripts and paper caveats, and record the exact failing command/message.
