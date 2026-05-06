# ⚠️ Safety Quick Reference — 3D Printing Lab

> **Read this before touching any machine.** This is the consolidated safety SOP for all FDM 3D printing operations. Post a copy at each workstation.

---

## 🔴 Emergency Actions (Memorize These)

| Situation | Immediate Action |
|-----------|----------------|
| Fire / smoke from printer | Kill power switch → grab Class C extinguisher → evacuate if spreading |
| Thermal runaway (temp climbing out of control) | Hit EMERGENCY STOP in Mainsail/OctoPrint → cut mains power |
| Electrical burn/shock | Do NOT touch the person — kill power first, then call emergency services |
| Thermal burn (skin contact with nozzle/bed) | Cool under cold running water for 10 minutes — do NOT apply ice |
| Fume inhalation (ABS/ASA/resin) | Move to fresh air immediately — seek medical attention if symptoms persist |

**Emergency Stop in Klipper/Mainsail:** Large red button in the Mainsail/Fluidd web interface, or send `M112` in the console.

**Fire Extinguisher location:** Within 2 meters of every printer. Class C (CO₂ or dry chemical) rated. Check label monthly.

---

## 🔌 Electrical Safety

1. **Verify PSU voltage selector** before first use — must match your mains: 110V (North America) or 230V (Europe/Australia). Mismatch destroys the PSU and may cause a fire.
2. **Never open a PSU** or touch internal components — mains voltage is present even when the printer appears off.
3. **Wait 30 seconds after unplugging** before touching any internal wiring — capacitors retain charge.
4. **Touch a grounded metal surface** before handling control boards or stepper drivers (ESD — Electrostatic Discharge — destroys electronics silently).
5. **No bare mains wiring.** All AC connections must use insulated ferrules, approved terminals, or connectors rated for mains voltage.
6. **Always unplug before opening any enclosure** or reaching inside the electronics bay.
7. **Inspect power cables weekly** — look for cracked insulation, melted plastic, or scorch marks. Remove from service immediately if found.
8. **Use ferrule crimps** on all stranded wire ends going into screw terminals. Unferruled strands fray, short, and cause fires.
9. **Never exceed connector current ratings:**
   - JST-XH: 3A max — fans, sensors only
   - XT30: 30A max — medium power rails
   - XT60: 60A max — PSU output / high-current
10. **Route heater wires separately** from signal wires (thermistor, endstop) — high-current cables create EMI that causes false readings.

---

## 🔥 Thermal Safety

### Hotend and Nozzle
- Nozzle operating temperature: **185–320°C** (machine dependent). At 200°C, a 1-second contact causes a third-degree burn.
- **Never touch the nozzle or heater block during or immediately after printing.** Use long tweezers or pliers.
- Allow **15–20 minutes** of cool-down after print completion before any hotend service.
- Post a **"HOT — DO NOT TOUCH"** warning tag on the printer during a print run.
- Wear **heat-resistant gloves** (silicone or Kevlar) when performing hot nozzle swaps.

### Heated Bed
- Bed operating temperatures: **55–120°C** (material dependent).
- PEI spring-steel beds reach temperature rapidly — never rest your hand flat on the bed surface without checking the display first.
- **Never place flammable materials** (paper, cardboard, cloth) on or near the heated bed.

### Enclosures and Chambers (Dragon)
- Dragon's heated enclosure reaches **40–50°C chamber temperature** — the air inside is hot enough to cause discomfort.
- Keep face and hands clear when opening the Dragon enclosure door during an ABS/ASA print.
- Verify the **thermal cutoff** (TPS switch) is functional before every long high-temp print. Test procedure in Module 1, Section 2.3.

---

## ⚙️ Mechanical Safety

1. **Power off before reaching inside** any moving area — belts and carriages move at up to **300 mm/s** during homing.
2. **Keep long hair, loose clothing, and jewelry** secured or removed before operating any printer.
3. **Do not force any movement** by hand against a stalled or powered motor — you risk stripping gears, bending lead screws, or triggering a short.
4. During nozzle replacement: use **two wrenches** — one to hold the heater block, one on the nozzle. Never torque against the heat break (it will snap).
5. During bed leveling: **keep hands clear of the Z-travel path** — the gantry or bed can descend quickly if the Z-offset is misconfigured.
6. **Inspect belt paths monthly** — a frayed belt that snaps under tension can flick at high speed.
7. **Do not operate printers with loose frame bolts** — a dropped gantry is a collision risk.

---

## 🧯 Fire Safety

| Rule | Details |
|------|---------|
| **Never leave a print fully unattended** | Check every 30 minutes minimum. Use webcam + Mainsail remote alerts for after-hours monitoring. |
| **Thermal runaway protection must be ON** | Klipper: `thermal_runaway_hysteresis`, `thermal_runaway_timeout` must be set. Never disable. |
| **ABS/ASA in enclosures** | Max chamber temp 105°C. Active ventilation required. Fire suppression device strongly recommended for overnight runs. |
| **Keep area clear** | 500 mm clearance minimum around all printers. No cardboard boxes, paper, or flammable storage within 1 meter. |
| **Extinguisher type** | Class C (CO₂ or dry chemical) for electrical fires. Water and foam MUST NOT be used on printer fires. |
| **Post-print inspection** | After each print: inspect for scorch marks, burnt smell, or discolored wires. Any of these = stop and investigate. |

---

## 🧪 Chemical Safety

| Material | Risk | Control |
|---------|------|---------|
| **PLA** | Very low — minimal fumes | Standard room ventilation |
| **PETG** | Low | Standard room ventilation |
| **ABS / ASA** | Styrene fumes — irritant, potential carcinogen | Dedicated fume extraction fan + HEPA filter, or print outdoors |
| **Nylon** | Irritant fumes when heated | Fume extraction required |
| **Carbon-fiber filament** | Fine particulate dust during post-processing | N95 mask when sanding |
| **Solder flux** | Toxic fumes | Fume extractor at soldering station — mandatory |
| **Acetone (ABS smoothing)** | Highly flammable, vapors heavier than air | Fume hood only. No open flame anywhere in room |
| **IPA (Isopropyl Alcohol)** | Flammable | Keep away from all heat sources. Use 90%+ IPA only |

---

## 🤖 Twin Dragon (IDEX) — Dual-Head Safety Rules

The Twin Dragon is the only machine in the fleet with two independently moving print heads (IDEX = Independent Dual Extrusion). This creates unique hazards not present on single-head machines.

### Head Collision Risk

1. **Verify parking position macros before every dual-head print.** If a non-active head parks at the wrong X coordinate, it can collide with the active head or the model mid-print.
   - Safe park position for head 0 (left): X = 0 (far left rail)
   - Safe park position for head 1 (right): X = 300 (far right rail)
   - Test manually by running the parking macro with no filament loaded, before the actual print.

2. **Never manually jog both X motors simultaneously** from the Mainsail interface without understanding their independent positions. Unexpected collision can occur.

3. **Always run `G28` for full homing** before any IDEX print — partial homing (X-only or Y-only) may leave one head at an unknown position.

### Tool-Change Safety

4. **Non-active head temperature:** During a tool change, the non-active head cools to standby temperature (~170°C for PLA). This is still hot enough to cause burns. Do NOT reach into the printer during a tool change.

5. **Ooze risk:** Heated non-active nozzles ooze filament during the print. The purge tower (configured in slicer) collects this ooze — do NOT disable the purge tower in dual-material prints.

6. **Duplication Mode head spacing:** In Duplication Mode, both heads move simultaneously and are fixed at half the bed width (150 mm) apart. Do NOT run a print wider than 150 mm in Duplication Mode — both heads will crash into the model.

### Twin Dragon Pre-Print IDEX Safety Checklist

```
IDEX SAFETY — TWIN DRAGON ADDITIONAL CHECKS
================================================
□ T0 parking position tested — moves to X=0 without collision
□ T1 parking position tested — moves to X=300 without collision
□ Both nozzles homed and Z-offsets calibrated independently
□ IDEX mode confirmed: Single / Dual Material / Duplication / Mirror
□ Build width <= 150 mm if using Duplication or Mirror Mode
□ Purge tower enabled in slicer for any dual-material print
□ Both filament paths clear — extrude 10 mm from each head before print
□ Non-active head standby temp set to 170°C or lower in slicer
```

---

## ✅ Pre-Print Safety Checklist (Run Before Every Print)

```
SAFETY CHECKLIST — ALL MACHINES
==================================
□ PSU voltage selector verified for local mains
□ All connectors checked — no loose, burnt, or corroded pins
□ Printer area clear of flammable materials (500mm radius)
□ Thermal runaway protection enabled (verify in Klipper config)
□ Fire extinguisher present and accessible within 2 meters
□ Fume extraction running (for ABS/ASA/Nylon)
□ Print will be monitored — webcam or physical presence
□ Emergency stop location known (Mainsail red button or M112)
□ Machine is registered in Fracktory with operator name
```

---

## 🚨 Who to Contact

| Situation | Contact |
|-----------|---------|
| Fire or medical emergency | **Emergency Services (911/112)** — then team lead |
| Electrical fault (no fire) | Team Lead immediately — do not power back on |
| Mechanical damage | Team Lead — log in Fracktory under Maintenance |
| Unknown firmware/config error | Team Lead — check Klipper logs before touching anything |

---

*[Back to Curriculum Index](README.md)*
