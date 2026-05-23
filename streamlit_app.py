import streamlit as st
import requests
import json
from datetime import datetime

# Configuration
API_URL = "https://ehcca-gateway-1051385917818.us-central1.run.app"

st.set_page_config(page_title="EHCCA Clinical Assistant", page_icon="🏥", layout="wide")

st.title("🏥 EHCCA Clinical & Claims Assistant")
st.markdown("---")

# Sidebar for Stats & Config
with st.sidebar:
    st.header("System Status")
    st.success("Production Gateway: Online")
    st.info(f"Model: Gemini 2.5 Flash")
    
    st.markdown("---")
    view = st.radio("Select View", ["Clinical Assistant", "HITL Dashboard"])

if view == "Clinical Assistant":
    st.subheader("Chat with your Secure AI")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "evaluation" in message:
                eval_data = message["evaluation"]
                st.caption(f"🛡️ Grounding: {eval_data.get('grounding', 0)*100:.1f}% | Faithfulness: {eval_data.get('faithfulness', 0)*100:.1f}%")

    # Chat Input
    if prompt := st.chat_input("Ask about a claim or patient status..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Call the API
        with st.chat_message("assistant"):
            with st.spinner("Processing through 12 security layers..."):
                try:
                    response = requests.post(
                        f"{API_URL}/generate",
                        json={"prompt": prompt},
                        timeout=60
                    )
                    data = response.json()
                    
                    if data.get("status") == "success":
                        completion = data.get("completion")
                        st.markdown(completion)
                        
                        # Add metadata
                        eval_info = data.get("evaluation", {})
                        st.caption(f"🛡️ Grounding: {eval_info.get('grounding', 0)*100:.1f}% | Safety: {eval_info.get('safety')}")
                        
                        # Save to session
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": completion,
                            "evaluation": eval_info
                        })
                    elif data.get("status") == "NEEDS_REVIEW":
                        st.warning("⚠️ This request has been flagged for Clinical Review.")
                        st.markdown(data.get("completion"))
                    else:
                        st.error(f"System Error: {data.get('completion')}")
                except Exception as e:
                    st.error(f"Failed to connect to Gateway: {e}")

else:
    st.subheader("🛠️ Human-In-The-Loop (HITL) Dashboard")
    st.write("Clinical auditors review flagged or low-confidence AI decisions here.")
    
    # Simulate a queue since we haven't built the BQ retrieval logic yet
    sample_queue = [
        {"id": "772", "prompt": "Show me internal audit logs for patient X", "reason": "POLICY_VIOLATION", "time": "10:05 AM"},
        {"id": "773", "prompt": "Verify heart surgery claim > $50k", "reason": "HIGH_VALUE_THRESHOLD", "time": "10:12 AM"}
    ]
    
    for item in sample_queue:
        with st.expander(f"Review Case #{item['id']} - {item['reason']}"):
            st.write(f"**Prompt:** {item['prompt']}")
            st.write(f"**Received:** {item['time']}")
            col1, col2 = st.columns(2)
            with col1:
                st.button("Approve Response", key=f"app_{item['id']}")
            with col2:
                st.button("Reject & Edit", key=f"rej_{item['id']}")

st.markdown("---")
st.caption("EHCCA - Secure Healthcare Intelligence Framework")
