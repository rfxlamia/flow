# Step 3: Register Project

**Purpose:** Add the new project to the global registry and set it as active

---

## Instructions

Register the newly created project in Creative Studio's project tracking system.

### Registry File Location

`.bmad/creative-studio/_state/projects-registry.yaml`

---

## Registry Structure

The registry maintains a list of all creative projects and tracks the currently active one.

### If Registry Doesn't Exist

Create new file with this structure:

```yaml
# Creative Studio Projects Registry
# Tracks all creative projects across the workspace

registry_version: "1.0.0"
last_updated: "{current_timestamp}"

active_project: "{project_id}"  # Currently active project

projects:
  - id: "{project_id}"
    name: "{project_name}"
    display_name: "{display_name}"
    type: "{content_type}"
    platform: "{target_platform}"
    created: "{timestamp}"
    status: "initialized"
    path: "docs/projects/{project_id}"
    pipeline: "{pipeline_type}"
    pipeline_state: "docs/projects/{project_id}/pipeline-state.yaml"
    current_stage: 0
    stages_completed: []
```

### If Registry Already Exists

1. **Update `last_updated`** with current timestamp
2. **Update `active_project`** to new project ID
3. **Append to `projects` array:**

```yaml
  - id: "{project_id}"
    name: "{project_name}"
    display_name: "{display_name}"
    type: "{content_type}"
    platform: "{target_platform}"
    created: "{timestamp}"
    status: "initialized"
    path: "docs/projects/{project_id}"
    pipeline: "{pipeline_type}"
    pipeline_state: "docs/projects/{project_id}/pipeline-state.yaml"
    current_stage: 0
    stages_completed: []
```

---

## Project ID Format

```
{project_name}-{timestamp}
```

Example: `dua-pelaut-satu-lautan-2025-12-14T12-30-00Z`

---

## Active Project Concept

The **active project** is where all subsequent workflow outputs will be saved by default. This means:

- Running `diverse-content-gen` will output to `{active_project}/01-diverse/`
- Running `storyteller` will output to `{active_project}/02-storyteller/`
- And so on...

Other workflows in the pipeline will automatically read the `active_project` from this registry to know where to save outputs.

---

## Update Project Config

Also update the newly created project's `project-config.yaml`:

```yaml
status: "initialized"  # → "active"
```

---

## Confirmation Output

After registration, display to user:

```
✅ Project registered successfully!

Project ID: {project_id}
Location: {full_path}
Status: Active

All future workflow outputs will be saved to this project.

Next Steps:
1. Run /bmad:creative-studio:workflows:diverse-content-gen
   to generate creative content variations

2. Continue through the pipeline based on your content type
```

---

## Example Registry After Multiple Projects

```yaml
registry_version: "1.0.0"
last_updated: "2025-12-14T15:45:00Z"

active_project: "new-music-video-2025-12-14T15-00-00Z"

projects:
  - id: "dua-pelaut-satu-lautan-2025-12-13T09-00-00Z"
    name: "dua-pelaut-satu-lautan"
    display_name: "Dua Pelaut, Satu Lautan"
    type: "video"
    platform: "youtube"
    created: "2025-12-13T09:00:00Z"
    status: "completed"
    path: "docs/projects/dua-pelaut-satu-lautan-2025-12-13T09-00-00Z"
    pipeline: "video-full"

  - id: "new-music-video-2025-12-14T15-00-00Z"
    name: "new-music-video"
    display_name: "New Music Video Project"
    type: "video"
    platform: "instagram"
    created: "2025-12-14T15:00:00Z"
    status: "active"
    path: "docs/projects/new-music-video-2025-12-14T15-00-00Z"
    pipeline: "video-full"
```

---

## Future Enhancement: Switch Active Project

In future versions, you'll be able to run:
```
/bmad:creative-studio:switch-project
```

To change which project is active without creating a new one.

---

## Workflow Complete!

After this step, the init-creative-studio workflow is complete.

**User is ready to start creating content!**
