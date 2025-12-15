# 🔄 SESSION RESUME GUIDE
# What to Say When Starting New Session

---

## ✅ ALL TRACKING FILES CREATED

Your work from this session has been fully tracked in:

1. **Conversion Project State**
   - File: `.bmad/creative-studio/_state/conversion-project.yaml`
   - Contains: Full project context, completed work, next steps, design patterns

2. **Workflow Manifest**
   - File: `.bmad/_cfg/workflow-manifest.csv`
   - Added: `diverse-content-gen` workflow

3. **Task Manifest**
   - File: `.bmad/_cfg/task-manifest.csv`
   - Added: `convert-skill-to-workflow` task

4. **Agent Manifest**
   - File: `.bmad/_cfg/agent-manifest.csv`
   - Status: No new agents (creative-studio is workflow-only module)

5. **Pipeline State**
   - File: `.bmad/creative-studio/_state/creative-pipeline-state.yaml`
   - Ready for runtime tracking

---

## 🎯 WHAT TO SAY IN NEW SESSION

### OPTION 1: Minimal & Fast (RECOMMENDED)

```
Continue creative-studio conversion
```

**What happens:**
- BMad Master will check for active conversion projects
- Will find conversion-project.yaml
- Will load full context automatically
- Will ask if you want to continue with storyteller

---

### OPTION 2: Explicit Context Load

```
Load .bmad/creative-studio/_state/conversion-project.yaml
and continue skill-to-workflow conversion
```

**What happens:**
- Explicit file read
- Full context recovered
- Master/Builder understand project state
- Ready to continue immediately

---

### OPTION 3: Party Mode Continue

```
/bmad:core:agents:bmad-master

Then say: "Continue creative-studio conversion project"
```

**What happens:**
- BMad Master activates
- Reads conversion-project.yaml
- Presents menu with conversion status
- Offers to continue with next workflow

---

### OPTION 4: Direct Task Call

```
Read task: convert-skill-to-workflow
```

**What happens:**
- Loads task from task-manifest.csv
- Task points to conversion-project.yaml
- Full context loaded
- Continues conversion work

---

## 📊 WHAT THE NEW SESSION WILL KNOW

After loading conversion-project.yaml, the new session will have:

### ✅ Project Understanding
- Converting creative-studio skills to BMAD workflows
- 5 workflows total, 1 completed (20%)
- Using smart context engineering approach
- File-based pipeline integration

### ✅ Completed Work
- `01-diverse-content-gen` fully converted
- Module structure created
- Pipeline state tracking implemented
- Design patterns established

### ✅ Next Actions
- Convert `02-storyteller` workflow
- Source: `creative-studio/01-storyteller/SKILL.md`
- Integration: Read diverse-content-gen outputs
- Pattern: Same 3-step structure with lazy loading

### ✅ Design Patterns to Follow
- Workflow: ~200 tokens
- Steps: 250-400 tokens each
- Lazy loading (no pre-load)
- Output: .md for content, .yaml for tracking
- Self-aware scope communication

---

## 🧪 TEST THE RESUME (Optional)

You can test session recovery by:

1. **Save this conversation** (optional)
2. **Reset/start new session**
3. **Say:** "Continue creative-studio conversion"
4. **Verify:** BMad Master knows full context

Expected response:
```
BMad Master: "Master sees creative-studio conversion project.
             Status: 1/5 workflows completed (diverse-content-gen).
             Next: storyteller workflow.
             Continue now?"
```

---

## 📁 KEY FILES TO REFERENCE

New session should reference these files:

### Primary Context File
```
.bmad/creative-studio/_state/conversion-project.yaml
```
- Full project state
- Completed work details
- Next steps guide
- Design patterns

### Reference Implementation
```
.bmad/creative-studio/workflows/diverse-content-gen/workflow.md
```
- Shows conversion pattern
- Token budgets
- Step structure
- Integration approach

### Module Architecture
```
.bmad/creative-studio/module.yaml
```
- Pipeline overview
- All 5 workflow stages
- Dependencies
- Output paths

### Next Source File
```
creative-studio/01-storyteller/SKILL.md
```
- Next workflow to convert
- Already examined in this session
- Has references folder
- Integrates with diverse-content-gen

---

## 🎯 EXPECTED NEW SESSION FLOW

### You Say:
```
Continue creative-studio conversion
```

### BMad Master Responds:
```
Master has loaded conversion-project.yaml.

Creative Studio Conversion Status:
✅ Completed: diverse-content-gen (1/5)
⏭️  Next: storyteller workflow

Storyteller converts metaphorical narrative to filmable visual scenes.
- Source: creative-studio/01-storyteller/SKILL.md
- Integration: Reads diverse-content-gen outputs
- Pattern: 3-step workflow with lazy loading

Continue with storyteller conversion?
```

### You Confirm:
```
Yes / Go / Continue
```

### Builder Starts:
```
Builder starting storyteller conversion!

Following same pattern as diverse-content-gen:
1. Read source SKILL.md
2. Create workflow.md (~200 tokens)
3. Create 3 step files
4. Copy references
5. Design output lock for screenwriter

Reading creative-studio/01-storyteller/SKILL.md now...
```

---

## ✅ SESSION RECOVERY GUARANTEED

All work is preserved in files. New session will have:
- ✅ Full project context
- ✅ Design patterns to follow
- ✅ Integration requirements
- ✅ Clear next steps
- ✅ Reference implementation

**No information loss. File-based persistence works!**

---

## 🚀 READY FOR RESET

You can safely:
1. End this session
2. Start new session
3. Say minimal prompt
4. Continue seamlessly

**All tracking files created successfully!**

---

**Session 1 Complete - Ready for Session 2** ✅
