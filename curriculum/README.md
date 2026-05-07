# 3D Printing Fresher Training Curriculum

> **Fracktal Works** — Full-Stack 3D Printing Training for Freshers
> Covers electronics fundamentals, mechanical basics, and all 3D-printing-specific skills from zero to confident operator.
> Machines: **Snowflake**, **Julia**, **Dragon**, **Twin Dragon**
> Tools: **Fracktory slicer**, **OctoPrint**, **Klipper**, **Cirkit Designer**

---

## Quick Start

```
1. Read this README for a bird's eye view
2. Open 00-introduction/ and read introduction.md
3. Work through modules in order — do not skip
4. Complete hands-on exercises before marking a module done
5. Test yourself with the knowledge check at the end of each module
```

---

## Curriculum Structure

The curriculum is organized into **three sections** plus supporting references:

```
curriculum/
├── 00-introduction/          ← What is 3D printing? Technologies overview
├── 01-electronics-basics/    ← Electronics FUNDAMENTALS (PSU, boards, wiring)
├── 02-mechanical-basics/     ← Mechanical FUNDAMENTALS (frame, motion, hotend)
├── 03-3d-printing/           ← ALL 3D PRINTING topics (slicing → advanced)
│   ├── 01-software-and-slicing/
│   ├── 02-filaments-and-materials/
│   ├── 03-printer-operations/
│   ├── 04-troubleshooting/
│   └── 05-advanced-topics/
├── machines/                 ← Quick-reference cards per printer
├── manuals/                  ← Step-by-step printer-specific manuals
├── resources/                ← Videos, links, G-code reference
└── images/                   ← All images used in modules (see images/README.md)
```

---

## Section Overview

### Section 00 — Introduction

| File | Content | Time |
|------|---------|------|
| [00-introduction/README.md](00-introduction/README.md) | Module index | — |
| [00-introduction/introduction.md](00-introduction/introduction.md) | Technologies, workflow, applications, glossary | ~2h |

---

### Section 01 — Electronics Basics

> General electronics knowledge needed to work with any FDM printer.

| File | Content | Time |
|------|---------|------|
| [01-electronics-basics/README.md](01-electronics-basics/README.md) | Module index | — |
| [01-electronics-basics/electronics.md](01-electronics-basics/electronics.md) | Multimeter, soldering, connectors, PSU, stepper motors, MKS Eagle & Manta M8P boards, CAN bus, Cirkit Designer | ~5h |

**Key topics:** multimeter use · soldering & crimping · JST/Dupont/XT60 connectors · 24V PSU · stepper drivers (TMC2209, TMC5160) · MKS Eagle V1.0 (Snowflake) · Manta M8P V2.0 (Dragon, Twin Dragon) · CAN bus architecture

---

### Section 02 — Mechanical Basics

> General mechanics knowledge needed to assemble and maintain any FDM printer.

| File | Content | Time |
|------|---------|------|
| [02-mechanical-basics/README.md](02-mechanical-basics/README.md) | Module index | — |
| [02-mechanical-basics/mechanical.md](02-mechanical-basics/mechanical.md) | Tools, fasteners, frame, linear motion, hotend, extruder, maintenance | ~4h |

**Key topics:** hex keys · calipers · M3/M4/M5 fasteners · aluminium extrusion · MGN linear rails · lead screws · GT2 belts · CoreXY kinematics · hotend anatomy · Bowden vs direct drive

---

### Section 03 — 3D Printing

> All 3D-printing-specific skills, organized by topic.

| Module | File | Content | Time |
|--------|------|---------|------|
| Software & Slicing | [03-3d-printing/01-software-and-slicing/](03-3d-printing/01-software-and-slicing/README.md) | Fracktory slicer, parameters, firmware, G-code, modeling tools | ~4h |
| Filaments & Materials | [03-3d-printing/02-filaments-and-materials/](03-3d-printing/02-filaments-and-materials/README.md) | PLA, PETG, ABS, TPU, Nylon, eSUN specs, storage | ~3h |
| Printer Operations | [03-3d-printing/03-printer-operations/](03-3d-printing/03-printer-operations/README.md) | Assembly, bed leveling, E-steps, flow, PID, OctoPrint, Wi-Fi printing | ~5h+5h |
| Troubleshooting | [03-3d-printing/04-troubleshooting/](03-3d-printing/04-troubleshooting/README.md) | Diagnostics, 10 common failures, machine-specific fixes | ~4h |
| Advanced Topics | [03-3d-printing/05-advanced-topics/](03-3d-printing/05-advanced-topics/README.md) | Klipper advanced, input shaping, pressure advance, DfAM | ~6h |

**Total Section 03: ~27 hours**

---

## Machine Quick-Reference Cards

> Keep these open whenever working on a specific printer.

| Machine | Motion | Build Volume | Firmware | Board | Quick Ref |
|---------|--------|-------------|---------|-------|-----------|
| **Snowflake** | CoreXY | 200×200×200 mm | Marlin | MKS Eagle V1.0 | [SNOWFLAKE-QUICK-REF.md](machines/SNOWFLAKE-QUICK-REF.md) |
| **Julia** | CoreXY | 250×250×250 mm | Marlin | MKS Robin Nano V3 | [JULIA-QUICK-REF.md](machines/JULIA-QUICK-REF.md) |
| **Dragon** | CoreXY | 400×300×400 mm | Klipper | Manta M8P V2.0 | [DRAGON-QUICK-REF.md](machines/DRAGON-QUICK-REF.md) |
| **Twin Dragon** | CoreXY + IDEX | 300×300×350 mm | Klipper | Manta M8P V2.0 | [TWIN-DRAGON-QUICK-REF.md](machines/TWIN-DRAGON-QUICK-REF.md) |

---

## Printer Manuals

> Step-by-step operational guides per machine.

| Machine | Manual |
|---------|--------|
| Snowflake | [manuals/snowflake/](manuals/snowflake/README.md) |
| Julia | [manuals/julia/](manuals/julia/README.md) |
| Dragon | [manuals/dragon/](manuals/dragon/README.md) |
| Twin Dragon | [manuals/twin-dragon/](manuals/twin-dragon/README.md) |
| Fracktory Slicer | [manuals/fracktory/](manuals/fracktory/README.md) |

---

## Resource Library

| Resource | What's Inside |
|----------|--------------|
| [resources/videos.md](resources/videos.md) | 64 curated YouTube videos organized by module and topic |
| [resources/links.md](resources/links.md) | Datasheets, documentation, wikis, and written guides |
| [resources/GCODE-REFERENCE.md](resources/GCODE-REFERENCE.md) | Quick reference for all Klipper and Marlin G-code / M-code commands |

---

## Skill Pillar Map

```
┌─────────────────────────────────────────────────────────────────┐
│                    LEARNING PATH                                 │
│                                                                  │
│  00-introduction   ←  Start here. No prior knowledge needed.    │
│         ↓                                                        │
│  01-electronics    ←  How the printer's electronics work         │
│         ↓                                                        │
│  02-mechanical     ←  How the printer moves                      │
│         ↓                                                        │
│  03-3d-printing    ←  Everything 3D-printing-specific            │
│    ├── software-and-slicing   (prepare your files)               │
│    ├── filaments-and-materials (choose your material)            │
│    ├── printer-operations     (run and calibrate)                │
│    ├── troubleshooting        (diagnose and fix)                 │
│    └── advanced-topics        (Klipper, DfAM, multi-material)   │
└─────────────────────────────────────────────────────────────────┘
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

- [00-introduction/SAFETY-QUICK-REFERENCE.md](00-introduction/SAFETY-QUICK-REFERENCE.md) — Electrical, thermal, mechanical, fire, and chemical safety rules + emergency procedures

---

## How This Repo Is Organized

Every section folder follows the same pattern:

```
XX-section-name/
├── README.md          ← Short index: objectives, navigation, prerequisites
└── module-name.md     ← Full lesson content with images, exercises, quiz
```

The `README.md` is the **landing page** on GitHub — it shows learning objectives and links to the full content file. All actual lesson text lives in the `.md` content file.

Images are stored in `images/` with subdirectories per section.
See [images/README.md](images/README.md) for the complete image inventory and naming guide.

---

*Maintained by Fracktal Works | support@fracktal.in*
