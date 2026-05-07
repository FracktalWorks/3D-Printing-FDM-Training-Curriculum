# Module 4: Filaments & Materials — Official Specifications

> Official material data sourced from **eSUN technical data sheets** and the **Fracktal Works Material & Nozzle Compatibility sheet** (Nov 2025).
> Use these specs when setting up Fracktory profiles. Do not use unofficial community settings as they may damage the hotend or produce poor prints.

![FDM extruder cross-section showing the filament path — from the cold end (stepper drive gear) through the heat break to the heated nozzle](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Extruder_lemio-en.svg/400px-Extruder_lemio-en.svg.png)
*Filament is fed from the spool through the extruder drive gears, past the heat break, and melts in the hotend before exiting the nozzle. Different materials (PLA, PETG, ABS, TPU) require different temperatures and flow rates at each stage. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Extruder_lemio-en.svg), CC BY-SA 4.0*

---

## 1. Material Compatibility by Machine

| Material | Snowflake | Dragon 400/500/700 | Twin Dragon 300/400/600 |
|----------|-------------|-------------------|------------------------|
| **PLA / ePLA+** | ✅ | ✅ | ✅ |
| **ePLA-Matte** | ✅ | ✅ | ✅ |
| **HIPS** | ✅ | ✅ | ✅ |
| **PETG** | ✅ | ✅ | ✅ |
| **TPU 85A (eFlex)** | ✅ | ✅ | ✅ |
| **TPU 98A (eTPU-95A)** | ✅ | ✅ | ✅ |
| **ABS / ABS+** | ❌ | ✅ | ✅ |
| **ASA (eASA)** | ❌ | ✅ | ✅ |
| **Nylon (ePA12)** | ❌ | ✅ | ✅ |
| **GF-Nylon (ePA12-CF)** | ❌ | ✅ | ✅ |
| **CF-Nylon (ePA-CF)** | ❌ | ✅ | ✅ |
| **PC (ePC)** | ❌ | ✅ | ✅ |
| **PVA (soluble support)** | ❌ | ❌ | ✅ |
| **Breakaway support** | ❌ | ❌ | ✅ |

> **Snowflake** is a compact machine with a max hotend temp of 265°C — this limits it to low/mid-temperature materials only.
> **Dragon and Twin Dragon** reach 300°C and can print all engineering-grade materials.

---

## 2. Official Print Settings (eSUN Technical Data)

All temperatures are for **1.75 mm diameter filament**. Adjust ±5°C if prints show under-extrusion or stringing.

### 2.1 ePLA+ (Standard PLA)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 210 – 230°C |
| **Bed Temperature** | 45 – 60°C |
| **Cooling Fan** | 100% |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 60°C / 4 hours |
| **Recommended Nozzle** | LT (Low Temperature) — brass ≤230°C |
| **Notes** | Most beginner-friendly. Biodegradable. Good dimensional accuracy. Low warp risk. |

### 2.2 ePLA-Matte

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 190 – 230°C |
| **Bed Temperature** | 45°C |
| **Cooling Fan** | 100% |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 60°C / 4 hours |
| **Recommended Nozzle** | LT |
| **Notes** | Flat, matte surface finish. Ideal for display models and artistic prints. Slightly lower temp than ePLA+. |

### 2.3 PETG

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 230 – 250°C |
| **Bed Temperature** | 75 – 90°C |
| **Cooling Fan** | 100% |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 70°C / 10 hours |
| **Recommended Nozzle** | LT / HT |
| **Notes** | More flexible and impact-resistant than PLA. Good for mechanical parts and outdoor use. Prone to stringing — reduce speed and retraction to 0.5–1.5 mm (direct drive). |

### 2.4 eTPU-95A (Flexible)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 220 – 250°C |
| **Bed Temperature** | 45 – 60°C |
| **Cooling Fan** | 100% |
| **Print Speed** | **20 – 50 mm/s** (must slow down — flexible material cannot be pushed fast) |
| **Drying Temp / Time** | 80°C / 10 hours |
| **Recommended Nozzle** | LT |
| **Notes** | Flexible, rubber-like. For gaskets, grips, seals, wearables. Retraction should be minimal (0.5–1 mm) or disabled to prevent grinding. |

### 2.5 eFlex / eTPU-87A

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 220 – 250°C |
| **Bed Temperature** | 45 – 60°C |
| **Cooling Fan** | 100% |
| **Print Speed** | 20 – 50 mm/s |
| **Drying Temp / Time** | 80°C / 10 hours |
| **Recommended Nozzle** | LT |
| **Notes** | Softer than eTPU-95A (87A Shore hardness). For wearables and highly compressible parts. |

### 2.6 ABS+ (Acrylonitrile Butadiene Styrene)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 230 – 270°C |
| **Bed Temperature** | 90 – 110°C |
| **Cooling Fan** | **0%** (no cooling — ABS warps severely with fan) |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 70°C / 6 hours |
| **Recommended Nozzle** | HT |
| **Notes** | Heat-resistant, impact-resistant. Requires enclosed build space or draft-free area. Emits styrene fumes — ventilate area. Use HEPA filter (Twin Dragon). **Not compatible with Snowflake.** |

### 2.7 eASA (ASA)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 240 – 270°C |
| **Bed Temperature** | 90 – 110°C |
| **Cooling Fan** | **0%** |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 70°C / 6 hours |
| **Recommended Nozzle** | HT |
| **Notes** | UV-stable outdoor material. ABS alternative with better weathering resistance. Same print rules as ABS. |

### 2.8 HIPS (High Impact Polystyrene)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 230 – 270°C |
| **Bed Temperature** | 100 – 115°C |
| **Cooling Fan** | **0%** |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 70°C / 6 hours |
| **Recommended Nozzle** | HT |
| **Notes** | Soluble in D-Limonene. Used as support material for ABS dual-extrusion (Twin Dragon). Can also be printed as a primary material — similar to ABS but slightly less strong. |

### 2.9 ePA12 — Nylon

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 260 – 290°C |
| **Bed Temperature** | 70 – 90°C |
| **Cooling Fan** | **0%** |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 80°C / 10 hours |
| **Recommended Nozzle** | HT |
| **Notes** | Excellent fatigue resistance and flexibility. For gears, hinges, industrial parts. **Very hygroscopic — must be dry before printing.** Prints poorly from wet filament (bubbling, weak layers). |

### 2.10 ePA-CF (Carbon Fiber Nylon)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 260 – 300°C |
| **Bed Temperature** | 45 – 60°C |
| **Cooling Fan** | **0%** |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 80°C / 10 hours |
| **Recommended Nozzle** | **HH (Hardened Steel) — MANDATORY** |
| **Notes** | Carbon fiber reinforced nylon. Extremely stiff and lightweight. For drone frames, brackets, structural components. **Abrasive — destroys brass nozzles quickly.** Always use HH nozzle. |

### 2.11 ePA12-CF (CF Nylon 12)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 270 – 300°C |
| **Bed Temperature** | 45 – 60°C |
| **Cooling Fan** | **0%** |
| **Print Speed** | 40 – 100 mm/s |
| **Drying Temp / Time** | 80°C / 10 hours |
| **Recommended Nozzle** | **HH (Hardened Steel) — MANDATORY** |
| **Notes** | Nylon 12 base (more flexible than PA6). Used in automotive and aerospace parts requiring flexible CF components. |

### 2.12 ePC (Polycarbonate)

| Parameter | Value |
|-----------|-------|
| **Hotend Temperature** | 240 – 270°C |
| **Bed Temperature** | 80 – 120°C |
| **Cooling Fan** | **0%** |
| **Print Speed** | 20 – 50 mm/s |
| **Drying Temp / Time** | 80°C / 10 hours |
| **Recommended Nozzle** | HT |
| **Notes** | Transparent, high-strength, high-temperature resistance. For light covers, heat shields, and impact-resistant enclosures. Must be dry — PC absorbs moisture quickly and prints poorly when wet. |

---

## 3. Nozzle Types — Official Guide

All Fracktal Works nozzles use the same base design but differ in tip material and max temperature:

| Nozzle Type | Full Name | Tip Material | Max Temp | Compatible Materials |
|------------|-----------|-------------|---------|---------------------|
| **LT** | Low Temperature | Brass | ≤230°C | PLA, ePLA+, PETG, TPU, eFlex |
| **HT** | High Temperature | Brass (full metal) | 230–270°C | ABS, ASA, HIPS, Nylon, PC, PETG |
| **HH** | High Temperature Hardened | Hardened steel | 230–300°C | CF-PA, GF-PA, CF-PA12, abrasive filaments |

> ⚠️ **Critical:** Using a **brass LT or HT nozzle with CF/GF filaments** will destroy the nozzle within hours. The abrasive carbon/glass fibers grind the soft brass tip away. Always verify nozzle type before printing reinforced filaments.

### 3.1 Available Nozzle Diameters (Fracktory Selection)

| Diameter | Use Case |
|----------|---------|
| **0.25 mm** | High detail; very slow; only for LT nozzle / low-temp materials |
| **0.4 mm** | Standard default for all machines |
| **0.6 mm** | Faster prints; better layer bonding; functional parts |
| **0.8 mm** | Fastest; large structural parts; low detail requirement |

---

## 4. Drying Guide

Moisture is the #1 cause of print quality failures with hygroscopic filaments (Nylon, PC, CF-PA, ABS, PETG). Symptoms include:
- Bubbling, popping, or crackling sounds from the nozzle
- Rough, bubbly surface texture on prints
- Weak layers and poor inter-layer adhesion
- Stringing worse than expected

### 4.1 Drying Temperatures and Times

| Material | Dry Temp | Dry Time | Priority |
|----------|---------|---------|---------|
| ePLA+ | 60°C | 4 hrs | Low |
| ePLA-Matte | 60°C | 4 hrs | Low |
| PETG | 70°C | 10 hrs | Medium |
| ABS / eASA / HIPS | 70°C | 6 hrs | Medium |
| eTPU-95A / eFlex | 80°C | 10 hrs | Medium |
| ePA12 (Nylon) | 80°C | 10 hrs | **High** |
| ePA-CF / ePA12-CF | 80°C | 10 hrs | **High** |
| ePC | 80°C | 10 hrs | **High** |

### 4.2 Storage

- Keep filament in **sealed zip-lock bags** or **air-tight containers** with **desiccant (silica gel)** when not in use.
- Recharge silica gel by baking at 120°C for 2 hours in an oven.
- Do not leave spools on the printer overnight in humid environments.
- Use the printer's **drybox system** for active dry printing — feeds filament from a sealed heated enclosure.

---

## 5. Dual Extrusion Combinations (Twin Dragon)

The Twin Dragon supports IDEX (Independent Dual Extrusion). Useful material pairings:

| T0 (Primary) | T1 (Support) | Use Case |
|-------------|-------------|---------|
| PLA+ | PLA+ (same color) | Duplication mode — 2× throughput |
| ABS+ | HIPS | ABS print + HIPS soluble support (dissolves in D-Limonene) |
| Nylon | PVA | Nylon print + PVA water-soluble support |
| PETG | PVA | PETG print + PVA water-soluble support |
| PLA+ (model color) | PLA+ (support color) | Breakaway support — snap off cleanly |

> ⚠️ **Note:** PVA and Breakaway filaments are only compatible with Twin Dragon — not Dragon or Snowflake. See compatibility table in Section 1.

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Moisture in Filament — Scientific Test](https://www.youtube.com/watch?v=FAXUjZZER5E) | CNC Kitchen | Lab-tested proof of moisture impact on print strength |
| [PLA vs PETG vs ABS vs ASA — Full Comparison](https://www.youtube.com/watch?v=ycGni1AoMIE) | CNC Kitchen | Mechanical testing of all common materials — data-driven |
| [Nylon 3D Printing — Everything You Need to Know](https://www.youtube.com/watch?v=Zqsc4bYQ9fs) | Maker's Muse | Nylon printing guide: drying, bed adhesion, settings |
| [Carbon Fiber Filament — HH Nozzle Explained](https://www.youtube.com/watch?v=9Jwi7NVGUbY) | CNC Kitchen | Why abrasive filaments destroy brass nozzles |

---

## 📚 Further Reading

- [eSUN Official Product Page](https://www.esun3d.com/products.html) — Technical data sheets for all eSUN materials
- [Fracktal Works Support Portal](https://care.fracktal.in) — Official support and material recommendations

---

## ✅ Knowledge Check

1. A Snowflake operator wants to print ABS+ parts. Is this possible? Why or why not?
2. You are printing ePA-CF on the Dragon 400. What nozzle type must you use and why?
3. Your Nylon print is producing a crackling sound from the nozzle and the surface looks bubbly. What is the most likely cause and what do you do?
4. What is the difference between a HIPS support and a PVA support? Which machine supports PVA?
5. List the drying temperature and time for ePA12 Nylon.
6. You want to print the same part twice simultaneously in half the time. Which machine and which print mode do you use?

---

*[← Software & Slicing](../01-software-and-slicing/README.md) | [Section Index](./README.md) | [🏠 Curriculum Index](../../README.md) | [Next: Printer Operations →](../03-printer-operations/README.md)*
