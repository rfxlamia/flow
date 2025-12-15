# Step 1: Read Registry

**Purpose:** Load and validate the projects registry

---

## Instructions

1. **Locate registry file:**
   ```
   .bmad/creative-studio/_state/projects-registry.yaml
   ```

2. **Check if file exists:**
   - If **exists**: Load the YAML content
   - If **NOT exists**: Display message:
     ```
     ════════════════════════════════════════════════════════════
       NO PROJECTS FOUND
     ════════════════════════════════════════════════════════════

     You haven't created any projects yet.

     Get started:
     /bmad:creative-studio:workflows:init-creative-studio

     ════════════════════════════════════════════════════════════
     ```
     Then STOP workflow (nothing to display)

3. **Parse YAML structure:**

Expected structure:
```yaml
registry_version: "1.0.0"
last_updated: "2025-12-14T12:30:00Z"
active_project: "project-id-timestamp"

projects:
  - id: "project-id-timestamp"
    name: "project-name"
    display_name: "Display Name"
    type: "video"
    platform: "youtube"
    created: "2025-12-14T12:30:00Z"
    status: "in-progress"
    path: "docs/projects/project-id"
    pipeline: "video-full"
```

4. **Validate registry data:**
   - Check `registry_version` exists
   - Check `projects` is an array (even if empty)
   - Store `active_project` ID

5. **Handle empty projects array:**
   If `projects: []` is empty, display:
   ```
   Registry exists but no projects found.

   Create your first project:
   /bmad:creative-studio:workflows:init-creative-studio
   ```
   Then STOP workflow

---

## Data to Pass to Step 2

If registry has projects, pass:

```yaml
registry_data:
  version: "1.0.0"
  last_updated: "2025-12-14T12:30:00Z"
  active_project_id: "dua-pelaut-satu-lautan-2025-12-14T12-30-00Z"
  total_projects: 3

projects_list:
  - id: "..."
    name: "..."
    display_name: "..."
    type: "..."
    platform: "..."
    created: "..."
    status: "..."
    path: "..."
    pipeline: "..."
  # ... more projects
```

---

## Next Step

If projects exist, proceed to `step-02-display-projects.md` with the loaded data.
