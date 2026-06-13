# Implementation Plan

## Ordered Work

1. Activate task with `task.py start`.
2. Load `trellis-before-dev` before editing scripts/paper files.
3. Reuse existing COMSOL qBIC outputs:
   - coarse spectrum.
   - refined spectrum.
   - Q summary.
   - field proxy CSV.
4. Add missing Python TCMT script and figures:
   - `outputs/python/tcmt_q_tradeoff.png`
   - `outputs/python/tcmt_detuning_map.png` if feasible.
5. Add a small parameter-scan or sensitivity figure:
   - Prefer using existing qBIC model with triangle side variations.
   - If time is too high, produce a clearly labeled reduced scan or theoretical/schematic sensitivity analysis.
6. Draft `course_paper.md`:
   - title and abstract.
   - introduction.
   - nonlinear optics/course connection.
   - literature route and table.
   - physical mechanism.
   - COMSOL method/results.
   - Python TCMT method/results.
   - improvement proposals and limitations.
   - conclusion.
   - references.
7. Optional conversion to `.docx` if tooling is available and time permits.
8. Run quality checks:
   - `python -m py_compile scripts/*.py` or explicit script list.
   - check generated figure paths.
   - paper completeness checklist.
   - citation/reference sanity check.
9. Update Trellis progress and spec if any new implementation lessons appear.
10. Finish-work/archive after checks pass.

## Files Expected To Change

- `course_paper.md`
- `scripts/*.py`
- `outputs/comsol/*`
- `outputs/python/*`
- `.trellis/tasks/06-12-full-gpt-pro-paper-delivery/*`

## Validation Commands

- Python syntax:
  - `python -m py_compile scripts/comsol_smoke.py scripts/build_qbic_model.py scripts/run_qbic_model.py scripts/evaluate_qbic_model.py scripts/sweep_qbic_spectrum.py scripts/plot_qbic_spectrum.py scripts/refine_qbic_peak.py`
- TCMT script:
  - `python scripts/tcmt_analysis.py`
- Existing COMSOL output checks:
  - validate CSV row counts and `R + T`.
- Paper checks:
  - search for all section headings.
  - verify all figure files referenced in the paper exist.
  - verify references section includes every cited key source.

## Risk / Downgrade Rules

- COMSOL parameter scan may be slow.
  - Downgrade to 3-point sensitivity scan or clearly labeled theoretical sensitivity discussion.
- Field-map export may be difficult through `mph`.
  - Use refined spectrum with `max |E|`/`max |E|^4` proxy and state limitation.
- Full Word `.docx` conversion may require extra tooling.
  - Deliver Markdown draft first; convert only if available.
- Exact quantitative reproduction is not required.
  - Label all simplified material constants and proxy models.
