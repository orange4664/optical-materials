/*
 * qbic_3r_mos2_unitcell.java
 */

import com.comsol.model.*;
import com.comsol.model.util.*;

/** Model exported on Jun 13 2026, 01:06 by COMSOL 6.3.0.290. */
public class qbic_3r_mos2_unitcell {

  public static Model run() {
    Model model = ModelUtil.create("Model");

    model
         .modelPath("C:\\Users\\Huyinze\\Desktop\\\u540c\u6d4e\u5927\u5b66\\\u5927\u4e09\u4e0b\\\u4f4e\u7ef4\u6750\u6599\u8bba\u6587\u4f5c\u4e1a\\outputs\\comsol");

    model.label("qbic_3r_mos2_unitcell");
    model.label("3R-MoS2 qBIC unit-cell scaffold");

    model.param().set("period", "500[nm]", "Metasurface lattice period");
    model.param().set("t_mos2", "25[nm]", "3R-MoS2 film thickness");
    model.param().set("tri_side", "374[nm]", "Equilateral triangular hole side length");
    model.param().set("air_top", "450[nm]", "Air layer above the film");
    model.param().set("sub_t", "450[nm]", "SiO2 substrate thickness in simulation box");
    model.param().set("wl0", "850[nm]", "Central wavelength near qBIC");
    model.param().set("freq0", "c_const/wl0", "Central optical frequency");

    model.component().create("comp1", true);

    model.component("comp1").label("qBIC unit cell");

    model.component("comp1").geom().create("geom1", 3);
    model.component("comp1").geom("geom1").lengthUnit("nm");
    model.component("comp1").geom("geom1").create("air", "Block");
    model.component("comp1").geom("geom1").feature("air").label("Air superstrate");
    model.component("comp1").geom("geom1").feature("air").set("size", new String[]{"period", "period", "air_top"});
    model.component("comp1").geom("geom1").feature("air")
         .set("pos", new String[]{"-period/2", "-period/2", "t_mos2"});
    model.component("comp1").geom("geom1").feature("air").set("selresult", "on");
    model.component("comp1").geom("geom1").feature("air").set("selresultshow", "dom");
    model.component("comp1").geom("geom1").create("substrate", "Block");
    model.component("comp1").geom("geom1").feature("substrate").label("SiO2 substrate");
    model.component("comp1").geom("geom1").feature("substrate")
         .set("size", new String[]{"period", "period", "sub_t"});
    model.component("comp1").geom("geom1").feature("substrate")
         .set("pos", new String[]{"-period/2", "-period/2", "-sub_t"});
    model.component("comp1").geom("geom1").feature("substrate").set("selresult", "on");
    model.component("comp1").geom("geom1").feature("substrate").set("selresultshow", "dom");
    model.component("comp1").geom("geom1").create("mos2_raw", "Block");
    model.component("comp1").geom("geom1").feature("mos2_raw")
         .label("3R-MoS2 film before triangular-hole subtraction");
    model.component("comp1").geom("geom1").feature("mos2_raw")
         .set("size", new String[]{"period", "period", "t_mos2"});
    model.component("comp1").geom("geom1").feature("mos2_raw")
         .set("pos", new String[]{"-period/2", "-period/2", "0"});
    model.component("comp1").geom("geom1").create("tri_wp", "WorkPlane");
    model.component("comp1").geom("geom1").feature("tri_wp").label("Triangular hole work plane");
    model.component("comp1").geom("geom1").feature("tri_wp").set("quickplane", "xy");
    model.component("comp1").geom("geom1").feature("tri_wp").set("quickz", "0");
    model.component("comp1").geom("geom1").feature("tri_wp").geom().create("tri", "Polygon");
    model.component("comp1").geom("geom1").feature("tri_wp").geom().feature("tri")
         .label("Equilateral triangular hole profile");
    model.component("comp1").geom("geom1").feature("tri_wp").geom().feature("tri")
         .set("x", new String[]{"-tri_side/2", "tri_side/2", "0"});
    model.component("comp1").geom("geom1").feature("tri_wp").geom().feature("tri")
         .set("y", new String[]{"-sqrt(3)*tri_side/6", "-sqrt(3)*tri_side/6", "sqrt(3)*tri_side/3"});
    model.component("comp1").geom("geom1").feature("tri_wp").geom().feature("tri").set("type", "solid");
    model.component("comp1").geom("geom1").create("tri_prism", "Extrude");
    model.component("comp1").geom("geom1").feature("tri_prism").label("Triangular air-filled through-hole prism");
    model.component("comp1").geom("geom1").feature("tri_prism").selection("input").set("tri_wp");
    model.component("comp1").geom("geom1").feature("tri_prism").set("distance", "t_mos2");
    model.component("comp1").geom("geom1").feature("tri_prism").set("selresult", "on");
    model.component("comp1").geom("geom1").feature("tri_prism").set("selresultshow", "dom");
    model.component("comp1").geom("geom1").create("mos2_hole", "Difference");
    model.component("comp1").geom("geom1").feature("mos2_hole").label("3R-MoS2 film with triangular hole");
    model.component("comp1").geom("geom1").feature("mos2_hole").selection("input").set("mos2_raw");
    model.component("comp1").geom("geom1").feature("mos2_hole").selection("input2").set("tri_prism");
    model.component("comp1").geom("geom1").feature("mos2_hole").set("keepsubtract", "on");
    model.component("comp1").geom("geom1").feature("mos2_hole").set("selresult", "on");
    model.component("comp1").geom("geom1").feature("mos2_hole").set("selresultshow", "dom");
    model.component("comp1").geom("geom1").run();

    model.component("comp1").selection().create("sel_air_top", "Box");
    model.component("comp1").selection("sel_air_top").label("Air superstrate domain selection");
    model.component("comp1").selection("sel_air_top").set("entitydim", "3");
    model.component("comp1").selection("sel_air_top").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("sel_air_top").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("sel_air_top").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("sel_air_top").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("sel_air_top").set("zmin", "t_mos2+1[nm]");
    model.component("comp1").selection("sel_air_top").set("zmax", "t_mos2+air_top+1[nm]");
    model.component("comp1").selection("sel_air_top").set("condition", "inside");
    model.component("comp1").selection().create("sel_film_slab", "Box");
    model.component("comp1").selection("sel_film_slab").label("Film-height slab selection for diagnostics");
    model.component("comp1").selection("sel_film_slab").set("entitydim", "3");
    model.component("comp1").selection("sel_film_slab").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("sel_film_slab").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("sel_film_slab").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("sel_film_slab").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("sel_film_slab").set("zmin", "-1[nm]");
    model.component("comp1").selection("sel_film_slab").set("zmax", "t_mos2+1[nm]");
    model.component("comp1").selection("sel_film_slab").set("condition", "inside");
    model.component("comp1").selection().create("sel_sio2_box", "Box");
    model.component("comp1").selection("sel_sio2_box").label("SiO2 substrate box selection");
    model.component("comp1").selection("sel_sio2_box").set("entitydim", "3");
    model.component("comp1").selection("sel_sio2_box").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("sel_sio2_box").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("sel_sio2_box").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("sel_sio2_box").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("sel_sio2_box").set("zmin", "-sub_t-1[nm]");
    model.component("comp1").selection("sel_sio2_box").set("zmax", "-1[nm]");
    model.component("comp1").selection("sel_sio2_box").set("condition", "inside");
    model.component("comp1").selection().create("sel_air", "Union");
    model.component("comp1").selection("sel_air").label("Air domain selection including triangular hole");
    model.component("comp1").selection("sel_air").set("entitydim", "3");
    model.component("comp1").selection("sel_air").set("input", new String[]{"geom1_air_dom", "geom1_tri_prism_dom"});
    model.component("comp1").selection().create("sel_mos2_checked", "Union");
    model.component("comp1").selection("sel_mos2_checked").label("3R-MoS2 film excluding triangular air hole");
    model.component("comp1").selection("sel_mos2_checked").set("entitydim", "3");
    model.component("comp1").selection("sel_mos2_checked").set("input", new String[]{"geom1_mos2_hole_dom"});
    model.component("comp1").selection().create("sel_sio2", "Union");
    model.component("comp1").selection("sel_sio2").label("SiO2 substrate domain selection");
    model.component("comp1").selection("sel_sio2").set("entitydim", "3");
    model.component("comp1").selection("sel_sio2").set("input", new String[]{"geom1_substrate_dom"});
    model.component("comp1").selection().create("bnd_top", "Box");
    model.component("comp1").selection("bnd_top").label("Top port boundary");
    model.component("comp1").selection("bnd_top").set("entitydim", "2");
    model.component("comp1").selection("bnd_top").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_top").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_top").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_top").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_top").set("zmin", "t_mos2+air_top-1[nm]");
    model.component("comp1").selection("bnd_top").set("zmax", "t_mos2+air_top+1[nm]");
    model.component("comp1").selection("bnd_top").set("condition", "inside");
    model.component("comp1").selection().create("bnd_bottom", "Box");
    model.component("comp1").selection("bnd_bottom").label("Bottom port boundary");
    model.component("comp1").selection("bnd_bottom").set("entitydim", "2");
    model.component("comp1").selection("bnd_bottom").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_bottom").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_bottom").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_bottom").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_bottom").set("zmin", "-sub_t-1[nm]");
    model.component("comp1").selection("bnd_bottom").set("zmax", "-sub_t+1[nm]");
    model.component("comp1").selection("bnd_bottom").set("condition", "inside");
    model.component("comp1").selection().create("bnd_xmin", "Box");
    model.component("comp1").selection("bnd_xmin").label("x-min periodic boundary");
    model.component("comp1").selection("bnd_xmin").set("entitydim", "2");
    model.component("comp1").selection("bnd_xmin").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_xmin").set("xmax", "-period/2+1[nm]");
    model.component("comp1").selection("bnd_xmin").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_xmin").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_xmin").set("zmin", "-sub_t-1[nm]");
    model.component("comp1").selection("bnd_xmin").set("zmax", "t_mos2+air_top+1[nm]");
    model.component("comp1").selection("bnd_xmin").set("condition", "inside");
    model.component("comp1").selection().create("bnd_xmax", "Box");
    model.component("comp1").selection("bnd_xmax").label("x-max periodic boundary");
    model.component("comp1").selection("bnd_xmax").set("entitydim", "2");
    model.component("comp1").selection("bnd_xmax").set("xmin", "period/2-1[nm]");
    model.component("comp1").selection("bnd_xmax").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_xmax").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_xmax").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_xmax").set("zmin", "-sub_t-1[nm]");
    model.component("comp1").selection("bnd_xmax").set("zmax", "t_mos2+air_top+1[nm]");
    model.component("comp1").selection("bnd_xmax").set("condition", "inside");
    model.component("comp1").selection().create("bnd_ymin", "Box");
    model.component("comp1").selection("bnd_ymin").label("y-min periodic boundary");
    model.component("comp1").selection("bnd_ymin").set("entitydim", "2");
    model.component("comp1").selection("bnd_ymin").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_ymin").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_ymin").set("ymin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_ymin").set("ymax", "-period/2+1[nm]");
    model.component("comp1").selection("bnd_ymin").set("zmin", "-sub_t-1[nm]");
    model.component("comp1").selection("bnd_ymin").set("zmax", "t_mos2+air_top+1[nm]");
    model.component("comp1").selection("bnd_ymin").set("condition", "inside");
    model.component("comp1").selection().create("bnd_ymax", "Box");
    model.component("comp1").selection("bnd_ymax").label("y-max periodic boundary");
    model.component("comp1").selection("bnd_ymax").set("entitydim", "2");
    model.component("comp1").selection("bnd_ymax").set("xmin", "-period/2-1[nm]");
    model.component("comp1").selection("bnd_ymax").set("xmax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_ymax").set("ymin", "period/2-1[nm]");
    model.component("comp1").selection("bnd_ymax").set("ymax", "period/2+1[nm]");
    model.component("comp1").selection("bnd_ymax").set("zmin", "-sub_t-1[nm]");
    model.component("comp1").selection("bnd_ymax").set("zmax", "t_mos2+air_top+1[nm]");
    model.component("comp1").selection("bnd_ymax").set("condition", "inside");
    model.component("comp1").selection().create("bnd_xpair", "Union");
    model.component("comp1").selection("bnd_xpair").label("x periodic boundary pair");
    model.component("comp1").selection("bnd_xpair").set("entitydim", "2");
    model.component("comp1").selection("bnd_xpair").set("input", new String[]{"bnd_xmin", "bnd_xmax"});
    model.component("comp1").selection().create("bnd_ypair", "Union");
    model.component("comp1").selection("bnd_ypair").label("y periodic boundary pair");
    model.component("comp1").selection("bnd_ypair").set("entitydim", "2");
    model.component("comp1").selection("bnd_ypair").set("input", new String[]{"bnd_ymin", "bnd_ymax"});

    model.component("comp1").material().create("mat_air", "Common");
    model.component("comp1").material("mat_air").label("Air");
    model.component("comp1").material("mat_air").selection().named("sel_air");
    model.component("comp1").material("mat_air").propertyGroup("def")
         .set("relpermittivity", new String[]{"1", "1", "1"});
    model.component("comp1").material("mat_air").propertyGroup("def")
         .set("relpermeability", new String[]{"1", "1", "1"});
    model.component("comp1").material("mat_air").propertyGroup("def")
         .set("electricconductivity", new String[]{"0", "0", "0"});
    model.component("comp1").material("mat_air").propertyGroup("def").set("refractiveindex", "1");
    model.component("comp1").material().create("mat_sio2", "Common");
    model.component("comp1").material("mat_sio2").label("SiO2 proxy");
    model.component("comp1").material("mat_sio2").selection().named("sel_sio2");
    model.component("comp1").material("mat_sio2").propertyGroup("def")
         .set("relpermittivity", new String[]{"2.1025", "2.1025", "2.1025"});
    model.component("comp1").material("mat_sio2").propertyGroup("def")
         .set("relpermeability", new String[]{"1", "1", "1"});
    model.component("comp1").material("mat_sio2").propertyGroup("def")
         .set("electricconductivity", new String[]{"0", "0", "0"});
    model.component("comp1").material("mat_sio2").propertyGroup("def").set("refractiveindex", "1.45");
    model.component("comp1").material().create("mat_mos2", "Common");
    model.component("comp1").material("mat_mos2").label("3R-MoS2 proxy, n=4.2");
    model.component("comp1").material("mat_mos2").selection().named("sel_mos2_checked");
    model.component("comp1").material("mat_mos2").propertyGroup("def")
         .set("relpermittivity", new String[]{"17.64", "17.64", "17.64"});
    model.component("comp1").material("mat_mos2").propertyGroup("def")
         .set("relpermeability", new String[]{"1", "1", "1"});
    model.component("comp1").material("mat_mos2").propertyGroup("def")
         .set("electricconductivity", new String[]{"0", "0", "0"});
    model.component("comp1").material("mat_mos2").propertyGroup("def").set("refractiveindex", "4.2");

    model.component("comp1").physics().create("ewfd", "ElectromagneticWavesFrequencyDomain", "geom1");
    model.component("comp1").physics("ewfd").label("Electromagnetic Waves, Frequency Domain");
    model.component("comp1").physics("ewfd").feature("wee1").label("Wave equation, material-controlled all domains");

    model.component("comp1").cpl().create("aveop_mos2", "Average");
    model.component("comp1").cpl("aveop_mos2").label("Average over MoS2 film excluding air hole");
    model.component("comp1").cpl("aveop_mos2").selection().named("sel_mos2_checked");
    model.component("comp1").cpl().create("intop_mos2", "Integration");
    model.component("comp1").cpl("intop_mos2").label("Integral over MoS2 film excluding air hole");
    model.component("comp1").cpl("intop_mos2").selection().named("sel_mos2_checked");
    model.component("comp1").cpl().create("maxop_mos2", "Maximum");
    model.component("comp1").cpl("maxop_mos2").label("Maximum over MoS2 film excluding air hole");
    model.component("comp1").cpl("maxop_mos2").selection().named("sel_mos2_checked");

    model.component("comp1").physics("ewfd").create("port_top", "Port", 2);
    model.component("comp1").physics("ewfd").feature("port_top").label("Top normal-incidence port");
    model.component("comp1").physics("ewfd").feature("port_top").selection().named("bnd_top");
    model.component("comp1").physics("ewfd").feature("port_top").set("PortExcitation", "on");
    model.component("comp1").physics("ewfd").feature("port_top").set("PortType", "Periodic");
    model.component("comp1").physics("ewfd").feature("port_top").set("InputType", "E");
    model.component("comp1").physics("ewfd").feature("port_top").set("E0", new String[]{"1[V/m]", "0", "0"});
    model.component("comp1").physics("ewfd").create("port_bottom", "Port", 2);
    model.component("comp1").physics("ewfd").feature("port_bottom").label("Bottom output port");
    model.component("comp1").physics("ewfd").feature("port_bottom").selection().named("bnd_bottom");
    model.component("comp1").physics("ewfd").feature("port_bottom").set("PortType", "Periodic");
    model.component("comp1").physics("ewfd").create("pc_x", "PeriodicCondition", 2);
    model.component("comp1").physics("ewfd").feature("pc_x").label("x-direction Floquet periodicity");
    model.component("comp1").physics("ewfd").feature("pc_x").selection().named("bnd_xpair");
    model.component("comp1").physics("ewfd").feature("pc_x").set("PeriodicType", "Floquet");
    model.component("comp1").physics("ewfd").feature("pc_x").set("kFloquet", new String[]{"0", "0", "0"});
    model.component("comp1").physics("ewfd").create("pc_y", "PeriodicCondition", 2);
    model.component("comp1").physics("ewfd").feature("pc_y").label("y-direction Floquet periodicity");
    model.component("comp1").physics("ewfd").feature("pc_y").selection().named("bnd_ypair");
    model.component("comp1").physics("ewfd").feature("pc_y").set("PeriodicType", "Floquet");
    model.component("comp1").physics("ewfd").feature("pc_y").set("kFloquet", new String[]{"0", "0", "0"});

    model.component("comp1").mesh().create("mesh1");
    model.component("comp1").mesh("mesh1").feature().create("size1", "Size");
    model.component("comp1").mesh("mesh1").feature("size1").label("User-controlled optical mesh");
    model.component("comp1").mesh("mesh1").feature("size1").set("hauto", "3");
    model.component("comp1").mesh("mesh1").feature("size1").set("custom", "on");
    model.component("comp1").mesh("mesh1").feature("size1").set("hmax", "80[nm]");
    model.component("comp1").mesh("mesh1").feature("size1").set("hmin", "5[nm]");
    model.component("comp1").mesh("mesh1").feature("size1").set("hgrad", "1.35");
    model.component("comp1").mesh("mesh1").feature().create("ftet1", "FreeTet");

    model.study().create("std1");
    model.study("std1").label("Wavelength sweep");
    model.study("std1").create("wave", "Wavelength");
    model.study("std1").feature("wave").set("plist", "range(780[nm],10[nm],900[nm])");

    return model;
  }

  public static void main(String[] args) {
    run();
  }

}
