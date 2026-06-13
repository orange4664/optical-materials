# Technical Design

## Scope

This task repairs the existing course-paper workspace. It does not replace the topic, discard existing outputs, or attempt a full nonlinear Maxwell SHG simulation. The target is a defensible simplified linear COMSOL model whose field-enhancement proxies can be discussed honestly in the paper.

## Model Geometry

The current geometry subtracts a triangular prism from the MoS2 film while the air block starts only above `z=t_mos2`. The repaired geometry will add an explicit triangular air-fill prism occupying the same `0 <= z <= t_mos2` volume as the removed hole. The air material selection will become a union of the superstrate air block and the triangular fill domain.

This design keeps the existing finite-height unit-cell model and avoids a broader Boolean rebuild. It is easier to audit in the Java export and reduces the chance of breaking port and periodic boundary selections.

## Domain Selections And Operators

The script will maintain named selections:

- `sel_air_top`: air above the film.
- `sel_air_hole`: triangular air-hole volume inside the MoS2 layer.
- `sel_air`: union of the two air selections.
- `sel_mos2`: MoS2 film excluding the triangular hole.
- `sel_sio2`: SiO2 substrate.

For field proxies, scripts will create and/or evaluate expressions constrained to `sel_mos2`. Preferred COMSOL coupling operators are:

- `aveop_mos2((ewfd.normE/1[V/m])^2)`
- `aveop_mos2((ewfd.normE/1[V/m])^4)`
- `maxop_mos2(ewfd.normE/1[V/m])`

If COMSOL coupling operators cannot be created reliably through the available API, the fallback is a deterministic sampled-grid proxy over points inside the film but outside the triangular hole. The fallback must be named as a sampled proxy, not an exact volume integral.

## Spectrum And Q Extraction

The refined sweep will use a smaller wavelength step than the existing 5 nm grid. The first target is `810-850 nm` in `1 nm` steps because the current project has a peak near this window. The script will estimate:

- peak wavelength from maximum reflectance,
- baseline from sweep endpoints,
- FWHM by linear interpolation around the half-height level,
- `Q = lambda0 / FWHM`.

Lorentzian/Fano fitting can be added if SciPy is available, but the acceptance criterion is a transparent refined FWHM estimate with the method recorded.

## Near-Field Figures

COMSOL field export through `mph` can be fragile. The preferred path is to evaluate `ewfd.normE` or `ewfd.normE^2` on an x-z and/or x-y point grid and render it with matplotlib. Points will be selected in physically meaningful slices:

- x-y slice at `z=t_mos2/2` for the film midplane.
- resonance wavelength from refined sweep peak.
- off-resonance wavelength chosen from a sweep endpoint or a fixed 800 nm/840 nm reference.

If point-grid evaluation fails in COMSOL, the scripts should still produce a clear failure rather than silently generating artificial field maps.

## Paper Update

`course_paper.md` will be edited to consume the repaired outputs:

- formal title block and abstract,
- numbered figures and table references,
- equations in Markdown/LaTeX math form,
- caveats next to COMSOL figures,
- explicit distinction between `F4_volume_proxy` and true SHG conversion efficiency.

The paper will keep the established topic and literature route from the Word file.

## Compatibility

The work stays within:

- Python scripts under `scripts/`,
- generated artifacts under `outputs/comsol/` and `outputs/python/`,
- paper draft at `course_paper.md`,
- Trellis artifacts under the active task directory.

No GUI-only model edits, database dependencies, or unrelated cleanup/deletion are part of this task.
