# 修复第二轮审计指出的 COMSOL 与论文论点对齐问题

## Goal

根据第二轮审计报告，修复 COMSOL 物理域设置、结果图和论文叙事之间的不一致，使课程论文最终定位为“qBIC-inspired 教学级趋势模型 + MoS2 域内 F4 代理分析 + TCMT 外耦合折中”，避免过度声称定量复现。

## Requirements

- 保留已有工作成果，不删除用户明确要求保留的项目源文件；旧结果可移出最终交付包或标注为历史输出，但不要破坏可追溯性。
- COMSOL 仍需脚本化运行，使用 Python `mph`/现有脚本，不依赖 GUI 手工改模型。
- P0：处理默认空气波方程 `wee1` 的域重叠风险；若 COMSOL 不允许编辑默认 `wee1` 选择域，则采用等价互斥方案：保留 material-controlled `wee1` 全域特征，移除额外手动 wave equation feature，并用材料选择域控制空气、SiO2、MoS2 介电常数。
- P0：重新运行关键 COMSOL 输出，至少覆盖 810-850 nm 细扫、MoS2 域内 F2/F4 代理量、反射峰/最大 F4/低 F4 对照近场图。
- P0：F4 图和论文表达必须改为归一化或 log-normalized 趋势，不展示 `1e34` 绝对值作为物理增强结论。
- P0：论文必须明确区分 849 nm 反射峰与 843 nm F4 代理峰；不得写成“849 nm 获得最大 SHG 增强”。
- P0：Q 表述必须降级为“反射谱宽度代理/教学级估计”，不得写成可靠 qBIC Q 因子。
- P1：三角孔边长扫描需同时记录最大 R 和最大 F4，不再只按最大 R 选点；最好输出 `side length × wavelength` 的 R 和 F4_norm 热图。
- P1：重做 TCMT Q tradeoff 右图，用 `gamma_e/gamma_i` 展示有限外耦合/内损耗下的中间最优点，避免图和标题不一致。
- P1：增加 `RUNS.md` 或等价说明，记录脚本运行顺序、输出文件含义和哪些结果用于正文。
- P2：论文加封面/姓名学号课程日期占位、页码/导出 DOCX/PDF 尽力完成、统一图注和引用语气。
- P2：最终交付包应排除开发环境痕迹、`__pycache__`、崩溃日志和旧冲突结果；若不删除原文件，应创建干净交付目录。

## Acceptance Criteria

- [x] `scripts/build_qbic_model.py` 中 `wee1` 调用为 `configure_wave_equation(..., "1", "sel_air")` 或等价互斥域设置。
- [x] Java 导出或诊断输出能证明 `wee1`、`wee_sio2`、`wee_mos2` 各自绑定到空气、SiO2、MoS2 选择域。
- [x] 新细扫 CSV 包含 `F4_norm` 或等价归一化列，并能识别反射峰波长与 F4 峰波长。
- [x] 近场图至少包含反射峰、F4 峰、低 F4 对照，且使用统一 color scale 或清楚说明不可直接比较。
- [x] 边长扫描 CSV 同时包含 `best_R_wavelength`、`best_R`、`F4_at_best_R`、`best_F4_wavelength`、`best_F4`、`R_at_best_F4` 或等价列。
- [x] 存在 R 热图和 F4_norm 热图，或记录运行阻塞与可复现命令。
- [x] `tcmt_q_tradeoff.png` 的右图实际展示外耦合比下的最优点，标题和正文一致。
- [x] `course_paper.md` 将模型定位为 qBIC-inspired/教学级趋势模型，不再声称定量复现原文实验或高 Q。
- [x] `course_paper.md` 明确写出“反射峰与 F4 代理峰不完全重合”的分析点。
- [x] 新 DOCX 导出成功；若 PDF 不能导出，记录原因。
- [x] 修改过的 Python 脚本通过 `python -m py_compile`。
- [x] Markdown 图片路径全部存在，最终交付目录或清单不包含开发环境目录、`__pycache__`、crash log、旧冲突结果。

## Verification Record

- COMSOL model rebuilt with explicit triangular air-fill domain. Java export shows `sel_air` includes `geom1_air_dom` and `geom1_tri_prism_dom`; `mat_air`, `mat_sio2`, and `mat_mos2` are bound to `sel_air`, `sel_sio2`, and `sel_mos2_checked`.
- Directly binding default `wee1` to `sel_air` failed in COMSOL because the default wave-equation feature selection was not editable; disabling it also failed. The accepted equivalent fix is to keep only default material-controlled `wee1` and remove extra `wee_sio2`/`wee_mos2` features, so no overlapping wave-equation features remain.
- `outputs/comsol/qbic_refined_810_850nm.csv` has 41 rows and normalized/log F4 columns. It identifies reflectance peak 849 nm and MoS2-domain F4 proxy peak 843 nm.
- `outputs/comsol/qbic_field_comparison.png` contains reflectance peak, F4 peak, and low-F4 reference field maps with shared color scaling.
- `outputs/comsol/qbic_tri_side_grid.csv` has 168 rows; `outputs/comsol/qbic_tri_side_sensitivity.csv` has best-R and best-F4 summary columns; R and F4 heatmaps were generated.
- `outputs/python/tcmt_q_tradeoff.png` was regenerated with coupling-ratio optimum; `outputs/python/tcmt_q_tradeoff_optimum.csv` gives optimum `gamma_e/gamma_i ≈ 1.49`.
- `course_paper.md` and `outputs/paper/course_paper.docx` were regenerated. PDF export was attempted but failed because local LaTeX is missing `footnote.sty`.
- Validation commands passed: Python `py_compile`, Markdown image path checks, CSV shape/column checks, final-package exclusion checks, and `task.py validate`.

## Notes

- 第二轮审计报告：`C:\Users\Huyinze\Downloads\低维材料论文作业_第二轮审计报告.md`。
- 本任务是复杂任务，必须包含 `prd.md`、`design.md`、`implement.md` 后才能 start。
