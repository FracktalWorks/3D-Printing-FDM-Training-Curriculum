# Module 6: Troubleshooting FDM 3D Printers

> A systematic, diagnostic-first approach to identifying and resolving every common FDM print failure — from first-layer adhesion problems to firmware errors and wiring faults. Machine-specific notes for Snowflake, Julia, Dragon, and Twin Dragon included.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Identify the root cause of any common FDM print failure from visual inspection
- Use a multimeter to diagnose electrical faults (heater, thermistor, endstop, wiring)
- Apply the 5-Why methodology to find root causes (not just symptoms)
- Follow a machine-specific diagnostic checklist for Snowflake, Julia, Dragon, and Twin Dragon
- Fix the top 15 FDM printing failures using proven procedures
- Document failures and resolutions in Fracktory for team knowledge sharing

## Prerequisites

- Module 1: Electronics (multimeter use, wiring)
- Module 4: Printer Basics (hotend, thermistor, bed leveling)
- Module 5: Operations (Klipper, OctoPrint, slicer)

---

## 🛠️ Tools Required

| Tool | Purpose |
|------|---------|
| Digital multimeter | Continuity, resistance, and voltage testing for electrical faults |
| SSH client / OctoPrint Terminal | Klipper diagnostic commands and log access |
| VS Code with Remote SSH | Reviewing and editing `printer.cfg` |
| Hex key set (1.5–5 mm) | Mechanical inspection and adjustment |
| Digital calipers | Measuring extrusion output, dimensional accuracy |
| Flashlight or LED headlamp | Inspecting nozzle, extruder, and belt paths |
| Fracktory dashboard | Log review and failure documentation |
| Paper and pen (or Notes app) | Recording the 5-Why analysis during fault investigation |
| Cold-pull filament (nylon or PETG) | Clearing nozzle clogs |

---

## ⚠️ Safety Guidelines

1. **Don't test on a running print.** Always stop or pause the print before reaching into the machine. Moving parts cause injuries.
2. **Thermal runaway errors are safety-critical.** Never reset and immediately reprint after a thermal runaway. Investigate root cause first — a failed heater is a fire risk.
3. **Use insulated probes when testing at temperature.** Keep meter leads away from live terminals when the printer is powered on.
4. **MCU errors can mask electrical faults.** A `MCU Connection Failure` can be caused by a shorted motor wire. Unplug all motors and check each coil for shorts to ground before swapping USB cables.
5. **Layer shift mid-print:** If motors are energized and a layer shift is detected, stop the print with `CANCEL_PRINT` — do NOT try to reposition manually.
6. **Document before touching.** Photograph the failure state and log it in Fracktory before changing anything. You lose diagnostic evidence the moment you start "fixing."

---

## 1. Diagnostic Methodology

### 1.1 The 5-Why Framework

Never fix symptoms — find root causes. The **5-Why** method drills down by asking "why" five times.

**Example: Print lifted off the bed**

| Why? | Answer |
|------|--------|
| Why did the print fail? | It detached from the bed mid-print |
| Why did it detach? | First layer didn't adhere properly |
| Why didn't the first layer adhere? | Bed surface had contamination |
| Why was the bed contaminated? | Previous operator didn't clean it after removing the last print |
| Why wasn't it cleaned? | No checklist reminder before starting a print |

**Root cause:** Missing pre-print checklist step. Fix: add bed cleaning to mandatory checklist.

### 1.2 The Diagnostic Ladder

When a print fails, work through this sequence:

```
1. Replicate the failure → confirm it's real and repeatable
2. Inspect visually → what does the failure look like exactly?
3. Isolate the layer → what layer/time did the failure occur?
4. Check mechanical → belts, rails, extruder
5. Check electrical → heater, thermistor, endstops, board
6. Check firmware / config → wrong settings, corrupted config
7. Check slicer / model → slicing errors, non-manifold geometry
8. Check material → wet filament, wrong material settings
```

### 1.3 Log Everything

Every failure and fix must be logged in Fracktory under the job record. Include:
- Machine name
- Material and spool ID
- Failure type (from dropdown)
- Root cause determined
- Fix applied
- Result of fix (resolved / escalated)

This builds a team knowledge base that prevents repeated failures.

---

## 2. Failure Reference Guide

### 2.1 First Layer Failures

#### 2.1.1 No Adhesion / Print Falls Off Immediately

**Symptoms:** First layer peels up immediately or print falls off before layer 3.

| Check | Finding | Fix |
|-------|---------|-----|
| Bed surface | Fingerprints or contamination | Clean with 90%+ IPA |
| Z-offset | Too far from bed (gaps in first layer) | Lower Z-offset by 0.05 mm increments |
| Bed temperature | Below target | Verify temp reading vs. actual (IR thermometer) |
| First layer speed | Too fast | Set first layer speed to 20–25 mm/s |
| Bed surface condition | Scratched or worn PEI | Replace PEI sheet |

**Machine Note — Julia:** Julia's PEI glass surface requires cleaning before every print. The glass retains heat well but does not have the self-releasing properties of spring-steel PEI. Let prints cool to room temperature before removal.

#### 2.1.2 First Layer Too Squished (Nozzle Dragging)

**Symptoms:** First layer is completely flat, no bead texture, nozzle may leave marks or gouge PEI.

**Cause:** Z-offset is too negative (nozzle too close).

**Fix:** Raise Z-offset by 0.05 mm at a time until a slight bead texture is visible on the first layer.

**Emergency Stop:** If you see the nozzle dragging, immediately press EMERGENCY STOP in OctoPrint. Forcing the nozzle into the bed can damage the PEI sheet and in severe cases bend the probe or nozzle.

#### 2.1.3 Uneven First Layer (One Corner Peeling)

**Symptoms:** 3 corners stick, 1 corner peels up.

**Cause:** Bed not trammed (one corner further from nozzle than others).

**Fix:** Run manual tramming procedure (Module 4, Section 5.2). Adjust the peeling corner's adjustment knob counter-clockwise (raise bed toward nozzle).

---

### 2.2 Extrusion Failures

#### 2.2.1 Under-Extrusion

**Symptoms:** Gaps between extrusion lines, thin walls, weak parts with visible holes.

**Diagnostic tree:**

```
Under-Extrusion
├── Extruder clicking/skipping?
│   ├── YES → Check for clog in nozzle (Section 2.2.3)
│   │         Check Vref / current setting on driver
│   └── NO  → Check rotation_distance calibration (Module 4, Section 6)
│              Check temperature (filament not melting fast enough?)
│              Check print speed (too fast for hotend throughput)
└── Consistent or random?
    ├── RANDOM → Filament diameter variation / wet filament
    └── CONSISTENT → E-steps / rotation_distance wrong
```

**Typical fixes:**
1. Recalibrate rotation_distance (E-steps)
2. Increase print temperature by 5°C
3. Reduce print speed by 20%
4. Dry filament if it has been exposed to humid air

#### 2.2.2 Over-Extrusion

**Symptoms:** Blobby surfaces, strings everywhere, layers merging incorrectly, dimensional inaccuracy (parts too large).

**Causes:**
- Rotation_distance too low (extruding too much per command)
- Extrusion multiplier > 1.0 in slicer
- Flow rate incorrectly set

**Fix:**
1. Set slicer flow rate / extrusion multiplier back to 100%.
2. Print an extrusion calibration cube and measure wall thickness.
3. Adjust rotation_distance until walls are exactly specified thickness.

#### 2.2.3 Clogged Nozzle

**Symptoms:** No extrusion, or very thin, intermittent extrusion. Extruder motor skipping.

**Cold Pull (Atomic Pull) Procedure:**
1. Heat hotend to print temperature (e.g., 200°C for PLA).
2. Feed filament manually until fresh material comes out.
3. Cool hotend to **80–85°C** for PLA (not 90°C — at 90°C the filament is still too soft and tears instead of pulling cleanly). For PETG: cool to 100°C. For Nylon: cool to 110°C.
4. Apply firm, steady pull on filament — it will come out pulling a plug of debris.
5. Repeat 2–3 times until the pulled plug comes out completely clean.

**Needle Clearing Procedure (for partial clogs):**
1. Heat to print temperature.
2. Push a **0.35 mm acupuncture needle** up through the nozzle from below.
3. Move it in and out to break up the clog.
4. Extrude 50 mm of filament to clear.

**Nuclear Option — Nozzle Replacement:**
If clog won't clear, replace the nozzle (see Module 2, Section 6.2).

**Prevention:** Never let the hotend sit at temperature with no filament for more than 10 minutes. The filament chars and creates a solid plug.

#### 2.2.4 Stringing

**Symptoms:** Fine plastic threads (strings) spanning between features or walls.

**Cause:** Molten filament oozes from the nozzle during travel moves.

| Parameter | Current | Adjust To |
|-----------|---------|-----------|
| Retraction distance (Bowden) | 4 mm | 5–7 mm |
| Retraction distance (Direct Drive) | 0.5 mm | 0.8–1.5 mm |
| Retraction speed | 25 mm/s | 40–60 mm/s |
| Print temperature | 210°C | Try 200°C |
| Travel speed | 150 mm/s | 200+ mm/s |

**Machine-specific defaults:**
- Dragon (Bowden): Retraction = 5 mm, 45 mm/s
- Snowflake (Direct Drive): Retraction = 0.8 mm, 50 mm/s
- Julia (Direct Drive): Retraction = 0.8 mm, 45 mm/s
- Twin Dragon T0 (Direct Drive): Retraction = 0.8 mm, 50 mm/s

**If stringing persists after settings adjustments:** Dry the filament. Wet filament strings excessively.

---

### 2.3 Layer Shift

**Symptoms:** Print suddenly shifts horizontally mid-print, all layers above the shift are offset.

**Diagnostic:**

```
Layer Shift
├── X shift only → Check X-axis
│   ├── Belt tension too loose → Re-tension
│   ├── Pulley set screw loose → Tighten + Loctite
│   ├── X motor driver overheating → Check Vref, add cooling
│   └── Acceleration too high → Reduce in firmware
├── Y shift only → Check Y-axis (same as above)
└── Both X and Y → Print speed / acceleration too high
    Or loose frame connection
```

**Procedure:**

1. Power off printer. Manually move the carriage. Does it move freely or feel rough?
2. Check belt tension (Module 2, Section 4.4) — should be 120–150 Hz.
3. Grab each pulley and try to twist it on the shaft — if it rotates relative to the shaft, the set screw is loose. Tighten, add Loctite 243.
4. Check motor driver temperature during printing — should be warm, not hot (> 60°C surface = too hot).
5. Reduce `max_accel` in Klipper config by 20% and test.

**Machine Note — Snowflake:** Snowflake has InputShaper configured. If layer shifts occur, run `SHAPER_CALIBRATE` to re-tune resonance compensation after any mechanical changes.

---

### 2.4 Warping and Bed Adhesion Loss

**Symptoms:** Corners or edges of print lifting off bed during printing.

**Primary Causes:**

1. **Thermal gradient:** Outer edges of the print cool faster than center → thermal contraction causes lifting
2. **Insufficient first layer adhesion:** Not enough contact area or wrong surface
3. **Material characteristic:** ABS and ASA warp significantly without enclosure

**Fixes:**

| Material | Solution |
|----------|---------|
| PLA | Clean bed, check Z-offset, add brim (5–10 mm) |
| PETG | Use 75°C bed, clean bed, try smooth PEI if textured fails |
| ABS/ASA | Use enclosure (30–40°C chamber), 110°C bed, disable part cooling, use Brim |
| Large flat parts | Add brim, use draft shield in slicer |

**Brim vs. Raft:**
- **Brim:** Flat ring of material around the base (same Z height as first layer). Fast to print, easy to remove. Preferred.
- **Raft:** Full platform under the print. Slower, uses more material, harder to remove. Use only when extreme adhesion is required.

**Machine Note — Dragon:** Dragon has the highest-temperature bed (120°C max) and is the only machine with a full enclosure. Print all ABS/ASA on Dragon. Set chamber temperature: `SET_TEMPERATURE_FAN_TARGET TEMPERATURE_FAN=chamber TARGET=40`

---

### 2.5 Z-Artifacts — Banding and Wobble

**Symptoms:** Horizontal lines or wavy patterns repeating at regular intervals in the Z direction.

#### Z-Banding (Horizontal Lines at Regular Intervals)

**Cause:** Lead screw pitch error, coupling flex, or bed/gantry mechanical resonance.

**Fixes:**
1. Check all Z-axis lead screw coupling set screws — tighten with Loctite.
2. Verify the coupling is flexible (not a rigid coupling with misalignment).
3. Lubricate lead screws.
4. If using 4 lead screws: run `Z_TILT_ADJUST` (Klipper) to equalize all four corners.

#### Z-Wobble (Wavy, Sinusoidal Pattern)

**Cause:** Lead screw is bent or mounted off-center, causing the screw to whip.

**Fix:**
1. Power off, support the gantry.
2. Remove the coupling from the motor.
3. Spin the lead screw by hand — a bent screw will visually wobble.
4. Replace the bent lead screw with a new one.
5. Realign lead screw to be vertical — use anti-backlash nut mount with slight float (not rigidly fixed top and bottom).

---

### 2.6 Thermal Runaway Error

**Symptoms:** Printer stops mid-print with `THERMAL RUNAWAY` or `Heating Failed` error. In Klipper: `Error: THERMAL RUNAWAY Extruder`.

**Cause:** Firmware detected that the hotend temperature is not tracking the heater's command — the hotend either cooled unexpectedly (heater failure, thermistor failure, fan blowing on hotend) or the thermistor failed.

**Diagnostic:**

```
Thermal Runaway
├── Hotend temp crashed to near 0°C instantly → Thermistor disconnected or shorted
├── Hotend temp slowly fell and never recovered → Heater cartridge failed
│   → Measure heater resistance (should be 10–20Ω). OL = dead cartridge.
├── Temperature swings ±10°C randomly → Thermistor loose or partial contact
└── Happened during fast movement → Part cooling fan blowing on heater block
    → Redirect fan airflow, add silicone sock to heater block
```

> ⚠️ **Never disable thermal runaway protection.** It is a fire safety feature. A failed heater cartridge that is on while the thermistor reports low temperature will cause the printer to run the heater at full power indefinitely. Without thermal runaway protection, this is a fire risk.

**Standard fix:**
1. Power off.
2. Measure heater cartridge resistance (10–20 Ω expected).
3. Measure thermistor resistance (should change with temperature).
4. Replace the failed component.
5. PID tune after replacing heater or thermistor.

---

### 2.7 Endstop Failures

**Symptoms:** Printer won't home, homes to wrong position, or crashes carriage into frame.

**Diagnostic:**

```bash
# In Klipper console — query endstop states
QUERY_ENDSTOPS
# Expected output when carriage is NOT at endstop:
#   x:open y:open z:open
# When carriage IS at endstop (triggered):
#   x:TRIGGERED y:open z:open
```

**Common failures:**

| Symptom | Cause | Fix |
|---------|-------|-----|
| `x:TRIGGERED` when not at endstop | Endstop always closed (short or stuck switch) | Replace endstop or check for debris |
| `x:open` when carriage is at endstop | Endstop not making contact, broken wire, or disconnected | Check connector, test continuity on wires |
| Carriage slams into frame | Endstop signal inverted in firmware | Add/remove `!` pin inversion in Klipper config |

**Endstop wire continuity test:**
1. Power off.
2. Disconnect endstop connector from board.
3. Set meter to continuity.
4. Test each wire in the connector to its corresponding pin at the endstop.
5. A healthy 3-wire mechanical endstop should show:
   - GND (continuity always)
   - VCC (continuity always)
   - SIG: beep when endstop NOT pressed, silence when pressed (or vice versa depending on NC/NO type)

---

### 2.8 Stepper Motor Failures

**Symptoms:** Motor not moving, vibrating without movement, making grinding noise, or moving in wrong direction.

**Diagnostic steps:**

1. **Wrong direction:** Add or remove `!` in front of `dir_pin` in Klipper config for that stepper.
2. **No movement at all:**
   - Check motor connector is fully seated.
   - Measure coil resistance (2–10 Ω per coil pair).
   - Check stepper driver — is it getting warm? Is it inserted correctly?
3. **Vibrating without movement (motor hunting):** Coil A or B is swapped. Swap pins 2 and 3 in the connector, or update wiring.
4. **Skipping steps:** Current set too low (adjust Vref) or acceleration too high (reduce `max_accel`).

---

### 2.9 Raspberry Pi / OctoPrint / Klipper Connectivity Issues

**Symptoms:** OctoPrint shows "Offline," can't connect to printer, or Klipper shows "MCU (Microcontroller Unit) Connection Failure."

**Step 1 — SSH to the Raspberry Pi and check Klipper status:**
```bash
ssh snowflake
sudo systemctl status klipper
# Should show: Active: active (running)
```

**Step 2 — Check USB connection:**
```bash
ls /dev/serial/by-id/
# Should list a USB device that matches printer MCU
# If empty: USB cable disconnected, damaged, or MCU needs a reflash
```

**Step 3 — Check Klipper log for errors:**
```bash
tail -50 ~/printer_data/logs/klippy.log
```

**Step 4 — Restart Klipper:**
```bash
sudo systemctl restart klipper
```

**Step 5 — If still failing:**
```bash
# Restart the entire Raspberry Pi
sudo reboot
```

**Step 6 — If Klipper fails to connect after reboot:** The MCU firmware may need reflashing. Follow the Klipper documentation for flashing the MKS board over DFU mode.

---

## 3. Machine-Specific Troubleshooting Notes

### 3.1 Snowflake — Quick Reference

| Issue | Known Cause | Fix |
|-------|------------|-----|
| Layer shift after fast infill | InputShaper needs recalibration | Run `SHAPER_CALIBRATE` |
| BLTouch deploy fails | Probe pin stuck | Manually retract pin, clean probe sleeve |
| Z-offset drifts between sessions | Thermal expansion of frame | Always run `PROBE_CALIBRATE` at print temperature |
| Extruder clicking at high speeds | Pressure advance misconfigured | Reduce PA to 0.04, re-calibrate |

### 3.2 Julia — Quick Reference

| Issue | Known Cause | Fix |
|-------|------------|-----|
| CR Touch gives inconsistent Z readings | Glass bed has inconsistent surface | Clean glass with IPA; run 5×5 mesh |
| First layer adhesion on glass | Surface not warm enough | Let bed soak at 60°C for 5 minutes before printing |
| Y-axis layer shift | Y belt tension tends to loosen | Check belt frequency weekly, re-tension |
| Klipper MCU disconnects | USB cable quality | Replace USB cable (use shielded data cable, not charge-only) |

### 3.3 Dragon — Quick Reference

| Issue | Known Cause | Fix |
|-------|------------|-----|
| Bowden path clog | PTFE tube degradation at high temps | Replace PTFE at 260°C+ — use Capricorn or all-metal hotend |
| Warping on large ABS prints | Insufficient chamber heat | Run chamber to 40°C before starting; use 5-mm brim |
| CAN bus connection error | Loose CAN connector on toolhead | Check and reseat CAN connector; check terminator resistor |
| Z-wobble | Lead screw whip on 400mm travel | Check coupling, add Z brace if present |

### 3.4 Twin Dragon — Quick Reference

| Issue | Known Cause | Fix |
|-------|------------|-----|
| T0/T1 X-offset wrong | Offset needs recalibration after any toolhead service | Run `T0_OFFSET_CALIBRATION` macro |
| Stringing on T1 during idle | T1 oozes while T0 prints | Increase T1 idle temperature cooldown or add wipe tower |
| Duplication mode size limit | Each head limited to half bed width | Parts max 150mm in X for duplication mode |
| IDEX carriage collision | Wrong T1 park position | Verify park position: `G0 X300` parks T1 at right of bed |

---

### 3.5 Twin Dragon — IDEX Head Collision Fault Tree

An IDEX carriage collision occurs when T0 and T1 attempt to occupy the same X position simultaneously. This is one of the more dangerous failure modes — the carriages can collide at 200+ mm/s, stripping belts and bending carriages.

**Causes and diagnosis:**

```
IDEX Head Collision
├── Did it happen during a toolchange?
│   ├── YES → T1 park position not set correctly in printer.cfg
│   │         Check: [dual_carriage] safe_distance setting
│   │         Fix: Increase safe_distance by 5 mm; verify T1 parks before T0 moves
│   └── NO (collision during printing)
│       ├── Is T1 active but idle temp not set?
│       │   → T1 ooze forces it out of park if not held by motor
│       │   Fix: Set idle temp on inactive head, enable hold_current
│       └── Is T0 commanded past the safe zone?
│           → Slicer placed geometry past X midpoint in duplication mode
│           Fix: In duplication mode, max X per part = 150 mm (half bed width)
```

**Recovery after collision:**
1. **EMERGENCY STOP immediately** — do not attempt `CANCEL_PRINT` after a collision.
2. Power off Twin Dragon completely.
3. Manually push both carriages away from each other.
4. Inspect belt teeth on both X-axis belts — look for skipped teeth or fraying.
5. Inspect carriage mounts — look for cracked printed parts or bent rods.
6. If belts are undamaged, re-home carefully: `SET_KINEMATIC_POSITION X=150` before `G28 X`.
7. Run `T0_OFFSET_CALIBRATION` after any collision before resuming dual-material prints.
8. Log the incident in Fracktory with "IDEX Collision" failure type.

> ⚠️ **Prevention is critical.** Never manually move T0 past X=280 mm or T1 below X=20 mm without first confirming the other head's position. Always test new IDEX toolchange macros with slow speed (`F300`) before running at production speed.

---

## 4. Real-World Troubleshooting Scenarios

### Scenario A: Snowflake Won't Start a Print

**Reported by operator:** "Snowflake shows an error after homing, can't start the print."

**Investigation:**
1. Connect to OctoPrint — error message reads: `Error: BLTouch failed to deploy`
2. Send `BLTOUCH_DEBUG COMMAND=pin_down` — probe doesn't deploy
3. Send `BLTOUCH_DEBUG COMMAND=reset` — still no movement
4. Power off, inspect BLTouch physically — probe pin is stuck in up position
5. Use a thin rod to gently push the pin down — it deploys

**Root Cause:** The probe pin had partially charred filament stuck around the sleeve (from a recent near-crash).

**Fix:** Clean the sleeve with IPA on a cotton swab. Test 5 deploy/retract cycles before printing.

**Resolution logged in Fracktory:** BLTouch probe pin stuck due to filament contamination — cleaned and verified.

---

### Scenario B: Julia Prints Have Horizontal Lines Every 2mm

**Reported:** "All prints on Julia have horizontal banding that repeats every 2mm."

**Investigation:**
1. Inspect the print — banding is very regular, every 2 mm → matches T8×2 lead screw pitch
2. Power off, inspect Z-axis lead screw coupling — find the set screws loose
3. Manually turn the lead screw — slight wobble detected
4. Tighten coupling set screws and add Loctite 243

**Root Cause:** Loose lead screw coupling causing the screw to translate eccentrically once per revolution, creating a pattern at the lead screw pitch interval.

**Fix:** Tighten + Loctite set screws. Print a calibration tower to verify — banding eliminated.

---

### Scenario C: Dragon Thermal Runaway During ABS Print

**Reported:** "Dragon stopped mid-print with a thermal runaway error. Print was 3 hours in."

**Investigation:**
1. SSH to Dragon Raspberry Pi — check `klippy.log`
2. Log shows: temperature dropped from 250°C to 190°C in 8 seconds, then triggered thermal runaway
3. Inspect hotend — heater cartridge connector is partially pulled out of board
4. Measure cartridge resistance: 15 Ω — cartridge itself is fine
5. Inspect connector on board — bent pin, intermittent contact

**Root Cause:** Connector pin damaged by repeated drag-chain stress, finally failed during thermal expansion at high temperature.

**Fix:** Replace connector with a properly crimped replacement. Secure wire with zip ties at cable chain entrance to prevent tension on connector. Re-PID tune.

---

## 5. Electrical Diagnostic Quick Reference

### 5.1 Multimeter Tests — All in One

| What to Test | Setting | Expected Result | Fail Result |
|-------------|---------|----------------|------------|
| PSU output | DC V, 50V | 23.8–24.2V | < 22V or > 26V |
| Heater cartridge | Ω, 200Ω | 10–20 Ω | OL (open) or 0 Ω |
| Thermistor (room temp) | Ω, 200kΩ | ~100 kΩ | OL or 0 Ω |
| Motor coil A | Ω, 200Ω | 2–10 Ω | OL or 0 Ω |
| Motor coil B | Ω, 200Ω | 2–10 Ω | OL or 0 Ω |
| Wire continuity | Continuity | Beep | Silence (open circuit) |
| TPS (thermal fuse) | Continuity | Beep (when healthy) | Silence (tripped) |
| Endstop (NO type) | Continuity | Silence (not pressed) / Beep (pressed) | Always same |
| Fan voltage | DC V, 50V | 24V (at fan connector) | 0V (no power) |

---

## ❌ Common Mistakes

| Mistake | What Happens | Correct Practice |
|---------|-------------|------------------|
| Fixing the symptom, not the root cause | Problem recurs within 1–5 prints | Apply 5-Why analysis first; document root cause in Fracktory |
| Replacing parts before testing | Wasted parts, same fault remains | Test with multimeter first; only replace after confirming component fails spec |
| Adjusting Z-offset to fix first-layer warping | Masks a bed leveling or mesh problem | Re-run `BED_MESH_CALIBRATE` first; adjust Z-offset only for a true height offset |
| Increasing hotend temp to fix under-extrusion | Stringing, blobs, thermal degradation | Check for partial clog first (cold pull); increase temp only as last resort |
| Running `G28` while a print is active | Destroys print in progress | Use `CANCEL_PRINT` macro — it retracts, cools, then homes safely |
| Ignoring the Klipper log during diagnosis | Missing the actual error (usually 5 lines above the visible message) | Run `tail -50 ~/printer_data/logs/klippy.log` and read from the first ERROR line |
| Changing multiple settings simultaneously | Can't identify which change fixed the problem | Change ONE variable at a time; test and document between each change |
| Dismissing wet filament as a cause | Every subsequent print has the same quality issues | Dry filament first and re-test before any other diagnosis |

---

## 6. Hands-On Exercises

### Exercise 6.1 — Fault Injection (Controlled Failures)
- [ ] Intentionally disconnect the thermistor connector on Julia (printer off). Power on and record the exact error message
- [ ] Reconnect thermistor. Verify the error clears after `FIRMWARE_RESTART`
- [ ] Intentionally set Z-offset 0.5 mm too high on Snowflake and inspect the first layer result

### Exercise 6.2 — Cold Pull
- [ ] Perform a cold pull on Julia's hotend using PLA
- [ ] Examine the pulled plug — is it clean? How many pulls did it take to clean?

### Exercise 6.3 — Endstop Diagnosis
- [ ] Use `QUERY_ENDSTOPS` to verify all endstops on Dragon are in the correct state
- [ ] Manually trigger each endstop and confirm the query changes to `TRIGGERED`

### Exercise 6.4 — Belt Tension Audit
- [ ] Measure belt tension on all axes of Snowflake and Julia
- [ ] Document values. Identify any out-of-spec axes
- [ ] Adjust and re-measure until all axes are within 120–150 Hz

### Exercise 6.5 — Log a Failure in Fracktory
- [ ] Take a failed print (from a previous exercise or a real failure)
- [ ] Complete the Fracktory failure log: machine, material, failure type, root cause, fix applied
- [ ] Review two other team members' logged failures

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [3D Printing Troubleshooting Guide](https://www.youtube.com/watch?v=7mKTxlRKrYw) | Teaching Tech | Visual guide to 25+ common print failures with fixes |
| [Solving Layer Shifts](https://www.youtube.com/watch?v=gkPNVgTR3_I) | ModBot | Systematic diagnosis of X and Y layer shifts |
| [Cold Pull / Atomic Pull Tutorial](https://www.youtube.com/watch?v=k0_nVmHNJLM) | Thomas Sanladerer | Correct cold pull technique for clearing clogs |
| [Klipper Thermal Runaway Explained](https://www.youtube.com/watch?v=Nqzf6HMD68M) | The Edge of Tech | What thermal runaway is, why it exists, and how to fix it |
| [Diagnosing Stringing](https://www.youtube.com/watch?v=cRvyBFNGKHY) | CNC Kitchen | Data-driven analysis of stringing causes and solutions |

---

## 📚 Further Reading

- [Teaching Tech Calibration Site](https://teachingtechyt.github.io/calibration.html) — Calibration tools and interactive troubleshooting guides
- [Ellis's Print Tuning Guide — Troubleshooting](https://ellis3dp.com/Print-Tuning-Guide/articles/troubleshooting.html) — Klipper-specific troubleshooting with root-cause depth
- [Klipper Troubleshooting Documentation](https://www.klipper3d.org/FAQ.html) — Official FAQ and known issues
- [Simplify3D Print Quality Troubleshooting](https://www.simplify3d.com/resources/print-quality-troubleshooting/) — Visual defect guide with photos and solutions

---

## ✅ Knowledge Check

1. A print on Dragon shows a layer shift only in the X-direction. List the three most likely causes and the order you would check them.
2. Klipper throws a `THERMAL RUNAWAY` error on Snowflake. What is the first electrical measurement you make, and what result would confirm a dead heater cartridge?
3. You pull a 0.5 mm acupuncture needle through a clogged nozzle. Some debris comes out, but extrusion is still inconsistent. What is the next step in the unclogging procedure?
4. Julia's CR Touch is giving inconsistent Z-readings across the bed mesh. The probe reads Z=1.45 in the front-left but Z=2.10 in the back-right. What are two possible causes, and which do you check first?
5. The Twin Dragon's T0/T1 X-offset appears to be 0.5 mm off after you replaced toolhead T1. What Klipper command do you run to recalibrate?
6. Using the 5-Why method, trace the root cause for: "ABS parts consistently warp on the third layer on Dragon."
7. A motor on Snowflake measures OL on both coil pairs. What does this indicate, and what do you do?

---

*Module 6 of 6 — [Back to Index](README.md)*
