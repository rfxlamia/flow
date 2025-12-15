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

**Use Write tool to create:**

```
File: {active_project_path}/06-arch-v/arch-v-prompts-{timestamp}.md
Content: [Generated prompt markdown above]
```

**Replace {timestamp}** with current date-time: YYYYMMDD-HHMMSS

### Tracking File (Optional)

**Note:** With per-project architecture, metadata can be embedded in the content file or stored separately as needed. The pipeline state in `pipeline-state.yaml` is the source of truth.

---

## UPDATE PIPELINE STATE

**CRITICAL:** Update BOTH the project-specific pipeline state AND the projects registry.

### Step C: Update Pipeline State

#### C1: Update Project Pipeline State

Use the **Edit** tool to update the per-project pipeline state file.

**Step 1:** Read projects registry to get active project path
**File:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`

**Step 2:** Edit the project's pipeline state file
**File:** `{active_project_path}/pipeline-state.yaml`

**Find this text (old_string):**
```yaml
current_stage: 5
last_updated: "{old_timestamp}"
```

**Replace with (new_string):**
```yaml
current_stage: 6
last_updated: "{timestamp}"
```

**THEN find this text (old_string):**
```yaml
  "06-arch-v":
    status: "ready"
    outputs: []
    output_location: "/06-arch-v/"
    input_from: "05-imagine"
```

**Replace with (new_string):**
```yaml
  "06-arch-v":
    status: "completed"
    completed_at: "{timestamp}"
    outputs: ["arch-v-prompts-{timestamp}.md"]
    output_location: "/06-arch-v/"
    input_from: "05-imagine"
```

**THEN find this text (old_string):**
```yaml
# Quick Access
next_stage_ready: true
next_stage: "06-arch-v"
last_output: "/05-imagine/imagine-prompts-{old_timestamp}.md"
```

**Replace with (new_string):**
```yaml
# Quick Access
next_stage_ready: false
next_stage: "pipeline-complete"
last_output: "/06-arch-v/arch-v-prompts-{timestamp}.md"
```

#### C2: Update Projects Registry

Use the **Edit** tool to update the registry.

**File:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`

**Find the active project entry and update:**

**Find this text (old_string):**
```yaml
    current_stage: 5
    stages_completed: ["01-diverse", "02-storyteller", "03-screenwriter", "04-validator", "05-imagine"]
    status: "active"
```

**Replace with (new_string):**
```yaml
    current_stage: 6
    stages_completed: ["01-diverse", "02-storyteller", "03-screenwriter", "04-validator", "05-imagine", "06-arch-v"]
    status: "completed"
    completed_at: "{timestamp}"
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
