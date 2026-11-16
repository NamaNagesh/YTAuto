"""
Curriculum Designer Agent.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage
from state import YTAutoState
from config import config, llm

def curriculum_designer_node(state: YTAutoState) -> YTAutoState:
    research_report = state.get("research_report", {})
    topic = state.get("topic", "")
    system_prompt = """Design a curriculum from basic to advanced. Return JSON with topic, modules (each with lessons having lesson_title, description, difficulty, coding_sample, estimated_duration_min), total_lessons, total_estimated_duration_min."""
    human_prompt = f"Design curriculum for: {topic}\nResearch: {research_report}"
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)])
        import json as _json
        curriculum = _json.loads(response.content)
    except Exception as exc:
        curriculum = {"topic": topic, "modules": [], "total_lessons": 0, "total_estimated_duration_min": 0, "error": str(exc)}
    state["curriculum"] = curriculum
    state["current_step"] = "curriculum_designer"
    state["status"] = "designing"
    state["updated_at"] = __import__("datetime").datetime.utcnow().isoformat()
    return state
