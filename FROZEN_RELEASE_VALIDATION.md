# Frozen one-file release validation

Release file: `ispy2_FINAL_RESEARCH_FROZEN_v1_0.py`

Wrapper version: `2026-07-27-final-research-v1.4.0-frozen-v7.0.1`

SHA-256:

```text
755372b6e809edf73e6016c889c84993f3ba1838afbefeddddb0811030e63b0b
```

## Scientific hierarchy

1. Primary internal validation: frozen v7.0.1 strictly nested `S10_C1_PLUS_MRI_STACK_NESTED` versus matched `S00_C1_RECALIBRATED_NESTED`.
2. Secondary/mechanistic analyses: exact uploaded v5 `T01-T03`, `M10`, and `D01-D10`.
3. The legacy v5 stack is context only and must not replace the v7.0.1 primary estimate.

## Frozen primary settings

- 5 outer folds × 3 split seeds
- 4 inner folds
- split seeds: `20260724, 20260725, 20260726`
- MRI initialization offsets: `0, 1000, 2000`
- L2 meta-model `C=0.1`
- 120 epochs, patience 20
- soft-collapse threshold `SD < 0.005`
- one prespecified replacement attempt
- finite low-variance fallback: `keep_best`, selected only from inner-selection log loss and fully audited
- Nadeau–Bengio corrected repeated-CV inference
- 5000 bootstrap replicates
- test locked by default

## Completed checks

- Python syntax compilation: passed
- embedded source SHA-256 verification: passed
- exact v5 source extraction: passed
- frozen v7.0.1 source extraction: passed
- v5 model-construction/finite-logit self-test: passed
- v7.0.1 meta-model/paired-metric self-test: passed
- synthetic manifest/cache preflight: passed
- frozen dry-run command-plan generation: passed

The private 784-patient GPU run has not been executed in this publication environment. Numerical research results become final only after the frozen full run completes and `FINAL_RESULT_INDEX.json` reports no missing outputs or scientific-validation errors.
