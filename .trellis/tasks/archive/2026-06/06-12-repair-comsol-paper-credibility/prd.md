# 修复课程论文 COMSOL 可信度与最终成文问题

## Goal

根据外部审计报告修复课程论文项目的关键可信度缺口，使最终稿能够被定位为“问题导向小综述 + 教学级简化 COMSOL 复现 + TCMT 分析”，而不是未经验证的定量复现实验。

## Requirements

- 保留现有文件和已有工作，不删除项目中的论文、脚本、输出或 Trellis 资料。
- COMSOL 工作必须脚本化完成，优先使用现有 Python `mph` 脚本；不依赖 COMSOL GUI 手工编辑。
- 修正三角孔几何/材料域问题，确保三角孔内部是空气求解域，而不是从电磁计算域中被挖空的非物理外边界。
- 不再把全域 `max |E|` 或 `max |E|^4` 写成 SHG 增强因子。结果和论文应使用 MoS2 域内的场增强代理量，例如域内均值/积分形式的 `F2_volume`、`F4_volume`，并保留最大场仅作为诊断量。
- 补充能支撑“局域场增强”的近场图，至少包含共振和失谐两个波长的对比图。
- 细化反射/透射谱扫描并输出 Q 因子拟合或明确的半高宽估算，报告 `lambda0`、`FWHM`、`Q` 和简化模型 caveat。
- 扩展三角孔边长敏感性扫描，至少覆盖 7 个点；若 COMSOL 时间或环境限制导致不能完整求解，必须在结果说明中透明记录并保留可运行脚本。
- 更新 `course_paper.md`，补上正式学术论文结构、图表编号、文献内引、公式格式和简化模型边界；删除“工作记录式”表述。
- 输出说明文件应明确材料参数为无色散/无吸收代理模型，不能声称定量复现实验 SHG 转换效率。

## Acceptance Criteria

- [x] `scripts/build_qbic_model.py` 中空气域或空气填充体覆盖三角孔体积，且材料/物理选择能将该体积纳入空气域。
- [x] 新的 COMSOL 结果 CSV 包含 MoS2 域内 `F2_volume_proxy`、`F4_volume_proxy` 或等价命名的 SHG 趋势代理量。
- [x] `outputs/comsol/` 下存在细扫谱图、细扫 CSV、Q 摘要文件和共振/失谐近场图。
- [x] `outputs/comsol/` 下存在扩展后的三角孔边长扫描 CSV/PNG，或有明确记录说明环境阻塞和可复现命令。
- [x] `course_paper.md` 引用的本地图像路径全部存在。
- [x] `course_paper.md` 明确写出“教学级简化模型/趋势验证”，不声称定量复现原文 SHG 效率。
- [x] 修改过的 Python 脚本通过 `python -m py_compile`。
- [x] Trellis 任务文档记录最终验证结果和已知局限。

## Verification Record

- `python scripts\build_qbic_model.py` passed and saved `.mph`/`.java` with `problems=[]`.
- `python scripts\run_qbic_model.py` passed build/mesh/single-wavelength solve with `problems_after_solve=[]`.
- `python scripts\evaluate_qbic_model.py` evaluated `aveop_mos2`, `intop_mos2`, and `maxop_mos2`; `ewfd.emwte` remains unavailable and is not used.
- `python scripts\refine_qbic_peak.py` produced the required CSV/PNG/field maps. COMSOL/JVM crashed during shutdown after outputs were saved; plotting scripts were then changed to `matplotlib.use("Agg")`.
- `python scripts\qbic_sensitivity_scan.py` completed 8 side lengths x 7 wavelengths and wrote CSV/PNG.
- `python scripts\tcmt_analysis.py` regenerated TCMT figures and CSV data.
- `pandoc course_paper.md -o outputs\paper\course_paper.docx` produced a non-empty Word file.
- CSV validation: refined sweep has 41 rows; side scan has 8 rows; refined `R_plus_T` max absolute error from 1 is about `8.95e-11`.
- Markdown image validation: 8 image references, 0 missing.

## Notes

- 审计报告路径：`C:\Users\Huyinze\Downloads\低维材料论文作业_审计报告.md`。
- 原始方向审计 Word：`低维材料论文方向审计与结论.docx`。
- 用户明确要求“必须做”“都不要删除”“COMSOL 先行”“不用 GUI，可直接使用 mph-py”。
