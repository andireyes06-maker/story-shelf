# THE URA — WRITING RULEBOOK

**Canon-status legend:** 🔒 LOCKED CANON · 🟢 EXPANDED CANON · 🟡 WORKING HYPOTHESIS · 🔵 IN-WORLD BELIEF · ⚪ OPEN MYSTERY · ❓ DEVELOPMENT QUESTION / PROPOSAL. Full definitions in `00_PROJECT_INDEX.md`. Lower-authority material never silently overrides higher-authority material.

This file answers **"how should the novel actually be written?"** It is prose-production craft, not lore. Where a rule depends on lore, it points at the relevant Bible file instead of restating it.

---

## VOICE & TONE — CRAFT RULEBOOK (DEEPENED)

This section is the standard every draft gets checked against. It exists because the default failure mode of AI-assisted genre fiction is **narration that announces mood instead of earning it through specific, trackable consequence.** Every rule below exists to kill that failure mode.

### 1 Foundational Parameters

- **POV:** Close third-person limited. Locked to one character's perception per scene. No POV slipping.
- **Tone target:** Adventure with real stakes + wry humor threaded through. Not full grimdark. Not comedic parody. Closer to Solo Leveling / SSS-Class Revival Hero in general feel. Borrows from Shadow Slave: failure is common and genuinely costly, not binary or dramatic-for-its-own-sake.
- **Chapter frame:** Open wide (world/sky-scale image) → narrow to one character's sensory experience → close wide again (transformed landscape). Never open with exposition-heavy scene-setting — open in motion or on one vivid, specific detail instead.

### 2 The Core Diagnostic

If a sentence could be deleted without losing plot information, it is almost certainly atmosphere-slop. Every surviving sentence should do at least two jobs at once — advance plot *and* carry tone, characterize *and* build tension, describe setting *and* reveal character interiority.

### 3 Prose Mechanics

- Prioritize strong nouns and verbs over adjectives and adverbs. If a moment needs an adverb to land, the verb chosen was wrong.
- Avoid generic phrasing, filler sentences, and idiom-as-shorthand for emotion ("blood ran cold," "heart in throat," "a chill ran down his spine"). These carry zero character-specific information — ban them outright and replace with something true only to this character, this body, this moment.
- Banned AI-tell stock phrases (non-exhaustive, expand as caught): "something in their eyes," "they didn't know what to say," "little did they know," "a presence unlike anything he'd felt before," "an oppressive [atmosphere word] hung over—." If it could appear unchanged in a hundred other stories, cut it.
- Limit adjectives and adverbs generally — let strong verbs and precise nouns carry the sentence's weight.
- Ground every paragraph in physical space, prioritizing sound and touch over sight (sight is the lazy default sense). Ask: what does this exact place smell like, feel like underfoot/underfinger, sound like in its silences?

### 4 Interiority

- Never summarize an emotion the reader should infer. Show it through body language, physical action, or subtext instead of naming it.
- Internal monologue stays voice-consistent to the POV character's established personality/logic at all times — including under fear or crisis. (For Kasane specifically: even panic gets processed through charcoal-burning/containment logic, never generic panic-language.)
- No stated theses or on-the-nose realizations ("she realized that true strength was really about—"). Let conclusions live in decisions and actions, never in narrated insight.
- Don't summarize emotions — show them through body language, sensory detail, and subtext, and don't restate an emotion a second time once it's already been shown through action once. Trust the first instance.

### 5 Dialogue

- Real dialogue over exposition. Characters should never explain to each other things they both already know purely to inform the reader.
- Avoid perfect, overly articulate conversations. Lean into hesitation, awkwardness, misreadings. Let people interrupt each other, trail off, answer the wrong question, pause too long.
- Differentiate characters by rhythm and register, not just vocabulary — two characters from the same region should still have distinguishable sentence *shapes* (clipped vs. padded-and-formal, blunt vs. deflecting), not just different word choices.

### 6 Backstory & Exposition

- No "telling" exposition, ever. Backstory surfaces through memory triggered by a present sensory detail, through what a character deliberately avoids saying, or through an object and its history — never through a narrator or character reciting facts.
- No exposition-heavy opening lines for any chapter or scene. Start in motion or on one vivid, specific detail.

### 7 Pacing & Tension

- Don't resolve discomfort or ambiguity too quickly. A scene should sit in unresolved tension slightly longer than feels comfortable — that discomfort is usually the correct length, not a mistake to fix.
- No sudden tonal whiplash between scenes or chapters without earning the transition. Register can shift, but consistency of craft (not mood) holds it together.

### 8 The "How Dark" Problem

Grimness must come from tracked, specific, *named* cost — never from mood-lighting adjectives or narrator commentary about how bleak things are. The system's cost structure (permanent Trait loss, memory loss, a burned relationship) only works dramatically if the loss is concrete and specific enough for the reader to actually track it disappearing — not "she lost something precious" but the literal, nameable thing that's gone, stated once, plainly, without a eulogy attached.

### 9 System Text Voice

- Bracketed, ALL-CAPS, bureaucratic/clinical register. This is the primary vehicle for dark comedy in the whole story — deadpan, occasionally too honest, never emotionally aware in the way a person would be.
- Around the Stitch specifically: the System never produces a clean stat-block. It hedges, warns, or outright fails to categorize. It should read as visibly unsettled without ever using a word like "unsettled" — the unease has to live in formatting glitches, repeated redacted classification symbols, and escalating administrative panic (see reference example below), not in a stated tone.
- Reference example (established, keep as calibration):

```
[SKILL DETECTED]
[CLASSIFICATION: ■■■■■■■■■]
[STATUS: UNABLE TO PROCESS]
[RANK: —]
[RECOMMENDATION: CEASE IMMEDIATELY]
[NOTE: THIS LOG HAS BEEN FLAGGED FOR MANDATORY REVIEW (×47)]
```

  Note why this works: the "×47" is a *specific number*, not "repeatedly flagged" — specificity is what makes the absurdity land instead of reading as a vague gesture at bureaucratic comedy.

### 10 Structural Devices

- Everyman protagonist defined by what they are NOT (not a clan hunter, not a warden, not expected) — never by narrated humility, only by contrast in how other characters and institutions treat them.
- Mundane trade and tools become combat-relevant, consistent with the character's actual skill set, not a convenient invention for one scene.
- Bathos is load-bearing, not comic relief bolted onto grim content — cosmic stakes rendered through ordinary objects is a structural technique, not a joke that undercuts tension.

```
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| SLOP PATTERN                                      | WHY IT FAILS                        | FIX DIRECTION                                               |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| "An oppressive darkness hung over the village,    | Labels mood, gives no image         | Name one concrete wrongness: what's missing or present that |
| thick with unspoken dread."                       |                                     | shouldn't be, stated flatly                                 |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| "A chill ran down his spine. His blood ran cold." | Dead idiom, zero specific           | Ground fear in one specific, unglamorous physical action or |
|                                                   | information                         | noticing                                                    |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| "He had no idea this decision would cost him      | Narrator does the reader's          | Cut. Let payoff work without a flag planted in advance      |
| everything."                                      | anticipation for them               |                                                             |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| "She realized that true strength wasn't about     | Stated thesis, no character         | Let the value show in a choice under pressure, never as a   |
| power, but about the people you protect."         | actually thinks in taglines         | stated conclusion                                           |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| "A presence unlike anything he'd ever felt        | Unfalsifiable, un-picturable        | Describe one specific wrong detail (wrong number of joints, |
| before."                                          |                                     | wrong smell, wrong silence)                                 |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
| Two characters who both speak in full, articulate | Reads as artificial regardless of   | Interrupt, misread, trail off -- hesitation is realism, not |
| paragraphs during a crisis                        | content                             | weakness                                                    |
+---------------------------------------------------+-------------------------------------+-------------------------------------------------------------+
```

### 11 Borrowing Technique, Not Surface (governs how the influence series in the old Section 11 material get used)

🟢 The governing rule for every reference series already cited (Shadow Slave, Solo Leveling, SSS-Class Revival Hero, Tensura, Mushoku Tensei, Re:Zero): **borrow the engine, not the paint.** If a technique only works when copied alongside the original work's specific characters, mythology, or progression system, it hasn't been abstracted enough. Concrete list of surface tropes to actively avoid replicating: Shadow Slave-style direct Nightmare analogues, Solo Leveling-style exact dungeon/guild progression, Revival Hero-style tower structure, Tensura-style nation-building clone, Mushoku Tensei-style identical travel chronology, Re:Zero-style reset/loop mechanic. If a recognizable plot device shows up mainly because a reference work used it successfully, that's the signal to rebuild it in this setting's own terms. Test: if a technique makes Kasane feel less like Kasane, or Yamashiro feel like someone else's fantasy nation, or the System start behaving like another series' system — remove it.

### 12 Failure Mechanics: Compounding, Not Humiliating

🟢 Failure should compound forward rather than resolve within the scene it happens in — worked example chain, usable as a template: Kasane uses the Stitch publicly to save people → they survive (immediate) → witnesses report what she did (secondary) → Akaishi claims it proves hidden Clan blood (later) → Haejin traders hear a distorted version about an "unaffiliated mobile Gate" (later still) → someone approaches her with an offer based on an event they've completely misunderstood (much later). A mission where everyone survives but Kasane exposes Null Passage, a Clan gains leverage, a witness loses trust, or her body doesn't fully recover can matter more than a scene with a body count.

**Failure is not humiliation** — competent characters fail because information was incomplete, conditions changed, the opponent was also competent, no option was clean, or someone else's priorities differed, never because they "forgot to think." Kasane's intelligence should make her failures more interesting, not embarrassing: she fails because thinking can't fully eliminate uncertainty, which is a sharper version of the intellectual-flaw material already in Section 18.5.

**Success can be more dangerous than failure** — Kasane can save everyone, close the breach, and survive, and still leave the scene in a worse political position because the method she used can't be hidden. This is an important standing technique: it stops combat competence from automatically resolving narrative tension.

### 13 Power, Rank, and Consequence

🟢 **Rank must be demonstrated, not stated** — a title earns meaning through behavior: everyone yielding command, a Gate-Lord deferring immediately, calm handling of a situation that terrified others, technical precision nobody else has. Institutional reaction can establish rank as effectively as combat does.

**Power fantasy should not be apologized for** — when Kasane earns a real breakthrough, let the scene acknowledge it ("that was extraordinary") rather than undercutting it with irony; the balancing mechanism is consequence, not embarrassment ("now everyone important knows she can do it" — both can be true at once).

**Power reveals must alter relationships, every time** — whenever Kasane demonstrates a major new Stitch capability, the scene should answer: who saw it, who understands her differently now, who becomes afraid, who becomes hopeful, who just gained leverage over her. A power reveal with no social consequence is a wasted beat.

### 14 The Escalation Model (eight axes, not one)

🟢 Escalation should never mean only "the enemy gets stronger." Track it across: **Capability** (what Kasane can do), **Cost** (what she risks), **Visibility** (who knows about her), **Geography** (how much of the world the story spans), **Politics** (which institutions get involved), **Information** (mysteries should deepen, not just resolve), **Relationships** (how many people now depend on each other), and **Threat** (the Erosion's actual progression, Section 11). Genuine escalation moves several of these at once without needing ever-larger combat to carry the feeling of stakes rising.

### 15 The Information Reveal Rule (mystery pacing structure)

🟢 For any major mystery, the reveal order should be **symptom → pattern → competing explanations → new evidence → partial model → model failure → deeper model** — never a flat "mystery → answer." Worked example: *why are Gates more frequent* → *the Erosion is weakening the seam* → *what is the Erosion* → *its behavior suggests both process and intelligence* → *why does it behave that way* → *the boundary itself isn't what humanity assumed* (this last step is Section 5H/8H's adopted late-saga reveal). Each answer should expand the world rather than simply closing a box — a good answer produces a better question, not a smaller one.

### 16 The Consequence Ledger (tracking tool for major choices)

🟢 For any major decision in a drafted chapter, it's worth being able to answer, in order: **Choice → immediate result → who noticed → who benefited → who lost → what rumor it produced → how an institution reacted → what it causes later.** This is what keeps continuity from becoming decorative — an Arc 1 choice should be traceable into Arc 3's consequences, an Arc 2 commercial decision into Arc 4's supply situation, an Arc 4 military failure into Arc 5's refugees (extends Section 17's "world doesn't wait" and off-page-development material with an actual tracking method).

### 17 Arc-Ending Discipline: Do Not Fully Fix a Region

🟢 Arc endings should produce movement, not utopia — no single protagonist resolves hereditary legitimacy, an entire economic system, a religious hierarchy, mass conscription, or state collapse in one arc (all already true of Yamashiro/Haejin/Bailian/Erkhaan/the Harrowed respectively). What an arc *can* change: a law, a precedent, an alliance, public understanding, a leadership figure, or the range of alternatives people can now imagine. The region keeps existing and keeps having problems after the protagonist leaves — consistent with Section 17's off-page-development material, stated here as an explicit ceiling on what "resolution" is allowed to mean.

### 18 Scene-Level Craft: Action Layers and Multi-Function Prose

🟢 A major action scene should carry at least three simultaneous layers: a **physical problem** (what's immediately dangerous), an **information problem** (what the POV character doesn't understand yet), and a **character problem** (what personal limitation or relationship shapes the choice). A sequence that only asks "can they win" is too thin.

At the sentence level, the same principle scaled down: prefer details that do more than one job at once. Not *"Kasane was nervous entering the fortress"* — instead, she notices the floor is polished enough that her work boots leave marks, which simultaneously carries anxiety, unfamiliar wealth, class difference, physical setting, and her habitual noticing of practical consequences (Section 18.1's hands-first observation habit). This is the same "every sentence does two jobs" diagnostic already locked in Section 1.2, given a second worked example.

### 19 Craft Checklists — Arc-Level and Scene-Level

🟢 Two reusable checklists, meant to be run against a draft before locking it, not new lore:

**Before locking an arc:** What does the protagonist want, and what do they misunderstand? What changes in them permanently? What does the regional institution do well, and who does it harm — and what condition is different about it by the arc's end? Why does this arc have to happen in this specific geography? What does the protagonist know that others don't, and vice versa? What important information exists only in distorted form (Section 16)? What background myth becomes more meaningful later (Section 11.7)? What goes wrong without ending the story? What doesn't return to normal afterward? Whose trust changes? What local development reflects the larger Erosion escalation without explaining it outright (Section 11.13)? If these can't be answered, the arc likely lacks structural depth.

**For a major scene**, it should ideally do several of the following at once (never forced to do all): advance immediate plot, change a relationship, reveal world information, complicate a character's belief, create a future consequence, establish geography, surface institutional pressure, alter someone's credibility, create or resolve a practical problem. Avoid scenes that accomplish exactly one of these and nothing else.

### 20 Closing Synthesis

🟢 What each reference series contributes in one line, restated as this project's own craft identity rather than as homage: failure has teeth (Shadow Slave); power has legibility (Solo Leveling); sincerity and humor coexist (SSS-Class Revival Hero); power changes institutions and relationships (Tensura); the world has distance, time, history, and consequence (Mushoku Tensei); knowledge and trust are both costly (Re:Zero). Combined: **becoming more capable should give characters more ability to act while simultaneously increasing how much their choices can damage.**

**What the whole project should feel like**, as a standing check: large but not vague; dark but not hopeless; funny but not flippant; powerful but not effortless; mythic but grounded in labor; political but character-driven; mysterious but fair to attentive readers; ensemble-driven without erasing individual identity; escalating without abandoning ordinary life.

**The craft philosophy in one line:** *Make power legible, failure persistent, institutions rational, relationships earned, geography real, information imperfect, and every victory expensive enough to change what comes next.*

---

---

## INFLUENCE-SERIES TECHNIQUE REFERENCE (original, base version — extended by the deepened rules above)

**From SHADOW SLAVE**
- Failure is common and expensive, not binary or dramatic.
- Growth costs something permanent.
- Darkness without nihilism — the world is genuinely hard, people survive and keep going.

**From SOLO LEVELING**
- Rank ladder legibility — universal F-S notation, genre readers know instantly what it means.
- Guild/faction politics as genuine plot engine in the Trade Republic arc.
- The power fantasy escalation arc is real and earned, not ironized away.

**From SSS-CLASS REVIVAL HERO**
- Wry tone threading through genuine stakes.
- Faith-vs-power tension (Bailian arc).
- Ensemble is earned, not assembled by plot convenience.

**From TENSURA**
- Faction-building as arc structure: Each arc is about what the institution in that region is doing, failing at, or becoming — not just protagonist power growth.
- Humanizing the Ura: The second world is inhabited, not just dangerous. The Erosion has context. The Ura has factions or history that Kasane's glimpses begin to reveal.
- Power creates political obligation: As Kasane becomes more capable, she becomes more politically significant — a burden, not just a reward.
- Retinue grows independently: Secondary characters develop off-page between arcs. They don't wait.
- Evolution as sacrifice: The jump from Early to Mid Stitch, Mid to Late, should feel like a threshold crossed that cannot be uncrossed. Kasane comes out of it changed, not just stronger.

**From MUSHOKU TENSEI**
- Geography as genuine obstacle: Travel between regions is difficult, dangerous, and rare. This is what makes Kasane's ability to cross boundaries remarkable.
- Rank requires craft: Rank reflects accumulated demonstrated competence, not just kill count or raw power.
- Long timescale: The saga spans years. Characters age. The world changes between arcs.
- Consequence chains: Failure in Arc 1 has reputation/relationship consequences visible in Arc 3. Track what characters lose and whether they've recovered.
- Mythology layers into present events: Each region's old stories about the Ura contain fragments of truth. Surface these as background texture in early arcs (concrete fragments locked in Section 9).
- Rumor is a graded signal, not a binary: Every region has its own reason for rumor to be distorted (clan politics, guild profit, religious censorship, state suppression, personal reputation-building — see Section 8 per-region rumor characters). Kasane's observational-intelligence trait (Section 5) is the reader's tool for weighing rumor against its source rather than taking it at face value or dismissing it outright.
- Distant places exist before they're visited: Each region has at least one named landmark city/site (Section 6, Section 8) referenced in dialogue and rumor well before any POV character sets foot there — this is what makes the world feel larger than the current arc's footprint.

**From RE:ZERO**
- Information asymmetry: Kasane's glimpses through the Stitch give her knowledge others can't verify. She can't prove how she knows. Other characters must decide whether to trust thin evidence. This is an ongoing burden, not a power.
- Psychological cost is social and relational: The Stitch's cost isn't just nosebleeds. It's isolation — she experiences things nobody else does, carries weight she can't share. She is hard to be close to.
- The world does not wait: The Erosion is working whether or not Kasane is paying attention. The Haejin guild wars deteriorated off-page. Events happen without a protagonist present.
- Earned trust: Other characters do not believe Kasane because she says so. Credibility is a resource that must be built and can be burned.
- Factions are non-binary: Every institution has a coherent internal logic and legitimate interests. The Bailian Communion genuinely protects people. The Erkhaan Dominion genuinely holds a front. Both things are true alongside the harm they cause.
- Edge is social and observational: Kasane's primary edge before (and separate from) the Stitch is her ability to read people and situations. Her power amplifies an existing edge; it does not replace it.

---

---

## Cross-References Out of This File

- Full Stitch mechanics: `Bible/03_MAGIC_AND_SYSTEM.md`.
- Kasane-specific writing rules (Do/Don't list): `Bible/02_CHARACTERS.md`.
- Yamashiro-specific and Erosion-specific writing rules: `Bible/01_WORLD_BIBLE.md`.
- Convergent-ensemble writing rules: `Story/01_SAGA_ARCHITECTURE.md`.
- The chapter-prompt template and Chapter 1's specific refinements: `Story/Arc_01_Yamashiro/CHAPTER_OUTLINE.md`.
- The locked decision that `the_coopers_reckoning.md` is voice-reference only, not canon: `Story/Arc_01_Yamashiro/CHAPTER_OUTLINE.md` (moved there since it's a Chapter-1-specific process decision).
