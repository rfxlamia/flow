# Step 03: Generate Output

**Purpose:** Create validated prompts and complete the workflow.

---

## OUTPUT GENERATION

### Path 1: Text-to-Video Output

Generate single markdown file with:

```markdown
# Veo 3 Text-to-Video Prompt

## Validated Prompt

[Final prompt text with all 8 components]

## Validation Checklist

- [x] Subject: [description]
- [x] Setting: [description]
- [x] Action: [description]
- [x] Style/Genre: [description]
- [x] Camera/Composition: [description]
- [x] Lighting/Mood: [description]
- [x] Audio: [description]
- [x] Constraints: [description]

## Production Notes

- Path: Text-to-Video (Direct Veo 3)
- Prompt Type: [short/long]
- Conflicts Resolved: [list or "None"]

Ready to use in Veo 3!
```

### Path 2: Image-to-Video Output

Generate markdown with TWO prompts:

```markdown
# Image-to-Video Pipeline Prompts

## Stage A: Imagen 3/4 Prompt (Still Image)

[Imagen prompt - visual components only]

### Visual Components
- Subject: [description]
- Setting: [description]
- Style: [description]
- Camera (Static): [description]
- Lighting: [description]
- Constraints: [description]

Generate this image in Imagen 3/4 first.

---

## Stage B: Veo 3 Motion Prompt

[Veo 3 prompt referencing the image]

### Motion Components
- Action: [description]
- Camera Movement: [description]
- Audio: [description]

Use this prompt in Veo 3 with your generated image!

## Production Notes

- Path: Image-to-Video (Imagen -> Veo 3)
- Motion Type: [short/long]
- Conflicts Resolved: [list or "None"]
```

---

## FILE CREATION

### Content File

**Use Edit tool to create:**

```
File: outputs/arch-v-prompts-{timestamp}.md
Content: [Generated prompt markdown above]
```

**Replace {timestamp}** with current date-time: YYYYMMDD-HHMMSS

### Tracking File

**Use Edit tool to create:**

```yaml
File: {project-root}/.bmad/creative-studio/_state/arch-v-{timestamp}.yaml
Content:
---
stage: 06
workflow: arch-v
timestamp: "{ISO timestamp}"
status: completed

path_used: "{text-to-video OR image-to-video}"
prompt_type: "{short OR long}"
validation_status: "passed"

output_files:
  prompts: "workflows/arch-v/outputs/arch-v-prompts-{timestamp}.md"

conflicts_resolved:
  - "{conflict 1}" # or empty array if none

components_validated:
  subject: true
  setting: true
  action: true
  style: true
  camera: true
  lighting: true
  audio: true
  constraints: true
```

---

## UPDATE PIPELINE STATE

**Edit `creative-pipeline-state.yaml`:**

Find the stages section and update stage 06:

```yaml
stage_06:
  workflow: arch-v
  status: completed
  timestamp: "{ISO timestamp}"
  tracking_file: "_state/arch-v-{timestamp}.yaml"
  output_file: "workflows/arch-v/outputs/arch-v-prompts-{timestamp}.md"
```

---

## COMPLETION MESSAGE

Present to user:

### For Path 1 (Text-to-Video):

```
PROMPT READY

Your Veo 3 text-to-video prompt has been validated and saved.

File: arch-v-prompts-{timestamp}.md

Ready to use in Veo 3!
```

### For Path 2 (Image-to-Video):

```
PIPELINE PROMPTS READY

Stage A: Imagen 3/4 prompt for still image
Stage B: Veo 3 motion prompt for animation

File: arch-v-prompts-{timestamp}.md

1. Generate image with Stage A prompt in Imagen 3/4
2. Use Stage B prompt in Veo 3 with your image

Happy creating!
```

---

## WORKFLOW COMPLETE

arch-v workflow finished. No handoff to next stage.

User proceeds to external Veo 3 / Imagen tools with generated prompts.
