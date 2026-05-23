from enum import Enum
from typing import Dict, Any, Optional

class AgentErrorCode(Enum):
    DATA_SOURCE_UNAVAILABLE = "DATA_SOURCE_UNAVAILABLE"
    LOW_GROUNDING_CONFIDENCE = "LOW_GROUNDING_CONFIDENCE"
    POLICY_VIOLATION = "POLICY_VIOLATION"
    AMBIGUOUS_QUERY = "AMBIGUOUS_QUERY"
    MODEL_TIMEOUT = "MODEL_TIMEOUT"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"

def create_error_response(
    code: AgentErrorCode, 
    message: str, 
    agent_name: str, 
    retryable: bool = False
) -> Dict[str, Any]:
    """
    Creates a standardized error response for the Agent Failure Taxonomy.
    """
    return {
        "status": "error",
        "error_code": code.value,
        "message": message,
        "agent": agent_name,
        "retryable": retryable
    }
