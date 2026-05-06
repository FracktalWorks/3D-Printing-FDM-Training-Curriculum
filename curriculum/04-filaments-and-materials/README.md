# Module 04: Filaments & Materials

> Understanding 3D printing materials — properties, print settings, strengths, weaknesses, and storage best practices.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Name at least 6 common 3D printing filament types and their key properties
- Select the correct material for a given application
- Configure appropriate slicer settings for each material
- Store filament correctly to prevent moisture absorption
- Identify failed prints caused by material issues

## Prerequisites

- Module 03: Software & Slicing (recommended)

---

## 1. Filament Basics

### 1.1 Standard Diameter

FDM filament comes in two standard diameters:
- **1.75 mm**: Dominant standard (most modern printers)
- **2.85 mm / 3 mm**: Older standard (still used by some Ultimaker and Lulzbot printers)

> ⚠️ Always match filament diameter to your extruder specification. Using the wrong diameter will cause jams.

### 1.2 Spool Weights

Filament spools are typically sold in:
- **1 kg** (most common)
- **500 g** (sampler / specialty)
- **5 kg** (bulk / production)

---

## 2. Material Guide

### 2.1 PLA — Polylactic Acid

**The go-to material for beginners.** Made from renewable plant starch (corn, sugarcane).

| Property | Value |
|---------|------|
| Print temp | 190–220°C |
| Bed temp | 50–60°C (or unheated) |
| Part cooling | 100% |
| Enclosure | Not needed |
| Strength | Moderate |
| Flexibility | Rigid, brittle |
| Heat resistance | ≈60°C (warps in hot cars!) |
| Biodegradable | Yes (industrially) |

**Best for**: Prototypes, display models, educational prints, mechanical parts that don't get hot.

**Avoid for**: Outdoor use, high-temperature environments, parts under sustained load.

**Tips**:
- Stores well (less moisture-sensitive than other materials)
- Very easy to tune — great first filament
- Post-process with sanding + primer, or resin coating

### 2.2 PETG — Polyethylene Terephthalate Glycol

**The step up from PLA.** Better temperature resistance, tougher, slightly flexible.

| Property | Value |
|---------|------|
| Print temp | 230–250°C |
| Bed temp | 70–85°C |
| Part cooling | 30–50% |
| Enclosure | Not needed |
| Strength | Good |
| Flexibility | Semi-flexible |
| Heat resistance | ≈80°C |
| Moisture sensitivity | Moderate |

**Best for**: Functional mechanical parts, food-safe containers (check filament certification), parts needing some flexibility or impact resistance.

**Avoid for**: Extreme high-temp applications.

**Tips**:
- Prone to **stringing** — tune retraction carefully
- Sticks aggressively to PEI beds — use release agent (glue stick, hairspray) or a dedicated PETG surface
- Use all-metal hot end for consistent results above 240°C

### 2.3 ABS — Acrylonitrile Butadiene Styrene

**Classic engineering plastic.** Tough, good temperature resistance, but challenging to print.

| Property | Value |
|---------|------|
| Print temp | 230–250°C |
| Bed temp | 100–110°C |
| Part cooling | 0% (or minimal) |
| Enclosure | **Required** |
| Strength | Good |
| Flexibility | Slightly flexible |
| Heat resistance | ≈100°C |
| Moisture sensitivity | Low |

**Best for**: Enclosures, parts needing high heat resistance, parts that will be acetone-smoothed.

**Avoid for**: Large flat prints without an enclosure (severe warping).

**Tips**:
- **Enclosure is mandatory**: ABS shrinks quickly and warps without ambient heat retention
- Fumes: ABS emits styrene when printing — use in a ventilated area or add filtration
- **Acetone smoothing**: ABS dissolves in acetone; brush on or vapor-smooth for a glossy surface

### 2.4 ASA — Acrylonitrile Styrene Acrylate

**ABS's outdoor-rated cousin.** UV-resistant; better for outdoor applications.

| Property | Value |
|---------|------|
| Print temp | 235–255°C |
| Bed temp | 90–110°C |
| Enclosure | **Required** |
| UV resistance | Excellent |

**Best for**: Outdoor parts, signage, automotive applications.

### 2.5 TPU — Thermoplastic Polyurethane

**The standard flexible filament.** Rubber-like properties.

| Property | Value |
|---------|------|
| Print temp | 220–240°C |
| Bed temp | 30–60°C |
| Shore hardness | 83A–98A (softer = more flexible) |
| Print speed | Slow (15–30 mm/s) |
| Moisture sensitivity | Moderate |

**Best for**: Phone cases, gaskets, flexible connectors, wheels, grips.

**Avoid**: Bowden extruders (buckling in the tube). **Direct drive only** recommended.

**Tips**:
- Print slowly — TPU is prone to buckling if pushed too fast
- Disable retraction or use minimal retraction (1 mm or less)
- Dry before use if stored long-term

### 2.6 Nylon (PA) — Polyamide

**Engineering-grade material.** Strong, tough, slightly flexible. High moisture absorption.

| Property | Value |
|---------|------|
| Print temp | 240–260°C |
| Bed temp | 70–90°C |
| Enclosure | Strongly recommended |
| Moisture sensitivity | **Extremely high** |
| Heat resistance | ≈100–130°C |

**Best for**: Gears, snap fits, bushings, structural parts, hinges.

**Critical requirement**: **Dry Nylon is mandatory.** Wet Nylon prints with bubbling, popping, and dramatically reduced strength. Dry at 65–70°C for 6–12 hours before printing.

**Tips**:
- Requires **all-metal hot end** (PTFE degrades above 240°C)
- Warps significantly — large brim or enclosure required

### 2.7 Composite Filaments

Base filaments (usually PLA or PA) with added materials for aesthetics or function:

| Composite | Added Material | Key Property | Notes |
|-----------|---------------|-------------|-------|
| **Carbon fiber PLA/PA** | Short CF strands | High stiffness, lower weight | Requires hardened steel nozzle — CF is extremely abrasive |
| **Glow in the dark** | Glow pigment | Glows after light exposure | Abrasive — use hardened nozzle |
| **Wood fill** | Wood fiber | Wood-like appearance | Sand and stain like wood |
| **Metal fill** | Bronze/copper/iron powder | Metal look; magnetic (iron) | Abrasive — hardened nozzle |
| **Silk PLA** | Silk additive | Shiny, metallic-looking surface | Standard brass nozzle OK |

---

## 3. Filament Comparison Quick Reference

| Material | Ease | Strength | Heat Resist. | Flexibility | Enclosure | All-Metal HE |
|---------|------|---------|------------|------------|---------|------------|
| PLA | ⭐⭐⭐⭐⭐ | ★★★ | ★★ | ★ | No | No |
| PETG | ⭐⭐⭐⭐ | ★★★★ | ★★★ | ★★ | No | Optional |
| ABS | ⭐⭐ | ★★★★ | ★★★★ | ★★ | **Yes** | Optional |
| ASA | ⭐⭐ | ★★★★ | ★★★★ | ★★ | **Yes** | Optional |
| TPU | ⭐⭐⭐ | ★★★ | ★★★ | ★★★★★ | No | No |
| Nylon | ⭐ | ★★★★★ | ★★★★ | ★★★ | Strongly rec. | **Yes** |
| CF PLA | ⭐⭐⭐ | ★★★★★ | ★★★ | ★ | No | **Yes** |

---

## 4. Moisture & Storage

**Moisture is the enemy of filament.** Hygroscopic filaments (Nylon, PETG, TPU, PVA) absorb water from the air. Wet filament causes:
- Bubbling and popping sounds while printing
- Surface roughness and blobs
- Dramatically reduced layer adhesion and part strength
- Stringing

### Storage Best Practices

1. **Reseal after use**: Put the filament back in its original bag with the desiccant packet and seal tightly
2. **Dry storage boxes**: Store multiple spools in an airtight container with fresh desiccant (silica gel)
3. **Dryboxes**: Print-while-dry enclosures that feed filament from a dry compartment
4. **Monitor humidity**: Keep storage humidity below 15–20% RH

### Drying Filament

| Material | Drying Temp | Drying Time |
|---------|------------|------------|
| PLA | 45°C | 4–6 hours |
| PETG | 55°C | 4–6 hours |
| ABS/ASA | 60°C | 4–6 hours |
| TPU | 55°C | 4–6 hours |
| Nylon | 70–80°C | 8–12 hours |

**Drying methods**: Purpose-built filament dryers (Printdry, eSUN eBOX), food dehydrators, or a household oven (set very low — ovens are often inaccurate, use a thermometer).

> ⚠️ Do NOT dry filament in ovens above the specified temperature — PLA will soften and fuse to the spool.

---

## 5. Choosing the Right Material

Use this decision tree:

```
Will the part be outdoors (UV exposure)?
  → Yes → ASA
  → No
     ↓
Does it need to be flexible?
  → Yes → TPU
  → No
     ↓
Does it need to resist heat (>60°C)?
  → Yes → ABS, ASA, Nylon, or CF composite
  → No
     ↓
Does it need maximum strength/toughness?
  → Yes → PETG, Nylon, or CF composite
  → No → PLA (easiest, most forgiving)
```

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Beginner's Guide to 3D Filament — Five Most Common Choices](https://www.youtube.com/watch?v=FPtKehjNXpE) | YouTube | Clear comparison of PLA, PETG, ABS, TPU and Nylon for beginners |
| [The Beginner's Guide to 3D Printing Filaments](https://www.youtube.com/watch?v=Ha_xrFHyuUY) | YouTube | Covers material properties, use cases, and print settings per filament |
| [Ultimate Filament Buying Guide for Those New to 3D Printing](https://www.youtube.com/watch?v=ZXk-HRmkTPk) | YouTube | Practical buying advice with budget tips for choosing first filaments |
| [Master 3D Printing Filaments: Tips & Tricks for PLA, ABS, PETG](https://www.youtube.com/watch?v=Py7z_I_nKnI) | YouTube | Tips on print settings, storage, and solving filament-specific problems |
| [Top 7 Filament Types You Need to Know About](https://www.youtube.com/watch?v=XSSHe9ogP5g) | YouTube | Covers specialty filaments (CF, wood, glow) beyond the basics |

---

## 📚 Further Reading & Forums

- [Makers101 — 3D Printing Filament Guide 2025: PLA, TPU, PETG, ABS, ASA](https://makers101.com/3d-printing-filament-guide/) — Up-to-date comprehensive filament comparison with print settings
- [Bambu Lab — 3D Printer Filament Comparison Guide](https://bambulab.com/en-us/filament/guide) — Official comparison from a leading modern printer manufacturer
- [Simplify3D — Ultimate Material Properties Table](https://www.simplify3d.com/resources/materials-guide/properties-table/) — Side-by-side material specs table (temperatures, strength, flexibility)
- [Ultimaker — PETG vs PLA vs ABS: 3D Printing Strength Comparison](https://ultimaker.com/learn/petg-vs-pla-vs-abs-3d-printing-strength-comparison/) — Technical comparison from a professional printer brand
- [MatterHackers — 3D Printer Filament Comparison Guide](https://www.matterhackers.com/3d-printer-filament-compare) — Interactive comparison tool with community ratings

---

## ✅ Knowledge Check

1. What is the biggest weakness of PLA and why does it fail in a hot car?
2. Why is TPU recommended only for direct-drive extruders?
3. What happens physically when you print with wet Nylon? Why does moisture cause this?
4. You need to print a part for outdoor use that will be exposed to UV and rain. Which material do you choose?
5. An abrasive composite filament destroys brass nozzles. What type of nozzle must you use instead?
6. What temperature and duration should you dry Nylon at before printing?

---

*Module 04 of 8 — [← Software & Slicing](../03-software-and-slicing/README.md) | [Next: Printer Operations →](../05-printer-operations/README.md) | [Back to Index](../README.md)*
