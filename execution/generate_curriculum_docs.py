"""
generate_curriculum_docs.py
---------------------------
Scaffolds the 3D printing training curriculum directory structure.
Creates module folders and README stubs if they don't already exist.
Does NOT overwrite existing content.

Usage:
    python execution/generate_curriculum_docs.py --all
    python execution/generate_curriculum_docs.py --module 01-electronics-basics
    python execution/generate_curriculum_docs.py --list

The agent (Copilot) writes the actual content after this script creates the structure.
"""

import argparse
import sys
from pathlib import Path

BASE = Path(__file__).parent.parent  # repo root
CURRICULUM = BASE / "curriculum"

# Module definitions: folder name, display title, subtitle
MODULES = [
    (
        "00-introduction",
        "Introduction to 3D Printing",
        "What is 3D printing, types of technology, industry applications, and your learning path.",
    ),
    (
        "01-electronics-basics",
        "Electronics Basics for 3D Printing",
        "Control boards, stepper motors, drivers, power supplies, thermistors, and wiring.",
    ),
    (
        "02-mechanical-basics",
        "Mechanical Basics for 3D Printing",
        "Frames, motion systems, hot ends, extruders, print beds, and cooling.",
    ),
    (
        "03-software-and-slicing",
        "Software & Slicing",
        "Slicer software, firmware, G-code basics, and 3D modeling tools.",
    ),
    (
        "04-filaments-and-materials",
        "Filaments & Materials",
        "PLA, PETG, ABS, TPU, Nylon, composite filaments, and storage best practices.",
    ),
    (
        "05-printer-operations",
        "Printer Operations & Calibration",
        "Assembly, bed leveling, E-steps, flow rate, PID tuning, and first-layer settings.",
    ),
    (
        "06-troubleshooting",
        "Troubleshooting Common Issues",
        "Systematic debugging for stringing, warping, layer shifts, clogs, and adhesion problems.",
    ),
    (
        "07-advanced-topics",
        "Advanced Topics",
        "Klipper deep dive, multi-material printing, post-processing, and Design for Additive Manufacturing.",
    ),
]

STUB_TEMPLATE = """\
# Module {num}: {title}

> {subtitle}

## 🎯 Learning Objectives

- [ ] *To be filled in by the agent*

## Prerequisites

- *None* (this is the first module) — or list what you need to know

---

## 1. Introduction

*Content coming soon — ask the agent to generate this module.*

## 🎥 Recommended Videos

*Run `python execution/fetch_youtube_videos.py --topic "{title}" --markdown` to populate this section.*

## 📚 Further Reading

*Run `python execution/search_web_resources.py --query "{title} 3D printing" --markdown` to populate this section.*

## ✅ Knowledge Check

1. *Question 1?*
2. *Question 2?*
3. *Question 3?*

---
*Module {num} of 8 — [Back to Index](../README.md)*
"""

INDEX_TEMPLATE = """\
# 3D Printing Fresher Training Curriculum

> A structured, open-source training curriculum for freshers learning 3D printing.
> Covers electronics, mechanical, software, and printer operations.

## How to Use

1. Start at **Module 00** — no prior knowledge required
2. Complete each module in order before moving to the next
3. Watch the recommended videos in each module
4. Test yourself with the knowledge check at the end of each module

---

## Curriculum Map

| Module | Topic | Pillar | Est. Time |
|--------|-------|--------|-----------|
| [00 — Introduction](00-introduction/README.md) | What is 3D Printing | All | 2h |
| [01 — Electronics Basics](01-electronics-basics/README.md) | Boards, motors, drivers, wiring | Electronics | 4h |
| [02 — Mechanical Basics](02-mechanical-basics/README.md) | Frames, motion, hot ends | Mechanical | 4h |
| [03 — Software & Slicing](03-software-and-slicing/README.md) | Slicers, firmware, G-code | Software | 5h |
| [04 — Filaments & Materials](04-filaments-and-materials/README.md) | PLA, PETG, ABS, TPU | Operations | 3h |
| [05 — Printer Operations](05-printer-operations/README.md) | Calibration, bed leveling | Operations | 4h |
| [06 — Troubleshooting](06-troubleshooting/README.md) | Debugging common issues | All | 3h |
| [07 — Advanced Topics](07-advanced-topics/README.md) | Klipper, multi-material, DfAM | All | 6h |

**Total estimated time: ~31 hours of self-study**

---

## Skill Pillars

```
Electronics    → Module 01
Mechanical     → Module 02
Software       → Module 03
Operations     → Modules 04, 05, 06
Advanced       → Module 07
```

---

## Contributing

Found an error or want to add content? Open an issue or PR.
This curriculum is maintained by the 3D Printing Training Agent.
"""


def create_module(folder_name: str, title: str, subtitle: str, num: str) -> bool:
    """Create a module folder and stub README. Returns True if created, False if already exists."""
    module_dir = CURRICULUM / folder_name
    readme = module_dir / "README.md"

    if readme.exists():
        print(f"  [SKIP] {folder_name}/README.md already exists")
        return False

    module_dir.mkdir(parents=True, exist_ok=True)
    content = STUB_TEMPLATE.format(num=num, title=title, subtitle=subtitle)
    readme.write_text(content, encoding="utf-8")
    print(f"  [CREATE] {folder_name}/README.md")
    return True


def create_index() -> bool:
    index = CURRICULUM / "README.md"
    if index.exists():
        print("  [SKIP] curriculum/README.md already exists")
        return False
    CURRICULUM.mkdir(parents=True, exist_ok=True)
    index.write_text(INDEX_TEMPLATE, encoding="utf-8")
    print("  [CREATE] curriculum/README.md")
    return True


def main():
    parser = argparse.ArgumentParser(description="Scaffold the 3D printing training curriculum")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Create all modules")
    group.add_argument("--module", help="Create a single module by folder name (e.g. 01-electronics-basics)")
    group.add_argument("--list", action="store_true", help="List all available modules")
    args = parser.parse_args()

    if args.list:
        print("Available modules:")
        for folder, title, subtitle in MODULES:
            exists = (CURRICULUM / folder / "README.md").exists()
            status = "✓" if exists else "○"
            print(f"  {status} {folder} — {title}")
        return

    if args.all:
        print(f"Scaffolding curriculum at: {CURRICULUM}")
        created = 0
        create_index()
        for folder, title, subtitle in MODULES:
            num = folder.split("-")[0]
            if create_module(folder, title, subtitle, num):
                created += 1
        print(f"\nDone. Created {created} new module(s). Skipped existing files.")
        if created > 0:
            print("\nNext step: Ask the agent to generate content for each module.")
            print("Example: 'Generate the electronics basics module'")

    elif args.module:
        match = next((m for m in MODULES if m[0] == args.module), None)
        if not match:
            print(f"ERROR: Unknown module '{args.module}'")
            print("Use --list to see available modules.")
            sys.exit(1)
        folder, title, subtitle = match
        num = folder.split("-")[0]
        create_index()
        created = create_module(folder, title, subtitle, num)
        if not created:
            print("Module already exists. Use the agent to update it.")


if __name__ == "__main__":
    main()
