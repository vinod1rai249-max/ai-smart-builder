export interface PromptResponse {
  prompt_id: string;
  original_prompt: string;
  redacted_prompt: string;
  completion: string;
  status: 'success' | 'NEEDS_REVIEW' | 'failed';
  hitl_reason?: string;
  evaluation?: {
    grounding: number;
    faithfulness: number;
    safety: string;
  };
  latency_ms?: Record<string, number>;
}

export interface HitlReview {
  interaction_id: string;
  status: 'PENDING' | 'RESOLVED';
  hitl_reason: string;
  prompt_redacted: string;
  suggested_response: string;
  created_at: string;
}

const API_BASE = "http://localhost:8080";

export const apiClient = {
  async generateResponse(prompt: string): Promise<PromptResponse> {
    const response = await fetch(`${API_BASE}/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
    return response.json();
  },

  async getHitlQueue(): Promise<HitlReview[]> {
    const response = await fetch(`${API_BASE}/hitl/queue`);
    return response.json();
  },

  async resolveHitl(id: string, action: string, notes: string): Promise<any> {
    const response = await fetch(`${API_BASE}/hitl/resolve`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ interaction_id: id, action, notes }),
    });
    return response.json();
  },
};
