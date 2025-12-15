# Great Prompt Anatomy Reference

Every solid Veo 3 prompt requires 8 mandatory components.

---

## THE 8 MUST-HAVE COMPONENTS

### 1. Subject
**What:** Who or what appears in the shot
**Example:** "A glass of red wine" or "Young couple under umbrella"
**Why mandatory:** Defines focal point; AI will invent subject if not specified

### 2. Setting
**What:** Where and when the scene happens
**Example:** "White linen tablecloth" or "Rain-soaked cobblestone street at dusk"
**Why mandatory:** Anchors spatial and temporal context

### 3. Action
**What:** What's unfolding in the scene
**Example:** "Tips over in slow motion" or "She adjusts umbrella, faint smile"
**Why mandatory:** Drives narrative momentum; static without action

### 4. Style/Genre
**What:** Visual aesthetic and mood category
**Example:** "Cinematic realism" or "Neo-noir with high-contrast shadows"
**Why mandatory:** Guides AI's aesthetic decisions

### 5. Camera/Composition
**What:** Shot size, angle, and movement
**Example:** "Close-up, low angle" or "Medium shot with gentle dolly-in"
**Why mandatory:** Defines cinematography; without this, AI chooses randomly

### 6. Lighting/Mood
**What:** Light sources and emotional tone
**Example:** "Moody with single warm spotlight" or "Soft natural sunlight"
**Why mandatory:** Shapes atmosphere; lighting is 50% of visual impact

### 7. Audio
**What:** Dialogue, ambient sound, music cues
**Formats:**
- Dialogue: `He says: "We don't have much time."`
- Ambience: "Soft string quartet fades into silence"
- Clean frames: Add `(no subtitles)` if dialogue without text overlay
**Why mandatory:** Sound sells the scene; silence must be specified

### 8. Constraints
**What:** Prohibitions or exact requirements
**Example:** "(no subtitles)" or "exactly six candles on the table"
**Why mandatory:** Prevents unwanted elements; AI creative unless constrained

---

## VALIDATION CHECKLIST

Before releasing prompt, verify:
- [ ] All 8 components present
- [ ] Camera movement uses standardized vocabulary
- [ ] Audio format correct (dialogue with colon)
- [ ] Constraints explicitly stated
- [ ] Style clear and consistent

---

## COMPLETE EXAMPLE

```
Close-up, low angle. A glass of red wine tips over in slow motion on a white
linen tablecloth. Rich burgundy liquid spills and spreads. Lighting: moody,
with a single warm spotlight. Audio: soft string quartet fades into silence.
(no subtitles)
```

**Breakdown:**
1. Subject: Glass of red wine
2. Setting: White linen tablecloth
3. Action: Tips over in slow motion, liquid spills
4. Style: (Implied cinematic realism)
5. Camera: Close-up, low angle
6. Lighting: Moody, single warm spotlight
7. Audio: Soft string quartet fades to silence
8. Constraints: (no subtitles)

---

## AUDIO PATTERNS

### Dialogue Format
`Character name: "Dialogue text"`

### Ambient Sound
Be specific: "Hollow wind whistling through ruins" vs generic "wind"

### Silence
Specify explicitly: "No background music" or "Complete silence"

### Subtitle Control
Clean frames: Add `(no subtitles)` after dialogue
