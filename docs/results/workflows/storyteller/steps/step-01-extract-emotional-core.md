# Step 01: Extract Emotional Core

**Goal:** Analyze the selected content from diverse-content-gen and extract the emotional foundation.

**Scope:** Analysis only - no visual transformation yet.

**Token Budget:** ~300 tokens (analysis logic + emotional mapping)

---

## INPUT VERIFICATION

Before proceeding, verify you have loaded these fields from diverse-content-gen:

| Field | Source | Example |
|-------|--------|---------|
| `content_file` | tracking YAML | "workflows/diverse-content-gen/outputs/content-2025-12-13.md" |
| `selected_idea_id` | tracking YAML | 3 |
| `emotional_core` | tracking YAML | "longing, devotion" |
| `pov` | tracking YAML | "first_person" |
| `setting` | tracking YAML | "coastal, frozen beach" |
| `tone` | tracking YAML | "poetic_mythic" |
| `structure_type` | tracking YAML | "extended_metaphor" |

**If missing:** Go back to Step 0 in workflow.md and load input properly.

---

## EMOTIONAL CORE ANALYSIS

### 1. Read the Selected Content

Load the content file and find the selected idea section:

1. Open the content markdown file
2. Navigate to "IDEA {selected_idea_id}"
3. Read the full content of that idea

### 2. Identify Primary Emotion

Analyze the content and identify:

**Primary Emotion:** What is the DOMINANT feeling?
- Single word or short phrase
- Examples: longing, grief, obsession, hope, devotion, abandonment, jealousy

**Emotional Intensity:** Scale 1-10
- 1-3: Subtle, understated
- 4-6: Present but controlled
- 7-9: Overwhelming, consuming
- 10: All-encompassing, destructive

**Relationship Dynamic:** Who feels what toward whom?
- Direction: Speaker → Beloved, Beloved → Speaker, Mutual
- Balance: Equal, one-sided, reversed
- Example: "Speaker → Beloved (one-directional adoration)"

**Temporal Context:** When is this emotion happening?
- Present pain
- Past memory
- Future fear
- Timeless/eternal state

### 3. Extract Key Metaphors

List all metaphors and abstract concepts that need visual translation:

**Format:**
```
METAPHOR 1: "[exact quote from content]"
Literal meaning: [what it literally says]
Emotional meaning: [what it really means]
Visual challenge: [why this is hard to film]

METAPHOR 2: "[exact quote]"
...
```

**Example:**
```
METAPHOR 1: "Aku menjadikanmu altar pribadi"
Literal meaning: I made you my personal altar
Emotional meaning: Worship-level devotion, treating beloved as sacred
Visual challenge: "Altar" is abstract - need physical behavior showing worship
```

### 4. Identify Visual Anchors

What concrete elements already exist in the content?

**Physical elements mentioned:**
- Locations (beach, room, street)
- Objects (jacket, letter, photograph)
- Actions (waiting, returning, watching)
- Time markers (dawn, years, seasons)

These become the foundation for scene building.

---

## OUTPUT: EMOTIONAL CORE DOCUMENT

Create a mental document with this structure:

```
EMOTIONAL CORE ANALYSIS
=======================

SOURCE: [content file path]
SELECTED IDEA: #[id] - [title]

PRIMARY EMOTION
---------------
Emotion: [word/phrase]
Intensity: [1-10]
Dynamic: [who → whom]
Temporal: [when]

METAPHORS TO TRANSLATE
----------------------
1. "[metaphor]" → [emotional meaning] → [visual challenge]
2. "[metaphor]" → [emotional meaning] → [visual challenge]
...

VISUAL ANCHORS (existing)
------------------------
Locations: [list]
Objects: [list]
Actions: [list]
Time markers: [list]

OVERALL TONE
------------
[tone from handoff] - [brief description of how to maintain this]
```

---

## SELF-AWARENESS CHECKPOINT

Before proceeding to step-02, verify:

- [ ] Selected content fully read and understood
- [ ] Primary emotion clearly identified
- [ ] All metaphors listed with emotional meanings
- [ ] Visual anchors extracted from existing content
- [ ] Tone preservation strategy noted

If any checkbox fails, re-read the content or ask user for clarification.

---

## LOAD NEXT STEP

Execute: `Load step-02-transform-to-visual.md`

---

**Proceed to Step 02 when emotional core is fully extracted.**
