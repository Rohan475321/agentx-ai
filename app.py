import streamlit as st
import requests

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AgentX AI", page_icon="🤖", layout="centered")

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .main {
        background-color: #0e1117;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>🤖 AgentX AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Multi-Agent Productivity Assistant</p>", unsafe_allow_html=True)

st.divider()

# ---- INPUT ----
query = st.text_input("💬 Enter your request")

# ---- BUTTON ----
if st.button("🚀 Run Agent"):
    if query:
        try:
            res = requests.post(
                "https://agentx-ai-7gs8.onrender.com/process-query",
                json={"query": query}
            )
            response = res.json()["response"]

            # ---- OUTPUT ----
            st.success(f"✅ {response}")

        except:
            st.error("⚠️ Error connecting to server")

# ---- FOOTER ----
st.markdown("---")
st.markdown("<p style='text-align:center; color: gray;'></p>", unsafe_allow_html=True)