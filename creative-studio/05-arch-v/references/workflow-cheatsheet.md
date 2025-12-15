# ARCH-V Workflow Quick Reference

Condensed cheatsheet for rapid workflow navigation.

## Decision Tree

```
START: "I want to create a video"
    │
    ├─────────────────────────────────────────────┐
    │                                             │
Path 1: Text-to-Video                    Path 2: Image-to-Video
    │                                             │
    ▼                                             ▼
"Short or Long?"                          STAGE A: Create Image
    │                                             │
    ├─> Short                                     ├─> imagine skill
    │   └─> short-prompt-guide                    ├─> great-prompt-anatomy
    │                                             │   (visual only: 1,2,4,5,6,8)
    ├─> Long                                      │
    │   └─> long-prompt-guide                     └─> Output: Imagen prompt
    │                                             │
    ├─> great-prompt-anatomy (all 8)              ▼
    ├─> camera-movements (if needed)       User generates image
    │                                             │
    └─> Validate & Output                         ▼
        └─> Veo 3 text-to-video prompt     STAGE B: Add Motion
                                                  │
                                                  ├─> "Short or Long motion?"
                                                  ├─> camera-movements
                                                  ├─> great-prompt-anatomy
                                                  │   (motion: 3,5,7)
                                                  │
                                                  └─> Validate & Output
                                                      └─> Veo 3 image-to-video prompt
```

---

## Path 1: Text-to-Video Checklist

### Short Prompt
```
[ ] Format & Style upfront
[ ] Subject (who/what)
[ ] Setting (where/when)
[ ] Action (what's happening)
[ ] Camera (shot + angle + 1 movement)
[ ] Lighting (brief)
[ ] Audio (ambience/dialogue)
[ ] Constraints (if any)
```

### Long Prompt (Minimum 4 blocks)
```
[ ] 1. Format & Tone
[ ] 2. Main Subjects
[ ] 4. Location & Framing (FG/MG/BG)
[ ] 7. Actions & Camera Beats

Optional additions:
[ ] 3. Wardrobe & Props
[ ] 5. Lighting & Palette (3-5 colors)
[ ] 6. Continuity Rules
[ ] 8. Montage Plan
[ ] 9. Dialogue
[ ] 10. Sound & Foley
[ ] 11. Finish
```

---

## Path 2: Image-to-Video Checklist

### Stage A: Imagen Prompt
```
[ ] Subject (detailed visual)
[ ] Setting (environment)
[ ] Style (photo or art style)
[ ] Camera (STATIC: size, angle only)
[ ] Lighting (sources, palette)
[ ] Constraints (visual only)

❌ NO Motion
❌ NO Audio
❌ NO Camera movements
✅ Token count < 480
```

### Stage B: Veo 3 Motion
```
[ ] Action (motion/animation)
[ ] Camera (movement from static)
[ ] Audio (sound design)

✅ Motion achievable from image
✅ Style matches Stage A
✅ Audio fits visual aesthetic
```

---

## Validation Quick Check

### Universal
- [ ] All required components present
- [ ] One camera movement per beat
- [ ] Style consistent throughout
- [ ] 3-5 color anchors (long prompts)

### Path 1 Specific
- [ ] Time/weather consistent
- [ ] Audio matches setting
- [ ] FG/MG/BG structure (long)

### Path 2A Specific (Imagen)
- [ ] NO motion verbs
- [ ] NO audio descriptions
- [ ] Token count < 480

### Path 2B Specific (Motion)
- [ ] Motion feasible from image
- [ ] Camera respects composition
- [ ] Style matches image

---

## Component Reference

### 8 Mandatory Components (great-prompt-anatomy)

| # | Component | Path 1 | Path 2A | Path 2B |
|---|-----------|--------|---------|---------|
| 1 | Subject | ✅ | ✅ | (from image) |
| 2 | Setting | ✅ | ✅ | (from image) |
| 3 | Action | ✅ | ❌ | ✅ |
| 4 | Style/Genre | ✅ | ✅ | (match image) |
| 5 | Camera/Comp | ✅ | ✅ static | ✅ movement |
| 6 | Lighting/Mood | ✅ | ✅ | (from image) |
| 7 | Audio | ✅ | ❌ | ✅ |
| 8 | Constraints | ✅ | ✅ | ✅ |

---

## Camera Movement Quick Ref

**Rule:** ONE movement per beat

**Common movements:**
- Dolly In/Out
- Pan Left/Right
- Tilt Up/Down
- Arc Left/Right
- Crane Up/Down
- FPV Drone
- Static
- Zoom In/Out

**See camera-movements skill for full list (64 movements)**

---

## Common Conflicts & Fixes

### Time/Weather
```
❌ "Golden hour" + "Harsh midday sun"
✅ "Golden hour" + "Low-angle warm sun"
```

### Camera Movement
```
❌ "Dolly in while panning left"
✅ "Dolly in" (choose one)
```

### Audio/Setting
```
❌ Quiet library + Loud traffic
✅ Quiet library + Pages turning, whispers
```

### Motion in Static (Imagen)
```
❌ "Person running across field"
✅ "Person frozen mid-stride"
```

---

## Output Format

### Path 1 Short
```
Format & style: [aesthetic]
[Subject] [action] in [setting]
[Camera] [lighting] [audio]
```

### Path 1 Long
```
Format & Tone: [genre/mood]
Main Subjects: [characters]
Location & Framing: [FG/MG/BG]
Actions & Camera Beats:
  0-Xs: [shot] [movement]; [action]
[Additional blocks as needed]
```

### Path 2A (Imagen)
```
[Art style or "A photo of"], [detailed subject],
[context/placement], [technical specs: lens/lighting],
[quality modifiers], [atmosphere]
```

### Path 2B (Veo 3 motion)
```
From this image: [specific motion], [camera movement],
[audio design], maintain [style from image]
```

---

## Skills Integration Map

```
ARCH-V (orchestrator)
    │
    ├─> great-prompt-anatomy
    │   └─> 8 components framework
    │
    ├─> camera-movements
    │   └─> 64 standardized movements
    │
    ├─> short-prompt-guide
    │   ├─> When to use
    │   ├─> Descriptive approach
    │   ├─> Directive approach
    │   └─> 55+ examples
    │
    ├─> long-prompt-guide
    │   ├─> Production Brief (11 blocks)
    │   ├─> Template
    │   └─> 5 complete examples
    │
    └─> imagine
        ├─> Subject-Context-Style
        ├─> Photography specs
        ├─> Art style references
        └─> Science SARU default
```

---

## Workflow Selection Guide

### Choose Path 1 if:
- Clear vision for complete video
- Comfortable describing motion in text
- Want faster single-step workflow
- Don't need perfect initial composition control

### Choose Path 2 if:
- Want precise control over starting visual
- Have specific still composition in mind
- Need perfect framing before motion
- Using art styles (Science SARU, etc.)
- Iterating on visual before animating

### Choose Short if:
- <3 sentences to describe
- Simple filler/B-roll
- Atmospheric scene
- No dialogue

### Choose Long if:
- Dialogue present
- Multiple characters
- >3 action beats
- Complex choreography
- Need continuity control

---

## Quick Start Templates

### Template 1: Path 1 Short - Product
```
Format & style: Clean product commercial
[Product name] on [surface], [lens 60-105mm macro],
[lighting type], [background], professional photography
```

### Template 2: Path 1 Long - Dialogue
```
Format & Tone: [genre] - [mood]
Main Subjects: [character descriptions]
Location & Framing:
  FG: [elements]
  MG: [characters]
  BG: [context]
Actions & Camera Beats:
  0-Xs: [shot] [movement]; [action]
Dialogue: Character: "Text"
Sound & Foley: [specific sounds]
```

### Template 3: Path 2A - Imagen
```
Science SARU animation style, [character description with
elastic limbs, large eyes], [environment with flat color blocks],
[golden hour lighting], [atmosphere], [quality modifiers]
```

### Template 4: Path 2B - Motion
```
From image: [character action], [camera movement from vocabulary],
[ambient sounds + music if needed], maintain [style from image]
```

---

## Token Budget Reference

| Component | Tokens |
|-----------|--------|
| ARCH-V orchestrator | ~2,000 |
| camera-movements | ~1,200 |
| great-prompt-anatomy | ~1,400 |
| short-prompt-guide | ~1,600 |
| long-prompt-guide | ~2,200 |
| imagine | (varies by style) |
| **Total system** | **~8,600** |
| **vs Monolithic** | **~15,000** |
| **Savings** | **43%** |

---

## Troubleshooting

### PROMPT-LOCKED?
1. Check error message for specific conflict
2. Review validation rules reference
3. Apply suggested fix
4. Re-validate

### Not sure which path?
- Default: Path 1 (faster)
- Need visual precision: Path 2
- Using art styles: Path 2

### Not sure short or long?
- Can describe in <3 sentences: Short
- Has dialogue: Long
- Has >3 action beats: Long
- Default: Short (simpler)

### Motion not working (Path 2B)?
- Check if motion possible from image
- Ensure camera movement respects composition
- Verify style matches image

---

## Progressive Disclosure

**Beginner:** Let ARCH-V guide with questions

**Intermediate:** Specify path: "Text-to-video short for product"

**Advanced:** Full spec: "Path 2, Science SARU style, golden hour Jakarta street, then slow dolly motion with street ambience"

ARCH-V adapts to your expertise level!
