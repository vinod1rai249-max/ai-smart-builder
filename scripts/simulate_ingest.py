import os
import json
import argparse
from google.cloud import storage

def simulate_ingest(project_id: str, bucket_name: str, file_path: str):
    """
    Simulates ingesting a claim file into the landing zone.
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    # Verify JSON schema (Simple check)
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if 'claim_id' not in data:
                print("Error: Missing 'claim_id' in claim file.")
                return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return

    # Upload to GCS
    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(os.path.basename(file_path))

    print(f"Uploading {file_path} to gs://{bucket_name}/...")
    blob.upload_from_filename(file_path)
    print("Ingestion successful.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="EHCCA Data Ingestion Simulator")
    parser.add_argument("--project", required=True, help="GCP Project ID")
    parser.add_argument("--bucket", required=True, help="Landing Bucket Name")
    parser.add_argument("--file", required=True, help="Path to JSON claim file")
    
    args = parser.parse_args()
    simulate_ingest(args.project, args.bucket, args.file)
