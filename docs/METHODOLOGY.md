# Methodology — frozen release v1.4.0

## 1. Scientific question

The study asks whether pretreatment DCE-MRI provides incremental predictive information for pathologic complete response (pCR) after clinical biology and the treatment regimen assigned before the first neoadjuvant-therapy dose are already known.

This is a prediction study conditional on baseline treatment assignment. It is not a causal treatment-effect or treatment-selection analysis.

## 2. Analysis hierarchy

### Primary internal-validation analysis

The official primary comparison is:

```text
S10_C1_PLUS_MRI_STACK_NESTED
minus
S00_C1_RECALIBRATED_NESTED
```

Both models are fitted within the same strict nested resampling framework. The principal estimand is improvement in Brier score / IPA, with AUROC, AUPRC, log loss, and calibration as secondary performance measures.

### Secondary and mechanistic analyses

The byte-exact v5 pipeline provides:

- `T01`: clinical biology;
- `T02`: clinical biology plus baseline-assigned treatment;
- `T03`: T02 plus conventional MRI features;
- `M10`: MRI-only six-channel Axial 3D model;
- `D01-D06`: precontrast, early, late, enhancement, and washout ablations;
- `D07-D09`: intratumoral and 0-5 mm peritumoral-region ablations;
- `D10`: full six-channel end-to-end sensitivity model.

These analyses localize possible sources of MRI increment. They do not replace the primary S10-versus-S00 estimate. Multiplicity and exploratory interpretation must be acknowledged.

## 3. Prediction time and leakage control

The intended prediction time is after treatment-arm assignment but before the first neoadjuvant dose. Permitted treatment fields must therefore be known at baseline. Variables derived from treatment completion, dose modification, toxicity, interim response, or any post-MRI event are prohibited.

The wrapper performs a structural time-zero audit and writes a variable-level audit template. A completed manual treatment-time audit is required before any one-time locked-test analysis.

## 4. Inputs

The executable requires only:

```text
manifest.csv
research_cache/
```

The manifest contains the patient-level outcome, split, clinical variables, treatment variables, conventional MRI features, and cache identifiers. The research cache contains the preprocessed MRI volumes and masks required by the specified channel modes.

No Model-Zoo workbook is required at runtime because the architecture and model ladder are frozen in the release.

## 5. Frozen primary resampling design

The v7.0.1 primary analysis uses:

- 5 outer folds;
- 3 fixed outer split seeds: `20260724`, `20260725`, `20260726`;
- 4 inner folds within every outer-training set;
- 3 fixed MRI initialization offsets: `0`, `1000`, `2000`;
- fixed L2 logistic meta-model regularization `C=0.1`;
- 120 maximum epochs and patience 20;
- 5000 bootstrap replicates;
- Nadeau-Bengio correction for repeated-cross-validation fold differences.

The outer holdout is not used to train base models, fit recalibration, fit the stack, select a replacement initialization, or choose an epoch.

## 6. Matched primary models

### S00: matched clinical baseline

Inner out-of-fold C1 probabilities are transformed to logits and used to fit a fixed L2 logistic recalibration model. The fitted recalibrator is applied to the outer-holdout C1 probability.

### S10: clinical plus MRI stack

The matched stack uses the C1 logit and the MRI-only ensemble logit. The fixed L2 logistic meta-model is trained only on inner out-of-fold predictions and then applied to the outer holdout.

This matched construction is intended to isolate the incremental contribution of MRI rather than an advantage from different calibration procedures.

## 7. MRI ensemble and numerical-collapse policy

Each MRI-only ensemble member uses the same prespecified Axial 3D architecture with a different fixed initialization. Numerical collapse is evaluated only on inner-selection predictions.

The frozen policy is:

1. train the prespecified member;
2. if the inner-selection probability distribution violates the frozen minimum-SD rule, perform one prespecified replacement attempt;
3. if all attempts are finite but low variance, retain the attempt with the best inner-selection log loss;
4. record the event, attempts, seeds, diagnostics, and selected member in the collapse audit.

No outer-holdout label or metric is used by this policy.

## 8. Metrics and inference

Reported model metrics include:

- AUROC;
- AUPRC;
- Brier score;
- IPA;
- log loss and log skill;
- calibration intercept and slope;
- probability-distribution diagnostics.

Paired fold-level differences are calculated on identical outer-holdout patients. Repeated-CV uncertainty is summarized using the Nadeau-Bengio corrected standard error and two-sided confidence interval / p-value. Patient-level bootstrap summaries are supplementary and do not replace the corrected repeated-CV inference.

## 9. Reproducibility controls

The release fixes Python, NumPy, PyTorch, and CUDA seeds; disables cuDNN benchmarking and TF32; sets deterministic cuDNN behavior; defaults to zero DataLoader workers; and includes the resolved precision in an immutable run signature.

The run records:

- wrapper and component SHA-256 hashes;
- manifest and cache signatures;
- cohort/split/target signature;
- Python, package, CUDA, cuDNN, and GPU information;
- exact subprocess commands;
- precision and worker count;
- output hashes and scientific-validation status.

Bitwise equality across different GPU and software stacks is not guaranteed. Scientific reproducibility means identical cohort and splits, identical frozen methods, compatible predictions/metrics, and the same substantive conclusion within declared numerical tolerances.

## 10. Locked test and interpretation boundary

The default full run produces the frozen internal-validation result and leaves the test split untouched. The one-time test analysis is available only for the v7.0.1 primary comparison after explicit confirmation and treatment-time governance.

The architecture was fixed after prior model-development work. Strict nested resampling prevents leakage within the frozen rerun, but it cannot erase all earlier design-selection history. The locked test or an independent external cohort is therefore required for an independent confirmatory estimate.

## 11. Final-result rule

A result set is accepted only when `FINAL_RESULT_INDEX.json` reports a passed status, no missing models/folds, and no scientific-validation errors. Runs using `--quick` or `--allow-cohort-drift` are not final research results.
