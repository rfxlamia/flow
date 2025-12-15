# Step 01: Key Frame Selection & Style

**Goal:** Review key frames from production-validator and confirm art style.

**Scope:** Selection and style confirmation only.

**Token Budget:** ~250 tokens

---

## INPUT VERIFICATION

Verify you have loaded from production-validator:

| Field | Required | Example |
|-------|----------|---------|
| `key_frames` | Yes | [{chunk_id, description, purpose}] |
| `visual_style_guide` | Yes | {color_palette, lighting, textures, mood} |
| `validated_screenplay_file` | Yes | Path to validated screenplay |

---

## KEY FRAME REVIEW

### 1. List Available Key Frames

From validator output, list all recommended key frames:

```
KEY FRAMES FOR IMAGE GENERATION:
================================

1. Chunk 1a: "Frozen beach wide establishing shot"
   Purpose: Location establishment
   Scene Context: Opening, sets tone

2. Chunk 1c: "Sarah placing jacket on ice"
   Purpose: Emotional beat
   Scene Context: Character action, symbolism

3. Chunk 3b: "Shrine corner close-up"
   Purpose: Character detail
   Scene Context: Reveals devotion

[Continue for all key frames]

Total Key Frames: {count}
```

### 2. Frame Prioritization

Categorize frames by importance:

| Priority | Use For | Count |
|----------|---------|-------|
| Essential | Hero images, poster, thumbnail | 3-5 |
| Important | Story beats, emotional moments | 5-8 |
| Supporting | Continuity, background | Remaining |

### 3. Verify Visual Consistency

Check visual_style_guide for consistency requirements:

```
VISUAL STYLE GUIDE:
==================
Color Palette: {palette}
Lighting: {lighting style}
Textures: {texture list}
Mood: {mood description}

CONSISTENCY REQUIREMENTS:
- All frames must maintain: {key elements}
- Character appearance: {repeat descriptors}
- Environment continuity: {key settings}
```

---

## ART STYLE SELECTION

### 1. Confirm Style with User

Present available art styles:

```
ART STYLE OPTIONS:

1. Science SARU (Default)
   - Anime aesthetic, Masaaki Yuasa style
   - Elastic limbs, expressive eyes, painterly textures
   - Best for: Emotional stories, stylized characters

2. Crewdson Hyperrealism
   - Cinematic staged photography
   - Dramatic lighting, suburban scenes
   - Best for: Atmospheric, mysterious tones

3. iPhone Social Media
   - Casual authentic photos
   - Natural lighting, everyday moments
   - Best for: Relatable, modern content

4. Corporate Memphis
   - Flat illustration style
   - Simple shapes, bright colors
   - Best for: Explainers, light content

5. Photography (No art style)
   - Photorealistic rendering
   - Technical camera specs
   - Best for: Documentary, realistic

Which style should I use? (default: Science SARU)
```

### 2. Load Art Style Reference

Once style is confirmed:

**If Science SARU:** Load `references/artstyle-sciencesaru.md`
**If Crewdson:** Load `references/artstyle-crewdson-hyperrealism.md`
**If iPhone:** Load `references/artstyle-iphone-social-media.md`
**If Corporate Memphis:** Load `references/artstyle-corporate-memphis.md`
**If Photography:** No reference needed, use technical specs

### 3. Extract Style Vocabulary

From loaded reference, extract:

```
STYLE: {name}
==============

Key Vocabulary:
- Character: {descriptors}
- Environment: {descriptors}
- Lighting: {descriptors}
- Texture: {descriptors}
- Color: {descriptors}

Prompt Pattern:
"{style foundation}, {character specs}, {environment specs}, {atmosphere specs}, {technical specs}"
```

---

## FRAME PREPARATION

For each key frame, prepare:

```
FRAME 1a PREPARATION:
====================
Chunk: 1a
Description: Frozen beach wide establishing shot
Art Style: {selected}
Aspect Ratio: 16:9 (widescreen landscape)

From Screenplay:
- Location: Frozen beach
- Time: Dawn
- Mood: Desolate, lonely
- Key Visuals: [list from screenplay]

From Style Guide:
- Color Palette: Muted blues and grays
- Lighting: Pale winter dawn

Notes for Prompt:
- {specific notes}
```

---

## LOAD NEXT STEP

Execute: `Load step-02-generate-prompts.md`

---

**Proceed to Step 02 when style is confirmed and frames are prepared.**
