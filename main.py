import streamlit as st
import requests
import uuid

# ---------------------------
# App Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Assistant Hub", 
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Agent Configurations
# ---------------------------
AGENTS = {
    "Calendar AI": {
        "title": "🗓️ Calendar AI Assistant",
        "description": "Manage your calendar, schedule events, and get calendar-related assistance",
        "webhook_url": "http://localhost:5678/webhook/chatBot_n8n",
        "icon": "🗓️",
        "color": "#FF6B6B"
    },
    "RAG AI": {
        "title": "🧠 RAG AI Assistant", 
        "description": "Ask questions and get answers from your knowledge base using RAG",
        "webhook_url": "http://localhost:5678/webhook/RAG_n8n",
        "icon": "🧠",
        "color": "#4ECDC4"
    }
}

# ---------------------------
# Session Management
# ---------------------------
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

if "selected_agent" not in st.session_state:
    st.session_state["selected_agent"] = "Calendar AI"

if "messages" not in st.session_state:
    st.session_state["messages"] = {}
    for agent in AGENTS.keys():
        st.session_state["messages"][agent] = []

# ---------------------------
# Enhanced Sidebar Design
# ---------------------------
with st.sidebar:
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
            color: white;
        }
        .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
            color: white;
        }
        .sidebar .sidebar-content button {
            border-radius: 8px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🤖 AI Assistant Hub")
    st.markdown("---")

    st.subheader("Select an Agent")

    # Agent selection with custom styling
    for agent_name, agent_config in AGENTS.items():
        if st.button(
            f"{agent_config['icon']} {agent_name}",
            key=f"btn_{agent_name}",
            use_container_width=True,
            type="primary" if st.session_state["selected_agent"] == agent_name else "secondary"
        ):
            st.session_state["selected_agent"] = agent_name
            st.rerun()

    st.markdown("---")

    # Current agent info
    current_agent = AGENTS[st.session_state["selected_agent"]]
    st.markdown(f"### Current Agent: {current_agent['icon']} {st.session_state['selected_agent']}")
    st.markdown(f"*{current_agent['description']}*")

    st.markdown("---")

    # Session info
    st.markdown("### Session Info")
    st.markdown(f"**Session ID:** `{st.session_state['session_id'][:8]}...`")

    # Clear conversation button
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state["messages"][st.session_state["selected_agent"]] = []
        st.rerun()

    # Reset all conversations
    if st.button("🔄 Reset All Conversations", use_container_width=True):
        for agent in AGENTS.keys():
            st.session_state["messages"][agent] = []
        st.session_state["session_id"] = str(uuid.uuid4())
        st.rerun()

# ---------------------------
# Enhanced Main Chat Interface
# ---------------------------
current_agent = AGENTS[st.session_state["selected_agent"]]

# Display current agent header
st.markdown(
    f"""
    <div style='text-align: center; padding: 1rem; background: {current_agent['color']}; color: white; border-radius: 8px;'>
        <h1>{current_agent['icon']} {current_agent['title']}</h1>
        <p>{current_agent['description']}</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Display conversation count
current_messages = st.session_state["messages"][st.session_state["selected_agent"]]
if len(current_messages) > 0:
    st.caption(f"💬 {len(current_messages) // 2} messages in this conversation")

# ---------------------------
# Display Chat History
# ---------------------------
for msg in current_messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# ---------------------------
# Chat Input
# ---------------------------
if prompt := st.chat_input(f"Ask {st.session_state['selected_agent']} anything..."):
    # Add user's message to current agent's conversation
    st.session_state["messages"][st.session_state["selected_agent"]].append({
        "role": "user", 
        "content": prompt
    })
    st.chat_message("user").write(prompt)

    # Placeholder for assistant message
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.write(f"{current_agent['icon']} Thinking...")

        try:
            # Send request to the selected agent's webhook
            response = requests.post(   
                current_agent["webhook_url"],
                json={
                    "message": prompt,
                    "sessionId": st.session_state["session_id"]
                },
                timeout=60
            )

            # Try parsing JSON safely
            try:
                data = response.json()
            except ValueError:
                st.warning(f"⚠️ Waiting for {st.session_state['selected_agent']}... (empty initial response)")
                data = {}

            # Check status code + extract reply
            if response.status_code == 200:
                reply = data.get("reply", f"No response received from {st.session_state['selected_agent']}.")
            else:
                reply = f"Error: Could not connect to {st.session_state['selected_agent']} (HTTP {response.status_code})."

        except requests.exceptions.RequestException as e:
            reply = f"Network error: {e}"

        # Update placeholder with final response
        placeholder.write(reply)

    # Save assistant message to current agent's conversation
    st.session_state["messages"][st.session_state["selected_agent"]].append({
        "role": "assistant", 
        "content": reply
    })

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <small>AI Assistant Hub • Switch between agents using the sidebar</small>
    </div>
    """, 
    unsafe_allow_html=True
)
