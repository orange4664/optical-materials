# Progress

## 2026-06-12

- User approved execution with two constraints:
  - COMSOL-first simulation is mandatory.
  - Do not use COMSOL GUI; use direct Python `mph` scripts only.
- Environment smoke test passed:
  - Python 3.13.3
  - `mph` 1.3.1
  - COMSOL 6.3
  - Wave Optics module available.
- Added scripts:
  - `scripts/comsol_smoke.py`
  - `scripts/build_qbic_model.py`
  - `scripts/run_qbic_model.py`
- Generated scripted COMSOL model:
  - `outputs/comsol/qbic_3r_mos2_unitcell.mph`
  - `outputs/comsol/qbic_3r_mos2_unitcell.java`
- Current qBIC scaffold includes:
  - 500 nm periodic unit cell.
  - 25 nm 3R-MoS2 film.
  - 374 nm equilateral triangular through-hole.
  - Air superstrate and SiO2 substrate.
  - Domain box selections for Air, MoS2, and SiO2.
  - Boundary box selections for top/bottom ports and x/y periodic sidewalls.
  - EWFD physics, periodic ports, Floquet periodic conditions.
  - User-controlled tetrahedral mesh.
- Verified:
  - Geometry builds.
  - Mesh builds.
  - Single-wavelength solve at 850 nm runs without reported problems.
  - Domain-dependent wave equations now use separate optical proxies:
    - Air: epsilonr = 1.
    - SiO2: epsilonr = 2.1025.
    - 3R-MoS2 proxy: epsilonr = 17.64.
  - Coarse wavelength sweep from 780 nm to 900 nm runs successfully.
  - Exported spectrum:
    - `outputs/comsol/qbic_spectrum_780_900nm.csv`
    - `outputs/comsol/qbic_spectrum_780_900nm.png`
  - The coarse sweep shows a strong reflectance peak and transmission dip near 820 nm.
  - Refined sweep from 800 nm to 840 nm in 5 nm steps completed:
    - `outputs/comsol/qbic_refined_800_840nm.csv`
    - `outputs/comsol/qbic_refined_800_840nm.png`
    - `outputs/comsol/qbic_peak_summary.txt`
  - Refined sweep includes sampled `max |E|`, a `max |E|^4` SHG proxy column, and a coarse Q estimate.

## Current Caveats

- Optical constants are simplified, wavelength-independent proxies; final paper text must label them as a pedagogical model, not quantitative reproduction.
- The Q estimate is coarse because it uses a 5 nm wavelength grid and simple half-width logic.
- The `|E|^4`-style SHG proxy is based on sampled maximum field values, not a volume integral over the MoS2 domain.
- Field-map export is still a useful optional enhancement if the task continues into full paper-figure generation.
