# Module 2: Mechanical Systems for 3D Printing

> Tools, fasteners, motion systems, and assembly practices every 3D printer technician must master — from selecting the right hex key to understanding CoreXY kinematics.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Identify and correctly use essential mechanical tools (hex keys, calipers, screwdrivers)
- Select the correct fastener type and size for a given joint
- Understand linear motion systems (rods, rails, lead screws, belts)
- Assemble and adjust a printer frame to specification
- Recognize and fix common mechanical failures (belt slack, Z-binding, loose couplers)
- Apply torque and assembly best practices to build reliable, repeatable machines

## Prerequisites

- Module 1: Electronics Basics (understanding of printer system components)

---

## ⚠️ Safety Guidelines

1. **Power off before mechanical work.** Moving parts (belts, motors, carriages) can cause pinching at speeds up to 300 mm/s.
2. **Wear safety glasses** when cutting zip ties, springs, or using flush cutters — small parts become projectiles.
3. **Never replace a nozzle cold.** Forcing a cold nozzle strips threads in the heater block. Heat to 190°C minimum before unscrewing.
4. **Hot nozzle burns are fast.** At 200°C, contact time under 0.5 seconds causes a burn. Always use tweezers or heat-resistant gloves.
5. **Lead screws can pinch.** Keep hands clear of Z-drive mechanisms during homing and calibration moves.
6. **Don't over-tighten frame bolts.** Cracked extrusion corner brackets fail suddenly under vibration. Use 1.5–2.0 N·m on M5 frame fasteners.
7. **WD-40 is not a lubricant** for printer rails. It attracts dust and leaves no lasting film. Use Super Lube PTFE grease or white lithium grease.
8. **Direct compressed air away** from your face and other electronics when blowing dust from mechanical components.

---

## 1. Essential Tools

Every technician should have these tools accessible at all times:

### 1.1 Hand Tools

| Tool | Specification | Use |
|------|--------------|-----|
| **Ball-end hex keys (Allen keys)** | 1.5 / 2 / 2.5 / 3 / 4 / 5 mm | M2–M6 socket-head cap screws |
| **Flathead screwdriver** | 3 mm, 6 mm | Terminal screws, heatset inserts |
| **Phillips screwdriver** | #1, #2 | General assembly screws |
| **Digital vernier caliper** | 0–150 mm, 0.01 mm resolution | Measuring parts, checking dimensions |
| **Open-end spanners** | M3–M10 sizes | Locking nuts, couplers |
| **Needle-nose pliers** | Standard | Gripping small parts, bending wire |
| **Flush cutters** | — | Trimming supports, cutting zip ties |
| **Loctite 243 (medium threadlock)** | Blue | Preventing vibration-induced loosening |
| **PTFE (polytetrafluoroethylene) plumber's tape** | — | Thread sealing on pneumatic fittings |
| **Torque screwdriver** | 0.5–5 N·m | Consistent torque on critical fasteners |

### 1.2 Measuring Tools

**Digital Vernier Caliper — How to Use:**

1. Close the jaws completely and verify the display reads **0.00 mm** (zero it if not).
2. For **outer diameter** (OD): place the part between the main jaws, close gently, read display.
3. For **inner diameter** (ID): use the upper small jaws, open until they contact the bore walls.
4. For **depth**: use the depth rod at the base — slide it into the hole, read display.
5. Always measure at least twice and average the readings.

> **Reference:** A filament spool tube inner diameter should measure **4.0 mm** for standard PTFE tubing. If your measurement reads 3.7 mm, the tube is blocked or compressed.

---

## 2. Fasteners

3D printers use metric fasteners (M-series) almost exclusively. Understanding fastener selection prevents stripping, cracking, and assembly failures.

### 2.1 Metric Fastener Reference

| Size | Hex Key | Thread Pitch | Common Use |
|------|---------|-------------|-----------|
| **M2** | 1.5 mm | 0.4 mm | Small fans, PCB mounting |
| **M3** | 2.5 mm | 0.5 mm | Most printer hardware: frame extrusions, carriages, hotends |
| **M4** | 3.0 mm | 0.7 mm | Belt tensioners, heavier brackets |
| **M5** | 4.0 mm | 0.8 mm | Extrusion frame T-nuts, lead screw nuts |
| **M6** | 5.0 mm | 1.0 mm | Nozzle, heat break threads |
| **M8** | 6.0 mm | 1.25 mm | Frame corners, large Z-axis components |

### 2.2 Fastener Types

| Type | Head Style | Drive | Use |
|------|-----------|-------|-----|
| **SHCS** (Socket Head Cap Screw) | Cylindrical | Hex socket | Standard assembly — most common |
| **BHCS** (Button Head Cap Screw) | Low-profile dome | Hex socket | Where head clearance is tight |
| **FHCS** (Flat/Countersunk Head) | Flush flush | Hex socket | Flush mounting through plates |
| **Set Screw** | No head (grub) | Hex socket | Locking pulleys and couplers to shafts |
| **T-Nut** | T-shaped body | — | Slides into aluminum extrusion slots |
| **Hex Nut** | Standard hex | Spanner | General fastening |
| **Nylock Nut** | Hex with nylon insert | Spanner | Vibration-resistant joints |

### 2.3 Torque Guidelines

Over-torquing strips threads. Under-torquing allows vibration loosening. Use these as starting points:

| Fastener | Into aluminum (3D print frame) | Into steel |
|----------|------------------------------|-----------|
| M3 | 0.5–0.8 N·m | 1.0–1.2 N·m |
| M4 | 1.0–1.5 N·m | 2.0–2.5 N·m |
| M5 | 2.0–3.0 N·m | 4.0–5.0 N·m |

> **Tip:** When screwing M3 into a 3D-printed PLA bracket, stop at **0.5 N·m**. PLA strips very easily. Use heat-set inserts for threaded joints that will be assembled/disassembled repeatedly.

### 2.4 Heat-Set Inserts

Heat-set brass inserts provide strong, reusable threads in 3D-printed parts.

**Installation:**
1. Print the hole to match insert outer diameter (e.g., M3 insert → 4.4 mm hole in PLA).
2. Place insert on hole entrance.
3. Heat soldering iron to **220–240°C** (lower than normal soldering temp — you’re melting the PLA around the insert, not soldering metal).
4. Press iron onto insert top — it will sink in slowly. Keep it plumb (vertical).
5. Stop when insert is flush or 0.1 mm below the surface.
6. Let cool for 30 seconds before threading a screw in.

---

## 3. Aluminum Extrusion Frame

Most modern FDM printers (including Dragon, Julia, Snowflake, Twin Dragon) use **2020 or 2040 aluminum extrusion** for their structural frame.

### 3.1 Extrusion Profile Naming

| Profile | Width × Height | Slot Width | Typical Use |
|---------|---------------|-----------|------------|
| **2020** | 20 × 20 mm | 6 mm | Light-duty frames, diagonals |
| **2040** | 20 × 40 mm | 6 mm | Vertical uprights, gantry |
| **3030** | 30 × 30 mm | 8 mm | Heavier machines |
| **4040** | 40 × 40 mm | 8 mm | Industrial builds |

### 3.2 Assembly with T-Nuts

1. Slide T-nuts into extrusion slots before assembly (post-assembly is difficult).
2. Position the T-nut in the slot, align the bracket hole over it.
3. Insert screw through bracket and turn until T-nut engages (you will feel resistance).
4. Tighten to specified torque.
5. Use a square to verify 90° before final tightening.

### 3.3 Frame Squareness Check

A non-square frame causes **layer shifts**, **inconsistent first layers**, and **Z-banding**.

**Method 1 — Diagonal measurement:**
1. Measure the diagonal across the frame from corner to corner (D1).
2. Measure the opposite diagonal (D2).
3. If D1 = D2 (within 1 mm), the frame is square.
4. If D1 ≠ D2, loosen corner brackets, adjust, re-measure.

**Method 2 — Machinist's square:**
Place the square at each corner. No visible gap = square.

---

## 4. Linear Motion Systems

Linear motion is what moves the print head and bed. Two technologies are used in our machines:

### 4.1 Linear Rods and LM8UU Bearings

Used in simpler/legacy builds.

- **Rods:** Hardened steel, 8 mm diameter (most common). Must be straight to within 0.1 mm over 300 mm.
- **LM8UU bearings:** Recirculating ball linear bearing. Slides on 8 mm rod.
- **Check:** Slide bearing by hand — should move freely with zero lateral play. If it wobbles, the rod is worn or the bearing has failed.

### 4.2 MGN Linear Rails (HIWIN Miniature Linear Rail System)

Used on Dragon, Julia, Snowflake, Twin Dragon — higher precision than rods.

| Spec | Details |
|------|---------|
| **Rail sizes** | MGN9, MGN12, MGN15 (number = rail width in mm) |
| **Carriage types** | H (standard) or C (compact) — affects travel length |
| **Preload** | Z0 (no preload, low friction) to Z3 (high preload, high stiffness) |
| **Accuracy grades** | Normal, High (H), Precision (P) |

**MGN12H Rail Installation:**
1. Clean the mounting surface — any debris will misalign the rail.
2. Lay the rail in position. Insert one M3 screw in the center hole loosely.
3. Use a precision square or indicator to align rail parallel to the frame edge.
4. Insert all remaining screws loosely.
5. Starting from center outward, torque to **0.5–0.8 N·m** in order.
6. Run the carriage full travel — should move smoothly with no catching.

### 4.3 Lead Screws (Z-Axis)

The Z-axis (up/down movement) is driven by a **lead screw** — a threaded rod that converts motor rotation into linear travel.

| Spec | Typical Value | Effect |
|------|--------------|--------|
| **Diameter** | 8 mm (T8) | Standard |
| **Lead** | 8 mm/revolution (T8 × 8) | High lead = faster Z but less precision |
| **Lead** | 2 mm/revolution (T8 × 2) | Slow, precise (better for quality) |
| **Material** | Stainless steel or hardened steel | — |

**Lead Screw Coupling:**
The lead screw connects to the motor via a **flexible coupler** (or rigid coupler on precision builds). A flexible coupler absorbs minor angular misalignment between motor shaft and lead screw.

- **Never fully rigid:** A rigid coupler with misalignment causes Z-binding and Z-wobble artifacts on prints.
- **Inspect:** Look for set screws that have loosened. Tighten all set screws with Loctite 243.

**Anti-backlash Nut:**
Standard brass nuts have **backlash** (slack) — the screw must turn slightly before the nut moves, causing Z-artifacts. Anti-backlash nuts use a spring-loaded split nut to eliminate slack.

### 4.4 Belts and Pulleys (X/Y Motion)

The X and Y axes use **GT2 timing belts** (2 mm pitch) and **GT2 pulleys**.

| Component | Specification | Notes |
|-----------|--------------|-------|
| Belt | GT2, 6 mm wide | Standard. 9 mm wide belts used on heavy gantries |
| Pulley (drive) | 20T GT2, 5 mm bore | 20 teeth, fits 5 mm motor shaft |
| Idler pulley | 20T GT2 or smooth | Toothed idler for backed-up belt paths, smooth for redirects |
| Belt tension | 120–150 Hz fundamental frequency | Measure with Gates Carbon Drive or smartphone app |

**Belt Tension Measurement:**
1. Download the **Gates Carbon Drive** app (iOS/Android).
2. Select belt type: GT2, 6mm.
3. Enter belt span length (mm) and weight per mm (for GT2: 0.076 g/mm).
4. Pluck the belt and hold the phone microphone near it.
5. Target frequency: **120–150 Hz** for typical CoreXY printer belts.
6. Too loose = low Hz → layer shifts, poor accuracy. Too tight = high Hz → bearing wear, motor strain.

**Belt Path Alignment:**
Belts must run parallel to the motion axis. A twisted belt will rub on pulley flanges and wear prematurely. Use an adjustable belt tension block to align.

> ⚠️ **CoreXY-specific requirement:** On CoreXY machines (Snowflake, Julia, Dragon, Twin Dragon), **both belts must be tensioned equally**. Unequal belt tension causes the X-axis to skew — the printhead tracks at a slight diagonal instead of straight, producing rhombus-shaped parts instead of squares. After tensioning, print a 100×100 mm square and measure both diagonals: they must be equal within 0.5 mm. If not, slightly increase tension on the slack belt.

---

## 5. Motion System Architectures

Our machines use different kinematic systems:

### 5.1 Cartesian (Bed-Slinger)

- **Description:** X-axis moves the hotend left/right. Y-axis moves the bed front/back. Z-axis lifts the gantry.
- **Examples:** Ender 3 Pro, MK3
- **Advantage:** Simple, easy to calibrate.
- **Disadvantage:** Heavy moving bed limits speed and acceleration.

### 5.2 CoreXY

- **Description:** Two motors at opposite sides of the gantry control X and Y simultaneously via crossed belts.
- **Examples:** Snowflake, Julia, Dragon, Twin Dragon
- **Advantage:** Lighter moving mass → higher speed, better quality at speed.
- **Disadvantage:** Belt routing is complex; both belts must be equal tension for accurate motion.

**CoreXY Belt Routing Principle:**
```
Motor A (left)         Motor B (right)
    │                       │
    ├───────────────────────┤  ← Crossed belt path
    │                       │
    └───→ Head moves X+Y diagonally based on A+B combination
```

- Move X only: Both motors rotate equal speeds in opposite directions.
- Move Y only: Both motors rotate equal speeds in the same direction.
- Move diagonally: One motor moves, other stays.

### 5.3 Delta

- **Description:** Three vertical towers, each with a carriage; hotend is suspended on diagonal arms.
- **Advantage:** Very fast, good for tall cylindrical prints.
- **Disadvantage:** Complex calibration; print volume is circular, not rectangular.

---

## 6. Hot End Mechanical Assembly

The hot end is the mechanical assembly that melts and extrudes filament.

### 6.1 Hot End Components

```
Filament →  [Extruder / Drive Gear]
             ↓
        [PTFE Tube / Bowden]
             ↓
      [Heat Break] ← Isolates hot from cold
             ↓
      [Heater Block] ← Holds heater cartridge + thermistor
             ↓
        [Nozzle] ← Extrudes molten filament
```

### 6.2 Nozzle Replacement

> ⚠️ **Safety:** Only replace nozzle when hot (190–230°C). Attempting cold removal WILL strip the threads.

1. Heat the nozzle to 200°C.
2. Use a **wrench to hold the heater block** — never torque against the heat break.
3. Use the nozzle wrench to unscrew the old nozzle (counter-clockwise).
4. Thread new nozzle in by hand until finger-tight.
5. Torque to **1.5–2.0 N·m** while hot (the block must be stationary using your second wrench).
6. The nozzle must be torqued HOT — the thermal expansion ensures a leak-free joint.

**Common Nozzle Materials:**

| Material | Wear Resistance | Use For |
|----------|----------------|---------|
| Brass (MK8) | Low | PLA, PETG, soft filaments |
| Hardened Steel | High | Abrasive filaments (carbon fiber, glow-in-dark) |
| Ruby-tip | Very High | All abrasive filaments, longevity |
| Copper | Medium | High-temp materials (requires higher temp) |

### 6.3 Bowden vs. Direct Drive Extruder

| Type | Description | Advantage | Disadvantage |
|------|-------------|-----------|-------------|
| **Bowden** | Motor sits on frame, PTFE tube guides filament to hotend | Light gantry, higher speed | Worse flexible filament performance, more retraction needed |
| **Direct Drive** | Motor sits directly on hotend carriage | Better flexible filament control | Heavier gantry |

**Our Machines:**
- Snowflake: Direct Drive
- Julia: Direct Drive
- Dragon: Bowden + optional Direct Drive upgrade
- Twin Dragon: Dual Direct Drive (IDEX configuration)

---

## 7. Common Mechanical Failures and Fixes

| Symptom | Likely Cause | Diagnostic | Fix |
|---------|-------------|-----------|-----|
| Layer shifts (X or Y) | Loose belt or pulley set screw | Grab belt — check tension. Wiggle pulley on shaft | Re-tension belt or tighten set screws with Loctite |
| Z-wobble on prints | Lead screw misalignment or coupler | Look at screw while printing — is it wobbling? | Align lead screw or replace flexible coupler |
| Z-binding | Rail/rod misalignment or lubrication | Run Z manually — listen for grinding | Re-align Z rails, lubricate with PTFE grease |
| Extruder skipping | Too much retraction or clogged nozzle | Listen for click sound | Reduce retraction, clear clog |
| Frame flex | Loose corner brackets | Grab frame and wiggle | Retighten all corners, check squareness |
| Bed uneven | Loose bed springs or missing tramming | First-layer inspection | Manual tram + BLTouch mesh |

---

## 8. Lubrication Reference

| Component | Lubricant | Interval |
|-----------|----------|---------|
| MGN linear rails | Super Lube (PTFE grease) or light machine oil | Every 200 print hours |
| Linear rods (8mm) | Light machine oil (3-in-1) | Every 100 print hours |
| Lead screws | Super Lube PTFE grease | Every 200 print hours |
| Extruder drive gears | No lubrication — keep dry | — |
| Nozzle thread (during install) | None — hot torque creates seal | — |

> ⚠️ **Never use WD-40 as a lubricant.** WD-40 is a water displacer that evaporates quickly and leaves no lasting lubrication. It will attract dust and accelerate wear.

---

## ❌ Common Mistakes

| Mistake | What Happens | Correct Practice |
|---------|-------------|------------------|
| Frame bolts over-tightened | Cracked T-nuts, stripped threads in extrusion | Torque M5 frame bolts to 1.5–2.0 N·m max |
| Belt over-tensioned | Premature bearing wear, axis motor overload | Target 120–150 Hz with the Gates belt tension app |
| Belt under-tensioned | Layer shifts and dimensional inaccuracy | Re-tension if deflection > 3 mm under 200 g load |
| Not squaring frame before tensioning belts | Print dimensions wrong in one axis | Measure diagonals first — difference must be < 1 mm |
| Using WD-40 or motor oil on rails | Dust accumulation, bearing seizure | Use PTFE grease on MGN rails; white lithium grease on lead screws |
| Cold nozzle removal | Stripped heater block threads | Heat to 190°C before unscrewing any nozzle |
| Under-torquing nozzle when hot | Nozzle loosens mid-print → leaks and layer shift | Torque 1.5–2.0 N·m at print temperature with thread locker |
| Installing MGN rail without preload check | Sloppy carriage movement, poor print quality | Verify carriage slides smoothly with zero play before bolting down |
| Heat-set insert installed crooked | Screw won't align, thread binding | Keep soldering iron tip vertical; apply even downward pressure |
| Cutting Bowden tube at an angle | Poor PTFE seal → filament jam at joint | Use a dedicated PTFE tube cutter for a perpendicular cut |

---

## 9. Hands-On Exercises

### Exercise 2.1 — Fastener Identification
- [ ] Pick up a random screw from the parts bin — identify size (M? ), head type, and correct hex key
- [ ] Install an M3 SHCS into a 3D-printed bracket using correct torque (0.5 N·m)
- [ ] Install a heat-set insert into a PLA test piece

### Exercise 2.2 — Belt Tensioning
- [ ] Measure belt tension on Snowflake X-axis using the Gates app
- [ ] Record the frequency and compare to the 120–150 Hz target
- [ ] Adjust the tensioner until spec is achieved; re-measure

### Exercise 2.3 — MGN Rail Inspection
- [ ] Run a carriage along the full travel of a Julia Y-axis rail
- [ ] Document any catching, roughness, or lateral play
- [ ] Apply Super Lube grease and repeat

### Exercise 2.4 — Nozzle Replacement
- [ ] Heat the Dragon hotend to 200°C
- [ ] Remove the old nozzle using the two-wrench method
- [ ] Install a new brass nozzle and torque correctly while hot
- [ ] Verify no ooze or leaks during first print

### Exercise 2.5 — Frame Squareness
- [ ] Measure both diagonals of a disassembled frame section
- [ ] Adjust until within 1 mm
- [ ] Re-torque corner brackets in the correct sequence

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [How to Use a Caliper](https://www.youtube.com/watch?v=_QJP5yBk5Xo) | AvE | Practical vernier caliper tutorial with real measurements |
| [CoreXY Explained](https://www.youtube.com/watch?v=SbonF7cBOKU) | Teaching Tech | Clear animation of CoreXY belt routing and motion math |
| [Belt Tension — Why It Matters](https://www.youtube.com/watch?v=8a4dSS5BVQY) | Thomas Sanladerer | Shows effect of incorrect tension on print quality |
| [Hot End Teardown and Rebuild](https://www.youtube.com/watch?v=5bSUHx1iuL0) | Maker's Muse | Step-by-step hotend disassembly and reassembly |
| [MGN12 Linear Rail Install Guide](https://www.youtube.com/watch?v=9pI3IrGjrxU) | Nero 3D | Rail installation, alignment, and greasing walkthrough |

---

## 📚 Further Reading

- [RepRap — CoreXY Kinematics](https://reprap.org/wiki/CoreXY) — Mathematical explanation of CoreXY motion
- [Voron Design — Assembly Manual](https://docs.vorondesign.com/) — Industry-leading reference for precision CoreXY printer assembly
- [Misumi Extrusion Profiles Catalog](https://us.misumi-ec.com/) — Full specifications for 2020/2040 extrusion hardware
- [GT2 Belt Specification Sheet](https://www.gates.com/content/dam/gates/home/knowledge-center/resource-library/catalog/gt2-timing-belt-catalog.pdf) — Official Gates GT2 belt dimensions and load ratings

---

## ✅ Knowledge Check

1. What tool do you use to check if a printer frame is square, and what measurement tolerance is acceptable?
2. A CoreXY printer has a layer shift in the X direction only. Which components are most likely at fault?
3. What is the difference between a flexible coupler and a rigid coupler for a Z-axis lead screw, and when would you use each?
4. You need to replace an M3 screw going into a 3D-printed PLA part. What torque should you apply, and what will happen if you exceed it?
5. What is the purpose of an anti-backlash nut on a lead screw?
6. Name the four components in a hot end assembly in order from extruder to nozzle.
7. What lubricant should you use on MGN linear rails, and how often?

---

*Module 2 of 6 — [Back to Index](README.md)*
