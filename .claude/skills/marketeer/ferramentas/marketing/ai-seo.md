# ai-seo

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/ai-seo

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers. Also use when the user mentions 'AI SEO,' 'AEO,' 'GEO,' 'LLMO,' 'answer engine optimization,' 'generative engine optimization,' 'LLM optimization,' 'AI Overviews,' 'optimize for ChatGPT,' 'optimize for Perplexity,' 'AI citations,' 'AI visibility,' 'zero-click search,' 'how do I show up in AI answers,' 'LLM mentions,' 'optimize for Claude/Gemini,' 'llms.txt,' 'llms-full.txt,' 'OKF,' 'Open Knowledge Format,' 'knowledge bundle,' 'agent-readable site,' 'agent readiness,' 'is my site agent-ready,' 'WebMCP,' 'do listicles still work for AI,' 'ChatGPT stopped citing comparison pages,' 'how do LLMs see our brand,' 'LinkedIn for AEO,' or 'AI citation format shift.' Use this whenever someone wants their content to be cited or surfaced by AI assistants and AI search engines. For traditional technical and on-page SEO audits, see seo-audit. For structured data implementation, see schema.


# AI SEO

You are an expert in AI search optimization — the practice of making content discoverable, extractable, and citable by AI systems including Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and Copilot. Your goal is to help users get their content cited as a source in AI-generated answers.

## Reference Routing

Start with this skill's core workflow. Open a reference when the user's question needs that detail; read additional references only when their topics are relevant.

| User questions | Local reference |
|---|---|
| Why can an agent not read our site? Are bot access, discovery files, or HTML blocking it? Can an agent sign up or check out for the user, through WebMCP or a skill file for our product? | [Agent readiness](references/agent-readiness.md) |
| AI barely shows up in referrals. How do we measure delayed visits, branded search, and pipeline from AI answers? | [AI attribution](references/ai-attribution.md) |
| Is AI saying something wrong about our price, features, or limits? How do we find and fix the source? | [Answer accuracy](references/answer-accuracy.md) |
| Which vendor does Claude Code or Cursor pick when a user says "deploy this"? How do we become the tool an agent installs mid-task? | [Agent defaults](references/agent-defaults.md) |
| Why are we cited but absent from the shortlist? Can our own buyer's guide help competitors? How should we measure recommendations? | [Citations vs. recommendations](references/citations-vs-recommendations.md) |
| How should we structure a definition, comparison, or FAQ? What makes an answer block useful on its own? | [Content patterns](references/content-patterns.md) |
| How does the approach differ for product pages, docs, local businesses, or ecommerce? Which content type should we improve? | [Content types](references/content-types.md) |
| Did an engine change which page formats it cites? Should we still invest in listicles or comparison pages? How do we separate a shift from noisy measurements? | [Format volatility](references/format-volatility.md) |
| Should we publish LinkedIn posts, articles, or company-page content? What makes that content discoverable and citable? | [LinkedIn citations](references/linkedin-ai-citations.md) |
| How do we run AEO in other languages and countries? Is ChatGPT Shopping worth it for our product? | [Multilingual and commerce](references/multilingual-and-commerce.md) |
| What belongs in an OKF bundle? Is it an established AI-search requirement or an emerging experiment? | [Open Knowledge Format](references/okf.md) |
| Which prompts should we track, how often, which topics are we losing, and how do we test multi-turn buying conversations? | [Prompt portfolio](references/prompt-portfolio.md) |
| Where should we start for a particular AI engine? Which search and training crawlers should we distinguish? | [Platform ranking factors](references/platform-ranking-factors.md) |
| Why does AI describe our positioning incorrectly? How can third-party consensus reinforce a specific use case? | [Positioning and consensus](references/positioning-and-consensus.md) |
| How should a video's title, captions, chapters, or description support citations? What should we check before publishing? | [YouTube citations](references/youtube-ai-citations.md) |

Read these bundled files from the installed skill directory; do not substitute a remote repository URL for a local reference. If a file is missing, say which reference is unavailable and use the core workflow without claiming to have read it. For time-sensitive statistics, platform behavior, or tool claims in any reference, check the source date and weigh evidence in this order: official platform documentation, then controlled experiments, then large observational datasets (often vendor research), then practitioner case studies. When documentation and observational data conflict, follow the documentation for eligibility and crawler controls and treat the data as a hypothesis to test. Never turn a study's percentage into a client forecast without matching engine, industry, language, market, and date.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

### 1. Current AI Visibility
- Do you know if your brand appears in AI-generated answers today?
- Have you checked ChatGPT, Perplexity, or Google AI Overviews for your key queries?
- What queries matter most to your business?

### 2. Content & Domain
- What type of content do you produce? (Blog, docs, comparisons, product pages)
- What's your domain authority / traditional SEO strength?
- Do you have existing structured data (schema markup)?

### 3. Goals
- Get cited as a source in AI answers?
- Appear in Google AI Overviews for specific queries?
- Compete with specific brands already getting cited?
- Optimize existing content or create new AI-optimized content?

### 4. Competitive Landscape
- Who are your top competitors in AI search results?
- Are they being cited where you're not?
- Do you have Wikipedia coverage or a presence on review sites?

---

## How AI Search Works

### The AI Search Landscape

| Platform | How It Works | Source Selection |
|----------|-------------|----------------|
| **Google AI Overviews** | Summarizes top-ranking pages | Strong correlation with traditional rankings |
| **ChatGPT (with search)** | Searches web, cites sources | Draws from wider range, not just top-ranked |
| **Perplexity** | Always cites sources with links | Favors authoritative, recent, well-structured content |
| **Gemini** | Google's AI assistant | Pulls from Google index + Knowledge Graph |
| **Copilot** | Bing-powered AI search | Bing index + authoritative sources |
| **Claude** | Brave Search (when enabled) | Training data + Brave search results |

For a deep dive on how each platform selects sources and what to optimize per platform, see [references/platform-ranking-factors.md](references/platform-ranking-factors.md).

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**.

In traditional search, you need to rank on page 1. In AI search, a well-structured page can get cited even if it ranks on page 2 or 3 — AI systems select sources based on content quality, structure, and relevance, not just rank position. Strong organic rankings are still one of the best predictors of AI visibility, so treat structure as a layer on top of SEO, not a replacement.

**Critical stats** (they drift; re-check before quoting to a client, and distrust vendor stats with no source or date):
- AI Overviews appeared on ~48% of the queries BrightEdge tracks (BrightEdge, Feb 2026), and position-one desktop CTR fell ~58% when one was present (Ahrefs, Dec 2025 data). Both are sample-specific, so don't forecast a site's traffic loss from them
- Adding statistics and citations raised visibility by roughly 30–40% in the original GEO study (Aggarwal et al., 2023)

### Google's Official Stance vs. Multi-Platform Reality

This is important to read once before doing anything else.

**Google's position** ([AI features optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)):
> "The best practices for SEO continue to be relevant because our generative AI features on Google Search are rooted in our core Search ranking and quality systems."

Google explicitly says:
- **No special markup or files are required** for AI Overviews or AI Mode
- **Don't chunk content for AI** — write for people, organize with normal headings and paragraphs
- **Don't write separate content for AI** — that risks "scaled content abuse" spam policy
- **Helpful, reliable, people-first content** wins — same E-E-A-T standards as regular Search
- **No AI-specific Search Console reporting** — use standard SEO metrics

**Other AI engines (ChatGPT, Claude, Perplexity, Copilot) behave differently:**
- They actively reward extractable structure — passages, FAQs, comparison tables, definition blocks
- They parse `llms.txt`, structured pricing pages, and machine-readable files when present
- They cite beyond top-ranked pages, including Reddit, Wikipedia, and review sites, in a mix that varies by engine

**What this means for the work:**
- The structural patterns in this skill (40–60 word answer blocks, FAQ schema, comparison tables) help **non-Google AI engines** materially. They also don't hurt Google — they're just normal good content organization.
- For Google AI Overviews / AI Mode specifically: optimize for people and core Search, full stop. Strong E-E-A-T, original information, semantic HTML, clean indexability.
- For ChatGPT/Claude/Perplexity: layer on the extractable structure + llms.txt + machine-readable files. When in doubt, write for people and organize for clarity; that satisfies both camps.

### Query Fan-Out (Google AI Search)

Google's AI features don't just answer the one query a user typed — they generate **concurrent, related queries** under the hood and retrieve results for each.

Google's own example: a user asking "how to fix lawns" triggers fan-out queries about herbicides, chemical-free removal, weed prevention, etc. The AI synthesizes across all of them.

**Implications:**
- Single-page-per-keyword targeting is less effective. Cover the **full topical cluster** so you're retrievable for the fan-out variants too.
- Long-tail intent matters less than topical authority — Google's AI systems understand synonyms and semantic equivalence.
- A page that comprehensively answers a parent topic (with sub-questions covered) will be retrieved more often than narrow per-query pages.

**Action**: when planning content, brainstorm the 5–10 related queries the AI is likely to fan out to and make sure your content (or your site as a whole) covers them, with one owning page per fact family (matrix in [references/content-patterns.md](references/content-patterns.md)).

ChatGPT fans out too — and you can extract its *literal* background queries for your niche via DevTools (method in [references/format-volatility.md](references/format-volatility.md)). Post-5.6, ChatGPT's fan-outs shifted away from "best/vs/top" modifiers toward `site:` and "official" searches — use the extraction to see where your category's fan-outs stand today.

---

## AI Visibility Audit

Before optimizing, assess your current AI search presence.

### Step 1: Check AI Answers for Your Key Queries

Test 10-20 of your most important queries across platforms:

| Query | Google AI Overview | ChatGPT | Perplexity | You Cited? | Competitors Cited? |
|-------|:-----------------:|:-------:|:----------:|:----------:|:-----------------:|
| [query 1] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |
| [query 2] | Yes/No | Yes/No | Yes/No | Yes/No | [who] |

**Query types to test**, spread across buyer awareness stages and written the way people actually type into a chat box:
- Problem-aware: "How do I [problem your product solves]?"
- Solution-aware: "What is [your product category]?" / "Best [category] for [use case]"
- Product-aware: "[Your brand] vs [competitor]" / "Is [your brand] good for [use case]?"
- Most aware: "[Your brand] pricing" / "Does [your brand] integrate with [tool]?"

Keep the list to prompts that would change revenue. A citation for a glossary question ("what is gross profit?") rarely sells anything. Track prompts like keywords: collapse wording variants of the same intent into one core prompt, then run each several times.

### Step 2: Analyze Citation Patterns

When your competitors get cited and you don't, examine:
- **Content structure** — Is their content more extractable?
- **Authority signals** — Do they have more citations, stats, expert quotes?
- **Freshness** — Is their content more recently updated?
- **Schema markup** — Do they have structured data you're missing?
- **Third-party presence** — Are they cited via Wikipedia, Reddit, review sites?

**Turn findings into work.** If an assistant states something wrong or vague about you, the page that should state that fact isn't saying it plainly; fix that page first. If you're absent, the sources it cites for the prompt are your target list for PR, review sites, and directories.

### Step 3: Content Extractability Check

For each priority page, verify:

| Check | Pass/Fail |
|-------|-----------|
| Clear definition in first paragraph? | |
| Self-contained answer blocks (work without surrounding context)? | |
| Statistics with sources cited? | |
| Comparison tables for "[X] vs [Y]" queries? | |
| FAQ section with natural-language questions? | |
| Schema markup (FAQ, HowTo, Article, Product)? | |
| Expert attribution (author name, credentials)? | |
| Recently updated (within 6 months)? | |
| Heading structure matches query patterns? | |
| AI crawler policy matches discovery and training goals? | |

### Step 4: AI Bot Access Check

Audit AI user agents by purpose. Search-discovery, user-triggered retrieval, model-training, and product-control tokens are not interchangeable:

- **Search discovery:** `OAI-SearchBot` (ChatGPT), `PerplexityBot`, `Claude-SearchBot`, `meta-webindexer` (Meta AI), and the conventional search crawlers that feed an answer product
- **User-triggered retrieval:** `ChatGPT-User`, `Claude-User`, `Perplexity-User`, and `meta-externalfetcher`; vendor handling can differ from automatic crawlers, so verify the current documentation
- **Potential model training:** `GPTBot`, `ClaudeBot`, and `meta-externalagent`
- **Google product control:** `Google-Extended` controls certain Gemini training and grounding uses of content Google already crawls; it does not affect Google Search inclusion or ranking

Default to one wildcard (`User-agent: *`) rule that allows agents, and add named groups only for deliberate exceptions such as a training opt-out; an allowlist of named crawlers silently excludes agent search APIs that run their own crawlers, and a named group replaces the `*` rules for that bot. Check each relevant user-agent group and any WAF or CDN rules separately. A publisher can allow search discovery while disallowing model-development crawlers; do not infer that blocking a training crawler necessarily blocks citations. See [references/platform-ranking-factors.md](references/platform-ranking-factors.md) for the full robots.txt configuration.

---

## Optimization Strategy

### The Three Pillars

```
1. Structure (make it extractable)
2. Authority (make it citable)
3. Presence (be where AI looks)
```

### Pillar 1: Structure — Make Content Extractable

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

For detailed templates for each block type, see [references/content-patterns.md](references/content-patterns.md).

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for snippet extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparison content
- Numbered lists beat paragraphs for process content
- Each paragraph should convey one clear idea

### Pillar 2: Authority — Make Content Citable

AI systems prefer sources they can trust. Build citation-worthiness.

**The Princeton GEO research** (KDD 2024, studied across Perplexity.ai) ranked 9 optimization methods:

| Method | Visibility Boost | How to Apply |
|--------|:---------------:|--------------|
| **Cite sources** | +40% | Add authoritative references with links |
| **Add statistics** | +37% | Include specific numbers with sources |
| **Add quotations** | +30% | Expert quotes with name and title |
| **Authoritative tone** | +25% | Write with demonstrated expertise |
| **Improve clarity** | +20% | Simplify complex concepts |
| **Technical terms** | +18% | Use domain-specific terminology |
| **Unique vocabulary** | +15% | Increase word diversity |
| **Fluency optimization** | +15-30% | Improve readability and flow |
| ~~Keyword stuffing~~ | **-10%** | **Actively hurts AI visibility** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more — up to 115% visibility increase with citations.

**Statistics and data** (+37-40% citation boost)
- Include specific numbers with sources
- Cite original research, not summaries of research
- Add dates to all statistics
- Original data beats aggregated data

**Expert attribution** (+25-30% citation boost)
- Named authors with credentials
- Expert quotes with titles and organizations
- "According to [Source]" framing for claims
- Author bios with relevant expertise

**Freshness signals**
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)
- Current year references and recent statistics
- Remove or update outdated information

**E-E-A-T alignment**
- First-hand experience demonstrated
- Specific, detailed information (not generic)
- Transparent sourcing and methodology
- Clear author expertise for the topic

### Pillar 3: Presence — Be Where AI Looks

AI systems cite your own site and the places that talk about you, in proportions that vary by engine and category. In one large dataset, company sites took about 57% of citations (ChatGPT 47%, Gemini 69%; Profound, July 2026), while shortlist recommendations lean on third-party consensus. Measure your category's citation mix before choosing channels; see [references/citations-vs-recommendations.md](references/citations-vs-recommendations.md).

**Third-party surfaces to cover:**
- Wikipedia (7.8% of ChatGPT citations in Profound's Aug 2024–Jun 2025 data)
- Reddit (1.8% in the same data, then nearly wiped from ChatGPT by Aug 2026 retrieval changes; still retrieved elsewhere; see the volatility section in [references/agent-readiness.md](references/agent-readiness.md))
- Industry publications and guest posts
- LinkedIn — among the most-cited domains for professional queries, but which surface gets cited depends on the engine (ChatGPT now favors posts over articles; Gemini barely cites LinkedIn). Front-load the target phrase, since a post's first words become its URL slug. See [references/linkedin-ai-citations.md](references/linkedin-ai-citations.md)
- Review sites (G2, Capterra, TrustRadius for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)
- Podcasts (episodes get transcribed, show notes published — both get crawled and cited)
- Quora answers

**Actions:**
- Ensure your Wikipedia page is accurate and current
- Participate authentically in Reddit communities — but as one surface in a portfolio, never the whole strategy (citation mixes shift overnight with retrieval updates)
- Get featured in industry roundups and comparison articles
- Make every third-party profile (G2, Capterra, Gartner, Crunchbase, LinkedIn) describe you with the same segment and positioning as your About page; models look for consensus. For repositioning, mergers, and head terms, see [references/positioning-and-consensus.md](references/positioning-and-consensus.md)
- Create YouTube content for key how-to queries — models don't watch the video, they read the text layer around it; see [references/youtube-ai-citations.md](references/youtube-ai-citations.md) for the full anatomy (transcript, captions, chapters, description, pinned comment)
- Guest on podcasts in your category (prep with the public-relations skill's podcast guest prep)
- Answer relevant Quora questions with depth

### Machine-Readable Files for AI Agents

> **Google's stance**: not required for AI Overviews or AI Mode. Their guide explicitly says you don't need new markup, AI files, or markdown to appear in generative AI search.
>
> **Why include them anyway**: non-Google AI engines (ChatGPT, Claude, Perplexity) and autonomous buying agents do reward extractable structure. The files below help with those engines without harming Google.

AI agents aren't just answering questions — they're becoming buyers. When an AI agent evaluates tools on behalf of a user, it needs structured, parseable information. If your pricing is locked in a JavaScript-rendered page or a "contact sales" wall, agents will skip you and recommend competitors whose information they can actually read.

**Audit this layer first**: [references/agent-readiness.md](references/agent-readiness.md) — the access/discovery/parseability checklist, free scoring tools (`npx is-agentic`, Frase's checker), Markdown content negotiation + `Link` headers, `llms-full.txt`, and the emerging agent-*actionable* layer (WebMCP, and a skill file for your product with a prefilled checkout link).

Add these machine-readable files to your site root:

**`/pricing.md` or `/pricing.txt`** — Structured pricing data for AI agents

```markdown
# Pricing — [Your Product Name]

## Free
- Price: $0/month
- Limits: 100 emails/month, 1 user
- Features: Basic templates, API access

## Pro
- Price: $29/month (billed annually) | $35/month (billed monthly)
- Limits: 10,000 emails/month, 5 users
- Features: Custom domains, analytics, priority support

## Enterprise
- Price: Custom — contact sales@example.com
- Limits: Unlimited emails, unlimited users
- Features: SSO, SLA, dedicated account manager
```

**Why this matters now:**
- AI agents increasingly compare products programmatically before a human ever visits your site
- Opaque pricing gets filtered out of AI-mediated buying journeys
- A simple markdown file is trivially parseable by any LLM — no rendering, no JavaScript, no login walls
- Same principle as `robots.txt` (for crawlers), `llms.txt` (for AI context), and `AGENTS.md` (for agent capabilities)

**Best practices:**
- Use consistent units (monthly vs. annual, per-seat vs. flat)
- Include specific limits and thresholds, not just feature names
- List what's included at each tier, not just what's different
- Keep it updated — stale pricing is worse than no file
- Link to it from your sitemap and main pricing page

**`/llms.txt`** — Context file for AI systems (see [llmstxt.org](https://llmstxt.org))

If you don't have one yet, add an `llms.txt` that gives AI systems a quick overview of what your product does, who it's for, and links to key pages (including your pricing).

**`/okf/` — Open Knowledge Format bundle (Google-backed, v0.1)**

Google [introduced OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) in June 2026 — a markdown spec for representing site content as a directory of cross-linked files with YAML frontmatter, agent-readable without scraping. Built primarily for data-team catalog metadata; the site-readable-by-agents repurposing was popularized by Suganthan Mohanadasan. No confirmed AI-search ranking signal today — treat it as protocol-layer registration like early schema.org. **For the full breakdown, implementation paths (free generator, WordPress plugin, by-hand), hosting guidance, and when to skip, see [references/okf.md](references/okf.md).**

### Schema Markup for AI

Structured data helps AI systems understand your content. Key schemas:

| Content Type | Schema | Why It Helps |
|-------------|--------|-------------|
| Articles/Blog posts | `Article`, `BlogPosting` | Author, date, topic identification |
| How-to content | `HowTo` | Step extraction for process queries |
| FAQs | `FAQPage` | Direct Q&A extraction |
| Products | `Product` | Pricing, features, reviews |
| Comparisons | `ItemList` | Structured comparison data |
| Reviews | `Review`, `AggregateRating` | Trust signals |
| Organization | `Organization` | Entity recognition |

No well-documented study isolates a schema lift on AI citations, so treat schema as context that helps engines parse your pages and expect no fixed lift from it. **Google's note**: structured data is "not required for generative AI search" but is recommended for overall SEO strategy. For implementation, use the **schema** skill.

---

## Agentic Experiences

Beyond AI search engines summarizing content, autonomous agents are starting to access sites directly — clicking, reading, comparing, even buying on behalf of users. Google's guide flags this as an emerging category to plan for.

**How agents access your site:**
- **Visual rendering** — they screenshot/read the page like a user would
- **DOM inspection** — they parse the page's HTML structure
- **Accessibility tree** — they rely on the same semantic information assistive tech uses (labels, roles, landmarks, headings)

**What to do:**
- **Render meaningful content without heavy JS gymnastics** — if the page is blank until 4 frameworks finish loading, agents see blank
- **Semantic HTML** — use `<main>`, `<nav>`, `<article>`, `<button>`, proper heading hierarchy, `alt` text on images
- **Clean accessibility tree** — every interactive element labelled; ARIA used correctly (or not at all when native HTML suffices)
- **Stable selectors / predictable layouts** — agents struggle with sites that re-render every interaction
- **Visible pricing, specs, contact info** — anything an agent would need to make a buying recommendation should be on a public, indexable page (this is where `/pricing.md` and similar files help). Date the facts that change ("4.7 on G2 as of October 2026") so an agent can judge freshness
- **Proof as text** — testimonials, ratings, and named customer logos in the HTML as text, not baked into images or injected by a widget script. If you can't select it with the mouse, an agent may not read it

**Emerging — Universal Commerce Protocol (UCP):**
Google references UCP as a forthcoming protocol that will give agents standardized hooks for commerce interactions (catalog discovery, pricing, checkout). Watch for adoption; for now, the structural recommendations above are the precursor.

For ecom and local business specifically, Google highlights:
- **Merchant Center feeds** + **Google Business Profile** for product/service visibility in AI Search
- **Business Agent** for conversational customer engagement (where applicable)

---

## Content Types That Get Cited Most

Not all content is equally citable — and the format mix is **volatile**. The long-standing baseline had comparison articles (~33%) and listicles (~10%) among the top citation earners, but **ChatGPT 5.6 (Aug 2026) demoted the exploited formats: listicle citations fell −50.5% and comparison-page citations −32.1%, while `site:` and "official" retrieval surged** — a shift toward primary sources and owned pages. Format strategy is now per-platform (comparisons still work on Google AIO/Gemini/Perplexity). See [references/format-volatility.md](references/format-volatility.md) for the shift data, the per-platform format table, LinkedIn's citation numbers, and the ChatGPT fan-out extraction diagnostic.

**Evergreen winners across platforms:** original research and data, definitive guides, and owned "official" pages — product, docs, pricing — with extractable structure.

**Underperformers:** generic unstructured posts, thin or gated or PDF-only content, and anything undated without author attribution.

**Citation ≠ recommendation.** Getting cited means your content was useful to consult; getting *recommended* — onto the buyer's actual shortlist — is governed by web-wide consensus (reviews, forums, analysts, press) and is largely independent of your own content. Self-promotional "best [category]" listicles can even backfire for emerging brands: in one 100-query B2B study, 69% of the AI Overview citations that self-promotional listicles earned came in answers that recommended competitors instead of the publishing brand. See [references/citations-vs-recommendations.md](references/citations-vs-recommendations.md) for the visibility ladder (retrieved → cited → mentioned → recommended), stage-dependent buyer's-guide strategy, what earns recommendations, and the attribution blind spot.

---

## Monitoring AI Visibility

### What to Track

| Metric | What It Measures | How to Check |
|--------|-----------------|-------------|
| AI Overview presence | Do AI Overviews appear for your queries? | Manual check or Semrush/Ahrefs |
| Brand citation rate | How often you're cited in AI answers | AI visibility tools (see below) |
| Share of AI voice | Your citations vs. competitors | Peec AI, Otterly, ZipTie, Omnia |
| Citation sentiment | How AI describes your brand | Manual review + monitoring tools |
| Recommendation rate | Whether you're on the shortlist, not just cited (see [citations-vs-recommendations.md](references/citations-vs-recommendations.md)) | Prompt tracking + mention framing |
| Source attribution | Which pages get cited, and what AI exposure does downstream | AI referrals plus delayed branded and direct visits ([ai-attribution.md](references/ai-attribution.md)) |

### AI Visibility Monitoring Tools

| Tool | Coverage | Best For |
|------|----------|----------|
| **Otterly AI** | ChatGPT, Perplexity, Google AI Overviews | Share of AI voice tracking |
| **Peec AI** | ChatGPT, Gemini, Perplexity, Claude, Copilot+ | Multi-platform monitoring at scale |
| **ZipTie** | Google AI Overviews, ChatGPT, Perplexity | Brand mention + sentiment tracking |
| **LLMrefs** | ChatGPT, Perplexity, AI Overviews, Gemini | SEO keyword → AI visibility mapping |
| **Profound, Ahrefs Brand Radar, Semrush** | Major assistants and Google AI surfaces | Larger programs: cited sources, answer text, prompt demand (Profound's studies are cited in the references as vendor research) |
| **Omnia** | Google AI Mode, Google AI Overviews, ChatGPT, Perplexity, Gemini, Claude, Copilot | AI visibility monitoring |

### DIY Monitoring (No Tools)

Monthly manual check:
1. Pick your top 20 queries
2. Run each through ChatGPT, Perplexity, and Google
3. Record: Are you cited? Who is? What page? Log it in a spreadsheet and track month-over-month

AI answers are **non-deterministic** — one run is an anecdote, not a measurement. Run each query 3–5 times per platform and track the mention *rate* with its sample size ("cited 3/5, n=5"), comparing rates over time rather than single runs. Full rigor checklist in [references/format-volatility.md](references/format-volatility.md).

### Search Console expectations

Google's guide is explicit: **there is no AI-specific Search Console reporting**. AI Overviews and AI Mode use core Search ranking, so the standard Search Console reports (Performance, Coverage, Core Web Vitals) are still what you measure with for Google. The third-party tools above are the only way to see cross-platform AI citation behavior.

---

## What NOT to Do

Google's guide calls these out explicitly — they hurt across both traditional Search and AI features.

1. **Write separate content "for AI"**. Same content should serve people and AI. Writing variants targeted at AI systems risks the **scaled content abuse spam policy** — Google's words.
2. **Chunk pages into AI-bait fragments**. Google's guide is direct: *"Don't break your content into tiny pieces for AI to better understand it."* Use normal paragraph + heading structure.
3. **Generate at scale for ranking manipulation**. AI-generated content is fine *if* it meets Search Essentials and spam policies. Mass-producing thin variations does not.
4. **Pursue inauthentic mentions**. Don't fabricate citations, invent awards, run "independent" review sites you own, or bulk-spam Reddit/Wikipedia for AI visibility. Fake or misleadingly sourced reviews can also break the FTC's 2024 reviews rule. Real participation only.
5. **Treat every AI user agent as the same control**. `GPTBot`, `ClaudeBot`, and `Google-Extended` have different documented purposes from `OAI-SearchBot`, `Claude-SearchBot`, and `PerplexityBot`. Decide separately for discovery, user retrieval, training, and grounding.
6. **Hide your main content behind JS that doesn't render**. Both core Search and AI agents need to see your content; JS-only rendering loses both audiences.
7. **Skip E-E-A-T fundamentals**. Author identity, first-hand experience, expertise signals, transparent sourcing — Google's guide leans heavily on these for AI features.

---

## AI SEO by Content Type

For tactical guidance on SaaS product pages, blog content, comparison/alternative pages, documentation, and local/ecom (Google's emphasis on Merchant Center + Business Profile), see [references/content-types.md](references/content-types.md).

---

## Common Mistakes

- **Ignoring AI search entirely** — AI Overviews appear on roughly half of tracked queries in many industries (BrightEdge, Feb 2026), and assistant usage keeps growing
- **Treating AI SEO as separate from SEO** — Good traditional SEO is the foundation; AI SEO adds structure and authority on top
- **Writing for AI, not humans** — If content reads like it was written to game an algorithm, it won't get cited or convert
- **No freshness signals** — Undated content loses to dated content because AI systems weight recency heavily. Show when content was last updated
- **Gating all content** — AI can't access gated content. Keep your most authoritative content open
- **Ignoring third-party presence** — Shortlist recommendations lean on what reviews, forums, and press say about you, even where your own site earns most citations
- **No structured data** — Schema markup gives AI systems structured context about your content
- **Keyword stuffing** — Unlike traditional SEO where it's just ineffective, keyword stuffing actively reduces AI visibility by 10% (Princeton GEO study)
- **Hiding pricing behind "contact sales" or JS-rendered pages** — AI agents evaluating your product on behalf of buyers can't parse what they can't read. Add a `/pricing.md` file
- **Blocking discovery crawlers without checking their purpose** — Restricting `OAI-SearchBot`, `PerplexityBot`, or `Claude-SearchBot` may reduce search visibility; training controls are separate
- **Generic content without data** — "We're the best" won't get cited. "Our customers see 3x improvement in [metric]" will
- **Forgetting to monitor** — You can't improve what you don't measure. Check AI visibility monthly at minimum

---

## Tool Integrations

For implementation, see the [tools registry](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md).

| Tool | Use For |
|------|---------|
| `semrush` | AI Overview tracking, keyword research, content gap analysis |
| `ahrefs` | Backlink analysis, content explorer, AI Overview data |
| `gsc` | Search Console performance data, query tracking |
| `ga4` | Referral traffic from AI sources |

---

## Related Skills

- **seo-audit**: For traditional technical and on-page SEO audits; **link-building** for earning links and mentions on the third-party pages AI engines cite
- **schema**: For implementing structured data that helps AI understand your content
- **content-strategy**: For planning what content to create
- **competitors**: For building comparison pages that get cited
- **programmatic-seo**: For building SEO pages at scale
- **copywriting**: For writing content that's both human-readable and AI-extractable
- **lead-magnets**: For packaging an owned course or content library as an installable agent skill (different from public-site AI visibility)



---

## `references/agent-defaults.md`

# Agent Defaults: When the Agent Picks the Vendor

A growing share of buying decisions happens inside a task. A developer tells Claude Code "deploy this," "add auth," or "send a welcome email," and the agent chooses a vendor, installs it, and moves on. There is no search results page and no shortlist for the user to compare. Whatever the agent reaches for first wins.

This applies most to developer tools, APIs, infrastructure, and SaaS with a CLI or SDK. It is spreading to anything a computer-use agent can sign up for. The rest of this skill covers being cited and recommended in answers; this reference covers being **the default an agent acts on**.

**Case: Railway (October 2026).** Founder Jake Cooper said on a podcast that the company grew from about $20M to about $100M ARR in a year with a go-to-market team of about seven, and named getting the models to "recommend us more and more" as a go-to-market goal. Practitioner breakdowns of their site counted thousands of self-hosting template pages, a deploy guide per framework, comparison and migration pages for each major competitor, an `llms.txt` with a summary per docs page, plugins inside ChatGPT and Claude Code, and `ssh railway new` to get a server with no signup. The same breakdowns claimed Claude Code picks Railway for most Python apps and Vercel for every Next.js app tested. Those counts and percentages are third-party and unverified; the pattern is the point.

## Measure your share of agent defaults

You can't improve a default you haven't measured, and nobody reports this number for you.

1. **Build a task panel.** 20–50 realistic tasks spread across the stacks your buyers use (a FastAPI service, a Next.js app, a Rails app, a cron worker, a static site). Write each the way a user would: "deploy this," "add a Postgres database," not "deploy this to [you]."
2. **Run each task in a clean environment** on every agent your buyers use (Claude Code, Cursor, Codex, plus ChatGPT or Claude chat for the "how do I" version). No project rules, memory, or MCP servers that name a vendor.
3. **Run each task 3+ times.** Agent choices vary run to run, and one sample is noise.
4. **Record per run:** the vendor chosen, whether the agent got to a working result, where it stalled (signup, email verification, payment, a failing CLI step), and which docs or URLs it fetched.
5. **Report share by stack.** The gap is usually one stack ("we win Python, lose everything front-end"). That stack is where content and tooling work goes.
6. **Rerun on every major model release.** Defaults can move overnight when a model changes, and new models tend to bring more code to deploy. Run it monthly between releases; the agent-default check loop in **marketing-loops** schedules it.

Where the agent stalled tells you more than which vendor it picked. A run that chose you and then died at email verification is a loss you can fix.

## What moves the default

| Lever | Why agents respond to it | Railway's version |
|---|---|---|
| **Shortest path to a working result** | Agents favor the route with the fewest human-gated steps: account creation, email verification, CAPTCHA, a credit card before first use | `ssh railway new` provisions a server before any signup; the account is claimed later |
| **Agent setup in one step** | An agent that has your MCP server, CLI, or skill installed uses it instead of guessing | A docs section for agents with one command that installs what Claude Code or Cursor needs |
| **Presence inside the assistants** | If the assistant has a native connector or plugin, deploying never leaves the chat | Plugins in ChatGPT and Claude Code |
| **Task-shaped pages per stack** | Agents fetch docs mid-task; a page that matches the exact task ("deploy Django") and ends in a working result gets followed | A guide per framework, each ending with the app live |
| **Template pages per popular tool** | Self-hosting and setup queries ("how do I run n8n") are a long tail that programmatic pages cover, see **programmatic-seo** | Thousands of one-click template pages |
| **Migration guides per competitor** | An agent moving a project follows steps; see **competitors** for the comparison side | A comparison page with a migration guide for each major competitor |
| **Docs agents can read** | An `llms.txt` index with one-line summaries, plus a markdown version of every page, lets the agent find the right page and quote it correctly (the Discovery checks in [agent-readiness.md](agent-readiness.md)) | An index of every docs page with a summary each, and a plain-text version of each page |
| **Fresh, dated changes** | Recently updated docs and changelogs keep answers current for search and models | A changelog page every week since 2021 |
| **CLI output an agent can recover from** | Non-interactive flags, JSON output, and errors that say what to run next keep the run alive past a failure | (General practice, not from the Railway breakdowns) |

Fix the stall points from your measurement first. Content won't help if the agent picks you and then can't finish.

## Audit your docs for coding agents

Treat a coding agent as its own answer engine. In Profound's sample of 24,135 responses with web search enabled, Claude searched the web in 93% of responses and Claude Code in 13%, and the brands each one mentioned overlapped only about 20% (Profound, August 2026; observational). When Claude Code did fetch pages, nearly three-quarters of visits went to documentation, informational, and pricing pages. So your chat-assistant visibility tells you little about your coding-agent visibility, and the pages agents read are docs and pricing.

Profound sells AI visibility tracking; treat these as vendor research and run your own panel (above) before acting on them.

**1. Map tasks to pages.** List what users ask a coding agent to do with your product: install, authenticate, integrate, migrate, debug, compare, estimate cost, check compatibility. Give each task one canonical page and list the facts that page must state.

| Task | Canonical page | Facts it must state | Gap |
|---|---|---|---|
| Install in a Next.js app | /docs/nextjs | Package name, minimum version, env vars, one working example | Example uses a deprecated import |
| Estimate cost | /pricing | Pricing unit, free tier limits, overage rate | Overage only in a PDF |

**2. Check retrieval.** For each canonical page:

- The title and headings name the task and the stack
- The answer or command comes before background
- Prerequisites, versions, and dates are explicit
- Examples are copyable and current
- Anchors and URLs stay stable between releases
- The text renders without JavaScript, and a markdown version exists (see [agent-readiness.md](agent-readiness.md))

Use question-shaped headings only where they match a real task. Don't stuff product names into docs.

**3. Keep a technical fact ledger.** One row per fact an agent might act on: supported versions and runtimes, regions, rate limits, pricing units, auth methods, data handling, deprecations. Record the canonical source and an owner for each. Then check the same fact everywhere it appears: docs, pricing page, README, package registry descriptions (npm, PyPI), examples, and changelog. An agent that finds two different rate limits will guess, or pick a vendor whose docs agree with themselves.

**4. Fill missing decision pages.** Compatibility matrices, migration guides, troubleshooting references, and a plain pricing explainer are the pages agents most often need and vendors most often skip.

**5. Test in fresh sessions.** Run your task panel in both the chat assistant and the coding agent, recording whether you were mentioned, which pages were fetched, and whether the facts came back right. Log errors in the claim ledger from [answer-accuracy.md](answer-accuracy.md).

Don't infer official Anthropic or OpenAI ranking factors from any of this. Check crawler and access controls against current vendor documentation.

## Limits and rules

- **Some defaults are structural.** A framework's own maker, or the vendor whose examples dominate the framework's docs, may hold that stack no matter what you publish. Railway's reported answer was to win adjacent stacks rather than fight Vercel on Next.js. Pick stacks where the default is still open.
- **Write instructions for using your product only.** Agent-facing docs, `llms.txt`, and skill files that tell agents to prefer your product over what the user asked for are prompt injection. Agent platforms treat them as manipulation, and users who notice stop trusting the tool. Describe how to do the task with your product; let the task decide.
- **Agent-provisioned resources still need guardrails.** No-signup provisioning needs abuse limits, expiry for unclaimed resources, and a clear path to claim and pay. Treat that as product work, with growth as the reason to do it.
- **Placements in agent tool registries change fast.** Recheck plugin and MCP registry listings when you rerun the panel, and treat any share figure, including the ones above, as dated.

---

*Framework lineage: the coding-agent docs audit (task-to-page map, technical fact ledger, Claude vs. Claude Code testing) is adapted (re-expressed and restructured) from Profound's MIT-licensed claude-code-discoverability-auditor skill and its August 2026 study, credited.*



---

## `references/agent-readiness.md`

# Agent Readiness — Can an Agent Reach, Navigate, and Parse Your Site?

AI visibility work splits into two layers: what your content says (the rest of this skill) and whether an agent can *get to it at all*. This reference covers the second layer — the access/discovery/parseability audit — plus the emerging shift from agent-*readable* to agent-*actionable* sites.

Two free scoring tools shipped in August 2026 and turned this into a measurable discipline:

| Tool | Run it | Method |
|---|---|---|
| **Is Agentic** (Vercel + Ora) | `npx is-agentic yourdomain.com` or [is-agentic.com](https://is-agentic.com) | 100+ checks; Essential checks carry most of the score; Recommended checks activate only when evidence shows you have that surface (API, MCP server, commerce); not-applicable checks are excluded, not failed; includes an observed agent journey showing where a real agent hit friction |
| **Frase Agent Readiness Checker** | [frase.io/tools/agent-readiness](https://www.frase.io/tools/agent-readiness) | Access / Discovery / Parseability triad; 80+ = agents can reliably use the site, 60–79 = solid with gaps, <60 = real access problems |

For developer documentation specifically, Fern's **Agent Score** grades a docs site for coding agents (run `npx afdocs check <docs-url>` locally first, or score it at buildwithfern.com/agent-score for a public report page).

Run one before and after any agent-readiness work — the score is a shareable artifact and the failed checks are your worklist. (All of these are vendor tools with a product behind them; the *checks* are the value, not the pitch.)

## The AgentReady standard

[AgentReady.org](https://agentready.org) (launched October 21, 2026) is an open spec for what a product should implement to be usable by agents. Ora leads it with a group of collaborators that includes Vercel, Stripe, and Google (current list on the site). It orders practices the way agents meet a site — **find → read → act** — and gives each a stable ID and a strength:

- **MUST** — agents failed without it in the studies. Only three: allow agents through robots.txt and bot protection (AR-FIND-01), put the answer in the initial HTML (AR-READ-01), return real HTTP status codes (AR-READ-02) — plus, *if the product should complete tasks*, an MCP server or CLI (AR-ACT-10).
- **SHOULD** — measurably shaped where agents went (first-party docs, sitemap, homepage links, llms.txt, JSON-LD, fenced code, pricing as text, auth, OpenAPI).
- **MAY** — emerging conventions (Markdown mirrors, AI Catalog).

Cite the IDs in audit findings ("fails AR-READ-01") so fixes map to a public spec rather than your opinion. In October 2026, only about 6% of sites Ora scanned graded B or above, so most sites have real gaps (live figures on the site).

**Why it matters (Ora research, "AX is the New AEO," arXiv:2609.34951, September 2026 — vendor research with a public dataset):**

- When an agent can't read the site, it answers anyway (~99% of dead-end journeys) from web search and other people's pages. Those answers were **3.7× as likely to contain none of the facts asked for**.
- Agent-ready businesses were **clearly recommended 1.9× as often** (20% vs 11%), matched on brand fame and third-party citations.
- **Pricing accuracy was 60% from the site's own pages vs 37% from elsewhere** — the widest gap of any question type. Agents that couldn't read the site punted to "contact sales" more often (22% vs 15%).
- 82% of answers traced to a page the agent fetched; that page was a **docs page 47% of the time** and llms.txt 14%.
- Agents use the same pages people do: docs reached in 83% of runs, homepage 69% (the first fetch 92% of the time), then a cliff — `.well-known/*` 23%, `openapi.json` 21% where shipped, `sitemap.xml` 4%.

Per the skill's evidence order, treat these as observational data from a party with a scanner to sell, not a forecast for any one site.

## The three questions

### 1. Access — can an agent get to the page and see real content?

- **Core content in the initial HTML response.** Most agents never execute JavaScript. If the content only exists after client-side rendering, it doesn't exist. This is the #1 essential check in both tools.
- **No bot challenge or firewall block** on the intended discovery path. Blocking `OAI-SearchBot`, `PerplexityBot`, or `Claude-SearchBot` may reduce search visibility. Blocking model-development crawlers such as `GPTBot` or `ClaudeBot` can be an intentional training opt-out and is not, by itself, a visibility failure. Audit what your CDN/WAF actually does to each user agent — many sites block them by default without anyone deciding to. Bot protection is a **separate gate from robots.txt**: a WAF that answers agents with a 403 or a challenge page blocks them however permissive the file is. Let verified agents through by the providers' published IP ranges or Web Bot Auth signatures. In Ora's studies, a bot block was one of only two changes that broke agents outright (the other was a JS-only answer); not-agent-ready sites blocked agents 2.1× as often.
- **Correct HTTP behavior**: real status codes, stable canonical URLs, recoverable errors. Return a 404 (or a redirect) for missing paths — a single-page app that returns 200 for every path makes dead URLs look live to an agent. When throttling, send a **429 with `Retry-After`** instead of a challenge page; agents treat 429 as "back off and return."
- **Pricing as text on a first-party page** — plans, free tier, and limits in the HTML, not an image, a calculator, or a sales form (the accuracy gap above).

### 2. Discovery — do your files tell agents what's here?

- **robots.txt with a deliberate AI-crawler stance.** AgentReady's default is one wildcard rule (`User-agent: *`) that allows agents, rather than an allowlist of named crawlers — an allowlist silently excludes agent search APIs (Exa, Tavily, Brave, Parallel) that run their own crawlers. Add named groups only for deliberate exceptions, such as blocking training crawlers (`GPTBot`, `ClaudeBot`) while leaving search (`OAI-SearchBot`, `Claude-SearchBot`) and user-triggered fetchers (`ChatGPT-User`, `Claude-User`) on the wildcard. Two catches: a named group like `User-agent: GPTBot` *replaces* your `*` rules for that bot, so audit existing groups; and user-triggered fetchers may not consult robots.txt at all. See the bot-access guidance in SKILL.md.
- **First-party docs that answer.** Docs were the most-read and most-cited page type in Ora's runs. Put setup, quickstart, and pricing answers on canonical, current docs pages and link them from the homepage.
- **A sitemap that loads and parses cleanly.** Standard for crawlers and search engines, even though agents fetch it directly in only ~4% of runs.
- **Link every discovery file from pages agents already read.** 86–100% of visits to llms.txt, `openapi.json`, `.well-known/*`, and AGENTS.md arrived through a link, not a guessed path. Put them in the footer, a resources section, or `<link>` tags in the homepage head. A file nothing points to is a file nothing fetches.
- **llms.txt at the domain root** (see Machine-Readable Files in SKILL.md).
- **`llms-full.txt`** — the newer companion: your entire site content in one file, so an agent gets everything in a single request instead of crawling. Emerging, cheap to generate alongside llms.txt, and scored as bonus signal by both tools.
- **robots.txt content-usage statements** — an emerging convention for declaring what AI may do with your content (train / cite / summarize), so the answer comes from you instead of being assumed.
- **AI Catalog** (MAY, unmeasured) — a JSON manifest at `/.well-known/ai-catalog.json` listing every agent-facing resource you ship (MCP server card, OpenAPI, A2A agent card, docs, llms.txt, skills), linked from the homepage head with `<link rel="ai-catalog" href="/.well-known/ai-catalog.json">`. Registries index published catalogs so agents can search across sites. Cheap to add once you have more than one agent surface.

### 3. Parseability — once there, can the agent tell what the page is?

- **Valid, substantive structured data** (JSON-LD — see the `schema` skill). Most agents read a page's text, not its `<script>` blocks, and Markdown converters may drop them — so **repeat every critical fact as visible text**. A price that exists only in JSON-LD or a hydration payload (e.g. the annual price behind a pricing toggle) goes unseen.
- **Fenced, language-tagged code blocks.** When an agent's answer included code, 61% of the time it lifted lines verbatim from a page on the site.
- **A Markdown representation of the page** (MAY). Agents requested Markdown on ~65% of web fetches, but format did **not** change task success in Ora's controlled experiment — nor did content negotiation or agent detection. Make the HTML work first; add a mirror second. Two implementations:
  - **Content negotiation**: serve compact Markdown at the *same canonical URL* when the request asks for `Accept: text/markdown`, with a `Vary` header keeping the HTML and Markdown cache entries separate. (This is how Is Agentic serves its own reports — agents get Markdown, browsers get HTML, one URL.)
  - **Link header or tag**: an HTTP `Link` header, or `<link rel="alternate" type="text/markdown" href="/page.md">` in the head, pointing to a parallel Markdown version — discoverable without guessing URLs.
- Clear document structure — one H1, headings that answer sub-questions, extractable answer blocks (the content-patterns reference).

## Emerging: agent-actionable, not just agent-readable

Reading is close to solved: in Ora's April 2026 scan, 80% of sites were reachable to every major AI crawler, but only 3% shipped a spec-grade MCP server, and OAuth metadata checks passed on ~1%. AgentReady's act tier applies when the product should *complete* a task, not just be read about:

- **An MCP server or a CLI** (AR-ACT-10, MUST for acting) — the interface an agent acts through. MCP for agents in chat and IDE hosts, a CLI for agents in a shell. Ship the one that fits how the product is used; don't ship an empty surface to tick the box.
- **Auth an agent can finish** (AR-ACT-01) — self-serve API keys with documented scopes; for user-delegated access, OAuth 2.0 with discoverable metadata under `/.well-known` (RFC 8414, RFC 9728).
- **A public API with OpenAPI** (AR-ACT-02) — operation IDs, typed responses and errors, documented rate limits.

The next race is whether an agent can *act* on your site — fill the form, book the meeting, start the trial. **WebMCP** is the emerging standard here: a page declares its forms and CTAs as callable tools with input schemas, so an agent doesn't have to reverse-engineer your UI. Early days (label: emerging, not yet a ranking/citation signal), but the direction is clear — if agents are becoming buyers, the site that exposes "start trial" as a structured action wins the agent-mediated conversion that a pretty button loses.

Practical today: make sure your highest-intent actions (signup, pricing, demo booking, contact) work without JavaScript-only flows, have labeled semantic form fields, and return machine-readable confirmation.

**Ways to add WebMCP** (all early; confirm browser and assistant support before promising anything):
- **Implement it yourself.** Follow the WebMCP draft to declare each action as a tool with an input schema, wired to the form or API the page already uses. Keep the tool list short (the 2–4 highest-intent actions) and reuse existing validation, spam protection, and permissions rather than building a parallel path.
- **Use your platform's support, if it has any.** Some site platforms and agent workflows add WebMCP for you. Ploy ◆, for example, has a Ploybook that inspects the site, defines tool contracts, implements them against existing form logic, and validates them. It's a guided workflow, not a hosted MCP server. ◆ marks a [Verified Partner](https://github.com/coreyhaines31/marketingskills/blob/main/tools/REGISTRY.md#verified-partners) of this repository (disclosure, not endorsement); name an alternative alongside it when you mention it.
- **Have a coding agent do it** in the site's repo, with the same scoping: a few actions, existing logic, a test for each.

Whichever path, test that each tool rejects bad input, that submissions land where the normal form's do (CRM, inbox, conversion tracking), and that nothing bypasses consent or rate limits.

### Ship a skill file for your product

A lighter act surface than MCP or WebMCP: a public `SKILL.md` (linked from llms.txt and your docs) that a user loads into their own Claude Code or Cursor session. `llms.txt` tells an agent what you are; a skill file tells it how to buy or set up your product for this user, and it runs where the user's context already is.

**Case: LinkDR (October 2026).** The backlink marketplace's `linkdr.com/SKILL.md` has the agent inspect the user's site, propose the target page and anchor text, price the order from a published table, and return one checkout link. The founder described it as a sales funnel running inside the buyer's agent. The pattern is the point; the numbers are theirs.

What to put in it:
- **Use the context the agent already has.** Onboarding stalls where the buyer must make a decision they can't make yet (which URL, which plan, which integration). Tell the agent to read the user's repo or site and propose an answer with its reasoning, then let the user confirm.
- **Pricing as text in the file** — the full table and any volume or annual rules, so the agent quotes exact numbers instead of guessing.
- **A prefilled checkout or signup URL.** Once the user agrees, the agent packs the choices into query parameters (`/agent/checkout?plan=pro&seats=5&billing=annual`) and hands back one link. No auth, API keys, or MCP install. Recompute the price on the server and never trust an amount in the URL; validate every parameter; add a source parameter so agent-built orders show up in conversion tracking.
- **An offer for ordering through an agent is fine when it's stated as information** ("code AGENT50 takes $50 off"). The agent shows it; the user decides.
- **Test with the agents your buyers use.** Run the file in a few fresh sessions and check that the agent proposes sensible defaults, quotes the right prices, and builds a valid URL.

**Don't make it coercive.** Instructions that force an upsell on every user, or that are tuned until the agent always pushes your offer regardless of the user's goal, are the manipulation [agent-defaults.md](agent-defaults.md) warns about: agent platforms treat them as prompt injection, and users who notice stop trusting the tool. Recommend the option that fits the user's stated goal and budget, mention one larger option only when it serves that goal, and let the user say no.

For products an agent installs mid-task (developer tools, APIs, infrastructure), the next step past acting on your site is being the vendor the agent picks in the first place. See [agent-defaults.md](agent-defaults.md).

## Citation-source volatility (why you diversify)

Third-party citation mixes are **not stable** — they shift overnight with model and retrieval updates, and August 2026 provided the case study: **ChatGPT's query fan-out changes nearly wiped Reddit as a citation source** within days (practitioner-reported by multiple AEO teams; one had been earning 24-hour citations from Reddit at 1M+ impressions/month before the change). Meanwhile the same practitioners report **business-owned websites dominate Gemini citations (~60%)**.

LinkedIn moved in the same update: ChatGPT's LinkedIn citations fell ~36% in mid-August 2026, and its citations of Pulse articles fell ~86% from May to Oct while citations of feed posts rose. Perplexity and Copilot moved the other way. See [linkedin-ai-citations.md](linkedin-ai-citations.md).

What this means for strategy:

- **Never concentrate AI-visibility work in one third-party surface.** The Presence pillar's list (Wikipedia, Reddit, YouTube, podcasts, review sites, Quora) is a portfolio, not a menu to pick one from. A surface that's 2% of citations today can be 0% after one retrieval update — or vice versa.
- **Owned-site fundamentals hedge the volatility.** Platform deals and retrieval changes reshuffle third-party sources; your own agent-readable site is the one surface no platform can drop you from — and on Gemini it's already the dominant citation class.
- **Treat any citation-share statistic as dated.** The "Reddit = 1.8% of ChatGPT citations" class of stats (including the ones in this skill) are snapshots — check the date, and verify against your own citation monitoring (the DIY monitoring loop in SKILL.md) before betting budget on them.
- **Speed is real**: fresh content on retrieved surfaces can be cited within ~24 hours. AI search rewards freshness faster than classic SEO ever did.

---

*Agent-readiness check taxonomy distilled from Vercel/Ora's Is Agentic (is-agentic.com) and Frase's Agent Readiness Checker (both August 2026, credited); AgentReady practice IDs, strengths, and study figures from agentready.org and Ora's research (October 2026, credited — vendor-run, dataset public at github.com/ora/research); citation-volatility events practitioner-reported (Ashni of Hype Partners (@ashnichrist) and others, August 2026) — labeled accordingly, verify against your own monitoring.*



---

## `references/ai-attribution.md`

# Measuring AI Search Impact Past the Referral Click

AI answers influence buyers who never click a link. They read a recommendation, then search your brand or type your URL a few days later. Referral reports miss most of that, so "AI sends us almost no traffic" is usually a measurement gap, and the impact sits in other channels.

Profound joined more than two million AI conversations with later browsing behavior (Profound, July 2026; observational, US-only, measured site visits rather than purchases). Two findings shape the setup below:

- Only **42%** of the downstream visits after an AI assistant introduced a brand happened within 24 hours. A same-session window misses most of the effect.
- More than **97%** of those visits carried no AI referral parameter, even after ChatGPT made its links easier to click.

SimilarWeb's journey data points the same way: about 9% of post-recommendation visits arrived as visible AI referrals (see [citations-vs-recommendations.md](citations-vs-recommendations.md)). Profound sells AI visibility tracking, so treat its numbers as vendor research, and don't present either study's lift as a forecast for one brand.

## Four layers

Report each layer separately. Rising visibility does not prove rising revenue.

| Layer | What it captures | Where it comes from |
|---|---|---|
| **Exposure** | Mentions, recommendations, prominence, framing, citations | Prompt tracking (see [prompt-portfolio.md](prompt-portfolio.md)) |
| **Immediate behavior** | AI referral sessions, landing pages, engaged sessions | Analytics, with AI referrers grouped (see the **analytics** skill) |
| **Delayed behavior** | Branded search, direct visits, return visits, cross-session conversions | Search Console branded queries, analytics, CRM |
| **Business outcome** | Signups, leads, qualified pipeline, purchases, revenue, retention | CRM and billing |

## Setup

1. **Name the decision.** "Should we keep funding AEO content?" needs a different design from "Did fixing our pricing page change anything?"
2. **Define exposure** by engine, prompt cohort, market, language, and date, so you know what changed and when.
3. **Fix referral capture.** Group known AI referrers (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai, and so on) into one channel. Preserve landing page, referrer, and query parameters. Expect it to undercount.
4. **Add delayed windows.** Measure branded search and direct visits to exposed pages over 1-hour, 24-hour, and 7-day windows after a known exposure change.
5. **Ask people.** A "How did you hear about us?" field with an AI option and a "What did you ask?" follow-up, plus tagged sales-call notes, catch journeys analytics can't see.
6. **Join to outcomes** in the CRM without counting the same conversion twice across layers.

## Evaluation designs

Pick the strongest design you can afford, and say which one you used.

| Design | Use when | Confidence |
|---|---|---|
| **Holdout** | You can leave comparable pages, products, or markets untouched | Highest |
| **Matched comparison** | Similar pages or markets exist, but you can't randomize | Medium |
| **Interrupted time series** | One clear intervention date and a long, stable baseline | Medium |
| **Pre/post on a stable cohort** | Nothing better is possible | Low; confounders easily swamp it |
| **Exposure panel or incrementality study** | Budget for a vendor panel | Varies with the panel's method |

List confounders before reading results: campaigns, launches, press, seasonality, pricing changes, and model or retrieval updates.

## Reporting language

Say which of three things you have: an **observation** ("branded search rose 18% after the change"), an **association** ("pages with more AI mentions saw more direct visits"), or a **causal result** ("the holdout pages didn't move; the treated pages did"). Most AEO reporting only supports the first two. Say so.

Respect privacy rules in panel and self-reported data: aggregate small groups and follow your consent and retention policies.

---

*Framework lineage: the four-layer model, attribution windows, and evaluation designs adapted (re-expressed and restructured) from Profound's MIT-licensed ai-search-attribution-planner skill and its "AI mention effect" study (July 2026), credited.*



---

## `references/answer-accuracy.md`

# Answer Accuracy: Auditing What AI Says About You

Visibility counts whether you appear. Accuracy checks what the answer says once you do. A brand can show up in every answer and still be described with last year's pricing, a missing integration, or a limitation it fixed months ago.

Much of an answer is commentary the user never asked for. Profound's analysis of 50,000 responses (Profound, June 2026) found about 47% of response content was unsolicited editorial material: comparisons, rankings, caveats, and recommendations. That editorial layer is where wrong claims about you tend to live.

Profound sells AI visibility tracking, so treat its figures as vendor research. Other trackers that capture answer text for this kind of audit include Ahrefs Brand Radar, Semrush's AI toolkit, Peec AI, Otterly, and ZipTie.

## When to run it

- An assistant states a wrong price, plan limit, feature, or compatibility claim
- Sales hears prospects repeat something false that "ChatGPT said"
- After a repositioning, pricing change, rebrand, or product retirement
- Quarterly for any brand with a regulated, safety, or pricing-sensitive product

## The claim ledger

Capture answers first, then log one row per claim. Record the engine, model or surface, locale, prompt, and capture date for every answer, since a claim you can't reproduce is hard to fix.

| Field | What goes in it |
|---|---|
| Engine and date | ChatGPT (search on), Gemini, AI Overviews, Perplexity, Copilot, Claude; capture date |
| Prompt | Exact wording, plus which prompt family it belongs to (see [prompt-portfolio.md](prompt-portfolio.md)) |
| Claim | The sentence as the model wrote it |
| Claim type | Price, availability, compatibility, feature, limitation, comparison, ranking, recommendation, caveat, sentiment |
| Verdict | One of the seven below |
| Evidence | The current source that confirms or contradicts it |
| Likely source | The page the claim probably came from: your page, docs, a feed, a profile, a third-party article, a forum thread, or unknown |
| Severity | Critical, high, medium, or low |
| Owner | Who fixes the source |

Extract every claim that could change a buying decision, including the ones the user didn't ask about. A question about pricing that comes back with an unprompted "but it lacks SSO" is two claims.

### Seven verdicts

1. **Accurate and current**
2. **Accurate but incomplete**: true, but missing the fact that matters (the free plan exists, but the answer omits its limits)
3. **Ambiguous**: could be read as true or false
4. **Stale**: was true, isn't now
5. **False**
6. **Subjective framing**: an opinion stated as fact ("best for small teams," "hard to set up")
7. **Unverifiable**: no current source either way

Check first-party facts against your own current product material, and claims about the outside world against reliable independent sources. Your preferred marketing wording is not evidence.

### Severity

| Level | Examples |
|---|---|
| **Critical** | Safety, legal, eligibility, price, availability, or compatibility errors that could cause a bad purchase or real harm |
| **High** | False comparisons, invented limitations, stale product facts in high-value prompt families |
| **Medium** | Incomplete or slanted framing that could plausibly change a decision |
| **Low** | Tone and wording that don't change the decision |

Weight severity by exposure too: a medium error that appears in every run of your top commercial prompt outranks a high error in one obscure prompt.

## Fix the source first

The answer is downstream of what the model retrieved or learned. Rewriting your homepage copy rarely fixes a claim that comes from a stale third-party review.

1. **Trace it.** Search the claim's wording, check which sources the engine cited for that answer, and look for the page where the wrong fact lives.
2. **Fix your own sources.** State the correct fact plainly on the page that should own it, with a date: pricing page, docs, changelog, comparison page, help center. Remove or redirect the outdated page. Update feeds and structured data that carry the same fact.
3. **Fix your profiles.** G2, Capterra, app marketplaces, Crunchbase, LinkedIn, and partner directories often hold the stale version.
4. **Ask third parties for factual corrections only.** Send the publisher the correct fact and a source. Don't ask them to remove legitimate criticism.
5. **Retest** the same prompts after a set observation window (4–8 weeks is a reasonable starting point), with a few controlled variants. Report movement over time; one clean run proves nothing.

Never promise that a source fix will change the answer. Models retrain and re-retrieve on their own schedules.

**Off limits:** fabricated corrections, editing Wikipedia about yourself, astroturfed forum posts, and pressuring publishers to pull fair criticism. These break platform rules, and models are getting better at discounting them.

## Report

1. Accuracy rate across the cohort, the riskiest narrative, and the main source problem
2. The claim ledger
3. Owned-source fixes, each with the exact fact and the page that should state it
4. Third-party correction requests, factual and sourced
5. The retest plan and date
6. Unknowns

This audit pairs with the positioning work in [positioning-and-consensus.md](positioning-and-consensus.md): accuracy fixes wrong facts, positioning fixes the wrong story. The AI-accuracy audit loop in **marketing-loops** can schedule it.

---

*Framework lineage: claim ledger, verdict set, and severity scale adapted (re-expressed and restructured) from Profound's MIT-licensed ai-answer-accuracy-auditor skill and its "Parrot Problem" research (June 2026), credited.*



---

## `references/citations-vs-recommendations.md`

# Citations vs. Recommendations: The AI Visibility Ladder

Being cited by an AI engine and being recommended by it are **two different outcomes governed by two different systems**. A citation means your page was useful enough to pull information from. A recommendation means the model put your brand on the buyer's shortlist. Optimizing for the first does not automatically earn the second — and for smaller brands, conflating them leads to content strategies that can actively help competitors.

Source note: the analysis and data in this reference draw on Lily Ray's (Amsive) 2026 study of B2B "best [category] software" queries, behavioral studies by Scrunch and SimilarWeb, and commentary by John-Henry Scherck (Growth Plays). The citation-mix taxonomy and decision rules are adapted (re-expressed and restructured) from Profound's MIT-licensed ai-citation-mix-strategist skill, credited.

---

## The Visibility Ladder

AI visibility is a ladder, not a binary. Each rung has different selection criteria and different measurement:

| Rung | What it means | What governs it | How to see it |
|---|---|---|---|
| **1. Retrieved** | The model read your content while building its answer, without citing it | Crawlability, parseable structure, query relevance | Mostly invisible; bot logs hint at it |
| **2. Cited** | Your page appears as a source in the answer | Content usefulness: structure, statistics, clarity, freshness | Prompt-tracking tools, AI Overview source lists |
| **3. Mentioned** | Your brand is named in the answer text | Entity recognition + how the web talks about you | Prompt-tracking tools |
| **4. Recommended** | Your product is on the shortlist the buyer actually considers | **Aggregate web consensus** — reviews, forums, analysts, press, video — largely independent of your own content | Prompt tracking + the framing around the mention |

Rungs 1–3 are legitimate signals your content is working, and most prompt-tracking tools report them. But rung 4 is where buying behavior changes, and it's earned differently: **citation is about whether your content is useful to consult; recommendation is mostly a reflection of what the broader web says about you** — whether you published a guide on the topic or not.

There is also a shadow rung: **recommended against**. On detailed, requirements-heavy prompts, models increasingly name products a buyer should *avoid* for their use case, with sources. The downside of weak third-party consensus is no longer just absence from the shortlist — it can be an explicit rule-out. This makes monitoring the *framing* around your mentions (favorable / neutral / hedged / negative), not just counting them, part of the job.

**Repairing a weakness models repeat.** Address it in public, with specifics, from a real person. One practitioner's client was "slaughtered" on implementation time; over 1.5–2 years, founder posts about the process, guides on real timelines, and a concrete "4–8 weeks" on the implementation page shifted how models described it (anecdote, Harpreet Singh on Edward Sturm's podcast, Sep 2026). More in [positioning-and-consensus.md](positioning-and-consensus.md).

---

## The Self-Promotional Listicle Risk

The common tactic — publish a "best [category] software" guide, rank yourself #1, and let it shape both organic search and AI answers — now has a stage-dependent payoff.

**The data:** Lily Ray (Amsive) analyzed 100 B2B "best [category] software" queries across three dates in spring 2026. Across the dataset, self-promotional listicles earned 323 citations in AI Overviews — and in 224 of them (**69% of the citations**), the answer left the publishing brand out of the recommendations, pointing buyers to competitors instead.

**The mechanism:** the model treats your guide as a source about the *category*. It happily extracts the competitor names, comparisons, and evaluation criteria you compiled — then makes its recommendation from web-wide consensus, where the established players dominate. For an emerging brand, a self-promotional buyer's guide can function as **a vote for your competitors**: you did the research that helps the model describe them.

**The split by stage:**

- **Established category leaders** get both outcomes. Their guides earn citations *and* their brands get recommended — because analysts, review sites, and forum discussions already validate them. For leaders, a definitive buyer's guide is highly advantageous: it shapes how the whole category (competitors included) gets described.
- **Emerging brands** may win the citation and even shape the category's framing, but miss the recommendation. That's not a wasted outcome — influencing how an LLM defines the category and its evaluation criteria is real positioning work — but it is not the shortlist placement the tactic promises.

**What this changes (and doesn't):** genuinely useful buyer's guides still belong in a B2B content strategy at any stage. What changes is the expectation and the investment split. If you're not yet the consensus pick, weight effort toward the offsite signals that actually govern recommendations (below) rather than publishing a plethora of self-ranked listicles.

**A third option between ranking yourself #1 and not writing the guide:** name the category leader first, say honestly what it does well, then show the specific cases where your product goes further (practitioner pattern, Sep 2026). It reads as a fair source, which is what models are now starting to filter for.

---

## What Earns Recommendations

Recommendation is a consensus signal. The inputs the models weigh live mostly off your site:

| Channel | Why it moves recommendations | Related skill |
|---|---|---|
| **Review platforms** (G2, Capterra, TrustRadius, app stores) | Third-party validation models treat as evidence of legitimacy | customer-research (review generation loops) |
| **Analyst coverage** (Gartner, Forrester, industry reports) | High-authority category framing; models echo analyst shortlists | public-relations |
| **Communities and forums** (Reddit, HN, Slack/Discord, niche forums) | Unprompted practitioner discussion is heavily retrieved and hard to fake | community-marketing |
| **Earned media and PR** | Independent sources repeating your positioning beyond your own site | public-relations |
| **Video and podcasts** | Increasingly retrieved; transcripts carry brand + category associations | video, social |

The test to apply before investing in another self-ranked guide: *if a model ignored everything on our domain, would the rest of the web still put us on the shortlist?* If not, that gap is the priority. AEO discourse often stops at "are we in the answer?" — the better question is "are we credible enough to be recommended?"

The encouraging flip side: earning an AI recommendation is harder to game than a top search ranking ever was. The durable strategy is the same at every stage — be the best fit for a clear set of buyers, and give those buyers reasons to talk about you in public, where the models can retrieve it.

---

## Reading the Citation Mix Before Picking Channels

"Do more PR" and "post on Reddit" are guesses until you know which sources the engines actually cite for your prompts. The mix differs sharply by engine and industry. Profound's analysis of 11.84 billion citations across eight models and 29 industries found about 57% went to company-operated sites overall, with ChatGPT at 47% and Gemini at 69%; in 24 of 29 industries, the median Profound customer got more citations from brand sites than from earned or social sources (Profound, July 2026). Profound sells AI visibility tracking, so treat this as vendor research. Ahrefs Brand Radar, Semrush, Peec AI, and Otterly also report cited domains you can classify the same way.

**Classify every cited source** across a stable prompt sample, split by engine and prompt cluster:

| Class | Examples | Roll-up |
|---|---|---|
| Your own site | Product, docs, pricing, blog | Owned |
| Competitor or adjacent company site | A rival's comparison page, a partner's docs | Owned (someone else's) |
| Earned editorial | Trade press, independent reviews, newsletters | Earned |
| Institutional or primary authority | Standards bodies, government, universities, analyst firms | Earned |
| PR wire | Press release distribution | Earned |
| Social and user-generated | Reddit, YouTube, LinkedIn, forums | Community |
| Marketplace, directory, or review platform | G2, Capterra, app stores, Amazon | Community |
| Other or unknown | Anything you can't classify yet | Unclassified |

Diagnose with the granular classes; report to executives with the three roll-ups. Separate sources that cite *you* from sources that only shape the surrounding answer.

**Then follow the mix:**

- **Engines already cite company sites, and yours lacks the facts:** strengthen owned content first. State specific, current facts on the page that should own them.
- **Editorial or institutional sources dominate:** pursue earned coverage and analyst inclusion. The **link-building** skill turns the cited pages into a prospect list.
- **Communities contribute materially:** participate where you can do it honestly and in your own name. Skip communities the engines don't cite.
- **Competitor pages get cited:** read them for the facts and framing you're missing. Don't copy them.
- **Engines disagree:** plan per engine. A blended average can hide opposite behavior.

Re-measure on the same prompt cohort over time; mixes shift with retrieval updates (see the volatility section in [agent-readiness.md](agent-readiness.md)).

---

## What a Recommendation Is Worth

Two behavioral studies quantified the gap between rungs:

- **Scrunch** (opt-in panel linking AI conversations to subsequent web behavior, compared against each user's own baseline — observational, not a controlled experiment): a genuine recommendation ("a great option is X") was associated with people searching for, visiting, and evaluating a brand **about twice as often** as a passing mention. For users with no recent observed engagement with the brand, a recommendation was followed within a week by **+182% branded searches, +117% site visits, and +185% product views**.
- **SimilarWeb** (thousands of real user journeys, seven days post-answer): when ChatGPT recommended a brand, it received **roughly 2.5× more new visitors** the following week than the competitors left off the list.

**The attribution blind spot:** in the SimilarWeb data, only about **9%** of those post-recommendation visits arrived as visible AI referral traffic; the largest share arrived via branded search, with direct and other channels making up the rest — indistinguishable from ordinary organic visitors. AI recommendations are already sending real, engaged buyers, but standard attribution underreports the AI touch.

**Measurement triad** (no single signal is complete; together they give a reliable read):

1. **AI prompt tracking** — whether and how you're mentioned/recommended in LLM answers, even when no click ever lands (tools in SKILL.md's Monitoring section). Track the framing around mentions — recommended, neutral, hedged, or recommended-against — not just the count.
2. **Self-reported attribution** — a "how did you hear about us?" field catches buyers whose journey started in an AI chat but arrived via branded search or direct. Add an AI option with a follow-up, "What did you type?", so buyers hand you real prompts to track. ChatGPT referral UTMs undercount, and AI Overview revenue can't be separated from organic in analytics, so this field is often the clearest signal you have.
3. **Sales call recordings** — buyers' own language often reveals an AI conversation shaped the shortlist long before any form fill.

Also watch **branded search volume** as a proxy: sustained lifts without a matching campaign are increasingly AI-influence showing up under another name.

---

## Applying This

- **Auditing an established brand:** buyer's guides and comparison content are high-leverage — publish the definitive version and shape the category's evaluation criteria.
- **Auditing an emerging brand:** publish the genuinely useful guides your ICP needs, but set expectations (citation and framing, not near-term recommendation) and rebalance investment toward reviews, communities, analysts, and earned media.
- **Reporting:** report the ladder, not a single "AI visibility" number — retrieved/cited/mentioned/recommended plus mention framing. A rising citation count with a flat recommendation rate is a specific, diagnosable gap: the web doesn't yet corroborate your content.
- **Risk check:** for requirements-heavy queries in your category, check whether models recommend *against* you, and trace the sources they cite when they do.



---

## `references/content-patterns.md`

# AEO and GEO Content Patterns

Reusable content block patterns optimized for answer engines and AI citation.

---

## Contents
- Answer Engine Optimization (AEO) Patterns (Definition Block, Step-by-Step Block, Comparison Table Block, Pros and Cons Block, FAQ Block, Listicle Block)
- Generative Engine Optimization (GEO) Patterns (Statistic Citation Block, Expert Quote Block, Authoritative Claim Block, Self-Contained Answer Block, Evidence Sandwich Block)
- Fact-Family Fan-Out Matrix
- Domain-Specific GEO Tactics (Technology Content, Health/Medical Content, Financial Content, Legal Content, Business/Marketing Content)
- Voice Search Optimization (Question Formats for Voice, Voice-Optimized Answer Structure)

## Answer Engine Optimization (AEO) Patterns

These patterns help content appear in featured snippets, AI Overviews, voice search results, and answer boxes.

### Definition Block

Use for "What is [X]?" queries.

```markdown
## What is [Term]?

[Term] is [concise 1-sentence definition]. [Expanded 1-2 sentence explanation with key characteristics]. [Brief context on why it matters or how it's used].
```

**Example:**
```markdown
## What is Answer Engine Optimization?

Answer Engine Optimization (AEO) is the practice of structuring content so AI-powered systems can easily extract and present it as direct answers to user queries. Unlike traditional SEO that focuses on ranking in search results, AEO optimizes for featured snippets, AI Overviews, and voice assistant responses. This approach has become essential as over 60% of Google searches now end without a click.
```

### Step-by-Step Block

Use for "How to [X]" queries. Optimal for list snippets.

```markdown
## How to [Action/Goal]

[1-sentence overview of the process]

1. **[Step Name]**: [Clear action description in 1-2 sentences]
2. **[Step Name]**: [Clear action description in 1-2 sentences]
3. **[Step Name]**: [Clear action description in 1-2 sentences]
4. **[Step Name]**: [Clear action description in 1-2 sentences]
5. **[Step Name]**: [Clear action description in 1-2 sentences]

[Optional: Brief note on expected outcome or time estimate]
```

**Example:**
```markdown
## How to Optimize Content for Featured Snippets

Earning featured snippets requires strategic formatting and direct answers to search queries.

1. **Identify snippet opportunities**: Use tools like Semrush or Ahrefs to find keywords where competitors have snippets you could capture.
2. **Match the snippet format**: Analyze whether the current snippet is a paragraph, list, or table, and format your content accordingly.
3. **Answer the question directly**: Provide a clear, concise answer (40-60 words for paragraph snippets) immediately after the question heading.
4. **Add supporting context**: Expand on your answer with examples, data, and expert insights in the following paragraphs.
5. **Use proper heading structure**: Place your target question as an H2 or H3, with the answer immediately following.

Most featured snippets appear within 2-4 weeks of publishing well-optimized content.
```

### Comparison Table Block

Use for "[X] vs [Y]" queries. Optimal for table snippets.

```markdown
## [Option A] vs [Option B]: [Brief Descriptor]

| Feature | [Option A] | [Option B] |
|---------|------------|------------|
| [Criteria 1] | [Value/Description] | [Value/Description] |
| [Criteria 2] | [Value/Description] | [Value/Description] |
| [Criteria 3] | [Value/Description] | [Value/Description] |
| [Criteria 4] | [Value/Description] | [Value/Description] |
| Best For | [Use case] | [Use case] |

**Bottom line**: [1-2 sentence recommendation based on different needs]
```

### Pros and Cons Block

Use for evaluation queries: "Is [X] worth it?", "Should I [X]?"

```markdown
## Advantages and Disadvantages of [Topic]

[1-sentence overview of the evaluation context]

### Pros

- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]
- **[Benefit category]**: [Specific explanation]

### Cons

- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]
- **[Drawback category]**: [Specific explanation]

**Verdict**: [1-2 sentence balanced conclusion with recommendation]
```

### FAQ Block

Use for topic pages with multiple common questions. Essential for FAQ schema.

```markdown
## Frequently Asked Questions

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].

### [Question phrased exactly as users search]?

[Direct answer in first sentence]. [Supporting context in 2-3 additional sentences].
```

**Tips for FAQ questions:**
- Use natural question phrasing ("How do I..." not "How does one...")
- Include question words: what, how, why, when, where, who, which
- Match "People Also Ask" queries from search results
- Keep answers between 50-100 words

### Listicle Block

Use for "Best [X]", "Top [X]", "[Number] ways to [X]" queries.

**Caveat for self-promotional listicles:** ranking yourself #1 in your own "best [category]" guide gets the page *cited* far more reliably than it gets your brand *recommended* — for emerging brands, AI answers often harvest the competitor names from the guide and recommend them instead. See [citations-vs-recommendations.md](citations-vs-recommendations.md) before building these at scale.

```markdown
## [Number] Best [Items] for [Goal/Purpose]

[1-2 sentence intro establishing context and selection criteria]

### 1. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]

### 2. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]

### 3. [Item Name]

[Why it's included in 2-3 sentences with specific benefits]
```

---

## Generative Engine Optimization (GEO) Patterns

These patterns optimize content for citation by AI assistants like ChatGPT, Claude, Perplexity, and Gemini.

### Statistic Citation Block

Statistics increase AI citation rates by 15-30%. Always include sources.

```markdown
[Claim statement]. According to [Source/Organization], [specific statistic with number and timeframe]. [Context for why this matters].
```

**Example:**
```markdown
Mobile optimization is no longer optional for SEO success. According to Google's 2024 Core Web Vitals report, 70% of web traffic now comes from mobile devices, and pages failing mobile usability standards see 24% higher bounce rates. This makes mobile-first indexing a critical ranking factor.
```

### Expert Quote Block

Named expert attribution adds credibility and increases citation likelihood.

```markdown
"[Direct quote from expert]," says [Expert Name], [Title/Role] at [Organization]. [1 sentence of context or interpretation].
```

**Example:**
```markdown
"The shift from keyword-driven search to intent-driven discovery represents the most significant change in SEO since mobile-first indexing," says Rand Fishkin, Co-founder of SparkToro. This perspective highlights why content strategies must evolve beyond traditional keyword optimization.
```

### Authoritative Claim Block

Structure claims for easy AI extraction with clear attribution.

```markdown
[Topic] [verb: is/has/requires/involves] [clear, specific claim]. [Source] [confirms/reports/found] that [supporting evidence]. This [explains/means/suggests] [implication or action].
```

**Example:**
```markdown
E-E-A-T is the cornerstone of Google's content quality evaluation. Google's Search Quality Rater Guidelines confirm that trust is the most critical factor, stating that "untrustworthy pages have low E-E-A-T no matter how experienced, expert, or authoritative they may seem." This means content creators must prioritize transparency and accuracy above all other optimization tactics.
```

### Self-Contained Answer Block

Create quotable, standalone statements that AI can extract directly.

```markdown
**[Topic/Question]**: [Complete, self-contained answer that makes sense without additional context. Include specific details, numbers, or examples in 2-3 sentences.]
```

**Example:**
```markdown
**Ideal blog post length for SEO**: The optimal length for SEO blog posts is 1,500-2,500 words for competitive topics. This range allows comprehensive topic coverage while maintaining reader engagement. HubSpot research shows long-form content earns 77% more backlinks than short articles, directly impacting search rankings.
```

### Evidence Sandwich Block

Structure claims with evidence for maximum credibility.

```markdown
[Opening claim statement].

Evidence supporting this includes:
- [Data point 1 with source]
- [Data point 2 with source]
- [Data point 3 with source]

[Concluding statement connecting evidence to actionable insight].
```

---

## Fact-Family Fan-Out Matrix

Engines rewrite a prompt into several background searches before answering, and those searches are often plain fact lookups even when the prompt asked for advice. In Profound's 14-day tracking of 10,000 prompts, ChatGPT, Perplexity, and Copilot each ran roughly 1.4–2 searches per answer, but 91% of ChatGPT's search queries were unique across repeated runs, against 14% for Perplexity and 47% for Copilot (Profound, April 2026; observational, vendor research). Exact query strings won't repeat, so plan content around the stable **fact families** underneath them.

1. **Pick a prompt family**, with its audience, buying stage, engine, and market.
2. **List the fan-outs.** Use observed queries where you have them (ChatGPT's background queries can be extracted; see [format-volatility.md](format-volatility.md)). Otherwise infer them, and mark every inferred row as a hypothesis.
3. **Break the job into fact families:** entities and category terms, factual sub-questions, comparison criteria, constraints (price, compatibility, location, recency), and the evidence that settles them (standards, definitions, reviews, primary data).
4. **Fill the matrix**, one row per fact family:

| Fact family | Observed or inferred | What the buyer needs | Current best source | Competitor source | Our owning page | Gap |
|---|---|---|---|---|---|---|
| Pricing for 10 seats | Observed | Monthly cost at 10 seats, annual discount | Third-party review (2025 prices) | Competitor pricing page | /pricing | Per-seat price not stated in text |
| SOC 2 status | Inferred | Report type and date | None | Competitor trust page | /security | Page says "enterprise-grade," no report type |

5. **Give each fact one owning page.** Improve or consolidate an existing page before creating a new one, and create one only when a real information gap exists. One strong page can answer several fact families. Never build a doorway page per fan-out query.
6. **Retest across repeated runs and engines.** Expect different retrieval paths each time; judge by whether the fact family gets answered from your page.

Engine priors to verify before relying on them: ChatGPT ranges widely across vocabulary and adjacent questions; Perplexity stays close to the prompt's own terms; Copilot compresses prompts into short search-style queries.

*Adapted (re-expressed and restructured) from Profound's MIT-licensed ai-retrieval-fanout-mapper skill and its April 2026 study, credited.*

---

## Domain-Specific GEO Tactics

Different content domains benefit from different authority signals.

### Technology Content
- Emphasize technical precision and correct terminology
- Include version numbers and dates for software/tools
- Reference official documentation
- Add code examples where relevant

### Health/Medical Content
- Cite peer-reviewed studies with publication details
- Include expert credentials (MD, RN, etc.)
- Note study limitations and context
- Add "last reviewed" dates

### Financial Content
- Reference regulatory bodies (SEC, FTC, etc.)
- Include specific numbers with timeframes
- Note that information is educational, not advice
- Cite recognized financial institutions

### Legal Content
- Cite specific laws, statutes, and regulations
- Reference jurisdiction clearly
- Include professional disclaimers
- Note when professional consultation is advised

### Business/Marketing Content
- Include case studies with measurable results
- Reference industry research and reports
- Add percentage changes and timeframes
- Quote recognized thought leaders

---

## Voice Search Optimization

Voice queries are conversational and question-based. Optimize for these patterns:

### Question Formats for Voice
- "What is..."
- "How do I..."
- "Where can I find..."
- "Why does..."
- "When should I..."
- "Who is..."

### Voice-Optimized Answer Structure
- Lead with direct answer (under 30 words ideal)
- Use natural, conversational language
- Avoid jargon unless targeting expert audience
- Include local context where relevant
- Structure for single spoken response



---

## `references/content-types.md`

# AI SEO by Content Type

Tactical guidance for optimizing specific content types for AI search citation. These tactics work for non-Google AI engines (ChatGPT, Claude, Perplexity, Copilot) and don't hurt Google AI Overviews / AI Mode.

For the cross-cutting strategy, see [SKILL.md](../SKILL.md).

---

## SaaS Product Pages

**Goal:** Get cited in "What is [category]?" and "Best [category]" queries. (Citation is the realistic goal here; being *recommended* in the answer depends on offsite consensus — see [citations-vs-recommendations.md](citations-vs-recommendations.md).)

**Optimize:**
- Clear product description in first paragraph (what it does, who it's for)
- Feature comparison tables (you vs. category, not just competitors)
- Specific metrics ("processes 10,000 transactions/sec" not "blazing fast")
- Customer count or social proof with numbers
- Pricing transparency (AI cites pages with visible pricing) — add a `/pricing.md` file so AI agents can parse your plans without rendering your page (see "Machine-Readable Files" in the main skill)
- FAQ section addressing common buyer questions

---

## Blog Content

**Goal:** Get cited as an authoritative source on topics in your space.

**Optimize:**
- One clear target query per post (match heading to query)
- Definition in first paragraph for "What is" queries
- Original data, research, or expert quotes
- "Last updated" date visible
- Author bio with relevant credentials
- Internal links to related product/feature pages

---

## Comparison / Alternative Pages

**Goal:** Get cited in "[X] vs [Y]" and "Best [X] alternatives" queries.

**Optimize:**
- Structured comparison tables (not just prose)
- Fair and balanced (AI penalizes obviously biased comparisons)
- Specific criteria with ratings or scores
- Updated pricing and feature data
- Cite the `competitors` skill for building these pages

---

## Industry / Segment Pages

**Goal:** Get recommended when a prompt names an industry or company size ("email marketing software for e-commerce," "RFP software for government," "enterprise [category]"). Models increasingly sort brands into segments and personalize answers, so a generic page can lose to a competitor's segment page.

**Optimize:**
- One page per core industry or segment you actually serve, with industry-specific workflows, integrations, compliance, and customer proof
- Start with core segments. Many pages are fine if each adds real, segment-specific value; templated pages that only swap the industry name are what the scaled-content policy targets (see the `programmatic-seo` skill)
- Match the segment language used on your third-party profiles (see [positioning-and-consensus.md](positioning-and-consensus.md))

---

## Documentation / Help Content

**Goal:** Get cited in "How to [X] with [your product]" queries.

**Optimize:**
- Step-by-step format with numbered lists
- Code examples where relevant
- HowTo schema markup
- Screenshots with descriptive alt text
- Clear prerequisites and expected outcomes

---

## Local Business / Ecom (Google emphasis)

Google's AI features pull from product feeds and business profiles for local + ecom queries. Optimize:

- **Merchant Center feeds** kept current with accurate inventory, pricing, attributes
- **Google Business Profile** complete with hours, services, photos, posts, Q&A answered
- **Reviews** — recent + sufficient volume; respond to reviews to signal active management
- **Service area schema** for local services
- **Business Agent** (where available) for conversational customer engagement



---

## `references/format-volatility.md`

# Format Volatility — Which Content Formats AI Cites (and How Fast That Changes)

Citation-*source* volatility (Reddit wiped overnight, Gemini favoring owned sites) is covered in [agent-readiness.md](agent-readiness.md). This reference covers the second volatility axis: citation-*format* — which page types AI engines retrieve and cite, and the August 2026 evidence that heavily-exploited formats get demoted.

Read this before recommending comparison pages, listicles, or "best X" content for AI visibility. The advice changed materially with ChatGPT 5.6.

## The ChatGPT 5.6 format shift (August 2026)

Data from Peec AI (shared by Tomek Rudzki via Lily Ray, Aug 2026), comparing ChatGPT retrieval behavior before and after the 5.6 launch:

**Fan-out queries** — the modifiers that declined most as a share of ChatGPT's background searches:

- "vs"
- "comparison"
- "top"
- "best"
- "reviews"

At the same time: a surge in `site:` searches and modifiers like **"official"**.

**Citations by page type** — share of total ChatGPT citations:

| Page type | Pre-5.6 | Post-5.6 | Change |
|---|---:|---:|---:|
| Listicles ("Top 10 X," "8 best Y") | 15.77% | 7.80% | **−50.5%** |
| Comparison pages ("X vs Y," alternatives) | 9.08% | 6.17% | **−32.1%** |

The interpretation (Lily Ray's, and it fits the fan-out data): these are exactly the two formats companies scaled for GEO over the prior 18 months, and ChatGPT adjusted retrieval to mitigate the spam. The `site:`/"official" surge points the same direction — **toward primary sources and owned domains, away from aggregator formats**.

## What this changes (and what it doesn't)

**It does NOT mean "stop making comparison pages."** Comparison and best-of content still:

- Converts human buyers (its original job)
- Gets cited by Google AI Overviews (which follow core rankings, not ChatGPT's retrieval)
- Feeds Gemini and Perplexity, which haven't shown the same demotion
- Answers real mid-funnel queries on your own site

**It DOES mean:**

1. **Stop justifying scaled listicle/comparison production with "it wins AI citations."** On ChatGPT — the largest AI answer surface — that rationale lost half its force in one release.
2. **The "official"/primary-source shift favors your owned pages.** Product pages, docs, pricing pages, original research — the pages only you can publish — are rising as the citable class. This compounds the Gemini finding (business-owned sites ≈ 60% of citations).
3. **Format strategy is now per-platform.** Check which engines matter for your category before choosing formats:

| Format | ChatGPT (post-5.6) | Google AIO | Gemini | Perplexity |
|---|---|---|---|---|
| Listicles / best-of | Demoted | Rankings-dependent | OK | OK |
| Comparison / vs pages | Demoted | Rankings-dependent | OK | OK |
| Original research + data | Strong | Strong | Strong | Strong |
| Product/docs/pricing (owned, "official") | **Rising** | Strong | **Dominant** | Strong |
| How-to / guides | Steady | Strong | OK | Strong |

*(Table caveat: the demotion was measured on ChatGPT only. "OK" for Gemini/Perplexity means no demotion has been reported there — not that stability was measured. Any engine can ship its own 5.6-style shift.)*

4. **Treat every number above as a dated snapshot.** Same doctrine as source volatility: these are Aug 2026 measurements of a moving system. Verify against your own citation monitoring before betting budget.

## LinkedIn as a citation surface

LinkedIn is among the most-cited domains for professional queries, but the surface mix shifted during 2026 and differs by engine: ChatGPT moved from Pulse articles to feed posts, Perplexity and Copilot still cite articles and company pages, and Gemini barely cites LinkedIn at all. A post's first words still become its URL slug, so front-load the target phrase.

Correction: LinkedIn's guide doesn't say Articles get ~60% of citations versus ~40% for Posts. It says articles, newsletters, and posts *combined* account for 60%. Third-party splits put Articles ahead overall (roughly 60–70% vs 25–35%), but not on ChatGPT anymore.

Full breakdown by engine, crawler access, a `noindex` self-check, and what makes posts citable: [linkedin-ai-citations.md](linkedin-ai-citations.md).

## DIY diagnostic: extract ChatGPT's real fan-out queries

You don't need a tool to see what ChatGPT actually searches for in your niche (method circulating publicly, Aug 2026):

1. Run an important query for your category in ChatGPT (with search).
2. Open DevTools → Network tab, refresh the conversation (URL id after `/c/`).
3. Find the conversation response payload and search it for `queries`.
4. You'll see the literal background searches ChatGPT fanned out to.

**Use it for:** building your query-test list from *real* fan-out behavior instead of guesses; checking whether your category's fan-outs still use "best/vs" modifiers or have shifted to `site:`/"official" patterns; finding sub-topics your content doesn't cover.

**Then work backwards from the domains.** If the fan-out runs `site:` searches on third-party sources (Gartner, G2, Capterra) for your category, those profiles are your priority list, often ahead of new pages on your own site. See [positioning-and-consensus.md](positioning-and-consensus.md).

**Do not use it for:** auto-generating and mass-publishing an article per fan-out query. That's the exact scaled-content pattern 5.6 demoted (and Google's scaled content abuse policy names). The diagnostic is for coverage planning, not content spam.

## Measurement rigor: AI answers are non-deterministic

A single ChatGPT answer is an anecdote, not a measurement — the same prompt returns different sources run-to-run. (The statistical-rigor framing here is popularized by Initial Commit's AEO audit skill, Josh Pigford, Aug 2026; the practice stands on its own.)

When auditing or monitoring:

- **Track prompts like keywords.** "I'm looking for the best X," "what is the best X," and "find me the best X" usually return the same brands. Collapse wording variants into one core prompt per intent, and spend the budget on repeat runs instead.
- **Run each query 3–5 times per platform**, fresh session each time.
- **Track mention/citation *rate*** ("cited in 3 of 5 runs"), never a yes/no from one run.
- **Report the sample size** with every number ("40% mention rate, n=5") so future-you knows how much to trust it.
- **Compare rates over time, not runs.** A drop from 4/5 to 3/5 is noise; a drop from 4/5 to 0/5 sustained across a month is signal.
- Before diagnosing *why* you're not cited, split causes the way an audit should: **technical** (can't be crawled/parsed — see agent-readiness.md), **comprehension** (AI describes you inaccurately or vaguely), or **trust** (understood but not selected — see citations-vs-recommendations.md).

---

*Sources, all labeled and dated: Peec AI pre/post-5.6 citation data via Tomek Rudzki and Lily Ray (Aug 2026); LinkedIn's AEO guide numbers via Chris Long (Sep 2026, platform-reported); fan-out extraction method as publicly circulated (Aug 2026); measurement-rigor framing credited to Initial Commit's AEO audit skill (Josh Pigford, Aug 2026). All snapshots of a volatile system — verify against your own monitoring.*



---

## `references/linkedin-ai-citations.md`

# LinkedIn Content That Gets Cited by AI

LinkedIn is one of the most-cited domains for professional and B2B queries. But which LinkedIn surface gets cited depends heavily on the engine, and the mix moved sharply during 2026. Treat every number here as a dated snapshot and check your own prompts.

## Contents
- Which Surface, Which Engine
- Who Can Crawl What
- What Makes LinkedIn Content Citable
- Durability
- Risks
- Checklist
- Sources

---

## Which Surface, Which Engine

| Engine | What it cites from LinkedIn (2026) |
|---|---|
| **ChatGPT** | Shifted from Pulse articles to feed posts. Ahrefs data shows ChatGPT citations of `/pulse/` down ~86% and `/posts/` up ~74% between May and Oct 2026, with a ~36% overall LinkedIn drop in the mid-August retrieval change that also hit Reddit |
| **Perplexity** | Largest raw count of LinkedIn citations in OtterlyAI's sample and our Ahrefs pull, with company pages the biggest share in Ahrefs. (Semrush, measuring the share of answers that cite LinkedIn at all, found it lower on Perplexity than on ChatGPT or AI Mode, so the ranking depends on the measure) |
| **Copilot** | Cites LinkedIn heavily and increasingly (citations more than doubled May → Oct 2026, ~6.5× its Reddit citations). Pulse and posts both appear |
| **Google AI Overviews / AI Mode** | Posts and Pulse both cited, plus company pages |
| **Gemini** | Almost never cites LinkedIn (~0 in three separate datasets). Don't count on LinkedIn for Gemini visibility |
| **Claude** | Its search crawler is allowed on articles, posts, profiles, and company pages; little published citation data |

**What this means:**
- Publish both: feed posts for ChatGPT, long-form articles for Perplexity, Copilot, and Google's AI features.
- Maintain the company page as well as people's profiles. Perplexity cites company pages most; ChatGPT and AI Mode mostly cite individual members.
- Skip collaborative articles (`/advice/`). They're effectively uncited now.

**Our Ahrefs snapshot** (citations of linkedin.com URLs in Ahrefs' AI-responses data, pulled 2026-10-02; the prompt pool changes over time, so treat as directional):

| Path | ChatGPT, May 1 | ChatGPT, now | Perplexity | AI Overviews | AI Mode | Copilot | Gemini |
|---|---|---|---|---|---|---|---|
| All linkedin.com | 239K | 185K | 787K | 352K | 292K | 154K (65K in May) | ~0.7K |
| `/pulse/` articles | 22.7K | 3.3K | 84K | 43K | 51K | 23K | ~0 |
| `/posts/` | 17.7K | 30.8K | 133K | 62K | 55K | 18K | 0 |
| `/company/` | — | — | 474K | 51K | 41K | 15K | — |
| `/in/` profiles | — | — | 103K | 12K | 13K | 15K | — |

---

## Who Can Crawl What

LinkedIn's robots.txt (checked 2026-10-02):

| Crawler | Articles, posts, profiles, company pages |
|---|---|
| Googlebot, Bingbot | Allowed |
| OAI-SearchBot (ChatGPT search), Claude-SearchBot | Allowed |
| GPTBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Perplexity-User, Google-Extended, CCBot | Blocked |

So ChatGPT and Claude can cite LinkedIn from their search indexes, but their live "go read this page" agents can't fetch it. Perplexity cites LinkedIn most despite both of its bots being blocked, presumably through another index.

**Check your own articles for `noindex`.** LinkedIn appears to noindex some Pulse articles, reportedly from low-follower or low-engagement accounts, and only for crawlers, so the logged-in author never sees it (one small test, n=3). Check both the robots meta tag and the `X-Robots-Tag` header on the final response, for each crawler you care about:

```bash
URL=https://www.linkedin.com/pulse/your-article-slug
for UA in Googlebot bingbot OAI-SearchBot; do
  echo "== $UA"
  curl -sIL -A "$UA" "$URL" | grep -iE '^(HTTP/|x-robots-tag)'
  curl -sL -A "$UA" "$URL" | grep -ioE '<meta[^>]+name="(robots|googlebot|bingbot)"[^>]*>'
done
```

A `noindex` in either place for a crawler means that engine's index likely won't carry the article. An absent tag isn't proof it's indexed; confirm with a `site:` search.

---

## What Makes LinkedIn Content Citable

**Supported by independent data:**
- **Engagement barely matters.** Likes and comments show almost no correlation with citation. The median cited post has 15–25 reactions; 100 reactions get cited about as often as 10,000.
- **Follower count matters little.** Authors under 500 followers get cited, and about half of citations come from authors under 10K.
- **Original over reshared.** About 95% of cited posts are original.
- **Teach something.** Most cited posts share knowledge or advice.
- **Consistency.** About 75% of cited post authors posted 5+ times in the prior four weeks.
- **Length.** Cited articles are mostly 500–2,000 words; cited posts mostly 50–300 words.
- **Recent.** About half of cited content is under three months old.

**Vendor causal model (Scrunch, ~4K posts, treat as directional):** technical detail (+77%), named entities like tools, companies, and people (+33%), and a niche topic (+18%) raised citation. Unicode bold or italic text (−58%) and "link in comments" (−31%) lowered the post's own citations. The study is about ChatGPT, and it also found link-in-comments can help the linked page get cited, so it's a trade-off if your goal is citations for your own site.

**Platform-reported (LinkedIn's guide, Mar 2026):** articles of 800–1,200 words, posts of 200–300 words, post 2–3 times a week. The guide also suggests 3,000+ followers and 10+ comments help, which the independent data above doesn't support.

**Mechanics:**
- A post's first words become its URL slug, so front-load the target phrase.
- Structure articles like blog content: clear headings, a direct answer early, specific numbers and names.

---

## Durability

- Citations can be durable for specific, low-competition prompts. One B2B writer's six Pulse articles were cited in 54–86% of 28 tracked runs over ~20 weeks for a niche prompt (Kaleigh Moore, Sep 2026, anecdote).
- At the platform level they're volatile. One fixed-prompt study measured LinkedIn's share of AI answers falling ~65% from Feb to Jul 2026, while others measured it rising on Perplexity over the same months. Track by engine, and don't put all your third-party effort into LinkedIn (see the volatility section in [agent-readiness.md](agent-readiness.md)).

---

## Risks

- **No canonical control.** LinkedIn sets its own canonical on articles, so a full republish of your blog post competes with your own page. Publish on your site first, then post an adapted version (rewrite a meaningful share of it) or a summary that links back.
- **You don't own it.** LinkedIn decides indexing, can noindex articles, and changes formats. By default, US members' content can be used to train LinkedIn and Microsoft models.
- **Gemini blind spot.** Visibility built on LinkedIn won't carry to Gemini.

---

## Checklist

- [ ] Feed posts and long-form articles both in the mix, matched to the engines you care about
- [ ] Company page complete and consistent with your About page (see [positioning-and-consensus.md](positioning-and-consensus.md))
- [ ] Target phrase in a post's first words
- [ ] Original, specific, technical content with named entities; no Unicode bold; decide deliberately where the link goes (in-post helps the post, in-comments may help the destination)
- [ ] Articles checked for crawler `noindex`
- [ ] Blog posts published on your own site first; LinkedIn version adapted, not duplicated
- [ ] Citations tracked per engine, re-checked monthly

---

## Sources

All dated; most are vendor studies running their own trackers, so none is fully neutral.

- Profound, LinkedIn as most-cited domain for professional queries (Mar 2026): https://www.tryprofound.com/blog/linkedin-is-the-most-cited-domain-for-professional-queries-in-ai-search
- Semrush, LinkedIn AI visibility study, 325K prompts (Mar 2026): https://www.semrush.com/blog/linkedin-ai-visibility-study/
- OtterlyAI, LinkedIn AI search citations study, 1.31M citations (Jun 2026): https://otterly.ai/blog/linkedin-ai-search-citations-study/
- Cloro, LinkedIn articles vs posts (Aug–Sep 2026): https://cloro.dev/blog/linkedin-articles-vs-posts/
- Goodie, social media AI citations study (Sep 2026): https://higoodie.com/blog/social-media-ai-citations-study-2026/
- Scrunch, LinkedIn posts and ChatGPT citations (May 2026): https://scrunch.com/blog/linkedin-posts-robots-cant-resist-what-data-says-about-chatgpt-citations
- Mid-August 2026 ChatGPT source shift (Promptwatch, Petra Labs): https://somethinginc.com/blog/chatgpt-citation-sources-docs-replaced-reddit/
- Ahrefs AI responses data by URL path, pulled 2026-10-02 (directional; the prompt pool changes over time)
- LinkedIn robots.txt, fetched 2026-10-02; LinkedIn's AEO guide (Mar 2026)



---

## `references/multilingual-and-commerce.md`

# Multilingual AEO and AI Shopping Surfaces

Two extensions of the core workflow that fail in predictable ways: translating an English AEO plan into other markets, and investing in AI shopping surfaces for products those surfaces rarely show.

## Multilingual and multi-market AEO

The language of the query changes which sources get cited. Profound's analysis of 3.25 billion citations across seven models and 14 countries, using native-language prompts, found citation mix and social-source rates shifted materially with query language (Profound, April 2026). Spanish-language markets looked alike across countries, so language sometimes mattered more than geography. Platforms diverged too: Google AI Overviews drew on a varied set of local social sources, while ChatGPT's social citations stayed concentrated on Reddit. Profound sells AI visibility tracking; treat these as vendor research and validate in your own category.

### Checklist

1. **Treat language and country as separate dimensions.** Spanish in Mexico, Spanish in Spain, and English in Mexico are three configurations.
2. **Build prompts from native-language demand.** Use local customer research, local search terms, and native speakers. Don't translate the English prompt list word for word; category names, units, and decision criteria differ.
3. **Run each prompt on each target engine** and classify cited sources: owned, competitor, earned editorial, institutional, social, marketplace or directory (taxonomy in [citations-vs-recommendations.md](citations-vs-recommendations.md)).
4. **Find the local source market.** Note which local publishers, directories, review sites, communities, and authorities recur per engine. Don't assume Reddit, YouTube, LinkedIn, or a global publisher matters equally everywhere.
5. **Audit local facts.** Prices and currency, availability, policies, legal claims, support hours, and local entities. A wrong local price is a critical error (see [answer-accuracy.md](answer-accuracy.md)).
6. **Separate three gap types.** A translation gap means the page exists but not in this language. An information gap means the fact doesn't exist anywhere locally. An entity gap means local profiles describe you inconsistently.
7. **Recommend local channels only where the local citation mix supports them.**
8. **Assign native-language review and a freshness owner** for every localized page.
9. **Report each language, country, and engine separately** before rolling anything up.

## AI shopping surfaces

AI shopping features (ChatGPT Shopping, product results in Google AI Mode, Meta's Muse agent, and similar) are worth investing in only for categories they actually show. In Profound's tests, product category was a stronger trigger for ChatGPT Shopping than purchase-intent wording: physical consumer products activated it far more often than software, services, travel, or financial products (Profound, March 2026; observational, and OpenAI hasn't published the trigger rules). Verify current merchant and feed requirements in each platform's documentation.

### Fit check first

Classify the offering before auditing anything:

| Offering | Typical fit |
|---|---|
| Shippable consumer product, consumables | Strong; audit in full |
| Large equipment or vehicles | Test narrowly |
| Software, digital products, services, travel, financial products | Usually weak; put the effort into ordinary AI recommendations instead |
| Local-only offerings | Focus on local surfaces and Business Profile |

Then test with repeated representative prompts. Cards and offers vary between runs, so one carousel is not a ranking.

### Data audit (when the fit is real)

- Canonical title and description, brand, and identifiers (GTIN, MPN)
- Category, attributes, variants, sizes, colors, and compatibility
- Images
- Price, currency, sale status, and availability, with how fast changes propagate
- Shipping, returns, and merchant policies
- Reviews and ratings from real customers

Agents that buy can also draw on commerce catalogs directly. Muse, for example, searches the Shopify product catalog, so a Shopify merchant's catalog data is part of the audit.

Compare the feed, product page, structured data, merchant records, and marketplace listings for conflicts. Fix wrong data before any editorial work. Track three outcomes separately: whether the product is included, whether you are the headline merchant or offer, and whether you appear among all offers.

Never fabricate reviews, ratings, availability, or discounts. For the agent-side protocols (Merchant Center, UCP), see the Agentic Experiences section in SKILL.md.

---

*Framework lineage: the market checklist and commerce fit check adapted (re-expressed and restructured) from Profound's MIT-licensed international-aeo-strategist and ai-commerce-readiness-auditor skills and their studies (March and April 2026), credited.*



---

## `references/okf.md`

# Open Knowledge Format (OKF)

Google's v0.1 markdown spec for representing site content as an agent-readable bundle. Introduced on the [Google Cloud blog](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) on 2026-06-12 and shipped inside Knowledge Catalog.

## What it is

OKF is a directory of cross-linked markdown files. Each file has:

- A YAML frontmatter block (`type` required; `title`, `description`, `resource`, `tags`, `timestamp` recommended)
- A standard markdown body
- Standard markdown links to other files in the bundle (which the spec treats as concept relationships)

An optional `index.md` lists the files for progressive disclosure. The bundle can be distributed as a git repo (recommended), a tarball/zip, or a subdirectory of a larger repo.

The [full spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/HEAD/okf/SPEC.md) fits on one page. The repo lives under `GoogleCloudPlatform` (the "not an official Google product" disclaimer is Google's standard open-source boilerplate, not a denial — it appears on most of Google's open-source repos including their main AI samples repo).

### A minimal concept file

```markdown
---
type: Article
title: How to Connect the Ahrefs MCP Server to Manus
description: The official MCP servers, why they did not connect, and the fix.
resource: https://yoursite.com/blog/ahrefs-mcp-manus/
tags: [mcp, ahrefs]
---

# How to Connect the Ahrefs MCP Server to Manus

The body of the post, as clean markdown.
```

Add an `index.md` that lists all files so an agent can see the bundle's shape before opening each file, and that is the entire format.

## Honest framing

**Google built OKF for data teams sharing catalog metadata** — BigQuery tables, API endpoints, metrics, playbooks. Most of the spec's examples are data-team artifacts, not blog posts. Google's blog post framing: "improve data sharing" and "standardized documentation" for collaboration across teams.

Pointing OKF at a marketing site is a **clever repurposing** popularized by [Suganthan Mohanadasan](https://suganthan.com/blog/open-knowledge-format/). It's a legitimate use case for the format but not Google's primary one. Frame it accurately when explaining it to founders or marketing teams.

## What it does for AI search today

Nothing immediate. Nothing crawls the web for OKF bundles yet — the spec is weeks old, no AI engine has announced integration, and Knowledge Catalog ingests bundles only for paying enterprise customers' data teams.

Treat OKF as **protocol-layer registration** — the same shape of bet as early `schema.org` adoption was a decade ago. Schema took the better part of ten years to pay off; people who shipped it early are still glad they did.

A secondary benefit that pays off today regardless: **generating the bundle is itself an internal-linking audit**. Suganthan's tool draws every page as a node and every internal link as an edge, so islands and orphans become obvious at a glance.

## Where OKF fits in the agent-readable stack

| Layer | Purpose |
|---|---|
| `sitemap.xml` | Tells a crawler which URLs exist |
| `robots.txt` (with AI bot rules) | Permits or blocks AI crawlers |
| `llms.txt` | Points an agent at the handful of pages you most want read |
| `/pricing.md` | Structured pricing for agent-buyer comparisons |
| **`/okf/` bundle** | Hands over the content itself as cross-linked concepts |
| Schema markup | Per-page structured data (Article, FAQPage, Product, etc.) |

These stack rather than compete. `llms.txt` is a signpost, OKF is the library.

## How to ship one

Three options, ordered by how much effort they take:

### 1. Suganthan's free web tool (recommended for most sites)

[suganthan.com/okf-generator](https://suganthan.com/okf-generator/) — paste a URL or sitemap, crawls up to 100 pages, returns a downloadable bundle. Also draws the resulting page graph so you can spot disconnected pages before publishing.

### 2. WordPress plugin (pending wp.org approval)

Suganthan's plugin (free, GPL, awaiting wp.org approval at time of writing) installs in a minute, serves the bundle at `/okf/`, and rebuilds on every publish or edit so it stays in sync. Direct download link is in [his blog post](https://suganthan.com/blog/open-knowledge-format/). Requires WordPress 6.0+ and PHP 7.4+. Read-only — never edits posts or settings.

### 3. By hand

Only practical for a handful of pages. Each post becomes a markdown file with frontmatter that you cross-link manually. Miserable for a whole site.

## Hosting & discovery

Serve the bundle at `yoursite.com/okf/`, starting with `yoursite.com/okf/index.md`:

- **Static hosts / Cloudflare**: drag and drop
- **WordPress**: Suganthan's plugin handles the serving
- **Static sites with custom paths**: upload the directory to `/okf/`
- **Closed platforms (Wix, Squarespace, most page-builders)**: you usually can't serve files at custom paths — skip OKF entirely

After it's serving, add a line to `llms.txt` pointing to the bundle so agents that read `llms.txt` (today) can discover the bundle (later).

## When to skip

- Site is <10 pages — overhead exceeds payoff
- Site is on a closed platform that won't allow custom paths
- You're not maintaining `llms.txt`, schema markup, or other machine-readable files (OKF compounds with those; alone it does nothing)
- You can't budget the 30 minutes a quarter to refresh the bundle as content changes

## What to watch

OKF is v0.1, weeks old. Worth tracking, not worth obsessing over:

- Whether Google announces OKF support in AI Overviews / Knowledge Graph (currently no signal)
- Whether non-Google engines (ChatGPT, Perplexity, Claude) announce OKF reading
- Whether the spec moves to v1.0 (breaking changes are possible at <1.0)
- Whether Knowledge Catalog adds public ingestion endpoints
- Adoption signals — search GitHub for `okf/index.md` to see who's shipping bundles



---

## `references/platform-ranking-factors.md`

# How Each AI Platform Picks Sources

Each AI search platform has its own search index, ranking logic, and content preferences. This guide covers what matters for getting cited on each one.

Sources cited throughout: Princeton GEO study (KDD 2024), SE Ranking's domain study (Nov 2025), Sellm.io's ranking-factor model, and Profound's citation data (2025). Most are vendor research with correlational methods.

**Evidence order.** Weigh claims in this order: (1) official engine documentation and webmaster guidance, (2) controlled experiments and primary research, (3) large observational datasets, (4) practitioner case studies and commentary. When official guidance and observational data conflict, follow the documentation for eligibility and crawler controls and test the observation. Every number below is a dated snapshot of a moving system; re-check it before quoting it to a client.

---

## The Fundamentals

Every AI platform shares three baseline requirements:

1. **Your content must be in their index** — Each platform uses a different search backend (Google, Bing, Brave, or their own). If you're not indexed, you can't be cited.
2. **Your content must be crawlable for discovery** — Allow the relevant search-discovery path through robots.txt and your WAF; model-training controls are separate.
3. **Your content must be extractable** — AI systems pull passages, not pages. Clear structure and self-contained paragraphs win.

Beyond these basics, each platform weights different signals. Here's what matters and where.

---

## Google AI Overviews

Google AI Overviews pull from Google's own index and lean heavily on E-E-A-T signals (Experience, Expertise, Authoritativeness, Trustworthiness). BrightEdge measured them on about 48% of its tracked queries in February 2026, with wide swings by industry (most B2B tech and healthcare queries, few shopping queries).

**What makes Google AI Overviews different:** They already have your traditional SEO signals — backlinks, page authority, topical relevance. The additional AI layer adds a preference for content with cited sources and structured data. The GEO study (Aggarwal et al., 2023) found that adding citations, quotations, and statistics raised visibility by roughly 30–40% on its own metric; individual examples in the paper show much larger jumps, but those aren't typical or additive.

**AI Overviews don't just recycle the traditional Top 10.** Some studies have put the overlap between AI Overview sources and conventional organic results as low as ~15%, though figures vary widely by study, date, and query set. Pages that wouldn't crack page 1 can still get cited with clear, extractable answers. Even so, practitioners consistently find that better organic rankings mean better AI visibility, so don't treat the low-overlap stat as permission to skip SEO.

**What to focus on:**
- Schema markup gives AI Overviews structured context (Article, HowTo, Product). It's one lever among several, and Google says no special markup is required for AI features. Google limited FAQ rich results to government and health sites in 2023, so don't promise an AI lift from FAQPage schema
- Build topical authority through content clusters with strong internal linking
- Include named, sourced citations in your content (not just claims)
- Author bios with real credentials matter — E-E-A-T is weighted heavily
- Get into Google's Knowledge Graph where possible (an accurate Wikipedia entry helps)
- Target "how to" and "what is" query patterns — these trigger AI Overviews most often

**Watch for OKF.** In June 2026 Google introduced the [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) — a markdown spec for agent-readable site bundles. There is no confirmed signal that AI Overviews factor it in today, but the spec is published, the GitHub repo lives under `GoogleCloudPlatform`, and it ships inside Knowledge Catalog. For protocol-layer "register early" plays, it has the same shape as early schema.org adoption did a decade ago. See **Machine-Readable Files for AI Agents** in the main `SKILL.md` for how to generate and serve a bundle.

---

## ChatGPT

ChatGPT's web search draws from a Bing-based index. It combines this with its training knowledge to generate answers, then cites the web sources it relied on.

**What makes ChatGPT different:** Link authority correlates strongly with citation. SE Ranking's study of 129,000 domains (Nov 2025) found referring domains were the single strongest predictor: sites with up to 2,500 referring domains averaged 1.6–1.8 citations, sites with more than 350,000 averaged 8.4, and citations nearly doubled past about 32,000. It's a correlation, and big brands have both links and everything else.

**Freshness is a major differentiator.** Several vendor studies report that recently updated pages earn several times more ChatGPT citations than stale ones. The multipliers vary by study and none is well documented, so treat freshness as a strong lean and don't forecast with any one multiplier.

**Content-answer fit matters most among page-level signals.** Sellm.io trained a model on 400,000+ URLs across 10,000 queries (undated vendor study) and found that how closely a page's substance and structure match ChatGPT's own answer was its strongest predictor of citation, well ahead of domain authority and on-page structure. Write the direct answer the question deserves, and you're more likely to be the source it cites.

**Where ChatGPT looks beyond your site:** In Profound's data from Aug 2024 to Jun 2025 (680 million citations), Wikipedia took 7.8% of ChatGPT citations, Reddit 1.8%, and Forbes 1.1%. Those shares have moved since: ChatGPT's August 2026 retrieval changes nearly removed Reddit as a source (see the volatility section in [agent-readiness.md](agent-readiness.md)). Company sites took most citations in Profound's later dataset (see [citations-vs-recommendations.md](citations-vs-recommendations.md)), and third-party mentions still shape recommendations.

**What to focus on:**
- Invest in earned links and authority; referring domains were the strongest correlate in SE Ranking's study
- Update competitive content at least monthly
- Structure your content the way ChatGPT structures its answers (conversational, direct, well-organized)
- Include verifiable statistics with named sources
- Clean heading hierarchy (H1 > H2 > H3) with descriptive headings

---

## Perplexity

Perplexity always cites its sources with clickable links, making it the most transparent AI search platform. It combines its own index with Google's and runs results through multiple reranking passes — initial relevance retrieval, then traditional ranking factor scoring, then ML-based quality evaluation that can discard entire result sets if they don't meet quality thresholds.

**What makes Perplexity different:** It's the most "research-oriented" AI search engine, and its citation behavior reflects that. Perplexity maintains curated lists of authoritative domains (Amazon, GitHub, major academic sites) that get inherent ranking boosts. It uses a time-decay algorithm that evaluates new content quickly, giving fresh publishers a real shot at citation.

**Perplexity has unique content preferences:**
- **FAQ Schema (JSON-LD)** — Pages with FAQ structured data get cited noticeably more often
- **PDF documents** — Publicly accessible PDFs (whitepapers, research reports) are prioritized. If you have authoritative PDF content gated behind a form, consider making a version public.
- **Publishing velocity** — How frequently you publish matters more than keyword targeting
- **Self-contained paragraphs** — Perplexity prefers atomic, semantically complete paragraphs it can extract cleanly

**What to focus on:**
- Allow PerplexityBot in robots.txt
- Implement FAQPage schema on any page with Q&A content
- Host PDF resources publicly (whitepapers, guides, reports)
- Add Article schema with publication and modification timestamps
- Write in clear, self-contained paragraphs that work as standalone answers
- Build deep topical authority in your specific niche

---

## Microsoft Copilot

Copilot is embedded across Microsoft's ecosystem — Edge, Windows, Microsoft 365, and Bing Search. It relies entirely on Bing's index, so if Bing hasn't indexed your content, Copilot can't cite it.

**What makes Copilot different:** The Microsoft ecosystem connection creates unique optimization opportunities. Copilot cites LinkedIn heavily (its LinkedIn citations more than doubled May → Oct 2026 and run about 6.5× its Reddit citations, per Ahrefs data), and GitHub content is a natural fit too. Copilot also puts more weight on page speed — sub-2-second load times are a clear threshold.

**What to focus on:**
- Submit your site to Bing Webmaster Tools (many sites only submit to Google Search Console)
- Read its **AI Performance** report (beta since February 2026): how often your pages are cited in Copilot and Bing's AI answers, plus the **grounding queries** Bing used to retrieve them. Grounding queries are Bing's interpretation of the request, not what the user typed, so they show what the engine is actually searching for. No click data, and no mapping from a query to a specific citation.
- Use IndexNow protocol for faster indexing of new and updated content
- Optimize page speed to under 2 seconds
- Write clear entity definitions — when your content defines a term or concept, make the definition explicit and extractable
- Build presence on LinkedIn (articles, posts, and a complete company page; see [linkedin-ai-citations.md](linkedin-ai-citations.md)) and GitHub if relevant
- Ensure Bingbot has full crawl access

---

## Claude

Claude uses Brave Search as its search backend when web search is enabled — not Google, not Bing. This is a completely different index, which means your Brave Search visibility directly determines whether Claude can find and cite you.

**What makes Claude different:** Claude is extremely selective about what it cites. While it processes enormous amounts of content, its citation rate is very low — it's looking for the most factually accurate, well-sourced content on a given topic. Data-rich content with specific numbers and clear attribution performs significantly better than general-purpose content.

**What to focus on:**
- Verify your content appears in Brave Search results (search for your brand and key terms at search.brave.com)
- If it's missing, request a crawl at search.brave.com/submit-url. It only alerts Brave's crawler: there's no webmaster console or sitemap submission, so check referrals from search.brave.com in your analytics to see whether it worked
- Decide separately whether to allow `Claude-SearchBot` for search discovery, `Claude-User` for user-directed retrieval, and `ClaudeBot` for potential model training
- Maximize factual density — specific numbers, named sources, dated statistics
- Use clear, extractable structure with descriptive headings
- Cite authoritative sources within your content
- Aim to be the most factually accurate source on your topic — Claude rewards precision
- Don't rely on self-ranked "best X" lists. In a live test (Sep 2026), Claude noted that results for a "best [category]" query were dominated by vendors ranking themselves #1 and leaned on juried awards and practitioner reputation instead

---

## Meta AI and Muse

Meta AI answers questions across Facebook, Instagram, WhatsApp, Messenger, and Meta's glasses. Muse, Meta's personal agent built on the Muse Spark model, launched in September 2026 and acts for the user: it connects to apps, recommends products, and buys them. Muse can search the full Shopify product catalog and check out with Link by Stripe, Shop Pay, and PayPal, plus retail connectors such as Walmart, Best Buy, Sephora, and Wayfair (TechCrunch, Sep 2026). Meta makes Muse free and expects to earn a fee on transactions, so shopping is the surface to watch.

Meta hasn't documented which search index Meta AI uses or how it picks sources. Early hands-on tests found Muse unreliable at shopping tasks (Tom's Guide and CNN, Sep 2026). Treat practitioner claims about "ranking in Muse" as unverified.

**What to focus on:**
- Allow `meta-webindexer`. Meta says it crawls to improve Meta AI search results and so Meta can cite and link your content. Decide on `meta-externalagent` (training) separately
- For physical products, make sure your Shopify catalog data is complete and current: titles, attributes, variants, price, and availability (see [multilingual-and-commerce.md](multilingual-and-commerce.md))
- Apply the agent-readability basics in SKILL.md's Agentic Experiences section, since Muse reads and acts on pages for the user
- Test with real prompts in the Meta AI app and log results with dates; there's no Meta citation report to rely on

---

## Allowing AI Bots in robots.txt

Do not copy one blanket allowlist. Choose controls by documented purpose, then check WAF and CDN rules as well as `robots.txt`.

```text
# Automatic search discovery
User-agent: Bingbot
User-agent: Googlebot
User-agent: OAI-SearchBot
User-agent: PerplexityBot
User-agent: Claude-SearchBot
User-agent: meta-webindexer
Allow: /

# Potential model training (publisher choice shown as disallow)
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: meta-externalagent
Disallow: /

# Gemini model training and grounding (publisher choice shown as disallow)
User-agent: Google-Extended
Disallow: /
```

User-triggered fetchers such as `ChatGPT-User`, `Claude-User`, and `Perplexity-User` are separate from automatic discovery. Vendor behavior can differ: OpenAI says `robots.txt` rules may not apply to `ChatGPT-User`, and Perplexity says `Perplexity-User` generally ignores them because these fetches are user-requested; Meta says `meta-externalfetcher` may bypass them. Meta also runs `facebookexternalhit` for link previews when a URL is shared on its apps; leave it allowed or shared links lose their title and image. Use `OAI-SearchBot`, not `ChatGPT-User`, to manage ChatGPT Search inclusion. `Google-Extended` is a standalone product token rather than a separate HTTP crawler; Google says it controls certain Gemini training and grounding uses and does not affect Google Search inclusion or ranking.

Verify the current names and consequences in the vendors' maintained documentation: [OpenAI](https://developers.openai.com/api/docs/bots), [Perplexity](https://docs.perplexity.ai/docs/resources/perplexity-crawlers), [Anthropic](https://privacy.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), [Meta](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers), and [Google](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers).

For implementation, inspect `/robots.txt` manually first. Optional helpers include each vendor's own crawler documentation and robots.txt testing tools.

---

## Where to Start

If you're optimizing for AI search for the first time, focus your effort where your audience actually is:

**Start with Google AI Overviews** — They reach the most users (about 48% of BrightEdge-tracked queries, Feb 2026) and you likely already have Google SEO foundations in place. Add schema markup, include cited sources in your content, and strengthen E-E-A-T signals.

**Then address ChatGPT** — It's the most-used standalone AI search tool for tech and business audiences. Focus on freshness (update content monthly), domain authority, and matching your content structure to how ChatGPT formats its responses.

**Then expand to Perplexity** — Especially valuable if your audience includes researchers, early adopters, or tech professionals. Add FAQ schema, publish PDF resources, and write in clear, self-contained paragraphs.

**Copilot, Claude, and Meta AI are lower priority** unless your audience skews enterprise/Microsoft (Copilot), developer/analyst (Claude), or consumer shopping on Meta's apps (Meta AI and Muse). But the fundamentals — structured content, cited sources, schema markup — help across all platforms.

**Actions that help everywhere:**
1. Set an explicit, purpose-specific robots policy: allow relevant discovery crawlers while deciding training and user-triggered retrieval separately
2. Implement schema markup (FAQPage, Article, Organization at minimum)
3. Include statistics with named sources in your content
4. Update content regularly — monthly for competitive topics
5. Use clear heading structure (H1 > H2 > H3)
6. Keep page load time under 2 seconds
7. Add author bios with credentials



---

## `references/positioning-and-consensus.md`

# Positioning and Consensus in AI Answers

LLMs don't just retrieve pages. They hold an association between your brand and a category, a segment, and a set of strengths and weaknesses, built from everything written about you. This reference covers how to shape that association, and why it moves slowly.

Most of this comes from practitioner experience rather than controlled studies, mainly Harpreet Singh on Edward Sturm's podcast (E1182, "AEO Companies Are Selling You 2016 SEO," Sep 2026). Claims are labeled as anecdote or opinion where that's all they are.

## Contents
- Old SEO, New Name
- Positioning Moves Slowly
- Make Every Profile Say the Same Thing
- Work Backwards from the Fan-Out
- Segment and Industry Pages
- Managing the "Cons" Others Write
- Head Terms Where Incumbents Are Already Chosen
- What Not to Copy

---

## Old SEO, New Name

Much of what gets sold as AEO is traditional SEO: keywords in URLs, FAQs, meta descriptions, solution pages, listicles, press releases. These still work, because strong organic rankings remain one of the best predictors of AI visibility, especially in Google's AI features.

The risk is applying them without the history. Tactics that were tuned for years (how many FAQs, how keyword-stuffed a URL, how many near-duplicate pages) get overused when someone presents them as new, and the result can be a short-term lift followed by lost organic traffic (practitioner opinion; no data cited).

**How to apply:** before recommending a tactic as "for AI," ask whether it's an SEO tactic with a known failure mode, and keep it inside normal SEO limits. Be skeptical of vendor statistics with no source or date.

---

## Positioning Moves Slowly

A brand known for one segment for years doesn't become known for another because its pages change.

- **Repositioning:** a mid-market brand that rewrites its site for enterprise can lose mid-market answers before it earns enterprise ones, and "disappear from LLMs for a while." Enterprise prompts are already associated with incumbents (anecdote, one client).
- **Mergers and rebrands:** an acquired brand often stops appearing for prompts it used to own once its pages fold into the parent (practitioner observation).
- **Local and niche markets too:** for many categories, models have "already picked their winners," and new entrants start behind (opinion).

**How to apply before a repositioning, rebrand, or merger** (a practitioner sequence, not a tested playbook):
1. Record a baseline for the old segment's prompts *and* the target segment's prompts.
2. Watch for a dip and warn stakeholders it may happen. This rests on practitioner reports, not controlled data.
3. Move off-site signals first (profiles, reviews, press, analyst listings, partner pages), then stage the on-site rewrite, rather than switching everything at once.
4. Keep pages that still win old-segment prompts until the new association shows up in tracking.

---

## Make Every Profile Say the Same Thing

Models look for consensus. Your G2, Capterra, Gartner, Crunchbase, LinkedIn, and partner-directory profiles should describe you with the same segment, category, and differentiators as your About page. If you're targeting enterprise, those profiles should say enterprise.

- Fill in free profiles fully (what you do, who it's for, which industries), even on platforms you don't pay for.
- Review text matters as much as profile text. Models read what customers say on those pages.
- This is one of the cheapest changes available: an afternoon of edits across profiles you already have.

Pair with the review-generation playbook in the directory-submissions skill.

---

## Work Backwards from the Fan-Out

Extract the real background queries for your key prompts (the DevTools method in [format-volatility.md](format-volatility.md)), then look at which domains they name.

- If ChatGPT's first fan-out round runs `site:` searches on Gartner, G2, or Capterra for your category, those profiles are your priority, often ahead of publishing another page on your own site.
- The mix differs by category and changes over time, so check your own prompts rather than copying someone else's list. One practitioner saw Gartner rise in finance-software fan-outs and moved review effort from G2 toward Gartner (anecdote).

---

## Segment and Industry Pages

AI answers are increasingly personalized and segment-aware: models place brands into enterprise, mid-market, or SMB, and match them to industries.

- Build pages for the core industries or segments you actually serve ("email marketing for e-commerce," "RFP software for government"), with real specifics for each.
- Start with your core segments. Scale isn't the problem in itself; near-duplicate pages that swap the industry name without adding real value are what Google's scaled-content policy targets. See [content-types.md](content-types.md).

---

## Managing the "Cons" Others Write

Affiliates and review aggregators list a con for every product to look balanced. Find what they say about you.

- If a listed con reinforces a known weakness models already repeat (for example, long implementation), ask the publisher to use a different con that is also true and less central.
- Never ask for negatives to be removed or for false claims. The goal is accuracy, not a clean sheet.

To repair a weakness models repeat, address it in public with specifics: one practitioner's client turned "implementation takes forever" around over 1.5–2 years with founder posts about the process, guides on real timelines, and a concrete "4–8 weeks" on the implementation page (anecdote). See also the "recommended against" section of [citations-vs-recommendations.md](citations-vs-recommendations.md).

---

## Head Terms Where Incumbents Are Already Chosen

For prompts like "best email marketing software," incumbents are in the training data and on every list. Practitioner playbooks (opinion, not tested):

- **Run both formats.** A solution page for the term and a buyer's-guide listicle, since engines currently weight them differently (see [format-volatility.md](format-volatility.md)).
- **Amplify earned third-party proof.** Publish and promote G2 grid placements and analyst mentions; don't just collect them.
- **Occupy several places on the results page.** Your YouTube video, creator coverage, review profiles, and press, not only your own page. Compare Google and Bing results, since different engines draw on different backends.
- **Rank the leader honestly.** In a "best X for Y" guide, it can work better to name the category leader first and show where you go further, than to rank yourself #1 (see the self-promotional listicle risk in [citations-vs-recommendations.md](citations-vs-recommendations.md)).

---

## What Not to Copy

The same episode floats tactics this skill does not recommend:

- **Invented awards or brand-run "review" sites** presented as independent. These are inauthentic mentions, and fake or misleadingly sourced reviews can break the FTC's 2024 rule on consumer reviews and testimonials (16 CFR Part 465).
- **Fast-decaying press-release tricks** (which cheap wire syndicates into which outlets). If you use press releases, check that the destination pages are indexed before paying; outlets change this without notice.



---

## `references/prompt-portfolio.md`

# Prompt Portfolio Design

Which prompts you track decides what your AI visibility numbers mean. A portfolio stuffed with glossary questions will report healthy visibility while you lose every shortlist. This reference covers how to choose prompts, group them, version them, and how often to run them, including the multi-turn buying conversations single prompts miss.

## Start with the measurement question

Write down the decision the numbers will drive before choosing a single prompt. "Are we on the shortlist for mid-market [category] buyers in the US?" needs a different portfolio from "Did our docs rewrite fix how Claude describes our API limits?"

## Build from real demand

Use the words buyers actually type. In order of preference:

1. Prompts buyers report directly (a "What did you ask the AI?" follow-up on your how-did-you-hear field, sales call notes)
2. Prompt-demand data from a tracking tool, if you have it
3. Customer research, support tickets, community threads, and sales objections
4. Your search terms, rewritten as someone would phrase them to an assistant

Don't mechanically turn a keyword list into questions. "crm small business" and "What CRM should a 5-person agency use if we live in Gmail?" retrieve different sources.

## Cover the intent families

| Family | Example shape |
|---|---|
| Category discovery | "What tools do teams use for [job]?" |
| Problem and solution research | "How do I stop [problem]?" |
| Comparisons and alternatives | "[You] vs [competitor]," "alternatives to [competitor]" |
| Recommendations and "best for" | "Best [category] for [segment or constraint]" |
| Trust, risk, and validation | "Is [you] legit?" "Does [you] have SOC 2?" |
| Price, availability, compatibility, limits | "[You] pricing," "Does [you] work with [tool]?" |
| Implementation and troubleshooting | "How do I set up [you] with [stack]?" |
| Local, shopping, or regulated | Only when they apply to the business |

Weight families by business value. A citation for a definition question rarely sells anything; see the revenue filter in SKILL.md's audit step.

## Three cohorts

| Cohort | Purpose | Rules |
|---|---|---|
| **Stable core** | Trend measurement | Changes rarely and only through versioning. This is the set you report on. |
| **Exploratory** | Emerging demand, new segments, new competitors | Rotates freely. Promote prompts into the core when they prove valuable. |
| **Diagnostic controls** | Known outcomes that tell you whether measurement drifted | Include prompts where you should always appear (your brand name) and never appear (an unrelated category). If those move, the tool or the engine changed, and your work had nothing to do with it. |

Keep engines, markets, languages, and personas as separate configurations. A US English ChatGPT run and a German Gemini run are different measurements; see [multilingual-and-commerce.md](multilingual-and-commerce.md).

Add paraphrase variants only where you need to measure wording sensitivity. Otherwise collapse variants of the same intent into one core prompt.

## How often to run

Two regimes, depending on portfolio size:

- **A broad portfolio (hundreds of prompts):** once a day is usually enough. In Profound's comparison of 753 prompts across seven platforms over two weeks, once-daily visibility estimates landed within about two percentage points of running each prompt ten times a day (Profound, July 2026). Extra runs helped citation share more than visibility, and couldn't remove day-to-day platform drift. Composition mattered more than frequency.
- **A small set (the 10–20 prompts of a DIY audit), short experiments, or citation-share precision:** run each prompt several times (3–5 per platform) and report the rate with its sample size, as the monitoring section in SKILL.md describes. With few prompts, one run per prompt is mostly noise.

Profound sells AI visibility tracking, so treat these figures as vendor research from one setup. Other trackers include Ahrefs Brand Radar, Semrush, Peec AI, Otterly, and ZipTie; check what each one samples before comparing their numbers.

## Version the portfolio

- Give the portfolio a version number and log every addition, removal, and weighting change with a date and reason.
- Never compare two periods that used materially different portfolios. Recalculate on the prompts both periods share.
- Freeze the core during an experiment.

## Read results by topic, then fix before you create

Score the portfolio by buying topic, not prompt by prompt. "Best auth API," "SSO provider for SaaS," and "SAML authentication tools" are one topic. For each topic, count how often you and each competitor appear across its prompts and runs: a competitor in 18 of 25 runs while you're in 4 is where to start, not a single prompt where both of you showed up once.

For the topics you're losing:

1. **Open the sources the engine cited when competitors won.** Record the page, the domain, the page type, and which competitor it mentions. After 20–30 prompts the same pages and domains repeat.
2. **Check whether you already have a page that should win.** If it exists, find out why it isn't surfacing (wrong intent, outdated, the answer buried, missing the proof or comparison the winning page has) before writing a new one. Two weak pages on one topic is worse than one fixed page.
3. **Rule out the technical layer** (indexing, crawler access, internal links) before rewriting anything.
4. **Decide the fix:** a new page, a better existing page, updated facts, or third-party sources (comparison pages and discussions you're absent from).
5. **Rerun the identical portfolio** once changes are crawled, with the same prompts and engines, and compare per topic.

*Topic-gap method adapted from Jam's AI search audit (October 2026).*

## Multi-turn buying journeys

Buyers don't stop at one prompt. Commercial conversations in ChatGPT were less likely to end after one turn than informational ones, and commercial intent rose from 13.9% to 19.2% of sampled conversations in a year (Profound, August 2026; sampled and modeled estimates). Earlier Profound research found web citations concentrate in the opening turns of a research conversation (Profound, Q4 2025 data). So the opening prompt decides which sources get pulled, and later turns decide who stays on the shortlist.

Map the journey by stage, then write one opening prompt and two or three realistic follow-ups for each:

| Stage | Typical follow-up |
|---|---|
| Define the need | "What should I look for in a [category]?" |
| Build a shortlist | "Which of these work for [constraint]?" |
| Compare | "How does [A] compare to [B] on [criterion]?" |
| Validate | "What do users complain about with [A]?" |
| Resolve risk | "Can I migrate from [incumbent] without losing [data]?" |
| Choose | "Which would you pick for a team like mine?" |

Run the conversation in one session and record, per turn, whether you were mentioned, recommended, cited, or dropped, and the framing around the mention. The turn where you fall off the shortlist is the content or evidence gap to fix. Track mention, shortlist inclusion, framing, and citations separately; see the visibility ladder in [citations-vs-recommendations.md](citations-vs-recommendations.md).

First decide whether AI buying conversations matter for the category at all. Profound found commercial-intent share varied about tenfold across industries in the same study.

---

*Framework lineage: cohort design, cadence regimes, and the journey map adapted (re-expressed and restructured) from Profound's MIT-licensed ai-prompt-portfolio-builder and commercial-ai-journey-mapper skills and the studies they cite (July and August 2026), credited.*



---

## `references/youtube-ai-citations.md`

# YouTube Videos That Get Cited by AI

YouTube is one of the most-cited third-party surfaces in AI answers — Google AI Overviews and Gemini cite it heavily, and ChatGPT/Perplexity lift from it for how-to queries. The core insight that changes how you produce for it:

**Models don't watch your video. They read everything around it.** The citation is earned by the text layer — title, transcript, captions, chapters, description, and comments — not the footage. A mediocre-looking video with a clean, structured text layer beats a beautiful one that's opaque to a crawler.

## The anatomy

Work through these in order of leverage:

### 1. The transcript (the real content)

This is what the model actually reads. Optimize the *spoken words*:

- **Answer questions in complete, liftable sentences.** "The five steps to create an SOP are…" extracts cleanly; a rambling answer spread across three tangents doesn't.
- Script or outline the key answers before recording so each core question gets a clear, structured spoken answer in one place.
- Say the important terms out loud — the product name, the category, the entities you want associated. If it's only on a slide, the model may never see it.

### 2. Accurate captions

Auto-captions are messy — misheard product names, no punctuation, broken sentences — and messy captions are what the model reads if you don't fix them. Upload cleaned captions (or at minimum correct the auto-generated ones). This is the cheapest fix on the list.

### 3. A question-shaped title

Models match the title against the user's prompt. "How to Create SOPs That Scale Your Business" beats a clever title every time. Front-load the question or task; save the branding for the channel.

### 4. Chapters and timestamps

Chapters let the model (and viewers) jump to the exact answer. Structure = extractability: each chapter title is another labeled, liftable claim about what the video covers. Match chapter titles to the sub-questions people actually ask.

### 5. A keyword-rich, structured description

Restate the video's key points *as text* in the description — a short summary, then a bulleted list of what's covered, then resource links. This reinforces the topic and entities in plain crawlable text and gives the model a second, cleaner copy of the answer.

### 6. A pinned comment with the summary

An extra liftable text block: pin a comment with the core answer in numbered steps plus the key links. It's indexed, it's structured, and it survives even when viewers never open the description.

### 7. Thumbnail and engagement

Engagement isn't read directly by LLMs, but it drives the watch signals that lift YouTube ranking — and YouTube ranking feeds what AI systems surface and cite. The thumbnail's job is the click; the text layer's job is the citation.

## Publishing checklist

- [ ] Title is question- or task-shaped and matches a real query
- [ ] Key answers spoken as complete, structured statements
- [ ] Captions uploaded or corrected (product names spelled right)
- [ ] Chapters added, titled by sub-question
- [ ] Description restates the key points in text with a bulleted breakdown
- [ ] Pinned comment carries the summary + links
- [ ] Important entities (brand, category, product) spoken *and* written

## Field notes (Sep 2026)

- **The citation bar can be low.** In a live check, an 8-day-old video with under 100 views was the first source cited in Google's AI Overview for "best email marketing software." Fresh, well-labeled videos on head terms are worth testing.
- **Ungate your demos.** Post product demos publicly with keyword-first titles ("[Category] software demo – [Brand]") instead of locking them behind a form.
- **Sponsored creator videos are hard to attribute.** Practitioners quote $20–40K per sponsored video and no reliable way to prove the return. Budget them with an attribution plan (the self-reported field in [citations-vs-recommendations.md](citations-vs-recommendations.md)) or not at all.

## Related

- The same "models read the text layer" logic applies to podcasts: episodes get transcribed and show notes get published, so podcast guesting is earned media that compounds in AI answers — see the `public-relations` skill's podcast guest prep reference.
- For producing the videos themselves, see the `video` skill.

---

*Anatomy pattern from Ross Simmonds / Foundation Inc. ("The Anatomy of a YouTube Video AI Cites," 2026), distilled and extended with credit.*
