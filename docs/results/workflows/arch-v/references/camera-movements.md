# Camera Movements Reference

Authoritative vocabulary for Veo 3 camera movement terminology.

---

## QUICK REFERENCE - Most Common Movements

### Basic Movements

| Movement | Description |
|----------|-------------|
| **Dolly In** | Camera moves forward toward subject |
| **Dolly Out** | Camera moves backward from subject |
| **Pan Left/Right** | Camera rotates horizontally |
| **Tilt Up/Down** | Camera rotates vertically |
| **Zoom In/Out** | Lens focal length change |

### Advanced Movements

| Movement | Description |
|----------|-------------|
| **Arc Left/Right** | Camera moves in curved path around subject |
| **Crane Up/Down** | Camera moves vertically on boom arm |
| **FPV Drone** | First-person view rapid movement |
| **Whip Pan** | Extremely fast horizontal pan with motion blur |
| **Push In** | Slow dolly combined with slight zoom |

### Specialty Movements

| Movement | Description |
|----------|-------------|
| **Dutch Angle** | Tilted frame for dramatic effect |
| **Snorricam** | Camera mounted to subject's body |
| **Bullet Time** | Matrix-style frozen moment with camera rotation |
| **Tracking Shot** | Camera follows subject movement laterally |
| **Steadicam** | Smooth floating movement following action |

---

## USAGE RULES

### ONE Movement Per Beat
Each timed beat should have ONE dominant camera movement.

**WRONG:** "Dolly in while arc left" (conflicting)
**CORRECT:** "Dolly in" OR "Arc left" (choose one)

### Precision Terminology
Use exact terms from vocabulary to ensure machine interpretation accuracy.

### Timing Format
`[Start-End]: [Movement]`

Example: `0-4s: Slow dolly in`

---

## MOVEMENT COMBINATIONS (Sequential)

For complex camera work, use sequential beats:

```
0-4s: Dolly in (establish subject)
4-8s: Arc right (reveal environment)
8-12s: Crane up (pull back to wide)
```

---

## COMMON CONFLICT PATTERNS

### Spatial Conflicts
- Dolly + Arc simultaneously
- Pan + Track simultaneously
- Zoom + Dolly simultaneously (unless "dolly zoom")

### Temporal Conflicts
- Multiple movements in same time range
- Movement speed mismatch (whip + slow dolly)

### Resolution
Choose primary movement, or split into sequential beats.
