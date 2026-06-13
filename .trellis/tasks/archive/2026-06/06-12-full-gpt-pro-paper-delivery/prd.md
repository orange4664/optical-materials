# 完成 GPT Pro 课程论文全交付

## Goal

完成 `低维材料论文方向审计与结论.docx` 中 GPT Pro 方案要求的完整课程论文交付，而不是只完成选题审计或单个 COMSOL scaffold。最终成果应是一篇可提交的中文课程论文草稿，围绕 3R-MoS2/TMD 范德华超表面中的共振增强二次谐波，包含文献主线、COMSOL 仿真结果、Python TCMT 分析、改进方案与局限、图表和参考文献。

## User Requirements

- 课程作业要求：
  - 结合课程内容，自主选择相关 topic。
  - 完成一篇符合学术论文基本规范的课程论文。
  - 可包含图片、示意图、实验结构图等。
  - 内容需具有分析与思考，避免简单资料堆砌。
- 用户已明确：
  - 必须完成 GPT Pro Word 方案里的全部要求，而不是只做 qBIC 起步。
  - 仿真必须做。
  - Word 中各路线和内容都不要删除。
  - COMSOL 先行。
  - 不使用 COMSOL GUI，使用 Python `mph` 脚本。

## Source Word Requirements

### Topic and Title

- Final topic: resonantly enhanced SHG in 2D van der Waals/TMD metasurfaces.
- Recommended title: `超薄 3R-MoS2 范德华超表面中二次谐波共振增强机制及其数值复现`
- Optional subtitle: `从 qBIC 局域场增强到最优 Q 因子分析`

### Literature Narrative

Keep all routes, but assign hierarchy:

- Route A: external metasurface-enhanced monolayer TMD.
- Route B: TMD itself as Mie/anapole resonator.
- Route C: 3R-MoS2 as recent core platform, including nanodisk anapole and ultrathin qBIC metasurface.
- Route D: WS2/MoS2 interface SHG plus exciton resonance as comparison.
- Outlook: non-local 3R-MoS2 metasurface and integrated nonlinear sources.

### Required Literature Table

The paper should include a comparison table covering:

- Zeng et al., Frontiers of Physics, 2024, nonlinear optics of 2D heterostructures.
- Zograf et al., Nature Photonics, 2024, 3R-MoS2 nanodisks.
- Zograf et al., Communications Physics, 2025, ultrathin 3R-MoS2 qBIC metasurfaces.
- Tognazzi et al., Light: Science & Applications, 2025, WS2/MoS2 interface SHG nanoantennas.
- Peng et al., Nature Photonics, 2025, 3R-MoS2 non-local metasurface.
- Background references: Verre 2019, Bernhardt 2020, Busschaert 2020, Nauman 2021, Huang 2024.

### Review/Theory Content

- Explain why 2D TMDs can have strong SHG but low conversion efficiency.
- Compare 2H and 3R stacking, especially inversion symmetry.
- Explain why 3R-MoS2 is suitable for nonlinear metasurfaces.
- Build the shared framework: material nonlinearity, local-field enhancement, Q factor, out-coupling, bandwidth, absorption, and fabrication tolerance.
- Explicitly argue that SHG enhancement is not simply “larger Q is always better.”

### COMSOL Requirements

Keep both basic and advanced routes:

- Basic route: 3R-MoS2 nanodisk anapole.
  - Geometry: disk radius scan 150-220 nm, thickness around 65 nm, substrate, normal incidence around 850-1000 nm.
  - Outputs: spectrum, field distribution, stored-energy or field proxy, SHG proxy.
- Advanced route: ultrathin 3R-MoS2 triangular-hole qBIC metasurface.
  - Geometry: 20-25 nm film, period around 500 nm, triangular hole side around 373-375 nm, substrate, wavelength 780-900 nm.
  - Boundaries: x/y Floquet periodic, top/bottom port or PML.
  - Outputs: reflectance/transmittance spectrum, resonance wavelength, approximate Q, field map, SHG proxy.
  - Parameter scans: triangular-hole size 340-390 nm, period 480-520 nm, thickness 20-25 nm, corner radius 0-10 nm, sidewall angle 75-90 degrees.
- Optional comparison: WS2/MoS2 interface SHG proxy model, comparing body-source and interface-source proxies.

### Python/TCMT Requirements

Python should support interpretation, not duplicate COMSOL:

- Single-resonance TCMT: SHG proxy vs detuning, Q, and bandwidth.
- Double-resonance TCMT: pump and second-harmonic mode detuning map.
- External coupling/Q analysis: show under-coupling/over-coupling trade-off.
- qBIC asymmetry parameter model: enhancement versus bandwidth/tolerance.

### Paper Structure

Final paper draft should include:

- Title.
- Abstract.
- Introduction.
- Nonlinear optics fundamentals and course connection.
- Literature review: route evolution and comparison table.
- Physical mechanism: Mie/anapole/qBIC/exciton resonance and SHG enhancement.
- COMSOL model and results.
- Python TCMT model and results.
- Improvement proposals and limitations.
- Conclusion.
- References.

## Existing Reusable Work

Already generated in the previous narrow task:

- Pure Python `mph` qBIC COMSOL scaffold.
- `outputs/comsol/qbic_3r_mos2_unitcell.mph`
- `outputs/comsol/qbic_spectrum_780_900nm.csv/png`
- `outputs/comsol/qbic_refined_800_840nm.csv/png`
- `outputs/comsol/qbic_peak_summary.txt`
- Coarse qBIC peak near 830 nm, estimated Q about 33.2.
- Sampled `max |E|` and `max |E|^4` proxy values.

These are reusable but incomplete relative to the Word requirements.

## Acceptance Criteria

- [x] Produce a complete Chinese course-paper draft in editable format.
- [x] Include all major Word routes A-D and outlook, without deleting them.
- [x] Include a literature comparison table.
- [x] Verify key references and produce a references section with usable citation metadata.
- [x] Include COMSOL qBIC results already generated, with limitations stated.
- [x] Add missing COMSOL/Python deliverables or justified simplified equivalents:
  - [x] nanodisk/anapole route figure or simulation/proxy discussion.
  - [x] qBIC spectrum, Q estimate, and field/SHG proxy figure.
  - [x] at least one parameter scan or a clearly labeled reduced scan.
  - [x] Python TCMT figures for Q/detuning/coupling trade-off.
  - [x] WS2/MoS2 comparison as mechanism/proxy discussion.
- [x] Include analysis that explicitly argues why optimal Q is a trade-off, not maximization.
- [x] Use generated figures/tables in the paper with captions.
- [x] Clearly label simplified models and avoid claiming quantitative reproduction beyond evidence.
- [x] Run quality checks: script syntax, generated artifact existence, paper completeness checklist.

## Out of Scope

- Full nonlinear Maxwell solution of absolute SHG conversion efficiency.
- Perfect quantitative reproduction of published data.
- COMSOL GUI interaction.
- Submission-ready formatting to a specific university template unless separately requested.
