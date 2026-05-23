import React, { useEffect, useState } from 'react';
import { apiClient, HitlReview } from '../api_client';

const HitlDashboard: React.FC = () => {
  const [queue, setQueue] = useState<HitlReview[]>([]);
  const [selectedReview, setSelectedReview] = useState<HitlReview | null>(null);

  useEffect(() => {
    loadQueue();
  }, []);

  const loadQueue = async () => {
    const data = await apiClient.getHitlQueue();
    setQueue(data);
  };

  const handleResolve = async (action: string) => {
    if (!selectedReview) return;
    await apiClient.resolveHitl(selectedReview.interaction_id, action, "Resolved via Dashboard");
    setSelectedReview(null);
    loadQueue();
  };

  return (
    <div className="dashboard-container">
      <h2>Clinical Review Queue</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Reason</th>
            <th>Date</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {queue.map((r) => (
            <tr key={r.interaction_id}>
              <td>{r.interaction_id.slice(0, 8)}</td>
              <td>{r.hitl_reason}</td>
              <td>{new Date(r.created_at).toLocaleString()}</td>
              <td>
                <button onClick={() => setSelectedReview(r)}>Review</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedReview && (
        <div className="modal">
          <h3>Review Interaction</h3>
          <div className="context">
            <p><strong>Prompt:</strong> {selectedReview.prompt_redacted}</p>
            <p><strong>AI Suggestion:</strong> {selectedReview.suggested_response}</p>
          </div>
          <div className="actions">
            <button onClick={() => handleResolve('APPROVE')}>Approve</button>
            <button onClick={() => handleResolve('REJECT')}>Reject</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default HitlDashboard;
