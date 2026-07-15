# Results

Numerical results are intentionally left blank until completion of the locked experiment.

## Cohort

| Split | Patients | pCR cases | pCR prevalence |
|---|---:|---:|---:|
| Train |  |  |  |
| Validation |  |  |  |
| Test |  |  |  |

## Test performance

| Model | AUROC | AUPRC | Brier | Log loss | Calibration slope |
|---|---:|---:|---:|---:|---:|
| Clinical and treatment |  |  |  |  |  |
| DCE-MRI |  |  |  |  |  |
| Fusion |  |  |  |  |  |

## Primary incremental-value comparison

| Comparison | Metric | Estimate | 95% CI |
|---|---|---:|---:|
| Fusion minus tabular | Delta AUROC |  |  |
| Fusion minus tabular | Delta AUPRC |  |  |
| Fusion minus tabular | Delta Brier |  |  |
| Fusion minus tabular | Delta log loss |  |  |

## Subgroup results

| Subgroup | N | Model | AUROC | AUPRC | Brier |
|---|---:|---|---:|---:|---:|
| HR-positive and HER2-negative |  | Fusion |  |  |  |
| HER2-positive |  | Fusion |  |  |  |
| Triple-negative |  | Fusion |  |  |  |

## Ablations

| Experiment | AUROC | AUPRC | Interpretation |
|---|---:|---:|---|
| Fusion without treatment variables |  |  |  |
| Fusion without region tokens |  |  |  |
| Fusion without cross-attention |  |  |  |
| Fusion without auxiliary losses |  |  |  |
| Logistic regression baseline |  |  |  |
| Gradient boosting baseline |  |  |  |

## Decision-curve analysis

Add the net-benefit figure and describe the threshold ranges over which fusion provides clinically meaningful improvement over the tabular baseline and treat-all or treat-none strategies.

## Failure analysis

Summarize false positives, false negatives, missing phases, low-quality segmentations, extreme calibration errors, and subgroup-specific failure patterns.
