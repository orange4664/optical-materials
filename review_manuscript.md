# Resonant Nonlinear Nanophotonics in van der Waals Metasurfaces

**Alternative title:** Beyond High-Q Resonances: Design Rules for Nonlinear van der Waals Metasurfaces

**Target positioning:** Primary target: *Nanophotonics* Review. Fallback: *Journal of Physics: Photonics* Topical Review/Perspective/Tutorial. Stretch target: *ACS Photonics* Perspective/Review.

## Abstract

Van der Waals (vdW) crystals combine atomically sharp interfaces, strong excitonic resonances, large nonlinear susceptibilities, and mechanical stackability, making them a compelling platform for nonlinear nanophotonics. Yet the useful second-harmonic-generation (SHG) response of vdW metasurfaces is not set by the largest quality factor alone. It is governed by the symmetry and spatial location of the nonlinear source, the overlap between that source and resonant modes at the fundamental and harmonic frequencies, radiative outcoupling, excitonic absorption, bandwidth, and fabrication tolerance. This selective Review surveys resonant nonlinear vdW metasurfaces from monolayer transition-metal dichalcogenides coupled to external dielectric metasurfaces to all-vdW resonators, 3R-stacked MoS2 metasurfaces, interface-driven WS2/MoS2 nanoantennas, and emerging layered platforms beyond TMDs. We emphasize figures of merit and comparison pitfalls, because enhancement factors, conversion efficiencies, pump fluences, collection numerical apertures, and reference baselines are often not interchangeable across reports. The central message is that useful SHG requires source-aware and outcoupling-aware design rules rather than a single-minded pursuit of maximum Q.

## 1. Introduction: why vdW nonlinear metasurfaces now?

This section will motivate the field around the short interaction length of atomically thin materials, the availability of high-index patterned vdW crystals, the emergence of 3R-stacked non-centrosymmetric TMDs, and the need for calibrated device-level figures of merit.

## 2. Nonlinear sources in layered crystals

The review will separate nonlinear sources by where the nonlinear polarization lives: bulk non-centrosymmetric chi2 in 3R-stacked crystals; surface chi2 in finite-thickness or symmetry-broken flakes; interface chi2 in heterobilayers and twisted stacks; exciton-enhanced chi2 near optical resonances; and chi3 sheet nonlinearities in graphene and related centrosymmetric vdW materials.

## 3. Resonant enhancement mechanisms

This section will compare Mie resonances, anapole modes, quasi-bound states in the continuum, non-local/guided-mode resonances, and exciton-cavity hybridization. For each mechanism, the review will state what is enhanced, what is not automatically enhanced, and which failure mode matters most.

## 4. Material platforms and representative progress

The discussion will be organized by platform rather than chronology: monolayer TMDs coupled to external dielectric metasurfaces; all-TMD resonators and metasurfaces; 3R-MoS2 nanodisks and anapole-enhanced SHG; ultrathin 3R-MoS2 qBIC and non-local metasurfaces; WS2/MoS2 interface SHG nanoantennas; and broader layered nonlinear platforms including GaSe, InSe, NbOCl2, hBN, and graphene.

See `outputs/review/representative_literature_table.md` for the curated starter table.

## 5. Figures of merit and comparison pitfalls

This is a central section, not supplementary material. The review will explain why reported enhancement factors and efficiencies cannot be compared without reference baseline, pump fluence, pulse duration, repetition rate, collection numerical aperture, polarization, and area normalization. See `outputs/review/fom_comparison_pitfalls.md`.

## 6. Design rules for useful SHG

1. Optimize source-mode overlap, not just field maxima.
2. Align fundamental-field enhancement with harmonic-frequency outcoupling.
3. Use optimum Q, not maximum Q.
4. Treat excitons as both enhancement channels and loss/saturation channels.
5. Report bandwidth, angular tolerance, and fabrication tolerance alongside peak enhancement.

## Box 1. Minimal modelling of resonant SHG

The existing Python TCMT workflow is appropriate for the main review because it illustrates general design rules. The existing COMSOL qBIC-inspired unit-cell model should be treated as an illustrative tutorial or supplementary workflow only. It uses simplified, lossless, wavelength-independent material constants and therefore must not be presented as a quantitative reproduction of any 3R-MoS2 qBIC experiment.

## 7. Outlook

Open questions include wafer-scale 3R-TMD fabrication, electrically and mechanically tunable vdW metasurfaces, twist-angle and interface engineering, integration with waveguides, inverse design under fabrication constraints, calibrated absolute SHG standards, and quantum nonlinear optical regimes.

## Display items

- Figure 1: Roadmap of resonant nonlinear vdW metasurfaces.
- Figure 2: Taxonomy of nonlinear sources in layered crystals.
- Figure 3: Resonant enhancement mechanisms and failure modes.
- Table 1: Representative progress in vdW nonlinear metasurfaces.
- Table 2: Figures of merit and comparison pitfalls.
- Figure 4: Design rules for useful SHG beyond maximum Q.
- Box 1: Minimal modelling of resonant SHG.

## Initial bibliography source

The first structured seed is `literature_database.csv` with 15 curated rows. It is intentionally not exhaustive; broad bibliography expansion and DOI completion for placeholder categories are follow-up work.
