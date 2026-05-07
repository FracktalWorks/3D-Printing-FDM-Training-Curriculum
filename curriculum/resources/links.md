# Web Resources — 3D Printing Reference Links

> Curated external links for all topics covered in the curriculum. All links verified.
> Organized by module topic. Not a replacement for the video library (`videos.md`) — this covers datasheets, docs, wikis, and written guides.

---

## Electronics & Control Boards

| Resource | Why It's Useful |
|---------|----------------|
| [BIGTREETECH Manta M8P V2.0 GitHub](https://github.com/bigtreetech/Manta-M8P) | Official pinout diagrams, wiring guides for Fracktal machines |
| [FracktalWorks Klipper IDEX Firmware](https://github.com/FracktalWorks/klipper_IDEX) | Official Klipper fork used in Dragon and Twin Dragon |
| [TMC5160 Datasheet (Trinamic)](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC5160_Datasheet.pdf) | Manta M8P onboard driver data sheet |
| [TMC2209 Datasheet (Trinamic)](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2209_Datasheet.pdf) | Full TMC2209 register map, UART setup, stealthChop configuration |
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
| [OctoPrint Documentation](https://docs.octoprint.org/) | OctoPrint web UI setup, plugins, and features |

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
| [BLTouch Official (Antclabs)](https://www.antclabs.com/bltouch) | Official BLTouch wiring, pin specifications, modes |
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
| [Fracktory Download](http://printers.fracktory.in/download) | Official Fracktory slicer for all Fracktal machines |
| [Fracktal Works Support](https://care.fracktal.in) | Official support portal and knowledge base |
| [Cura Marketplace (plugins)](https://marketplace.ultimaker.com/app/cura/plugins) | Plugin directory for Cura (Fracktory is Cura-based) |
| [Ellis3D Tuning Guide](https://ellis3d.com/tuning/) | Community guide: pressure advance, first layer, retraction — very detailed |

---

## Fracktory Slicer

| Resource | Why It's Useful |
|---------|----------------|
| [Fracktory Download](http://printers.fracktory.in/download) | Download page for Windows, macOS, Linux |
| [Fracktal Works Website](https://www.fracktal.in) | Official Fracktal Works product information |
| [Fracktal Support Portal](https://care.fracktal.in) | Setup guide, printer integration, support tickets |

---

## Filaments & Materials

| Resource | Why It's Useful |
|---------|----------------|
| [eSUN Filament Technical Data Sheets](https://www.esun3d.com/products.html) | Official eSUN TDS with print temps, drying, and material specs |
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
