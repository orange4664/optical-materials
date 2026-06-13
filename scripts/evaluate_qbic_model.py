from __future__ import annotations

from pathlib import Path

import mph


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "outputs" / "comsol" / "qbic_3r_mos2_unitcell.mph"


EXPRESSIONS = [
    ("freq", "Hz"),
    ("ewfd.normE", "V/m"),
    ("ewfd.Ex", "V/m"),
    ("ewfd.Ey", "V/m"),
    ("ewfd.Ez", "V/m"),
    ("ewfd.emwte", "J/m^3"),
    ("ewfd.Poavz", "W/m^2"),
    ("abs(ewfd.S11)^2", "1"),
    ("abs(ewfd.S21)^2", "1"),
    ("aveop_mos2((ewfd.normE/1[V/m])^2)", "1"),
    ("aveop_mos2((ewfd.normE/1[V/m])^4)", "1"),
    ("intop_mos2((ewfd.normE/1[V/m])^4)", "m^3"),
    ("maxop_mos2(ewfd.normE/1[V/m])", "1"),
]


def main() -> int:
    mph.option("session", "stand-alone")
    client = mph.start(cores=1)
    model = client.load(MODEL_PATH)
    print(f"loaded={MODEL_PATH}")
    print("datasets=", model.datasets())
    print("solutions=", model.solutions())

    for expression, unit in EXPRESSIONS:
        try:
            value = model.evaluate(expression, unit=unit)
            print(f"{expression} [{unit}] = {value}")
        except Exception as exc:  # noqa: BLE001 - expression discovery diagnostic.
            print(f"{expression} [{unit}] ERROR {type(exc).__name__}: {exc}")

    client.remove(model)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
