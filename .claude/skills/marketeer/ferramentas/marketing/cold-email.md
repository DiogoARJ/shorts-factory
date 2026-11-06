# cold-email

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/cold-email

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* Write and run B2B cold outbound that gets replies, from cold emails and follow-ups to sending setup, LinkedIn, multichannel cadences, and reply handling. Use when the user mentions "cold email," "cold outreach," "outbound," "prospecting email," "SDR emails," "follow-up sequence," "nobody's replying," "email deliverability," "sending domains," "warm up inboxes," "LinkedIn outreach," "connection request message," "multichannel sequence," "cadence," "cold call," "voicemail," "handle replies," "AI SDR," "teardown outreach," or "product-led outbound." Send from secondary domains, verify lists first, turn off open tracking, and stop every channel when a prospect replies. Copy avoids AI tells like 'it's not X, it's Y' reveals. For building the list and account research, see prospecting. For lifecycle email, see emails. For call scripts and sales collateral, see sales-enablement.


# Cold Email Writing

You are an expert in cold outbound. Your goal is to write emails that sound like they came from a sharp, thoughtful human — not a sales machine following a template — and to make sure they reach the inbox, work alongside the other channels, and turn replies into meetings.

## Before Writing

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Understand the situation (ask if not provided):

1. **Who are you writing to?** — Role, company, why them specifically
2. **What do you want?** — The outcome (meeting, reply, intro, demo)
3. **What's the value?** — The specific problem you solve for people like them
4. **What's your proof?** — A result, case study, or credibility signal
5. **Any research signals?** — Funding, hiring, LinkedIn posts, company news, tech stack changes

Work with whatever the user gives you. If they have a strong signal and a clear value prop, that's enough to write. Don't block on missing inputs — use what you have and note what would make it stronger.

---

## Writing Principles

### Write like a peer, not a vendor

The email should read like it came from someone who understands their world and isn't trying to sell them something. Use contractions. Read it aloud. If it sounds like marketing copy, rewrite it.

### Every sentence must earn its place

Cold email is ruthlessly short. If a sentence doesn't move the reader toward replying, cut it. The best cold emails feel like they could have been shorter, not longer.

### Personalization must connect to the problem

If you remove the personalized opening and the email still makes sense, the personalization isn't working. The observation should naturally lead into why you're reaching out.

See [personalization.md](references/personalization.md) for the 4-level system and research signals.

### Lead with their world, not yours

The reader should see their own situation reflected back. "You/your" should dominate over "I/we." Don't open with who you are or what your company does.

### One ask, low friction

Interest-based CTAs ("Worth exploring?" / "Would this be useful?") beat meeting requests. One CTA per email. Make it easy to say yes with a one-line reply.

---

## Voice & Tone

**The target voice:** A smart colleague who noticed something relevant and is sharing it. Conversational but not sloppy. Confident but not pushy.

**Calibrate to the audience:**

- C-suite: ultra-brief, peer-level, understated
- Mid-level: more specific value, slightly more detail
- Technical: precise, no fluff, respect their intelligence

**What it should NOT sound like:**

- A template with fields swapped in
- A pitch deck compressed into paragraph form
- A LinkedIn DM from someone you've never met
- An AI-generated email (avoid the telltale patterns: "I hope this email finds you well," "I came across your profile," "leverage," "synergy," "best-in-class")

---

## Structure

There's no single right structure. Choose a framework that fits the situation, or write freeform if the email flows naturally without one.

**Common shapes that work:**

- **Observation → Problem → Proof → Ask** — You noticed X, which usually means Y challenge. We helped Z with that. Interested?
- **Question → Value → Ask** — Struggling with X? We do Y. Company Z saw [result]. Worth a look?
- **Trigger → Insight → Ask** — Congrats on X. That usually creates Y challenge. We've helped similar companies with that. Curious?
- **Story → Bridge → Ask** — [Similar company] had [problem]. They [solved it this way]. Relevant to you?

For the full catalog of frameworks with examples, see [frameworks.md](references/frameworks.md).

---

## Subject Lines

Short, boring, internal-looking. The subject line's only job is to get the email opened.

- 2-4 words, lowercase, no punctuation tricks
- Should look like it came from a colleague ("reply rates," "hiring ops," "Q2 forecast")
- No product pitches, no urgency, no emojis, no prospect's first name

See [subject-lines.md](references/subject-lines.md) for the full data.

---

## Follow-Up Sequences

Each follow-up should add something new — a different angle, fresh proof, a useful resource. "Just checking in" gives the reader no reason to respond.

- 3-5 total emails, increasing gaps between them
- Each email should stand alone (they may not have read the previous ones)
- The breakup email is your last touch — honor it

See [follow-up-sequences.md](references/follow-up-sequences.md) for cadence, angle rotation, and breakup email templates.

---

## Before You Send

Copy only matters if it reaches the inbox. Before the first send:
- Send from **secondary domains**, never your primary one, with SPF, DKIM, and DMARC set up and mailboxes warmed for 3–4 weeks.
- **Verify every list** right before upload and keep bounces under 2%.
- **Turn off open and click tracking.** Measure replies.
- Include a plain-text **opt-out line and your postal address** in every email.

Domain and mailbox math, the Google, Yahoo, and Microsoft rules, monitoring, and stop-loss thresholds are in [deliverability.md](references/deliverability.md).

---

## Beyond Email

Most outbound that works in 2026 runs on more than one channel:
- **LinkedIn**: profile, limits, the engage-then-connect sequence, message copy, and the automation decision. See [linkedin-outreach.md](references/linkedin-outreach.md).
- **Cadence**: how email, LinkedIn, calls, video, and ads fit together by tier, and the rule that a reply on any channel stops all of them. See [multichannel-cadence.md](references/multichannel-cadence.md). Call scripts are in the sales-enablement skill.
- **Plays**: value-first teardowns for services, product-led outbound for self-serve SaaS, problem-led outbound with a free sample, and founder-led outreach. See [outbound-plays.md](references/outbound-plays.md).

## When They Reply

Classify every reply (positive, information request, objection, not now, referral, out of office, unsubscribe), answer positive replies within minutes, and book with two proposed times plus a link. What an agent can handle alone and what needs a human is in [reply-handling.md](references/reply-handling.md).

---

## Quality Check

Before presenting, gut-check:

- Does it sound like a human wrote it? (Read it aloud, and check for the AI tells below)
- Would YOU reply to this if you received it?
- Does every sentence serve the reader, not the sender?
- Is the personalization connected to the problem?
- Is there one clear, low-friction ask?

---

## What to Avoid

- Opening with "I hope this email finds you well" or "My name is X and I work at Y"
- Jargon: "synergy," "leverage," "circle back," "best-in-class," "leading provider"
- Feature dumps. One proof point beats ten features
- AI tells, which prospects spot in the first line and delete:
  - Contrast reveals ("It's not about X, it's about Y") and "no X, no Y, no Z" lists
  - A claim followed by a comma and more restating clauses
  - Self-answered questions ("The result? 40% more meetings.") and colon reveals. A real question you want them to answer is fine
  - Stock phrases: "Here's the thing," "I'll be honest," "Quick question" as an opener, "Say goodbye to," "Unlock," "Take it to the next level"
  - Em dashes
  - For the full blacklist, use the **copywriting** skill's AI-tells reference
- HTML, images, or multiple links
- Fake "Re:" or "Fwd:" subject lines
- Identical templates with only {{FirstName}} swapped
- Asking for 30-minute calls in first touch
- "Just checking in" follow-ups

---

## Data & Benchmarks

The references contain performance data if you need to make informed choices:

- [benchmarks.md](references/benchmarks.md) — Reply rates, conversion funnels, expert methods, common mistakes
- [deliverability.md](references/deliverability.md) — Sending domains, mailboxes, mailbox-provider rules, warmup, monitoring, stop-loss rules
- [linkedin-outreach.md](references/linkedin-outreach.md) — LinkedIn profile, limits, sequence, copy, automation risk
- [multichannel-cadence.md](references/multichannel-cadence.md) — Cadences by tier, cross-channel rules, calls, video, direct mail, ads
- [outbound-plays.md](references/outbound-plays.md) — Value-first teardown, product-led, problem-led, and founder-led plays
- [reply-handling.md](references/reply-handling.md) — Reply types, speed, booking, early objections, agent permissions
- [personalization.md](references/personalization.md) — 4-level personalization system, research signals
- [subject-lines.md](references/subject-lines.md) — Subject line data and optimization
- [follow-up-sequences.md](references/follow-up-sequences.md) — Cadence, angles, breakup emails
- [frameworks.md](references/frameworks.md) — All copywriting frameworks with examples

Use this data to inform your writing — not as a checklist to satisfy.

---

## Tool Integrations

For setup, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md), including its sales outbound quick start. Tools most used with this skill:

| Job | Tools | Guides |
|-----|-------|--------|
| Email sending and sequences | Instantly, lemlist, Outreach | [instantly.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/instantly.md), [lemlist.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/lemlist.md), [outreach.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/outreach.md) |
| LinkedIn steps | HeyReach, lemlist (both carry LinkedIn terms-of-service risk) | [heyreach.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/heyreach.md) |
| Verification before send | Truelist, Hunter | [truelist.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/truelist.md), [hunter.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/hunter.md) |
| CRM and reply logging | HubSpot, Attio, Close | [attio.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/attio.md), [close.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/close.md) |
| Booking | Calendly, SavvyCal | [calendly.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/calendly.md), [savvycal.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/savvycal.md) |

Instantly's webhooks (reply received, lead interested, bounced, unsubscribed) are the simplest way to drive the cross-channel stop and reply triage from an agent.

---

## Related Skills

- **prospecting**: For building and qualifying the prospect list, signals, enrichment, verification, and account research — the natural upstream step before cold-email
- **copywriting**: For landing pages and web copy
- **emails**: For lifecycle/nurture email sequences (not cold outreach)
- **social**: For LinkedIn and social posts
- **product-marketing**: For establishing foundational positioning
- **revops**: For lead scoring, routing, pipeline management, and the outbound stage model
- **sales-enablement**: For cold call scripts, voicemails, and deal-stage objections
- **marketing-loops**: For running outbound on a schedule (signal sweeps, reply triage, domain health, sequence reviews)



---

## `references/benchmarks.md`

# Benchmarks, Data & Expert Methods

## Core Performance Metrics

Almost every public cold email benchmark comes from a vendor that sells sending, data, or agency services, and each measures differently (some count auto-replies as replies, some don't). Use these as ranges, and judge yourself against your own baseline.

| Metric | Average | Good | Excellent | Source |
|--------|---------|------|-----------|--------|
| Reply rate | ~3.4% | 5.5%+ (top quartile) | 10%+ (top decile) | Instantly, 2025 sends (published 2026) |
| Reply rate (signal-based, small segments) | — | 2–3× your static-list rate | — | Inferred from several 2025–26 vendor datasets; claims of 15–25% are unverified |
| Share of replies from email 1 | ~58% | — | — | Instantly 2026 |
| Meetings booked | 0.5–1% of contacts | 1–2% | 2.5%+ | Reachoutly, Cleverly |
| Bounce rate | — | under 2% | under 1% | Mailbox-provider guidance; see deliverability.md |
| Spam complaints | — | under 0.1% | — | Google sender guidelines |

**Don't use open rate.** Apple Mail Privacy Protection opens tracked emails automatically, many filters treat the tracking pixel as a spam signal, and one large sender dataset found reply rates roughly doubled with open tracking off. Measure replies, positive replies, and meetings.

## Realistic Funnel Model

1,000 contacts → ~34 replies (3.4%) → ~10–15 positive (30–45% of replies) → ~5–8 meetings → 1–2 customers. Roughly **100–200 contacts per meeting** on a static list; signal-based segments often need 30–60 (an estimate from the ranges above, not a measured benchmark).

## Performance Levers (ranked by impact)

1. **Hook type** — Timeline hooks outperform problem hooks by 3.4x in meetings
2. **Personalization depth** — Up to 250% more replies
3. **Brevity** — 25–75 words optimal, 83% more replies under 75 words
4. **Targeting precision** — ≤50 contacts per campaign = 2.76x higher reply rates
5. **Follow-up strategy** — First follow-up adds 49% more replies
6. **Reading level** — 3rd–5th grade = 67% more replies
7. **Send timing** — Thursday peaks at 6.87% reply rate

## Declining Effectiveness Trend

Reply rates fell from 7–8% (2020–2022) to roughly 3.5–5.8% (2024–2025 datasets). Drivers: inbox saturation (10+ cold emails/week, 20% say none relevant), stricter anti-spam (Google's threshold: 0.1% complaints), AI email flood (more volume, less quality signal). Writing craft matters more, not less — gap between average and excellent is widening.

## Response Rates by Seniority

- **Entry-level:** Highest engagement at 8% reply, 50% open
- **C-level:** 23% more likely to respond than non-C-suite when they engage (6.4% vs 5.2%)
- **CTOs/VP Tech:** 7.68% reply
- **CEOs/Founders:** 7.63% reply
- **Heads of Sales:** 6.60% (most targeted role, highest saturation)

## Industry Variation

**Highest responding:** Nonprofits (16.5%+), legal (10%), EdTech (7.8%), chemical (7.3%), manufacturing (6.1%).
**Lowest responding:** SaaS (3.5%), financial services (3.4%), IT services (3.5%).

## Top 15 Mistakes (ranked by impact)

1. **Too long** — 70% of emails above 10th-grade level. Under 75 words = 83% more replies
2. **Too self-focused** — "We are a leading..." signals sales pitch. Count I/We sentences
3. **No clear value prop** — 71% of decision-makers ignore irrelevant emails
4. **Generic templates** — {{FirstName}} isn't personalization. Recipients detect instantly
5. **Feature dumping** — "Great reps lead with problems" (Lavender). One proof point beats ten features
6. **False personalization** — "Loved your post!" without specifics is transparent
7. **Asking too much too soon** — 30-min call in first email = "proposing on first date"
8. **Pushy language** — "Act Now" stacking increases spam flagging by 67%
9. **No CTA** — Without a clear next step, momentum dies
10. **"Just checking in" follow-ups** — "I never heard back" = 12% drop in bookings
11. **Wrong tone for audience** — Founder ≠ RevOps lead ≠ sales leader
12. **Jargon/buzzwords** — "Leverage synergistic platform" → "We help you book more meetings"
13. **Unsubstantiated claims** — "300% more leads" without proof triggers skepticism
14. **Too many contacts per company** — 1–2 people = 7.8% reply; 10+ = 3.8%
15. **Fake urgency** — Fake "Re:" / "Fwd:" / countdown timers destroy trust

## Cultural Calibration

| Factor       | US              | UK                       | Germany/DACH         | Scandinavia             |
| ------------ | --------------- | ------------------------ | -------------------- | ----------------------- |
| Tone         | Direct, casual  | Polite, professional     | Precise, data-driven | Fact-based, egalitarian |
| Length       | Shorter, blunt  | Longer, insight-led      | Detail-oriented      | Concise but substantive |
| Social proof | Outcome numbers | Research-led credibility | Technical precision  | Shared values           |

North America: 4.1% response. Europe: 3.1%. Asia-Pacific: 2.8%. Shorter, more direct sequences work better in US. UK needs more insight/personality. GDPR affects European tone.

## Expert Quick Reference

| Expert         | Core Method                                                     | Best For                                        |
| -------------- | --------------------------------------------------------------- | ----------------------------------------------- |
| Alex Berman    | 3C's: Compliment → Case Study → CTA                             | High-ticket B2B services, agencies              |
| Josh Braun     | "Poke the Bear" — neutral questions exposing invisible problems | Empathy-driven consultative selling             |
| Kyle Coleman   | Systematic research + AI personalization at scale               | Bridging mass outreach and deep personalization |
| Becc Holland   | Psychographic personalization, Premise Buckets                  | Combining personalization with relevance        |
| Will Allred    | Data-driven coaching, Mouse Trap, Vanilla Ice Cream             | Any context; universal frameworks               |
| Justin Michael | 1–3 sentence hyper-brevity, quote their own words               | High-velocity SDR teams at scale                |
| Sam Nelson     | Agoge Sequence — Triple on Day 1 (email + LinkedIn + call)      | Multi-channel, tiered personalization           |



---

## `references/deliverability.md`

# Cold Email Deliverability

The best cold email does nothing if it lands in spam. Deliverability is set up before the first send and watched every week after. This reference covers the sending setup, the mailbox providers' rules, volume limits, warmup, monitoring, and when to stop.

Numbers here come mostly from sending-infrastructure vendors and mailbox providers' own guidelines. Mailbox providers change enforcement without notice, so treat the volume figures as starting points and let your own placement tests decide.

## The rules from Google, Yahoo, and Microsoft

| Provider | What it requires | Enforcement |
|----------|------------------|-------------|
| **Gmail** | SPF and DKIM for everyone; for bulk senders (about 5,000+ messages a day to personal Gmail), also DMARC, alignment, one-click unsubscribe on marketing mail, and spam complaints under 0.3% | Since November 2025, non-compliant mail gets permanent rejections rather than temporary deferrals. Once you're classified as a bulk sender, the status is permanent |
| **Yahoo** | Matches Google's requirements | Since 2024 |
| **Microsoft** (Outlook.com, Hotmail, Live) | SPF, DKIM, and DMARC for senders above 5,000 a day | Since May 5, 2025, non-compliant mail is rejected (`550 5.7.515`) |

Google's bulk-sender rules apply to mail sent to personal Gmail accounts, not to Google Workspace business addresses. A cold program under 5,000 a day isn't technically a "bulk sender." Follow the rules anyway: they describe what every filter rewards, and the complaint threshold applies to everyone.

**Complaint rate:** keep spam complaints under 0.1% and never reach 0.3%. Practitioners report Workspace sending degrading well before 0.3%.

## Sending setup

**Never send cold email from your primary domain.** One bad campaign can damage the domain your customers, invoices, and password resets depend on.

1. **Buy secondary domains** that are obviously yours (`getacme.com`, `acmehq.com`, `tryacme.com`). Redirect each to your main site.
2. **Authenticate every domain:** SPF, DKIM, and DMARC (start at `p=none` with reporting), aligned to the From domain. Add a custom tracking domain only if you track clicks (see Tracking, below).
3. **Create 2–3 mailboxes per domain**, each a real-looking person with a name, photo, and signature. Never use aliases of a single mailbox; both Google and Microsoft treat that as abuse of their terms.
4. **Only buy mailboxes from properly licensed tenants.** In late 2025 Google reportedly suspended large numbers of resold Workspace mailboxes built on education, nonprofit, or legacy accounts. Cheap "reseller" inboxes are disposable at best.
5. **Match the provider to your prospects where you can.** Google-hosted mailboxes for audiences on Google Workspace (most startups and SaaS), Microsoft-hosted for enterprise audiences on Microsoft 365. Vendors report better inbox placement when the two match. Check a prospect's mail host from their MX record.

### Volume math

| Setting | Starting point |
|---------|----------------|
| Sends per mailbox per day | 20–30 (Google-hosted); test lower for Microsoft-hosted, where 2026 operator reports range from single digits to dozens |
| Mailboxes per domain | 2–3 |
| Daily volume | Mailboxes × sends per mailbox |

Example: 500 sends a day ≈ 20 mailboxes at 25 each ≈ 7–10 domains. Follow-ups count toward the daily volume.

Plan for spares. Keep 10–20% extra domains warmed and idle, so a burned domain can be swapped out without stopping the program.

## Warmup

New mailboxes need 3–4 weeks of ramp before full cold volume:
- **Weeks 1–2:** warmup only, plus a handful of real emails to people likely to reply.
- **Weeks 3–4:** start cold sends at 5–10 a day per mailbox and increase gradually.
- **After that:** keep light warmup running in the background.

Warmup networks still help new mailboxes, but a mailbox whose only engagement is warmup traffic is a recognizable pattern. Real replies are the strongest reputation signal there is, which is one more reason to write emails people answer.

## The email itself

- **Plain text.** No images, no HTML templates, no attachments.
- **No link in the first email,** and at most one link in later ones. Never use link shorteners.
- **Turn off open tracking.** Apple Mail Privacy Protection makes opens meaningless, and the tracking pixel itself is a spam signal. One large sender dataset found reply rates roughly doubled when open tracking was off. Measure replies instead.
- **Turn off click tracking** unless you need it, and then only with a custom tracking domain.
- **Under about 80 words** for the first email.
- **Vary the copy.** Identical bodies across thousands of sends look like bulk mail. Segment-specific copy and real personalization fix this naturally. Keep spintax as a last resort.
- **Opt-out line.** A plain-text line ("If this isn't relevant, reply 'no' and I won't follow up") plus your postal address in the signature. CAN-SPAM requires both; see the prospecting skill's compliance reference.

## Verify before you send

Bounces are the fastest way to damage a domain. Keep them under 2% per campaign; under 1% is best in class. A single day with several percent bounces can trigger a review at Google.

- Verify every list before upload, and re-verify anything older than about a week.
- Handle catch-all domains with a policy. See the prospecting skill's sourcing and enrichment reference.
- Pause any campaign automatically when its bounce rate passes 2%.

## Monitoring

| Check | How | When |
|-------|-----|------|
| Inbox placement | Seed tests (MailReach, GlockApps, or your sending tool's built-in test) | Before every new campaign and weekly |
| Domain reputation | Google Postmaster Tools; Microsoft SNDS | Weekly |
| Bounce rate | Sending tool, per campaign and per mailbox | Daily |
| Spam complaints | Postmaster Tools; replies containing "spam" or "stop" | Weekly |
| Blocklists | A blocklist checker for each sending domain | Weekly |
| Authentication | DMARC aggregate reports | Monthly |

## Stop-loss rules

Decide these before launch and enforce them automatically where your tool allows:

| Trigger | Action |
|---------|--------|
| Bounce rate above 2% on a campaign | Pause the campaign and re-verify the list |
| Inbox placement below ~70% on a mailbox or domain | Pull it from rotation, return it to warmup, investigate |
| Spam complaints approaching 0.1% | Pause, cut volume, review targeting and copy |
| Domain appears on a major blocklist | Stop sending from it; delist or retire it |
| Reply rate under ~1% after 300+ sends | Stop the campaign; the targeting or offer is wrong, and more volume makes it worse |

## Common mistakes

- Sending from the primary domain
- Buying the cheapest reseller mailboxes and losing all of them at once
- Skipping verification "because the data provider verified it"
- Leaving open tracking on and optimizing for a number that isn't real
- Scaling volume to fix a low reply rate
- Running warmup and cold sends at full volume from day one

## Tools

| Job | Options |
|-----|---------|
| Sending and mailbox rotation | Instantly, Smartlead, lemlist, EmailBison, Salesforge |
| Domain and mailbox provisioning | Inframail, Maildoso, Mailforge, Truelist Outbound (managed domains, mailboxes, and a dedicated IP with an enforced ramp), Zapmail, or Google Workspace and Microsoft 365 directly |
| Placement testing | GlockApps, MailReach, or your sending tool's built-in test (Instantly has one) |
| Reputation | Google Postmaster Tools, Microsoft SNDS |
| DMARC monitoring | EasyDMARC, dmarcian, Valimail |
| List verification | Bouncer, MillionVerifier, NeverBounce, Truelist, ZeroBounce, and others |

Setup guides: [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md).



---

## `references/follow-up-sequences.md`

# Follow-Up Sequences

The first email draws most replies (about 58% in Instantly's 2026 benchmark), but the remaining ~42% arrive on follow-ups. A sequence that stops after one send gives up nearly half its replies.

## How Many: 3–5 Total Emails

- Highest single-email reply rate: **8.4%** (Belkins).
- 4–7 email campaigns achieve **27% reply rates** vs 9% for 1–3 emails (Woodpecker, 20M emails).
- By 4th follow-up, response rates drop **55%** and spam complaints **triple**.
- Resolution: longer sequences catch different timing windows. Cap at 4 follow-ups (5 total emails). Each must add genuinely new value.

## Optimal Cadence

Increase the gap between each touch:

| Touch         | Day   | Notes                                          |
| ------------- | ----- | ---------------------------------------------- |
| Initial email | 0     | Maximum personalization investment             |
| Follow-up 1   | 3     | Waiting 3 days increases response by up to 31% |
| Follow-up 2   | 7–8   | Different angle                                |
| Follow-up 3   | 14    | New value piece                                |
| Follow-up 4   | 21–28 | Breakup email                                  |

**Best days:** Tuesday–Thursday (Thursday peaks at 6.87% reply rate).
**Best times:** 9–11 AM or 1–3 PM in prospect's local time.
**Avoid:** Monday mornings (inbox overload), Friday afternoons (checked out).

## Angle Rotation

Each follow-up must stand alone while building toward the goal. Never just "bump this up."

| Email       | Angle                                                      | Purpose                    |
| ----------- | ---------------------------------------------------------- | -------------------------- |
| Initial     | Personalized hook + core value prop + soft CTA             | Introduce problem/solution |
| Follow-up 1 | Different angle, new value piece (stat, insight, resource) | Show additional benefit    |
| Follow-up 2 | Social proof / case study from similar company             | Build credibility          |
| Follow-up 3 | New insight, industry trend, or relevant resource          | Demonstrate expertise      |
| Follow-up 4 | Breakup — acknowledge silence, leave door open             | Trigger loss aversion      |

Add only **one new value proposition per email** (SalesBread). This naturally forces different angles.

## The Breakup Email

Leverages loss aversion — removing pressure while creating scarcity through withdrawal. Close.com reports **10–15% response rates** from breakup emails with cold prospects.

**Structure:**

1. Acknowledge you've reached out multiple times
2. Validate their potential lack of interest
3. State this is your final email for now
4. Leave the door open

**Example:**

> I haven't heard back, so I'll assume now isn't the right time. Before I close the loop: [1-sentence insight or resource]. If that changes things, feel free to reply. Otherwise, no hard feelings. Good luck with [their goal].

**1-2-3 Format** (reduces friction to near zero):

> Since I haven't heard back, I'll keep it simple. Reply with a number:
>
> 1: Interested, let's talk
> 2: Not now, check back in 3 months
> 3: Not interested, please stop

**Critical rule:** If you send a breakup email, honor it. Do not contact the prospect again.

## Phrases That Kill Response Rates

- "I never heard back" → **12% drop** in meeting booking rate (Gong)
- "Just checking in" → Zero value, signals laziness
- "Bumping this to the top of your inbox" → Presumptuous
- "Did you see my last email?" → Guilt-tripping
- "Following up on my previous message" → Generic, adds nothing

## CTA Adjustment by Seniority

**Executives/founders:** Ultra-low-effort, curiosity-driven. "Curious?" or "Worth 2 min?"

**Mid-level managers:** More specific value. "Want me to walk through how [Company] saved 15 hours/week?"

Higher in the org chart = less friction you can ask for.



---

## `references/frameworks.md`

# Cold Email Copywriting Frameworks

Frameworks beat templates — they teach thinking patterns, not copy-paste shortcuts.

## PAS — Problem, Agitate, Solution (default)

**Structure:** Identify pain → Amplify consequences → Present solution + soft CTA.
**Best for:** Problem-aware but not solution-aware prospects. The workhorse framework.

> Most VP Sales at companies your size spend 5+ hours/week on manual CRM reporting. That's 250+ hours/year not spent coaching reps, and it often means inaccurate forecasts reaching leadership. We built a tool that auto-generates CRM reports in real time. Teams like Datadog reduced reporting time by 80%. Would it make sense to see how?

## BAB — Before, After, Bridge

**Structure:** Current painful situation → Ideal future → Your product as the bridge.
**Best for:** Transformation-driven offers with clear before/after. Emotional decision-makers.

> Right now, your team is likely spending hours manually sourcing leads. Feast or famine each quarter. Imagine qualified leads arriving daily on autopilot, reps spending 100% of their time selling. That's what our platform does. Companies like HubSpot saw a 40% pipeline increase within 90 days. Can I show you how?

## QVC — Question, Value, CTA

**Structure:** Targeted pain question → Brief value → Direct next step.
**Best for:** C-suite prospects who prefer brevity. Qualify interest immediately.

> Are your SDRs spending more time researching than selling? We help sales teams automate prospect research so reps focus on conversations. Clients see 3x more meetings per rep per week. Worth a 10-minute demo?

## AIDA — Attention, Interest, Desire, Action

**Structure:** Hook/stat → Address specific challenge → Social proof/outcome → Clear CTA.
**Best for:** Data-driven prospects, high-ticket pitches with strong stats.

> Companies in pharma lose 30% of leads due to manual outreach. Given {{Company}}'s growth this quarter, pipeline velocity is likely top of mind. Customers like Pfizer use our platform to automate lead qualification and cut time-to-contact by 60%. Worth a 15-minute call?

## PPP — Praise, Picture, Push

**Structure:** Genuine compliment → How things could be better → Gentle push to action.
**Best for:** Senior prospects who respond to relationship-building. Requires genuine trigger.

> Your keynote on scaling SDR teams was spot-on, especially on ramp time as the hidden cost. What if you could cut that in half? Our in-inbox coach helps new reps write effective emails from day one with real-time scoring. Open to a quick chat about how this could support your growth?

## Star-Story-Solution

**Structure:** Introduce character (customer) → Tell challenge narrative → Reveal results.
**Best for:** Strong customer success stories. Humanizes the pitch.

> Last year, Sarah, VP Sales at a Series B startup, had 5 SDRs competing against a rival with 20. Her team was getting crushed on volume. They adopted our AI prospecting tool and sent hyper-personalized emails at 3x pace without losing quality. Within 90 days, they booked more meetings than their competitor's entire team. Happy to share how this could work for {{Company}}.

## SCQ — Situation, Complication, Question

**Structure:** Current reality → Complicating challenge → Question that speaks to need → Optional answer.
**Best for:** Consultative selling. Mirrors how professionals present to leadership.

> Your team doubled this year. That usually means onboarding is eating into selling time. How are you handling ramp for new hires?

## ACCA — Awareness, Comprehension, Conviction, Action

**Structure:** Contrarian hook → Explain benefit simply → Provide proof → Strong CTA.
**Best for:** Analytical buyers who need evidence (engineers, CFOs, ops leaders).

> Most sales teams measure rep activity. The top 5% measure rep efficiency instead. When Acme switched, they booked 40% more meetings with fewer emails. Worth seeing how?

## 3C's (Alex Berman)

**Structure:** Compliment → Case Study → CTA.
**Best for:** Agency/services cold outreach. Case study does the heavy lifting.

> Big fan of [Company]. We just built an app for [Competitor] that does XYZ. I have a few more ideas. Interested?

## Mouse Trap (Lavender/Will Allred)

**Structure:** Observation + Binary value-prop question. 1–2 sentences total.
**Best for:** Maximum brevity. Impulsive reply based on curiosity.

> Looks like you're hiring reps. Would it be helpful to get a more granular look at how they're ramping on email?

## Justin Michael Method

**Structure:** Trigger/Pain → Solution hint → Binary CTA. 1–3 sentences, no intro.
**Best for:** High-velocity SDR teams. Mobile-optimized. Deliberately polarizing.

Spend max 1 minute on personalization. Use industry/persona-level signals. For top-tier prospects, quote their own words from interviews — they almost always respond.

## Vanilla Ice Cream (Lavender)

**Structure:** Observation → Problem/Insight → Credibility → Solution → Call-to-Conversation.
**Best for:** Universal "base" framework that works everywhere. Five parts.

## PASTOR (Ray Edwards)

**Structure:** Problem → Amplify → Story → Testimony → Offer → Response.
**Best for:** Longer-form or multi-email sequences. Consulting, education, complex B2B services. Each element can be developed across separate touches.



---

## `references/linkedin-outreach.md`

# LinkedIn Outreach

LinkedIn is the second channel in most B2B outbound and the first for some audiences: people who ignore cold email often accept a relevant connection request. It also has the tightest limits and the highest account risk of any channel. This reference covers the profile, the limits, the sequence, the copy, and the automation decision.

Figures below come mostly from LinkedIn automation vendors' and agencies' own datasets (2025–26). Use them as ranges.

## Fix the profile first

Every prospect who gets a request or a message looks at the sender's profile. Before outreach:
- **Headline** says who you help and how.
- **About** opens with the problem you solve, then proof.
- **Featured** holds one case study, teardown, or resource a prospect would actually click.
- **Recent activity** shows posts or thoughtful comments from the last few weeks. Accounts that post regularly see noticeably higher acceptance rates.
- A real photo and a banner that reinforces what you do.

## Limits

| Action | Safe range |
|--------|-----------|
| Connection requests | About 100 a week per account; 15–25 a day. New or low-activity accounts start at 20–30 a week |
| Messages to connections | Roughly 50–100 a day, spread out |
| Profile views | A few hundred a day at most |
| InMail | Limited by your Sales Navigator or Premium credits |

Volume isn't the only thing LinkedIn looks at. In 2026 it also flags unusual behavior: activity from data-center IP addresses, identical timing between actions, and low acceptance rates. A 15% acceptance rate tells LinkedIn your requests are unwanted. Keep acceptance above about 25–30% by sending fewer, better-targeted requests.

Withdraw requests that are still pending after 2–3 weeks; a large pending pile counts against you.

## The sequence

Warm up the account's visibility before asking for anything:

1. **Day 1:** view their profile, follow them, and react to or comment on a recent post (a real comment, not "Great post!").
2. **Day 2–3:** connection request. A note is optional (see below).
3. **After acceptance:** a short first message tied to why you connected. No pitch.
4. **3–5 days later:** a message with value: an insight, a resource, a relevant example.
5. **5–7 days later:** a light ask, or a voice note.

Stop at three messages without a reply. Vendor data shows replies falling sharply beyond that.

Run LinkedIn alongside email, not instead of it, and stop both the moment either gets a reply. See [multichannel-cadence.md](multichannel-cadence.md).

## Copy

**Connection request**
- Notes cut acceptance slightly but raise replies once accepted (one 2025 agency study: about 25% vs 28% acceptance, 8% vs 5% reply). Use a note when you have a specific, credible reason; skip it when you don't.
- Under ~200 characters. The reason you're connecting, nothing else.
- AI-written notes underperform human ones by a measurable margin in vendor data. Write these yourself, or edit hard.

> Saw your post on moving pricing tests off the homepage. We've run a few of those for SaaS teams; would be good to connect.

**First message after acceptance**
- 150–200 characters performs best in vendor datasets.
- Reference the reason you connected. Ask something easy to answer.

> Thanks for connecting. Curious how you're deciding what to test first on the new pricing page. Is that sitting with you or with product?

**Voice notes** (mobile app only) stand out in a text inbox. Keep them under 45 seconds, say their name and the specific reason, and never read a script. Public data on voice notes is thin, so test them.

**InMail** suits senior people you can't reach any other way. It gets the same rules as cold email: short, specific, one ask.

Everything in the main cold-email skill about voice and AI tells applies here, even more strongly: LinkedIn messages sit next to the sender's face and name.

## The automation decision

**Every third-party LinkedIn automation tool violates LinkedIn's User Agreement.** That includes cloud tools, browser extensions, and APIs that operate your account through its session. LinkedIn has escalated from restricting individual users to acting against vendors: it removed company pages for Apollo and Seamless in 2025 and HeyReach in March 2026, and sued scraping vendors.

Make the decision deliberately:

| Option | Risk | When it fits |
|--------|------|--------------|
| **Manual** (Sales Navigator, phone, a daily routine) | None beyond normal limits | Tier 1 accounts; founders; anyone whose personal profile is a business asset |
| **Assisted** (tools that queue tasks for a human to do, CRM reminders) | Low | Most teams |
| **Automated** (HeyReach, Expandi, La Growth Machine, Dripify, Waalaxy, Unipile-based tools) | Account restriction, and the vendor itself can disappear | High-volume Tier 3 programs, on profiles the business can afford to lose |

If you automate:
- Use only real profiles owned by the people they represent. Never rent or buy accounts.
- Stay well under the limits above, with randomized timing.
- Prefer tools with dedicated residential IPs per account.
- Keep a plan for losing the tool overnight: export your data regularly.

For agents: HeyReach and Unipile expose APIs (and HeyReach an MCP), which makes them the most scriptable options. The terms-of-service risk is the same as any other automation.

## Measure

| Metric | Typical range (vendor data, 2025–26) |
|--------|--------------------------------------|
| Acceptance rate | 25–30% average; 30%+ for active, followed profiles |
| Reply rate to messages | 7–10% |

Track positive replies and meetings, the same as email. A high acceptance rate with no replies means the targeting is fine and the messages aren't.



---

## `references/multichannel-cadence.md`

# Multichannel Cadence

Most buyers need to see a name a few times, in more than one place, before they respond. A cadence coordinates email, LinkedIn, phone, and the occasional video or package so each touch builds on the last and nobody gets hit on four channels in one afternoon.

## Which channels for which tier

| Tier | Channels |
|------|----------|
| Tier 1 (1:1) | Email, LinkedIn, phone, personalized video; direct mail after engagement |
| Tier 2 (1:few) | Email and LinkedIn; phone for the best-fit accounts |
| Tier 3 (1:many) | Email; LinkedIn only if it can be done without automation risk |

Tiers are defined in the prospecting skill's signal plays reference.

## A 21-day Tier 1 cadence

| Day | Touch |
|-----|-------|
| 1 | View their LinkedIn profile and engage with a recent post. Send email 1 (short, no link) |
| 3 | LinkedIn connection request |
| 4 | Email 2, as a reply in the same thread |
| 6 | Call 1. If no answer, leave a short voicemail and send an email recapping it |
| 8 | LinkedIn message if connected; otherwise a short personalized video by email |
| 11 | Email 3: new angle or a case study |
| 13 | Call 2 |
| 15 | LinkedIn voice note or a comment on a new post |
| 18 | Email 4: breakup or referral ask |
| 21 | Call 3. Then move the contact to nurture and ad retargeting |

Shorten it for Tier 2 (email and LinkedIn over about 14 days). Tier 3 is the email sequence alone; see [follow-up-sequences.md](follow-up-sequences.md).

## Rules that hold any cadence together

1. **A reply on any channel stops every channel.** Someone who answered on LinkedIn mustn't get email 3 the next morning. This needs one shared record of who has replied, checked before each touch.
2. **An opt-out on one channel is an opt-out on all of them.** Key the suppression list on email, LinkedIn URL, and phone together. See the prospecting skill's sourcing and enrichment reference.
3. **One sender per account at a time.** Two reps, or a rep and an agent, sequencing the same company looks disorganized and doubles the annoyance.
4. **Each touch references the last** when it helps ("Following up on the voicemail I left Tuesday"), but must also make sense on its own.
5. **Keep it to 4–7 emails and at most 3 LinkedIn messages.** More touches don't rescue the wrong offer.
6. **Space touches across days.** Never two channels on the same day except a voicemail and its recap email.

Most sequencing tools only coordinate their own channels. When email, LinkedIn, and calls run in different tools, connect them with a shared state (the CRM or a simple table keyed on the contact) and webhooks that pause every sequence when any reply arrives.

## Calls

Calls are the slowest channel and the fastest to a conversation. Vendor and agency datasets from 2025 put the dial-to-conversation rate around 10% and roughly one meeting per several hundred dials. Mobile numbers connect far better than office lines.

- **Best times:** mid-week, mid-to-late afternoon in the prospect's time zone. Test your own.
- **Attempts:** 3 calls per contact across the cadence, on different days and times.
- **Openers:** say who you are and why you're calling, then ask permission to continue. Avoid "Did I catch you at a bad time?", which call-analysis data ranks among the worst openers.
- **Voicemail:** 20–30 seconds, your name, one specific reason, and "I'll send you a note too." Then send it.
- **Rules:** scrub against Do Not Call lists, and never use AI voice on US mobile numbers without consent. See the prospecting skill's compliance reference.

Scripts for openers, voicemails, and common pushback are in the sales-enablement skill's cold call scripts reference.

## Video

A short video recorded for one person stands out in a text inbox, and it's the natural format for value-first plays (see [outbound-plays.md](outbound-plays.md)).
- **60–120 seconds** for a pure outreach video; **2–4 minutes** for a teardown or audit.
- Show their thing (their site, their product, their dashboard) on screen in the first few seconds.
- Send a thumbnail or GIF that shows their page, linked to the video. Don't attach the file.
- For Tier 1 only, or after a reply. Video doesn't scale like text, and that's the point.

Tools: Loom, Tella, Sendspark, Vidyard.

## Direct mail and gifts

Useful for Tier 1 accounts that have engaged but stalled. Something relevant to the conversation (a book you referenced, a printed teardown) beats a generic gift. Sendoso and Reachdesk handle sending and address confirmation. Check company gift policies, which often cap or ban gifts in regulated industries and government.

## Ads to target accounts

Upload your target account and contact lists to LinkedIn Matched Audiences (or other ad platforms) and run light awareness ads during the cadence. When the email arrives, the name is already familiar. See the ads skill's ABM playbook.

## SMS and WhatsApp

Not for cold outreach. US SMS to mobile numbers needs consent and 10DLC registration; WhatsApp business messaging needs an opt-in. Use them only after a prospect has engaged and agreed, for scheduling and reminders.

## Measure by channel

Track, per channel and per step: touches sent, replies, positive replies, meetings. Attribute the meeting to the touch that produced the reply, and keep the full sequence on the record so you can see which combinations work. A channel that never produces a positive reply after a few hundred touches is costing more than it returns.



---

## `references/outbound-plays.md`

# Outbound Plays

A play is a repeatable outbound motion: a trigger, an offer, a sequence, and a definition of success. Plays keep outbound from becoming a pile of one-off emails. This reference covers four that work in 2026, with the conditions each needs.

## 1. Value-first teardown (services and agencies)

Give a specific piece of the work before asking for anything. It works best when what you sell is expertise someone can see: conversion optimization, design, SEO, ads, copy, analytics.

**Trigger:** something visible changed or matters right now: a new pricing or landing page, a redesign, launched ad campaigns, a new head of growth, fresh funding with growth targets.

**The sequence**
1. **Email 1 asks permission, with no link.** Name one specific thing you noticed on their page, and offer the rest.
   > Looked at your new pricing page. The annual toggle defaults to monthly, which usually costs a few points of annual uptake. I noted two other things I'd test there. Want me to send them over?
2. **When they say yes,** send a 2–4 minute video (or a one-page annotated screenshot) covering 3 specific, testable ideas on *their* page. Show their page on screen in the first seconds.
3. **Follow-up** asks a small question about the ideas, not for a meeting: "Was the second one already on your list?"
4. **Then offer the call:** "Happy to walk through how we'd prioritize the rest."

**Why the permission step:** no link or attachment in the first email protects deliverability, a "yes" filters for real interest, and the teardown goes only to people who asked for it. That keeps a time-intensive asset efficient.

**Rules**
- The ideas must be real and specific to their page. A generic checklist dressed as a teardown burns trust and the brand.
- Give enough to be useful, and leave the "how we'd do all of it" for the call.
- Volume is low by design: around 50 well-chosen accounts a week, mostly Tier 1 and 2.
- An agent can draft the teardown (screenshot, analysis against your CRO or design framework), but a human expert reviews every one before it goes out. It represents your expertise.

**Measure:** permission rate (yes to email 1), teardown-to-call rate, call-to-proposal rate.

## 2. Product-led outbound (self-serve and freemium SaaS)

Reach out to people already using the product, when their usage shows they're ready for more.

**Triggers**, in rough order of strength:
- Hitting a plan, credit, or usage limit
- A large job or upload (a much bigger list, project, or import than usual)
- Inviting teammates
- Signing up from a company domain that matches the ICP
- Returning repeatedly to pricing or upgrade pages

**The sequence**
1. **Within minutes of the trigger,** a short plain-text email from a founder or named account owner, sent from their own address. Reference what they're doing:
   > Saw you're verifying larger lists this week. If you're running these before outbound campaigns, a couple of settings help with catch-all domains. Happy to share them, or set you up with a volume plan if you're doing this regularly.
2. **LinkedIn connect** the same or next day, for company-domain users.
3. **One follow-up** with a specific resource for their use case.
4. **Stop** if they upgrade, go quiet for two weeks, or say no.

**Rules**
- Speed matters more here than anywhere: the trigger loses most of its value within a day.
- Never make the tracking feel like surveillance. Talk about the job they're doing and leave the logged events out of it.
- Offer help first and an upgrade second. Product-qualified users convert far better than cold contacts (vendors report many times higher), so you don't need a hard sell.
- Route accounts that exceed self-serve limits to a person. See the revops skill's routing rules.

**Measure:** trigger-to-reply rate, trigger-to-upgrade rate within 14 days, expansion revenue per triggered account.

## 3. Problem-led cold outbound (any product)

The default play for accounts with no product usage: lead with a problem the segment is known to have, prove you understand it, and offer something small.

**Trigger:** a signal from the prospecting skill's signal plays reference, or a tightly defined segment.

**Offer something smaller than a meeting:** a sample of the work (verify a sample of their list, audit one page, benchmark one metric), a relevant resource, or a quick answer to a question they're probably asking.

**Example for a technical product** (an email verification tool selling to agencies that send cold email for clients):
> Agencies running outbound for several clients usually find out about a bad list when the domain is already hurting. Want me to run a sample of one client's list through and send back what would have bounced?

**Rules**
- The problem must be specific to the segment, with proof from a similar customer.
- The free sample has to be genuinely small to deliver, or the play won't scale.
- If you sell deliverability, compliance, or quality, your own outbound has to be flawless. A bounce, a typo, or a missing opt-out from a company selling those things undercuts the pitch.

## 4. Founder-led outbound

Early-stage, or for a small set of strategic accounts: the founder writes personally, from their own account, about why they built the thing.

- Short, personal, specific to the recipient. No templates.
- Ask for advice or feedback as often as for a meeting. People answer founders.
- 10–20 a week, done consistently, beats occasional bursts.
- Pairs naturally with the founder posting on LinkedIn, so the name is familiar when the email lands.

## Choosing plays

| If you... | Start with |
|-----------|-----------|
| Sell services where expertise is visible | Value-first teardown |
| Have self-serve users | Product-led outbound for usage triggers, plus problem-led for everyone else |
| Sell a technical product to a defined segment | Problem-led with a free sample |
| Are pre-product-market fit or chasing a few big logos | Founder-led |

Run one play at a time until it works. Each needs its own copy, its own success metric, and a few hundred touches before you can judge it.



---

## `references/personalization.md`

# Personalization at Scale

Personalization drives **50–250% more replies** (Lavender). The key insight: **if your personalization has nothing to do with the problem you solve, it's just an attention hack** (Clay).

## Four Levels of Personalization

### Level 1 — Basic (merge tags)

First name, company name, job title. Table stakes, no longer differentiating. ~5% lift.

### Level 2 — Industry/segment

Industry-specific pain points, trends, regulatory challenges. Scalable via micro-segmentation.

> Most {{industry}} teams struggle with {{lead gen problem}}, which often leads to wasted effort.

### Level 3 — Role-level

Challenges specific to their role and seniority.

> As Head of Sales, keeping pipeline steady is probably your biggest headache. Your RevOps team is small, so you're likely wearing multiple hats during scaling.

### Level 4 — Individual (gold standard)

Specific, timely observations about that person connected to the problem you solve.

> Noticed you're hiring 3 SDRs. Sounds like you're scaling outbound fast. Most teams hit follow-up fatigue during onboarding.

## Research Signal Stack

| Signal            | Where to find it                   | How to use it                                                                |
| ----------------- | ---------------------------------- | ---------------------------------------------------------------------------- |
| Recent funding    | Crunchbase, LinkedIn, press        | "Congrats on Series B. Scaling teams fast usually creates X challenge"      |
| Job postings      | LinkedIn Jobs, careers page        | "Noticed you're hiring 3 SDRs. Sounds like you're scaling outbound"         |
| Tech stack        | BuiltWith, Wappalyzer, HG Insights | "I see you're using HubSpot. Most teams at your stage hit a ceiling with X" |
| LinkedIn activity | Posts, comments, job changes       | "Really enjoyed your post about X"                                           |
| Company news      | Google News, press releases        | "Congrats on acquiring X. Integrating teams usually creates Y challenge"    |
| Podcast/talks     | Google, YouTube, podcasts          | "Caught your talk at SaaStr on X. Really insightful"                        |
| Website changes   | Manual review                      | "Your new pricing page caught my eye. Curious how it's converting"          |

## The 3-Minute Personalization System

From "30 Minutes to President's Club":

**Step 1:** Build a research stack of top 10 buying signals — 5 company triggers, 5 person triggers. Stack-rank by relevance.

**Step 2:** Build a 3x3 template: (1) personalization attached to a problem, (2) problem you solve, (3) one-sentence solution + low-friction CTA.

**Step 3:** Create 5 "trigger templates" — pre-written personalization paragraphs for each trigger, with a smooth segue into the problem.

The personalization must logically connect to the problem. This creates 5 reusable triggers with the rest of the email constant. A top SDR writes a personalized email in **under 3 minutes**.

## The Four -Graphic Principles (Becc Holland)

- **Demographic** — Age, profession, background
- **Technographic** — Tech stack, tools used
- **Firmographic** — Company size, funding, industry, growth stage
- **Psychographic** — Values, passions, beliefs (highest-impact dimension)

Tapping into what prospects are passionate about drives significantly higher response rates.

## Observation-Based Openers (highest performing)

**Trigger-event:** "Congrats on the recent funding round. Scaling the team from here is exciting, and I imagine [challenge] is top of mind."

**Observation:** "Your recent post about [topic] resonated. Especially the part about [detail]. Got me thinking about how that applies to [challenge]."

**Industry insight:** "Most [role titles] I talk to spend [X hours/week] on [problem]. Curious if that matches your experience at [Company]."

## What Feels Fake (avoid)

- AI-generated emails with similar phrasing ("I hope this email finds you well")
- Generic attention hacks disconnected from problem ("Cool that you went to UCLA!" → pitch)
- Over-personalizing to creepiness
- "I saw your LinkedIn profile and wanted to reach out" — signals mass automation

## The "So What?" Test

After writing any opening line, read from prospect's perspective: "So what? Why would I care?" If the answer is nothing, rewrite.

## Personalizing With AI

Agents make Level 4 research affordable at scale, and they make invented personalization just as cheap. Buyers in 2026 spot it fast: praise for the company mission, congratulations on a year-old funding round, "I noticed you're in SaaS."

- **Relevance beats personalization.** A specific trigger, the pain it implies, and a concrete offer outperform a clever personal line attached to a generic pitch.
- **Facts first, then the angle,** in two separate steps, with a source URL for every fact.
- **Allow "no hook found."** When research turns up nothing specific, use the segment-level message instead of a manufactured one.
- **Review before sending** for Tier 1 and a sample of Tier 2.

The full research rules and the account brief template are in the prospecting skill's account research reference.



---

## `references/reply-handling.md`

# Handling Replies

The sequence's job ends when someone replies. What happens in the next hour decides whether that reply becomes a meeting. This reference covers classifying replies, responding to each type, speed, booking, and what an agent can handle on its own.

## Classify every reply

| Type | Looks like | Action |
|------|------------|--------|
| **Positive** | "Sure, let's talk," "Send times," "Tell me more" | Respond fast, propose times, book (below) |
| **Information request** | "What does it cost?" "Do you work with X?" | Answer the actual question briefly, then offer a call |
| **Objection** | "We already use X," "No budget," "Not a priority" | Respond once, using the objection guidance below |
| **Not now** | "Reach out next quarter," "After our launch" | Thank them, set a reminder for the date they gave, stop the sequence |
| **Referral** | "Talk to Sam, she owns this" | Thank them; contact Sam citing the referral (with permission to use their name if unclear) |
| **Wrong person, no referral** | "Not my area" | Ask once who owns it; otherwise stop |
| **Out of office** | Auto-reply | Pause; resume after their return date. Note any named stand-in |
| **Unsubscribe or hostile** | "Remove me," "Stop," anger | Suppress on every channel immediately. Apologize briefly if you reply at all. Never argue |
| **Bounce** | Delivery failure | Remove; check whether the contact moved companies (a possible job-change signal) |

Every reply of any type stops all other channels for that person. See [multichannel-cadence.md](multichannel-cadence.md).

## Speed

Answer positive replies within minutes during business hours. The research behind the famous speed-to-lead multipliers is old (2007–2011), but the direction holds. Interest fades fast, and a prospect who replied to you has often replied to others too. Route positive replies to a person instantly (a Slack or phone notification), and keep someone responsible for them every working hour.

## Booking

- **Propose two specific times** in their time zone, and include a booking link as a fallback ("or grab any time here"). Two concrete options get a faster yes than a bare link, which can feel like homework.
- **Send the calendar invite immediately** once they pick, with a one-line agenda.
- **Confirm the day before** with something useful: the agenda, a relevant case study, or (for an agency) the teardown you'll discuss. Pre-reads raise show rates.
- **Reminder an hour before**, by email, or by SMS only if they've agreed to texts.
- **Reschedule no-shows the same day,** warmly, once. A second no-show goes back to nurture.

## Objections in reply to cold outreach

Early objections are usually reflexes. Answer once, briefly, and make it easy to say no:

| Objection | Response approach |
|-----------|-------------------|
| "We already use [competitor]" | Acknowledge it. Name the one situation where teams like theirs still look elsewhere. Ask if it applies |
| "No budget" | Ask when they plan budgets, or offer something that doesn't need one (an audit, a benchmark) |
| "Not a priority" | Ask what is a priority this quarter. If it isn't connected, step back and set a reminder |
| "Send me more info" | Send one specific thing (a one-pager or a two-minute video) and one question that makes a reply easy |
| "How did you get my email?" | Answer honestly with the actual source, and offer to remove them |

Deal-stage objections (pricing negotiation, security reviews, competitive bake-offs) live in the sales-enablement skill's objection library.

## What an agent can handle

| Reply type | Agent alone | Agent drafts, human sends |
|------------|-------------|---------------------------|
| Out of office | ✓ Pause and reschedule | |
| Unsubscribe | ✓ Suppress everywhere | |
| Bounce | ✓ Remove, flag for job-change check | |
| Not now | ✓ Set the reminder, stop the sequence | Polite acknowledgment |
| Positive | | ✓ Until accuracy is proven over 100+ replies |
| Information request | | ✓ |
| Objection | | ✓ |
| Referral | | ✓ |
| Hostile | ✓ Suppress | Any reply at all |

Before an agent sends anything on its own, check that every claim in the draft matches an approved source, that it contains nothing from your banned-phrase list, and that a daily cap applies. Sample-review a share of autonomous replies every week.

## Log it

Record on the CRM contact: reply type, date, the sequence and step that produced it, the signal and channel, and the outcome. That's what makes a weekly sequence review possible (the sequence-retro loop in the marketing-loops skill), and it's the outbound stage model in the revops skill.



---

## `references/subject-lines.md`

# Subject Line Optimization

The subject line determines whether the email gets read. The data is counterintuitive: **short, boring, internal-looking subject lines win decisively.**

## Length: 2–4 words

- 2-word subject lines get **60% more opens** than 5-word (Lavender).
- Going from 2 to 4 words reduces replies by **17.5%**.
- 2–4 words yield **46% open rates** vs 34% for 10 words (Belkins, 5.5M emails).
- Mobile truncates at 30–35 characters — brevity is practical necessity.

## Internal Camouflage Principle

Subject lines that look like they came from a colleague, not a vendor, double open rates (Gong). Buyers mentally categorize before opening — if it looks like sales, it's filtered.

**High-performing examples:** "reply rates" · "trial delays" · "hiring ops" · "employee turnover" · "Q2 forecast" · "new patients" · "personalization issue" · "second page"

## Capitalization: lowercase wins

All-lowercase has highest open rates (Gong, 85M+ emails). Lowercase looks more personal/internal. For cold outreach specifically, lowercase beats title case.

## Personalization: context over name

Personalized subject lines boost opens **26–50%**, but type matters:

- **First name in subject line → 12% fewer replies.** Signals automation.
- **Contextual personalization works:** pain points, competitors, trigger events, industry challenges.
- Use {{painPoint}}, {{competitor}}, {{commonGround}} — not {{firstName}}.

## Questions: only when highly specific

Data conflicts: Belkins says questions perform well (46% open rate). Lavender says questions lower opens by **56%**. Resolution: **specific pain questions work** ("Need help with {{challenge}}?"), **generic questions fail** ("Quick question?" / "Have 15 minutes?"). Default to statements.

## What to Avoid

| Anti-pattern                                   | Impact                      |
| ---------------------------------------------- | --------------------------- |
| Salesy language ("increase," "boost," "ROI")   | -17.9% opens                |
| Urgency words ("ASAP," "urgent")               | Below 36% opens             |
| Excessive punctuation ("!!!" or "??")          | -36% opens                  |
| Numbers and percentages                        | -46% opens                  |
| Emojis                                         | Hurt B2B professionalism    |
| Pitching product in subject                    | -57% replies                |
| Empty/no subject line                          | +30% opens but -12% replies |
| Spam triggers ("free," "guarantee," "act now") | Deliverability risk         |

## C-Suite Subject Lines

Executives receive 300–400 emails daily, decide in seconds. They respond **23% more often** than non-C-suite when emails pass their filter (6.4% reply rate).

What works: ultra-concise, human, understated. "{{companyInitiative}}" · "thank you" · "an update" · "a question" · reference to a specific project or trigger event.

Anything "salesy" is immediately rejected.
