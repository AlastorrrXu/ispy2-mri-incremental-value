# I-SPY2 pretreatment DCE-MRI incremental-value study

This repository contains the frozen research pipeline for evaluating whether pretreatment breast DCE-MRI adds predictive value for pathologic complete response beyond clinical biology and the treatment regimen assigned before the first neoadjuvant-therapy dose.

## Frozen release

The final executable is distributed as one Python file:

```text
ispy2_FINAL_RESEARCH_FROZEN_v1_0.py
```

Release identifier:

```text
2026-07-27-final-research-release-v1.0.0-v7.0.1
```

The one-file release embeds and SHA-256-verifies two readable source components at runtime.

### Exact v5 secondary/mechanistic analysis

- `T01_C0_L2_Logistic`: clinical biology
- `T02_C1_L2_Logistic`: clinical biology plus treatment assigned before the first NAT dose
- `T03_C2_L2_Logistic`: C1 plus conventional MRI morphology/kinetics
- `M10_AX3_MULTI6_MRI_ONLY_BCE`: MRI-only six-channel Axial 3D model
- `D01-D06`: temporal and kinetic ablations
- `D07-D09`: tumor and 0–5 mm peritumoral spatial ablations
- `D10_AX3_MULTI6_CAT_BCE`: full six-channel end-to-end sensitivity model

### New frozen v7.0.1 strict nested primary analysis

The official primary comparison is:

```text
S10_C1_PLUS_MRI_STACK_NESTED
versus
S00_C1_RECALIBRATED_NESTED
```

Frozen settings:

- 5 outer folds × 3 split seeds
- 4 inner folds
- split seeds `20260724, 20260725, 20260726`
- MRI initialization offsets `0, 1000, 2000`
- L2 meta-model `C=0.1`
- 120 epochs, patience 20
- audited soft-collapse `keep_best` rule
- Nadeau–Bengio corrected repeated-CV inference
- locked test by default

The v7.0.1 analysis is a **new prospective frozen analysis version**. Results must be reported as one frozen result set; they must not be selected against an older v6.x workbook according to whichever metric is higher.

## Scientific hierarchy

1. **Primary internal validation:** v7.0.1 strict nested S10 versus matched S00.
2. **Secondary/mechanistic analyses:** v5 T01–T03, M10, and D01–D10.
3. **Context only:** the legacy v5 stack is not the official primary estimate.

## Required inputs

Only the actual study data are required:

```text
manifest.csv
research_cache/
```

A JSON configuration and Model-Zoo workbook are not required. Put the two data inputs beside the script, or pass only their locations.

```powershell
python ispy2_FINAL_RESEARCH_FROZEN_v1_0.py `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

Data are not redistributed in this repository.

## Recommended execution sequence

### 1. Code self-test

```powershell
python ispy2_FINAL_RESEARCH_FROZEN_v1_0.py --self-test
```

### 2. Full data preflight

```powershell
python ispy2_FINAL_RESEARCH_FROZEN_v1_0.py `
  --preflight `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

The preflight checks the frozen cohort, labels, treatment fields, patient/cache coverage, MRI keys, masks, array shapes, physical spacing, and conventional-MRI JSON.

### 3. Inspect the frozen command plan

```powershell
python ispy2_FINAL_RESEARCH_FROZEN_v1_0.py `
  --dry-run `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

### 4. Full frozen run

```powershell
python ispy2_FINAL_RESEARCH_FROZEN_v1_0.py `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

Do not use `--quick` as a scientific result. Do not change seeds, select a more favorable retry, or tune the model after reviewing the result.

## Reproducibility controls

- global seed `20260724`
- fixed repeated split seeds and initialization offsets
- DataLoader workers default to `0`
- cuDNN deterministic enabled
- cuDNN benchmark disabled
- TF32 disabled
- deterministic PyTorch algorithms enabled in warning mode by default
- optional `--strict-determinism` hard-failure mode
- resolved numerical precision is passed explicitly to both pipelines and signature-locked
- code, manifest, cache inventory, split/target signature, environment, GPU, commands, and outputs are audited

Different GPU, CUDA, cuDNN, or PyTorch stacks may not be bitwise identical. The repository targets scientific reproducibility of the frozen cohort, splits, methods, predictions, metrics, and conclusions rather than unsupported cross-hardware bit identity.

## Locked test governance

The test split is never accessed by default. v5 secondary analyses are never allowed to unlock the test through the final wrapper. A one-time v7.0.1 primary test analysis additionally requires:

- a completed treatment-time audit CSV
- `--strict-treatment-audit`
- `--baseline-treatment-confirmation BASELINE_TREATMENT_VERIFIED`
- `--test-confirmation FINAL_ANALYSIS_FROZEN`

The test must remain locked until the internal analysis, endpoints, code, and interpretation are frozen.

## Main outputs

```text
ispy2_final_research_results/
├── 00_protocol/
├── 10_secondary_v5/
├── 20_primary_v7_0/
├── ISPY2_FINAL_RESEARCH_SUMMARY.xlsx
└── FINAL_RESULT_INDEX.json
```

## Validation status

Completed without private data:

- syntax compilation
- embedded source integrity verification
- v5 model-construction and finite-logit self-test
- v7.0.1 meta-model and paired-metric self-test
- synthetic manifest/cache preflight
- frozen command-plan generation
- ambiguous-data-pair safety stop

The full private 784-patient GPU run has not been executed in the publication environment represented by this repository. Final numerical results are established only after the frozen full run completes and its generated scientific audit passes.

## Research-use boundary

This is retrospective prediction research, not a clinical device. Treatment variables condition prediction on assigned/known treatment and do not estimate causal treatment effects or individualized treatment recommendations. External validation is required before clinical use.

## Author

Conceptualization, methodology, and implementation: **Duorui Xu**.

## License

Repository-authored code and documentation are released under the MIT License. Dataset terms remain governed by the original data providers.
