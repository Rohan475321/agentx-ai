from fastapi import FastAPI
from pydantic import BaseModel
from agents import main_agent

app = FastAPI()

# 👇 THIS FIXES YOUR ISSUE
class Query(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "AgentX AI Running"}

@app.post("/process-query")
def process_query(data: Query):
    result = main_agent(data.query)

    return {"response": result}