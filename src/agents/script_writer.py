"""
Script Writer Agent.
"""
from typing import Dict, Any, List
from langchain_core.messages import HumanMessage, SystemMessage
from state import YTAutoState
from config import config, llm

def script_writer_node(state: YTAutoState) -> YTAutoState:
    curriculum = state.get("curriculum", {})
    topic = state.get("topic", "")
    modules = curriculum.get("modules", [])
    scripts: List[Dict[str, Any]] = []
    system_prompt = """Write a 5-10 minute video script for a lesson. Return JSON with lesson_title, video_title, description, tags, script, coding_samples, estimated_duration_min."""
    for module in modules:
        for lesson in module.get("lessons", []):
            human_prompt = f"""Write a video script for:\nTopic: {topic}\nModule: {module.get("module_name","")}\nLesson: {lesson.get("lesson_title","")}\nDescription: {lesson.get("description","")}\nDifficulty: {lesson.get("difficulty","basic")}"""
            try:
                response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)])
                import json as _json
                script_data = _json.loads(response.content)
            except Exception as exc:
                script_data = {"lesson_title": lesson.get("lesson_title",""), "video_title": f"{topic} - {lesson.get('lesson_title','')}", "description": lesson.get("description",""), "tags": [topic, "tutorial"], "script": f"Script error: {exc}", "coding_samples": [], "estimated_duration_min": 7}
            scripts.append(script_data)
    state["scripts"] = scripts
    state["current_step"] = "script_writer"
    state["status"] = "scripting"
    state["updated_at"] = __import__("datetime").datetime.utcnow().isoformat()
    return state
