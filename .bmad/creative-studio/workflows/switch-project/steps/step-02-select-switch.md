# Step 2: Select and Switch

**Purpose:** Prompt user to select a project and update the registry

---

## Instructions

1. **Prompt for selection:**

```
Which project would you like to activate?

Enter the number (1-{max}) or project ID:
>
```

2. **Accept input:**
   - **Number:** `1`, `2`, `3` → Maps to project index
   - **Project ID:** Full ID string → Find matching project
   - **Cancel:** `cancel`, `exit`, `q` → Abort without changes

3. **Validate input:**

   **If number:**
   - Check if in range (1 to total_projects)
   - Map to project by index

   **If project ID:**
   - Search projects list for matching ID
   - If not found, show error and re-prompt

   **If invalid:**
   ```
   ❌ Invalid selection. Please enter a number or project ID.
   ```
   Re-prompt.

4. **Check if already active:**

   If selected project is already active:
   ```
   ════════════════════════════════════════════════════════════

   ℹ️  This project is already active.

     → {project.id}
     "{project.display_name}"

   No changes made.

   ════════════════════════════════════════════════════════════
   ```
   STOP workflow.

5. **Update registry:**

   Modify `.bmad/creative-studio/_state/projects-registry.yaml`:

   ```yaml
   registry_version: "1.0.0"
   last_updated: "{current_timestamp}"  # Update this
   active_project: "{new_project_id}"    # Update this

   projects:
     # ... (no changes to project list)
   ```

6. **Confirm switch:**

```
════════════════════════════════════════════════════════════

✅ Active project switched successfully!

Previous Active:
  {previous_project_id}
  "{previous_display_name}"

Now Active:
  {new_project_id}
  "{new_display_name}"

────────────────────────────────────────────────────────────

All future workflow outputs will be saved to:
{new_project_path}/

To view project status:
/bmad:creative-studio:workflows:project-status

════════════════════════════════════════════════════════════
```

---

## Example Interaction

```
Which project would you like to activate?

Enter the number (1-3) or project ID:
> 2

════════════════════════════════════════════════════════════

✅ Active project switched successfully!

Previous Active:
  dua-pelaut-satu-lautan-2025-12-14T12-30-00Z
  "Dua Pelaut, Satu Lautan"

Now Active:
  music-video-test-2025-12-13T08-00-00Z
  "Music Video Test"

────────────────────────────────────────────────────────────

All future workflow outputs will be saved to:
docs/projects/music-video-test-2025-12-13T08-00-00Z/

To view project status:
/bmad:creative-studio:workflows:project-status

════════════════════════════════════════════════════════════
```

---

## Error Handling

**If registry file cannot be written:**
```
❌ ERROR: Unable to update projects registry.

Check file permissions:
.bmad/creative-studio/_state/projects-registry.yaml

No changes were made.
```

**If selected project path doesn't exist:**
```
⚠️  WARNING: Selected project activated, but project folder not found:

  {project.path}

The project exists in the registry but its files may have been moved or deleted.

Registry has been updated anyway. Create the folder structure if needed.
```

---

## Workflow Complete!

Registry updated, active project switched.
