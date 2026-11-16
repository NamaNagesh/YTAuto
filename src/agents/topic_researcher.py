"""
Topic Researcher Agent.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage
from state import YTAutoState
from config import config, llm

def topic_researcher_node(state: YTAutoState) -> YTAutoState:
    topic = state.get("topic") or state.get("user_prompt", "")
    system_prompt = """You are an expert technical researcher. Research basics and advanced concepts for a software topic. Return JSON with topic, basics, advanced, subtopics, prerequisites, difficulty_level."""
    human_prompt = f"Research the software topic: {topic}"
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)])
        import json as _json
        research_report = _json.loads(response.content)
    except Exception as exc:
        research_report = {"topic": topic, "basics": [], "advanced": [], "subtopics": [], "prerequisites": [], "difficulty_level": "beginner", "error": str(exc)}
    state["topic"] = topic
    state["research_report"] = research_report
    state["current_step"] = "topic_researcher"
    state["status"] = "researching"
    state["updated_at"] = __import__("datetime").datetime.utcnow().isoformat()
    return state
