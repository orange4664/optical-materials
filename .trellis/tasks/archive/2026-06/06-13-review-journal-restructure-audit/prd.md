# 重构为综述期刊目标稿并落实重新审计意见

## Goal

根据“首选 Nanophotonics，备选 JPhys Photonics / ACS Photonics Perspective”的重新审计意见，把当前课程论文项目规划为一篇选择性、批判性、观点明确的英文综述稿：

> Resonant Nonlinear Nanophotonics in van der Waals Metasurfaces

核心主线从“3R-MoS2 qBIC COMSOL 小复现”改为“vdW 非线性超表面的 useful SHG 由非线性源对称性、模式重叠、二倍频出射、激子吸收、带宽和加工容差共同决定，而不是由最大 Q 因子单独决定”。

本任务的直接目标是完成综述稿重构的第一阶段：建立期刊目标、文献数据库、综述骨架、图表计划和 manuscript scaffold，使后续扩写到 Nanophotonics/JPhys/ACS 级别有可执行基础。不要在本任务中把教学级 COMSOL 作为主文核心证据。

## Requirements

- 遵守用户约束：用户也在用 Python `mph` 跑 COMSOL；本任务不得终止、重启或清理任何现有 `python`/`comsolmphserver` 进程。
- 不删除已有课程论文、COMSOL 输出和最终包；如需避免旧内容干扰，应新建综述稿文件和专用输出目录。
- 目标期刊定位：
  - 首选 Nanophotonics Review：选择性、批判性、观点化、面向 nanophotonics/nonlinear/metasurface 读者。
  - 备选 JPhys Photonics Topical Review/Perspective/Tutorial：允许更强 reproducible workflow/开放数据代码取向。
  - 可冲 ACS Photonics Perspective/Review：更适合 “Beyond high-Q resonances” 式观点稿。
- 文章定位必须从课程作业改成英文综述稿，不得保留课程名、姓名学号占位、课程联系等课程痕迹。
- 主文不得声称“复现 3R-MoS2 qBIC 结构”；COMSOL/Python 只能作为 Box、Tutorial 或 Supplementary scaffold。
- 新稿必须采用英文标题、英文 abstract 和英文 section outline。
- 新稿核心结构应覆盖：
  1. Introduction: why vdW nonlinear metasurfaces now?
  2. Nonlinear sources in layered crystals.
  3. Resonant enhancement mechanisms.
  4. Material platforms and representative progress.
  5. Figures of merit and comparison pitfalls.
  6. Design rules.
  7. Box: minimal modelling of resonant SHG.
  8. Outlook.
- 必须建立 `literature_database.csv` 或等价结构化文献库；本轮只要求 curated starter seed，重点覆盖关键路线与图表框架，后续再扩展到 60-100 条。
- 文献库字段至少包含：year, material/platform, dimensionality/source type, resonance mechanism, nonlinear process, metric reported, baseline/reference, pump condition note, device geometry, key message, DOI/URL, role in review。
- 必须新增或规划综述 display items，至少 6 个：
  1. field roadmap from monolayer-on-metasurface to all-vdW metasurfaces;
  2. nonlinear source taxonomy;
  3. resonance mechanism taxonomy;
  4. representative literature table;
  5. FoM/comparison pitfalls table or schematic;
  6. design-rule summary figure.
- TCMT 图应保留并重画为 clean 英文综述图；COMSOL 图全部降级到 Box/Supplementary，不作为主文结论图。
- 必须新增 FoM 与 comparison pitfalls 章节，明确 enhancement factor、absolute conversion efficiency、single-pass efficiency、pump fluence、pulse duration、repetition rate、collection NA、reference baseline 等指标不能直接混比。
- 如果本任务导出文档，应优先导出 Markdown/DOCX；PDF 若受本机 LaTeX 缺包影响，可记录原因。

## Acceptance Criteria

- [x] 新 Trellis 任务包含 `prd.md`、`design.md`、`implement.md`，并通过 `task.py validate`。
- [x] 存在新的英文综述稿 scaffold，建议路径为 `review_manuscript.md` 或 `manuscripts/review_manuscript.md`，且标题不再是课程论文题目。
- [x] 新稿删除课程信息、姓名学号占位和“课程联系”章节。
- [x] 新稿英文 abstract 明确提出 useful SHG / beyond maximum Q 的综述论点。
- [x] 新稿目录采用综述结构，并把 COMSOL/Python 内容移至 Box/Supplementary planning，而不是主文核心章节。
- [x] 存在 `literature_database.csv`，包含 curated starter seed，字段覆盖 Requirements 中列出的核心元数据，并明确标注文献库后续可扩展。
- [x] 存在代表文献表或从文献库生成的表格草案，覆盖 monolayer + external metasurface、all-TMD resonators、3R-MoS2 nanodisks、3R-MoS2 qBIC/non-local metasurfaces、WS2/MoS2 interface SHG、GaSe/InSe/NbOCl/hBN/graphene 等扩展平台。
- [x] 存在 FoM/comparison pitfalls 表，至少覆盖 enhancement factor、absolute conversion efficiency、pump fluence、pulse duration、repetition rate、collection NA、reference baseline。
- [x] 存在 display item plan，并至少生成或草拟 6 个 display items 的源文件/Markdown 图表说明。
- [x] `RUNS.md` 或新增 `REVIEW_RUNS.md` 说明综述稿与原课程论文/COMSOL scaffold 的关系。
- [x] 不终止用户的 COMSOL/Python 进程；如检查进程，只读观察，不执行 `Stop-Process`。
- [x] 修改后的文稿图片/表格路径存在，Python/CSV 生成脚本如有新增则通过 `python -m py_compile`。

## Verification Record

- Created `review_manuscript.md` as a separate English review scaffold. It uses the title `Resonant Nonlinear Nanophotonics in van der Waals Metasurfaces`, includes an English abstract, and contains the required review sections.
- Preserved `course_paper.md`, existing COMSOL outputs, and previous final package; no existing course-paper artifact was deleted.
- Created `literature_database.csv` as a 15-row curated starter seed after the user clarified that broad bibliography expansion can wait. The file includes all required metadata columns and TODO rows for GaSe/InSe, hBN, and graphene expansion.
- Created `outputs/review/representative_literature_table.md`, `outputs/review/fom_comparison_pitfalls.csv`, `outputs/review/fom_comparison_pitfalls.md`, and `outputs/review/display_item_plan.md`.
- Created `REVIEW_RUNS.md` documenting the relationship between the new review scaffold and the original COMSOL/Python course-paper scaffold.
- Added `scripts/build_review_assets.py`, an offline asset builder that does not start, stop, restart, or inspect COMSOL processes.
- Validation passed: `python -m py_compile scripts\build_review_assets.py`, CSV column/row checks, manuscript section and metadata checks, review artifact path checks, and Trellis `task.py validate`.

## Notes

- Keep `prd.md` focused on requirements, constraints, and acceptance criteria.
- 重新审计意见来自用户消息：“综述期刊目标重新审计与行动清单”。
- 官方目标期刊信息需在设计或稿件说明中引用/记录：Nanophotonics scope includes metamaterials, nanophotonic devices, ultrafast/nonlinear pulse propagation in nanomaterials/nanostructures, light-matter interaction, nanofabrication；JPhys Photonics accepts Topical Reviews/Perspectives/Tutorial Articles and emphasizes data/code/material openness；ACS Photonics accepts Reviews/Perspectives/Roadmaps.
- 本任务很可能需要联网补文献；文献条目必须以 DOI/URL 或清晰 bibliographic metadata 支撑。
