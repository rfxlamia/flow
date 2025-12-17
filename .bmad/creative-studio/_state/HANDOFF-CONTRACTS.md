# Creative Studio Pipeline - Handoff Contracts

**Purpose:** Developer reference for stage-to-stage data contracts.

**Audience:** Workflow developers and maintainers.

**Status:** Documentation only - NOT loaded during runtime.

---

## Overview

Creative Studio uses a **handoff contract system** where each workflow stage produces:
1. **Content file** (`.md`) - User-facing output
2. **Tracking file** (`.yaml`) - Machine-readable metadata

The tracking YAML files contain **required fields** that the next stage needs to operate. This document defines those contracts.

---

## Timestamp Standard

All timestamps in Creative Studio use **ISO8601 format**:

```yaml
format: "YYYY-MM-DDTHH-MM-SSZ"
example: "2025-12-13T04-30-00Z"
generation: "AI generates using current date/time"
```

**Note:** Colons replaced with hyphens for filename safety.

---

## Stage 01 → 02: diverse-content-gen → storyteller

### Contract: `diverse_content_gen_to_storyteller`

**Purpose:** Content ideation output for visual story transformation.

### Output Files

```
content_file:  workflows/diverse-content-gen/outputs/content-{timestamp}.md
tracking_file: _state/content-gen-{timestamp}.yaml
```

### Required Fields in Tracking YAML

#### Content Identification

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `content_file` | string | Path to markdown with generated ideas | `workflows/diverse-content-gen/outputs/content-2025-12-13T04-30-00Z.md` |
| `selected_idea_id` | integer | Which idea user selected (1-5) | `3` |
| `selected_idea_title` | string | Title of selected idea | `"The Frozen Shore - A tale of eternal waiting"` |

#### Emotional & Tonal Data (for storyteller)

| Field | Type | Values | Example |
|-------|------|--------|---------|
| `emotional_core` | string | Primary emotion | `"longing, devotion bordering on obsession"` |
| `pov` | enum | `first_person`, `second_person`, `third_person`, `interlocutor_absent` | `"first_person"` |
| `setting` | string | Environment/location context | `"coastal, frozen beach at dawn"` |
| `tone` | enum | `vulnerable_raw`, `poetic_mythic`, `theatrical_absurd`, `nostalgic_epistolary`, `cinematic` | `"poetic_mythic"` |
| `structure_type` | enum | `linear_monolog`, `letter`, `parallel_scenes`, `extended_metaphor`, `one_sided_dialog` | `"extended_metaphor"` |

#### Analysis Data

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `why_this_wins` | string | Strength analysis | `"Universal emotion + unique visual metaphor + clear character arc"` |
| `diversity_markers` | string | VS dimensions varied | `"POV: first_person, Setting: coastal, Tone: poetic_mythic"` |

#### Pipeline Control

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `metaphorical_content` | boolean | Needs visual translation? | `true` |
| `target_duration` | string | Target video duration | `"5-10min"` |
| `ready_for_next_stage` | boolean | Ready for storyteller? | `true` |

---

## Stage 02 → 03: storyteller → screenwriter

### Contract: `storyteller_to_screenwriter`

**Purpose:** Visual scene breakdown for screenplay formatting.

### Output Files

```
content_file:  workflows/storyteller/outputs/scenes-{timestamp}.md
tracking_file: _state/storyteller-{timestamp}.yaml
```

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `scene_breakdown_file` | string | Path to scene breakdown | `workflows/storyteller/outputs/scenes-2025-12-13T04-30-00Z.md` |
| `total_scenes` | integer | Number of scenes | `12` |
| `characters` | list | Character descriptions | `["Emma - protagonist, 28", "Voice - unseen presence"]` |
| `story_logic_map` | object | Metaphor → visual translation | `{frozen_shore: "literal_beach", "waiting": "watching_horizon"}` |
| `estimated_duration` | string | Total estimated duration | `"7 minutes"` |
| `emotional_arc` | string | Progression through scenes | `"hope → despair → acceptance → transcendence"` |

---

## Stage 03 → 04: screenwriter → production-validator

### Contract: `screenwriter_to_production_validator`

**Purpose:** Formatted screenplay for production validation.

### Output Files

```
content_file:  workflows/screenwriter/outputs/screenplay-{timestamp}.md
tracking_file: _state/screenwriter-{timestamp}.yaml
```

### Required Fields

| Field | Type | Description | Example |
|-------|------|-------------|---------|
| `screenplay_file` | string | Path to formatted screenplay | `workflows/screenwriter/outputs/screenplay-2025-12-13T04-30-00Z.md` |
| `format_version` | string | Screenplay format used | `"standard_hollywood"` |
| `scene_count` | integer | Number of scenes | `12` |
| `location_list` | list | All unique locations | `["EXT. FROZEN BEACH - DAWN", "INT. CABIN - NIGHT"]` |
| `prop_list` | list | Key props needed | `["lantern", "letter", "compass"]` |

---

## Stage 04 → 05: production-validator → imagine

### Contract: `production_validator_to_imagine`

**Purpose:** Validated screenplay for image prompt generation.

### Output Files

```
content_file:  workflows/production-validator/outputs/validated-{timestamp}.md
tracking_file: _state/validator-{timestamp}.yaml
```

### Required Fields

| Field | Type | Description | Values/Example |
|-------|------|-------------|----------------|
| `validated_screenplay_file` | string | Path to validated screenplay | `workflows/production-validator/outputs/validated-2025-12-13T04-30-00Z.md` |
| `validation_status` | enum | Production readiness status | `passed`, `passed_with_notes`, `needs_revision` |
| `production_notes` | list | Notes for visual production | `["Scene 3: simplify hand gesture", "Scene 7: add continuity tag for wardrobe"]` |
| `key_frames` | list | Recommended frames for images | `["Scene 1 - 0:04s opening shot", "Scene 3 - 1:23s emotional peak"]` |
| `visual_style_guide` | object | Color/lighting/mood references | `{palette: ["#2C4E5A", "#F4E8D0"], lighting: "golden_hour", mood: "melancholic"}` |

---

## How to Use This Document

### For Workflow Developers

When creating a workflow's **output step** (usually `step-03-generate-output.md`):

1. Find your workflow's contract section above
2. Ensure your tracking YAML includes **ALL required fields**
3. Use **exact field names** - no variations
4. Follow the data types and value constraints

### For Next-Stage Workflows

When creating a workflow's **input loading** (usually in `workflow.md` or `step-01`):

1. Find your INPUT contract (the previous stage's OUTPUT)
2. Read the tracking YAML from the previous stage
3. Extract and validate all required fields before processing
4. Handle missing/invalid fields gracefully

### State File Discovery Pattern

To find the latest output from a previous stage:

```yaml
# 1. Read projects registry
Read: {project-root}/.bmad/creative-studio/_state/projects-registry.yaml

# 2. Get active project path
active_project_path = projects_registry → active_project → path

# 3. Read pipeline state for that project
Read: {active_project_path}/pipeline-state.yaml

# 4. Find the stage you need input from
previous_stage_data = pipeline_state → stages → {stage_id}

# 5. Read tracking file
Read: {active_project_path}/{previous_stage_data → outputs → tracking_file}
```

---

## Implementation Notes

### Why This Isn't Runtime-Loaded

Each workflow's `step-03` file **already contains the template** for its tracking YAML output. The templates are **embedded directly** in the step files, making this document unnecessary at runtime.

**This document exists for:**
- Developer reference when creating new stages
- Validation during code review
- Documentation of pipeline architecture
- Ensuring consistency across stages

### Template vs Contract

- **This document (HANDOFF-CONTRACTS.md)** = Specification (what fields are required)
- **step-03 files** = Implementation (actual templates with those fields)

Both should be kept in sync when contracts change.

---

## Version History

**v1.0** (2025-12-13)
- Initial handoff schema for 5-stage pipeline
- Contracts: content-gen → storyteller → screenwriter → validator → imagine

**v1.1** (2025-12-15)
- Converted from `handoff-schema.yaml` to `HANDOFF-CONTRACTS.md`
- Clarified developer-only documentation status
- Added implementation notes and usage patterns
