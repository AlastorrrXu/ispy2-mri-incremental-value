# Data, ethics, and clinical-use statement

## Data governance

This repository does not redistribute imaging or patient metadata. The pipeline downloads data from the original public sources. Users must verify and follow all applicable dataset licenses, data-use agreements, attribution requirements, and restrictions.

## Privacy

Do not commit patient-level source data, raw imaging, identifiers, manifests containing protected identifiers, model outputs containing identifiable fields, or authentication tokens. Patient identifiers in analytical exports should be replaced with study-safe IDs when required.

## Clinical interpretation

The model predicts pCR conditional on variables available in the retrospective dataset. It does not estimate individual treatment effects and does not recommend treatment. Observed treatment indicators may encode trial design, selection, site, or temporal effects.

## Research-use warning

This code is not cleared or approved as a medical device. It must not be used for patient care, triage, treatment selection, or prognosis without prospective validation, governance review, and appropriate regulatory processes.

## Bias and generalizability

Performance may differ by demographic group, receptor subtype, scanner, imaging protocol, institution, treatment era, and prevalence. Aggregate internal test performance is insufficient evidence of clinical generalizability.
