# Validation Rules & Conflict Detection

Comprehensive validation logic used by ARCH-V orchestrator.

## Table of Contents
- [Universal Validations](#universal-validations)
- [Path 1 Validations (Text-to-Video)](#path-1-validations-text-to-video)
- [Path 2 Validations (Image-to-Video)](#path-2-validations-image-to-video)
- [Conflict Detection Examples](#conflict-detection-examples)
- [Fix Suggestions](#fix-suggestions)

---

## Universal Validations

These apply to ALL workflows regardless of path.

### Mandatory Component Presence

**Rule:** All required components for chosen workflow must be present with specific details.

**Checks:**
- No empty placeholders ("TBD", "will add later", "[insert here]")
- No vague descriptions ("nice lighting", "good mood", "interesting")
- Specific details provided ("golden hour backlight", "melancholic tone", "worn leather jacket")

**Examples:**

❌ **FAIL:**
```
Subject: A person
Setting: Somewhere outdoors
Style: Good looking
```

✅ **PASS:**
```
Subject: Elderly woman, 70s, weathered hands, kind smile
Setting: Park bench, autumn afternoon, fallen leaves around
Style: Documentary realism, intimate portrait
```

### Camera Movement Validation

**Rule:** ONE camera movement per beat/timestamp. Use standardized vocabulary from camera-movements skill.

**Checks:**
- Single movement per time segment
- Movement name matches camera-movements vocabulary exactly
- No compound movements ("dolly while panning")
- Movement appropriate for shot type

**Examples:**

❌ **FAIL:**
```
0-4s: Dolly in while panning left and tilting up
```

✅ **PASS:**
```
0-4s: Dolly in
4-8s: Pan left
8-12s: Tilt up
```

**Movement Vocabulary Check:**
- Query camera-movements skill for valid terms
- Exact match required (case-insensitive)
- Variations must map to standard terms:
  - "push in" → "Dolly In"
  - "track left" → "Dolly Left"
  - "crane rise" → "Crane Up"

### Style Consistency

**Rule:** Aesthetic approach maintained throughout prompt.

**Checks:**
- Style explicitly stated
- Visual elements support stated style
- No contradictory style markers

**Examples:**

❌ **FAIL:**
```
Style: Gritty documentary realism
Lighting: Soft diffusion, warm glow, vintage romance
Finish: Heavy bloom, dreamy halation
```
*Conflict: Documentary realism conflicts with romantic soft aesthetics*

✅ **PASS:**
```
Style: Gritty documentary realism
Lighting: Harsh natural light, high contrast, minimal fill
Finish: Light grain, desaturated, authentic feel
```

### Color Anchor Specification

**Rule:** For long prompts, 3-5 specific colors must be defined as anchors.

**Checks:**
- Minimum 3 colors named
- Maximum 5 colors (avoid too many)
- Colors specific (not "red" but "burgundy red" or "burnt orange")
- Colors repeated in continuity rules if multi-shot

**Examples:**

❌ **FAIL:**
```
Colors: Nice warm colors
```

✅ **PASS:**
```
Color anchors: Amber gold, navy blue, blush pink, cool gray, ivory
```

---

## Path 1 Validations (Text-to-Video)

Specific to direct Veo 3 text-to-video generation.

### 8 Component Completeness

**Rule:** All 8 components from great-prompt-anatomy must be present.

**Checklist:**
1. ✅ Subject
2. ✅ Setting  
3. ✅ Action
4. ✅ Style/Genre
5. ✅ Camera/Composition
6. ✅ Lighting/Mood
7. ✅ Audio
8. ✅ Constraints

**Validation logic:**
```
FOR each component:
  IF component empty OR vague:
    PROMPT-LOCKED
    SUGGEST specific examples
```

### Time/Weather Continuity

**Rule:** Time of day and weather must be consistent throughout unless intentional transition specified.

**Conflict patterns to detect:**

**Time Conflicts:**
- "Golden hour" + "Midnight"
- "Dawn" + "Harsh noon sun"
- "Dusk" + "Morning light"

**Weather Conflicts:**
- "Bright sunny day" + "Heavy rain"
- "Clear skies" + "Overcast diffused light"
- "Fog" + "Crystal clear visibility"

**Lighting Conflicts:**
- "Soft morning light" + "Dramatic sunset colors"
- "Overcast even lighting" + "Long harsh shadows"

**Detection algorithm:**
```
EXTRACT time indicators from Setting and Lighting
IF indicators conflict:
  PROMPT-LOCKED
  IDENTIFY conflicting phrases
  SUGGEST consistent alternative
```

**Examples:**

❌ **FAIL:**
```
Setting: Cobblestone street at golden hour sunset
Lighting: Harsh midday sun creating short shadows
```

✅ **PASS:**
```
Setting: Cobblestone street at golden hour sunset
Lighting: Low-angle warm sun, long soft shadows, golden glow
```

### Spatial Coherence (Long Prompts Only)

**Rule:** Location must define Foreground, Midground, Background structure.

**Checks:**
- FG, MG, BG explicitly stated
- Spatial relationships logical
- Depth layers don't contradict

**Examples:**

❌ **FAIL:**
```
Location: Street scene
```

✅ **PASS:**
```
Location: Urban street
Foreground: Fallen autumn leaves
Midground: Couple walking, holding hands
Background: Blurred cafés and shops, soft bokeh
```

### Audio Appropriateness

**Rule:** Audio must match visual environment and style.

**Checks:**
- Dialogue format correct: `Character: "Text"`
- Ambient sounds logical for setting
- Music style fits mood
- Subtitle constraint specified if needed

**Conflicts to detect:**

❌ **Audio doesn't match setting:**
```
Setting: Quiet library
Audio: Loud street traffic, honking, construction
```

❌ **Music conflicts with mood:**
```
Mood: Somber, melancholic
Audio: Upbeat pop music, energetic
```

✅ **PASS:**
```
Setting: Quiet library
Audio: Pages turning, pencil on paper, distant whispers, clock ticking
Mood: Contemplative
```

---

## Path 2 Validations (Image-to-Video)

Split into Stage A (Imagen) and Stage B (Veo 3 motion).

### Stage A: Imagen Prompt Validations

**Rule:** Static image only - NO motion, NO audio.

**Forbidden elements:**
- Motion verbs: running, flying, walking, jumping, moving, etc.
- Action indicators: "in motion", "blurred movement"
- Audio descriptions: sounds, music, dialogue
- Time-based sequences: "then", "before", "after"

**Detection algorithm:**
```
SCAN prompt for motion keywords
IF motion_verb found:
  PROMPT-LOCKED
  SUGGEST static alternative:
    "running" → "frozen mid-stride"
    "jumping" → "suspended in air"
    "walking" → "standing with forward lean"
```

**Examples:**

❌ **FAIL:**
```
Person running across field, arms swinging, hair flowing in wind
```

✅ **PASS:**
```
Person frozen mid-stride in running pose, arms extended, 
hair suspended showing motion freeze-frame
```

**Technical Specifications Check:**

**Required:**
- Subject description (detailed)
- Context/environment
- Style approach (photographic or artistic)
- Camera framing (shot size, angle - STATIC only)
- Lighting setup

**Imagen-specific:**
- Lens specification if photographic (24-85mm portraits, 60-105mm macro, etc.)
- Quality modifiers (sharp focus, high detail, professional photography)
- Token count under 480

**Token validation:**
```
COUNT tokens in prompt
IF tokens > 480:
  PROMPT-LOCKED
  SUGGEST condensing verbose sections
```

### Stage B: Veo 3 Motion Validations

**Rule:** Motion must be achievable from static starting image.

**Feasibility checks:**

**Camera movement feasibility:**
- Movement must respect image composition
- Can't "pan left" if subject fills right side (no left content)
- Can't "dolly out" if already wide establishing
- Can't "crane up" if already overhead

**Action feasibility:**
- Subject must be capable of action
- Action must fit subject's position/pose in image
- No teleportation (subject can't suddenly be elsewhere)

**Examples:**

❌ **FAIL:**
```
[Image: Close-up portrait of face]
Motion: Dolly out revealing full body walking down street
```
*Can't reveal content not in original composition*

✅ **PASS:**
```
[Image: Close-up portrait of face]
Motion: Slight head turn toward camera, eyes blink, subtle smile
```

**Audio Addition:**
- Audio REQUIRED for video (wasn't in image)
- Audio must match visual style from Stage A
- Ambient appropriate for setting

**Style Matching:**
- Style from Stage A must be maintained
- Color palette consistency
- Lighting approach unchanged
- Aesthetic coherence

**Validation logic:**
```
LOAD Stage A image description
COMPARE with Stage B motion prompt
IF style_mismatch OR impossible_motion:
  PROMPT-LOCKED
  SUGGEST feasible alternative
```

---

## Conflict Detection Examples

### Example 1: Time/Weather Conflict

**Prompt:**
```
Setting: Beach at golden hour, sunset colors
Lighting: Harsh overhead sun, short vertical shadows
```

**Detection:**
```
time_indicators = ["golden hour", "sunset"] → Evening, low sun
lighting_indicators = ["overhead sun", "short shadows"] → Noon, high sun
CONFLICT detected: time_of_day
```

**Output:**
```
⚠️ PROMPT-LOCKED

Conflict: Time of day inconsistency
- Setting indicates: Golden hour/sunset (evening, low sun)
- Lighting indicates: Overhead sun (noon, high sun)

Fix: Match lighting to golden hour
Suggested: "Low-angle warm sun, long soft shadows, orange-pink glow"
```

### Example 2: Camera Movement Compound

**Prompt:**
```
0-5s: Dolly in while panning right and tilting up
```

**Detection:**
```
movement_count = 3 ["Dolly in", "Pan right", "Tilt up"]
IF movement_count > 1:
  CONFLICT: multiple_movements_per_beat
```

**Output:**
```
⚠️ PROMPT-LOCKED

Conflict: Multiple camera movements in single beat
- Beat 0-5s contains: Dolly in + Pan right + Tilt up

Fix: Choose ONE movement per beat
Option A: "0-5s: Dolly in"
Option B: Split into three beats:
  "0-2s: Dolly in"
  "2-4s: Pan right" 
  "4-6s: Tilt up"
```

### Example 3: Style Contradiction

**Prompt:**
```
Style: Gritty documentary realism, raw authentic
Lighting: Soft diffusion, warm romantic glow, dreamy halation
Finish: Heavy bloom, vintage film look, nostalgic atmosphere
```

**Detection:**
```
style_markers = ["gritty", "raw", "authentic", "documentary"]
conflicting_markers = ["soft", "romantic", "dreamy", "nostalgic", "vintage"]
IF style_conflict(style_markers, conflicting_markers):
  CONFLICT: style_inconsistency
```

**Output:**
```
⚠️ PROMPT-LOCKED

Conflict: Style inconsistency
- Declared style: Gritty documentary realism (raw, authentic)
- Lighting/Finish: Romantic soft aesthetic (dreamy, nostalgic)

These approaches conflict. Choose one:

Option A: Maintain documentary realism
- Lighting: Harsh natural light, high contrast
- Finish: Light grain, desaturated, authentic

Option B: Embrace romantic aesthetic
- Style: Romantic drama, soft emotional
- Keep current lighting/finish
```

### Example 4: Imagen Motion Violation

**Prompt (Stage A):**
```
Young woman running through forest, hair flowing behind her,
leaves scattering as she moves quickly through trees
```

**Detection:**
```
motion_verbs = ["running", "flowing", "scattering", "moves"]
IF contains_motion_verb(prompt):
  CONFLICT: motion_in_static_image
```

**Output:**
```
⚠️ IMAGEN PROMPT LOCKED

Error: Motion detected in static image prompt
- Found: "running", "flowing", "scattering", "moves"

Imagen generates STILL IMAGES. Motion not possible.

Fix: Describe static frozen moment
Suggested: "Young woman frozen mid-stride running through 
forest, hair suspended in air showing motion freeze-frame, 
fallen leaves captured mid-scatter around her"

Then add motion in Stage B (Veo 3 image-to-video)
```

### Example 5: Audio Mismatch

**Prompt:**
```
Setting: Quiet meditation room, serene atmosphere
Style: Peaceful, contemplative
Audio: Heavy metal music, distorted guitars, aggressive drumming
```

**Detection:**
```
setting_mood = ["quiet", "serene", "peaceful", "contemplative"]
audio_mood = ["heavy metal", "aggressive"]
IF mood_mismatch(setting_mood, audio_mood):
  CONFLICT: audio_setting_mismatch
```

**Output:**
```
⚠️ PROMPT-LOCKED

Conflict: Audio doesn't match setting/mood
- Setting: Quiet, serene meditation room
- Audio: Heavy metal, aggressive music

Fix: Match audio to setting
Suggested: "Ambient meditation sounds, singing bowl, gentle 
breath, distant wind chimes, peaceful silence"
```

---

## Fix Suggestions

ARCH-V provides actionable fixes for each conflict type.

### Fix Pattern: Missing Component

```
⚠️ PROMPT-LOCKED

Missing: [Component name]

What this means: [Brief explanation]

Example addition: [Specific example relevant to user's prompt]

Would you like me to suggest options for this component?
```

### Fix Pattern: Conflict Resolution

```
⚠️ PROMPT-LOCKED

Conflict: [Conflict type]
- [Specific conflicting element 1]
- [Specific conflicting element 2]

Fix options:
A. [Keep element 1, change element 2]
B. [Keep element 2, change element 1]
C. [Alternative approach that resolves both]

Which direction would you prefer?
```

### Fix Pattern: Feasibility Issue

```
⚠️ PROMPT-LOCKED

Feasibility issue: [What's not possible]

Why: [Technical or logical explanation]

Alternative: [Achievable approach]

Would this work for your vision?
```

---

## Validation Priority Order

ARCH-V validates in this sequence for efficiency:

1. **Mandatory presence** (fastest to check, blocks everything else)
2. **Format validation** (dialogue format, token counts)
3. **Component completeness** (all 8 present)
4. **Internal consistency** (time/weather/style)
5. **Cross-component conflicts** (audio/setting match)
6. **Technical feasibility** (camera movements, motion possibility)
7. **Optimization suggestions** (optional improvements)

If validation fails at any step, ARCH-V stops and provides fixes before continuing.

---

## Advanced Validation: Multi-Shot Sequences

For long prompts with multiple beats/shots:

### Color Anchor Consistency

**Rule:** Color anchors from Lighting block must appear in Continuity Rules.

**Check:**
```
lighting_colors = extract_colors(Lighting_Palette)
continuity_colors = extract_colors(Continuity_Rules)
IF lighting_colors NOT IN continuity_colors:
  WARNING: color_continuity_missing
```

### Temporal Progression

**Rule:** Time-based beats must progress logically.

**Check:**
```
beats = [(0,4), (4,8), (8,12)]
FOR each beat in sequence:
  IF beat[0] != previous_beat[1]:
    CONFLICT: temporal_gap
```

### Camera Movement Progression

**Rule:** Camera movements should build logically (wide → medium → close OR reverse).

**Soft validation (warning, not blocking):**
```
shot_sequence = ["Wide", "Close-up", "Wide"]
IF illogical_progression(shot_sequence):
  SUGGEST: smooth_progression
```

---

## Validation Output Format

### Success Output

```
✅ PROMPT READY

All validations passed:
- 8 components present ✓
- No time/weather conflicts ✓
- Camera movements valid ✓
- Audio appropriate ✓
- Style consistent ✓

[Final prompt displayed]

Token count: [X] / 480 (Imagen) or unlimited (Veo 3)
Estimated quality: High
```

### Locked Output

```
⚠️ PROMPT-LOCKED

Validation failed: [X] issues found

Critical issues (must fix):
1. [Issue 1 with specific fix]
2. [Issue 2 with specific fix]

Warnings (optional improvements):
- [Warning 1 with suggestion]

Shall I help you resolve these?
```

---

## Custom Validation for Art Styles

When imagine skill is loaded with specific art style:

### Science SARU Specific

**Additional checks:**
- Character design: simplified, elastic limbs mentioned
- Linework: rough, loose, variable thickness specified
- Color: flat blocks with gradients
- Movement: fluid, elastic deformation noted

**If missing key elements:**
```
⚠️ STYLE WARNING

Science SARU style selected but missing key elements:
- Character design should mention: elastic limbs, large eyes
- Linework should mention: loose rough, variable thickness
- Consider adding: painterly watercolor texture

Would you like me to enhance the prompt with these elements?
```

This extensible pattern applies to any art style added to imagine skill references.
