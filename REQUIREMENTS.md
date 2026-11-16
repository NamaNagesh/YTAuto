# YTAuto Requirements Document

## 1. Functional Requirements

### FR1 - Topic Input
- The system shall accept a user prompt describing a software topic (e.g., "Strings in Java", "Python Decorators", "React Hooks").
- Input shall be a free-text string.

### FR2 - Topic Research
- The system shall research all basics and advanced concepts related to the topic.
- Research shall include: concept names, descriptions, difficulty levels, prerequisites, and key sub-topics.
- Output shall be a structured research report.

### FR3 - Curriculum Design
- The system shall organize concepts from basic to advanced.
- Each concept shall have associated coding samples.
- Curriculum shall be divided into modules/lessons with estimated durations.

### FR4 - Script Generation
- The system shall write a video script for each curriculum lesson.
- Scripts shall include: introduction, explanation, code examples, and conclusion.
- Code samples shall be copy-paste ready and commented.

### FR5 - Video Planning
- The system shall create a playlist of videos, each 5-10 minutes long.
- Each video shall have: title, description, tags, estimated duration, and script reference.
- Videos shall be ordered from basic to advanced.

### FR6 - Human Review
- The system shall pause before YouTube upload for user review.
- User shall be able to approve, request revisions, or reject the playlist.

### FR7 - YouTube Upload Preparation
- The system shall generate upload-ready metadata (title, description, tags, privacy status).
- The system shall optionally upload videos via YouTube Data API v3.

## 2. Non-Functional Requirements

### NFR1 - Performance
- Research and curriculum generation shall complete within 60 seconds for a typical topic.

### NFR2 - Reliability
- The workflow shall support checkpointing and resumption (LangGraph state persistence).

### NFR3 - Security
- API keys and secrets shall be stored in environment variables (.env), never in source code.

### NFR4 - Extensibility
- New agents and tools shall be easy to add without modifying existing node logic.

### NFR5 - Maintainability
- All code shall follow PEP 8 style guidelines and include docstrings.

## 3. Technical Requirements

### 3.1 Core Stack
| Component | Technology | Version |
|-----------|------------|---------|
| Language | Python | 3.10+ |
| Workflow Framework | LangGraph | latest |
| LLM Integration | LangChain | latest |
| LLM Provider | OpenAI (or compatible) | gpt-4o-mini / gpt-4o |
| Web Search | Tavily / Serper / DuckDuckGo | optional |
| YouTube API | Google API Python Client | latest |
| Environment | python-dotenv | latest |
| Testing | pytest | latest |

### 3.2 State Schema (LangGraph)
The workflow state shall include:
- `user_prompt`: str
- `topic`: str
- `research_report`: dict
- `curriculum`: dict
- `scripts`: list[dict]
- `video_playlist`: list[dict]
- `current_step`: str
- `status`: str (researching, designing, scripting, planning, reviewing, uploading, complete, error)
- `human_approved`: bool
- `revision_notes`: str
- `errors`: list[str]

### 3.3 Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| OPENAI_API_KEY | OpenAI API key | Yes |
| YOUTUBE_API_KEY | YouTube Data API v3 key | No (for upload) |
| YOUTUBE_CLIENT_ID | OAuth client ID | No |
| YOUTUBE_CLIENT_SECRET | OAuth client secret | No |
| SEARCH_API_KEY | Web search API key | No |
| LLM_MODEL | LLM model name | No (default: gpt-4o-mini) |

## 4. Acceptance Criteria

| ID | Criteria |
|----|----------|
| AC1 | Given prompt "Strings in Java", system produces research report covering basics and advanced concepts |
| AC2 | Curriculum is ordered from basic to advanced with coding samples |
| AC3 | Each video script is 5-10 minutes when spoken at normal pace |
| AC4 | Graph pauses at human review node and can resume after approval |
| AC5 | YouTube metadata (title, description, tags) is generated for each video |
| AC6 | Unit tests pass for all agents and workflow transitions |

## 5. Out of Scope

- Video recording/editing (scripts only; user records videos manually)
- Automatic thumbnail generation
- YouTube channel management beyond video upload
- Multi-language support (English only)