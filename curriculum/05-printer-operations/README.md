# Module 05: Printer Operations & Calibration

> From first power-on to a perfect first layer — assembly basics, calibration procedures, and ongoing maintenance.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Describe the steps to assemble and verify a printer before first use
- Perform manual and automatic bed levelling
- Calibrate E-steps (extruder steps per mm)
- Calibrate flow rate (extrusion multiplier)
- Run a PID autotune for hot end and bed
- Perform regular maintenance tasks

## Prerequisites

- Module 01: Electronics Basics
- Module 02: Mechanical Basics
- Module 03: Software & Slicing

---

## 1. Pre-Flight Checklist (Before First Print)

Before powering on a newly assembled or received printer, verify:

### Mechanical
- [ ] Frame is square (measure diagonals — should be equal)
- [ ] All bolts are tight (but not over-tightened — can crack printed parts)
- [ ] Belts are tensioned — should sound like a low bass note when plucked
- [ ] Bed is roughly level (all four corners at similar height)
- [ ] Hot end fan spins freely
- [ ] Part cooling fan spins freely
- [ ] Extruder can push filament smoothly by hand (with motors off)

### Electrical
- [ ] PSU voltage switch set correctly (110V or 230V)
- [ ] All wiring connections seated firmly
- [ ] Thermistor wires are not pinched or touching the heater block
- [ ] No loose ferrules or bare copper exposed near hot components

### First Power-On
1. Power on without loading filament
2. Check that the screen/interface responds
3. Navigate to **Preheat** → preheat PLA → verify hot end and bed heat up
4. Check temperatures are reading sensibly (room temp, ~20–25°C)
5. **Home all axes** — the printer should move each axis to its end stop without crashing

---

## 2. Bed Levelling

The bed must be **co-planar with the toolhead's XY plane** at exactly the right Z distance from the nozzle.

### 2.1 Manual Bed Levelling (Paper Method)

**Goal**: Set each corner so a piece of paper slides with slight resistance when pulled between the nozzle and bed.

**Steps**:
1. Home all axes (`G28`)
2. Disable steppers (`M18`) so you can move the toolhead by hand
3. Move nozzle to front-left corner (5mm from each edge)
4. Slide paper under nozzle — adjust corner knob until slight resistance
5. Repeat for front-right, rear-right, rear-left, and centre
6. Go around 2–3 times until all corners are consistent

> ℹ️ The "paper" gap is approximately 0.1mm — about the thickness of a standard sheet of printer paper.

### 2.2 Automatic Bed Levelling (ABL / Mesh Levelling)

With a probe (BLTouch, CR Touch, etc.):

1. Ensure Z-offset is calibrated (see below)
2. Run `G29` (Marlin) or `BED_MESH_CALIBRATE` (Klipper)
3. The probe measures a grid of points (3×3 to 10×10 depending on config)
4. Firmware applies real-time Z compensation as the print head moves

### 2.3 Z-Offset Calibration

**Z-offset** = the distance from the probe trigger point to the nozzle tip.

**Method (Marlin)**:
1. Heat bed and hot end to print temperature
2. Home all axes
3. Navigate to **Motion → Z Probe Offset** (or use `M851`)
4. Use a sheet of paper; lower nozzle with `M851 Z-x.xx` until paper resistance is felt
5. Save: `M500`

**Method (Klipper)**:
1. Run `PROBE_CALIBRATE`
2. Use paper method to find Z height
3. `SAVE_CONFIG`

---

## 3. E-Steps Calibration (Extruder Steps Per mm)

**E-steps** = how many motor steps are needed to push 1mm of filament.

If E-steps are wrong, the printer under- or over-extrudes regardless of slicer settings.

### Procedure

1. **Mark 120mm** of filament from a reference point at the extruder entry
2. Send `G1 E100 F100` (extrude 100mm at 100mm/min)
3. **Measure the remaining distance** to your mark — should be 20mm remaining (100mm extruded)
4. If actual extruded distance ≠ 100mm, calculate correction:

$$\text{New E-steps} = \frac{\text{Current E-steps} \times 100}{\text{Actual extruded distance (mm)}}$$

5. Set new E-steps: `M92 E<new_value>` then save with `M500`

> ℹ️ Typical E-steps: MK8 extruder with standard Ender 3 = ~93 steps/mm. BMG 3:1 gear ratio = ~415 steps/mm.

---

## 4. Flow Rate / Extrusion Multiplier

E-steps get close; **flow rate** (a.k.a. extrusion multiplier) fine-tunes actual extrusion for a specific filament brand and colour.

### Procedure

1. Print a **single-wall cube** (0% infill, 1 perimeter, no top/bottom layers) at least 20mm tall
2. Measure the wall thickness with digital calipers at multiple points
3. Target thickness = nozzle diameter (0.4mm for standard nozzle) × line width factor

$$\text{Correction factor} = \frac{\text{Target wall thickness}}{\text{Measured wall thickness}}$$

4. Set in slicer as **Flow Rate** (e.g., 0.95 = 95%)

---

## 5. PID Tuning

**PID (Proportional-Integral-Derivative)** is a control loop algorithm that maintains stable temperatures. Without proper PID tuning, temperatures oscillate, causing inconsistent extrusion.

### PID Autotune — Hot End

```gcode
M303 E0 S215 C8    ; Autotune hot end (nozzle 0) at 215°C, 8 cycles
```

After completion, the firmware reports the PID values (Kp, Ki, Kd). Set them:

```gcode
M301 P22.20 I1.08 D114.00   ; Example values — use your own output
M500                          ; Save to EEPROM
```

### PID Autotune — Heated Bed

```gcode
M303 E-1 S60 C8   ; Autotune bed at 60°C, 8 cycles
M304 P... I... D... ; Set bed PID
M500
```

> ℹ️ PID tune at your **typical print temperature** for that material. Re-tune if you switch from PLA to ABS (different operating temp).

---

## 6. First Layer Calibration

The first layer is the foundation of the print. Use a live-adjust during the first layer:

**Perfect first layer signs**:
- Filament squishes slightly flat against the bed
- Lines slightly merge together
- No gaps between lines, no lifted edges
- No "spaghetti" or nozzle dragging through filament

**Too high (Z too far)**: Lines are round (not squished), don't stick, gaps between lines.

**Too low (Z too close)**: Nozzle drags, lines disappear, filament builds up on nozzle.

---

## 7. Regular Maintenance Schedule

### Every Print
- [ ] Visually inspect first layer before walking away
- [ ] Check that PTFE tube coupler is seated (no filament leaking from above)

### Every 10 Hours (or every few spools)
- [ ] Clean the print surface (isopropyl alcohol 70%+)
- [ ] Check belt tension — ping the belt, should sound consistent
- [ ] Check all printed parts for cracks (print quality degrades on cracked parts)

### Every 100 Hours
- [ ] Lubricate Z-axis lead screw (PTFE dry lube or super lube — NOT WD-40)
- [ ] Lubricate linear rods (light machine oil or PTFE)
- [ ] Inspect PTFE tube for cracks or yellowing near the hot end
- [ ] Verify all electrical connections are tight

### Every 500 Hours / as needed
- [ ] Replace PTFE tube (degrades with heat over time)
- [ ] Replace nozzle (brass nozzles wear after ~500h of abrasive filament)
- [ ] Inspect and re-tension belts
- [ ] Re-check E-steps if you notice over/under extrusion creeping in

---

## 8. Cold Pull (Nozzle Cleaning)

When a clog is forming but not complete, a cold pull can clear it without disassembly:

1. Heat hot end to print temp (e.g., 220°C for PLA)
2. Push filament manually until it extrudes cleanly
3. Cool hot end to ~90°C (PLA) — soft but not liquid
4. Pull filament firmly and quickly upward
5. The pulled filament will have a tip shaped by the nozzle interior — inspect for debris
6. Repeat 2–3 times until the tip comes out clean and conical

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Advanced Bed Leveling — Calibrating Your 3D Printer First Layer](https://www.youtube.com/watch?v=OVcULgI2VG8) | YouTube | Detailed first-layer calibration walkthrough for best adhesion |
| [Bed Levelling for Beginners — Perfect First Layer](https://www.youtube.com/watch?v=Ze36SX1xzOE) | YouTube | Friendly step-by-step manual bed levelling guide |
| [How to Calibrate Extruder E-steps (Ender 3)](https://www.youtube.com/watch?v=q3osFg0uBuI) | YouTube | Clear E-steps calibration procedure with the math explained |
| [Ender 3 S1 Pro — How To Calibrate E-Steps (Quick & Easy)](https://www.youtube.com/watch?v=VZScw30B4KA) | YouTube | Quick practical E-steps walkthrough on a popular beginner printer |
| [Calibrating eSteps For Frustrated Beginners](https://www.youtube.com/watch?v=-DEde0FhwLU) | YouTube | Troubleshoots common E-steps mistakes beginners make |

---

## 📚 Further Reading & Forums

- [Sovol3D — 3D Printer Calibration Step by Step for Beginners](https://www.sovol3d.com/blogs/news/3d-printer-calibration-step-by-step-beginners-guide) — Structured calibration guide from printer start to perfect first layer
- [Kingroon — Comprehensive Guide for 3D Printer Calibration](https://kingroon.com/blogs/3d-printing-guides/3d-printer-calibration) — Covers all calibration steps with photos
- [Obico — The Comprehensive OrcaSlicer Calibration Guide](https://www.obico.io/blog/orcaslicer-comprehensive-calibration-guide/) — Modern calibration workflow using OrcaSlicer's built-in tools
- [3DPrintingByBokey — Bed Leveling, E-Steps, and Flow Rate Explained](https://www.3dprintingbybokey.com/blog/calibrating-your-3d-printer-bed-leveling-e-steps-and-flow-rate) — Explains the 'why' behind each calibration step
- [r/ender3v2 — Calibration Instructions List (Forum)](https://www.reddit.com/r/ender3v2/comments/xeazbe/calibration_instructions_looking_for_a_list_of/) — Community-sourced calibration checklist
- [Teaching Tech Calibration Site](https://teachingtechyt.github.io/calibration.html) — Interactive calculators for E-steps, PID, flow rate, and first layer

---

## ✅ Knowledge Check

1. What is the paper method for bed levelling and what gap does it approximate?
2. You extruded 100mm of filament but only 92mm came out. What is your correction formula, and would the new E-steps value be higher or lower than the original?
3. What does PID tuning do, and what symptoms indicate poorly tuned PID?
4. Describe the signs of a first layer that is printed too far from the bed vs too close.
5. What lubricant should you use on a Z-axis lead screw, and what common lubricant should you avoid?

---

*Module 05 of 8 — [← Filaments & Materials](../04-filaments-and-materials/README.md) | [Next: Troubleshooting →](../06-troubleshooting/README.md) | [Back to Index](../README.md)*
