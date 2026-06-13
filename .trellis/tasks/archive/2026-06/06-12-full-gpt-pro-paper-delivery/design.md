# Design

## Deliverable Shape

Primary deliverable:

- `course_paper.md` or `course_paper.docx` draft in Chinese.

Supporting deliverables:

- `figures/` or `outputs/` figure assets.
- COMSOL scripts and outputs under `scripts/` and `outputs/comsol/`.
- Python TCMT scripts and outputs under `scripts/` and `outputs/python/`.
- Reference list with verified citation metadata.

## Paper Argument

Central thesis:

> Two-dimensional TMDs have large second-order nonlinear susceptibility but limited conversion efficiency because the optical interaction length is atomically thin. Resonant van der Waals metasurfaces, especially 3R-MoS2 qBIC/anapole structures, enhance SHG by increasing local fields and controlling out-coupling. However, the best design is not simply the largest Q factor; it balances field enhancement, radiation, bandwidth, absorption, and fabrication tolerance.

## Content Hierarchy

- Main platform: ultrathin 3R-MoS2 qBIC metasurface.
- Mechanism explanation: 3R-MoS2 nanodisk anapole.
- Historical route:
  - external metasurface + monolayer TMD.
  - all-TMD resonators/metasurfaces.
- Comparison route: WS2/MoS2 interface SHG nanoantenna.
- Outlook: non-local 3R-MoS2 metasurface.

Nothing from Word is deleted. Material is assigned to one of:

- Main evidence.
- Mechanism support.
- Historical background.
- Comparison.
- Outlook.

## Figure/Table Plan

Required:

- Figure 1: mechanism schematic or route diagram for SHG enhancement in TMD metasurfaces.
- Table 1: representative literature comparison.
- Figure 2: existing qBIC COMSOL reflectance/transmittance spectrum.
- Figure 3: refined qBIC spectrum with field proxy.
- Figure 4: Python TCMT plot showing Q/detuning/coupling trade-off.

Optional if time allows:

- Parameter scan figure for triangle side length/period/thickness.
- Nanodisk/anapole simplified proxy figure.
- WS2/MoS2 interface-source versus body-source schematic/proxy.

## Simulation Strategy

### COMSOL

Use existing pure-script `mph` qBIC scaffold as the main simulation evidence.

Must include in paper:

- Geometry and boundary-condition description.
- Material proxy limitations.
- Reflection/transmission spectrum.
- Refined peak/Q estimate.
- Field enhancement or `|E|^4` proxy.

Reduced parameter scan:

- Prefer triangle side length scan if feasible because it maps directly to the Word requirements.
- If full COMSOL parameter scan is too slow, run a small 3-point scan and label it as sensitivity demonstration.

Nanodisk/anapole:

- If full nanodisk COMSOL is too costly, include it as a literature-backed mechanism case with a schematic/proxy explanation, not as the main simulation.

WS2/MoS2:

- Include as comparison of source term:
  - body-source proxy for 3R-MoS2.
  - interface-source proxy for heterobilayer.

### Python TCMT

Create deterministic plots:

- single-resonance SHG proxy vs detuning for several Q values.
- SHG peak/bandwidth trade-off versus Q.
- external coupling trade-off.

These plots are explanatory and do not claim to reproduce a specific paper.

## Writing Constraints

- Chinese academic prose.
- Avoid overclaiming quantitative agreement with experiments.
- Explain all simplified models.
- Keep formulas readable in Markdown/Word form.
- Use citations near claims, not only in a final bibliography.

## Quality Gates

- All scripts compile.
- All referenced figures/tables exist.
- Paper contains all required sections.
- Paper explicitly includes:
  - course connection.
  - literature route A-D and outlook.
  - COMSOL results.
  - Python TCMT results.
  - Q-factor trade-off conclusion.
  - limitations.
- References are traceable to verified sources.
