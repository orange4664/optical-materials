# 课程论文方向审计 Design

## Scope

Plan a course-paper direction that keeps every major route in the DOCX while preventing the paper from becoming a flat survey. The paper will be structured around one central question:

> How do resonant nanophotonic modes in 3R-MoS2 / TMD van der Waals metasurfaces enhance SHG, and why is the best design not simply the largest Q factor?

## Content Architecture

Use a layered narrative:

- Main case: ultrathin 3R-MoS2 qBIC metasurface.
  - Owns the core simulation and main mechanism discussion.
  - Connects directly to reflectance/transmission, field localization, nonlinear optics, and low-dimensional optical measurement.
- Mechanism case: 3R-MoS2 nanodisk anapole resonance.
  - Explains internal field enhancement despite weak far-field scattering.
  - Supports interpretation of why a resonance can enhance SHG.
- Comparison case: WS2/MoS2 interface SHG nanoantenna.
  - Compares body non-centrosymmetry in 3R-MoS2 with interface symmetry breaking in hetero-bilayers.
  - Stays as a mechanism comparison, not a second full simulation target.
- Background route: monolayer TMD plus external metasurface and all-TMD Mie resonator literature.
  - Establishes technology evolution.
  - Does not compete with the main case for page budget.
- Outlook route: non-local 3R-MoS2 metasurface and integrated nonlinear sources.
  - Used for final discussion of efficiency, bandwidth, and device relevance.

## COMSOL-First Simulation Design

Implementation route:

- Use the Python `mph` package as the primary COMSOL control interface.
- Script model creation, parameter assignment, solve, and export where practical.
- Do not use COMSOL GUI. If qBIC model construction is too slow or opaque through `mph`, downgrade to a simpler scripted model.
- Keep `cli-anything-mph` as a fallback inspection/solve/export tool, not the primary path.

Primary COMSOL target:

- Linear optical model of the 3R-MoS2 qBIC metasurface unit cell.
- Geometry:
  - 3R-MoS2 film thickness around 20-25 nm.
  - Period around 500 nm.
  - Equilateral triangular hole with side length around 373-375 nm.
  - Glass or SiO2 substrate.
- Excitation:
  - Normal-incidence plane wave or port excitation.
  - Wavelength scan around 780-900 nm.
  - Periodic/Floquet lateral boundaries and open/PML or port boundaries vertically.
- Required outputs:
  - Reflection or transmission spectrum.
  - Resonance wavelength and approximate linewidth/Q.
  - Electric-field map near resonance.
  - Field-enhancement proxy, preferably a volume or domain integral related to `|E|^4`, as a qualitative SHG proxy.

Secondary COMSOL target if qBIC model is too hard to build quickly:

- 3R-MoS2 nanodisk anapole model.
- Required outputs:
  - Scattering or extinction-like spectral trend.
  - Internal electric-field map at resonance.
  - Qualitative field-enhancement proxy.

This fallback still supports the central physics and keeps the qBIC structure in the paper as literature-backed analysis.

## Python Role

Python is secondary:

- Use TCMT to explain the Q-factor trade-off after COMSOL establishes resonant field enhancement.
- Produce simple plots for SHG proxy versus detuning, loaded Q, and external coupling.
- Do not present Python as replacing the COMSOL simulation.

## Compatibility With Course Requirements

- Academic-paper format: use title, abstract, introduction, theory, literature route, simulation method, results/discussion, limitations, conclusion, references.
- Figures:
  - Literature comparison schematic/table.
  - qBIC/anapole geometry schematic.
  - COMSOL reflection/transmission spectrum.
  - COMSOL field map.
  - Optional Python TCMT curve.
- Analysis beyond aggregation:
  - Explain baseline differences in reported enhancement factors.
  - Compare body SHG and interface SHG.
  - Argue the Q-factor optimum trade-off: enhancement, bandwidth, out-coupling, absorption, and fabrication tolerance.

## Risks And Downgrades

- Risk: full qBIC periodic COMSOL model is slow or difficult.
  - Downgrade: use anapole nanodisk COMSOL as the required simulation and keep qBIC as literature main case with parameter discussion.
- Risk: no reliable nonlinear material tensor data.
  - Downgrade: use linear field proxy only, explicitly label it as a SHG trend proxy.
- Risk: CLI-based construction is not desired and not the main route.
  - Downgrade: use direct `mph` Python API only; if qBIC node construction is blocked, switch to a simpler fully scripted COMSOL model.
- Risk: direct `mph` model construction requires verbose Java API calls.
  - Downgrade: simplify the scripted target to a nanodisk/anapole or slab resonance model that can still demonstrate resonant field enhancement.
- Risk: scope is too wide.
  - Downgrade: keep all routes but enforce role hierarchy: background, main case, mechanism case, comparison, outlook.
