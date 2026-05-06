# Snowflake — Machine Quick Reference

> One-page cheat sheet for daily operation, calibration, and first-line troubleshooting.
> Keep this open during any Snowflake maintenance or setup session.

---

## Hardware Specs

| Item | Value |
|------|-------|
| **Motion System** | CoreXY |
| **Build Volume** | 300 × 300 × 300 mm |
| **Control Board** | MKS Monster8 (STM32F407) |
| **Firmware** | Klipper + Mainsail |
| **Stepper Drivers** | TMC2209 (UART, stealthChop) |
| **Extruder** | Direct Drive |
| **Max Hotend Temp** | 300°C |
| **Max Bed Temp** | 110°C |
| **Bed Surface** | PEI spring-steel (magnetic) |
| **Auto-leveling** | BLTouch |
| **Host** | Raspberry Pi 4 (Mainsail) |
| **Network** | `http://192.168.1.101` (or `http://snowflake`) |

---

## Klipper Console — Essential Commands

```
G28                          → Home all axes
BED_MESH_CALIBRATE           → Run 5×5 auto bed leveling mesh
PROBE_CALIBRATE              → Interactive Z-offset calibration
PID_CALIBRATE HEATER=extruder TARGET=200   → PID tune hotend at 200°C
PID_CALIBRATE HEATER=heater_bed TARGET=60  → PID tune bed at 60°C
SAVE_CONFIG                  → Write calibration results to printer.cfg
FIRMWARE_RESTART             → Reload printer.cfg without rebooting Pi
QUERY_ENDSTOPS               → Check all endstop states
SHAPER_CALIBRATE             → Re-tune resonance compensation (InputShaper)
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

## BLTouch Probe Offsets

```
X offset: -38.0 mm    (probe is 38 mm LEFT of nozzle)
Y offset:  +3.0 mm    (probe is 3 mm BEHIND nozzle)
Z offset:  1.45 mm    (verify with PROBE_CALIBRATE — update as needed)
```

> ⚠️ After any nozzle swap or BLTouch re-mount, re-run `PROBE_CALIBRATE` and `SAVE_CONFIG`.

---

## Monthly Calibration Schedule

| Task | Command | Frequency |
|------|---------|-----------|
| Z-offset drift check | `PROBE_CALIBRATE` | Monthly or after nozzle swap |
| PID tune — hotend | `PID_CALIBRATE HEATER=extruder TARGET=200` | If oscillation > ±3°C |
| PID tune — bed | `PID_CALIBRATE HEATER=heater_bed TARGET=60` | If oscillation > ±2°C |
| Bed mesh | `BED_MESH_CALIBRATE` | After bed surface change |
| Belt tension check | Gates app (120–150 Hz) | Monthly |
| InputShaper re-tune | `SHAPER_CALIBRATE` | After any mechanical change |
| E-steps / rotation_distance | Mark + extrude + measure | After extruder service |

---

## Top 5 Known Failure Modes

| # | Symptom | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | BLTouch fails to deploy | Probe pin stuck (filament debris in sleeve) | Clean sleeve with IPA; send `BLTOUCH_DEBUG COMMAND=reset` |
| 2 | Layer shift after long infill run | InputShaper needs recalibration | Run `SHAPER_CALIBRATE` after any mechanical change |
| 3 | Z-offset drifts between sessions | Thermal expansion of frame | Re-run `PROBE_CALIBRATE` at print temperature every session |
| 4 | Extruder clicking at high speeds | Pressure advance misconfigured | Reduce `pressure_advance` to 0.04, re-calibrate |
| 5 | Klipper "MCU timeout" error | USB connection issue | Replace USB cable (shielded data cable); restart Pi |

---

## SSH Access

```bash
ssh pi@192.168.1.101
# Or using SSH config alias:
ssh snowflake

# Klipper config location:
~/printer_data/config/printer.cfg

# Restart Klipper:
sudo systemctl restart klipper

# View live Klipper log:
tail -f ~/printer_data/logs/klippy.log
```

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
| BLTouch (5-wire) | SERVO + Z-PROBE | JST-XH 5-pin |
| Part Cooling Fan | FAN0 | JST-XH 2-pin |
| Hotend Fan | FAN1 | JST-XH 2-pin |
| X Endstop | X-STOP | JST-XH 3-pin |
| Y Endstop | Y-STOP | JST-XH 3-pin |

---

*See full wiring schematic in `machines/wiring/snowflake-wiring-v1.pdf`*
*[Back to Curriculum Index](../README.md)*
