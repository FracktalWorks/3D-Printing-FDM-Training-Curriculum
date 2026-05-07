# Module 06: Troubleshooting Common Issues

> A systematic guide to diagnosing and fixing the most common 3D printing failures.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Use a systematic diagnostic approach to identify print failures
- Diagnose and fix the 10 most common 3D printing problems
- Distinguish between hardware, software, and settings causes
- Know when to attempt a fix vs when to restart

## Prerequisites

- Module 03: Software & Slicing
- Module 05: Printer Operations & Calibration

---

## 1. Systematic Diagnostic Approach

Before guessing, follow a process:

```
1. Identify the symptom (what does the failed print look like?)
2. When did it start? (First layer? Mid-print? Always? Intermittent?)
3. What changed recently? (New filament? New settings? Hardware?)
4. Form a hypothesis (most likely cause)
5. Test ONE fix at a time
6. Verify the fix worked before changing anything else
```

> ⚠️ Never change multiple settings at once. You won't know which fix worked.

---

## 2. Issue Reference Table

| Issue | Primary Cause Category | Jump To |
|-------|----------------------|---------|
| Stringing | Retraction / temperature | §3 |
| Warping / lifting | Bed adhesion / temperature | §4 |
| Layer shifting | Mechanical / speed | §5 |
| Under-extrusion | Flow / extruder / clog | §6 |
| Over-extrusion | Flow settings | §7 |
| Clogged nozzle | Temperature / debris | §8 |
| Poor layer adhesion | Temperature / speed | §9 |
| First layer not sticking | Z-offset / bed surface | §10 |
| Spaghetti / print failure | Detachment from bed | §11 |
| Ringing / ghosting | Speed / belt tension / vibration | §12 |

---

## 3. Stringing

**Symptom**: Thin strings of filament crossing open spaces between features.

```
Good:  □        □
Bad:   □--------□   ← strings
```

**Causes & Fixes**:

| Cause | Fix |
|-------|-----|
| Retraction distance too low | Increase retraction (Bowden: 4–7mm, Direct: 0.5–2mm) |
| Retraction speed too low | Increase to 40–60 mm/s |
| Temperature too high | Lower hot end temp by 5°C increments |
| Travel speed too slow | Increase travel speed (200+ mm/s) |
| Combing OFF | Enable combing — travels within the part don't cross gaps |
| PETG — inherently stringy | Lower temp, enable coasting, reduce retraction speed |

**Diagnostic print**: Print a stringing tower (multiple columns) to dial in retraction.

---

## 4. Warping / Lifting

**Symptom**: Corners or edges of the print lift off the bed during printing.

**Root cause**: The material contracts as it cools. If the bottom layers cool unevenly or too fast, they pull the print off the bed.

| Cause | Fix |
|-------|-----|
| Bed too cold | Increase bed temperature (ABS: 110°C, PETG: 80°C) |
| No enclosure (ABS/ASA) | Print inside an enclosure — traps heat |
| Draught | Eliminate air movement around the printer |
| Poor first layer adhesion | Re-calibrate Z-offset; clean bed with IPA |
| Bed surface worn out | Replace or condition PEI surface |
| Part cooling too high | Reduce part cooling fan speed |
| Print not using brim | Add a brim (5–15mm) in slicer to anchor edges |

**Material-specific**:
- ABS always needs an enclosure
- PETG: mild warping — small brim usually fixes it
- PLA: minimal warping — usually a Z-offset or bed cleanliness issue

---

## 5. Layer Shifting

**Symptom**: Layers are misaligned in X or Y — the print looks "stepped" or sheared.

```
Good:     ████████
          ████████
Bad:       ████████  ← shifted right
          ████████
```

| Cause | Fix |
|-------|-----|
| Belt too loose | Re-tension the belt — should sound like a low bass note |
| Print speed too high | Reduce print speed (especially for CoreXY at high accel) |
| Motor current too low | Increase stepper driver current (check driver specs) |
| Motor overheating | Check driver cooling; reduce motor current if very hot |
| Acceleration too high | Reduce max acceleration in firmware |
| Something obstructing the motion | Inspect for cables caught in belts or carriage |
| Grub screw loose on pulley | Check and tighten grub screws on motor pulleys |

**Which axis shifted?**: Look at the direction of shift.
- Shift in X-direction → Y-axis motor/belt issue (or CoreXY: one of the two motors)
- Shift in Y-direction → X-axis motor/belt issue (or CoreXY: same)

---

## 6. Under-Extrusion

**Symptom**: Gaps in layers, thin walls, weak prints with missing material.

```
Good:  ████████████  (solid, no gaps)
Bad:   ██ ███  ████  (gaps in lines)
```

| Cause | Fix |
|-------|-----|
| Partial clog in nozzle | Cold pull; replace nozzle if persistent |
| Extruder grinding filament | Reduce retraction; reduce print speed; increase temp slightly |
| Temperature too low | Increase hot end temp by 5°C |
| Flow rate too low | Increase flow rate in slicer |
| E-steps wrong | Re-calibrate E-steps |
| PTFE tube gap (Bowden) | Ensure PTFE tube pushes all the way into the hot end — no gap |
| Filament too thin (bad spool) | Check filament diameter variance with calipers |
| Wet filament | Dry the filament |

---

## 7. Over-Extrusion

**Symptom**: Too much material — blobs, bulging corners, rough surface, dimensional inaccuracy.

| Cause | Fix |
|-------|-----|
| Flow rate too high | Reduce flow rate (extrusion multiplier) in slicer |
| E-steps too high | Re-calibrate E-steps |
| Temperature too high (low viscosity) | Lower hot end temp |

---

## 8. Clogged Nozzle

**Symptom**: No filament coming out, or very thin/inconsistent flow despite no movement blockage.

### Severity Levels

| Level | Symptom | Fix |
|-------|---------|-----|
| Partial | Under-extrusion, weak prints | Cold pull (see Module 05) |
| Full | No extrusion at all | Cold pull → nozzle removal → replace |

### Clog Prevention

- Always print at the minimum recommended temp (too low = unmelted filament jams)
- Purge before starting if the printer has been idle with filament loaded
- Replace nozzle every ~500 hours or if consistently clogging
- Use hardened nozzle for abrasive filaments

### Nozzle Removal Procedure

1. Heat to print temperature (nozzle must be hot to remove safely)
2. Use a nozzle wrench or socket to unscrew counterclockwise (hold heater block steady with a spanner — do NOT let the block spin)
3. Clear residue; thread in new nozzle hand-tight; final 1/8 turn with wrench

> ⚠️ **Hot tightening**: Nozzle must be tightened at operating temperature. A cold-tightened nozzle may leak at temperature due to thermal expansion.

---

## 9. Poor Layer Adhesion

**Symptom**: Print delaminating (layers separating), weak Z-strength, layers peeling apart.

| Cause | Fix |
|-------|-----|
| Temperature too low | Increase hot end temp — better layer fusion |
| Print speed too high | Reduce speed — layers need time to bond |
| Layer height too large | Reduce layer height — more overlap between layers |
| Part cooling too aggressive | Reduce fan speed, especially for ABS/PETG |
| Wet filament | Dry the filament |

---

## 10. First Layer Not Sticking

**Symptom**: First layer lifts, slides around, or doesn't adhere to the bed.

| Cause | Fix |
|-------|-----|
| Z-offset too high | Lower the nozzle (smaller Z-offset number) |
| Dirty bed | Clean with IPA 70%+ — oils from fingers ruin adhesion |
| Wrong bed surface for material | Match surface to material (see Module 04) |
| Bed temp too low | Increase bed temperature |
| First layer speed too fast | Reduce first layer speed to 20–25 mm/s |
| No brim for small footprint | Add a brim |

---

## 11. Print Detaches Mid-Print (Spaghetti)

**Symptom**: Print detaches mid-way through, printer continues printing into air, producing "spaghetti".

**Primary cause**: First layer adhesion failure that wasn't caught early.

**Fixes**: 
- Fix the root cause (Z-offset, bed surface, temperature)
- Enable failure detection via OctoPrint cameras — monitor prints remotely and pause if issues arise

---

## 12. Ringing / Ghosting

**Symptom**: Rippled or wavy pattern on walls near sharp features (like text, sharp corners). Pattern repeats at regular intervals.

```
Before corner:  ~~~CORNER~~~  (wavy ripples from vibration)
```

| Cause | Fix |
|-------|-----|
| Print speed too high | Reduce print speed |
| Acceleration too high | Reduce acceleration |
| Loose belts | Tighten belts |
| Heavy toolhead (direct drive) | Reduce acceleration; add input shaping (Module 07) |
| Resonance from surface | Place printer on a foam mat |

**Best fix**: Input shaping (Klipper) — accelerometer-based vibration compensation. Covered in Module 07.

---

## 13. Quick Reference Cheat Sheet

| Symptom | First Thing to Check |
|---------|---------------------|
| Stringing | Retraction distance + temperature |
| Warping | Bed temp + enclosure + brim |
| Layer shift | Belt tension + print speed |
| Under-extrusion | Nozzle clog + E-steps + flow rate |
| No extrusion | Nozzle clog + extruder grinding |
| First layer peeling | Z-offset + clean bed + bed temp |
| Weak prints | Temperature + layer adhesion |
| Blobs on walls | Retraction + travel speed |
| Ringing on walls | Print speed + belt tension |

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [20+ Reasons Your 3D Prints Look Terrible (SOLVED)](https://www.youtube.com/watch?v=IVhVmARVgig) | YouTube | Comprehensive visual guide — matches every print defect to its cause and fix |
| [How to Diagnose and Fix Layer Shifts in Your 3D Prints](https://www.youtube.com/watch?v=9VFpXUXgyJ8) | YouTube | Systematic layer-shift diagnosis covering mechanical and electrical causes |
| [The ACTUAL REASON Why 3D Prints WARP](https://www.youtube.com/watch?v=-ZPV-nVIIX4) | YouTube | Science-based explanation of warping — not just surface fixes |
| [Say Goodbye to Stringing Forever — 3D Printing Tips](https://www.youtube.com/watch?v=yaxRq4unCEY) | YouTube | Step-by-step retraction tuning to eliminate stringing permanently |
| [How To FIX Warping and Adhesion Problems](https://www.youtube.com/watch?v=U8vM6lAkcYU) | YouTube | All bed adhesion and warping fixes in one comprehensive video |

---

## 📚 Further Reading & Forums

- [Obico — 3D Print Troubleshooting: The Ultimate Guide to Fix Every Problem](https://www.obico.io/blog/3d-print-troubleshooting-guide/) — Comprehensive defect-by-defect guide with photos and fixes
- [Simplify3D — Print Quality Troubleshooting Guide](https://www.simplify3d.com/resources/print-quality-troubleshooting/) — Industry-standard visual reference for diagnosing print defects
- [Ellis' Print Tuning Guide](https://ellis3dp.com/Print-Tuning-Guide/) — Community's most complete calibration and troubleshooting resource
- [r/FixMyPrint — Free 3D Printing Troubleshooting Guides (Forum)](https://www.reddit.com/r/FixMyPrint/comments/1sx6xty/free_3d_printing_troubleshooting_guides_stringing/) — Community-curated troubleshooting guides for stringing, warping, wet filament
- [Fracktal Works Support Portal](https://care.fracktal.in) — Official Fracktal support for Dragon, Twin Dragon, and Snowflake machines
- [Sovol3D — Fixing 3D Printer Layer Shifting](https://www.sovol3d.com/blogs/news/fix-3d-print-layers-shifting-common-issues-and-solutions) — Focused guide on layer shift causes and solutions

---

## ✅ Knowledge Check

1. You see strings between features on your print. Name three settings to adjust and in what direction.
2. Your print's corners are lifting during the print. You're printing ABS without an enclosure. What is the most likely cause and fix?
3. A layer shift occurs mid-way through a long print. How do you determine which axis shifted, and what do you check first?
4. Why should you only change one setting at a time when troubleshooting?
5. What is the difference between stringing and oozing? Are they fixed the same way?
6. Describe the cold pull procedure and when to use it.

---

*Module 06 of 8 — [← Printer Operations](../05-printer-operations/README.md) | [Next: Advanced Topics →](../07-advanced-topics/README.md) | [Back to Index](../README.md)*
