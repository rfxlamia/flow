# Step 02: Component Building & Validation

**Purpose:** Guide user through building mandatory components and validate for conflicts.

---

## LOAD APPROPRIATE REFERENCES

Based on step-01 choices, NOW load:

### If short prompt/motion:
Read: `./references/short-prompt-guide.md`

### If long prompt/motion:
Read: `./references/long-prompt-guide.md`

### For all paths:
Read: `./references/great-prompt-anatomy.md` (for 8-component validation)

### If camera movement specified:
Read: `./references/camera-movements.md` (for vocabulary validation)

---

## PATH 1: TEXT-TO-VIDEO WORKFLOW

### Component Collection

Guide user through ALL 8 mandatory components:

**Checklist Template:**
- [ ] 1. Subject (who/what in shot)
- [ ] 2. Setting (where/when)
- [ ] 3. Action (what's happening)
- [ ] 4. Style/Genre (aesthetic)
- [ ] 5. Camera/Composition (shot size, angle, movement)
- [ ] 6. Lighting/Mood (light sources, emotional tone)
- [ ] 7. Audio (dialogue, ambience, music)
- [ ] 8. Constraints (prohibitions, exact requirements)

**For each missing component:**
Ask user to provide specific details. Use examples from loaded prompt guide.

---

## PATH 2: IMAGE-TO-VIDEO WORKFLOW

### Stage A: Imagen Prompt (Visual Components)

Collect VISUAL components only:
- [ ] 1. Subject (detailed visual description)
- [ ] 2. Setting (environment, placement)
- [ ] 4. Style/Genre (photographic or artistic style)
- [ ] 5. Camera/Composition (shot size, angle - STATIC, no movement)
- [ ] 6. Lighting/Mood (light sources, color palette)
- [ ] 8. Constraints (visual prohibitions)

**NOT included in Stage A:**
- Action (no motion in still image)
- Audio (images have no sound)
- Camera movements (static composition)

**Validate:** No motion words (running, flying, moving) - image is static

### Stage B: Veo 3 Motion Prompt

After user confirms Stage A complete:

Collect MOTION components:
- [ ] 3. Action (what motion/animation occurs)
- [ ] 5. Camera/Composition (movement from static image)
- [ ] 7. Audio (sound design for video)

**Load camera-movements.md** for movement vocabulary

---

## VALIDATION CHECKS

### Time/Weather Conflicts

**REJECT combinations like:**
- "Golden hour" with "midnight"
- "Harsh noon sun" with "soft evening light"

**FIX:** Make lighting consistent with time of day

### Camera Movement Conflicts

**REJECT:**
- Multiple movements per beat: "Dolly in while arc left"

**FIX:** Choose ONE movement per beat from standardized vocabulary

### Spatial Coherence (Long Prompts Only)

**REQUIRE:**
- FG/MG/BG structure defined
- Color anchors (3-5 colors repeated)
- Continuity rules explicit

### Path 2 Stage A Validation

**REJECT motion in static image:**
- "person running across field"

**FIX:** Describe static composition
- "person mid-stride in running pose"

---

## VALIDATION RESULT

### If All Valid:

```
VALIDATION PASSED

All 8 components present
No conflicts detected
Camera movements use standardized vocabulary
Style consistency maintained

Ready for output generation
```

**Proceed to step-03**

### If Validation Fails:

```
PROMPT-LOCKED

Missing/Conflicting:
- [specific issue 1]
- [specific issue 2]

Suggested fixes:
- [actionable fix 1]
- [actionable fix 2]

Would you like me to help resolve these?
```

**Stay in step-02 until resolved**

---

## OUTPUT TO STEP-03

Pass these values:
- `validation_status`: passed OR locked
- `components`: All 8 components collected
- `prompt_text`: Draft prompt text
- `path_type`: text-to-video OR image-to-video
- `conflicts_resolved`: List of any resolved conflicts

---

## HANDOFF

When validation passes, load: `./steps/step-03-generate-output.md`
