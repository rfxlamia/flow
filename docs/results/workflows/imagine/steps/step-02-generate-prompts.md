# Step 02: Generate Imagen Prompts

**Goal:** Create detailed Imagen 3/4 prompts for each key frame.

**Scope:** Prompt generation using selected art style.

**Token Budget:** ~400 tokens

---

## PROMPT GENERATION PROCESS

### 1. For Each Key Frame

Build prompt using Subject-Context-Style framework:

**Layer 1: Subject**
- Who/what is in the frame
- Physical description, clothing, features
- Position and pose

**Layer 2: Context**
- Environment and setting
- Background elements
- Spatial relationships
- Time of day, weather

**Layer 3: Style**
- Art style vocabulary (from reference)
- Technical specifications
- Lighting and color
- Quality modifiers

### 2. Prompt Template by Type

**Photography Prompt:**
```
A photo of [detailed subject], [context/placement], [technical specs: lens, lighting], [mood descriptors], [quality modifiers]
```

**Art Style Prompt (e.g., Science SARU):**
```
[Art style name and descriptors], [character with style-specific features], [environment with style-specific treatment], [atmosphere and mood], [color and lighting approach], [texture and technical quality]
```

**Cinematic Prompt:**
```
[Cinematography term], [scene composition], [subject description], [lighting setup], [color grading], [atmosphere], [quality: shot on X, film stock]
```

---

## EXAMPLE PROMPTS

### Photography Example

**Key Frame:** "Sarah placing jacket on ice"

```
A photo of a woman in her late 30s with dark hair pulled back, wearing a heavy wool coat, kneeling on frozen shoreline placing a worn leather jacket on ice, pale winter dawn light with soft blue shadows, mist rising from ice formations, 50mm lens, natural lighting from low horizon sun, intimate emotional moment, high detail on textures (coat fabric, ice crystals, leather), professional portrait photography, 8K resolution
```

### Science SARU Example

**Key Frame:** "Sarah placing jacket on ice"

```
Science SARU animation style directed by Masaaki Yuasa, digitally-assisted 2D hand-drawn aesthetic. Woman character with simplified design (late 30s), elastic limbs with soft rounded contours, large expressive eyes showing deep longing, dark hair with loose rough linework, heavy wool coat in muted earth tones. Frozen beach environment at golden hour with simplified geometric ice formations, clean vector linework, cool blue-gray palette with warm sunset accents in sky, dramatic long shadows on ice, wet reflective surfaces. Melancholic but tender atmosphere, desaturated base colors with warm light on character's face, complementary cool shadows. Flat color blocks with gradients, painterly watercolor texture on ice, deliberately unfinished aesthetic, bloom lighting effect around low sun, character kneeling in intimate pose holding leather jacket, fluid emotional weight in gesture
```

### Crewdson Hyperrealism Example

**Key Frame:** "Sarah placing jacket on ice"

```
Gregory Crewdson cinematic photography style, staged hyperrealistic scene. Woman in late 30s kneeling on frozen shoreline at dawn, meticulously placed within frozen landscape, holding worn leather jacket with reverent care. Dramatic theatrical lighting with key light from low horizon, fill light creating detail in shadows, practical lights suggesting off-frame presence. Muted color palette with blue-gray frozen tones, single warm accent from distant sunrise. Sharp architectural precision in ice formation arrangement, surreal stillness, uncanny atmosphere of suspended time. Shot on 8x10 large format, extreme depth of field, perfect focus throughout, museum-quality detail, production values of major film set
```

---

## PROMPT CHECKLIST

For each prompt, verify:

- [ ] Subject clearly described in first 50 words
- [ ] Art style vocabulary used consistently
- [ ] Technical specifications included (lens, lighting)
- [ ] Color palette matches visual style guide
- [ ] Mood and atmosphere captured
- [ ] Under 480 tokens
- [ ] No instructive language in negative terms

### Negative Prompt Guidelines

**DO:** Use descriptive terms
- "blurry background, out of focus, oversaturated colors"

**DON'T:** Use instructive terms
- "no blurry background, avoid oversaturation"

---

## ASPECT RATIO SELECTION

| Frame Type | Ratio | Notes |
|------------|-------|-------|
| Wide establishing | 16:9 | Landscape, environment |
| Character portrait | 3:4 | Vertical, intimate |
| Action scene | 16:9 | Cinematic |
| Detail/close-up | 1:1 or 4:3 | Focus on object |
| Social media | 9:16 | Vertical scroll |

---

## GENERATE ALL PROMPTS

For each key frame from Step 01:

```
PROMPT 1: Frame 1a - Frozen beach establishing
==========================================
Art Style: {selected}
Aspect Ratio: 16:9
Purpose: Location establishment

PROMPT:
"{complete prompt text}"

Negative Prompt:
"blurry, low quality, text, watermark, signature"

Technical Settings:
- enhancePrompt: true
- personGeneration: dont_allow
- safetySetting: block_medium_and_above

---

PROMPT 2: Frame 1c - Sarah placing jacket
==========================================
...
```

---

## LOAD NEXT STEP

Execute: `Load step-03-generate-output.md`

---

**Proceed to Step 03 when all prompts are generated.**
