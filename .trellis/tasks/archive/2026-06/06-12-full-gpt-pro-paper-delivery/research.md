# Research Notes

## Verified Core Sources

- Zograf et al., "Combining ultrahigh index with exceptional nonlinearity in resonant 3R-MoS2 nanodisks", Nature Photonics, 2024.
  - URL: https://www.nature.com/articles/s41566-024-01444-9
  - Role: 3R-MoS2 nanodisk/anapole mechanism case.
- Zograf et al., "Ultrathin 3R-MoS2 metasurfaces with atomically precise edges for efficient nonlinear nanophotonics", Communications Physics, 2025.
  - URL: https://www.nature.com/articles/s42005-025-02194-y
  - Role: main qBIC metasurface case and primary COMSOL target.
- Tognazzi et al., "Interface second harmonic generation enhancement in bulk WS2/MoS2 hetero-bilayer van der Waals nanoantennas", Light: Science & Applications, 2025.
  - URL: https://www.nature.com/articles/s41377-025-01983-y
  - Role: interface SHG and exciton/anapole comparison.
- Peng et al., "3R-stacked transition metal dichalcogenide non-local metasurface for efficient second-harmonic generation", Nature Photonics, 2025.
  - URL: https://www.dare.uva.nl/id/e69de26d-d74a-48a0-b406-85174baaf003
  - DOI noted by secondary source: 10.1038/s41566-025-01781-3.
  - Role: outlook/application endpoint.

## Verified Background Sources

- Zeng et al., "Nonlinear optics of two-dimensional heterostructures", Frontiers of Physics, 2024.
  - URL: https://link.springer.com/article/10.1007/s11467-023-1363-6
  - Role: broad 2D heterostructure nonlinear optics background.
- Verre et al., "Transition metal dichalcogenide nanodisks as high-index dielectric Mie nanoresonators", Nature Nanotechnology, 2019.
  - URL: https://pubmed.ncbi.nlm.nih.gov/31061517/
  - DOI: 10.1038/s41565-019-0442-x.
  - Role: TMDs as high-index Mie/anapole nanoresonators.
- Bernhardt et al., "Quasi-BIC resonant enhancement of second-harmonic generation in WS2 monolayers", Nano Letters, 2020.
  - URL: https://pubs.acs.org/doi/10.1021/acs.nanolett.0c01603
  - Role: external dielectric metasurface enhancing monolayer WS2 SHG.
- Nauman et al., "Tunable unidirectional nonlinear emission from transition-metal-dichalcogenide metasurfaces", Nature Communications, 2021.
  - URL: https://www.nature.com/articles/s41467-021-25717-x
  - Role: all-TMD metasurface nonlinear emission and mode-control background.

## Existing Local Simulation Evidence

- `outputs/comsol/qbic_spectrum_780_900nm.csv`
- `outputs/comsol/qbic_spectrum_780_900nm.png`
- `outputs/comsol/qbic_refined_800_840nm.csv`
- `outputs/comsol/qbic_refined_800_840nm.png`
- `outputs/comsol/qbic_peak_summary.txt`

Local qBIC scaffold result:

- Refined sampled peak: 830 nm.
- Coarse Q estimate: 33.2.
- R + T is approximately 1 for the simplified lossless proxy model.
- `max |E|` and `max |E|^4` proxy are available in refined CSV.

## Citation Caution

- Treat local COMSOL results as a pedagogical proxy, not quantitative reproduction.
- Exact citation metadata should be checked once more when writing the final reference list.
