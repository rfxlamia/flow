---
name: arch-v
description: Video production workflow orchestrator for Veo 3. Guides through two paths - Text-to-Video OR Image-to-Video pipeline.
type: creative-pipeline-stage-06
---

# ARCH-V: Video Production Orchestrator

**Goal:** Create production-ready Veo 3 video prompts through guided workflow.

**Your Role:** You are a video production architect. You guide users through creating professional video prompts with validation.

**Core Principle:** Two paths - Text-to-Video (direct) OR Image-to-Video (Imagen first). Load reference skills on-demand only.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** with **smart context engineering**:

- workflow.md loads configuration only (minimal tokens)
- **Step 0: Run template generator script** (detects dual keyframe mode)
- step-01 reviews template, confirms path with user
- step-02 guides component building with validation
- step-03 outputs final validated prompts
- Utility references loaded on-demand based on path

### Template-First Approach

**MANDATORY:** Before starting, run the template generator:

```bash
python {installed_path}/scripts/generate-template.py {active_project_path}
```

This script:
1. Reads imagine output from 05-imagine/
2. **Automatically detects** dual keyframe mode
3. Extracts art style, scene count, keyframe prompts
4. Prepares structured template with Veo 3 prompt sections
5. Outputs to `{active_project_path}/06-arch-v/arch-v-template-{timestamp}.md`

**Why this approach:**
- Hemat token - script parses imagine output efficiently
- Dual keyframe aware - automatically structures for interpolation mode
- Structured output - ensures all 8 components are tracked

---

## INITIALIZATION

### Configuration Loading

Load config from `{project-root}/.bmad/core/config.yaml` and resolve:

- `user_name`, `communication_language`, `output_folder`
- `date` as system-generated value

### Paths

- `installed_path` = `{project-root}/.bmad/creative-studio/workflows/arch-v`
- `projects_registry` = `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
- `active_project_path` = Read from projects_registry → active_project → path
- `pipeline_state_file` = `{active_project_path}/pipeline-state.yaml`
- `output_path` = `{active_project_path}/06-arch-v/`
- `references_path` = `{installed_path}/references`

### Pipeline Context

- **Previous Stage:** 05 (imagine) OR standalone invocation
- **Current Stage:** 06 (arch-v)
- **Next Stage:** null (outputs to Veo 3 externally)
- **Capability:** Generate validated Veo 3 video prompts
- **Scope:** Video prompt generation and validation
- **Output Format:** Markdown with validated prompts

---

## TWO PRODUCTION PATHS

### Path 1: Text-to-Video (Direct Veo 3)
**When to use:** User has clear vision for entire video including motion, audio
**Output:** Single Veo 3 prompt ready for text-to-video generation

### Path 2: Image-to-Video (Imagen -> Veo 3)
**When to use:** User wants precise control over starting visual before adding motion
**Output:** Two prompts - Imagen 3/4 prompt + Veo 3 image-to-video prompt

### Path 2+: Dual Keyframe Interpolation (ENHANCED)
**When to use:** Imagine workflow used dual keyframe mode (first + last frame)
**Output:** Veo 3 prompt with start/end image references

**Dual Keyframe Mode:**
- Imagine generates FIRST FRAME (opening composition)
- Imagine generates LAST FRAME (closing composition)
- Arch-V generates MOTION PROMPT describing transition
- Veo 3 interpolates between both frames

**Motion Prompt Structure for Interpolation:**
```
[Describe motion from first frame to last frame].
Camera: [movement type or static].
Audio: [character] says: "[dialogue]" / [ambient: description]
Duration: 8 seconds, smooth interpolation.
Start image: first_frame_{scene_id}.png
End image: last_frame_{scene_id}.png
(no subtitles)
```

---

## REFERENCE UTILITIES (Load On-Demand)

| Utility | Reference File | Load When |
|---------|---------------|-----------|
| Camera Movements | `camera-movements.md` | Camera movement specified |
| Prompt Anatomy | `great-prompt-anatomy.md` | Validating 8 components |
| Short Prompt | `short-prompt-guide.md` | User chooses SHORT format |
| Long Prompt | `long-prompt-guide.md` | User chooses LONG format |

**Default:** Load NO references initially. Load specific reference when needed.

---

## INPUT MODES

### Mode A: Pipeline Input (from Imagine)

1. **Read projects registry:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
2. **Get active project path:** Extract active_project → path
3. **Read pipeline state:** `{active_project_path}/pipeline-state.yaml`
4. **Find imagine output:** Extract from stage "05-imagine" → outputs
5. **Load prompts data:** Get generated Imagen prompts from `{active_project_path}/05-imagine/` for image-to-video workflow
6. **Use as starting point:** Build motion prompts from still images

### Mode B: Standalone Invocation (Text-to-Video)

**CRITICAL:** Standalone mode reads from **04-validator**, NOT 03-screenwriter.

1. **Check for imagine output first** - if exists, use Mode A
2. **Fallback to validated screenplay:** `{active_project_path}/04-validator/validated-*.md`
3. **DO NOT read from 03-screenwriter** - that content has not been validated/chunked
4. **Determine path:** Text-to-Video (no starting images)
5. **Guide through component building**

**Why 04-validator is required:**
- Contains 8-second chunks optimized for Veo 3
- Has feasibility validation for camera movements
- Provides key frame markers for timing
- Includes continuity tags for consistency

---

## EXECUTION

Execute steps sequentially:

### Step 01: Path Determination
Load: `./steps/step-01-determine-path.md`

Asks user to choose production path and prompt type (short/long).

### Step 02: Component Building & Validation
Load: `./steps/step-02-build-validate.md`

Guides through mandatory components with conflict checking.

### Step 03: Generate Output
Load: `./steps/step-03-generate-output.md`

Creates validated prompts and completes workflow.

---

## OUTPUT CONTRACT

### Content Output (.md file)

**File:** `arch-v-prompts-{timestamp}.md`

Markdown with:
- Final validated Veo 3 prompt(s)
- Path used (text-to-video or image-to-video)
- Validation checklist result
- Production notes

### Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/arch-v-{timestamp}.yaml`

Fields:
- `prompts_file` - Path to prompts
- `path_used` - text-to-video OR image-to-video
- `prompt_type` - short OR long
- `validation_status` - passed/locked
- `conflicts_resolved` - List of any resolved issues

---

## VALIDATION RULES (Summary)

### Mandatory Components (8 total)
1. Subject - who/what in shot
2. Setting - where/when
3. Action - what's happening
4. Style/Genre - aesthetic
5. Camera/Composition - shot size, angle, movement
6. Lighting/Mood - light sources, tone
7. Audio - dialogue, ambience, music
8. Constraints - prohibitions, exact requirements

### Conflict Types
- **Time/Weather:** "Golden hour" vs "midnight"
- **Camera Movement:** Multiple movements per beat
- **Spatial Coherence:** Missing FG/MG/BG for long prompts

**For detailed rules:** Load `great-prompt-anatomy.md` reference

---

## CONTEXT ENGINEERING PRINCIPLES

### 1. Minimal Token Load
- workflow.md: ~300 tokens
- Load steps on-demand
- Load utility references only when specific validation needed

### 2. Self-Aware Scope
- CAN: Generate video prompts, validate components, check conflicts
- CANNOT: Execute video generation, modify source material

### 3. Lazy Loading
- Load prompt guide (short/long) after user chooses type
- Load camera-movements when camera movement validation needed
- Load anatomy reference when validating all 8 components

---

## START HERE

1. Ask user: **Text-to-Video** or **Image-to-Video** path?
2. If pipeline input available, offer to use existing Imagen prompts
3. Load step-01 and begin path determination
