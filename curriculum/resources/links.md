# Web Resources — 3D Printing Reference Links

> Curated external links for all topics covered in the curriculum. All links verified.
> Organized by module topic. Not a replacement for the video library (`videos.md`) — this covers datasheets, docs, wikis, and written guides.

---

## Electronics & Control Boards

| Resource | Why It's Useful |
|---------|----------------|
| [MKS Monster8 GitHub](https://github.com/makerbase-mks/MKS-Monster8) | Official pinout diagrams, wiring guides, firmware configs for Snowflake and Twin Dragon |
| [MKS Robin Nano V3 GitHub](https://github.com/makerbase-mks/MKS-Robin-Nano-V3) | Official pinout diagrams for Julia's control board |
| [MKS Eagle GitHub](https://github.com/makerbase-mks/MKS-Eagle) | Board documentation for Dragon |
| [TMC2209 Datasheet (Trinamic)](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2209_Datasheet.pdf) | Full TMC2209 register map, UART setup, stealthChop configuration |
| [TMC2208 Datasheet (Trinamic)](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2208_v3.0_Datasheet.pdf) | Julia's stepper driver — current limits, register configuration |
| [NEMA 17 Stepper Reference (RepRap)](https://reprap.org/wiki/NEMA_Motor) | Electrical specs, coil wiring, current ratings |
| [Cirkit Designer](https://app.cirkitdesigner.com/) | Browser-based schematic/wiring diagram tool used in Module 1 exercises |

---

## Firmware — Klipper

| Resource | Why It's Useful |
|---------|----------------|
| [Klipper Official Documentation](https://www.klipper3d.org/Overview.html) | Complete reference for all Klipper features |
| [Klipper Configuration Reference](https://www.klipper3d.org/Config_Reference.html) | Every `printer.cfg` parameter explained |
| [Klipper G-Code Commands](https://www.klipper3d.org/G-Codes.html) | Full list of Klipper console commands |
| [Klipper BLTouch Guide](https://www.klipper3d.org/BLTouch.html) | BLTouch wiring and config for Klipper |
| [Klipper Bed Mesh Guide](https://www.klipper3d.org/Bed_Mesh.html) | BED_MESH_CALIBRATE parameters and mesh visualization |
| [Klipper Input Shaper Guide](https://www.klipper3d.org/Resonance_Compensation.html) | ADXL345 setup and SHAPER_CALIBRATE |
| [Klipper Pressure Advance](https://www.klipper3d.org/Pressure_Advance.html) | Pressure advance calibration procedure |
| [Klipper IDEX Configuration](https://www.klipper3d.org/Config_Reference.html#dual_carriage) | Dual carriage (IDEX) configuration — Twin Dragon specific |
| [Klipper Installation Guide](https://www.klipper3d.org/Installation.html) | How to install Klipper on a Raspberry Pi |
| [Mainsail Documentation](https://docs.mainsail.xyz/) | Mainsail web UI setup and features |
| [Fluidd Documentation](https://docs.fluidd.xyz/) | Fluidd web UI setup and features (Julia) |

---

## Firmware — Marlin (Secondary Reference)

| Resource | Why It's Useful |
|---------|----------------|
| [Marlin G-Code Reference](https://marlinfw.org/meta/gcode/) | All Marlin G-code and M-code commands |
| [Marlin Configuration Reference](https://marlinfw.org/docs/configuration/configuration.html) | `Configuration.h` and `Configuration_adv.h` parameters |
| [Marlin GitHub](https://github.com/MarlinFirmware/Marlin) | Latest Marlin releases and example configs |
| [Teaching Tech — Marlin PID Tuning](https://teachingtech.com.au/3d-printer-pid-tuning/) | Practical PID tuning walkthrough for Marlin |

---

## Mechanical Components

| Resource | Why It's Useful |
|---------|----------------|
| [BLTouch Official (Antclabs)](https://www.antclabs.com/bltouch) | Official wiring, pin specifications, modes |
| [CR Touch Guide](https://www.creality.com/pages/creality-crtouch) | CR Touch calibration and setup (Julia) |
| [HIWIN MGN12H Rail Datasheet](https://www.hiwin.com/products/linear-guideways/miniature-linear-guideways/) | MGN12H specs, load ratings, installation torques |
| [Gates Carbon Drive Belt App](https://www.gatescarbondrive.com/) | Belt tension calculator by Gates (target 120–150 Hz) |
| [GT2 Belt Guide (RepRap)](https://reprap.org/wiki/GT2_Belt) | GT2 timing belt profiles, pitch specs |
| [E3D V6 Hotend Guide (official)](https://e3d-online.com/blogs/news/v6-wiring) | V6 hotend wiring, assembly, and thermocouple specs |
| [E3D Volcano Guide](https://e3d-online.com/pages/volcano-faq) | Dragon's Volcano nozzle FAQ and specifications |
| [Bowden vs Direct Drive Comparison](https://www.3dprintingmedia.network/bowden-vs-direct-drive/) | Written comparison with trade-offs (useful for Module 2) |

---

## Slicing Software

| Resource | Why It's Useful |
|---------|----------------|
| [OrcaSlicer GitHub](https://github.com/SoftFever/OrcaSlicer) | Downloads, release notes, and machine profiles |
| [OrcaSlicer Wiki](https://github.com/SoftFever/OrcaSlicer/wiki) | Official user guide and calibration flows |
| [PrusaSlicer Help](https://help.prusa3d.com/category/prusaslicer_204) | Official PrusaSlicer documentation |
| [Cura Marketplace (plugins)](https://marketplace.ultimaker.com/app/cura/plugins) | Plugin directory for Cura (if used) |
| [Slic3r Manual](https://manual.slic3r.org/) | Original slicer documentation — foundational concepts |
| [Ellis3D Tuning Guide](https://ellis3d.com/tuning/) | Community guide: pressure advance, first layer, retraction — very detailed |

---

## OctoPrint

| Resource | Why It's Useful |
|---------|----------------|
| [OctoPrint Official](https://octoprint.org/) | Download, setup, and official guides |
| [OctoPrint Plugin Repository](https://plugins.octoprint.org/) | All available OctoPrint plugins with reviews |
| [OctoPrint GitHub](https://github.com/OctoPrint/OctoPrint) | Source code, issue tracker, releases |
| [Bed Visualizer Plugin](https://plugins.octoprint.org/plugins/bedlevelvisualizer/) | Visual bed mesh overlay — recommended plugin |

---

## Fracktory

| Resource | Why It's Useful |
|---------|----------------|
| [Fracktory Official](https://www.fracktory.com/) | Agent install, dashboards, print monitoring |
| [Fracktory Documentation](https://docs.fracktory.com/) | Setup guide, printer integration, logging API |

---

## Filaments & Materials

| Resource | Why It's Useful |
|---------|----------------|
| [Prusa Filament Storage Blog](https://blog.prusa3d.com/how-to-store-and-dry-filament_38465/) | Evidence-based drying temps/times and storage best practices |
| [All3DP Material Guide](https://all3dp.com/2/the-best-3d-printer-filament-types-guide/) | Overview of all FDM materials with pros/cons |
| [Polymaker Material Guide](https://polymaker.com/resources/) | Datasheets for PLA, PETG, PA, PC — with moisture specs |
| [Filaween Testing Database](http://www.filaween.com/) | Community-tested filament specs and brand comparisons |
| [R3D Material Print Settings](https://support.raise3d.com/hc/en-us) | Commercial slicer profiles by material |

---

## Safety & Regulations

| Resource | Why It's Useful |
|---------|----------------|
| [California Air Resources Board — FFF Emissions](https://www.arb.ca.gov/research/resnotes/notes/11-09.htm) | Study on ultrafine particle emissions from FDM printing |
| [ANSI/ACGIH TLV for Styrene](https://www.acgih.org/tlv-bei-guidelines/) | ABS/ASA styrene exposure limits |
| [OSHA PPE Standards](https://www.osha.gov/personal-protective-equipment) | General PPE requirements — applies to workshop safety |

---

## Learning Platforms

| Resource | Why It's Useful |
|---------|----------------|
| [Teaching Tech (YouTube/website)](https://teachingtech.com.au/) | Best single-author guide covering calibration, slicing, and tuning |
| [RepRap Wiki](https://reprap.org/wiki/Main_Page) | Original open-source 3D printing encyclopedia — deep technical content |
| [Printables (3D model library)](https://www.printables.com/) | Free 3D models for calibration prints and test parts |
| [Thingiverse](https://www.thingiverse.com/) | Large community model library |
| [Hackaday FDM Tag](https://hackaday.com/tag/3d-printing/) | Advanced build projects and technical articles |

---

## Calibration Tools and Reference

| Resource | Why It's Useful |
|---------|----------------|
| [Calibration Cube (Printables)](https://www.printables.com/model/5765-calibration-cube) | Standard XY-calibration cube — 20 mm cube with XYZE on each face |
| [Ellis Pressure Advance Guide](https://ellis3d.com/tuning/pressure_linear_advance/) | Step-by-step pressure advance calibration |
| [Ellis First Layer Tuning](https://ellis3d.com/tuning/first_layer/) | First layer visual diagnosis with photos |
| [Teaching Tech Calibration Site](https://teachingtech.com.au/Calibration/) | Online calculators for E-steps, first layer, retraction |
| [Rotation Distance Calculator](https://ellis3d.com/tuning/extruder_calibration/) | Klipper `rotation_distance` calculation from steps/mm |

---

*For video resources, see [resources/videos.md](videos.md)*
*[Back to Curriculum Index](../README.md)*
