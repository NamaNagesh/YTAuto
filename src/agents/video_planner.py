"""
Video Planner Agent.
"""
from typing import Dict, Any, List
from langchain_core.messages import HumanMessage, SystemMessage
from state import YTAutoState
from config import config, llm

def video_planner_node(state: YTAutoState) -> YTAutoState:
    scripts = state.get("scripts", [])
    topic = state.get("topic", "")
    system_prompt = """Organize scripts into a playlist of 5-10 videos, each 5-10 minutes. Return JSON with playlist_title, playlist_description, videos (list with video_title, description, tags, estimated_duration_min, script_index, order), total_videos, total_duration_min."""
    human_prompt = f"Plan playlist for: {topic}\nScripts count: {len(scripts)}\nScripts: {scripts}"
    try:
        response = llm.invoke([SystemMessage(content=system_prompt), HumanMessage(content=human_prompt)])
        import json as _json
        playlist = _json.loads(response.content)
    except Exception as exc:
        playlist = {"playlist_title": f"{topic} Guide", "playlist_description": "", "videos": [], "total_videos": 0, "total_duration_min": 0, "error": str(exc)}
    state["video_playlist"] = playlist.get("videos", [])
    state["current_step"] = "video_planner"
    state["status"] = "planning"
    state["updated_at"] = __import__("datetime").datetime.utcnow().isoformat()
    return state
