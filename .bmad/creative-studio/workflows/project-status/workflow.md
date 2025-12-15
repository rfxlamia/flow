# Project Status Workflow

**Purpose:** View all creative projects and their current status

**Version:** 1.0.0
**Type:** Utility (Non-pipeline)

---

## Overview

This workflow reads the projects registry and displays all creative projects with their status, progress, and details. It helps you:

- See all projects you've created
- Check which project is currently active
- View project progress through pipeline stages
- Find project paths quickly

## What This Workflow Does

1. **Reads projects registry** from `.bmad/creative-studio/_state/projects-registry.yaml`
2. **Displays all projects** in a formatted table
3. **Highlights active project** currently receiving workflow outputs
4. **Shows progress** for each project (stages completed)
5. **Provides project paths** for easy navigation

---

## Outputs

This is a read-only workflow - it displays information but doesn't create or modify files.

**Console Output:**
- Formatted project list
- Status indicators
- Progress tracking
- Quick navigation paths

---

## Steps

### Step 1: Read Registry
**File:** `steps/step-01-read-registry.md`

Loads the projects registry file and validates it exists.

### Step 2: Display Projects
**File:** `steps/step-02-display-projects.md`

Formats and displays all projects in a user-friendly table.

---

## Usage

```bash
# Run from Claude Code
/bmad:creative-studio:workflows:project-status
```

No prompts or inputs required - just displays current state.

---

## Example Output

```
════════════════════════════════════════════════════════════
  CREATIVE STUDIO - PROJECT STATUS
════════════════════════════════════════════════════════════

Active Project: dua-pelaut-satu-lautan-2025-12-14T12-30-00Z

┌────────────────────────────────────────────────────────────┐
│ PROJECT LISTING (3 total)                                  │
└────────────────────────────────────────────────────────────┘

[ACTIVE] dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
  Name: Dua Pelaut, Satu Lautan
  Type: video → YouTube
  Status: in-progress
  Progress: [████████░░] 80% (5/6 stages)
    ✅ 01-diverse
    ✅ 02-storyteller
    ✅ 03-screenwriter
    ✅ 04-validator
    ✅ 05-imagine
    ⏳ 06-arch-v (pending)
  Path: docs/projects/dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
  Created: 2025-12-14 12:30:00

────────────────────────────────────────────────────────────

[COMPLETED] music-video-test-2025-12-13T08-00-00Z
  Name: Music Video Test
  Type: video → Instagram
  Status: completed
  Progress: [██████████] 100% (6/6 stages)
  Path: docs/projects/music-video-test-2025-12-13T08-00-00Z
  Created: 2025-12-13 08:00:00

────────────────────────────────────────────────────────────

[INITIALIZED] blog-post-draft-2025-12-12T14-00-00Z
  Name: Blog Post Draft
  Type: blog → Medium
  Status: initialized
  Progress: [░░░░░░░░░░] 0% (0/6 stages)
  Path: docs/projects/blog-post-draft-2025-12-12T14-00-00Z
  Created: 2025-12-12 14:00:00

════════════════════════════════════════════════════════════

Quick Actions:
- Switch active project: /bmad:creative-studio:workflows:switch-project
- Create new project: /bmad:creative-studio:workflows:init-creative-studio

════════════════════════════════════════════════════════════
```

---

## Related Workflows

- **init-creative-studio** - Create new project
- **switch-project** - Change active project
- **archive-project** - Mark project as completed/archived (future)

---

**Author:** V
**Created:** 2025-12-14
**Module:** creative-studio v1.2.0
