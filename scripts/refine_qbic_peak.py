from __future__ import annotations

import csv
from pathlib import Path

import mph
import pandas as pd

from qbic_metrics import (
    add_normalized_f4_columns,
    estimate_reflectance_q,
    evaluate_mos2_metrics,
    find_spectral_markers,
    save_refined_spectrum_plot,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "outputs" / "comsol" / "qbic_3r_mos2_unitcell.mph"
CSV_PATH = ROOT / "outputs" / "comsol" / "qbic_refined_810_850nm.csv"
PNG_PATH = ROOT / "outputs" / "comsol" / "qbic_refined_810_850nm.png"
SUMMARY_PATH = ROOT / "outputs" / "comsol" / "qbic_peak_summary.txt"

def main() -> int:
    mph.option("session", "stand-alone")
    client = mph.start(cores=2)
    model = client.load(MODEL_PATH)

    rows: list[dict[str, float]] = []
    for wavelength_nm in range(810, 851):
        print(f"solving_wavelength_nm={wavelength_nm}")
        model.java.study("std1").feature("wave").set("plist", f"{wavelength_nm}[nm]")
        model.solve("Wavelength sweep")
        reflectance = float(model.evaluate("abs(ewfd.S11)^2", unit="1"))
        transmittance = float(model.evaluate("abs(ewfd.S21)^2", unit="1"))
        metrics = evaluate_mos2_metrics(model)
        row = {
            "wavelength_nm": float(wavelength_nm),
            "reflectance_R": reflectance,
            "transmittance_T": transmittance,
            "R_plus_T": reflectance + transmittance,
            **metrics,
        }
        rows.append(row)
        print(
            f"R={reflectance:.6g} T={transmittance:.6g} "
            f"F4={metrics['mos2_F4_volume_proxy']:.6g} Emax_mos2={metrics['mos2_max_E_enhancement']:.6g}"
        )

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    data = add_normalized_f4_columns(pd.DataFrame(rows))
    with CSV_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data.columns))
        writer.writeheader()
        writer.writerows(data.to_dict(orient="records"))

    peak = estimate_reflectance_q(data)
    markers = find_spectral_markers(data)
    save_refined_spectrum_plot(data, peak, markers, PNG_PATH)

    with SUMMARY_PATH.open("w", encoding="utf-8") as file:
        file.write("qBIC-inspired refined spectral summary\n")
        file.write(f"R_peak_wavelength_nm={markers.r_peak_wavelength_nm}\n")
        file.write(f"R_peak_reflectance={markers.r_peak_value}\n")
        file.write(f"F4_peak_wavelength_nm={markers.f4_peak_wavelength_nm}\n")
        file.write(f"F4_peak_value_raw={markers.f4_peak_value}\n")
        file.write(f"low_F4_wavelength_nm={markers.low_f4_wavelength_nm}\n")
        file.write(f"low_F4_value_raw={markers.low_f4_value}\n")
        file.write(f"baseline_reflectance={peak.baseline}\n")
        file.write(f"half_level={peak.half_level}\n")
        file.write(f"fwhm_nm={peak.fwhm_nm}\n")
        file.write(f"spectral_width_proxy_Q_from_reflectance_FWHM={peak.q_factor}\n")
        file.write("method=1 nm wavelength sweep, half-height crossing by linear interpolation.\n")
        file.write(
            "note=Simplified lossless qBIC-inspired model; this Q is a spectral-width proxy, "
            "not a reliable qBIC modal Q or experiment reproduction.\n"
        )

    model.save(MODEL_PATH)
    client.remove(model)
    print(f"saved_csv={CSV_PATH}")
    print(f"saved_png={PNG_PATH}")
    print(f"saved_summary={SUMMARY_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
