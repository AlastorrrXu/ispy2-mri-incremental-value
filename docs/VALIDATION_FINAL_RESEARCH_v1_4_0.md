# Validation record — frozen one-file release v1.4.0

- File: `ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py`
- Internal wrapper version: `2026-07-27-final-research-v1.4.0-frozen-v7.0.1`
- SHA-256: `0d90623bbbb1419d5e658621c1a2a361babc9da7926cfb68fb99dfdd7f91525c`
- Size: 194437 bytes
- Lines: 2729

## Scientific hierarchy

1. Primary internal validation: frozen v7.0.1 strictly nested `S10_C1_PLUS_MRI_STACK_NESTED` versus matched `S00_C1_RECALIBRATED_NESTED`.
2. Secondary/mechanistic analyses: byte-exact uploaded v5 `T01-T03`, `M10`, and `D01-D10`.
3. The legacy v5 stack is not the official primary estimate.

## Frozen primary settings

- 5 outer folds × 3 split seeds
- 4 inner folds
- split seeds: 20260724, 20260725, 20260726
- MRI initialization offsets: 0, 1000, 2000
- meta-model C: 0.1
- epochs/patience: 120/20
- collapse minimum probability SD: 0.005
- one prespecified replacement attempt
- finite low-variance fallback: `keep_best`, based only on inner-selection log loss and fully audited
- Nadeau-Bengio corrected repeated-CV inference
- 5000 bootstrap replicates
- test locked by default

## Completed validation without private study data

- Python syntax compilation: passed
- embedded component SHA-256 verification: passed
- exact v5 component extraction: passed
- frozen v7.0.1 component extraction: passed
- v5 construction/finite-logit self-test: passed
- v7.0.1 meta-model/paired-metric self-test: passed
- synthetic manifest/cache preflight: passed
- frozen dry-run command plan: passed

The private 784-patient GPU training run has not been executed in this environment. Numerical results become final only after the frozen full run completes and `FINAL_RESULT_INDEX.json` reports no missing outputs or scientific-validation errors.
