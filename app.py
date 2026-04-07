import streamlit as st
import requests

st.title("AgentX AI Dashboard")

query = st.text_input("Enter your task")

if st.button("Run"):
    res = requests.post(
        "https://agentx-ai-7gs8.onrender.com/process-query",
        json={"query": query}
    )
    st.write(res.json())