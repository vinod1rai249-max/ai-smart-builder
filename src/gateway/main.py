import os
import uuid
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .dlp_service import DLPService
from .vertex_service import VertexService
from .evaluation_service import EvaluationService
from ..agents.orchestrator import Orchestrator
from ..utils.logger import logger

app = FastAPI(title="EHCCA AI Gateway Proxy")

# Enable CORS for the UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
project_id = os.getenv("GOOGLE_CLOUD_PROJECT", "ehcca-dev-project")
dlp = DLPService(project_id=project_id)
vertex = VertexService(project_id=project_id)
evaluator = EvaluationService(project_id=project_id)
orchestrator = Orchestrator()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    prompt_id: str
    original_prompt: str
    redacted_prompt: str
    completion: str
    status: str = "success"
    hitl_reason: str = None
    evaluation: dict = None
    latency_ms: dict = None

def check_hitl_triggers(redacted_prompt: str, agent_response: dict) -> tuple[bool, str]:
    """
    Checks if the response should be routed to a Human-In-The-Loop.
    """
    # Trigger 1: High value claims
    if agent_response.get("agent") == "ClaimsAgent":
        amount = agent_response.get("data", {}).get("amount", 0)
        if amount > 5000:
            return True, f"High value claim detected: ${amount}"

    # Trigger 2: Low confidence clinical reasoning
    if agent_response.get("agent") == "ClinicalAgent":
        confidence = agent_response.get("data", {}).get("confidence", 1.0)
        if confidence < 0.85:
            return True, f"Low clinical confidence: {confidence}"

    return False, None

@app.post("/generate", response_model=PromptResponse)
async def generate_response(request: PromptRequest):
    """
    Main entry point for the AI Gateway.
    Redacts PHI, Orchestrates Agents, Evaluates, and Logs results.
    """
    start_total = time.time()
    prompt_id = str(uuid.uuid4())
    
    try:
        # 1. Redact PHI
        start_dlp = time.time()
        redacted = dlp.redact_phi(request.prompt)
        dlp_latency = int((time.time() - start_dlp) * 1000)
        
        # 2. Orchestrate Agents
        start_agent = time.time()
        agent_result = orchestrator.route_and_execute(redacted)
        agent_latency = int((time.time() - start_agent) * 1000)
        
        # 3. Handle Agent Failures
        if agent_result.get("status") == "error":
            error_code = agent_result.get("error_code", "UNKNOWN_AGENT_ERROR")
            return PromptResponse(
                prompt_id=prompt_id,
                original_prompt=request.prompt,
                redacted_prompt=redacted,
                completion=f"Request stopped by {agent_result.get('agent', 'System')}: {agent_result['message']}",
                status="error",
                hitl_reason=f"Agent Error: {error_code}"
            )
        
        # 4. Check HITL Triggers (Contextual)
        needs_hitl, reason = check_hitl_triggers(redacted, agent_result)
        
        if needs_hitl:
            return PromptResponse(
                prompt_id=prompt_id,
                original_prompt=request.prompt,
                redacted_prompt=redacted,
                completion="This request requires a human review due to security/accuracy policies.",
                status="NEEDS_REVIEW",
                hitl_reason=reason
            )

        # 5. Model Completion
        start_model = time.time()
        completion = vertex.get_completion(f"Analyze this {agent_result['agent']} data: {agent_result['data']}")
        model_latency = int((time.time() - start_model) * 1000)
        
        # 6. Automated Evaluation (New in Sprint 005)
        eval_result = evaluator.evaluate_response(
            redacted, 
            agent_result.get("data", {}).get("evidence_grounding", []), 
            completion
        )
        
        # 7. Governance Logging
        total_latency = int((time.time() - start_total) * 1000)
        latency_map = {
            "dlp_ms": dlp_latency,
            "agent_ms": agent_latency,
            "model_ms": model_latency,
            "total_ms": total_latency
        }
        
        logger.log_interaction({
            "prompt_id": prompt_id,
            "agent": agent_result["agent"],
            "evaluation": eval_result["metrics"],
            "latency": latency_map,
            "status": "success"
        })
        
        return PromptResponse(
            prompt_id=prompt_id,
            original_prompt=request.prompt,
            redacted_prompt=redacted,
            completion=completion,
            status="success",
            evaluation=eval_result["metrics"],
            latency_ms=latency_map
        )
    except Exception as e:
        logger.log_interaction({"prompt_id": prompt_id, "status": "failed", "error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
