from typing import Dict, Any
from .base_agent import BaseAgent
from ..utils.errors import create_error_response, AgentErrorCode

class ClaimsAgent(BaseAgent):
    def __init__(self):
        super().__init__("ClaimsAgent")

    def run(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes claims analysis (updated with error handling).
        """
        try:
            print(f"[{self.name}] Querying Silver Layer for: {query}")
            
            # Simulate a policy violation for specific terms
            if "internal audit" in query.lower():
                return create_error_response(
                    AgentErrorCode.POLICY_VIOLATION,
                    "Access to internal audit records is restricted to Governance Officers.",
                    self.name
                )

            # Mock successful response
            return {
                "status": "success",
                "agent": self.name,
                "data": {
                    "claim_id": "CLM-12345",
                    "status": "PAID",
                    "amount": 1250.00,
                    "paid_date": "2026-05-20"
                }
            }
        except Exception as e:
            return create_error_response(
                AgentErrorCode.UNKNOWN_ERROR,
                f"An unexpected error occurred in ClaimsAgent: {str(e)}",
                self.name
            )
