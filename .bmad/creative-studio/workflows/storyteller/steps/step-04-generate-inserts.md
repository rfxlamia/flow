# Step 04: Generate Atmospheric Inserts

**Goal:** Create atmospheric insert shots that provide emotional breathing room and texture-based storytelling.

**Scope:** Insert generation, placement strategy, XML structure for screenwriter.

**Token Budget:** ~200 tokens

---

## WHAT ARE ATMOSPHERIC INSERTS?

Brief 2-4 second micro-scenes that:
- Provide emotional breathing room between main scenes
- Add texture-based storytelling through environmental details
- Reinforce visual metaphors and symbolic progression
- Create cinematic depth through sensory detail

**NOT action-driven** - These are contemplative, texture-focused moments.

---

## INSERT GENERATION PROCESS

### 1. Identify Insert Opportunities

For each babak/act in the story, identify 4-6 insert opportunities:

| Placement | Purpose | Example |
|-----------|---------|---------|
| Pre-scene | Set atmosphere before action | Decay detail before character appears |
| Mid-scene | Emotional punctuation | Hands gripping during tension |
| Post-scene | Lingering resonance | Empty space after departure |

### 2. Apply Insert Categories

**Load reference if needed:** `./references/insert-categories.md`

**Core Categories:**

| Category | Emotional Function | Visual Focus |
|----------|-------------------|--------------|
| Decay | Loss, passage of time | Peeling, rusting, weathering |
| Intimacy | Connection, warmth | Hands, shared objects, proximity |
| Strain | Tension, breaking point | Fraying, stretching, overflowing |
| Absence | Grief, emptiness | Empty spaces, ghost presence |

### 3. Track Texture Progression

Map texture evolution across the story:

```
Babak I:   Rough/Decayed → Establish broken world
Babak II:  Soft/Warm → Intimacy growing
Babak III: Fraying/Neglected → Relationship strain
Babak IV:  Ghostly/Empty → Absence and grief
```

---

## INSERT TEMPLATE

For each insert, generate:

```xml
<insert
  id="INSERT-{babak}-{number}"
  category="{decay|intimacy|strain|absence}"
  duration="2-4s"
  placement="{pre|mid|post}"
  scene_context="{scene_number}">

  <shot_type>{ECU|CU|Detail|Wide}</shot_type>
  <description>{Specific visual description - what camera sees}</description>
  <texture>{Primary texture/material focus}</texture>
  <mood>{Emotional quality}</mood>
  <purpose>{Why this insert matters to the story}</purpose>
  <symbolic>{What it represents metaphorically}</symbolic>

</insert>
```

---

## GENERATION RULES

### Quality Standards

- [ ] Each insert is NON-NARRATIVE (no character action)
- [ ] Focus on texture, not movement
- [ ] 2-4 second duration (still image or minimal motion)
- [ ] Clear emotional function
- [ ] Supports story arc progression

### Distribution Guidelines

- 4-6 inserts per babak/act
- Balance categories across story
- Ensure progression from rough → soft → fraying → empty
- Placement variety (mix pre/mid/post)

### Sensory Mapping

Track visual themes across inserts:
- **Water motif:** Aggressive → Calm → Leak → Dead calm
- **Color temp:** Cool/harsh → Warm/golden → Desaturating → Colorless
- **Texture:** Intact → Fraying → Breaking → Absent

---

## OUTPUT FORMAT

Add inserts section to scene breakdown output:

```markdown
## Atmospheric Inserts

### Babak I: [Title] (5 inserts)

<insert id="INSERT-1-01" category="decay" duration="2-3s" placement="pre" scene_context="1">
  <shot_type>ECU</shot_type>
  <description>Peeling blue paint on boat hull, salt crystallized in cracks</description>
  <texture>Weathered wood, salt deposits, paint chips</texture>
  <mood>Harsh, decayed, abandoned</mood>
  <purpose>Establish broken soul before protagonist appears</purpose>
  <symbolic>Years of neglect and isolation</symbolic>
</insert>

[Continue for all inserts...]
```

---

## HANDOFF TO SCREENWRITER

Inserts are passed as separate XML blocks for:
- Different chunking strategy (2-4s vs 8s scenes)
- Different production path (Imagen stills vs Veo video)
- Clear separation from narrative scenes

---

## PROCEED TO COMPLETION

After generating all inserts:
1. Add inserts section to scene breakdown file
2. Update pipeline state with insert count
3. Return to step-03 completion flow

---

**Insert generation complete. Atmospheric texture layer added to story.**
