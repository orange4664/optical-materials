# 课程论文方向审计 Implementation Plan

## Ordered Checklist

1. Confirm paper title and central question.
   - Recommended title: `超薄 3R-MoS2 范德华超表面中二次谐波共振增强机制及其数值复现`
   - Central question: resonant SHG enhancement and optimal-Q trade-off in 3R-MoS2/TMD metasurfaces.

2. Prepare COMSOL-first baseline.
   - Use the Python `mph` package as the primary COMSOL interface.
   - Check that `import mph` works and that `mph.start()` can launch a COMSOL session.
   - Create a scripted qBIC unit-cell `.mph` model if practical.
   - Do not use COMSOL GUI. If qBIC construction through `mph` is too verbose, downgrade to a simpler fully scripted COMSOL model.

3. Build required qBIC simulation.
   - Geometry: 20-25 nm 3R-MoS2 film, about 500 nm period, triangular hole about 373-375 nm, glass/SiO2 substrate.
   - Physics: frequency-domain electromagnetic wave optics.
   - Boundary conditions: lateral Floquet/periodic boundaries; vertical port/PML/open boundaries.
   - Sweep: 780-900 nm or equivalent frequency range.
   - Outputs: reflection/transmission spectrum, field map at resonance, approximate Q, `|E|^4` or equivalent field-enhancement proxy.

4. If qBIC model blocks progress, execute fallback simulation.
   - 3R-MoS2 nanodisk anapole resonance.
   - Outputs: spectral resonance/scattering trend, internal field map, field-enhancement proxy.
   - Keep qBIC as main literature case, and state the simulation reproduces the simpler mechanism case.

5. Add Python TCMT only after COMSOL baseline exists.
   - Plot SHG proxy versus detuning.
   - Plot SHG proxy versus Q or external coupling.
   - Use it to support the “Q is not simply larger-is-better” conclusion.

6. Draft paper structure.
   - Abstract.
   - Introduction: low-dimensional TMD SHG strength versus thinness limitation.
   - Theory/course link: SHG, symmetry breaking, optical resonances, reflectance/transmission.
   - Literature route: external metasurface -> all-TMD resonator -> 3R-MoS2 qBIC/anapole -> interface SHG -> non-local metasurface.
   - COMSOL simulation method/results.
   - Python TCMT analysis if available.
   - Discussion: enhancement factor baselines, body/interface SHG, Q/bandwidth/out-coupling/fabrication tolerance.
   - Conclusion.

7. Final checks.
   - Ensure all DOCX content lines are retained as main/background/comparison/outlook rather than deleted.
   - Ensure the simulation is clearly described as linear-field/proxy analysis unless a full nonlinear solve is actually completed.
   - Verify reference details for all key papers before final bibliography.

## Validation Commands

- Python/MPh import check:
  - `python -c "import mph; print(mph.__version__)"`
- COMSOL session smoke test:
  - `python -c "import mph; mph.option('session','stand-alone'); client=mph.start(cores=1); print(client)"`
- Model automation pattern:
  - `client = mph.start(cores=1)`
  - `model = client.create('qBIC_3R_MoS2')` or `model = client.load('model.mph')`
  - `model.parameter('period', '500[nm]')`
  - `model.build()`
  - `model.mesh()`
  - `model.solve()`
  - `model.evaluate('<expression>')`
  - `model.save('output.mph')`

Note: `mph` 1.3.1 imports successfully in Python 3.13 on this machine. `cli-anything-mph` is installed but should be treated as fallback only because the user prefers direct `mph` use.

## Risk Points

- COMSOL model creation through CLI may be limited.
- Direct `mph` model construction may require low-level Java node/property calls.
- GUI use is disallowed by user preference, so every fallback must remain script-based.
- Periodic electromagnetic boundary setup is the most likely source of delay.
- Material constants and nonlinear tensor values may be incomplete.
- A full SHG conversion-efficiency solve is likely too large for a course-paper timeline.

## Rollback Points

- If qBIC periodic model fails: switch to nanodisk anapole model for COMSOL output.
- If direct `mph` construction fails for qBIC: switch to a simpler fully scripted COMSOL geometry such as nanodisk/anapole or slab resonance.
- If COMSOL output is incomplete: keep geometry/spectrum screenshots plus Python TCMT curves as supplementary analysis, but label limitations clearly.
- If all model building fails: use a simpler electromagnetic resonance model only after documenting why qBIC construction was blocked.
