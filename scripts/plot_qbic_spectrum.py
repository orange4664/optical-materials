from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "outputs" / "comsol" / "qbic_spectrum_780_900nm.csv"
PNG_PATH = ROOT / "outputs" / "comsol" / "qbic_spectrum_780_900nm.png"


def main() -> int:
    data = pd.read_csv(CSV_PATH)
    fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=180)
    ax.plot(data["wavelength_nm"], data["reflectance_R"], marker="o", label="Reflectance R")
    ax.plot(data["wavelength_nm"], data["transmittance_T"], marker="s", label="Transmittance T")
    ax.set_xlabel("Wavelength (nm)")
    ax.set_ylabel("Power coefficient")
    ax.set_xlim(data["wavelength_nm"].min(), data["wavelength_nm"].max())
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()
    PNG_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG_PATH)
    print(f"saved_png={PNG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
