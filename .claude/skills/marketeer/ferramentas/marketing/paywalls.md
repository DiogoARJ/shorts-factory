# paywalls

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/paywalls

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use when the user mentions "paywall," "upgrade screen," "upgrade modal," "upsell," "feature gate," "convert free to paid," "freemium conversion," "trial expiration screen," "limit reached screen," "plan upgrade prompt," "in-app pricing," "free users won't upgrade," "trial to paid conversion," or "how do I get users to pay," "mobile app paywall," "subscription app paywall," or "App Store subscription pricing." Use this for any in-product moment where you're asking users to upgrade. Distinct from public pricing pages (see cro) — this focuses on in-product upgrade moments where the user has already experienced value. For pricing decisions, see pricing.


# Paywall and Upgrade Screen CRO

You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at moments when they've experienced enough value to justify the commitment.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before providing recommendations, understand:

1. **Upgrade Context** - Freemium → Paid? Trial → Paid? Tier upgrade? Feature upsell? Usage limit?

2. **Product Model** - What's free? What's behind paywall? What triggers prompts? Current conversion rate?

3. **User Journey** - When does this appear? What have they experienced? What are they trying to do?

---

## Core Principles

### 1. Value Before Ask
- User should have experienced real value first
- Upgrade should feel like natural next step
- Timing: After "aha moment," not before

### 2. Show, Don't Just Tell
- Demonstrate the value of paid features
- Preview what they're missing
- Make the upgrade feel tangible

### 3. Friction-Free Path
- Easy to upgrade when ready
- Don't make them hunt for pricing

### 4. Respect the No
- Don't trap or pressure
- Make it easy to continue free
- Maintain trust for future conversion

---

## Paywall Trigger Points

### Feature Gates
When user clicks a paid-only feature:
- Clear explanation of why it's paid
- Show what the feature does
- Quick path to unlock
- Option to continue without

### Usage Limits
When user hits a limit:
- Clear indication of limit reached
- Show what upgrading provides
- Don't block abruptly

### Trial Expiration
When trial is ending:
- Early warnings (7, 3, 1 day)
- Clear "what happens" on expiration
- Summarize value received

### Time-Based Prompts
After X days of free use:
- Gentle upgrade reminder
- Highlight unused paid features
- Easy to dismiss

---

## Paywall Screen Components

1. **Headline** - Focus on what they get: "Unlock [Feature] to [Benefit]"

2. **Value Demonstration** - Preview, before/after, "With Pro you could..."

3. **Feature Comparison** - Highlight key differences, current plan marked

4. **Pricing** - Clear, simple, annual vs. monthly options

5. **Social Proof** - Customer quotes, "X teams use this"

6. **CTA** - Specific and value-oriented: "Start Getting [Benefit]"

7. **Escape Hatch** - Clear "Not now" or "Continue with Free"

---

## Specific Paywall Types

### Feature Lock Paywall
```
[Lock Icon]
This feature is available on Pro

[Feature preview/screenshot]

[Feature name] helps you [benefit]:
• [Capability]
• [Capability]

[Upgrade to Pro - $X/mo]
[Maybe Later]
```

### Usage Limit Paywall
```
You've reached your free limit

[Progress bar at 100%]

Free: 3 projects | Pro: Unlimited

[Upgrade to Pro]  [Delete a project]
```

### Trial Expiration Paywall
```
Your trial ends in 3 days

What you'll lose:
• [Feature used]
• [Data created]

What you've accomplished:
• Created X projects

[Continue with Pro]
[Remind me later]  [Downgrade]
```

---

## Timing and Frequency

### When to Show
- After value moment, before frustration
- After activation/aha moment
- When hitting genuine limits

### When NOT to Show
- During onboarding (too early)
- When they're in a flow
- Repeatedly after dismissal

### Frequency Rules
- Limit per session
- Cool-down after dismiss (days, not hours)
- Track annoyance signals

---

## Upgrade Flow Optimization

### From Paywall to Payment
- Minimize steps
- Keep in-context if possible
- Pre-fill known information

### Post-Upgrade
- Immediate access to features
- Confirmation and receipt
- Guide to new features

---

## A/B Testing

### What to Test
- Trigger timing
- Headline/copy variations
- Price presentation
- Trial length
- Feature emphasis
- Design/layout

### Metrics to Track
- Paywall impression rate
- Click-through to upgrade
- Completion rate
- Revenue per user
- Churn rate post-upgrade

**For comprehensive experiment ideas**: See [references/experiments.md](references/experiments.md)

**For consumer iOS/Android subscription apps** (paywall inside onboarding, yearly-first plans, trials and reminders, store fees, web checkout, revenue per download): See [references/mobile-subscription-paywalls.md](references/mobile-subscription-paywalls.md)

---

## Anti-Patterns to Avoid

### Dark Patterns
- Hiding the close button
- Confusing plan selection
- Guilt-trip copy
- Fake countdowns or "limited" offers with no real deadline

### Conversion Killers
- Asking before value delivered
- Too frequent prompts
- Blocking critical flows
- Complicated upgrade process

---

## Task-Specific Questions

1. What's your current free → paid conversion rate?
2. What triggers upgrade prompts today?
3. What features are behind the paywall?
4. What's your "aha moment" for users?
5. What pricing model? (per seat, usage, flat)
6. Mobile app, web app, or both?

---

## Related Skills

- **churn-prevention**: For cancel flows, save offers, and reducing churn post-upgrade
- **cro**: For public pricing page optimization
- **onboarding**: For driving to aha moment before upgrade
- **ab-testing**: For testing paywall variations



---

## `references/experiments.md`

# Paywall Experiment Ideas

Comprehensive list of A/B tests and experiments for paywall optimization.

## Contents
- Trigger & Timing Experiments (When to Show, Trigger Type)
- Paywall Design Experiments (Layout & Format, Value Presentation, Visual Elements)
- Pricing Presentation Experiments (Price Display, Plan Options, Discounts & Offers)
- Copy & Messaging Experiments (Headlines, CTAs, Objection Handling)
- Trial & Conversion Experiments (Trial Structure, Trial Expiration, Upgrade Path)
- Personalization Experiments (Usage-Based, Segment-Specific)
- Frequency & UX Experiments (Frequency Capping, Dismiss Behavior)

## Trigger & Timing Experiments

### When to Show
- Test trigger timing: after aha moment vs. at feature attempt
- Early trial reminder (7 days) vs. late reminder (1 day before)
- Show after X actions completed vs. after X days
- Test soft prompts at different engagement thresholds
- Trigger based on usage patterns vs. time-based only

### Trigger Type
- Hard gate (can't proceed) vs. soft gate (preview + prompt)
- Feature lock vs. usage limit as primary trigger
- In-context modal vs. dedicated upgrade page
- Banner reminder vs. modal prompt
- Exit-intent on free plan pages

---

## Paywall Design Experiments

### Layout & Format
- Full-screen paywall vs. modal overlay
- Minimal paywall (CTA-focused) vs. feature-rich paywall
- Single plan display vs. plan comparison
- Image/preview included vs. text-only
- Vertical layout vs. horizontal layout on desktop

### Value Presentation
- Feature list vs. benefit statements
- Show what they'll lose (loss aversion) vs. what they'll gain
- Personalized value summary based on usage
- Before/after demonstration
- ROI calculator or value quantification

### Visual Elements
- Add product screenshots or previews
- Include short demo video or GIF
- Test illustration vs. product imagery
- Animated vs. static paywall
- Progress visualization (what they've accomplished)

---

## Pricing Presentation Experiments

### Price Display
- Show monthly vs. annual vs. both with toggle
- Highlight savings for annual ($ amount vs. % off)
- Price per day framing ("Less than a coffee")
- Show price after trial vs. emphasize "Start Free"
- Display price prominently vs. de-emphasize until click

### Plan Options
- Single recommended plan vs. multiple tiers
- Add "Most Popular" badge to target plan
- Test number of visible plans (2 vs. 3)
- Show enterprise/custom tier vs. hide it
- Include one-time purchase option alongside subscription

### Discounts & Offers

Test discounts where they reward commitment or a real moment, not as a standing price cut for new buyers (see the `offers` skill on why acquisition discounts backfire). Any countdown must reflect a real deadline.

- Annual-plan pricing presentation (the commitment discount, shown per month vs. billed amount)
- Time-bound offer tied to a real window (seasonal sale, trial end) vs. no offer
- Loyalty discount based on free usage duration
- Upgrade discount for existing paid users moving up a tier
- Referral discount for social proof
- Risk reversal (guarantee, extended trial) vs. discount

---

## Copy & Messaging Experiments

### Headlines
- Benefit-focused ("Unlock unlimited projects") vs. feature-focused ("Get Pro features")
- Question format ("Ready to do more?") vs. statement format
- Urgency-based ("Don't lose your work") vs. value-based
- Personalized headline with user's name or usage data
- Social proof headline ("Join 10,000+ Pro users")

### CTAs
- "Start Free Trial" vs. "Upgrade Now" vs. "Continue with Pro"
- First person ("Start My Trial") vs. second person ("Start Your Trial")
- Value-specific ("Unlock Unlimited") vs. generic ("Upgrade")
- Add urgency ("Upgrade Today") vs. no pressure
- Include price in CTA vs. separate price display

### Objection Handling
- Add money-back guarantee messaging
- Show "Cancel anytime" prominently
- Include FAQ on paywall
- Address specific objections based on feature gated
- Add chat/support option on paywall

---

## Trial & Conversion Experiments

### Trial Structure
- 7-day vs. 14-day vs. 30-day trial length
- Credit card required vs. not required for trial
- Full-access trial vs. limited feature trial
- Trial extension offer for engaged users
- Second trial offer for expired/churned users

### Trial Expiration
- Countdown timer visibility (always vs. near end)
- Email reminders: frequency and timing
- Grace period after expiration vs. immediate downgrade
- "Last chance" offer with discount
- Pause option vs. immediate cancellation

### Upgrade Path
- One-click upgrade from paywall vs. separate checkout
- Pre-filled payment info for returning users
- Multiple payment methods offered
- Quarterly plan option alongside monthly/annual
- Team invite flow for solo-to-team conversion

---

## Personalization Experiments

### Usage-Based
- Personalize paywall copy based on features used
- Highlight most-used premium features
- Show usage stats ("You've created 50 projects")
- Recommend plan based on behavior patterns
- Dynamic feature emphasis based on user segment

### Segment-Specific
- Different paywall for power users vs. casual users
- B2B vs. B2C messaging variations
- Industry-specific value propositions
- Role-based feature highlighting
- Traffic source-based messaging

---

## Frequency & UX Experiments

### Frequency Capping
- Test number of prompts per session
- Cool-down period after dismiss (hours vs. days)
- Escalating urgency over time vs. consistent messaging
- Once per feature vs. consolidated prompts
- Re-show rules after major engagement

### Dismiss Behavior
- "Maybe later" vs. "No thanks" vs. "Remind me tomorrow"
- Ask reason for declining
- Offer alternative (lower tier, annual discount)
- Exit survey on dismiss
- Friendly vs. neutral decline copy



---

## `references/mobile-subscription-paywalls.md`

# Mobile Subscription App Paywalls

Consumer iOS and Android subscription apps (fitness, learning, focus, faith, scanners) run on different paywall mechanics from SaaS upgrade screens. Billing goes through the app stores, the paywall usually sits inside onboarding, and most revenue comes from a yearly plan sold on day one. Use this reference for those apps; the rest of the skill still applies to the copy, design, and testing.

## Contents

- Placement: after the first personalized result
- Hard paywall vs. freemium
- Plan presentation
- Trials
- One abandon offer
- Store fees and web checkout
- Unit economics per download
- App Store review checklist

## Placement: after the first personalized result

The common pattern is **onboarding → personalized result → paywall**. Onboarding asks a few questions about the user's goal, the app shows something built for them (a plan, a score, a first analysis), and the paywall follows while that result is on screen. The result is the value moment the paywall leans on; a paywall on first launch, before anything personal has happened, asks for money with nothing to point at.

## Hard paywall vs. freemium

A hard paywall (no core use without a trial or purchase) and freemium (a capped free tier) are both legitimate. RevenueCat's State of Subscription Apps 2026 found hard-paywall apps converting roughly five times as many users to paid in the first 35 days as freemium apps, while one-year retention of yearly subscribers was about the same for both (27% vs. 28%). Freemium still fits when the free tier drives sharing or word of mouth. If you keep a free tier, cap it daily so the limit is felt in the habit, not after a month.

## Plan presentation

1. **Lead with the yearly plan**, with the per-week or per-month equivalent as supporting text ("$0.58/week, billed $29.99 yearly"). The billed amount and period must stay clear; the breakdown is framing, not a replacement.
2. **Offer at most one shorter option** (weekly or monthly) as the comparison.
3. **Localize prices by storefront** rather than converting one price.
4. **Test price, plan mix, trial length, and design** remotely so changes don't need an app release. Paywall platforms such as Superwall, RevenueCat Paywalls, and Adapty do this; pick on fit with your stack.

## Trials

- **Offer a free trial on the yearly plan** and schedule a reminder before it ends. Surprise renewals drive refunds, one-star reviews, and chargebacks.
- **Trial length is a test, not a default.** RevenueCat's 2026 data shows longer trials (17+ days) converting at a higher median rate than trials of four days or less, at the cost of waiting longer for revenue. Short trials suit apps where value lands in a day or two; longer trials suit habits that take a week to form.

## One abandon offer

When someone closes the paywall without starting a trial, one discounted yearly offer is a standard move. Show it **once**, not on every close, and keep it consistent with the rules in the main skill (respect the no, no fake countdowns).

## Store fees and web checkout

Fees change and differ by country, so treat these as a snapshot (October 2026) and check current terms before modeling:

- **Apple:** subscriptions pay 15% for members of the App Store Small Business Program (under $1M in annual proceeds). Otherwise 30% in a subscriber's first year and 15% after.
- **Google Play (US, UK, EEA, from June 30, 2026):** a 10% service fee on subscriptions plus a 5% billing fee when Google Play's billing is used, so 15% in practice. The 10% service fee also applies when users pay through an alternative biller or a web link; only the billing fee drops away. Other markets follow on later dates.
- **US iOS link-outs to web checkout** are allowed, and Apple's commission on them is still being set in court. Model the web path at a range of possible rates rather than at zero.

**Web-to-app funnel:** ad → web onboarding quiz → web paywall → download link. It moves payment off the store and lets you test onboarding without app releases, but it adds a step between the ad and the app. Check each storefront's link-out rules before building it.

## Unit economics per download

```
revenue per download = trial start rate × trial-to-paid rate × yearly price × (1 − store fee)
```

One founder's working estimate is 30% of downloads starting a trial and 30% of trials paying about $30 a year, which comes to about $2.70 per download before fees. Treat that as a starting assumption to replace with your own numbers within a few weeks of launch, not a benchmark. Revenue per download is what tells you how much you can pay per install on ads or creators.

## App Store review checklist

- [ ] Price, billing period, trial length, and "auto-renews until cancelled" shown on the paywall
- [ ] Links to Terms of Use (EULA) and Privacy Policy
- [ ] Restore Purchases
- [ ] A visible close button, no dark patterns
- [ ] Trial-ending reminder scheduled
- [ ] `paywall_viewed`, `trial_started`, and `subscription_started` events fire with the paywall variant ID

---

*Patterns adapted from Blake Anderson's ai-app-playbook (MIT, October 2026); conversion and trial-length data from RevenueCat's State of Subscription Apps 2026; fees from Google's Android Developers Blog (June 2026), Apple's Small Business Program terms, and coverage of the Epic v. Apple link-out proceedings.*
