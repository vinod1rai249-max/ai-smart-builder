from typing import Dict, Any
from .claims_agent import ClaimsAgent
from .clinical_agent import ClinicalAgent

class Orchestrator:
    def __init__(self):
        self.claims_agent = ClaimsAgent()
        self.clinical_agent = ClinicalAgent()

    def route_and_execute(self, query: str) -> Dict[str, Any]:
        """
        Routes the query to the correct agent.
        """
        # Simple rule-based routing for the prototype
        # In production, this would use an LLM for intent classification
        query_lower = query.lower()
        
        if "claim" in query_lower or "paid" in query_lower or "status" in query_lower:
            return self.claims_agent.run(query, {})
        elif "clinical" in query_lower or "diagnosis" in query_lower or "patient" in query_lower:
            return self.clinical_agent.run(query, {})
        else:
            return {
                "status": "error",
                "message": "I'm not sure if this is a claims or clinical query. Could you please clarify?",
                "agent": "Orchestrator"
            }
