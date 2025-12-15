---
name: imagine
description: Generate professional Imagen 3/4 prompts for key frames from validated screenplay
type: creative-pipeline-stage-05
---

# Imagine Workflow

**Goal:** Generate detailed Imagen 3/4 prompts for key frames from the validated screenplay.

**Your Role:** You are a visual prompt architect. You translate screenplay chunks into professional image generation prompts.

**Core Principle:** Use natural language descriptions, not keyword lists. Imagen rewards verbose prose.

---

## WORKFLOW ARCHITECTURE

This uses **micro-file architecture** with **smart context engineering**:

- workflow.md loads configuration only (minimal tokens)
- step-01 loads key frames and selects art style
- step-02 generates Imagen prompts for each key frame
- step-03 creates output files with prompts and metadata
- References loaded on-demand for art styles

---

## INITIALIZATION

### Configuration Loading

Load config from `{project-root}/.bmad/core/config.yaml` and resolve:

- `user_name`, `communication_language`, `output_folder`
- `date` as system-generated value

### Paths

- `installed_path` = `{project-root}/.bmad/creative-studio/workflows/imagine`
- `output_path` = `{installed_path}/outputs`
- `state_file` = `{project-root}/.bmad/creative-studio/_state/creative-pipeline-state.yaml`
- `references_path` = `{installed_path}/references`

### Pipeline Context

- **Previous Stage:** 04 (production-validator)
- **Current Stage:** 05 (imagine)
- **Next Stage:** null (final stage)
- **Capability:** Generate Imagen 3/4 prompts for images
- **Scope:** Prompt generation for still images
- **Output Format:** Markdown with structured prompts

---

## INPUT LOADING

### Step 0: Load Input from Production-Validator

**BEFORE executing step-01:**

1. **Read pipeline state:** `creative-pipeline-state.yaml`
2. **Find validator tracking file:** Extract `tracking_file` from stage 04
3. **Load tracking YAML:** Read the validator-{timestamp}.yaml file
4. **Extract data:** Get key_frames, visual_style_guide, validation_status
5. **Load validated screenplay:** For additional context if needed

**Required input fields:**
- `validated_screenplay_file` - Path to validated output
- `key_frames` - Recommended frames for image generation
- `visual_style_guide` - Color, lighting, mood guidance

---

## CORE CONCEPTS

### Imagen Prompt Structure

Build prompts using **Subject-Context-Style** framework:

1. **Subject:** Primary focus (person, object, scenery)
2. **Context:** Environment, placement, background
3. **Style:** Aesthetic approach with technical specs

### Prompt Types

| Type | Use Case | Pattern |
|------|----------|---------|
| Photography | Realistic shots | "A photo of [subject], [context], [technical specs]" |
| Artistic | Stylized | "[Art style], [scene], [aesthetic details]" |
| Cinematic | Film frames | "[Cinematography], [scene], [color grading]" |

### Technical Specifications

**Lens types:**
- 24-85mm: Portraits, characters
- 60-105mm macro: Close-ups, details
- 10-24mm wide-angle: Landscapes, establishing

**Lighting:**
- Natural light, studio lighting
- Golden hour, dramatic lighting
- Soft diffused, hard shadows

**Quality modifiers:**
- Sharp focus, high detail
- Professional photography, 8K resolution
- Shot on ARRI Alexa, 35mm film

---

## ART STYLE REFERENCES

### Available Styles

| Style | Reference File | Description |
|-------|---------------|-------------|
| Science SARU | `artstyle-sciencesaru.md` | Anime, Masaaki Yuasa aesthetic (DEFAULT) |
| Crewdson Hyperrealism | `artstyle-crewdson-hyperrealism.md` | Cinematic staged photography |
| iPhone Social Media | `artstyle-iphone-social-media.md` | Casual authentic photos |
| Corporate Memphis | `artstyle-corporate-memphis.md` | Flat illustration style |

**Default style:** Science SARU (unless user specifies otherwise)

### Using Art Styles

1. **Load reference:** Read the artstyle-{name}.md file
2. **Extract key vocabulary:** Visual language, techniques
3. **Apply to prompts:** Use style-specific descriptors

---

## EXECUTION

Execute steps sequentially:

### Step 01: Key Frame Selection & Style
Load: `./steps/step-01-select-frames.md`

Reviews key frames from validator and confirms art style.

### Step 02: Generate Imagen Prompts
Load: `./steps/step-02-generate-prompts.md`

Creates detailed prompts for each key frame.

### Step 03: Generate Output Files
Load: `./steps/step-03-generate-output.md`

Creates final prompt file and completes pipeline.

---

## OUTPUT CONTRACT

### Content Output (.md file)

**File:** `outputs/imagine-prompts-{timestamp}.md`

Markdown with:
- Prompt for each key frame
- Technical parameters (aspect ratio, settings)
- Art style applied
- Visual consistency notes

### Tracking Output (.yaml file)

**File:** `{project-root}/.bmad/creative-studio/_state/imagine-{timestamp}.yaml`

Fields:
- `prompts_file` - Path to prompts
- `total_prompts` - Number generated
- `art_style` - Style used
- `pipeline_completed` - Boolean

---

## CONTEXT ENGINEERING PRINCIPLES

### 1. Minimal Token Load
- workflow.md: ~250 tokens
- Load steps on-demand
- Load art style reference only when generating

### 2. Self-Aware Scope
- CAN: Generate image prompts, apply art styles
- CANNOT: Generate video, modify screenplay

### 3. Lazy Loading
- Load art style reference when style is confirmed
- Load additional styles only if user requests

---

## CRITICAL CONSTRAINTS

### Imagen Limits
- **Text in image:** Max 25 characters per phrase, 3 phrases total
- **Token limit:** 480 tokens per prompt
- **Negative prompts:** Use descriptive terms, not instructions

### Best Practices
- Natural language over keywords
- Verbose descriptions rewarded
- Specific materials and textures
- Cinematography vocabulary

---

## START HERE

1. Load input from production-validator (Step 0)
2. Verify key frames are available
3. Load step-01 and begin frame selection
