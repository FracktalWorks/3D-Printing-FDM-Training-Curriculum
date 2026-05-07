# Generate Curriculum — Directive

## Goal
Generate or regenerate the complete 3D printing fresher training curriculum as Markdown files
inside `curriculum/`. Each module gets its own `README.md` with full training content,
YouTube video references, and further reading links.

## When to Use
- User asks to "generate the curriculum" or "create all training docs"
- User wants to rebuild the docs from scratch
- A module is missing or outdated

## Curriculum Map

| Folder | Module | Key Topics |
|--------|--------|-----------|
| `00-introduction/` | Introduction to 3D Printing | Technologies, applications, learning path |
| `01-electronics-basics/` | Electronics Basics | Boards, motors, drivers, PSU, thermistors, end stops |
| `02-mechanical-basics/` | Mechanical Basics | Frames, motion systems, hot ends, extruders, beds |
| `03-software-and-slicing/` | Software & Slicing | Cura, PrusaSlicer, firmware, G-code, modeling tools |
| `04-filaments-and-materials/` | Filaments & Materials | PLA, PETG, ABS, TPU, Nylon, storage |
| `05-printer-operations/` | Printer Operations | Assembly, bed leveling, calibration, E-steps, PID |
| `06-troubleshooting/` | Troubleshooting | Stringing, warping, layer shifts, clogs, adhesion |
| `07-advanced-topics/` | Advanced Topics | Klipper, multi-material, post-processing, DfAM |

## Execution

### Step 1: Run the generator script

```bash
python execution/generate_curriculum_docs.py --all
```

To generate a single module:
```bash
python execution/generate_curriculum_docs.py --module 01-electronics-basics
```

### Step 2: Enrich with YouTube Videos

For each module, run the YouTube fetch:
```bash
python execution/fetch_youtube_videos.py --topic "<module topic>" --max 8 --output .tmp/videos_<module>.json
```

Then embed the results into the module's README under `## 🎥 Recommended Videos`.

### Step 3: Update the curriculum index

After all modules are generated, ensure `curriculum/README.md` has an accurate table of contents
linking to each module.

## Required Document Structure (Per Module)

Every module README must contain these sections in order:

```markdown
# Module N: Title

> One-line description of what this module covers.

## 🎯 Learning Objectives
- Bullet list of what the fresher will be able to do after this module

## Prerequisites
- What the fresher should know before this module

## 1. Section Title
Content...

## 2. Section Title
Content...

## 🎥 Recommended Videos
| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Video Title](YouTube URL) | Channel Name | One-line reason |

## 📚 Further Reading
- [Resource Title](URL) — one-line description

## ✅ Knowledge Check
1. Question 1?
2. Question 2?
3. Question 3?

---
*Module N of 8 — [Back to Index](../README.md)*
```

## Quality Rules

- No spec or number without a source
- All acronyms defined on first use
- Beginner-friendly language — assume zero prior knowledge
- Every module must have ≥3 YouTube video references
- Every module must have ≥2 further reading links

## Edge Cases

- If `curriculum/` does not exist → create it before writing any files
- If a module folder does not exist → create it
- If an existing README already has good content → do NOT overwrite; enrich instead (see `update_curriculum.md`)

## Known Good Resources to Reference

- RepRap Wiki: https://reprap.org/wiki/RepRap
- Prusa Knowledge Base: https://help.prusa3d.com
- Klipper Docs: https://www.klipper3d.org/Overview.html
- Teaching Tech YouTube: https://www.youtube.com/@TeachingTech
- CNC Kitchen YouTube: https://www.youtube.com/@CNCKitchen
- Maker's Muse YouTube: https://www.youtube.com/@MakersMuse
