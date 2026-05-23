import os
import json
from google.cloud import storage
from google.cloud import bigquery
from google.cloud import dlp_v2
from datetime import datetime

class ClaimIngestionPipeline:
    def __init__(self, project_id: str, kms_key_id: str):
        self.project_id = project_id
        self.kms_key_id = kms_key_id
        self.storage_client = storage.Client(project=project_id)
        self.bq_client = bigquery.Client(project=project_id)
        self.dlp_client = dlp_v2.DlpServiceClient()

    def process_claim(self, bucket_name: str, blob_name: str):
        """
        Ingests a claim from GCS, redacts PHI, and saves to BigQuery.
        """
        print(f"Processing claim: gs://{bucket_name}/{blob_name}")
        
        # 1. Download from GCS
        bucket = self.storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        content = blob.download_as_text()
        claim_data = json.loads(content)

        # 2. Redact PHI (Patient Name)
        patient_name = claim_data.get("patient_name", "")
        masked_name = self._redact_text(patient_name)

        # 3. Prepare for BigQuery
        row_to_insert = [
            {
                "claim_id": claim_data["claim_id"],
                "patient_id_masked": masked_name,
                "status": claim_data["status"],
                "amount": claim_data["total_amount"],
                "ingested_at": datetime.utcnow().isoformat(),
                "raw_source_gs": f"gs://{bucket_name}/{blob_name}"
            }
        ]

        # 4. Insert into Silver Layer
        table_id = f"{self.project_id}.data_silver.claims"
        errors = self.bq_client.insert_rows_json(table_id, row_to_insert)
        
        if not errors:
            print("New rows have been added.")
        else:
            print(f"Encountered errors while inserting rows: {errors}")

    def _redact_text(self, text: str) -> str:
        parent = f"projects/{self.project_id}/locations/global"
        item = {"value": text}
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {"primitive_transformation": {"replace_with_info_type_config": {}}}
                ]
            }
        }
        inspect_config = {"info_types": [{"name": "PERSON_NAME"}]}
        
        response = self.dlp_client.deidentify_content(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
        return response.item.value

if __name__ == "__main__":
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "ehcca-dev-project")
    KMS_KEY_ID = os.getenv("KMS_KEY_ID")
    pipeline = ClaimIngestionPipeline(PROJECT_ID, KMS_KEY_ID)
    # Example usage:
    # pipeline.process_claim("claims-raw-landing-ehcca", "sample_claim.json")
