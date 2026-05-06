# Twin Dragon — Machine Quick Reference

> One-page cheat sheet for daily operation, calibration, and first-line troubleshooting.
> Twin Dragon is the only IDEX (dual-head) machine in the fleet — read IDEX mode rules carefully.
> Keep this open during any Twin Dragon maintenance or setup session.

---

## Hardware Specs

| Item | Value |
|------|-------|
| **Motion System** | CoreXY + IDEX (Independent Dual Extrusion) |
| **Build Volume** | 300 × 300 × 400 mm (TD 300) |
| **Build Volume (Duplication Mode)** | 2× 150 × 300 × 400 mm |
| **Control Board** | BIGTREETECH Manta M8P V2.0 + RP2040 toolboards T0/T1 (CAN bus) |
| **Firmware** | Klipper + OctoPrint + IDEX macros (FracktalWorks fork) |
| **Stepper Drivers** | TMC5160 (onboard Manta M8P) |
| **Extruders** | Dual BGM Direct Drive (IDEX) |
| **Max Hotend Temp** | 300°C (both heads) |
| **Max Bed Temp** | 110°C |
| **Bed Surface** | PEI flexible build plate |
| **Auto-leveling** | Yes (per-head) |
| **HEPA Filter** | Yes — captures particulates from ABS/CF/Nylon |
| **Display** | 5-inch Touchscreen |
| **Connectivity** | USB, Wi-Fi, Ethernet |
| **Host** | Raspberry Pi CM4 (OctoPrint) |
| **Network** | `http://192.168.1.104` (or `http://twin-dragon`) |

---

## IDEX Modes — Cheat Sheet

| Mode | Description | X-Travel per Head | Use Case |
|------|-------------|------------------|---------|
| **Single T0** | Only left extruder active, right parked | Full 300 mm | Single material — acts like standard printer |
| **Single T1** | Only right extruder active, left parked | Full 300 mm | Single material on right head |
| **Dual Material** | Both heads active, tool-changes as needed | Full 300 mm | Multi-material or support printing |
| **Duplication** | Both heads move in sync, print same part simultaneously | 150 mm each | 2× throughput of same part |
| **Mirror** | Heads move in X-mirror, print mirrored pairs | 150 mm each | Mirror-image part pairs |

---

## Klipper Console — Essential Commands

```
G28                          → Home all axes (both X motors)
T0                           → Switch to left extruder (head 0)
T1                           → Switch to right extruder (head 1)
BED_MESH_CALIBRATE           → Run 5×5 bed mesh with active head
PROBE_CALIBRATE              → Z-offset for active head (run for T0, then T1)
PID_CALIBRATE HEATER=extruder TARGET=200        → PID tune head 0
PID_CALIBRATE HEATER=extruder1 TARGET=200       → PID tune head 1
DUAL_NOZZLE_CALIBRATE        → Print dual tower to measure XY offset between heads
SAVE_CONFIG                  → Write calibration results to printer.cfg
FIRMWARE_RESTART             → Reload printer.cfg without rebooting Pi
QUERY_ENDSTOPS               → Check all endstop states (both X endstops shown)
M112                         → EMERGENCY STOP
```

---

## Pre-Print Checklist (Twin Dragon)

```
□ Bed surface clean — IPA wipe, no fingerprints, no filament remnants
□ Both PEI spring-steel corners flat (check all 4 corners)
□ G28 completed — both X motors homed without collision
□ T0 PROBE_CALIBRATE completed and Z-offset saved
□ T1 PROBE_CALIBRATE completed and Z-offset saved (if using dual-head)
□ XY nozzle offset calibrated within last 20 print hours
□ Both filaments loaded and purged (20 mm each, confirm flow from both)
□ Both filaments in drybox — RH < 30%
□ IDEX mode set correctly in slicer start G-code
□ Parking position macro tested (non-active head parks safely)
□ Print job logged in Fracktory with IDEX mode noted
□ Webcam positioned to see both heads
```

---

## Material Quick Settings (Twin Dragon)

| Material | Hotend T0 | Hotend T1 | Bed | Cooling | Retraction | Notes |
|----------|-----------|-----------|-----|---------|-----------|-------|
| PLA + PLA | 210°C | 210°C | 60°C | 100% | 0.8 mm / 50 mm/s | Standard dual |
| PLA + PVA (soluble support) | 210°C | 215°C | 60°C | 100% | 1.0 mm / 40 mm/s | T1 = PVA support |
| PETG + PETG | 240°C | 240°C | 75°C | 40% | 1.2 mm / 40 mm/s | Watch ooze |
| PLA + TPU | 210°C | 225°C | 50°C | 80% / 20% | 0.8 mm / 0 mm | T1 = TPU (no retract) |

---

## Dual BLTouch Probe Offsets

### Head 0 (Left Extruder)
```
X offset: -38.0 mm
Y offset:  +3.0 mm
Z offset:  1.45 mm    ← verify with PROBE_CALIBRATE for T0
```

### Head 1 (Right Extruder)
```
X offset: +38.0 mm    (probe is 38 mm RIGHT of right nozzle)
Y offset:  +3.0 mm
Z offset:  1.47 mm    ← verify with PROBE_CALIBRATE for T1 (may differ from T0)
```

> ⚠️ Head 1 Z-offset MUST be calibrated independently. Even a 0.1 mm difference between heads causes dual-material layer mismatches.

---

## Nozzle XY Offset Calibration

Nozzle offset between T0 and T1 must be measured and configured. Do this monthly or after any carriage maintenance.

**Procedure:**
1. Print a dual nozzle calibration tower (provided in `calibration-profiles/dual-tower.3mf`)
2. Measure X and Y offset between the two towers using calipers (goal: both columns perfectly aligned)
3. Update `[dual_carriage]` section in `printer.cfg`:
   ```ini
   [dual_carriage]
   axis: x
   step_pin: ...
   nozzle_diameter: 0.4
   # Update these values based on calibration measurement:
   offset_x: -0.15    # Positive = right head is shifted right
   offset_y: 0.08     # Positive = right head is shifted back
   ```
4. `SAVE_CONFIG` and `FIRMWARE_RESTART`
5. Re-print tower to verify < 0.2 mm misalignment

---

## Monthly Calibration Schedule

| Task | Command | Frequency |
|------|---------|-----------|
| T0 Z-offset | `T0` → `PROBE_CALIBRATE` | Monthly |
| T1 Z-offset | `T1` → `PROBE_CALIBRATE` | Monthly |
| Dual nozzle XY offset | Print calibration tower, measure, update cfg | Monthly |
| PID both hotends | `PID_CALIBRATE` for both HEATER and HEATER1 | If oscillation > ±3°C |
| Belt tension — both X motors | Gates app (120–150 Hz) for X0 and X1 belt | Monthly |
| Both BLTouch probes | Clean pins, deploy/retract test | Monthly |
| Parking position test | Move T0 to park, then T1 — no collision | Monthly |
| Filament path — both extruders | Inspect PTFE tubes, idler tension | Monthly |

---

## Top 5 Known Failure Modes

| # | Symptom | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | X motor desync / heads collide | Unequal belt tension on X0 vs X1 | Pluck both belts — must match in Hz; re-tension the looser one |
| 2 | Head 1 Z-offset wrong after print | T1 Z-offset not independently calibrated | Always run `T1` then `PROBE_CALIBRATE` and `SAVE_CONFIG` |
| 3 | Non-active head oozes onto model | Parking temp too high or coasting too short | Lower standby temp: `T1_STANDBY: 170`; increase coasting distance |
| 4 | Layer misalignment in Duplication Mode | Nozzle XY offset not calibrated | Re-run dual tower calibration; update `offset_x` in config |
| 5 | Filament stringing between heads | Tool change retraction inadequate | Increase retraction on tool change in `[gcode_macro T0/T1]` macro |

---

## SSH Access

```bash
ssh pi@192.168.1.104
# Or using SSH config alias:
ssh twin-dragon

# Klipper config location:
~/printer_data/config/printer.cfg

# Restart Klipper:
sudo systemctl restart klipper

# View live Klipper log:
tail -f ~/printer_data/logs/klippy.log
```

---

## Fleet Comparison Summary

| Feature | Twin Dragon | Snowflake | Julia | Dragon |
|---------|------------|-----------|-------|--------|
| Heads | **2 (IDEX)** | 1 | 1 | 1 |
| Motion | **CoreXY+IDEX** | CoreXY | CoreXY | CoreXY |
| Volume | **300×300×350** | 300³ | 250³ | 350×350×400 |
| Max temp | 300°C | 300°C | 280°C | **320°C** |
| Drive type | Direct (×2) | Direct | Direct | Bowden |
| Unique skill | **Dual material** | InputShaper | Compact | High-temp |

---

*See full wiring schematic in `machines/wiring/twin-dragon-wiring-v1.pdf`*
*[Back to Curriculum Index](../README.md)*
