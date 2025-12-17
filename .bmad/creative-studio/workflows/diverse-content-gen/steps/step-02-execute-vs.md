# Step 02: Execute VS Technique

**Goal:** Execute Verbalized Sampling to generate diverse creative content.

**Scope:** Content generation only - presentation handled by step-03.

**Token Budget:** ~600 tokens (execution logic + required reference + optional MCP calls)

---

## REQUIRED REFERENCE LOADING

**ALWAYS load the core VS reference for creative context:**

```yaml
# MANDATORY - Load this FIRST before any generation
Load: references/vs-core-technique.md

# This provides:
# - VS philosophy and theory (WHY it works)
# - Mode collapse problem understanding
# - Production-ready prompt templates
# - Parameter selection guidance
# - Quality control checklist
```

**Rationale:** VS requires creative philosophy context, not just mechanical templates. The reference file contains essential context that improves output diversity and quality.

**Additional references (load on-demand):**

```yaml
IF vs_technique == "vs-multi":
  Load: references/advanced-techniques.md (VS-Multi section only)

IF vs_technique == "vs-batch":
  Load: references/advanced-techniques.md (batching section)

IF errors_occurred:
  Load: references/troubleshooting.md (specific error section)
```

---

## MCP SERVER INTEGRATION (Optional Enhancement)

Check for available MCP servers and use them for enhanced quality:

### Sequential Thinking MCP (Ideation Enhancement)

**Detection:** Check if `mcp__sequential-thinking__sequentialthinking` tool is available.

**When to use:** For complex creative requests requiring deep ideation.

**Workflow:**
```yaml
IF sequential_thinking_available AND content_type IN ["story-concept", "campaign-idea", "complex-narrative"]:

  # Use Sequential Thinking BEFORE VS generation
  # This helps explore diversity dimensions systematically

  STEP 1: Ideation via Sequential Thinking
    - Thought 1: "Analyzing user request for diversity opportunities..."
    - Thought 2: "Identifying POV variations: first person, second person, third..."
    - Thought 3: "Exploring tonal dimensions: vulnerable, poetic, theatrical..."
    - Thought 4: "Considering structural variations: monolog, letter, parallel..."
    - Thought 5: "Synthesizing optimal diversity matrix for this request..."

  STEP 2: Use ideation output to inform VS generation
    - Apply discovered diversity dimensions to VS prompt
    - Ensure each candidate explores different dimension combinations
```

### Gemini MCP (Orchestrator/Validator Pattern)

**Detection:** Check if Gemini MCP server tools are available (e.g., `mcp__gemini__*`).

**When to use:** For production-quality content requiring validation.

**Multi-Model Architecture:**
```
USER REQUEST
    ↓
┌─────────────────────────────────────┐
│ GEMINI (Orchestrator/Validator)     │
│ Via MCP Server                      │
└─────────────────────────────────────┘
    ↓
    ├─→ STEP 1: Prompt Engineering
    │   • Receives raw user request
    │   • Crafts optimal VS prompt
    │   • Sets k, threshold, target_words
    │   • Adds task-specific constraints
    │
    ↓
┌─────────────────────────────────────┐
│ CLAUDE (Generator)                  │
│ Main model with VS technique        │
└─────────────────────────────────────┘
    ↓
    • Generates k candidates with VS
    • Returns outputs to Gemini
    ↓
┌─────────────────────────────────────┐
│ GEMINI (Validator)                  │
└─────────────────────────────────────┘
    ↓
    ├─→ STEP 2: Diversity Validation
    │   • Analyze semantic distance between candidates
    │   • Check if candidates cover different dimensions
    │   • Calculate diversity score
    │
    ├─→ STEP 3: Quality Check
    │   • IF diversity LOW (similar outputs):
    │       → Adjust parameters (lower threshold, increase k)
    │       → Request RETRY from Claude
    │   • IF diversity HIGH:
    │       → Outputs validated! ✅
    │       → Pass to presentation step
    │
    └─→ OUTPUT: Validated diverse candidates
```

**Implementation:**
```yaml
IF gemini_mcp_available:

  # Phase 1: Gemini crafts the VS prompt
  gemini_prompt_engineering:
    input: user_request, content_type, target_count
    output: optimized_vs_prompt, parameters

  # Phase 2: Claude generates with VS
  claude_generation:
    input: optimized_vs_prompt
    output: k_candidates

  # Phase 3: Gemini validates diversity
  gemini_validation:
    input: k_candidates
    checks:
      - semantic_distance_between_candidates
      - dimension_coverage (POV, Tone, Structure, Setting)
      - quality_baseline_met
    output:
      IF validation_passed: final_candidates
      IF validation_failed: retry_with_adjusted_params

  # Retry loop (max 2 retries)
  IF retry_needed:
    adjust: lower_threshold OR increase_k OR explicit_dimension_constraints
    GOTO: claude_generation
```

### Fallback (No MCP Available)

**If no MCP servers detected:** Proceed with standard VS execution using Claude only.
This is still effective - MCP integration is an enhancement, not a requirement.

---

## EMBEDDED VS TEMPLATE

For standard VS-Basic execution, use this template without loading references:

### VS Prompt Template

```
Generate {k} responses to: {user_request}

Use DIVERSE approaches across these dimensions:
- POV: First person / Second person / Third person / Interlocutor-absent
- Setting: Urban contemporary / Coastal/nature / Abstract space / Dual timeline
- Tone: Vulnerable raw / Poetic mythic / Theatrical absurd / Nostalgic epistolary
- Structure: Linear monolog / Letter / Parallel scenes / Extended metaphor / One-sided dialog

For each response, ensure it's DISTINCTLY DIFFERENT from others.

Return JSON format with key "responses" (list of dicts).
Each dict must include:
• text: the complete response
• probability: estimated probability (0.0-1.0)
• diversity_markers: which dimensions were varied

Give ONLY the JSON object, no extra text.
```

### Standard Parameters

```yaml
k: 5  # Number of candidates
temperature: 0.8  # Moderate diversity
threshold: 0.10  # Optional probability filter
```

---

## EXECUTION WORKFLOW

### 1. Construct VS Prompt

Based on user's content request and detected content_type:

**For Story/Narrative:**
```
Generate 5 diverse narrative variations on: "{user's theme/concept}"

Vary across:
- POV (first/second/third person, timeline perspective)
- Setting (urban/natural/abstract/cultural contexts)
- Tone (raw/poetic/theatrical/nostalgic/cinematic)
- Structure (monolog/letter/parallel/metaphor/dialog)

Each must feel DISTINCTLY DIFFERENT.

Return JSON: {"responses": [{"text": "...", "probability": 0.x, "diversity_markers": "..."}]}

JSON only, no other text.
```

**For Campaign/Marketing:**
```
Generate 5 diverse campaign approaches for: "{user's product/goal}"

Vary across:
- Angle (emotional/rational/humor/fear/aspiration)
- Tone (professional/casual/bold/subtle/provocative)
- Format (story/question/statement/challenge/invitation)
- Target (demographics, psychographics, pain points)

Return JSON format only.
```

**For Social Media Captions:**
```
Generate 5 diverse social media captions for: "{user's context}"

Vary:
- Voice (friendly/authoritative/humorous/inspirational/educational)
- Structure (hook-question-CTA / story / statement / list / quote)
- Length (short punchy / medium / long narrative)
- Emoji usage (none / minimal / abundant / strategic)

JSON only.
```

### 2. Execute LLM Call

**Generate the diverse content directly.** As Claude, you ARE the LLM - execute the VS prompt now:

1. Take the user's content request
2. Apply the diversity dimensions (POV, Setting, Tone, Structure)
3. Generate 5 distinctly different variations
4. For each variation, mentally note which dimensions you varied

**Output Format:** Generate as structured text (not JSON). Use this format:

```
---
VARIATION 1: [Brief Title]
Diversity: POV={variation}, Setting={variation}, Tone={variation}, Structure={variation}

[Full generated content here]

---
VARIATION 2: [Brief Title]
...
```

### 3. Parse Response

After generating variations, organize them into a structured list:

**For each variation, extract:**
- **Title:** Brief descriptive title
- **Content:** The full generated text
- **Diversity markers:** Which dimensions were varied
- **Estimated strength:** How well does this address the user's request? (strong/medium/weak)

**Quality check:**
- Are all 5 variations distinctly different?
- Do they cover different POVs, tones, or structures?
- If variations feel too similar, regenerate with more explicit dimension changes

### 4. Validate Diversity

Perform a mental diversity check:

**Checklist:**
- [ ] At least 3 different POVs used across variations
- [ ] At least 2 different tones represented
- [ ] Opening lines are all different
- [ ] Content lengths vary (not all same length)
- [ ] Different emotional angles explored

**If diversity is LOW:**
1. Identify which dimensions are too similar
2. Regenerate 1-2 variations with explicit different dimensions
3. Example: "Generate another variation, but this time use SECOND PERSON POV and THEATRICAL ABSURD tone"

### 5. Store Generated Content

Update your mental tracking (frontmatter state):
```yaml
---
current_step: 2
steps_completed: [1, 2]
content_generated: true
candidates_count: 5
diversity_score: {calculated_score}
generated_content: {candidates}
---
```

---

## DIVERSITY SCORING

Estimate the diversity score based on your generated variations:

**Scoring Guide:**
- **1.0** = Baseline (all variations similar, minimal diversity)
- **1.3-1.5** = Low diversity (some variation in 1-2 dimensions)
- **1.6-1.8** = Good diversity (variation across 3+ dimensions)
- **1.9-2.1** = Excellent diversity (distinct approaches in all dimensions)

**How to estimate:**
1. Count how many different POVs used (1-4)
2. Count how many different tones used (1-4)
3. Count how many different structures used (1-4)
4. Average these counts, then multiply by 0.5 and add 1.0

**Example:**
- POVs: 3 different (first, second, third)
- Tones: 2 different (poetic, theatrical)
- Structures: 3 different (monolog, letter, metaphor)
- Average: (3+2+3)/3 = 2.67
- Score: 1.0 + (2.67 × 0.5) = 1.0 + 1.33 = **1.83**

---

## ERROR HANDLING

### Common Issues & Solutions

**Variations too similar:**
1. Explicitly state different dimensions for each regeneration
2. Use more extreme contrasts: "Make variation 3 use THEATRICAL ABSURD tone - completely different from the poetic ones"
3. Load `references/advanced-techniques.md` for VS-Multi approach

**Quality too low:**
1. Focus on fewer but better variations (3 instead of 5)
2. Load `references/advanced-techniques.md` for quality improvement techniques
3. Consider VS-Multi: generate first, let user select best, then refine

**User unhappy with all variations:**
1. Ask clarifying questions about what they're looking for
2. Regenerate with more specific constraints
3. Offer to combine elements from multiple variations

---

## OUTPUT

Prepare data for step-03:

```yaml
execution_result:
  status: "success"
  candidates_generated: 5
  diversity_score: 1.8
  vs_technique_used: "vs-basic"
  temperature: 0.8
  timestamp: "{timestamp}"
  ready_for_presentation: true
```

---

## LOAD NEXT STEP

Execute: `Load step-03-present-refine.md`

---

**Proceed to Step 03 when content generated successfully.**
