# Step 01: Path Determination

**Purpose:** Determine production path and prompt type for Veo 3 prompt creation.

---

## PATH SELECTION

### Ask User

Present these options:

```
Which production path?

1. TEXT-TO-VIDEO (Direct Veo 3)
   - Describe entire video in single prompt
   - Faster workflow
   - Less control over initial composition

2. IMAGE-TO-VIDEO (Imagen -> Veo 3 pipeline)
   - Create perfect still image first
   - Then add motion and animation
   - Maximum control over visual composition
   - Two-step process
```

**Store choice as:** `path_type` = "text-to-video" OR "image-to-video"

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
