# Module 00: Introduction to 3D Printing

> What is 3D printing, the major technologies, industry applications, and how this curriculum is structured.

![An FDM 3D printer showing the complete assembly — frame, gantry, hotend, and heated build plate](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/3D_printer2.jpg/400px-3D_printer2.jpg)
*An FDM desktop 3D printer showing the frame, gantry, control board, and build plate — the same core architecture as all Fracktal machines. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:3D_printer2.jpg), CC BY-SA 3.0*

## 🎯 Learning Objectives

After completing this module, you will be able to:
- Define 3D printing and explain how it differs from traditional manufacturing
- Name and describe at least 4 types of 3D printing technology
- Identify the key industries where 3D printing is used
- Understand the learning path ahead and what each module covers

## Prerequisites

None. This is the starting point.

---

## 1. What Is 3D Printing?

**3D printing**, also called **additive manufacturing (AM)**, is the process of creating a physical object by depositing or curing material layer by layer based on a digital 3D model.

Unlike **subtractive manufacturing** (CNC machining, which cuts away material) or **formative manufacturing** (injection molding, which shapes material in a mold), 3D printing builds objects by *adding* material only where it is needed.

### The Basic Workflow

![FDM printer actively building a white plastic model layer by layer on the print bed](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/3D_printer2.jpg/400px-3D_printer2.jpg)
*An FDM printer building a model layer by layer — each layer fuses to the previous one as it cools. Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:3D_printer2.jpg), CC BY-SA 3.0*

```
3D Model (CAD)  →  Slicer Software  →  G-code  →  Printer  →  Physical Part
```

1. **Design**: Create or download a 3D model (`.stl`, `.3mf`, `.obj` file)
2. **Slice**: Convert the model to printer instructions (G-code) using slicer software
3. **Print**: The printer reads the G-code and builds the object layer by layer
4. **Post-process**: Remove supports, clean, and finish the part

---

## 2. Types of 3D Printing Technology

### 2.1 FDM — Fused Deposition Modeling

![FDM process diagram: 1 – Extruder/nozzle, 2 – Deposited material layers forming the part, 3 – Controlled movable build platform](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/FDM_printing_diagram.svg/500px-FDM_printing_diagram.svg.png)
*FDM process: heated filament is extruded through a nozzle (1) and deposited layer by layer to form the part (2) on a movable platform (3). Source: [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:FDM_printing_diagram.svg), CC BY-SA 4.0*

**How it works**: A plastic filament is melted through a heated nozzle and deposited onto a build plate. Each layer fuses to the previous one as it cools.

- **Common materials**: PLA, PETG, ABS, TPU, Nylon
- **Resolution**: 0.1–0.3 mm layer height typical
- **Cost**: Low (printer $200–$2000, filament $20–$50/kg)
- **Best for**: Functional prototypes, enclosures, mechanical parts
- **Examples of printers**: Fracktal Snowflake, Dragon 400, Twin Dragon 300

> ✅ **FDM is the primary focus of this curriculum.** It is the most common technology in workshops, makerspaces, and entry-level manufacturing.

### 2.2 SLA — Stereolithography

**How it works**: A UV laser cures liquid photopolymer resin layer by layer. The build plate lifts out of the resin tank as each layer cures.

- **Materials**: Photopolymer resins (standard, ABS-like, flexible, castable)
- **Resolution**: 25–100 µm — much finer detail than FDM
- **Cost**: Medium (printer $300–$3000, resin $30–$150/L)
- **Best for**: Jewellery, dental, miniatures, high-detail parts
- **Examples**: Formlabs Form 3, Elegoo Mars

### 2.3 SLS — Selective Laser Sintering

**How it works**: A high-power laser sinters (fuses) powdered material (usually nylon) layer by layer. No support structures needed — unfused powder supports the part.

- **Materials**: Nylon PA12, PA11, TPU powder, metal powders
- **Resolution**: 80–150 µm
- **Cost**: High (printer $10,000–$500,000)
- **Best for**: End-use parts, complex geometries, production runs
- **Examples**: EOS P3, Formlabs Fuse 1

### 2.4 DLP — Digital Light Processing

**How it works**: Similar to SLA but uses a digital projector to cure an entire resin layer at once instead of tracing with a laser. Generally faster than SLA for small builds.

- **Examples**: Anycubic Photon Mono X, Elegoo Saturn

### 2.5 MJF — Multi Jet Fusion (HP)

**How it works**: An inkjet array deposits fusing and detailing agents onto a powder bed, then a heating element fuses the layer. Parts are isotropic (equal strength in all directions).

- **Examples**: HP Jet Fusion 5200

### 2.6 DMLS / SLM — Direct Metal Laser Sintering / Selective Laser Melting

**How it works**: Laser melts metal powder (stainless steel, titanium, aluminium, Inconel) layer by layer. Produces dense, functional metal parts.

- **Best for**: Aerospace, medical implants, tooling

---

## 3. Industry Applications

| Industry | Application | Technology |
|----------|------------|-----------|
| Automotive | Prototyping, jigs, end-use brackets | FDM, SLS |
| Aerospace | Lightweight structural parts, turbine components | DMLS, SLS |
| Medical | Surgical guides, implants, prosthetics | SLA, SLS, DMLS |
| Consumer Goods | Custom products, product development | FDM, SLA |
| Jewellery | Lost-wax casting masters | SLA, DLP |
| Education | Teaching models, STEM projects | FDM |
| Architecture | Scale models | FDM, SLA |
| Electronics | Enclosures, jigs, fixtures | FDM |

---

## 4. Key Terms Glossary

| Term | Definition |
|------|-----------|
| **FDM** | Fused Deposition Modeling — filament-based printing |
| **G-code** | Machine instructions that tell the printer where to move and what to do |
| **Slicer** | Software that converts a 3D model into G-code |
| **Layer height** | Thickness of each printed layer (e.g. 0.2 mm) |
| **Infill** | The internal structure of a print (e.g. 15% gyroid) |
| **Support** | Temporary material printed to hold overhanging parts |
| **Bed** | The flat surface the printer prints on |
| **Hot end** | The heated assembly that melts and extrudes filament |
| **Extruder** | The mechanism that feeds filament into the hot end |
| **Retraction** | Pulling filament back to reduce oozing during travel moves |

---

## 5. Your Learning Path

This curriculum covers 3D printing from four pillars:

| Pillar | What You'll Learn | Module |
|--------|------------------|--------|
| Electronics | How the printer's electronics work | Module 01 |
| Mechanical | How the printer moves and deposits material | Module 02 |
| Software | How to prepare files and configure firmware | Module 03 |
| Operations | How to run, calibrate, and troubleshoot | Modules 04–06 |
| Advanced | Klipper, multi-material, post-processing | Module 07 |

---

## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Updated Beginners Guide To 3D Printers In 2024!](https://www.youtube.com/watch?v=40rIIjCGIU0) | YouTube | Complete 2024 beginner overview — technologies, workflow, first printer advice |
| [3D Printing Made Easy - Complete Guide 2023](https://www.youtube.com/watch?v=G2OzH27i_8U) | YouTube | Step-by-step walkthrough from digital model to finished print |
| [Best 3D Printers of 2024! For Beginners and Pros!](https://www.youtube.com/watch?v=xYo_FnFak9I) | YouTube | Covers printer categories and how to choose the right one for your level |
| [How to Use Ultimaker Cura 5: A Beginner's Guide 2024](https://www.youtube.com/watch?v=i1ZjXsKoKPQ) | YouTube | End-to-end slicer tutorial — the final step before printing |
| [3D Printer Academy Tutorials (Playlist)](https://www.youtube.com/@3DPrinterAcademyTutorials/videos) | 3D Printer Academy | Structured video series ideal for structured self-study |

---

## 📚 Further Reading & Forums

- [The Free Beginner's Guide — 3D Printing Industry](https://3dprintingindustry.com/3d-printing-basics-free-beginners-guide/) — Comprehensive industry-produced beginner guide covering all technologies
- [All3DP — 3D Printing for Beginners: How to Get Started with FDM](https://all3dp.com/2/3d-printing-for-beginners-all-you-need-to-know-to-get-started/) — Practical FDM-focused beginner guide
- [r/3Dprinting Wiki: Getting Started](https://www.reddit.com/r/3Dprinting/wiki/gettingstarted/) — Community-maintained getting-started guide with printer recommendations
- [r/3Dprinting — Where should I start? (Forum thread)](https://www.reddit.com/r/3Dprinting/comments/q7qs1l/where_should_i_start_learning_about_3d_printing/) — Real community advice on learning path for newcomers
- [EufyMake — 3D Printing for Beginners: Basics, Tips & Budget Guide](https://www.eufymake.com/blogs/printing-guides/beginners-guide-to-3d-printing) — Budget-focused guide covering hardware basics

---

## ✅ Knowledge Check

1. What does "additive manufacturing" mean and how does it differ from CNC machining?
2. Name three types of 3D printing technology and give one use case for each.
3. What is the role of slicer software in the 3D printing workflow?
4. Which 3D printing technology is primarily covered in this curriculum, and why?
5. What industry would use DMLS (Direct Metal Laser Sintering), and why?

---

*[🏠 Curriculum Index](../README.md) | [Next: Electronics Basics →](../01-electronics-basics/README.md)*
