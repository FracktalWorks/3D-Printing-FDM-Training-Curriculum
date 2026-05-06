# Module 02: Mechanical Basics for 3D Printing

> The physical structures, motion systems, and toolhead components that determine print quality and reliability.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Identify the major mechanical components of an FDM printer
- Compare Cartesian, CoreXY, and Delta kinematics
- Explain how belts, lead screws, and linear rails create motion
- Describe the hot end assembly and how filament is melted
- Differentiate Bowden and direct-drive extruder systems

## Prerequisites

- Module 00: Introduction to 3D Printing
- Module 01: Electronics Basics (recommended, not required)

---

## 1. Frame Types & Kinematics

The **kinematics** of a printer defines how it moves the toolhead relative to the bed to create the X, Y, and Z axes.

### 1.1 Cartesian (Bed-Slinger)

The most common configuration for budget printers. The **bed moves in Y**, the **toolhead moves in X**, and the **Z-axis lifts the gantry**.

```
         Gantry (X-axis)
    ← X-carriage (toolhead) →
         |
    [Build Plate] ←→ Y-axis
         |
    Z leadscrews (lift gantry)
```

**Examples**: Creality Ender 3, Prusa MK3S+, Anycubic Kobra

**Pros**: Simple, cheap, easy to maintain
**Cons**: Moving bed adds mass → limits print speed and quality at speed; tall/heavy prints can wobble (Y-axis inertia)

### 1.2 CoreXY

Both motors drive the toolhead in X and Y simultaneously. The bed only moves in Z (no bed inertia issues).

```
    Motor A + Motor B = X movement
    Motor A - Motor B = Y movement
```

**Examples**: Fracktal Snowflake, Dragon, Twin Dragon (all CoreXY)

**Pros**: High speed, no bed mass limitation, better print quality at speed
**Cons**: More complex belt path, belt tension matters more, harder to build/tune

### 1.3 Delta

Three vertical towers with carriages. The toolhead hangs from three arms. All three motors move to position the toolhead in X, Y, and Z.

**Examples**: Anycubic Kossel, FLSUN V400

**Pros**: Very fast (low moving mass), excellent for tall cylindrical prints
**Cons**: Complex kinematics and calibration, circular build volume, difficult to DIY

---

## 2. Motion Systems

### 2.1 Belts

**GT2 timing belts** (2mm pitch) transmit motor rotation to linear toolhead motion.

- **6mm width**: Standard for X and Y axes
- **9mm width**: Higher-end machines for stiffer motion
- **Material**: Rubber with fibreglass reinforcement (standard) or steel-reinforced (premium)
- **Tensioning**: Too loose = backlash and ringing artefacts; too tight = binding and motor overload

> **GT2 pulleys**: 20-tooth pulleys are standard. With 20 teeth × 2mm pitch = 40mm of belt movement per revolution. With 200 steps/rev and 16× microstepping: 80mm/revolution ÷ 3200 steps = **0.0125 mm/step resolution**.

### 2.2 Lead Screws

**Lead screws** (threaded rods with a matching nut) are used for Z-axis motion — they need to be self-locking (hold position when motor is off) and provide high precision.

| Type | Lead (mm/revolution) | Use |
|------|---------------------|-----|
| **T8 (4 start, 2mm pitch)** | 8mm | Standard Z-axis on most printers |
| **T8 (1 start, 2mm pitch)** | 2mm | High precision, slow |
| **Ball screw** | varies | High-end/CNC — low friction, not self-locking |

**Anti-backlash nuts** (spring-loaded split nuts) eliminate the small amount of free play in standard lead screw nuts, improving Z precision.

### 2.3 Linear Rails & Rods

Linear rails and rods guide the toolhead along each axis.

| Type | Description | Precision | Cost |
|------|------------|---------|------|
| **Smooth rods + LM8UU bearings** | 8mm steel rods with ball bearing carriages | Good | Low |
| **IGUS bushings** | Self-lubricating polymer bushings on rods | Good, no lubrication needed | Medium |
| **MGN12 linear rail** | Single-rail with carriage block | Excellent | Medium–High |
| **MGN9 linear rail** | Narrower rail — lighter, for lightweight toolheads | Excellent | Medium–High |

---

## 3. Hot End Assembly

The **hot end** melts the filament and extrudes it through the nozzle. Understanding its components is critical for maintenance and troubleshooting clogs.

```
Filament
   ↓
[Heat Sink / Cold Zone]   ← kept cold by the hot end fan
   ↓
[Heat Break]              ← the narrow thermal barrier
   ↓
[Heater Block]            ← contains heater cartridge and thermistor
   ↓
[Nozzle]                  ← the precision orifice filament exits through
```

### 3.1 Heat Sink

A finned aluminium block that dissipates heat upward away from the heat break. It must stay cool (≤40°C) to prevent **heat creep** (filament softening in the cold zone and jamming).

### 3.2 Heat Break

The **heat break** is a narrow, thermally resistant tube connecting the heat sink to the heater block. Its job is to create a sharp thermal gradient — hot below, cold above.

- **PTFE-lined heat break**: PTFE (Teflon) sleeve inside the tube. Good for PLA, PETG. **Max ~240°C** (PTFE degrades at high temperatures and releases fumes above 260°C)
- **All-metal heat break**: No PTFE — made of titanium or stainless steel. Required for ABS, ASA, Nylon, and high-temperature filaments (≥240°C). Harder to tune retraction.

### 3.3 Heater Block

An aluminium block (or copper for higher-end builds) housing:
- **Heater cartridge**: Ceramic or coiled resistance wire; generates heat
- **Thermistor**: Reads temperature so the firmware can maintain target

### 3.4 Nozzle

The nozzle is the precision orifice through which melted filament is extruded.

| Nozzle Type | Material | Max Temp | Abrasive? | Best For |
|------------|---------|---------|---------|---------|
| **Brass MK8 / E3D V6** | Brass | ~300°C | No | PLA, PETG, ABS |
| **Hardened steel** | Tool steel | ~500°C | Yes | Carbon fiber, glow, abrasive filaments |
| **Ruby-tipped** | Brass + ruby | ~500°C | Yes | Production use with abrasives |
| **Copper** | Copper | ~500°C | Limited | High-temperature filaments |

**Nozzle diameters**: 0.4mm is the universal standard. 0.2mm for fine detail, 0.6mm or 0.8mm for faster/thicker prints.

---

## 4. Extruder

The **extruder** is the mechanism that grips and feeds filament into the hot end. It consists of a driven gear (motor) and an idler (spring-loaded), which pinch and push the filament.

### 4.1 Bowden Extruder

The extruder motor is **remote** — mounted on the frame. Filament travels through a **PTFE tube (Bowden tube)** from the extruder to the hot end.

**Examples**: Creality Ender 3 (stock), original E3D Bowden setups

| Pros | Cons |
|------|------|
| Lighter toolhead → faster X/Y motion | Long PTFE tube adds flex → worse retraction |
| Simpler toolhead design | Flexible filaments (TPU) are very hard to print |
| Less toolhead mass | Requires more retraction tuning |

### 4.2 Direct Drive Extruder

The extruder motor sits **on the toolhead**, directly above or adjacent to the hot end. No Bowden tube.

**Examples**: Dragon, Twin Dragon (BGM direct drive extruder)

| Pros | Cons |
|------|------|
| Precise retraction control | Heavier toolhead |
| Excellent flexible filament support | More mass = more ringing if not compensated |
| Shorter filament path | |

### 4.3 Common Extruder Designs

| Extruder | Drive Ratio | Notes |
|---------|------------|-------|
| **MK8** | 1:1 | Simple, stock on Creality printers |
| **BMG** | 3:1 | Dual-drive gears — excellent grip |
| **Orbiter v2** | 7.5:1 | Very light, high ratio — popular for direct drive |
| **Galileo 2** | 9:1 | Orbiter-like, popular in Voron community |

---

## 5. Print Bed

### 5.1 Heated Bed Types

| Type | Material | Adhesion | Notes |
|------|---------|---------|-------|
| **Glass + hairspray/glue stick** | Borosilicate glass | Good for PLA | Flat surface; print releases when cool |
| **PEI sheet (smooth)** | PEI on spring steel | Excellent for PLA, PETG | Print pops off when cooled |
| **PEI sheet (textured)** | PEI with texture pattern | Excellent adhesion + finish | Textured pattern transfers to bottom of print |
| **Garolite (G10)** | Fibreglass laminate | Excellent for Nylon | Specialty surface |

### 5.2 Bed Levelling

The print bed must be **level and at a consistent height** relative to the nozzle. Even a 0.05mm variation across the bed can cause the first layer to fail.

- **Manual levelling**: Four corner knobs + paper method
- **Mesh bed levelling (ABL)**: Probe measures 9–100+ points, firmware applies correction in real time

> **Z-offset**: The distance from the probe trigger point to the nozzle tip. Must be calibrated so the nozzle is the correct distance from the bed.

---

## 6. Cooling

### Part Cooling

A **part cooling fan** blows cold air directly onto the freshly extruded layer to:
- Lock in the shape before the next layer is deposited
- Improve overhang quality
- Reduce stringing

**Ducts and shrouds** direct airflow from multiple directions for even coverage.

### Hot End Cooling

Always-on fan keeps the heat sink cold. Stops when the printer powers off (ensure the hot end cools below 50°C before cutting power to this fan — some firmware does this automatically).

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [How does a 3D Printer work? (Bambu Lab A1)](https://www.youtube.com/watch?v=f94CnlQ0eq4) | YouTube | Clear visual walkthrough of all mechanical subsystems on a modern printer |
| [Build your own 3D Printer: Frames and Linear Motion!](https://www.youtube.com/watch?v=E5FqrycYL40) | YouTube | Explains frame types, linear rails, rods, and motion components in detail |
| [How to Build a 3D Printer — The Ultimate Guide](https://www.youtube.com/watch?v=qub5chyIQ0s) | YouTube | Full build walkthrough — great for understanding how every part connects |
| [How a Delta 3D Printer Works (The Basics)](https://www.youtube.com/watch?v=mfjp9i9aJDg) | YouTube | Covers delta kinematics and how it differs from Cartesian |
| [Build a 3D Printer from Scratch — Part 1](https://www.youtube.com/watch?v=SZO9NTPdU2A) | YouTube | First-principles build — ideal for understanding mechanical design decisions |

---

## 📚 Further Reading & Forums

- [Flashforge — A Breakdown of All the Parts of a 3D Printer](https://www.flashforge.com/blogs/news/parts-of-a-3d-printer) — Visual reference guide to every 3D printer component
- [All3DP — 3D Printer Extruder: All You Need to Know](https://all3dp.com/2/3d-printer-extruder-guide/) — Comprehensive extruder guide covering types, pros/cons, and tuning
- [E3D — Anatomy of a 3D Printer HotEnd](https://e3d-online.com/blogs/news/anatomy-of-a-hotend) — Official E3D explainer of hot end components from the leading manufacturer
- [MatterHackers — Anatomy of a 3D Printer: How Does a 3D Printer Work?](https://www.matterhackers.com/articles/anatomy-of-a-3d-printer) — Illustrated guide to the full printer anatomy
- [DyzeDesign — The Ultimate Guide to 3D Printer Extruders](https://dyzedesign.com/2020/08/the-ultimate-guide-to-3d-printer-extruder/) — Technical deep-dive into extruder design and performance

---

## ✅ Knowledge Check

1. What are the three main printer kinematics types? Which one moves the bed in Y-axis, and what is the downside of this?
2. What is the purpose of the heat break, and why might you choose an all-metal heat break over a PTFE-lined one?
3. A printer with a 20-tooth GT2 pulley, 200-step motor, and 16× microstepping — what is its theoretical XY step resolution in mm?
4. What is the difference between a Bowden and a direct-drive extruder? Name one scenario where direct drive is essential.
5. Why must the hot end fan stay running when the hot end is hot, and what failure mode does it prevent?

---

*Module 02 of 8 — [← Electronics Basics](../01-electronics-basics/README.md) | [Next: Software & Slicing →](../03-software-and-slicing/README.md) | [Back to Index](../README.md)*
