# attribution

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/attribution

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to figure out which marketing actually drives conversions and revenue, choose or interpret an attribution model, or reconcile conflicting numbers across tools. Also use when the user mentions "attribution," "attribution model," "first-touch vs last-touch," "multi-touch," "which channel drives revenue," "what's my real CAC," "my dashboards disagree," "Google/Meta says X but GA says Y," "media mix model," "MMM," "incrementality," "geo lift," "holdout test," "how did you hear about us," "self-reported attribution," "dark social," or wants to instrument attribution themselves — "stitch my bookings to their source," "SavvyCal/Calendly attribution," "close the identify gap," "track conversions on a third-party domain," "first-party / self-hosted attribution." For event tracking setup and UTMs, see analytics. For ad-platform pixels/CAPI and conversion tracking, see conversion-tracking. For pipeline and CRM revenue reporting, see revops. For the AI-search attribution blind spot, see ai-seo.


# Attribution

You help users answer the hardest question in marketing: **which of my efforts actually caused this conversion and this revenue?** Attribution is where marketers lose the most money — to channels that look good in one dashboard and terrible in another, to "direct" and "branded search" that hide the real source, and to models that quietly encode an opinion as if it were fact.

This skill has two pillars. Know which one the user needs before you dive in:

- **(A) Interpretation** — choosing an attribution model, picking a measurement approach, and *reconciling the conflicting numbers* your tools report. This applies to everyone, even with zero engineering.
- **(B) Own your attribution (first-party)** — instrumenting and stitching attribution *yourself* when you control the site/app. This is the build track. Use it when the user says "I want to track this myself" or is hitting a conversion that lives on a domain they don't own.

Most requests start with (A). Reach for (B) only when they control the surface and want to build.

Product context: check for `.agents/product-marketing.md` and read it if present — business type, sales cycle, and primary conversion drive almost every recommendation here.

## Boundaries — what this skill does NOT own

State these up front so you don't rebuild neighboring skills:

- **General event tracking, tracking plans, UTM setup, GA4/GTM** → **analytics**. Attribution *assumes tracking exists*. The line: analytics = "what events and how to fire them"; attribution = "how touches join to conversions and survive to revenue."
- **Ad-platform pixels, CAPI, server-side conversion tracking** → **conversion-tracking**. Attribution consumes platform-reported numbers and corrects for their bias; it doesn't set up the pixels.
- **Pipeline stages, lead lifecycle, CRM revenue dashboards** → **revops**. Attribution feeds pipeline data; it doesn't define stages.
- **Showing up in / measuring AI search** → **ai-seo**. Attribution names AI traffic as a blind spot only.

---

## Pillar A — Interpretation

### 1. What attribution can and can't tell you

Set expectations before touching a number:

- **Attribution is directional, not truth.** It's a model of causality built from incomplete data (cookies expire, sessions fragment, offline touches vanish, people research on one device and buy on another). Treat it as a strong hint, never a verdict.
- **Every model is an opinion.** "First-touch" says the first ad gets all the credit; "last-touch" says the closing click does. Both are wrong in opposite directions. Choosing a model is choosing whose story to believe — say so out loud.
- **The attribution gap is normal, so separate outcomes from credit.** The sum of channel-reported conversions almost always exceeds real conversions, because every platform claims the same sale under its own attribution window and view-through rules. Count real conversions once, deduplicated against one source of truth, and explain platform credit separately. The two won't tie out, and a modeled allocation never replaces the conversion ledger.

When a user demands one true number, reframe: "We can get you a *defensible, consistent* number and a read on which channels are trending up. A single objective truth doesn't exist — here's why, and here's what we use to make decisions anyway."

### 2. Attribution models

The classic rule-based set plus data-driven — and when each one lies. **Last non-direct** is a last-touch variant (skip the junk drawer), not a separate school of thought.

| Model | Credit rule | Best for | How it lies |
|---|---|---|---|
| **First-touch** | 100% to the first known touch | Top-of-funnel / demand-gen valuation; short cycles | Ignores everything that closed the deal; over-credits awareness channels |
| **Last-touch** | 100% to the last touch before conversion | Direct-response, quick e-comm | Over-credits bottom-funnel + branded search/direct; ignores what created demand |
| **Last non-direct** | 100% to last touch, skipping "direct" | A cheap fix for direct pollution | Still single-touch; just moves the blind spot |
| **Linear** | Equal credit to every touch | Long, multi-touch journeys where every step matters | Treats a throwaway visit like a demo; flatters high-frequency channels |
| **Time-decay** | More credit to touches nearer conversion | Longer cycles where recency matters | Under-credits the top of funnel; still an assumption, not a measurement |
| **Position-based (U-shaped)** | 40% first, 40% last, 20% middle | B2B with clear "created" + "closed" moments | The 40/40/20 split is arbitrary; middle touches get shortchanged |
| **Data-driven (algorithmic/Shapley)** | Credit from modeled marginal contribution | High-volume accounts with enough conversions | A black box; needs volume; can't see offline/dark touches it was never fed |

**Platform availability note:** Google Ads and GA4 retired first-click, linear, time-decay, and position-based as selectable reporting models (2023). Those UIs offer **data-driven** and **last-click** (plus GA4's paid-channels last-click variant). Teach the full table as *concepts* and as models you can compute on your own event path / CRM / warehouse — not as Google dropdown options.

**Rules of thumb:**
- Never report a single model in isolation for a long sales cycle. Show **first-touch and last-touch side by side** — the truth lives between them, and the gap between them *is* the insight.
- Data-driven attribution needs volume. Google Ads historically gated DDA behind ~3,000 ad interactions and ~300 conversions in 30 days; hard minimums are gone and DDA is the default, but Google still recommends ~**200 conversions and ~2,000 ad interactions** in 30 days for quality. Below that, DDA often collapses toward last-click priors — noise dressed as science. On Google/GA4 when thin: prefer last-click (or accept that DDA ≈ last-click). Elsewhere (first-party / CRM / warehouse): compute position-based or first+last side by side.
- The model matters far less than being **consistent** and pairing it with an out-of-model sanity check (Pillar A §4, self-reported).

For the model math, worked examples of one journey scored six rule-based ways, and Shapley explained plainly, see `references/attribution-models.md`.

### 3. The three measurement paradigms

Models split credit *within* your tracked data. Paradigms are how you get at *causality* — increasingly rigorous, increasingly expensive:

| Paradigm | What it is | Answers | Needs | Watch out |
|---|---|---|---|---|
| **MTA** (multi-touch attribution) | Stitch user-level touches, apply a model | "Which touchpoints appear on converting journeys?" | Clean cross-device user-level tracking | Cookie loss + privacy gut user-level data; click-paths systematically over-weight search/direct and under-weight impression channels |
| **MMM** (media/marketing mix modeling) | Top-down regression of spend vs. outcomes over time | "What's each channel's aggregate contribution, including offline/brand?" | 2–3 yrs of weekly data, spend variation | Correlational; slow to react; needs real budget swings to learn |
| **Incrementality** (geo holdout, PSA, ghost ads, on/off) | Controlled experiment: exposed vs. withheld | "Did this channel *cause* lift I wouldn't have gotten anyway?" | Ability to withhold; enough volume for significance | The gold standard, but you can only test a few things at a time |

**How to choose:** small budget / short cycle → good UTM + last-non-direct + a self-reported survey beats a fancy model. Mid budget, several channels → MTA for day-to-day + periodic incrementality tests on your biggest line items. Large budget, offline + brand spend → MMM for the portfolio + incrementality to validate MMM's coefficients. Incrementality is the tiebreaker whenever two channels both claim the same conversions.

Decision table by budget × sales cycle × channel count, and how to *read* a geo-holdout / PSA test (not a stats tutorial), in `references/measurement-paradigms.md`.

### 4. Self-reported attribution

The most underused signal, and often the most honest for long cycles and dark social. A post-conversion "How did you hear about us?" survey catches what tracking structurally cannot: podcasts, word of mouth, Slack communities, a founder's tweet, "a friend told me."

- **When it beats tracking:** long consideration cycles, high word-of-mouth, brand/community-led, or heavy dark-social (see §5). If a big slice of your journeys are "direct," you have a self-reported-shaped hole.
- **Ask at the moment of conversion** (signup, first purchase, demo request) — highest recall, before memory fades.
- **Wording:** open-ended ("How did you first hear about us?") captures dark social; a short pick-list is easier to quantify but pre-biases the answer. Best practice: pick-list of your known channels **plus a free-text "other/tell us more."**
- **Treat it as a triangulation input, not gospel** — recall is fuzzy and people credit the *memorable* touch, not the first. **Discount survey share when turning it into credit** (e.g. 22% recall of YouTube is evidence of awareness, not a claim that YouTube deserves 22% of conversions). Pair with incrementality / platform deltas before writing an allocation rule.
- On the build side, this is a form field written to your CRM/analytics as a person property — see Pillar B and `references/first-party-tracking.md`.

### 5. Reconciling conflicting sources

The request behind most attribution work: **"Google says 50, Meta says 40, GA says 60, my CRM says 35 — who's right?"** Nobody is. Here's the framework.

**Why each source systematically lies:**

| Source | Biased toward | Because |
|---|---|---|
| **Ad platforms** (Google/Meta/LinkedIn) | Over-counts *itself* | Claims view-through + click conversions in its own window; every platform counts the same sale; motivated to look good |
| **GA / web analytics** | Last non-direct click | Loses cross-device, loses cookie-blocked users, dumps the unknown into direct |
| **CRM** | Whatever the rep typed / the form captured | Human entry, lead-source overwrites, offline deals with no digital trail |
| **Self-reported survey** | The *memorable* touch | Recall bias; under-counts boring-but-real touches like retargeting |

**How to triangulate:**
1. **Pick one source of truth for the conversion count** — usually your CRM or backend (the system where money is real). Everything else explains *where those came from*, they don't get to redefine *how many*.
2. **Never sum across platforms.** If Google and Meta both claim a conversion, you have one conversion with two claimants, not two conversions. De-dupe against the source-of-truth total.
3. **Read directional agreement, not absolute match.** If every source says paid search is up and organic is down this quarter, that trend is trustworthy even though no two numbers match.
4. **Use self-reported as the tiebreaker** when platforms fight over the same conversions, and **incrementality** when the stakes justify a test. Do **not** turn a platform-vs-GA gap into a multiplier rule (Meta claims 2× GA ≠ "double Meta") — investigate windows and view-through, then ground any override in incrementality.
5. **Expect and budget for the gap.** Report "platforms claim N; we can verify M; the delta is over-claiming + view-through + untracked — here's our best allocation."
6. **Operationalize triangulation as rules when you can** — once you have a holdout or a trusted survey band for a channel, apply a documented **channel-level override** on reporting (shift credit from Direct/branded into the under-credited channel for the test window) rather than pretending raw MTA is truth. Details in `references/measurement-paradigms.md`.

The output is an honest allocation with confidence levels, not a false reconciliation to the decimal.

### 6. The blind spots

Where conversions hide, making real channels look weak:

- **Direct** — the junk drawer. Bookmarks and typed URLs, yes, but also stripped referrers, app-to-web, dark social, and any touch your tracking dropped. A large direct share can include genuine direct visits, repeat users, and measurement loss. Investigate its composition before treating it as a tracking defect.
- **Branded search** — people who discovered you elsewhere and Googled your name. Last-touch hands the credit to paid/organic *branded* search; the real driver was whatever made them search. Segment branded vs. non-branded or you'll defund the top of funnel.
- **Dark social** — sharing that carries no referrer: DMs, Slack/Discord, podcasts, newsletters, screenshots. Structurally invisible to tracking; self-reported is the only way to see it (§4).
- **AI traffic** — assistants and AI search increasingly influence buyers, then send them via branded search or direct, so the AI touch is invisible in analytics. Name it and hand deeper work to **ai-seo**.

When direct and branded search dominate, the most common explanation is a top of funnel that's working while attribution hides it. Confirm before concluding: rule out existing customers, lost referrers, and offline discovery, then check self-reported attribution or run an incrementality test. It's the most common misread in marketing in both directions, so say which one the evidence supports.

### 7. Business-type fork

Defaults differ sharply. Summary here; full playbooks in `references/by-business-type.md`.

- **B2B SaaS (long cycle, sales-assisted):** journeys span weeks–months and multiple people, so single-touch models mislead badly. Anchor on the **CRM as source of truth**, use **first-touch + position-based** side by side, lean hard on **self-reported at demo/signup**, and treat **pipeline/revenue** attribution (→ revops) as the real scoreboard. Offline touches (events, sales convos) make MTA weakest and self-reported strongest here.
- **Ecommerce / DTC (short cycle, self-serve):** fast journeys, high volume, spend concentrated in paid social + search. Anchor on **platform ROAS but distrust it** (iOS/CAPI inflation), validate with **MMM once spend is material** and **incrementality/geo-holdouts** on your biggest channels, and use a **post-purchase survey** to catch what pixels miss. Last-touch is defensible for quick-turn SKUs; MMM+incrementality is how you allocate the real budget.

---

## Pillar B — Own your attribution (first-party)

Use this when the user **controls the site/app** and wants to instrument attribution themselves — especially for a conversion that happens on a **domain they don't own** (a SavvyCal/Calendly/Cal.com booking, a Stripe Checkout page). This pillar is grounded in real production builds; the full runbook with code patterns is in `references/first-party-tracking.md`. The essentials:

### The identity graph

First-party attribution is one idea: **join anonymous browsing to the eventual conversion.**

1. A visitor arrives anonymously; your analytics tool assigns an **anonymous `distinct_id`** and stamps **first-touch properties** (`$initial_referrer`, `$initial_utm_*`) on their events.
2. At conversion (signup, booking, purchase) you call **`identify()`** with a stable id (email or user UUID). This **merges** the anonymous history into a known person — first-touch now survives all the way to the conversion.
3. Every conversion event can now be broken down by first-touch channel. That's the whole game.

### Closing the `identify()` gap

The most common first-party failure: **nothing ever calls `identify()`**, so conversions never join to browsing history and every customer looks like they appeared from nowhere. (Framing adapted from Tessa Kriesel's PostHog approach.) The fix is to call identify at each real conversion. **Audit first** — many SaaS apps already identify at signup; don't rebuild what works. Find the *specific* un-instrumented conversions and close only those.

### Stitching conversions on a third-party domain

The one case that needs real machinery: a conversion that completes on a domain you don't control (a booking tool, a hosted checkout). You can't run your analytics there, so:

1. **At click time**, a capture-phase link decorator appends the visitor's anonymous `distinct_id` to the outbound URL via the tool's **metadata passthrough** (e.g. `?metadata[ph_distinct_id]=<id>`). One document-level listener covers every CTA — no per-link edits.
2. The third-party tool stores that metadata and returns it in its **webhook**.
3. Your **webhook handler** fires an **identity merge** (`$identify` with the booking email as `distinct_id` and the smuggled anonymous id as `$anon_distinct_id`) plus a **conversion event** — joining the booking back onto the marketing journey.

### Guardrails (do not skip)

- **Anonymity guard — fail closed.** Only ever smuggle the *anonymous* id. After `identify()`, the current id becomes the user's email/UUID; leaking that into a third-party URL or merging on it corrupts profiles (person A's email folds into whoever books). Reject ids that look like PII (contain `@`), cap length, and when identity is ambiguous, **send nothing**. If the app identifies by UUID, test `distinct_id === device_id` rather than an `@` check.
- **First-touch data quality.** Redirects overwrite the true first touch. Exclude OAuth/checkout referrers (`accounts.google.com`, `checkout.stripe.com`, `login.*`), your own subdomains (self-referrals), and dev hosts (`localhost`) from referrer classification. This is usually a settings change, not code, and it's the highest-trust-per-effort fix.
- **Cross-subdomain stitching.** Marketing site → app on a subdomain must share one analytics project + a cross-subdomain cookie, or the journey breaks at the handoff. Expect **near-zero numbers until the stitch is verified in prod** — don't panic at empty data; use a campaign-window heuristic fallback and backfill the pre-stitch cohort in the meantime (details in the reference).

### Reporting and the last mile

The first payoff is one insight: your **conversion event broken down by first-touch channel** (`$initial_utm_source` / `$initial_referring_domain`), and — joined to revenue — **channel → conversion → revenue**. Confirm first-touch vs. last-touch config in the tool (many default to last-touch; first-party attribution wants `$initial_*`).

But first-touch alone can't run the multi-touch models from §2. **Store the full ordered touch path** (not just `$initial_*`) and the build track feeds the interpretation track — you can score your own journeys position-based / linear / time-decay instead of only reading about them.

**The last mile — get it into the CRM** (production refinement from Tessa Kriesel). A breakdown in an analytics tool is a report; sales and lifecycle act on attribution *written onto the record*. Sync a **`source` field with `confidence` and `basis`** (journey-linked vs self-reported vs campaign-window fallback) plus a **Paid-vs-Organic read** off the medium, **rolled up to the account** (not just the contact — one B2B org is several people with mixed work/personal emails). How pipeline/lifecycle then *use* it is **revops**' job.

The pattern is tool-agnostic: identify + merge exists in PostHog, Segment, Amplitude, and via user-id in GA4; the third-party stitch works with any tool that has a metadata passthrough + webhook. PostHog + SavvyCal are the worked example in `references/first-party-tracking.md`.

---

## Output format

Deliver an **attribution readout**, not a data dump:

```markdown
# Attribution Readout — [date]

## The question
[What decision this informs — e.g. "where should next quarter's budget go?"]

## Source of truth
[Which system defines the conversion count, and why]

## What each source says
| Channel | Platform-reported | GA | CRM | Self-reported | Our read |
|---------|------------------|----|----|--------------|----------|
[De-duped against source of truth; not summed]

## Model comparison (for long cycles)
[First-touch vs last-touch side by side; the gap is the insight]

## Confidence & gaps
[The attribution gap, the blind spots, what we can't see]

## Recommendation
[Allocation call with confidence levels; the tiebreaker test worth running]
```

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md). Key tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **PostHog** | First-party attribution, identify/merge, funnels | - | [posthog.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/posthog.md) |
| **GA4** | Web analytics, model comparison, user-id stitching | ✓ | [ga4.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/ga4.md) |
| **Dub** | Short-link + click attribution | ✓ | [dub-co.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/dub-co.md) |
| **Segment** | CDP — route identify/track to every destination | - | [segment.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/segment.md) |
| **HubSpot** | CRM lead-source + self-reported fields | ✓ | [hubspot.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/hubspot.md) |
| **Salesforce** | CRM as revenue source of truth | - | [salesforce.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/salesforce.md) |
| **Supermetrics** | Pull platform numbers into one place to reconcile | ✓ | [supermetrics.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/supermetrics.md) |
| **RB2B** | De-anonymize B2B website visitors | - | [rb2b.md](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/rb2b.md) |

---

## Related Skills

- **analytics** — event tracking, tracking plans, UTMs, GA4/GTM setup. Do this *before* attribution.
- **conversion-tracking** — ad-platform pixels, CAPI, server-side conversion tracking, and tracking audits.
- **revops** — pipeline stages, lead lifecycle, CRM revenue reporting. Attribution feeds it.
- **ai-seo** — the AI-search attribution blind spot in depth.
- **ab-testing** — controlled experiments; the incrementality mindset applied to on-site changes.



---

## `references/attribution-models.md`

# Attribution Models — The Math, Worked

Six rule-based credit rules on one journey, plus data-driven attribution explained without the black box. Use this when the user wants to understand *why* two models disagree, or needs to pick one defensibly.

**Availability:** Google Ads and GA4 no longer offer first-click, linear, time-decay, or position-based as reporting models (retired 2023). Use this file for *concepts* and for scoring journeys on your own data (CRM, warehouse, first-party path). In Google UIs today: data-driven and last-click only.

## The worked journey

A single B2B buyer's path to a $12,000 annual deal, five touches over 38 days:

| # | Day | Touch | Role in the story |
|---|---|---|---|
| T1 | 0 | LinkedIn ad (paid social) | First discovered you — created awareness |
| T2 | 5 | Organic blog post (organic search) | Came back to learn — built interest |
| T3 | 12 | Retargeting ad (paid social) | Nudged back mid-consideration |
| T4 | 30 | Branded search (paid search, branded) | Ready to act — searched your name |
| T5 | 38 | Direct → demo request (direct) | Converted |

The whole point: **the touch that gets credit depends entirely on the model, and each model tells a different story about where your $12k came from.**

## The six rule-based models, applied

Credit for the $12,000 deal under each rule (last non-direct is a last-touch variant that skips Direct):

| Touch | Channel | First-touch | Last-touch | Last non-direct | Linear | Time-decay | Position (U) |
|---|---|---|---|---|---|---|---|
| T1 | Paid social | **$12,000** | $0 | $0 | $2,400 | $175 | **$4,800** |
| T2 | Organic | $0 | $0 | $0 | $2,400 | $290 | $800 |
| T3 | Paid social | $0 | $0 | $0 | $2,400 | $575 | $800 |
| T4 | Paid search (branded) | $0 | $0 | **$12,000** | $2,400 | $3,415 | $800 |
| T5 | Direct | $0 | **$12,000** | $0 | $2,400 | **$7,545** | **$4,800** |

*(Time-decay uses a 7-day half-life — weight = 0.5^(days-before-conversion / 7), normalized: shares of ~1.5% / 2.4% / 4.8% / 28.5% / 62.9% (dollars rounded to sum to $12,000). With a 38-day journey the credit concentrates hard on the last two touches — which is exactly why time-decay behaves almost like last-touch on long cycles. Position-based is 40/40/20, the 20% split evenly across T2–T4.)*

**Read the disagreement:**
- **First-touch** hands everything to the **LinkedIn ad** — great for arguing paid social's demand-gen value, blind to what closed it.
- **Last-touch** hands everything to **Direct** — which is really "we don't know," the junk-drawer channel (see SKILL.md §6). This is how top-of-funnel gets defunded.
- **Last non-direct** hands it to **branded search** — but branded search only happened *because* the LinkedIn ad and blog created the demand. Crediting the closing branded click is crediting your own brand for demand someone else's channel created.
- **Linear** spreads it evenly — honest that all five mattered, useless for deciding what to cut (everything looks equally important).
- **Time-decay** favors the recent — reasonable for short cycles, but here it under-credits the LinkedIn ad that started everything.
- **Position-based** credits the **bookends** (discovered + closed) — usually the most defensible single model for B2B, because "what created this deal" and "what closed it" are the two decisions you actually make.

**The takeaway to give the user:** report **first-touch and last-touch side by side**. The LinkedIn-vs-Direct gap *is* the insight — it tells you paid social creates demand that later shows up as direct/branded. No single number captures that; the spread does.

## Data-driven / algorithmic attribution (Shapley), plainly

Data-driven attribution (Google's DDA, most MTA tools) doesn't use a fixed rule. It asks a counterfactual: **how much does each touch actually change the probability of conversion?** The formal engine is the **Shapley value** from cooperative game theory.

The plain-English version:

- Treat each touch as a "player" on a team that produced the conversion.
- Look across *all* your journeys — converting and non-converting.
- For a given touch, compare conversion rates of journeys that had it vs. otherwise-similar journeys that didn't, across every possible combination of the other touches.
- A touch's credit = its **average marginal lift** to conversion probability across all those combinations.

So if journeys with a retargeting touch convert meaningfully more often than identical journeys without it, retargeting earns real credit. If adding a channel changes nothing, it earns ~zero — even if it appears on every path.

**When it's worth it:**
- You have **volume** — the counterfactuals need enough conversions to be stable. Google Ads historically gated DDA behind ~3,000 ad interactions and ~300 conversions in 30 days; hard gates are gone and DDA is the default, but Google still recommends ~**200 conversions and ~2,000 ad interactions** in 30 days for quality. Below that, DDA often looks a lot like last-click. On Google/GA4 when thin: use last-click (or accept noisy DDA). On your own data: prefer position-based or first+last side by side.
- Your journeys are **mostly digital and tracked** — Shapley can only weigh touches it was fed. Offline events, dark social, and cookie-lost touches are invisible to it, so a high-word-of-mouth B2B motion will get a confidently-wrong DDA. Pair it with self-reported (SKILL.md §4).

**Its honest limitations:**
- **Black box** — you can't easily explain to a CFO why LinkedIn got 23%. "The model says so" is a weak budget argument on its own.
- **Correlation, not causation** — it models what *co-occurs* with conversion, not what *causes* it. That's why incrementality testing (see `measurement-paradigms.md`) exists: to validate what DDA claims.
- **Garbage in** — inherits every blind spot in your tracking. If half your journeys are "direct," DDA is confidently splitting credit on half-blind data.

## Choosing — a short decision guide

- **Short cycle, few touches, small volume** → last non-direct, plus a self-reported survey. Don't over-model.
- **Long B2B cycle, clear created/closed moments** → position-based as the primary *on your own path data*, first-touch + last-touch shown alongside. (Not a Google Ads model picker option.)
- **High volume, mostly-digital, need day-to-day allocation** → data-driven, validated periodically by incrementality.
- **Offline + brand-heavy, real budget** → don't rely on any user-level model; go MMM + incrementality (see `measurement-paradigms.md`).

In every case: **pick one model, stay consistent, and pair it with an out-of-model check.** Model-switching to make a channel look good is the fastest way to lose trust in the whole attribution program.



---

## `references/by-business-type.md`

# Attribution by Business Type

Attribution defaults differ sharply by business model. The same "which channel drives revenue?" question wants a different source of truth, model, and paradigm depending on how long your cycle is, how many people are involved, and where your budget goes. Two playbooks: B2B SaaS and Ecommerce/DTC. Match the user's product to one (or blend, for PLG-with-sales).

---

## B2B SaaS (long cycle, sales-assisted)

**Shape of the problem:** journeys run weeks to months, span multiple people (champion, economic buyer, users), and include touches that never appear in web analytics — a conference conversation, a sales call, a Slack-community mention, a peer recommendation. Deal values are high and volume is low, so every deal matters and averages are noisy.

**Why single-touch models mislead badly here:** with 15 touches over 3 months across 4 people, "last-touch = direct" and "first-touch = one LinkedIn ad" are both almost useless. The middle — and the offline — is where the deal was actually won.

### The B2B playbook

1. **Source of truth = the CRM**, not any analytics tool. Revenue is real in the CRM (closed-won, ARR); everything else explains where those deals came from. Pipeline and revenue attribution live in **revops** — attribution feeds it the "source" dimension.
2. **Models: first-touch + position-based, shown together.** First-touch values demand creation (which channel *started* the accounts that became pipeline). Position-based credits the created-and-closed bookends, the two decisions you actually make. Last-touch alone will defund your top of funnel — don't lead with it.
3. **Self-reported attribution is your strongest signal, not a nice-to-have.** Ask "How did you first hear about us?" on the **demo request / signup form** and again qualitatively on sales calls. For high word-of-mouth and dark-social-heavy B2B, this catches what tracking structurally can't (podcasts, communities, "my old coworker used you"). Weight it heavily.
4. **Attribute to pipeline stages, not just the conversion.** The useful B2B question isn't "what drove the form fill" — it's "what drove *qualified pipeline* and *closed revenue*." Break down MQL→SQL→closed-won by first-touch channel; a channel that fills forms but never closes is a trap. (Stage mechanics → revops.)
5. **MTA is weakest here; incrementality is awkward but valuable.** Low volume makes data-driven attribution unreliable and geo-tests hard. Use **on/off tests** for big-ticket programs (turn off a channel for a quarter, watch pipeline) and lean on self-reported + first-touch for the rest.
6. **Account-level, not just lead-level.** Attribution should roll touches up to the *account* (all the people at the buying company), or you'll credit whichever individual happened to fill the form. In practice one org is several people signing up with **mixed work *and* personal emails**, so person-level attribution scatters the story across records — match contacts to the account (email domain, enrichment, or your CRM's contact→account link) and attribute at the **account** level. That's where the signal has to land to be useful to a rep working the whole buying committee. Exclude free-mail domains (gmail/yahoo/outlook) from domain matching — they can't identify a company; fall back to enrichment or manual matching for personal-email signups. *(Production emphasis from Tessa Kriesel; the CRM-sync mechanics live in `first-party-tracking.md` Step 5.)*

**Tooling:** CRM (HubSpot/Salesforce) as truth; a product-analytics tool identifying by user/account UUID for first-party first-touch (see `first-party-tracking.md`); self-reported fields written to the CRM; RB2B-style de-anonymization to catch un-formed account visits.

**The B2B trap to name for the user:** branded search and direct will look like your best "channels" because that's where researched buyers convert. They're not channels — they're where demand *created elsewhere* cashes out. Segment branded vs. non-branded search and treat a big direct share as evidence your top-of-funnel is working, not as a channel to invest in.

---

## Ecommerce / DTC (short cycle, self-serve)

**Shape of the problem:** journeys are fast (minutes to a few days), high-volume, and almost entirely digital and self-serve. Budget concentrates in paid social + paid search + email/SMS. The conversion is a purchase you fully control (your checkout or a hosted one). The dominant lie is **platform over-attribution** — Meta and Google each claiming the same sales.

### The DTC playbook

1. **Source of truth = your store/backend** (Shopify, your payments system) — the count of actual orders. Platform-reported conversions get de-duped *against* that total; they never define it and are never summed.
2. **Distrust platform ROAS by default.** Post-iOS ATT, platforms model and estimate conversions, count view-through, and use generous windows — reported ROAS runs well above incremental ROAS. Use it for in-platform optimization (it's fine for the algorithm) but not for cross-channel budget truth.
3. **Last-touch is defensible for quick-turn, impulse SKUs** — the closing click really is most of the story for a $30 impulse buy. It gets dangerous as consideration lengthens (higher AOV, considered purchases), where it over-credits retargeting and branded search.
4. **MMM once spend is material.** When you're spending real money across paid social, search, and offline (podcasts, TV, influencers, OOH), MMM is how you allocate — it's the only paradigm that sees the untrackable channels and the saturation curves. Below ~six figures/month of blended spend, MMM is overkill; good UTMs + a survey do more.
5. **Incrementality on your biggest channels — especially the "always credited" ones.** Geo-holdouts and on/off tests earn their keep on retargeting, branded search, and Meta prospecting, which platform reporting flatters most. Incremental CPA (spend ÷ *incremental* orders) is the number that should move budget. (See `measurement-paradigms.md`.)
6. **Post-purchase survey to catch the dark-social + brand demand.** A one-question "How did you hear about us?" on the order-confirmation page consistently reveals that podcasts, TikTok organic, and word-of-mouth drive far more than pixels credit — because those touches convert later as "direct" or branded search. Kickstarter-era DTC brands run this as standard for exactly this reason.

**Tooling:** store/backend as truth; platform pixels + CAPI for optimization (setup → conversion-tracking); Supermetrics/Coupler to pull platform numbers into one place for de-duping; a post-purchase survey app; MMM tooling (Robyn/Meridian or a vendor) once spend justifies it.

**The DTC trap to name for the user:** summing platform-reported conversions. If Meta claims 100 and Google claims 80 but you had 120 orders, you do **not** have 180 conversions — you have 120 with overlapping claims. Anchor on the 120 and allocate the overlap with incrementality, not by trusting whichever platform shouts loudest.

---

## Blended / PLG-with-sales

Many modern SaaS businesses are both: self-serve signups *and* a sales-assisted motion for larger accounts. Blend the playbooks:

- Use the **DTC approach for the self-serve funnel** (fast, high-volume, first-party first-touch → conversion, defensible last-non-direct + survey).
- Use the **B2B approach for the sales-assisted funnel** (CRM as truth, position-based, pipeline-stage attribution, self-reported at demo).
- **Alias identities across the two** so a self-serve signup who later becomes a sales-assisted expansion keeps one journey (email↔UUID alias at signup — see `first-party-tracking.md`).
- Report them **separately.** Blending a $50 self-serve signup and a $50k enterprise deal into one "attribution" number hides both stories.



---

## `references/first-party-tracking.md`

# First-Party Attribution — The Own-Your-Attribution Runbook

How to instrument and stitch attribution yourself when you control the site/app. This is the build track (Pillar B). It's distilled from real production builds and kept tool-agnostic — **PostHog + SavvyCal are the worked example**, but the pattern maps to any product-analytics tool with `identify()`/merge (Segment, Amplitude, GA4 user-id) and any third-party conversion domain with a metadata passthrough + webhook (Calendly, Cal.com, Stripe Checkout, Typeform).

The core method — closing the `identify()` gap so conversions join to anonymous browsing history — is **adapted from Tessa Kriesel's PostHog attribution approach**. Several of the production refinements that make this operate at scale are also hers, credited inline: the full-touch-path capture that feeds the model track (Step 4), the CRM last-mile with source/confidence/basis and a Paid-vs-Organic read (Step 5), the account rollup, and the "expect ~zero until the stitch is verified, with a campaign-window fallback + backfill" window (Cross-subdomain stitching). Credit where due.

## The one idea

First-party attribution joins **anonymous browsing** to the **eventual conversion**:

```
anonymous visitor          identify() at conversion         breakdown
─────────────────          ────────────────────────         ─────────
distinct_id = anon_uuid    identify(email)                  conversion event
$initial_utm_source=...  → merges anon history        →     by $initial_utm_source
$initial_referrer=...      into person(email)               = "where do customers come from"
```

Everything below serves that join. If `identify()` never fires, every customer looks like they appeared from nowhere — that's *the gap*.

## Step 0 — Audit before you build

The most expensive mistake is rebuilding attribution that already works. Many SaaS apps already `identify()` at signup and already carry first-touch on person profiles. **Check the live data first:**

- Do person profiles carry `$initial_utm_source` / `$initial_referring_domain`?
- Does a conversion event (`Signed up`, `Converted to paid`) break down *cleanly* by channel, or is everything "Direct"?
- Is identity keyed by **email** or by an internal **UUID**? (This changes every guard below.)
- Does cross-subdomain stitching work (marketing site → app.yourdomain.com)?

Only instrument the **specific conversions that are genuinely un-joined**. In one real audit the self-serve funnel was already solved end-to-end; the *only* gap was a booking on a third-party domain. Don't touch what works.

## Step 1 — Identify at each real conversion

At every conversion moment, call `identify()` with a stable id, and set person properties:

```js
// Normalize before use as a distinct_id — analytics tools match exact strings,
// so "Corey@x.com" and "corey@x.com" split into two people otherwise.
export function identifyUser(email) {
  const normalized = email.trim().toLowerCase();
  window.posthog?.identify(normalized, { email: normalized });
}
```

With `person_profiles: 'identified_only'`, this is the moment the person is created and their first-touch props are stamped. Fire it on form success, signup, first purchase — any moment you learn who the anonymous visitor actually is.

## Step 2 — Stitch conversions on a domain you don't own

When the conversion completes on a third-party domain (a booking tool, hosted checkout), you can't run your analytics there. Smuggle the anonymous id through the tool's **metadata passthrough**, then merge it back in the **webhook**.

### 2a — Capture-phase link decorator

One document-level listener rewrites every outbound booking link at click time — no per-CTA edits, and it covers plain clicks, keyboard activation, and middle-click (`auxclick`):

```js
// Refresh anonymous metadata on each SavvyCal activation; clear stale IDs.
function decorate(e) {
  const anchor = e.target?.closest?.("a[href]");
  if (!(anchor instanceof HTMLAnchorElement)) return;

  let url;
  try { url = new URL(anchor.href); } catch { return; }
  const host = url.hostname;
  if (host !== "savvycal.com" && !host.endsWith(".savvycal.com")) return;

  const distinctId = getPostHogDistinctId();   // anonymous-only — see guard
  if (distinctId) {
    url.searchParams.set("metadata[ph_distinct_id]", distinctId);
  } else {
    // The same anchor may have been decorated before identify() or reset().
    url.searchParams.delete("metadata[ph_distinct_id]");
  }
  anchor.href = url.toString();
}
document.addEventListener("click", decorate, true);    // capture phase
document.addEventListener("auxclick", decorate, true);
```

An early return when the guard rejects the current ID leaves any previously added metadata on the anchor. Remove that one parameter instead, preserving the booking path, other parameters and fragment. Check both `click` and `auxclick` after an identity change.

For an **inline embed** (e.g. `/demo` with an embedded calendar), pass the same id in the embed's metadata config instead; poll briefly (~2s) for the id on fresh visits, but never block the calendar from rendering.

### 2b — Read the anonymous id safely

The SDK stub queues calls before it loads, so `get_distinct_id()` returns undefined early — fall back to the tool's own cookie:

```js
export function getPostHogDistinctId() {
  if (typeof window === "undefined") return null;

  // Prefer the loaded SDK.
  try {
    if (window.posthog?.__loaded) {
      const id = window.posthog.get_distinct_id();
      if (id) return isAnonymousDistinctId(id) ? id : null;
    }
  } catch {}

  // Fall back to PostHog's cookie before the SDK finishes loading.
  try {
    const prefix = `ph_${POSTHOG_API_KEY}_posthog=`;
    const cookie = document.cookie.split(/;\s*/).find(c => c.startsWith(prefix));
    if (!cookie) return null;
    const parsed = JSON.parse(decodeURIComponent(cookie.slice(prefix.length)));
    return typeof parsed.distinct_id === "string" && isAnonymousDistinctId(parsed.distinct_id)
      ? parsed.distinct_id : null;
  } catch { return null; }
}
```

### 2c — Merge in the webhook

The third-party tool returns your metadata in its `booking.created` (or `checkout.completed`) webhook. Fire an identity merge + a conversion event to your analytics ingestion endpoint:

```js
// Normalize the booking email the same way the app does (Step 1), or the
// booking person will split from the app-side identity for the same user.
const userId = email.trim().toLowerCase();

const events = [];
if (anonId) {
  events.push({
    event: "$identify",
    distinct_id: userId,                                  // the known person
    properties: { $anon_distinct_id: anonId, $set: { email: userId, name } },  // merge the journey
  });
}
events.push({
  event: "discovery_call_booked",
  distinct_id: userId,
  properties: { booking_id, journey_linked: Boolean(anonId) },  // track the fallback rate
});

// Run after the booking's business-critical work; analytics must not fail it.
try {
  const response = await fetch(`${POSTHOG_HOST}/batch/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ api_key: POSTHOG_API_KEY, batch: events }),
    signal: AbortSignal.timeout(3000),
  });
  // fetch resolves for HTTP errors too; a resolved promise isn't acceptance.
  if (!response.ok) {
    console.warn("Analytics ingestion rejected", { booking_id, status: response.status });
  }
} catch {
  // Timeouts and network errors stay non-fatal. Never log the payload or email.
  console.warn("Analytics ingestion unavailable", { booking_id });
}
```

When no id survives (link bypassed the decorator, e.g. a booking link inside a generated email/PDF), fall back to **email-only capture** with `journey_linked: false`. You still get the conversion; you just don't get the journey for that one.

**First-touch survival caveat (PostHog specifics):** the `$anon_distinct_id` merge carries the anonymous person's *event* history, but with `person_profiles: 'identified_only'` the anonymous visitor may never have had a person profile, so their `$initial_*` first-touch props aren't guaranteed to land on the merged person. Two robust fixes: call `posthog.createPersonProfile()` client-side *before* the visitor navigates off to the third-party domain (so the profile and its `$initial_*` exist to merge into), **or** capture the first-touch values client-side and pass them through the same metadata passthrough, then re-assert them in the webhook with `$set_once` (`$set_once` never overwrites an existing value, so it's safe). Without one of these, you can get the booking joined to the journey's *events* but a blank `$initial_utm_source` on the person — verify on a real booking. ([posthog-js#1524](https://github.com/PostHog/posthog-js/issues/1524).)

## Step 3 — The guardrails (do not skip)

### Anonymity guard — fail closed

Only ever smuggle the *anonymous* id. After `identify()`, the current `distinct_id` becomes the user's email/UUID — leaking that into a third-party URL, or merging on it in the webhook, folds unrelated people together and leaks PII.

**Pick the guard that matches your identity model — the two are not interchangeable.** The `@`-check below is *only* safe when your app identifies by **email**; do not copy it into a UUID-identity app.

```js
// EMAIL-IDENTITY apps only. True only for ids safe to smuggle: reject
// email-shaped values (an identified email) and cap length.
export function isAnonymousDistinctId(id) {
  return id.length > 0 && id.length <= 100 && !id.includes("@");
}
```

**If the app identifies by UUID, not email**, the `@` check is useless — an identified UUID would pass it and leak. Instead test that the current `distinct_id` still equals the `device_id` (calling `identify()` changes `distinct_id` but leaves `device_id`), and **fail closed** when `device_id` is unreadable:

```js
// UUID-identity variant: only anonymous when distinct_id still == device_id.
function isAnonymous(posthog) {
  const did = posthog.get_distinct_id?.();
  const dev = posthog.get_property?.("$device_id");
  if (!did || !dev) return false;   // ambiguous → treat as identified, send nothing
  return did === dev;
}
```

The rule in one line: **when identity is ambiguous, send nothing.** A missing journey is a data gap; a wrong merge is corruption.

### First-touch data quality — the cheapest big win

Redirects overwrite the true first touch, inflating "Direct"/"Referral" and hiding real acquisition. Exclude these from referrer/channel classification (usually a *settings* change in the analytics tool, not code):

- **OAuth / checkout redirects:** `accounts.google.com`, `login.microsoftonline.com`, `login.live.com`, `checkout.stripe.com`
- **Self / subdomain referrals:** `yourdomain.com`, `app.yourdomain.com`, `auth.yourdomain.com`
- **Dev/internal traffic:** `localhost`, `127.0.0.1`, test accounts

This is the **highest-trust-per-effort** fix in the whole runbook — no deploy, immediate accuracy gain. Do it first.

### Cross-subdomain stitching

Marketing site → app on a subdomain must share **one analytics project** and a **cross-subdomain cookie** (PostHog's `cross_subdomain_cookie` default handles `yourdomain.com` → `app.yourdomain.com`). Verify the journey survives the handoff, or every signup looks like it started at the app.

**Expect near-zero numbers until the stitch is verified in prod — don't panic.** (Production note from Tessa Kriesel.) Before the cross-subdomain stitch is confirmed live, first-party attribution reads *basically nothing* — journeys break at the handoff and everything looks like direct. It flips from ~0 to real numbers the week the stitch actually ships. Two things get you through that window:

- **A campaign-window heuristic fallback.** When a signup has no linked journey, attribute it to the campaign/channel that was live during its signup window — but only when **date + landing page + active UTMs uniquely narrow it to one source**. With overlapping campaigns, evergreen ads, email sends, branded/direct demand, or a shared landing page, the window can't isolate the cause — mark those `unknown` / low-confidence rather than falsely crediting whatever was live. Used narrowly, it's a real signal while the stitch stabilizes and beats a blank; used bluntly, it manufactures false attribution.
- **Backfill only the pre-stitch records that are actually missing a source.** Many pre-stitch signups already have verified or self-reported attribution — **never overwrite a higher-confidence source with the heuristic.** Backfill only the blanks (campaign-window or self-reported), tag them as such, and keep the heuristic-backfilled history visually separate from verified trends so you don't read a cliff on launch day as a real shift.

Mark these fallback-attributed conversions with a lower-confidence `basis` (see Step 5) so you never confuse a heuristic guess with a verified journey.

### Harden the webhook

- Verify the provider's **signature** (`SAVVYCAL_WEBHOOK_SECRET` etc.).
- **Validate** the smuggled id (string, ≤100 chars, no `@`) before merging.
- Run the analytics call **after** any business-critical work, bounded by a timeout, **non-fatal** on failure. Check HTTP status and catch timeout/network rejections, as in Step 2c. If delivery needs retry guarantees, enqueue analytics separately with idempotency rather than failing or replaying the booking.
- **Log the booking id, never the email.**

## Step 4 — Report

- **Config check:** many tools default to *last-touch* (PostHog's Marketing Analytics scene does). First-party attribution wants first-touch — build insights on `$initial_*` explicitly, or switch the default.
- **The payoff insight:** conversion event broken down by `$initial_utm_source` / `$initial_referring_domain` — "where does every signup/booking come from."
- **Channel → revenue:** conversion event by channel, joined to revenue/MRR person properties. Note: some tools compute revenue props *at ingest* (person-on-events), so historical events may read 0 — use the persons table for current MRR, or tier by plan.
- **Track your own coverage:** the `journey_linked: false` rate tells you how many conversions bypassed the stitch. Watch it after launch.
- **Store the full touch path, not just `$initial_*`.** (Refinement from Tessa Kriesel.) First-touch alone lets you break conversions down by *first* channel — but it can't run the multi-touch models from the interpretation track (SKILL.md §2: position-based, linear, time-decay). If you also persist the **ordered sequence of touches** per person (channel + timestamp for each, e.g. an events-table query or a `touch_path` array on the person), the build track *feeds* the interpretation track: you can now score the same journey six ways on your own data instead of only reading about the models. This is what makes Pillar A and Pillar B shake hands — capture first-touch to ship, capture the full path to model.

## Step 5 — The last mile: get attribution into the CRM

(This whole step is a production refinement from Tessa Kriesel — it's the thing that turned first-party attribution from a dashboard into an operating signal.)

A channel breakdown living in your analytics tool is a *report*. The thing sales and lifecycle actually act on is **attribution written onto the record in the CRM**, per account. Sync it out:

- **A `source` field, plus `source_confidence` and `source_basis`.** Don't write a bare channel — write the channel *and how you know it*. `basis` is the **evidence type**: `journey_linked` (verified stitch), `self_reported` (survey), or `campaign_window` (the heuristic fallback above). `confidence` is computed from **evidence quality, not just the basis** — a journey_linked touch with clean UTMs is high, the same touch with dirty/missing UTMs is lower, and a *specific* self-report can be high while a vague one is low. Sales treats a high-confidence source very differently from a low-confidence guess — give them both fields or they'll distrust the whole thing.
- **A Paid-vs-Organic read off the medium.** The single most-used cut in practice: mark a touch **`paid`** only from explicit paid mediums (`cpc`, `ppc`, `paid-social`, `display`, `paid`), and classify the rest into a small, configurable taxonomy rather than a blunt "organic" — `owned` (email, push, SMS — though a sponsored newsletter is *paid*), `earned` (organic search/social, referral — but a partner/affiliate referral is closer to paid), `direct` (no medium — unknown, not organic), `unknown`. The fast operational question a rep or nurture flow needs is really **paid vs non-paid** (did this account cost acquisition dollars) — get that boundary right and keep the finer buckets configurable.
- **Roll up to the account, not just the contact** (B2B) — see the account-rollup note below and in `by-business-type.md`.
- **Hand the record off to revops.** Once the source/confidence/basis + paid/organic live on the account, how pipeline and lifecycle *use* them (routing, lead scoring, nurture branching, revenue attribution reporting) is the **revops** skill's job. This runbook's job is to get a trustworthy, labeled source onto the record.

**Account rollup (B2B).** One org is several people signing up with mixed work *and* personal emails, so person-level attribution scatters the story across records. Roll each person's source up to the **account** and attribute at the account level — that's where the signal has to land to be useful to a salesperson working the whole buying committee. Match on email domain, **but exclude free-mail domains** (`gmail.com`, `yahoo.com`, `outlook.com`, …) — those can't identify a company, so a domain match would collapse unrelated people into one bogus account. For personal-email signups, fall back to enrichment, your CRM's contact→account link, or manual matching.

## Verification checklist

- Click a booking CTA → URL shows `metadata[<id_param>]=<anon-uuid>`.
- In console: `posthog.identify('test@x.com')` → click again → the param must **NOT** appear (guard works). `posthog.reset()` after.
- Hand-POST a webhook `/batch/` payload → expect `{"status":"Ok"}`, person appears merged.
- Post-ship: first real webhook log shows `journey_linked: true`.
- Confirm first-touch survives cross-subdomain: start on marketing site, sign up in app, check the person carries the original `$initial_utm_source`.

## Adapting to other stacks

| Piece | PostHog (worked example) | Generalizes to |
|---|---|---|
| Anonymous id | `distinct_id` / `$device_id` | Segment `anonymousId`, Amplitude `deviceId`, GA4 client_id |
| Merge call | `$identify` + `$anon_distinct_id` | Segment `identify` (known `userId`, same `anonymousId`) + `alias` where needed; Amplitude `setUserId` on the session that still holds the anonymous `deviceId` (the stitch is deviceId↔userId — Amplitude's Identify API only sets user *properties*, it does not merge); GA4 `user_id` on the same `client_id` |
| Ingestion | `/batch/` | Segment HTTP API, Amplitude HTTP v2, GA4 Measurement Protocol |
| Third-party passthrough | SavvyCal `metadata[...]` | **Calendly:** only standard UTMs (`utm_source`/`medium`/`campaign`/`content`/`term`) plus `salesforce_uuid` — map the anon id into a supported UTM (e.g. `utm_term`), not a free-form `metadata[]` param. Cal.com metadata; Stripe `client_reference_id`/metadata |
| First-touch props | `$initial_*` | Segment/Amplitude first-touch, GA4 first_user_* dimensions |

The shape never changes: **grab the anonymous id → carry it across the boundary → merge on the far side → break the conversion down by first-touch.**



---

## `references/measurement-paradigms.md`

# Measurement Paradigms — MTA vs. MMM vs. Incrementality

Attribution *models* (see `attribution-models.md`) split credit *within* your tracked data. They can't tell you what would have happened anyway. That's what these three paradigms are for — increasingly rigorous, increasingly expensive ways to get closer to causality. Use this reference to help a user pick, and to explain how a test *reads* (not how to run the statistics).

## The three, compared

| | **MTA** (multi-touch) | **MMM** (media mix modeling) | **Incrementality** (experiments) |
|---|---|---|---|
| **Approach** | Bottom-up: stitch user-level touches, apply a model | Top-down: regress outcomes vs. spend/factors over time | Controlled: withhold exposure from a group, measure the difference |
| **Answers** | "Which touchpoints are on converting journeys?" | "What's each channel's aggregate contribution?" | "Did this channel *cause* lift I wouldn't have gotten?" |
| **Granularity** | Per user, per touch | Per channel, per week | Per test (one channel/tactic at a time) |
| **Data needed** | Clean cross-device user-level tracking | 2–3 yrs weekly data + spend variation | Ability to withhold + enough volume for significance |
| **Reacts** | Real-time | Slowly (weeks/quarters) | Per test cycle |
| **Handles offline/brand** | No | Yes | Yes (if you can split exposure) |
| **Privacy-durable** | Weak (cookie/ID loss) | Strong (aggregate) | Strong (aggregate) |
| **Cost/effort** | Low–medium | High | Medium–high |

## MTA — multi-touch attribution

**What it is:** the user-level approach most marketers mean by "attribution" — join a person's touches, apply first/linear/position/data-driven credit.

**Where it shines:** day-to-day, tactical decisions. "Is this campaign showing up on converting journeys?" Fast, granular, cheap if your tracking exists.

**Why it's structurally weakening:** MTA depends on tracking one person across touches and devices, and that data keeps eroding — Safari/Firefox ITP-style cookie limits, iOS ATT, browser consent gating, ad blockers, and ordinary cross-device / in-app-browser behavior (research on mobile, buy on desktop). (Chrome's third-party-cookie deprecation was announced, then walked back, so "cookies are going away" is no longer the clean story — but everything else on that list already limits user-level tracking today.)

Click-based paths add a second bias: **impression channels (social, video, display) often never enter the journey** — a view with no click leaves no stitchable touch — so MTA systematically **over-weights demand-capture** (search, email, direct) and **under-weights demand-creation**. MTA doesn't announce the gap: it silently under-measures anything it can't follow (dumping it into direct) and over-measures what it *can* see. Treat MTA as **incomplete and directionally biased** — not a clean lower bound (its retargeting/branded numbers are often *over*-stated) — and never the sole basis for a big reallocation.

**Use it for:** ongoing optimization and trend-watching — never as the sole basis for a big budget reallocation.

## MMM — media/marketing mix modeling

**What it is:** a top-down statistical model (historically regression; modern open-source options like Meta's Robyn or Google's Meridian) that explains an outcome (revenue, signups) as a function of spend per channel plus controls (seasonality, promotions, price, macro). It never looks at individuals — it's all aggregate time-series, which is exactly why privacy changes don't touch it.

**What it uniquely gives you:**
- **Offline + brand + hard-to-track channels** — TV, podcasts, OOH, PR, organic — because it works on aggregate spend and outcomes, not clicks.
- **Diminishing returns / saturation curves** — where the next dollar in a channel stops paying off.
- **A portfolio view** — how the whole mix drives the outcome, not credit for one journey.

**What it costs and where it's weak:**
- Needs **2–3 years of weekly data** and **real variation in spend** — if you always spend the same on Meta, the model can't learn Meta's effect. You sometimes have to deliberately vary budgets to feed it.
- **Correlational and slow** — it sees what moved together historically; it reacts in quarters, not days. It can't tell you what to do with tomorrow's campaign.
- **Sensitive to specification** — garbage controls, garbage coefficients. It's a real modeling exercise, not a dashboard toggle.

**Use it for:** annual/quarterly budget allocation across a material, multi-channel (esp. offline-inclusive) spend. Validate its coefficients with incrementality tests — MMM says "Meta contributed X"; a holdout proves whether that's causal.

## Incrementality — the experiments

**What it is:** the only paradigm that measures *causality* directly. Split your audience into an **exposed** group and a **withheld/control** group; the difference in outcomes is the **incremental lift** — conversions you got *because of* the channel, not ones that would have happened anyway.

**Common designs:**
- **Geo holdout / geo-lift** — run the channel in some regions, hold it out of comparable ones; compare outcomes. The workhorse for channels you can't split at the user level. *(Meta's GeoLift, Google's geo experiments.)*
- **PSA tests** — the control group is shown a *public-service ad* in your ad's place, so both groups are equally targeted and "ad-exposed"; the only difference is whether they saw *your* ad. Isolates ad effect from audience-quality bias (the exposed group isn't just "people the algorithm judged likely to convert").
- **Ghost ads** — the platform runs the auction but **withholds your ad** from the control group and logs the impression that *would* have served; the control user may see another advertiser's ad (or organic inventory) instead of a PSA placeholder. You compare converters among would-have-been-exposed vs. actually-exposed. Cleaner and cheaper than PSAs (no wasted PSA spend), and the modern default where the platform supports it. (Logging would-have-served opportunities helps identify the relevant comparison set; it is separate from the intent-to-treat analysis principle.)
- **Intent-to-treat analysis** — compare outcomes by the groups participants were randomly assigned to, regardless of whether they actually saw an ad. It estimates the effect of assignment and preserves the randomized comparison; it is not a synonym for switching a channel off. See the [Cochrane explanation of assignment effects](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-08).
- **On-off (pulse) tests** — switch a channel off for a defined window and examine total outcomes. A simple before/after comparison can be confounded by seasonality, demand changes, and other campaigns. Use randomized regions or time blocks and an appropriate analysis when feasible; [Google's geo-experiment research](https://research.google.com/pubs/archive/38355.pdf) describes a controlled advertising design. Account for carryover and spillover before interpreting the change as causal.
- **Holdout audiences** — withhold a random % from a retargeting or email program; the delta is the program's true lift.

### How to *read* a test (not run the stats)

You don't need to compute significance by hand, but you must read a result honestly:

1. **Lift = exposed rate − control rate.** If exposed geos converted at 4.2% and control at 3.6%, incremental lift is ~0.6pp — the rest of that 4.2% would have converted anyway. This is why last-click ROAS is almost always *overstated*: it counts the whole 4.2%.
2. **Check the confidence interval.** "5% lift, interval −2% to +12%" includes zero and losses: you can't claim a win. Compare the interval to the smallest lift that changes your decision; if it straddles it, the test was too small to decide.
3. **Watch for contamination.** Control users who were reached anyway (cross-device, spillover between geos) shrink the measured gap. A "no lift" result can be a leaky test, not a dead channel.
4. **Translate to a decision.** Incremental CPA = spend ÷ *incremental* conversions (not total). This is the number that should drive budget — and it's usually worse than the platform's reported CPA, which is the point.

**Use it for:** the highest-stakes questions and the tiebreakers — "does retargeting actually do anything?", "is branded-search paid just buying clicks we'd get free?", "which of our two biggest channels is really driving growth?" You can only test a few things at a time, so spend those tests on the decisions that matter most.

## Putting them together (the mature stack)

They're layers, not competitors:

- **MTA** for daily/weekly tactical optimization and trend-watching — cheap, granular, directional.
- **MMM** for quarterly/annual portfolio allocation across the full mix including offline — durable, holistic. Prefer **marginal ROI / saturation curves** over average platform ROAS when allocating the next dollar.
- **Incrementality** as the **calibration and tiebreaker** — the ground-truth that keeps MTA and MMM honest, run on your biggest bets.

### Triangulated overrides (making MTA "closer to reality")

When incrementality, surveys, and platform gaps all say the same channel is under-credited in click-MTA, **don't invent a platform-gap multiplier**. Document a rule:

1. **Channel-level override (reporting layer):** after MTA runs, shift a bounded share of conversions from Direct / branded search into the under-credited channel for the window you have evidence for (holdout dates, campaign flight). Keep the raw MTA table intact; decision dashboards read the adjusted table. Fast to ship; channel-level only.
2. **User-level insertion (advanced):** before MTA runs, add synthetic touchpoints (e.g. "YouTube impression") onto a subset of Direct journeys where survey match, geo-test membership, or platform exposure logs justify it — then re-score. Needs engineering; unlocks creative/audience granularity.

Start with one channel, one override, temporal bounds, and a conservative slice of measured lift (not 100% of a noisy point estimate). Expand only after stakeholders trust the first rule.

**Scale to the user:** most SMBs need good UTMs + last-non-direct + a self-reported survey + the occasional on/off test — not an MMM. Bring MMM in when offline/brand spend is material and MTA visibly can't see it. Bring in formal incrementality when a single channel's budget is big enough that being wrong about it is expensive. Match the rigor to the size of the decision.
