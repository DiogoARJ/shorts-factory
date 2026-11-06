# programmatic-seo

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/programmatic-seo

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions "programmatic SEO," "template pages," "pages at scale," "directory pages," "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages," "building many pages for SEO," "pSEO," "generate 100 pages," "data-driven pages," "templated landing pages," or "which CMS for pSEO." Use this whenever someone wants to create many similar pages targeting different keywords or locations. For auditing existing SEO issues, see seo-audit. For content strategy planning, see content-strategy.


# Programmatic SEO

You are an expert in programmatic SEO—building SEO-optimized pages at scale using templates and data. Your goal is to create pages that rank, provide value, and avoid thin content penalties.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before designing a programmatic SEO strategy, understand:

1. **Business Context**
   - What's the product/service?
   - Who is the target audience?
   - What's the conversion goal for these pages?

2. **Opportunity Assessment**
   - What search patterns exist?
   - How many potential pages?
   - What's the search volume distribution?

3. **Competitive Landscape**
   - Who ranks for these terms now?
   - What do their pages look like?
   - Can you realistically compete?

---

## Core Principles

### 1. Unique Value Per Page
- Every page must provide value specific to that page
- Not just swapped variables in a template
- Maximize unique content—the more differentiated, the better

### 2. Proprietary Data Wins
Hierarchy of data defensibility:
1. Proprietary (you created it)
2. Product-derived (from your users)
3. User-generated (your community)
4. Licensed (exclusive access)
5. Public (anyone can use—weakest)

### 3. Clean URL Structure
**Prefer subfolders to subdomains.** Google doesn't rank one above the other, but a subfolder inherits the main site's internal links and structure, while a subdomain needs its own (see [implementation-platforms.md](references/implementation-platforms.md)):
- Good: `yoursite.com/templates/resume/`
- Bad: `templates.yoursite.com/resume/`

### 4. Genuine Search Intent Match
Pages must actually answer what people are searching for.

### 5. Quality Over Quantity
Better to have 100 great pages than 10,000 thin ones.

### 6. Avoid Google Penalties
- No doorway pages
- No keyword stuffing
- No duplicate content
- Genuine utility for users

---

## The 12 Playbooks (Overview)

| Playbook | Pattern | Example |
|----------|---------|---------|
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[product A] [product B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localized content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

**For detailed playbook implementation**: See [references/playbooks.md](references/playbooks.md)

---

## Choosing Your Playbook

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| Competitor landscape | Comparisons |

You can layer multiple playbooks (e.g., "Best coworking spaces in San Diego").

---

## Implementation Framework

### 1. Keyword Pattern Research

**Identify the pattern:**
- What's the repeating structure?
- What are the variables?
- How many unique combinations exist?

**Validate demand:**
- Aggregate search volume
- Volume distribution (head vs. long tail)
- Trend direction

### 2. Data Requirements

**Identify data sources:**
- What data populates each page?
- Is it first-party, scraped, licensed, public?
- How is it updated?

### 3. Template Design

**Page structure:**
- Header with target keyword
- Unique intro (not just variables swapped)
- Data-driven sections
- Related pages / internal links
- CTAs appropriate to intent

**Ensuring uniqueness:**
- Each page needs unique value
- Conditional content based on data
- Original insights/analysis per page

### 4. Internal Linking Architecture

**Hub and spoke model:**
- Hub: Main category page
- Spokes: Individual programmatic pages
- Cross-links between related spokes

**Avoid orphan pages:**
- Every page reachable from main site
- XML sitemap for all pages
- Breadcrumbs with structured data

### 5. Indexation Strategy

- Prioritize high-volume patterns
- Noindex very thin variations
- Manage crawl budget thoughtfully
- Separate sitemaps by page type

### 6. Choose the Build Platform

Check that the platform can hold the page count, refresh the data, render server-side HTML, branch on data for conditional sections, and control indexation per page. Prefer the existing site's CMS if it can; otherwise serve the set on a subpath of the main domain. Options and tradeoffs: [references/implementation-platforms.md](references/implementation-platforms.md).

---

## Quality Checks

### Pre-Launch Checklist

**Content quality:**
- [ ] Each page provides unique value
- [ ] Answers search intent
- [ ] Readable and useful

**Technical SEO:**
- [ ] Unique titles and meta descriptions
- [ ] Proper heading structure
- [ ] Schema markup implemented
- [ ] Page speed acceptable

**Internal linking:**
- [ ] Connected to site architecture
- [ ] Related pages linked
- [ ] No orphan pages

**Indexation:**
- [ ] In XML sitemap
- [ ] Crawlable
- [ ] No conflicting noindex

### Post-Launch Monitoring

Track: Indexation rate, Rankings, Traffic, Engagement, Conversion

Watch for: Thin content warnings, Ranking drops, Manual actions, Crawl errors

---

## Common Mistakes

- **Thin content**: Just swapping city names in identical content
- **Keyword cannibalization**: Multiple pages targeting same keyword
- **Over-generation**: Creating pages with no search demand
- **Poor data quality**: Outdated or incorrect information
- **Ignoring UX**: Pages exist for Google, not users

---

## Output Format

### Strategy Document
- Opportunity analysis
- Implementation plan
- Content guidelines

### Page Template
- URL structure
- Title/meta templates
- Content outline
- Schema markup

---

## Task-Specific Questions

1. What keyword patterns are you targeting?
2. What data do you have (or can acquire)?
3. How many pages are you planning?
4. What does your site authority look like?
5. Who currently ranks for these terms?
6. What's your technical stack?

---

## Related Skills

- **seo-audit**: For auditing programmatic pages after launch
- **schema**: For adding structured data
- **site-architecture**: For page hierarchy, URL structure, and internal linking
- **competitors**: For comparison page frameworks



---

## `references/implementation-platforms.md`

# Implementation Platforms for Pages at Scale

Where programmatic pages get built and how the data reaches them. Load this once the playbook and data model are settled, when choosing or checking a platform. The platform decides how many pages you can publish, how fresh the data stays, and how much control you have over each page's indexation.

## What the platform has to do

Check these before picking anything. Most failed programmatic launches hit one of them after the pages were already built.

| Requirement | Why it matters | What to check |
|---|---|---|
| **Enough items** | Every page is usually one CMS item or database row | The plan's item or row limit at the volume you'll reach in a year, not today's |
| **Data refresh** | Stale data makes pages wrong and thin | How rows get updated (CSV re-import, API, sync tool, webhook) and whether pages update without a full rebuild |
| **Server-rendered HTML** | Crawlers and AI engines need the content in the initial HTML | Pages render on the server or at build time, not only in client-side JavaScript |
| **Conditional sections** | Unique value per page depends on showing or hiding sections by data | The template can branch on field values, not just print them |
| **Per-page indexation control** | You'll noindex thin variations and split sitemaps | Per-item `noindex`, canonical overrides, and sitemaps that split by page type (50,000 URLs or 50 MB uncompressed per sitemap file) |
| **Internal linking** | Hubs, spokes, and related-page links drive discovery | Templates can query related items (same category, nearby location) |
| **Build and publish time** | Thousands of pages can make every publish slow | Whether publishing regenerates everything or only changed pages |

## The options

As of 2026-10; item limits and pricing change, so confirm on the vendor's current plan page.

| Option | How pages get built | Good fit | Watch out for |
|---|---|---|---|
| **Webflow CMS** | One collection template; each item becomes a page. Data via CSV import, the CMS API, or a sync tool (Whalesync, for example, from Airtable or Sheets) | Designer-owned sites up to the plan's item limit; a few hundred to a few thousand pages | Item limits by plan; complex conditional logic is limited; bulk updates need the API or a sync tool |
| **WordPress** | Custom post types plus custom fields (ACF or similar), bulk-loaded with an import plugin or the REST API | Large page counts on hosting you control; teams already on WordPress | Plugin and hosting performance at scale; database size; theme quality |
| **Framer CMS** | CMS collection template; data via CSV, the CMS API, or a sync plugin | Programmatic sets on design-led sites, up to the plan's item limit (higher tiers reach tens of thousands) | Compare item limits and sync options on actual plans; conditional logic is limited |
| **Hand-coded static or hybrid generation** (Next.js, Astro, and similar) | Templates read from JSON, a database, or an API at build time, or on demand with incremental regeneration | Tens of thousands of pages, complex logic, full control | Engineers own everything; very large sites need incremental builds to keep publishes fast |
| **Headless CMS + framework** (Sanity, Contentful, Storyblok) | Structured content in the CMS, templates in code | Editorial teams that also need programmatic sets | Two systems; schema changes need engineering |
| **AI-native site platforms** (Ploy ◆ PloyDB, and similar) | A database table backs a dynamic template; rows become pages | Teams already building on the platform who want data-driven pages without managing a separate CMS | Young products; hosting tied to the vendor; check export limits |

**Ploy ◆ specifics** (from its docs, 2026-10): PloyDB tables take CSV imports up to 32 MB and up to 97 columns, and pages built on a table update within about a minute without a republish. Rows can be updated through the CLI, the PloyDB API, or a webhook. CSV export caps at 10,000 rows. Ploy's own comparison page suggests Webflow when heavy programmatic SEO is the core motion, so weigh it against the volume you expect. Setup steps are in the [integration guide](https://github.com/coreyhaines31/marketingskills/blob/main/tools/integrations/ploy.md).

◆ marks a [Verified Partner](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md#verified-partners) of this repository: disclosure, not endorsement. When you name a ◆ tool in an answer, say it's a Verified Partner of the repository this skill comes from, and name an alternative alongside it. Also disclose, if Ploy comes up, that this repo's maintainer authored the "Programmatic SEO at Scale" Ploybook in Ploy's library, which follows the same 12 playbooks as this skill.

## Choosing

1. **Start with the site you already have.** If its CMS can hold the page count and supports the template logic, build there. The pages inherit the domain's authority and internal links.
2. **If it can't, decide subpath or subdomain on effort.** Google doesn't rank one above the other. A reverse-proxied subpath keeps the set inside the main site's structure and links but adds proxy setup; a subdomain is simpler but needs its own internal links and sitemap. The `site-architecture` skill's platforms reference has the proxy checklist.
3. **Size for the next year.** Pick the option whose item limits and publish times work at the page count you'll reach, with headroom for the variations you'll add.
4. **Prove it on a small batch.** Launch the 20–50 strongest pages first, check they index and rank, then scale (see Quality Checks in SKILL.md).



---

## `references/playbooks.md`

# The 12 Programmatic SEO Playbooks

Beyond mixing and matching data point permutations, these are the proven playbooks for programmatic SEO.

## Contents
- 1. Templates
- 2. Curation
- 3. Conversions
- 4. Comparisons
- 5. Examples
- 6. Locations
- 7. Personas
- 8. Integrations
- 9. Glossary
- 10. Translations
- 11. Directory
- 12. Profiles
- Choosing Your Playbook (Match to Your Assets, Combine Playbooks)

## 1. Templates

**Pattern**: "[Type] template" or "free [type] template"
**Example searches**: "resume template", "invoice template", "pitch deck template"

**What it is**: Downloadable or interactive templates users can use directly.

**Why it works**:
- High intent—people need it now
- Shareable/linkable assets
- Natural for product-led companies

**Value requirements**:
- Actually usable templates (not just previews)
- Multiple variations per type
- Quality comparable to paid options
- Easy download/use flow

**URL structure**: `/templates/[type]/` or `/templates/[category]/[type]/`

---

## 2. Curation

**Pattern**: "best [category]" or "top [number] [things]"
**Example searches**: "best website builders", "top 10 crm software", "best free design tools"

**What it is**: Curated lists ranking or recommending options in a category.

**Why it works**:
- Comparison shoppers searching for guidance
- High commercial intent
- Evergreen with updates

**Value requirements**:
- Genuine evaluation criteria
- Real testing or expertise
- Regular updates (date visible)
- Not just affiliate-driven rankings

**URL structure**: `/best/[category]/` or `/[category]/best/`

---

## 3. Conversions

**Pattern**: "[X] to [Y]" or "[amount] [unit] in [unit]"
**Example searches**: "$10 USD to GBP", "100 kg to lbs", "pdf to word"

**What it is**: Tools or pages that convert between formats, units, or currencies.

**Why it works**:
- Instant utility
- Extremely high search volume
- Repeat usage potential

**Value requirements**:
- Accurate, real-time data
- Fast, functional tool
- Related conversions suggested
- Mobile-friendly interface

**URL structure**: `/convert/[from]-to-[to]/` or `/[from]-to-[to]-converter/`

---

## 4. Comparisons

**Pattern**: "[X] vs [Y]" or "[X] alternative"
**Example searches**: "webflow vs wordpress", "notion vs coda", "figma alternatives"

**What it is**: Head-to-head comparisons between products, tools, or options.

**Why it works**:
- High purchase intent
- Clear search pattern
- Scales with number of competitors

**Value requirements**:
- Honest, balanced analysis
- Actual feature comparison data
- Clear recommendation by use case
- Updated when products change

**URL structure**: `/compare/[x]-vs-[y]/` or `/[x]-vs-[y]/`

*See also: competitors skill for detailed frameworks*

---

## 5. Examples

**Pattern**: "[type] examples" or "[category] inspiration"
**Example searches**: "saas landing page examples", "email subject line examples", "portfolio website examples"

**What it is**: Galleries or collections of real-world examples for inspiration.

**Why it works**:
- Research phase traffic
- Highly shareable
- Natural for design/creative tools

**Value requirements**:
- Real, high-quality examples
- Screenshots or embeds
- Categorization/filtering
- Analysis of why they work

**URL structure**: `/examples/[type]/` or `/[type]-examples/`

---

## 6. Locations

**Pattern**: "[service/thing] in [location]"
**Example searches**: "coworking spaces in san diego", "dentists in austin", "best restaurants in brooklyn"

**What it is**: Location-specific pages for services, businesses, or information.

**Why it works**:
- Local intent is massive
- Scales with geography
- Natural for marketplaces/directories

**Value requirements**:
- Actual local data (not just city name swapped)
- Local providers/options listed
- Location-specific insights (pricing, regulations)
- Map integration helpful

**URL structure**: `/[service]/[city]/` or `/locations/[city]/[service]/`

---

## 7. Personas

**Pattern**: "[product] for [audience]" or "[solution] for [role/industry]"
**Example searches**: "payroll software for agencies", "crm for real estate", "project management for freelancers"

**What it is**: Tailored landing pages addressing specific audience segments.

**Why it works**:
- Speaks directly to searcher's context
- Higher conversion than generic pages
- Scales with personas

**Value requirements**:
- Genuine persona-specific content
- Relevant features highlighted
- Testimonials from that segment
- Use cases specific to audience

**URL structure**: `/for/[persona]/` or `/solutions/[industry]/`

---

## 8. Integrations

**Pattern**: "[your product] [other product] integration" or "[product] + [product]"
**Example searches**: "slack asana integration", "zapier airtable", "hubspot salesforce sync"

**What it is**: Pages explaining how your product works with other tools.

**Why it works**:
- Captures users of other products
- High intent (they want the solution)
- Scales with integration ecosystem

**Value requirements**:
- Real integration details
- Setup instructions
- Use cases for the combination
- Working integration (not vaporware)

**URL structure**: `/integrations/[product]/` or `/connect/[product]/`

---

## 9. Glossary

**Pattern**: "what is [term]" or "[term] definition" or "[term] meaning"
**Example searches**: "what is pSEO", "api definition", "what does crm stand for"

**What it is**: Educational definitions of industry terms and concepts.

**Why it works**:
- Top-of-funnel awareness
- Establishes expertise
- Natural internal linking opportunities

**Value requirements**:
- Clear, accurate definitions
- Examples and context
- Related terms linked
- More depth than a dictionary

**URL structure**: `/glossary/[term]/` or `/learn/[term]/`

---

## 10. Translations

**Pattern**: Same content in multiple languages
**Example searches**: "qué es pSEO", "was ist SEO", "マーケティングとは"

**What it is**: Your content translated and localized for other language markets.

**Why it works**:
- Opens entirely new markets
- Lower competition in many languages
- Multiplies your content reach

**Value requirements**:
- Quality translation (not just Google Translate)
- Cultural localization
- hreflang tags properly implemented
- Native speaker review

**URL structure**: `/[lang]/[page]/` or `yoursite.com/es/`, `/de/`, etc.

---

## 11. Directory

**Pattern**: "[category] tools" or "[type] software" or "[category] companies"
**Example searches**: "ai copywriting tools", "email marketing software", "crm companies"

**What it is**: Comprehensive directories listing options in a category.

**Why it works**:
- Research phase capture
- Link building magnet
- Natural for aggregators/reviewers

**Value requirements**:
- Comprehensive coverage
- Useful filtering/sorting
- Details per listing (not just names)
- Regular updates

**URL structure**: `/directory/[category]/` or `/[category]-directory/`

---

## 12. Profiles

**Pattern**: "[person/company name]" or "[entity] + [attribute]"
**Example searches**: "stripe ceo", "airbnb founding story", "elon musk companies"

**What it is**: Profile pages about notable people, companies, or entities.

**Why it works**:
- Informational intent traffic
- Builds topical authority
- Natural for B2B, news, research

**Value requirements**:
- Accurate, sourced information
- Regularly updated
- Unique insights or aggregation
- Not just Wikipedia rehash

**URL structure**: `/people/[name]/` or `/companies/[name]/`

---

## Choosing Your Playbook

### Match to Your Assets

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Directory, Profiles, Curation |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| International potential | Translations |
| Competitor landscape | Comparisons |

### Combine Playbooks

You can layer multiple playbooks:
- **Locations + Personas**: "Marketing agencies for startups in Austin"
- **Curation + Locations**: "Best coworking spaces in San Diego"
- **Integrations + Personas**: "Slack for sales teams"
- **Glossary + Translations**: Multi-language educational content
