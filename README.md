# I-SPY2 Pretreatment DCE-MRI Incremental-Value Transformer

A research pipeline for testing whether pretreatment dynamic contrast-enhanced breast MRI adds predictive value beyond clinical biology and known treatment regimen when predicting pathologic complete response (pCR) in I-SPY2.

## Research question

The primary question is not merely whether MRI can predict pCR. It is whether MRI contributes measurable out-of-sample value beyond a clinically informed baseline containing patient biology and treatment variables.

The repository therefore compares three independently evaluated models:

1. Clinical and treatment tabular model
2. Pretreatment DCE-MRI image model
3. Multimodal fusion model

The prespecified primary comparison is fusion versus the tabular baseline on the held-out test set.

## Method summary

The imaging branch uses a 3D ConvNeXt encoder to process three DCE phases. Global, tumor, and peritumoral region tokens are extracted from each phase and integrated by a Transformer. The tabular branch tokenizes clinical and treatment variables with learned missing-value embeddings. Bidirectional gated cross-attention performs multimodal fusion.

Predictions are temperature-calibrated using validation data. Incremental value is quantified using paired stratified bootstrap confidence intervals for changes in AUROC, AUPRC, Brier score, and log loss. The pipeline also exports subgroup analyses and decision-curve data.

See [docs/METHODOLOGY.md](docs/METHODOLOGY.md) for the full methodological specification.

## Repository status

The implementation and analysis plan are provided. Numerical results are intentionally left blank until the locked experiment is completed.

## Project structure

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── src/
│   └── ispy2_incremental_transformer.py
├── docs/
│   ├── METHODOLOGY.md
│   ├── CONTRIBUTIONS.md
│   └── DATA_AND_ETHICS.md
└── results/
    └── RESULTS_TEMPLATE.md
```

## Installation

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS or Linux
source .venv/bin/activate

python -m pip install -r requirements.txt
```

Install the CUDA-compatible PyTorch build using the official PyTorch installation selector when GPU training is required.

## Running the pipeline

Edit the `RunConfig` block in the script if necessary, then run:

```bash
python src/ispy2_incremental_transformer.py
```

The script downloads the official BreastDCEDL I-SPY2 MinCrop data when needed, constructs a locked patient-level split, trains the three models, calibrates predictions, and exports patient-level and aggregate analyses.

## Expected outputs

The main outputs are:

```text
ispy2_results/analysis/model_performance.csv
ispy2_results/analysis/incremental_value_bootstrap.csv
ispy2_results/analysis/test_predictions_all_models.csv
ispy2_results/analysis/subgroup_performance.csv
ispy2_results/analysis/decision_curve.csv
ispy2_results/analysis/incremental_value_summary.json
```

## Reproducibility principles

The experiment uses a fixed random seed, a locked train/validation/test manifest, patient-level evaluation, validation-only calibration, paired testing on identical test patients, and machine-readable exports. Model selection is based on validation AUPRC. The test set is reserved for final reporting.

## Important limitations

This is retrospective research code, not a clinical device. Treatment variables condition prediction under observed or assigned regimens and must not be interpreted as causal treatment recommendations. External validation is required before clinical interpretation. Because model capacity may be large relative to the cohort, overfitting and calibration instability must be assessed explicitly.

## Data availability

The code references the official BreastDCEDL and I-SPY2-derived public resources. Data are downloaded from their original hosts and are not redistributed in this repository. Users are responsible for complying with the source dataset terms and citation requirements.

## Authors and credit

Initial methodology and implementation: **Duorui Xu**.

Clinical collaborators, imaging specialists, statistical reviewers, and additional contributors should be added according to substantive contribution before submission. See [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md).

## License

Code is released under the MIT License. Dataset licenses and terms remain governed by the original data providers.
