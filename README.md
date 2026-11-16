# YTAuto - YouTube Video Automation Workflow

YTAuto is a LangGraph-powered workflow automation project that transforms a software topic prompt into a complete YouTube video playlist. It researches basics and advanced concepts, designs a curriculum, writes scripts, plans 5-10 minute videos, and prepares them for YouTube upload.

## Project Goal

Given a user prompt about a software topic (e.g., "Strings in Java"), the workflow:

1. **Researches** all basics and advanced concepts of the topic
2. **Designs** a basic-to-advanced curriculum with coding samples
3. **Writes** video scripts for each topic segment
4. **Plans** a playlist of 5-10 minute videos covering all topics
5. **Prepares** videos for review and YouTube upload

## Project Structure

```
YTAuto/
├── README.md
├── PROJECT_PLAN.md
├── REQUIREMENTS.md
├── requirements.txt
├── .env.example
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── state.py
│   ├── langgraph_workflow.py
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── topic_researcher.py
│   │   ├── curriculum_designer.py
│   │   ├── script_writer.py
│   │   ├── video_planner.py
│   │   └── youtube_uploader.py
│   └── tools/
│       ├── __init__.py
│       ├── web_search.py
│       ├── youtube_api.py
│       └── file_utils.py
├── tests/
│   ├── __init__.py
│   └── test_workflow.py
├── data/
│   ├── topics/
│   └── output/
└── notebooks/
    └── workflow_demo.ipynb
```

## Quick Start

```bash
# 1. Navigate to project
cd d:\pythonRepo\YTAuto

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
copy .env.example .env
# Edit .env with your API keys

# 5. Run the workflow
python src/main.py
```

## LangGraph Workflow Overview

The core workflow is defined in `src/langgraph_workflow.py` using LangGraph's `StateGraph`. Key nodes:

- `topic_researcher` - Researches basics and advanced concepts
- `curriculum_designer` - Designs basic-to-advanced curriculum
- `script_writer` - Writes scripts with coding samples
- `video_planner` - Plans 5-10 minute video playlist
- `human_review` - Human review checkpoint (interrupt)
- `youtube_uploader` - Prepares YouTube upload

## Requirements

- Python 3.10+
- LangGraph
- LangChain
- OpenAI API key (or compatible LLM)
- YouTube Data API v3 credentials (for upload)

See `REQUIREMENTS.md` for full details.