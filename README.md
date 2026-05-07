# 3D Printing Fresher Training Curriculum

> **Fracktal Works** — Full-Stack 3D Printing Training for Freshers
> Covers electronics fundamentals, mechanical basics, and all 3D-printing-specific skills from zero to confident operator.
> Machines: **Snowflake**, **Julia**, **Dragon**, **Twin Dragon**
> Tools: **Fracktory slicer**, **OctoPrint**, **Klipper**, **Cirkit Designer**

---

## Quick Start

```
1. Open curriculum/00-introduction/ and read introduction.md
2. Work through modules in order — do not skip
3. Complete hands-on exercises before marking a module done
4. Test yourself with the knowledge check at the end of each module
```

---

## Curriculum Structure

```
curriculum/
├── 00-introduction/          ←  What is 3D printing? Technologies overview
├── 01-electronics-basics/    ←  Electronics FUNDAMENTALS (PSU, boards, wiring)
├── 02-mechanical-basics/     ←  Mechanical FUNDAMENTALS (frame, motion, hotend)
├── 03-3d-printing/           ←  ALL 3D PRINTING topics (slicing → advanced)
│   ├── 01-software-and-slicing/
│   ├── 02-filaments-and-materials/
│   ├── 03-printer-operations/
│   ├── 04-troubleshooting/
│   └── 05-advanced-topics/
├── machines/                 ←  Quick-reference cards per printer
├── manuals/                  ←  Step-by-step printer-specific manuals
└── resources/                ←  Videos, links, G-code reference
```

---

## Section Overview

### Section 00 — Introduction

| File | Content | Time |
|------|---------|------|
| [00-introduction/README.md](curriculum/00-introduction/README.md) | Module index | — |
| [00-introduction/introduction.md](curriculum/00-introduction/introduction.md) | Technologies, workflow, applications, glossary | ~2h |

---

### Section 01 — Electronics Basics

> General electronics knowledge needed to work with any FDM printer.

| File | Content | Time |
|------|---------|------|
| [01-electronics-basics/README.md](curriculum/01-electronics-basics/README.md) | Module index | — |
| [01-electronics-basics/electronics.md](curriculum/01-electronics-basics/electronics.md) | Multimeter, soldering, connectors, PSU, stepper motors, MKS Eagle & Manta M8P boards, CAN bus, Cirkit Designer | ~5h |

**Key topics:** multimeter use · soldering & crimping · JST/Dupont/XT60 connectors · 24V PSU · stepper drivers (TMC2209, TMC5160) · MKS Eagle V1.0 (Snowflake) · Manta M8P V2.0 (Dragon, Twin Dragon) · CAN bus architecture

---

### Section 02 — Mechanical Basics

> General mechanics knowledge needed to assemble and maintain any FDM printer.

| File | Content | Time |
|------|---------|------|
| [02-mechanical-basics/README.md](curriculum/02-mechanical-basics/README.md) | Module index | — |
| [02-mechanical-basics/mechanical.md](curriculum/02-mechanical-basics/mechanical.md) | Tools, fasteners, frame, linear motion, hotend, extruder, maintenance | ~4h |

**Key topics:** hex keys · calipers · M3/M4/M5 fasteners · aluminium extrusion · MGN linear rails · lead screws · GT2 belts · CoreXY kinematics · hotend anatomy · Bowden vs direct drive

---

### Section 03 — 3D Printing

> All 3D-printing-specific skills, organized by topic.

| Module | File | Content | Time |
|--------|------|---------|------|
| Software & Slicing | [03-3d-printing/01-software-and-slicing/](curriculum/03-3d-printing/01-software-and-slicing/README.md) | Fracktory slicer, parameters, firmware, G-code, modeling tools | ~4h |
| Filaments & Materials | [03-3d-printing/02-filaments-and-materials/](curriculum/03-3d-printing/02-filaments-and-materials/README.md) | PLA, PETG, ABS, TPU, Nylon, eSUN specs, storage | ~3h |
| Printer Operations | [03-3d-printing/03-printer-operations/](curriculum/03-3d-printing/03-printer-operations/README.md) | Assembly, bed leveling, E-steps, flow, PID, OctoPrint, Wi-Fi printing | ~5h+5h |
| Troubleshooting | [03-3d-printing/04-troubleshooting/](curriculum/03-3d-printing/04-troubleshooting/README.md) | Diagnostics, 10 common failures, machine-specific fixes | ~4h |
| Advanced Topics | [03-3d-printing/05-advanced-topics/](curriculum/03-3d-printing/05-advanced-topics/README.md) | Klipper advanced, input shaping, pressure advance, DfAM | ~6h |

**Total Section 03: ~27 hours**

---

## Machine Quick-Reference Cards

> Keep these open whenever working on a specific printer.

| Machine | Motion | Build Volume | Firmware | Board | Quick Ref |
|---------|--------|-------------|---------|-------|-----------|
| **Snowflake** | CoreXY | 200×200×200 mm | Marlin | MKS Eagle V1.0 | [SNOWFLAKE-QUICK-REF.md](curriculum/machines/SNOWFLAKE-QUICK-REF.md) |
| **Julia** | CoreXY | 250×250×250 mm | Marlin | MKS Robin Nano V3 | [JULIA-QUICK-REF.md](curriculum/machines/JULIA-QUICK-REF.md) |
| **Dragon** | CoreXY | 400×300×400 mm | Klipper | Manta M8P V2.0 | [DRAGON-QUICK-REF.md](curriculum/machines/DRAGON-QUICK-REF.md) |
| **Twin Dragon** | CoreXY + IDEX | 300×300×350 mm | Klipper | Manta M8P V2.0 | [TWIN-DRAGON-QUICK-REF.md](curriculum/machines/TWIN-DRAGON-QUICK-REF.md) |

---

## Printer Manuals

> Step-by-step operational guides per machine.

| Machine | Manual |
|---------|--------|
| Snowflake | [manuals/snowflake/](curriculum/manuals/snowflake/README.md) |
| Julia | [manuals/julia/](curriculum/manuals/julia/README.md) |
| Dragon | [manuals/dragon/](curriculum/manuals/dragon/README.md) |
| Twin Dragon | [manuals/twin-dragon/](curriculum/manuals/twin-dragon/README.md) |
| Fracktory Slicer | [manuals/fracktory/](curriculum/manuals/fracktory/README.md) |

---

## Resource Library

| Resource | What's Inside |
|----------|--------------|
| [resources/videos.md](curriculum/resources/videos.md) | Curated YouTube videos organized by module and topic |
| [resources/links.md](curriculum/resources/links.md) | Datasheets, documentation, wikis, and written guides |
| [resources/GCODE-REFERENCE.md](curriculum/resources/GCODE-REFERENCE.md) | Quick reference for all Klipper and Marlin G-code / M-code commands |

---

## Skill Pillar Map

```
┌───────────────────────────────────────────────────────────────────┐
│                    LEARNING PATH                                 │
│                                                                  │
│  00-introduction   ←  Start here. No prior knowledge needed.    │
│         ↓                                                        │
│  01-electronics    ←  How the printer’s electronics work         │
│         ↓                                                        │
│  02-mechanical     ←  How the printer moves                      │
│         ↓                                                        │
│  03-3d-printing    ←  Everything 3D-printing-specific            │
│    ├── software-and-slicing   (prepare your files)               │
│    ├── filaments-and-materials (choose your material)            │
│    ├── printer-operations     (run and calibrate)                │
│    ├── troubleshooting        (diagnose and fix)                 │
│    └── advanced-topics        (Klipper, DfAM, multi-material)   │
└───────────────────────────────────────────────────────────────────┘
```

---

## Learning Paths by Role

| Role | Recommended Modules | Skip |
|------|---------------------|------|
| **Operator (print jobs only)** | Intro → Filaments → Operations → Troubleshooting | Electronics, Mechanical, Advanced |
| **Technician (maintenance + repair)** | All modules | Nothing |
| **Firmware Engineer** | Electronics → Software → Advanced | Filaments |
| **New Fresher (all-round)** | Complete in order (00 → 03-advanced) | Nothing |

---

## Estimated Total Time

| Section | Time |
|---------|------|
| 00 — Introduction | ~2h |
| 01 — Electronics Basics | ~5h |
| 02 — Mechanical Basics | ~4h |
| 03 — 3D Printing (all 5 modules) | ~27h |
| **Total** | **~38 hours** |

---

## Safety Reference

> Read before operating any machine.

- [00-introduction/SAFETY-QUICK-REFERENCE.md](curriculum/00-introduction/SAFETY-QUICK-REFERENCE.md) — Electrical, thermal, mechanical, fire, and chemical safety rules + emergency procedures

---

*Maintained by Fracktal Works | support@fracktal.in*


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
