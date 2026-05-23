# VPC Service Controls (VPC-SC) Implementation Guide

## Overview
This document details the configuration for the `ehcca-phi-perimeter` to protect PHI within the Google Cloud ecosystem.

## 1. Access Level Configuration
Define an access level based on authorized IP ranges (e.g., Corporate Office/VPN).

```yaml
# access_level.yaml
- ipSubnetworks:
  - 123.45.67.89/32
```

## 2. Service Perimeter Definition
The perimeter encompasses the projects handling PHI and restricts core APIs.

### Protected Projects
- `ehcca-data-project-123`
- `ehcca-ai-project-456`

### Restricted Services
- `bigquery.googleapis.com`
- `storage.googleapis.com`
- `aiplatform.googleapis.com`
- `dlp.googleapis.com`

## 3. Ingress and Egress Policies
To allow the AI Gateway (in the AI project) to query the Data project, explicit ingress rules are required.

### Ingress Rule: AI Gateway to BigQuery
- **From:** Service Account `ehcca-gateway@ehcca-ai-project-456.iam.gserviceaccount.com`
- **To:** BigQuery Service in `ehcca-data-project-123`
- **Method:** `google.bigquery.v2.JobService.InsertJob`

## 4. Troubleshooting
Check Cloud Logging using the following filter to identify "Dry Run" violations:

```sql
resource.type="audited_resource"
protoPayload.serviceName="accesscontextmanager.googleapis.com"
protoPayload.metadata.violationType="SERVICE_PERIMETER_VIOLATION"
```
