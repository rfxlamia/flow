# Prompt Optimization Patterns

Technical optimization patterns for transforming screenplay action into Veo 3 prompts.

## Prompt Structure Template

### Optimal Order (Research-Validated)

```
1. [Shot type + Camera movement]  - "Close-up shot, slow dolly in"
2. [Subject description]          - "young woman with dark hair, blue coat"
3. [Action/Motion]                - "turns to face the window"
4. [Setting/Environment]          - "inside minimalist apartment"
5. [Lighting/Atmosphere]          - "soft natural light from large windows"
6. [Style/Aesthetic]              - "cinematic, warm color grade"
7. [Audio cues]                   - "ambient city sounds, soft piano"
8. [Constraints/Negatives]        - "negative prompt: no text, no artifacts"
```

### Word Count Guidelines

| Section | Target Words | Purpose |
|---------|--------------|---------|
| Shot + Camera | 5-10 | Technical specification |
| Subject | 15-25 | Visual identification |
| Action | 10-20 | What happens |
| Setting | 10-15 | Where it happens |
| Lighting | 5-10 | Mood and atmosphere |
| Style | 5-10 | Aesthetic direction |
| Audio | 5-15 | Sound design |
| Constraints | 10-20 | Quality control |

**Total optimal:** 80-150 words (3-6 sentences)

---

## Camera Movement Terminology

### Use Exact Cinematic Terms

| Term | Effect | Veo 3 Performance |
|------|--------|-------------------|
| `dolly in` | Camera moves forward | ✅ Excellent |
| `dolly out` | Camera moves backward | ✅ Excellent |
| `slow pan left/right` | Horizontal rotation | ✅ Excellent |
| `tilt up/down` | Vertical rotation | ✅ Good |
| `tracking shot` | Follows subject | ✅ Good |
| `crane up/down` | Vertical boom | ✅ Good |
| `static` | No movement | ✅ Excellent |
| `handheld` | Subtle shake | ⚠️ Moderate |
| `aerial` | High angle moving | ✅ Good |
| `orbit` | 360° around subject | ⚠️ Moderate |

### Speed Modifiers

Always include speed:
- `slow` - Deliberate, contemplative
- `gentle` - Subtle, barely noticeable
- `smooth` - Professional, stable
- `quick` - Fast but controlled
- `rapid` - Very fast (risk of artifacts)

**Example:**
```
✅ "slow dolly in over 8 seconds"
❌ "camera moves closer" (too vague)
```

---

## Subject Description Patterns

### First Appearance (Detailed)

Include ALL identifying features:

```
[AGE/BUILD] [GENDER if relevant] with [HAIR], wearing [CLOTHING], 
[DISTINCTIVE FEATURES], [CURRENT STATE/EMOTION]

Example:
"tall woman in her 30s with shoulder-length auburn hair, wearing olive green 
field jacket over white blouse, round glasses, small scar above left eyebrow, 
expression of determined curiosity"
```

### Continuation Appearance (Abbreviated)

Repeat KEY identifiers only:

```
"same auburn-haired woman in olive jacket" 
OR
"the woman with round glasses from previous"
```

### Non-Human Subjects

Apply same pattern:

```
"boxy robot with weathered chrome frame, single glowing blue optical sensor, 
mechanical treads, small antenna on top, dust-covered exterior"
```

---

## Action Optimization

### Strong vs Weak Verbs

| Weak (Avoid) | Strong (Use) |
|--------------|--------------|
| walks | strides, trudges, ambles |
| looks | gazes, glances, stares |
| picks up | grasps, snatches, lifts |
| moves | glides, lurches, drifts |
| says | whispers, announces, mutters |

### Motion Clarity

Be specific about:
- Direction (left to right, toward camera)
- Speed (slow, deliberate, sudden)
- Starting position (enters from left)
- Ending position (stops at center frame)

```
✅ "strides confidently from left frame edge toward camera, stops at center"
❌ "walks across the scene"
```

### Multi-Beat Actions

For 8s, limit to 1-2 actions:

```
✅ "reaches for the letter, unfolds it slowly"
❌ "reaches for the letter, unfolds it, reads it, puts it down, sighs, walks away"
```

---

## Lighting Patterns

### Natural Lighting Terms

| Term | Effect | Best For |
|------|--------|----------|
| `golden hour` | Warm, low sun | Romance, nostalgia |
| `blue hour` | Cool twilight | Mystery, melancholy |
| `overcast` | Soft, diffused | Neutral, documentary |
| `harsh noon` | Strong shadows | Drama, tension |
| `backlit` | Rim lighting | Silhouettes, mystery |
| `soft natural` | Window light | Interior, intimate |

### Artificial Lighting Terms

| Term | Effect | Best For |
|------|--------|----------|
| `neon` | Colored, urban | Cyberpunk, night scenes |
| `practical` | In-scene lights | Realism, atmosphere |
| `rim light` | Edge highlighting | Separation, drama |
| `key light` | Main illumination | Standard setup |
| `high-key` | Bright, even | Commercial, happy |
| `low-key` | Dark, contrasted | Noir, thriller |

### Lighting + Color Grade

Combine lighting with grade:

```
"golden hour backlight with warm orange-teal color grade"
"neon-lit street with high contrast, desaturated shadows"
"soft window light, naturalistic color palette"
```

---

## Audio Patterns

### Audio Prompt Format

```
Audio: [ambient layer], [specific SFX], [music if any]
```

### Ambient Categories

| Category | Examples |
|----------|----------|
| Urban | traffic, sirens, crowd chatter |
| Nature | wind, birds, rustling leaves |
| Interior | room tone, clock ticking, HVAC hum |
| Weather | rain, thunder, wind howling |
| Industrial | machinery, beeping, hydraulics |

### SFX Specificity

Be exact:
```
✅ "footsteps on gravel, door creaking open"
❌ "walking sounds"
```

### Dialogue Format

```
[Character] says: "[exact dialogue]" (no subtitles)
```

**Example:**
```
Audio: Sarah says: "I didn't expect to see you here" with soft rain ambience 
and distant traffic. (no subtitles)
```

---

## Negative Prompts

### Essential Negatives

Always include:
```
negative prompt: no text overlays, no watermarks
```

### Continuity Negatives

For continuation chunks:
```
negative prompt: no lighting change, no character drift, no style shift, 
no background change
```

### Quality Negatives

For problem-prone content:
```
negative prompt: no hand distortion, no face warping, no object morphing
```

### Common Issues to Negate

| Issue | Negative |
|-------|----------|
| Garbled text | `no text, no signs` |
| Hand problems | `no hand distortion` |
| Face issues | `no face warping, no uncanny expressions` |
| Object instability | `no morphing, no object change` |
| Style drift | `no style shift, maintain aesthetic` |
| Lighting jumps | `no lighting change` |
| Extra elements | `no additional characters, no new objects` |

---

## Optimization Examples

### Before (Screenplay Action)

```
Robot rolls across wasteland. Stops at rubble pile. Discovers tiny flower. 
Reaches toward it carefully.
```

### After (Optimized Veo 3 Prompt)

```
Establishing wide shot, slow dolly forward, post-apocalyptic wasteland with 
ruined skyscrapers silhouetted against pale morning sun, gray dust covering 
cracked asphalt, thick smog atmosphere. A boxy robot with weathered chrome body 
and single glowing blue optical sensor is visible in the distance, rolling 
slowly across the terrain. Cinematic, muted color palette with subtle warm 
highlights. Audio: wind howling softly, distant debris settling, mechanical 
whir. negative prompt: no text, no multiple subjects in motion
```

### Continuation Prompt

```
[CONTINUATION from previous clip] Medium shot, static camera, same weathered 
chrome robot with blue optical sensor rolls into frame from left, mechanical 
treads leaving marks in gray dust. Slow, deliberate movement. Same wasteland 
environment, same golden lighting, maintain atmosphere. Robot stops at pile of 
concrete rubble at center frame. Audio: mechanical whirring, treads on gravel, 
wind. negative prompt: no lighting change, no character drift, no style shift
```

---

## Prompt Templates

### Establishing Shot

```
[Wide/Extreme wide] establishing shot, [slow camera movement], [setting with 
specific details], [time of day lighting], [atmospheric elements]. [Subject if 
present] visible [position]. [Style description], [color palette]. Audio: 
[ambient sounds]. negative prompt: [relevant negatives]
```

### Character Introduction

```
[Shot size] shot, [camera movement], [FULL character description including 
age/appearance/clothing/distinctive features], [action with direction], 
[setting context], [lighting], [style]. Audio: [ambient + relevant SFX]. 
negative prompt: no face warping, no costume change
```

### Continuation

```
[CONTINUATION from previous clip] [Shot size], [camera movement], [abbreviated 
character description with key identifiers], [continued action from setup 
point], same [setting], maintain [lighting/atmosphere]. Audio: [matching audio]. 
negative prompt: no lighting change, no character drift, no style shift
```

### Dialogue

```
[Close-up/Medium] shot, [static or gentle movement], [character description], 
[speaking action]. [Character name] says: "[exact dialogue]" [Setting context], 
[lighting]. Audio: [delivery style], [ambient underneath]. (no subtitles)
negative prompt: no text overlays
```

### Reveal

```
[Shot transitioning closer], slow [dolly in/push in], [the revealed element 
with detail], [spatial relationship to previous], [subject reaction if visible], 
[lighting emphasis], [emotional tone]. Audio: [punctuating sound or silence]. 
negative prompt: [relevant to reveal type]
```
