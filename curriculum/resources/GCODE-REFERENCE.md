# G-Code & M-Code Quick Reference

> FDM printer command reference for Klipper and Marlin firmware.
> Commands marked 🟢 work on both. Commands marked 🔵 are Klipper-only. Commands marked 🟠 are Marlin-only.

---

## 1. Movement Commands

| Command | Parameters | Description | Firmware |
|---------|-----------|-------------|---------|
| `G0 X Y Z F` | Coords + Feedrate | Rapid move (no extrusion). G0 and G1 are equivalent in most firmware. | 🟢 Both |
| `G1 X Y Z E F` | Coords + Extrusion + Feedrate | Linear move with optional extrusion. Most common print move. | 🟢 Both |
| `G28` | `X Y Z` (optional) | Home axes. `G28 X Y` homes only X and Y. `G28` homes all. | 🟢 Both |
| `G90` | None | Set **absolute** positioning mode (default). All moves relative to 0,0,0 origin. | 🟢 Both |
| `G91` | None | Set **relative** positioning mode. All moves are offsets from current position. | 🟢 Both |
| `G92 E0` | Axis + value | Set current position as a new zero. Used after filament change to reset E. | 🟢 Both |
| `G29` | None | Run auto bed leveling. In Klipper, use `BED_MESH_CALIBRATE` instead. | 🟠 Marlin |

### Feedrate Notes
- Feedrate (`F`) is in **mm/min** (not mm/s). Example: `F3000` = 50 mm/s.
- Feedrate is sticky — once set, it applies to all subsequent moves until changed.

---

## 2. Temperature Commands

| Command | Parameters | Description | Firmware |
|---------|-----------|-------------|---------|
| `M104 S<temp>` | Target temp | Set **hotend temperature** — does NOT wait. Print continues immediately. | 🟢 Both |
| `M109 S<temp>` | Target temp | Set hotend temp and **wait** for it to stabilize before next command. | 🟢 Both |
| `M140 S<temp>` | Target temp | Set **bed temperature** — does NOT wait. | 🟢 Both |
| `M190 S<temp>` | Target temp | Set bed temp and **wait** for it to stabilize. | 🟢 Both |
| `M106 S<0-255>` | Speed 0–255 | Set part **cooling fan** speed. `M106 S255` = 100%. `M106 S128` ≈ 50%. | 🟢 Both |
| `M107` | None | Turn part cooling fan **OFF**. Equivalent to `M106 S0`. | 🟢 Both |
| `M301 P I D` | PID values | Set hotend PID values directly (Marlin). Use `SAVE_CONFIG` in Klipper. | 🟠 Marlin |
| `M303 E0 S<temp> C8` | Extruder, temp, cycles | Run **PID autotune** on hotend — 8 cycles at target temp (Marlin). | 🟠 Marlin |

> **Klipper equivalent for PID:** `PID_CALIBRATE HEATER=extruder TARGET=200` — saves automatically.

---

## 3. Extruder Commands

| Command | Parameters | Description | Firmware |
|---------|-----------|-------------|---------|
| `G1 E50 F300` | E + Feedrate | **Extrude** 50 mm of filament at 5 mm/s (F300 = 5 mm/s). | 🟢 Both |
| `G1 E-5 F1200` | Negative E | **Retract** 5 mm at 20 mm/s (F1200 = 20 mm/s). | 🟢 Both |
| `G10` | None | Firmware **retraction** (if `M207` is configured). | 🟢 Both |
| `G11` | None | Firmware **unretract** (recover after G10). | 🟢 Both |
| `M207 S<mm> F<mm/min>` | Length + Speed | Set firmware retraction length and speed. | 🟢 Both |
| `T0` | None | Switch to **extruder 0** (left head on Twin Dragon). | 🟢 Both |
| `T1` | None | Switch to **extruder 1** (right head on Twin Dragon). | 🟢 Both |

> **Important:** Always heat hotend to print temperature before issuing any extrude command. Cold extrusion protection (`PREVENT_COLD_EXTRUSION`) will block it if too cold.

---

## 4. EEPROM and Settings (Marlin)

| Command | Parameters | Description | Firmware |
|---------|-----------|-------------|---------|
| `M500` | None | **Save** current settings to EEPROM (persistent memory). | 🟠 Marlin |
| `M501` | None | **Load** settings from EEPROM (discard RAM changes). | 🟠 Marlin |
| `M502` | None | **Reset** settings to firmware compiled defaults (does NOT save). | 🟠 Marlin |
| `M503` | None | **Report** all current settings to serial terminal. | 🟠 Marlin |
| `M92 E<steps>` | Steps/mm | Set extruder steps per mm (E-steps). Use before `M500`. | 🟠 Marlin |
| `M851 Z<offset>` | Z value | Set Z-probe offset (probe-to-nozzle Z distance). | 🟠 Marlin |

> **Klipper equivalent:** All calibration data is saved to `printer.cfg` via `SAVE_CONFIG`. No EEPROM needed.

---

## 5. Endstops and Probing

| Command | Parameters | Description | Firmware |
|---------|-----------|-------------|---------|
| `M119` | None | **Report** current state of all endstops (open/triggered). | 🟢 Both |
| `M211 S0` | S0 = disable | **Disable** software endstops (use with caution — movement out of bounds is possible). | 🟢 Both |
| `M211 S1` | S1 = enable | **Re-enable** software endstops. | 🟢 Both |
| `G161` | None | Home axes in negative direction (Marlin). | 🟠 Marlin |

---

## 6. Klipper-Only Commands 🔵

| Command | Description |
|---------|-------------|
| `QUERY_ENDSTOPS` | Report endstop states in Klipper console. More readable than M119. |
| `BED_MESH_CALIBRATE` | Run auto bed leveling and generate mesh. Use instead of G29. |
| `BED_MESH_OUTPUT` | Print current mesh data to console for inspection. |
| `PROBE_CALIBRATE` | Interactive Z-offset calibration (paper method with TESTZ commands). |
| `TESTZ Z=-0.1` | Move nozzle down 0.1 mm during `PROBE_CALIBRATE`. |
| `TESTZ Z=+0.1` | Move nozzle up 0.1 mm during `PROBE_CALIBRATE`. |
| `ACCEPT` | Accept current position as Z-offset during `PROBE_CALIBRATE`. |
| `PID_CALIBRATE HEATER=extruder TARGET=200` | Auto-tune PID for hotend. |
| `PID_CALIBRATE HEATER=heater_bed TARGET=60` | Auto-tune PID for heated bed. |
| `SET_PRESSURE_ADVANCE ADVANCE=0.04` | Set pressure advance value without restarting. |
| `PRESSURE_ADVANCE_CALIBRATE` | Run pressure advance calibration tower. |
| `SHAPER_CALIBRATE` | Run input shaper calibration (requires ADXL345 accelerometer). |
| `SET_INPUT_SHAPER SHAPER_TYPE=mzv SHAPER_FREQ_X=48` | Apply input shaper settings. |
| `TEMPERATURE_WAIT SENSOR=extruder MINIMUM=170` | Wait for sensor to reach minimum temp. |
| `SET_HEATER_TEMPERATURE HEATER=extruder TARGET=200` | Set heater temp (equivalent to M104). |
| `FIRMWARE_RESTART` | Reload `printer.cfg` and reconnect. Use after config edits. |
| `RESTART` | Full Klipper restart (software restart). |
| `M112` | Emergency stop — immediately halt all movement and heating. |

---

## 7. Diagnostic Commands

| Command | Description | Firmware |
|---------|-------------|---------|
| `M105` | **Report** current temperatures for all sensors. | 🟢 Both |
| `M114` | **Report** current XYZ position of all axes. | 🟢 Both |
| `M115` | **Report** firmware version and capabilities. | 🟢 Both |
| `M112` | **Emergency stop** — stops everything immediately. | 🟢 Both |
| `STATUS` | Klipper: report current printer state (ready / printing / error). | 🔵 Klipper |
| `QUERY_PROBE` | Klipper: report BLTouch / probe state (triggered or open). | 🔵 Klipper |
| `BLTOUCH_DEBUG COMMAND=reset` | Klipper: reset BLTouch if pin is stuck. | 🔵 Klipper |

---

## 8. G-Code: Start / End Patterns

### Minimum Start G-Code (Klipper machines)

```gcode
; Klipper machines — call START_PRINT macro with temp params
START_PRINT BED_TEMP={bed_temperature[0]} EXTRUDER_TEMP={temperature[0]}
```

### Minimum End G-Code

```gcode
END_PRINT
```

### Common Inline G-Code Sequence (for testing without a macro)

```gcode
M140 S60             ; Start bed heating (no wait)
M104 S200            ; Start hotend heating (no wait)
G28 X Y              ; Home X and Y while heating
M190 S60             ; Wait for bed to reach 60°C
M109 S200            ; Wait for hotend to reach 200°C
BED_MESH_CALIBRATE   ; Run auto bed leveling
G92 E0               ; Reset extruder position
G1 Z5 F500           ; Lift nozzle to safety height
G1 X5 Y10 F3000      ; Move to purge position
G1 Z0.3 F300         ; Lower to first layer height
G1 X100 E15 F500     ; Draw purge line (prime nozzle)
G92 E0               ; Reset extruder position again
; --- Start actual print below this line ---
```

---

## 9. Machine-Specific Quick Reference

| Machine | Start Macro | End Macro | Web UI |
|---------|------------|----------|--------|
| Snowflake | `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=210` | `END_PRINT` | `http://snowflake` |
| Julia | `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=210` | `END_PRINT` | `http://julia` |
| Dragon | `START_PRINT BED_TEMP=105 EXTRUDER_TEMP=255` | `END_PRINT` | `http://dragon` |
| Twin Dragon | `START_PRINT BED_TEMP=60 EXTRUDER_TEMP=210 HEAD=T0` | `END_PRINT` | `http://twin-dragon` |

---

## 10. Common Mistake Reference

| Mistake | Symptom | Correct Practice |
|---------|---------|----------------|
| Using `G0`/`G1` with E on a cold hotend | Extrusion command ignored or MINTEMP error | Heat to print temp first, then extrude |
| Using `M500` on Klipper | Command not recognized | Use `SAVE_CONFIG` in Klipper |
| Forgetting `G90` after relative move testing | All subsequent moves are relative — printer moves wrong distances | Always `G90` after any relative (G91) test |
| Using F in mm/s instead of mm/min | Speed is 60× off | Convert: mm/s × 60 = F value. 50 mm/s = F3000 |
| Homing with `G28` mid-print | Resets all position data | Never home during a print unless macro designed for it |

---

*Sources: [Klipper G-Codes Reference](https://www.klipper3d.org/G-Codes.html) | [Marlin G-Code Reference](https://marlinfw.org/meta/gcode/) | [RepRap G-Code Wiki](https://reprap.org/wiki/G-code)*

*[Back to Curriculum Index](../README.md)*
