# Step 01: Intent Detection & Routing

**Goal:** Understand user's content generation needs and route to appropriate VS workflow.

**Scope:** Decision-making only - no content generation yet.

**Token Budget:** ~250 tokens (detection logic + routing decision)

---

## INTENT DETECTION

Analyze user's request and categorize:

### Content Type Detection

| User Request Pattern | Content Type | Route To |
|---------------------|--------------|----------|
| "Generate/brainstorm [N] [content]" | Multiple variations | Step 02 (basic VS) |
| "I need diverse ideas for..." | Creative ideation | Step 02 (basic VS) |
| "Give me options/variations/angles" | Exploration | Step 02 (basic VS) |
| "Write [story/narrative/campaign]" | Long-form creative | Step 02 (VS + task-specific) |
| "Need higher quality" or mentioned "refinement" | Quality improvement | Step 02 (VS-Multi) |
| Mentioned "save to file" or "batch" | File integration | Step 02 (VS + file ops) |

### VS Technique Selection

Based on user intent, select appropriate VS technique:

- **VS-Basic:** Standard 5-candidate generation (most common)
- **VS-Multi:** Generate → User selects → Refine (for quality)
- **VS-CoT:** Chain-of-thought for complex reasoning
- **VS-Batch:** Multiple calls for large quantities

**Default:** VS-Basic (k=5, temp=0.8)

---

## REFERENCE LOADING DECISION

**ONLY load references if user explicitly needs them:**

| User Signal | Load Reference |
|-------------|---------------|
| "How does VS work?" | `references/vs-core-technique.md` |
| "Need help with [specific task type]" | `references/task-workflows.md` |
| "Getting errors" or "outputs too similar" | `references/troubleshooting.md` |
| "Which model to use?" | `references/research-findings.md` |
| Otherwise | NO references loaded yet |

**Default:** Load NO references in step-01. Let step-02 load what it needs.

---

## EXECUTION

### 1. Analyze User Request

Read user's message and extract:
- **What type of content?** (story, campaign, caption, etc.)
- **How many variations?** (explicit number or implied "multiple")
- **Quality level?** (quick brainstorm vs polished final)
- **Any special requirements?** (save to file, specific format, etc.)

### 2. Select VS Technique

Based on analysis, choose:
- VS-Basic (default, 90% of cases)
- VS-Multi (if quality refinement mentioned)
- VS-Batch (if large quantity >10 items)

### 3. Communicate Scope

**IMPORTANT:** Tell user what this workflow will do:

```
"I'll help you generate [N] diverse [content-type] using Verbalized Sampling.

This workflow focuses on IDEATION ONLY - generating multiple creative variations.

If you select an idea you like, we can then pass it to the storyteller workflow
for visual scene development, and eventually to screenwriter for formatting.

Ready to generate diverse ideas?"
```

### 4. Update Frontmatter

```yaml
---
current_step: 1
steps_completed: [1]
vs_technique_selected: "vs-basic" # or vs-multi, vs-batch
content_type: "{detected type}"
user_confirmed: true
---
```

### 5. Load Next Step

Execute: `Load step-02-execute-vs.md`

---

## SELF-AWARENESS CHECKPOINT

Before proceeding to step-02, verify:

- [ ] User intent clearly understood
- [ ] VS technique selected appropriately
- [ ] Workflow scope communicated to user
- [ ] User confirmed ready to proceed
- [ ] NO unnecessary references loaded

If any checkbox fails, ask clarifying questions instead of proceeding.

---

## EXAMPLE EXECUTION

**User:** "Give me 5 story concepts about lost love"

**Step-01 Analysis:**
- Content type: story concepts
- Quantity: 5
- Quality: standard brainstorm
- Technique: VS-Basic (k=5)

**Step-01 Output:**
```
I'll help you generate 5 diverse story concepts about lost love using
Verbalized Sampling technique.

This workflow will create multiple creative variations with different:
- Points of view (first person, second person, etc.)
- Settings (urban, coastal, abstract, etc.)
- Tones (vulnerable, poetic, theatrical, etc.)
- Structures (monolog, letter, parallel timeline, etc.)

These will be raw story concepts. If you like one, we can then develop it
into visual scenes with the storyteller workflow.

Generating now...
```

**Load:** step-02-execute-vs.md

---

**Proceed to Step 02 when ready.**
