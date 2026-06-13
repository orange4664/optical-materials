from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mph
import numpy as np
import pandas as pd

from qbic_metrics import add_normalized_f4_columns, evaluate_mos2_metrics


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "outputs" / "comsol" / "qbic_3r_mos2_unitcell.mph"
CSV_PATH = ROOT / "outputs" / "comsol" / "qbic_tri_side_sensitivity.csv"
GRID_CSV_PATH = ROOT / "outputs" / "comsol" / "qbic_tri_side_grid.csv"
PNG_PATH = ROOT / "outputs" / "comsol" / "qbic_tri_side_sensitivity.png"
R_HEATMAP_PATH = ROOT / "outputs" / "comsol" / "qbic_tri_side_R_heatmap.png"
F4_HEATMAP_PATH = ROOT / "outputs" / "comsol" / "qbic_tri_side_F4_norm_heatmap.png"


def save_heatmap(data: pd.DataFrame, value_column: str, path: Path, colorbar_label: str, cmap: str = "viridis") -> None:
    pivot = data.pivot(index="tri_side_nm", columns="wavelength_nm", values=value_column).sort_index()
    fig, ax = plt.subplots(figsize=(7.0, 4.4), dpi=180)
    image = ax.imshow(
        pivot.to_numpy(dtype=float),
        origin="lower",
        aspect="auto",
        extent=[
            float(pivot.columns.min()),
            float(pivot.columns.max()),
            float(pivot.index.min()),
            float(pivot.index.max()),
        ],
        cmap=cmap,
    )
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Triangular-hole side length (nm)")
    fig.colorbar(image, ax=ax, label=colorbar_label)
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)


def main() -> int:
    mph.option("session", "stand-alone")
    client = mph.start(cores=2)
    model = client.load(MODEL_PATH)

    grid_rows: list[dict[str, float]] = []
    side_values = [340, 350, 360, 370, 374, 380, 390, 400]
    wavelength_values = list(range(810, 851, 2))
    for side_nm in side_values:
        model.parameter("tri_side", f"{side_nm}[nm]")
        model.build()
        model.mesh()
        for wavelength_nm in wavelength_values:
            print(f"solving_side_nm={side_nm} wavelength_nm={wavelength_nm}")
            model.java.study("std1").feature("wave").set("plist", f"{wavelength_nm}[nm]")
            model.solve("Wavelength sweep")
            reflectance = float(model.evaluate("abs(ewfd.S11)^2", unit="1"))
            transmittance = float(model.evaluate("abs(ewfd.S21)^2", unit="1"))
            metrics = evaluate_mos2_metrics(model)
            grid_rows.append(
                {
                "tri_side_nm": float(side_nm),
                "wavelength_nm": float(wavelength_nm),
                "reflectance_R": reflectance,
                "transmittance_T": transmittance,
                "R_plus_T": reflectance + transmittance,
                **metrics,
                }
            )

    grid = add_normalized_f4_columns(pd.DataFrame(grid_rows))
    summary_rows: list[dict[str, float]] = []
    for side_nm, group in grid.groupby("tri_side_nm", sort=True):
        best_r = group.loc[group["reflectance_R"].idxmax()]
        best_f4 = group.loc[group["mos2_F4_volume_proxy"].idxmax()]
        summary_rows.append(
            {
                "tri_side_nm": float(side_nm),
                "best_R_wavelength_nm": float(best_r["wavelength_nm"]),
                "best_R": float(best_r["reflectance_R"]),
                "F4_at_best_R": float(best_r["mos2_F4_volume_proxy"]),
                "F4_norm_to_min_at_best_R": float(best_r["mos2_F4_norm_to_min"]),
                "best_F4_wavelength_nm": float(best_f4["wavelength_nm"]),
                "best_F4": float(best_f4["mos2_F4_volume_proxy"]),
                "best_F4_norm_to_min": float(best_f4["mos2_F4_norm_to_min"]),
                "R_at_best_F4": float(best_f4["reflectance_R"]),
            }
        )
        print(
            "best",
            f"side={side_nm}",
            f"R@{best_r['wavelength_nm']}nm={best_r['reflectance_R']:.6g}",
            f"F4@{best_f4['wavelength_nm']}nm={best_f4['mos2_F4_volume_proxy']:.6g}",
        )

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    grid.to_csv(GRID_CSV_PATH, index=False)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    data = pd.DataFrame(summary_rows)
    fig, ax1 = plt.subplots(figsize=(6.0, 4.0), dpi=180)
    ax1.plot(data["tri_side_nm"], data["best_R"], marker="o", label="Best sampled R")
    ax1.set_xlabel("Triangular-hole side length (nm)")
    ax1.set_ylabel("Best sampled reflectance")
    ax1.set_ylim(0, 1.05)
    ax1.grid(True, alpha=0.25)
    ax2 = ax1.twinx()
    ax2.plot(data["tri_side_nm"], data["best_F4_norm_to_min"], color="tab:green", marker="^", label="Best normalized F4")
    ax2.set_ylabel("Best normalized MoS2 F4")
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [line.get_label() for line in lines], frameon=False, loc="best")
    fig.tight_layout()
    fig.savefig(PNG_PATH)
    plt.close(fig)
    save_heatmap(grid, "reflectance_R", R_HEATMAP_PATH, "Reflectance R")
    save_heatmap(grid, "mos2_log10_F4_norm_to_min", F4_HEATMAP_PATH, "log10 normalized MoS2 F4", cmap="magma")
    client.remove(model)
    print(f"saved_grid_csv={GRID_CSV_PATH}")
    print(f"saved_csv={CSV_PATH}")
    print(f"saved_png={PNG_PATH}")
    print(f"saved_R_heatmap={R_HEATMAP_PATH}")
    print(f"saved_F4_heatmap={F4_HEATMAP_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
