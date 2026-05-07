# Update Curriculum — Directive

## Goal
Update or enrich an existing curriculum module without destroying current content.
The default mode is additive: add sections, improve clarity, add more videos, fix errors.

## When to Use
- User asks to "update", "improve", or "add to" a specific module
- A module is missing videos or further reading
- Content is outdated (technology changed, links are dead)
- User found an error or inaccuracy

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Module Path | Yes | e.g. `curriculum/01-electronics-basics/README.md` |
| What to Update | Yes | Specific section, or "all" for a full review |
| New Content / Context | No | Extra info the user provides to incorporate |

## Execution

### Step 1: Read the existing module

Read the target file in full before making any changes. Never edit blindly.

### Step 2: Identify gaps

Check the module against the quality checklist:
- [ ] Has `## 🎯 Learning Objectives`
- [ ] Has `## Prerequisites`
- [ ] Has `## 🎥 Recommended Videos` with ≥3 videos
- [ ] Has `## 📚 Further Reading` with ≥2 links
- [ ] Has `## ✅ Knowledge Check` with ≥3 questions
- [ ] No broken or placeholder links
- [ ] No acronyms undefined on first use
- [ ] All specs have citations

### Step 3: Enrich Videos (if needed)

If the video section is missing or has <3 videos:
```bash
python execution/fetch_youtube_videos.py --topic "<module topic>" --max 10 --output .tmp/videos_update.json
```

Add the best results to the `## 🎥 Recommended Videos` table.

### Step 4: Apply edits

- Only modify what needs changing
- Do not rewrite sections that are already high quality
- Preserve the author's voice if the content is good
- Add new sections at the end (before `## ✅ Knowledge Check`) rather than inserting mid-doc

### Step 5: Validate

After editing, re-read the module and confirm:
- All new links are valid (do not guess URLs)
- No new acronyms were introduced without definition
- The knowledge check still makes sense with the additions

## Safe Edit Rules

1. **Never delete existing content** unless it is factually wrong
2. **Never change specs** without sourcing the new values
3. **Never reorder sections** without user request
4. **Preserve all existing video links** — only add new ones, don't replace

## Bulk Update (All Modules)

If the user asks to "update all modules" or "add videos to everything":

For each module in `curriculum/`:
1. Read the module
2. Identify gaps
3. Run YouTube fetch if needed
4. Apply edits
5. Confirm changes

Do this sequentially (not in parallel) so you can report progress after each module.
