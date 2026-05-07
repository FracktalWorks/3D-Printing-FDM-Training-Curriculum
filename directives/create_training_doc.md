# Create Training Doc — Directive

## Goal
Create a brand-new training Markdown document for a topic not yet covered in the curriculum.
The doc will be placed in `curriculum/` under a new numbered folder and indexed in `curriculum/README.md`.

## When to Use
- User asks to "create a training doc on [topic]"
- User wants to add a new module beyond the base 8
- A subtopic needs its own dedicated doc (e.g., a deep-dive on Klipper)

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Topic | Yes | What the doc is about (e.g. "dual extrusion", "Klipper input shaping") |
| Skill Level | No | `beginner`, `intermediate`, `advanced`. Default: `beginner` |
| Pillar | No | `electronics`, `mechanical`, `software`, `operations`. Determines placement |
| Module Number | No | If not provided, append as next available number |

## Execution

### Step 1: Plan the document structure

Before writing, outline:
1. What are the 3-5 learning objectives for a fresher reading this doc?
2. What prerequisite knowledge is required?
3. What are the 4-6 main sections (H2 headings)?
4. What specs or data need to be sourced?

### Step 2: Search for videos

```bash
python execution/fetch_youtube_videos.py --topic "<topic>" --max 10 --output .tmp/videos_new_doc.json
```

Select ≥3 videos before writing the doc.

### Step 3: Search for references

```bash
python execution/search_web_resources.py --query "<topic> 3D printing guide" --max 5
```

### Step 4: Write the document

Use the standard template from `generate_curriculum.md`:

```markdown
# Module N: Title

> One-line description.

## 🎯 Learning Objectives
## Prerequisites
## 1. ...
## 2. ...
## 🎥 Recommended Videos
## 📚 Further Reading
## ✅ Knowledge Check
```

### Step 5: Update the curriculum index

Add the new module to `curriculum/README.md` in the table of contents.

### Step 6: Update `generate_curriculum.md`

Add the new module to the curriculum map table in `directives/generate_curriculum.md` so future regenerations include it.

## Writing Quality Standards

1. **Zero-knowledge baseline**: Write as if the reader has never heard of the topic
2. **Define every acronym on first use**: e.g., "FDM (Fused Deposition Modeling)"
3. **Use numbered steps for procedures**: never prose-only for how-to content
4. **Include a diagram description** (use ASCII art or describe a figure) for complex concepts
5. **Cite every spec**: "NEMA 17 motors typically use 1.8° step angle ([RepRap Wiki](https://reprap.org/wiki/NEMA_17_Stepper_motor))"
6. **End with a knowledge check**: 3-5 questions a trainer could quiz on

## Document Length Guidelines

| Skill Level | Target Length |
|-------------|--------------|
| Beginner | 600-1200 words |
| Intermediate | 1000-2000 words |
| Advanced | 1500-3000 words |

Do not pad. Write exactly as much as the topic needs.
