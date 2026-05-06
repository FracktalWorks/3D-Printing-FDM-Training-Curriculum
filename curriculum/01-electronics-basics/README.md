# Module 01: Electronics Basics for 3D Printing

> Understanding the electronic components that make a 3D printer work — control boards, stepper motors, drivers, power supplies, sensors, and wiring.

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Identify the key electronic components on a 3D printer
- Explain what a control board does and name common examples
- Describe how stepper motors and stepper drivers work together
- Understand how a thermistor measures temperature
- Identify safe wiring practices and spot common wiring mistakes

## Prerequisites

- Module 00: Introduction to 3D Printing

---

## 1. The Electronics Overview

A 3D printer is essentially a **computer-controlled motion system with a heater**. The electronics orchestrate all of it:

```
Power Supply → Control Board → Stepper Drivers → Stepper Motors (motion)
                            ↘ Heater Cartridge → Hot End (melts filament)
                            ↘ Heated Bed       → Build Plate (adhesion)
                            ↘ Thermistors      → Temperature sensing
                            ↘ End Stops        → Position reference
                            ↘ Fans             → Part & hot end cooling
```

---

## 2. Power Supply Unit (PSU)

The **PSU (Power Supply Unit)** converts mains AC voltage (110V or 230V) to DC voltage the printer uses.

### Common Voltages

| Voltage | Used For |
|---------|---------|
| **24V** | Modern standard — most printers (Fracktal Dragon, Twin Dragon, Snowflake) |
| **12V** | Older designs (original Ender 3, RAMPS-based printers) |
| **48V** | High-performance printers (high-speed industrial builds) |

### Key Specs

- **Wattage**: Total power available. A heated bed alone can draw 100–200W. Most printers use 200–500W PSUs.
- **Amperage**: Watts ÷ Voltage = Amps. A 360W/24V PSU = 15A.
- **Safety**: PSUs carry mains voltage on the input side. **Never open a PSU or work near it while plugged in.** Use a PSU rated for your local voltage (110V or 230V).

### Meanwell Brand

**Meanwell** PSUs (e.g., LRS-350-24) are the gold standard for 3D printers due to their reliability, safety certifications (UL, CE), and efficiency. Generic PSUs from unknown brands are a common cause of fires.

---

## 3. Control Board (Mainboard)

The **control board** is the brain of the printer. It:
- Runs the printer firmware (Marlin, Klipper, etc.)
- Controls stepper motor timing and direction
- Reads sensor data (temperature, end stops)
- Manages heaters and fans via MOSFETs

### Common Control Boards

| Board | Voltage | MCU | Stepper Drivers | Best For |
|-------|---------|-----|----------------|---------|
| **RAMPS 1.4** | 12V | Arduino Mega 2560 | Plug-in (A4988, DRV8825) | Learning, DIY, legacy |
| **BTT SKR Mini E3 V3** | 24V | STM32 | TMC2209 (integrated) | Ender 3 upgrades |
| **BTT Octopus** | 24V | STM32 | 8 drivers (plug-in) | Large multi-axis builds |
| **Duet 3 Mini 5+** | 24V | SAME54 | TMC2240 | Professional, RepRapFirmware |
| **Manta M8P V2.0** | 24V | STM32H723 | TMC5160 onboard | Fracktal Dragon, Twin Dragon (Klipper); Snowflake (Marlin) |

### Board Anatomy

```
[USB/UART port]  — for flashing firmware and serial communication
[MCU chip]       — the processor running the firmware
[Stepper sockets]— X, Y, Z, E0, E1 ... (one per axis)
[Thermistor inputs] — TH0 (hot end), TH1 (bed)
[Heater outputs] — HE0 (hot end), HE1 (bed)
[Fan outputs]    — FAN0 (part cooling), FAN1 (hot end)
[End stop inputs]— X_MIN, Y_MIN, Z_MIN
[SD card slot]   — for printing G-code files
```

---

## 4. Stepper Motors

**Stepper motors** are the actuators that move the printer's axes (X, Y, Z) and push filament (extruder). Unlike regular DC motors, steppers move in discrete angular steps, allowing precise position control without encoders.

### NEMA 17 — The Standard

Most FDM printers use **NEMA 17** (42mm × 42mm flange) motors with:
- **Step angle**: 1.8° per step → 200 steps/revolution ([RepRap Wiki](https://reprap.org/wiki/NEMA_17_Stepper_motor))
- **Microstepping**: Drivers subdivide steps (e.g., 1/16, 1/32) for smoother motion
- **Typical specs**: 40 N·cm holding torque, 1.5–2A rated current, 2-phase bipolar

### NEMA 23

Larger (57mm × 57mm) motors used in heavy-duty printers (large-format, direct-drive Z-axis with heavy beds).

### How Stepper Motors Work

A stepper motor has four coils (two phases). By energizing them in sequence, the rotor is pulled to each position. The driver generates this sequence:

```
Step 1: Phase A+    Step 2: Phase B+
Step 3: Phase A-    Step 4: Phase B-
```

This gives 200 full steps per revolution. With 16× microstepping: 3200 microsteps/revolution.

---

## 5. Stepper Drivers

**Stepper drivers** sit between the control board and the stepper motors. They:
- Convert step/direction signals from the MCU into motor coil currents
- Allow microstepping (smoother motion)
- Protect the motor from overcurrent

### Common Drivers

| Driver | Microstepping | Max Current | Noise | Best For |
|--------|-------------|------------|-------|---------|
| **A4988** | 1/16 | 2A | Loud (chopper noise) | Entry-level, budget |
| **DRV8825** | 1/32 | 2.5A | Moderate | Older printers |
| **TMC2208** | 1/256 | 1.2A RMS | Very quiet | Quiet operation |
| **TMC2209** | 1/256 | 2A RMS | Very quiet | Current standard — sensorless homing |
| **TMC2240** | 1/256 | 3A RMS | Near-silent | High-performance, high-torque |

> **TMC2209** is the current industry favourite: quiet, supports **sensorless homing** (no physical end stops needed for X/Y), and can communicate with the MCU via UART for real-time configuration.

### Setting Motor Current (Vref)

For A4988/DRV8825, motor current is set by a small potentiometer using a formula:

```
Vref = (Motor rated current × 8 × Rsense)
```

For TMC drivers, current is set in firmware (much safer, no potentiometer).

---

## 6. Heater Cartridge & Thermistor

### Heater Cartridge

The **heater cartridge** is a resistive element inserted into the heater block. When current flows through it, it heats up.

- **Typical power**: 30–60W
- **Voltage**: Must match PSU (24V or 12V)
- **Connection**: Two bare wires; polarity does not matter

### Thermistor

A **thermistor** is a temperature-sensitive resistor. The printer reads its resistance to calculate temperature.

- **NTC (Negative Temperature Coefficient)**: Resistance decreases as temperature rises
- **Common types**: NTC 100K (B3950 or EPCOS 100K) — exact type must match firmware config
- **Connection**: Two wires; polarity does not matter

> ⚠️ **Wrong thermistor type in firmware = inaccurate temperatures.** If your thermistor type is wrong, the printer may overheat or trigger false thermal runaway.

---

## 7. Heated Bed & MOSFET

The **heated bed** keeps the bottom of the print warm, preventing warping.

- **Typical power**: 150–300W (the biggest power draw on the printer)
- **Voltage**: 24V or 12V; some use 48V for faster heating
- **Construction**: Resistive traces printed on PCB or silicone mat

The heated bed is controlled via a **MOSFET (Metal-Oxide-Semiconductor Field-Effect Transistor)**. The control board's output is only a signal; the MOSFET is the switch that handles the high current.

> ⚠️ On cheap boards, the on-board MOSFET for the bed can fail (sometimes with sparks). An **external MOSFET module** is a recommended safety upgrade for printers with high-wattage beds.

---

## 8. End Stops & Probes

### End Stops (Limit Switches)

**End stops** tell the printer when an axis has reached its physical limit (home position). During homing, the printer moves the axis until it triggers the end stop.

- **Mechanical end stop**: A physical microswitch. Simple and reliable.
- **Optical end stop**: Uses an IR LED and photodiode — triggered when a flag blocks the beam. More precise.
- **Hall effect sensor**: Triggered by a magnet on the moving part. Contactless.

### Bed Probes (Auto Bed Leveling)

Instead of (or in addition to) a Z end stop, probes measure the bed surface and build a mesh that the firmware uses to compensate for any unevenness.

| Probe | Type | Repeatability | Notes |
|-------|------|--------------|-------|
| **BLTouch** | Servo + Hall effect | ~0.005 mm | Most popular, works on all bed surfaces |
| **CR Touch** | Servo + optical | ~0.005 mm | Creality's BLTouch clone |
| **Klicky** | Magnetic contact | ~0.002 mm | Open-source, no servo, very reliable |
| **Eddy Current (BTT Eddy)** | Electromagnetic | ~0.001 mm | Senses metal beds; ultra-precise |

---

## 9. Fans

| Fan Type | Location | Purpose |
|----------|----------|---------|
| **Hot end fan** | Heat sink | Keeps the cold zone cold — prevents heat creep |
| **Part cooling fan** | Print head | Blows air on the freshly deposited layer to solidify it |
| **Electronics fan** | Case/board | Keeps control board and drivers cool |

> ⚠️ **The hot end fan must run whenever the hot end is above ~40°C.** If it stops, filament softens in the cold zone (heat creep) and causes a clog.

---

## 10. Wiring Best Practices

1. **Cable management**: Use cable chains or drag chains to prevent wire fatigue from repeated motion
2. **Ferrules**: Terminate stranded wire with ferrule crimp connectors before inserting into terminal blocks — prevents loose strands causing shorts
3. **Correct wire gauge**: Bed heater wires should be ≥18 AWG; signal wires can be 24 AWG
4. **No bare copper**: Heater and bed wires exposed to air can oxidize; use proper connectors
5. **Polarity on DC lines**: Red = positive (+), Black = negative (−) — always double-check before powering on
6. **Earth/ground**: The printer frame should be grounded through the PSU ground wire

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Diving into DIY Motion Control; Explaining Stepper Motors](https://www.youtube.com/watch?v=Z_6wpdbHNtY) | YouTube | Deep technical explainer of how stepper motors work with animations |
| [Control a NEMA 17 Stepper Motor with A4988 Driver](https://www.youtube.com/watch?v=wcLeXXATCR4) | YouTube | Hands-on wiring and control tutorial with real hardware |
| [Stepper Motors and Arduino — The Ultimate Guide](https://www.youtube.com/watch?v=7spK_BkMJys) | YouTube | Comprehensive practical guide to stepper motor control |
| [STEPPER MOTORS EXPLAINED: how to control them](https://www.youtube.com/watch?v=PWGR52zSmyk) | YouTube | Covers full-step, half-step, and microstepping clearly |
| [The Anatomy of a 3D Printer // Stepper Drivers](https://www.youtube.com/watch?v=R2-uOKo1yj4) | YouTube | 3D-printer-specific breakdown of stepper driver chips and their role |

---

## 📚 Further Reading & Forums

- [HowToMechatronics — Stepper Motors and Arduino: The Ultimate Guide](https://howtomechatronics.com/tutorials/arduino/stepper-motors-and-arduino-the-ultimate-guide/) — Authoritative written guide with schematics and code examples
- [Instructables — How to Set Up a Stepper Motor in Under 10 Minutes](https://www.instructables.com/How-to-set-up-a-stepper-motor-in-under-10-minutes/) — Step-by-step practical setup guide
- [RepRap Wiki — RAMPS 1.4](https://reprap.org/wiki/RAMPS_1.4) — Detailed documentation on the classic RAMPS control board
- [Trinamic TMC2209 Datasheet](https://www.trinamic.com/fileadmin/assets/Products/ICs_Documents/TMC2209_Datasheet_V103.pdf) — Official driver IC datasheet with electrical specs
- [3D Printing Stack Exchange — Electronics Q&A](https://3dprinting.stackexchange.com/questions/tagged/electronics) — Community Q&A on electronics issues

---

## ✅ Knowledge Check

1. What voltage do most modern 3D printers use, and why is using a Meanwell PSU recommended?
2. What is the function of a stepper driver, and why is the TMC2209 preferred over the A4988 today?
3. A NEMA 17 stepper motor has a 1.8° step angle. How many full steps does it take to complete one revolution?
4. What is the difference between a thermistor and a heater cartridge — what does each do?
5. Why must the hot end fan run whenever the hot end is above 40°C?
6. What is sensorless homing and which driver enables it?

---

*Module 01 of 8 — [← Introduction](../00-introduction/README.md) | [Next: Mechanical Basics →](../02-mechanical-basics/README.md) | [Back to Index](../README.md)*
