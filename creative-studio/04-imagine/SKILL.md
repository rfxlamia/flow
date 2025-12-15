---
name: imagine
description: Prepare detailed, professional prompts for Google Imagen 3/4 image generation. Supports character, environment, and object prompts using natural language with technical photography specifications. Includes Science SARU art style by default, with extensible support for additional art styles via reference files.
---

# Imagine: Imagen Prompt Architect

Generate detailed, professional prompts for Google Imagen 3/4 that leverage its natural language processing strengths and technical parameter understanding.

## Core Prompt Structure

Imagen uses a **Subject-Context-Style framework** powered by T5-XXL language models. Build prompts in three layers:

1. **Subject**: Primary focus (person, object, animal, scenery)
2. **Context**: Environment, placement, background, setting
3. **Style**: Aesthetic approach (photographic, artistic, specific technique)

### Photography Prompts Pattern

Start with explicit photography signals: `"A photo of [detailed subject description], [context/placement], [technical specifications]"`

**Technical specifications include:**
- Lens type: 24-85mm (portraits), 60-105mm macro (products), 10-24mm wide-angle (landscapes)
- Lighting: natural light, studio lighting, golden hour, dramatic lighting
- Quality modifiers: sharp focus, high detail, professional photography, 8K resolution
- Camera/equipment: shot on ARRI Alexa, 35mm film, DSLR

**Example**: `"A photo of an elderly woman with weathered hands holding a steaming cup of tea, soft sunlight highlighting her wrinkles and smile, 35mm lens, warm and intimate mood, natural outdoor setting, sharp focus, professional portrait photography"`

### Artistic/Stylized Prompts Pattern

For non-photographic styles, read the relevant artstyle reference file first, then layer:

**Foundation**: `"[Art style name] aesthetic, [medium/technique], [key visual characteristics]"`

**Character/Subject**: Specific features, proportions, design elements

**Environment**: Scene composition, spatial elements, atmospheric details  

**Atmosphere**: Mood, color palette, lighting approach

**Technical**: Rendering specifics, texture, quality markers

## Using Artstyle References

**Current default style**: Science SARU (references/artstyle-sciencesaru.md)

**Before creating prompts with Science SARU style**:
1. Read references/artstyle-sciencesaru.md to understand the complete visual language
2. Apply the layered prompting strategy from the reference
3. Use the technical descriptors provided for linework, movement, color, lighting

**For future art styles**:
- User will provide artstyle-[name].md files
- Always read the relevant artstyle file before generating prompts
- Follow the style-specific guidelines and vocabulary from each reference

## Best Practices from Imagen Architecture

### Natural Language Advantage
- Write detailed descriptive sentences, not keyword lists
- Imagen rewards verbose descriptions over brevity
- Use professional creative brief language
- Default enhancePrompt=true automatically optimizes your prose

### Iterative Refinement
Start simple, layer details progressively:
1. Base: `"A cat"`
2. Add specifics: `"A fluffy Persian cat with bright blue eyes"`
3. Add context: `"...sitting on a velvet cushion in a sunlit room"`
4. Add technical: `"A photo of a fluffy Persian cat with bright blue eyes, sitting on a velvet cushion in a sunlit room, 50mm lens, natural soft lighting, warm colors, professional pet photography"`

### Critical Constraints
- **Text-in-image**: Maximum 25 characters per phrase, 3 phrases total
- **Negative prompts**: Use plain descriptive terms ("wall, frame") not instructive language ("no walls, without frame")
- **Token limit**: 480 tokens for prompt text

### Technical Parameters
**Aspect ratios** (match use case):
- 1:1 - Square social media
- 3:4 - Portrait ads, vertical social
- 4:3 - Traditional photography, TV
- 16:9 - Widescreen landscape, modern displays
- 9:16 - Vertical video, tall subjects

**Safety/person controls**: Adjust personGeneration (allow_adult, allow_all, dont_allow) and safetySetting (block_low_and_above, block_medium_and_above, block_only_high, block_none) as needed

## Practical Use Case Patterns

### Character/Portrait
`"Portrait of [character description with age, features, clothing, emotion], [lens specification 24-85mm], [lighting type], [mood descriptors], [setting], [quality modifiers]"`

**Science SARU character specifics**: Simplified designs, elastic limbs, large expressive eyes, minimalist features, loose rough linework, moderate stylization

### Environment/Landscape  
`"[Environment type], [weather/time/season], [lens specification 10-24mm wide-angle], [atmospheric conditions], [quality modifiers]"`

**Science SARU environment specifics**: Dense layered urban scenes, flat color blocks with gradients, dramatic stylized lighting, painterly watercolor texture

### Product/Object
`"[Product] on [surface], [lens specification 60-105mm macro], [lighting type], [background type], [material/texture details], [quality modifiers]"`

### Cinematic/Stylized
`"[Animation/art style], [scene description], [color grading approach], [cinematography terms], [atmospheric effects]"`

**Science SARU cinematic specifics**: Golden hour emotional coding, bloom lighting effects, backlit silhouettes, complementary shadow colors, dynamic tracking camera

## Workflow for Creating Prompts

1. **Determine type**: Photography, artistic style, or hybrid?
2. **If using art style**: Read relevant references/artstyle-[name].md file completely
3. **Build foundation**: Establish subject clearly and early
4. **Layer context**: Add environment, placement, spatial relationships
5. **Specify style**: Include aesthetic approach with technical vocabulary
6. **Add technical specs**: Lens type, lighting, quality modifiers appropriate to subject
7. **Refine iteratively**: Start simple, add detail progressively until satisfied
8. **Validate constraints**: Check text-in-image limits, negative prompt format, token count

## Example Complete Prompts

### Photography Example
`"A photo of a plate of traditional Indonesian nasi goreng with fried egg on top, colorful vegetables visible, served on rustic ceramic plate on wooden table, 100mm macro lens, natural window lighting from side, warm atmosphere, steam rising from rice, glistening sauce, high detail, professional food photography, appetizing composition"`

### Science SARU Style Example  
`"Science SARU animation style directed by Masaaki Yuasa, digitally-assisted 2D hand-drawn aesthetic. Young Indonesian street vendor character with simplified design, elastic limbs with soft rounded contours, large expressive eyes, minimalist features, worn clothing in muted earth tones, loose rough linework with variable thickness. Dense layered Jakarta street scene at golden hour, simplified geometric shophouses with clean vector linework, vibrant warm tropical palette transitioning to orange-pink sunset gradient sky, atmospheric heat haze, dramatic long shadows, wet reflective surfaces, vertical composition with hanging power lines and palm trees. Melancholic but hopeful atmosphere, desaturated base with warm sunset accents, cool blue-purple shadows, bloom lighting effects, isolated character against silhouetted crowd. Flat color blocks with gradients, painterly watercolor texture, irregular geometric shapes, deliberately unfinished aesthetic, complementary shadow colors, dynamic low-angle camera, perpetual subtle character deformation, fluid elastic movement, watercolor-flow quality"`

### Hybrid Example (Science SARU character, photographic background)
`"A photo of a simplified cartoon character in Science SARU animation style with elastic limbs and large expressive eyes, loose rough linework, standing on actual Jakarta street, 35mm lens, golden hour natural lighting, real urban background with simplified cartoon character overlay, professional photography with 2D animation integration, warm atmospheric lighting, high detail background with stylized character"`

## Tips for Quality Output

- **Be specific with materials and textures**: "glistening sauce," "rough ceramic," "polished wood" guide fine detail
- **Use cinematography vocabulary**: "shot on ARRI Alexa," "Summilux lens," "volumetric lighting" elevate professional quality  
- **Time of day matters**: Golden hour, overcast, midday sun, twilight each create distinct lighting and mood
- **Color grading terms**: "muted cold tones," "warm sepia," "desaturated," "high contrast" specify aesthetic precisely
- **Atmospheric effects**: "misty," "foggy," "heat haze," "rain-soaked" add environmental depth

## Extensibility

This skill is designed to grow with your needs:
- Add new artstyle-[name].md files to references/ for different visual styles
- Follow the pattern from artstyle-sciencesaru.md for documentation structure
- Always read the relevant artstyle file before generating style-specific prompts
- Science SARU remains the default style when no other style is specified
