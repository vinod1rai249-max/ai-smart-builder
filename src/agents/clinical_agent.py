import time
import os
from typing import Dict, Any
from google.cloud import discoveryengine_v1 as discoveryengine
from .base_agent import BaseAgent
from ..utils.errors import create_error_response, AgentErrorCode

class ClinicalAgent(BaseAgent):
    def __init__(self):
        super().__init__("ClinicalAgent")
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        self.location = "global"
        self.data_store_id = os.getenv("SEARCH_ENGINE_ID", "clinical-data-store")
        self.client = discoveryengine.SearchServiceClient()

    def run(self, query: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes clinical reasoning using REAL Vertex AI Search (RAG).
        """
        start_time = time.time()
        print(f"[{self.name}] Searching Vertex AI Search for: {query}")
        
        serving_config = self.client.serving_config_path(
            project=self.project_id,
            location=self.location,
            data_store=self.data_store_id,
            serving_config="default_serving_config",
        )

        try:
            # 1. Real RAG Retrieval
            request = discoveryengine.SearchRequest(
                serving_config=serving_config,
                query=query,
                page_size=5,
            )
            response = self.client.search(request)
            
            retrieved_context = []
            citations = []
            
            for result in response.results:
                # Extract text from the document snippets
                snippet = result.document.derived_struct_data.get("snippets", [{}])[0].get("snippet", "")
                if snippet:
                    retrieved_context.append(snippet)
                    citations.append(result.document.id)

            if not retrieved_context:
                return create_error_response(
                    AgentErrorCode.LOW_GROUNDING_CONFIDENCE,
                    "No clinical documentation found in the Search Engine.",
                    self.name
                )

            latency = time.time() - start_time
            
            return {
                "status": "success",
                "agent": self.name,
                "data": {
                    "diagnosis_summary": "Retrieved from Clinical Search Engine",
                    "evidence_grounding": retrieved_context,
                    "confidence": 0.98,
                    "citations": list(set(citations)),
                    "latency_ms": int(latency * 1000)
                }
            }
        except Exception as e:
            return create_error_response(
                AgentErrorCode.DATA_SOURCE_UNAVAILABLE,
                f"Vertex AI Search failed: {str(e)}",
                self.name,
                retryable=True
            )
