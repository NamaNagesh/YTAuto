# YTAuto Project Plan

## 1. Project Overview

**Project Name:** YTAuto  
**Goal:** Automate end-to-end creation of YouTube educational video playlists from a single software topic prompt using LangGraph workflow automation.  
**Example Input:** "Strings in Java"  
**Expected Output:** A structured playlist of 5-10 minute videos covering basics to advanced concepts, complete with scripts, coding samples, and upload-ready metadata.

## 2. Objectives

| Objective | Description |
|-----------|-------------|
| Topic Research | Pull all basics and advanced concepts for a given software topic |
| Curriculum Design | Organize concepts from basic to advanced with coding samples |
| Script Generation | Write video scripts for each curriculum segment |
| Video Planning | Create a playlist of 5-10 minute videos |
| Human Review | Allow user to review and approve videos before upload |
| YouTube Upload | Prepare/upload videos to YouTube (via API) |

## 3. Workflow Stages (LangGraph Nodes)

### Stage 1: Topic Researcher
- Input: User prompt (e.g., "Strings in Java")
- Action: Search web/documentation for basics and advanced concepts
- Output: Research report with concept list, difficulty levels, key sub-topics

### Stage 2: Curriculum Designer
- Input: Research report
- Action: Structure concepts from basic to advanced; assign coding samples
- Output: Curriculum with modules, lessons, estimated video durations

### Stage 3: Script Writer
- Input: Curriculum
- Action: Write detailed video scripts including code examples and explanations
- Output: Scripts for each video lesson

### Stage 4: Video Planner
- Input: Scripts
- Action: Group into 5-10 minute videos, create playlist order, generate metadata (title, description, tags)
- Output: Video playlist plan with metadata

### Stage 5: Human Review (Interrupt)
- Input: Video playlist plan
- Action: Pause for user review and approval/revision
- Output: Approved plan or revision requests

### Stage 6: YouTube Uploader
- Input: Approved plan
- Action: Prepare upload package (scripts, metadata, thumbnail ideas); optional API upload
- Output: Upload confirmation or upload-ready files

## 4. Deliverables

| Deliverable | Format | Location |
|-------------|--------|----------|
| Project Plan | Markdown | PROJECT_PLAN.md |
| Requirements Document | Markdown | REQUIREMENTS.md |
| LangGraph Workflow | Python | src/langgraph_workflow.py |
| Agent Implementations | Python | src/agents/ |
| Tool Integrations | Python | src/tools/ |
| Entry Point | Python | src/main.py |
| Configuration | Python | src/config.py |
| State Schema | Python | src/state.py |
| Unit Tests | Python | tests/ |
| Dependencies | requirements.txt | requirements.txt |
| Environment Template | .env.example | .env.example |

## 5. Timeline (Suggested)

| Phase | Task | Estimated |
|-------|------|-----------|
| Phase 1 | Project setup, requirements, state schema | 1 day |
| Phase 2 | Implement agents (researcher, curriculum, script) | 2 days |
| Phase 3 | Implement video planner and YouTube uploader | 1 day |
| Phase 4 | LangGraph wiring, human-in-the-loop, testing | 2 days |
| Phase 5 | Documentation, demo, cleanup | 1 day |

## 6. Success Criteria

- [ ] User can input any software topic and get a complete video playlist plan
- [ ] Curriculum progresses from basic to advanced concepts
- [ ] Each video script includes coding samples
- [ ] Video durations are within 5-10 minutes
- [ ] Human review checkpoint works (graph can pause and resume)
- [ ] YouTube upload preparation is complete (metadata, descriptions, tags)

## 7. Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| LLM hallucination in technical content | Ground research with web search; add validation step |
| YouTube API quota limits | Prepare upload files locally; optional API upload |
| Long video scripts exceeding 10 mins | Curriculum designer enforces duration limits per segment |
| API key management | Use .env file; never commit secrets |