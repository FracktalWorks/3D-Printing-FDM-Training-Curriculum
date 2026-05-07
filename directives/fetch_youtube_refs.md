# Fetch YouTube References — Directive

## Goal
Search YouTube for high-quality tutorial videos on a given 3D printing topic and embed them
as a reference table inside a curriculum module README.

## When to Use
- User asks to "add videos to module X"
- During initial curriculum generation (every module needs ≥3 videos)
- User asks to "find YouTube resources for topic X"

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Topic / Search Query | Yes | e.g. "3D printer electronics stepper motor wiring" |
| Module Path | Yes | Path to the README to update, e.g. `curriculum/01-electronics-basics/README.md` |
| Max Results | No | Default: 8. How many videos to fetch before filtering |

## Execution

### Step 1: Search YouTube

```bash
python execution/fetch_youtube_videos.py \
  --topic "your search query here" \
  --max 10 \
  --output .tmp/videos_results.json
```

The script returns: title, channel, URL, view count, duration, description snippet.

### Step 2: Filter Results

From the returned list, select videos that:
- Are from reputable channels (Teaching Tech, CNC Kitchen, Maker's Muse, Prusa, Creality, etc.)
- Are ≥5 minutes long (depth > quick tips)
- Have ≥10,000 views (community validated)
- Are not older than 4 years (unless covering timeless fundamentals)
- Match the module's skill level (beginner-appropriate for 00-05, intermediate for 06-07)

### Step 3: Embed in Module README

Add or update the `## 🎥 Recommended Videos` section in the target README:

```markdown
## 🎥 Recommended Videos

| Title | Channel | Why Watch |
|-------|---------|-----------|
| [Video Title](https://youtu.be/VIDEO_ID) | Channel Name | Covers X and Y clearly for beginners |
| [Video Title](https://youtu.be/VIDEO_ID) | Channel Name | Best explanation of Z concept |
| [Video Title](https://youtu.be/VIDEO_ID) | Channel Name | Hands-on demo of calibration |
```

Minimum: 3 videos. Target: 5 videos per module.

## Search Query Templates (Per Module)

Use these as starting points; refine based on results:

| Module | Suggested Query |
|--------|----------------|
| 00-introduction | `"introduction to 3D printing beginners 2023"` |
| 01-electronics-basics | `"3D printer electronics control board stepper motor explained"` |
| 02-mechanical-basics | `"3D printer mechanical components how it works"` |
| 03-software-and-slicing | `"3D printing slicer software tutorial beginners Cura PrusaSlicer"` |
| 04-filaments-and-materials | `"3D printing filament guide PLA PETG ABS comparison"` |
| 05-printer-operations | `"3D printer calibration bed leveling guide beginner"` |
| 06-troubleshooting | `"3D printing troubleshooting common problems fixes"` |
| 07-advanced-topics | `"Klipper firmware setup input shaping pressure advance"` |

## Fallback: No API Key

If `YOUTUBE_API_KEY` is not set:
1. Run `execution/search_web_resources.py --site youtube.com --query "your topic"` as a fallback
2. Or manually search YouTube and paste 3 URLs — the agent will fetch titles and format the table

## Known Reputable Channels

Always prefer videos from:
- **Teaching Tech** — Calibration, beginner guides, firmware
- **CNC Kitchen** — Materials science, structural testing
- **Maker's Muse** — Design, philosophy, reviews
- **Prusa3D** — Official Prusa tutorials
- **Tomb of 3D Printed Horrors** — Troubleshooting, fixes
- **Stefan (CNC Kitchen)** — Engineering deep dives
- **3D Printing Nerd** — Reviews and comparisons
- **ModBot** — Electronics and wiring

## Edge Cases

- If a video URL returns 404 when embedded → search for the same content again
- If a topic has no results > 10k views → lower the threshold to 1k for niche topics
- If results are all in a foreign language → add `language:en` filter or refine query
