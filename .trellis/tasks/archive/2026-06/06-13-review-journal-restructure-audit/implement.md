# Implementation Plan

## Step Order

1. Read project specs before implementation:
   - `.trellis/spec/guides/index.md`
   - `.trellis/spec/backend/index.md`
   - relevant backend guidelines for CSV/data outputs, quality, and logging.
2. Create review artifact folders without deleting existing course-paper outputs:
   - `manuscripts/` or root-level `review_manuscript.md`
   - `outputs/review/`
3. Build `literature_database.csv`:
   - seed from current 10 course-paper references;
   - keep a curated starter seed focused on the papers needed for this scaffold;
   - include DOI/URL or stable bibliographic metadata.
4. Create review manuscript scaffold:
   - English title and alternative title;
   - English abstract;
   - journal-target positioning note;
   - required section headings;
   - Box placement for minimal modelling;
   - COMSOL demotion language.
5. Create FoM and pitfalls assets:
   - `outputs/review/fom_comparison_pitfalls.csv` or Markdown table;
   - define enhancement factor, absolute conversion efficiency, single-pass efficiency, pump fluence, pulse duration, repetition rate, collection NA, reference baseline.
6. Create representative literature table:
   - generated or manually curated from `literature_database.csv`;
   - cover all required platform categories.
7. Create display item plan:
   - at least 6 display items with captions, evidence source, and status;
   - generate simple Markdown/CSV tables now, schematic image generation only if time permits and does not distract from manuscript structure.
8. Optionally create clean English TCMT review figure:
   - do not run COMSOL;
   - use existing Python-only TCMT logic or new review plotting script.
9. Create `REVIEW_RUNS.md`:
   - distinguish review manuscript from course paper;
   - list current review artifacts;
   - state COMSOL is Box/Supplementary only.
10. Validate:
   - `task.py validate`;
   - CSV columns and row count;
   - manuscript required headings and absence of course metadata;
   - Markdown links/paths;
   - Python syntax for any new scripts.
11. Ask user for review before `task.py start`, then start implementation only after explicit approval.

## Validation Commands

```powershell
python ./.trellis/scripts/task.py validate .trellis/tasks/06-13-review-journal-restructure-audit
python - <<'PY'
import pandas as pd
df = pd.read_csv('literature_database.csv')
required = {
    'id','year','authors','title','venue','material_platform',
    'dimensionality_or_source_type','resonance_mechanism',
    'nonlinear_process','metric_reported','baseline_or_reference',
    'pump_condition_note','device_geometry','key_message',
    'role_in_review','doi_or_url'
}
assert len(df) >= 15
assert required <= set(df.columns)
PY
```

If new Python scripts are added:

```powershell
python -m py_compile scripts\<new_script>.py
```

If DOCX export is requested:

```powershell
pandoc review_manuscript.md -o outputs\review\review_manuscript.docx --resource-path='.;outputs;outputs\review;outputs\python'
```

## Review Gates

- Do not start implementation until the user approves the planning artifacts.
- Do not stop or restart any COMSOL/Python process.
- Do not present the starter literature database as exhaustive; label it a first structured seed and leave broad expansion as follow-up work.
- Do not include current COMSOL figures in main-text display items unless explicitly captioned as illustrative Box/Supplementary material.
- Do not fabricate bibliographic data. If DOI is unknown, use a stable URL and mark missing DOI explicitly.

## Rollback Points

- If literature expansion is too slow or search quality is poor, keep the curated starter seed and mark broad bibliography expansion as follow-up work.
- If display-item generation takes too long, complete figure plans and tables first; full polished schematics can be a follow-up child task.
- If manuscript scope grows beyond first-stage scaffold, keep this task to scaffold + database + tables and create a child task for full prose expansion.
