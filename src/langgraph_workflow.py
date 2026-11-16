"""YTAuto LangGraph Workflow.

Defines the StateGraph workflow that orchestrates the entire
YouTube video automation pipeline from topic prompt to upload-ready playlist.
"""
import os, json
from typing import Dict, Any, List
from datetime import datetime
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
# from langchain_openai import ChatOpenAI  # Commented out - using Ollama
from langchain_core.messages import HumanMessage, SystemMessage
from state import YTAutoState, create_initial_state
from config import config, llm
from agents.topic_researcher import topic_researcher_node
from agents.curriculum_designer import curriculum_designer_node
from agents.script_writer import script_writer_node
from agents.video_planner import video_planner_node
from agents.youtube_uploader import youtube_uploader_node

# llm = ChatOpenAI(...)  # Now imported from config (Ollama)

def human_review_node(state: YTAutoState) -> YTAutoState:
    print()
    print("=" * 60)
    print("[HUMAN REVIEW] Video Playlist Ready for Review")
    print("=" * 60)
    print(f"Topic: {state.get("topic")}")
    print(f"Videos: {len(state.get("video_playlist", []))}")
    print(f"Status: {state.get("status")}")
    print("=" * 60)
    print()
    print("Review playlist in data/output/")
    print("To approve: set human_approved=True and resume.")
    print("To revise: provide revision_notes and resume.")
    print()
    state["current_step"] = "human_review"
    state["status"] = "reviewing"
    state["updated_at"] = datetime.utcnow().isoformat()
    return state

def should_continue_after_review(state: YTAutoState) -> str:
    return "upload" if state.get("human_approved") else "revise"

def build_workflow(use_checkpoint: bool = False) -> StateGraph:
    workflow = StateGraph(YTAutoState)
    workflow.add_node("topic_researcher", topic_researcher_node)
    workflow.add_node("curriculum_designer", curriculum_designer_node)
    workflow.add_node("script_writer", script_writer_node)
    workflow.add_node("video_planner", video_planner_node)
    workflow.add_node("human_review", human_review_node)
    workflow.add_node("youtube_uploader", youtube_uploader_node)
    workflow.add_edge("topic_researcher", "curriculum_designer")
    workflow.add_edge("curriculum_designer", "script_writer")
    workflow.add_edge("script_writer", "video_planner")
    workflow.add_edge("video_planner", "human_review")
    workflow.add_conditional_edges("human_review", should_continue_after_review, {"upload": "youtube_uploader", "revise": "video_planner"})
    workflow.add_edge("youtube_uploader", END)
    workflow.set_entry_point("topic_researcher")
    if use_checkpoint:
        return workflow.compile(checkpointer=MemorySaver())
    return workflow.compile()

def run_workflow(user_prompt: str, use_checkpoint: bool = False, thread_id: str = "default") -> Dict[str, Any]:
    app = build_workflow(use_checkpoint=use_checkpoint)
    initial_state = create_initial_state(user_prompt)
    config_dict = {"configurable": {"thread_id": thread_id}} if use_checkpoint else {}
    return app.invoke(initial_state, config=config_dict)

def resume_workflow(thread_id: str = "default", human_approved: bool = True, revision_notes: str = "") -> Dict[str, Any]:
    app = build_workflow(use_checkpoint=True)
    config_dict = {"configurable": {"thread_id": thread_id}}
    current_state = app.get_state(config_dict)
    if current_state is None:
        raise ValueError(f"No checkpoint found for thread_id: {thread_id}")
    updated_state = current_state.values.copy()
    updated_state["human_approved"] = human_approved
    updated_state["revision_notes"] = revision_notes
    updated_state["status"] = "uploading" if human_approved else "revising"
    updated_state["updated_at"] = datetime.utcnow().isoformat()
    app.update_state(config_dict, updated_state)
    return app.invoke(None, config=config_dict)

if __name__ == "__main__":
    result = run_workflow("Strings in Java", use_checkpoint=False)
    print(json.dumps({k: v for k, v in result.items() if k != "scripts"}, indent=2, default=str))
