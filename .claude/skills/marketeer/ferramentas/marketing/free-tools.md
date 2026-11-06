# free-tools

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/free-tools

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or brand awareness. Also use when the user mentions "engineering as marketing," "free tool," "marketing tool," "calculator," "generator," "interactive tool," "lead gen tool," "build a tool for leads," "free resource," "ROI calculator," "grader tool," "audit tool," "should I build a free tool," or "tools for lead gen." Use this whenever someone wants to build something useful and give it away to attract leads or earn links. For downloadable content lead magnets (ebooks, checklists, templates), see lead-magnets.


# Free Tool Strategy (Engineering as Marketing)

You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before designing a tool strategy, understand:

1. **Business Context** - What's the core product? Who is the target audience? What problems do they have?

2. **Goals** - Lead generation? SEO/traffic? Brand awareness? Product education?

3. **Resources** - Technical capacity to build? Ongoing maintenance bandwidth? Budget for promotion?

---

## Core Principles

**"Your product is my marketing opportunity."** Bezos said "your margin is my opportunity." The engineering-as-marketing version: take a capability others monetize and build a free version as an acquisition channel. Unsplash gave away the stock photos Getty sold — and Getty acquired it. See [references/tool-benchmarks.md](references/tool-benchmarks.md) for sourced cases and measurement limits.

### 1. Solve a Real Problem
- Tool must provide genuine value
- Solves a problem your audience actually has
- Useful even without your main product

### 2. Adjacent to Core Product
- Related to what you sell
- Natural path from tool to product
- Educates on problem you solve

### 3. Simple and Focused
- Does one thing well
- Low friction to use
- Immediate value

### 4. Worth the Investment
- Lead value × expected leads > build cost + maintenance

---

## Tool Types Overview

| Type | Examples | Best For |
|------|----------|----------|
| Calculators | ROI, savings, pricing estimators | Decisions involving numbers |
| Generators | Templates, policies, names | Creating something quickly |
| Analyzers | Website graders, SEO auditors | Evaluating existing work |
| Testers | Meta tag preview, speed tests | Checking if something works |
| Libraries | Icon sets, templates, snippets | Reference material |
| Interactive | Tutorials, playgrounds, quizzes | Learning/understanding |

**For detailed tool types and examples**: See [references/tool-types.md](references/tool-types.md)

**For sourced case examples (Unsplash, HubSpot Website Grader, Buffer, Shopify) and evidence requirements**: See [references/tool-benchmarks.md](references/tool-benchmarks.md)

---

## Ideation Framework

### Start with Pain Points

1. **What problems does your audience Google?** - Search query research, common questions

2. **What manual processes are tedious?** - Spreadsheet tasks, repetitive calculations

3. **What do they need before buying your product?** - Assessments, planning, comparisons

4. **What information do they wish they had?** - Data they can't easily access, benchmarks

### Validate the Idea

- **Search demand**: Is there search volume? How competitive?
- **Uniqueness**: What exists? How can you be 10x better?
- **Lead quality**: Does this audience match buyers?
- **Build feasibility**: How complex? Can you scope an MVP?

---

## Lead Capture Strategy

### Gating Options

| Approach | Pros | Cons |
|----------|------|------|
| Fully gated | Maximum capture | Lower usage |
| Partially gated | Balance of both | Common pattern |
| Ungated + optional | Maximum reach | Lower capture |
| Ungated entirely | Pure SEO/brand | No direct leads |

### Lead Capture Best Practices
- Value exchange clear: "Get your full report"
- Minimal friction: Email only
- Show preview of what they'll get
- Optional: Segment by asking one qualifying question

---

## SEO Considerations

### Keyword Strategy
**Tool landing page**: "[thing] calculator", "[thing] generator", "free [tool type]"

**Supporting content**: "How to [use case]", "What is [concept]"

### Link Building
Free tools attract links because:
- Genuinely useful (people reference them)
- Unique (can't link to just any page)
- Shareable (social amplification)

---

## Build vs. Buy

### Build Custom
When: Unique concept, core to brand, high strategic value, have dev capacity

### Use No-Code Tools
Options: Outgrow, Involve.me, Typeform, Tally, Bubble, Webflow
When: Speed to market, limited dev resources, testing concept

### Embed Existing
When: Something good exists, white-label available, not core differentiator

---

## MVP Scope

### Minimum Viable Tool
1. Core functionality only—does the one thing, works reliably
2. Essential UX—clear input, obvious output, mobile works
3. Basic lead capture—email collection, leads go somewhere useful

### What to Skip Initially
Account creation, saving results, advanced features, perfect design, every edge case

---

## Evaluation Scorecard

Rate each factor 1-5:

| Factor | Score |
|--------|-------|
| Search demand exists | ___ |
| Audience match to buyers | ___ |
| Uniqueness vs. existing | ___ |
| Natural path to product | ___ |
| Build feasibility | ___ |
| Maintenance burden (inverse) | ___ |
| Link-building potential | ___ |
| Share-worthiness | ___ |

**25+**: Strong candidate | **15-24**: Promising | **<15**: Reconsider

---

## Task-Specific Questions

1. What existing tools does your audience use for workarounds?
2. How do you currently generate leads?
3. What technical resources are available?
4. What's the timeline and budget?

---

## Common Pitfalls

- **Over-engineering** — Shipping a bloated tool before validating demand. Unsplash started as a Tumblr blog with Dropbox links, then invested in a custom site after demand emerged. Scope to one useful job and test it with your audience.
- **Poor product integration** — A tool with no natural path to your product earns traffic but not pipeline. The best cases surface the product's value (an analyzer can demonstrate the problem your paid product solves).
- **Maintenance / security debt** — Tools that scrape, call APIs, or take user input rot and become attack surfaces. Budget for upkeep before you build.
- **Vanity metrics** — Visitors and usage feel good but don't pay. Track leads, qualification rate, and trial/signup conversion — measured in your own funnel.

## Related Skills

- **lead-magnets**: For downloadable content lead magnets (ebooks, checklists, templates)
- **cro**: For optimizing the tool's landing page
- **seo-audit**: For SEO-optimizing the tool
- **link-building**: For promoting the tool to sites that link to resources like it
- **analytics**: For measuring tool usage
- **emails**: For nurturing leads from the tool



---

## `references/tool-benchmarks.md`

# Free Tool Case Examples

Use these sourced examples to study product design and distribution. They are not transferable conversion benchmarks: a tool's existence or later acquisition does not establish its visitor-to-lead rate, CAC, or incremental revenue.

## Framing: "Your product is my marketing opportunity"

Give away a useful capability that others sell, and test whether it attracts the audience for your product. [Unsplash's founder describes](https://unsplash.com/blog/hello-unsplash-inc/) launching a Tumblr blog with Dropbox links: 20,000 people signed up on day one, and a few months later it had 80,000 members and over one million downloads. Selecting ten featured photos every ten days took about an hour; the post does not give a build time. [Unsplash later announced its acquisition by Getty Images](https://unsplash.com/blog/unsplash-getty/). These are historical facts, not a promise of similar acquisition outcomes.

## Case Library

| Tool | Company | What the primary source establishes | Design lesson to test |
|------|---------|-------------------------------------|-----------------------|
| Unsplash | Crew | Founder account: 20,000 day-one signups, 80,000 members and 1M+ downloads after a few months; later Getty acquisition | A useful byproduct can become a resource library |
| [Website Grader](https://blog.hubspot.com/marketing/website-grader) | HubSpot | A free website assessment tool | An analyzer can demonstrate expertise before a sales conversation |
| [SaaS business calculators](https://changelog.baremetrics.com/saas-business-calculators-25uoes) | Baremetrics | A free calculator suite including startup runway | Solve a calculation adjacent to your paid product |
| [Headline Analyzer](https://coschedule.com/headline-analyzer) | CoSchedule | A free headline analysis entry point | Repeatable feedback can introduce a broader product |
| [Salary Calculator](https://buffer.com/resources/transparent-salaries/) | Buffer | A public calculator based on Buffer's salary formula | A shareable resource can communicate company values |
| [Logo Maker](https://www.shopify.com/tools/logo-maker) | Shopify | A free logo creation tool | Solve a task prospective merchants face while starting a business |

The sources above do not establish comparable trial-conversion or signup rates. Do not quote the former unsourced rates as benchmarks. If you add a quantitative case, attach its primary source, reporting date, cohort, numerator and denominator, funnel stage, and attribution limits. Distinguish visitors, leads, trials, paying customers, and incremental outcomes.

## What each case teaches

- **Crew → Unsplash** — A small photo library can attract an audience before a custom platform is needed. The founder describes starting with Tumblr and Dropbox links, then investing in a standalone site after demand emerged. Give away something useful and validate demand before expanding.
- **HubSpot Website Grader** — An analyzer can demonstrate expertise and introduce a sales conversation; its inputs can help identify customer fit. Measure qualification in your own funnel rather than borrowing an unsupported rate.
- **Baremetrics Forecasting** — A calculation adjacent to revenue analytics can make the paid product's value easier to understand. Test whether that connection helps prospective customers.
- **CoSchedule Headline Analyzer** — Repeat-use feedback can keep the brand in front of an audience and introduce a broader product. Measure repeat use and downstream customer contribution.
- **[Moz Keyword Explorer](https://moz.com/products/pro/pricing)** — Moz describes limited Keyword Explorer access through its free Community account. A limited free surface of a paid product can work as its demonstration. Test that path without assuming a trial-conversion rate or CAC reduction.
- **Buffer Salary Calculator** — A shareable resource can express company values even when it is not adjacent to the paid product. Distinguish reach from qualified customer demand.
- **Shopify Hatchful** — A logo generator solves a task prospective merchants face during onboarding. Test whether that helpful entry point carries into product adoption.

## How to use these examples

- **Pattern-match**: Borrow a useful mechanism, such as grading, calculating, or generating. Treat the proposed effect on your funnel as a hypothesis.
- **Forecast explicitly**: Use your own baseline or label low/base/high conversion assumptions. Do not substitute another company's traffic or lifetime revenue for your expected outcome.
- **Justify the build**: Compare expected qualified-customer contribution against build, distribution, and ongoing maintenance costs. Track tool use → qualified lead → customer by cohort, then test incremental contribution where feasible.



---

## `references/tool-types.md`

# Free Tool Types Reference

Detailed guide to each type of marketing tool you can build.

## Contents
- Calculators
- Generators
- Analyzers/Auditors
- Testers/Validators
- Libraries/Resources
- Interactive Educational
- Tool Concept Examples by Industry (SaaS product, agency/services, e-commerce, developer tools, finance)

## Calculators

**Best for**: Decisions involving numbers, comparisons, estimates

**Examples**:
- ROI calculator
- Savings calculator
- Cost comparison tool
- Salary calculator
- Tax estimator
- Pricing estimator
- Compound interest calculator
- Break-even calculator

**Why they work**:
- Personalized output
- High perceived value
- Share-worthy results
- Clear problem → solution

**Implementation tips**:
- Keep inputs simple
- Show calculations transparently
- Make results shareable
- Add "powered by" branding

---

## Generators

**Best for**: Creating something useful quickly

**Examples**:
- Policy generator (privacy, terms)
- Template generator
- Name/tagline generator
- Email subject line generator
- Resume builder
- Color palette generator
- Logo maker
- Contract generator

**Why they work**:
- Tangible output
- Saves time
- Easily shared
- Repeat usage

**Implementation tips**:
- Output should be immediately usable
- Allow customization
- Offer download/export options
- Include email gating for premium outputs

---

## Analyzers/Auditors

**Best for**: Evaluating existing work or assets

**Examples**:
- Website grader
- SEO analyzer
- Email subject tester
- Headline analyzer
- Security checker
- Performance auditor
- Accessibility checker
- Code quality analyzer

**Why they work**:
- Curiosity-driven
- Personalized insights
- Creates awareness of problems
- Natural lead to solution

**Implementation tips**:
- Score or grade for gamification
- Benchmark against averages
- Provide actionable recommendations
- Follow up with improvement offers

---

## Testers/Validators

**Best for**: Checking if something works

**Examples**:
- Meta tag preview
- Email rendering test
- Mobile-friendly test
- Speed test
- DNS checker
- SSL certificate checker
- Redirect checker
- Broken link finder

**Why they work**:
- Immediate utility
- Bookmark-worthy
- Repeat usage
- Professional necessity

**Implementation tips**:
- Fast results are essential
- Show pass/fail clearly
- Provide fix instructions
- Integrate with your product where relevant

---

## Libraries/Resources

**Best for**: Reference material

**Examples**:
- Icon library
- Template library
- Code snippet library
- Example gallery
- Industry directory
- Resource list
- Swipe file collection
- Font pairing tool

**Why they work**:
- High SEO value
- Ongoing traffic
- Establishes authority
- Linkable asset

**Implementation tips**:
- Make searchable/filterable
- Allow easy copying/downloading
- Update regularly
- Accept community submissions

---

## Interactive Educational

**Best for**: Learning/understanding

**Examples**:
- Interactive tutorials
- Code playgrounds
- Visual explainers
- Quizzes/assessments
- Simulators
- Comparison tools
- Decision trees
- Configurators

**Why they work**:
- Engages deeply
- Demonstrates expertise
- Shareable
- Memory-creating

**Implementation tips**:
- Make it hands-on
- Show immediate feedback
- Lead to deeper resources
- Capture engaged users

---

## Tool Concept Examples by Industry

### SaaS Product
- Product ROI calculator
- Competitor comparison tool
- Readiness assessment quiz
- Template library for use case
- Feature configurator

### Agency/Services
- Industry benchmark tool
- Project scoping calculator
- Portfolio review tool
- Cost estimator
- Proposal generator

### E-commerce
- Product finder quiz
- Comparison tool
- Size/fit calculator
- Savings calculator
- Gift finder

### Developer Tools
- Code snippet library
- Testing/preview tool
- Documentation generator
- Interactive tutorials
- API playground

### Finance
- Financial calculators
- Investment comparison
- Budget planner
- Tax estimator
- Loan calculator
