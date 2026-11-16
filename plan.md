# Plan: YTAuto Agent Enhancements & Feasibility Analysis

Since you're in **Plan mode**, I'll outline the architecture, agents, subscriptions, and free-vs-paid reality check before anything is built.

---

## 1. Enhanced Topic Research Agent

**Goal:** Take a user topic (e.g., "Strings in Java") and research it across the internet, blogs, existing YouTube channels, and documentation.

### New Sub-Components to Add

| Component | Purpose | Free Options | Paid Options |
|-----------|---------|--------------|--------------|
| **Web Search** | Search Google/Bing for blogs, docs, tutorials | DuckDuckGo HTML scraping, Serper.dev (free tier), Tavily (free tier) | Serper, Tavily, Google Custom Search |
| **YouTube Research** | Find existing videos/channels on the topic to avoid duplication and identify gaps | YouTube Data API v3 (free quota: 10k units/day) | YouTube API (paid if over quota) |
| **Blog Scraper** | Extract article content from top search results | BeautifulSoup + requests, Playwright (headless browser) | Apify, ScrapingBee |
| **RSS Feed Reader** | Subscribe to tech blogs (medium, dev.to, etc.) | `feedparser` (free) | — |
| **LLM Synthesizer** | Merge all sources into structured research report | Local Ollama (free) | OpenAI/Anthropic (paid) |

### Output of This Agent
```json
{
  "topic": "Strings in Java",
  "sources": [{"url": "...", "title": "...", "type": "blog|video|docs"}],
  "key_concepts": [...],
  "common_mistakes": [...],
  "existing_video_gaps": [...],
  "difficulty_progression": ["basic", "intermediate", "advanced"]
}
```

---

## 2. New: Code Execution & Capture Agent (Critical for Your Requirement)

**Goal:** Run the sample code from the curriculum and record the screen/output so it can be turned into video.

### Architecture

```
Script → Code Extraction → Sandbox Execution → Screen Capture → Video Segment
```

### Tools Needed

| Task | Tool | Free? | Notes |
|------|------|-------|-------|
| Code sandbox | **E2B** (free tier), **Daytona**, or local Docker | Yes (E2B has free tier) | Isolated execution for Java/Python/etc. |
| Terminal capture | `asciinema`, `script` command, or FFmpeg | Yes | Records terminal output |
| Screen recording | **FFmpeg** (screen capture), **PyAutoGUI**, **Playwright** | Yes | Can record browser or desktop |
| Code output parsing | Custom Python | Yes | Captures stdout/stderr |

### What It Produces
- Video files of code running (terminal/screen recordings)
- Screenshots of code output
- Error logs (if code fails)

---

## 3. Enhanced Video Planner / Video Generation Agent

**Goal:** Generate complete interactive videos using AI, without you recording manually.

### Pipeline per Video

```
Script → TTS (voiceover) → Code Execution Capture → Visual Assembly → Final MP4
```

### Components

| Component | Free Options | Paid Options |
|-----------|--------------|--------------|
| **Text-to-Speech** | Edge-TTS (free, unlimited), Microsoft Azure TTS (free tier), Google TTS (free tier), pyttsx3 (offline, robotic) | ElevenLabs (high quality, paid), Play.ht |
| **Video Assembly** | **FFmpeg** (free) — combine TTS audio + screen recordings + title cards | Adobe Premiere API, Cloudinary |
| **AI Avatars (talking head)** | None truly free | HeyGen, D-ID, Synthesia (all paid) |
| **Animations/Code Visuals** | **Manim** (free, math/code animations), **Remotion** (free, React-based video) | — |
| **Subtitles/Captions** | Whisper (local, free), FFmpeg burn-in | AWS Transcribe, Azure Speech |

---

## 4. Recommended Agent Pipeline (New Order)

1. **Topic Researcher** (Enhanced) — web + YouTube + blog research
2. **Curriculum Designer** (Existing) — basic → advanced structure
3. **Script Writer** (Enhanced) — write scripts *with* code blocks marked for execution
4. **Code Execution Agent** (NEW) — run code in sandbox, capture video/screenshots
5. **Video Planner / Generator** (Enhanced) — TTS voiceover + assemble video segments
6. **Human Review** — you approve the generated videos
7. **YouTube Uploader** — metadata + optional API upload

---

## 5. Subscriptions & APIs You Might Need

### Absolutely Free Tier Available

| Service | Free Tier | Limit |
|---------|-----------|-------|
| **Ollama (local LLM)** | 100% free | Your hardware limits |
| **YouTube Data API v3** | Free | 10,000 units/day |
| **Edge-TTS** | Free | Unlimited (Microsoft) |
| **FFmpeg** | Free | No limit |
| **E2B Code Sandbox** | Free tier | Limited execution minutes |
| **DuckDuckGo search** | Free (scraping) | Rate-limited |
| **feedparser (RSS)** | Free | No limit |

### Likely Paid (for quality video)

| Service | Why | Approx Cost |
|---------|-----|-------------|
| **ElevenLabs TTS** | Human-like voiceover | $5–$22/month |
| **HeyGen / D-ID** | AI talking-head avatar | $29–$199/month |
| **Serper.dev / Tavily** | Reliable web search (no scraping blocks) | $0–$50/month |
| **Cloud video rendering** | FFmpeg on cloud if local too slow | $0.01–$0.10/min |

---

## 6. Can This Be Done 100% Free Without You Recording?

### Honest Answer: Partially, but with major compromises.

| Task | Free Without Your Recording? | Reality |
|------|------------------------------|---------|
| Research & scripting | ✅ Yes | Ollama + free search works |
| Code execution + capture | ⚠️ Mostly | Local Docker + FFmpeg can record terminal, but setting it up reliably is complex |
| AI voiceover | ✅ Yes | Edge-TTS or pyttsx3 (robotic but free) |
| AI talking-head avatar | ❌ No | HeyGen/D-ID/Synthesia all require paid plans |
| Full video assembly | ✅ Yes | FFmpeg can combine audio + screen recordings |
| YouTube upload | ✅ Yes | YouTube API is free |

### The Bottleneck
**AI-generated video without any human recording is hard to do completely free.** Specifically:
- **Talking head:** No free high-quality AI avatar service exists.
- **Screen recording automation:** Requires significant custom coding (FFmpeg + Playwright + window management) to reliably capture code execution.
- **Video quality:** Free TTS (pyttsx3) sounds robotic; Edge-TTS is better but still not studio-quality.

### Realistic "Free-ish" Stack

If you want to minimize spending:

```
Research:   Ollama + DuckDuckGo + YouTube API (free)
Script:     Ollama (free)
Code run:   Local Docker + FFmpeg screen capture (free)
Voice:      Edge-TTS (free)
Assembly:   FFmpeg (free)
Upload:     YouTube API (free)
```

**Estimated cost: $0/month** — but you'll spend significant time building the automation pipeline.

---

## 7. Agents You Should Build (Priority Order)

```
Phase 1 (Immediate)
├── Enhanced Topic Researcher (web + YouTube + blogs)
├── Code Execution & Capture Agent (sandbox + FFmpeg recording)
└── Enhanced Video Planner (TTS + FFmpeg assembly)

Phase 2 (Later)
├── AI Avatar Integration (paid API or local SadTalker/Wav2Lip)
├── Multi-language support
└── Batch topic processing
```

---

## 8. Immediate Next Steps (Plan Only)

1. **Decide your budget:** $0/month vs. $30–$50/month for better voice/video quality.
2. **Choose code sandbox:** Local Docker (free, complex setup) vs. E2B (free tier, easier).
3. **Choose TTS:** Edge-TTS (free, good quality) vs. ElevenLabs (paid, best quality).
4. **Build the Code Execution Agent first** — this is the hardest part and determines if your "no manual recording" vision works.
5. **Prototype one video end-to-end** with "Strings in Java" before scaling to more topics.

---

## ⚠️ Limitations to Be Aware Of

- **Java execution:** Requires JDK installation in sandbox; more complex than Python.
- **Screen recording on Linux headless:** Requires Xvfb (virtual display) + FFmpeg; not trivial.
- **YouTube automation:** YouTube may flag fully AI-generated channels; manual review recommended.
- **Legal:** Scraping blogs/YouTube may violate ToS; use APIs where possible.

**Would you like me to proceed to Act mode and build the Enhanced Topic Research Agent and Code Execution Agent first?** Or would you like to refine the plan further?