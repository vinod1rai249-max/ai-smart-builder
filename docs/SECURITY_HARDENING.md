# Security Hardening

This document details the advanced security measures for protecting PHI within the EHCCA ecosystem.

## 1. VPC Service Controls (VPC-SC)
The VPC-SC Service Perimeter is the primary defense against data exfiltration.

### Configuration
- **Perimeter Name:** `ehcca-phi-perimeter`
- **Implementation Status:** Sprint 006 Enforced.
- **Protected Resources:** Data and AI Projects.
- **See also:** `docs/VPC_SC_GUIDE.md` for detailed ingress/egress policies.

## 2. Fine-Grained IAM Policies
We follow the principle of least privilege for service accounts.

| Service Account | Roles | Scope |
|---|---|---|
| `ehcca-gateway@...` | `roles/dlp.user`, `roles/aiplatform.user` | Global |
| `ehcca-claims-agent@...` | `roles/bigquery.dataViewer` | `data_silver` dataset only |
| `ehcca-clinical-agent@...` | `roles/bigquery.dataViewer` | `data_gold` dataset only |
| **Reviewers** | `roles/browser`, `ehcca.hitlReviewer` | HITL Dashboard only |

## 3. Secret Management
All sensitive configuration (API keys, Service Account keys) is managed via **Google Cloud Secret Manager**.
- **Access:** Restricted to the Gateway Service Account via `roles/secretmanager.secretAccessor`.
