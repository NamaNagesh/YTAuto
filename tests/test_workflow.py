"""
Unit tests for YTAuto workflow components.
"""
import os, sys, json, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from state import YTAutoState, create_initial_state
from config import config

def test_create_initial_state():
    state = create_initial_state("Strings in Java")
    assert state["user_prompt"] == "Strings in Java"
    assert state["topic"] == ""
    assert state["status"] == "researching"
    assert state["human_approved"] is False
    assert state["scripts"] == []
    assert state["video_playlist"] == []
    assert "created_at" in state

def test_config_defaults():
    assert config.MIN_VIDEOS == 5
    assert config.MAX_VIDEOS == 10
    assert config.MAX_VIDEO_DURATION_MIN == 5
    assert config.MAX_VIDEO_DURATION_MAX == 10

def test_state_fields():
    required = ["user_prompt","topic","research_report","curriculum","scripts","video_playlist","current_step","status","human_approved","revision_notes","errors","created_at","updated_at"]
    for f in required:
        assert f in YTAutoState.__annotations__, f"Missing: {f}"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
