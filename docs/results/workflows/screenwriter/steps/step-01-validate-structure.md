# Step 01: Validate Scene Structure

**Goal:** Validate scene breakdown from storyteller and prepare for formatting.

**Scope:** Validation only - no formatting yet.

**Token Budget:** ~250 tokens

---

## INPUT VERIFICATION

Verify you have loaded from storyteller:

| Field | Required | Example |
|-------|----------|---------|
| `scene_breakdown_file` | Yes | "workflows/storyteller/outputs/scenes-2025-12-13.md" |
| `total_scenes` | Yes | 12 |
| `characters` | Yes | [{name: "Sarah", description: "..."}] |
| `locations` | Yes | ["Frozen beach", "Small apartment"] |
| `emotional_arc` | Yes | "hope → despair → acceptance" |

**If missing:** Stop and inform user that storyteller output is incomplete.

---

## SCENE VALIDATION

### 1. Count Verification

Compare actual scenes in markdown with `total_scenes` field:

- Count number of "### Scene" headings
- Verify matches expected count
- If mismatch: Warn user, proceed with actual count

### 2. Scene Content Check

For each scene, verify it contains:

- [ ] Location specified
- [ ] Time of day specified
- [ ] Visual action described (not just dialogue)
- [ ] Key visuals listed
- [ ] Emotional beat defined

**Missing elements:** Note which scenes need enhancement.

### 3. Character Consistency

Check character references:

- [ ] All characters mentioned in scenes are in character list
- [ ] No new characters appear without description
- [ ] Names are consistent (no "Sarah" vs "Sara")

### 4. Location Extraction

Build complete location list:

```
LOCATIONS IDENTIFIED:
1. [Location] - INT/EXT decision - Time(s) used
2. [Location] - INT/EXT decision - Time(s) used
...
```

### 5. Duration Estimation

Verify scene durations add up:

- Sum all individual scene durations
- Compare to target (5-10 minutes = 300-600 seconds)
- Adjust if total is too long/short

---

## VALIDATION REPORT

Create mental validation document:

```
SCENE STRUCTURE VALIDATION
==========================

Input File: [path]
Expected Scenes: [count]
Actual Scenes: [count]
Status: [PASS/MISMATCH]

CONTENT COMPLETENESS:
- Scenes with all elements: [X of Y]
- Scenes needing enhancement: [list]

CHARACTER CONSISTENCY:
- Total characters: [count]
- Consistency: [PASS/ISSUES]
- Issues: [if any]

LOCATIONS:
[numbered list with INT/EXT decisions]

DURATION CHECK:
- Total estimated: [X seconds / Y minutes]
- Target: 5-10 minutes
- Status: [PASS/ADJUST]

READY FOR FORMATTING: [Yes/No]
```

---

## ENHANCEMENT DECISIONS

If scenes need enhancement:

**Option 1: Minimal Enhancement**
- Add only required missing elements
- Don't change existing content
- Quick path to formatted output

**Option 2: Full Enhancement**
- Enrich visual descriptions
- Add atmosphere details
- Load `references/advanced-techniques.md`
- Better for final production quality

**Default:** Option 1 (minimal) unless user requests full enhancement.

---

## LOAD NEXT STEP

Execute: `Load step-02-apply-formatting.md`

---

**Proceed to Step 02 when validation is complete.**
