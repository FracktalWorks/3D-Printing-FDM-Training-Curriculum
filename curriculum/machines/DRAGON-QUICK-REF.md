# Dragon — Machine Quick Reference

> One-page cheat sheet for daily operation, calibration, and first-line troubleshooting.
> Dragon is the high-temperature, large-format machine. Extra caution required at high-temp.
> Keep this open during any Dragon maintenance or setup session.

---

## Hardware Specs

| Item | Value |
|------|-------|
| **Motion System** | CoreXY |
| **Build Volume** | 400 × 300 × 400 mm (Dragon 400) |
| **Control Board** | BIGTREETECH Manta M8P V2.0 + RP2040 toolboard (CAN bus) |
| **Firmware** | Klipper + OctoPrint |
| **Stepper Drivers** | TMC5160 (onboard) |
| **Extruder** | Direct drive |
| **Nozzle** | 0.4 mm (standard), 0.6 mm / 0.8 mm LT/HT/HH available |
| **Max Hotend Temp** | 300°C |
| **Max Bed Temp** | 110°C |
| **Bed Surface** | PEI flexible build plate |
| **Auto-leveling** | Yes |
| **Display** | 5-inch Touchscreen |
| **Host** | Raspberry Pi CM4 (OctoPrint) |
| **Connectivity** | USB, Wi-Fi, Ethernet |
| **Network** | `http://192.168.1.103` (or `http://dragon`) |

---

## ⚠️ Dragon-Specific Safety Rules

1. **Use correct nozzle for material** — LT for PLA/PETG, HT for ABS/HIPS, HH for CF/GF filaments.
2. **Allow 60 seconds** for nozzle to stabilize at target temperature before starting a print.
3. **Filament runout sensor active** — machine will pause automatically when filament runs out.
4. **CAN bus toolboard** — do not disconnect the CAN connector from the toolboard while the machine is powered.
5. **Wi-Fi printing** — Dragon prints are sent via Fracktory (Wi-Fi) or by placing `.gcode` on USB.

---

## Klipper Console — Essential Commands

```
G28                          → Home all axes (sensor-less homing)
BED_MESH_CALIBRATE           → Run 5×5 bed mesh at print temperature
PROBE_CALIBRATE              → Interactive Z-offset calibration
HIGH_TEMP_CALIBRATE          → PID tune hotend at 300°C (high-temp specific)
PID_CALIBRATE HEATER=extruder TARGET=300   → PID tune hotend at 300°C
PID_CALIBRATE HEATER=heater_bed TARGET=100 → PID tune bed at 100°C
ENCLOSURE_PREHEAT            → Ramp enclosure to 60°C and wait for stabilization
BOWDEN_PURGE                 → Extrude 30 mm at 290°C to clear Bowden path
SAVE_CONFIG                  → Write calibration results to printer.cfg
FIRMWARE_RESTART             → Reload printer.cfg without rebooting Pi
QUERY_ENDSTOPS               → Check all endstop states
M112                         → EMERGENCY STOP
```

---

## Pre-Print Checklist (Dragon — High-Temp)

```
□ Fume extractor ON and verified running (mandatory for ABS/ASA)
□ Enclosure pre-heated to 50°C — run ENCLOSURE_PREHEAT macro
□ Safety: all flammable materials removed from 500mm radius
□ Bed surface clean — IPA wipe, dried fully before heating
□ PEI sheet flat — check corners with straightedge
□ G28 completed without errors (sensorless homing)
□ Bed mesh run AT print temperature (mesh changes with thermal expansion)
□ Z-offset verified — re-run after enclosure stabilizes
□ Bowden tube inspected — no kinks, no cracks near hot end
□ Filament: bone-dry (ABS/ASA max 1hr exposed; Nylon max 30min)
□ Print job logged in Fracktory as HIGH-TEMP run
□ Webcam + OctoPrint alerts set for remote monitoring
```

---

## Material Quick Settings (Dragon — Volcano 0.6 mm nozzle)

| Material | Hotend | Bed | Chamber | Cooling | Retraction | Notes |
|----------|--------|-----|---------|---------|-----------|-------|
| ABS | 255°C | 105°C | 50°C | 0% | 2.0 mm / 40 mm/s | Enclosure mandatory |
| ASA | 260°C | 110°C | 55°C | 0% | 2.0 mm / 40 mm/s | UV-stable ABS variant |
| PETG | 245°C | 80°C | 35°C | 40% | 2.5 mm / 35 mm/s | 0.6 mm nozzle needs de-tuning |
| PA-CF (Nylon) | 280°C | 80°C | 50°C | 0% | 1.5 mm / 40 mm/s | Must be bone-dry (< 15% RH) |
| PC (Polycarbonate) | 310°C | 120°C | 70°C | 0% | 2.0 mm / 35 mm/s | Full enclosure + max temp |
| High-Temp Resin | — | — | — | — | — | Dragon is FDM only; no resin |

> **Volcano 0.6 mm note:** Minimum layer height = 0.25 mm. Maximum volumetric flow = 15 mm³/s. Set line width = 0.72 mm in slicer.

---

## Auto-Leveling (Load Cell / BED_MESH_CALIBRATE)

Dragon uses built-in auto-leveling. Run before any new material or after bed changes:

```gcode
G28            ; home all axes
BED_MESH_CALIBRATE    ; run mesh probing
SAVE_CONFIG    ; save to printer.cfg
```

```
X offset: -35.0 mm    (probe is 35 mm LEFT of nozzle)
Y offset:  +2.0 mm    (probe is 2 mm BEHIND nozzle)
Z offset:  1.55 mm    (verify at enclosure operating temperature)
```

> ⚠️ Dragon's Z-offset drifts with thermal expansion. Always re-calibrate at operating temperature, not cold.

---

## Monthly Calibration Schedule

| Task | Command | Frequency |
|------|---------|-----------|
| Z-offset check at temp | `PROBE_CALIBRATE` at operating temp | Monthly or after nozzle swap |
| High-temp PID tune | `PID_CALIBRATE HEATER=extruder TARGET=300` | After hotend service |
| Bed mesh at temp | `BED_MESH_CALIBRATE` with bed at 110°C | After surface change |
| Volcano nozzle wear | Measure with calipers (replace > 0.64 mm) | Monthly |
| Bowden tube inspection | Visual — look for cracks, discoloration | Monthly |
| Enclosure fan test | Manual spin + airflow verify | Monthly |
| Enclosure thermostat | IR gun vs display reading ± 3°C | Monthly |
| InputShaper | `SHAPER_CALIBRATE` | After any mechanical change |

---

## Top 5 Known Failure Modes

| # | Symptom | Root Cause | Fix |
|---|---------|-----------|-----|
| 1 | Layer shift at 1+ hour into print | Thermal expansion changes Z mesh | Re-run `BED_MESH_CALIBRATE` at full operating temp; add mid-print re-probe macro |
| 2 | Bowden plug / backflow at nozzle | Retraction too large for Volcano | Reduce retraction to ≤ 2 mm; increase retraction speed to 45 mm/s |
| 3 | Volcano nozzle partial clog | Carbon deposits from high-temp | Soak in 99% IPA for 2 hours; if still clogged — replace nozzle |
| 4 | Auto-leveling probe intermittent | CAN toolboard cable loose or bad connection | Check CAN connector on toolboard, re-seat if needed |
| 5 | Stepper skip at 320°C print speed | Bowden drag increases at high temp | Reduce speed by 15%; increase `run_current` to 0.9 A |

---

## SSH Access

```bash
ssh pi@192.168.1.103
# Or using SSH config alias:
ssh dragon

# Klipper config location:
~/printer_data/config/printer.cfg

# Restart Klipper:
sudo systemctl restart klipper

# View live Klipper log:
tail -f ~/printer_data/logs/klippy.log
```

---

## Dragon vs. Other Machines

| Feature | Dragon | Snowflake | Twin Dragon |
|---------|-----------|-------------|---------------|
| Max temp | **300°C** | 265°C | 300°C |
| Nozzle (std) | **0.4 mm** | 0.4 mm | 0.4 mm |
| Build volume | **400×300×400 mm** | 200×200×200 mm | 300×300×400 mm (TD 300) |
| Enclosure | No (open frame) | No | No |
| Drive type | **Direct drive** | Dual-Gear Direct | BGM Direct Drive (IDEX) |
| Firmware | **Klipper** | Marlin | Klipper |
| Board | Manta M8P V2.0 | Manta M8P V2.0 | Manta M8P V2.0 |
| Max Speed | **600 mm/s** (Dragon 400) | 150 mm/s | 500 mm/s |

---

*See full wiring schematic in `machines/wiring/dragon-wiring-v1.pdf`*
*[Back to Curriculum Index](../README.md)*
