import os
from google.cloud import bigquery
from google.cloud import kms

def create_bq_tables(project_id, kms_key_id):
    client = bigquery.Client(project=project_id)
    
    # 1. Silver Layer - Claims
    silver_dataset = f"{project_id}.data_silver"
    claims_table_id = f"{silver_dataset}.claims"
    
    schema = [
        bigquery.SchemaField("claim_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("patient_id_masked", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("status", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("amount", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("ingested_at", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("raw_source_gs", "STRING", mode="NULLABLE"),
    ]
    
    table = bigquery.Table(claims_table_id, schema=schema)
    table.encryption_configuration = bigquery.EncryptionConfiguration(kms_key_name=kms_key_id)
    
    try:
        client.create_table(table)
        print(f"Created table {claims_table_id}")
    except Exception as e:
        print(f"Table {claims_table_id} already exists or error: {e}")

    # 2. Governance Logs
    governance_table_id = f"{project_id}.ehcca_monitoring.interaction_logs"
    gov_schema = [
        bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("prompt_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("agent", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("grounding_score", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("latency_ms", "RECORD", fields=[
            bigquery.SchemaField("dlp_ms", "INTEGER"),
            bigquery.SchemaField("agent_ms", "INTEGER"),
            bigquery.SchemaField("model_ms", "INTEGER"),
            bigquery.SchemaField("total_ms", "INTEGER"),
        ]),
        bigquery.SchemaField("status", "STRING", mode="NULLABLE"),
    ]
    
    gov_table = bigquery.Table(governance_table_id, schema=gov_schema)
    gov_table.encryption_configuration = bigquery.EncryptionConfiguration(kms_key_name=kms_key_id)
    
    try:
        client.create_table(gov_table)
        print(f"Created table {governance_table_id}")
    except Exception as e:
        print(f"Table {governance_table_id} already exists or error: {e}")

    # 3. HITL Queue
    hitl_table_id = f"{project_id}.ehcca_ops.hitl_queue"
    hitl_schema = [
        bigquery.SchemaField("interaction_id", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("status", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("hitl_reason", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("created_at", "TIMESTAMP", mode="REQUIRED"),
    ]
    
    hitl_table = bigquery.Table(hitl_table_id, schema=hitl_schema)
    hitl_table.encryption_configuration = bigquery.EncryptionConfiguration(kms_key_name=kms_key_id)
    
    try:
        client.create_table(hitl_table)
        print(f"Created table {hitl_table_id}")
    except Exception as e:
        print(f"Table {hitl_table_id} already exists or error: {e}")

if __name__ == "__main__":
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "ehcca-dev-project")
    KMS_KEY_ID = os.getenv("KMS_KEY_ID") # Should be the full resource ID
    if not KMS_KEY_ID:
        print("Error: KMS_KEY_ID environment variable not set.")
    else:
        create_bq_tables(PROJECT_ID, KMS_KEY_ID)
