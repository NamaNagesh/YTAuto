"""
YTAuto LangGraph State Schema.
"""
from typing import TypedDict, List, Dict, Any
from datetime import datetime

class YTAutoState(TypedDict, total=False):
    user_prompt: str
    topic: str
    research_report: Dict[str, Any]
    curriculum: Dict[str, Any]
    scripts: List[Dict[str, Any]]
    video_playlist: List[Dict[str, Any]]
    current_step: str
    status: str
    human_approved: bool
    revision_notes: str
    errors: List[str]
    created_at: str
    updated_at: str

def create_initial_state(user_prompt: str) -> YTAutoState:
    now = datetime.utcnow().isoformat()
    return YTAutoState(
        user_prompt=user_prompt, topic="", research_report={}, curriculum={},
        scripts=[], video_playlist=[], current_step="start", status="researching",
        human_approved=False, revision_notes="", errors=[],
        created_at=now, updated_at=now,
    )
