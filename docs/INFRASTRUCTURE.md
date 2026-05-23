# Infrastructure Setup

This document details the GCP resources required for the EHCCA Foundation Layer.

## 1. Cloud KMS (Encryption)
Create a keyring and key in `us-central1` for Customer-Managed Encryption Keys (CMEK).

```bash
gcloud kms keyrings create ehcca-keyring --location us-central1
gcloud kms keys create ehcca-phi-key --location us-central1 --keyring ehcca-keyring --purpose encryption
```

## 2. BigQuery (Data Layer)
Create datasets with the CMEK key.

```bash
# Get the KMS key resource ID first
KMS_KEY_ID="projects/[PROJECT_ID]/locations/us-central1/keyrings/ehcca-keyring/cryptoKeys/ehcca-phi-key"

bq mk --location=us-central1 --dataset --default_kms_key=$KMS_KEY_ID data_raw
bq mk --location=us-central1 --dataset --default_kms_key=$KMS_KEY_ID data_silver
bq mk --location=us-central1 --dataset --default_kms_key=$KMS_KEY_ID data_gold
```

## 3. Cloud Storage (Landing Zone)
Create buckets with CMEK and Uniform Bucket-Level Access.

```bash
gsutil mb -l us-central1 -b on gs://claims-raw-landing-[PROJECT_ID]
gsutil kms encryption -k $KMS_KEY_ID gs://claims-raw-landing-[PROJECT_ID]

gsutil mb -l us-central1 -b on gs://clinical-docs-gold-[PROJECT_ID]
gsutil kms encryption -k $KMS_KEY_ID gs://clinical-docs-gold-[PROJECT_ID]
```

## 4. Service Account Permissions
The Gateway service account needs the following:
- `roles/dlp.user`
- `roles/aiplatform.user`
- `roles/logging.logWriter`
