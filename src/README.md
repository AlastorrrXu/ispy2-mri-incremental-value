# Source code status

The complete experimental pipeline is being retained locally while the data manifest, split construction, and analysis plan are validated.

Before a public code release, the following items should be confirmed:

1. Official dataset paths and checksums
2. Patient-level split provenance
3. Absence of train, validation, and test leakage
4. Treatment-variable interpretation
5. Reproducibility across multiple random seeds
6. Removal of patient-level outputs and local paths

The planned implementation includes official-data download, manifest construction, 3D DCE-MRI preprocessing, clinical-treatment and image-only baselines, cross-attention fusion, validation-only temperature calibration, paired bootstrap analysis, subgroup evaluation, and decision-curve export.

The executable source can be added here after validation without changing the documented study design or blank results template.
