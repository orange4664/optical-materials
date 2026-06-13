from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "python"


def single_resonance_response(detuning: np.ndarray, q_loaded: float) -> np.ndarray:
    gamma = 1.0 / (2.0 * q_loaded)
    amplitude = 1.0 / (1j * detuning + gamma)
    shg_proxy = np.abs(amplitude) ** 4
    return shg_proxy / shg_proxy.max()


def coupled_power_from_ratio(coupling_ratio: np.ndarray, gamma_absorption: float = 1.0) -> np.ndarray:
    gamma_external = coupling_ratio * gamma_absorption
    gamma_total = gamma_external + gamma_absorption
    field_build_up = gamma_external / gamma_total**2
    out_coupling = gamma_external / gamma_total
    proxy = field_build_up**2 * out_coupling
    return proxy / proxy.max()


def q_tradeoff_plot() -> Path:
    detuning = np.linspace(-0.08, 0.08, 500)
    q_values = [20, 50, 100, 200]

    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), dpi=180)

    for q_value in q_values:
        axes[0].plot(detuning, single_resonance_response(detuning, q_value), label=f"Q={q_value}")
    axes[0].set_xlabel("Normalized detuning")
    axes[0].set_ylabel("Normalized SHG proxy")
    axes[0].set_title("Peak rises while bandwidth narrows")
    axes[0].grid(True, alpha=0.25)
    axes[0].legend(frameon=False)

    coupling_ratio = np.logspace(-2, 2, 500)
    proxy = coupled_power_from_ratio(coupling_ratio)
    optimum_index = int(np.argmax(proxy))
    optimum_ratio = float(coupling_ratio[optimum_index])
    axes[1].plot(coupling_ratio, proxy, color="tab:red", label="Useful SHG proxy")
    axes[1].axvline(
        optimum_ratio,
        color="0.25",
        linestyle=":",
        linewidth=1.2,
        label=fr"optimum $\gamma_e/\gamma_i$={optimum_ratio:.2g}",
    )
    axes[1].set_xscale("log")
    axes[1].set_xlabel(r"External coupling ratio $\gamma_e/\gamma_i$")
    axes[1].set_ylabel("Normalized useful SHG proxy")
    axes[1].set_title("Finite coupling gives an optimum")
    axes[1].grid(True, alpha=0.25)
    axes[1].legend(frameon=False)

    fig.tight_layout()
    path = OUT_DIR / "tcmt_q_tradeoff.png"
    fig.savefig(path)
    plt.close(fig)

    response_data = {"detuning": detuning}
    for q_value in q_values:
        response_data[f"normalized_shg_proxy_Q_{q_value}"] = single_resonance_response(detuning, q_value)
    pd.DataFrame(response_data).to_csv(OUT_DIR / "tcmt_q_tradeoff_curves.csv", index=False)
    pd.DataFrame(
        {
            "gamma_external_over_gamma_internal": coupling_ratio,
            "normalized_useful_shg_proxy": proxy,
            "optimum_gamma_external_over_gamma_internal": np.full_like(coupling_ratio, optimum_ratio),
        }
    ).to_csv(OUT_DIR / "tcmt_q_tradeoff_optimum.csv", index=False)
    return path


def detuning_map_plot() -> Path:
    pump_detuning = np.linspace(-0.08, 0.08, 180)
    sh_detuning = np.linspace(-0.08, 0.08, 180)
    dp, ds = np.meshgrid(pump_detuning, sh_detuning)
    gamma_p = 0.015
    gamma_s = 0.025
    pump_field = 1.0 / (dp**2 + gamma_p**2)
    sh_out = 1.0 / (ds**2 + gamma_s**2)
    proxy = pump_field**2 * sh_out
    proxy = proxy / proxy.max()

    fig, ax = plt.subplots(figsize=(5.0, 4.2), dpi=180)
    image = ax.imshow(
        proxy,
        origin="lower",
        extent=[pump_detuning.min(), pump_detuning.max(), sh_detuning.min(), sh_detuning.max()],
        aspect="auto",
        cmap="magma",
    )
    ax.set_xlabel("Pump-mode detuning")
    ax.set_ylabel("SH-mode detuning")
    ax.set_title("Double-resonance alignment maximizes proxy")
    fig.colorbar(image, ax=ax, label="Normalized SHG proxy")
    fig.tight_layout()
    path = OUT_DIR / "tcmt_detuning_map.png"
    fig.savefig(path)
    plt.close(fig)
    pd.DataFrame(proxy, index=sh_detuning, columns=pump_detuning).to_csv(OUT_DIR / "tcmt_detuning_map.csv")
    return path


def asymmetry_plot() -> Path:
    asymmetry = np.linspace(0.02, 0.5, 300)
    q_rad = 1.0 / asymmetry**2
    q_abs = 180.0
    q_loaded = 1.0 / (1.0 / q_rad + 1.0 / q_abs)
    coupling = 1.0 / q_rad
    linewidth = 1.0 / q_loaded
    proxy = (q_loaded**2) * coupling
    proxy = proxy / proxy.max()

    fig, ax1 = plt.subplots(figsize=(6.0, 4.0), dpi=180)
    ax1.plot(asymmetry, proxy, color="tab:blue", label="Useful SHG proxy")
    ax1.set_xlabel("qBIC asymmetry parameter")
    ax1.set_ylabel("Normalized useful proxy")
    ax1.grid(True, alpha=0.25)
    ax2 = ax1.twinx()
    ax2.plot(asymmetry, linewidth / linewidth.max(), color="tab:orange", linestyle="--", label="Relative linewidth")
    ax2.set_ylabel("Relative linewidth")
    lines = ax1.get_lines() + ax2.get_lines()
    ax1.legend(lines, [line.get_label() for line in lines], frameon=False)
    ax1.set_title("qBIC asymmetry trades enhancement for tolerance")
    fig.tight_layout()
    path = OUT_DIR / "tcmt_qbic_asymmetry.png"
    fig.savefig(path)
    plt.close(fig)
    pd.DataFrame(
        {
            "asymmetry": asymmetry,
            "q_rad": q_rad,
            "q_loaded": q_loaded,
            "normalized_useful_proxy": proxy,
            "relative_linewidth": linewidth / linewidth.max(),
        }
    ).to_csv(OUT_DIR / "tcmt_qbic_asymmetry.csv", index=False)
    return path


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = [q_tradeoff_plot(), detuning_map_plot(), asymmetry_plot()]
    summary = OUT_DIR / "tcmt_summary.txt"
    summary.write_text(
        "TCMT outputs are normalized pedagogical proxies. They illustrate detuning, Q, "
        "external coupling, and qBIC asymmetry trade-offs rather than fitting a specific experiment.\n",
        encoding="utf-8",
    )
    for path in paths:
        print(f"saved={path}")
    print(f"saved={summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
