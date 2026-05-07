# Module 07: Advanced Topics

> Klipper deep dive, multi-material printing, post-processing techniques, and Design for Additive Manufacturing (DfAM).

![3D printer extruder cross-section — Klipper firmware provides advanced control over all extruder components including pressure advance and resonance compensation](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/3D_Printer_Extruder.svg/400px-3D_Printer_Extruder.svg.png)
*Klipper firmware controls every aspect of the extruder with precision: pressure advance compensates for filament compression, and input shaping cancels resonance vibrations measured by an ADXL345 accelerometer. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:3D_Printer_Extruder.svg), CC BY-SA 4.0*

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Configure and use Klipper's advanced features (input shaping, pressure advance)
- Understand how multi-material systems work (MMU, AMS, ERCF)
- Apply post-processing techniques (sanding, priming, painting, acetone smoothing)
- Apply DfAM (Design for Additive Manufacturing) principles to improve print success

## Prerequisites

- All previous modules (00–06)

---

## 1. Klipper — Advanced Configuration

Klipper (covered briefly in Module 03) runs on a Raspberry Pi and enables features impossible with Marlin on limited MCUs.

### 1.1 Installation Overview

```
Raspberry Pi (or SBC) → runs Klipper host + OctoPrint web UI
         ↕ USB serial
MCU (printer board)   → runs Klipper firmware (step generation only)
```

**Klipper Stack**:
- **Klipper**: Core firmware — runs on Pi
- **Moonraker**: REST API layer
- **OctoPrint**: Web interface (browser-based printer control)
- **KIAUH**: Easy installer script ([github.com/dw-0/kiauh](https://github.com/dw-0/kiauh))

### 1.2 printer.cfg Basics

Klipper is configured via a single human-readable file — no recompiling.

```ini
[printer]
kinematics: cartesian
max_velocity: 300
max_accel: 3000

[stepper_x]
step_pin: PC2
dir_pin: PB9
enable_pin: !PC3
microsteps: 16
rotation_distance: 40    # mm per revolution = belt_pitch × pulley_teeth = 2 × 20
endstop_pin: PA5
position_endstop: 0
position_max: 235

[extruder]
step_pin: PB4
dir_pin: PB3
enable_pin: !PC3
microsteps: 16
rotation_distance: 33.500  # calibrate this per extruder
nozzle_diameter: 0.400
filament_diameter: 1.750

[heater_bed]
heater_pin: PA15
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PC3
min_temp: 0
max_temp: 130
```

### 1.3 Input Shaping

**Input shaping** measures the printer's resonant frequencies using an accelerometer (ADXL345) and applies compensation to eliminate ringing without reducing print speed.

**Setup**:
1. Connect ADXL345 to Raspberry Pi SPI pins
2. Mount accelerometer to the toolhead
3. Run `SHAPER_CALIBRATE AXIS=X` and `SHAPER_CALIBRATE AXIS=Y`
4. Klipper measures resonances, fits a compensation filter (MZV, EI, 2HUMP_EI, etc.)
5. Save recommended values to `printer.cfg`

**Result**: Print speeds of 200–500 mm/s without ringing artefacts.

### 1.4 Pressure Advance

**Pressure advance** (equivalent to Marlin's Linear Advance) compensates for the pressure buildup in the hot end during direction changes, producing sharper corners and more consistent extrusion.

**Calibration**:
```gcode
SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500
TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005
```
Print a test pattern; find the layer height where corners are sharpest; calculate PA value.

Typical values: 0.02–0.08 for direct drive; 0.3–0.7 for Bowden.

### 1.5 Macros

Klipper's macro system lets you automate sequences:

```ini
[gcode_macro PARK]
gcode:
  {% set th = printer.toolhead %}
  G0 X{th.axis_maximum.x//2} Y{th.axis_maximum.y - 2} F6000

[gcode_macro LOAD_FILAMENT]
gcode:
  M83
  G1 E50 F300   ; Push 50mm at 300mm/min
  G1 E25 F150   ; Slow push to prime nozzle
  M82
```

---

## 2. Multi-Material Printing

Printing with more than one filament colour or material in a single print.

### 2.1 How It Works

Multi-material systems use a **filament switching mechanism** that:
1. Retracts the current filament back out of the hot end
2. Loads the new filament
3. Purges old material before resuming

**The challenge**: The purge volume (waste) is significant — colour changes require purging the entire hot end volume.

### 2.2 Systems Comparison

| System | Printer | Type | Filaments | Purge Method |
|--------|---------|------|----------|-------------|
| **Twin Dragon IDEX (Fracktal)** | Twin Dragon | Independent Dual Extrusion (IDEX) | 2 | No purge (T1 parks) |
| **ERCF (Enraged Rabbit)** | Any Klipper printer | DIY filament changer | Up to 12 | Purge tower / wipe |
| **Toolchanger (Tapchanger)** | Custom / Voron | Multiple toolheads | Unlimited | No purge needed |

### 2.3 Purge Tower

Most multi-material systems generate a **purge tower** (a solid block printed to flush old material out of the nozzle before resuming the actual print).

- Purge volume depends on colour change (dark → light = more purge needed)
- Purge towers waste significant filament — budget 10–30% extra per print

### 2.4 Water-Soluble Support Interface (PVA / BVOH)

With dual-material printing, you can print supports in **PVA (Polyvinyl Alcohol)** or **BVOH**:
- PVA dissolves completely in warm water
- The main part is unaffected
- Enables perfectly clean surfaces on support interfaces

---

## 3. Post-Processing Techniques

The part coming off the printer is just the starting point. Post-processing unlocks a professional finish.

### 3.1 Support Removal

- Use flush cutters for Bowden-style supports near surfaces
- Use needle-nose pliers for tree supports
- **Support interface layers** (Fracktory/Cura) create a weak bond — easier removal with cleaner surfaces

### 3.2 Sanding

1. Start with **120 grit** — remove layer lines
2. Progress to **220 grit** — smooth out scratches
3. **400–600 grit** — near-smooth surface
4. **1000–2000 grit** — ultra-smooth surface for painting

**Wet sanding** (with water) reduces clogging of sandpaper and produces better results on plastic.

### 3.3 Priming & Painting

1. Apply **2–3 thin coats** of plastic-compatible spray primer (Rust-Oleum, Tamiya)
2. Sand lightly with 400 grit between coats
3. Apply **acrylic or enamel paints** — brush or spray
4. Seal with **clear coat** (matte, satin, or gloss)

### 3.4 Acetone Smoothing (ABS Only)

ABS dissolves in acetone. Two methods:

**Brush method**: Dip a brush in acetone and brush over the surface. Surface softens and self-levels.

**Vapour smoothing**:
1. Pour a small amount of acetone into a sealed container (metal pot or glass jar)
2. Place part on a raised platform inside
3. Seal the container and wait 5–15 minutes
4. The acetone vapour dissolves the surface uniformly — dramatic smoothing

> ⚠️ Acetone is highly flammable. No open flames near the process. Work in a ventilated area. Use glass or metal containers only.

### 3.5 Epoxy Coating (XTC-3D)

**XTC-3D** (Smooth-On) is a two-part epoxy that brushes onto any FDM print:
- Self-levels and fills layer lines
- Hard, durable finish
- Works on PLA, PETG, ABS
- Mix ratio: 2A:1B by volume

### 3.6 UV Resin Coating

Thin layer of UV resin brushed onto the surface, cured with a UV lamp. Very smooth finish; seals the part.

---

## 4. Design for Additive Manufacturing (DfAM)

DfAM means designing parts specifically to work well with 3D printing — leveraging its strengths and avoiding its weaknesses.

### 4.1 Layer Orientation Matters

FDM parts are **weakest in Z** (between layers, not within them). Design critical load paths perpendicular to Z when possible.

```
Part under tension in Z:   ████   (weak — load is pulling layers apart)
                           ████
Part under tension in X/Y: ████████  (strong — load is within layers)
```

### 4.2 Overhang Rules

- **<45°** from vertical: Prints without supports
- **>45°** from vertical: Needs supports or design changes

**Design tricks to avoid supports**:
- **Chamfers** instead of sharp undercuts
- **Bridging** (horizontal spans up to 50mm can print without support)
- **Tear-drop holes** (rotate holes 45° — teardrop shape instead of circle) for better roundness on horizontal holes

### 4.3 Wall Thickness & Infill

- **Minimum wall thickness**: 2× nozzle diameter = 0.8mm (for 0.4mm nozzle)
- **Recommended functional wall**: 3–4 perimeters = 1.2–1.6mm
- **No infill is often fine**: Well-designed thin-shell parts can be stronger than thickly infilled parts of the same weight

### 4.4 Tolerance & Fit

FDM parts shrink slightly as they cool. For mating parts:

| Fit Type | Clearance |
|---------|---------|
| **Tight press fit** | 0.0–0.1mm |
| **Light press fit** | 0.1–0.2mm |
| **Slip fit (moves freely)** | 0.2–0.4mm |
| **Loose fit** | 0.4–0.6mm |

> Always print test tokens before printing final assemblies. Tolerances vary by printer, material, and slicer settings.

### 4.5 Fasteners

- **Heat-set inserts**: Brass threaded inserts melted into print for reusable metal threads — much stronger than threading directly into plastic
- **Captured nuts**: Design pockets for standard M3/M4 hex nuts — simple and effective
- **Self-tapping screws**: Work into PLA/PETG; strip easily in ABS

---

## 5. Print Farm Basics

A **print farm** is multiple printers running simultaneously for production-scale output.

### Key Concepts

- **OctoPrint**: Network management and monitoring of printers
- **Octoeverywhere / Obico**: Remote monitoring, print failure detection
- **Slicer queuing**: Slice once, send to multiple printers
- **Quality control**: Every part off the farm gets a dimensional check and visual inspection
- **Filament management**: Consistent filament drying and tracking across all machines

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Klipper Guide: Input Shaping, Pressure Advance and Macros](https://www.youtube.com/watch?v=EJapxNsntsQ) | YouTube | Complete Klipper tuning guide — covers the three key advanced features |
| [Klipper Input Shaping — A Leap Forward in Speed AND Quality](https://www.youtube.com/watch?v=er7q-CJL1lc) | YouTube | Deep technical explanation of resonance compensation and its impact |
| [Klipper Configuration: Input Shaper and Pressure Advance](https://www.youtube.com/watch?v=KFHxF8JYLsg) | YouTube | Step-by-step configuration walkthrough for both features |
| [How to Convert to Klipper Firmware — Step by Step](https://www.youtube.com/watch?v=Cj7KpzbgExQ) | YouTube | Full migration guide from Marlin to Klipper |
| [Input Shaping Made Easy with a USB Accelerometer!](https://www.youtube.com/watch?v=aHQju3e2guE) | YouTube | Practical hands-on guide to running input shaping with an ADXL345 |

---

## 📚 Further Reading & Forums

- [Klipper3D — Resonance Compensation (Official Docs)](https://www.klipper3d.org/Resonance_Compensation.html) — Official Klipper documentation for input shaping setup
- [Klipper3D — Full Documentation Overview](https://www.klipper3d.org/Overview.html) — Starting point for all Klipper configuration and features
- [All3DP — Klipper Input Shaping: Simply Explained](https://all3dp.com/2/klipper-input-shaping-simply-explained/) — Accessible explanation of resonance compensation for beginners
- [Obico — Klipper Input Shaping for Ender 3](https://www.obico.io/blog/klipper-input-shaping-ender-3/) — Practical Ender 3 walkthrough for input shaping
- [Sovol3D — Input Shaping vs Pressure Advance: When to Use Each](https://www.sovol3d.com/blogs/news/input-shaping-vs-pressure-advance-when-to-use-each-method) — Explains the difference and when each feature matters
- [r/klippers — How exactly does Klipper improve prints? (Forum)](https://www.reddit.com/r/klippers/comments/17f0b32/how_exactly_does_klipper_improve_prints_without/) — Community Q&A explaining Klipper benefits in plain language

---

## ✅ Knowledge Check

1. What are the two key Klipper features that allow printing at speeds of 300+ mm/s without quality loss?
2. Why do multi-material prints require a purge tower, and what determines how large it needs to be?
3. You're designing a bracket that will be loaded in tension. Should the load run in the Z direction or XY direction? Why?
4. What is the maximum overhang angle that typically prints without supports?
5. Describe two post-processing techniques to achieve a smooth surface on a PLA print.
6. What are heat-set inserts and why are they better than threading screws directly into plastic?

---

*[← Troubleshooting](../04-troubleshooting/README.md) | [Section Index](./README.md) | [🏠 Curriculum Index](../../README.md)*
