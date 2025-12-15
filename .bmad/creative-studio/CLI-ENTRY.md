# Creative Studio - Universal CLI Entry Point

This file works with ANY AI CLI tool (Claude Code, Gemini CLI, Aider, Continue, etc).

## How to Use This Module

### Option 1: Project Management

**Create new project:**
```
Read and execute: .bmad/creative-studio/workflows/init-creative-studio/workflow.md

Create a video project for Instagram about [YOUR IDEA]
```

**Check project status:**
```
Read and execute: .bmad/creative-studio/workflows/project-status/workflow.md
```

### Option 2: Run Pipeline Workflows

Tell your AI assistant:
```
Read and execute: .bmad/creative-studio/workflows/[WORKFLOW]/workflow.md
```

Replace `[WORKFLOW]` with one of:
- `diverse-content-gen` - Stage 01: Content variations
- `storyteller` - Stage 02: Visual scene transformation
- `screenwriter` - Stage 03: Screenplay formatting
- `production-validator` - Stage 04: Veo 3 validation
- `imagine` - Stage 05: Imagen prompt generation
- `arch-v` - Stage 06: Veo 3 video prompt generation

**Note:** Workflows automatically read from active project's pipeline state.

### Option 3: Quick Video Prompt (Standalone)

Tell your AI assistant:
```
Read .bmad/creative-studio/workflows/arch-v/workflow.md and help me create a video prompt for: [YOUR VIDEO IDEA]
```

---

## Available Workflows

| Workflow | Purpose | Entry Point |
|----------|---------|-------------|
| diverse-content-gen | Generate creative variations | `workflows/diverse-content-gen/workflow.md` |
| storyteller | Metaphor → filmable scenes | `workflows/storyteller/workflow.md` |
| screenwriter | Format as screenplay | `workflows/screenwriter/workflow.md` |
| production-validator | Validate for Veo 3 | `workflows/production-validator/workflow.md` |
| imagine | Imagen 3/4 prompts | `workflows/imagine/workflow.md` |
| arch-v | Veo 3 video prompts | `workflows/arch-v/workflow.md` |

---

## CLI-Specific Instructions

### Claude Code
Use slash commands:
```
/bmad:creative-studio:workflows:init-creative-studio
/bmad:creative-studio:workflows:project-status
/bmad:creative-studio:workflows:diverse-content-gen
/bmad:creative-studio:workflows:storyteller
/bmad:creative-studio:workflows:arch-v
```

### Gemini CLI / Aider / Continue
Copy-paste this prompt:
```
Read and execute .bmad/creative-studio/workflows/init-creative-studio/workflow.md to create a new video project for [PLATFORM] about [IDEA]

Then run the pipeline stages in order:
1. diverse-content-gen
2. storyteller
3. screenwriter
4. production-validator
5. imagine
6. arch-v
```

### Quick Status Check (Any CLI)
```
Read .bmad/creative-studio/workflows/project-status/workflow.md and show all projects
```

---

## Documentation

| Document | Path | Purpose |
|----------|------|---------|
| User Guide | `.bmad/creative-studio/README.md` | How to use |
| Architecture | `.bmad/creative-studio/ARCHITECTURE.md` | Technical details |
| Module Config | `.bmad/creative-studio/module.yaml` | Pipeline definition |

---

## Quick Reference

### arch-v Two Paths

**Path 1: Text-to-Video**
- Direct Veo 3 prompt
- Faster, less control

**Path 2: Image-to-Video**
- Create still image with Imagen first
- Then add motion with Veo 3
- Maximum control

### 8 Mandatory Video Prompt Components

1. Subject (who/what)
2. Setting (where/when)
3. Action (what happens)
4. Style/Genre (aesthetic)
5. Camera/Composition (shot, angle, movement)
6. Lighting/Mood (sources, tone)
7. Audio (dialogue, ambience, music)
8. Constraints (prohibitions)
