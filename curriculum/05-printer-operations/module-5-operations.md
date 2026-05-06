# Module 5: Printer Operations — Slicing, OctoPrint, Klipper, and Drybox

> End-to-end operational knowledge for running production-quality prints — from loading filament and slicing a model to monitoring jobs remotely via OctoPrint, configuring Klipper macros, and maintaining filament quality with a drybox.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Slice a 3D model with correct settings for each of our four machines
- Start, monitor, and manage print jobs via OctoPrint and Mainsail
- Configure and use Klipper macros for common operations (START_PRINT, END_PRINT)
- Set up and use the drybox system to prevent moisture-related print failures
- Use Fracktory for print job management and machine status tracking
- Perform PID tuning for hotend and heated bed
- Understand and apply key slicer parameters (layer height, infill, supports, speeds)

## Prerequisites

- Module 3: Software Tools
- Module 4: Printer Basics

---

## 🛠️ Tools Required

| Tool | Purpose |
|------|---------|
| OrcaSlicer (latest) | Primary slicer for all Klipper machines |
| PrusaSlicer (latest) | Secondary slicer — Marlin reference profiles |
| Browser (Chrome/Firefox) | Mainsail, Fluidd, OctoPrint web interfaces |
| VS Code with Remote SSH | Editing `printer.cfg` macros |
| Fracktory account | Print job logging and monitoring |
| SSH client | Accessing printer Pi hosts |
| Hygrometer (included in drybox) | Verifying filament storage humidity |
| Filament dryer (SUNLU or equivalent) | Drying wet filament before printing |
| Digital calipers | Measuring printed test parts for calibration |

> 💡 **Optional:** A spool of each material (PLA, PETG, ABS, TPU) is useful for the material settings exercises.

---

## ⚠️ Safety Guidelines

1. **Never print ABS or ASA without fume extraction.** Styrene fumes emitted at 240°C+ are an irritant and potential carcinogen. Start the exhaust fan before heating the hotend.
2. **Don't leave prints unattended overnight without alerts.** Configure Mainsail temperature alerts or Fracktory notifications before leaving the lab.
3. **Drying filament in a kitchen oven:** Use a standalone thermometer to verify actual temperature. Oven thermostats are often off by ±20°C — too hot deforms the spool.
4. **Never slice with incorrect bed dimensions.** A print that exceeds bed bounds will crash the carriage into the frame at full speed.
5. **Verify `START_PRINT` macro parameter names match the slicer's output.** A mismatch causes the macro to run cold, failing the first layer.
6. **Dragon: pre-heat the enclosure before printing ABS/PC.** Starting a high-temp print without enclosure pre-heat causes thermal shock warping on the first 10 layers.
7. **IPA for bed cleaning is flammable.** Apply IPA to a cloth, not directly to a hot bed. Vapours ignite at 13°C.

---

## 1. Slicing Fundamentals

A **slicer** converts a 3D model (STL, STEP, OBJ) into **G-code** — a text file of movement and temperature commands that the printer executes.

### 1.1 Recommended Slicers

| Slicer | Cost | Best For | Notes |
|--------|------|---------|-------|
| **PrusaSlicer** | Free | Most FDM printers | Best profile management, Klipper support |
| **Cura** | Free | Beginners, Creality machines | Large plugin ecosystem |
| **OrcaSlicer** | Free | Klipper-based machines | Best Klipper integration, pressure advance calibration |
| **Simplify3D** | Paid | Multi-process complex prints | Legacy tool, less actively updated |

**Recommended for our machines:** **OrcaSlicer** (Klipper) and **PrusaSlicer** (Marlin)

### 1.2 Essential Slicer Parameters

#### Layer Height

| Parameter | Value | Effect |
|-----------|-------|--------|
| Layer height | 0.20 mm | Standard — best balance of quality and speed |
| Layer height | 0.12 mm | High detail — slower, sharper features |
| Layer height | 0.28 mm | Draft mode — fast, reduced quality |
| First layer height | 0.24 mm | Slightly thicker for better adhesion |

> **Rule:** Maximum layer height = 75% of nozzle diameter. For a 0.4 mm nozzle, max = 0.30 mm.

#### Infill

| Pattern | Density | Strength | Speed | Use Case |
|---------|---------|---------|-------|---------|
| Gyroid | 15% | High (isotropic) | Medium | Mechanical parts, general use |
| Grid | 20% | Medium | Fast | Prototype parts |
| Lines | 15% | Low | Fast | Visual models, non-structural |
| Honeycomb | 20% | High | Slow | Structural parts |
| Solid | 100% | Maximum | Slow | Load-bearing surfaces |

**Standard settings for our operations:**
- Functional parts: **Gyroid, 20–30%**
- Display/visual models: **Lines or Grid, 10–15%**
- Structural brackets: **Gyroid, 40–60%**

#### Print Speed

| Feature | PLA | PETG | ABS/ASA |
|---------|-----|------|---------|
| Perimeters / walls | 60 mm/s | 45 mm/s | 40 mm/s |
| Infill | 120 mm/s | 80 mm/s | 60 mm/s |
| First layer | 25 mm/s | 20 mm/s | 20 mm/s |
| Bridges | 30 mm/s | 25 mm/s | 25 mm/s |
| Travel | 200 mm/s | 150 mm/s | 120 mm/s |

#### Temperature Settings

| Material | Hotend | Bed | Enclosure |
|----------|--------|-----|-----------|
| PLA | 200–220°C | 55–65°C | Not needed |
| PETG | 230–245°C | 70–85°C | Optional |
| ABS | 230–250°C | 100–110°C | Required |
| ASA | 240–260°C | 100–110°C | Required |
| TPU (95A) | 220–235°C | 30–50°C | Not needed |
| Nylon PA12 | 250–270°C | 70–90°C | Required |

#### Supports

| Type | Use |
|------|-----|
| Linear / Grid | Fast to generate and remove; leaves marks on surface |
| Tree / Organic | Better surface finish; efficient for complex geometries |
| None | When design allows (max 45° overhang without supports) |

**Support settings for Snowflake/Julia (PLA):**
- Interface layers: 3 (smooth contact surface)
- Interface layer height: 0.20 mm
- Z distance: 0.20 mm (gap between support and part)
- XY distance: 0.60 mm

### 1.3 Generating G-code for Our Machines

**In OrcaSlicer:**
1. Click **File → Import → Import 3MF or STL**
2. Select the printer profile matching your machine (Snowflake, Julia, Dragon, Twin Dragon)
3. Select material profile (PLA, PETG, ABS)
4. Review orientation — minimize supports where possible
5. Click **Slice Now**
6. Review layer preview — pay special attention to first layer, supports, and bridging
7. Export: **File → Export → Export G-code**
8. Save to SD card or upload to OctoPrint/Mainsail

### 1.4 Slicer Start/End G-code

The **start G-code** is custom code that runs at the beginning of every print. For Klipper machines, use macros:

**Klipper start G-code in slicer:**
```gcode
START_PRINT BED_TEMP={first_layer_bed_temperature[0]} EXTRUDER_TEMP={first_layer_temperature[0]}
```

> 💡 **How this works:** OrcaSlicer resolves `{first_layer_bed_temperature[0]}` to the actual number you set (e.g., `60`), so the printer receives `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=200`. The macro then reads `params.BED_TEMP` and `params.EXTRUDER_TEMP`. The placeholder names in curly braces are OrcaSlicer variables — they are **not** what the printer sees. If you use PrusaSlicer instead, the placeholder names differ: use `{first_layer_bed_temperature}` (no index) and `{first_layer_temperature[0]}`.

**Klipper end G-code in slicer:**
```gcode
END_PRINT
```

**The actual macros are defined in `printer.cfg` or `macros.cfg`** — the slicer just calls them by name.

**Example START_PRINT macro (Klipper):**
```ini
[gcode_macro START_PRINT]
gcode:
    {% set BED_TEMP = params.BED_TEMP|default(60)|float %}
    {% set EXTRUDER_TEMP = params.EXTRUDER_TEMP|default(200)|float %}
    
    # Pre-heat without full temp (prevent ooze during homing)
    M140 S{BED_TEMP}        ; Set bed temp
    M104 S150               ; Set hotend to 150°C (no ooze)
    
    G28                     ; Home all axes
    BED_MESH_CALIBRATE      ; Run bed mesh
    
    # Heat to full temp
    M190 S{BED_TEMP}        ; Wait for bed temp
    M109 S{EXTRUDER_TEMP}   ; Wait for hotend temp
    
    # Purge line
    G0 X5 Y5 Z0.3 F3000
    G1 X80 E15 F1500        ; Extrude purge line
    G1 Z2 F3000
    G92 E0                  ; Reset extruder position
```

**Example END_PRINT macro:**
```ini
[gcode_macro END_PRINT]
gcode:
    G91                     ; Relative positioning
    G1 Z10 F3000            ; Lift Z 10mm
    G90                     ; Absolute positioning
    G0 X0 Y300 F6000        ; Park head at rear
    M104 S0                 ; Turn off hotend
    M140 S0                 ; Turn off bed
    M84                     ; Disable motors
```

**CANCEL_PRINT macro (required — do not use emergency stop for mid-print cancellation):**
```ini
[gcode_macro CANCEL_PRINT]
rename_existing: BASE_CANCEL_PRINT
gcode:
    {% set max_z = printer.toolhead.axis_maximum.z %}
    {% set act_z = printer.toolhead.position.z %}
    {% if act_z < (max_z - 10) %}
        G91
        G1 Z10 F3000        ; Lift Z 10mm to clear the part
        G90
    {% endif %}
    G1 E-2 F1800            ; Retract 2mm to reduce ooze
    G0 X0 Y{printer.toolhead.axis_maximum.y} F6000  ; Park head at rear
    M104 S0                 ; Turn off hotend
    M140 S0                 ; Turn off bed
    M84                     ; Disable motors
    BASE_CANCEL_PRINT       ; Call Klipper's built-in cancel
```

> ⚠️ **Always use `CANCEL_PRINT`, not the emergency stop button**, when cancelling a print cleanly. `CANCEL_PRINT` retracts, lifts, parks, and cools before stopping. Emergency stop cuts power immediately — motors remain at position with the hot nozzle contacting the print surface.

---

## 2. OctoPrint

**OctoPrint** is a web-based print server that runs on a Raspberry Pi. It lets you upload G-code, start prints, monitor via webcam, and control the printer from any device on the network.

### 2.1 Accessing OctoPrint

1. Ensure your laptop is on the same network as the Raspberry Pi.
2. Open a browser and navigate to the Pi's IP address (e.g., `http://192.168.1.101`).
3. Log in with your credentials.
4. The OctoPrint dashboard shows printer status, temperature graphs, and file list.

### 2.2 OctoPrint Interface Overview

```
┌─────────────────────────────────────────────────────────────┐
│  [Temperature]  [Control]  [Terminal]  [Timelapse]          │
│                                                             │
│  Temperatures: Hotend: 200°C / Bed: 60°C                   │
│                                                             │
│  [Upload G-code]  [File List with Print/Delete]             │
│                                                             │
│  [Webcam Feed]                   [Progress Bar]             │
│                                                             │
│  Job: snowflake_bracket.gcode    ETA: 1h 23m               │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Uploading and Starting a Print

1. Click **Upload** (folder icon) — select G-code file.
2. File appears in the file list with estimated print time.
3. Click the **print** icon (▶) next to the file.
4. OctoPrint sends heating commands → printer heats up → print begins.
5. Monitor temperature graph — hotend and bed should reach target within 3–5 minutes.

### 2.4 Useful OctoPrint Plugins

| Plugin | Purpose |
|--------|---------|
| **OctoEverywhere** | Remote access from outside your local network (securely) |
| **Bed Visualizer** | Visualize BLTouch mesh as a 3D heatmap |
| **PrintTimeGenius** | More accurate print time estimation |
| **Octolapse** | Timelapse generation synchronized with layer changes |
| **FilamentManager** | Track filament usage and remaining spool weight |
| **MQTT (Message Queuing Telemetry Transport)** | Integration with home automation / Fracktory |

### 2.5 OctoPrint Terminal — Direct Commands

The **Terminal** tab lets you send G-code commands directly:

```gcode
M105           ; Query current temperatures
M503           ; Report all EEPROM settings (Marlin)
G28            ; Home all axes
G0 X150 Y150 Z10  ; Move to center, 10mm height
M104 S200      ; Set hotend to 200°C (don't wait)
M109 S200      ; Set hotend to 200°C (wait until reached)
M140 S60       ; Set bed to 60°C
M190 S60       ; Set bed to 60°C (wait)
M84            ; Disable all steppers
```

---

## 3. Mainsail and Fluidd (Klipper Interfaces)

Our Klipper-based machines (Snowflake, Dragon, Twin Dragon) use **Mainsail** or **Fluidd** — web interfaces for Klipper that are more powerful than OctoPrint for Klipper.

### 3.1 Mainsail vs. Fluidd

| Feature | Mainsail | Fluidd |
|---------|----------|--------|
| UI Design | Dark, dashboard-focused | Clean, more compact |
| Macro Panel | Yes — large buttons | Yes — sidebar |
| Config Editor | Built-in | Built-in |
| Spoolman Integration | Yes | Yes |
| Klipper Exclusive | Yes | Yes |

Both are functionally equivalent — the choice is team preference.

### 3.2 Console Commands in Mainsail/Fluidd (Klipper)

```
G28                        ; Home all
BED_MESH_CALIBRATE         ; Run auto bed level
BED_MESH_PROFILE SAVE=default  ; Save mesh profile
PROBE_CALIBRATE            ; Run Z-offset calibration
PID_CALIBRATE HEATER=extruder TARGET=200  ; PID tune hotend
PID_CALIBRATE HEATER=heater_bed TARGET=60  ; PID tune bed
SAVE_CONFIG                ; Save all calibrations to printer.cfg
FIRMWARE_RESTART           ; Restart Klipper firmware
```

---

## 4. Klipper Configuration

**Klipper** is firmware that runs on a Raspberry Pi (not on the printer board) and communicates with a low-level MCU firmware on the printer's control board via USB or serial.

### 4.1 printer.cfg Structure

```ini
# ==========================================
# PRINTER CONFIGURATION — SNOWFLAKE
# Version: 1.3 | Last Updated: 2026-04-01
# ==========================================

[printer]
kinematics: corexy         ; Machine type
max_velocity: 300          ; mm/s
max_accel: 3000            ; mm/s²
max_z_velocity: 25
max_z_accel: 30

[mcu]
serial: /dev/serial/by-id/usb-Klipper_stm32f407xx_...

[stepper_x]
step_pin: PE3
dir_pin: !PE2
enable_pin: !PE4
rotation_distance: 40
microsteps: 16
full_steps_per_rotation: 200
endstop_pin: PA15
position_min: 0
position_endstop: 0
position_max: 300
homing_speed: 50

[stepper_y]
# Similar to stepper_x...

[stepper_z]
step_pin: PB5
dir_pin: PB4
enable_pin: !PB6
rotation_distance: 8       ; Lead screw lead in mm
microsteps: 16
endstop_pin: probe:z_virtual_endstop  ; Uses BLTouch
position_max: 300
position_min: -5

[extruder]
step_pin: PD6
dir_pin: !PD5
enable_pin: !PD4
rotation_distance: 7.71    ; Calibrate this for your extruder
microsteps: 16
nozzle_diameter: 0.4
filament_diameter: 1.75
heater_pin: PE5
sensor_type: NTC 100K beta 3950
sensor_pin: PC1
min_temp: 0
max_temp: 300
pressure_advance: 0.05     ; Tune with pressure advance calibration

[heater_bed]
heater_pin: PA0
sensor_type: EPCOS 100K B57560G104F
sensor_pin: PC0
min_temp: 0
max_temp: 130
```

### 4.2 PID Tuning

**PID (Proportional-Integral-Derivative)** tuning calibrates the temperature control loop so the hotend and bed reach and maintain target temperature without oscillating.

**Why it matters:** Poorly tuned PID causes temperature swings (±5°C or more), which causes inconsistent extrusion and print artifacts.

**Hotend PID Tune:**
```
PID_CALIBRATE HEATER=extruder TARGET=200
# Wait 5–10 minutes for calibration cycles to complete
# Klipper will print: pid_kp, pid_ki, pid_kd values
SAVE_CONFIG
```

**Bed PID Tune:**
```
PID_CALIBRATE HEATER=heater_bed TARGET=60
SAVE_CONFIG
```

### 4.3 Pressure Advance (Klipper)

**Pressure Advance** compensates for the delay between extruder movement and actual filament pressure at the nozzle. Without it, corners are blobby and accelerations cause inconsistent extrusion.

**Quick calibration procedure:**
1. Print the Klipper pressure advance calibration tower (available on the Klipper docs site).
2. The tower has varying PA values printed on each level.
3. Find the level where corners are sharpest without voids.
4. Update `pressure_advance` in printer.cfg.

**Typical values:**
- PLA, direct drive: 0.04–0.08
- PETG, direct drive: 0.08–0.12
- PLA, Bowden: 0.5–1.0

---

## 5. Fracktory

**Fracktory** is a print farm management platform used to track machine status, print jobs, filament consumption, and operator assignments across all our printers.

### 5.1 Connecting Printers to Fracktory

1. Ensure the Raspberry Pi has internet access.
2. Install the Fracktory agent on the Raspberry Pi:
   ```bash
   curl -sSL https://install.fracktory.com | bash
   ```
3. Enter the API key provided by your team lead.
4. The printer will appear in the Fracktory dashboard within 2–3 minutes.

### 5.2 Fracktory Dashboard Features

| Feature | Description |
|---------|-------------|
| **Machine Overview** | Live status of all printers (idle, printing, error) |
| **Job Queue** | Assign print jobs to specific machines |
| **Filament Tracking** | Log filament usage, material type, and spool status |
| **Print History** | Complete log of all prints with start/end times and outcomes |
| **Alerts** | Email/Slack notifications on print completion or failure |
| **Analytics** | Machine uptime, failure rate, material consumption reports |

### 5.3 Logging a Print in Fracktory

1. Log in at your team's Fracktory instance.
2. Click **New Job** → fill in: model name, material, machine, estimated time.
3. Start print on the machine.
4. Mark job as **In Progress** in Fracktory.
5. On completion, mark as **Complete** and log actual print time and outcome.
6. If failed, mark as **Failed** and enter failure reason (select from dropdown).

---

## 6. Filament Storage and Drybox

Moisture is the enemy of filament. **Hygroscopic filaments** (those that absorb water from air) produce poor quality prints when wet: bubbling, stringing, weak layer bonds, and crackling sounds during extrusion.

### 6.1 Moisture Sensitivity by Material

| Material | Sensitivity | Max Air Exposure Before Issues |
|----------|------------|-------------------------------|
| PLA | Low | 24–48 hours in humid environment |
| PETG | Medium | 4–8 hours |
| ABS | Medium | 8–12 hours |
| TPU | High | 2–4 hours |
| Nylon | Very High | 30–60 minutes |
| PVA | Extreme | Absorbs in minutes — must stay in drybox |

### 6.2 How to Identify Wet Filament

- **Crackling or popping sounds** during extrusion (steam venting from moisture)
- **Bubbles in extrudate** (steam pockets)
- **Increased stringing** compared to usual
- **Rough surface finish** on prints
- **Weakened parts** — layer adhesion drops significantly

### 6.3 Drybox Setup

A **drybox** is a sealed container with desiccant (silica gel) that maintains low relative humidity (RH) to keep filament dry during printing.

**Our drybox configuration:**

| Component | Specification |
|-----------|--------------|
| Container | Airtight storage box (12L per spool) |
| Desiccant | Silica gel beads, 100–200g per box |
| Humidity indicator | Digital hygrometer inside each box |
| Target RH | < 15% RH for Nylon/PVA, < 30% RH for others |
| PTFE feedthrough | 4 mm tube fitting in lid — filament passes through without breaking the seal |

### 6.4 Drying Wet Filament

When filament has absorbed moisture, it must be dried before use.

| Material | Drying Temp | Drying Time |
|----------|------------|------------|
| PLA | 45°C | 4–6 hours |
| PETG | 55°C | 4–6 hours |
| ABS | 60°C | 4–6 hours |
| TPU | 50°C | 4–6 hours |
| Nylon | 70–80°C | 8–12 hours |
| PVA | 45°C | 6–8 hours |

**Drying methods:**
1. **Food dehydrator** — Ideal: even heat, fits multiple spools, accurate temp control
2. **Filament dryer (PrintDry, eSUN eBOX)** — Designed for filament, often has built-in active drying + storage
3. **Oven** — Use with caution: most home ovens overshoot temperature. Verify with a thermometer. Never use a microwave.

**Process:**
1. Remove spool from sealed bag.
2. Place in dryer at the correct temperature.
3. After drying, immediately transfer to drybox.
4. Let spool cool to room temperature inside the sealed box before opening.

### 6.5 Silica Gel Regeneration

Silica gel beads change color when saturated (blue → pink for indicating beads). They can be regenerated:

1. Remove beads from drybox.
2. Spread on baking sheet.
3. Bake at **90–100°C for 1–2 hours** in an oven. Do not exceed 120°C — high temperatures permanently damage silica gel bead structure and reduce absorption capacity.
4. Let cool to room temperature, then return to drybox sealed immediately.

---

## 7. Pre-Print Checklist

Run this checklist before every print:

```
PRE-PRINT CHECKLIST — ALL MACHINES
=====================================
□ Filament loaded and extruder pre-purged (10mm at print temp)
□ Filament in drybox with RH < 30% (< 15% for Nylon/PVA)
□ Build surface clean (wiped with 90%+ IPA, no fingerprints)
□ Previous print removed, surface inspected for damage
□ G28 (home all axes) completed successfully
□ Bed mesh run (or last mesh < 12 hours old for same surface)
□ Z-offset verified with paper test or last known good value
□ First-layer preview reviewed in slicer
□ Print start G-code verified in slicer profile
□ Correct material profile selected
□ Temperature settings match material
□ Machine logged in Fracktory (new job created)
□ Webcam positioned for monitoring
```

---

## ❌ Common Mistakes

| Mistake | What Happens | Correct Practice |
|---------|-------------|------------------|
| Layer height > 75% of nozzle diameter | Under-extrusion, poor layer adhesion | Max: 0.30 mm for 0.4 mm nozzle; 0.45 mm for 0.6 mm nozzle (Dragon) |
| Wrong retraction length for extruder type | Stringing (too low) or clogs (too high) | Direct drive: 0.5–1.5 mm. Bowden (Dragon): 1.5–3.0 mm |
| `START_PRINT` called without temperature parameters | Printer homes and prints cold | Slicer start G-code must pass `BED_TEMP` and `EXTRUDER_TEMP` parameters |
| Slicing with wrong nozzle diameter in profile | Over/under-extrusion despite correct settings | Verify: 0.4 mm (Snowflake/Julia/Twin Dragon), 0.6 mm (Dragon) |
| No supports on overhangs > 45° | Drooping bridges, failed geometry | Enable auto-supports for any overhang exceeding 45° |
| No skirt on first print with new filament | Nozzle starts model with air or oxidised filament | Add 3-loop skirt to prime nozzle before model begins |
| Printing wet filament | Bubbling, stringing, weak layers, steam popping sounds | Dry to spec (see drybox table) before printing |
| Not logging print in Fracktory | No audit trail for failures; team loses diagnostic context | Log every print job — machine, operator, material, spool ID |
| Running PID tune at room temperature | PID values don't match operating conditions | Run `PID_CALIBRATE` with the printer fully warmed up |

---

## 8. Hands-On Exercises

### Exercise 5.1 — Slicing
- [ ] Import a provided STL file into OrcaSlicer
- [ ] Slice for Julia (PLA, 0.20 mm, 20% Gyroid infill)
- [ ] Review layer preview — identify the number of layers and estimated time
- [ ] Export G-code and verify the start/end macros are correct

### Exercise 5.2 — OctoPrint / Mainsail
- [ ] Access Mainsail for Snowflake via browser
- [ ] Upload a G-code file and start a test print
- [ ] Monitor the temperature graph for the first 5 minutes
- [ ] Cancel the print using the emergency stop, then resume a new print correctly

### Exercise 5.3 — Klipper Macros
- [ ] Read the `macros.cfg` file on Snowflake via SSH
- [ ] Identify the START_PRINT and END_PRINT macros
- [ ] Run `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=200` from the Mainsail console
- [ ] Observe the sequence of operations and verify each step completes

### Exercise 5.4 — PID Tuning
- [ ] Run `PID_CALIBRATE HEATER=extruder TARGET=200` on Julia
- [ ] Record the PID values before and after
- [ ] Verify temperature stability by checking the temperature graph for ±1°C tolerance

### Exercise 5.5 — Drybox
- [ ] Check the humidity level in each drybox (should be documented on a log sheet)
- [ ] Identify any spool that has been open > 24 hours and assess for drying
- [ ] Load a spool of PETG through the drybox feedthrough correctly

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [OrcaSlicer Complete Guide](https://www.youtube.com/watch?v=RYRPvb5BI2o) | Softfever (OrcaSlicer) | Official tutorial covering all key features |
| [Klipper Setup from Scratch](https://www.youtube.com/watch?v=8vkM2Yoy7-M) | Ellis's Print Tuning | Complete Klipper install and config guide |
| [Pressure Advance Calibration](https://www.youtube.com/watch?v=MkpCuFVq6aE) | Teaching Tech | Step-by-step pressure advance tuning |
| [Filament Moisture — Why It Matters](https://www.youtube.com/watch?v=FAXUjZZER5E) | CNC Kitchen | Scientific test showing impact of moisture on print strength |
| [OctoPrint Setup and Plugins](https://www.youtube.com/watch?v=HBd0olxI-No) | Teaching Tech | OctoPrint install, config, and best plugins |

---

## 📚 Further Reading

- [Klipper Documentation](https://www.klipper3d.org/Overview.html) — Complete official Klipper reference
- [Ellis's Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/) — The most comprehensive Klipper print quality tuning guide available
- [OrcaSlicer Wiki](https://github.com/SoftFever/OrcaSlicer/wiki) — All OrcaSlicer features and calibration tools
- [OctoPrint Plugin Repository](https://plugins.octoprint.org/) — Browse all OctoPrint plugins
- [Filament Drying Guide — CNC Kitchen](https://www.cnckitchen.com/blog/how-to-dry-your-filament) — Data-backed filament drying research

---

## ✅ Knowledge Check

1. What does pressure advance compensate for, and what print defect does it prevent at corners?
2. A PETG print is making crackling sounds during extrusion. What is the likely cause and what immediate action do you take?
3. The temperature graph for Snowflake's hotend shows ±8°C oscillation around 200°C. What calibration procedure do you run?
4. Write the OrcaSlicer start G-code for a Klipper machine that passes bed and extruder temperatures to the START_PRINT macro.
5. Twin Dragon is in Duplication Mode. Describe what both heads do and when you would use this mode.
6. What is the target relative humidity inside a drybox when storing Nylon filament?
7. A print in Fracktory shows as "In Progress" but the machine is idle. What steps do you take?

---

*Module 5 of 6 — [Back to Index](README.md)*
