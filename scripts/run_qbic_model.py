from __future__ import annotations

from pathlib import Path
import argparse

import mph


ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "outputs" / "comsol" / "qbic_3r_mos2_unitcell.mph"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--open-sidewall",
        action="store_true",
        help="Remove periodic conditions and add scattering sidewalls for diagnostics.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    mph.option("session", "stand-alone")
    client = mph.start(cores=2)
    model = client.load(MODEL_PATH)

    print(f"loaded={MODEL_PATH}")
    print("problems_before=", model.problems())

    print("building_geometry")
    model.build()
    print("meshing")
    model.mesh()
    print("problems_after_mesh=", model.problems())

    print("setting_single_wavelength_for_smoke_solve")
    model.java.study("std1").feature("wave").set("plist", "850[nm]")
    if args.open_sidewall:
        print("using_open_sidewall_smoke_mode")
        ewfd = model.java.component("comp1").physics("ewfd")
        for tag in ["pc_x", "pc_y"]:
            try:
                ewfd.feature().remove(tag)
                print(f"removed_periodic_condition={tag}")
            except Exception as exc:  # noqa: BLE001 - diagnostic run should continue.
                print(f"remove_periodic_condition_failed={tag}: {type(exc).__name__}: {exc}")
        for tag, selection in [
            ("sctr_xmin", "bnd_xmin"),
            ("sctr_xmax", "bnd_xmax"),
            ("sctr_ymin", "bnd_ymin"),
            ("sctr_ymax", "bnd_ymax"),
        ]:
            try:
                ewfd.create(tag, "Scattering", 2)
                feature = ewfd.feature(tag)
                feature.label(f"Open sidewall {selection}")
                feature.selection().named(selection)
                print(f"created_scattering_boundary={tag}")
            except Exception as exc:  # noqa: BLE001 - COMSOL may keep features from prior runs.
                print(f"create_scattering_failed={tag}: {type(exc).__name__}: {exc}")
    print("solving")
    model.solve("Wavelength sweep")
    print("problems_after_solve=", model.problems())

    model.save(MODEL_PATH)
    print(f"saved={MODEL_PATH}")
    client.remove(model)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
