# Fracktory Slicer — Reference Data

Drop all Fracktory documentation, machine profiles, and G-code templates here.

## What is Fracktory?

**Fracktory** is the official slicer for all Fracktal Works machines. It is based on **Ultimaker Cura** (open-source) and comes with pre-configured printer profiles for Snowflake, Dragon, and Twin Dragon.

- **Download**: http://printers.fracktory.in/download
- **Support**: support@fracktal.in / https://care.fracktal.in
- **System Requirements**: Windows Vista+ (64-bit), macOS 10.11+ (64-bit), Linux Ubuntu 14.04+ (64-bit), 4 GB RAM, 205 MB disk

## What Belongs Here

| File | Description |
|------|-------------|
| `Fracktory-guide.pdf` | Official Fracktory slicer documentation |
| `snowflake-profile.curaprofile` | Fracktory machine profile for Snowflake |
| `dragon-400-profile.curaprofile` | Fracktory machine profile for Dragon 400 |
| `dragon-500-profile.curaprofile` | Fracktory machine profile for Dragon 500 |
| `dragon-700-profile.curaprofile` | Fracktory machine profile for Dragon 700 |
| `twin-dragon-300-profile.curaprofile` | Fracktory machine profile for Twin Dragon 300 (IDEX) |
| `twin-dragon-400-profile.curaprofile` | Fracktory machine profile for Twin Dragon 400 (IDEX) |
| `twin-dragon-600-profile.curaprofile` | Fracktory machine profile for Twin Dragon 600 (IDEX) |
| `ePLA-base-settings.curaprofile` | Filament profile — ePLA+ (base settings) |
| `PETG-base-settings.curaprofile` | Filament profile — PETG |
| `ABS-base-settings.curaprofile` | Filament profile — ABS+ |
| `TPU-base-settings.curaprofile` | Filament profile — eTPU-95A |

## Machine Profile Start G-code Template

All Fracktory (Cura-based) profiles use Cura variable syntax:

```gcode
START_PRINT BED_TEMP={material_bed_temperature} EXTRUDER_TEMP={material_print_temperature}
```

End G-code:
```gcode
END_PRINT
```

> ⚠️ Note: Fracktory uses **Cura variable syntax** (`{material_bed_temperature}`) — NOT OrcaSlicer/other slicer syntax (`{first_layer_bed_temperature[0]}`). Do not mix these up when editing profiles.

## Fracktory Version

| Item | Value |
|------|-------|
| Base | Ultimaker Cura (open-source) |
| Download | http://printers.fracktory.in/download |
| Klipper compatibility | Yes — uses START_PRINT/END_PRINT macros |
| Wi-Fi printing | Yes — direct to printer IP address |

## Nozzle Size Selection

Fracktory supports multiple nozzle sizes. Select the correct one in the machine settings:

| Nozzle | Use Case |
|--------|---------|
| 0.25 mm | High detail, slow |
| **0.4 mm** | Standard (default for all machines) |
| 0.6 mm | Faster prints, functional parts |
| 0.8 mm | Fastest prints, large structural parts |

## Calibration Workflow

Run these in order when setting up a new machine profile or after any hardware change:

1. **Z offset** — run `PROBE_CALIBRATE` in OctoPrint Terminal, adjust until paper has slight drag
2. **Bed mesh** — run `BED_MESH_CALIBRATE` to map bed surface, save with `SAVE_CONFIG`
3. **First layer** — print a single-layer square, verify squish is uniform across bed
4. **Pressure advance** — run `SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500` + `TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=0.005`
5. **Input shaper** — attach ADXL345 accelerometer, run `SHAPER_CALIBRATE`
4. **First layer** — print `first-layer-test.3mf`, verify adhesion and Z-offset
