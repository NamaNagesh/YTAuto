"""
YouTube Uploader Agent.
"""
from typing import Dict, Any
import json, os
from state import YTAutoState
from config import config

def youtube_uploader_node(state: YTAutoState) -> YTAutoState:
    video_playlist = state.get("video_playlist", [])
    topic = state.get("topic", "")
    human_approved = state.get("human_approved", False)
    if not human_approved:
        state["status"] = "error"
        state["errors"] = state.get("errors", []) + ["Human approval required before upload."]
        return state
    upload_package = {
        "topic": topic,
        "playlist_title": f"{topic} - Complete Basic to Advanced Guide",
        "playlist_description": f"Learn {topic} from basics to advanced with coding examples.",
        "videos": video_playlist,
        "upload_ready": True,
        "uploaded_at": __import__("datetime").datetime.utcnow().isoformat(),
    }
    os.makedirs(config.OUTPUT_DIR, exist_ok=True)
    upload_path = os.path.join(config.OUTPUT_DIR, f"{topic.replace(" ", "_")}_upload_package.json")
    with open(upload_path, "w", encoding="utf-8") as f:
        json.dump(upload_package, f, indent=2)
    state["current_step"] = "youtube_uploader"
    state["status"] = "complete"
    state["updated_at"] = __import__("datetime").datetime.utcnow().isoformat()
    return state
