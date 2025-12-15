# Step 1: Gather Project Information

**Purpose:** Collect essential project details from the user

---

## Instructions

Ask the user the following questions to configure their creative project:

### 1. Project Name

**Question:** "What would you like to name this creative project?"

**Guidelines:**
- Use a descriptive, memorable name
- Will be converted to slug format (lowercase, hyphens)
- Example: "Dua Pelaut Satu Lautan" → "dua-pelaut-satu-lautan"

**Store as:** `project_name`

---

### 2. Content Type

**Question:** "What type of content are you creating?"

**Options:**
- **Video** (Short film, music video, documentary, etc)
- **Blog** (Article, essay, story) [Coming Soon]
- **Carousel** (Instagram/LinkedIn multi-slide post) [Coming Soon]
- **Thread** (Twitter/X thread) [Coming Soon]
- **Other** (Describe custom type)

**Store as:** `content_type`

**Note:** For now, only "Video" pipeline is fully implemented. Other types will use diverse-content-gen but require manual continuation.

---

### 3. Target Platform

**Question:** "Where will this content be published?" (depends on content_type)

**For Video:**
- YouTube (long-form)
- Instagram Reels
- TikTok
- Cinema/Festival
- Other

**For Blog:**
- Medium
- Personal Blog
- Substack
- Other

**Store as:** `target_platform`

---

### 4. Project Description

**Question:** "Brief description of this project (1-2 sentences):"

**Example:** "A 12-minute short film exploring devotion and loss through the metaphor of two sailors at sea."

**Store as:** `description`

---

### 5. Estimated Duration/Length (Optional)

**Question:** "Estimated content length?" (optional, depends on type)

**For Video:** Duration (e.g., "12 minutes", "90 seconds")
**For Blog:** Word count (e.g., "1500 words")
**For Carousel:** Slide count (e.g., "10 slides")

**Store as:** `estimated_length`

---

## Output Variables

After gathering information, you should have:

```yaml
project_name: "dua-pelaut-satu-lautan"
content_type: "video"
target_platform: "youtube"
description: "A 12-minute short film exploring devotion and loss"
estimated_length: "12 minutes"
timestamp: "2025-12-14T12-30-00Z"
```

These variables will be used in Step 2 to create the project structure.

---

## Next Step

Proceed to `step-02-create-structure.md` with the gathered information.
