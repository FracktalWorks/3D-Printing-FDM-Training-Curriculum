# Machine Quick-Reference Cards

> One-page operational cheat sheets for each printer in the fleet.
> Use these during maintenance, first prints, and troubleshooting sessions.

---

## Fleet Overview

| Machine | Type | Volume | Max Temp | Firmware | Board | Quick Ref |
|---------|------|--------|---------|---------|-------|----------|
| **Snowflake** | CoreXY, Dual-Gear Drive | 200×200×200 mm | 265°C | Marlin | MKS Eagle V1.0 | [SNOWFLAKE-QUICK-REF.md](SNOWFLAKE-QUICK-REF.md) |
| **Julia** | CoreXY, Direct Drive | 250×250×250 mm | 280°C | MKS Robin Nano V3 | [JULIA-QUICK-REF.md](JULIA-QUICK-REF.md) |
| **Dragon** | CoreXY, Direct Drive | 400×300×400 mm | 300°C | Klipper | Manta M8P V2.0 | [DRAGON-QUICK-REF.md](DRAGON-QUICK-REF.md) |
| **Twin Dragon** | CoreXY + IDEX (dual head) | 300×300×400 mm | 300°C | Klipper | Manta M8P V2.0 | [TWIN-DRAGON-QUICK-REF.md](TWIN-DRAGON-QUICK-REF.md) |

---

## Machine Selection Guide

| Use Case | Recommended Machine |
|---------|-------------------|
| First print / training runs | **Julia** (forgiving, compact, direct drive) |
| Standard PLA / PETG production | **Snowflake** (reliable, well-tuned) |
| High-temp materials (ABS, ASA, PC, Nylon) | **Dragon** (enclosure + 320°C) |
| Multi-material or dual-material objects | **Twin Dragon** (IDEX) |
| Large parts | **Dragon** (largest volume in fleet: 350×350×400) |
| Same part × 2 in one run | **Twin Dragon** (Duplication Mode) |

---

## Network Access

| Machine | IP Address | Web UI | SSH Alias |
|---------|-----------|--------|----------|
| Snowflake | `192.168.1.101` | `http://snowflake` | `ssh snowflake` |
| Julia | `192.168.1.102` | `http://julia` | `ssh julia` |
| Dragon | `192.168.1.103` | `http://dragon` | `ssh dragon` |
| Twin Dragon | `192.168.1.104` | `http://twin-dragon` | `ssh twin-dragon` |

---

*[Back to Curriculum Index](../README.md)*
