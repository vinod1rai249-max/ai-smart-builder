import requests
import json
import csv
from datetime import datetime

GATEWAY_URL = "http://127.0.0.1:8110/generate"

def run_evaluation(dataset_path: str):
    print(f"Starting Batch Evaluation using {dataset_path}...")
    
    with open(dataset_path, "r") as f:
        cases = json.load(f)

    results = []
    
    for case in cases:
        print(f"Testing Case {case['id']}: {case['prompt']}")
        
        try:
            # Note: This assumes the gateway is running locally
            # In a CI environment, we would use a test client
            response = requests.post(GATEWAY_URL, json={"prompt": case["prompt"]})
            data = response.json()
            
            evaluation = data.get("evaluation") or {}
            latency_ms = data.get("latency_ms") or {}
            
            eval_row = {
                "id": case["id"],
                "status": data.get("status"),
                "grounding": evaluation.get("grounding", 0),
                "latency_total": latency_ms.get("total_ms", 0),
                "passed": data.get("status") == case.get("expected_status", "success")
            }
            results.append(eval_row)
            
        except Exception as e:
            print(f"Error evaluating case {case['id']}: {e}")

    # Export to CSV
    report_file = f"evaluation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    if results:
        keys = results[0].keys()
        with open(report_file, "w", newline="") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(results)
    
    print(f"Evaluation complete. Report saved to {report_file}")

if __name__ == "__main__":
    # In a real environment, this script would be triggered by a CI/CD pipeline
    run_evaluation("F:\\matured_ai_practice\\120x-Operators-Kit\\120x-Operators-Kit\\builds\\ai-smart-builder\\samples\\golden_dataset.json")
