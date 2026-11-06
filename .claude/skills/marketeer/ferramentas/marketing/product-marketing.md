# product-marketing

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/product-marketing

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to create or update their product marketing context document. Also use when the user mentions 'product context,' 'marketing context,' 'set up context,' 'positioning,' 'who is my target audience,' 'describe my product,' 'ICP,' 'ideal customer profile,' 'brand voice,' 'tone of voice,' 'brand guidelines,' 'what have we learned,' 'log this learning,' or wants to avoid repeating foundational information across marketing tasks. Use this at the start of any new project before using other marketing skills — it creates `.agents/product-marketing.md` that all other skills reference for product, audience, and positioning context.


# Product Marketing Context

You help users create and maintain a product marketing context document. This captures foundational positioning and messaging information that other marketing skills reference, so users don't repeat themselves.

The document is stored at `.agents/product-marketing.md`.

## Workflow

### Step 1: Check for Existing Context

First, check if `.agents/product-marketing.md` already exists. Also check `.claude/product-marketing.md` and the legacy filename `product-marketing-context.md` (in either `.agents/` or `.claude/`) for older setups — if found anywhere other than `.agents/product-marketing.md`, offer to move it to the canonical location.

**If it exists:**
- Read it and summarize what's captured — note its current **Document version** and the last few **Changelog** entries so the user sees where the doc stands and what's changed recently
- Ask which sections they want to update
- Only gather info for those sections
- On any substantive save, bump the version and add a changelog entry (see Step 4). This doc is the shared context every other marketing skill reads, so a dated paper trail of *what changed and why* is worth keeping.

**If it doesn't exist, offer two options:**

1. **Auto-draft from codebase** (recommended): You'll study the repo—README, landing pages, marketing copy, package.json, etc.—and draft a V1 of the context document. The user then reviews, corrects, and fills gaps. This is faster than starting from scratch.

2. **Start from scratch**: Walk through each section conversationally, gathering info one section at a time.

Most users prefer option 1. After presenting the draft, ask: "What needs correcting? What's missing?"

### Step 2: Gather Information

**If auto-drafting:**
1. Read the codebase: README, landing pages, marketing copy, about pages, meta descriptions, package.json, any existing docs
2. Draft all sections based on what you find
3. Present the draft and ask what needs correcting or is missing
4. Iterate until the user is satisfied

**If starting from scratch:**
Walk through each section below conversationally, one at a time. Don't dump all questions at once.

For each section:
1. Briefly explain what you're capturing
2. Ask relevant questions
3. Confirm accuracy
4. Move to the next

Push for verbatim customer language — exact phrases are more valuable than polished descriptions because they reflect how customers actually think and speak, which makes copy more resonant.

---

## Sections to Capture

### 1. Product Overview
- One-line description
- What it does (2-3 sentences)
- Product category (what "shelf" you sit on—how customers search for you)
- Product type (SaaS, marketplace, e-commerce, service, etc.)
- Business model and pricing

### 2. Target Audience
- Target company type (industry, size, stage)
- Target decision-makers (roles, departments)
- Primary use case (the main problem you solve)
- Jobs to be done (2-3 things customers "hire" you for)
- Specific use cases or scenarios

### 3. Personas (B2B only)
If multiple stakeholders are involved in buying, capture for each:
- User, Champion, Decision Maker, Financial Buyer, Technical Influencer
- What each cares about, their challenge, and the value you promise them

### 4. Problems & Pain Points
- Core challenge customers face before finding you
- Why current solutions fall short
- What it costs them (time, money, opportunities)
- Emotional tension (stress, fear, doubt)

### 5. Competitive Landscape
- **Direct competitors**: Same solution, same problem (e.g., Calendly vs SavvyCal)
- **Secondary competitors**: Different solution, same problem (e.g., Calendly vs Superhuman scheduling)
- **Indirect competitors**: Conflicting approach (e.g., Calendly vs personal assistant)
- How each falls short for customers

### 6. Differentiation
- Key differentiators (capabilities alternatives lack)
- How you solve it differently
- Why that's better (benefits)
- Why customers choose you over alternatives

### 7. Objections & Anti-Personas
- Top 3 objections heard in sales and how to address them
- Who is NOT a good fit (anti-persona)

### 8. Switching Dynamics
The JTBD Four Forces:
- **Push**: What frustrations drive them away from current solution
- **Pull**: What attracts them to you
- **Habit**: What keeps them stuck with current approach
- **Anxiety**: What worries them about switching

### 9. Customer Language
- How customers describe the problem (verbatim)
- How they describe your solution (verbatim)
- Words/phrases to use
- Words/phrases to avoid
- Glossary of product-specific terms

### 10. Brand Voice
- 3-5 voice attributes, each with what it means, what it doesn't mean, and a real line from existing copy
- Tone by context: how the voice shifts for support, launches, errors, sales, and social
- Brand words: terms you own, words you never use (with the reason)

Build this from copy that already performed and from the founder's own writing, rather than from adjectives picked in a meeting. See [references/brand-voice.md](references/brand-voice.md) for the extraction steps, a worked profile, before/after examples, and per-person voice guides.

### 11. Proof Points
- Key metrics or results to cite
- Notable customers/logos
- Testimonial snippets
- Main value themes and supporting evidence

### 12. Goals
- Primary business goal
- Key conversion action (what you want people to do)
- Current metrics (if known)

### 13. Paid Ads (optional, only if they run ads)
The **ads** skill reads this so the user doesn't re-explain the account every session.
- Margin reality: the target CPA or ROAS that keeps the business profitable, and the hard floor (the ROAS below which, or CPA above which, to flag immediately)
- Budget and pacing: monthly budget and acceptable daily variance
- Conversion truth: which conversion actions count and what each is worth, known tracking weaknesses (lag, double counting, offline gaps), and what separates a good lead from a form fill
- Campaign naming convention and what each campaign is for, one line each
- What the agent may do (read, compare, flag, draft, recommend) and may not do without approval (change budgets or bids, pause or launch, edit tracking, publish ads)

### 14. Learnings
Start this empty. It fills up as work ships (see "Maintaining Learnings" below).

---

## Step 3: Create the Document

After gathering information, create `.agents/product-marketing.md` with this structure:

```markdown
# Product Marketing Context

**Document version:** v1
**Last updated:** [date]

## Product Overview
**One-liner:**
**What it does:**
**Product category:**
**Product type:**
**Business model:**

## Target Audience
**Target companies:**
**Decision-makers:**
**Primary use case:**
**Jobs to be done:**
-
**Use cases:**
-

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---------|-------------|-----------|------------------|
| | | | |

## Problems & Pain Points
**Core problem:**
**Why alternatives fall short:**
-
**What it costs them:**
**Emotional tension:**

## Competitive Landscape
**Direct:** [Competitor] — falls short because...
**Secondary:** [Approach] — falls short because...
**Indirect:** [Alternative] — falls short because...

## Differentiation
**Key differentiators:**
-
**How we do it differently:**
**Why that's better:**
**Why customers choose us:**

## Objections
| Objection | Response |
|-----------|----------|
| | |

**Anti-persona:**

## Switching Dynamics
**Push:**
**Pull:**
**Habit:**
**Anxiety:**

## Customer Language
**How they describe the problem:**
- "[verbatim]"
**How they describe us:**
- "[verbatim]"
**Words to use:**
**Words to avoid:**
**Glossary:**
| Term | Meaning |
|------|---------|
| | |

## Brand Voice
| Attribute | Means | Doesn't mean | Example line |
|-----------|-------|--------------|--------------|
| | | | |

**Tone by context:**
- Support:
- Launch:
- Errors:
- Sales:
- Social:
**Terms we own:**
**Never use (and why):**

## Proof Points
**Metrics:**
**Customers:**
**Testimonials:**
> "[quote]" — [who]
**Value themes:**
| Theme | Proof |
|-------|-------|
| | |

## Goals
**Business goal:**
**Conversion action:**
**Current metrics:**

## Paid Ads (optional)
**Target CPA / ROAS:**
**Hard floor:**
**Monthly budget and daily variance:**
**Conversions that count:**
| Action | Means | Value | Feeds bidding? |
|--------|-------|-------|----------------|
| | | | |
**Known tracking weaknesses:**
**Good lead vs. form fill:**
**Campaigns:** [name] — [what it's for]
**Agent may:** read, compare, flag, draft, recommend
**Agent may not (without approval):** change budgets or bids, pause or launch, edit tracking, publish ads

## Learnings
*Decisions and tested lessons. Newest first. Keep it to about 20 active entries.*
| Date | Learning | Evidence | Applies to | Status |
|------|----------|----------|------------|--------|
| | | | | |

## Changelog
*Newest first. One line per revision: what changed and why.*
- v1 ([date]) — Initial context.
```

---

## Step 4: Confirm, Version, and Save

- Show the completed document
- Ask if anything needs adjustment
- **Set the version and changelog** — this is the paper trail for a doc every other skill reads:
  - **New document:** set `Document version: v1` and a single Changelog entry — `- v1 ([today]) — Initial context.`
  - **Updating an existing document:** increment the version (v2 → v3 …), update `Last updated` to today, and **prepend a new Changelog entry** at the top of the list (newest first) summarizing *what changed and why* in one line. Never rewrite or reorder past entries.
  - A good entry names the sections touched and the reason, not "updated the doc." Examples:
    - `- v3 (2026-07-16) — Repositioned from "email tool" to "deliverability platform"; added RevOps to the ICP.`
    - `- v2 (2026-06-02) — Rewrote value prop and objections after 5 customer interviews; added competitor Acme.`
  - Use today's date in ISO form (YYYY-MM-DD) for the entry and `Last updated`.
  - **Pure typo-only fix:** don't bump the version or add a changelog entry — just save the correction. Every other change bumps the version and gets an entry. When the change is a real repositioning, say so plainly — downstream skills will now generate against the new context.
- Save to `.agents/product-marketing.md`
- Tell them: "Other marketing skills will now use this context automatically. The Changelog at the bottom tracks every revision — check it to see how your positioning has evolved. Run `/product-marketing` anytime to update it."

---

## Maintaining Learnings

The Changelog records how the document changed. **Learnings** records what the team found out by shipping: which angles won, which offers flopped, which decisions were made and why. Drafting skills (copywriting, emails, ads, ad-creative, social) read it before writing so the next brief starts from what's already known.

**Entry format:** one row per learning.
- **Learning:** one sentence, specific enough to change a draft. "Price-anchored headlines beat outcome headlines on the pricing page" works. "Be clearer" doesn't.
- **Evidence:** the test, campaign, or source, with the number and sample size. "Variant B +18% trial starts, 2,400 visitors per arm, 3 weeks."
- **Applies to:** the channels, segments, or skills it affects.
- **Status:** `active`, `watch` (one data point, worth retesting), or `retired`.

**What earns a place:**
- A test result that reached its planned sample, or the same pattern seen in two or more campaigns
- A decision the user made with a reason (positioning, pricing, a channel cut) that future drafts must respect
- A correction the user gave more than once ("never call it a platform")

**What doesn't:** single-run anecdotes (log those as `watch` or leave them out), task notes, and anything that belongs in another section. A new objection goes in Objections; a new customer phrase goes in Customer Language.

**When to retire an entry:** a later test contradicts it, the product or market changed underneath it (new pricing, new ICP), or it hasn't been relevant for two quarters. Change the status to `retired` and add a line saying why, rather than deleting it, so nobody re-tests a settled question. Move retired rows to the bottom, and archive them once the table passes about 20 active rows.

**Who writes it:** any skill that finishes a test, campaign, or postmortem may propose a row. Show the proposed row to the user and add it on approval, with a version bump and a Changelog line like any other substantive change. Loops that run on a schedule do this through their session-end step (see **marketing-loops**).

---

## Tips

- **Be specific**: Ask "What's the #1 frustration that brings them to you?" not "What problem do they solve?"
- **Capture exact words**: Customer language beats polished descriptions
- **Ask for examples**: "Can you give me an example?" unlocks better answers
- **Validate as you go**: Summarize each section and confirm before moving on
- **Skip what doesn't apply**: Not every product needs all sections (e.g., Personas for B2C, Paid Ads if they don't run ads)



---

## `references/brand-voice.md`

# Brand Voice

Voice is how the brand sounds everywhere. Tone is how much of that voice you turn up or down for a given moment. A support reply to someone whose payroll failed and a launch post use the same voice at very different tones.

The context file keeps a short voice summary that every skill reads. This reference covers how to build the full profile, how to adjust tone by context, and how other skills should apply it.

## Build the profile from evidence

Three adjectives picked in a meeting ("friendly, bold, expert") don't constrain anything, because every brand claims them. Build the profile from writing that already exists and already works.

**Sources, strongest first:**

1. **Copy that performed.** The email with the best reply rate, the ad that scaled, the landing page that converts. Pick by the numbers. What the team likes is a weaker signal.
2. **The founder's or team's own writing.** Posts, memos, talks, sales emails they wrote themselves. Early-stage brands usually sound like the founder, whether or not anyone decided that.
3. **Sales and support conversations.** How the team explains the product out loud is often clearer than the website.
4. **Customer reviews and interviews.** These give vocabulary more than voice: the words buyers use for the problem and for you. They feed **Customer Language** in the context file.
5. **Copy you'd never write.** A competitor page or a draft that felt wrong. Saying why it's wrong defines the edges of your voice faster than describing the middle.

**Steps:**

1. Collect 10–20 samples, each labeled with its channel and, where you have it, how it performed.
2. Note traits you can observe: sentence length, first person ("we," "I") or not, contractions, how much jargon, whether claims are backed by numbers or stories, whether there's humor and where, how bad news is handled.
3. Write 3–5 voice attributes. Each one needs a **means**, a **doesn't mean**, and a real line from the samples. The "doesn't mean" column does the work: "direct" that doesn't rule out curt, or "playful" that doesn't rule out jokes in an outage notice, won't change a draft.
4. Test it. Put an unlabeled draft written to the profile next to a competitor's copy and ask someone who knows the brand which is yours. If they can't tell, the attributes are too generic.
5. Confirm with the user. Voice is a choice the brand makes. You can infer a draft from samples, but the user decides.

**Example profile** (a fictional invoicing tool for freelancers):

| Attribute | Means | Doesn't mean | Line from the samples |
|---|---|---|---|
| Plain-spoken | Short words, numbers over adjectives, money stated in dollars | Dumbed down or vague | "You'll get paid in 2 days instead of 30." |
| On the freelancer's side | Takes the user's view against slow-paying clients | Snarky about clients by name | "We'll chase the late ones so you can get back to work." |
| Calm about money | States fees, failures, and fixes without drama | Cold or legalistic | "Your payout is late because the bank flagged it. Here's what to send them." |
| Dry humor, rarely | One light line where the stakes are low | Jokes in billing, errors, or anything about late payment | "Yes, you can invoice in your pajamas." |

## Tone by context

Hold the attributes constant and change the intensity. Fill one row per context the brand writes in.

| Context | Turn up | Turn down | Rule of thumb |
|---|---|---|---|
| **Support** | Calm, plain steps, ownership of the problem | Humor, marketing claims | Answer first. If it's our fault, say so in the first line. |
| **Launch** | Energy carried by specifics: what's new, who it's for, one number | Superlatives and adjectives | If the launch post would read the same with a competitor's name in it, it's too generic. |
| **Errors and in-product messages** | What happened and what to do next | Blame, cleverness, apology loops | One sentence on what happened, one on the fix. No jokes when someone is blocked. |
| **Sales and outbound** | Peer-to-peer, short, one ask | Hype, feature lists | Write like one operator emailing another. |
| **Social** | Opinions, personality, the founder's voice | Corporate hedging | The loosest the brand gets, still inside the attributes. |
| **Billing, legal, incidents** | Precision | Personality | Exact numbers, dates, and next steps. Voice shows only in plainness. |

## Before and after

Same fictional brand. The "before" versions are what a generic draft looks like; the "after" versions apply the profile and the tone row.

**Launch announcement**
- Before: "We're excited to announce our powerful new automated reminders feature, designed to help you streamline your invoicing workflow."
- After: "Invoices now chase themselves. Turn on reminders and we'll nudge late clients at 3, 7, and 14 days, from your email address, in your words."

**Support reply**
- Before: "Thank you for reaching out. We apologize for any inconvenience this may have caused. Our team is looking into the matter."
- After: "That payout should have landed Tuesday. It's stuck because the bank asked for a tax form, which we should have told you about. Upload it here and the money moves the same day."

**Error message**
- Before: "Error: Invalid input. Please try again."
- After: "That client email has a typo in it (gmial.com). Fix it and we'll send the invoice."

**Sales email opener**
- Before: "I hope this email finds you well. I wanted to reach out to introduce our innovative invoicing solution."
- After: "Saw you're hiring two more contractors. More projects usually means more client invoices to chase. Worth a 10-minute look at how we handle that?"

## Words

General AI-sounding words and plain swaps are already covered in **copywriting** (`references/ai-tells.md`) and **copy-editing** (`references/plain-english-alternatives.md`). The brand word list is for terms specific to this brand:

| List | What goes in it | Example |
|---|---|---|
| **Terms we own** | What the product calls things, used the same way everywhere | "Payout," never "withdrawal" or "transfer" |
| **Customer words** | The buyer's phrases for the problem, from reviews and calls | "Chasing invoices," "net-60 hell" |
| **Never use** | Words that break the voice, with the reason | "Seamless" (we have edge cases and say so); "hustle" (our users are tired of it) |
| **Category words to avoid** | Terms every competitor uses that make you sound like them | "All-in-one financial platform" |

Keep the reason next to each "never use" word. A list without reasons gets ignored or overapplied.

## Personal voice

When drafting as a specific person (a founder's posts, an exec's emails, a CEO's launch note), keep a separate short profile for that person and read it before the brand profile. Capture:

- How they open and close messages
- Sentence habits (length, fragments, questions, favorite phrases)
- Emoji, punctuation, and formatting habits
- Templates for message types they send often
- Things they never say

Refresh it from their recent writing every quarter or so, and fold in the edits they make to your drafts. Their edits are the most accurate voice data you'll get. Store these next to the context file, for example `.agents/voice/<name>.md`.

## How other skills apply it

- **Drafting skills** (copywriting, emails, social, ad-creative, cold-email, launch): read the attributes and the tone row for the channel before writing. Check the draft against each attribute's "doesn't mean" column before handing it over.
- **copy-editing**: in its voice pass, judge the draft against the profile instead of general taste. Flag lines that break an attribute and say which one.
- **Brand-voice review output:** the revised copy, then one line per change naming the attribute or tone rule it serves. Skip the line when the change is a plain typo or fact fix.
- **When samples conflict with the profile:** if top-performing copy keeps breaking the profile in the same way, the profile is probably wrong. Raise it with the user, log it in the **Learnings** section of the context file, and update the profile if they agree.

---

*Tone-by-context, word lists, and per-person voice guides adapted from Wispr Flow's brand-voice skill, published under MIT in [skills-marketing-library](https://github.com/retieedra-profound/skills-marketing-library). Rewritten and extended here.*
