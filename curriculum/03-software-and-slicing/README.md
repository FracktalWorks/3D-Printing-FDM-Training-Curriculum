# Module 03: Software & Slicing

> How to convert a 3D model into printer instructions — slicer software, key parameters, firmware, G-code basics, and 3D modeling tools.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Explain what a slicer does and slice a model using Fracktory
- Define and adjust the most critical slicer parameters
- Understand the role of firmware (Marlin vs Klipper)
- Read and interpret basic G-code commands
- Name the main 3D modeling tools and their appropriate use cases

## Prerequisites

- Module 00: Introduction to 3D Printing

---

## 1. The Software Stack

The software stack for 3D printing:

```
CAD / Modeling Tool          →  3D model file (.stl, .3mf, .obj)
Slicer Software              →  G-code file (.gcode, .bgcode)
Firmware (on the printer)    →  Executes G-code → physical print
```

Each layer does a distinct job. You will interact primarily with the slicer.

---

## 2. Slicer Software

A **slicer** takes a 3D model and slices it into horizontal layers, generating the toolpaths and settings the printer follows.

### 2.1 Cura (by Ultimaker / UltiMaker)

**Free and open-source.** The most widely used slicer globally.

- Supports hundreds of printers via printer profiles
- Beginner-friendly UI with "Recommended" and "Custom" modes
- Plugin marketplace for extensions
- Download: [ultimaker.com/software/ultimaker-cura](https://ultimaker.com/software/ultimaker-cura/)

### 2.2 Fracktory (by Fracktal Works) — **Primary Slicer**

**Free.** Built on the Ultimaker Cura open-source base. This is the official slicer for all Fracktal Works machines.

- Pre-configured machine profiles for Snowflake, Dragon, and Twin Dragon
- Wi-Fi printing directly from slicer to printer
- Cura-based plugin ecosystem
- Nozzle size selection: 0.25 mm, 0.4 mm, 0.6 mm, 0.8 mm
- Windows (Vista+, 64-bit), macOS (10.11+), Linux (Ubuntu 14.04+)
- **Download**: [printers.fracktory.in/download](http://printers.fracktory.in/download)
- **Support**: support@fracktal.in / https://care.fracktal.in

---

## 3. Key Slicer Parameters

Understanding these parameters is the most critical skill for a 3D printer operator.

### 3.1 Layer Height

**What it is**: The thickness of each printed layer.

| Layer Height | Print Time | Surface Quality | Strength |
|-------------|-----------|----------------|---------|
| 0.1 mm | Very slow | Excellent | Good |
| **0.2 mm** | Standard | Good | Standard |
| 0.3 mm | Faster | Visible layers | Good |
| 0.4 mm | Fast | Rough | Good |

> Rule of thumb: layer height should be 25–80% of nozzle diameter. For a 0.4mm nozzle: 0.1–0.32mm practical range.

### 3.2 Infill

**What it is**: The internal structure of the print (the pattern and density of material inside the solid outer walls).

**Infill density**: 0% = hollow, 100% = solid

| Density | Use Case |
|---------|---------|
| 0–5% | Display models, lightweight |
| 10–20% | General purpose, decorative |
| 30–50% | Functional parts, good strength |
| 70–100% | Maximum strength, very slow |

**Infill patterns**: 
- **Lines**: Fastest, weakest in Z
- **Grid**: Balanced — good default
- **Gyroid**: Isotropic (equal strength in all directions) — best for flexible or structural parts
- **Lightning**: Ultra-fast, only provides surface support — for quick visual models

### 3.3 Print Speed

Speed is in mm/s. Higher speed = faster print, but potentially lower quality.

| Setting | Typical Range | Notes |
|---------|-------------|-------|
| Outer wall speed | 25–80 mm/s | Slower = better surface quality |
| Infill speed | 50–200 mm/s | Can be faster; quality less critical |
| Travel speed | 150–300 mm/s | Not printing — move fast |
| Max acceleration | 500–20,000 mm/s² | Depends on kinematics and tuning |

> **Input shaping** (Klipper, Module 07) allows much higher speeds by compensating for vibration-induced ringing.

### 3.4 Temperature

| Material | Hot End Temp | Bed Temp |
|---------|-------------|---------|
| PLA | 190–220°C | 50–60°C (or 0°C) |
| PETG | 230–250°C | 70–85°C |
| ABS | 230–250°C | 100–110°C |
| TPU | 220–240°C | 30–60°C |
| Nylon | 240–260°C | 70–90°C |

### 3.5 Cooling

**Part cooling fan speed** controls how fast deposited material solidifies.

- **PLA**: 100% cooling — benefits greatly from fast cooling
- **PETG**: 30–50% — too much cooling causes layer delamination
- **ABS/ASA**: 0% or minimal — prevents warping; needs enclosure
- **TPU**: 30–50%

### 3.6 Retraction

**What it is**: Pulling filament back into the nozzle during travel moves to prevent oozing.

| Setting | Bowden | Direct Drive |
|---------|--------|------------|
| Retraction distance | 4–8 mm | 0.5–2 mm |
| Retraction speed | 40–60 mm/s | 25–45 mm/s |

Over-retraction causes **grinding** (the extruder chews through the filament) or **clogs**.

### 3.7 Supports

Supports are temporary structures printed beneath overhangs ≥45–60°.

| Support Type | Best For |
|-------------|---------|
| **Normal/linear** | Simple overhangs |
| **Tree supports** | Complex geometry, touching supports |
| **Organic supports** (Cura/Fracktory) | Minimal contact, easiest removal |
| **Paintable supports** | Manually select exactly where supports go |

### 3.8 First Layer Settings

The first layer is the most critical. Key first-layer settings:
- **First layer height**: 0.2–0.3 mm (slightly thicker to squish into bed)
- **First layer speed**: 20–30 mm/s (slower for adhesion)
- **First layer fan**: OFF (no cooling — let it bond to bed)

---

## 4. Firmware

**Firmware** is the software that runs on the printer's control board. It:
- Receives G-code commands
- Controls stepper motors, heaters, fans, and sensors in real time
- Implements safety features (thermal runaway protection)

### 4.1 Marlin

**The most widely deployed 3D printer firmware.** Open-source (GPL), runs on AVR (Arduino Mega) and ARM (STM32) processors.

- Configuration is done by editing `Configuration.h` and `Configuration_adv.h` and recompiling
- Runs directly on the printer's MCU
- Used by: Creality, Anycubic, and hundreds of other brands
- Docs: [marlinfw.org](https://marlinfw.org)

### 4.2 Klipper

**The modern high-performance alternative.** Runs on a Raspberry Pi (or similar SBC) and offloads computations to the SBC, leaving the MCU only for real-time step generation.

Key advantages over Marlin:
- Configuration via human-readable `printer.cfg` text file (no recompiling)
- **Input shaping**: Accelerometer-based vibration compensation for higher speeds
- **Pressure advance**: Firmware-level retraction compensation for clean corners
- **Macro system**: Python-like scripting for advanced automation
- Docs: [klipper3d.org](https://www.klipper3d.org)

### 4.3 RepRapFirmware (RRF)

Used primarily by Duet boards. Feature-rich, CAN-bus support for modular toolheads. Popular for professional and large-format machines.

---

## 5. G-code Basics

**G-code** is the language printers speak. The slicer generates it; the firmware executes it.

### Essential Commands

| Command | Meaning | Example |
|---------|---------|---------|
| `G0` | Rapid move (no extrusion) | `G0 X10 Y20 F3000` |
| `G1` | Linear move (with extrusion) | `G1 X50 Y50 E1.5 F1800` |
| `G28` | Home all axes | `G28` |
| `G29` | Auto bed levelling probe | `G29` |
| `G92` | Set position | `G92 E0` (reset extruder position) |
| `M104` | Set hot end temp (no wait) | `M104 S200` |
| `M109` | Set hot end temp (wait) | `M109 S215` |
| `M140` | Set bed temp (no wait) | `M140 S60` |
| `M190` | Set bed temp (wait) | `M190 S60` |
| `M106` | Set fan speed | `M106 S255` (full speed) |
| `M107` | Fan off | `M107` |
| `M503` | Report EEPROM settings | `M503` |

### Start G-code Example (Typical)

```gcode
G28          ; Home all axes
G29          ; Auto bed levelling
G92 E0       ; Reset extruder
G1 Z2.0 F3000  ; Move nozzle up
G1 X0.1 Y20 Z0.3 F5000  ; Move to purge start
G1 X0.1 Y200 E15 F1500  ; Draw purge line
G92 E0       ; Reset extruder after purge
```

---

## 6. 3D Modeling Tools

| Tool | Level | Cost | Best For |
|------|-------|------|---------|
| **Tinkercad** | Beginner | Free | Simple shapes, quick edits, educational |
| **Fusion 360** | Intermediate | Free (personal) | Parametric engineering parts |
| **FreeCAD** | Intermediate | Free | Open-source parametric CAD |
| **Onshape** | Intermediate | Free (public) | Cloud-based parametric CAD |
| **SolidWorks** | Advanced | Paid | Industry-standard mechanical CAD |
| **Blender** | Intermediate | Free | Organic shapes, art, sculpting |
| **OpenSCAD** | Intermediate | Free | Code-based parametric modeling |

### Repair Tools

Sometimes STL files from the internet have errors (non-manifold geometry, holes). Repair tools:
- **Fracktory/Cura**: Built-in repair (powered by Netfabb)
- **Meshmixer**: Free, powerful mesh repair and hollowing
- **Netfabb** (online): [netfabb.autodesk.com](https://netfabb.autodesk.com)

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Model File to 3D Print — Beginner's Guide to Using Cura](https://www.youtube.com/watch?v=e-lQPGJ3Psc) | YouTube | Full workflow from STL file to print-ready G-code in Cura |
| [Cura 3D Slicer for Beginners — In-Depth Tutorial](https://www.youtube.com/watch?v=9Ja9utWCKWA) | YouTube | Every important Cura setting explained step-by-step |
| [Fracktory Slicer Quick Setup](https://www.youtube.com/results?search_query=fracktory+slicer+fracktal+works) | YouTube | Fracktory slicer setup and profile workflow for Fracktal machines |

---

## 📚 Further Reading & Forums

- [Fracktory Download & Documentation](http://printers.fracktory.in/download) — Official Fracktory slicer download and setup guide
- [Fracktal Works Support](https://care.fracktal.in) — Official support portal and knowledge base

---

## ✅ Knowledge Check

1. What is the practical layer height range for a 0.4mm nozzle, and what are the trade-offs of choosing 0.1mm vs 0.4mm?
2. What infill pattern would you choose for a part that needs equal strength in all directions?
3. Why does PETG need less part cooling than PLA?
4. What is the key advantage of Klipper over Marlin that makes it popular for high-speed printing?
5. Write the G-code command to heat the hot end to 210°C and wait for it to reach temperature.
6. A slicer shows retraction distance of 6mm. Is this likely Bowden or direct drive? Why?

---

*Module 03 of 8 — [← Mechanical Basics](../02-mechanical-basics/README.md) | [Next: Filaments & Materials →](../04-filaments-and-materials/README.md) | [Back to Index](../README.md)*
