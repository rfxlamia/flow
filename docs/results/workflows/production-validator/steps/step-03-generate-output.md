# Step 03: Generate Output

**Goal:** Create validated XML with Veo 3 prompts and tracking files.

**Scope:** Prompt generation, file creation, pipeline update.

**Token Budget:** ~400 tokens

---

## VEO 3 PROMPT GENERATION

### Prompt Structure

Build each chunk's prompt using this structure:

```
[Shot + Camera] [Subject description] [Action] [Setting] [Lighting] [Style] [Audio] [Negative prompts]
```

### Component Details

**1. Shot + Camera (first):**
- "Cinematic establishing shot, wide angle"
- "Medium shot, static camera"
- "Close-up, slow dolly forward"

**2. Subject Description (within first 50 words):**
- Character: Full description on first appearance
- Subsequent: Key identifiers for consistency
- Example: "woman (38, dark hair, heavy wool coat)"

**3. Action (what happens):**
- Present tense, active voice
- Specific movements
- Example: "walks slowly toward frozen shoreline"

**4. Setting:**
- Location details
- Environmental elements
- Example: "frozen beach with ice formations, gray sky"

**5. Lighting:**
- Time of day
- Light quality
- Example: "pale winter dawn light, soft shadows"

**6. Style:**
- Visual quality
- Example: "photorealistic, cinematic color grading, high detail"

**7. Audio (Veo 3 supports):**
- Ambient sounds
- Sound effects
- Example: "Audio: wind howling, ice cracking, distant waves"

**8. Negative Prompts:**
- What to avoid
- Example: "negative prompt: no text, no multiple moving objects, no sudden lighting changes"

### Continuation Prompts

For chunks that continue from previous:

**Add prefix:** `[CONTINUATION]`

**Add consistency notes:**
- "same character, same lighting, same environment"
- "maintain {specific element} from previous"

**Example:**
```
[CONTINUATION] Medium shot, static camera, same woman (38, dark hair, heavy wool coat) from previous shot, kneels on ice placing leather jacket, same frozen beach environment, same pale dawn lighting, photorealistic. Audio: fabric rustling, ice groaning. negative prompt: no character drift, maintain lighting consistency
```

---

## OUTPUT FILE CREATION

### File A: Validated Screenplay

**File path:** `{project-root}/.bmad/creative-studio/workflows/production-validator/outputs/validated-{timestamp}.md`

**Content structure:**

```markdown
# Validated Screenplay: [Title]

## Validation Summary

- **Total Scenes:** {count}
- **Total Chunks:** {count}
- **Validation Status:** {PASSED / PASSED_WITH_NOTES / NEEDS_REVISION}
- **Risk Assessment:** {X} LOW, {Y} MEDIUM, {Z} HIGH, {W} CRITICAL
- **Generated:** {timestamp}

## Production Notes

[Any HIGH/CRITICAL risk items and their alternatives]

---

## Validated Scenes

<!-- Scene 1 -->
<validated_scene number="1" original_duration="30s">
  <feasibility_check>
    <risk_score>LOW</risk_score>
    <risky_elements>
      <element risk="NONE">Single subject - optimal for Veo 3</element>
    </risky_elements>
    <safe_for_veo3>true</safe_for_veo3>
  </feasibility_check>

  <chunks>
    <chunk id="1a" duration="8s">
      <shot_type>establishing</shot_type>
      <shot_relationship>new</shot_relationship>
      <camera_movement>Slow dolly forward</camera_movement>
      <action>Wide establishing shot of frozen beach at dawn...</action>
      <veo3_prompt>
Cinematic establishing shot, wide angle, frozen beach with ice formations
silhouetted against pale dawn sky, gray mist over water, slow dolly forward,
winter morning lighting with soft blue tones, photorealistic, high detail.
Audio: wind howling, ice cracking, distant waves.
negative prompt: no text, no multiple moving objects
      </veo3_prompt>
      <continuation_setup>Camera ends focused on shoreline edge</continuation_setup>
    </chunk>

    <chunk id="1b" duration="8s" continues_from="1a">
      <shot_type>continuation</shot_type>
      <shot_relationship>continues_from_1a</shot_relationship>
      <camera_movement>Static (subject enters)</camera_movement>
      <action>Woman (Sarah) enters frame from left...</action>
      <veo3_prompt>
[CONTINUATION] Medium shot, static camera, woman (38, dark hair pulled back,
heavy wool coat, weathered but elegant) enters from left walking slowly,
same frozen beach environment, same pale dawn lighting, footsteps crunch on ice,
photorealistic. Audio: footsteps on ice, wind.
negative prompt: no character drift, maintain lighting
      </veo3_prompt>
      <continuation_setup>Sarah reaches edge of ice</continuation_setup>
    </chunk>

    [Continue for all chunks...]
  </chunks>

  <editing_notes>
    - Chunks 1a-1d flow continuously
    - Smooth cuts between chunks (maintain spatial continuity)
    - Character consistency: Repeat "38, dark hair, heavy wool coat"
  </editing_notes>
</validated_scene>

---

<!-- Scene 2 -->
[Continue for all scenes...]

---

## Key Frames for Image Generation

| Chunk ID | Frame Description | Use For |
|----------|------------------|---------|
| 1a | Frozen beach wide shot | Establishing |
| 1c | Sarah placing jacket on ice | Emotional beat |
| 3b | Shrine corner close-up | Character detail |
[List recommended key frames]

## Visual Style Guide

- **Color Palette:** Muted blues and grays, occasional warm amber
- **Lighting:** Soft, diffused, winter morning quality
- **Texture:** Ice formations, worn fabrics, weathered surfaces
- **Mood:** Melancholic, contemplative, lonely beauty

---

*Validated by Production Validator Workflow*
*Ready for: Imagine (image generation)*
```

### File B: Tracking YAML

**File path:** `{project-root}/.bmad/creative-studio/_state/validator-{timestamp}.yaml`

**Content (matching handoff-schema.yaml):**

```yaml
---
# Creative Pipeline State - production-validator
workflow_stage: 04-production-validator
next_stage: 05-imagine
status: completed
created_at: "{timestamp}"
user_name: "{user_name}"

# Input Reference
input_from: "03-screenwriter"
input_tracking_file: "_state/screenwriter-{previous_timestamp}.yaml"

# Output Reference
validated_screenplay_file: "workflows/production-validator/outputs/validated-{timestamp}.md"

# === HANDOFF METADATA FOR IMAGINE ===
# Reference: _state/handoff-schema.yaml → production_validator_to_imagine

# Validation results
validation_status: "passed"  # or "passed_with_notes", "needs_revision"
risk_summary:
  low: {count}
  medium: {count}
  high: {count}
  critical: {count}

# Chunk data
total_chunks: {number}
chunks_per_scene:
  scene_1: 4
  scene_2: 3
  # ...

# Production notes (issues found and alternatives)
production_notes:
  - scene: 3
    issue: "Multiple camera movements"
    resolution: "Split into separate chunks"
  # ...

# Key frames for image generation
key_frames:
  - chunk_id: "1a"
    description: "Frozen beach wide establishing shot"
    purpose: "Location establishment"
  - chunk_id: "1c"
    description: "Sarah placing jacket on ice"
    purpose: "Emotional beat"
  # ...

# Visual style guide
visual_style_guide:
  color_palette: "Muted blues and grays with warm amber accents"
  lighting: "Soft diffused winter morning"
  textures: ["ice formations", "worn fabrics", "weathered surfaces"]
  mood: "Melancholic, contemplative"

# Pipeline control
ready_for_next_stage: true
veo3_prompts_generated: true
continuity_tags_added: true

---
```

---

## UPDATE PIPELINE STATE

Use the **Edit** tool to update `creative-pipeline-state.yaml`:

**Update stage 04:**
```yaml
  - stage: 04-production-validator
    status: completed
    input_from: "03-screenwriter"
    output_file: "workflows/production-validator/outputs/validated-{timestamp}.md"
    tracking_file: "_state/validator-{timestamp}.yaml"
    completed_at: "{timestamp}"
```

**Update stage 05:**
```yaml
  - stage: 05-imagine
    status: ready
    input_from: "04-production-validator"
    waiting_for_user: false
```

**Update Quick Access:**
```yaml
current_stage: "05-imagine"
last_output: "workflows/production-validator/outputs/validated-{timestamp}.md"
next_stage_ready: true
```

---

## WORKFLOW COMPLETION

### Summary for User

```
✅ Production Validation Complete!

📄 Validated Screenplay: {file_path}
🎬 Total Scenes: {count}
📦 Total Chunks: {chunk_count} (all ≤8 seconds)
⚠️ Risk Assessment: {summary}

VALIDATION RESULTS:
- Veo 3 feasibility checked for all scenes
- Scenes chunked into 8-second segments
- Veo 3 prompts generated for each chunk
- Continuity tags added for seamless editing
- Key frames identified for image generation

NEXT STEP OPTIONS:

1. **Continue to Imagine Workflow**
   Generate images from key frames using Imagen

2. **Review Validation**
   Check specific scenes or production notes

3. **Request Revisions**
   Modify risky elements before proceeding

4. **Exit Pipeline**
   Save progress and exit

What would you like to do?
```

---

## COMPLETION CHECKLIST

Before marking complete:

- [ ] Validated screenplay file written
- [ ] All scenes have feasibility checks
- [ ] All chunks ≤8 seconds
- [ ] All chunks have Veo 3 prompts
- [ ] Continuity tags assigned
- [ ] Key frames identified
- [ ] Tracking YAML created
- [ ] Pipeline state updated

---

**Production-validator workflow complete. Ready for imagine or user exit.**
