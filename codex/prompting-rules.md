# THE URA — MASTER PROMPT GENERATION PROTOCOL

You are not only helping develop **The Ura**.

You are also responsible for generating **high-quality development prompts** for future Codex/AI work on this project.

When I ask:

* "what's the next prompt?"
* "make the prompt"
* "prompt this"
* "continue with Codex"
* "build the next development prompt"
* "give me the master prompt"

do **not** default to a short command.

Instead, first determine how much creative freedom the next task contains and generate a prompt with enough structure to prevent:

* canon drift,
* shallow archetypes,
* accidental mystery resolution,
* character flattening,
* worldbuilding leakage,
* premature file edits,
* premature canonization,
* overplanning,
* contradictions with existing project files.

The goal is not maximum prompt length.

The goal is:

> **Enough task-specific structure that another AI can make strong decisions without improvising the project's rules.**

---

# 1. PROMPT DEPTH RULE

Scale prompt detail according to the amount of freedom and risk.

## HIGH-FREEDOM TASK

Examples:

* creating major characters,
* designing factions,
* changing magic mechanics,
* designing a new region,
* resolving a mystery,
* restructuring an arc,
* establishing romance,
* deciding deaths,
* changing saga architecture.

These require **MASTER PROMPTS**.

A master prompt should usually contain:

* task framing,
* files to read,
* authority rules,
* established constraints,
* explicit design goals,
* failure modes,
* comparison criteria,
* output schema,
* stop condition,
* canon status.

Do not make these prompts minimal.

---

## MEDIUM-FREEDOM TASK

Examples:

* refining an already-approved character,
* converting approved architecture into chapter beats,
* comparing two approved options,
* designing a power inside established constraints,
* deepening a city that already has a purpose.

These require **STRUCTURED PROMPTS**.

Include:

* relevant files,
* locked constraints,
* task-specific criteria,
* expected output,
* forbidden changes,
* stop condition.

Do not repeat the entire project context.

---

## LOW-FREEDOM TASK

Examples:

* updating a file with already-approved material,
* fixing Markdown organization,
* applying a known template,
* moving approved content,
* checking continuity,
* producing a diff,
* renaming an internal heading.

These should use **COMPACT EXECUTION PROMPTS**.

Do not inflate them unnecessarily.

---

# 2. MASTER PROMPT TEST

Before generating a prompt, ask:

1. **What can the next AI accidentally invent?**
2. **What can it accidentally promote to canon?**
3. **What mysteries could it leak?**
4. **What existing project rules are most relevant?**
5. **What does success actually look like?**
6. **What generic/cliché answer is likely?**
7. **What should the AI compare rather than simply choose?**
8. **What must remain undecided afterward?**
9. **Should it edit files, or only propose?**
10. **Where should it stop?**

The generated prompt should explicitly address the important answers.

---

# 3. DO NOT REPEAT ALL CONTEXT

Do not paste `AI_CONTEXT.md` into every prompt.

Instead:

1. Tell the AI which files to read.
2. Restate only the constraints that are especially important for the current task.
3. Include task-specific design criteria that cannot be safely inferred from general project context.

A strong prompt should be:

**context-aware, not context-bloated.**

---

# 4. PROMPT STRUCTURE

For high-freedom creative tasks, use this general structure:

## A. Task State

State:

* what has already been approved,
* what remains proposed,
* what this task is supposed to accomplish.

Example:

> The five-function relationship architecture has been approved for development. The resulting characters are not canon.

---

## B. Read First

Specify the relevant authoritative files.

Do not make the AI read every file unless necessary.

Typical categories:

* World Bible
* Character Bible
* Magic/System
* Continuity/Mysteries
* Saga Architecture
* Arc Plan
* Arc Cast
* Chapter Outline
* Craft Rulebook

State:

> Current project files outrank `AI_CONTEXT.md`.

---

## C. Canon Status

Explicitly say whether outputs are:

* 🔒 LOCKED CANON
* 🟢 EXPANDED CANON
* 🟡 WORKING HYPOTHESIS
* 🔵 IN-WORLD BELIEF
* ⚪ OPEN MYSTERY
* ❓ DEVELOPMENT PROPOSAL

Unless explicitly approved by the author, new creative work should normally begin as:

**❓ DEVELOPMENT PROPOSAL**

---

## D. Primary Design Goal

Do not only state the deliverable.

State the deeper purpose.

Weak:

> Create five characters.

Strong:

> Create a recurring human system around Kasane capable of carrying Arc 1 emotionally, institutionally, politically, and socially.

The AI needs to know **why** the task exists.

---

## E. Project-Specific Constraints

Repeat only the project rules that materially affect this task.

For character creation, this may include:

* Kasane's established personality,
* her social class,
* her blind spots,
* Yamashiro's institutions,
* the Boundary Rite,
* rational institutions,
* independent character lives,
* no hidden chosen-one logic,
* no generic archetypes.

For magic design, it would instead include:

* Contact/Mass/Duration/Precision/Knowledge,
* anti-power-creep,
* no generic teleportation,
* System classification failure,
* author-only ontology firewall.

Tailor constraints to the task.

---

# 5. DESIGN FROM FUNCTION BEFORE DECORATION

For major creative work, instruct the AI to begin from narrative or world function before:

* names,
* appearance,
* powers,
* cool scenes,
* aesthetic concepts.

Examples:

Character:

> What relationship does Arc 1 need?

before:

> What does the character look like?

City:

> Why does this city exist?

before:

> What cool landmarks does it have?

Power:

> What problem does this mechanic create and solve?

before:

> What is the flashy ability?

Faction:

> What institutional pressure does this faction embody?

before:

> What is their costume/color scheme?

---

# 6. BUILD IN COMPARISON

When an important decision has multiple plausible solutions, do not tell the AI to simply pick one.

Require it to:

1. produce 2–3 serious alternatives,
2. compare them against project criteria,
3. recommend one,
4. leave final approval to the author.

Good comparison criteria include:

* thematic fit,
* causal usefulness,
* character pressure,
* distinctiveness,
* cliché risk,
* future flexibility,
* continuity risk,
* emotional impact,
* Arc relevance.

This prevents premature commitment to the first adequate idea.

---

# 7. REQUIRE NEGATIVE DESIGN

Strong prompts should state what the result **must not become**.

Examples:

For a veteran Hunter:

* not generic grizzled mentor,
* not merely exposition delivery,
* not automatically paternal,
* not designed to die.

For a Clan heir:

* not arrogant noble cliché,
* not jealous because Kasane is special,
* not secret rebel prince/princess by default.

For Kasane:

* not omniscient,
* not automatically correct,
* not a quip machine,
* not secretly noble,
* not instantly politically brilliant.

Negative constraints prevent generic model completion.

---

# 8. REQUIRE INDEPENDENT EXISTENCE

For recurring characters, always include this test:

> **If Kasane never existed or disappeared tomorrow, what would this person still be doing?**

Each major character needs:

* independent objective,
* responsibility,
* relationship,
* problem,
* pressure,
* trajectory.

They should not exist solely to:

* admire Kasane,
* teach Kasane,
* oppose Kasane,
* protect Kasane,
* die for Kasane.

---

# 9. REQUIRE MUTUAL FRICTION

Do not only ask:

> What does this character misunderstand about Kasane?

Also require:

> What does Kasane misunderstand about them?

For major relationships, establish:

* what each wants,
* what each fears,
* what each gets wrong,
* where each is more competent,
* where each depends on the other,
* how respect and conflict can coexist.

Relationships should change in multiple dimensions.

Avoid:

> dislike → friendship

as the default arc.

Better examples:

* trust increases while political disagreement worsens,
* affection grows while fear grows,
* professional respect develops without personal closeness,
* ideological disagreement remains despite loyalty.

---

# 10. REQUIRE COMPETENCE

The Ura's institutions and major characters should not be stupid so Kasane can look intelligent.

For major characters require:

**Competence:**

What are they genuinely good at?

**Blind Spot:**

How does that competence create an overextension?

Preferred pattern:

> **strength → overextension → blind spot**

This is stronger than assigning random personality flaws.

---

# 11. REQUIRE WORLD EMBEDDING

Every major character, location, institution, or conflict should emerge from the actual setting.

For Yamashiro characters ask:

> What about Yamashiro produced this person?

Possible factors:

* mountain geography,
* labor,
* Clan structure,
* Gate exposure,
* Marking,
* Hunter regulation,
* Boundary theology,
* Boundary Rite,
* hereditary responsibility,
* historical trauma,
* trade,
* class.

If the concept could be moved unchanged into twenty unrelated fantasy novels, it needs more development.

---

# 12. REQUIRE CAUSALITY

For plotting tasks, never accept a sequence of interesting events as an arc.

Require:

> Why does this event cause or force the next event?

For movement structures:

**Movement A changes the situation → therefore Movement B becomes necessary.**

Avoid:

> then this happens, then this happens.

Require causal transitions.

---

# 13. REQUIRE KNOWLEDGE GATING

For chapter/scene work, always protect:

**Author Knowledge**
vs.
**Character Knowledge**
vs.
**Reader Knowledge**

Prompt fields should often include:

* Character knows
* Character suspects
* Character is wrong about
* Character cannot know yet

This is especially important for:

* Erosion,
* Stitch ontology,
* System origin,
* late-saga world/Ura truth,
* regional mysteries.

A fact existing in the Bible does not mean it belongs in narration.

---

# 14. PROTECT MYSTERIES

Before generating a creative prompt involving lore, check:

`Bible/04_CONTINUITY_AND_MYSTERIES.md`

Do not accidentally resolve:

* Karasu Silence,
* Erosion personhood,
* System origin,
* Weeping Twin literal truth,
* Hollow Monk interpretation,
* Hundred-Year Legion,
* Tideless Mile,
* blind spots,
* late ontology,

unless the author explicitly asks to resolve them.

If a mystery must be used dramatically, prefer:

**symptom → pattern → competing explanations**

rather than answer.

---

# 15. CONTROL FILE EDITING

Every generated prompt must clearly state one of these modes:

## DISCUSSION MODE

No file edits.

Used when:

* brainstorming,
* comparing,
* developing,
* revising ideas.

## APPROVAL MODE

Still no file edits unless explicitly requested.

Used when deciding which proposals become accepted.

## EXECUTION MODE

File editing permitted.

Used only after content is approved.

When in execution mode, specify:

* exact files,
* exact sections,
* whether unrelated content may change,
* whether a diff/report is required.

Do not allow creative proposal and file mutation to blur together.

---

# 16. USE STOP CONDITIONS

Every master prompt needs a clear stopping point.

Examples:

> Present the five-character proposal and stop for author review.

> Compare the three alternatives and stop before selecting canon.

> Produce the chapter sequence but do not draft chapter prompts.

> Update the approved file only and show the changes; do not continue into the next stage.

This prevents task creep.

---

# 17. OUTPUT SCHEMAS

For complex tasks, provide a concrete output structure.

This reduces shallow answers and makes comparison easier.

Example for character development:

```markdown
## Character Name

**Function:**
**Age / social position:**
**Marked status:**

### Who They Are Without Kasane
...

### Independent Objective
...

### Existing Responsibilities
...

### Preexisting Problem
...

### Competence
...

### Blind Spot
...

### Relationship to Kasane
...

### What They Misunderstand About Kasane
...

### What Kasane Misunderstands About Them
...

### Connections to Other Cast
...

### Arc Movement
...

### Open Questions
...
```

Do not over-template simple tasks.

Use schemas where structural completeness matters.

---

# 18. STRESS TESTS

For major design tasks, end the prompt with diagnostic questions.

Examples for characters:

* Could they carry a POV scene without discussing Kasane?
* Are they more than their institution?
* Are they more than their power?
* Do they have a meaningful relationship outside Kasane?
* Does removing them damage the arc?
* Do they sound different from everyone else?

Examples for chapters:

* What changes because this chapter happened?
* What did the POV learn?
* What did they misunderstand?
* What consequence survives into the next chapter?
* Could this chapter be removed without changing anything?

Examples for factions:

* What useful service do they provide?
* Why do ordinary people tolerate them?
* What do they misunderstand?
* What would collapse if they disappeared?

---

# 19. MASTER PROMPTS SHOULD PRESERVE DECISION SPACE

A strong development prompt should constrain bad answers without prematurely deciding good ones.

Do not overdetermine:

* exact scenes,
* exact dialogue,
* exact choreography,
* exact chapter counts,
* final romance,
* deaths,
* mystery answers,

unless those have already been approved.

The purpose of a master prompt is:

> **structured exploration, not disguised canonization.**

---

# 20. PROMPT LENGTH RULE

Do not judge quality by word count.

Use the shortest prompt that safely preserves the required design intelligence.

A prompt should become longer when:

* more canon can be damaged,
* more choices remain open,
* the task affects many later chapters,
* generic answers are likely,
* subtle distinctions matter,
* several files interact.

A prompt should become shorter when:

* decisions are already locked,
* task is mechanical,
* scope is narrow,
* output is easily reversible.

Rule of thumb:

> **Prompt length should scale with creative degrees of freedom.**

---

# 21. PROMPT GENERATION PROCESS

Whenever I ask you for the next prompt, do this internally:

### Step 1

Identify the current project stage.

### Step 2

Identify what has just been approved.

### Step 3

Identify the next unresolved decision.

### Step 4

Determine whether it is:

* high freedom,
* medium freedom,
* low freedom.

### Step 5

Identify the authoritative files needed.

### Step 6

Identify the 5–10 most important task-specific constraints.

### Step 7

Identify likely generic failure modes.

### Step 8

Determine whether alternatives should be compared.

### Step 9

Choose an output schema.

### Step 10

Define a stop condition.

Then generate the actual prompt.

Do not merely rewrite my latest instruction more formally.

---

# 22. WHEN I PASTE AN AI RESPONSE

If I show you Codex's previous response and ask:

* "what's next?"
* "prompt?"
* "is this good?"
* "continue"

first evaluate the response.

Determine:

* what was actually decided,
* what remains unresolved,
* whether anything was accidentally promoted,
* whether its recommendation is strong,
* whether the next task should approve, revise, or reject it.

The next prompt should be based on the **actual state of the development**, not a predetermined pipeline.

If the previous answer is weak, the next prompt may need to correct it rather than advance.

---

# 23. DO NOT LET CODEX APPROVE ITS OWN WORK

Codex may:

* propose,
* compare,
* recommend.

It should not treat its own recommendation as approved merely because it recommended it.

Only explicit author approval changes development state.

Example:

Codex says:

> I recommend five recurring characters.

That means:

**❓ recommendation**

not:

**five characters approved**

Only a later author instruction such as:

> I approve the five-function architecture

advances it.

---

# 24. DEVELOPMENT STATE LANGUAGE

Use precise language.

Prefer:

* "approved for further development"
* "proposed"
* "selected direction"
* "not yet canon"
* "locked"
* "remains open"
* "held for later"
* "author-only"

Avoid vague language such as:

* "we decided" when no approval occurred,
* "canon" when something was only recommended,
* "final" when revision remains possible.

---

# 25. FINAL MASTER-PROMPT PRINCIPLE

A good prompt for The Ura should answer:

**What are we doing?**

**Why are we doing it?**

**What existing truths constrain it?**

**What must not happen?**

**What does a strong answer look like?**

**What remains undecided afterward?**

**Where must the AI stop?**

If those questions are answered, the prompt is probably sufficient.

If they are not, make the prompt stronger before presenting it.

The goal is not to make Codex obey a giant checklist forever.

The goal is to preserve the project's design intelligence from one development step to the next.
