#!/usr/bin/env python3
"""
Arch-V Workflow - Output Template Generator

Generates a structured output template by reading imagine prompts.
Detects dual keyframe mode and prepares Veo 3 prompt structure.

Input Sources (priority order):
1. 05-imagine/ - Imagen prompts (Image-to-Video path)
2. 04-validator/ - Validated screenplay (Text-to-Video standalone path)

CRITICAL: Standalone mode reads from 04-validator, NOT 03-screenwriter.
Production-validator provides 8-second chunks required for Veo 3.

Usage:
    python generate-template.py <project_path>

Example:
    python generate-template.py /path/to/project/claudia-2025-12-14
"""

import sys
import os
import yaml
import re
from datetime import datetime, timezone
from pathlib import Path

def load_pipeline_state(project_path: str) -> dict:
    """Load pipeline state from project."""
    state_file = Path(project_path) / "pipeline-state.yaml"
    if not state_file.exists():
        print(f"ERROR: Pipeline state not found: {state_file}")
        sys.exit(1)

    with open(state_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def find_imagine_output(project_path: str, pipeline_state: dict) -> tuple:
    """Find the imagine prompts file or validated screenplay (standalone mode).

    Returns: (file_path, source_type) where source_type is 'imagine' or 'validated'

    Priority:
    1. 05-imagine/ - Image-to-Video path
    2. 04-validator/ - Text-to-Video standalone path (CRITICAL: NOT 03-screenwriter)
    """
    imagine_output = pipeline_state.get('stages', {}).get('05-imagine', {})
    outputs = imagine_output.get('outputs', [])

    imagine_dir = Path(project_path) / "05-imagine"

    if outputs:
        # Try from pipeline state
        for output in outputs:
            output_file = imagine_dir / output
            if output_file.exists():
                return (output_file, 'imagine')

    # Fallback: find any imagine-prompts file
    if imagine_dir.exists():
        prompt_files = list(imagine_dir.glob("imagine-prompts-*.md"))
        if prompt_files:
            return (sorted(prompt_files)[-1], 'imagine')  # Most recent

        # Or template file
        template_files = list(imagine_dir.glob("imagine-template-*.md"))
        if template_files:
            return (sorted(template_files)[-1], 'imagine')

    # Standalone mode: Try VALIDATED screenplay from 04-validator (NOT 03-screenwriter)
    print("⚠️  No imagine output found. Checking for validated screenplay (standalone mode)...")

    validator_output = pipeline_state.get('stages', {}).get('04-validator', {})
    outputs = validator_output.get('outputs', [])

    validator_dir = Path(project_path) / "04-validator"

    if outputs:
        for output in outputs:
            validated_file = validator_dir / output
            if validated_file.exists():
                print(f"✓ Found validated screenplay: {validated_file.name}")
                return (validated_file, 'validated')

    # Fallback: find any validated file in 04-validator
    if validator_dir.exists():
        validated_files = list(validator_dir.glob("validated-screenplay-*.md"))
        if validated_files:
            validated_file = sorted(validated_files)[-1]
            print(f"✓ Found validated screenplay: {validated_file.name}")
            return (validated_file, 'validated')

        validated_files = list(validator_dir.glob("validated-*.md"))
        if validated_files:
            validated_file = sorted(validated_files)[-1]
            print(f"✓ Found validated screenplay: {validated_file.name}")
            return (validated_file, 'validated')

    print("ERROR: No imagine output OR validated screenplay found")
    print("  - For Image-to-Video path, run imagine workflow first")
    print("  - For Text-to-Video path, run production-validator workflow first")
    print("")
    print("  CRITICAL: Arch-v requires 04-validator output for standalone mode.")
    print("  DO NOT use 03-screenwriter - those scenes are not chunked for Veo 3.")
    sys.exit(1)

def detect_dual_keyframe_mode(imagine_content: str) -> bool:
    """Detect if dual keyframe mode was used."""
    patterns = [
        r'DUAL KEYFRAME',
        r'FIRST KEYFRAME.*LAST KEYFRAME',
        r'Mode:.*Dual',
        r'first_frame.*last_frame',
        r'Scene.*a.*Scene.*b',
    ]

    for pattern in patterns:
        if re.search(pattern, imagine_content, re.IGNORECASE | re.DOTALL):
            return True

    return False

def extract_scenes(imagine_content: str) -> list:
    """Extract scenes from imagine output."""
    scenes = []

    # Pattern 1: Scene headers
    scene_pattern = r'###\s*(?:Scene|SCENE|Prompt)\s*(\d+)[ab]?:?\s*([^\n]+)?'
    matches = re.findall(scene_pattern, imagine_content, re.IGNORECASE)

    seen_ids = set()
    for match in matches:
        scene_id = match[0]
        title = match[1].strip() if len(match) > 1 and match[1] else f"Scene {scene_id}"
        if scene_id not in seen_ids:
            seen_ids.add(scene_id)
            scenes.append({
                'id': scene_id,
                'title': title,
                'has_dual': False
            })

    # Check for dual keyframes per scene
    for scene in scenes:
        pattern = rf'Scene\s*{scene["id"]}[ab]'
        if len(re.findall(pattern, imagine_content, re.IGNORECASE)) >= 2:
            scene['has_dual'] = True

    return scenes

def extract_scenes_from_screenplay(screenplay_content: str) -> list:
    """Extract scenes from screenplay (standalone mode)."""
    scenes = []

    # Pattern: <scene number="X"> tags from screenwriter
    scene_pattern = r'<scene\s+number="(\d+[AB]?)"[^>]*>'
    matches = re.findall(scene_pattern, screenplay_content, re.IGNORECASE)

    seen_ids = set()
    for scene_num in matches:
        # Extract base number (remove A/B suffix if exists)
        base_num = re.sub(r'[AB]$', '', scene_num, flags=re.IGNORECASE)

        if base_num not in seen_ids:
            seen_ids.add(base_num)
            scenes.append({
                'id': base_num,
                'title': f"Scene {base_num}",
                'has_dual': False  # Standalone mode doesn't use dual keyframe
            })

    # Fallback: Count any scene markers if no XML tags
    if not scenes:
        scene_markers = re.findall(r'(?:Scene|SCENE)\s*(\d+)', screenplay_content)
        for scene_id in set(scene_markers):
            scenes.append({
                'id': scene_id,
                'title': f"Scene {scene_id}",
                'has_dual': False
            })

    return scenes

    return scenes if scenes else [{'id': str(i), 'title': f'Scene {i}', 'has_dual': False} for i in range(1, 11)]

def extract_keyframe_prompts(imagine_content: str, scene_id: str) -> dict:
    """Extract first and last keyframe prompts for a scene."""
    result = {
        'first_frame': None,
        'last_frame': None,
        'transition_intent': None
    }

    # First keyframe pattern
    first_pattern = rf'(?:FIRST KEYFRAME|Scene\s*{scene_id}a)[^`]*```([^`]+)```'
    first_match = re.search(first_pattern, imagine_content, re.IGNORECASE | re.DOTALL)
    if first_match:
        result['first_frame'] = first_match.group(1).strip()

    # Last keyframe pattern
    last_pattern = rf'(?:LAST KEYFRAME|Scene\s*{scene_id}b)[^`]*```([^`]+)```'
    last_match = re.search(last_pattern, imagine_content, re.IGNORECASE | re.DOTALL)
    if last_match:
        result['last_frame'] = last_match.group(1).strip()

    # Transition intent
    transition_pattern = r'Transition Intent:\s*([^\n]+)'
    trans_match = re.search(transition_pattern, imagine_content, re.IGNORECASE)
    if trans_match:
        result['transition_intent'] = trans_match.group(1).strip()

    return result

def extract_art_style(imagine_content: str) -> str:
    """Extract art style from imagine output."""
    patterns = [
        r'Art Style:\s*([^\n]+)',
        r'\*\*Art Style:\*\*\s*([^\n]+)',
        r'Style:\s*(Science SARU|Crewdson|iPhone|Corporate Memphis|Photography)',
    ]

    for pattern in patterns:
        match = re.search(pattern, imagine_content, re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return "Science SARU"  # Default

def generate_template(
    project_path: str,
    project_name: str,
    is_dual_keyframe: bool,
    scenes: list,
    art_style: str,
    imagine_content: str
) -> str:
    """Generate the arch-v output template."""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")

    # Determine path type
    path_type = "image-to-video" if is_dual_keyframe else "text-to-video"

    template = f"""# Arch-V Output Template: {project_name}

**Generated:** {timestamp}
**Status:** TEMPLATE - Awaiting Claude completion

---

## INPUT ANALYSIS

### From Imagine Workflow:
- **Art Style:** {art_style}
- **Dual Keyframe Mode:** {'YES' if is_dual_keyframe else 'NO'}
- **Total Scenes:** {len(scenes)}
- **Path Type:** {path_type}

### Scenes Detected:
{chr(10).join([f'- Scene {s["id"]}: {s["title"]} {"(DUAL)" if s["has_dual"] else "(SINGLE)"}' for s in scenes])}

---

## WORKFLOW QUESTIONS FOR USER

### Q1: Production Path
```
Berdasarkan output Imagine, path yang terdeteksi: {path_type.upper()}

{'Dual keyframe mode aktif - setiap scene memiliki first frame dan last frame.' if is_dual_keyframe else 'Single keyframe mode - setiap scene memiliki satu frame saja.'}

{'Veo 3 akan menginterpolasi antara kedua frame untuk menghasilkan video.' if is_dual_keyframe else 'Veo 3 akan generate video dari single image atau text prompt.'}

Konfirmasi path ini? [Y] Ya / [N] Ubah ke path lain
```

### Q2: Prompt Complexity
```
Untuk setiap scene, pilih kompleksitas prompt:

1. SHORT PROMPT (untuk scene sederhana)
   - Filler shots, B-roll, atmospheric
   - < 3 sentences

2. LONG PROMPT (untuk scene kompleks)
   - Dialogue, character continuity
   - Multi-beat sequences, complex choreography

Default: Otomatis berdasarkan scene type
```

---

## VEO 3 PROMPT GENERATION

### 8 Mandatory Components Checklist

Untuk setiap prompt, pastikan memiliki:
- [ ] 1. Subject (who/what in shot)
- [ ] 2. Setting (where/when)
- [ ] 3. Action (what's happening)
- [ ] 4. Style/Genre (aesthetic)
- [ ] 5. Camera/Composition (shot size, angle, movement)
- [ ] 6. Lighting/Mood (light sources, emotional tone)
- [ ] 7. Audio (dialogue, ambience, music)
- [ ] 8. Constraints (prohibitions, exact requirements)

---

## SCENE PROMPTS

"""

    # Generate scene sections
    for scene in scenes:
        scene_id = scene['id']
        title = scene['title']
        has_dual = scene['has_dual']

        keyframes = extract_keyframe_prompts(imagine_content, scene_id)

        if has_dual and is_dual_keyframe:
            template += f"""### Scene {scene_id}: {title}
**Mode:** DUAL KEYFRAME (Image-to-Video Interpolation)

#### Input from Imagine:
**First Frame Prompt:**
```
{keyframes.get('first_frame', '[TO BE LOADED FROM IMAGINE OUTPUT]')}
```

**Last Frame Prompt:**
```
{keyframes.get('last_frame', '[TO BE LOADED FROM IMAGINE OUTPUT]')}
```

**Transition Intent:** {keyframes.get('transition_intent', '[DESCRIBE: What motion happens between frames]')}

#### Veo 3 Motion Prompt:
**Status:** [ ] Generated

```
[GENERATE VEO 3 PROMPT HERE]

Components:
- Subject: [FROM IMAGINE]
- Setting: [FROM IMAGINE]
- Action: [DESCRIBE MOTION FROM FIRST TO LAST FRAME]
- Style: {art_style}
- Camera: [MOVEMENT IF ANY]
- Lighting: [FROM IMAGINE]
- Audio: [DIALOGUE/AMBIENT/MUSIC]
- Constraints: [PROHIBITIONS]

Technical:
- Start Image: first_frame.png
- End Image: last_frame.png
- Interpolation: smooth transition
- Duration: 8 seconds
```

**Validation:**
- [ ] All 8 components present
- [ ] Motion describes first→last transition
- [ ] Camera movement uses standardized vocabulary
- [ ] No time/weather conflicts

---

"""
        else:
            template += f"""### Scene {scene_id}: {title}
**Mode:** {'TEXT-TO-VIDEO' if not is_dual_keyframe else 'SINGLE KEYFRAME'}

#### Veo 3 Prompt:
**Status:** [ ] Generated

```
[GENERATE VEO 3 PROMPT HERE]

Components:
- Subject: [DESCRIBE]
- Setting: [WHERE/WHEN]
- Action: [WHAT HAPPENS]
- Style: {art_style}
- Camera: [SHOT TYPE, MOVEMENT]
- Lighting: [LIGHT SOURCES, MOOD]
- Audio: [DIALOGUE/AMBIENT]
- Constraints: [PROHIBITIONS]
```

**Validation:**
- [ ] All 8 components present
- [ ] Camera movement standardized
- [ ] No conflicts

---

"""

    template += f"""
## DUAL KEYFRAME INTEGRATION GUIDE

{'### How Dual Keyframe Works with Veo 3' if is_dual_keyframe else '### Single Frame Mode Active'}

{'''
**Image-to-Video Interpolation:**

1. **First Frame (from Imagine):** Opening composition
   - Character starting position
   - Initial emotional state
   - Environment at t=0

2. **Last Frame (from Imagine):** Closing composition
   - Character ending position
   - Final emotional state
   - Environment at t=8s

3. **Veo 3 Motion Prompt:**
   - Describe the MOTION between frames
   - Camera movement (if any)
   - Audio/dialogue timing
   - Action pacing

**Prompt Structure for Interpolation:**
```
[Describe motion from first frame to last frame].
Camera: [movement or static].
Audio: [character] says: "[dialogue]" / [ambient sound]
Duration: 8 seconds, smooth interpolation.
Start image: [reference first frame]
End image: [reference last frame]
```
''' if is_dual_keyframe else '''
**Text-to-Video Mode:**

Single prompt generates full video sequence without image references.
Focus on clear action description and timing.
'''}

---

## COMPLETION CHECKLIST

### Before Starting:
- [ ] User confirmed path type
- [ ] Imagine output loaded and parsed
- [ ] Dual keyframe status confirmed

### Generation Progress:
- [ ] Scene 1 prompt generated
{chr(10).join([f'- [ ] Scene {s["id"]} prompt generated' for s in scenes[1:6]])}
{'- [ ] ... (remaining scenes)' if len(scenes) > 6 else ''}

### Validation:
- [ ] All prompts have 8 components
- [ ] Camera movements use standardized vocabulary
- [ ] No time/weather conflicts
- [ ] Dual keyframes have transition intent

### Final Output:
- [ ] Output file: veo3-prompts-{timestamp}.md
- [ ] Pipeline state updated

---

## NEXT STEPS FOR CLAUDE

1. Load imagine output from 05-imagine/
2. Present Q1, Q2 to user
3. For each scene:
   a. Load keyframe prompts (if dual mode)
   b. Generate Veo 3 motion prompt
   c. Validate 8 components
4. Output final file

---

*Template generated by arch-v/scripts/generate-template.py*
*Ready for Claude completion*
"""

    return template

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-template.py <project_path>")
        print("Example: python generate-template.py ./docs/projects/claudia-2025-12-14")
        sys.exit(1)

    project_path = sys.argv[1]

    if not os.path.isdir(project_path):
        print(f"ERROR: Project path not found: {project_path}")
        sys.exit(1)

    project_name = os.path.basename(project_path)
    print(f"📋 Generating Arch-V template for: {project_name}")

    # Load pipeline state
    pipeline_state = load_pipeline_state(project_path)
    print("✓ Pipeline state loaded")

    # Find input source (imagine OR screenplay)
    source_file, source_type = find_imagine_output(project_path, pipeline_state)
    print(f"✓ Found {source_type}: {source_file.name}")

    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process based on source type
    if source_type == 'imagine':
        # Image-to-Video path
        is_dual_keyframe = detect_dual_keyframe_mode(content)
        print(f"✓ Dual keyframe mode: {'YES' if is_dual_keyframe else 'NO'}")

        scenes = extract_scenes(content)
        print(f"✓ Scenes detected: {len(scenes)}")

        art_style = extract_art_style(content)
        print(f"✓ Art style: {art_style}")

        imagine_content = content

    else:  # source_type == 'validated'
        # Text-to-Video path (standalone from validated screenplay)
        print("✓ Standalone mode (Text-to-Video from validated screenplay)")
        is_dual_keyframe = False  # Not applicable for standalone

        scenes = extract_scenes_from_screenplay(content)
        print(f"✓ Scenes detected from validated screenplay: {len(scenes)}")

        art_style = "User will provide (no imagine output)"
        imagine_content = None  # No imagine content in standalone mode

    # Generate template
    template = generate_template(
        project_path=project_path,
        project_name=project_name,
        is_dual_keyframe=is_dual_keyframe,
        scenes=scenes,
        art_style=art_style,
        imagine_content=imagine_content
    )

    # Write output
    output_dir = Path(project_path) / "06-arch-v"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
    output_file = output_dir / f"arch-v-template-{timestamp}.md"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)

    print(f"\n✅ Template generated: {output_file}")

    if source_type == 'imagine':
        print(f"\n📌 Next: Claude will generate Veo 3 prompts with image interpolation")
    else:
        print(f"\n📌 Next: Claude will generate Veo 3 prompts (Text-to-Video mode)")

    print(f"   Mode: {'Dual Keyframe Interpolation' if is_dual_keyframe else 'Standard'}")


    return str(output_file)

if __name__ == "__main__":
    main()
