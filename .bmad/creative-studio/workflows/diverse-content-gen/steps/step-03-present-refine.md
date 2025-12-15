# Step 03: Present & Refine

**Goal:** Present generated content to user, handle selection, create output files.

**Scope:** User interaction, file creation, pipeline handoff.

**Token Budget:** ~300 tokens (presentation + file ops)

---

## PRESENTATION FORMAT

Present generated candidates in readable format with clear structure:

### Format Template

```markdown
# Diverse Content Generation Results

Generated using Verbalized Sampling (VS) technique
Diversity Score: {diversity_score}× (baseline: 1.0, excellent: 2.1)

---

## Candidate 1: {Brief Title}

**Diversity Markers:** {POV variation, tone, structure}
**Probability:** {probability score}

{Full generated content}

---

## Candidate 2: {Brief Title}

...

---

## Selection

Which candidate resonates most with your vision?
- Enter number (1-5) to select
- Enter "more" for additional variations
- Enter "refine [number]" to improve specific candidate
- Enter "combine [numbers]" to merge elements
```

---

## USER INTERACTION

### Handle User Selection

**User enters number (1-5):**
1. Mark selected candidate
2. Extract emotional core / key themes
3. Proceed to file creation

**User says "more":**
1. Run step-02 again with same parameters
2. Generate 5 new variations
3. Present alongside previous (total 10)

**User says "refine [N]":**
1. Load `references/advanced-techniques.md` (VS-Multi section)
2. Take selected candidate as seed
3. Generate refined variations
4. Present refined options

**User says "combine [N] and [M]":**
1. Extract key elements from both
2. Create hybrid prompt
3. Generate new variation merging elements

---

## OUTPUT FILE CREATION

### 1. Content Output (.md file)

**File:** `/diverse-content-gen-{timestamp}.md`

Use format from example: `@creative-studio/example/diverse-narrative-ideas.md`

**Structure:**
```markdown
# {Content Title}

## Original Request

{User's original request}

---

## Diversity Dimensions Used

| Dimension | Variations |
|-----------|-----------|
| POV | {variations used} |
| Setting | {variations used} |
| Tone | {variations used} |
| Structure | {variations used} |

---

# IDEA 1: {Title}

### Approach
**POV:** ...
**Setting:** ...
**Tone:** ...
**Structure:** ...

### Content

{Full generated content}

---

### 🏆 WHY THIS IDEA WINS

| Strength | Explanation |
|----------|-------------|
| {aspect} | {reason} |

---

# IDEA 2: ...

---

## USER SELECTION

**Selected:** Idea {N}

**Why Selected:** {user's reasoning if provided}

**Next Step:** Ready for storyteller workflow (visual scene development)

---

*Generated using Verbalized Sampling (VS) methodology*
*Diversity Score: {score}×*
```

### 2. Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/content-gen-{timestamp}.yaml`

**Timestamp Format:** Use ISO8601 format: `YYYY-MM-DDTHH-MM-SSZ` (replace colons with hyphens for filename safety)

**IMPORTANT:** This YAML must match the handoff schema. Reference: `_state/handoff-schema.yaml`

```yaml
---
# Creative Pipeline State - diverse-content-gen
workflow_stage: 01-diverse-content-gen
next_stage: 02-storyteller
status: completed
created_at: "{timestamp}"  # ISO8601 format
user_name: "{user_name}"

# VS Execution Data
vs_parameters:
  k: 5
  temperature: 0.8
  threshold: 0.10
  technique: "vs-basic"

# Generated Content Summary
candidates_generated: 5
diversity_score: 1.8
content_type: "story-concept"

# User Selection
selected_idea_id: 3  # Which idea user selected (1-5)
selected_idea_title: "{title of selected idea}"

# === HANDOFF METADATA FOR STORYTELLER ===
# ALL fields below are REQUIRED by storyteller workflow
# Reference: _state/handoff-schema.yaml → diverse_content_gen_to_storyteller

# Content identification
content_file: "workflows/diverse-content-gen//content-{timestamp}.md"
selected_content_section: "IDEA {N}"

# Emotional & tonal data (REQUIRED for storyteller)
emotional_core: "{primary emotion - e.g., longing, devotion, grief}"
pov: "{first_person | second_person | third_person | interlocutor_absent}"
setting: "{environment description - e.g., coastal, urban, abstract}"
tone: "{vulnerable_raw | poetic_mythic | theatrical_absurd | nostalgic_epistolary | cinematic}"
structure_type: "{linear_monolog | letter | parallel_scenes | extended_metaphor | one_sided_dialog}"

# Analysis data
why_this_wins: "{strength analysis - what makes this idea compelling}"
diversity_markers: "{POV: X, Setting: Y, Tone: Z}"

# Pipeline control
metaphorical_content: true  # Does content contain metaphors needing visual translation?
target_duration: "5-10min"
ready_for_next_stage: true

---
```

### How to Extract Handoff Fields

When user selects an idea, extract these fields from the generated content:

1. **emotional_core:** Read the content and identify the PRIMARY emotion (one word or short phrase)
2. **pov:** Check how the narrative is written (I/me = first_person, you = second_person, etc.)
3. **setting:** Identify where the story takes place
4. **tone:** Match to one of the enum values based on writing style
5. **structure_type:** Identify the narrative structure used
6. **why_this_wins:** Copy from the "WHY THIS IDEA WINS" section in the content

### 3. Update Pipeline State

**File:** `{project-root}/.bmad/creative-studio/_state/creative-pipeline-state.yaml`

**IMPORTANT:** You MUST update this file for pipeline continuity. Follow these exact steps:

---

## FILE OPERATIONS

Execute these file operations IN ORDER. Each step uses Claude's tools directly.

### Step A: Write Content File

Use the **Write** tool to create the content markdown file:

**File path:** `{project-root}/.bmad/creative-studio/workflows/diverse-content-gen//content-{timestamp}.md`

**Content:** The formatted markdown with all generated ideas and user selection (format shown above)

---

### Step B: Write Tracking File

Use the **Write** tool to create the tracking YAML:

**File path:** `{project-root}/.bmad/creative-studio/_state/content-gen-{timestamp}.yaml`

**Content:** The YAML structure shown above with ALL handoff fields populated

---

### Step C: Update Pipeline State

**CRITICAL:** Update BOTH the project-specific pipeline state AND the projects registry.

#### C1: Update Project Pipeline State

Use the **Edit** tool to update the per-project pipeline state file.

**Step 1:** Read projects registry to get active project path
**File:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`

**Step 2:** Edit the project's pipeline state file
**File:** `{active_project_path}/pipeline-state.yaml`

**Find this text (old_string):**
```yaml
current_stage: 0
last_updated: "{old_timestamp}"
```

**Replace with (new_string):**
```yaml
current_stage: 1
last_updated: "{timestamp}"
```

**THEN find this text (old_string):**
```yaml
  "01-diverse":
    status: "pending"
    outputs: []
    output_location: "/01-diverse/"
```

**Replace with (new_string):**
```yaml
  "01-diverse":
    status: "completed"
    completed_at: "{timestamp}"
    outputs: ["diverse-content-gen-{timestamp}.md"]
    output_location: "/01-diverse/"
```

**THEN find this text (old_string):**
```yaml
  "02-storyteller":
    status: "pending"
    outputs: []
    output_location: "/02-storyteller/"
    input_from: "01-diverse"
```

**Replace with (new_string):**
```yaml
  "02-storyteller":
    status: "ready"
    outputs: []
    output_location: "/02-storyteller/"
    input_from: "01-diverse"
```

**THEN find this text (old_string):**
```yaml
# Quick Access
next_stage_ready: false
next_stage: "01-diverse"
last_output: null
```

**Replace with (new_string):**
```yaml
# Quick Access
next_stage_ready: true
next_stage: "02-storyteller"
last_output: "/01-diverse/diverse-content-gen-{timestamp}.md"
```

#### C2: Update Projects Registry

Use the **Edit** tool to update the registry.

**File:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`

**Find the active project entry and update:**

**Find this text (old_string):**
```yaml
    current_stage: 0
    stages_completed: []
```

**Replace with (new_string):**
```yaml
    current_stage: 1
    stages_completed: ["01-diverse"]
```

---

### Step D: Verify Updates

After all edits, read the pipeline state file to confirm updates were applied correctly

---

## WORKFLOW COMPLETION

### Summary for User

```
✅ Diverse Content Generation Complete!

📄 Content File: {file_path}
📊 Diversity Score: {score}× improvement
🎯 Selected: Idea {N} - "{title}"

NEXT STEP OPTIONS:

1. **Continue to Storyteller Workflow**
   Transform your selected metaphorical narrative into filmable visual scenes

2. **Generate More Variations**
   Create additional diverse ideas with different dimensions

3. **Refine Selection**
   Improve the selected idea with VS-Multi technique

4. **Exit Pipeline**
   Save current progress and exit

What would you like to do?
```

---

## HANDOFF INSTRUCTIONS

### If User Selects "Continue to Storyteller"

```
Great! I'll prepare your selected content for the storyteller workflow.

The storyteller will:
- Extract the emotional core from your selected idea
- Transform metaphorical language into filmable visual actions
- Create scene-by-scene breakdown
- Prepare for screenplay formatting

Loading storyteller workflow...

[Load: {project-root}/.bmad/creative-studio/workflows/storyteller/workflow.md]
```

### If User Exits

```
Progress saved!

📁 Your content: {content_file}
📊 Pipeline state: Saved to creative-pipeline-state.yaml

You can resume anytime by:
1. Opening the storyteller workflow directly
2. Or re-running diverse-content-gen for new variations

All files are preserved and ready for next session.
```

---

## COMPLETION

Update frontmatter:
```yaml
---
current_step: 3
steps_completed: [1, 2, 3]
workflow_status: completed
files_created: 2
pipeline_state_updated: true
ready_for_handoff: true
---
```

**Workflow complete. Ready for next stage or user exit.**
