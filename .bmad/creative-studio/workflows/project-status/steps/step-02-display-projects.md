# Step 2: Display Projects

**Purpose:** Format and display all projects in a user-friendly view

---

## Instructions

Using the data from Step 1, create a formatted display of all projects.

### Display Format

```
════════════════════════════════════════════════════════════
  CREATIVE STUDIO - PROJECT STATUS
════════════════════════════════════════════════════════════

Active Project: {active_project_id}
Last Updated: {last_updated}

┌────────────────────────────────────────────────────────────┐
│ PROJECT LISTING ({total} total)                            │
└────────────────────────────────────────────────────────────┘

{for each project in projects_list}

[{STATUS_BADGE}] {project.id}
  Name: {project.display_name}
  Type: {project.type} → {project.platform}
  Status: {project.status}
  Progress: {progress_bar} {percentage}% ({completed}/{total} stages)
    {stage_checklist}
  Path: {project.path}
  Created: {formatted_date}

────────────────────────────────────────────────────────────

{end for}

════════════════════════════════════════════════════════════

Quick Actions:
- Switch active project: /bmad:creative-studio:workflows:switch-project
- Create new project: /bmad:creative-studio:workflows:init-creative-studio

════════════════════════════════════════════════════════════
```

---

## Status Badges

Map project status to display badge:

- `initialized` → `[INITIALIZED]`
- `in-progress` → `[ACTIVE]` (if active_project) or `[IN PROGRESS]`
- `completed` → `[COMPLETED]`
- `archived` → `[ARCHIVED]`

---

## Progress Calculation

For each project, read its **pipeline-state.yaml** to get accurate stage completion:

```
{project.path}/pipeline-state.yaml
```

Look for:
```yaml
current_stage: 3
last_updated: "2025-12-14T15:00:00Z"

stages:
  "01-diverse":
    status: "completed"
    completed_at: "..."
    outputs: [...]
  "02-storyteller":
    status: "completed"
    completed_at: "..."
    outputs: [...]
  "03-screenwriter":
    status: "in_progress"
    outputs: []
  "04-validator":
    status: "pending"
    outputs: []
  # ...
```

Count completed stages and calculate percentage:
```
completed_count = count(stages where status == "completed")
total_stages = 6 (for video pipeline)
percentage = (completed_count / total_stages) * 100
```

**Fallback:** If `pipeline-state.yaml` doesn't exist, read from `project-config.yaml` instead.

---

## Progress Bar

Visual representation using blocks:

```
[██████████] 100% (6/6 stages)  # All complete
[████████░░] 80%  (5/6 stages)  # 5 complete
[██████░░░░] 60%  (4/6 stages)  # 4 complete
[████░░░░░░] 40%  (3/6 stages)  # 3 complete
[██░░░░░░░░] 20%  (2/6 stages)  # 2 complete
[░░░░░░░░░░] 0%   (0/6 stages)  # None complete
```

---

## Stage Checklist

Show each stage with status icon:

```
✅ 01-diverse (completed)
✅ 02-storyteller (completed)
✅ 03-screenwriter (completed)
✅ 04-validator (completed)
⏳ 05-imagine (in-progress)
⬜ 06-arch-v (pending)
```

Icons:
- ✅ = completed
- ⏳ = in-progress
- ⬜ = pending

---

## Date Formatting

Convert ISO timestamp to readable format:

```
Input:  "2025-12-14T12:30:00Z"
Output: "2025-12-14 12:30:00"
```

Or even friendlier:
```
Output: "Dec 14, 2025 at 12:30 PM"
```

---

## Sorting Projects

Display projects in order:

1. **Active project first** (highlighted)
2. **In-progress projects** (by most recent)
3. **Initialized projects** (by most recent)
4. **Completed projects** (by most recent)
5. **Archived projects** (by most recent)

---

## If Reading pipeline-state.yaml Fails

If you can't read a project's pipeline state file, fall back to `project-config.yaml`:

```
[WARNING] {project.id}
  Name: {project.display_name}
  Status: {project.status}
  Path: {project.path}
  ⚠️  Pipeline state unavailable (using basic config)
```

If neither file exists:

```
[ERROR] {project.id}
  Name: {project.display_name}
  Status: Unknown
  Path: {project.path}
  ❌ Project configuration missing
```

---

## Final Output

Display the complete formatted view to the console.

**Workflow complete!**
