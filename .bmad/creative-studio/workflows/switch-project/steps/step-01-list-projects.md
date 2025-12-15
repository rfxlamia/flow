# Step 1: List Available Projects

**Purpose:** Display all projects that can be activated

---

## Instructions

1. **Read registry file:**
   ```
   .bmad/creative-studio/_state/projects-registry.yaml
   ```

2. **Handle missing registry:**
   If file doesn't exist:
   ```
   ════════════════════════════════════════════════════════════
     NO PROJECTS FOUND
   ════════════════════════════════════════════════════════════

   You don't have any projects yet.

   Create your first project:
   /bmad:creative-studio:workflows:init-creative-studio

   ════════════════════════════════════════════════════════════
   ```
   STOP workflow.

3. **Handle empty projects:**
   If `projects: []` is empty, show same message and STOP.

4. **Display current active project:**

```
════════════════════════════════════════════════════════════
  SWITCH ACTIVE PROJECT
════════════════════════════════════════════════════════════

Current Active Project:
  → {active_project_id}
  "{display_name}"

════════════════════════════════════════════════════════════
```

5. **List all available projects:**

For each project in registry:

```
{index}. [{BADGE}] {project.id}
   "{project.display_name}"
   Type: {project.type} → {project.platform}
   Status: {project.status} ({completed}/{total} stages)
   Created: {formatted_date}
```

Badges:
- `[ACTIVE]` - Currently active project
- No badge - Inactive project

---

## Example Output

```
════════════════════════════════════════════════════════════
  SWITCH ACTIVE PROJECT
════════════════════════════════════════════════════════════

Current Active Project:
  → dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
  "Dua Pelaut, Satu Lautan"

════════════════════════════════════════════════════════════

Available Projects ({total_count}):

1. [ACTIVE] dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
   "Dua Pelaut, Satu Lautan"
   Type: video → YouTube
   Status: in-progress (5/6 stages)
   Created: Dec 14, 2025

2. music-video-test-2025-12-13T08-00-00Z
   "Music Video Test"
   Type: video → Instagram
   Status: completed (6/6 stages)
   Created: Dec 13, 2025

3. blog-post-draft-2025-12-12T14-00-00Z
   "Blog Post Draft"
   Type: blog → Medium
   Status: initialized (0/6 stages)
   Created: Dec 12, 2025

════════════════════════════════════════════════════════════
```

---

## Handle Single Project Edge Case

If there's only ONE project (which is already active):

```
════════════════════════════════════════════════════════════
  ONLY ONE PROJECT EXISTS
════════════════════════════════════════════════════════════

You only have one project, and it's already active:

  → {project.id}
  "{project.display_name}"

Create a new project to have multiple projects to switch between:
/bmad:creative-studio:workflows:init-creative-studio

════════════════════════════════════════════════════════════
```

STOP workflow (nothing to switch to).

---

## Data to Pass to Step 2

If multiple projects exist:

```yaml
current_active_id: "dua-pelaut-satu-lautan-2025-12-14T12-30-00Z"

projects_list:
  - index: 1
    id: "dua-pelaut-satu-lautan-2025-12-14T12-30-00Z"
    display_name: "Dua Pelaut, Satu Lautan"
    is_active: true
    # ... other fields

  - index: 2
    id: "music-video-test-2025-12-13T08-00-00Z"
    display_name: "Music Video Test"
    is_active: false
    # ... other fields
```

---

## Next Step

Proceed to `step-02-select-switch.md` with the project list.
