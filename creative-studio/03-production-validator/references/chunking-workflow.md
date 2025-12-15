# Chunking Workflow

Detailed guide for splitting scenes into 8-second chunks with continuation prompts.

## The 8-Second Rule

Veo 3 generates a maximum of 8 seconds per generation. Any scene longer than 8 seconds must be chunked into segments that can be extended or stitched together.

### Chunking Decision Tree

```
scene_duration ≤ 8s
  └── NO CHUNKING NEEDED
      └── Single chunk output
      
scene_duration > 8s AND ≤ 16s
  └── SPLIT INTO 2 CHUNKS
      └── Chunk A: 8s (setup + action)
      └── Chunk B: remaining (continuation + resolution)
      
scene_duration > 16s
  └── SPLIT INTO N CHUNKS
      └── chunk_count = ceil(duration / 8)
      └── Distribute action across chunks
      └── Each chunk: ~8s (last chunk may be shorter)
```

---

## Chunk Anatomy

### Required Elements Per Chunk

```xml
<chunk id="[scene_number][letter]" duration="8s" continues_from="[previous_id]">
  <shot_type>[establishing/continuation/reveal/action/dialogue]</shot_type>
  <shot_relationship>[new/continues_from_X/match_cut_from_X]</shot_relationship>
  <action>[2-3 sentences describing what happens]</action>
  <veo3_prompt>[Full optimized prompt for Veo 3]</veo3_prompt>
  <camera_movement>[ONE movement only]</camera_movement>
  <continuation_setup>[Visual anchor for next chunk]</continuation_setup>
</chunk>
```

### Chunk ID Convention
- Scene 1, first chunk: `1a`
- Scene 1, second chunk: `1b`
- Scene 1, third chunk: `1c`
- Scene 2, first chunk: `2a`

---

## Chunking Process

### Step 1: Analyze Scene Content

Read the scene's action and identify:
1. **Key beats** - Major story moments
2. **Character entrances/exits** - Natural breakpoints
3. **Camera opportunities** - Where movement changes make sense
4. **Emotional shifts** - Pacing considerations

### Step 2: Calculate Chunk Count

```python
# Pseudo-code
scene_duration_seconds = parse_duration(scene.duration)  # "30s" → 30
chunk_count = math.ceil(scene_duration_seconds / 8)

# Example: 30s scene
# chunk_count = ceil(30 / 8) = ceil(3.75) = 4 chunks
```

### Step 3: Distribute Action

**Pacing Guidelines:**
| Chunk Position | Function | Duration | Notes |
|----------------|----------|----------|-------|
| First (Xa) | Establishing | 8s | Set scene, introduce subject |
| Middle (Xb-Xn) | Development | 8s each | Action, dialogue, progression |
| Last (Xz) | Resolution | 6-8s | Payoff, transition setup |

**Example: 30-second scene split into 4 chunks:**

```
Original action:
"Robot rolls across wasteland. Stops at rubble pile. 
Discovers tiny flower. Reaches toward it carefully."

Chunk distribution:
1a (8s): Establishing - "Wide shot of wasteland, robot visible in distance"
1b (8s): Approach - "Robot rolls toward camera, enters medium shot"
1c (8s): Discovery - "Robot stops at rubble, notices flower"
1d (6s): Resolution - "Close-up as robot reaches toward flower"
```

### Step 4: Define Continuation Points

Each chunk (except the last) needs a **continuation setup** - a clear visual anchor that the next chunk can reference.

**Good Continuation Setups:**
- Subject in stable pose at frame edge
- Clear environmental landmark visible
- Consistent lighting direction
- Subject facing specific direction

**Bad Continuation Setups:**
- Subject mid-motion (hard to match)
- Ambiguous framing
- Lighting about to change
- Subject obscured

---

## Continuation Prompt Generation

### Template Structure

```
[CONTINUATION from previous clip] 
[Shot type], [Subject with FULL visual description], 
[New action starting from continuation point], 
same [setting], maintain [lighting/atmosphere], 
[ONE camera movement]. 
Audio: [matching audio style]. 
negative prompt: no lighting change, no character drift, no style shift
```

### Example Continuation Prompt

**Chunk 1a ends with:**
```
continuation_setup: "Robot visible in medium shot, facing right, dust settling around treads"
```

**Chunk 1b prompt:**
```
[CONTINUATION from previous clip] Medium shot, boxy robot with weathered chrome body
and glowing blue optical sensor (same robot from previous), continues rolling right
across cracked asphalt, treads leaving marks in gray dust, same wasteland environment
with ruined skyscrapers in background, maintain golden hour lighting, static camera
as robot moves through frame. Audio: mechanical whirring, treads on gravel. 
negative prompt: no lighting change, no character appearance drift, no background shift
```

### Character Description Repetition

**CRITICAL:** Every continuation prompt must repeat the full character description to maintain consistency.

```
First appearance (chunk 1a):
"ROBOT (boxy frame, weathered chrome body, single blue optical sensor, 
mechanical treads, antenna on top)"

Continuation (chunk 1b):
"boxy robot with weathered chrome body and glowing blue optical sensor, 
mechanical treads, antenna on top" ← REPEAT ALL DETAILS

Continuation (chunk 1c):
"same weathered chrome robot with blue optical sensor, antenna visible" ← SHORTER OK but include key identifiers
```

---

## Chunk Types

### Establishing Chunk
- **Purpose:** Set scene, mood, environment
- **Typical shot:** Wide, establishing
- **Camera:** Slow movement (dolly in, crane, aerial reveal)
- **Subject:** May be absent or distant
- **Duration:** Full 8s

```xml
<chunk id="1a" duration="8s">
  <shot_type>establishing</shot_type>
  <shot_relationship>new</shot_relationship>
  <camera_movement>Slow crane down revealing landscape</camera_movement>
</chunk>
```

### Continuation Chunk
- **Purpose:** Continue action from previous
- **Typical shot:** Medium, follows previous framing
- **Camera:** Match previous momentum or introduce new
- **Subject:** Same as previous, may move
- **Duration:** Full 8s

```xml
<chunk id="1b" duration="8s" continues_from="1a">
  <shot_type>continuation</shot_type>
  <shot_relationship>continues_from_1a</shot_relationship>
  <camera_movement>Tracking shot following subject</camera_movement>
</chunk>
```

### Reveal Chunk
- **Purpose:** Show something new, important
- **Typical shot:** Push in, close-up
- **Camera:** Dolly in, focus pull
- **Subject:** The revealed element
- **Duration:** 6-8s (can be shorter for punch)

```xml
<chunk id="1c" duration="8s" continues_from="1b">
  <shot_type>reveal</shot_type>
  <shot_relationship>continues_from_1b</shot_relationship>
  <camera_movement>Slow dolly in to close-up</camera_movement>
</chunk>
```

### Dialogue Chunk
- **Purpose:** Character speech
- **Typical shot:** Medium, close-up
- **Camera:** Often static for lip-sync quality
- **Subject:** Speaking character
- **Duration:** Full 8s (dialogue timing)

```xml
<chunk id="2a" duration="8s">
  <shot_type>dialogue</shot_type>
  <shot_relationship>new</shot_relationship>
  <camera_movement>Static medium shot</camera_movement>
</chunk>
```

### Action Chunk
- **Purpose:** Physical action, movement
- **Typical shot:** Wide to medium
- **Camera:** Dynamic (tracking, handheld)
- **Subject:** Character in motion
- **Duration:** Full 8s

```xml
<chunk id="3b" duration="8s" continues_from="3a">
  <shot_type>action</shot_type>
  <shot_relationship>continues_from_3a</shot_relationship>
  <camera_movement>Tracking shot following runner</camera_movement>
</chunk>
```

---

## Edge Cases

### Scene Exactly 8 Seconds
No chunking needed, but still generate full validation:

```xml
<chunk id="1a" duration="8s">
  <!-- All standard fields -->
  <continuation_setup>N/A - single chunk scene</continuation_setup>
</chunk>
```

### Scene Under 8 Seconds
Pad to 6-8 seconds by extending establishing or holding final moment:

```
Original: 5s scene
Options:
1. Add 3s establishing shot at start
2. Hold final frame 3s longer
3. Slow down action timing
```

### Very Long Scene (40+ seconds)
Split into logical acts, consider natural breakpoints:

```
40s emotional scene:
1a (8s): Character enters, establishes mood
1b (8s): Discovers letter, reads it
1c (8s): Emotional reaction builds
1d (8s): Breaks down crying
1e (8s): Recovers, makes decision
```

### Dialogue-Heavy Scene
Prioritize lip-sync quality, may need shorter chunks:

```
30s dialogue scene:
1a (8s): Character A speaks first line
1b (8s): Character B responds
1c (8s): Character A's emotional response
1d (6s): Final exchange, resolution
```

---

## Validation Checklist

Before finalizing chunks:

- [ ] All chunks ≤ 8 seconds
- [ ] Each chunk has ONE camera movement
- [ ] Continuation setups are clear visual anchors
- [ ] Character descriptions repeated in every chunk
- [ ] No action split mid-motion between chunks
- [ ] Lighting consistent across chunk sequence
- [ ] Audio style matches throughout
- [ ] Negative prompts included for consistency
