# Veo 3 Knowledge Base

Comprehensive reference for Veo 3/3.1 capabilities, limitations, and feasibility scoring.

## Technical Specifications

**Duration:**
- Maximum: 8 seconds per generation (hard limit)
- Extension: +7-8 seconds per hop via Extend feature
- Maximum extended: ~148 seconds (20 extension hops)

**Resolution:**
- Standard: 720p or 1080p at 24 fps
- Aspect ratios: 16:9 (landscape), 9:16 (vertical)
- 4K available via upscaling (may introduce artifacts)

**Audio:**
- Native dialogue generation with lip-sync
- Ambient sounds and SFX
- Background music
- Limitation: Complex dialogue + music in same 8s = risky

---

## Capabilities Matrix

### What Veo 3 Handles WELL (LOW Risk)

| Capability | Details | Prompt Tips |
|------------|---------|-------------|
| Single subject focus | One main character/object | Put subject in first 50 words |
| Basic camera movements | Dolly, pan, tilt, static | ONE movement per 8s chunk |
| Physics simulation | Water, fabric, smoke, fire | Be specific about physics behavior |
| Lighting control | Natural, cinematic, multiple sources | Specify color temperature |
| Simple motion | Walk, sit, stand, reach | Use clear action verbs |
| Environmental detail | Weather, atmosphere, particles | Include ambient audio |
| Lip-sync dialogue | Character speech | Use "Character says: [text]" format |

### What Veo 3 Handles MODERATELY (MEDIUM Risk)

| Capability | Details | Mitigation |
|------------|---------|------------|
| 2-3 subjects | Multiple characters interacting | Clearly define spatial relationships |
| Hand close-ups | Fingers, gestures | Simplify to basic poses |
| Character consistency | Same person across shots | Repeat visual description in every prompt |
| Complex camera moves | Crane, arc, tracking | Use precise cinematic terminology |
| Slow motion | Time manipulation | Avoid with fast action |
| Eye contact direction | Characters looking at each other | Add explicit interaction cues |

### What Veo 3 Handles POORLY (HIGH Risk)

| Limitation | Why It Fails | AI-Friendly Alternative |
|------------|--------------|------------------------|
| Multiple objects in motion | Objects morph, distort, vanish | Focus on ONE moving subject per beat |
| Text in scene | Garbled, nonsense characters | Remove text, add in post-production |
| Complex interactions | Characters touching, fighting | Simplify to reaction shots |
| Rapid scene changes | Continuity breaks | Extend individual beats |
| Extreme slow-mo + fast action | Temporal artifacts | Choose one speed |
| 60fps output | Motion artifacts | Stay at 24fps cinema standard |

### What Veo 3 CANNOT Do (CRITICAL Risk)

| Limitation | Technical Reason | Workaround |
|------------|------------------|------------|
| Multiple camera movements | Conflicting direction vectors | ONE movement per chunk |
| Shots >8 seconds | Hard generation limit | Use extension/chaining |
| Perfect character consistency | No persistent identity model | Use reference images + repeat descriptions |
| Accurate text rendering | Limited OCR training | Composite text in post |
| Complex physics interactions | Not a physics engine | Simplify or use practical effects |

---

## Risky Elements Catalog

### CRITICAL (Will Fail - Must Fix)

| Element | Pattern to Detect | Fix |
|---------|-------------------|-----|
| Multiple camera movements | "dolly in while panning" | Choose ONE movement |
| Conflicting time/lighting | "midnight" + "golden hour" | Make consistent |
| >8 second continuous action | Scene duration exceeds limit | Chunk into segments |
| Explicit violence/gore | Combat wounds, blood | Abstract or cutaway |
| Copyrighted characters | Named IP references | Create original characters |

### HIGH (Likely to Fail - Should Fix)

| Element | Pattern to Detect | Fix |
|---------|-------------------|-----|
| Multiple moving objects | "cars racing", "crowd running" | Focus on single subject |
| Visible text/signs | "reads the sign", "billboard shows" | Remove from prompt |
| Complex hand choreography | "intricate gestures", "typing" | Simplify to basic poses |
| Rapid cuts in single prompt | "cut to", "smash cut" | Separate into chunks |
| Character transformation | "morphs into", "changes to" | Use dissolve transition |
| Detailed UI/screens | "computer screen shows" | Add in post |

### MEDIUM (May Need Iteration)

| Element | Pattern to Detect | Mitigation |
|---------|-------------------|------------|
| 2-3 subjects interacting | Multiple character names | Define clear spatial positions |
| Dialogue + music | Both specified | Prioritize one, add other in post |
| Character without anchor | Generic description | Add 3-5 distinctive visual traits |
| Complex lighting setup | 3+ light sources | Simplify to key + fill |
| Specific lens effects | "anamorphic flares" | May not render accurately |
| Precise timing | "at exactly 4 seconds" | Use beat structure instead |

### LOW (Generally Safe)

| Element | Why It Works |
|---------|--------------|
| Single subject | Model optimization |
| One camera movement | Clear direction vector |
| Simple action verbs | Well-trained vocabulary |
| Standard lighting | Common in training data |
| Static + enter/exit | Simple spatial logic |
| Natural physics | Emergent capability |

---

## Prompt Optimization Patterns

### Structure (Recommended Order)
```
1. Shot type + Camera    : "Close-up shot, slow dolly in"
2. Subject               : "young woman with dark hair, blue coat"
3. Action                : "turns to face the window"
4. Setting               : "inside minimalist apartment"
5. Lighting              : "soft natural light from large windows"
6. Style                 : "cinematic, warm color grade"
7. Audio                 : "ambient city sounds, soft piano"
8. Constraints           : "negative prompt: no text, no artifacts"
```

### Continuation Prompt Template
```
[CONTINUATION from previous clip] [Shot type], [Subject with REPEATED visual 
anchors], [New action continuing from last frame], same [setting/environment], 
maintain [lighting/atmosphere], [camera movement]. Audio: [matching sound design].
negative prompt: no lighting change, no character drift, no style shift
```

### Character Consistency Anchors
Always include in every chunk prompt:
- Physical build/height
- Hair color/style
- Clothing description (specific colors)
- Distinctive features (scars, glasses, etc.)
- Color palette association

Example: "tall woman with shoulder-length auburn hair, wearing olive green jacket over white blouse, round glasses, freckles"

---

## Extension/Chaining Best Practices

### Frame-to-Video Technique
1. Generate first 8s clip
2. Screenshot last frame
3. Use as seed for next clip
4. Repeat character description in new prompt
5. Add "[CONTINUATION]" prefix
6. Match lighting, color palette, camera height

### Extend Feature (Flow)
- Adds 7-8s per extension
- Uses last second as context
- Best for establishing shots, simple motion
- Less reliable for dialogue scenes
- May drop to Veo 2 quality without sound

### Continuity Checklist
- [ ] Character appearance matches previous chunk
- [ ] Lighting direction consistent
- [ ] Color palette maintained (3-5 anchor colors)
- [ ] Camera height/angle logical continuation
- [ ] Audio style matching
- [ ] No conflicting environmental changes

---

## Risk Scoring Algorithm

### Calculate Scene Risk Score

```
CRITICAL elements = 0
HIGH elements = 0
MEDIUM elements = 0

FOR each element in scene:
  IF matches CRITICAL pattern: CRITICAL += 1
  IF matches HIGH pattern: HIGH += 1
  IF matches MEDIUM pattern: MEDIUM += 1

IF CRITICAL > 0:
  risk_score = "CRITICAL"
  safe_for_veo3 = false
ELSE IF HIGH > 1:
  risk_score = "HIGH"
  safe_for_veo3 = false
ELSE IF HIGH == 1 OR MEDIUM > 2:
  risk_score = "MEDIUM"
  safe_for_veo3 = true (with warnings)
ELSE:
  risk_score = "LOW"
  safe_for_veo3 = true
```

### Output Format
```xml
<feasibility_check>
  <risk_score>MEDIUM</risk_score>
  <risky_elements>
    <element risk="MEDIUM" line="5">2 characters interacting - define spatial positions</element>
    <element risk="LOW" line="8">Single camera movement - optimal</element>
  </risky_elements>
  <recommendations>
    <rec priority="1">Add explicit positions: "Sarah on left, facing right; Tom on right, facing left"</rec>
  </recommendations>
  <safe_for_veo3>true</safe_for_veo3>
</feasibility_check>
```

---

## Camera Movement Reference

### Veo 3 Validated Movements

| Movement | Description | Veo 3 Performance |
|----------|-------------|-------------------|
| Dolly in/out | Forward/backward on track | ✅ Excellent |
| Pan left/right | Horizontal rotation | ✅ Excellent |
| Tilt up/down | Vertical rotation | ✅ Good |
| Tracking shot | Follow subject laterally | ✅ Good |
| Crane up/down | Vertical boom movement | ✅ Good |
| Arc left/right | Curved path around subject | ⚠️ Moderate |
| Static | No movement | ✅ Excellent |
| Handheld | Subtle shake | ⚠️ Moderate |
| Aerial/drone | High angle movement | ✅ Good |
| POV | First-person perspective | ⚠️ Moderate |

### Movement Conflicts (NEVER Combine)
- Dolly + Pan (conflicting vectors)
- Crane + Tilt (redundant vertical)
- Arc + Tracking (conflicting curves)
- Zoom + Dolly (lens vs physical)

### Movement Per Beat Rule
```
✅ CORRECT: "Slow dolly in over 8 seconds"
❌ WRONG: "Dolly in while panning left and tilting up"
```

---

## Audio Guidelines

### Native Audio Types
- **Dialogue**: Character speech with lip-sync
- **Ambient**: Environmental sounds (wind, traffic, nature)
- **SFX**: Specific sound effects (footsteps, doors, impacts)
- **Music**: Background score (genre, mood, tempo)

### Audio Prompt Format
```
Audio: [ambient description], [specific SFX], [music if needed]
```

### Audio Limitations
- Complex dialogue + detailed music = pick one
- Very specific music tracks = unlikely to match
- Real song references = will generate similar style, not actual song

### Audio Best Practices
```
✅ "Audio: gentle rain on windows, distant thunder, melancholic piano"
❌ "Audio: play 'Moonlight Sonata' while character gives speech about philosophy"
```
