# Module 1: Electronics for 3D Printing

> Hands-on electronics knowledge required to wire, diagnose, and maintain FDM 3D printers — including multimeter use, soldering, connectors, and MKS control boards.

![NEMA 17 stepper motor — the primary motion actuator used in all axes and the extruder of an FDM 3D printer](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Stepper_motor.jpg/320px-Stepper_motor.jpg)
*A NEMA 17 stepper motor — the standard actuator in 3D printers, used for X, Y, Z axes and the extruder. This module covers how to wire and diagnose these and the board they connect to. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Stepper_motor.jpg), CC BY 3.0*

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Use a multimeter to measure voltage, current, resistance, and test continuity
- Identify and safely use common connectors (JST, Dupont, Molex, XT60)
- Perform basic soldering and de-soldering tasks to a production standard
- Identify MKS board pinouts and connect stepper drivers, heaters, and sensors
- Safely wire a 3D printer from board to peripherals
- Design simple circuits using Cirkit Designer

## Prerequisites

- None. Basic literacy and comfort handling small components is sufficient.

---

## 🛠️ Tools Required

| Tool | Purpose |
|------|---------|
| Digital multimeter (auto-ranging preferred) | Voltage, resistance, continuity testing |
| Soldering iron (25–60W, adjustable) | Soldering XT60, PCB repairs |
| Solder (60/40 rosin-core, 0.8 mm) | Joining wires and connector pins |
| Flux pen | Improving solder flow on pads |
| JST crimp tool (PA-09 or equivalent) | Crimping JST-XH, JST-PH connectors |
| Ferrule crimp tool + assorted ferrules | Terminating stranded wire to terminals |
| Wire strippers (0.5–6 mm²) | Stripping wire insulation cleanly |
| Desoldering pump or solder wick | Removing old solder |
| Helping-hands tool or PCB vise | Holding work steady during soldering |
| ESD wrist strap | Preventing electrostatic damage to boards |
| Safety glasses | Flux spatter protection |

---

## 1. Safety First

**Always observe these rules before touching any electronics:**

1. **Unplug before working** — Disconnect the printer's mains cable before opening any enclosure or touching wiring.
2. **Discharge capacitors** — Power supplies hold charge after unplugging. Wait 30 seconds.
3. **No bare mains wiring** — 110V/230V AC is lethal. All mains connections must use insulated ferrules or approved connectors.
4. **ESD precaution** — Touch a grounded metal surface before handling control boards or stepper drivers to avoid electrostatic discharge (ESD) damage.
5. **Multimeter range** — Always start on the highest range and work down to avoid damaging the meter.

> ⚠️ **Critical:** The PSU (Power Supply Unit) input side carries mains voltage. Never probe inside a PSU while it is plugged in.

---

## 2. Multimeter Fundamentals

![Digital multimeter (DMM) — essential diagnostic tool for measuring voltage, resistance, current and testing continuity in 3D printer wiring](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Digital_Multimeter_Aka.jpg/350px-Digital_Multimeter_Aka.jpg)
*A digital multimeter (DMM) — measures DC/AC voltage (V), resistance (Ω), current (A), and tests continuity. This is the most important tool for diagnosing 3D printer electrical faults. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Digital_Multimeter_Aka.jpg), CC BY-SA 2.5*

A **multimeter** (also called a VOM — Volt-Ohm-Meter) is the single most important diagnostic tool you will use. Master it before touching a printer.

### 2.1 Multimeter Modes

| Mode | Symbol | What It Measures | Typical Use |
|------|--------|-----------------|-------------|
| DC Voltage | V⎓ | Voltage of batteries, power rails | Check 24V PSU output, logic levels |
| AC Voltage | V~ | Mains voltage | Verify wall outlet (dangerous — use caution) |
| DC Current | A⎓ | Current draw | Measure motor or heater current |
| Resistance | Ω | Resistance in ohms | Check thermistor, motor coil, fuse |
| Continuity | )))  | Beeps if circuit is closed | Check wiring, detect shorts and breaks |
| Diode | ▷| | Forward voltage of a diode | Verify polarity, check MOSFETs |

### 2.2 How to Measure DC Voltage (e.g., checking 24V PSU)

1. Set the dial to **DC Voltage (V⎓)**, range 50V or auto-range.
2. Plug the **black probe into COM**, red probe into **VΩmA**.
3. Touch black probe to **GND** (negative terminal), red to **V+** (positive terminal).
4. Read display. A healthy 24V PSU should read **23.8–24.2V**.
5. If reading is 0V: check mains connection and fuse.
6. If reading is significantly below 24V under load: PSU may be failing or overloaded.

### 2.3 Continuity Testing — The Most Important Skill

Continuity testing tells you whether a wire or connection is **complete (closed circuit)** or **broken**.

**Steps:**
1. Power OFF and disconnect the circuit entirely.
2. Set multimeter to **Continuity mode** (beeper symbol `)))`).
3. Touch both probes together — meter should beep. This confirms the meter works.
4. Touch one probe to each end of the wire or connection being tested.
5. **Beep = Good continuity** (wire is intact).
6. **Silence = Open circuit** (wire is broken or connection is faulty).

**TPS Continuity Testing (Thermal Protection Switch):**

The TPS is a resettable thermal fuse on some heated beds and hot ends. If a printer refuses to heat:

1. Power off and disconnect the TPS from the circuit.
2. Test continuity across the TPS terminals.
3. **Beep** = TPS is OK (fault is elsewhere).
4. **Silence** = TPS has tripped. Locate the reset button (small button on the device) and press it. Re-test. If it still doesn't reset, the TPS is failed and must be replaced.

### 2.4 Resistance Measurement (Thermistors and Motor Coils)

**NTC Thermistor (temperature sensor):**
- At room temperature (~25°C), a 100K NTC thermistor reads approximately **100,000 Ω (100 kΩ)**.
- As temperature rises, resistance falls (NTC = Negative Temperature Coefficient).
- If the printer shows `MINTEMP` or `999°C` errors, measure thermistor resistance:
  - Disconnect thermistor connector from the board.
  - Set meter to Ω, 200kΩ range.
  - Probe the thermistor leads.
  - Room temp should read ~100kΩ. If reading is 0Ω (short) or OL (open), the thermistor is failed.

**Stepper Motor Coil Check:**

![NEMA 17 stepper motor — the 1.7-inch (42 mm) face width standard used in all FDM 3D printers for X, Y, Z, and extruder motion](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Stepper_motor.jpg/320px-Stepper_motor.jpg)
*A NEMA 17 stepper motor. The four wires (two coils, A and B) are visible at the back. Measuring coil resistance is the fastest way to diagnose a failed motor. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Stepper_motor.jpg), CC BY 3.0*

- A NEMA 17 (National Electrical Manufacturers Association — 17 refers to 1.7-inch face width) stepper motor has two coils (A and B), typically reading **2–10 Ω** per coil.
- Disconnect the motor connector from the board.
- Set meter to Ω, 200Ω range.
- Probe pins 1+2 (Coil A) → should read 2–10 Ω.
- Probe pins 3+4 (Coil B) → should read 2–10 Ω.
- An open reading (OL) means a broken winding → motor must be replaced.

---

## 3. Soldering

Soldering is the process of permanently joining two metal conductors using a filler metal (solder) melted at low temperature.

### 3.1 Equipment

| Tool | Purpose |
|------|---------|
| Soldering iron (350–400°C) | Heat source |
| Solder (60/40 Sn/Pb or lead-free 63/37) | Filler metal — creates the joint |
| Flux | Cleans oxide layer, helps solder flow |
| Desoldering pump (solder sucker) | Removes old solder |
| Helping hands / vise | Holds components while soldering |
| Brass tip cleaner | Keeps iron tip clean |
| Fume extractor | Removes toxic flux fumes |

> ⚠️ **Safety:** Always use a fume extractor or work in a well-ventilated area. Solder fumes are toxic.

### 3.2 Soldering a Wire to a Terminal (Step-by-Step)

1. **Tin the iron tip** — melt a small amount of solder onto the clean tip until it is shiny.
2. **Strip the wire** — remove 5–8 mm of insulation. Twist the strands tightly.
3. **Tin the wire** — heat the wire end and flow solder into the strands until fully coated.
4. **Tin the pad or terminal** — heat the target and apply a thin layer of solder.
5. **Join the parts** — hold tinned wire against tinned terminal, apply iron briefly (1–2 sec). Remove iron while holding parts still. Let cool for 5 seconds without moving.
6. **Inspect** — a good joint is **shiny and volcano-shaped**. A bad joint (cold joint) looks **dull and grainy** — reheat it.
7. **Tug test** — gently pull the wire. It must not come loose.

### 3.3 Common Soldering Mistakes

| Mistake | Cause | Fix |
|---------|-------|-----|
| Cold joint (dull, grainy) | Moved parts during cooling or insufficient heat | Reheat and let flow properly |
| Solder bridges | Too much solder or shaky hand | Use desoldering wick to remove excess |
| Lifted pad | Iron too hot or held too long | Repair with wire-to-via bridge |
| Burnt insulation | Iron touched wire insulation | Use heat-shrink tubing, avoid contact |

### 3.4 Desoldering

1. Heat the joint with the iron until solder melts.
2. While keeping iron on joint, place the pump nozzle directly over the joint.
3. Press the pump trigger — solder is sucked out.
4. Repeat until the component leg is free.

---

## 4. Connectors in 3D Printers

![JST-XH 2.5mm connectors — the standard low-current signal connector used throughout 3D printers for thermistors, endstops, and fans](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Balancer_Buchse_XH.JPG/400px-Balancer_Buchse_XH.JPG)
*JST-XH 2.5mm connectors (shown with housing). Used throughout 3D printers for low-current signals: thermistors (temperature sensing), endstops (homing), fans, and probe wiring. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Balancer_Buchse_XH.JPG), CC BY 3.0*

Connectors allow wires to be disconnected for maintenance without cutting. Knowing connector types saves hours of troubleshooting.

### 4.1 Connector Reference Table

| Connector | Pitch | Current Rating | Typical Use in Printers |
|-----------|-------|---------------|------------------------|
| **JST-XH** | 2.54 mm | 3A | Thermistors, endstops, fans, probes |
| **JST-PH** | 2.0 mm | 2A | Smaller sensors, LCD cables |
| **Dupont** | 2.54 mm | 1A | Prototype connections, jumpers |
| **Molex Mini-Fit Jr** | 4.2 mm | 13A | Stepper motor wiring |
| **XT30** | — | 30A | Medium power, bed heaters |
| **XT60** | — | 60A | High-current battery/PSU connections |
| **Wire-to-board screw terminal** | 3.5–5.08 mm | 10–25A | PSU input/output |

### 4.2 Crimping a JST-XH Connector

JST-XH connectors are used throughout 3D printers for low-current signals. Correct crimping eliminates intermittent faults.

**Tools needed:** Crimping tool (SN-28B or PA-09), JST-XH terminals, JST-XH housing.

1. Strip wire to **2 mm** of bare conductor (no more — excess conductor causes shorts).
2. Insert wire into the crimp terminal with the insulation wings surrounding the insulation and conductor wings surrounding the bare wire.
3. Squeeze the crimper firmly — both sets of wings should curl inward and grip.
4. Test: gently pull wire — it must not pull out of the crimp.
5. Insert terminal into housing until it clicks. Tug to confirm locking.

> **Common Mistake:** Crimping with strands not fully inserted causes intermittent contact. Always confirm all strands are inside the terminal before crimping.

### 4.3 XT60 / XT30 Connectors (High Current)

XT60 connectors are rated for 60A continuous and are used for PSU output rails and heated bed connections on high-power builds.

1. **Tin both the XT60 cup and the wire** before joining.
2. Use a **high-wattage iron (60–80W)** — XT60 cups are large and dissipate heat quickly.
3. Insert the tinned wire into the cup, apply iron to the cup side until solder flows completely around the wire.
4. **Never heat from the plastic side** — the plastic will melt.

---

## 5. Fracktal Control Boards

![Direct drive extruder and hotend assembly with all components labeled — stepper motor, heat break, heater block, thermistor, part cooling fan](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Extruder_lemio-en.svg/400px-Extruder_lemio-en.svg.png)
*Direct drive extruder and hotend assembly — every component shown (stepper motor, thermistor, heater cartridge, fans) connects to the control board via JST-XH or screw terminal connectors. The Fracktal boards (MKS Eagle V1.0, Manta M8P V2.0) provide connectors for each of these. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Extruder_lemio-en.svg), CC BY-SA 4.0*

Fracktal machines use two different control boards:

- **Snowflake** — **MKS Eagle V1.0** (Marlin firmware, standalone, no Raspberry Pi)
- **Dragon & Twin Dragon** — **BIGTREETECH Manta M8P V2.0** + RP2040 CAN toolboards (Klipper firmware)

### 5.1 Control Board Overview

| Component | Snowflake | Dragon / Twin Dragon |
|-----------|-----------|---------------------|
| **Main Board** | MKS Eagle V1.0 | BIGTREETECH Manta M8P V2.0 |
| **MCU** | STM32F407 | STM32H723 |
| **Firmware** | Marlin | Klipper (via Katapult bootloader) |
| **Stepper Drivers** | TMC2209 (onboard) | TMC5160 (onboard) |
| **Compute Module** | None (standalone) | Raspberry Pi CM4 (on-board slot) |
| **Web Interface** | None (LCD only) | OctoPrint (via RPi CM4) |
| **CAN Toolboard T0** | None | RP2040-based (hotend 0) |
| **CAN Toolboard T1** | None | RP2040-based — Twin Dragon only |

### 5.2 MKS Eagle V1.0 — Snowflake Specs

| Spec | Value |
|------|-------|
| **MCU** | STM32F407 |
| **Stepper Drivers** | 5× onboard TMC2209 |
| **Firmware** | Marlin |
| **Interface** | USB serial (250000 baud) / SD card |
| **Heater outputs** | HE0 (hotend), HB (bed) |
| **Thermistor inputs** | TH0, TB |

### 5.3 Manta M8P V2.0 — Dragon / Twin Dragon Specs

| Spec | Value |
|------|-------|
| **MCU** | STM32H723 |
| **Bootloader** | Katapult (formerly CanBoot) |
| **Stepper Drivers** | 8× onboard TMC5160 |
| **CAN bus** | PD0 (RX), PD1 (TX) at 1000000 baud |
| **Compute Module** | Raspberry Pi CM4 in onboard M.2 socket |
| **Firmware repo** | https://github.com/FracktalWorks/klipper_IDEX |

### 5.4 CAN Bus Architecture (Dragon / Twin Dragon)

```
┌──────────────────────────────────────────────────────────┐
│              Manta M8P V2.0 (Main Board)                 │
│                                                          │
│  CM4 slot  ┌──────────────┐                             │
│  [Pi CM4] ─┤ Klipper Host ├─────────────────────────┐   │
│             └──────────────┘                         │   │
│                                                      │   │
│  STM32H723 MCU ← Katapult bootloader                │   │
│                                                      │   │
│  CAN Bus (PD0/PD1 @ 1Mbit)──────────────────────────┘   │
│       │                                                  │
│  ┌────┴──────────────────────────────────────────┐       │
│  │  CAN Toolboard (T0 — RP2040)                  │       │
│  │  • Hotend heater (HE0)                        │       │
│  │  • Hotend thermistor (TH0)                    │       │
│  │  • Part cooling fan                           │       │
│  │  • Filament runout sensor                     │       │
│  └────────────────────────────────────────────┘         │
│       │ (Twin Dragon only)                               │
│  ┌────┴──────────────────────────────────────────┐       │
│  │  CAN Toolboard (T1 — RP2040)                  │       │
│  │  • Hotend heater (HE1)                        │       │
│  │  • Hotend thermistor (TH1)                    │       │
│  │  • Part cooling fan (T1)                      │       │
│  └────────────────────────────────────────────┘         │
└──────────────────────────────────────────────────────────┘
```

### 5.4 CAN Bus Toolboard Identification (UUID-based)

Each CAN toolboard is identified by a unique UUID. When flashing or configuring Klipper:

```bash
# Scan for CAN devices on the bus:
python3 ~/klippy-env/bin/python ~/klipper/scripts/canbus_query.py can0

# Flash toolboard using UUID:
python3 ~/katapult/scripts/flash_can.py -i can0 -u <toolboard_uuid> -f ~/klipper/out/klipper.bin
```

> 📌 The UUID is printed on a label on the toolboard or can be found in the Klipper `printer.cfg` under `[mcu toolboard_t0]`. Do not swap toolboards between machines without reconfiguring the UUID in `printer.cfg`.

### 5.3 Stepper Driver Installation

Stepper drivers are small plug-in modules that convert step/direction signals from the board into phase currents for the motor.

**Common drivers used in our printers:**

| Driver | Key Feature | Noise Level | Use Case |
|--------|-------------|------------|---------|
| **A4988** | Simple, cheap | Loud | Budget/legacy builds |
| **TMC2208** | Silent, UART config | Very quiet | All machines |
| **TMC2209** | Silent, UART + StallGuard | Very quiet | Sensorless homing |
| **TMC5160** | High current, SPI | Quiet | High-torque applications |

**Installation Steps:**
1. Power board OFF completely.
2. Confirm driver orientation — **EN pin aligns with the EN label on the board** (check datasheet for your specific board).
3. Seat the driver module firmly into the socket.
4. Set Vref (reference voltage) for current limit (A4988 / DRV8825 only — NOT required for TMC2208/2209 in UART mode):
   - **A4988 formula:** `Vref = RMS_Amps × 2.5 × Rsense` (where Rsense = 0.1 Ω on most boards)
   - **DRV8825 formula:** `Vref = RMS_Amps × 2 × Rsense`
   - Example (A4988): Motor rated 0.8A RMS → Vref = 0.8 × 2.5 × 0.1 = **0.20V**
   - Use a small flat-head screwdriver on the potentiometer. Measure Vref between the center of the pot and GND while the board is powered.
5. For TMC2208/2209 in UART mode: no Vref adjustment needed — current is configured in firmware (`run_current` in Klipper).

> ⚠️ **Warning:** Inserting a stepper driver backwards will instantly destroy it and may damage the board. Double-check orientation before powering on.

---

## 6. Circuit Design with Cirkit Designer

**Cirkit Designer** (https://app.cirkitdesigner.com/) is a browser-based circuit design and simulation tool used for schematic capture and wiring diagrams.

### 6.1 Getting Started

1. Open https://app.cirkitdesigner.com/ in a browser.
2. Create a free account.
3. Click **New Project** → select **Schematic**.

### 6.2 Building a Basic Printer Wiring Diagram

**Exercise: Draw the MKS Eagle V1.0 (Snowflake) and Manta M8P V2.0 (Dragon) connection diagrams for one axis each.**

1. Search component library for **STM32** MCU → place on canvas.
2. Place a **NEMA 17 Stepper Motor** component.
3. Place a **Mechanical Endstop** component.
4. Connect stepper motor pins (A1, A2, B1, B2) to the X-motor port on the board.
5. Connect endstop (VCC, GND, SIG) to the X-MIN endstop port.
6. Add a **24V DC Power Supply** component and connect to board power input.
7. Export schematic as PNG or PDF for documentation.

### 6.3 Simulation Features

Cirkit Designer supports basic simulation. For wiring verification:
- Use the **net checker** to confirm all connections are valid.
- Use **voltage probes** to simulate PSU output reaching board.

---

## 7. Wiring Best Practices

| Practice | Why It Matters |
|----------|---------------|
| Use ferrules on stranded wire ends going into screw terminals | Prevents strand fraying and short circuits |
| Route motor wires away from heater wires | Reduces EMI (Electromagnetic Interference) noise on motor signals |
| Use cable ties every 50–100 mm | Prevents vibration from wearing insulation |
| Label every connector with masking tape | Saves hours during troubleshooting |
| Never exceed connector current rating | Overloaded connectors cause fires |
| Use braided sleeving on moving cable chains | Extends wire life in drag chains |
| Crimped connectors, not twisted + taped joins | Twisted joins corrode and fail |

---

## ❌ Common Mistakes

| Mistake | What Happens | Correct Practice |
|---------|-------------|------------------|
| Skipping ESD precaution | Silent board damage — appears fine until first power-on | Always use ESD strap or touch a grounded surface before handling boards |
| Probing inside PSU with mains connected | Electrocution risk | Never probe inside a PSU while mains power is connected |
| Cold solder joint | Intermittent connection → erratic printer behaviour | Heat the pad, not the solder; tin both surfaces before joining |
| Wrong JST polarity | Reversed signal → motor fault or board damage | Verify pin order with multimeter before plugging in |
| Overtightening screw terminals | Cracked housing, stripped threads | Hand-tight then 1/4 turn only on terminal block screws |
| Mixing signal and power grounds | Noise on thermistor → temperature spikes | Route signal GND and power GND separately |
| Not tinning wire ends before ferrule crimp | Ferrule fails, strand fraying | **Never tin stranded wire before inserting into a ferrule** — tinning creates a hard spot that cracks under vibration and is against IEC 60947 standards. Insert bare twisted strands into the ferrule and crimp only. |
| PSU voltage selector wrong (115 vs 230V) | Immediate PSU failure, possible fire | Check voltage selector before connecting mains — every time |
| Stepper driver installed backwards | Driver overheats and burns within seconds | Align thermal pad with the board orientation marker |

---

## 8. Hands-On Exercises

### Exercise 1.1 — Multimeter Mastery
- [ ] Measure the output voltage of a 24V PSU (should read 23.8–24.2V)
- [ ] Perform continuity test on 5 different wires of varying lengths
- [ ] Measure the resistance of a spare thermistor at room temperature
- [ ] Test continuity of a TPS (thermal protection switch) on the bench

### Exercise 1.2 — Connector Crimping
- [ ] Crimp 3× JST-XH 3-pin connectors onto pre-cut wires
- [ ] Assemble one XT60 connector pair (male + female) with proper soldering

### Exercise 1.3 — Soldering
- [ ] Solder a wire to a screw terminal block
- [ ] Solder a bridge wire on a prototype board
- [ ] Desolder a through-hole component without lifting pads

### Exercise 1.4 — Fracktal Board Familiarization
- [ ] Identify all zones on a MKS Eagle V1.0 (Snowflake) and a Manta M8P V2.0 (Dragon) — photograph and label
- [ ] Locate the CAN bus connector (PD0/PD1) and the CM4 slot on the board
- [ ] Run `canbus_query.py` on a live Dragon or Twin Dragon and record the toolboard UUID

### Exercise 1.5 — Cirkit Designer
- [ ] Create a schematic of the endstop wiring for all 3 axes
- [ ] Export and share the schematic as PDF

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [How to Use a Multimeter](https://www.youtube.com/watch?v=rPGoMbVSUu8) | EEVblog | Best multimeter beginner tutorial — covers all modes |
| [Soldering is Easy](https://www.youtube.com/watch?v=Qps9woUGkvI) | Mitch Altman | Comic-book style guide — perfect for absolute beginners |
| [JST Connector Crimping Tutorial](https://www.youtube.com/watch?v=jt4KNZ9OGo0) | Clough42 | Detailed crimping walkthrough with close-up camera work |
| [BIGTREETECH Manta M8P V2.0 Overview](https://www.youtube.com/watch?v=example) | Teaching Tech | Overview of the Manta M8P board used in Dragon and Twin Dragon |
| [Klipper CAN Bus Toolboards Explained](https://www.youtube.com/watch?v=VFYFV_TatpE) | Teaching Tech | Explains CAN bus toolboard wiring and UUID-based config |

---

## 📚 Further Reading

- [Marlin Firmware — Pin Configuration](https://marlinfw.org/docs/configuration/pins.html) — Official pin definitions for supported boards
- [BIGTREETECH Manta M8P V2.0 GitHub](https://github.com/bigtreetech/Manta-M8P) — Schematics, pinout, and documentation for Dragon and Twin Dragon
- [MKS Eagle V1.0 GitHub](https://github.com/makerbase-mks/MKS-Eagle) — Schematics and pinout for Snowflake
- [FracktalWorks Klipper IDEX Firmware](https://github.com/FracktalWorks/klipper_IDEX) — Official Klipper fork for Fracktal IDEX machines

---

## ✅ Knowledge Check

1. What does a beep during a continuity test indicate?
2. A thermistor at room temperature measures 1.2 kΩ — is this normal for a 100K NTC thermistor? What does this reading suggest?
3. You need to crimp a JST-XH connector. What is the correct strip length for the wire?
4. A TMC2208 stepper driver is installed in UART mode. Do you need to adjust the Vref potentiometer? Why or why not?
5. List three wiring best practices and explain why each matters.
6. What control board does Snowflake use, and what control board do Dragon and Twin Dragon use? What firmware runs on each?
7. What is the difference between an XT30 and XT60 connector?

---

*[← Section Index](./README.md) | [🏠 Curriculum Index](../README.md) | [Next: Mechanical Basics →](../02-mechanical-basics/README.md)*
