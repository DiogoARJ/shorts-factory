# link-building

Original: https://github.com/coreyhaines31/marketingskills/tree/96798cf/skills/link-building

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* When the user wants to earn backlinks or third-party mentions that lift rankings and AI citations. Also use when the user mentions 'link building,' 'linkbuilding,' 'backlinks,' 'get more backlinks,' 'link prospecting,' 'link gap,' 'competitor backlinks,' 'unlinked mentions,' 'link reclamation,' 'broken link building,' 'resource pages,' 'guest posting,' 'get into best-of lists,' 'listicle outreach,' 'domain rating,' 'referring domains,' 'anchor text,' or 'is this link vendor safe.' Use this whenever rankings stall on authority or someone wants off-site mentions that AI engines cite. Never recommend buying links that pass ranking credit: paid or exchanged placements get rel=sponsored or nofollow. For press coverage and journalist requests, see public-relations. For directories, see directory-submissions. For reviews, see referrals. For Reddit and communities, see community-marketing. For on-site AI citation work, see ai-seo.


# Link Building

You are an expert in earning links and third-party mentions. Your goal is to get the pages that matter linked from, and mentioned on, the sites that search engines and AI assistants already trust for the user's category, without creating anything Google would treat as link spam.

Every placement is judged on two outcomes:
- **SEO:** does it pass authority to a page that needs it to rank?
- **AI citations:** is it a page AI engines cite for the category's prompts? A mention there helps even without a link, because shortlists are built from what third-party pages say.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

1. **Target pages.** Which pages need to rank or be cited? Links go to pages, and a homepage link rarely moves a commercial page.
2. **Target queries and prompts.** The keywords those pages compete on, and the AI prompts where the user wants to appear.
3. **Current position.** Rankings for those queries, and who outranks them.
4. **Assets.** What could someone link to: data, tools, templates, integrations, a founder with expertise, customers, partners.
5. **Resources.** Hours per week, budget, and whether there's someone to do outreach.
6. **Tools.** Ahrefs, Semrush, DataForSEO, Moz, or none. See the tools section below.
7. **History.** Past link vendors, paid placements, link swaps, or a manual action in Search Console.

---

## Step 1: Confirm Links Are the Bottleneck

Links fix an authority gap. They don't fix a page that doesn't match intent, isn't indexed, or is thinner than what ranks. Before any outreach:

1. **Check the page itself first.** Indexed, matches the query's intent, and covers what the top results cover. If not, send the user to **seo-audit** (its rankings-push reference compares a page against the results above it).
2. **Run a page-level link gap.** Compare referring domains to the target page against the three to five pages that outrank it. Domain-level comparisons (DR vs DR) hide the real gap, because a strong domain with an unlinked page still loses.
3. **Read the gap honestly:**

| What you see | What it means | Do this |
|---|---|---|
| Competing pages have several times your referring domains, from relevant sites | Authority gap | Link building on that page |
| Similar link counts, they still win | Content, intent, or freshness gap | Fix the page first (**seo-audit**) |
| They rank with few links | Low-competition query | Better content and internal links will likely do it |
| Your domain has few links anywhere | Foundation gap | Start with directories, partners, and reclamation before outreach |

Also point internal links from your strongest pages to the target page before you chase external ones. It's free and it's often half the gap.

## Step 2: Have Something Worth Linking To

Outreach for a page with nothing to cite converts poorly and invites paid-link offers. Linkable assets, in order of how often they earn links on their own:

- **Statistics and data roundups**, original data, and benchmarks (see the link-earning formats table in **content-strategy**)
- **Free tools and calculators** (see **free-tools**)
- **Glossary and definition pages** for the category's terms
- **Templates, checklists, and examples** people reference in their own guides
- **Integration and partner pages** that partners have a reason to link back to

Put the asset near the target page and link to the target page from it. Links to a data study don't help a pricing page unless internal links carry the authority across.

## Step 3: Pick Tactics by Effort and Quality

Start at the top. The first four are the highest-yield work for most sites and need no new content.

| Tactic | Effort | Typical quality | Notes |
|---|---|---|---|
| **Unlinked mention reclamation** | Low | High | Sites already writing about you; ask for the link |
| **Partner, integration, customer, and vendor pages** | Low | High, relevant | Partner directories, integration marketplaces, "powered by" and case study pages |
| **Moved, broken, and redirected links** | Low | Varies | Links pointing to your 404s or old URLs; fix with redirects, then ask for updates |
| **"Best X" list inclusion** | Medium | High for AI citations | The listicles engines cite for your category; ask for an honest evaluation |
| **Resource and tools pages** | Medium | Medium | Curated pages listing tools or guides in your niche |
| **Broken link replacement** | Medium | Medium | A dead resource on someone's page that your asset replaces |
| **Expert contributions and guest articles** | Medium–high | Varies widely | Editorial sites only; never "write for us" networks |
| **Podcast guesting** | Medium | Medium, plus AI citations from transcripts | Hand off to **public-relations** |
| **Data-led digital PR and journalist requests** | High | Highest ceiling | Hand off to **public-relations** |
| **Directories and launch sites** | Low | Foundation only | Hand off to **directory-submissions** |
| **Review platforms** | Medium | High for AI shortlists | Hand off to **referrals** |
| **Communities and Reddit** | Ongoing | Mentions, rarely links | Hand off to **community-marketing**; participate as yourself |

Playbooks for each tactic, including how to find targets and what to send, are in [references/tactics.md](references/tactics.md).

### Choosing targets for AI citations

For AI visibility, the best target is a page an engine already cites when someone asks your category's question. Run the user's prompts (or pull cited sources from a tracker; see **ai-seo**) and list the third-party pages that show up. Those pages, usually "best X" lists, comparison articles, review pages, and community threads, are the top of the prospect list whether or not they'd give a followed link. Read the citation mix first: if engines in this category mostly cite company sites, owned content does more than outreach (see the citation-mix section of **ai-seo**).

## Step 4: Prospect, Qualify, Reach Out

Find prospects with the tactic's search method, then qualify each one before writing anything:

- **Relevant:** would this site's readers plausibly need the product? Topic relevance matters more than domain rating.
- **Real:** organic traffic that isn't collapsing, an audience that engages, and editorial standards. Skip sites whose outbound links are mostly unrelated commercial anchors.
- **Reachable:** a named person who owns the page.
- **Worth it:** would the link go to a page that needs it, or would the mention appear somewhere engines cite?

Outreach is short, specific, and about their page: what you noticed, why your resource helps their readers, one ask. Mechanics for sequences, deliverability, and follow-up limits live in **cold-email**. Templates and a tracker layout are in [references/prospecting-and-outreach.md](references/prospecting-and-outreach.md).

Draft outreach for the user to approve and send. Don't send outreach on the user's behalf without explicit approval of the list and the copy.

## Step 5: Stay Inside the Rules

Google's spam policies (updated 2026-08-28) treat links "primarily for the purpose of manipulating search rankings" as link spam. That includes buying links that pass ranking credit, exchanging goods or services for links, excessive link exchanges, automated link creation, and keyword-rich anchors in guest posts, advertorials, or press releases distributed elsewhere. Paid links are fine when they carry `rel="sponsored"` or `rel="nofollow"`.

What this means for the work:

- **You can pay for a placement when the link passes no ranking credit.** Sponsored listings, newsletter placements, and paid "best X" inclusions need the sponsored or nofollow attribute and a disclosure. They can still be worth it for AI citations and referral traffic.
- **Products in exchange for a review-with-link count as payment.** The link needs a qualifying attribute.
- **Link swaps are fine in moderation and when relevant.** Partner pages built only to cross-link are not.
- **Guest posts are for reach and expertise.** Use branded or plain anchors in author bios and body links.
- **Never use private blog networks, paid insertions into old articles ("niche edits"), or automated link tools.**

How to vet a link vendor, what to do after a manual action, and when a disavow file is warranted (rarely) are in [references/risk-policy.md](references/risk-policy.md).

## Step 6: Anchors and Pace

- **Let other people choose the anchor text.** Natural profiles are mostly branded, URL, and generic anchors. Ask for the link and leave the wording to them.
- **Don't plan a link velocity.** There's no safe or unsafe number of links per month for earned links. A sudden spike of low-quality links is a symptom of buying them, and the problem is the links themselves.
- **Spread links across pages that need them.** Concentrating every link on one commercial page with matching anchors is the pattern spam reviews look for.

## Step 7: Measure Both Outcomes

| Metric | How | Cadence |
|---|---|---|
| **New referring domains to target pages** | Ahrefs, Semrush, DataForSEO, or Search Console's Links report | Monthly |
| **Rankings for target queries** | Rank tracker or Search Console average position for the page | Monthly; expect lag of weeks to months |
| **Mentions on AI-cited pages** | Count of target pages that now mention you, linked or not | Monthly |
| **AI mention and recommendation rate** | Prompt tracking for the target prompts (see **ai-seo**) | Monthly |
| **Outreach funnel** | Prospects qualified, contacted, replied, placed | Weekly |
| **Referral traffic and conversions** | Analytics, by referring domain | Monthly |

Report placements by target page. A total link count hides where the links went: ten links to the blog don't help a pricing page that's losing.

## Running It as a Loop

Link building works as a weekly habit more than a campaign. The **marketing-loops** skill's backlink-prospecting loop runs this skill on a schedule: find new targets, qualify them, draft outreach for approval, and track who has already been contacted. Its brand-mention loop sends unlinked mentions here for reclamation.

## Tools

| Need | Tools |
|---|---|
| Backlink data, link gap, competitor links | [Ahrefs](../../tools/integrations/ahrefs.md), [Semrush](../../tools/integrations/semrush.md), [DataForSEO](../../tools/integrations/dataforseo.md), Moz |
| Finding prospects and mentions | Search operators, [Exa](../../tools/integrations/exa.md), [Firecrawl](../../tools/integrations/firecrawl.md), Google Alerts, mention monitors |
| Finding the contact | [Hunter](../../tools/integrations/hunter.md), the site's own about or contact page |
| Done-for-you placements | Managed placement services such as [LinkDR](https://linkdr.com) source sites, pitch editors, and confirm links go live. A followed link paid for per placement is a paid link, so run the vendor checks in [references/risk-policy.md](references/risk-policy.md) first |
| Free fallback | Search Console's Links report for your own links; search operators for prospects |

## Output Format

For a link building plan, deliver:

1. **Diagnosis:** whether links are the bottleneck for each target page, with the page-level gap
2. **Assets:** what exists to link to, and what to build first if nothing does
3. **Tactic mix:** the three or four tactics to run first, with why
4. **Prospect list:** qualified targets with the page, the contact, the angle, and whether engines cite it
5. **Outreach drafts:** for approval, one per tactic at minimum
6. **Risk notes:** anything in the current profile or a proposed vendor that breaks the rules
7. **Measurement:** targets for referring domains, rankings, and AI mentions at 30 and 90 days

## Related Skills

- **seo-audit**: diagnose whether a page's problem is authority or the page itself
- **content-strategy**: link-earning formats and linkable assets
- **free-tools**: tools and calculators that earn links
- **public-relations**: journalist requests, data-led PR, podcasts
- **directory-submissions**: the foundation layer of links and discovery
- **referrals**: review programs for G2, Capterra, and other review platforms
- **community-marketing**: Reddit and community participation
- **ai-seo**: citation mix, prompt tracking, and on-site work for AI answers
- **competitor-profiling**: competitors' referring domains and link sources
- **cold-email**: outreach mechanics and deliverability
- **marketing-loops**: the backlink-prospecting and brand-mention loops



---

## `references/prospecting-and-outreach.md`

# Prospecting and Outreach

How to build a prospect list, qualify it, write outreach people answer, and track it so nobody gets pitched twice.

## Building the List

Start from the target page and work outward:

1. **Competitor link gap.** Pull referring domains for the three to five pages that outrank the target page. Domains that link to two or more competitors but not to you are the warmest prospects (Ahrefs Link Intersect, Semrush Backlink Gap, or a DataForSEO backlinks comparison).
2. **AI-cited pages.** Run the target prompts and record the third-party pages engines cite. Add every one that discusses the category.
3. **Tactic searches.** Unlinked mentions, resource pages, broken links, and "best X" lists, using the searches in [tactics.md](tactics.md).
4. **Relationships.** Partners, integrations, customers, vendors, and event organizers.

Deduplicate by domain and keep the specific page with each domain, because outreach is about a page.

## Qualifying

Score each prospect before writing. Drop anything that fails the first two.

| Check | Pass | Fail |
|---|---|---|
| **Relevance** | Readers could plausibly need the product, or the page covers the category | Unrelated topic, whatever its domain rating |
| **Legitimacy** | Real organic traffic, named authors, editorial standards | Outbound links mostly unrelated commercial anchors, "write for us" on every topic, link prices listed |
| **AI citation** | Engines cite this page for the target prompts | Not cited (doesn't fail, just scores lower) |
| **Value to the target page** | A link here would reach a page that needs authority | Would only link the homepage |
| **Reachability** | A named person owns the page | Only a generic form |

Domain rating and similar scores are third-party estimates. Use them to sort, never as the qualifying test.

## Writing Outreach

Rules that apply to every tactic:

- **Lead with their page.** Name the page and what you noticed on it. If you can't name something specific, the prospect isn't qualified yet.
- **One ask.** Pick one: a link, an update, or an evaluation.
- **Make it easy.** Give the exact URL and, for a fix, the exact location on their page.
- **Offer something real** when you have it: a data point for their article, a fixed broken link, an expert quote, a free account to evaluate. Never offer money for a followed link.
- **Keep it under 100 words.** Editors skim.
- **One follow-up**, about a week later. Then stop. See **cold-email** for sending limits, deliverability, and opt-out handling.

### Unlinked mention

```
Subject: Thanks for including [brand] in [article title]

Hi [name],

Thanks for mentioning [brand] in "[article title]". The line about [specific detail] was spot on.

Would you link the mention to [specific URL]? It covers [what the reader gets there], which fits that section.

[sender name]
```

### Broken link

```
Subject: Broken link on [page title]

Hi [name],

The link to [dead resource name] in your "[page title]" section on [their page] returns a 404.

If you want a replacement, our [asset name] covers the same [topic], updated for [year]: [URL]. Either way, wanted you to know.

[sender name]
```

### "Best X" evaluation

```
Subject: [product] for your [list title]

Hi [name],

Your "[list title]" is one of the guides people use to choose a [category] tool. We're [product], built for [specific audience and use case].

If you update it, I can send a free account, pricing, and screenshots so you can judge it yourself.

[sender name]
```

### Resource page

```
Subject: A resource for your [page title] page

Hi [name],

Your [page title] page lists [type of resources] for [audience]. Our [asset name] ([URL]) is a free [what it is] that [what it does for that audience].

If it fits the list, I'd be glad to see it there.

[sender name]
```

Rewrite each draft for the specific page. Templates sent unchanged read as templates.

## Tracking

Keep one sheet so nobody is contacted twice and results can be measured:

| Column | What goes in it |
|---|---|
| Domain and page | The exact URL |
| Tactic | Mention, broken link, list, resource, partner, guest |
| Target page | Which of your pages the link should go to |
| AI-cited? | Yes or no, and for which prompt |
| Contact | Name, role, how found |
| Status | Qualified, drafted, approved, sent, followed up, replied, placed, declined |
| Dates | Sent, followed up, placed |
| Result | Link (followed, nofollow, sponsored), mention only, or none |

The **marketing-loops** backlink-prospecting loop reads this sheet as its state, so a weekly run can skip anyone already contacted.



---

## `references/risk-policy.md`

# Risk Policy

What Google treats as link spam, how to judge a link vendor or a paid placement, and what to do if the profile already has problems. Policy checked against Google Search Central's spam policies, last updated 2026-08-28. Re-check before advising on a borderline case.

## What Google Says

Google defines link spam as creating links "primarily for the purpose of manipulating search rankings." Named examples include:

- Buying or selling links that pass ranking credit, including exchanging goods or services for links and sending a product in exchange for a post with a link
- Excessive link exchanges, and partner pages made only for cross-linking
- Automated programs or services that create links
- Text ads or text links that don't block ranking credit
- Advertorials or native ads with paid links that pass ranking credit
- Links with optimized anchor text in articles, guest posts, or press releases distributed on other sites

Google also says buying and selling links is a normal part of advertising and sponsorship, and that it's not a violation as long as the links carry `rel="sponsored"` or `rel="nofollow"`. Use `rel="ugc"` for user-generated content such as comments and forum posts.

Separately, the **site reputation abuse** policy covers third-party content placed on a strong site mainly to borrow its ranking signals. Paying for an article on a big publisher's "partner content" section to rank a commercial page falls here.

## Paid Placements

Paying for visibility is legitimate. The rule is about ranking credit and disclosure.

| Placement | Allowed? | Requirement |
|---|---|---|
| Sponsored listing in a directory or "best X" list | Yes | `sponsored` or `nofollow` link, and a visible disclosure |
| Newsletter or podcast sponsorship | Yes | Disclosed as sponsored; links in email don't pass ranking credit anyway |
| Free product sent for review | Yes | The reviewer qualifies the link and discloses the relationship (FTC endorsement rules apply in the US) |
| Paid guest post with a followed link | No | Link spam |
| Paid insertion into an existing article ("niche edit") | No | Link spam |
| Private blog network links | No | Link spam |

A sponsored placement can still be worth buying for referral traffic and AI visibility. AI engines read the page whether or not the link passes ranking credit. Judge it on audience and citation value, and never promise the user an SEO lift from it.

## Vetting a Link Vendor

When the user asks whether a link building agency or marketplace is safe, check:

1. **Do they sell "do-follow" links at a price per link or by domain rating?** That's selling ranking credit. Decline.
2. **Can they show the placements?** Real outreach produces pages on sites with their own audience and named authors. A list of sites that publish anything for a fee is a network.
3. **Do the sites sell to everyone?** Look for a "write for us" page on every topic, outbound links to unrelated casinos, loans, or supplements, and traffic that's flat or falling.
4. **Is the anchor text yours to choose?** Vendors who let you pick exact-match anchors on guest posts are offering the pattern Google names.
5. **What do they report?** Link counts and domain rating alone, with no rankings or traffic, means the links are the product.

Legitimate agencies sell the work: content, digital PR, outreach on your behalf, and placements they can't guarantee.

## If the Profile Already Has Problems

- **Manual action in Search Console:** read the notice under Security & Manual Actions. Remove or qualify the links you control or paid for, document what you couldn't remove, then file a reconsideration request that explains what happened and what changed.
- **No manual action, but a history of bought links:** stop buying, ask for removal or a `sponsored` attribute where you have a contact, and focus on earning links. Google says it ignores most spammy links algorithmically.
- **Disavow:** Google recommends the disavow tool only when there's a manual action, or a large number of paid or spammy links you created that are likely to cause one. Don't disavow links just because a tool scores them as "toxic." A disavow of good links can hurt.
- **Negative SEO worries:** random spammy links pointing at a site are common and usually ignored. Watch for a manual action instead of reacting to every one.

## Disclosure Inside This Repo's Guidance

When a recommendation involves paying a site, a creator, or a vendor, say so plainly and name the requirement (link attribute and audience disclosure). Recommend more than one option, and say when a vendor has a commercial relationship with the person recommending it.



---

## `references/tactics.md`

# Link Building Tactics

Playbooks for each tactic in the SKILL.md table: how to find targets, what to send, and what to watch for. Outreach templates are in [prospecting-and-outreach.md](prospecting-and-outreach.md).

## Contents
- Unlinked mention reclamation
- Partner, integration, customer, and vendor pages
- Moved, broken, and redirected links
- "Best X" list inclusion
- Resource and tools pages
- Broken link replacement
- Expert contributions and guest articles
- Handoffs: PR, podcasts, directories, reviews, communities

---

## Unlinked Mention Reclamation

Sites that already name your brand, product, founder, or data without linking. The writer has already decided you're relevant, so the ask is small.

**Find them:**
- Search for the brand in quotes, minus your own domain: `"brand name" -site:yourdomain.com`
- Repeat for the product names, the founder's name, and the titles of your data studies
- Use a mention monitor or the mentions report in Ahrefs or Semrush, filtered to pages that don't link to you
- Run the user's AI prompts and check whether the third-party pages engines cite mention you without a link

**Qualify:** skip forum posts, scraped copies, and pages that mention you negatively (those need a response decision before any outreach).

**Ask:** one line thanking them for the mention, the exact sentence that mentions you, and the URL that would help their reader most. That's often a specific page rather than the homepage.

Mentions on AI-cited pages count even if the writer declines to add a link. Log them as wins for AI visibility.

## Partner, Integration, Customer, and Vendor Pages

The most relevant links you can get, and the easiest, because there's a business relationship already.

- **Integration partners:** most have an integrations directory or marketplace listing. Ask for the listing, a partner page, and a mention in their docs where the integration is set up.
- **Technology vendors:** many tools feature customers in case studies or "built with" pages. Offer a case study.
- **Customers:** customers who publish their stack, or write about how they work, may link to you. Ask the happy ones, and only ask once.
- **Agencies and consultants** who implement the product often keep a tools or partners page.
- **Events you sponsor or speak at** list sponsors and speakers. Check that the link goes to a useful page.

Reciprocal links between real partners are normal. A partner page built only to swap links isn't (see [risk-policy.md](risk-policy.md)).

## Moved, Broken, and Redirected Links

Links you already earned but are losing.

1. Export your backlinks and filter to target URLs that return 404 or redirect chains.
2. Redirect each dead URL (301) to the closest live equivalent. This recovers most of the value without outreach.
3. For high-value links pointing at redirects, ask the site to update the URL directly.
4. After any site migration or URL change, rerun this check. Migrations lose more links than most outreach campaigns earn.

## "Best X" List Inclusion

The listicles and comparison articles that rank for "best [category]" queries, and that AI engines cite when asked the same question. For AI shortlists, these are the most valuable pages in the category.

**Find them:**
- Search the category's "best X," "top X," "X alternatives," and "X vs Y" queries, plus variants by use case and audience ("best X for agencies")
- Run the same questions through ChatGPT, Perplexity, Gemini, and AI Overviews and record which articles get cited
- Check which lists name two or more of your competitors but not you

**Qualify:** prefer lists that are updated, rank or get cited, and evaluate products with some evidence. A list that sells every slot is advertising; any placement there needs a `sponsored` link and a disclosure.

**Ask:** offer what the writer needs to evaluate you honestly: a short product summary, who it's best for, pricing, a free account or demo, and screenshots. Don't ask to be ranked first. Lists that rank the category leader first and explain where alternatives win tend to be the ones engines trust.

**Watch for:** writers who want payment for inclusion. Paying is allowed only with a qualifying link attribute and a disclosure; decide whether the placement is worth it for referral traffic and AI visibility alone.

## Resource and Tools Pages

Curated pages that list tools, guides, or templates in a niche: university resource pages, association member resources, "tools we use" pages, and curated GitHub "awesome" lists.

**Find them:** `"[topic]" inurl:resources`, `"[topic]" "useful links"`, `"[topic]" intitle:tools`, `awesome-[topic]` on GitHub.

**Ask:** point to the one asset that fits the list. Product homepages rarely belong on resource pages; free tools, templates, and guides do.

## Broken Link Replacement

A dead link on someone else's page that your asset could replace.

1. Find pages in your niche with outbound links to 404s. Ahrefs and Semrush both report broken outbound links on a domain; the Wayback Machine shows what the dead page contained.
2. Pick dead resources that many pages linked to. One dead study with 50 linking pages is 50 prospects.
3. Make sure your replacement covers what the dead page did. If it doesn't, build it first or skip it.
4. Tell the site owner which link is broken and where (they get a fix), then offer your page as one replacement.

## Expert Contributions and Guest Articles

Writing for editorial sites your buyers read. The point is reach and credibility with that audience; the link is a side effect.

- Pitch topics where the author has real expertise and the site has a gap.
- Write for sites with editorial standards, where an editor reviews submissions. Skip sites with a "write for us" page that accepts anything on any topic, and anyone selling guest-post slots.
- Use a branded or plain-language link in the author bio and at most one contextual link where it helps the reader. Keyword-rich anchors in guest posts are a named example of link spam.
- Expert quote requests and roundup contributions are lighter-weight versions of the same tactic; see **public-relations** for journalist request platforms.

## Handoffs

These tactics have their own skills. Use them, then count the results here.

| Tactic | Skill | What it adds for links and citations |
|---|---|---|
| Data-led digital PR, newsjacking, journalist requests | **public-relations** | Editorial links from news and trade press; the highest ceiling and the most effort |
| Podcast guesting | **public-relations** | Show-notes links, and transcripts that AI engines can retrieve |
| Startup, SaaS, AI, and MCP directories | **directory-submissions** | A foundation of relevant links and discovery |
| G2, Capterra, and other review platforms | **referrals** | Review pages that AI engines cite for shortlists |
| Reddit, Slack, Discord, and forums | **community-marketing** | Mentions in threads engines retrieve. Participate as yourself and disclose your affiliation; planted posts and sockpuppet accounts break platform rules and get removed |
| Co-authored content and partner campaigns | **co-marketing** | Links from partners' audiences, with relevant reciprocal linking |
