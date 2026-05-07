# Twin Dragon — Machine Data

Drop all Twin Dragon documentation here.

## What belongs here

| File | Description |
|------|-------------|
| `TWIN-DRAGON-USER-MANUAL.pdf` | Official machine user manual including IDEX setup |
| `twin-dragon-wiring-diagram.pdf` | Full wiring schematic (both extruders, dual BLTouch) |
| `twin-dragon-BOM.xlsx` | Bill of Materials |
| `printer.cfg` | Current production Klipper configuration with IDEX macros |
| `macros.cfg` | T0/T1 tool-change macros, parking, DUAL_NOZZLE_CALIBRATE |
| `calibration-profiles/` | Sub-folder: `dual-tower.3mf` and other IDEX calibration models |
| `twin-dragon-build-photos/` | Sub-folder for build and maintenance photos |

## Machine Summary

| Item | Value |
|------|-------|
| Motion | CoreXY + IDEX |
| Build Volume | 300 × 300 × 350 mm |
| Board | MKS Monster8 |
| Firmware | Klipper + OctoPrint |
| Network | `http://twin-dragon` / `http://192.168.1.104` |
| Probe | Dual BLTouch (one per head) |
| Nozzle T0 | 0.4 mm brass |
| Nozzle T1 | 0.4 mm hardened steel |

## IDEX Modes Quick Reference

| Mode | Slicer Setting | Use Case |
|------|---------------|---------|
| Single T0 | Default | Standard single-material |
| Dual Material | Dual extruder profile | Multi-material / soluble supports |
| Duplication | Mirror/duplicate mode | 2× throughput same part (max 150 mm X) |
| Mirror | Mirror mode | Left/right mirror pairs |

> Quick reference card: [`../machines/TWIN-DRAGON-QUICK-REF.md`](../machines/TWIN-DRAGON-QUICK-REF.md)
