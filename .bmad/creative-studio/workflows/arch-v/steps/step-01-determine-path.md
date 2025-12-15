# Step 01: Template Review & Path Confirmation

**Purpose:** Run template generator, review imagine input, confirm production path.

---

## STEP 0: RUN TEMPLATE GENERATOR

**MANDATORY FIRST ACTION:**

```bash
python {installed_path}/scripts/generate-template.py {active_project_path}
```

**Expected output:** `{active_project_path}/06-arch-v/arch-v-template-{timestamp}.md`

If script fails, check:
- Pipeline state exists at project path
- Imagine output (05-imagine/) has prompts file
- Python environment has yaml module

---

## STEP 1: LOAD AND REVIEW TEMPLATE

Read the generated template file. It contains:

1. **Input Analysis:**
   - Art style (from imagine)
   - Dual keyframe mode detection
   - Total scenes
   - Auto-detected path type

2. **Questions for User:**
   - Q1: Confirm production path
   - Q2: Prompt complexity (short/long)

3. **Scene Sections:**
   - Each scene with keyframe prompts (if dual mode)
   - 8-component checklist per scene
   - Validation status

---

## STEP 2: CONFIRM PATH WITH USER

Based on template analysis, present:

```
Berdasarkan output Imagine:

- Art Style: {art_style}
- Mode: {DUAL KEYFRAME / SINGLE KEYFRAME}
- Total Scenes: {scene_count}

{If dual keyframe:}
Dual Keyframe Mode terdeteksi. Setiap scene memiliki:
- First Frame (komposisi awal)
- Last Frame (komposisi akhir)
- Arch-V akan generate motion prompt untuk interpolasi

Path yang direkomendasikan: IMAGE-TO-VIDEO (Interpolation)

{If single:}
Single keyframe mode. Pilih path:
1. TEXT-TO-VIDEO - Generate video langsung dari text
2. IMAGE-TO-VIDEO - Generate video dari single image

Konfirmasi path? [Y] Ya / [N] Ubah
```

---

## PROMPT TYPE SELECTION

### For Path 1 (Text-to-Video):

```
What type of video prompt?

SHORT PROMPT (for):
- Filler shots, B-roll
- Atmospheric scenes
- Quick establishing shots
- <3 sentences to describe

LONG PROMPT (for):
- Dialogue scenes
- Character continuity
- Multi-beat sequences (>3 beats)
- Complex choreography
```

**Store choice as:** `prompt_type` = "short" OR "long"

### For Path 2 (Image-to-Video):

**Stage A (Imagen):** Always uses imagine workflow patterns

```
For Veo 3 motion, what complexity?

SHORT MOTION (for):
- Simple camera movement
- Atmospheric animation
- Single motion element

LONG MOTION (for):
- Complex choreography
- Multiple action beats
- Character animation with timing
```

**Store choice as:** `motion_type` = "short" OR "long"

---

## CHECK FOR PIPELINE INPUT

### If Pipeline State Available:

1. Read `creative-pipeline-state.yaml`
2. Check if stage 05 (imagine) completed
3. If yes, offer: "Use existing Imagen prompts for Image-to-Video?"
4. If user accepts, load imagine output as starting point

### If Standalone:

Continue with user-provided concept

---

## LOAD APPROPRIATE REFERENCES

Based on choices, prepare to load:

| Choice | Reference to Load |
|--------|------------------|
| Short prompt/motion | `short-prompt-guide.md` |
| Long prompt/motion | `long-prompt-guide.md` |
| Any path | `great-prompt-anatomy.md` (for validation) |
| Camera movement needed | `camera-movements.md` |

**DO NOT load yet - pass to step-02 for on-demand loading**

---

## OUTPUT TO STEP-02

Pass these values:
- `path_type`: text-to-video OR image-to-video
- `prompt_type` OR `motion_type`: short OR long
- `pipeline_input`: boolean - whether using imagine output
- `user_concept`: The video concept/description from user

---

## HANDOFF

When path and type determined, load: `./steps/step-02-build-validate.md`
