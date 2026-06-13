# Progress

## 2026-06-12

Completed full GPT Pro course-paper delivery scope:

- Created complete Chinese paper draft:
  - `course_paper.md`
- Reused existing COMSOL qBIC outputs:
  - `outputs/comsol/qbic_spectrum_780_900nm.png`
  - `outputs/comsol/qbic_refined_800_840nm.png`
  - `outputs/comsol/qbic_peak_summary.txt`
- Added qBIC triangle-side sensitivity scan:
  - `scripts/qbic_sensitivity_scan.py`
  - `outputs/comsol/qbic_tri_side_sensitivity.csv`
  - `outputs/comsol/qbic_tri_side_sensitivity.png`
- Added Python TCMT analysis:
  - `scripts/tcmt_analysis.py`
  - `outputs/python/tcmt_q_tradeoff.png`
  - `outputs/python/tcmt_detuning_map.png`
  - `outputs/python/tcmt_qbic_asymmetry.png`
  - `outputs/python/tcmt_summary.txt`

Paper content includes:

- Topic/title/abstract.
- Course connection to nonlinear optics, reflectance/transmission, and low-dimensional optical measurement.
- Literature route A-D and outlook.
- Literature comparison table.
- Physical mechanism section covering Mie, anapole, qBIC, exciton resonance, and optimal Q trade-off.
- COMSOL method/results with limitations.
- Python TCMT method/results.
- WS2/MoS2 interface SHG comparison.
- Improvement proposals and limitations.
- References.

Validation:

- Python scripts compile.
- All paper image paths exist.
- Required paper sections exist.
- COMSOL CSV files have expected row counts and `R + T` close to 1 for the simplified lossless proxy model.

Known limitations:

- `course_paper.md` is a complete draft, not university-template formatted `.docx`.
- COMSOL constants are simplified and wavelength-independent.
- `max |E|^4` is a sampled maximum-field proxy, not a volume-integrated nonlinear source.
- Nanodisk/anapole and WS2/MoS2 are retained as mechanism/comparison discussions rather than full additional COMSOL models.
