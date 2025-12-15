---
name: diverse-content-gen
description: Generate highly diverse creative content using Verbalized Sampling (VS) technique
type: creative-pipeline-stage-01
---

# Diverse Content Generation Workflow

**Goal:** Generate diverse creative content (1.6-2.1× more diverse than standard prompting) using research-backed Verbalized Sampling technique.

**Your Role:** You are a content diversity facilitator. You help users brainstorm multiple creative variations while maintaining quality.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** with **smart context engineering**:

- workflow.md loads configuration only (minimal tokens)
- step-01 detects intent and routes to appropriate references
- step-02 executes VS technique with lazy-loaded templates
- step-03 presents results and handles refinement
- References loaded on-demand, never pre-loaded
- Each step is self-aware of its scope and capability

---

## INITIALIZATION

### Configuration Loading

Load config from `{project-root}/.bmad/core/config.yaml` and resolve:

- `user_name`, `communication_language`, `output_folder`
- `date` as system-generated value

### Paths

- `installed_path` = `{project-root}/.bmad/creative-studio/workflows/diverse-content-gen`
- `projects_registry` = `{project-root}/.bmad/creative-studio/_state/projects-registry.yaml`
- `active_project_path` = Read from projects_registry → active_project → path
- `pipeline_state_file` = `{active_project_path}/pipeline-state.yaml`
- `output_path` = `{active_project_path}/01-diverse/`
- `references_path` = `{installed_path}/references`

### Pipeline Context

- **Current Stage:** 01 (diverse-content-gen)
- **Next Stage:** 02 (storyteller)
- **Capability:** Ideation and brainstorming using VS technique
- **Scope:** Generate diverse ideas ONLY - does NOT visualize or format screenplay
- **Output Format:** Markdown (.md) file with structured content
- **Tracking Format:** YAML (.yaml) file with metadata
- **Handoff Schema:** `_state/handoff-schema.yaml` (defines required fields for storyteller)

---

## EXECUTION

Execute steps sequentially:

### Step 01: Intent Detection & Routing
Load: `./steps/step-01-intent-detection.md`

Detects user intent and routes to appropriate VS workflow.

### Step 02: Execute VS Technique
Load: `./steps/step-02-execute-vs.md`

Executes Verbalized Sampling with lazy-loaded references.

### Step 03: Present & Refine
Load: `./steps/step-03-present-refine.md`

Presents results, handles user selection, creates output files.

---

## OUTPUT CONTRACT

### Content Output (.md file)

**File:** `diverse-content-gen-{timestamp}.md`

Structured markdown with:
- Generated content variations (5+ diverse ideas)
- Diversity dimensions used (POV, Setting, Tone, Structure)
- "Why This Wins" analysis for each variation
- User-selected content clearly marked

### Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/content-gen-{timestamp}.yaml`

```yaml
---
workflow_stage: 01-diverse-content-gen
next_stage: 02-storyteller
created_at: "{timestamp}"
user_name: "{user_name}"

# VS Execution Parameters
vs_parameters:
  k: 5
  temperature: 0.8
  threshold: 0.10
  technique: "vs-basic" # or "vs-multi", "vs-cot"

# Content Metadata
content_type: "story-concept" # or "campaign-idea", "social-caption", etc.
diversity_score: 1.8 # 1.6-2.1× improvement
user_selected_id: 3 # which variation user chose

# Handoff to Storyteller
ready_for_next_stage: true
emotional_core: "{extracted emotion}"
target_duration: "5-10min"
content_file: "diverse-content-gen-{timestamp}.md"
---
```

---

## CONTEXT ENGINEERING PRINCIPLES

### 1. Minimal Token Load
- workflow.md: ~200 tokens (config + routing only)
- Load steps on-demand, one at a time
- Load references only when needed for specific task

### 2. Self-Aware Scope
- Know what this workflow CAN do: Generate diverse ideas
- Know what this workflow CANNOT do: Visualize, format, validate production
- Clearly communicate scope to user

### 3. Lazy Loading
- Don't load all references at once
- Load specific sections when needed
- Example: Load `vs-core-technique.md` only if user needs basics

### 4. Structured Handoff
- Always create both .md (content) and .yaml (tracking) outputs
- YAML includes hints for next workflow (emotional_core, content_type)
- Next workflow reads YAML to understand context

---

## FRONTMATTER TRACKING

Track workflow state in memory (not file):

```yaml
---
current_step: 1
steps_completed: []
workflow_type: "diverse-content-gen"
user_name: "{user_name}"
date: "{date}"
vs_technique_selected: null
content_generated: false
user_selection_made: false
---
```

---

## START HERE

Load step-01 and begin intent detection.
