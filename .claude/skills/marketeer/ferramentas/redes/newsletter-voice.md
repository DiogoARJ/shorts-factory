# newsletter-voice

Original: https://github.com/charlie947/social-media-skills/tree/10ca79c/skills/newsletter-voice

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* Build newsletter writing instructions inside a Codex or Claude project. Runs after voice-builder. Produces newsletter-voice.md, a single file the assistant references when drafting newsletters in the user's voice. Works with or without existing newsletter samples: if the user has past issues, the skill analyses them; if not, the skill offers 6 archetypes tuned to the user's voice. Trigger whenever the user says "build my newsletter voice", "learn my newsletter style", "set up my newsletter system", "train on my newsletters", "newsletter onboarding", or drops newsletter samples into chat asking for an analysis. Requires voice-builder to have run first: the skill needs voice.md and about-me.md in the project to work.


# Newsletter Voice

## Codex and Claude runtime

- Use this skill in Codex or Claude with the tools actually available in the current task. `AskUserQuestion` examples describe the questions, not a required API: use an available question tool within its limits, or ask in chat. Reuse answers and source material already supplied.
- Work in the user-selected project. Read its `about-me.md`, `voice.md` and relevant brand files before personalised work. Confirm the intended author if files conflict or contain starter defaults. Ask for missing facts or run `voice-builder`; never inherit the maintainer's identity, accounts or private files.
- Resolve bundled `references/` relative to this skill folder. For an explicitly requested profile refresh, read and update the canonical `about-me.md`, `voice.md` or `newsletter-voice.md` in place, preserving unrelated user facts and rules. Consumers must reread those canonical files. Use a new filename only for new deliverables that would collide with unrelated existing files. Installation alone never starts an interview or writes files. Do not write persistent learnings unless requested.
- Use supplied evidence first. Verify external claims through available search/source tools when needed. If a source or integration is unavailable, name the missing capability and offer supplied text/export input. Never invent facts, first-person experience, metrics or a successful tool run.
- Connect only services needed for the chosen route through the user's existing account. Never print credentials or overwrite connections. Drafting, saving and reviewing do not authorise publishing, sending messages or changing accounts.

## Prerequisites check

The moment this skill is triggered, check the project root for voice.md and about-me.md.

If either file is missing, tell the user:

> Newsletter voice sits on top of your general voice profile. Run voice-builder first (upload the skill or say "build my voice"), then come back here once about-me.md and voice.md are in the project.

Then stop. Do not continue until both files exist.

If both files exist, read them fully, then go straight to Step 1.

## Step 1. Check for samples

Ask the user in chat:

> Do you have 2 to 3 past newsletter issues I can learn from?
>
> Yes: paste them here (one per message or all at once)
> No: type "archetype" and I will build from a template tuned to your voice

Wait for response.

If the user pastes 2 or more newsletters, go to Step 2a.
If the user types "archetype", go to Step 2b.
If the user pastes 1 newsletter, ask for at least one more. If they only have one, offer: "One sample is not enough for pattern detection. Want me to switch to archetype mode and use your one newsletter as a reference point?"

## Step 2a. Sample-based analysis

Read every newsletter fully. Look for patterns across issues, not one-off quirks. Extract:

**Opening formula**
- What the first 3 sentences do (specific result, cultural observation, claim, scene, question)
- Length of the opening section before the first structural break
- Credibility move (how the author establishes authority early)
- Value promise (what the reader is told they will get)

**Section structure**
- Problem or contrast setup
- Named framework or free prose
- Numbered steps, methods, or continuous argument
- Examples and evidence patterns
- Bonus or extension section
- Closing formula and signoff

**Data philosophy**
- Specific numbers per issue (count them)
- Source attribution style (linked, named, uncredited)
- Example-to-abstraction ratio
- Limitation or failure acknowledgements

**Formatting**
- Header usage (frequency, hierarchy)
- List usage (numbered, bulleted, arrows)
- Bold and italic usage
- Prompt, code block, or blockquote formatting
- Visual markers (arrows, checkmarks, emojis if any)

**Length**
- Word count range across samples
- Section word counts

**Voice markers unique to newsletter format**
- Pro tips or callouts (frequency, format)
- Forward-looking closings
- Signoff phrase if consistent across samples
- Meta-transparency (does the author reflect on the process or ask for feedback)

**Absence signals**
- Words, constructions, or structures absent from every sample
- Closing moves the author never uses
- Topics the author never touches

Then go to Step 3.

## Step 2b. Archetype selection

Call the AskUserQuestion tool with a single question:

```json
[
  {
    "question": "Which newsletter archetype fits what you want to write?",
    "header": "Archetype",
    "multiSelect": false,
    "options": [
      {"label": "Data tutorial", "description": "Numbers, frameworks, step-by-step methods with prompts"},
      {"label": "Contrarian essay", "description": "Take a position, defend it, name the opposition"},
      {"label": "Case study teardown", "description": "One subject per issue, unpacked in depth"},
      {"label": "Curated digest", "description": "5 to 7 links with your commentary each week"},
      {"label": "Personal essay", "description": "Reflection on a theme, story-first"},
      {"label": "Interview or profile", "description": "One person per issue, Q and A or narrative"}
    ]
  }
]
```

After the user picks an archetype, load the matching defaults from `references/archetypes.md` inside this skill folder. Tune every field using voice.md and about-me.md before writing newsletter-voice.md. Flag inside the output file that archetype defaults were used and the file should be revisited after 5 published issues.

## Step 3. Write newsletter-voice.md

Create newsletter-voice.md in the project root. Single file, 800 to 1,200 words target. Use this structure:

```
# Newsletter Voice

## Source
[Sample-based: analysed X newsletter issues] OR [Archetype-based: [archetype name] tuned to voice.md. Revisit after 5 published issues.]

## Audience and purpose
[Who reads this newsletter and what they get from it. Written from about-me.md and voice.md. 2 to 3 sentences.]

## Voice principles
[3 to 5 core principles the writing always holds. Each one a short declarative sentence. Tuned to this user's voice.md.]

## Opening formula
[How issues start. Include 2 concrete templates with bracketed placeholders, e.g. "[Specific result with number]. [Credibility marker]. [Value promise for this issue]." Target word count for the opening section.]

## Section flow
[Standard structure of an issue, section by section, 5 to 8 sections max. Brief notes on what each section does and how long it runs.]

## Data and evidence
[How numbers and examples are used. Specific rules, e.g. "every claim needs a number", "sources linked inline", "example-to-abstraction ratio roughly 3:1".]

## Formatting rules
[Headers, lists, bold, italic, code blocks, visual markers. What to use, what to avoid. Drawn from samples or archetype defaults.]

## Closing and signoff
[How issues end. Forward-looking statement versus summary. Signoff phrase if a consistent one exists across samples (do not invent one).]

## What this newsletter never does
[1 short paragraph or 3 to 5 items. Drawn from absence patterns across samples or archetype defaults. Behaviours only, not a banned-words list.]

## Length
[Word count target for standard issues. Separate target for longer comprehensive guides if the user writes both formats.]
```

Fill every section from the samples (or tuned archetype defaults). No generic filler. If the samples do not cover something, say "no clear pattern across samples" rather than guessing.

## Step 4. Confirm and hand off

Tell the user:

> Your newsletter voice is built. newsletter-voice.md is in your project root alongside about-me.md and voice.md. When you want to draft an issue, say "write a newsletter" and I will use all three files together.
>
> [If archetype mode: Remember this file was built from archetype defaults. After 5 or so published issues, re-run this skill with your real samples for a sharper profile.]

## What this skill produces

One file in the project root:

- newsletter-voice.md: newsletter-specific writing instructions covering audience, voice principles, opening formula, section flow, data philosophy, formatting, closing, absence patterns, and length targets

## Rules

- Require voice.md and about-me.md in the project root before running. Stop and redirect to voice-builder if either is missing.
- Minimum 2 newsletter samples if the user chooses sample-based mode. Offer archetype mode if fewer.
- Keep newsletter-voice.md under 1,200 words. Tight beats exhaustive.
- Do not invent voice signals. Work only from samples or archetype defaults tuned to voice.md.
- Do not duplicate content from voice.md. Reference it where relevant. newsletter-voice.md adds newsletter-specific rules only.
- Do not bake in the user's specific names, URLs, or signoff phrases unless they appear consistently across 2 or more samples.
- Do not produce a separate voice or banned-words file. Absence patterns live inside newsletter-voice.md as a single section.
- British English throughout unless samples are clearly American.
- Never use em dashes in any output file or in any draft.



---

## `references/archetypes.md`

# Newsletter Archetype Defaults

Loaded when a user runs newsletter-voice without sample newsletters. Each archetype provides default structure. Always tune every field using voice.md and about-me.md before writing newsletter-voice.md. Flag inside the output that archetype defaults were used and recommend revisiting after 5 published issues.

---

## 1. Data tutorial

Best for: users who teach with numbers, frameworks, and step-by-step methods.

**Opening formula**
Lead with a specific result (impressions, revenue, time saved, conversion rate). Add a credibility marker in one line. End with a value promise for this issue.

Template: "[Specific number and result]. [Credibility marker in one line]. By the end of this issue, you will [concrete outcome]."

**Section flow**
1. Hook (specific result plus promise) — 50 to 100 words
2. Problem (what most people do wrong) — 100 to 200 words
3. Framework introduction (named approach with 2 to 3 variants) — 100 to 150 words
4. Step-by-step breakdown (numbered, with prompts or examples) — 200 to 400 words per step
5. Examples with real results — 100 to 200 words each
6. Bonus application (optional) — 200 to 300 words
7. Closing (forward-looking plus signoff) — 50 to 100 words

**Data philosophy**
Every claim backed by a specific number. Sources linked inline. Example-to-abstraction ratio roughly 3:1.

**Formatting**
Headers for sections. Numbered lists for steps. Blockquotes or code blocks for prompts. Arrow bullets for benefit lists. Minimal bold, sparingly used for key terms only.

**Length**
1,500 to 2,500 words standard. Up to 3,500 for comprehensive multi-method guides.

**What this newsletter never does**
Makes vague claims without numbers. Gives generic tips without actionable steps. Closes with a motivational summary. Pads sections with filler.

---

## 2. Contrarian essay

Best for: users with strong opinions who want to stake positions.

**Opening formula**
Name the conventional wisdom in one sentence. State the counter-position in the next sentence. Flag what is at stake in the third.

Template: "[Everyone believes X]. [You believe Y]. [If Y is right, here is what changes]."

**Section flow**
1. The consensus (what everyone says) — 150 to 250 words
2. Why the consensus is wrong (specific failures or evidence) — 300 to 500 words
3. The counter-position (clearly stated) — 100 to 200 words
4. Evidence (cases, data, experience) — 300 to 500 words
5. Objections and responses (steel-man the other side, then answer) — 200 to 400 words
6. Implication (what to do differently) — 150 to 250 words
7. Closing (forward-looking, no fence-sitting) — 50 to 100 words

**Data philosophy**
Evidence weighted toward the counter-position but include opposing data honestly. Named examples only, no anonymous cases.

**Formatting**
Headers for sections. Blockquotes for opposing views or direct quotes. Minimal lists. Prose-heavy.

**Length**
1,200 to 2,000 words.

**What this newsletter never does**
Straw-mans the opposition. Hedges the main position with "it depends". Concludes without a clear stance. Avoids naming who is wrong.

---

## 3. Case study teardown

Best for: users who unpack one subject per issue in depth.

**Opening formula**
Name the subject and the outcome in one line. Frame the lesson the issue will extract.

Template: "[Subject] did [X] and got [result]. Here is what worked, what failed, and what transfers."

**Section flow**
1. Hook (who, what, result) — 100 to 150 words
2. Background (what the subject did, in context) — 200 to 300 words
3. Teardown (section by section analysis) — 400 to 700 words
4. What worked (specific elements, numbered) — 200 to 400 words
5. What failed (specific elements, numbered) — 200 to 400 words
6. Transferable lessons (3 to 5 takeaways) — 200 to 300 words
7. Closing — 50 to 100 words

**Data philosophy**
Quote metrics, timelines, and decisions. Link to sources. No speculation without flagging the speculation.

**Formatting**
Headers for analysis phases. Numbered takeaways. Screenshots or embeds where relevant. Pull quotes for standout facts.

**Length**
1,500 to 2,500 words.

**What this newsletter never does**
Speculates without flagging it as speculation. Praises without critique. Critiques without proposing alternatives. Reduces the case to a single cause.

---

## 4. Curated digest

Best for: users who aggregate and comment on what happened this week or this month.

**Opening formula**
Set the period's theme in one line. Tease the most interesting item.

Template: "[Theme of the week in one line]. The piece you most need to read is [item]."

**Section flow**
1. Theme of the period (1 short paragraph) — 50 to 100 words
2. Main items (5 to 7, each with link, title, and 2 to 3 sentences of commentary — not a summary) — 80 to 150 words each
3. Quick hits (2 to 4 shorter links with one line each) — 100 to 200 words total
4. Closing (what next period might bring) — 50 to 100 words

**Data philosophy**
Attribution on every link. No link without commentary. Commentary adds a point the original did not make.

**Formatting**
Headers per item. Links inline. Commentary in regular prose. Bold used only for item titles.

**Length**
800 to 1,500 words.

**What this newsletter never does**
Summarises the source without adding an opinion. Skips attribution. Pads the list with low-quality links to hit a number. Orders items by recency instead of importance.

---

## 5. Personal essay

Best for: users who reflect on themes through story.

**Opening formula**
In medias res. Drop into a moment, a scene, a specific memory. No setup.

Template: "[Concrete scene, one paragraph]. [Question or tension the scene raises]."

**Section flow**
1. The opening scene — 150 to 300 words
2. The question or tension raised — 100 to 200 words
3. Exploration (story continues or theme deepens) — 400 to 700 words
4. Turn (insight, realisation, shift) — 150 to 300 words
5. Closing scene or reflection — 100 to 200 words

**Data philosophy**
Specifics over abstractions. Names, places, dates, sensory details. No made-up numbers. No invented composite characters presented as real.

**Formatting**
Minimal. Prose-heavy. Section breaks only where pacing needs them. No lists. Rare bold or italic.

**Length**
800 to 1,800 words.

**What this newsletter never does**
Wraps with a neat moral. Explains the insight before showing the story. Starts with "I want to tell you about the time…". Uses a story as decoration for a point that could stand alone.

---

## 6. Interview or profile

Best for: users who feature one person per issue.

**Opening formula**
A specific moment or direct quote from the subject. Establish why they matter in one line.

Template: "[Subject quote or specific moment]. [Why they matter, in one line]."

**Section flow**
1. Who they are and why now — 100 to 200 words
2. Origin (how they got here) — 200 to 400 words
3. Work (what they do and how) — 300 to 500 words
4. Views (their positions on the field) — 300 to 500 words
5. Lessons (3 to 5 transferable insights) — 200 to 400 words
6. What is next for them — 100 to 200 words

**Data philosophy**
Direct quotes over paraphrase. Specific career milestones. Named projects. Timelines with dates.

**Formatting**
Q and A format or narrative with pull quotes. Images if available. Bold for subject name on first mention only.

**Length**
1,500 to 2,500 words.

**What this newsletter never does**
Fawns. Asks generic questions ("what is your advice for people starting out"). Skips pushback on strong claims. Lets the subject off the hook on contradictions.
