# design-system

Original: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/b7d5353/.claude/skills/design-system

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs, strategic slide creation. Use for design tokens, systematic design, brand-compliant presentations.


# Design System

Token architecture, component specifications, systematic design, slide generation.

## When to Use

- Design token creation
- Component state definitions
- CSS variable systems
- Spacing/typography scales
- Design-to-code handoff
- Tailwind theme configuration
- **Slide/presentation generation**

## Token Architecture

Load: `references/token-architecture.md`

### Three-Layer Structure

```
Primitive (raw values)
       ↓
Semantic (purpose aliases)
       ↓
Component (component-specific)
```

**Example:**
```css
/* Primitive */
--color-blue-600: #2563EB;

/* Semantic */
--color-primary: var(--color-blue-600);

/* Component */
--button-bg: var(--color-primary);
```

## Script Paths

Script paths in this skill and its `references/` are relative to the directory that contains this SKILL.md, not to the project: `scripts/<file>` is this skill's own `scripts/` folder, and `../<skill>/scripts/<file>` is a sibling sub-skill installed alongside it. Build the full path from that directory (Claude Code reports it as the skill's base directory when the skill loads) and keep the working directory at the project root — the scripts read and write project files such as `docs/brand-guidelines.md`, `assets/design-tokens.json` or `src/` relative to it.

## Quick Start

**Generate tokens:**
```bash
node scripts/generate-tokens.cjs --config tokens.json -o tokens.css
```

**Validate usage:**
```bash
node scripts/validate-tokens.cjs --dir src/
```

## References

| Topic | File |
|-------|------|
| Token Architecture | `references/token-architecture.md` |
| Primitive Tokens | `references/primitive-tokens.md` |
| Semantic Tokens | `references/semantic-tokens.md` |
| Component Tokens | `references/component-tokens.md` |
| Component Specs | `references/component-specs.md` |
| States & Variants | `references/states-and-variants.md` |
| Tailwind Integration | `references/tailwind-integration.md` |

## Component Spec Pattern

| Property | Default | Hover | Active | Disabled |
|----------|---------|-------|--------|----------|
| Background | primary | primary-dark | primary-darker | muted |
| Text | white | white | white | muted-fg |
| Border | none | none | none | muted-border |
| Shadow | sm | md | none | none |

## Scripts

| Script | Purpose |
|--------|---------|
| `generate-tokens.cjs` | Generate CSS from JSON token config |
| `validate-tokens.cjs` | Check for hardcoded values in code |
| `search-slides.py` | BM25 search + contextual recommendations |
| `slide-token-validator.py` | Validate slide HTML for token compliance |
| `fetch-background.py` | Fetch images from Pexels/Unsplash |

## Templates

| Template | Purpose |
|----------|---------|
| `design-tokens-starter.json` | Starter JSON with three-layer structure |

## Integration

**With brand:** Extract primitives from brand colors/typography
**With ui-styling:** Component tokens → Tailwind config

**Skill Dependencies:** brand, ui-styling
**Primary Agents:** ui-ux-designer, frontend-developer

## Slide System

Brand-compliant presentations using design tokens + Chart.js + contextual decision system.

### Source of Truth

| File | Purpose |
|------|---------|
| `docs/brand-guidelines.md` | Brand identity, voice, colors |
| `assets/design-tokens.json` | Token definitions (primitive→semantic→component) |
| `assets/design-tokens.css` | CSS variables (import in slides) |
| `assets/css/slide-animations.css` | CSS animation library |

### Slide Search (BM25)

```bash
# Basic search (auto-detect domain)
python scripts/search-slides.py "investor pitch"

# Domain-specific search
python scripts/search-slides.py "problem agitation" -d copy
python scripts/search-slides.py "revenue growth" -d chart

# Contextual search (Premium System)
python scripts/search-slides.py "problem slide" --context --position 2 --total 9
python scripts/search-slides.py "cta" --context --position 9 --prev-emotion frustration
```

### Decision System CSVs

| File | Purpose |
|------|---------|
| `data/slide-strategies.csv` | 15 deck structures + emotion arcs + sparkline beats |
| `data/slide-layouts.csv` | 25 layouts + component variants + animations |
| `data/slide-layout-logic.csv` | Goal → Layout + break_pattern flag |
| `data/slide-typography.csv` | Content type → Typography scale |
| `data/slide-color-logic.csv` | Emotion → Color treatment |
| `data/slide-backgrounds.csv` | Slide type → Image category (Pexels/Unsplash) |
| `data/slide-copy.csv` | 25 copywriting formulas (PAS, AIDA, FAB) |
| `data/slide-charts.csv` | 25 chart types with Chart.js config |

### Contextual Decision Flow

```
1. Parse goal/context
        ↓
2. Search slide-strategies.csv → Get strategy + emotion beats
        ↓
3. For each slide:
   a. Query slide-layout-logic.csv → layout + break_pattern
   b. Query slide-typography.csv → type scale
   c. Query slide-color-logic.csv → color treatment
   d. Query slide-backgrounds.csv → image if needed
   e. Apply animation class from slide-animations.css
        ↓
4. Generate HTML with design tokens
        ↓
5. Validate with slide-token-validator.py
```

### Pattern Breaking (Duarte Sparkline)

Premium decks alternate between emotions for engagement:
```
"What Is" (frustration) ↔ "What Could Be" (hope)
```

System calculates pattern breaks at 1/3 and 2/3 positions.

### Slide Requirements

**ALL slides MUST:**
1. Import `assets/design-tokens.css` - single source of truth
2. Use CSS variables: `var(--color-primary)`, `var(--slide-bg)`, etc.
3. Use Chart.js for charts (NOT CSS-only bars)
4. Include navigation (keyboard arrows, click, progress bar)
5. Center align content
6. Focus on persuasion/conversion

### Chart.js Integration

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

<canvas id="revenueChart"></canvas>
<script>
new Chart(document.getElementById('revenueChart'), {
    type: 'line',
    data: {
        labels: ['Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            data: [5, 12, 28, 45],
            borderColor: '#FF6B6B',  // Use brand coral
            backgroundColor: 'rgba(255, 107, 107, 0.1)',
            fill: true,
            tension: 0.4
        }]
    }
});
</script>
```

### Token Compliance

```css
/* CORRECT - uses token */
background: var(--slide-bg);
color: var(--color-primary);
font-family: var(--typography-font-heading);

/* WRONG - hardcoded */
background: #0D0D0D;
color: #FF6B6B;
font-family: 'Space Grotesk';
```

### Reference Implementation

Working example with all features:
```
assets/designs/slides/claudekit-pitch-251223.html
```

### Command

```bash
/slides:create "10-slide investor pitch for ClaudeKit Marketing"
```

## Best Practices

1. Never use raw hex in components - always reference tokens
2. Semantic layer enables theme switching (light/dark)
3. Component tokens enable per-component customization
4. Use HSL format for opacity control
5. Document every token's purpose
6. **Slides must import design-tokens.css and use var() exclusively**



---

## `data/slide-backgrounds.csv`

````csv
slide_type,image_category,overlay_style,text_placement,image_sources,search_keywords
hero,abstract-tech,gradient-dark,center,pexels:unsplash,technology abstract gradient dark
vision,future-workspace,gradient-brand,left,pexels:unsplash,futuristic office modern workspace
team,professional-people,gradient-dark,bottom,pexels:unsplash,business team professional diverse
testimonial,office-environment,blur-dark,center,pexels:unsplash,modern office workspace bright
cta,celebration-success,gradient-brand,center,pexels:unsplash,success celebration achievement
problem,frustration-pain,desaturate-dark,center,pexels:unsplash,stress frustration problem dark
solution,breakthrough-moment,gradient-accent,right,pexels:unsplash,breakthrough success innovation light
hook,attention-grabbing,gradient-dark,center,pexels:unsplash,dramatic abstract attention bold
social,community-connection,blur-dark,center,pexels:unsplash,community collaboration connection
demo,product-showcase,gradient-dark,left,pexels:unsplash,technology product showcase clean
````



---

## `data/slide-charts.csv`

````csv
id,chart_type,keywords,best_for,data_type,when_to_use,when_to_avoid,max_categories,slide_context,css_implementation,accessibility_notes,sources
1,Bar Chart Vertical,"bar, vertical, comparison, categories, ranking",Comparing values across categories,Categorical discrete,"Comparing 3-12 categories, showing ranking, highlighting differences",Continuous time data trends,12,Traction metrics feature comparison,"Chart.js or CSS flexbox with height percentage bars",Always label axes include values,Atlassian Data Charts
2,Bar Chart Horizontal,"horizontal bar, ranking, long labels, categories",Categories with long names ranking,Categorical discrete,"Long category names, 5+ items, reading left-to-right natural",Few categories time series,15,Team performance competitor analysis,"CSS flexbox with width percentage bars",Natural reading direction for labels,Datylon Blog
3,Line Chart,"line, trend, time series, growth, change over time",Showing trends over continuous time,Time series continuous,"Time-based data, showing growth trajectory, 10+ data points",Categorical comparisons,50+ points,Revenue growth MRR user growth,"Chart.js line or SVG path element",Include data point markers for screen readers,Tableau Best Practices
4,Area Chart,"area, cumulative, volume, trend, filled line",Showing volume or magnitude over time,Time series cumulative,"Emphasizing magnitude, showing cumulative totals, comparing totals",Precise value comparison,3-4 series,Revenue breakdown market share over time,"Chart.js area or SVG path with fill",Use patterns not just colors for series,Data Visualization Guide
5,Pie Chart,"pie, composition, percentage, parts, whole",Showing parts of a whole,Proportional percentage,"2-5 slices, showing simple composition, adds to 100%",More than 6 categories precise comparison,6 max,Market share budget allocation simple splits,"CSS conic-gradient or Chart.js pie",Never use 3D always include percentages,FusionCharts Blog
6,Donut Chart,"donut, composition, percentage, center metric",Parts of whole with center highlight,Proportional percentage,"Like pie but need center space for key metric, 2-5 segments",Many categories,6 max,Composition with key stat in center,"CSS conic-gradient with inner circle",Same as pie include legend,Modern alternative to pie
7,Stacked Bar,"stacked, composition, comparison, breakdown",Comparing composition across categories,Categorical + proportional,"Showing composition AND comparison, segment contribution",Too many segments precise values,5 segments,Revenue by segment across quarters,"Chart.js stacked bar or CSS nested divs",Order segments consistently use legend,Atlassian Data Charts
8,Grouped Bar,"grouped, clustered, side by side, multi-series",Comparing multiple metrics per category,Multi-series categorical,"Direct comparison of 2-3 metrics per category",Too many groups (>4) or categories (>8),4 groups,Feature comparison pricing tiers,"Chart.js grouped bar CSS grid bars",Color code consistently across groups,Data Visualization Best Practices
9,100% Stacked Bar,"100%, proportion, normalized, percentage",Comparing proportions across categories,Proportional comparative,"Comparing percentage breakdown across categories, not absolute values",Showing absolute values,5 segments,Market share comparison percentage breakdown,"CSS flexbox 100% width segments",Clearly indicate percentage scale,Proportional analysis
10,Funnel Chart,"funnel, conversion, stages, drop-off, pipeline",Showing conversion or drop-off through stages,Sequential stage-based,"Sales funnel, conversion rates, sequential process with decreasing values",Non-sequential data equal stages,6-8 stages,User conversion sales pipeline,"CSS trapezoid shapes or SVG",Label each stage with count and percentage,Marketing/Sales standard
11,Gauge Chart,"gauge, progress, goal, target, kpi",Showing progress toward a goal,Single metric vs target,"Single KPI progress, goal completion, health scores",Multiple metrics,1 metric,Goal progress health score,"CSS conic-gradient or arc SVG",Include numeric value not just visual,Dashboard widgets
12,Sparkline,"sparkline, mini, inline, trend, compact",Showing trend in minimal space,Time series inline,"Inline metrics, table cells, compact trend indication",Detailed analysis,N/A,Metric cards with trend indicator,SVG path or canvas inline,Supplement with text for accessibility,Edward Tufte
13,Scatter Plot,"scatter, correlation, relationship, distribution",Showing relationship between two variables,Bivariate continuous,"Correlation analysis, pattern detection, outlier identification",Categorical data simple comparisons,100+ points,Correlation analysis segmentation,Canvas or SVG circles positioned,Include trend line if meaningful,Statistical visualization
14,Bubble Chart,"bubble, three variables, scatter, size",Showing three variables simultaneously,Trivariate continuous,"Three-variable comparison, population/size matters",Simple comparisons,30-50 bubbles,Market analysis with size dimension,"SVG circles with varying radius",Legend for size scale essential,Data Visualization Guide
15,Heatmap,"heatmap, matrix, intensity, correlation, grid",Showing intensity across two dimensions,Matrix intensity,"Large data matrices, time-day patterns, correlation matrices",Few data points,Unlimited grid,Usage patterns correlation matrices,CSS grid with background-color intensity,Use colorblind-safe gradients,Datylon Blog
16,Waterfall Chart,"waterfall, bridge, contribution, breakdown",Showing how values add to a total,Cumulative contribution,"Financial analysis, showing positive/negative contributions",Non-additive data,10-15 items,Revenue bridge profit breakdown,"CSS positioned bars with connectors",Clear positive/negative color coding,Financial reporting standard
17,Treemap,"treemap, hierarchy, nested, proportion",Showing hierarchical proportional data,Hierarchical proportional,"Nested categories, space-efficient proportions, 2 levels max",Simple comparisons few items,50+ items,Budget breakdown category analysis,"CSS grid with calculated areas",Include text labels on larger segments,Ben Shneiderman
18,Radar Chart,"radar, spider, multi-metric, profile",Comparing multiple metrics for single item,Multi-metric profile,"Comparing 5-8 metrics for one or two items, skill profiles",More than 3 items to compare,8 axes max,Feature profile skill assessment,SVG polygon on axes,Ensure scale is clear and consistent,Profile comparison
19,Bullet Chart,"bullet, target, actual, performance",Showing actual vs target with ranges,KPI with target,"Progress against target with qualitative ranges",Simple goal tracking,1-3 per slide,KPI performance with targets,"CSS layered bars with markers",Clearly label target and actual,Stephen Few
20,Timeline,"timeline, chronology, history, milestones",Showing events over time,Event-based temporal,"History roadmap milestones, showing progression",Quantitative comparison,10-15 events,Company history product roadmap,"CSS flexbox with positioned markers",Ensure logical reading order,Chronological visualization
21,Sankey Diagram,"sankey, flow, distribution, connections",Showing flow or distribution between nodes,Flow distribution,"Showing how values flow from source to destination",Simple distributions,15-20 nodes,User flow budget flow,D3.js or dedicated library,Alternative text description essential,Complex flow visualization
22,KPI Card,"kpi, metric, number, stat, scorecard",Highlighting single important metric,Single metric,"Dashboard hero metrics, emphasizing one key number",Showing trends or comparisons,1 number,Main KPI highlight,"Large font-size centered number",Include trend context if relevant,Dashboard design
23,Progress Bar,"progress, completion, percentage, bar",Showing completion percentage,Single percentage,"Simple progress indication, goal completion",Multiple goals comparison,1 per context,Project completion goal progress,"CSS width with percentage gradient",Include numeric percentage,UI/UX standard
24,Comparison Table,"table, comparison, matrix, features",Detailed feature or value comparison,Multi-attribute categorical,"Detailed comparison, many attributes, exact values matter",Visual impact storytelling,10-15 rows,Feature matrix pricing comparison,"HTML table with CSS styling",Proper table headers and scope,Information design
25,Icon Array,"icon array, pictogram, proportion, visual",Showing proportions with visual metaphor,Proportional visual,"Making statistics tangible (e.g. 1 in 10 people), visual impact",Precise values large numbers,100 icons,Statistics visualization impact slides,"CSS grid or flexbox with icons",Describe proportion in text,ISOTYPE Otto Neurath
````



---

## `data/slide-color-logic.csv`

````csv
emotion,background,text_color,accent_usage,use_full_bleed,gradient,card_style
frustration,dark-surface,foreground,minimal,false,none,subtle-border
hope,accent-bleed,dark,none,true,none,none
fear,dark-background,primary,stats-only,false,none,glow-primary
relief,surface,foreground,icons,false,none,accent-bar
trust,surface-elevated,foreground,metrics,false,none,subtle-border
urgency,gradient,white,cta-button,true,primary,none
curiosity,dark-glow,gradient-text,badge,false,glow,glow-secondary
confidence,surface,foreground,chart-accent,false,none,none
warmth,dark-surface,foreground,avatar-ring,false,none,none
evaluation,surface-elevated,foreground,highlight,false,none,comparison
narrative,dark-background,foreground-secondary,timeline-dots,false,none,none
clarity,surface,foreground,icons,false,none,feature-card
interest,dark-glow,foreground,demo-highlight,false,glow,none
````



---

## `data/slide-copy.csv`

````csv
id,formula_name,keywords,components,use_case,example_template,emotion_trigger,slide_type,source
1,AIDA,"aida, attention, interest, desire, action",Attention→Interest→Desire→Action,Lead-gen CTAs general persuasion,"{Attention hook} → {Interesting detail} → {Desirable outcome} → {Action step}",Curiosity→Engagement→Want→Urgency,CTA slides,Classic copywriting 1898
2,PAS,"pas, problem, agitation, solution, dan kennedy",Problem→Agitate→Solution,Sales pages problem slides most reliable,"You're struggling with {problem}. It's costing you {agitation}. {Solution} fixes this.",Frustration→Fear→Relief,Problem slides,Dan Kennedy
3,4Ps,"4ps, promise, picture, proof, push, ray edwards",Promise→Picture→Proof→Push,Home pages lead-gen,"{Promise benefit} → {Picture future state} → {Proof it works} → {Push to act}",Hope→Vision→Trust→Action,Solution slides,Ray Edwards
4,Before-After-Bridge,"bab, before, after, bridge, transformation",Before→After→Bridge,Transformation case studies,"Before: {old state}. After: {new state}. Bridge: {how to get there}",Pain→Pleasure→Path,Before/after slides,Copywriting classic
5,QUEST,"quest, qualify, understand, educate, stimulate, transition",Qualify→Understand→Educate→Stimulate→Transition,Matching solution to prospect,"{Qualify audience} → {Show understanding} → {Educate on solution} → {Stimulate desire} → {Transition to CTA}",Recognition→Empathy→Learning→Excitement,Educational slides,Michel Fortin
6,Star-Story-Solution,"star, story, solution, narrative",Star→Story→Solution,Personality brands info products,"{Introduce character} → {Tell their struggle} → {Reveal their solution}",Connection→Empathy→Hope,Case study slides,CopyHackers
7,Feature-Advantage-Benefit,"fab, feature, advantage, benefit",Feature→Advantage→Benefit,Feature explanations product slides,"{Feature name}: {What it does} → {Why that matters} → {How it helps you}",Curiosity→Understanding→Desire,Feature slides,Sales training classic
8,What If,"what if, imagination, possibility, hook",What if + Possibility,Opening hooks vision slides,"What if you could {desirable outcome} without {common obstacle}?",Wonder→Possibility,Title problem slides,Headline formula
9,How To,"how to, tutorial, guide, instruction",How to + Specific outcome,Educational actionable content,"How to {achieve specific result} in {timeframe or steps}",Curiosity→Empowerment,Educational slides,Headline formula
10,Number List,"number, list, reasons, ways, tips",Number + Topic + Promise,Scannable benefit lists,"{Number} {Ways/Reasons/Tips} to {achieve outcome}",Curiosity→Completeness,Feature summary slides,Content marketing
11,Question Hook,"question, hook, curiosity, engagement",Question that implies answer,Opening engagement slides,"{Question that reader answers yes to}? Here's how.",Recognition→Curiosity,Opening slides,Rhetorical technique
12,Proof Stack,"proof, evidence, credibility, stats",Stat→Source→Implication,Building credibility trust,"{Impressive stat} (Source: {credible source}). This means {implication for audience}.",Trust→Validation,Traction proof slides,Social proof theory
13,Future Pacing,"future, vision, imagine, picture this",Imagine + Future state,Vision and aspiration slides,"Imagine: {desirable future scenario}. That's what {solution} delivers.",Aspiration→Desire,Solution CTA slides,NLP technique
14,Social Proof,"social proof, testimonial, customers, trust",Who + Result + Quote,Credibility through others,"{Customer name} increased {metric} by {amount}. '{Quote about experience}'",Trust→FOMO,Testimonial slides,Robert Cialdini
15,Scarcity Urgency,"scarcity, urgency, limited, deadline, fomo",Limited + Deadline + Consequence,Driving action urgency,"Only {quantity} available. Offer ends {date}. {Consequence of missing out}.",Fear of loss→Action,CTA closing slides,Cialdini influence
16,Cost of Inaction,"cost, inaction, consequence, loss",Current cost + Future cost + Comparison,Motivating change,"Every {timeframe} without {solution} costs you {quantified loss}. That's {larger number} per year.",Loss aversion→Urgency,Problem agitation slides,Loss aversion psychology
17,Simple Benefit,"benefit, value, outcome, result",You get + Specific benefit,Clear value communication,"{Solution}: You get {specific tangible benefit}.",Clarity→Desire,Any slide,Direct response
18,Objection Preempt,"objection, concern, but, however, faq",Objection + Response + Proof,"Handling concerns proactively","You might think {objection}. Actually, {counter with proof}.",Doubt→Resolution,FAQ objection slides,Sales training
19,Comparison Frame,"comparison, versus, than, better, alternative",Us vs Them + Specific difference,Competitive positioning,"{Competitor approach}: {limitation}. {Our approach}: {advantage}.",Evaluation→Preference,Comparison slides,Positioning strategy
20,Pain-Claim-Gain,"pcg, pain, claim, gain",Pain point→Bold claim→Specific gain,Concise value proposition,"{Pain point}? {Bold claim about solution}. Result: {specific gain}.",Frustration→Hope→Excitement,Problem/solution slides,Copywriting framework
21,One Thing,"one thing, single, focus, key",The one thing + Why it matters,Focus and clarity,"The #1 thing {audience} needs to {outcome} is {one thing}.",Focus→Clarity,Key message slides,Gary Keller concept
22,Riddle Open,"riddle, mystery, puzzle, question",Mystery + Reveal + Implication,Engagement through curiosity,"{Intriguing mystery or paradox}. The answer: {reveal}. For you: {implication}.",Mystery→Insight,Opening slides,Storytelling technique
23,Hero Journey,"hero, journey, transformation, story",Ordinary→Call→Challenge→Triumph,Narrative structure,"{Character in ordinary world} → {Discovers challenge} → {Overcomes with solution} → {Achieves transformation}",Identification→Tension→Triumph,Full deck structure,Joseph Campbell
24,Value Stack,"value, stack, bundle, worth",Component + Value → Total value,Justifying price/investment,"{Item 1} (Worth ${X}) + {Item 2} (Worth ${Y}) + ... = Total value ${Z}. Your investment: ${actual price}.",Value perception,Pricing offer slides,Info product marketing
25,Power Statement,"power, statement, bold, declaration",Bold declaration + Supporting fact,Authority and confidence,"{Bold declaration}. {Supporting evidence or fact}.",Confidence→Trust,Key message slides,Thought leadership
````



---

## `data/slide-layout-logic.csv`

````csv
goal,emotion,layout_pattern,direction,visual_weight,break_pattern,use_bg_image
hook,curiosity,split-hero,visual-right,70-visual,false,true
problem,frustration,card-grid,centered,balanced,false,false
agitation,fear,full-bleed-stat,centered,100-text,true,false
solution,relief,split-feature,visual-left,50-50,false,true
proof,trust,metric-grid,centered,numbers-dominant,false,false
social,connection,quote-hero,centered,80-text,true,true
comparison,evaluation,split-compare,side-by-side,balanced,false,false
traction,confidence,chart-insight,chart-left,60-chart,false,false
cta,urgency,gradient-cta,centered,100-text,true,true
team,warmth,team-grid,centered,balanced,false,true
pricing,evaluation,pricing-cards,centered,balanced,false,false
demo,interest,split-demo,visual-left,60-visual,false,false
vision,hope,full-bleed-hero,centered,100-visual,true,true
timeline,narrative,timeline-flow,horizontal,balanced,false,false
features,clarity,feature-grid,centered,balanced,false,false
````



---

## `data/slide-layouts.csv`

````csv
id,layout_name,keywords,use_case,content_zones,visual_weight,cta_placement,recommended_for,avoid_for,css_structure,card_variant,metric_style,quote_style,grid_columns,visual_treatment,animation_class
1,Title Slide,"title, cover, opening, intro, hero",Opening slide first impression,"Center: Logo + Title + Tagline, Bottom: Date/Presenter",Visual-heavy minimal text,None or subtle,All presentations,Never skip,"display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center",none,none,none,1,gradient-glow,animate-fade-up
2,Problem Statement,"problem, pain, challenge, issue",Establish the problem being solved,"Left: Problem headline, Right: Pain point bullets or icon grid",50/50 text visual balance,None,Pitch decks sales,Internal updates,"display:grid; grid-template-columns:1fr 1fr; gap:48px; align-items:center",icon-left,none,none,2,subtle-border,animate-stagger
3,Solution Overview,"solution, answer, approach, how",Introduce your solution,"Top: Solution headline, Center: Solution visual/diagram, Bottom: 3 key points",Visual-dominant,Subtle learn more,After problem slide,Without context,"display:flex; flex-direction:column; gap:32px",accent-bar,none,none,3,icon-top,animate-scale
4,Feature Grid,"features, grid, cards, capabilities, 3-column",Showcase multiple features,"Top: Section title, Grid: 3-6 feature cards with icon+title+description",Balanced grid,Bottom CTA optional,Product demos SaaS,Storytelling slides,"display:grid; grid-template-columns:repeat(3,1fr); gap:24px",accent-bar,none,none,3,icon-top,animate-stagger
5,Metrics Dashboard,"metrics, kpis, numbers, stats, data",Display key performance data,"Top: Context headline, Center: 3-4 large metric cards, Bottom: Trend context",Numbers-dominant,None,Traction slides QBRs,Early-stage no data,"display:grid; grid-template-columns:repeat(4,1fr); gap:16px",metric-card,gradient-number,none,4,none,animate-stagger-scale
6,Comparison Table,"comparison, vs, versus, table, matrix",Compare options or competitors,"Top: Comparison title, Center: Feature comparison table, Bottom: Conclusion",Table-heavy,Highlight winner row,Competitive analysis,Storytelling,"display:flex; flex-direction:column; table width:100%",comparison,none,none,2,highlight-winner,animate-fade-up
7,Timeline Flow,"timeline, roadmap, journey, steps, process",Show progression over time,"Top: Timeline title, Center: Horizontal timeline with milestones, Bottom: Current status",Visual timeline,End milestone CTA,Roadmaps history,Dense data,"display:flex; flex-direction:column; timeline:flex with arrows",none,none,none,1,timeline-dots,animate-stagger
8,Team Grid,"team, people, founders, leadership",Introduce team members,"Top: Team title, Grid: Photo + Name + Title + Brief bio cards",Photo-heavy,None or careers link,Investor decks about,Technical content,"display:grid; grid-template-columns:repeat(4,1fr); gap:24px",avatar-card,none,none,4,avatar-ring,animate-stagger
9,Quote Testimonial,"quote, testimonial, social proof, customer",Feature customer endorsement,"Center: Large quote text, Bottom: Photo + Name + Title + Company logo",Quote-dominant minimal UI,None,Sales case studies,Without real quotes,"display:flex; flex-direction:column; justify-content:center; font-size:large; font-style:italic",none,none,large-italic,1,author-avatar,animate-fade-up
10,Two Column Split,"split, two-column, side-by-side, comparison",Present two related concepts,"Left column: Content A, Right column: Content B",50/50 balanced,Either column bottom,Comparisons before/after,Single concept,display:grid; grid-template-columns:1fr 1fr; gap:48px,none,none,none,2,offset-image,animate-fade-up
11,Big Number Hero,"big number, stat, impact, headline metric",Emphasize one powerful metric,"Center: Massive number, Below: Context label and trend",Number-dominant,None,Impact slides traction,Multiple metrics,"display:flex; flex-direction:column; justify-content:center; align-items:center; font-size:120px",none,oversized,none,1,centered,animate-count
12,Product Screenshot,"screenshot, product, demo, ui, interface",Show product in action,"Top: Feature headline, Center: Product screenshot with annotations, Bottom: Key callouts",Screenshot-dominant,Try it CTA,Product demos,Abstract concepts,"display:flex; flex-direction:column; img max-height:60vh",none,none,none,1,screenshot-shadow,animate-scale
13,Pricing Cards,"pricing, plans, tiers, packages",Present pricing options,"Top: Pricing headline, Center: 2-4 pricing cards side by side, Bottom: FAQ or guarantee",Cards balanced,Each card has CTA,Sales pricing pages,Free products,"display:grid; grid-template-columns:repeat(3,1fr); gap:24px; .popular:scale(1.05)",pricing-card,none,none,3,popular-highlight,animate-stagger
14,CTA Closing,"cta, closing, call to action, next steps, final",Drive action end presentation,"Center: Bold headline + Value reminder, Center: Primary CTA button, Below: Secondary option",CTA-dominant,Primary center,All presentations,Middle slides,"display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center",none,none,none,1,gradient-bg,animate-pulse
15,Agenda Overview,"agenda, outline, contents, structure",Preview presentation structure,"Top: Agenda title, Center: Numbered list or visual timeline of sections",Text-light scannable,None,Long presentations,Short 3-5 slides,"display:flex; flex-direction:column; ol list-style-type:decimal",none,none,none,1,numbered-list,animate-stagger
16,Before After,"before, after, transformation, results, comparison",Show transformation impact,"Left: Before state (muted), Right: After state (vibrant), Center: Arrow or transition",50/50 high contrast,After column CTA,Case studies results,No transformation data,"display:grid; grid-template-columns:1fr 1fr; .before:opacity(0.7)",comparison,none,none,2,contrast-pair,animate-scale
17,Icon Grid Stats,"icons, stats, grid, key points, summary",Summarize key points visually,"Grid: 4-6 icon + stat + label combinations",Icons-dominant,None,Summary slides,Detailed explanations,"display:grid; grid-template-columns:repeat(3,1fr); gap:32px; text-align:center",icon-stat,sparkline,none,3,icon-top,animate-stagger
18,Full Bleed Image,"image, photo, visual, background, hero",Create visual impact,"Full background image, Overlay: Text with contrast, Corner: Logo",Image-dominant,Overlay CTA optional,Emotional moments,Data-heavy,background-size:cover; color:white; text-shadow for contrast,none,none,none,1,bg-overlay,animate-ken-burns
19,Video Embed,"video, demo, embed, multimedia",Show video content,"Top: Context headline, Center: Video player (16:9), Bottom: Key points if needed",Video-dominant,After video CTA,Demos testimonials,Reading-focused,"aspect-ratio:16/9; video controls",none,none,none,1,video-frame,animate-scale
20,Funnel Diagram,"funnel, conversion, stages, pipeline",Show conversion or process flow,"Top: Funnel title, Center: Funnel visualization with stage labels and metrics",Diagram-dominant,None,Sales marketing funnels,Non-sequential data,SVG or CSS trapezoid shapes,none,funnel-numbers,none,1,funnel-gradient,animate-chart
21,Quote Plus Stats,"quote, stats, hybrid, testimonial, metrics",Combine social proof with data,"Left: Customer quote with photo, Right: 3 supporting metrics",Balanced quote/data,None,Sales enablement,Without both elements,"display:grid; grid-template-columns:1.5fr 1fr; gap:48px",metric-card,gradient-number,side-quote,2,author-avatar,animate-stagger
22,Section Divider,"section, divider, break, transition",Transition between sections,"Center: Section number + Section title, Minimal design",Typography-only,None,Long presentations,Every slide,"display:flex; justify-content:center; align-items:center; font-size:48px",none,none,none,1,section-number,animate-fade-up
23,Logo Grid,"logos, clients, partners, trust, social proof",Display client or partner logos,"Top: Trust headline, Grid: 8-16 logos evenly spaced",Logos-only,None,Credibility slides,Few logos <6,"display:grid; grid-template-columns:repeat(4,1fr); gap:32px; filter:grayscale(1)",none,none,none,4,logo-grayscale,animate-stagger
24,Chart Focus,"chart, graph, data, visualization, analytics",Present data visualization,"Top: Chart title and context, Center: Single large chart, Bottom: Key insight",Chart-dominant,None,Data-driven slides,Poor data quality,"chart max-height:65vh; annotation for key point",none,sparkline,none,1,chart-left,animate-chart
25,Q&A Slide,"qa, questions, discussion, interactive",Invite audience questions,"Center: Q&A or Questions? text, Below: Contact info or submission method",Minimal text,None,End of presentations,Skip if no time,"display:flex; justify-content:center; align-items:center; font-size:64px",none,none,none,1,centered,animate-fade-up
````



---

## `data/slide-strategies.csv`

````csv
id,strategy_name,keywords,slide_count,structure,goal,audience,tone,narrative_arc,key_metrics,sources,emotion_arc,sparkline_beats
1,YC Seed Deck,"yc, seed, startup, investor, funding, vc, venture","10-12","1.Title 2.Problem 3.Solution 4.Traction 5.Market 6.Product 7.Business Model 8.Team 9.Financials 10.Ask",Raise seed funding from VCs,Seed investors hunting asymmetric upside,Clear concise focused narrative,Problem→Solution→Evidence→Ask,MRR ARR growth rate user count,Y Combinator Library,"curiosity→frustration→hope→confidence→trust→urgency","hook|what-is|what-could-be|proof|proof|what-could-be|proof|trust|what-could-be|action"
2,Guy Kawasaki 10/20/30,"kawasaki, pitch, investor, 10 slides, venture","10","1.Title 2.Problem/Opportunity 3.Value Proposition 4.Underlying Magic 5.Business Model 6.Go-to-Market 7.Competition 8.Team 9.Projections 10.Status/Timeline/Ask",Pitch to investors in 20 min,VCs angel investors,Confident not arrogant,Hook→Magic→Proof→Ask,5yr projections milestones,Guy Kawasaki Blog,"curiosity→frustration→hope→confidence→trust→urgency","hook|what-is|what-could-be|what-could-be|proof|proof|evaluation|trust|proof|action"
3,Series A Deck,"series a, growth, scale, investor, traction","12-15","1.Title 2.Mission 3.Problem 4.Solution 5.Traction/Metrics 6.Product Demo 7.Market Size 8.Business Model 9.Competition 10.Team 11.Go-to-Market 12.Financials 13.Use of Funds 14.Ask",Raise Series A funding,Growth-stage VCs,Data-driven confident,Traction→Scale→Vision,Revenue growth LTV CAC cohorts,YC Library,"curiosity→hope→frustration→relief→confidence→trust→urgency","hook|what-could-be|what-is|what-could-be|proof|proof|proof|proof|evaluation|trust|proof|proof|what-could-be|action"
4,Product Demo,"demo, product, walkthrough, features, saas","5-8","1.Hook/Problem 2.Solution Overview 3.Live Demo/Screenshots 4.Key Features 5.Benefits 6.Pricing 7.CTA",Demonstrate product value,Prospects users,Enthusiastic helpful,Problem→See it work→Value,Conversion engagement time-saved,Product-led growth best practices,"curiosity→frustration→hope→confidence→urgency","hook|what-is|what-could-be|what-could-be|what-could-be|evaluation|action"
5,Sales Pitch,"sales, pitch, prospect, close, deal","7-10","1.Personalized Hook 2.Their Problem 3.Cost of Inaction 4.Your Solution 5.Proof/Case Studies 6.Differentiators 7.Pricing/ROI 8.Objection Handling 9.CTA 10.Next Steps",Close deal win customer,Qualified prospects,Consultative trustworthy,Pain→Agitate→Solve→Prove,ROI case study metrics,Sandler Sales Training,"connection→frustration→fear→hope→trust→confidence→urgency","hook|what-is|what-is|what-could-be|proof|what-could-be|evaluation|trust|action|action"
6,Nancy Duarte Sparkline,"duarte, sparkline, story, transformation, resonate","Varies","Alternate: What Is→What Could Be→What Is→What Could Be→New Bliss",Transform audience perspective,Any audience needing persuasion,Inspiring visionary,Tension→Release→Tension→Release→Resolution,Audience transformation,Nancy Duarte Resonate,"frustration→hope→frustration→hope→relief","what-is|what-could-be|what-is|what-could-be|new-bliss"
7,Problem-Solution-Benefit,"psb, simple, clear, benefit, value","3-5","1.Problem Statement 2.Solution Introduction 3.Key Benefits 4.Proof 5.CTA",Quick persuasion simple message,Time-pressed audience,Direct clear,Problem→Solution→Outcome,Core value metrics,Marketing fundamentals,"frustration→hope→confidence→urgency","what-is|what-could-be|what-could-be|proof|action"
8,Quarterly Business Review,"qbr, business review, internal, stakeholder","10-15","1.Executive Summary 2.Goals vs Results 3.Key Metrics 4.Wins 5.Challenges 6.Learnings 7.Customer Insights 8.Competitive Update 9.Next Quarter Goals 10.Resource Needs",Update stakeholders on progress,Internal leadership,Professional factual,Review→Analyze→Plan,KPIs OKRs progress %,Internal communications,"clarity→trust→confidence→evaluation→hope","summary|proof|proof|celebration|what-is|insight|trust|evaluation|what-could-be|action"
9,Team All-Hands,"all-hands, company, internal, culture, update","8-12","1.Opening/Energy 2.Company Wins 3.Metrics Dashboard 4.Team Spotlights 5.Product Updates 6.Customer Stories 7.Challenges/Learnings 8.Roadmap Preview 9.Q&A 10.Closing Motivation",Align and motivate team,All employees,Transparent inspiring,Celebrate→Update→Align→Energize,Company-wide KPIs,Internal communications,"warmth→confidence→trust→connection→hope→urgency","hook|celebration|proof|connection|what-could-be|trust|what-is|what-could-be|interaction|action"
10,Conference Talk,"conference, talk, keynote, public speaking, thought leadership","15-25","1.Hook/Story 2.Credibility 3.Big Idea 4.Point 1 + Evidence 5.Point 2 + Evidence 6.Point 3 + Evidence 7.Synthesis 8.Call to Action 9.Q&A Prep",Establish thought leadership,Conference attendees,Expert engaging,Story→Teach→Inspire,Audience engagement social shares,TED Talk guidelines,"curiosity→trust→hope→confidence→confidence→confidence→clarity→urgency","hook|trust|what-could-be|proof|proof|proof|synthesis|action|interaction"
11,Workshop Training,"workshop, training, education, how-to, tutorial","20-40","1.Welcome/Objectives 2.Agenda 3.Concept 1 4.Exercise 1 5.Concept 2 6.Exercise 2 7.Concept 3 8.Exercise 3 9.Synthesis 10.Resources 11.Q&A",Teach practical skills,Learners trainees,Patient instructive,Learn→Practice→Apply→Reflect,Skill acquisition completion,Adult learning principles,"warmth→clarity→confidence→confidence→confidence→confidence→clarity→hope","welcome|structure|teaching|practice|teaching|practice|teaching|practice|synthesis|resources|interaction"
12,Case Study Presentation,"case study, success story, customer, results","8-12","1.Customer Introduction 2.Their Challenge 3.Why They Chose Us 4.Implementation 5.Solution Details 6.Results/Metrics 7.Customer Quote 8.Lessons Learned 9.Applicability 10.CTA",Prove value through example,Prospects similar to case,Authentic factual,Challenge→Journey→Transformation,Before/after metrics ROI,Marketing case study best practices,"connection→frustration→trust→hope→confidence→celebration→trust→clarity→urgency","connection|what-is|trust|what-could-be|what-could-be|proof|trust|insight|what-could-be|action"
13,Competitive Analysis,"competitive, analysis, comparison, market","6-10","1.Market Landscape 2.Competitor Overview 3.Feature Comparison Matrix 4.Pricing Comparison 5.Strengths/Weaknesses 6.Our Differentiation 7.Market Positioning 8.Strategic Recommendations",Inform strategic decisions,Internal leadership,Analytical objective,Landscape→Analysis→Strategy,Market share feature gaps,Competitive intelligence,"clarity→evaluation→evaluation→evaluation→clarity→hope→confidence→urgency","overview|evaluation|comparison|comparison|analysis|what-could-be|proof|action"
14,Board Meeting Deck,"board, governance, investor update, quarterly","15-20","1.Agenda 2.Executive Summary 3.Financial Overview 4.Key Metrics 5.Product Update 6.Sales/Marketing 7.Operations 8.Team/Hiring 9.Risks/Challenges 10.Strategic Initiatives 11.Upcoming Milestones 12.Ask/Discussion",Update board on company status,Board members,Professional detailed,Report→Analyze→Discuss→Decide,All key business metrics,Board governance best practices,"clarity→confidence→trust→trust→confidence→confidence→trust→connection→evaluation→hope→confidence→urgency","structure|summary|proof|proof|proof|proof|proof|trust|what-is|what-could-be|proof|action"
15,Webinar Presentation,"webinar, online, education, lead gen","20-30","1.Welcome/Housekeeping 2.Presenter Intro 3.Agenda 4.Hook/Problem 5.Teaching Content 6.Case Study 7.Product Introduction 8.Demo 9.Offer/CTA 10.Q&A 11.Resources",Generate leads educate prospects,Webinar registrants,Educational helpful,Teach→Demonstrate→Offer,Registrations attendance conversion,Webinar marketing best practices,"warmth→trust→clarity→curiosity→confidence→trust→hope→confidence→urgency→connection→clarity","welcome|trust|structure|hook|teaching|trust|what-could-be|proof|action|interaction|resources"
````



---

## `data/slide-typography.csv`

````csv
content_type,primary_size,secondary_size,accent_size,weight_contrast,letter_spacing,line_height
hero-statement,120px,32px,14px,700-400,tight,1.0
metric-callout,96px,18px,12px,700-500,normal,1.1
feature-grid,28px,16px,12px,600-400,normal,1.4
quote-block,36px,18px,14px,400-italic,loose,1.5
data-insight,48px,20px,14px,700-400,normal,1.2
cta-action,64px,24px,16px,700-500,tight,1.1
title-only,80px,24px,14px,700-400,tight,1.0
subtitle-heavy,56px,28px,16px,600-400,normal,1.2
body-focus,24px,18px,14px,500-400,normal,1.6
comparison,32px,16px,12px,600-400,normal,1.3
timeline,28px,16px,12px,500-400,normal,1.4
pricing,48px,20px,14px,700-500,normal,1.2
team,24px,16px,14px,600-400,normal,1.4
testimonial,32px,20px,14px,400-italic,loose,1.5
````



---

## `references/component-specs.md`

# Component Specifications

Detailed specs for core components with states and variants.

## Button

### Variants

| Variant | Background | Text | Border | Use Case |
|---------|------------|------|--------|----------|
| default | primary | white | none | Primary actions |
| secondary | gray-100 | gray-900 | none | Secondary actions |
| outline | transparent | foreground | border | Tertiary actions |
| ghost | transparent | foreground | none | Subtle actions |
| link | transparent | primary | none | Navigation |
| destructive | red-600 | white | none | Dangerous actions |

### Sizes

| Size | Height | Padding X | Padding Y | Font Size | Icon Size |
|------|--------|-----------|-----------|-----------|-----------|
| sm | 32px | 12px | 6px | 14px | 16px |
| default | 40px | 16px | 8px | 14px | 18px |
| lg | 48px | 24px | 12px | 16px | 20px |
| icon | 40px | 0 | 0 | - | 18px |

### States

| State | Background | Text | Opacity | Cursor |
|-------|------------|------|---------|--------|
| default | token | token | 1 | pointer |
| hover | darker | token | 1 | pointer |
| active | darkest | token | 1 | pointer |
| focus | token | token | 1 | pointer |
| disabled | muted | muted-fg | 0.5 | not-allowed |
| loading | token | token | 0.7 | wait |

### Anatomy

```
┌─────────────────────────────────────┐
│  [icon]  Label Text  [icon]         │
└─────────────────────────────────────┘
     ↑                      ↑
  leading icon         trailing icon
```

---

## Input

### Variants

| Variant | Description |
|---------|-------------|
| default | Standard text input |
| textarea | Multi-line text |
| select | Dropdown selection |
| checkbox | Boolean toggle |
| radio | Single selection |
| switch | Toggle switch |

### Sizes

| Size | Height | Padding | Font Size |
|------|--------|---------|-----------|
| sm | 32px | 8px 12px | 14px |
| default | 40px | 8px 12px | 14px |
| lg | 48px | 12px 16px | 16px |

### States

| State | Border | Background | Ring |
|-------|--------|------------|------|
| default | gray-300 | white | none |
| hover | gray-400 | white | none |
| focus | primary | white | primary/20% |
| error | red-500 | white | red/20% |
| disabled | gray-200 | gray-100 | none |

### Anatomy

```
Label (optional)
┌─────────────────────────────────────┐
│ [icon] Placeholder/Value   [action] │
└─────────────────────────────────────┘
Helper text or error message
```

---

## Card

### Variants

| Variant | Shadow | Border | Use Case |
|---------|--------|--------|----------|
| default | sm | 1px | Standard card |
| elevated | lg | none | Prominent content |
| outline | none | 1px | Subtle container |
| interactive | sm→md | 1px | Clickable card |

### Anatomy

```
┌─────────────────────────────────────┐
│ Card Header                         │
│   Title                             │
│   Description                       │
├─────────────────────────────────────┤
│ Card Content                        │
│   Main content area                 │
│                                     │
├─────────────────────────────────────┤
│ Card Footer                         │
│   Actions                           │
└─────────────────────────────────────┘
```

### Spacing

| Area | Padding |
|------|---------|
| header | 24px 24px 0 |
| content | 24px |
| footer | 0 24px 24px |
| gap | 16px |

---

## Badge

### Variants

| Variant | Background | Text |
|---------|------------|------|
| default | primary | white |
| secondary | gray-100 | gray-900 |
| outline | transparent | foreground |
| destructive | red-600 | white |
| success | green-600 | white |
| warning | yellow-500 | gray-900 |

### Sizes

| Size | Padding | Font Size | Height |
|------|---------|-----------|--------|
| sm | 4px 8px | 11px | 20px |
| default | 4px 10px | 12px | 24px |
| lg | 6px 12px | 14px | 28px |

---

## Alert

### Variants

| Variant | Icon | Background | Border |
|---------|------|------------|--------|
| default | info | gray-50 | gray-200 |
| destructive | alert | red-50 | red-200 |
| success | check | green-50 | green-200 |
| warning | warning | yellow-50 | yellow-200 |

### Anatomy

```
┌─────────────────────────────────────┐
│ [icon]  Title                    [×]│
│         Description text            │
└─────────────────────────────────────┘
```

---

## Dialog

### Sizes

| Size | Max Width | Use Case |
|------|-----------|----------|
| sm | 384px | Simple confirmations |
| default | 512px | Standard dialogs |
| lg | 640px | Complex forms |
| xl | 768px | Data-heavy dialogs |
| full | 100% - 32px | Full-screen on mobile |

### Anatomy

```
┌───────────────────────────────────────┐
│ Dialog Header                      [×]│
│   Title                               │
│   Description                         │
├───────────────────────────────────────┤
│ Dialog Content                        │
│   Scrollable if needed                │
│                                       │
├───────────────────────────────────────┤
│ Dialog Footer                         │
│                     [Cancel] [Confirm]│
└───────────────────────────────────────┘
```

---

## Table

### Row States

| State | Background | Use Case |
|-------|------------|----------|
| default | white | Normal row |
| hover | gray-50 | Mouse over |
| selected | primary/10% | Selected row |
| striped | gray-50/white | Alternating |

### Cell Alignment

| Content Type | Alignment |
|--------------|-----------|
| Text | Left |
| Numbers | Right |
| Status/Badge | Center |
| Actions | Right |

### Spacing

| Element | Value |
|---------|-------|
| cell padding | 12px 16px |
| header padding | 12px 16px |
| row height (compact) | 40px |
| row height (default) | 48px |
| row height (comfortable) | 56px |



---

## `references/component-tokens.md`

# Component Tokens

Component-specific tokens referencing semantic layer.

## Button Tokens

```css
:root {
  /* Default (Primary) */
  --button-bg: var(--color-primary);
  --button-fg: var(--color-primary-foreground);
  --button-hover-bg: var(--color-primary-hover);
  --button-active-bg: var(--color-primary-active);

  /* Secondary */
  --button-secondary-bg: var(--color-secondary);
  --button-secondary-fg: var(--color-secondary-foreground);
  --button-secondary-hover-bg: var(--color-secondary-hover);

  /* Outline */
  --button-outline-border: var(--color-border);
  --button-outline-fg: var(--color-foreground);
  --button-outline-hover-bg: var(--color-accent);

  /* Ghost */
  --button-ghost-fg: var(--color-foreground);
  --button-ghost-hover-bg: var(--color-accent);

  /* Destructive */
  --button-destructive-bg: var(--color-destructive);
  --button-destructive-fg: var(--color-destructive-foreground);
  --button-destructive-hover-bg: var(--color-destructive-hover);

  /* Sizing */
  --button-padding-x: var(--space-4);
  --button-padding-y: var(--space-2);
  --button-padding-x-sm: var(--space-3);
  --button-padding-y-sm: var(--space-1-5);
  --button-padding-x-lg: var(--space-6);
  --button-padding-y-lg: var(--space-3);

  /* Shape */
  --button-radius: var(--radius-md);
  --button-font-size: var(--font-size-sm);
  --button-font-weight: var(--font-weight-medium);
}
```

## Input Tokens

```css
:root {
  /* Background & Border */
  --input-bg: var(--color-background);
  --input-border: var(--color-input);
  --input-fg: var(--color-foreground);

  /* Placeholder */
  --input-placeholder: var(--color-muted-foreground);

  /* Focus */
  --input-focus-border: var(--color-ring);
  --input-focus-ring: var(--color-ring);

  /* Error */
  --input-error-border: var(--color-error);
  --input-error-fg: var(--color-error);

  /* Disabled */
  --input-disabled-bg: var(--color-muted);
  --input-disabled-fg: var(--color-muted-foreground);

  /* Sizing */
  --input-padding-x: var(--space-3);
  --input-padding-y: var(--space-2);
  --input-radius: var(--radius-md);
  --input-font-size: var(--font-size-sm);
}
```

## Card Tokens

```css
:root {
  /* Background & Border */
  --card-bg: var(--color-card);
  --card-fg: var(--color-card-foreground);
  --card-border: var(--color-border);

  /* Shadow */
  --card-shadow: var(--shadow-default);
  --card-shadow-hover: var(--shadow-md);

  /* Spacing */
  --card-padding: var(--space-6);
  --card-padding-sm: var(--space-4);
  --card-gap: var(--space-4);

  /* Shape */
  --card-radius: var(--radius-lg);
}
```

## Badge Tokens

```css
:root {
  /* Default */
  --badge-bg: var(--color-primary);
  --badge-fg: var(--color-primary-foreground);

  /* Secondary */
  --badge-secondary-bg: var(--color-secondary);
  --badge-secondary-fg: var(--color-secondary-foreground);

  /* Outline */
  --badge-outline-border: var(--color-border);
  --badge-outline-fg: var(--color-foreground);

  /* Destructive */
  --badge-destructive-bg: var(--color-destructive);
  --badge-destructive-fg: var(--color-destructive-foreground);

  /* Sizing */
  --badge-padding-x: var(--space-2-5);
  --badge-padding-y: var(--space-0-5);
  --badge-radius: var(--radius-full);
  --badge-font-size: var(--font-size-xs);
}
```

## Alert Tokens

```css
:root {
  /* Default */
  --alert-bg: var(--color-background);
  --alert-fg: var(--color-foreground);
  --alert-border: var(--color-border);

  /* Destructive */
  --alert-destructive-bg: var(--color-destructive);
  --alert-destructive-fg: var(--color-destructive-foreground);

  /* Spacing */
  --alert-padding: var(--space-4);
  --alert-radius: var(--radius-lg);
}
```

## Dialog/Modal Tokens

```css
:root {
  /* Overlay */
  --dialog-overlay-bg: rgb(0 0 0 / 0.5);

  /* Content */
  --dialog-bg: var(--color-background);
  --dialog-fg: var(--color-foreground);
  --dialog-border: var(--color-border);
  --dialog-shadow: var(--shadow-lg);

  /* Spacing */
  --dialog-padding: var(--space-6);
  --dialog-radius: var(--radius-lg);
  --dialog-max-width: 32rem;
}
```

## Table Tokens

```css
:root {
  /* Header */
  --table-header-bg: var(--color-muted);
  --table-header-fg: var(--color-muted-foreground);

  /* Body */
  --table-row-bg: var(--color-background);
  --table-row-hover-bg: var(--color-muted);
  --table-row-fg: var(--color-foreground);

  /* Border */
  --table-border: var(--color-border);

  /* Spacing */
  --table-cell-padding-x: var(--space-4);
  --table-cell-padding-y: var(--space-3);
}
```

## Usage Example

```css
.button {
  background: var(--button-bg);
  color: var(--button-fg);
  padding: var(--button-padding-y) var(--button-padding-x);
  border-radius: var(--button-radius);
  font-size: var(--button-font-size);
  font-weight: var(--button-font-weight);
  transition: background var(--duration-fast);
}

.button:hover {
  background: var(--button-hover-bg);
}

.button.secondary {
  background: var(--button-secondary-bg);
  color: var(--button-secondary-fg);
}
```



---

## `references/primitive-tokens.md`

# Primitive Tokens

Raw design values - foundation of the design system.

## Color Scales

### Gray Scale

```css
:root {
  --color-gray-50:  #F9FAFB;
  --color-gray-100: #F3F4F6;
  --color-gray-200: #E5E7EB;
  --color-gray-300: #D1D5DB;
  --color-gray-400: #9CA3AF;
  --color-gray-500: #6B7280;
  --color-gray-600: #4B5563;
  --color-gray-700: #374151;
  --color-gray-800: #1F2937;
  --color-gray-900: #111827;
  --color-gray-950: #030712;
}
```

### Primary Colors (Blue)

```css
:root {
  --color-blue-50:  #EFF6FF;
  --color-blue-100: #DBEAFE;
  --color-blue-200: #BFDBFE;
  --color-blue-300: #93C5FD;
  --color-blue-400: #60A5FA;
  --color-blue-500: #3B82F6;
  --color-blue-600: #2563EB;
  --color-blue-700: #1D4ED8;
  --color-blue-800: #1E40AF;
  --color-blue-900: #1E3A8A;
}
```

### Status Colors

```css
:root {
  /* Success - Green */
  --color-green-500: #22C55E;
  --color-green-600: #16A34A;

  /* Warning - Yellow */
  --color-yellow-500: #EAB308;
  --color-yellow-600: #CA8A04;

  /* Error - Red */
  --color-red-500: #EF4444;
  --color-red-600: #DC2626;

  /* Info - Blue */
  --color-info: var(--color-blue-500);
}
```

## Spacing Scale

4px base unit system.

```css
:root {
  --space-0:   0;
  --space-px:  1px;
  --space-0-5: 0.125rem;  /* 2px */
  --space-1:   0.25rem;   /* 4px */
  --space-1-5: 0.375rem;  /* 6px */
  --space-2:   0.5rem;    /* 8px */
  --space-2-5: 0.625rem;  /* 10px */
  --space-3:   0.75rem;   /* 12px */
  --space-3-5: 0.875rem;  /* 14px */
  --space-4:   1rem;      /* 16px */
  --space-5:   1.25rem;   /* 20px */
  --space-6:   1.5rem;    /* 24px */
  --space-7:   1.75rem;   /* 28px */
  --space-8:   2rem;      /* 32px */
  --space-9:   2.25rem;   /* 36px */
  --space-10:  2.5rem;    /* 40px */
  --space-12:  3rem;      /* 48px */
  --space-14:  3.5rem;    /* 56px */
  --space-16:  4rem;      /* 64px */
  --space-20:  5rem;      /* 80px */
  --space-24:  6rem;      /* 96px */
}
```

## Typography Scale

```css
:root {
  /* Font Sizes */
  --font-size-xs:   0.75rem;   /* 12px */
  --font-size-sm:   0.875rem;  /* 14px */
  --font-size-base: 1rem;      /* 16px */
  --font-size-lg:   1.125rem;  /* 18px */
  --font-size-xl:   1.25rem;   /* 20px */
  --font-size-2xl:  1.5rem;    /* 24px */
  --font-size-3xl:  1.875rem;  /* 30px */
  --font-size-4xl:  2.25rem;   /* 36px */
  --font-size-5xl:  3rem;      /* 48px */

  /* Line Heights */
  --leading-none:   1;
  --leading-tight:  1.25;
  --leading-snug:   1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose:  2;

  /* Font Weights */
  --font-weight-normal:   400;
  --font-weight-medium:   500;
  --font-weight-semibold: 600;
  --font-weight-bold:     700;

  /* Letter Spacing */
  --tracking-tighter: -0.05em;
  --tracking-tight:   -0.025em;
  --tracking-normal:  0;
  --tracking-wide:    0.025em;
  --tracking-wider:   0.05em;
}
```

## Border Radius

```css
:root {
  --radius-none:    0;
  --radius-sm:      0.125rem;  /* 2px */
  --radius-default: 0.25rem;   /* 4px */
  --radius-md:      0.375rem;  /* 6px */
  --radius-lg:      0.5rem;    /* 8px */
  --radius-xl:      0.75rem;   /* 12px */
  --radius-2xl:     1rem;      /* 16px */
  --radius-3xl:     1.5rem;    /* 24px */
  --radius-full:    9999px;
}
```

## Shadows

```css
:root {
  --shadow-none: none;
  --shadow-sm:   0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-default: 0 1px 3px 0 rgb(0 0 0 / 0.1),
                    0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md:   0 4px 6px -1px rgb(0 0 0 / 0.1),
                 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg:   0 10px 15px -3px rgb(0 0 0 / 0.1),
                 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl:   0 20px 25px -5px rgb(0 0 0 / 0.1),
                 0 8px 10px -6px rgb(0 0 0 / 0.1);
  --shadow-2xl:  0 25px 50px -12px rgb(0 0 0 / 0.25);
  --shadow-inner: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);
}
```

## Motion / Duration

```css
:root {
  --duration-75:  75ms;
  --duration-100: 100ms;
  --duration-150: 150ms;
  --duration-200: 200ms;
  --duration-300: 300ms;
  --duration-500: 500ms;
  --duration-700: 700ms;
  --duration-1000: 1000ms;

  /* Semantic durations */
  --duration-fast:   var(--duration-150);
  --duration-normal: var(--duration-200);
  --duration-slow:   var(--duration-300);
}
```

## Z-Index Scale

```css
:root {
  --z-auto:     auto;
  --z-0:        0;
  --z-10:       10;
  --z-20:       20;
  --z-30:       30;
  --z-40:       40;
  --z-50:       50;
  --z-dropdown: 1000;
  --z-sticky:   1100;
  --z-modal:    1200;
  --z-popover:  1300;
  --z-tooltip:  1400;
}
```



---

## `references/semantic-tokens.md`

# Semantic Tokens

Purpose-based aliases referencing primitive tokens.

## Color Semantics

### Background & Foreground

```css
:root {
  /* Page background */
  --color-background: var(--color-gray-50);
  --color-foreground: var(--color-gray-900);

  /* Card/surface background */
  --color-card: white;
  --color-card-foreground: var(--color-gray-900);

  /* Popover/dropdown */
  --color-popover: white;
  --color-popover-foreground: var(--color-gray-900);
}
```

### Primary

```css
:root {
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-700);
  --color-primary-active: var(--color-blue-800);
  --color-primary-foreground: white;
}
```

### Secondary

```css
:root {
  --color-secondary: var(--color-gray-100);
  --color-secondary-hover: var(--color-gray-200);
  --color-secondary-foreground: var(--color-gray-900);
}
```

### Muted

```css
:root {
  --color-muted: var(--color-gray-100);
  --color-muted-foreground: var(--color-gray-500);
}
```

### Accent

```css
:root {
  --color-accent: var(--color-gray-100);
  --color-accent-foreground: var(--color-gray-900);
}
```

### Destructive

```css
:root {
  --color-destructive: var(--color-red-600);
  --color-destructive-hover: var(--color-red-700);
  --color-destructive-foreground: white;
}
```

### Status Colors

```css
:root {
  --color-success: var(--color-green-600);
  --color-success-foreground: white;

  --color-warning: var(--color-yellow-500);
  --color-warning-foreground: var(--color-gray-900);

  --color-error: var(--color-red-600);
  --color-error-foreground: white;

  --color-info: var(--color-blue-500);
  --color-info-foreground: white;
}
```

### Border & Ring

```css
:root {
  --color-border: var(--color-gray-200);
  --color-input: var(--color-gray-200);
  --color-ring: var(--color-blue-500);
}
```

## Spacing Semantics

```css
:root {
  /* Component internal spacing */
  --spacing-component-xs: var(--space-1);
  --spacing-component-sm: var(--space-2);
  --spacing-component: var(--space-3);
  --spacing-component-lg: var(--space-4);

  /* Section spacing */
  --spacing-section-sm: var(--space-8);
  --spacing-section: var(--space-12);
  --spacing-section-lg: var(--space-16);

  /* Page margins */
  --spacing-page-x: var(--space-4);
  --spacing-page-y: var(--space-6);
}
```

## Typography Semantics

```css
:root {
  /* Headings */
  --font-heading: var(--font-size-2xl);
  --font-heading-lg: var(--font-size-3xl);
  --font-heading-xl: var(--font-size-4xl);

  /* Body */
  --font-body: var(--font-size-base);
  --font-body-sm: var(--font-size-sm);
  --font-body-lg: var(--font-size-lg);

  /* Labels & Captions */
  --font-label: var(--font-size-sm);
  --font-caption: var(--font-size-xs);
}
```

## Interactive States

```css
:root {
  /* Focus ring */
  --ring-width: 2px;
  --ring-offset: 2px;
  --ring-color: var(--color-ring);

  /* Opacity for disabled */
  --opacity-disabled: 0.5;

  /* Transitions */
  --transition-colors: color, background-color, border-color;
  --transition-transform: transform;
  --transition-all: all;
}
```

## Dark Mode Overrides

```css
.dark {
  --color-background: var(--color-gray-950);
  --color-foreground: var(--color-gray-50);

  --color-card: var(--color-gray-900);
  --color-card-foreground: var(--color-gray-50);

  --color-popover: var(--color-gray-900);
  --color-popover-foreground: var(--color-gray-50);

  --color-muted: var(--color-gray-800);
  --color-muted-foreground: var(--color-gray-400);

  --color-secondary: var(--color-gray-800);
  --color-secondary-foreground: var(--color-gray-50);

  --color-accent: var(--color-gray-800);
  --color-accent-foreground: var(--color-gray-50);

  --color-border: var(--color-gray-800);
  --color-input: var(--color-gray-800);
}
```

## Usage Patterns

### Applying Semantic Tokens

```css
/* Good - uses semantic tokens */
.card {
  background: var(--color-card);
  color: var(--color-card-foreground);
  border: 1px solid var(--color-border);
}

/* Bad - uses primitive tokens directly */
.card {
  background: var(--color-gray-50);
  color: var(--color-gray-900);
}
```

### Theme Switching

Semantic tokens enable instant theme switching:

```js
// Toggle dark mode
document.documentElement.classList.toggle('dark');
```



---

## `references/states-and-variants.md`

# States and Variants

Component state definitions and variant patterns.

## Interactive States

### State Definitions

| State | Trigger | Visual Change |
|-------|---------|---------------|
| default | None | Base appearance |
| hover | Mouse over | Slight color shift |
| focus | Tab/click | Focus ring |
| active | Mouse down | Darkest color |
| disabled | disabled attr | Reduced opacity |
| loading | Async action | Spinner + opacity |

### State Priority

When multiple states apply, priority (highest to lowest):

1. disabled
2. loading
3. active
4. focus
5. hover
6. default

### State Transitions

```css
/* Standard transition for interactive elements */
.interactive {
  transition-property: color, background-color, border-color, box-shadow;
  transition-duration: var(--duration-fast);
  transition-timing-function: ease-in-out;
}
```

| Transition | Duration | Easing |
|------------|----------|--------|
| Color changes | 150ms | ease-in-out |
| Background | 150ms | ease-in-out |
| Transform | 200ms | ease-out |
| Opacity | 150ms | ease |
| Shadow | 200ms | ease-out |

## Focus States

### Focus Ring Spec

```css
/* Standard focus ring */
.focusable:focus-visible {
  outline: none;
  box-shadow: 0 0 0 var(--ring-offset) var(--color-background),
              0 0 0 calc(var(--ring-offset) + var(--ring-width)) var(--ring-color);
}
```

| Property | Value |
|----------|-------|
| Ring width | 2px |
| Ring offset | 2px |
| Ring color | primary (blue-500) |
| Offset color | background |

### Focus Within

```css
/* Container focus when child is focused */
.container:focus-within {
  border-color: var(--color-ring);
}
```

## Disabled States

### Visual Treatment

```css
.disabled {
  opacity: var(--opacity-disabled); /* 0.5 */
  pointer-events: none;
  cursor: not-allowed;
}
```

| Property | Disabled Value |
|----------|----------------|
| Opacity | 50% |
| Pointer events | none |
| Cursor | not-allowed |
| Background | muted |
| Color | muted-foreground |

### Accessibility

- Use `aria-disabled="true"` for semantic disabled
- Use `disabled` attribute for form elements
- Maintain sufficient contrast (3:1 minimum)

## Loading States

### Spinner Placement

| Component | Spinner Position |
|-----------|------------------|
| Button | Replace icon or center |
| Input | Trailing position |
| Card | Center overlay |
| Page | Center of viewport |

### Loading Treatment

```css
.loading {
  position: relative;
  pointer-events: none;
}

.loading::after {
  content: '';
  /* spinner styles */
}

.loading > * {
  opacity: 0.7;
}
```

## Error States

### Visual Indicators

```css
.error {
  border-color: var(--color-error);
  color: var(--color-error);
}

.error:focus-visible {
  box-shadow: 0 0 0 2px var(--color-background),
              0 0 0 4px var(--color-error);
}
```

| Element | Error Treatment |
|---------|-----------------|
| Input border | red-500 |
| Input focus ring | red/20% |
| Helper text | red-600 |
| Icon | red-500 |

### Error Messages

- Position below input
- Use error color
- Include icon for accessibility
- Clear on valid input

## Variant Patterns

### Color Variants

```css
/* Pattern for color variants */
.component {
  --component-bg: var(--color-primary);
  --component-fg: var(--color-primary-foreground);
  background: var(--component-bg);
  color: var(--component-fg);
}

.component.secondary {
  --component-bg: var(--color-secondary);
  --component-fg: var(--color-secondary-foreground);
}

.component.destructive {
  --component-bg: var(--color-destructive);
  --component-fg: var(--color-destructive-foreground);
}
```

### Size Variants

```css
/* Pattern for size variants */
.component {
  --component-height: 40px;
  --component-padding: var(--space-4);
  --component-font: var(--font-size-sm);
}

.component.sm {
  --component-height: 32px;
  --component-padding: var(--space-3);
  --component-font: var(--font-size-xs);
}

.component.lg {
  --component-height: 48px;
  --component-padding: var(--space-6);
  --component-font: var(--font-size-base);
}
```

## Accessibility Requirements

### Color Contrast

| Element | Minimum Ratio |
|---------|---------------|
| Normal text | 4.5:1 |
| Large text (18px+) | 3:1 |
| UI components | 3:1 |
| Focus indicator | 3:1 |

### State Indicators

- Never rely on color alone
- Use icons, text, or patterns
- Ensure focus is visible
- Provide loading announcements

### ARIA States

```html
<!-- Disabled -->
<button disabled aria-disabled="true">Submit</button>

<!-- Loading -->
<button aria-busy="true" aria-describedby="loading-text">
  <span id="loading-text" class="sr-only">Loading...</span>
</button>

<!-- Error -->
<input aria-invalid="true" aria-describedby="error-msg">
<span id="error-msg" role="alert">Error message</span>
```



---

## `references/tailwind-integration.md`

# Tailwind Integration

Map design system tokens to Tailwind CSS configuration.

## CSS Variables Setup

### Base Layer

```css
/* globals.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    /* Primitives */
    --color-blue-600: 37 99 235;  /* HSL: 217 91% 60% */

    /* Semantic */
    --background: 0 0% 100%;
    --foreground: 222 47% 11%;
    --primary: 217 91% 60%;
    --primary-foreground: 0 0% 100%;
    --secondary: 220 14% 96%;
    --secondary-foreground: 222 47% 11%;
    --muted: 220 14% 96%;
    --muted-foreground: 220 9% 46%;
    --accent: 220 14% 96%;
    --accent-foreground: 222 47% 11%;
    --destructive: 0 84% 60%;
    --destructive-foreground: 0 0% 100%;
    --border: 220 13% 91%;
    --input: 220 13% 91%;
    --ring: 217 91% 60%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222 47% 4%;
    --foreground: 210 40% 98%;
    --primary: 217 91% 60%;
    --primary-foreground: 0 0% 100%;
    --secondary: 217 33% 17%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217 33% 17%;
    --muted-foreground: 215 20% 65%;
    --accent: 217 33% 17%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62% 30%;
    --destructive-foreground: 0 0% 100%;
    --border: 217 33% 17%;
    --input: 217 33% 17%;
    --ring: 217 91% 60%;
  }
}
```

## Tailwind Config

### tailwind.config.ts

```typescript
import type { Config } from 'tailwindcss'

const config: Config = {
  darkMode: ['class'],
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
    },
  },
  plugins: [],
}

export default config
```

## HSL Format Benefits

Using HSL without function allows opacity modifiers:

```tsx
// With HSL format (space-separated)
<div className="bg-primary/50">   // 50% opacity
<div className="text-primary/80"> // 80% opacity

// CSS output
background-color: hsl(217 91% 60% / 0.5);
```

## Component Classes

### Button Example

```css
@layer components {
  .btn {
    @apply inline-flex items-center justify-center
           rounded-md font-medium
           transition-colors
           focus-visible:outline-none focus-visible:ring-2
           focus-visible:ring-ring focus-visible:ring-offset-2
           disabled:pointer-events-none disabled:opacity-50;
  }

  .btn-default {
    @apply bg-primary text-primary-foreground
           hover:bg-primary/90;
  }

  .btn-secondary {
    @apply bg-secondary text-secondary-foreground
           hover:bg-secondary/80;
  }

  .btn-outline {
    @apply border border-input bg-background
           hover:bg-accent hover:text-accent-foreground;
  }

  .btn-ghost {
    @apply hover:bg-accent hover:text-accent-foreground;
  }

  .btn-destructive {
    @apply bg-destructive text-destructive-foreground
           hover:bg-destructive/90;
  }

  /* Sizes */
  .btn-sm { @apply h-8 px-3 text-xs; }
  .btn-md { @apply h-10 px-4 text-sm; }
  .btn-lg { @apply h-12 px-6 text-base; }
}
```

## Spacing Integration

```typescript
// tailwind.config.ts
theme: {
  extend: {
    spacing: {
      // Map to CSS variables if needed
      'section': 'var(--spacing-section)',
      'component': 'var(--spacing-component)',
    }
  }
}
```

## Animation Tokens

```typescript
// tailwind.config.ts
theme: {
  extend: {
    transitionDuration: {
      fast: '150ms',
      normal: '200ms',
      slow: '300ms',
    },
    keyframes: {
      'accordion-down': {
        from: { height: '0' },
        to: { height: 'var(--radix-accordion-content-height)' },
      },
      'accordion-up': {
        from: { height: 'var(--radix-accordion-content-height)' },
        to: { height: '0' },
      },
    },
    animation: {
      'accordion-down': 'accordion-down 0.2s ease-out',
      'accordion-up': 'accordion-up 0.2s ease-out',
    },
  }
}
```

## Dark Mode Toggle

```typescript
// Toggle dark mode
function toggleDarkMode() {
  document.documentElement.classList.toggle('dark')
}

// System preference
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.classList.add('dark')
}
```

## shadcn/ui Alignment

This configuration aligns with shadcn/ui conventions:

- Same CSS variable naming
- Same HSL format
- Same color scale structure
- Compatible with `npx shadcn@latest add` commands

### Using with shadcn/ui

```bash
# Initialize (uses same token structure)
npx shadcn@latest init

# Add components (styled with these tokens)
npx shadcn@latest add button card input
```

Components will automatically use your design system tokens.



---

## `references/token-architecture.md`

# Token Architecture

Three-layer token system for scalable, themeable design systems.

## Layer Overview

```
┌─────────────────────────────────────────┐
│  Component Tokens                       │  Per-component overrides
│  --button-bg, --card-padding            │
├─────────────────────────────────────────┤
│  Semantic Tokens                        │  Purpose-based aliases
│  --color-primary, --spacing-section     │
├─────────────────────────────────────────┤
│  Primitive Tokens                       │  Raw design values
│  --color-blue-600, --space-4            │
└─────────────────────────────────────────┘
```

## Why Three Layers?

| Layer | Purpose | When to Change |
|-------|---------|----------------|
| Primitive | Base values (colors, sizes) | Rarely - foundational |
| Semantic | Meaning assignment | Theme switching |
| Component | Component customization | Per-component needs |

## Layer 1: Primitive Tokens

Raw design values without semantic meaning.

```css
:root {
  /* Colors */
  --color-gray-50: #F9FAFB;
  --color-gray-900: #111827;
  --color-blue-500: #3B82F6;
  --color-blue-600: #2563EB;

  /* Spacing (4px base) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */

  /* Typography */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;

  /* Radius */
  --radius-sm: 0.25rem;
  --radius-default: 0.5rem;
  --radius-lg: 0.75rem;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-default: 0 1px 3px rgb(0 0 0 / 0.1);
}
```

## Layer 2: Semantic Tokens

Purpose-based aliases that reference primitives.

```css
:root {
  /* Background */
  --color-background: var(--color-gray-50);
  --color-foreground: var(--color-gray-900);

  /* Primary */
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-700);

  /* Secondary */
  --color-secondary: var(--color-gray-100);
  --color-secondary-foreground: var(--color-gray-900);

  /* Muted */
  --color-muted: var(--color-gray-100);
  --color-muted-foreground: var(--color-gray-500);

  /* Destructive */
  --color-destructive: var(--color-red-600);
  --color-destructive-foreground: white;

  /* Spacing */
  --spacing-component: var(--space-4);
  --spacing-section: var(--space-6);
}
```

## Layer 3: Component Tokens

Component-specific tokens referencing semantic layer.

```css
:root {
  /* Button */
  --button-bg: var(--color-primary);
  --button-fg: white;
  --button-hover-bg: var(--color-primary-hover);
  --button-padding-x: var(--space-4);
  --button-padding-y: var(--space-2);
  --button-radius: var(--radius-default);

  /* Input */
  --input-bg: var(--color-background);
  --input-border: var(--color-gray-300);
  --input-focus-ring: var(--color-primary);
  --input-padding: var(--space-2) var(--space-3);

  /* Card */
  --card-bg: var(--color-background);
  --card-border: var(--color-gray-200);
  --card-padding: var(--space-4);
  --card-radius: var(--radius-lg);
  --card-shadow: var(--shadow-default);
}
```

## Dark Mode

Override semantic tokens for dark theme:

```css
.dark {
  --color-background: var(--color-gray-900);
  --color-foreground: var(--color-gray-50);
  --color-muted: var(--color-gray-800);
  --color-muted-foreground: var(--color-gray-400);
  --color-secondary: var(--color-gray-800);
}
```

## Naming Convention

```
--{category}-{item}-{variant}-{state}

Examples:
--color-primary           # category-item
--color-primary-hover     # category-item-state
--button-bg-hover         # component-property-state
--space-section-sm        # category-semantic-variant
```

## Categories

| Category | Examples |
|----------|----------|
| color | primary, secondary, muted, destructive |
| space | 1, 2, 4, 8, section, component |
| font-size | xs, sm, base, lg, xl |
| radius | sm, default, lg, full |
| shadow | sm, default, lg |
| duration | fast, normal, slow |

## File Organization

```
tokens/
├── primitives.css     # Raw values
├── semantic.css       # Purpose aliases
├── components.css     # Component tokens
└── index.css          # Imports all
```

Or single file with layer comments:

```css
/* === PRIMITIVES === */
:root { ... }

/* === SEMANTIC === */
:root { ... }

/* === COMPONENTS === */
:root { ... }

/* === DARK MODE === */
.dark { ... }
```

## Migration from Flat Tokens

Before (flat):
```css
--button-primary-bg: #2563EB;
--button-secondary-bg: #F3F4F6;
```

After (three-layer):
```css
/* Primitive */
--color-blue-600: #2563EB;
--color-gray-100: #F3F4F6;

/* Semantic */
--color-primary: var(--color-blue-600);
--color-secondary: var(--color-gray-100);

/* Component */
--button-bg: var(--color-primary);
--button-secondary-bg: var(--color-secondary);
```

## W3C DTCG Alignment

Token JSON format (W3C Design Tokens Community Group):

```json
{
  "color": {
    "blue": {
      "600": {
        "$value": "#2563EB",
        "$type": "color"
      }
    }
  }
}
```



---

## `scripts/embed-tokens.cjs`

````js
#!/usr/bin/env node
/**
 * embed-tokens.cjs
 * Reads design-tokens.css and outputs embeddable inline CSS.
 * Use when generating standalone HTML files (infographics, slides, etc.)
 *
 * Usage:
 *   node embed-tokens.cjs           # Output full CSS
 *   node embed-tokens.cjs --minimal # Output only commonly used tokens
 *   node embed-tokens.cjs --style   # Wrap in <style> tags
 */

const fs = require('fs');
const path = require('path');

// Find project root (look for assets/design-tokens.css)
function findProjectRoot(startDir) {
  // Walk up until dirname stops changing: on Windows the root is 'C:\', so a
  // `dir !== '/'` guard never terminates.
  let dir = startDir;
  for (;;) {
    if (fs.existsSync(path.join(dir, 'assets', 'design-tokens.css'))) {
      return dir;
    }
    const parent = path.dirname(dir);
    if (parent === dir) break;
    dir = parent;
  }
  return null;
}

const projectRoot = findProjectRoot(process.cwd());
if (!projectRoot) {
  console.error('Error: Could not find assets/design-tokens.css');
  process.exit(1);
}

const tokensPath = path.join(projectRoot, 'assets', 'design-tokens.css');

// Minimal tokens commonly used in infographics/slides
const MINIMAL_TOKENS = [
  '--primitive-spacing-',
  '--primitive-fontSize-',
  '--primitive-fontWeight-',
  '--primitive-lineHeight-',
  '--primitive-radius-',
  '--primitive-shadow-glow-',
  '--primitive-gradient-',
  '--primitive-duration-',
  '--color-primary',
  '--color-secondary',
  '--color-accent',
  '--color-background',
  '--color-surface',
  '--color-foreground',
  '--color-border',
  '--typography-font-',
  '--card-',
];

function extractTokens(css, minimal = false) {
  // Extract :root block
  const rootMatch = css.match(/:root\s*\{([^}]+)\}/g);
  if (!rootMatch) return '';

  let allVars = [];
  for (const block of rootMatch) {
    const vars = block.match(/--[\w-]+:\s*[^;]+;/g) || [];
    allVars = allVars.concat(vars);
  }

  if (minimal) {
    allVars = allVars.filter(v =>
      MINIMAL_TOKENS.some(token => v.includes(token))
    );
  }

  // Dedupe
  allVars = [...new Set(allVars)];

  return `:root {\n  ${allVars.join('\n  ')}\n}`;
}

// Parse args
const args = process.argv.slice(2);
const minimal = args.includes('--minimal');
const wrapStyle = args.includes('--style');

try {
  const css = fs.readFileSync(tokensPath, 'utf-8');
  let output = extractTokens(css, minimal);

  if (wrapStyle) {
    output = `<style>\n/* Design Tokens (embedded for standalone HTML) */\n${output}\n</style>`;
  } else {
    output = `/* Design Tokens (embedded for standalone HTML) */\n${output}`;
  }

  console.log(output);
} catch (err) {
  console.error(`Error reading tokens: ${err.message}`);
  process.exit(1);
}
````



---

## `scripts/fetch-background.py`

````python
#!/usr/bin/env python3
"""
Background Image Fetcher
Fetches real images from Pexels for slide backgrounds.
Uses web scraping (no API key required) or WebFetch tool integration.
"""

import json
import csv
import re
import sys
import os
from pathlib import Path

# The skill can be installed outside the project it operates on (user-level
# ~/.claude/skills/, or as a plugin), so the project root cannot be derived from
# this file's location. Resolve it from the working directory instead -- the same
# convention generate-tokens.cjs and validate-tokens.cjs already use via
# process.cwd(). DESIGN_SYSTEM_PROJECT_ROOT overrides it explicitly.
def _find_project_root():
    override = os.environ.get('DESIGN_SYSTEM_PROJECT_ROOT')
    if override:
        return Path(override).resolve()
    start = Path.cwd().resolve()
    markers = (
        Path('assets') / 'design-tokens.json',
        Path('assets') / 'design-tokens.css',
        Path('package.json'),
        Path('.git'),
    )
    for candidate in (start, *start.parents):
        if any((candidate / marker).exists() for marker in markers):
            return candidate
    return start


PROJECT_ROOT = _find_project_root()
TOKENS_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.json'
BACKGROUNDS_CSV = Path(__file__).parent.parent / 'data' / 'slide-backgrounds.csv'


def resolve_token_reference(ref: str, tokens: dict) -> str:
    """Resolve token reference like {primitive.color.ocean-blue.500} to hex value."""
    if not ref or not ref.startswith('{') or not ref.endswith('}'):
        return ref  # Already a value, not a reference

    # Parse reference: {primitive.color.ocean-blue.500}
    path = ref[1:-1].split('.')  # ['primitive', 'color', 'ocean-blue', '500']
    current = tokens
    for key in path:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return None  # Invalid path
    # Return $value if it's a token object
    if isinstance(current, dict) and '$value' in current:
        return current['$value']
    return current


def load_brand_colors():
    """Load colors from assets/design-tokens.json for overlay gradients.

    Resolves semantic token references to actual hex values.
    """
    try:
        with open(TOKENS_PATH) as f:
            tokens = json.load(f)

        colors = tokens.get('primitive', {}).get('color', {})
        semantic = tokens.get('semantic', {}).get('color', {})

        # Try semantic tokens first (preferred) - resolve references
        if semantic:
            primary_ref = semantic.get('primary', {}).get('$value')
            secondary_ref = semantic.get('secondary', {}).get('$value')
            accent_ref = semantic.get('accent', {}).get('$value')
            background_ref = semantic.get('background', {}).get('$value')

            primary = resolve_token_reference(primary_ref, tokens)
            secondary = resolve_token_reference(secondary_ref, tokens)
            accent = resolve_token_reference(accent_ref, tokens)
            background = resolve_token_reference(background_ref, tokens)

            if primary and secondary:
                return {
                    'primary': primary,
                    'secondary': secondary,
                    'accent': accent or primary,
                    'background': background or '#0D0D0D',
                }

        # Fallback: find first color palette with 500 value (primary)
        primary_keys = ['ocean-blue', 'coral', 'blue', 'primary']
        secondary_keys = ['golden-amber', 'purple', 'amber', 'secondary']
        accent_keys = ['emerald', 'mint', 'green', 'accent']

        primary_color = None
        secondary_color = None
        accent_color = None

        for key in primary_keys:
            if key in colors and isinstance(colors[key], dict):
                primary_color = colors[key].get('500', {}).get('$value')
                if primary_color:
                    break

        for key in secondary_keys:
            if key in colors and isinstance(colors[key], dict):
                secondary_color = colors[key].get('500', {}).get('$value')
                if secondary_color:
                    break

        for key in accent_keys:
            if key in colors and isinstance(colors[key], dict):
                accent_color = colors[key].get('500', {}).get('$value')
                if accent_color:
                    break

        background = colors.get('dark', {}).get('800', {}).get('$value', '#0D0D0D')

        return {
            'primary': primary_color or '#3B82F6',
            'secondary': secondary_color or '#F59E0B',
            'accent': accent_color or '#10B981',
            'background': background,
        }
    except (FileNotFoundError, KeyError, TypeError):
        # Fallback defaults
        return {
            'primary': '#3B82F6',
            'secondary': '#F59E0B',
            'accent': '#10B981',
            'background': '#0D0D0D',
        }


def load_backgrounds_config():
    """Load background configuration from CSV."""
    config = {}
    try:
        with open(BACKGROUNDS_CSV, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                config[row['slide_type']] = row
    except FileNotFoundError:
        print(f"Warning: {BACKGROUNDS_CSV} not found")
    return config


def get_overlay_css(style: str, brand_colors: dict) -> str:
    """Generate overlay CSS using brand colors from design-tokens.json."""
    overlays = {
        'gradient-dark': f"linear-gradient(135deg, {brand_colors['background']}E6, {brand_colors['background']}B3)",
        'gradient-brand': f"linear-gradient(135deg, {brand_colors['primary']}CC, {brand_colors['secondary']}99)",
        'gradient-accent': f"linear-gradient(135deg, {brand_colors['accent']}99, transparent)",
        'blur-dark': f"rgba(13,13,13,0.8)",
        'desaturate-dark': f"rgba(13,13,13,0.7)",
    }
    return overlays.get(style, overlays['gradient-dark'])


# Curated high-quality images from Pexels (free to use, pre-selected for brand aesthetic)
CURATED_IMAGES = {
    'hero': [
        'https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/2582937/pexels-photo-2582937.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'vision': [
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'team': [
        'https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3184338/pexels-photo-3184338.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3182773/pexels-photo-3182773.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'testimonial': [
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/1181622/pexels-photo-1181622.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'cta': [
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3184298/pexels-photo-3184298.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'problem': [
        'https://images.pexels.com/photos/3760529/pexels-photo-3760529.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/897817/pexels-photo-897817.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'solution': [
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3184644/pexels-photo-3184644.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'hook': [
        'https://images.pexels.com/photos/2582937/pexels-photo-2582937.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/1089438/pexels-photo-1089438.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'social': [
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3184287/pexels-photo-3184287.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
    'demo': [
        'https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=1920',
        'https://images.pexels.com/photos/3861958/pexels-photo-3861958.jpeg?auto=compress&cs=tinysrgb&w=1920',
    ],
}


def get_curated_images(slide_type: str) -> list:
    """Get curated images for slide type."""
    return CURATED_IMAGES.get(slide_type, CURATED_IMAGES.get('hero', []))


def get_pexels_search_url(keywords: str) -> str:
    """Generate Pexels search URL for manual lookup."""
    import urllib.parse
    return f"https://www.pexels.com/search/{urllib.parse.quote(keywords)}/"


def get_background_image(slide_type: str) -> dict:
    """
    Get curated image matching slide type and brand aesthetic.
    Uses pre-selected Pexels images (no API/scraping needed).
    """
    brand_colors = load_brand_colors()
    config = load_backgrounds_config()

    slide_config = config.get(slide_type)
    overlay_style = 'gradient-dark'
    keywords = slide_type

    if slide_config:
        keywords = slide_config.get('search_keywords', slide_config.get('image_category', slide_type))
        overlay_style = slide_config.get('overlay_style', 'gradient-dark')

    # Get curated images
    urls = get_curated_images(slide_type)
    if urls:
        return {
            'url': urls[0],
            'all_urls': urls,
            'overlay': get_overlay_css(overlay_style, brand_colors),
            'attribution': 'Photo from Pexels (free to use)',
            'source': 'pexels-curated',
            'search_url': get_pexels_search_url(keywords),
        }

    # Fallback: provide search URL for manual selection
    return {
        'url': None,
        'overlay': get_overlay_css(overlay_style, brand_colors),
        'keywords': keywords,
        'search_url': get_pexels_search_url(keywords),
        'available_types': list(CURATED_IMAGES.keys()),
    }


def generate_css_for_background(result: dict, slide_class: str = '.slide-with-bg') -> str:
    """Generate CSS for a background slide."""
    if not result.get('url'):
        search_url = result.get('search_url', '')
        return f"""/* No image scraped. Search manually: {search_url} */
/* Overlay ready: {result.get('overlay', 'gradient-dark')} */
"""

    return f"""{slide_class} {{
    background-image: url('{result['url']}');
    background-size: cover;
    background-position: center;
    position: relative;
}}

{slide_class}::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: {result['overlay']};
}}

{slide_class} .content {{
    position: relative;
    z-index: 1;
}}

/* {result.get('attribution', 'Pexels')} - {result.get('search_url', '')} */
"""


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Get background images for slides')
    parser.add_argument('slide_type', nargs='?', help='Slide type (hero, vision, team, etc.)')
    parser.add_argument('--list', action='store_true', help='List available slide types')
    parser.add_argument('--css', action='store_true', help='Output CSS for the background')
    parser.add_argument('--json', action='store_true', help='Output JSON')
    parser.add_argument('--colors', action='store_true', help='Show brand colors')
    parser.add_argument('--all', action='store_true', help='Show all curated URLs')

    args = parser.parse_args()

    if args.colors:
        colors = load_brand_colors()
        print("\nBrand Colors (from design-tokens.json):")
        for name, value in colors.items():
            print(f"  {name}: {value}")
        return

    if args.list:
        print("\nAvailable slide types (curated images):")
        for slide_type, urls in CURATED_IMAGES.items():
            print(f"  {slide_type}: {len(urls)} images")
        return

    if not args.slide_type:
        parser.print_help()
        return

    result = get_background_image(args.slide_type)

    if args.json:
        print(json.dumps(result, indent=2))
    elif args.css:
        print(generate_css_for_background(result))
    elif args.all:
        print(f"\nAll images for '{args.slide_type}':")
        for i, url in enumerate(result.get('all_urls', []), 1):
            print(f"  {i}. {url}")
    else:
        print(f"\nImage URL: {result['url']}")
        print(f"Alternatives: {len(result.get('all_urls', []))} available (use --all)")
        print(f"Overlay: {result['overlay']}")


if __name__ == '__main__':
    main()
````



---

## `scripts/generate-slide.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide Generator - Generates HTML slides using design tokens
ALL styles MUST use CSS variables from design-tokens.css
NO hardcoded colors, fonts, or spacing allowed
"""

import argparse
import json
from html import escape
from pathlib import Path
from datetime import datetime


def _e(value, default=''):
    """HTML-escape a user-supplied value for safe embedding in HTML content."""
    return escape(str(value if value is not None else default))


def _safe_url(url, default='#'):
    """Validate and escape a URL for use in href attributes.

    Only allows http://, https://, #, and / schemes to prevent
    javascript: URI injection (CWE-79).
    """
    if url and str(url).strip().lower().startswith(('http://', 'https://', '#', '/')):
        return escape(str(url), quote=True)
    return default

# Paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
TOKENS_CSS = Path(__file__).resolve().parents[4] / "assets" / "design-tokens.css"
TOKENS_JSON = Path(__file__).resolve().parents[4] / "assets" / "design-tokens.json"
OUTPUT_DIR = Path(__file__).resolve().parents[4] / "assets" / "designs" / "slides"

# ============ BRAND-COMPLIANT SLIDE TEMPLATE ============
# ALL values reference CSS variables from design-tokens.css

SLIDE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <!-- Brand Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">

    <!-- Design Tokens - SINGLE SOURCE OF TRUTH -->
    <link rel="stylesheet" href="{tokens_css_path}">

    <style>
        /* ============================================
           STRICT TOKEN USAGE - NO HARDCODED VALUES
           All styles MUST use var(--token-name)
           ============================================ */

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html, body {{
            width: 100%;
            height: 100%;
        }}

        body {{
            font-family: var(--typography-font-body);
            background: var(--color-background);
            color: var(--color-foreground);
            line-height: var(--primitive-lineHeight-relaxed);
        }}

        /* Slide Container - 16:9 aspect ratio */
        .slide-deck {{
            width: 100%;
            max-width: 1920px;
            margin: 0 auto;
        }}

        .slide {{
            width: 100%;
            aspect-ratio: 16 / 9;
            padding: var(--slide-padding);
            background: var(--slide-bg);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }}

        .slide + .slide {{
            margin-top: var(--primitive-spacing-8);
        }}

        /* Background Variants */
        .slide--surface {{
            background: var(--slide-bg-surface);
        }}

        .slide--gradient {{
            background: var(--slide-bg-gradient);
        }}

        .slide--glow::before {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 150%;
            height: 150%;
            background: var(--primitive-gradient-glow);
            pointer-events: none;
        }}

        /* Typography - MUST use token fonts and sizes */
        h1, h2, h3, h4, h5, h6 {{
            font-family: var(--typography-font-heading);
            font-weight: var(--primitive-fontWeight-bold);
            line-height: var(--primitive-lineHeight-tight);
        }}

        .slide-title {{
            font-size: var(--slide-title-size);
            background: var(--primitive-gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .slide-heading {{
            font-size: var(--slide-heading-size);
            color: var(--color-foreground);
        }}

        .slide-subheading {{
            font-size: var(--primitive-fontSize-3xl);
            color: var(--color-foreground-secondary);
            font-weight: var(--primitive-fontWeight-medium);
        }}

        .slide-body {{
            font-size: var(--slide-body-size);
            color: var(--color-foreground-secondary);
            max-width: 80ch;
        }}

        /* Brand Colors - Primary/Secondary/Accent */
        .text-primary {{ color: var(--color-primary); }}
        .text-secondary {{ color: var(--color-secondary); }}
        .text-accent {{ color: var(--color-accent); }}
        .text-muted {{ color: var(--color-foreground-muted); }}

        .bg-primary {{ background: var(--color-primary); }}
        .bg-secondary {{ background: var(--color-secondary); }}
        .bg-accent {{ background: var(--color-accent); }}
        .bg-surface {{ background: var(--color-surface); }}

        /* Cards - Using component tokens */
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: var(--card-radius);
            padding: var(--card-padding);
            box-shadow: var(--card-shadow);
            transition: border-color var(--primitive-duration-base) var(--primitive-easing-out);
        }}

        .card:hover {{
            border-color: var(--card-border-hover);
        }}

        /* Buttons - Using component tokens */
        .btn {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: var(--button-primary-padding-y) var(--button-primary-padding-x);
            border-radius: var(--button-primary-radius);
            font-size: var(--button-primary-font-size);
            font-weight: var(--button-primary-font-weight);
            font-family: var(--typography-font-body);
            text-decoration: none;
            cursor: pointer;
            border: none;
            transition: all var(--primitive-duration-base) var(--primitive-easing-out);
        }}

        .btn-primary {{
            background: var(--button-primary-bg);
            color: var(--button-primary-fg);
            box-shadow: var(--button-primary-shadow);
        }}

        .btn-primary:hover {{
            background: var(--button-primary-bg-hover);
        }}

        .btn-secondary {{
            background: transparent;
            color: var(--color-primary);
            border: 2px solid var(--color-primary);
        }}

        /* Layout Utilities */
        .flex {{ display: flex; }}
        .flex-col {{ flex-direction: column; }}
        .items-center {{ align-items: center; }}
        .justify-center {{ justify-content: center; }}
        .justify-between {{ justify-content: space-between; }}
        .gap-4 {{ gap: var(--primitive-spacing-4); }}
        .gap-6 {{ gap: var(--primitive-spacing-6); }}
        .gap-8 {{ gap: var(--primitive-spacing-8); }}

        .grid {{ display: grid; }}
        .grid-2 {{ grid-template-columns: repeat(2, 1fr); }}
        .grid-3 {{ grid-template-columns: repeat(3, 1fr); }}
        .grid-4 {{ grid-template-columns: repeat(4, 1fr); }}

        .text-center {{ text-align: center; }}
        .mt-auto {{ margin-top: auto; }}
        .mb-4 {{ margin-bottom: var(--primitive-spacing-4); }}
        .mb-6 {{ margin-bottom: var(--primitive-spacing-6); }}
        .mb-8 {{ margin-bottom: var(--primitive-spacing-8); }}

        /* Metric Cards */
        .metric {{
            text-align: center;
            padding: var(--primitive-spacing-6);
        }}

        .metric-value {{
            font-family: var(--typography-font-heading);
            font-size: var(--primitive-fontSize-6xl);
            font-weight: var(--primitive-fontWeight-bold);
            background: var(--primitive-gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .metric-label {{
            font-size: var(--primitive-fontSize-lg);
            color: var(--color-foreground-secondary);
            margin-top: var(--primitive-spacing-2);
        }}

        /* Feature List */
        .feature-item {{
            display: flex;
            align-items: flex-start;
            gap: var(--primitive-spacing-4);
            padding: var(--primitive-spacing-4) 0;
        }}

        .feature-icon {{
            width: 48px;
            height: 48px;
            border-radius: var(--primitive-radius-lg);
            background: var(--color-surface-elevated);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--color-primary);
            font-size: var(--primitive-fontSize-xl);
            flex-shrink: 0;
        }}

        .feature-content h4 {{
            font-size: var(--primitive-fontSize-xl);
            color: var(--color-foreground);
            margin-bottom: var(--primitive-spacing-2);
        }}

        .feature-content p {{
            color: var(--color-foreground-secondary);
            font-size: var(--primitive-fontSize-base);
        }}

        /* Testimonial */
        .testimonial {{
            background: var(--color-surface);
            border-radius: var(--primitive-radius-xl);
            padding: var(--primitive-spacing-8);
            border-left: 4px solid var(--color-primary);
        }}

        .testimonial-quote {{
            font-size: var(--primitive-fontSize-2xl);
            color: var(--color-foreground);
            font-style: italic;
            margin-bottom: var(--primitive-spacing-6);
        }}

        .testimonial-author {{
            font-size: var(--primitive-fontSize-lg);
            color: var(--color-primary);
            font-weight: var(--primitive-fontWeight-semibold);
        }}

        .testimonial-role {{
            font-size: var(--primitive-fontSize-base);
            color: var(--color-foreground-muted);
        }}

        /* Badge/Tag */
        .badge {{
            display: inline-block;
            padding: var(--primitive-spacing-2) var(--primitive-spacing-4);
            background: var(--color-surface-elevated);
            border-radius: var(--primitive-radius-full);
            font-size: var(--primitive-fontSize-sm);
            color: var(--color-accent);
            font-weight: var(--primitive-fontWeight-medium);
        }}

        /* Chart Container */
        .chart-container {{
            background: var(--color-surface);
            border-radius: var(--primitive-radius-xl);
            padding: var(--primitive-spacing-6);
            height: 100%;
            display: flex;
            flex-direction: column;
        }}

        .chart-title {{
            font-family: var(--typography-font-heading);
            font-size: var(--primitive-fontSize-xl);
            color: var(--color-foreground);
            margin-bottom: var(--primitive-spacing-4);
        }}

        /* CSS-only Bar Chart */
        .bar-chart {{
            display: flex;
            align-items: flex-end;
            gap: var(--primitive-spacing-4);
            height: 200px;
            padding-top: var(--primitive-spacing-4);
        }}

        .bar {{
            flex: 1;
            background: var(--primitive-gradient-primary);
            border-radius: var(--primitive-radius-md) var(--primitive-radius-md) 0 0;
            position: relative;
            min-width: 40px;
        }}

        .bar-label {{
            position: absolute;
            bottom: -30px;
            left: 50%;
            transform: translateX(-50%);
            font-size: var(--primitive-fontSize-sm);
            color: var(--color-foreground-muted);
            white-space: nowrap;
        }}

        .bar-value {{
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            font-size: var(--primitive-fontSize-sm);
            color: var(--color-foreground);
            font-weight: var(--primitive-fontWeight-semibold);
        }}

        /* Progress Bar */
        .progress {{
            height: 12px;
            background: var(--color-surface-elevated);
            border-radius: var(--primitive-radius-full);
            overflow: hidden;
        }}

        .progress-fill {{
            height: 100%;
            background: var(--primitive-gradient-primary);
            border-radius: var(--primitive-radius-full);
        }}

        /* Footer */
        .slide-footer {{
            margin-top: auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: var(--primitive-spacing-6);
            border-top: 1px solid var(--color-border);
            color: var(--color-foreground-muted);
            font-size: var(--primitive-fontSize-sm);
        }}

        /* Glow Effects */
        .glow-coral {{
            box-shadow: var(--primitive-shadow-glow-coral);
        }}

        .glow-purple {{
            box-shadow: var(--primitive-shadow-glow-purple);
        }}

        .glow-mint {{
            box-shadow: var(--primitive-shadow-glow-mint);
        }}
    </style>
</head>
<body>
    <div class="slide-deck">
        {slides_content}
    </div>
</body>
</html>
'''


# ============ SLIDE GENERATORS ============

def generate_title_slide(data):
    """Title slide with gradient headline"""
    return f'''
    <section class="slide slide--glow flex flex-col items-center justify-center text-center">
        <div class="badge mb-6">{_e(data.get('badge', 'Pitch Deck'))}</div>
        <h1 class="slide-title mb-6">{_e(data.get('title', 'Your Title Here'))}</h1>
        <p class="slide-subheading mb-8">{_e(data.get('subtitle', 'Your compelling subtitle'))}</p>
        <div class="flex gap-4">
            <a href="#" class="btn btn-primary">{_e(data.get('cta', 'Get Started'))}</a>
            <a href="#" class="btn btn-secondary">{_e(data.get('secondary_cta', 'Learn More'))}</a>
        </div>
        <div class="slide-footer">
            <span>{_e(data.get('company', 'Company Name'))}</span>
            <span>{_e(data.get('date', datetime.now().strftime('%B %Y')))}</span>
        </div>
    </section>
    '''


def generate_problem_slide(data):
    """Problem statement slide using PAS formula"""
    return f'''
    <section class="slide slide--surface">
        <div class="badge mb-6">The Problem</div>
        <h2 class="slide-heading mb-8">{_e(data.get('headline', 'The problem your audience faces'))}</h2>
        <div class="grid grid-3 gap-8">
            <div class="card">
                <div class="text-primary" style="font-size: var(--primitive-fontSize-4xl); margin-bottom: var(--primitive-spacing-4);">01</div>
                <h4 style="margin-bottom: var(--primitive-spacing-2); font-size: var(--primitive-fontSize-xl);">{_e(data.get('pain_1_title', 'Pain Point 1'))}</h4>
                <p class="text-muted">{_e(data.get('pain_1_desc', 'Description of the first pain point'))}</p>
            </div>
            <div class="card">
                <div class="text-secondary" style="font-size: var(--primitive-fontSize-4xl); margin-bottom: var(--primitive-spacing-4);">02</div>
                <h4 style="margin-bottom: var(--primitive-spacing-2); font-size: var(--primitive-fontSize-xl);">{_e(data.get('pain_2_title', 'Pain Point 2'))}</h4>
                <p class="text-muted">{_e(data.get('pain_2_desc', 'Description of the second pain point'))}</p>
            </div>
            <div class="card">
                <div class="text-accent" style="font-size: var(--primitive-fontSize-4xl); margin-bottom: var(--primitive-spacing-4);">03</div>
                <h4 style="margin-bottom: var(--primitive-spacing-2); font-size: var(--primitive-fontSize-xl);">{_e(data.get('pain_3_title', 'Pain Point 3'))}</h4>
                <p class="text-muted">{_e(data.get('pain_3_desc', 'Description of the third pain point'))}</p>
            </div>
        </div>
        <div class="slide-footer">
            <span>{_e(data.get('company', 'Company Name'))}</span>
            <span>{_e(data.get('page', '2'))}</span>
        </div>
    </section>
    '''


def generate_solution_slide(data):
    """Solution slide with feature highlights"""
    return f'''
    <section class="slide">
        <div class="badge mb-6">The Solution</div>
        <h2 class="slide-heading mb-8">{_e(data.get('headline', 'How we solve this'))}</h2>
        <div class="flex gap-8" style="flex: 1;">
            <div style="flex: 1;">
                <div class="feature-item">
                    <div class="feature-icon">&#10003;</div>
                    <div class="feature-content">
                        <h4>{_e(data.get('feature_1_title', 'Feature 1'))}</h4>
                        <p>{_e(data.get('feature_1_desc', 'Description of feature 1'))}</p>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">&#10003;</div>
                    <div class="feature-content">
                        <h4>{_e(data.get('feature_2_title', 'Feature 2'))}</h4>
                        <p>{_e(data.get('feature_2_desc', 'Description of feature 2'))}</p>
                    </div>
                </div>
                <div class="feature-item">
                    <div class="feature-icon">&#10003;</div>
                    <div class="feature-content">
                        <h4>{_e(data.get('feature_3_title', 'Feature 3'))}</h4>
                        <p>{_e(data.get('feature_3_desc', 'Description of feature 3'))}</p>
                    </div>
                </div>
            </div>
            <div style="flex: 1;" class="card flex items-center justify-center">
                <div class="text-center">
                    <div class="text-accent" style="font-size: 80px; margin-bottom: var(--primitive-spacing-4);">&#9670;</div>
                    <p class="text-muted">Product screenshot or demo</p>
                </div>
            </div>
        </div>
        <div class="slide-footer">
            <span>{_e(data.get('company', 'Company Name'))}</span>
            <span>{_e(data.get('page', '3'))}</span>
        </div>
    </section>
    '''


def generate_metrics_slide(data):
    """Traction/metrics slide with large numbers"""
    metrics = data.get('metrics', [
        {'value': '10K+', 'label': 'Active Users'},
        {'value': '95%', 'label': 'Retention Rate'},
        {'value': '3x', 'label': 'Revenue Growth'},
        {'value': '$2M', 'label': 'ARR'}
    ])

    metrics_html = ''.join([f'''
        <div class="card metric">
            <div class="metric-value">{_e(m.get('value', ''))}</div>
            <div class="metric-label">{_e(m.get('label', ''))}</div>
        </div>
    ''' for m in metrics[:4]])

    return f'''
    <section class="slide slide--surface slide--glow">
        <div class="badge mb-6">Traction</div>
        <h2 class="slide-heading mb-8 text-center">{_e(data.get('headline', 'Our Growth'))}</h2>
        <div class="grid grid-4 gap-6" style="flex: 1; align-items: center;">
            {metrics_html}
        </div>
        <div class="slide-footer">
            <span>{_e(data.get('company', 'Company Name'))}</span>
            <span>{_e(data.get('page', '4'))}</span>
        </div>
    </section>
    '''


def generate_chart_slide(data):
    """Chart slide with CSS bar chart"""
    bars = data.get('bars', [
        {'label': 'Q1', 'value': 40},
        {'label': 'Q2', 'value': 60},
        {'label': 'Q3', 'value': 80},
        {'label': 'Q4', 'value': 100}
    ])

    bars_html = ''.join([f'''
        <div class="bar" style="height: {int(b.get('value', 0))}%;">
            <span class="bar-value">{_e(b.get('display', str(b.get('value', 0)) + '%'))}</span>
            <span class="bar-label">{_e(b.get('label', ''))}</span>
        </div>
    ''' for b in bars])

    return f'''
    <section class="slide">
        <div class="badge mb-6">{_e(data.get('badge', 'Growth'))}</div>
        <h2 class="slide-heading mb-8">{_e(data.get('headline', 'Revenue Growth'))}</h2>
        <div class="chart-container" style="flex: 1;">
            <div class="chart-title">{_e(data.get('chart_title', 'Quarterly Revenue'))}</div>
            <div class="bar-chart" style="flex: 1; padding-bottom: 40px;">
                {bars_html}
            </div>
        </div>
        <div class="slide-footer">
            <span>{_e(data.get('company', 'Company Name'))}</span>
            <span>{_e(data.get('page', '5'))}</span>
        </div>
    </section>
    '''


def generate_testimonial_slide(data):
    """Social proof slide"""
    return f'''
    <section class="slide slide--surface flex flex-col justify-center">
        <div class="badge mb-6">What They Say</div>
        <div class="testimonial" style="max-width: 900px;">
            <p class="testimonial-quote">"{_e(data.get('quote', 'This product changed how we work. Incredible results.'))}"</p>
            <p class="testimonial-author">{_e(data.get('author', 'Jane Doe'))}</p>
            <p class="testimonial-role">{_e(data.get('role', 'CEO, Example Company'))}</p>
        </div>
        <div class="slide-footer">
            <span>{_e(data.get('company', 'Company Name'))}</span>
            <span>{_e(data.get('page', '6'))}</span>
        </div>
    </section>
    '''


def generate_cta_slide(data):
    """Closing CTA slide"""
    return f'''
    <section class="slide slide--gradient flex flex-col items-center justify-center text-center">
        <h2 class="slide-heading mb-6" style="color: var(--color-foreground);">{_e(data.get('headline', 'Ready to get started?'))}</h2>
        <p class="slide-body mb-8" style="color: rgba(255,255,255,0.8);">{_e(data.get('subheadline', 'Join thousands of teams already using our solution.'))}</p>
        <div class="flex gap-4">
            <a href="{_safe_url(data.get('cta_url', '#'))}" class="btn" style="background: var(--color-foreground); color: var(--color-primary);">{_e(data.get('cta', 'Start Free Trial'))}</a>
        </div>
        <div class="slide-footer" style="border-color: rgba(255,255,255,0.2); color: rgba(255,255,255,0.6);">
            <span>{_e(data.get('contact', 'contact@example.com'))}</span>
            <span>{_e(data.get('website', 'www.example.com'))}</span>
        </div>
    </section>
    '''


# Slide type mapping
SLIDE_GENERATORS = {
    'title': generate_title_slide,
    'problem': generate_problem_slide,
    'solution': generate_solution_slide,
    'metrics': generate_metrics_slide,
    'traction': generate_metrics_slide,
    'chart': generate_chart_slide,
    'testimonial': generate_testimonial_slide,
    'cta': generate_cta_slide,
    'closing': generate_cta_slide
}


def generate_deck(slides_data, title="Pitch Deck"):
    """Generate complete deck from slide data list"""
    slides_html = ""
    for slide in slides_data:
        slide_type = slide.get('type', 'title')
        generator = SLIDE_GENERATORS.get(slide_type)
        if generator:
            slides_html += generator(slide)
        else:
            print(f"Warning: Unknown slide type '{slide_type}'")

    # Calculate relative path to tokens CSS
    tokens_rel_path = "../../../assets/design-tokens.css"

    return SLIDE_TEMPLATE.format(
        title=escape(str(title)),
        tokens_css_path=tokens_rel_path,
        slides_content=slides_html
    )


def main():
    parser = argparse.ArgumentParser(description="Generate brand-compliant slides")
    parser.add_argument("--json", "-j", help="JSON file with slide data")
    parser.add_argument("--output", "-o", help="Output HTML file path")
    parser.add_argument("--demo", action="store_true", help="Generate demo deck")

    args = parser.parse_args()

    if args.demo:
        # Demo deck showcasing all slide types
        demo_slides = [
            {
                'type': 'title',
                'badge': 'Investor Deck 2024',
                'title': 'ClaudeKit Marketing',
                'subtitle': 'Your AI marketing team. Always on.',
                'cta': 'Join Waitlist',
                'secondary_cta': 'See Demo',
                'company': 'ClaudeKit',
                'date': 'December 2024'
            },
            {
                'type': 'problem',
                'headline': 'Marketing teams are drowning',
                'pain_1_title': 'Content Overload',
                'pain_1_desc': 'Need to produce 10x content with same headcount',
                'pain_2_title': 'Tool Fatigue',
                'pain_2_desc': '15+ tools that don\'t talk to each other',
                'pain_3_title': 'No Time to Think',
                'pain_3_desc': 'Strategy suffers when execution consumes all hours',
                'company': 'ClaudeKit',
                'page': '2'
            },
            {
                'type': 'solution',
                'headline': 'AI agents that actually get marketing',
                'feature_1_title': 'Content Creation',
                'feature_1_desc': 'Blog posts, social, email - all on brand, all on time',
                'feature_2_title': 'Campaign Management',
                'feature_2_desc': 'Multi-channel orchestration with one command',
                'feature_3_title': 'Analytics & Insights',
                'feature_3_desc': 'Real-time optimization without the spreadsheets',
                'company': 'ClaudeKit',
                'page': '3'
            },
            {
                'type': 'metrics',
                'headline': 'Early traction speaks volumes',
                'metrics': [
                    {'value': '500+', 'label': 'Beta Users'},
                    {'value': '85%', 'label': 'Weekly Active'},
                    {'value': '4.9', 'label': 'NPS Score'},
                    {'value': '50hrs', 'label': 'Saved/Week'}
                ],
                'company': 'ClaudeKit',
                'page': '4'
            },
            {
                'type': 'chart',
                'badge': 'Revenue',
                'headline': 'Growing month over month',
                'chart_title': 'MRR Growth ($K)',
                'bars': [
                    {'label': 'Sep', 'value': 20, 'display': '$5K'},
                    {'label': 'Oct', 'value': 40, 'display': '$12K'},
                    {'label': 'Nov', 'value': 70, 'display': '$28K'},
                    {'label': 'Dec', 'value': 100, 'display': '$45K'}
                ],
                'company': 'ClaudeKit',
                'page': '5'
            },
            {
                'type': 'testimonial',
                'quote': 'ClaudeKit replaced 3 tools and 2 contractors. Our content output tripled while costs dropped 60%.',
                'author': 'Sarah Chen',
                'role': 'Head of Marketing, TechStartup',
                'company': 'ClaudeKit',
                'page': '6'
            },
            {
                'type': 'cta',
                'headline': 'Ship campaigns while you sleep',
                'subheadline': 'Early access available. Limited spots.',
                'cta': 'Join the Waitlist',
                'contact': 'hello@claudekit.ai',
                'website': 'claudekit.ai'
            }
        ]

        html = generate_deck(demo_slides, "ClaudeKit Marketing - Pitch Deck")

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        output_path = OUTPUT_DIR / f"demo-pitch-{datetime.now().strftime('%y%m%d')}.html"
        output_path.write_text(html, encoding='utf-8')
        print(f"Demo deck generated: {output_path}")

    elif args.json:
        with open(args.json, 'r') as f:
            data = json.load(f)

        html = generate_deck(data.get('slides', []), data.get('title', 'Presentation'))

        output_path = Path(args.output) if args.output else OUTPUT_DIR / f"deck-{datetime.now().strftime('%y%m%d-%H%M')}.html"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding='utf-8')
        print(f"Deck generated: {output_path}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
````



---

## `scripts/generate-tokens.cjs`

````js
#!/usr/bin/env node
/**
 * Generate CSS variables from design tokens JSON
 *
 * Usage:
 *   node generate-tokens.cjs --config tokens.json -o tokens.css
 *   node generate-tokens.cjs --config tokens.json --format tailwind
 */

const fs = require('fs');
const path = require('path');

/**
 * Parse command line arguments
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const options = {
    config: null,
    output: null,
    format: 'css' // css | tailwind
  };

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--config' || args[i] === '-c') {
      options.config = args[++i];
    } else if (args[i] === '--output' || args[i] === '-o') {
      options.output = args[++i];
    } else if (args[i] === '--format' || args[i] === '-f') {
      options.format = args[++i];
    } else if (args[i] === '--help' || args[i] === '-h') {
      console.log(`
Usage: node generate-tokens.cjs [options]

Options:
  -c, --config <file>   Input JSON token file (required)
  -o, --output <file>   Output file (default: stdout)
  -f, --format <type>   Output format: css | tailwind (default: css)
  -h, --help            Show this help
      `);
      process.exit(0);
    }
  }

  return options;
}

/**
 * Resolve token references like {primitive.color.blue.600}
 */
function resolveReference(value, tokens) {
  if (typeof value !== 'string' || !value.startsWith('{')) {
    return value;
  }

  const path = value.slice(1, -1).split('.');
  let result = tokens;

  for (const key of path) {
    result = result?.[key];
  }

  if (result?.$value) {
    return resolveReference(result.$value, tokens);
  }

  return result || value;
}

/**
 * Convert token name to CSS variable name
 */
function toCssVarName(path) {
  return '--' + path.join('-').replace(/\./g, '-');
}

/**
 * Flatten tokens into CSS variables
 */
function flattenTokens(obj, tokens, prefix = [], result = {}) {
  for (const [key, value] of Object.entries(obj)) {
    const currentPath = [...prefix, key];

    if (value && typeof value === 'object') {
      if (value.$value !== undefined) {
        // This is a token
        const cssVar = toCssVarName(currentPath);
        const resolvedValue = resolveReference(value.$value, tokens);
        result[cssVar] = resolvedValue;
      } else {
        // Recurse into nested object
        flattenTokens(value, tokens, currentPath, result);
      }
    }
  }

  return result;
}

/**
 * Generate CSS output
 */
function generateCSS(tokens) {
  const primitive = flattenTokens(tokens.primitive || {}, tokens, ['primitive']);
  const semantic = flattenTokens(tokens.semantic || {}, tokens, []);
  const component = flattenTokens(tokens.component || {}, tokens, []);
  const darkSemantic = flattenTokens(tokens.dark?.semantic || {}, tokens, []);

  let css = `/* Design Tokens - Auto-generated */
/* Do not edit directly - modify tokens.json instead */

/* === PRIMITIVES === */
:root {
${Object.entries(primitive).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}

/* === SEMANTIC === */
:root {
${Object.entries(semantic).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}

/* === COMPONENTS === */
:root {
${Object.entries(component).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}
`;

  if (Object.keys(darkSemantic).length > 0) {
    css += `
/* === DARK MODE === */
.dark {
${Object.entries(darkSemantic).map(([k, v]) => `  ${k}: ${v};`).join('\n')}
}
`;
  }

  return css;
}

/**
 * Generate Tailwind config output
 */
function generateTailwind(tokens) {
  const semantic = flattenTokens(tokens.semantic || {}, tokens, []);

  // Extract colors for Tailwind
  const colors = {};
  for (const [key, value] of Object.entries(semantic)) {
    if (key.includes('color')) {
      const name = key.replace('--color-', '').replace(/-/g, '.');
      colors[name] = `var(${key})`;
    }
  }

  return `// Tailwind color config - Auto-generated
// Add to tailwind.config.ts theme.extend.colors

module.exports = {
  colors: ${JSON.stringify(colors, null, 2).replace(/"/g, "'")}
};
`;
}

/**
 * Main
 */
function main() {
  const options = parseArgs();

  if (!options.config) {
    console.error('Error: --config is required');
    process.exit(1);
  }

  // Resolve config path
  const configPath = path.resolve(process.cwd(), options.config);

  if (!fs.existsSync(configPath)) {
    console.error(`Error: Config file not found: ${configPath}`);
    process.exit(1);
  }

  // Read and parse tokens
  const tokens = JSON.parse(fs.readFileSync(configPath, 'utf-8'));

  // Generate output
  let output;
  if (options.format === 'tailwind') {
    output = generateTailwind(tokens);
  } else {
    output = generateCSS(tokens);
  }

  // Write output
  if (options.output) {
    const outputPath = path.resolve(process.cwd(), options.output);
    fs.mkdirSync(path.dirname(outputPath), { recursive: true });
    fs.writeFileSync(outputPath, output);
    console.log(`Generated: ${outputPath}`);
  } else {
    console.log(output);
  }
}

main();
````



---

## `scripts/html-token-validator.py`

````python
#!/usr/bin/env python3
"""
HTML Design Token Validator
Ensures all HTML assets (slides, infographics, etc.) use design tokens.
Source of truth: assets/design-tokens.css

Usage:
  python html-token-validator.py                    # Validate all HTML assets
  python html-token-validator.py --type slides      # Validate only slides
  python html-token-validator.py --type infographics # Validate only infographics
  python html-token-validator.py path/to/file.html  # Validate specific file
  python html-token-validator.py --fix              # Auto-fix issues (WIP)
"""

import re
import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# The skill can be installed outside the project it operates on (user-level
# ~/.claude/skills/, or as a plugin), so the project root cannot be derived from
# this file's location. Resolve it from the working directory instead -- the same
# convention generate-tokens.cjs and validate-tokens.cjs already use via
# process.cwd(). DESIGN_SYSTEM_PROJECT_ROOT overrides it explicitly.
def _find_project_root():
    override = os.environ.get('DESIGN_SYSTEM_PROJECT_ROOT')
    if override:
        return Path(override).resolve()
    start = Path.cwd().resolve()
    markers = (
        Path('assets') / 'design-tokens.json',
        Path('assets') / 'design-tokens.css',
        Path('package.json'),
        Path('.git'),
    )
    for candidate in (start, *start.parents):
        if any((candidate / marker).exists() for marker in markers):
            return candidate
    return start


PROJECT_ROOT = _find_project_root()

# Force UTF-8 on stdout/stderr: this script prints emoji, which raises
# UnicodeEncodeError on a Windows console (cp1252). Same guard as
# src/ui-ux-pro-max/scripts/search.py.
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
TOKENS_JSON_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.json'
TOKENS_CSS_PATH = PROJECT_ROOT / 'assets' / 'design-tokens.css'

# Asset directories to validate
ASSET_DIRS = {
    'slides': PROJECT_ROOT / 'assets' / 'designs' / 'slides',
    'infographics': PROJECT_ROOT / 'assets' / 'infographics',
}

# Patterns that indicate hardcoded values (should use tokens)
FORBIDDEN_PATTERNS = [
    (r'#[0-9A-Fa-f]{3,8}\b', 'hex color'),
    (r'rgb\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)', 'rgb color'),
    (r'rgba\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*[\d.]+\s*\)', 'rgba color'),
    (r'hsl\([^)]+\)', 'hsl color'),
    (r"font-family:\s*'[^v][^a][^r][^']*',", 'hardcoded font'),  # Exclude var()
    (r'font-family:\s*"[^v][^a][^r][^"]*",', 'hardcoded font'),
]

# Allowed rgba patterns (brand colors with transparency - CSS limitation)
# These are derived from brand tokens but need rgba for transparency
ALLOWED_RGBA_PATTERNS = [
    r'rgba\(\s*59\s*,\s*130\s*,\s*246',    # --color-primary (#3B82F6)
    r'rgba\(\s*245\s*,\s*158\s*,\s*11',    # --color-secondary (#F59E0B)
    r'rgba\(\s*16\s*,\s*185\s*,\s*129',    # --color-accent (#10B981)
    r'rgba\(\s*20\s*,\s*184\s*,\s*166',    # --color-accent alt (#14B8A6)
    r'rgba\(\s*0\s*,\s*0\s*,\s*0',         # black transparency (common)
    r'rgba\(\s*255\s*,\s*255\s*,\s*255',   # white transparency (common)
    r'rgba\(\s*15\s*,\s*23\s*,\s*42',      # --color-surface (#0F172A)
    r'rgba\(\s*7\s*,\s*11\s*,\s*20',       # --color-background (#070B14)
]

# Allowed exceptions (external images, etc.)
ALLOWED_EXCEPTIONS = [
    'pexels.com', 'unsplash.com', 'youtube.com', 'ytimg.com',
    'googlefonts', 'fonts.googleapis.com', 'fonts.gstatic.com',
]


class ValidationResult:
    """Validation result for a single file."""
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.passed = True

    def add_error(self, msg: str):
        self.errors.append(msg)
        self.passed = False

    def add_warning(self, msg: str):
        self.warnings.append(msg)


def load_css_variables() -> Dict[str, str]:
    """Load CSS variables from design-tokens.css."""
    variables = {}
    if TOKENS_CSS_PATH.exists():
        content = TOKENS_CSS_PATH.read_text()
        # Extract --var-name: value patterns
        for match in re.finditer(r'(--[\w-]+):\s*([^;]+);', content):
            variables[match.group(1)] = match.group(2).strip()
    return variables


def is_inside_block(content: str, match_pos: int, open_tag: str, close_tag: str) -> bool:
    """Check if position is inside a specific HTML block."""
    pre = content[:match_pos]
    tag_open = pre.rfind(open_tag)
    tag_close = pre.rfind(close_tag)
    return tag_open > tag_close


def is_allowed_exception(context: str) -> bool:
    """Check if the hardcoded value is in an allowed exception context."""
    context_lower = context.lower()
    return any(exc in context_lower for exc in ALLOWED_EXCEPTIONS)


def is_allowed_rgba(match_text: str) -> bool:
    """Check if rgba pattern uses brand colors (allowed for transparency)."""
    return any(re.match(pattern, match_text) for pattern in ALLOWED_RGBA_PATTERNS)


def get_context(content: str, pos: int, chars: int = 100) -> str:
    """Get surrounding context for a match position."""
    start = max(0, pos - chars)
    end = min(len(content), pos + chars)
    return content[start:end]


def validate_html(content: str, file_path: Path, verbose: bool = False) -> ValidationResult:
    """
    Validate HTML content for design token compliance.

    Checks:
    1. design-tokens.css import present
    2. No hardcoded colors in CSS (except in <script> for Chart.js)
    3. No hardcoded fonts
    4. Uses var(--token-name) pattern
    """
    result = ValidationResult(file_path)

    # 1. Check for design-tokens.css import
    if 'design-tokens.css' not in content:
        result.add_error("Missing design-tokens.css import")

    # 2. Check for forbidden patterns in CSS
    for pattern, description in FORBIDDEN_PATTERNS:
        for match in re.finditer(pattern, content):
            match_text = match.group()
            match_pos = match.start()
            context = get_context(content, match_pos)

            # Skip if in <script> block (Chart.js allowed)
            if is_inside_block(content, match_pos, '<script', '</script>'):
                if verbose:
                    result.add_warning(f"Allowed in <script>: {match_text}")
                continue

            # Skip if in allowed exception context (external URLs)
            if is_allowed_exception(context):
                if verbose:
                    result.add_warning(f"Allowed external: {match_text}")
                continue

            # Skip rgba using brand colors (needed for transparency effects)
            if description == 'rgba color' and is_allowed_rgba(match_text):
                if verbose:
                    result.add_warning(f"Allowed brand rgba: {match_text}")
                continue

            # Skip if part of var() reference (false positive)
            if 'var(' in context and match_text in context:
                # Check if it's a fallback value in var()
                var_pattern = rf'var\([^)]*{re.escape(match_text)}[^)]*\)'
                if re.search(var_pattern, context):
                    continue

            # Error if in <style> or inline style
            if is_inside_block(content, match_pos, '<style', '</style>'):
                result.add_error(f"Hardcoded {description} in <style>: {match_text}")
            elif 'style="' in context:
                result.add_error(f"Hardcoded {description} in inline style: {match_text}")

    # 3. Check for required var() usage indicators
    token_patterns = [
        r'var\(--color-',
        r'var\(--primitive-',
        r'var\(--typography-',
        r'var\(--card-',
        r'var\(--button-',
    ]
    token_count = sum(len(re.findall(p, content)) for p in token_patterns)

    if token_count < 5:
        result.add_warning(f"Low token usage ({token_count} var() references). Consider using more design tokens.")

    return result


def validate_file(file_path: Path, verbose: bool = False) -> ValidationResult:
    """Validate a single HTML file."""
    if not file_path.exists():
        result = ValidationResult(file_path)
        result.add_error("File not found")
        return result

    content = file_path.read_text()
    return validate_html(content, file_path, verbose)


def validate_directory(dir_path: Path, verbose: bool = False) -> List[ValidationResult]:
    """Validate all HTML files in a directory."""
    results = []
    if dir_path.exists():
        for html_file in sorted(dir_path.glob('*.html')):
            results.append(validate_file(html_file, verbose))
    return results


def print_result(result: ValidationResult, verbose: bool = False):
    """Print validation result for a file."""
    status = "✓" if result.passed else "✗"
    print(f"  {status} {result.file_path.name}")

    if result.errors:
        for error in result.errors[:5]:  # Limit output
            print(f"      ├─ {error}")
        if len(result.errors) > 5:
            print(f"      └─ ... and {len(result.errors) - 5} more errors")

    if verbose and result.warnings:
        for warning in result.warnings[:3]:
            print(f"      [warn] {warning}")


def print_summary(all_results: Dict[str, List[ValidationResult]]):
    """Print summary of all validation results."""
    total_files = 0
    total_passed = 0
    total_errors = 0

    print("\n" + "=" * 60)
    print("HTML DESIGN TOKEN VALIDATION SUMMARY")
    print("=" * 60)

    for asset_type, results in all_results.items():
        if not results:
            continue

        passed = sum(1 for r in results if r.passed)
        failed = len(results) - passed
        errors = sum(len(r.errors) for r in results)

        total_files += len(results)
        total_passed += passed
        total_errors += errors

        status = "✓" if failed == 0 else "✗"
        print(f"\n{status} {asset_type.upper()}: {passed}/{len(results)} passed")

        for result in results:
            if not result.passed:
                print_result(result)

    print("\n" + "-" * 60)
    if total_errors == 0:
        print(f"✓ ALL PASSED: {total_passed}/{total_files} files valid")
    else:
        print(f"✗ FAILED: {total_files - total_passed}/{total_files} files have issues ({total_errors} total errors)")
    print("-" * 60)

    return total_errors == 0


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate HTML assets for design token compliance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Validate all HTML assets
  %(prog)s --type slides             # Validate only slides
  %(prog)s --type infographics       # Validate only infographics
  %(prog)s path/to/file.html         # Validate specific file
  %(prog)s --colors                  # Show brand colors from tokens
"""
    )
    parser.add_argument('files', nargs='*', help='Specific HTML files to validate')
    parser.add_argument('-t', '--type', choices=['slides', 'infographics', 'all'],
                        default='all', help='Asset type to validate')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show warnings')
    parser.add_argument('--colors', action='store_true', help='Print CSS variables from tokens')
    parser.add_argument('--fix', action='store_true', help='Auto-fix issues (experimental)')

    args = parser.parse_args()

    # Show colors mode
    if args.colors:
        variables = load_css_variables()
        print("\nDesign Tokens (from design-tokens.css):")
        print("-" * 40)
        for name, value in sorted(variables.items())[:30]:
            print(f"  {name}: {value}")
        if len(variables) > 30:
            print(f"  ... and {len(variables) - 30} more")
        return

    all_results: Dict[str, List[ValidationResult]] = {}

    # Validate specific files
    if args.files:
        results = []
        for file_path in args.files:
            path = Path(file_path)
            if path.exists():
                results.append(validate_file(path, args.verbose))
            else:
                result = ValidationResult(path)
                result.add_error("File not found")
                results.append(result)
        all_results['specified'] = results
    else:
        # Validate by type
        types_to_check = ASSET_DIRS.keys() if args.type == 'all' else [args.type]

        for asset_type in types_to_check:
            if asset_type in ASSET_DIRS:
                results = validate_directory(ASSET_DIRS[asset_type], args.verbose)
                all_results[asset_type] = results

    # Print results
    success = print_summary(all_results)

    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
````



---

## `scripts/search-slides.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide Search CLI - Search slide design databases for strategies, layouts, copy, and charts
"""

import sys
import json
import argparse
from slide_search_core import (
    search, search_all, AVAILABLE_DOMAINS,
    search_with_context, get_layout_for_goal, get_typography_for_slide,
    get_color_for_emotion, get_background_config
)

# Force UTF-8 on stdout/stderr: this script prints emoji, which raises
# UnicodeEncodeError on a Windows console (cp1252). Same guard as
# src/ui-ux-pro-max/scripts/search.py.
import io

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_result(result, domain):
    """Format a single search result for display"""
    output = []

    if domain == "strategy":
        output.append(f"**{result.get('strategy_name', 'N/A')}**")
        output.append(f"  Slides: {result.get('slide_count', 'N/A')}")
        output.append(f"  Structure: {result.get('structure', 'N/A')}")
        output.append(f"  Goal: {result.get('goal', 'N/A')}")
        output.append(f"  Audience: {result.get('audience', 'N/A')}")
        output.append(f"  Tone: {result.get('tone', 'N/A')}")
        output.append(f"  Arc: {result.get('narrative_arc', 'N/A')}")
        output.append(f"  Source: {result.get('sources', 'N/A')}")

    elif domain == "layout":
        output.append(f"**{result.get('layout_name', 'N/A')}**")
        output.append(f"  Use case: {result.get('use_case', 'N/A')}")
        output.append(f"  Zones: {result.get('content_zones', 'N/A')}")
        output.append(f"  Visual weight: {result.get('visual_weight', 'N/A')}")
        output.append(f"  CTA: {result.get('cta_placement', 'N/A')}")
        output.append(f"  Recommended: {result.get('recommended_for', 'N/A')}")
        output.append(f"  Avoid: {result.get('avoid_for', 'N/A')}")
        output.append(f"  CSS: {result.get('css_structure', 'N/A')}")

    elif domain == "copy":
        output.append(f"**{result.get('formula_name', 'N/A')}**")
        output.append(f"  Components: {result.get('components', 'N/A')}")
        output.append(f"  Use case: {result.get('use_case', 'N/A')}")
        output.append(f"  Template: {result.get('example_template', 'N/A')}")
        output.append(f"  Emotion: {result.get('emotion_trigger', 'N/A')}")
        output.append(f"  Slide type: {result.get('slide_type', 'N/A')}")
        output.append(f"  Source: {result.get('source', 'N/A')}")

    elif domain == "chart":
        output.append(f"**{result.get('chart_type', 'N/A')}**")
        output.append(f"  Best for: {result.get('best_for', 'N/A')}")
        output.append(f"  Data type: {result.get('data_type', 'N/A')}")
        output.append(f"  When to use: {result.get('when_to_use', 'N/A')}")
        output.append(f"  When to avoid: {result.get('when_to_avoid', 'N/A')}")
        output.append(f"  Max categories: {result.get('max_categories', 'N/A')}")
        output.append(f"  Slide context: {result.get('slide_context', 'N/A')}")
        output.append(f"  CSS: {result.get('css_implementation', 'N/A')}")
        output.append(f"  Accessibility: {result.get('accessibility_notes', 'N/A')}")

    return "\n".join(output)


def format_context(context):
    """Format contextual recommendations for display."""
    output = []
    output.append(f"\n=== CONTEXTUAL RECOMMENDATIONS ===")
    output.append(f"Inferred Goal: {context.get('inferred_goal', 'N/A')}")
    output.append(f"Position: Slide {context.get('slide_position')} of {context.get('total_slides')}")

    if context.get('recommended_layout'):
        output.append(f"\n📐 Layout: {context['recommended_layout']}")
        output.append(f"   Direction: {context.get('layout_direction', 'N/A')}")
        output.append(f"   Visual Weight: {context.get('visual_weight', 'N/A')}")

    if context.get('typography'):
        typo = context['typography']
        output.append(f"\n📝 Typography:")
        output.append(f"   Primary: {typo.get('primary_size', 'N/A')}")
        output.append(f"   Secondary: {typo.get('secondary_size', 'N/A')}")
        output.append(f"   Contrast: {typo.get('weight_contrast', 'N/A')}")

    if context.get('color_treatment'):
        color = context['color_treatment']
        output.append(f"\n🎨 Color Treatment:")
        output.append(f"   Background: {color.get('background', 'N/A')}")
        output.append(f"   Text: {color.get('text_color', 'N/A')}")
        output.append(f"   Accent: {color.get('accent_usage', 'N/A')}")

    if context.get('should_break_pattern'):
        output.append(f"\n⚡ Pattern Break: YES (use contrasting layout)")

    if context.get('should_use_full_bleed'):
        output.append(f"\n🖼️ Full Bleed: Recommended for emotional impact")

    if context.get('use_background_image') and context.get('background'):
        bg = context['background']
        output.append(f"\n📸 Background Image:")
        output.append(f"   Category: {bg.get('image_category', 'N/A')}")
        output.append(f"   Overlay: {bg.get('overlay_style', 'N/A')}")
        output.append(f"   Keywords: {bg.get('search_keywords', 'N/A')}")

    output.append(f"\n✨ Animation: {context.get('animation_class', 'animate-fade-up')}")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Search slide design databases",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  search-slides.py "investor pitch"           # Auto-detect domain (strategy)
  search-slides.py "funnel conversion" -d chart
  search-slides.py "headline hook" -d copy
  search-slides.py "two column" -d layout
  search-slides.py "startup funding" --all    # Search all domains
  search-slides.py "metrics dashboard" --json # JSON output

Contextual Search (Premium System):
  search-slides.py "problem slide" --context --position 2 --total 9
  search-slides.py "cta" --context --position 9 --total 9 --prev-emotion frustration
        """
    )

    parser.add_argument("query", help="Search query")
    parser.add_argument("-d", "--domain", choices=AVAILABLE_DOMAINS,
                        help="Specific domain to search (auto-detected if not specified)")
    parser.add_argument("-n", "--max-results", type=int, default=3,
                        help="Maximum results to return (default: 3)")
    parser.add_argument("--all", action="store_true",
                        help="Search across all domains")
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON")

    # Contextual search options
    parser.add_argument("--context", action="store_true",
                        help="Use contextual search with layout/typography/color recommendations")
    parser.add_argument("--position", type=int, default=1,
                        help="Slide position in deck (1-based, default: 1)")
    parser.add_argument("--total", type=int, default=9,
                        help="Total slides in deck (default: 9)")
    parser.add_argument("--prev-emotion", type=str, default=None,
                        help="Previous slide's emotion for contrast calculation")

    args = parser.parse_args()

    # Contextual search mode
    if args.context:
        result = search_with_context(
            args.query,
            slide_position=args.position,
            total_slides=args.total,
            previous_emotion=args.prev_emotion
        )

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_context(result['context']))

            # Also show base search results
            if result.get('base_results'):
                print("\n\n=== RELATED SEARCH RESULTS ===")
                for domain, data in result['base_results'].items():
                    print(f"\n--- {domain.upper()} ---")
                    for item in data['results']:
                        print(format_result(item, domain))
                        print()
        return

    if args.all:
        results = search_all(args.query, args.max_results)

        if args.json:
            print(json.dumps(results, indent=2))
        else:
            if not results:
                print(f"No results found for: {args.query}")
                return

            for domain, data in results.items():
                print(f"\n=== {domain.upper()} ===")
                print(f"File: {data['file']}")
                print(f"Results: {data['count']}")
                print()
                for result in data['results']:
                    print(format_result(result, domain))
                    print()
    else:
        result = search(args.query, args.domain, args.max_results)

        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result.get("error"):
                print(f"Error: {result['error']}")
                return

            print(f"Domain: {result['domain']}")
            print(f"Query: {result['query']}")
            print(f"File: {result['file']}")
            print(f"Results: {result['count']}")
            print()

            if result['count'] == 0:
                print("No matching results found.")
                return

            for i, item in enumerate(result['results'], 1):
                print(f"--- Result {i} ---")
                print(format_result(item, result['domain']))
                print()


if __name__ == "__main__":
    main()
````



---

## `scripts/slide-token-validator.py`

````python
#!/usr/bin/env python3
"""
Slide Token Validator (Legacy Wrapper)
Now delegates to html-token-validator.py for unified HTML validation.

For new usage, prefer:
  python html-token-validator.py --type slides
  python html-token-validator.py --type infographics
  python html-token-validator.py                       # All HTML assets
"""

import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
UNIFIED_VALIDATOR = SCRIPT_DIR / 'html-token-validator.py'


def main():
    """Delegate to unified html-token-validator.py with --type slides."""
    args = sys.argv[1:]

    # If no files specified, default to slides type
    if not args or all(arg.startswith('-') for arg in args):
        cmd = [sys.executable, str(UNIFIED_VALIDATOR), '--type', 'slides'] + args
    else:
        cmd = [sys.executable, str(UNIFIED_VALIDATOR)] + args

    result = subprocess.run(cmd)
    sys.exit(result.returncode)


if __name__ == '__main__':
    main()
````



---

## `scripts/slide_search_core.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide Search Core - BM25 search engine for slide design databases
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "strategy": {
        "file": "slide-strategies.csv",
        "search_cols": ["strategy_name", "keywords", "goal", "audience", "narrative_arc"],
        "output_cols": ["strategy_name", "keywords", "slide_count", "structure", "goal", "audience", "tone", "narrative_arc", "sources"]
    },
    "layout": {
        "file": "slide-layouts.csv",
        "search_cols": ["layout_name", "keywords", "use_case", "recommended_for"],
        "output_cols": ["layout_name", "keywords", "use_case", "content_zones", "visual_weight", "cta_placement", "recommended_for", "avoid_for", "css_structure"]
    },
    "copy": {
        "file": "slide-copy.csv",
        "search_cols": ["formula_name", "keywords", "use_case", "emotion_trigger", "slide_type"],
        "output_cols": ["formula_name", "keywords", "components", "use_case", "example_template", "emotion_trigger", "slide_type", "source"]
    },
    "chart": {
        "file": "slide-charts.csv",
        "search_cols": ["chart_type", "keywords", "best_for", "when_to_use", "slide_context"],
        "output_cols": ["chart_type", "keywords", "best_for", "data_type", "when_to_use", "when_to_avoid", "max_categories", "slide_context", "css_implementation", "accessibility_notes"]
    }
}

AVAILABLE_DOMAINS = list(CSV_CONFIG.keys())


# ============ BM25 IMPLEMENTATION ============
class BM25:
    """BM25 ranking algorithm for text search"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query):
        """Score all documents against query"""
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using BM25"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Build documents from search columns
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # BM25 search
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Get top results with score > 0
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "strategy": ["pitch", "deck", "investor", "yc", "seed", "series", "demo", "sales", "webinar",
                     "conference", "board", "qbr", "all-hands", "duarte", "kawasaki", "structure"],
        "layout": ["slide", "layout", "grid", "column", "title", "hero", "section", "cta",
                   "screenshot", "quote", "timeline", "comparison", "pricing", "team"],
        "copy": ["headline", "copy", "formula", "aida", "pas", "hook", "cta", "benefit",
                 "objection", "proof", "testimonial", "urgency", "scarcity"],
        "chart": ["chart", "graph", "bar", "line", "pie", "funnel", "metrics", "data",
                  "visualization", "kpi", "trend", "comparison", "heatmap", "gauge"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "strategy"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["strategy"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_all(query, max_results=2):
    """Search across all domains for comprehensive results"""
    all_results = {}

    for domain in AVAILABLE_DOMAINS:
        result = search(query, domain, max_results)
        if result.get("count", 0) > 0:
            all_results[domain] = result

    return all_results


# ============ CONTEXTUAL SEARCH (Premium Slide System) ============

# New CSV configurations for decision system
DECISION_CSV_CONFIG = {
    "layout-logic": {
        "file": "slide-layout-logic.csv",
        "key_col": "goal"
    },
    "typography": {
        "file": "slide-typography.csv",
        "key_col": "content_type"
    },
    "color-logic": {
        "file": "slide-color-logic.csv",
        "key_col": "emotion"
    },
    "backgrounds": {
        "file": "slide-backgrounds.csv",
        "key_col": "slide_type"
    }
}


def _load_decision_csv(csv_type):
    """Load a decision CSV and return as dict keyed by primary column."""
    config = DECISION_CSV_CONFIG.get(csv_type)
    if not config:
        return {}

    filepath = DATA_DIR / config["file"]
    if not filepath.exists():
        return {}

    data = _load_csv(filepath)
    return {row[config["key_col"]]: row for row in data if config["key_col"] in row}


def get_layout_for_goal(goal, previous_emotion=None):
    """
    Get layout recommendation based on slide goal.
    Uses slide-layout-logic.csv for decision.
    """
    layouts = _load_decision_csv("layout-logic")
    row = layouts.get(goal, layouts.get("features", {}))

    result = dict(row) if row else {}

    # Apply pattern-breaking logic
    if result.get("break_pattern") == "true" and previous_emotion:
        result["_pattern_break"] = True
        result["_contrast_with"] = previous_emotion

    return result


def get_typography_for_slide(slide_type, has_metrics=False, has_quote=False):
    """
    Get typography recommendation based on slide content.
    Uses slide-typography.csv for decision.
    """
    typography = _load_decision_csv("typography")

    if has_metrics:
        return typography.get("metric-callout", {})
    if has_quote:
        return typography.get("quote-block", {})

    # Map slide types to typography
    type_map = {
        "hero": "hero-statement",
        "hook": "hero-statement",
        "title": "title-only",
        "problem": "subtitle-heavy",
        "agitation": "metric-callout",
        "solution": "subtitle-heavy",
        "features": "feature-grid",
        "proof": "metric-callout",
        "traction": "data-insight",
        "social": "quote-block",
        "testimonial": "testimonial",
        "pricing": "pricing",
        "team": "team",
        "cta": "cta-action",
        "comparison": "comparison",
        "timeline": "timeline",
    }

    content_type = type_map.get(slide_type, "feature-grid")
    return typography.get(content_type, {})


def get_color_for_emotion(emotion):
    """
    Get color treatment based on emotional beat.
    Uses slide-color-logic.csv for decision.
    """
    colors = _load_decision_csv("color-logic")
    return colors.get(emotion, colors.get("clarity", {}))


def get_background_config(slide_type):
    """
    Get background image configuration.
    Uses slide-backgrounds.csv for decision.
    """
    backgrounds = _load_decision_csv("backgrounds")
    return backgrounds.get(slide_type, {})


def should_use_full_bleed(slide_index, total_slides, emotion):
    """
    Determine if slide should use full-bleed background.
    Premium decks use 2-3 full-bleed slides strategically.

    Rules:
    1. Never consecutive full-bleed
    2. One in first third, one in middle, one at end
    3. Reserved for high-emotion beats (hope, urgency, fear)
    """
    high_emotion_beats = ["hope", "urgency", "fear", "curiosity"]

    if emotion not in high_emotion_beats:
        return False

    if total_slides < 3:
        return False

    third = total_slides // 3
    strategic_positions = [1, third, third * 2, total_slides - 1]

    return slide_index in strategic_positions


def calculate_pattern_break(slide_index, total_slides, previous_emotion=None):
    """
    Determine if this slide should break the visual pattern.
    Used for emotional contrast (Duarte Sparkline technique).
    """
    # Pattern breaks at strategic positions
    if total_slides < 5:
        return False

    # Break at 1/3 and 2/3 points
    third = total_slides // 3
    if slide_index in [third, third * 2]:
        return True

    # Break when switching between frustration and hope
    contrasting_emotions = {
        "frustration": ["hope", "relief"],
        "hope": ["frustration", "fear"],
        "fear": ["hope", "relief"],
    }

    if previous_emotion in contrasting_emotions:
        return True

    return False


def search_with_context(query, slide_position=1, total_slides=9, previous_emotion=None):
    """
    Enhanced search that considers deck context.

    Args:
        query: Search query
        slide_position: Current slide index (1-based)
        total_slides: Total slides in deck
        previous_emotion: Emotion of previous slide (for contrast)

    Returns:
        Search results enriched with contextual recommendations
    """
    # Get base results from existing BM25 search
    base_results = search_all(query, max_results=2)

    # Detect likely slide goal from query
    goal = detect_domain(query.lower())
    if "problem" in query.lower():
        goal = "problem"
    elif "solution" in query.lower():
        goal = "solution"
    elif "cta" in query.lower() or "call to action" in query.lower():
        goal = "cta"
    elif "hook" in query.lower() or "title" in query.lower():
        goal = "hook"
    elif "traction" in query.lower() or "metric" in query.lower():
        goal = "traction"

    # Enrich with contextual recommendations
    context = {
        "slide_position": slide_position,
        "total_slides": total_slides,
        "previous_emotion": previous_emotion,
        "inferred_goal": goal,
    }

    # Get layout recommendation
    layout = get_layout_for_goal(goal, previous_emotion)
    if layout:
        context["recommended_layout"] = layout.get("layout_pattern")
        context["layout_direction"] = layout.get("direction")
        context["visual_weight"] = layout.get("visual_weight")
        context["use_background_image"] = layout.get("use_bg_image") == "true"

    # Get typography recommendation
    typography = get_typography_for_slide(goal)
    if typography:
        context["typography"] = {
            "primary_size": typography.get("primary_size"),
            "secondary_size": typography.get("secondary_size"),
            "weight_contrast": typography.get("weight_contrast"),
        }

    # Get color treatment
    emotion = layout.get("emotion", "clarity") if layout else "clarity"
    color = get_color_for_emotion(emotion)
    if color:
        context["color_treatment"] = {
            "background": color.get("background"),
            "text_color": color.get("text_color"),
            "accent_usage": color.get("accent_usage"),
            "card_style": color.get("card_style"),
        }

    # Calculate pattern breaking
    context["should_break_pattern"] = calculate_pattern_break(
        slide_position, total_slides, previous_emotion
    )
    context["should_use_full_bleed"] = should_use_full_bleed(
        slide_position, total_slides, emotion
    )

    # Get background config if needed
    if context.get("use_background_image"):
        bg_config = get_background_config(goal)
        if bg_config:
            context["background"] = {
                "image_category": bg_config.get("image_category"),
                "overlay_style": bg_config.get("overlay_style"),
                "search_keywords": bg_config.get("search_keywords"),
            }

    # Suggested animation classes
    animation_map = {
        "hook": "animate-fade-up",
        "problem": "animate-fade-up",
        "agitation": "animate-count animate-stagger",
        "solution": "animate-scale",
        "features": "animate-stagger",
        "traction": "animate-chart animate-count",
        "proof": "animate-stagger-scale",
        "social": "animate-fade-up",
        "cta": "animate-pulse",
    }
    context["animation_class"] = animation_map.get(goal, "animate-fade-up")

    return {
        "query": query,
        "context": context,
        "base_results": base_results,
    }
````



---

## `scripts/validate-tokens.cjs`

````js
#!/usr/bin/env node
/**
 * Validate token usage in codebase
 * Finds hardcoded values that should use design tokens
 *
 * Usage:
 *   node validate-tokens.cjs --dir src/
 *   node validate-tokens.cjs --dir src/ --fix
 */

const fs = require('fs');
const path = require('path');

/**
 * Parse command line arguments
 */
function parseArgs() {
  const args = process.argv.slice(2);
  const options = {
    dir: null,
    fix: false,
    ignore: ['node_modules', '.git', 'dist', 'build', '.next']
  };

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--dir' || args[i] === '-d') {
      options.dir = args[++i];
    } else if (args[i] === '--fix') {
      options.fix = true;
    } else if (args[i] === '--ignore' || args[i] === '-i') {
      options.ignore.push(args[++i]);
    } else if (args[i] === '--help' || args[i] === '-h') {
      console.log(`
Usage: node validate-tokens.cjs [options]

Options:
  -d, --dir <path>      Directory to scan (required)
  --fix                 Show suggested fixes (no auto-fix)
  -i, --ignore <dir>    Additional directories to ignore
  -h, --help            Show this help

Checks for:
  - Hardcoded hex colors (#RGB, #RRGGBB)
  - Hardcoded pixel values (except 0, 1px)
  - Hardcoded rem values in CSS
      `);
      process.exit(0);
    }
  }

  return options;
}

/**
 * Patterns to detect hardcoded values
 */
const patterns = {
  hexColor: {
    regex: /#([0-9A-Fa-f]{3}){1,2}\b/g,
    message: 'Hardcoded hex color',
    suggestion: 'Use var(--color-*) token'
  },
  rgbColor: {
    regex: /rgb\s*\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\)/gi,
    message: 'Hardcoded RGB color',
    suggestion: 'Use var(--color-*) token'
  },
  pixelValue: {
    regex: /:\s*(\d{2,})px/g, // 2+ digit px values
    message: 'Hardcoded pixel value',
    suggestion: 'Use var(--space-*) or var(--radius-*) token'
  },
  remValue: {
    regex: /:\s*\d+\.?\d*rem(?![^{]*\$value)/g, // rem not in token definition
    message: 'Hardcoded rem value',
    suggestion: 'Use var(--space-*) or var(--font-size-*) token'
  }
};

/**
 * File extensions to scan
 */
const extensions = ['.css', '.scss', '.tsx', '.jsx', '.ts', '.js', '.vue', '.svelte'];

/**
 * Files/patterns to skip
 */
const skipPatterns = [
  /\.min\.(css|js)$/,
  /tailwind\.config/,
  /globals\.css/, // Token definitions
  /tokens\.(css|json)/
];

/**
 * Get all files recursively
 */
function getFiles(dir, ignore, files = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      if (!ignore.includes(entry.name)) {
        getFiles(fullPath, ignore, files);
      }
    } else if (entry.isFile()) {
      const ext = path.extname(entry.name);
      if (extensions.includes(ext)) {
        files.push(fullPath);
      }
    }
  }

  return files;
}

/**
 * Check if file should be skipped
 */
function shouldSkip(filePath) {
  return skipPatterns.some(pattern => pattern.test(filePath));
}

/**
 * Scan file for violations
 */
function scanFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf-8');
  const lines = content.split('\n');
  const violations = [];

  lines.forEach((line, index) => {
    // Skip comments
    if (line.trim().startsWith('//') || line.trim().startsWith('/*')) {
      return;
    }

    for (const [name, pattern] of Object.entries(patterns)) {
      const matches = line.match(pattern.regex);
      if (matches) {
        matches.forEach(match => {
          // Skip common exceptions
          if (name === 'hexColor' && ['#000', '#fff', '#FFF', '#000000', '#FFFFFF'].includes(match.toUpperCase())) {
            return; // Skip black/white, often intentional
          }

          violations.push({
            file: filePath,
            line: index + 1,
            column: line.indexOf(match) + 1,
            value: match,
            type: name,
            message: pattern.message,
            suggestion: pattern.suggestion,
            context: line.trim().substring(0, 80)
          });
        });
      }
    }
  });

  return violations;
}

/**
 * Format violation report
 */
function formatReport(violations) {
  if (violations.length === 0) {
    return '✅ No token violations found';
  }

  let report = `⚠️  Found ${violations.length} potential token violations:\n\n`;

  // Group by file
  const byFile = {};
  violations.forEach(v => {
    if (!byFile[v.file]) byFile[v.file] = [];
    byFile[v.file].push(v);
  });

  for (const [file, fileViolations] of Object.entries(byFile)) {
    report += `📁 ${file}\n`;
    fileViolations.forEach(v => {
      report += `   Line ${v.line}: ${v.message}\n`;
      report += `   Found: ${v.value}\n`;
      report += `   Suggestion: ${v.suggestion}\n`;
      report += `   Context: ${v.context}\n\n`;
    });
  }

  // Summary
  const byType = {};
  violations.forEach(v => {
    byType[v.type] = (byType[v.type] || 0) + 1;
  });

  report += `\n📊 Summary:\n`;
  for (const [type, count] of Object.entries(byType)) {
    report += `   ${patterns[type].message}: ${count}\n`;
  }

  return report;
}

/**
 * Main
 */
function main() {
  const options = parseArgs();

  if (!options.dir) {
    console.error('Error: --dir is required');
    process.exit(1);
  }

  const dirPath = path.resolve(process.cwd(), options.dir);

  if (!fs.existsSync(dirPath)) {
    console.error(`Error: Directory not found: ${dirPath}`);
    process.exit(1);
  }

  console.log(`Scanning ${dirPath} for token violations...\n`);

  const files = getFiles(dirPath, options.ignore);
  const allViolations = [];

  for (const file of files) {
    if (shouldSkip(file)) continue;

    const violations = scanFile(file);
    allViolations.push(...violations);
  }

  console.log(formatReport(allViolations));

  // Exit with error code if violations found
  if (allViolations.length > 0) {
    process.exit(1);
  }
}

main();
````



---

## `templates/design-tokens-starter.json`

````json
{
  "$schema": "https://design-tokens.org/schema.json",
  "primitive": {
    "color": {
      "gray": {
        "50": { "$value": "#F9FAFB", "$type": "color" },
        "100": { "$value": "#F3F4F6", "$type": "color" },
        "200": { "$value": "#E5E7EB", "$type": "color" },
        "300": { "$value": "#D1D5DB", "$type": "color" },
        "400": { "$value": "#9CA3AF", "$type": "color" },
        "500": { "$value": "#6B7280", "$type": "color" },
        "600": { "$value": "#4B5563", "$type": "color" },
        "700": { "$value": "#374151", "$type": "color" },
        "800": { "$value": "#1F2937", "$type": "color" },
        "900": { "$value": "#111827", "$type": "color" },
        "950": { "$value": "#030712", "$type": "color" }
      },
      "blue": {
        "50": { "$value": "#EFF6FF", "$type": "color" },
        "500": { "$value": "#3B82F6", "$type": "color" },
        "600": { "$value": "#2563EB", "$type": "color" },
        "700": { "$value": "#1D4ED8", "$type": "color" },
        "800": { "$value": "#1E40AF", "$type": "color" }
      },
      "red": {
        "500": { "$value": "#EF4444", "$type": "color" },
        "600": { "$value": "#DC2626", "$type": "color" },
        "700": { "$value": "#B91C1C", "$type": "color" }
      },
      "green": {
        "500": { "$value": "#22C55E", "$type": "color" },
        "600": { "$value": "#16A34A", "$type": "color" }
      },
      "yellow": {
        "500": { "$value": "#EAB308", "$type": "color" }
      },
      "white": { "$value": "#FFFFFF", "$type": "color" }
    },
    "spacing": {
      "0": { "$value": "0", "$type": "dimension" },
      "1": { "$value": "0.25rem", "$type": "dimension" },
      "2": { "$value": "0.5rem", "$type": "dimension" },
      "3": { "$value": "0.75rem", "$type": "dimension" },
      "4": { "$value": "1rem", "$type": "dimension" },
      "5": { "$value": "1.25rem", "$type": "dimension" },
      "6": { "$value": "1.5rem", "$type": "dimension" },
      "8": { "$value": "2rem", "$type": "dimension" },
      "10": { "$value": "2.5rem", "$type": "dimension" },
      "12": { "$value": "3rem", "$type": "dimension" },
      "16": { "$value": "4rem", "$type": "dimension" }
    },
    "fontSize": {
      "xs": { "$value": "0.75rem", "$type": "dimension" },
      "sm": { "$value": "0.875rem", "$type": "dimension" },
      "base": { "$value": "1rem", "$type": "dimension" },
      "lg": { "$value": "1.125rem", "$type": "dimension" },
      "xl": { "$value": "1.25rem", "$type": "dimension" },
      "2xl": { "$value": "1.5rem", "$type": "dimension" },
      "3xl": { "$value": "1.875rem", "$type": "dimension" },
      "4xl": { "$value": "2.25rem", "$type": "dimension" }
    },
    "radius": {
      "none": { "$value": "0", "$type": "dimension" },
      "sm": { "$value": "0.125rem", "$type": "dimension" },
      "default": { "$value": "0.25rem", "$type": "dimension" },
      "md": { "$value": "0.375rem", "$type": "dimension" },
      "lg": { "$value": "0.5rem", "$type": "dimension" },
      "xl": { "$value": "0.75rem", "$type": "dimension" },
      "full": { "$value": "9999px", "$type": "dimension" }
    },
    "shadow": {
      "none": { "$value": "none", "$type": "shadow" },
      "sm": { "$value": "0 1px 2px 0 rgb(0 0 0 / 0.05)", "$type": "shadow" },
      "default": { "$value": "0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)", "$type": "shadow" },
      "md": { "$value": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)", "$type": "shadow" },
      "lg": { "$value": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)", "$type": "shadow" }
    },
    "duration": {
      "fast": { "$value": "150ms", "$type": "duration" },
      "normal": { "$value": "200ms", "$type": "duration" },
      "slow": { "$value": "300ms", "$type": "duration" }
    }
  },
  "semantic": {
    "color": {
      "background": { "$value": "{primitive.color.gray.50}", "$type": "color" },
      "foreground": { "$value": "{primitive.color.gray.900}", "$type": "color" },
      "primary": { "$value": "{primitive.color.blue.600}", "$type": "color" },
      "primary-hover": { "$value": "{primitive.color.blue.700}", "$type": "color" },
      "primary-foreground": { "$value": "{primitive.color.white}", "$type": "color" },
      "secondary": { "$value": "{primitive.color.gray.100}", "$type": "color" },
      "secondary-foreground": { "$value": "{primitive.color.gray.900}", "$type": "color" },
      "muted": { "$value": "{primitive.color.gray.100}", "$type": "color" },
      "muted-foreground": { "$value": "{primitive.color.gray.500}", "$type": "color" },
      "destructive": { "$value": "{primitive.color.red.600}", "$type": "color" },
      "destructive-foreground": { "$value": "{primitive.color.white}", "$type": "color" },
      "border": { "$value": "{primitive.color.gray.200}", "$type": "color" },
      "ring": { "$value": "{primitive.color.blue.500}", "$type": "color" }
    },
    "spacing": {
      "component": { "$value": "{primitive.spacing.4}", "$type": "dimension" },
      "section": { "$value": "{primitive.spacing.12}", "$type": "dimension" }
    }
  },
  "component": {
    "button": {
      "bg": { "$value": "{semantic.color.primary}", "$type": "color" },
      "fg": { "$value": "{semantic.color.primary-foreground}", "$type": "color" },
      "hover-bg": { "$value": "{semantic.color.primary-hover}", "$type": "color" },
      "padding-x": { "$value": "{primitive.spacing.4}", "$type": "dimension" },
      "padding-y": { "$value": "{primitive.spacing.2}", "$type": "dimension" },
      "radius": { "$value": "{primitive.radius.md}", "$type": "dimension" },
      "font-size": { "$value": "{primitive.fontSize.sm}", "$type": "dimension" }
    },
    "input": {
      "bg": { "$value": "{semantic.color.background}", "$type": "color" },
      "border": { "$value": "{semantic.color.border}", "$type": "color" },
      "focus-ring": { "$value": "{semantic.color.ring}", "$type": "color" },
      "padding-x": { "$value": "{primitive.spacing.3}", "$type": "dimension" },
      "padding-y": { "$value": "{primitive.spacing.2}", "$type": "dimension" },
      "radius": { "$value": "{primitive.radius.md}", "$type": "dimension" }
    },
    "card": {
      "bg": { "$value": "{primitive.color.white}", "$type": "color" },
      "border": { "$value": "{semantic.color.border}", "$type": "color" },
      "shadow": { "$value": "{primitive.shadow.default}", "$type": "shadow" },
      "padding": { "$value": "{primitive.spacing.6}", "$type": "dimension" },
      "radius": { "$value": "{primitive.radius.lg}", "$type": "dimension" }
    }
  },
  "dark": {
    "semantic": {
      "color": {
        "background": { "$value": "{primitive.color.gray.950}", "$type": "color" },
        "foreground": { "$value": "{primitive.color.gray.50}", "$type": "color" },
        "secondary": { "$value": "{primitive.color.gray.800}", "$type": "color" },
        "muted": { "$value": "{primitive.color.gray.800}", "$type": "color" },
        "muted-foreground": { "$value": "{primitive.color.gray.400}", "$type": "color" },
        "border": { "$value": "{primitive.color.gray.800}", "$type": "color" }
      }
    }
  }
}
````
