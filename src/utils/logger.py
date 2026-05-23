import json
import time
from datetime import datetime
from typing import Dict, Any

class GovernanceLogger:
    def __init__(self, log_path: str = "interaction_logs.json"):
        self.log_path = log_path

    def log_interaction(self, payload: Dict[str, Any]):
        """
        Logs interaction metadata to a local JSON file (simulating BigQuery sink).
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "data": payload
        }
        
        # In production, this would use:
        # from google.cloud import bigquery
        # client.insert_rows_json(table_id, [log_entry])
        
        print(f"[GovernanceLogger] Logging interaction: {payload.get('prompt_id', 'unknown')}")
        
        try:
            with open(self.log_path, "a") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception as e:
            print(f"Logging failed: {e}")

# Global instance
logger = GovernanceLogger()
