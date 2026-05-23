import os
from typing import Optional
from google.cloud import dlp_v2

class DLPService:
    def __init__(self, project_id: Optional[str] = None):
        self.project_id = project_id or os.getenv("GOOGLE_CLOUD_PROJECT")
        self.client = dlp_v2.DlpServiceClient()

    def redact_phi(self, text: str) -> str:
        """
        Redacts PHI from the given text using GCP Sensitive Data Protection.
        """
        if not text:
            return text

        # Define the parent resource
        parent = f"projects/{self.project_id}"

        # Define the item to inspect
        item = {"value": text}

        # Define the de-identification config
        # Here we use a simple replacement with the info type name
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "replace_with_info_type_config": {}
                        }
                    }
                ]
            }
        }

        # Define the inspection config (common PHI types)
        inspect_config = {
            "info_types": [
                {"name": "PERSON_NAME"},
                {"name": "PHONE_NUMBER"},
                {"name": "EMAIL_ADDRESS"},
                {"name": "US_SOCIAL_SECURITY_NUMBER"},
                {"name": "STREET_ADDRESS"},
                {"name": "DATE_OF_BIRTH"}
            ]
        }

        try:
            # Call the DLP API
            response = self.client.deidentify_content(
                request={
                    "parent": parent,
                    "deidentify_config": deidentify_config,
                    "inspect_config": inspect_config,
                    "item": item,
                }
            )
            return response.item.value
        except Exception as e:
            print(f"DLP Redaction failed: {e}")
            # In a real clinical assistant, we might block the request if redaction fails
            return "[REDACTION_FAILED] " + text
