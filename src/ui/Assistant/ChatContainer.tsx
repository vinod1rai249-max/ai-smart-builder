import React, { useState } from 'react';
import { apiClient, PromptResponse } from '../api_client';

const ClinicalAssistant: React.FC = () => {
  const [prompt, setPrompt] = useState("");
  const [messages, setMessages] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!prompt) return;
    
    const userMsg = { role: 'user', text: prompt };
    setMessages([...messages, userMsg]);
    setPrompt("");
    setLoading(true);

    try {
      const response: PromptResponse = await apiClient.generateResponse(prompt);
      const aiMsg = {
        role: 'assistant',
        text: response.completion,
        status: response.status,
        evaluation: response.evaluation,
      };
      setMessages((prev) => [...prev, aiMsg]);
    } catch (error) {
      console.error("Failed to generate response", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="assistant-container">
      <div className="chat-history">
        {messages.map((m, i) => (
          <div key={i} className={`message ${m.role}`}>
            <p>{m.text}</p>
            {m.status === 'NEEDS_REVIEW' && (
              <span className="badge warning">Pending Clinical Review</span>
            )}
            {m.evaluation && (
              <div className="metrics">
                Grounding: {(m.evaluation.grounding * 100).toFixed(1)}%
              </div>
            )}
          </div>
        ))}
        {loading && <p>Processing Healthcare Query...</p>}
      </div>
      <div className="input-area">
        <input 
          value={prompt} 
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Ask a clinical or claims question..."
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
};

export default ClinicalAssistant;
