from __future__ import annotations

from pathlib import Path

import mph


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "comsol"
MODEL_PATH = OUT_DIR / "qbic_3r_mos2_unitcell.mph"
JAVA_PATH = OUT_DIR / "qbic_3r_mos2_unitcell.java"


def set_param(model: mph.Model, name: str, value: str, description: str) -> None:
    model.java.param().set(name, value, description)


def feature(node, tag: str):
    return node.feature(tag)


def add_block(geom, tag: str, label: str, size: list[str], pos: list[str]) -> None:
    geom.create(tag, "Block")
    block = feature(geom, tag)
    block.label(label)
    block.set("size", size)
    block.set("pos", pos)


def add_domain_box_selection(comp, tag: str, label: str, zmin: str, zmax: str) -> None:
    comp.selection().create(tag, "Box")
    selection = comp.selection(tag)
    selection.label(label)
    selection.set("entitydim", "3")
    selection.set("xmin", "-period/2-1[nm]")
    selection.set("xmax", "period/2+1[nm]")
    selection.set("ymin", "-period/2-1[nm]")
    selection.set("ymax", "period/2+1[nm]")
    selection.set("zmin", zmin)
    selection.set("zmax", zmax)
    selection.set("condition", "inside")


def add_domain_union_selection(comp, tag: str, label: str, inputs: list[str]) -> None:
    comp.selection().create(tag, "Union")
    selection = comp.selection(tag)
    selection.label(label)
    selection.set("entitydim", "3")
    selection.set("input", inputs)


def add_domain_difference_selection(comp, tag: str, label: str, input_tag: str, subtract_tag: str) -> None:
    comp.selection().create(tag, "Difference")
    selection = comp.selection(tag)
    selection.label(label)
    selection.set("entitydim", "3")
    selection.set("add", [input_tag])
    selection.set("subtract", [subtract_tag])


def add_boundary_box_selection(
    comp,
    tag: str,
    label: str,
    xmin: str,
    xmax: str,
    ymin: str,
    ymax: str,
    zmin: str,
    zmax: str,
    condition: str = "intersects",
) -> None:
    comp.selection().create(tag, "Box")
    selection = comp.selection(tag)
    selection.label(label)
    selection.set("entitydim", "2")
    selection.set("xmin", xmin)
    selection.set("xmax", xmax)
    selection.set("ymin", ymin)
    selection.set("ymax", ymax)
    selection.set("zmin", zmin)
    selection.set("zmax", zmax)
    selection.set("condition", condition)


def add_union_selection(comp, tag: str, label: str, inputs: list[str]) -> None:
    comp.selection().create(tag, "Union")
    selection = comp.selection(tag)
    selection.label(label)
    selection.set("entitydim", "2")
    selection.set("input", inputs)


def add_geometry_result_selection(geom, feature_tag: str) -> None:
    geom.feature(feature_tag).set("selresult", "on")
    geom.feature(feature_tag).set("selresultshow", "dom")


def add_coupling_operator(comp, tag: str, kind: str, label: str, selection: str) -> None:
    comp.cpl().create(tag, kind)
    operator = comp.cpl(tag)
    operator.label(label)
    operator.selection().named(selection)


def configure_wave_equation(feature, epsilonr: str, selection: str | None = None) -> None:
    if selection is not None:
        feature.selection().named(selection)
    feature.set("DisplacementFieldModel", "RelativePermittivity")
    feature.set("epsilonr_mat", "userdef")
    feature.set("epsilonr", [epsilonr, epsilonr, epsilonr])
    feature.set("mur_mat", "userdef")
    feature.set("mur", ["1", "1", "1"])
    feature.set("sigma_mat", "userdef")
    feature.set("sigma", ["0", "0", "0"])


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    mph.option("session", "stand-alone")
    client = mph.start(cores=2)
    model = client.create("qbic_3r_mos2_unitcell")
    java = model.java
    java.label("3R-MoS2 qBIC unit-cell scaffold")

    set_param(model, "period", "500[nm]", "Metasurface lattice period")
    set_param(model, "t_mos2", "25[nm]", "3R-MoS2 film thickness")
    set_param(model, "tri_side", "374[nm]", "Equilateral triangular hole side length")
    set_param(model, "air_top", "450[nm]", "Air layer above the film")
    set_param(model, "sub_t", "450[nm]", "SiO2 substrate thickness in simulation box")
    set_param(model, "wl0", "850[nm]", "Central wavelength near qBIC")
    set_param(model, "freq0", "c_const/wl0", "Central optical frequency")

    java.component().create("comp1", True)
    comp = java.component("comp1")
    comp.label("qBIC unit cell")

    comp.geom().create("geom1", 3)
    geom = comp.geom("geom1")
    geom.lengthUnit("nm")

    # Coordinate convention: MoS2 film occupies 0 <= z <= t_mos2.
    # The air and substrate boxes give the electromagnetic domain finite height.
    add_block(
        geom,
        "air",
        "Air superstrate",
        ["period", "period", "air_top"],
        ["-period/2", "-period/2", "t_mos2"],
    )
    add_geometry_result_selection(geom, "air")
    add_block(
        geom,
        "substrate",
        "SiO2 substrate",
        ["period", "period", "sub_t"],
        ["-period/2", "-period/2", "-sub_t"],
    )
    add_geometry_result_selection(geom, "substrate")
    add_block(
        geom,
        "mos2_raw",
        "3R-MoS2 film before triangular-hole subtraction",
        ["period", "period", "t_mos2"],
        ["-period/2", "-period/2", "0"],
    )

    # Triangular through-hole as a prism. The triangle is centered at x=y=0.
    # For an equilateral triangle: height = sqrt(3)/2 * side.
    geom.create("tri_wp", "WorkPlane")
    wp = feature(geom, "tri_wp")
    wp.label("Triangular hole work plane")
    wp.set("quickplane", "xy")
    wp.set("quickz", "0")
    wp_geom = wp.geom()
    wp_geom.create("tri", "Polygon")
    tri = wp_geom.feature("tri")
    tri.label("Equilateral triangular hole profile")
    tri.set(
        "x",
        [
            "-tri_side/2",
            "tri_side/2",
            "0",
        ],
    )
    tri.set(
        "y",
        [
            "-sqrt(3)*tri_side/6",
            "-sqrt(3)*tri_side/6",
            "sqrt(3)*tri_side/3",
        ],
    )
    tri.set("type", "solid")

    geom.create("tri_prism", "Extrude")
    prism = feature(geom, "tri_prism")
    prism.label("Triangular air-filled through-hole prism")
    prism.selection("input").set("tri_wp")
    prism.set("distance", "t_mos2")
    add_geometry_result_selection(geom, "tri_prism")

    geom.create("mos2_hole", "Difference")
    diff = feature(geom, "mos2_hole")
    diff.label("3R-MoS2 film with triangular hole")
    diff.selection("input").set("mos2_raw")
    diff.selection("input2").set("tri_prism")
    diff.set("keepsubtract", "on")
    add_geometry_result_selection(geom, "mos2_hole")

    geom.run()

    add_domain_box_selection(comp, "sel_air_top", "Air superstrate domain selection", "t_mos2+1[nm]", "t_mos2+air_top+1[nm]")
    add_domain_box_selection(comp, "sel_film_slab", "Film-height slab selection for diagnostics", "-1[nm]", "t_mos2+1[nm]")
    add_domain_box_selection(comp, "sel_sio2_box", "SiO2 substrate box selection", "-sub_t-1[nm]", "-1[nm]")
    add_domain_union_selection(
        comp,
        "sel_air",
        "Air domain selection including triangular hole",
        ["geom1_air_dom", "geom1_tri_prism_dom"],
    )
    add_domain_union_selection(comp, "sel_mos2_checked", "3R-MoS2 film excluding triangular air hole", ["geom1_mos2_hole_dom"])
    add_domain_union_selection(comp, "sel_sio2", "SiO2 substrate domain selection", ["geom1_substrate_dom"])
    add_boundary_box_selection(
        comp,
        "bnd_top",
        "Top port boundary",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "t_mos2+air_top-1[nm]",
        "t_mos2+air_top+1[nm]",
        "inside",
    )
    add_boundary_box_selection(
        comp,
        "bnd_bottom",
        "Bottom port boundary",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "-sub_t-1[nm]",
        "-sub_t+1[nm]",
        "inside",
    )
    add_boundary_box_selection(
        comp,
        "bnd_xmin",
        "x-min periodic boundary",
        "-period/2-1[nm]",
        "-period/2+1[nm]",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "-sub_t-1[nm]",
        "t_mos2+air_top+1[nm]",
        "inside",
    )
    add_boundary_box_selection(
        comp,
        "bnd_xmax",
        "x-max periodic boundary",
        "period/2-1[nm]",
        "period/2+1[nm]",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "-sub_t-1[nm]",
        "t_mos2+air_top+1[nm]",
        "inside",
    )
    add_boundary_box_selection(
        comp,
        "bnd_ymin",
        "y-min periodic boundary",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "-period/2-1[nm]",
        "-period/2+1[nm]",
        "-sub_t-1[nm]",
        "t_mos2+air_top+1[nm]",
        "inside",
    )
    add_boundary_box_selection(
        comp,
        "bnd_ymax",
        "y-max periodic boundary",
        "-period/2-1[nm]",
        "period/2+1[nm]",
        "period/2-1[nm]",
        "period/2+1[nm]",
        "-sub_t-1[nm]",
        "t_mos2+air_top+1[nm]",
        "inside",
    )
    add_union_selection(comp, "bnd_xpair", "x periodic boundary pair", ["bnd_xmin", "bnd_xmax"])
    add_union_selection(comp, "bnd_ypair", "y periodic boundary pair", ["bnd_ymin", "bnd_ymax"])

    comp.material().create("mat_air", "Common")
    mat_air = comp.material("mat_air")
    mat_air.label("Air")
    mat_air.selection().named("sel_air")
    mat_air.propertyGroup("def").set("relpermittivity", ["1", "1", "1"])
    mat_air.propertyGroup("def").set("relpermeability", ["1", "1", "1"])
    mat_air.propertyGroup("def").set("electricconductivity", ["0", "0", "0"])
    mat_air.propertyGroup("def").set("refractiveindex", "1")

    comp.material().create("mat_sio2", "Common")
    mat_sio2 = comp.material("mat_sio2")
    mat_sio2.label("SiO2 proxy")
    mat_sio2.selection().named("sel_sio2")
    mat_sio2.propertyGroup("def").set("relpermittivity", ["2.1025", "2.1025", "2.1025"])
    mat_sio2.propertyGroup("def").set("relpermeability", ["1", "1", "1"])
    mat_sio2.propertyGroup("def").set("electricconductivity", ["0", "0", "0"])
    mat_sio2.propertyGroup("def").set("refractiveindex", "1.45")

    comp.material().create("mat_mos2", "Common")
    mat_mos2 = comp.material("mat_mos2")
    mat_mos2.label("3R-MoS2 proxy, n=4.2")
    mat_mos2.selection().named("sel_mos2_checked")
    mat_mos2.propertyGroup("def").set("relpermittivity", ["17.64", "17.64", "17.64"])
    mat_mos2.propertyGroup("def").set("relpermeability", ["1", "1", "1"])
    mat_mos2.propertyGroup("def").set("electricconductivity", ["0", "0", "0"])
    mat_mos2.propertyGroup("def").set("refractiveindex", "4.2")

    comp.physics().create("ewfd", "ElectromagneticWavesFrequencyDomain", "geom1")
    ewfd = comp.physics("ewfd")
    ewfd.label("Electromagnetic Waves, Frequency Domain")
    ewfd.feature("wee1").label("Wave equation, material-controlled all domains")

    add_coupling_operator(comp, "aveop_mos2", "Average", "Average over MoS2 film excluding air hole", "sel_mos2_checked")
    add_coupling_operator(comp, "intop_mos2", "Integration", "Integral over MoS2 film excluding air hole", "sel_mos2_checked")
    add_coupling_operator(comp, "maxop_mos2", "Maximum", "Maximum over MoS2 film excluding air hole", "sel_mos2_checked")
    ewfd.create("port_top", "Port", 2)
    port_top = ewfd.feature("port_top")
    port_top.label("Top normal-incidence port")
    port_top.selection().named("bnd_top")
    port_top.set("PortExcitation", "on")
    port_top.set("PortType", "Periodic")
    port_top.set("InputType", "E")
    port_top.set("E0", ["1[V/m]", "0", "0"])

    ewfd.create("port_bottom", "Port", 2)
    port_bottom = ewfd.feature("port_bottom")
    port_bottom.label("Bottom output port")
    port_bottom.selection().named("bnd_bottom")
    port_bottom.set("PortType", "Periodic")

    ewfd.create("pc_x", "PeriodicCondition", 2)
    pc_x = ewfd.feature("pc_x")
    pc_x.label("x-direction Floquet periodicity")
    pc_x.selection().named("bnd_xpair")
    pc_x.set("PeriodicType", "Floquet")
    pc_x.set("kFloquet", ["0", "0", "0"])

    ewfd.create("pc_y", "PeriodicCondition", 2)
    pc_y = ewfd.feature("pc_y")
    pc_y.label("y-direction Floquet periodicity")
    pc_y.selection().named("bnd_ypair")
    pc_y.set("PeriodicType", "Floquet")
    pc_y.set("kFloquet", ["0", "0", "0"])

    comp.mesh().create("mesh1")
    mesh = comp.mesh("mesh1")
    mesh.feature().create("size1", "Size")
    size = mesh.feature("size1")
    size.label("User-controlled optical mesh")
    size.set("hauto", "3")
    size.set("custom", "on")
    size.set("hmax", "80[nm]")
    size.set("hmin", "5[nm]")
    size.set("hgrad", "1.35")
    mesh.feature().create("ftet1", "FreeTet")

    java.study().create("std1")
    study = java.study("std1")
    study.label("Wavelength sweep")
    study.create("wave", "Wavelength")
    study.feature("wave").set("plist", "range(780[nm],10[nm],900[nm])")

    model.save(MODEL_PATH)
    model.save(JAVA_PATH, format="java")

    print(f"saved_mph={MODEL_PATH}")
    print(f"saved_java={JAVA_PATH}")
    print("components=", model.components())
    print("geometries=", model.geometries())
    print("materials=", model.materials())
    print("physics=", model.physics())
    print("studies=", model.studies())
    print("problems=", model.problems())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
