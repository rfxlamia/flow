---
name: production-validator
description: Validate screenplay for AI video generation and chunk into 8-second segments
type: creative-pipeline-stage-04
---

# Production Validator Workflow

**Goal:** Validate screenplay for Veo 3 feasibility, chunk scenes into 8-second segments, and generate continuation prompts.

**Your Role:** You are a technical producer. You ensure the creative vision can be executed by AI video generation tools.

**Core Principle:** Validate before production to save iteration time.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** with **smart context engineering**:

- workflow.md loads configuration only (minimal tokens)
- step-01 validates feasibility and identifies risky elements
- step-02 chunks scenes into 8-second segments
- step-03 generates Veo 3 prompts and output files
- References loaded on-demand for Veo 3 knowledge

---

## INITIALIZATION

### Configuration Loading

Load config from `{project-root}/.bmad/core/config.yaml` and resolve:

- `user_name`, `communication_language`, `output_folder`
- `date` as system-generated value

### Paths

- `installed_path` = `{project-root}/.bmad/creative-studio/workflows/production-validator`
- `projects_registry` = `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
- `active_project_path` = Read from projects_registry → active_project → path
- `pipeline_state_file` = `{active_project_path}/pipeline-state.yaml`
- `output_path` = `{active_project_path}/04-validator/`
- `references_path` = `{installed_path}/references`

### Pipeline Context

- **Previous Stage:** 03 (screenwriter)
- **Current Stage:** 04 (production-validator)
- **Next Stage:** 05 (imagine)
- **Capability:** Validate, chunk, and optimize for Veo 3
- **Scope:** Validation and optimization ONLY - does NOT change story
- **Output Format:** Enhanced XML with chunks and Veo 3 prompts
- **Key Constraint:** All chunks must be ≤8 seconds

---

## INPUT LOADING

### Step 0: Load Input from Screenwriter

**BEFORE executing step-01:**

1. **Read projects registry:** `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
2. **Get active project path:** Extract active_project → path
3. **Read pipeline state:** `{active_project_path}/pipeline-state.yaml`
4. **Find screenwriter output:** Extract from stage "03-screenwriter" → outputs
5. **Load screenplay:** Read the XML-tagged screenplay markdown from `{active_project_path}/03-screenwriter/`

**Required input fields:**
- `screenplay_file` - Path to formatted screenplay
- `scene_count` - Number of scenes
- `location_list` - All unique locations
- `prop_list` - Key props identified

---

## KEY CONCEPTS

### Veo 3 Constraints

Veo 3 generates maximum 8 seconds per clip. This workflow:
1. Validates each scene for AI-feasibility
2. Chunks scenes >8s into 8-second segments
3. Generates continuation prompts for seamless editing

### Risk Levels

| Risk | Meaning | Action |
|------|---------|--------|
| LOW | Veo 3 handles well | Proceed as-is |
| MEDIUM | May need iteration | Note potential issues |
| HIGH | Likely to fail | Suggest alternatives |
| CRITICAL | Will fail | Must optimize |

### Risky Elements (Quick Reference)

| Element | Risk | Alternative |
|---------|------|-------------|
| Multiple objects in motion | HIGH | Focus on one subject per beat |
| Text/signs visible | HIGH | Remove text, add in post |
| Complex hand gestures | MEDIUM | Simplify to basic poses |
| Multiple camera movements | CRITICAL | One movement per 8s chunk |
| Rapid scene changes | HIGH | Extend individual beats |

**For complete catalog:** Load `references/veo3-knowledge-base.md`

---

## EXECUTION

Execute steps sequentially:

### Step 01: Feasibility Validation
Load: `./steps/step-01-validate-feasibility.md`

Validates each scene for Veo 3 feasibility and identifies risky elements.

### Step 02: Scene Chunking
Load: `./steps/step-02-chunk-scenes.md`

Splits scenes >8s into 8-second segments with continuity.

### Step 03: Generate Output
Load: `./steps/step-03-generate-output.md`

Creates validated XML with Veo 3 prompts and tracking files.

---

## OUTPUT CONTRACT

### Content Output (.md file)

**File:** `validated-{timestamp}.md`

Enhanced XML with:
- Feasibility check results for each scene
- Chunked scenes (all ≤8 seconds)
- Veo 3 prompts for each chunk
- Continuity tags for editing
- Camera movement per chunk
- Continuation setup for seamless clips

### Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/validator-{timestamp}.yaml`

Required fields for imagine (from handoff-schema.yaml):
- `validated_screenplay_file` - Path to validated output
- `validation_status` - passed/passed_with_notes/needs_revision
- `total_chunks` - Number of 8-second chunks
- `production_notes` - Issues and alternatives
- `key_frames` - Recommended frames for image generation
- `visual_style_guide` - Color/lighting consistency notes

---

## CONTEXT ENGINEERING PRINCIPLES

### 1. Minimal Token Load
- workflow.md: ~300 tokens
- Load steps on-demand
- Load references only for complex validations

### 2. Self-Aware Scope
- CAN: Validate, chunk, optimize prompts, add continuity tags
- CANNOT: Change story, add scenes, alter emotional arc

### 3. Lazy Loading
- Load `veo3-knowledge-base.md` for complex risky element checks
- Load `chunking-workflow.md` for detailed chunking methodology
- Load `prompt-optimization.md` for Veo 3 prompt patterns
- Load `continuity-tagging.md` for continuity tag system and validation

---

## START HERE

1. Load input from screenwriter (Step 0)
2. Verify screenplay XML is properly formatted
3. Load step-01 and begin feasibility validation
