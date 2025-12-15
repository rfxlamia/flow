# Continuity Tagging System

Reference for shot relationships, transition types, and editing metadata.

## Table of Contents
- [Shot Relationships](#shot-relationships)
- [Transition Types](#transition-types)
- [Editing Notes Format](#editing-notes-format)
- [Continuity Elements](#continuity-elements)
- [Shot Type Reference](#shot-type-reference)
- [Scene Continuity Tags](#scene-continuity-tags)
- [Match Cut Opportunities](#match-cut-opportunities)
- [Audio Continuity](#audio-continuity)
- [Quick Reference](#quick-reference-continuity-codes)

## Shot Relationships

### Relationship Types

| Type | Code | Description | Use Case |
|------|------|-------------|----------|
| New | `new` | Fresh scene start | Scene opening, new location |
| Continues | `continues_from_[id]` | Direct continuation | Same action, same shot |
| Match Cut | `match_cut_from_[id]` | Visual match to previous | Shape/motion similarity |
| Jump Cut | `jump_cut_from_[id]` | Same subject, time skip | Same angle, different time |
| Cutaway | `cutaway_from_[id]` | Different angle, returns | Reaction shot, detail insert |
| Cross Cut | `cross_cut_from_[id]` | Parallel action | Intercut between scenes |

### Relationship Decision Tree

```
Is this the first chunk of a scene?
├── YES → shot_relationship: "new"
└── NO → Does it continue the same shot/motion?
    ├── YES → shot_relationship: "continues_from_[previous_id]"
    └── NO → Is there a visual match (shape, motion, color)?
        ├── YES → shot_relationship: "match_cut_from_[previous_id]"
        └── NO → Is it the same subject, different time?
            ├── YES → shot_relationship: "jump_cut_from_[previous_id]"
            └── NO → Is it a reaction/detail shot?
                ├── YES → shot_relationship: "cutaway_from_[main_id]"
                └── NO → shot_relationship: "cross_cut_from_[parallel_id]"
```

---

## Transition Types

### Standard Transitions

| Transition | XML Tag | Description | When to Use |
|------------|---------|-------------|-------------|
| Hard Cut | `hard_cut` | Instant switch | Default, most edits |
| Dissolve | `dissolve` | Gradual blend | Time passage, mood shift |
| Fade Out | `fade_out` | Fade to black | Scene end, act break |
| Fade In | `fade_in` | Fade from black | Scene start, new act |
| Wipe | `wipe_[direction]` | Stylized sweep | Stylistic choice |
| Match Cut | `match_dissolve` | Blended match | Dream sequences |

### Transition Guidelines

**Hard Cut (default):**
- Use for: Most scene continuations
- Avoid when: Major time/location change

**Dissolve:**
- Duration: 1-2 seconds
- Use for: Time passage (hours, days)
- Use for: Emotional transition
- Use for: Dream/memory sequences

**Fade:**
- Duration: 1-3 seconds
- Fade Out: End of act, major scene break
- Fade In: Beginning of new section
- Combined (Fade Out → Fade In): Complete scene change

---

## Editing Notes Format

### Standard Editing Notes Structure

```xml
<editing_notes>
  - [Flow description]: Chunks [ids] flow [continuously/with cuts]
  - [Cut type]: [description of transition between specific chunks]
  - [Hold instruction]: [frame to hold for transition]
  - [Continuity reminder]: [character/setting consistency notes]
  - [Audio note]: [sound continuity or transition]
  - [Special instruction]: [any unique editing requirement]
</editing_notes>
```

### Example Editing Notes

```xml
<editing_notes>
  - Chunks 1a-1c flow continuously over 24 seconds (single scene)
  - Smooth cuts between all chunks (maintain spatial continuity)
  - 1a→1b: Match robot position at frame edge
  - 1b→1c: Robot stops, hold for 0.5s before cut
  - Final frame (flower close-up) holds 2s for dissolve to Scene 2
  - Character consistency: Repeat "boxy robot, weathered chrome, blue sensor"
  - Audio: Wind ambient consistent throughout, add servo whir on chunk 1c
  - Pacing note: Scene 1 is contemplative, maintain slow rhythm
</editing_notes>
```

---

## Continuity Elements

### Visual Continuity Checklist

For each chunk transition, verify:

| Element | Check | Notes |
|---------|-------|-------|
| Subject position | Match frame position | Left→Left, Right→Right |
| Subject facing | Match eye line | If facing right, continue right |
| Lighting direction | Match key light | Sun position consistent |
| Color palette | Match grade | Same 3-5 anchor colors |
| Background elements | Match visible landmarks | Same buildings, terrain |
| Weather | Match conditions | Same rain, fog, sun |
| Time of day | Match shadows | Same sun angle |
| Costume/props | Match exactly | Same clothing, items |

### 180-Degree Rule

Maintain screen direction across chunks:

```
Scene layout:
  [A] ←→ [B]
     camera

If A is on LEFT in chunk 1, keep A on LEFT in chunk 2.
Crossing the line causes spatial confusion.
```

### Eyeline Match

For dialogue/interaction scenes:

```
Chunk 1: Character A looks RIGHT →
Chunk 2: Character B looks ← LEFT (toward A's position)
```

---

## Shot Type Reference

### Establishing Shots

```xml
<shot_type>establishing</shot_type>
```
- Wide or extreme wide
- Sets location, mood, time
- Often first chunk of scene
- May not include main subject

### Medium Shots

```xml
<shot_type>medium</shot_type>
```
- Waist-up framing
- Standard dialogue coverage
- Subject and some environment

### Close-ups

```xml
<shot_type>close_up</shot_type>
```
- Face or detail
- Emotional emphasis
- Important objects

### Over-the-Shoulder (OTS)

```xml
<shot_type>ots</shot_type>
```
- Dialogue coverage
- Shows relationship
- Includes back of one subject

### Point of View (POV)

```xml
<shot_type>pov</shot_type>
```
- What character sees
- Subjective camera
- First-person perspective

### Insert

```xml
<shot_type>insert</shot_type>
```
- Detail shot
- Hands, objects, screens
- Cutaway material

---

## Scene Continuity Tags

### Within-Scene Continuity

When chunks belong to same continuous scene:

```xml
<chunk id="1a">
  <shot_relationship>new</shot_relationship>
  <editing_transition>to_1b:hard_cut</editing_transition>
</chunk>

<chunk id="1b" continues_from="1a">
  <shot_relationship>continues_from_1a</shot_relationship>
  <editing_transition>to_1c:hard_cut</editing_transition>
</chunk>

<chunk id="1c" continues_from="1b">
  <shot_relationship>continues_from_1b</shot_relationship>
  <editing_transition>to_scene_2:dissolve</editing_transition>
</chunk>
```

### Cross-Scene Continuity

When transitioning between scenes:

```xml
<!-- End of Scene 1 -->
<chunk id="1c">
  <editing_transition>to_scene_2:dissolve:2s</editing_transition>
</chunk>

<!-- Start of Scene 2 -->
<chunk id="2a">
  <shot_relationship>new</shot_relationship>
  <!-- New scene, fresh start -->
</chunk>
```

---

## Match Cut Opportunities

### Visual Match Types

| Match Type | Description | Example |
|------------|-------------|---------|
| Shape | Similar shapes | Wheel → Sun |
| Motion | Similar movement | Bird flying → Plane |
| Color | Color continuity | Red dress → Red flower |
| Size | Scale match | Eye → Planet |
| Position | Frame position | Subject stays center |

### Match Cut Tagging

```xml
<chunk id="1c">
  <editing_transition>match_cut_to_2a</editing_transition>
  <match_element>circular_shape:robot_eye</match_element>
</chunk>

<chunk id="2a">
  <shot_relationship>match_cut_from_1c</shot_relationship>
  <match_element>circular_shape:sun_rising</match_element>
</chunk>
```

---

## Audio Continuity

### Audio Transition Types

| Type | Description | Tag |
|------|-------------|-----|
| Continuous | Same audio across cut | `audio:continuous` |
| Shift | Audio changes at cut | `audio:shift` |
| Overlap | Audio bridges cut | `audio:overlap:[seconds]` |
| Silent | Intentional silence | `audio:silent` |

### Audio Notes in Editing

```xml
<editing_notes>
  - Audio: Wind ambient carries through chunks 1a-1c
  - Audio: Dialogue starts in 1b, music fades under
  - Audio: 1c ends with rising score, carries into Scene 2
  - Audio: Hard sound cut at scene break (no overlap)
</editing_notes>
```

---

## Quick Reference: Continuity Codes

### Relationship Codes
- `new` - New scene/shot
- `cont:[id]` - Continues from
- `match:[id]` - Match cut from
- `jump:[id]` - Jump cut from
- `cut:[id]` - Cutaway from
- `cross:[id]` - Cross cut from

### Transition Codes
- `hard` - Hard cut (default)
- `diss:[s]` - Dissolve with duration
- `fade_out:[s]` - Fade to black
- `fade_in:[s]` - Fade from black
- `wipe:[dir]` - Wipe with direction

### Hold Codes
- `hold:[s]` - Hold frame for seconds
- `freeze:[s]` - Freeze frame
- `slow:[%]` - Slow to percentage
