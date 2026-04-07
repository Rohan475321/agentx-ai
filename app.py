import streamlit as st
import requests
import sqlite3
import pandas as pd

# ---- CONFIG ----
st.set_page_config(page_title="AgentX AI", page_icon="🤖", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
body {background-color: #0e1117; color: white;}
.chat-box {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.user {
    background-color: #1f77b4;
    color: white;
    text-align: right;
}
.bot {
    background-color: #262730;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.title("🤖 AgentX AI")
st.caption("Multi-Agent Productivity Assistant")

# ---- SESSION STATE (chat memory) ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- LAYOUT ----
col1, col2 = st.columns([2, 1])

# ================= CHAT UI =================
with col1:
    st.subheader("💬 Chat Assistant")

    # show chat history
    for msg in st.session_state.messages:
        role, text = msg
        if role == "user":
            st.markdown(f"<div class='chat-box user'>🧑 {text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-box bot'>🤖 {text}</div>", unsafe_allow_html=True)

    # input
    query = st.text_input("Type your message...")

    if st.button("Send"):
        if query:
            # store user message
            st.session_state.messages.append(("user", query))

            try:
                res = requests.post(
                    "https://agentx-ai-7gs8.onrender.com/process-query",
                    json={"query": query}
                )
                response = res.json()["response"]
            except:
                response = "Error connecting to backend"

            # store bot reply
            st.session_state.messages.append(("bot", response))
            st.rerun()

# ================= ANALYTICS =================
with col2:
    st.subheader("📊 Dashboard")

    try:
        conn = sqlite3.connect("data.db")
        tasks = pd.read_sql("SELECT * FROM tasks", conn)
        notes = pd.read_sql("SELECT * FROM notes", conn)

        # ---- METRICS (CARDS) ----
        st.metric("📌 Total Tasks", len(tasks))
        st.metric("📝 Notes Saved", len(notes))

        st.divider()

        # ---- TABLE ----
        st.write("📋 Task List")
        st.dataframe(tasks)

        st.write("🗒️ Notes")
        st.dataframe(notes)

        # ---- CHART ----
        if not tasks.empty:
            st.write("📈 Task Activity")
            st.bar_chart(tasks.index)

    except:
        st.info("No data available yet")

# ---- FOOTER ----
st.markdown("---")
st.markdown("🚀 Built with FastAPI + Gemini + Streamlit")