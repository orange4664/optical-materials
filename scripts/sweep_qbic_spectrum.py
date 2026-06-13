from __future__ import annotations

import csv
from pathlib import Path

import mph

from qbic_metrics import evaluate_mos2_metrics


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "outputs" / "comsol" / "qbic_3r_mos2_unitcell.mph"
CSV_PATH = ROOT / "outputs" / "comsol" / "qbic_spectrum_780_900nm.csv"


def main() -> int:
    mph.option("session", "stand-alone")
    client = mph.start(cores=2)
    model = client.load(MODEL_PATH)

    rows: list[dict[str, float]] = []
    for wavelength_nm in range(780, 901, 20):
        print(f"solving_wavelength_nm={wavelength_nm}")
        model.java.study("std1").feature("wave").set("plist", f"{wavelength_nm}[nm]")
        model.solve("Wavelength sweep")
        reflectance = float(model.evaluate("abs(ewfd.S11)^2", unit="1"))
        transmittance = float(model.evaluate("abs(ewfd.S21)^2", unit="1"))
        metrics = evaluate_mos2_metrics(model)
        rows.append(
            {
                "wavelength_nm": float(wavelength_nm),
                "reflectance_R": reflectance,
                "transmittance_T": transmittance,
                "R_plus_T": reflectance + transmittance,
                **metrics,
            }
        )
        print(
            f"R={reflectance:.6g} T={transmittance:.6g} R_plus_T={reflectance + transmittance:.6g} "
            f"F4={metrics['mos2_F4_volume_proxy']:.6g}"
        )

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    model.save(MODEL_PATH)
    print(f"saved_csv={CSV_PATH}")
    client.remove(model)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
