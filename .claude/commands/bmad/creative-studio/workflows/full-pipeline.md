---
description: 'Run full Creative Studio pipeline from concept to Veo 3 video prompts (6 stages)'
---

IT IS CRITICAL THAT YOU FOLLOW THIS COMMAND: Run the Creative Studio pipeline.

## Instructions

1. READ the module manifest: @.bmad/creative-studio/module.yaml
2. For each stage (01-06), LOAD and EXECUTE the workflow:
   - Stage 01: @.bmad/creative-studio/workflows/diverse-content-gen/workflow.md
   - Stage 02: @.bmad/creative-studio/workflows/storyteller/workflow.md
   - Stage 03: @.bmad/creative-studio/workflows/screenwriter/workflow.md
   - Stage 04: @.bmad/creative-studio/workflows/production-validator/workflow.md
   - Stage 05: @.bmad/creative-studio/workflows/imagine/workflow.md
   - Stage 06: @.bmad/creative-studio/workflows/arch-v/workflow.md

3. Pass handoff data between stages using the state file:
   @.bmad/creative-studio/_state/creative-pipeline-state.yaml

4. Follow each workflow's directions exactly.

## User Input Required

If $ARGUMENTS provided, use as initial concept.
Otherwise, ask user: "What creative concept would you like to develop into a video?"
