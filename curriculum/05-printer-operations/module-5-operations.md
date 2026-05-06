# Module 5: Printer Operations — Slicing, Wi-Fi Printing, Klipper, and Drybox

> End-to-end operational knowledge for running production-quality prints — from loading filament and slicing a model with Fracktory to monitoring jobs remotely via OctoPrint, configuring Klipper macros, and maintaining filament quality with a drybox.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Slice a 3D model with correct settings for each of our three machines (Snowflake, Dragon, Twin Dragon)
- Start, monitor, and manage print jobs via Fracktory and OctoPrint
- Configure and use Klipper macros for common operations (START_PRINT, END_PRINT)
- Set up and use the drybox system to prevent moisture-related print failures
- Use Fracktory for Wi-Fi print sending and machine status tracking
- Perform PID tuning for hotend and heated bed
- Understand and apply key slicer parameters (layer height, infill, supports, speeds)

## Prerequisites

- Module 3: Software Tools
- Module 4: Printer Basics

---

## 🛠️ Tools Required

| Tool | Purpose |
|------|---------|
| Fracktory Slicer (latest) | Primary slicer for all Fracktal machines — download: http://printers.fracktory.in/download |
| Browser (Chrome/Firefox) | OctoPrint web interface (Dragon, Twin Dragon) |
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
2. **Don't leave prints unattended overnight without alerts.** Configure OctoPrint temperature alerts or Fracktory notifications before leaving the lab.
3. **Drying filament in a kitchen oven:** Use a standalone thermometer to verify actual temperature. Oven thermostats are often off by ±20°C — too hot deforms the spool.
4. **Never slice with incorrect bed dimensions.** A print that exceeds bed bounds will crash the carriage into the frame at full speed.
5. **Verify `START_PRINT` macro parameter names match the slicer's output.** A mismatch causes the macro to run cold, failing the first layer.
6. **Dragon: pre-heat the enclosure before printing ABS/PC.** Starting a high-temp print without enclosure pre-heat causes thermal shock warping on the first 10 layers.
7. **IPA for bed cleaning is flammable.** Apply IPA to a cloth, not directly to a hot bed. Vapours ignite at 13°C.

---

## 1. Slicing Fundamentals

A **slicer** converts a 3D model (STL, STEP, OBJ) into **G-code** — a text file of movement and temperature commands that the printer executes.

### 1.1 Fracktory Slicer — Our Primary Tool

**Fracktory** is a free, Fracktal-customised slicer built on top of the industry-standard open-source Cura engine. It comes pre-configured with printer profiles and material settings specifically tuned for Fracktal machines (Snowflake, Dragon, Twin Dragon).

| Feature | Detail |
|---------|--------|
| **Download** | http://printers.fracktory.in/download |
| **Platform** | Windows (Vista+, 64-bit), macOS (10.11+), Linux (Ubuntu 14.04+) |
| **RAM** | 4 GB minimum |
| **OpenGL** | 2.0 minimum (4.1 for 3D layer view) |
| **Based on** | Ultimaker Cura (open source) |
| **Pre-loaded profiles** | Snowflake, Dragon (400/500/700), Twin Dragon (300/400/600) |

**Why Fracktory instead of generic slicers?**
- Machine profiles are pre-configured with correct bed size, nozzle diameter, and max temperatures — no manual setup required.
- Material profiles are validated against Fracktal's own material compatibility sheet.
- Start/end G-code and Wi-Fi printing workflow are pre-set for each machine.

**Recommended for our machines: Fracktory Slicer (all machines)**

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

### 1.3 Generating G-code in Fracktory

1. Open Fracktory — on first launch, select your printer model from the list (Snowflake, Dragon 400/500/700, Twin Dragon 300/400/600).
2. Click the **Open File** button (top-left) and select your STL or 3MF file.
3. The model loads onto the virtual build plate at the correct bed dimensions for your machine.
4. **Material assignment:** Click the material dropdown on the right sidebar → select the material you have loaded.
5. **Nozzle diameter:** Match the nozzle installed on your printer (0.4 mm default, 0.6 mm or 0.8 mm for Dragon/Twin Dragon).
6. Adjust orientation — minimize supports where possible (auto-orient button available).
7. Click **Slice** — Fracktory computes layers, paths, and support structures.
8. Review the layer preview — pay attention to first layer coverage, support placement, and bridge spans.
9. **Save/Print:**
   - Save to USB stick and walk it to the printer, OR
   - Use **Wi-Fi Printing** (see Section 5.2 of Dragon/Twin Dragon manuals) to send directly to the printer's web interface.

### 1.4 Slicer Start/End G-code

The **start G-code** is custom code that runs at the beginning of every print. For Klipper machines, use macros:

**Fracktory start G-code (pre-configured for Fracktal machines):**
```gcode
START_PRINT BED_TEMP={material_bed_temperature} EXTRUDER_TEMP={material_print_temperature}
```

> 💡 **How this works:** Fracktory (Cura-based) resolves `{material_bed_temperature}` to the actual number from the material profile (e.g., `60`), so the printer receives `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=210`. The Klipper macro then reads `params.BED_TEMP` and `params.EXTRUDER_TEMP`. These curly-brace placeholders are Fracktory variables resolved at slice time — the printer only sees the resolved values. **Do not change the start G-code unless you understand Klipper macro parameter passing.**

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

## 2. Wi-Fi Printing with Fracktory

All Fracktal Works machines support **Wi-Fi printing** directly from the Fracktory slicer. After slicing, click **Print over Network** — Fracktory uploads the G-code to the printer via its IP address.

### 2.1 Network Setup

Ensure your laptop is on the same Wi-Fi or LAN as the printers. Default IP addresses:

| Machine | IP Address | Web Interface |
|---------|-----------|-------------|
| Snowflake | 192.168.1.101 | File transfer only (Marlin — no web UI; use LCD or USB) |
| Dragon | 192.168.1.103 | http://192.168.1.103 (OctoPrint) |
| Twin Dragon | 192.168.1.104 | http://192.168.1.104 (OctoPrint) |

### 2.2 Printing via Fracktory (Wi-Fi)

1. Slice your model in Fracktory.
2. Click the **Print** button (top right) → select **Print over Network**.
3. Fracktory uploads the `.gcode` file to the printer (Dragon and Twin Dragon: OctoPrint interface; Snowflake: file transfer to LAN address).
4. The printer heats up and starts printing automatically.
5. Monitor progress: Dragon/Twin Dragon — open the printer's IP in a browser (OctoPrint). Snowflake — watch the LCD display.

### 2.3 Printing via USB

If Wi-Fi is unavailable:
1. Save G-code to a USB drive from Fracktory: **File → Save G-code to disk**.
2. Insert USB drive into the printer's USB port.
3. On the touchscreen: **Print → USB → select file → Start**.

### 2.4 OctoPrint Web Interface Overview (Dragon / Twin Dragon)

Open the printer's IP in any browser for full control:

```
┌─────────────────────────────────────────────────────────────┐
│  [Dashboard]  [Files]  [Config]  [Console]  [History]       │
│                                                             │
│  Temperatures: Hotend: 215°C / Bed: 60°C                   │
│                                                             │
│  [Macro Buttons: HOME_ALL | BED_MESH | CANCEL_PRINT]        │
│                                                             │
│  [Webcam Feed]                   [Progress Bar]             │
│                                                             │
│  Job: snowflake_bracket.gcode    ETA: 1h 23m               │
└─────────────────────────────────────────────────────────────┘
```

### 2.5 OctoPrint Terminal — Direct Commands

```gcode
G28                     ; Home all axes
BED_MESH_CALIBRATE      ; Run auto bed leveling
PROBE_CALIBRATE         ; Z-offset calibration
M104 S200               ; Set hotend to 200°C
M140 S60                ; Set bed to 60°C
CANCEL_PRINT            ; Cancel current print (safe — retracts and parks)
M112                    ; EMERGENCY STOP
```

---

## 3. OctoPrint (Dragon & Twin Dragon Web Interface)

Dragon and Twin Dragon use **OctoPrint** — a web interface that provides full printer control from any browser on the lab network.

### 3.1 OctoPrint Overview

| Feature | Description |
|---------|------------|
| Temperature graphs | Live hotend and bed temperatures with history |
| Macro buttons | One-click buttons for `START_PRINT`, `HOME_ALL`, `BED_MESH_CALIBRATE` |
| File manager | Upload, preview, and start G-code files |
| Config editor | Edit `printer.cfg` and `macros.cfg` directly in browser |
| Console | Direct Klipper command input |
| Camera feed | Live webcam (if installed) |

### 3.2 Terminal Commands in OctoPrint (Klipper)

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

### 5.1 What Fracktory Does

**Fracktory** serves two roles in our lab:
1. **Slicer** — The desktop application used to slice STL files and send print jobs to the machine (covered in Section 1).
2. **Print management platform** — Tracks job history, filament usage, and machine status.

**Download the latest Fracktory slicer:** http://printers.fracktory.in/download

Register your machine in Fracktory during first setup — enter the serial number from the machine label to link it to your account and enable analytics.

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
- [ ] Install Fracktory from http://printers.fracktory.in/download
- [ ] On first launch, select your printer model (e.g., Snowflake or Dragon 400)
- [ ] Import a provided STL file
- [ ] Slice for Snowflake (PLA, 0.20 mm, 20% Gyroid infill)
- [ ] Review layer preview — identify the number of layers and estimated time
- [ ] Send to printer via Wi-Fi and verify the start G-code parameters

### Exercise 5.2 — OctoPrint Web Interface (Dragon)
- [ ] Open a browser and navigate to `http://192.168.1.103` (Dragon's OctoPrint)
- [ ] Identify the temperature graph, macro buttons, and terminal
- [ ] Send `G28` from the terminal and watch the axes home
- [ ] Upload a G-code file and start a test print
- [ ] Cancel the print cleanly using `CANCEL_PRINT` (not emergency stop)
- [ ] Verify the nozzle lifts, parks, and temperatures return to 0

### Exercise 5.3 — Klipper Macros
- [ ] Read the `macros.cfg` file on Dragon via SSH
- [ ] Identify the START_PRINT and END_PRINT macros
- [ ] Run `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=200` from the OctoPrint Terminal tab
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
| [Fracktory Quick Setup & Bed Calibration](https://www.youtube.com/watch?v=Tf-kSS7adt4) | Fracktal Works | Official Fracktory setup and bed calibration walkthrough |
| [Klipper Setup from Scratch](https://www.youtube.com/watch?v=8vkM2Yoy7-M) | Ellis's Print Tuning | Complete Klipper install and config guide |
| [Pressure Advance Calibration](https://www.youtube.com/watch?v=MkpCuFVq6aE) | Teaching Tech | Step-by-step pressure advance tuning |
| [Filament Moisture — Why It Matters](https://www.youtube.com/watch?v=FAXUjZZER5E) | CNC Kitchen | Scientific test showing impact of moisture on print strength |
| [OctoPrint Setup Guide](https://www.youtube.com/watch?v=RtYPbh3SPOE) | Teaching Tech | OctoPrint features and setup for 3D printers |

---

## 📚 Further Reading

- [Fracktory Software & User Manual](https://care.fracktal.in/portal/en/kb/articles/fractory-software-and-user-manual) — Official Fracktory documentation and download links
- [Fracktal Works Official Website](https://www.fracktal.in) — Hardware, software, and support for all Fracktal machines
- [Klipper Documentation](https://www.klipper3d.org/Overview.html) — Complete official Klipper reference
- [Ellis's Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/) — The most comprehensive Klipper print quality tuning guide available
- [Filament Drying Guide — CNC Kitchen](https://www.cnckitchen.com/blog/how-to-dry-your-filament) — Data-backed filament drying research

---

## ✅ Knowledge Check

1. What does pressure advance compensate for, and what print defect does it prevent at corners?
2. A PETG print is making crackling sounds during extrusion. What is the likely cause and what immediate action do you take?
3. The temperature graph for Snowflake's hotend shows ±8°C oscillation around 200°C. What calibration procedure do you run?
4. Write the Fracktory start G-code for a Klipper machine that passes bed and extruder temperatures to the START_PRINT macro.
5. Twin Dragon is in Duplication Mode. Describe what both heads do and when you would use this mode.
6. What is the target relative humidity inside a drybox when storing Nylon filament?
7. A print in Fracktory shows as "In Progress" but the machine is idle. What steps do you take?

---

*Module 5 of 6 — [Back to Index](README.md)*
