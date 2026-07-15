# Methodology

## 1. Objective

The study evaluates the incremental predictive value of pretreatment DCE-MRI for pathologic complete response after accounting for clinical biology and the known treatment regimen.

Primary estimand:

> Difference in held-out predictive performance between the multimodal fusion model and the clinical-treatment tabular model on the same patients.

This framing distinguishes incremental clinical information from standalone image classification performance.

## 2. Cohort and unit of analysis

The unit of analysis is the patient. A single locked manifest assigns each patient to train, validation, or test. No patient may occur in more than one split. The binary outcome is pCR.

The code builds the manifest from the official BreastDCEDL I-SPY2 MinCrop metadata and treatment metadata. It resolves pretreatment, early post-contrast, late post-contrast, and tumor-mask NIfTI files.

## 3. Inputs

### Imaging inputs

Three DCE-MRI phases are used:

* Pretreatment or precontrast phase
* Early post-contrast phase
* Late post-contrast phase

A tumor segmentation mask is used to define tumor and peritumoral regions.

### Clinical inputs

* Standardized age
* Hormone receptor status
* HER2 status
* HR and HER2 interaction
* MammaPrint value
* MammaPrint missingness indicator
* Premenopausal indicator
* Postmenopausal indicator

### Treatment inputs

Binary or numeric indicators encode the recorded treatment regimen, including paclitaxel, trastuzumab, pertuzumab, carboplatin, pembrolizumab, neratinib, T-DM1, MK-2206, AMG 386, ABT 888, ganetespib, and ganitumab when present in source metadata.

## 4. Preprocessing

NIfTI images are converted from NiBabel spatial order to PyTorch depth-height-width order. Missing image phases are represented by zero volumes and an explicit phase-availability mask. Image intensity normalization uses robust reference statistics from an available phase, based on median and percentile-derived scale, followed by clipping.

Volumes and masks are resized to a fixed 3D shape. Training augmentation applies spatial flips and phase-consistent intensity transformations to preserve contrast kinetics.

Age standardization is estimated from the training cohort only. Missing tabular values receive learned missing-value embeddings.

## 5. Models

### Tabular baseline

Each clinical and treatment feature is converted into a learned numerical token. Clinical and treatment type embeddings distinguish the two feature groups. A Transformer encoder produces a tabular summary representation followed by an MLP prediction head.

### Image-only model

Each DCE phase is processed sequentially by a 3D ConvNeXt backbone. At the final feature map, three regional representations are extracted:

* Global breast or crop representation
* Tumor representation
* Peritumoral representation

Phase and region embeddings are added. A Transformer integrates the resulting phase-region token sequence and produces the image summary representation.

### Fusion model

The image and tabular encoders are initialized from independently trained unimodal models. Bidirectional gated cross-attention lets image tokens attend to tabular context and tabular tokens attend to image context. The final classifier receives image embedding, tabular embedding, elementwise product, and absolute difference.

Auxiliary image and tabular losses are retained during fusion training to discourage collapse of either modality.

## 6. Optimization

Models are trained with AdamW, cosine learning-rate decay, warmup, gradient accumulation, gradient clipping, automatic mixed precision when available, exponential moving average weights, and early stopping.

Model selection is based only on validation AUPRC. Test performance is evaluated after model selection.

## 7. Calibration

A scalar temperature is fitted using validation logits and labels. Raw and calibrated test metrics are both exported. No test labels are used to fit calibration parameters.

## 8. Primary analysis

The primary comparison is:

```text
multimodal fusion minus clinical-treatment tabular baseline
```

Metrics include:

* AUROC
* AUPRC
* Brier score
* Log loss
* Accuracy at threshold 0.5
* Sensitivity and specificity at threshold 0.5
* Calibration intercept and slope
* Expected calibration error

Paired stratified bootstrap resampling preserves class representation and compares models on identical resampled patients. The analysis reports point estimates and percentile 95% confidence intervals.

Positive differences indicate improvement for AUROC and AUPRC. Negative differences indicate improvement for Brier score and log loss.

## 9. Secondary analyses

* Fusion versus image-only model
* HR-positive and HER2-negative subgroup
* HER2-positive subgroup
* Triple-negative subgroup
* Decision-curve net benefit over clinically relevant thresholds

Subgroup analyses are exploratory unless sufficient sample size and multiplicity control are prespecified.

## 10. Required additions before a manuscript claim

1. Report exact cohort counts and event rates for every split.
2. Confirm source split provenance and absence of leakage.
3. Add repeated seeds or nested resampling for model-development uncertainty.
4. Compare against simpler baselines such as penalized logistic regression and gradient boosting.
5. Report confidence intervals for every principal metric.
6. Inspect calibration curves and failure cases.
7. Add external or temporally distinct validation when possible.
8. Conduct ablation studies for region tokens, treatment variables, fusion, calibration, and auxiliary losses.
9. Publish a model card and exact software environment.
10. Obtain clinical coauthor review before making clinical-value claims.
