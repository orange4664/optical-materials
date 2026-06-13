# 课程论文方向审计

## Goal

评估 `低维材料论文方向审计与结论.docx` 中提出的课程论文方向是否适合本门“低维材料”课程作业，并给出可执行的收束建议：是否采用、采用哪个题目、保留哪些主线、哪些内容需要降级或删去。

## Requirements

- 判断选题与课程内容的贴合度，尤其是非线性光学、反射/透射、Raman/光学测量、超快光学、光电流/lock-in、低维材料光学测量等课程主题的关联。
- 判断文档方案是否满足课程论文要求：符合学术论文规范，可包含图示/结构图/仿真图，必须有分析与思考，避免简单资料堆砌。
- 审核文档中推荐的核心主题是否过大、过新、过难或偏离课程。
- 核验关键文献主线是否基本真实可靠，避免建立在不存在或不适合的论文上。
- 给出一个明确结论：适合、不适合，或适合但需要收窄。
- 给出下一步论文写作范围建议，包括题目、核心问题、章节骨架、仿真/模型工作的最低可交付版本。
- 用户已明确要求：仿真必须做；DOCX 中列出的文献路线和内容都不要删除。规划需要在“全部保留”的前提下做层级安排，而不是删减范围。

## Acceptance Criteria

- [x] 明确回答该方向是否适合作为课程论文 topic。
- [x] 说明适合或不适合的主要理由，至少覆盖课程贴合度、分析深度、可完成性和风险。
- [x] 指出文档方案中应保留的主线和应压缩/删除的部分。
- [x] 给出推荐题目和最低可行论文结构。
- [x] 提出一个仍需用户决定的最高价值问题，并给出推荐答案。
- [x] 将所有拟保留内容分配到主线、对照、背景或展望位置，避免正文变成平铺综述。
- [x] 明确仿真的必做交付物、可选增强项和失败降级方案。
- [x] 在“必须仿真、保留全部内容、COMSOL 先行、不使用 GUI”的约束下完成纯脚本 COMSOL qBIC scaffold。

## Notes

Confirmed facts:

- User course assignment asks for a self-chosen course-related topic, academic-paper style writing, optional figures/schematics/experimental structures, and analysis beyond source aggregation.
- Course schedule includes solid-state physics, optical properties of solids, reflectance/transmission, Raman spectroscopy, nonlinear optics, ultrafast optics, photocurrent/lock-in, and optical measurement in low-dimensional materials.
- The DOCX is not a finished paper; it is a detailed topic audit and writing plan.
- The DOCX recommends focusing on resonantly enhanced second-harmonic generation in 3R-MoS2 / TMD van der Waals metasurfaces, especially qBIC/anapole mechanisms and an “optimal Q factor” argument.
- The DOCX proposes a small review plus simplified COMSOL/Python modeling, not a broad survey.
- Quick literature verification found real matching anchors for the major claims:
  - 2024 Nature Photonics paper on resonant 3R-MoS2 nanodisks and SHG/anapole enhancement.
  - 2025 Communications Physics paper, “Ultrathin 3R-MoS2 metasurfaces with atomically precise edges for efficient nonlinear nanophotonics.”
  - 2025 Light: Science & Applications paper on interface SHG in bulk WS2/MoS2 hetero-bilayer van der Waals nanoantennas.
  - A Nature Photonics non-local 3R-MoS2 metasurface paper appears real, but exact publication/date/citation details should be checked carefully before final bibliography.

User scope decision:

- Simulation is mandatory.
- Do not delete any major content line from the DOCX. The plan may compress, reorder, or demote material into background/comparison/outlook, but should not remove the listed literature routes or proposed simulation/modeling ideas outright.
- COMSOL should be first priority. Python is secondary and should support interpretation or fallback, not replace the COMSOL simulation.
- User prefers direct `mph` Python package control over `cli-anything-mph`. Planning and execution should use `mph`/COMSOL API as the main simulation route.
- User approved entering execution and added a hard constraint: do not use COMSOL GUI. Build and run through scripts only.

Initial assessment:

- The direction is suitable, but the paper must use hierarchy to stay coherent: one physical question remains central, while the broader literature and extra modeling routes become supporting layers.
- The strongest course-paper angle is not “2D nonlinear optics overview,” but “3R-MoS2 qBIC/anapole metasurfaces as a case study connecting nonlinear optics, optical resonances, reflectance/transmission spectra, and low-dimensional material optical measurement.”
- The highest risk is overpromising COMSOL/Python reproduction. Because simulation is mandatory, the plan should define a guaranteed baseline simulation and treat harder nonlinear reproduction as optional enhancement.
- COMSOL-first baseline should target linear optical resonance/field enhancement in the qBIC/anapole structure. Full nonlinear SHG conversion efficiency can remain an advanced extension.

Likely out of scope or downgraded:

- Full nonlinear Maxwell solution of SHG conversion efficiency.
- Large literature survey of all 2D heterostructure nonlinear optics as equal-weight main text. It can remain as background and comparison.
- Detailed fabrication process replication. Fabrication can remain as context and limitation.
- Treating COMSOL/Python work as publishable quantitative reproduction rather than a pedagogical support model.

Proposed hierarchy under “do not delete”:

- Main case: ultrathin 3R-MoS2 qBIC metasurface, with COMSOL-style linear optical resonance and field enhancement as the required simulation target.
- Mechanism case: 3R-MoS2 nanodisk anapole resonance, used to explain why low far-field scattering can coexist with high internal field.
- Comparison case: WS2/MoS2 interface SHG nanoantenna, used to compare body non-centrosymmetry versus interface symmetry breaking.
- Outlook case: non-local 3R-MoS2 metasurface and higher-efficiency integrated nonlinear sources.
- Background route: external metasurface-enhanced monolayer TMD and all-TMD Mie/nanoresonator work.

Delivered simulation artifacts:

- Pure Python `mph` scripts under `scripts/`.
- COMSOL model and Java audit export under `outputs/comsol/`.
- Coarse 780-900 nm reflectance/transmittance sweep CSV and PNG.
- Refined 800-840 nm sweep CSV and PNG.
- Coarse Q estimate from the refined reflectance peak.
- Sampled max-field and `max |E|^4` SHG proxy columns in the refined sweep.
- Verified build, mesh, 850 nm solve, coarse sweep, and refined sweep without COMSOL GUI.
