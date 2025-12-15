# Step 02: Apply Screenplay Formatting

**Goal:** Convert scene breakdown to professional screenplay format with XML tags.

**Scope:** Formatting and visual enhancement only.

**Token Budget:** ~400 tokens

---

## FORMATTING PROCESS

### 1. Create Sluglines

For each scene, create professional slugline:

**Format:** `INT/EXT. LOCATION - TIME`

**Decision guide:**
| Location Type | Use |
|--------------|-----|
| Buildings, rooms, vehicles | INT. |
| Outdoors, streets, nature | EXT. |
| Threshold (doorways, windows) | INT./EXT. |

**Time options:**
- DAY - General daylight
- NIGHT - After dark
- DAWN - Early morning, sunrise
- DUSK - Evening, sunset
- CONTINUOUS - Immediately follows previous scene

**Example:**
```
Scene: "Frozen beach at dawn, woman standing alone"
Slugline: EXT. FROZEN BEACH - DAWN
```

### 2. Write Action Lines

Transform visual action into screenplay format:

**Before (from storyteller):**
```
Woman stands at frozen beach, staring at horizon.
She places his jacket on the ice.
```

**After (screenplay format):**
```
SARAH (38, weathered but elegant, wearing a heavy wool coat) stands at the edge of the frozen shoreline. Pale winter light catches the ice crystals around her.

She removes a worn leather jacket from her bag—clearly a man's jacket, too large for her. Her hands tremble as she places it carefully on the ice, smoothing the shoulders as if dressing an invisible form.
```

**Enhancement checklist:**
- [ ] Character name ALL CAPS on first appearance
- [ ] Physical description on first appearance
- [ ] Lighting/atmosphere mentioned
- [ ] Sensory details added
- [ ] Present tense throughout
- [ ] Active voice

### 3. Generate Key Visuals

Extract 3-5 specific visual elements for each scene:

**Good key visuals:**
- "frozen shoreline with ice crystal formations"
- "woman in heavy wool coat, wind-blown hair"
- "worn leather jacket placed on ice"
- "pale winter sunrise, weak light"

**Bad key visuals (too vague):**
- "beach"
- "woman"
- "morning"

### 4. Add Mood Tags

Extract mood from emotional beat:

| Emotional Beat | Mood Tags |
|---------------|-----------|
| "longing, waiting" | "melancholic, yearning" |
| "grief, loss" | "somber, heavy" |
| "hope emerging" | "tender, hopeful" |
| "obsession intensifying" | "unsettling, desperate" |

---

## XML STRUCTURE

Format each scene with this structure:

```xml
<scene number="{N}" duration="{X}s">
  <slugline>{INT/EXT. LOCATION - TIME}</slugline>
  <location>{Location Name}</location>
  <time>{Time of Day}</time>
  <characters>{Comma-separated character names}</characters>
  <mood>{mood tags}</mood>
  <key_visuals>
    <visual>{specific visual 1}</visual>
    <visual>{specific visual 2}</visual>
    <visual>{specific visual 3}</visual>
  </key_visuals>
  <action>
{Full action lines with screenplay formatting}
  </action>
  <!-- Optional: only if scene has dialogue -->
  <dialogue>
CHARACTER NAME
(parenthetical if needed)
Dialogue text here.
  </dialogue>
</scene>
```

### Dialogue Guidelines

**Use sparingly:** Short films need visual storytelling.

**When to include:**
- Critical plot information
- Character voice establishment
- Emotional climax moments

**Format:**
```
CHARACTER NAME
(emotional cue)
Short, punchy dialogue. Maximum 3-4 lines.
```

---

## VISUAL ENHANCEMENT REFERENCE

If scenes need richer visual descriptions:

**Load:** `references/advanced-techniques.md`

**Enhancement techniques:**
1. **Lighting language:** "harsh fluorescent" vs "soft golden hour"
2. **Texture details:** "cracked leather" vs "smooth plastic"
3. **Color palette:** "muted blues and grays" vs "warm amber tones"
4. **Atmospheric elements:** "dust motes in light" vs "steam rising"

---

## SCENE-BY-SCENE OUTPUT

Process each scene and create formatted version:

```
SCENE 1 FORMATTED:
==================
<scene number="1" duration="45s">
  [complete XML structure]
</scene>

SCENE 2 FORMATTED:
==================
...
```

---

## PROPS IDENTIFICATION

While formatting, build prop list:

```
PROPS IDENTIFIED:
- Worn leather jacket (male, too large for Sarah)
- Wool coat (heavy, dark color)
- Ice formations (natural, crystal-like)
...
```

This feeds into production-validator.

---

## LOAD NEXT STEP

Execute: `Load step-03-generate-output.md`

---

**Proceed to Step 03 when all scenes are formatted.**
