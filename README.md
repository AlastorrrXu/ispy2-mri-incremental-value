# I-SPY2 Pretreatment DCE-MRI Incremental-Value Transformer

A research repository for evaluating whether pretreatment dynamic contrast-enhanced breast MRI adds predictive value beyond clinical biology and the known treatment regimen when predicting pathologic complete response in I-SPY2.

## Research question

The primary question is not merely whether MRI predicts pCR. It is whether MRI contributes measurable held-out predictive value beyond a clinically informed baseline containing patient biology and treatment variables.

The planned comparison contains three models:

1. Clinical and treatment tabular model
2. Pretreatment DCE-MRI image model
3. Multimodal fusion model

The prespecified primary comparison is fusion versus the tabular baseline on the same held-out test patients.

## Method summary

The imaging branch uses a 3D ConvNeXt encoder for three DCE phases. Global, tumor, and peritumoral tokens are integrated by a Transformer. The tabular branch tokenizes clinical and treatment variables with learned missing-value embeddings. Bidirectional gated cross-attention performs multimodal fusion.

Predictions are calibrated using validation-only temperature scaling. Incremental value is quantified with paired stratified bootstrap confidence intervals for changes in AUROC, AUPRC, Brier score, and log loss. The analysis plan also includes subgroup evaluation and decision-curve analysis.

See [docs/METHODOLOGY.md](docs/METHODOLOGY.md) for the full specification.

## Repository status

This public repository currently contains the study design, contribution statement, data and ethics guidance, citation metadata, dependency list, and a blank results template. Numerical results are intentionally omitted until completion of the locked experiment.

The complete executable pipeline is retained locally while the manifest construction, data split, privacy safeguards, and release readiness are checked. See [src/README.md](src/README.md).

## Project structure

```text
.
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── src/
│   └── README.md
├── docs/
│   ├── METHODOLOGY.md
│   ├── CONTRIBUTIONS.md
│   └── DATA_AND_ETHICS.md
└── results/
    └── RESULTS_TEMPLATE.md
```

## Planned outputs

```text
model_performance.csv
incremental_value_bootstrap.csv
test_predictions_all_models.csv
subgroup_performance.csv
decision_curve.csv
incremental_value_summary.json
```

## Reproducibility principles

The planned experiment uses a locked patient-level train, validation, and test manifest, validation-only model selection and calibration, paired comparison on identical test patients, and machine-readable exports. The test set is reserved for final reporting.

## Important limitations

This is retrospective research, not a clinical device. Treatment variables condition prediction under observed or assigned regimens and must not be interpreted as causal treatment recommendations. External validation is required before clinical interpretation.

## Data availability

Data are not redistributed in this repository. Users must obtain the official BreastDCEDL and I-SPY2-derived resources from their original hosts and comply with the applicable terms and citation requirements.

## Authors and credit

Initial conceptualization, methodology, and implementation: **Duorui Xu**.

Clinical collaborators, imaging specialists, statistical reviewers, and supervisors should be added according to substantive contribution before submission. See [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md).

## License

Repository-authored code and documentation are released under the MIT License. Dataset terms remain governed by the original providers.
