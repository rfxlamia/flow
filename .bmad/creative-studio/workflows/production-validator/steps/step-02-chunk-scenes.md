# Step 02: Scene Chunking

**Goal:** Split scenes >8 seconds into 8-second segments with continuity.

**Scope:** Chunking logic only - prompt generation in step-03.

**Token Budget:** ~350 tokens

---

## INITIALIZATION

### Load Continuity System

**BEFORE chunking:** Load continuity tagging reference for tag system understanding:

```
Load: ../references/continuity-tagging.md
```

This defines:
- Continuity tag types (WARDROBE, LIGHTING, etc.)
- How to track elements across chunks
- Validation rules for seamless editing

---

## CHUNKING RULES

### The 8-Second Rule

Veo 3 generates maximum 8 seconds per clip. Every scene must be chunked:

| Scene Duration | Chunks Needed | Notes |
|----------------|---------------|-------|
| ≤8 seconds | 1 chunk | No split needed |
| 9-16 seconds | 2 chunks | ~8s each |
| 17-24 seconds | 3 chunks | ~8s each |
| 25-32 seconds | 4 chunks | ~8s each |
| >32 seconds | ceil(duration/8) | May need scene split |

**Formula:** `chunk_count = ceil(duration_seconds / 8)`

### Chunk Duration Guidelines

- **Optimal:** 8 seconds (maximum content per clip)
- **Acceptable:** 6-8 seconds
- **Avoid:** <6 seconds (feels rushed)
- **Never:** >8 seconds (will fail generation)

---

## CHUNKING PROCESS

### 1. Identify Scenes Needing Chunks

```
CHUNKING ANALYSIS:
Scene 1: 45s → 6 chunks needed
Scene 2: 30s → 4 chunks needed
Scene 3: 8s → 1 chunk (no split)
...
```

### 2. Distribute Action Across Chunks

For each scene requiring multiple chunks:

**Step A: Identify Natural Breaks**
- Look for action beats (pauses, transitions)
- Find visual anchor points (clear moments to end on)
- Maintain subject continuity

**Step B: Divide Action**
- First chunk: Establishing/introduction
- Middle chunks: Development/action
- Last chunk: Resolution/transition setup

**Step C: Create Continuation Setup**
- Each chunk (except last) ends with clear visual anchor
- Next chunk references this anchor for continuity

### 3. Chunk Template

For each chunk, create this structure:

```
CHUNK {scene_number}{letter} ({duration}s)
=====================================
Shot Type: {establishing/continuation/reveal/closeup}
Shot Relationship: {new/continues_from_{id}}
Camera Movement: {ONE movement only}

Action Summary:
{What happens in these 8 seconds}

Continuation Setup:
{How this chunk ends - visual anchor for next}

Key Visuals:
- {visual 1}
- {visual 2}
- {visual 3}
```

### 4. Continuity Tags

Tag each chunk's relationship:

| Relationship | When to Use |
|--------------|-------------|
| `new` | First chunk of scene, fresh start |
| `continues_from_{id}` | Direct continuation of previous |
| `match_cut_from_{id}` | Visual similarity to previous |
| `jump_cut_from_{id}` | Same subject, time skip |

### 5. Camera Movement Rule

**CRITICAL:** ONE camera movement per chunk maximum.

**Valid movements:**
- Static (subject moves, camera doesn't)
- Pan (horizontal rotation)
- Tilt (vertical rotation)
- Dolly (forward/backward)
- Track (side to side)
- Crane (up/down)
- Zoom (lens change)

**Invalid (split into multiple chunks):**
- Pan + Zoom
- Dolly + Tilt
- Any combination

---

## CHUNKING EXAMPLE

**Original Scene:**
```
Scene 5: 30 seconds
Sarah walks to frozen beach, places jacket on ice, stands watching horizon.
```

**Chunked:**
```
CHUNK 5a (8s) - new
Shot: Wide establishing
Camera: Slow dolly forward
Action: Sarah walks toward frozen beach, wind whipping coat
Continuation Setup: Sarah reaches edge of ice

CHUNK 5b (8s) - continues_from_5a
Shot: Medium
Camera: Static (subject moves)
Action: Sarah kneels, removes jacket from bag, places on ice
Continuation Setup: Jacket rests on ice, Sarah's hands smooth shoulders

CHUNK 5c (8s) - continues_from_5b
Shot: Wide/medium
Camera: Slow crane up
Action: Sarah stands, faces horizon, holds position
Continuation Setup: Silhouette against pale sky (transition ready)

CHUNK 5d (6s) - continues_from_5c
Shot: Close-up
Camera: Static
Action: Sarah's face, wind moving hair, eyes fixed on horizon
Continuation Setup: Hold for dissolve
```

---

## REFERENCE LOADING

**Load `references/chunking-workflow.md` when:**
- Complex scene with multiple subjects
- Unclear where to make cuts
- Need advanced continuity patterns

**Default:** Use embedded logic for standard scenes.

---

## OUTPUT: CHUNKING MAP

Prepare chunking data for step-03:

```
SCENE CHUNKING MAP
==================

Scene 1: 45s → 6 chunks (1a-1f)
Scene 2: 30s → 4 chunks (2a-2d)
Scene 3: 8s → 1 chunk (3a)
...

Total Chunks: {count}
Average Chunk Duration: {X}s

DETAILED CHUNK LIST:
[chunk templates for each]
```

---

## LOAD NEXT STEP

Execute: `Load step-03-generate-output.md`

---

**Proceed to Step 03 when all scenes are chunked.**
