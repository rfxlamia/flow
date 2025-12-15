---
name: storyteller
description: Transform abstract/metaphorical narrative into concrete visual story structure
type: creative-pipeline-stage-02
---

# Storyteller Workflow

**Goal:** Transform metaphorical/theatrical narrative from diverse-content-gen into filmable visual scenes with preserved emotional core.

**Your Role:** You are a visual story architect. You bridge the gap between poetic writing and production-ready scene breakdowns.

**Core Principle:** Preserve emotional truth while making content filmable.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** with **smart context engineering**:

- workflow.md loads configuration only (minimal tokens)
- step-01 loads input from diverse-content-gen and extracts emotional core
- step-02 transforms metaphors to visual equivalents
- step-03 generates scene breakdown and creates output files
- References loaded on-demand, never pre-loaded
- Each step is self-aware of its scope and capability

---

## INITIALIZATION

### Configuration Loading

Load config from `{project-root}/.bmad/core/config.yaml` and resolve:

- `user_name`, `communication_language`, `output_folder`
- `date` as system-generated value

### Paths

- `installed_path` = `{project-root}/.bmad/creative-studio/workflows/storyteller`
- `projects_registry` = `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
- `active_project_path` = Read from projects_registry → active_project → path
- `pipeline_state_file` = `{active_project_path}/pipeline-state.yaml`
- `output_path` = `{active_project_path}/02-storyteller/`
- `references_path` = `{installed_path}/references`
- `input_schema` = `{project-root}/.bmad/creative-studio/_state/handoff-schema.yaml`

### Pipeline Context

- **Previous Stage:** 01 (diverse-content-gen)
- **Current Stage:** 02 (storyteller)
- **Next Stage:** 03 (screenwriter)
- **Capability:** Transform metaphorical narrative into filmable visual scenes
- **Scope:** Visual scene breakdown ONLY - does NOT format screenplay
- **Output Format:** Markdown (.md) file with scene-by-scene breakdown
- **Tracking Format:** YAML (.yaml) file with metadata
- **Handoff Schema:** `_state/handoff-schema.yaml` (defines required fields for screenwriter)

---

## INPUT LOADING

### Step 0: Load Input from Previous Stage

**BEFORE executing step-01, you MUST load input from diverse-content-gen:**

1. **Read projects registry:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
2. **Get active project path:** Extract active_project → path
3. **Read pipeline state:** `{active_project_path}/pipeline-state.yaml`
4. **Find diverse-content-gen output:** Extract from stage "01-diverse" → outputs
5. **Load content file:** Read the selected idea from the content markdown in `{active_project_path}/01-diverse/`

**Required input fields (from handoff schema):**
- `content_file` - Path to markdown with selected idea
- `selected_idea_id` - Which idea was chosen
- `emotional_core` - Primary emotion
- `pov` - Point of view
- `setting` - Environment/location
- `tone` - Emotional tone
- `structure_type` - Narrative structure
- `why_this_wins` - Strength analysis
- `metaphorical_content` - Does it need visual translation?

**If any required field is missing:** Stop and inform user that diverse-content-gen output is incomplete.

---

## EXECUTION

Execute steps sequentially:

### Step 01: Extract Emotional Core
Load: `./steps/step-01-extract-emotional-core.md`

Analyzes the selected content and extracts the emotional foundation.

### Step 02: Transform to Visual
Load: `./steps/step-02-transform-to-visual.md`

Converts metaphorical language into filmable visual actions.

### Step 03: Generate Scene Breakdown
Load: `./steps/step-03-generate-scenes.md`

Creates the scene-by-scene breakdown and output files.

### Step 04: Generate Atmospheric Inserts (ENHANCED)
Load: `./steps/step-04-generate-inserts.md`

Creates atmospheric insert shots for texture-based storytelling:
- 4-6 inserts per babak/act
- Categories: decay, intimacy, strain, absence
- XML structure for screenwriter handoff
- 2-4 second duration specifications

**References (load on-demand):**
- `./references/insert-categories.md` - Category definitions
- `./references/texture-progression.md` - Texture consistency framework

---

## OUTPUT CONTRACT

### Content Output (.md file)

**File:** `scenes-{timestamp}.md`

Structured markdown with:
- Source material summary
- Character descriptions
- Scene-by-scene breakdown with filmable actions
- Key visuals for each scene
- Story logic map (metaphor → visual translation)

### Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/storyteller-{timestamp}.yaml`

Required fields for screenwriter (from handoff-schema.yaml):
- `scene_breakdown_file` - Path to scene markdown
- `total_scenes` - Number of scenes
- `characters` - List with descriptions
- `story_logic_map` - Metaphor translations
- `estimated_duration` - Total duration estimate
- `emotional_arc` - Progression through scenes
- `ready_for_next_stage` - Boolean

---

## CONTEXT ENGINEERING PRINCIPLES

### 1. Minimal Token Load
- workflow.md: ~250 tokens (config + routing only)
- Load steps on-demand, one at a time
- Load references only when needed for specific transformation

### 2. Self-Aware Scope
- Know what this workflow CAN do: Transform metaphors to visual scenes
- Know what this workflow CANNOT do: Format screenplay, validate production, generate images
- Clearly communicate scope to user

### 3. Lazy Loading
- Load `visual-vocabulary.md` only when translating complex emotions
- Load `transformation-methodology.md` only for detailed methodology reference
- Default: Transform using embedded knowledge first

### 4. Structured Handoff
- Always create both .md (content) and .yaml (tracking) outputs
- YAML includes all fields required by screenwriter
- Update creative-pipeline-state.yaml upon completion

---

## FILMABILITY RULES

### What Makes a Scene "Filmable"

**FILMABLE:**
- Physical actions (walking, touching, looking, moving objects)
- Observable emotions (tears, shaking, stillness, posture)
- Environmental details (weather, lighting, objects in space)
- Time progression (morning→night, seasons changing)

**NOT FILMABLE:**
- Internal thoughts ("She thinks about him")
- Abstract concepts ("Love fills the room")
- Unvisualizable metaphors ("Her heart is a frozen sea")
- Telling instead of showing ("She is sad")

### Translation Strategy

| Metaphor Type | Visual Approach |
|---------------|-----------------|
| "I am [element]" | Character interacts with that element; element as backdrop |
| "You are my [sacred thing]" | Ritualistic worship-like behaviors; lighting elevates beloved |
| "I am waiting for..." | Same location revisited; objects accumulated/deteriorating |
| "When you left..." | Empty spaces; untouched belongings; contrast flashbacks |

---

## START HERE

1. Load input from diverse-content-gen (Step 0)
2. Verify all required handoff fields are present
3. Load step-01 and begin emotional core extraction
