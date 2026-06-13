from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


E0_EXPR = "1[V/m]"
F2_EXPR = f"aveop_mos2((ewfd.normE/{E0_EXPR})^2)"
F4_EXPR = f"aveop_mos2((ewfd.normE/{E0_EXPR})^4)"
EMAX_EXPR = f"maxop_mos2(ewfd.normE/{E0_EXPR})"


@dataclass(frozen=True)
class PeakEstimate:
    wavelength_nm: float
    reflectance: float
    baseline: float
    half_level: float
    fwhm_nm: float | None
    q_factor: float | None


@dataclass(frozen=True)
class SpectralMarkers:
    r_peak_wavelength_nm: float
    r_peak_value: float
    f4_peak_wavelength_nm: float
    f4_peak_value: float
    low_f4_wavelength_nm: float
    low_f4_value: float


def evaluate_mos2_metrics(model) -> dict[str, float]:
    f2 = float(np.asarray(model.evaluate(F2_EXPR, unit="1")).squeeze())
    f4 = float(np.asarray(model.evaluate(F4_EXPR, unit="1")).squeeze())
    emax = float(np.asarray(model.evaluate(EMAX_EXPR, unit="1")).squeeze())
    return {
        "mos2_F2_volume_proxy": f2,
        "mos2_F4_volume_proxy": f4,
        "mos2_max_E_enhancement": emax,
    }


def add_normalized_f4_columns(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()
    f4 = data["mos2_F4_volume_proxy"].astype(float)
    positive = f4[f4 > 0]
    if positive.empty:
        data["mos2_F4_norm_to_min"] = np.nan
        data["mos2_F4_norm_to_median"] = np.nan
        data["mos2_log10_F4_norm_to_min"] = np.nan
        return data
    min_positive = float(positive.min())
    median_positive = float(positive.median())
    data["mos2_F4_norm_to_min"] = f4 / min_positive
    data["mos2_F4_norm_to_median"] = f4 / median_positive
    data["mos2_log10_F4_norm_to_min"] = np.log10(np.maximum(data["mos2_F4_norm_to_min"], 1e-300))
    return data


def find_spectral_markers(data: pd.DataFrame) -> SpectralMarkers:
    r_idx = data["reflectance_R"].astype(float).idxmax()
    f4_idx = data["mos2_F4_volume_proxy"].astype(float).idxmax()
    low_f4_idx = data["mos2_F4_volume_proxy"].astype(float).idxmin()
    return SpectralMarkers(
        r_peak_wavelength_nm=float(data.loc[r_idx, "wavelength_nm"]),
        r_peak_value=float(data.loc[r_idx, "reflectance_R"]),
        f4_peak_wavelength_nm=float(data.loc[f4_idx, "wavelength_nm"]),
        f4_peak_value=float(data.loc[f4_idx, "mos2_F4_volume_proxy"]),
        low_f4_wavelength_nm=float(data.loc[low_f4_idx, "wavelength_nm"]),
        low_f4_value=float(data.loc[low_f4_idx, "mos2_F4_volume_proxy"]),
    )


def estimate_reflectance_q(data: pd.DataFrame) -> PeakEstimate:
    peak_index = data["reflectance_R"].idxmax()
    peak_wavelength = float(data.loc[peak_index, "wavelength_nm"])
    peak_reflectance = float(data.loc[peak_index, "reflectance_R"])
    baseline = float(min(data["reflectance_R"].iloc[0], data["reflectance_R"].iloc[-1]))
    half_level = baseline + 0.5 * (peak_reflectance - baseline)

    wavelengths = data["wavelength_nm"].to_numpy(dtype=float)
    reflectance = data["reflectance_R"].to_numpy(dtype=float)
    above = reflectance >= half_level
    crossing_indices = np.flatnonzero(above[:-1] != above[1:])
    if len(crossing_indices) < 2:
        return PeakEstimate(peak_wavelength, peak_reflectance, baseline, half_level, None, None)

    crossings: list[float] = []
    for idx in crossing_indices:
        x0, x1 = wavelengths[idx], wavelengths[idx + 1]
        y0, y1 = reflectance[idx], reflectance[idx + 1]
        if y1 == y0:
            crossings.append(float(x0))
        else:
            crossings.append(float(x0 + (half_level - y0) * (x1 - x0) / (y1 - y0)))

    fwhm = float(crossings[-1] - crossings[0])
    q_factor = peak_wavelength / fwhm if fwhm > 0 else None
    return PeakEstimate(peak_wavelength, peak_reflectance, baseline, half_level, fwhm, q_factor)


def save_refined_spectrum_plot(data: pd.DataFrame, peak: PeakEstimate, markers: SpectralMarkers, path: Path) -> None:
    fig, ax1 = plt.subplots(figsize=(6.4, 4.2), dpi=180)
    ax1.plot(data["wavelength_nm"], data["reflectance_R"], marker="o", markersize=3.2, label="Reflectance R")
    ax1.plot(data["wavelength_nm"], data["transmittance_T"], marker="s", markersize=3.2, label="Transmittance T")
    ax1.axvline(markers.r_peak_wavelength_nm, color="0.25", linestyle=":", linewidth=1.1, label="R peak")
    ax1.axvline(markers.f4_peak_wavelength_nm, color="tab:green", linestyle=":", linewidth=1.1, label="F4 peak")
    ax1.axhline(peak.half_level, color="0.45", linestyle="--", linewidth=1.0, label="R half level")
    ax1.set_xlabel("Wavelength (nm)")
    ax1.set_ylabel("Power coefficient")
    ax1.set_ylim(0, 1.05)
    ax1.grid(True, alpha=0.25)

    ax2 = ax1.twinx()
    ax2.plot(
        data["wavelength_nm"],
        data["mos2_log10_F4_norm_to_min"],
        color="tab:green",
        marker="^",
        markersize=3.2,
        label="log10 normalized MoS2 F4",
    )
    ax2.set_ylabel("log10 normalized MoS2 F4 proxy")

    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [line.get_label() for line in lines], frameon=False, loc="best")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)


def field_map_samples_from_solution(model) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x_nm, y_nm, z_nm, field = model.evaluate(
        ["x", "y", "z", f"(ewfd.normE/{E0_EXPR})^2"],
        unit=["nm", "nm", "nm", "1"],
    )
    x = np.asarray(x_nm, dtype=float).ravel()
    y = np.asarray(y_nm, dtype=float).ravel()
    z = np.asarray(z_nm, dtype=float).ravel()
    intensity = np.asarray(field, dtype=float).ravel()

    film = (z >= 0.0) & (z <= 25.0)
    if film.sum() < 10:
        film = np.isfinite(intensity)

    x = x[film]
    y = y[film]
    intensity = intensity[film]
    finite = np.isfinite(intensity) & np.isfinite(x) & np.isfinite(y)
    x = x[finite]
    y = y[finite]
    intensity = intensity[finite]
    if len(intensity) == 0:
        raise RuntimeError("No finite field samples available for field-map plotting.")

    log_intensity = np.log10(1.0 + np.maximum(intensity, 0.0))
    return x, y, log_intensity


def triangular_hole_outline(tri_side: float = 374.0) -> tuple[np.ndarray, np.ndarray]:
    tri_x = np.array([-tri_side / 2.0, tri_side / 2.0, 0.0, -tri_side / 2.0])
    tri_y = np.array(
        [
            -np.sqrt(3.0) * tri_side / 6.0,
            -np.sqrt(3.0) * tri_side / 6.0,
            np.sqrt(3.0) * tri_side / 3.0,
            -np.sqrt(3.0) * tri_side / 6.0,
        ]
    )
    return tri_x, tri_y


def save_field_map_samples(
    x: np.ndarray,
    y: np.ndarray,
    log_intensity: np.ndarray,
    wavelength_nm: float,
    path: Path,
    title: str,
    vmin: float | None = None,
    vmax: float | None = None,
) -> None:
    tri_side = 374.0
    tri_x, tri_y = triangular_hole_outline(tri_side)

    fig, ax = plt.subplots(figsize=(5.2, 4.4), dpi=180)
    image = ax.hexbin(x, y, C=log_intensity, gridsize=85, reduce_C_function=np.mean, cmap="magma", vmin=vmin, vmax=vmax)
    ax.plot(tri_x, tri_y, color="cyan", linewidth=1.2, label="triangular air hole")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x (nm)")
    ax.set_ylabel("y (nm)")
    ax.set_title(f"{title}, {wavelength_nm:.1f} nm")
    ax.legend(frameon=False, loc="upper right", fontsize=7)
    fig.colorbar(image, ax=ax, label=r"$\log_{10}(1+|E/E_0|^2)$ sampled in film slab")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)


def save_field_map_from_solution(
    model,
    wavelength_nm: float,
    path: Path,
    title: str,
    vmin: float | None = None,
    vmax: float | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    x, y, log_intensity = field_map_samples_from_solution(model)
    save_field_map_samples(x, y, log_intensity, wavelength_nm, path, title, vmin=vmin, vmax=vmax)
    return x, y, log_intensity


def save_field_comparison_plot(
    samples: list[tuple[str, float, np.ndarray, np.ndarray, np.ndarray]],
    path: Path,
) -> None:
    if not samples:
        raise ValueError("At least one field sample is required.")
    all_values = np.concatenate([sample[4] for sample in samples])
    vmin = float(np.nanpercentile(all_values, 1.0))
    vmax = float(np.nanpercentile(all_values, 99.0))
    tri_x, tri_y = triangular_hole_outline()

    fig, axes = plt.subplots(
        1,
        len(samples),
        figsize=(5.0 * len(samples) + 0.8, 4.4),
        dpi=180,
        squeeze=False,
        constrained_layout=True,
    )
    last_image = None
    for ax, (label, wavelength_nm, x, y, log_intensity) in zip(axes[0], samples):
        last_image = ax.hexbin(
            x,
            y,
            C=log_intensity,
            gridsize=85,
            reduce_C_function=np.mean,
            cmap="magma",
            vmin=vmin,
            vmax=vmax,
        )
        ax.plot(tri_x, tri_y, color="cyan", linewidth=1.1)
        ax.set_aspect("equal", adjustable="box")
        ax.set_xlabel("x (nm)")
        ax.set_ylabel("y (nm)")
        ax.set_title(f"{label}\n{wavelength_nm:.1f} nm")
    if last_image is not None:
        fig.colorbar(
            last_image,
            ax=axes.ravel().tolist(),
            location="right",
            shrink=0.86,
            pad=0.02,
            label=r"$\log_{10}(1+|E/E_0|^2)$, shared scale",
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)
    plt.close(fig)
