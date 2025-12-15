# Init Creative Studio Workflow

**Purpose:** Initialize a new creative project with centralized output structure

**Version:** 1.0.0
**Stage:** 00 (Foundation)

---

## Overview

This workflow creates a structured project workspace for any creative content type (video, blog, carousel, etc). It ensures all pipeline outputs are centralized in one easy-to-access location.

## What This Workflow Does

1. **Gathers project information** from you
2. **Creates organized directory structure** for all outputs
3. **Generates project configuration** files
4. **Registers project** as the active workspace
5. **Prepares you** for content creation

## Outputs

- **Project Directory:** `docs/projects/{project-name}-{timestamp}/`
- **Configuration:** `project-config.yaml`
- **Documentation:** `README.md`
- **Registry Entry:** Updates `.bmad/creative-studio/_state/projects-registry.yaml`

---

## Steps

### Step 1: Gather Project Information
**File:** `steps/step-01-gather-info.md`

Collects:
- Project name (slug-friendly)
- Content type (video, blog, carousel, etc)
- Target platform (YouTube, Instagram, Medium, etc)
- Brief description

### Step 2: Create Directory Structure
**File:** `steps/step-02-create-structure.md`

Creates:
- Main project folder with timestamp
- Stage subdirectories (01-06 or more)
- Templates for configuration and documentation

### Step 3: Register Project
**File:** `steps/step-03-register-project.md`

Updates:
- Projects registry with new entry
- Sets project as "active"
- Stores metadata for workflow continuity

---

## Usage

```bash
# Run from Claude Code
/bmad:creative-studio:workflows:init-creative-studio
```

Follow the prompts to set up your new creative project.

---

## Next Steps After Init

Depending on your content type:

**For Video Projects:**
1. Run `diverse-content-gen` to generate creative variations
2. Continue through video pipeline (storyteller → screenwriter → validator → imagine → arch-v)

**For Blog/Carousel Projects (Coming Soon):**
1. Run `diverse-content-gen` to generate creative variations
2. Continue through appropriate pipeline

---

**Author:** V
**Created:** 2025-12-14
**Module:** creative-studio v1.1.0
