from fastapi import APIRouter
from app.agents.langgraph_agent import build_agent

router = APIRouter()
agent = build_agent()

@router.post("/")
def chat(data: dict):
    return agent.invoke({"input": data["message"]})