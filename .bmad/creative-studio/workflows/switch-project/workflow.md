# Switch Project Workflow

**Purpose:** Change which project is currently active

**Version:** 1.0.0
**Type:** Utility (Non-pipeline)

---

## Overview

This workflow allows you to switch between different creative projects. The **active project** is where all workflow outputs will be saved by default.

When you switch projects:
- Registry is updated with new active project
- Future workflow runs output to the new active project
- Previous project remains intact but inactive

## What This Workflow Does

1. **Reads all projects** from registry
2. **Shows list** of available projects
3. **Prompts you** to select which project to activate
4. **Updates registry** with new active project
5. **Confirms** the switch

---

## Outputs

**Modified File:**
- `.bmad/creative-studio/_state/projects-registry.yaml` (active_project field updated)

**Console Output:**
- List of available projects
- Confirmation message

---

## Steps

### Step 1: List Available Projects
**File:** `steps/step-01-list-projects.md`

Reads registry and displays all projects you can switch to.

### Step 2: Select and Switch
**File:** `steps/step-02-select-switch.md`

Prompts for selection and updates the registry.

---

## Usage

```bash
# Run from Claude Code
/bmad:creative-studio:workflows:switch-project
```

Follow the prompts to select which project to activate.

---

## Example Interaction

```
════════════════════════════════════════════════════════════
  SWITCH ACTIVE PROJECT
════════════════════════════════════════════════════════════

Current Active Project:
  → dua-pelaut-satu-lautan-2025-12-14T12-30-00Z

Available Projects:

1. [ACTIVE] dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
   "Dua Pelaut, Satu Lautan"
   Type: video → YouTube
   Status: in-progress (5/6 stages)

2. music-video-test-2025-12-13T08-00-00Z
   "Music Video Test"
   Type: video → Instagram
   Status: completed (6/6 stages)

3. blog-post-draft-2025-12-12T14-00-00Z
   "Blog Post Draft"
   Type: blog → Medium
   Status: initialized (0/6 stages)

════════════════════════════════════════════════════════════

Which project would you like to activate? (Enter number or project ID)

> 2

════════════════════════════════════════════════════════════

✅ Active project switched!

Previous: dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
Now Active: music-video-test-2025-12-13T08-00-00Z

All future workflow outputs will save to:
docs/projects/music-video-test-2025-12-13T08-00-00Z/

════════════════════════════════════════════════════════════
```

---

## Use Cases

**When to use this workflow:**

1. **Working on multiple projects** - Switch between different creative works
2. **Returning to old project** - Reactivate a paused or completed project
3. **Testing workflows** - Switch to test project before running on main work
4. **Collaboration** - Switch to different client/collaborator projects

---

## Related Workflows

- **project-status** - View all projects and their status
- **init-creative-studio** - Create new project
- **archive-project** - Mark project as completed (future)

---

**Author:** V
**Created:** 2025-12-14
**Module:** creative-studio v1.2.0
