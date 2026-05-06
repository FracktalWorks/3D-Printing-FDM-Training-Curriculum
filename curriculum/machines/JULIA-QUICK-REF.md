# Julia — Machine Quick Reference

> ⚠️ **ARCHIVED / NOT IN CURRENT FLEET** — Julia is not part of the current Fracktal Works machine lineup. No official manual is available.
> This file is retained for historical reference only. For current machines, refer to [Snowflake](SNOWFLAKE-QUICK-REF.md), [Dragon](DRAGON-QUICK-REF.md), or [Twin Dragon](TWIN-DRAGON-QUICK-REF.md).

---

## Hardware Specs

| Item | Value |
|------|-------|
| **Motion System** | CoreXY (compact) |
| **Build Volume** | 250 × 250 × 250 mm |
| **Control Board** | MKS Robin Nano V3 (STM32F407) |
| **Firmware** | Marlin |
| **Stepper Drivers** | TMC2208 (UART) |
| **Extruder** | Direct Drive |
| **Max Hotend Temp** | 280°C |
| **Max Bed Temp** | 100°C |
| **Bed Surface** | Textured PEI spring-steel (magnetic) |
| **Auto-leveling** | CR Touch (optical + mechanical) |
| **Host** | Raspberry Pi 4 (Fluidd) |
| **Network** | `http://192.168.1.102` (or `http://julia`) |

---

## Klipper Console — Essential Commands

```
G28                          → Home all axes
BED_MESH_CALIBRATE           → Run 4×4 auto bed leveling mesh
PROBE_CALIBRATE              → Interactive Z-offset calibration
PID_CALIBRATE HEATER=extruder TARGET=215   → PID tune hotend at 215°C
PID_CALIBRATE HEATER=heater_bed TARGET=60  → PID tune bed at 60°C
SAVE_CONFIG                  → Write calibration results to printer.cfg
FIRMWARE_RESTART             → Reload printer.cfg without rebooting Pi
QUERY_ENDSTOPS               → Check all endstop states
M112                         → EMERGENCY STOP
```

---

## Pre-Print Checklist (Julia)

```
□ Bed surface clean — wipe with 90%+ IPA, no fingerprints
□ PEI spring-steel seated magnetically (check all 4 corners are flat)
□ G28 completed without errors
□ CR Touch functional — pin deploys and retracts cleanly
□ Bed mesh run — or last mesh < 12 hours old on same surface
□ Z-offset verified — paper test shows slight drag, no gouge
□ Filament loaded and purged — no air gaps in Bowden path
□ Filament RH < 30% (use moisture card in drybox)
□ Print job logged in Fracktory
```

---

## Material Quick Settings (Julia)

| Material | Hotend | Bed | Cooling | Retraction | Notes |
|----------|--------|-----|---------|-----------|-------|
| PLA | 210°C | 60°C | 100% | 3.0 mm / 50 mm/s | Standard profile |
| PETG | 235°C | 75°C | 40% | 4.0 mm / 35 mm/s | Watch for ooze |
| ABS | 245°C | 100°C | 0% | 3.5 mm / 45 mm/s | Close Julia's enclosure |
| TPU 95A | 225°C | 40°C | 30% | 0 mm / 25 mm/s | Disable retraction |

> **Note:** Julia uses Bowden-style extrusion path — retraction values are higher than Snowflake (direct drive).

---

## CR Touch Probe Offsets

```
X offset: -42.0 mm    (probe is 42 mm LEFT of nozzle)
Y offset:  +5.0 mm    (probe is 5 mm BEHIND nozzle)
Z offset:  2.2 mm     (verify with PROBE_CALIBRATE — update as needed)
```

> ⚠️ CR Touch trigger distance should be 2.5–3.0 mm. If > 3.5 mm, clean the optical lens with compressed air.

---

## Monthly Calibration Schedule

| Task | Command | Frequency |
|------|---------|-----------|
| Z-offset drift check | `PROBE_CALIBRATE` | Monthly or after nozzle swap |
| CR Touch lens clean | Compressed air puff at lens | Monthly |
| PID tune — hotend | `PID_CALIBRATE HEATER=extruder TARGET=215` | If oscillation > ±5°C |
| PID tune — bed | `PID_CALIBRATE HEATER=heater_bed TARGET=60` | If oscillation > ±3°C |
| Bed mesh | `BED_MESH_CALIBRATE` | After bed surface change |
| Belt tension check | Gates app (120–150 Hz) or 2–3 mm deflection | Monthly |
| Bowden tube inspection | Visual check for kinks, discoloration | Monthly |
| Corner spring check | Manual press — bed should spring back flat | Monthly |

---

## Top 5 Known Failure Modes

| # | Symptom | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | CR Touch won't trigger / Z stuck | Dust on optical lens | Clean lens with compressed air — never touch with fingers |
| 2 | Z-banding (horizontal lines in print) | Worn Z-coupler or bent leadscrew | Inspect coupler, replace if has >0.5 mm runout |
| 3 | Filament jam in Bowden path | PTFE tube kinked or ID < 3.5 mm | Pull Bowden tube, inspect; replace if kinked |
| 4 | Heated bed heats slowly | PSU voltage sagging or thin wiring | Measure PSU output — should be ≥ 23.5V at bed connector |
| 5 | Corner not adhering | Bed spring fatigue (500+ prints) | Replace corner bed springs; also check frame squareness |

---

## SSH Access

```bash
ssh pi@192.168.1.102
# Or using SSH config alias:
ssh julia

# Klipper config location:
~/printer_data/config/printer.cfg

# Restart Klipper:
sudo systemctl restart klipper

# View live Klipper log:
tail -f ~/printer_data/logs/klippy.log
```

---

## Julia: Key Differences vs. Snowflake

| Feature | Snowflake | Julia |
|---------|-----------|-------|
| Board | MKS Monster8 | MKS Robin Nano V3 |
| Drivers | TMC2209 | TMC2208 (lower power) |
| Probe | BLTouch | CR Touch |
| Web UI | OctoPrint | OctoPrint |
| Max temp | 300°C | 280°C |
| Build volume | 300³ | 250³ |
| Current budget | Higher | Lower — `run_current` max 0.8 A |

---

## Wiring Reference

| Connection | Board Pin | Connector |
|-----------|----------|---------|
| X Motor | X-MOTOR | Molex 4-pin |
| Y Motor | Y-MOTOR | Molex 4-pin |
| Z Motor | Z-MOTOR | Molex 4-pin |
| Extruder Motor | E0-MOTOR | Molex 4-pin |
| Hotend Heater | HE0 | XT30 |
| Hotend Thermistor | T0 | JST-XH 2-pin |
| Bed Heater | HB | XT60 |
| Bed Thermistor | TB | JST-XH 2-pin |
| CR Touch (5-wire) | SERVO + Z-PROBE | JST-XH 5-pin |
| Part Cooling Fan | FAN0 | JST-XH 2-pin |
| Hotend Fan | FAN1 | JST-XH 2-pin |

---

*See full wiring schematic in `machines/wiring/julia-wiring-v1.pdf`*
*[Back to Curriculum Index](../README.md)*
