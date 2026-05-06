# Module 4: 3D Printer Basics — FDM Machines and Components

> A complete technical orientation to FDM 3D printing machines — how they work, what each component does, and machine-specific details for Snowflake, Julia, Dragon, and Twin Dragon.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Explain the FDM (Fused Deposition Modeling) process from first principles
- Identify every major component of a 3D printer and its function
- Describe the differences between our four machines (Snowflake, Julia, Dragon, Twin Dragon)
- Configure bed leveling (manual and automatic with BLTouch/CR Touch)
- Wire a hotend assembly including heater cartridge, thermistor, and part cooling fan
- Understand extruder E-steps calibration and why it matters

## Prerequisites

- Module 1: Electronics Basics
- Module 2: Mechanical Systems

---

## 🛠️ Tools Required

| Tool | Purpose |
|------|---------|
| Digital multimeter | Heater cartridge resistance test, thermistor check |
| Hex key set (1.5–5 mm) | Extruder and hotend assembly |
| Tweezers (ESD-safe, heat-resistant) | Handling hotend components |
| Sheet of A4 paper (80 g/m²) | Z-offset calibration (paper drag test) |
| OrcaSlicer (installed on laptop) | Slicing test prints for calibration |
| Mainsail / Fluidd web interface (browser) | Klipper console commands |
| VS Code with Remote SSH | Editing `printer.cfg` |
| Infrared thermometer (optional) | Verifying bed surface temperature |
| Torque driver (1.5–2.0 N·m) | Hot-tightening nozzle at temperature |

> 📌 **Machine access required:** At least one of Snowflake, Julia, Dragon, or Twin Dragon powered on and connected.

---

## ⚠️ Safety Guidelines

1. **Thermal runaway protection must always be ON.** Never comment out `thermal_runaway_hysteresis` or set it to 0 in `printer.cfg`. A failed heater with no runaway check will run at full power until a fire starts.
2. **Never reach into a homing machine.** During `G28`, axes move at high speed. Keep hands clear until motion stops and Klipper shows "Ready."
3. **Z-offset calibration — go slowly.** Use `TESTZ Z=-0.05` increments. A negative offset that's too large will drive the nozzle through the bed surface.
4. **Heat the hotend before extruding.** Cold extrusion (< 170°C for PLA) grinds the drive gear against solid plastic. Klipper's `PREVENT_COLD_EXTRUSION` blocks this by default — never disable it.
5. **Don't home when a print is running.** `G28` mid-print resets all position data and immediately destroys the print. Use `CANCEL_PRINT` first.
6. **Verify BLTouch/CR Touch probe state before homing.** Run `QUERY_PROBE` before `G28`. A stuck-down probe causes incorrect homing.
7. **Dragon Volcano takes longer to stabilize.** Allow 120 seconds at target temperature before printing. Rushing causes thermal shock and inconsistent first layers.

---

## 1. How FDM Works

**FDM (Fused Deposition Modeling)** is a manufacturing process where a 3D object is built by depositing melted plastic layer by layer.

### 1.1 The Process — Step by Step

```
1. DIGITAL MODEL     →  A 3D CAD file (.STL, .STEP, .OBJ)
        ↓
2. SLICING           →  Software converts model into layers + G-code instructions
        ↓
3. G-CODE            →  A text file of movement commands (G1 X10 Y20 Z0.3 E5.0)
        ↓
4. PRINTING          →  Printer reads G-code, moves XY, extrudes melted filament
        ↓
5. LAYER ADHESION    →  Each layer fuses to the one below while both are at temperature
        ↓
6. PART COMPLETED    →  Remove from bed, post-process as needed
```

### 1.2 Why Layer Adhesion Matters

FDM parts are **anisotropic** — they are stronger in the X/Y plane than in the Z direction (between layers). Layer adhesion depends on:
- **Temperature:** Higher print temp = better inter-layer fusion, but may cause stringing
- **Layer height:** Thicker layers bond better but reduce resolution
- **Print speed:** Slower = more time for fusion = stronger bonds
- **Material:** PETG, ASA, and ABS bond better than PLA

---

## 2. Anatomy of an FDM Printer

```
                  [Filament Spool]
                        │
              [Extruder / Feeder Motor]
                        │ (Bowden tube or direct)
              [Hot End Assembly]
              ├── Heat Break (thermal barrier)
              ├── Heater Block + Cartridge
              ├── Thermistor
              └── Nozzle (0.4 mm standard)
                        │ (molten filament)
              [Build Surface / Bed]

Motion System:
  X-axis: Hotend carriage moves LEFT ↔ RIGHT
  Y-axis: Bed (Cartesian) or gantry (CoreXY) moves FRONT ↔ BACK
  Z-axis: Gantry/bed moves UP ↓ DOWN (layer-by-layer)

Control:
  [Control Board] → drives motors, reads sensors, controls heaters
  [Firmware] (Marlin or Klipper) → interprets G-code
  [Host] (Raspberry Pi + OctoPrint/Mainsail) → sends G-code to board
```

---

## 3. Our Machines

### 3.1 Snowflake

| Spec | Value |
|------|-------|
| **Motion System** | CoreXY |
| **Build Volume** | 300 × 300 × 300 mm |
| **Extruder Type** | Direct Drive |
| **Control Board** | MKS Monster8 |
| **Firmware** | Klipper |
| **Host** | Raspberry Pi 4 (Mainsail) |
| **Bed** | PEI spring-steel magnetic sheet |
| **Auto-leveling** | BLTouch |
| **Nozzle** | 0.4 mm brass (standard), 0.6 mm hardened steel (abrasives) |
| **Max Hotend Temp** | 300°C |
| **Max Bed Temp** | 110°C |

**Notes:**
- Snowflake is our primary production machine — treat it with priority care
- Uses TMC2209 drivers in UART mode (silent operation)
- BLTouch mounts to carriage left side — do not disassemble without recording probe offset

### 3.2 Julia

| Spec | Value |
|------|-------|
| **Motion System** | CoreXY |
| **Build Volume** | 250 × 250 × 250 mm |
| **Extruder Type** | Direct Drive |
| **Control Board** | MKS Robin Nano V3 |
| **Firmware** | Klipper |
| **Host** | Raspberry Pi 3B+ (Fluidd) |
| **Bed** | Glass with PEI coating |
| **Auto-leveling** | CR Touch |
| **Nozzle** | 0.4 mm brass |
| **Max Hotend Temp** | 280°C |
| **Max Bed Temp** | 100°C |

**Notes:**
- Julia is the training machine — freshers do calibration exercises here
- CR Touch probe offset: X offset = -38 mm, Y offset = +3 mm (verify before printing)
- TMC2208 drivers — configured via UART in Klipper

### 3.3 Dragon

| Spec | Value |
|------|-------|
| **Motion System** | CoreXY |
| **Build Volume** | 350 × 350 × 400 mm |
| **Extruder Type** | Bowden (default), Direct Drive upgrade available |
| **Control Board** | MKS Eagle |
| **Firmware** | Klipper |
| **Host** | Raspberry Pi 4 (Mainsail) |
| **Bed** | Heated aluminum + PEI sheet |
| **Auto-leveling** | BLTouch |
| **Nozzle** | 0.4–0.8 mm (task dependent) |
| **Max Hotend Temp** | 320°C |
| **Max Bed Temp** | 120°C |

**Notes:**
- Dragon is our large-format machine for production parts
- With Bowden setup: retraction = 4–6 mm. With Direct Drive: retraction = 0.5–1.5 mm
- High-temp capable — use for PETG, ABS, ASA, and Nylon
- CAN bus wiring on toolhead — do not disconnect CAN connector while powered

### 3.4 Twin Dragon (IDEX)

| Spec | Value |
|------|-------|
| **Motion System** | CoreXY + IDEX (Independent Dual Extruder) |
| **Build Volume** | 300 × 300 × 350 mm (per head) |
| **Extruder Type** | Dual Direct Drive |
| **Control Board** | MKS Monster8 |
| **Firmware** | Klipper (with IDEX configuration) |
| **Host** | Raspberry Pi 4 (Mainsail) |
| **Bed** | Full-width PEI flexible sheet |
| **Auto-leveling** | Dual BLTouch (one per head) |
| **Nozzle** | T0: 0.4 mm brass | T1: 0.4 mm hardened steel |
| **Max Hotend Temp** | 300°C (both) |
| **Max Bed Temp** | 110°C |

**IDEX Modes:**

| Mode | Description | Use Case |
|------|-------------|---------|
| **Single T0** | Only left head prints | Standard single-material prints |
| **Single T1** | Only right head prints | Abrasive materials |
| **Dual Material** | Both heads print different materials | Soluble supports (PVA + PLA) |
| **Mirror Mode** | Both heads mirror each other | Print 2 identical parts simultaneously |
| **Duplication Mode** | Both heads print same path, shifted | Batch production — 2× throughput |

**Notes:**
- IDEX calibration requires X-offset between T0 and T1 — stored in Klipper config
- Always park unused head at park position before switching tools
- Run `T0_OFFSET_CALIBRATION` macro after any toolhead service

---

## 4. The Hotend — Deep Dive

### 4.1 Heater Cartridge

The **heater cartridge** is a resistive element that converts electrical power into heat. It sits inside the heater block.

| Spec | Typical Value |
|------|--------------|
| **Voltage** | 12V or 24V (must match PSU) |
| **Wattage** | 30–60W |
| **Resistance (24V, 40W)** | R = V²/P = 576/40 = **14.4 Ω** |

**Checking a heater cartridge:**
1. Power off and unplug the printer.
2. Disconnect the heater cartridge leads from the board.
3. Set multimeter to Ω (200Ω range).
4. Probe the two heater leads.
5. Expected: **10–20 Ω** for a 24V cartridge. `OL` = open circuit (dead cartridge). `0 Ω` = shorted cartridge (dangerous — replace immediately).

### 4.2 Thermistor

The **thermistor** is a temperature-sensitive resistor used to measure the hotend and bed temperature.

**NTC 100K thermistor (Beta 3950) — resistance vs. temperature:**

| Temperature | Resistance |
|------------|-----------|
| 0°C | ~330 kΩ |
| 25°C | ~100 kΩ |
| 100°C | ~6.5 kΩ |
| 200°C | ~1.4 kΩ |
| 250°C | ~0.8 kΩ |

**Klipper thermistor config:**
```ini
[extruder]
sensor_type: NTC 100K beta 3950
sensor_pin: PA1
```

**Common thermistor errors:**
- `MINTEMP error`: Thermistor reads extremely high resistance (wire broken or thermistor disconnected) → Marlin/Klipper sees temperature of –999°C
- `MAXTEMP error`: Thermistor reads near 0 Ω (short circuit) → Marlin/Klipper sees temperature of 999°C

### 4.3 Part Cooling Fan

The **part cooling fan** blows air directly on the just-extruded plastic to solidify it quickly and prevent drooping (especially for overhangs).

| Material | Part Cooling | Notes |
|----------|-------------|-------|
| PLA | 100% | Full cooling required for overhangs |
| PETG | 30–50% | Moderate cooling — too much reduces layer bonding |
| ABS / ASA | 0–10% | Minimal cooling — prevents warping and layer delamination |
| TPU | 30% | Some cooling to maintain shape |
| Nylon | 0% | No cooling — needs full thermal retention |

---

## 5. Bed Leveling

**Bed leveling** (more accurately: **bed tramming**) ensures that the nozzle is a consistent, precise distance from the bed across the entire print surface.

### 5.1 Why It Matters

- Too close: Nozzle scrapes bed, clogs, or gouges PEI surface
- Too far: First layer doesn't adhere → print lifts and fails
- Uneven: One corner sticks, opposite corner doesn't

### 5.2 Manual Bed Tramming

Used on machines without auto-leveling or as a prerequisite before auto-leveling.

**Required: A piece of standard A4 paper (0.10 mm thickness)**

1. Preheat bed to print temperature (PLA → 60°C, PETG → 70°C, ABS → 100°C).
2. Preheat nozzle to 150°C (soft enough to ooze but won't burn you instantly).
3. In OctoPrint/Mainsail: send `G28` (home all axes).
4. Send `G0 Z0.2` to bring nozzle close to bed — **never send `G0 Z0` directly**, the nozzle may crash into the surface before homing is applied.
5. Move nozzle to front-left corner (`G0 X30 Y30`).
6. Slide paper under nozzle. Adjust corner knob until paper has slight resistance but can still slide.
7. Repeat for all 4 corners: front-right (G0 X270 Y30), back-right (G0 X270 Y270), back-left (G0 X30 Y270).
8. Return to center (G0 X150 Y150) — verify paper drag is consistent.
9. Repeat 2–3 times until all corners are consistent.

### 5.3 BLTouch / CR Touch Auto-Leveling

**BLTouch** and **CR Touch** are automatic bed probing devices. They deploy a small pin, touch the bed, and record the exact Z height at multiple probe points. The firmware uses this data to create a **mesh** that compensates for bed unevenness during printing.

**BLTouch connection on MKS boards:**

```
BLTouch → Board
  Brown (GND)  → GND
  Red   (V+)   → 5V
  Orange (Control) → Servo pin (e.g., PA8)
  Black  (GND) → GND
  White  (Signal) → Z-probe pin (e.g., PC6)
```

**Klipper BLTouch configuration:**

```ini
[bltouch]
sensor_pin: ^PC6       # ^ = pull-up enabled
control_pin: PA8
x_offset: -38.0        # Julia-specific measured value. Measure on YOUR machine: nozzle X minus probe X
y_offset: +3.0         # Julia-specific. Positive = probe is behind nozzle
z_offset: 1.45         # Starting value only — fine-tune with PROBE_CALIBRATE macro

[bed_mesh]
speed: 120
horizontal_move_z: 5
mesh_min: 35, 6
mesh_max: 245, 245
probe_count: 5, 5      # 5×5 = 25 probe points
algorithm: bicubic
```

> 📌 **Critical:** The `x_offset` and `y_offset` values above are Julia-specific measured values. On any other machine, measure the physical distance between nozzle tip and probe pin with calipers and enter your own values. Do not copy these numbers to Snowflake or Dragon.

**Running a bed mesh:**

```
# In Mainsail or Fluidd console:
G28              # Home all axes
BED_MESH_CALIBRATE  # Probe all mesh points (takes 3–5 minutes)
SAVE_CONFIG      # Writes mesh to printer.cfg
```

### 5.4 Z-Offset Calibration

The **Z-offset** is the distance between the probe trigger point and the actual nozzle tip. It must be set accurately or the first layer will be too high (poor adhesion) or too low (nozzle gouges bed).

```
# Klipper Z-offset calibration procedure:
G28
PROBE_CALIBRATE
# Nozzle will lower to probe point
# Use TESTZ Z=-0.05 to lower, TESTZ Z=+0.05 to raise
# Slide paper under nozzle until slight friction
ACCEPT
SAVE_CONFIG
```

---

## 6. Extruder E-Steps Calibration

**E-steps** (Extruder steps-per-mm) tells the firmware how many motor steps are required to push 1 mm of filament. If this is wrong, you will either under-extrude or over-extrude.

> **Klipper equivalent:** `rotation_distance` in `[extruder]` config.

### 6.1 Procedure (Marlin Firmware)

1. Heat the hotend to printing temperature (PLA: 200°C).
2. Remove the Bowden tube from the extruder (for Bowden setups) or measure from a reference mark.
3. Mark the filament **100 mm** above the extruder entry point (use a marker).
4. In the printer control, extrude **100 mm** of filament.
5. Measure how much filament actually moved. E.g., measured = **95 mm**.

**Calculation:**

```
New E-steps = (Current E-steps × Commanded distance) ÷ Actual distance
            = (420 × 100) ÷ 95
            = 442 steps/mm
```

6. Update in Marlin: `M92 E442` → `M500` (save to EEPROM).

### 6.2 Procedure (Klipper Firmware)

In Klipper, E-steps is replaced by `rotation_distance`:

```
rotation_distance = (old_rotation_distance × actual_distance) ÷ commanded_distance
```

Update in `printer.cfg`:
```ini
[extruder]
rotation_distance: 7.71    # Adjusted from measurement
```

Send `FIRMWARE_RESTART` to apply.

---

## 7. First Layer Troubleshooting

The first layer determines whether a print will succeed or fail. Learn to read it visually:

| First Layer Appearance | Diagnosis | Fix |
|----------------------|-----------|-----|
| Barely sticking, gaps between lines | Nozzle too far from bed | Lower Z-offset |
| Squished flat, no bead texture visible | Nozzle too close to bed | Raise Z-offset |
| One corner peeling immediately | Bed not trammed (corner too high) | Re-tram that corner |
| Consistent adhesion but lifting after 3–4 layers | Bed temp too low or draft | Increase bed temp, add enclosure |
| Print sticks at start, detaches mid-print | Bed surface contaminated | Clean with IPA (isopropyl alcohol) |
| Curling at corners (ABS/ASA) | Thermal gradient — not enough bed heat | Increase bed temp; use enclosure |

---

## 8. Wiring a Hotend Assembly

This procedure covers wiring a replacement hotend from scratch on Julia or Snowflake.

### 8.1 Components to Wire

1. Heater cartridge (2 leads — not polarity sensitive)
2. Thermistor (2 leads — not polarity sensitive, but fragile)
3. Part cooling fan (2 leads — polarity sensitive; red = V+)
4. Hotend fan / cold-end fan (2 leads — polarity sensitive)
5. BLTouch (5 leads — polarity critical, see Section 5.3)

### 8.2 Cable Management

1. Route all hotend wires through the **cable chain** (drag chain) before connecting.
2. Leave **100–150 mm of slack** at the hotend end to allow motion without tension.
3. Secure wires to the carriage with zip ties every 30–50 mm inside the chain.
4. Separate signal wires (thermistor, endstop) from power wires (heater, fans) inside the chain to minimize EMI.
5. Use heat-shrink tubing on all bare solder joints before routing.

### 8.3 Verification Before Power-On

- [ ] All connectors fully seated and clicked
- [ ] Heater cartridge polarity confirmed (AC-current only, no polarity, but check voltage rating matches PSU)
- [ ] Thermistor connector orientation confirmed (check board silkscreen for polarity label)
- [ ] Fans connected with correct polarity (red to V+)
- [ ] BLTouch wired per diagram (5-wire — verify brown=GND, red=5V, orange=control, black=GND, white=signal)
- [ ] Continuity check on all heater connections
- [ ] No bare wires touching metal frame or each other

---

## ❌ Common Mistakes

| Mistake | What Happens | Correct Practice |
|---------|-------------|------------------|
| Z-offset too negative (nozzle too close) | Nozzle gouges bed / blocks extrusion | Paper drag test: slight resistance only. Use `TESTZ Z=-0.05` increments |
| Z-offset too positive (nozzle too far) | First layer doesn't adhere | Decrease Z-offset by 0.05–0.1 mm and re-test |
| Running `BED_MESH_CALIBRATE` on a cold bed | Mesh reflects cold geometry, not print geometry | Always heat bed to print temperature before running mesh calibration |
| Not running `SAVE_CONFIG` after calibration | Calibration values lost on restart (RAM only) | Run `SAVE_CONFIG` immediately after every calibration session |
| Skipping PID tune after hotend swap | Temperature oscillation → poor extrusion and layer quality | Run `PID_CALIBRATE HEATER=extruder TARGET=200` after any hotend swap |
| Measuring `rotation_distance` at wrong temperature | Filament slips differently at different temps | Measure at actual print temperature, not room temperature |
| Forgetting `T1 PROBE_CALIBRATE` on Twin Dragon | Head 1 Z-offset wrong → dual-head print fails | Calibrate both heads independently on Twin Dragon |
| Using `G29` on a Klipper machine | `G29` is Marlin — on Klipper it does nothing | Use `BED_MESH_CALIBRATE` on all Klipper machines |
| Starting a print immediately after `M140` (no wait) | Bed hasn't stabilised → first layers at wrong temperature | Use `M190 S<temp>` (blocks until temperature reached) in START_PRINT |

---

## 9. Hands-On Exercises

### Exercise 4.1 — Machine Identification
- [ ] Photograph each machine (Snowflake, Julia, Dragon, Twin Dragon) and label at least 10 components per machine
- [ ] Record the current firmware version displayed on each machine's screen

### Exercise 4.2 — Hotend Electrical Testing
- [ ] Using a multimeter, measure heater cartridge resistance on Julia — record value and confirm it is within spec
- [ ] Measure thermistor resistance at room temperature on Dragon — confirm ~100kΩ
- [ ] Test fan continuity on Snowflake

### Exercise 4.3 — Manual Bed Tramming
- [ ] Perform a full manual tram on Julia from scratch (all 4 corners + center verify)
- [ ] Record the before and after Z-height variation across corners

### Exercise 4.4 — BLTouch Bed Mesh
- [ ] Run `BED_MESH_CALIBRATE` on Snowflake
- [ ] Export the mesh visualization from Mainsail
- [ ] Identify the highest and lowest points in the mesh

### Exercise 4.5 — E-Steps / Rotation Distance Verification
- [ ] Mark filament 120 mm above extruder on Julia
- [ ] Command 100 mm extrude
- [ ] Measure actual extrusion
- [ ] Calculate corrected rotation_distance and update printer.cfg

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [FDM 3D Printing — How Does It Work?](https://www.youtube.com/watch?v=1uLs8m1UBCc) | Thomas Sanladerer | First-principles explanation with great animations |
| [BLTouch Installation and Calibration](https://www.youtube.com/watch?v=eF060dBEnfs) | Teaching Tech | Complete BLTouch setup including Z-offset calibration |
| [E-Steps Calibration — The Right Way](https://www.youtube.com/watch?v=X3A9Ir4P7gU) | Teaching Tech | Step-by-step extruder calibration with calculation |
| [Perfect First Layer — Visual Guide](https://www.youtube.com/watch?v=dCmB1cGHOps) | Maker's Muse | Diagnosing first layer issues from visual inspection |
| [CoreXY Printers Explained](https://www.youtube.com/watch?v=SbonF7cBOKU) | Teaching Tech | Kinematics and belt routing for CoreXY machines |

---

## 📚 Further Reading

- [Klipper Documentation — Bed Leveling](https://www.klipper3d.org/Bed_Level.html) — Official Klipper bed mesh and probe configuration
- [Klipper Documentation — BLTouch](https://www.klipper3d.org/BLTouch.html) — Full BLTouch wiring and config reference
- [Teaching Tech 3D Printer Calibration Guide](https://teachingtechyt.github.io/calibration.html) — Systematic calibration from E-steps to temperature towers
- [MKS Monster8 Documentation](https://github.com/makerbase-mks/MKS-Monster8) — Board schematic and pinout reference for Snowflake and Twin Dragon

---

## ✅ Knowledge Check

1. What does FDM stand for, and describe the process in 3 steps.
2. Twin Dragon's IDEX system has a mode called "Duplication Mode." What does this mode do, and when would you use it?
3. You measure a heater cartridge and get `OL` on your multimeter. What does this mean, and what do you do?
4. The BLTouch probe's X-offset is set to -38 mm. Explain what this value means physically.
5. A print on Julia shows the first layer squished completely flat with no visible bead texture. What is the likely cause and what do you adjust?
6. After replacing the extruder on Snowflake, you measure 94 mm of actual extrusion when 100 mm was commanded, and the current rotation_distance is 7.71. Calculate the corrected rotation_distance.
7. What is the difference between bed tramming and bed meshing? When do you need both?

---

*Module 4 of 6 — [Back to Index](README.md)*
