from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "outputs" / "review"
LITERATURE_CSV = ROOT / "literature_database.csv"
REPRESENTATIVE_TABLE = OUT_DIR / "representative_literature_table.md"
FOM_TABLE_CSV = OUT_DIR / "fom_comparison_pitfalls.csv"
FOM_TABLE_MD = OUT_DIR / "fom_comparison_pitfalls.md"
DISPLAY_PLAN = OUT_DIR / "display_item_plan.md"
REVIEW_RUNS = ROOT / "REVIEW_RUNS.md"
MANUSCRIPT = ROOT / "review_manuscript.md"


COLUMNS = [
    "id",
    "year",
    "authors",
    "title",
    "venue",
    "material_platform",
    "dimensionality_or_source_type",
    "resonance_mechanism",
    "nonlinear_process",
    "metric_reported",
    "baseline_or_reference",
    "pump_condition_note",
    "device_geometry",
    "key_message",
    "role_in_review",
    "doi_or_url",
]


LITERATURE_ROWS = [
    {
        "year": "2024",
        "authors": "Zeng et al.",
        "title": "Nonlinear optics of two-dimensional heterostructures",
        "venue": "Frontiers of Physics",
        "material_platform": "2D heterostructures",
        "dimensionality_or_source_type": "bulk/surface/interface/exciton-enhanced chi2",
        "resonance_mechanism": "material and exciton physics",
        "nonlinear_process": "SHG and broader nonlinear optics",
        "metric_reported": "review; not a single device FoM",
        "baseline_or_reference": "not applicable",
        "pump_condition_note": "varies across reviewed literature",
        "device_geometry": "2D heterostructures",
        "key_message": "Broad context for nonlinear sources, stacking, symmetry, and heterostructure control.",
        "role_in_review": "review and context",
        "doi_or_url": "https://link.springer.com/article/10.1007/s11467-023-1363-6",
    },
    {
        "year": "2019",
        "authors": "Verre et al.",
        "title": "Transition metal dichalcogenide nanodisks as high-index dielectric Mie nanoresonators",
        "venue": "Nature Nanotechnology",
        "material_platform": "TMD nanodisks",
        "dimensionality_or_source_type": "patterned vdW semiconductor resonator",
        "resonance_mechanism": "Mie resonance",
        "nonlinear_process": "linear resonance platform; nonlinear design context",
        "metric_reported": "scattering/resonance response",
        "baseline_or_reference": "nanodisk vs unpatterned material context",
        "pump_condition_note": "not the main SHG FoM source",
        "device_geometry": "TMD nanodisks",
        "key_message": "Establishes TMDs as high-index resonant building blocks, not only passive monolayer sheets.",
        "role_in_review": "all-TMD resonators",
        "doi_or_url": "https://doi.org/10.1038/s41565-019-0442-x",
    },
    {
        "year": "2020",
        "authors": "Bernhardt et al.",
        "title": "Quasi-BIC Resonant Enhancement of Second-Harmonic Generation in WS2 Monolayers",
        "venue": "Nano Letters",
        "material_platform": "WS2 monolayer on dielectric metasurface",
        "dimensionality_or_source_type": "monolayer chi2 sheet",
        "resonance_mechanism": "quasi-BIC",
        "nonlinear_process": "SHG",
        "metric_reported": "enhancement factor",
        "baseline_or_reference": "monolayer/reference metasurface baseline must be checked before comparison",
        "pump_condition_note": "pulse and collection conditions must be extracted before quantitative comparison",
        "device_geometry": "monolayer TMD coupled to external metasurface",
        "key_message": "Representative monolayer-plus-external-resonator route for SHG enhancement.",
        "role_in_review": "monolayer + external metasurface",
        "doi_or_url": "https://doi.org/10.1021/acs.nanolett.0c01603",
    },
    {
        "year": "2020",
        "authors": "Busschaert et al.",
        "title": "Transition metal dichalcogenide resonators for second harmonic signal enhancement",
        "venue": "ACS Photonics",
        "material_platform": "TMD resonators",
        "dimensionality_or_source_type": "patterned TMD nonlinear source",
        "resonance_mechanism": "Mie / resonator enhancement",
        "nonlinear_process": "SHG",
        "metric_reported": "SHG signal enhancement",
        "baseline_or_reference": "resonator vs reference geometry; exact baseline needs extraction",
        "pump_condition_note": "extract before numerical comparison",
        "device_geometry": "TMD resonators",
        "key_message": "Early bridge from TMD materials to resonant nonlinear nanostructures.",
        "role_in_review": "all-TMD resonators",
        "doi_or_url": "https://pubs.acs.org/journal/apchd5",
    },
    {
        "year": "2021",
        "authors": "Nauman et al.",
        "title": "Tunable unidirectional nonlinear emission from transition-metal-dichalcogenide metasurfaces",
        "venue": "Nature Communications",
        "material_platform": "MoS2 metasurface",
        "dimensionality_or_source_type": "patterned TMD nonlinear source",
        "resonance_mechanism": "Mie multipole interference",
        "nonlinear_process": "SHG / nonlinear emission",
        "metric_reported": "directional nonlinear emission",
        "baseline_or_reference": "radiation pattern and collection geometry matter",
        "pump_condition_note": "extract before efficiency comparison",
        "device_geometry": "patterned TMD metasurface",
        "key_message": "Shows that useful SHG includes emission direction and outcoupling, not only local field magnitude.",
        "role_in_review": "all-TMD resonators",
        "doi_or_url": "https://doi.org/10.1038/s41467-021-25717-x",
    },
    {
        "year": "2024",
        "authors": "Zograf et al.",
        "title": "Combining ultrahigh index with exceptional nonlinearity in resonant 3R-MoS2 nanodisks",
        "venue": "Nature Photonics",
        "material_platform": "3R-MoS2 nanodisks",
        "dimensionality_or_source_type": "bulk non-centrosymmetric chi2",
        "resonance_mechanism": "anapole / Mie resonance",
        "nonlinear_process": "SHG",
        "metric_reported": "SHG enhancement and resonant response",
        "baseline_or_reference": "nanodisk/reference definition must be kept explicit",
        "pump_condition_note": "extract before comparing absolute values",
        "device_geometry": "3R-MoS2 nanodisks",
        "key_message": "Key case for source-rich, high-index all-vdW resonators and anapole-enhanced internal fields.",
        "role_in_review": "3R-MoS2 nanodisks",
        "doi_or_url": "https://doi.org/10.1038/s41566-024-01444-9",
    },
    {
        "year": "2025",
        "authors": "Zograf et al.",
        "title": "Ultrathin 3R-MoS2 metasurfaces with atomically precise edges for efficient nonlinear nanophotonics",
        "venue": "Communications Physics",
        "material_platform": "ultrathin 3R-MoS2 metasurface",
        "dimensionality_or_source_type": "bulk non-centrosymmetric chi2",
        "resonance_mechanism": "qBIC",
        "nonlinear_process": "SHG",
        "metric_reported": "nonlinear metasurface performance",
        "baseline_or_reference": "published reference must be used; local COMSOL scaffold is illustrative only",
        "pump_condition_note": "extract for FoM comparison",
        "device_geometry": "triangular-hole ultrathin 3R-MoS2 metasurface",
        "key_message": "Primary qBIC-inspired 3R-MoS2 case, but not the sole review storyline.",
        "role_in_review": "3R-MoS2 qBIC metasurfaces",
        "doi_or_url": "https://doi.org/10.1038/s42005-025-02194-y",
    },
    {
        "year": "2025",
        "authors": "Tognazzi et al.",
        "title": "Interface second harmonic generation enhancement in bulk WS2/MoS2 hetero-bilayer van der Waals nanoantennas",
        "venue": "Light: Science & Applications",
        "material_platform": "WS2/MoS2 hetero-bilayer nanoantenna",
        "dimensionality_or_source_type": "interface chi2",
        "resonance_mechanism": "anapole / exciton-enhanced resonance",
        "nonlinear_process": "interface SHG",
        "metric_reported": "interface SHG enhancement",
        "baseline_or_reference": "interface source requires different baseline than bulk 3R-MoS2",
        "pump_condition_note": "exciton absorption and pump conditions must be tracked",
        "device_geometry": "hetero-bilayer vdW nanoantenna",
        "key_message": "Key counterexample showing nonlinear source location can dominate design rules.",
        "role_in_review": "interface SHG",
        "doi_or_url": "https://doi.org/10.1038/s41377-025-01983-y",
    },
    {
        "year": "2025",
        "authors": "Peng et al.",
        "title": "3R-stacked transition metal dichalcogenide non-local metasurface for efficient second-harmonic generation",
        "venue": "Nature Photonics",
        "material_platform": "3R-stacked TMD non-local metasurface",
        "dimensionality_or_source_type": "bulk non-centrosymmetric chi2",
        "resonance_mechanism": "non-local resonance / guided-mode resonance",
        "nonlinear_process": "SHG",
        "metric_reported": "efficient SHG",
        "baseline_or_reference": "device-level baseline must be extracted",
        "pump_condition_note": "extract pump and collection calibration before comparison",
        "device_geometry": "non-local 3R-TMD metasurface",
        "key_message": "Shows a route from isolated nanoresonators toward integrated non-local vdW metasurfaces.",
        "role_in_review": "3R non-local metasurfaces",
        "doi_or_url": "https://doi.org/10.1038/s41566-025-01781-3",
    },
    {
        "year": "2024",
        "authors": "Huang et al.",
        "title": "Control of second-harmonic generation in two-dimensional layered materials",
        "venue": "Advanced Functional Materials",
        "material_platform": "2D layered materials",
        "dimensionality_or_source_type": "symmetry-controlled chi2",
        "resonance_mechanism": "material control / light-matter interaction",
        "nonlinear_process": "SHG",
        "metric_reported": "review; control strategies",
        "baseline_or_reference": "not applicable",
        "pump_condition_note": "varies across reviewed literature",
        "device_geometry": "2D layered-material systems",
        "key_message": "Review context for symmetry breaking, stacking, and light-matter interaction control of SHG.",
        "role_in_review": "review and context",
        "doi_or_url": "https://onlinelibrary.wiley.com/journal/16163028",
    },
    {
        "year": "2025",
        "authors": "Li et al.",
        "title": "Second harmonic generation from bound-state in the continuum-hosted few-layers van der Waals metasurface",
        "venue": "Nanophotonics",
        "material_platform": "few-layer vdW metasurface",
        "dimensionality_or_source_type": "few-layer vdW nonlinear source",
        "resonance_mechanism": "BIC / qBIC",
        "nonlinear_process": "SHG",
        "metric_reported": "BIC-hosted SHG enhancement",
        "baseline_or_reference": "check few-layer reference and pump conditions",
        "pump_condition_note": "extract before comparison",
        "device_geometry": "few-layer vdW metasurface",
        "key_message": "Directly fits Nanophotonics target and connects BIC physics to few-layer vdW nonlinear sources.",
        "role_in_review": "broader vdW nonlinear platforms",
        "doi_or_url": "https://doi.org/10.1515/nanoph-2024-0630",
    },
    {
        "year": "2024",
        "authors": "Nan et al.",
        "title": "van der Waals NbOCl2 Nanodisks for Enhanced Second-Harmonic Generation",
        "venue": "Nano Letters",
        "material_platform": "NbOCl2 vdW nanodisks",
        "dimensionality_or_source_type": "bulk/surface chi2",
        "resonance_mechanism": "Mie resonance",
        "nonlinear_process": "SHG",
        "metric_reported": "enhanced SHG",
        "baseline_or_reference": "nanodisk/reference baseline to extract",
        "pump_condition_note": "extract before comparison",
        "device_geometry": "vdW nanodisks",
        "key_message": "Extends the review beyond TMDs to emerging non-centrosymmetric layered materials.",
        "role_in_review": "broader vdW nonlinear platforms",
        "doi_or_url": "https://doi.org/10.1021/acs.nanolett.4c05114",
    },
    {
        "year": "various",
        "authors": "GaSe / InSe nonlinear photonics literature",
        "title": "Layered III-VI semiconductors for second-order nonlinear nanophotonics",
        "venue": "to be expanded",
        "material_platform": "GaSe / InSe layered semiconductors",
        "dimensionality_or_source_type": "bulk/surface chi2",
        "resonance_mechanism": "exciton / cavity / Mie resonance",
        "nonlinear_process": "SHG",
        "metric_reported": "candidate FoM entries need extraction",
        "baseline_or_reference": "to be extracted",
        "pump_condition_note": "to be extracted",
        "device_geometry": "layered flakes or resonators",
        "key_message": "Placeholder category for follow-up bibliography expansion beyond the initial TMD-centered seed.",
        "role_in_review": "broader vdW nonlinear platforms",
        "doi_or_url": "TODO: add specific GaSe/InSe papers",
    },
    {
        "year": "various",
        "authors": "hBN nonlinear/polaritonic photonics literature",
        "title": "hBN polaritonic and nonlinear nanophotonics as a comparison platform",
        "venue": "to be expanded",
        "material_platform": "hBN",
        "dimensionality_or_source_type": "surface/interface nonlinear source or chi3/polaritonic response",
        "resonance_mechanism": "phonon polariton / cavity resonance",
        "nonlinear_process": "SHG / THG / nonlinear polaritonics",
        "metric_reported": "candidate FoM entries need extraction",
        "baseline_or_reference": "to be extracted",
        "pump_condition_note": "to be extracted",
        "device_geometry": "polaritonic flakes, cavities, or resonators",
        "key_message": "Placeholder category to keep the final review from becoming TMD-only.",
        "role_in_review": "broader vdW nonlinear platforms",
        "doi_or_url": "TODO: add specific hBN papers",
    },
    {
        "year": "various",
        "authors": "Graphene nonlinear metasurface literature",
        "title": "Graphene chi3 nonlinear nanophotonics as a contrast to chi2 vdW metasurfaces",
        "venue": "to be expanded",
        "material_platform": "graphene",
        "dimensionality_or_source_type": "chi3 sheet conductivity",
        "resonance_mechanism": "plasmonic / cavity resonance",
        "nonlinear_process": "THG / Kerr / four-wave mixing",
        "metric_reported": "candidate FoM entries need extraction",
        "baseline_or_reference": "to be extracted",
        "pump_condition_note": "to be extracted",
        "device_geometry": "graphene plasmonic or cavity-coupled structures",
        "key_message": "Contrasts chi3 sheet nonlinearities with chi2 source engineering in non-centrosymmetric vdW crystals.",
        "role_in_review": "chi3 comparison platform",
        "doi_or_url": "TODO: add specific graphene papers",
    },
]


FOM_ROWS = [
    ("Enhancement factor", "SHG signal from resonant structure divided by a chosen reference signal.", "Depends on the reference: bare substrate, flat flake, unpatterned film, off-resonance wavelength, or different collection geometry.", "Reference definition, pump wavelength, collection NA, polarization, area normalization, pulse conditions."),
    ("Absolute conversion efficiency", "Generated second-harmonic power divided by incident fundamental power.", "Varies with peak intensity, pulse duration, focusing area, repetition rate, and collection calibration.", "Average and peak pump power, spot size, pulse duration, repetition rate, detected and total emitted SH power calibration."),
    ("Single-pass efficiency", "Frequency-conversion efficiency for one pass through the nonlinear structure.", "Not directly comparable to focused free-space nanoantenna experiments.", "Input/output coupling loss, propagation length, mode area, phase matching or resonance condition."),
    ("Pump fluence / peak intensity", "Pulse energy or peak power density at the fundamental frequency.", "Average power alone hides pulse duration and repetition-rate differences.", "Pulse width, repetition rate, spot size, pulse shape, average power, estimated peak intensity."),
    ("Collection NA and radiation pattern", "Angular collection window and far-field radiation distribution.", "A directional antenna can look stronger simply because more light enters the objective.", "Objective NA, collection side, polarization analyzer, radiation-pattern correction if available."),
    ("Bandwidth / tolerance", "Spectral, angular, temperature, or fabrication window over which the nonlinear response remains useful.", "Peak enhancement alone ignores detuning sensitivity.", "Linewidth, Q extraction method, angular tolerance, fabrication parameter sweep, fit residuals when applicable."),
    ("Source-mode overlap", "Spatial and tensor overlap between nonlinear polarization source and resonant fields.", "Maximum field at a boundary or corner may not represent useful nonlinear source strength.", "Material-domain or interface-domain overlap integral, tensor component, field normalization."),
]


DISPLAY_ITEMS = [
    ("Figure 1", "Roadmap of resonant nonlinear vdW metasurfaces", "Monolayer-on-metasurface -> all-TMD resonator -> 3R/non-local vdW metasurface."),
    ("Figure 2", "Taxonomy of nonlinear sources in layered crystals", "Bulk chi2, surface chi2, interface chi2, exciton-enhanced chi2, and chi3 sheets."),
    ("Figure 3", "Resonant enhancement mechanisms and failure modes", "Mie, anapole, qBIC, non-local resonance, exciton/cavity hybridization; each with what is enhanced and what can go wrong."),
    ("Table 1", "Representative progress in vdW nonlinear metasurfaces", "Curated rows from literature_database.csv grouped by platform and role."),
    ("Table 2", "Figures of merit and comparison pitfalls", "Definitions, pitfalls, and minimum reporting requirements."),
    ("Figure 4", "Design rules for useful SHG beyond maximum Q", "Source-mode overlap, double resonance, optimum Q, excitons as gain/loss, robust fabrication window."),
    ("Box 1", "Minimal modelling of resonant SHG", "TCMT useful-SHG proxy and illustrative qBIC-inspired COMSOL workflow demoted to tutorial/supplementary status."),
]


def write_csv(path: Path, rows: list[dict[str, str]], columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell.replace("|", "/") for cell in row) + " |")
    return "\n".join(lines) + "\n"


def numbered_rows() -> list[dict[str, str]]:
    rows = []
    for index, row in enumerate(LITERATURE_ROWS, start=1):
        rows.append({"id": f"R{index:03d}", **row})
    return rows


def write_representative_table(rows: list[dict[str, str]]) -> None:
    table_rows = [
        [
            row["role_in_review"],
            row["year"],
            row["material_platform"],
            row["resonance_mechanism"],
            row["title"],
            row["doi_or_url"],
        ]
        for row in rows
    ]
    content = "# Representative Literature Table\n\n"
    content += "This is a curated starter table, not the final exhaustive bibliography.\n\n"
    content += markdown_table(["Role", "Year", "Platform", "Mechanism", "Representative paper", "DOI/URL"], table_rows)
    REPRESENTATIVE_TABLE.write_text(content, encoding="utf-8")


def write_fom_tables() -> None:
    rows = [
        {
            "metric": metric,
            "definition": definition,
            "comparison_pitfall": pitfall,
            "minimum_report": minimum,
        }
        for metric, definition, pitfall, minimum in FOM_ROWS
    ]
    write_csv(FOM_TABLE_CSV, rows, ["metric", "definition", "comparison_pitfall", "minimum_report"])
    md_rows = [[row["metric"], row["definition"], row["comparison_pitfall"], row["minimum_report"]] for row in rows]
    content = "# Figures of Merit and Comparison Pitfalls\n\n"
    content += markdown_table(["Metric", "Definition", "Comparison pitfall", "Minimum reporting requirement"], md_rows)
    FOM_TABLE_MD.write_text(content, encoding="utf-8")


def write_display_plan() -> None:
    lines = ["# Display Item Plan", "", "This is the first display-item scaffold. Polished schematics are follow-up work.", ""]
    for item_id, title, content in DISPLAY_ITEMS:
        lines.extend([f"## {item_id}: {title}", "", f"- Content: {content}", "- Status: drafted as plan / table callout.", ""])
    DISPLAY_PLAN.write_text("\n".join(lines), encoding="utf-8")


def write_manuscript(row_count: int) -> None:
    content = f"""# Resonant Nonlinear Nanophotonics in van der Waals Metasurfaces

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

The first structured seed is `literature_database.csv` with {row_count} curated rows. It is intentionally not exhaustive; broad bibliography expansion and DOI completion for placeholder categories are follow-up work.
"""
    MANUSCRIPT.write_text(content, encoding="utf-8")


def write_review_runs(row_count: int) -> None:
    content = f"""# Review Manuscript Runs

This file tracks the review-journal restructuring artifacts. It does not replace `RUNS.md`, which documents the course-paper COMSOL/Python scaffold.

## Current Review Artifacts

- `review_manuscript.md` - English review manuscript scaffold.
- `literature_database.csv` - curated starter literature database with {row_count} rows.
- `outputs/review/representative_literature_table.md`
- `outputs/review/fom_comparison_pitfalls.csv`
- `outputs/review/fom_comparison_pitfalls.md`
- `outputs/review/display_item_plan.md`

## Relationship To Existing COMSOL Work

The COMSOL qBIC-inspired model remains useful as tutorial or supplementary material. It should not be used as the central evidence chain for a Nanophotonics/JPhys/ACS review. The review's main evidence should come from published literature, comparison of figures of merit, and mechanism-level design rules.

## Process Constraint

No COMSOL process is started, stopped, restarted, or cleaned by the review asset builder. The user may run independent `mph`/COMSOL jobs in parallel.

## Follow-Up Literature Work

The current database is a scoped seed, not a final bibliography. Later work should expand GaSe, InSe, hBN, graphene, metrology, and calibration entries with paper-specific DOI and metric extraction.
"""
    REVIEW_RUNS.write_text(content, encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = numbered_rows()
    write_csv(LITERATURE_CSV, rows, COLUMNS)
    write_representative_table(rows)
    write_fom_tables()
    write_display_plan()
    write_manuscript(len(rows))
    write_review_runs(len(rows))
    print(f"saved_literature_csv={LITERATURE_CSV} rows={len(rows)}")
    print(f"saved_manuscript={MANUSCRIPT}")
    print(f"saved_review_dir={OUT_DIR}")
    print(f"saved_review_runs={REVIEW_RUNS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
