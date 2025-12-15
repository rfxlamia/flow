# Step 02: Transform to Visual

**Goal:** Convert each metaphor into filmable visual equivalents while preserving emotional truth.

**Scope:** Transformation logic only - scene structure handled in step-03.

**Token Budget:** ~400 tokens (transformation logic + optional reference loading)

---

## LAZY REFERENCE LOADING

**Load reference ONLY if needed:**

| Situation | Load Reference |
|-----------|----------------|
| Complex emotion not in standard list | `references/visual-vocabulary.md` |
| Need detailed methodology for tricky metaphor | `references/transformation-methodology.md` |
| Simple/standard metaphor | NO reference needed - use embedded knowledge |

**Default:** Transform using embedded knowledge first. Only load references for edge cases.

---

## TRANSFORMATION PROCESS

### 1. For Each Metaphor, Apply This Framework

Take each metaphor from Step 01 and transform it:

**Question 1: What is the FEELING?**
Strip away the poetic language. What raw emotion remains?

**Question 2: What BEHAVIOR shows this feeling?**
How do humans physically express this emotion?

**Question 3: What ENVIRONMENT reinforces this feeling?**
Where would this emotion naturally occur or intensify?

**Question 4: What OBJECTS carry symbolic weight?**
What physical items could represent the emotion?

### 2. Standard Visual Translations

Use this reference for common emotion types:

| Emotion | Physical Behavior | Environment | Symbolic Objects |
|---------|------------------|-------------|------------------|
| **Longing/Waiting** | Returns to same spot; checks window/phone; keeps item from absent person | Transit points (train stations, beaches, doorways) | Letters, photos, clocks, empty chairs |
| **Worship/Devotion** | Ritualistic routines; serving without being asked; lowering self | Sacred spaces, altars, shrines, pedestals | Candles, offerings, memorabilia collections |
| **Grief/Loss** | Stillness; touching empty spaces; unable to change environment | Unchanged rooms; frozen-in-time spaces | Untouched belongings, unworn clothes |
| **Obsession** | Collecting; repetitive actions; deteriorating self-care | Cramped spaces full of items; single-focus environments | Collections, walls of photos, journals |
| **Abandonment Fear** | Checking behaviors; inability to be alone; startling at sounds | Doorways, windows, transitional spaces | Phones, keys, packed bags ready to leave |

### 3. Apply to Each Metaphor

For each metaphor from emotional core analysis:

```
METAPHOR: "[original metaphor]"
EMOTION: [underlying emotion]
VISUAL TRANSLATION:
  Behavior: [what character physically does]
  Environment: [where this happens]
  Objects: [what items are involved]

WHY THIS WORKS:
  [Explain connection between visual and emotion]

ALTERNATIVE CONSIDERED:
  [Another option that could work]
```

**Example:**
```
METAPHOR: "Aku menjadikanmu altar pribadi"
EMOTION: Worship-level devotion, treating beloved as sacred

VISUAL TRANSLATION:
  Behavior: Woman arranges photos and small items in corner of room each morning.
            Lights a candle. Sits before it briefly before starting day.
            Never lets anyone else enter this space.
  Environment: Small alcove or corner transformed into intimate shrine space.
               Soft morning light. Quiet, sacred atmosphere.
  Objects: Photographs, dried flowers, small mementos, single candle,
           items that belonged to the beloved.

WHY THIS WORKS:
  "Altar" becomes literal - a physical shrine space.
  Daily ritual shows ongoing worship, not past moment.
  Privacy (not letting others in) shows personal/sacred nature.

ALTERNATIVE CONSIDERED:
  Could show devotion through service behaviors (cooking their food,
  ironing their clothes) - but altar imagery is stronger.
```

### 4. Create Story Logic Map

Document ALL transformations in a table:

```
STORY LOGIC MAP
===============

| # | Original Metaphor | Emotional Core | Visual Translation | Why It Works |
|---|-------------------|----------------|-------------------|--------------|
| 1 | "..." | worship | shrine-building ritual | altar = literal shrine |
| 2 | "..." | longing | repeated returns to location | waiting made visible |
| 3 | "..." | grief | unchanged room frozen in time | loss = frozen space |
```

This map becomes part of the final output for transparency.

---

## FILMABILITY CHECK

For each visual translation, verify:

- [ ] **Action is VISIBLE:** Can a camera capture this?
- [ ] **No internal thoughts:** Not describing what character "thinks" or "feels"
- [ ] **Specific not vague:** "Woman stands at frozen beach at dawn" not "She is sad"
- [ ] **Time can pass:** Scene has clear beginning/middle/end potential
- [ ] **Objects are physical:** Real things that can be props

**If a translation fails any check:** Revise until it passes all checks.

---

## PRESERVE TONE

Maintain the original tone throughout:

| Original Tone | Visual Approach |
|---------------|-----------------|
| vulnerable_raw | Intimate close-ups; exposed emotions; minimal environment |
| poetic_mythic | Elevated visuals; symbolic imagery; timeless quality |
| theatrical_absurd | Exaggerated behaviors; surreal elements; heightened reality |
| nostalgic_epistolary | Warm colors; handwritten elements; past-present intercut |
| cinematic | Wide establishing shots; professional framing; genre-aware |

---

## OUTPUT: TRANSFORMATION DOCUMENT

Prepare this information for step-03:

```
VISUAL TRANSFORMATIONS
======================

ORIGINAL TONE: [tone]
PRESERVATION STRATEGY: [how we maintain this tone]

TRANSFORMATION 1:
  Metaphor: "[quote]"
  Visual: [full description]
  Why: [connection explanation]

TRANSFORMATION 2:
  ...

STORY LOGIC MAP:
[table format]

VISUAL ANCHORS FROM SOURCE:
[already-concrete elements to incorporate]

READY FOR SCENE BREAKDOWN: Yes
```

---

## LOAD NEXT STEP

Execute: `Load step-03-generate-scenes.md`

---

**Proceed to Step 03 when all metaphors are transformed to filmable visuals.**
