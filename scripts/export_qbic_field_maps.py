from __future__ import annotations

from pathlib import Path

import mph
import pandas as pd

from qbic_metrics import find_spectral_markers, save_field_comparison_plot, save_field_map_from_solution


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "outputs" / "comsol" / "qbic_3r_mos2_unitcell.mph"
CSV_PATH = ROOT / "outputs" / "comsol" / "qbic_refined_810_850nm.csv"
FIELD_R_PEAK_PATH = ROOT / "outputs" / "comsol" / "qbic_field_R_peak.png"
FIELD_F4_PEAK_PATH = ROOT / "outputs" / "comsol" / "qbic_field_F4_peak.png"
FIELD_LOW_F4_PATH = ROOT / "outputs" / "comsol" / "qbic_field_low_F4.png"
FIELD_COMPARISON_PATH = ROOT / "outputs" / "comsol" / "qbic_field_comparison.png"


def main() -> int:
    data = pd.read_csv(CSV_PATH)
    markers = find_spectral_markers(data)
    targets = [
        ("R peak", markers.r_peak_wavelength_nm, FIELD_R_PEAK_PATH),
        ("F4 peak", markers.f4_peak_wavelength_nm, FIELD_F4_PEAK_PATH),
        ("low F4 reference", markers.low_f4_wavelength_nm, FIELD_LOW_F4_PATH),
    ]

    mph.option("session", "stand-alone")
    client = mph.start(cores=2)
    model = client.load(MODEL_PATH)
    samples = []
    for label, wavelength_nm, path in targets:
        print(f"solving_field_map_wavelength_nm={wavelength_nm}")
        model.java.study("std1").feature("wave").set("plist", f"{wavelength_nm}[nm]")
        model.solve("Wavelength sweep")
        x, y, log_intensity = save_field_map_from_solution(model, wavelength_nm, path, label)
        samples.append((label, wavelength_nm, x, y, log_intensity))
        print(f"saved_field_map={path}")
    save_field_comparison_plot(samples, FIELD_COMPARISON_PATH)
    print(f"saved_field_comparison={FIELD_COMPARISON_PATH}")
    client.remove(model)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
