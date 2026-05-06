# Dragon — Machine Quick Reference

> One-page cheat sheet for daily operation, calibration, and first-line troubleshooting.
> Dragon is the high-temperature, large-format machine. Extra caution required at high-temp.
> Keep this open during any Dragon maintenance or setup session.

---

## Hardware Specs

| Item | Value |
|------|-------|
| **Motion System** | CoreXY, insulated enclosure |
| **Build Volume** | 350 × 350 × 400 mm |
| **Control Board** | MKS Eagle (STM32H743) |
| **Firmware** | Klipper + Mainsail |
| **Stepper Drivers** | TMC2209 (UART, sensorless-homing capable) |
| **Extruder** | Bowden drive |
| **Nozzle** | E3D Volcano 0.6 mm (larger flow than standard) |
| **Max Hotend Temp** | 320°C (high-temp capable) |
| **Max Bed Temp** | 120°C |
| **Bed Surface** | Cast aluminum + PEI sheet |
| **Auto-leveling** | BLTouch (primary) + mechanical endstop (backup) |
| **Enclosure** | Insulated cover, active exhaust fan |
| **Host** | Raspberry Pi 4 (Mainsail) |
| **Network** | `http://192.168.1.103` (or `http://dragon`) |

---

## ⚠️ Dragon-Specific Safety Rules

1. **Pre-heat enclosure before printing** — always heat enclosure to 50°C before starting any print.
2. **Allow 120 seconds** for nozzle to reach 320°C (don't rush — thermal shock risks nozzle microcracking).
3. **DO NOT open the enclosure door mid-print** during ABS/ASA runs — rapid thermal drop causes warping.
4. **Active exhaust fan must be running** before heating above 200°C.
5. **BLTouch probe can false-trigger** from hot-air currents inside enclosure — re-probe only when enclosure is at stable temp.

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
□ Webcam + Mainsail alerts set for remote monitoring
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

## BLTouch Probe Offsets

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
| 4 | BLTouch false-triggers inside enclosure | Hot air currents deflecting probe | Clean lens; increase Z-clearance; use mechanical endstop backup |
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

| Feature | Dragon | Snowflake | Julia |
|---------|--------|-----------|-------|
| Max temp | **320°C** | 300°C | 280°C |
| Nozzle | **0.6 mm Volcano** | 0.4 mm E3D V6 | 0.4 mm brass |
| Build volume | **350×350×400** | 300³ | 250³ |
| Enclosure | **Yes (insulated)** | No | No |
| Drive type | **Bowden** | Direct | Direct |
| Board | MKS Eagle | MKS Monster8 | MKS Robin Nano V3 |

---

*See full wiring schematic in `machines/wiring/dragon-wiring-v1.pdf`*
*[Back to Curriculum Index](../README.md)*
