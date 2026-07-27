# I-SPY2 pretreatment DCE-MRI incremental-value study

## Frozen one-file research release v1.4.0

The executable release is a single Python file:

```text
ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py
```

The user only keeps and runs this file. It contains two SHA-256-verified, readable source components and extracts them into the run audit directory:

1. **Exact v5 secondary/mechanistic pipeline**
   - `T01_C0_L2_Logistic`: clinical biology
   - `T02_C1_L2_Logistic`: clinical biology plus treatment assigned before the first NAT dose
   - `T03_C2_L2_Logistic`: C1 plus conventional MRI features
   - `M10_AX3_MULTI6_MRI_ONLY_BCE`: MRI-only six-channel Axial 3D model
   - `D01-D06`: phase and kinetic ablations
   - `D07-D09`: tumor/peritumoral spatial ablations
   - `D10`: full six-channel end-to-end sensitivity model

2. **Frozen v7.0.1 primary pipeline**
   - official primary comparison: `S10_C1_PLUS_MRI_STACK_NESTED` versus matched `S00_C1_RECALIBRATED_NESTED`
   - 5 outer folds × 3 fixed split seeds
   - 4 inner folds
   - 3 fixed MRI initialization members
   - fixed L2 meta-model `C=0.1`
   - 120 epochs; patience 20
   - inner-selection-only soft-collapse retry/keep-best rule, fully audited
   - Nadeau-Bengio corrected repeated-CV inference
   - 5000 bootstrap replicates

The v7.0.1 result is a **new prospectively frozen primary analysis**. It must not be selected against older v6.x workbooks according to whichever result looks better.

## Reconstructing the one-file release from this repository

The GitHub branch stores the exact source in ordered integrity-checked parts. Run:

```bash
python assemble_final_release.py
```

This writes `ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py` and verifies SHA-256:

```text
0d90623bbbb1419d5e658621c1a2a361babc9da7926cfb68fb99dfdd7f91525c
```

The assembled file is byte-identical to the downloadable local one-file release.

## What counts as the final result

A full run is the final **internal-validation** result only when all of the following are true:

- the command does not include `--quick` or `--allow-cohort-drift`;
- the frozen cohort preflight passes;
- all expected v5 and v7.0.1 outputs are present;
- `FINAL_RESULT_INDEX.json` reports `status: passed` and no scientific-validation errors;
- the code, seeds, endpoints, and interpretation are not changed after seeing the results;
- the locked test has not been used during development.

The official primary estimate is the v7.0.1 S10-versus-S00 comparison. v5 T01-T03, M10, and D01-D10 are secondary/mechanistic analyses. The legacy v5 stack is context only.

## Required inputs

Only the real study data are required:

```text
manifest.csv
research_cache/
```

No JSON configuration and no Model-Zoo workbook are required. Put the data beside the script or pass the two paths explicitly.

## Recommended Windows sequence

### 1. Self-test

```powershell
& "C:/Users/LENOVO/AppData/Local/Programs/Python/Python310/python.exe" `
  "E:/Downloads/ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py" `
  --self-test
```

### 2. Full data preflight

```powershell
& "C:/Users/LENOVO/AppData/Local/Programs/Python/Python310/python.exe" `
  "E:/Downloads/ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py" `
  --preflight `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

### 3. Review the frozen command plan

```powershell
& "C:/Users/LENOVO/AppData/Local/Programs/Python/Python310/python.exe" `
  "E:/Downloads/ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py" `
  --dry-run `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

### 4. Full frozen internal-validation run

```powershell
& "C:/Users/LENOVO/AppData/Local/Programs/Python/Python310/python.exe" `
  "E:/Downloads/ispy2_FINAL_RESEARCH_FROZEN_v1_4_0.py" `
  --manifest "E:/ISPY2/manifest.csv" `
  --research-cache "E:/ISPY2/research_cache"
```

The identical command may be rerun after interruption; compatible artifacts are resumed. Do not use `--force-retrain` unless a documented technical failure requires a full rebuild.

## Fixed reproducibility settings

- global seed: `20260724`
- outer split seeds: `20260724, 20260725, 20260726`
- MRI initialization offsets: `0, 1000, 2000`
- DataLoader workers: `0` by default
- cuDNN deterministic: enabled
- cuDNN benchmark: disabled
- TF32: disabled
- deterministic PyTorch algorithms: warning mode by default; `--strict-determinism` makes unsupported operations fatal
- precision is resolved once and included in the frozen run signature

Different GPU, CUDA, cuDNN, or PyTorch stacks may still prevent bitwise-identical probabilities. The release records the software/hardware environment, code hashes, input signatures, commands, and output hashes.

## Output structure

```text
ispy2_final_research_results/
├── 00_protocol/
├── 10_secondary_v5/
├── 20_primary_v7_0/
├── ISPY2_FINAL_RESEARCH_SUMMARY.xlsx
└── FINAL_RESULT_INDEX.json
```

## Important methodological boundary

The architecture was fixed after earlier model-development work. The strict nested rerun prevents leakage within the frozen analysis, but it cannot erase all earlier architecture-selection history. The result is therefore internal validation; independent confirmation requires the one-time locked test or an external cohort.

## Locked test

The test split is locked by default. Secondary v5 analyses are never allowed to unlock it through this wrapper. A one-time v7.0.1 primary test run requires explicit confirmation and a completed treatment-time audit. Do not unlock the test until the internal analysis, manuscript endpoints, code hash, and interpretation are frozen.

Research use only. This pipeline is not a clinical device and does not estimate individualized causal treatment effects.
