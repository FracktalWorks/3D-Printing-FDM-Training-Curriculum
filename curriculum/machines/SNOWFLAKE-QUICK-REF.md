# Snowflake — Machine Quick Reference

> One-page cheat sheet for daily operation, calibration, and first-line troubleshooting.
> Keep this open during any Snowflake maintenance or setup session.

---

## Hardware Specs

| Item | Value |
|------|-------|
| **Motion System** | CoreXY |
| **Build Volume** | 200 × 200 × 200 mm |
| **Machine Dimensions** | 572 × 300 × 456 mm |
| **Control Board** | MKS Eagle V1.0 |
| **Firmware** | Marlin |
| **Stepper Drivers** | TMC2209 (onboard MKS Eagle) |
| **Extruder** | Dual-Gear Drive (direct drive) |
| **Max Hotend Temp** | 265°C |
| **Max Bed Temp** | 100°C |
| **Bed Surface** | PEI flexible build plate |
| **Auto-leveling** | Load Cell Bed Levelling (no external probe) |
| **Display** | 2.8-inch LCD Dial Display |
| **Connectivity** | USB, LAN |
| **Power** | 500 W |
| **Net Weight** | 16 kg |
| **Network** | `192.168.1.101` (LAN — for file transfer / SD card access) |

---

## Marlin G-code Commands

```
G28                          → Home all axes
G29                          → Run auto bed leveling (Load Cell mesh)
M48                          → Probe repeatability test (should be < 0.01 mm deviation)
M303 E0 S210 C8              → PID auto-tune hotend at 210°C (8 cycles)
M303 E-1 S60 C8              → PID auto-tune bed at 60°C (8 cycles)
M851                         → Report/set Z probe offset
M500                         → Save all settings to EEPROM
M503                         → Print all current EEPROM settings
M119                         → Report all endstop states
M112                         → EMERGENCY STOP
```

---

## Pre-Print Checklist (Snowflake)

```
□ Bed surface clean — wipe with 90%+ IPA, no fingerprints
□ PEI sheet seated on magnetic base (no lifted edges)
□ G28 completed without errors
□ Bed mesh run — or last mesh < 12 hours old on same surface
□ Z-offset verified — paper test shows slight drag, no gouge
□ Filament loaded and purged — fresh extrusion, no air gaps
□ Filament in drybox — RH < 30%
□ Webcam positioned for monitoring
□ Print job logged in Fracktory
```

---

## Material Quick Settings (Snowflake)

| Material | Hotend | Bed | Cooling | Retraction | Notes |
|----------|--------|-----|---------|-----------|-------|
| PLA | 210°C | 60°C | 100% | 0.8 mm / 50 mm/s | Standard profile |
| PETG | 240°C | 75°C | 40% | 1.2 mm / 40 mm/s | No blobs profile |
| ABS | 245°C | 105°C | 0% | 0.8 mm / 50 mm/s | Use enclosure cover |
| TPU 95A | 230°C | 40°C | 30% | 0.5 mm / 25 mm/s | Slow speed |
| Nylon PA12 | 265°C | 80°C | 0% | 1.0 mm / 40 mm/s | Must be bone-dry |

---

## Load Cell Bed Levelling — Calibration

Snowflake uses **Load Cell Bed Levelling** (sensor built into the print head — no external probe hardware).

- **Run bed mesh:** Send `G29` — machine probes 25 points and builds a compensation mesh
- **Check Z offset:** `M851` (report current Z offset) → adjust via LCD → Settings → Z Offset
- **Test repeatability:** Send `M48` — deviation should be < 0.01 mm
- **Save settings:** `M500` after any Z offset or calibration change

> ⚠️ After any nozzle swap, re-run `G29` and verify Z offset. Save with `M500`.

---

## Monthly Calibration Schedule

| Task | Command | Frequency |
|------|---------|-----------|
| Z-offset drift check | `M851` → adjust via LCD → `M500` | Monthly or after nozzle swap |
| PID tune — hotend | `M303 E0 S210 C8` then `M500` | If temp oscillation > ±3°C |
| PID tune — bed | `M303 E-1 S60 C8` then `M500` | If temp oscillation > ±2°C |
| Bed mesh | `G29` | After bed surface change |
| Belt tension check | Gates app (120–150 Hz) | Monthly |
| E-steps calibration | Mark + extrude + measure → `M92 E<steps>` → `M500` | After extruder service |

---

## Top 5 Known Failure Modes

| # | Symptom | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | Load cell levelling fails / inconsistent | Debris on bed surface or nozzle tip | Clean nozzle and bed; re-run `G29` |
| 2 | Layer shift after long infill run | Loose belt — check X/Y belt tension | Re-tension belts (Gates app 120–150 Hz target) |
| 3 | Z-offset drifts between sessions | Thermal expansion of frame | Re-verify Z offset at print temperature; save with `M500` |
| 4 | Extruder clicking at high speeds | Linear Advance misconfigured or excessive speed | Reduce print speed 10%; tune `M900 K<value>` (Linear Advance) |
| 5 | Serial communication error (host software drops) | USB cable or baud rate mismatch | Use shielded USB cable; set baud to 250000 in host software |

---

## USB / Serial Access

Snowflake runs **Marlin firmware** — no SSH or Raspberry Pi required. Control the printer via:

- **LCD Dial Display** (on-machine): Navigate menus to start prints, set temperatures, run `Auto Home`, `Auto Bed Leveling`, adjust Z offset
- **USB serial** (host computer): Connect with a host program (Pronterface, Repetier-Host, or Cura)
  - Baud rate: **250000**
  - Select the correct COM port in the host software
- **SD card**: Save `.gcode` from Fracktory → insert SD card → LCD → Print → select file
- **LAN (file transfer)**: `192.168.1.101` — used for G-code file transfer only (not a web interface)

---

## Wiring Reference

| Connection | Board Pin | Connector |
|-----------|----------|---------|
| X Motor | X-MOTOR port | Molex 4-pin |
| Y Motor | Y-MOTOR port | Molex 4-pin |
| Z Motor | Z-MOTOR port | Molex 4-pin |
| Extruder Motor | E0-MOTOR port | Molex 4-pin |
| Hotend Heater | HE0 | XT30 |
| Hotend Thermistor | T0 | JST-XH 2-pin |
| Bed Heater | HB | XT60 |
| Bed Thermistor | TB | JST-XH 2-pin |
| Load Cell (bed probe) | LOAD-CELL port | JST-XH 4-pin |
| Part Cooling Fan | FAN0 | JST-XH 2-pin |
| Hotend Fan | FAN1 | JST-XH 2-pin |
| X Endstop | X-STOP | JST-XH 3-pin |
| Y Endstop | Y-STOP | JST-XH 3-pin |

---

*See full wiring schematic in `machines/wiring/snowflake-wiring-v1.pdf`*
*[Back to Curriculum Index](../README.md)*
