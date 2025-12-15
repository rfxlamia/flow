# Creative Studio Module

AI-powered content creation pipeline from ideation to video production (Veo 3).

**Version:** 1.1.0
**Author:** V
**BMAD Core:** >=6.0.0

---

## Overview

Creative Studio is a 6-stage pipeline that transforms creative concepts into production-ready video prompts. Each stage uses **context engineering** to minimize token usage while maximizing output quality.

```
Concept → Content → Scenes → Screenplay → Validation → Images → Video Prompts
```

---

## Quick Start

### Run Full Pipeline

```
User: "Create a romantic rain scene video"
```

The pipeline will guide you through each stage automatically.

### Run Individual Stage

```
User: "Run storyteller workflow with this concept: [your concept]"
```

### Run Video Production Only

```
User: "Run arch-v for a coffee shop morning video"
```

---

## Pipeline Stages

| Stage | Workflow | Purpose | Output |
|-------|----------|---------|--------|
| 01 | `diverse-content-gen` | Generate creative content using Verbalized Sampling | Diverse content variations |
| 02 | `storyteller` | Transform metaphor to visual scenes | Filmable scene descriptions |
| 03 | `screenwriter` | Format into screenplay | Professional screenplay format |
| 04 | `production-validator` | Validate for Veo 3 feasibility | 8-second chunks, key frames |
| 05 | `imagine` | Generate Imagen prompts | Imagen 3/4 prompts for stills |
| 06 | `arch-v` | Generate Veo 3 prompts | Validated video prompts |

---

## Stage Details

### Stage 01: Diverse Content Generation

**Purpose:** Generate multiple creative variations using Verbalized Sampling (VS) technique.

**Input:** User concept or idea
**Output:** 3-5 diverse content variations

**Key Features:**
- Increases diversity by 1.6-2.1x
- Maintains quality while varying style
- Lazy-loads VS references only when needed

---

### Stage 02: Storyteller

**Purpose:** Transform metaphorical narrative into filmable visual scenes.

**Input:** Selected content from Stage 01
**Output:** Visual scene breakdown with emotional beats

**Key Features:**
- Extracts emotional core
- Transforms abstract concepts to concrete visuals
- Maintains narrative coherence

---

### Stage 03: Screenwriter

**Purpose:** Format visual scenes into professional screenplay format.

**Input:** Visual scenes from Stage 02
**Output:** Formatted screenplay with XML structure

**Key Features:**
- Professional screenplay conventions
- Scene headers, action lines, dialogue
- Technical annotations for production

---

### Stage 04: Production Validator

**Purpose:** Validate production readiness and technical feasibility for Veo 3.

**Input:** Screenplay from Stage 03
**Output:** Validated chunks, key frames, feasibility report

**Key Features:**
- 8-second scene chunking (Veo 3 limit)
- Camera movement validation
- Continuity checking
- Key frame identification

---

### Stage 05: Imagine

**Purpose:** Generate professional Imagen 3/4 prompts for key frames.

**Input:** Key frames from Stage 04
**Output:** Imagen prompts for still image generation

**Key Features:**
- Subject-Context-Style framework
- Art style selection (Science SARU default)
- 480 token limit per prompt
- Natural language descriptions

**Available Art Styles:**
- Science SARU (default)
- Crewdson Hyperrealism
- iPhone Social Media
- Corporate Memphis

---

### Stage 06: Arch-V (Video Orchestrator)

**Purpose:** Generate validated Veo 3 video prompts.

**Input:** Imagen output OR direct user concept
**Output:** Validated Veo 3 prompts

**Two Production Paths:**

#### Path 1: Text-to-Video (Direct Veo 3)
- Single prompt for complete video
- Faster workflow
- Best for: clear video vision

#### Path 2: Image-to-Video (Imagen → Veo 3)
- Stage A: Generate still image with Imagen
- Stage B: Add motion with Veo 3
- Maximum control over composition

**8 Mandatory Components:**
1. Subject (who/what)
2. Setting (where/when)
3. Action (what happens)
4. Style/Genre (aesthetic)
5. Camera/Composition (shot, angle, movement)
6. Lighting/Mood (sources, tone)
7. Audio (dialogue, ambience, music)
8. Constraints (prohibitions)

**Validation Checks:**
- Component completeness
- Time/weather conflicts
- Camera movement conflicts (one per beat)
- Spatial coherence (FG/MG/BG)

---

## File Structure

```
.bmad/creative-studio/
├── module.yaml                    # Module manifest
├── README.md                      # This file
├── ARCHITECTURE.md                # Technical details
├── _state/
│   ├── creative-pipeline-state.yaml   # Global state
│   ├── handoff-schema.yaml            # Stage contracts
│   └── conversion-project.yaml        # Conversion tracking
└── workflows/
    ├── diverse-content-gen/
    │   ├── workflow.md
    │   ├── steps/
    │   ├── references/
    │   └── outputs/
    ├── storyteller/
    │   ├── workflow.md
    │   ├── steps/
    │   ├── references/
    │   └── outputs/
    ├── screenwriter/
    │   ├── workflow.md
    │   ├── steps/
    │   ├── references/
    │   └── outputs/
    ├── production-validator/
    │   ├── workflow.md
    │   ├── steps/
    │   ├── references/
    │   └── outputs/
    ├── imagine/
    │   ├── workflow.md
    │   ├── steps/
    │   ├── references/
    │   └── outputs/
    └── arch-v/
        ├── workflow.md
        ├── steps/
        │   ├── step-01-determine-path.md
        │   ├── step-02-build-validate.md
        │   └── step-03-generate-output.md
        ├── references/
        │   ├── camera-movements.md
        │   ├── movement-catalog.md
        │   ├── great-prompt-anatomy.md
        │   ├── anatomy-examples.md
        │   ├── short-prompt-guide.md
        │   ├── short-prompt-examples.md
        │   ├── long-prompt-guide.md
        │   ├── long-prompt-examples.md
        │   └── production-brief-template.md
        └── outputs/
```

---

## Context Engineering

Creative Studio uses aggressive context engineering to minimize token usage:

### Token Budget

| Stage | Initial Load | With All Refs | Savings |
|-------|-------------|---------------|---------|
| diverse-content-gen | ~250 | ~2,500 | 90% |
| storyteller | ~250 | ~500 | 50% |
| screenwriter | ~250 | ~400 | 38% |
| production-validator | ~250 | ~1,800 | 86% |
| imagine | ~250 | ~1,500 | 83% |
| arch-v | ~300 | ~3,000 | 90% |

**Total Initial: ~1,550 tokens** vs Monolithic: ~15,000+ tokens

### Lazy Loading Strategy

1. **Workflow.md** loads config and routing only
2. **Step files** load sequentially as needed
3. **References** load conditionally based on user choices
4. **Extended examples** in separate files, loaded on-demand

### Handoff Schema

Each stage produces:
- `content.md` - User-facing output
- `tracking.yaml` - Machine-readable metadata

Global state tracked in `creative-pipeline-state.yaml`.

---

## Tips & Best Practices

### For Best Results

1. **Be specific early** - Detailed concepts reduce back-and-forth
2. **Trust validation** - PROMPT-LOCKED means real conflicts exist
3. **Use path 2 for control** - Image-to-Video gives precise composition
4. **Follow the 8 components** - Missing elements create quality issues

### Common Mistakes to Avoid

- Multiple camera movements per beat
- Time/weather conflicts (golden hour + midnight)
- Vague subjects ("a person doing something")
- Missing audio descriptions
- Generic lighting ("nice lighting")

### Prompt Quality Indicators

- All 8 components present
- One camera movement per beat
- 3-5 color anchors for consistency
- FG/MG/BG spatial structure
- Specific foley sounds (not "ambient noise")

---

## Integration with External Tools

### Imagen 3/4
- Use Stage 05 (imagine) prompts
- 480 token limit per prompt
- Natural language descriptions

### Veo 3
- Use Stage 06 (arch-v) prompts
- 8-second scene chunks
- Text-to-video or image-to-video modes

---

## Changelog

### v1.1.0 (2025-12-13)
- Added Stage 06: arch-v (Video Orchestrator)
- Consolidated 5 video production skills into arch-v
- Added 9 reference files for video production
- Updated pipeline to output Veo 3 prompts

### v1.0.0 (2025-12-13)
- Initial release with 5 stages
- Diverse content generation with VS
- Storyteller metaphor transformation
- Screenwriter formatting
- Production validation
- Imagen prompt generation
