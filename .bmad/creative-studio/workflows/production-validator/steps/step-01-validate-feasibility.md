# Step 01: Validate Feasibility

**Goal:** Validate each scene for Veo 3 feasibility and identify risky elements.

**Scope:** Validation only - no modification yet.

**Token Budget:** ~300 tokens

---

## INPUT VERIFICATION

Verify you have loaded from screenwriter:

| Field | Required | Example |
|-------|----------|---------|
| `screenplay_file` | Yes | "workflows/screenwriter/outputs/screenplay-2025-12-13.md" |
| `scene_count` | Yes | 12 |
| `location_list` | Yes | [{name, type, scenes}] |
| `prop_list` | Yes | [{item, description, scenes}] |

**If missing:** Stop and inform user that screenwriter output is incomplete.

---

## FEASIBILITY VALIDATION

### 1. Parse Screenplay XML

For each `<scene>` tag, extract:
- `number` and `duration`
- `action` content
- `key_visuals`
- `characters`

### 2. Scan for Risky Elements

Check each scene's action against known risky elements:

**CRITICAL Risk (Will Fail):**
- [ ] Multiple camera movements in one take
- [ ] Impossible physics (flying without support, etc.)
- [ ] Conflicting simultaneous movements

**HIGH Risk (Likely to Fail):**
- [ ] Multiple objects moving independently
- [ ] Text or signage that must be readable
- [ ] Rapid scene changes within single shot
- [ ] More than 3 subjects in motion

**MEDIUM Risk (May Need Iteration):**
- [ ] Complex hand gestures or fine motor
- [ ] Character without visual reference image
- [ ] Dialogue + music together
- [ ] 2-3 subjects interacting

**LOW Risk (Should Work):**
- [ ] Single subject, simple motion
- [ ] Standard camera movement
- [ ] Clear visual anchors
- [ ] Static or slow movement

### 3. Calculate Risk Score

For each scene:
- Count CRITICAL elements × 4
- Count HIGH elements × 2
- Count MEDIUM elements × 1
- Sum = Risk Score

**Score interpretation:**
- 0: LOW risk
- 1-2: MEDIUM risk
- 3-4: HIGH risk
- 5+: CRITICAL risk

### 4. Document Risky Elements

For each risky element found:

```
SCENE {N}: {title}
Risk Score: {score} ({LOW/MEDIUM/HIGH/CRITICAL})

Risky Elements:
1. [RISK_LEVEL] {element description}
   - Location in action: "{quoted text}"
   - Suggested alternative: {AI-friendly version}

2. [RISK_LEVEL] {element description}
   ...
```

### 5. Reference Loading (If Needed)

**Load `references/veo3-knowledge-base.md` when:**
- Encountering unusual element not in quick reference
- Need detailed alternatives for complex issues
- User requests deeper explanation

**Default:** Use embedded quick reference for common issues.

---

## VALIDATION REPORT

Create validation document:

```
FEASIBILITY VALIDATION REPORT
=============================

Total Scenes: {count}
LOW Risk: {count} scenes
MEDIUM Risk: {count} scenes
HIGH Risk: {count} scenes
CRITICAL Risk: {count} scenes

OVERALL STATUS: {PASS / PASS_WITH_NOTES / NEEDS_REVISION}

SCENES REQUIRING ATTENTION:

Scene 3: "Title" - HIGH RISK
- [HIGH] Multiple objects in independent motion
  Alternative: Focus on single subject, others static background

Scene 7: "Title" - CRITICAL RISK
- [CRITICAL] Multiple camera movements (pan + zoom + track)
  Alternative: Split into multiple chunks, one movement each

[Continue for all HIGH/CRITICAL scenes]

AUTOMATIC PASSES:
Scenes 1, 2, 4, 5, 6, 8-12: LOW/MEDIUM risk, proceed as-is
```

---

## DECISION POINT

**If CRITICAL risk scenes exist:**
1. Present alternatives to user
2. Ask if they want to auto-apply fixes
3. Or proceed with warnings

**If only HIGH/MEDIUM risk:**
1. Note in production notes
2. Proceed to chunking
3. Iterate during generation if needed

---

## LOAD NEXT STEP

Execute: `Load step-02-chunk-scenes.md`

---

**Proceed to Step 02 when validation is complete.**
