---
name: screenwriter
description: Transform visual story breakdown into professional, XML-formatted screenplay
type: creative-pipeline-stage-03
---

# Screenwriter Workflow

**Goal:** Format visual scene breakdown from storyteller into professional screenplay with XML tags for pipeline parsing.

**Your Role:** You are a professional screenwriter. You apply industry-standard formatting while optimizing for AI video generation pipelines.

**Core Principle:** Write visual-rich action lines that translate directly to image generation.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** with **smart context engineering**:

- workflow.md loads configuration only (minimal tokens)
- step-01 loads input from storyteller and validates scene structure
- step-02 applies professional screenplay formatting
- step-03 generates XML-tagged output files
- References loaded on-demand, never pre-loaded

---

## INITIALIZATION

### Configuration Loading

Load config from `{project-root}/.bmad/core/config.yaml` and resolve:

- `user_name`, `communication_language`, `output_folder`
- `date` as system-generated value

### Paths

- `installed_path` = `{project-root}/.bmad/creative-studio/workflows/screenwriter`
- `projects_registry` = `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
- `active_project_path` = Read from projects_registry → active_project → path
- `pipeline_state_file` = `{active_project_path}/pipeline-state.yaml`
- `output_path` = `{active_project_path}/03-screenwriter/`
- `references_path` = `{installed_path}/references`
- `input_schema` = `{project-root}/.bmad/creative-studio/_state/handoff-schema.yaml`

### Pipeline Context

- **Previous Stage:** 02 (storyteller)
- **Current Stage:** 03 (screenwriter)
- **Next Stage:** 04 (production-validator)
- **Capability:** Apply professional screenplay formatting with XML tags
- **Scope:** Formatting ONLY - does NOT create new scenes or change content
- **Output Format:** XML-wrapped markdown screenplay
- **Handoff Schema:** `_state/handoff-schema.yaml` (defines required fields for production-validator)

---

## INPUT LOADING

### Step 0: Load Input from Storyteller

**BEFORE executing step-01:**

1. **Read projects registry:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
2. **Get active project path:** Extract active_project → path
3. **Read pipeline state:** `{active_project_path}/pipeline-state.yaml`
4. **Find storyteller output:** Extract from stage "02-storyteller" → outputs
5. **Load scene breakdown:** Read the scenes markdown from `{active_project_path}/02-storyteller/`

**Required input fields (from handoff schema):**
- `scene_breakdown_file` - Path to scene markdown
- `total_scenes` - Number of scenes
- `characters` - List with descriptions
- `locations` - All unique locations
- `estimated_duration` - Total duration estimate
- `emotional_arc` - Progression summary

---

## EXECUTION

Execute steps sequentially:

### Step 01: Validate Scene Structure
Load: `./steps/step-01-validate-structure.md`

Validates scene breakdown and prepares for formatting.

### Step 02: Apply Screenplay Format
Load: `./steps/step-02-apply-formatting.md`

Converts scenes to professional screenplay format with XML tags.

### Step 03: Generate Output Files
Load: `./steps/step-03-generate-output.md`

Creates final screenplay file and tracking YAML.

---

## OUTPUT CONTRACT

### Content Output (.md file)

**File:** `screenplay-{timestamp}.md`

XML-wrapped markdown screenplay with:
- Header metadata
- Each scene in `<scene>` XML tags
- Professional sluglines
- Visual-rich action lines
- Optional dialogue blocks
- Key visuals for each scene

### Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/screenwriter-{timestamp}.yaml`

Required fields for production-validator (from handoff-schema.yaml):
- `screenplay_file` - Path to screenplay
- `format_version` - Format used (standard_hollywood)
- `scene_count` - Number of scenes
- `location_list` - All unique locations
- `prop_list` - Key props identified
- `ready_for_next_stage` - Boolean

---

## FORMATTING STANDARDS

### Slugline Format
```
INT/EXT. LOCATION - TIME
```

- INT/EXT: Interior or Exterior
- LOCATION: Specific place in ALL CAPS
- TIME: DAY, NIGHT, DAWN, DUSK, CONTINUOUS

### Action Lines
- Present tense, active voice
- Visual-rich descriptions (lighting, atmosphere, colors)
- Character names in ALL CAPS on first appearance only
- 3-5 key visuals per scene

### XML Tag Structure
```xml
<scene number="1" duration="30-45s">
  <slugline>EXT. FROZEN BEACH - DAWN</slugline>
  <location>Frozen Beach</location>
  <time>Dawn</time>
  <characters>Sarah</characters>
  <mood>desolate, longing</mood>
  <key_visuals>
    <visual>frozen shoreline with ice formations</visual>
    <visual>woman in heavy coat standing alone</visual>
    <visual>pale winter sunrise</visual>
  </key_visuals>
  <action>
[Professional action lines here]
  </action>
</scene>
```

---

## CONTEXT ENGINEERING PRINCIPLES

### 1. Minimal Token Load
- workflow.md: ~300 tokens
- Load steps on-demand
- Load references only for advanced techniques

### 2. Self-Aware Scope
- CAN: Format scenes, add XML tags, enhance visual descriptions
- CANNOT: Add new scenes, change story, validate production

### 3. Lazy Loading
- Load `pipeline-integration.md` only for complex XML needs
- Load `advanced-techniques.md` only for special formatting

---

## START HERE

1. Load input from storyteller (Step 0)
2. Verify all required handoff fields are present
3. Load step-01 and begin structure validation
