# 3D Printing Training — Fresher Onboarding Repository

> Complete technical training for freshers joining a 3D printing (FDM) operations team.
> Covers electronics, mechanical, software, printer skills, operations, and troubleshooting.
> Machines: **Snowflake · Julia · Dragon · Twin Dragon**
> Tools: **Cirkit Designer · OctoPrint · Klipper · Fracktory · MKS Boards**

---

## 🚀 Start Here

New to the team? Start with the **[Curriculum Index](curriculum/README.md)** and work through modules in order.

No prior 3D printing knowledge required.

---

## 📚 Training Modules

| Module | Topic | Time |
|--------|-------|------|
| [Module 1 — Electronics](curriculum/module-1-electronics.md) | Multimeter, soldering, connectors, MKS boards | 5h |
| [Module 2 — Mechanical](curriculum/module-2-mechanical.md) | Tools, fasteners, motion systems, hotend | 4h |
| [Module 3 — Software](curriculum/module-3-software.md) | Git, GitHub, SSH, Linux, VS Code | 4h |
| [Module 4 — Printer Basics](curriculum/module-4-printer-basics.md) | FDM, machine specs, bed leveling, wiring | 5h |
| [Module 5 — Operations](curriculum/module-5-operations.md) | Slicing, OctoPrint, Klipper, drybox, Fracktory | 5h |
| [Module 6 — Troubleshooting](curriculum/module-6-troubleshooting.md) | Diagnostics, fault finding, machine fixes | 4h |
| [📹 Video Library](curriculum/resources/videos.md) | 64 curated YouTube videos by topic | — |

---

## Expected Learning Outcomes

After completing all 6 modules a fresher will be able to:

- ✅ Use a multimeter to test wiring, heaters, thermistors, and endstops
- ✅ Solder and crimp connectors to production standard
- ✅ Read and wire from a Cirkit Designer schematic
- ✅ Identify and replace mechanical components (belts, rails, nozzles, lead screws)
- ✅ Use Git/GitHub to track and manage printer configurations
- ✅ SSH into a Raspberry Pi, navigate Linux, and manage Klipper/OctoPrint
- ✅ Operate Snowflake, Julia, Dragon, and Twin Dragon independently
- ✅ Slice models in OrcaSlicer with correct settings for each material
- ✅ Run bed leveling, E-steps calibration, PID tuning, and pressure advance
- ✅ Diagnose and fix the 15 most common FDM print failures
- ✅ Log jobs and failures in Fracktory

---

## Prerequisites

- Basic computer literacy (file browser, web browser)
- Nothing else — all technical knowledge is taught from scratch

---

# 3D Printing Fresher Training Agent

A curriculum-authoring agent that generates, enriches, and maintains Markdown-based
training documents for freshers learning 3D printing — ready to host on GitHub.

## What This Agent Does

- **Generates structured training docs** across 8 curriculum modules
- **Searches YouTube** for curated tutorial videos embedded as references in each doc
- **Searches the web** for official docs, articles, and datasheets to cite
- **Maintains the curriculum** — update, extend, or add new modules on demand

## Curriculum Modules

| # | Module | Skills Covered |
|---|--------|---------------|
| 00 | Introduction | What is 3D printing, technologies, learning path |
| 01 | Electronics Basics | Boards, motors, drivers, PSU, wiring, sensors |
| 02 | Mechanical Basics | Frames, motion systems, hot ends, extruders |
| 03 | Software & Slicing | Cura, PrusaSlicer, firmware, G-code, modeling |
| 04 | Filaments & Materials | PLA, PETG, ABS, TPU, Nylon, storage |
| 05 | Printer Operations | Assembly, bed leveling, calibration, PID |
| 06 | Troubleshooting | Systematic debugging for all common issues |
| 07 | Advanced Topics | Klipper, multi-material, post-processing, DfAM |

## Quick Start

### 1. Clone and set up

```bash
git clone <this-repo>
cd 3d-printing-training-agent
```

**Windows:**
```powershell
.\setup.ps1
```

**Linux/macOS:**
```bash
chmod +x setup.sh && ./setup.sh
```

### 2. Configure API keys

```bash
cp .env.example .env
# Edit .env and fill in your API keys
```

| Key | Where to get it | Required? |
|-----|----------------|-----------|
| `YOUTUBE_API_KEY` | [Google Cloud Console](https://console.cloud.google.com) → YouTube Data API v3 | Yes (for video search) |
| `SERPAPI_KEY` | [SerpAPI](https://serpapi.com) | Optional |
| `OPENAI_API_KEY` | [OpenAI](https://platform.openai.com) | Optional |

### 3. Generate the full curriculum

```bash
python execution/generate_curriculum_docs.py --all
```

Or generate a single module:
```bash
python execution/generate_curriculum_docs.py --module 01-electronics-basics
```

### 4. Fetch YouTube references for a module

```bash
python execution/fetch_youtube_videos.py --topic "3D printer stepper motors" --max 10
```

---

## Using with GitHub Copilot (Recommended)

Open the workspace in VS Code. The agent is pre-configured. Ask Copilot:

- *"Generate the full 3D printing curriculum"*
- *"Find YouTube videos for the electronics module and embed them"*
- *"Create a new training doc on dual-extrusion printing"*
- *"Update the troubleshooting module with stringing fixes"*
- *"Search for resources on Klipper input shaping"*

---

## Publishing to GitHub

The `curriculum/` folder is self-contained and ready to push as a standalone repo:

```bash
cd curriculum
git init
git add .
git commit -m "Initial 3D printing training curriculum"
gh repo create 3d-printing-fresher-training --public --source=. --push
```

---

## Directory Structure

```
├── AGENTS.md                    ← Agent system prompt (read by Copilot)
├── README.md                    ← This file
├── requirements.txt             ← Python dependencies
├── .env.example                 ← Environment variable template
├── setup.ps1 / setup.sh        ← One-click setup scripts
├── directives/                  ← Agent SOPs
│   ├── generate_curriculum.md
│   ├── fetch_youtube_refs.md
│   ├── create_training_doc.md
│   └── update_curriculum.md
├── execution/                   ← Deterministic Python scripts
│   ├── generate_curriculum_docs.py
│   ├── fetch_youtube_videos.py
│   └── search_web_resources.py
└── curriculum/                  ← The training repo (push this to GitHub)
    ├── README.md
    ├── 00-introduction/
    ├── 01-electronics-basics/
    ├── 02-mechanical-basics/
    ├── 03-software-and-slicing/
    ├── 04-filaments-and-materials/
    ├── 05-printer-operations/
    ├── 06-troubleshooting/
    └── 07-advanced-topics/
```

---

## Contributing / Extending

To add a new module:
1. Ask the agent: *"Create a new training doc on [topic]"*
2. The agent reads `directives/create_training_doc.md` and writes the doc
3. It fetches YouTube videos and web references automatically
4. The new module is added to `curriculum/` and indexed in `curriculum/README.md`
