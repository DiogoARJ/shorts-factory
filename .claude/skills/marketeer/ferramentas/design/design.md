# design

Original: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/b7d5353/.claude/skills/design

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corporate identity program (50 deliverables, CIP mockups), HTML presentations (Chart.js), banner design (22 styles, social/ads/web/print), icon design (15 styles, SVG, Gemini 3.1 Pro), social photos (HTML→screenshot, multi-platform). Actions: design logo, create CIP, generate mockups, build slides, design banner, generate icon, create social photos, social media images, brand identity, design system. Platforms: Facebook, Twitter, LinkedIn, YouTube, Instagram, Pinterest, TikTok, Threads, Google Ads.


# Design

Unified design skill: brand, tokens, UI, logo, CIP, slides, banners, social photos, icons.

## When to Use

- Brand identity, voice, assets
- Design system tokens and specs
- UI styling with shadcn/ui + Tailwind
- Logo design and AI generation
- Corporate identity program (CIP) deliverables
- Presentations and pitch decks
- Banner design for social media, ads, web, print
- Social photos for Instagram, Facebook, LinkedIn, Twitter, Pinterest, TikTok

## Sub-skill Routing

| Task | Sub-skill | Details |
|------|-----------|---------|
| Brand identity, voice, assets | `brand` | Bundled sibling skill |
| Tokens, specs, CSS vars | `design-system` | Bundled sibling skill |
| shadcn/ui, Tailwind, code | `ui-styling` | Bundled sibling skill |
| Logo creation, AI generation | Logo (built-in) | `references/logo-design.md` |
| CIP mockups, deliverables | CIP (built-in) | `references/cip-design.md` |
| Presentations, pitch decks | Slides (built-in) | `references/slides.md` |
| Banners, covers, headers | Banner (built-in) | `references/banner-sizes-and-styles.md` |
| Social media images/photos | Social Photos (built-in) | `references/social-photos-design.md` |
| SVG icons, icon sets | Icon (built-in) | `references/icon-design.md` |

## Script Paths

Script paths in this skill and its `references/` are relative to the directory that contains this SKILL.md, not to the project: `scripts/<file>` is this skill's own `scripts/` folder, and `../<skill>/scripts/<file>` is a sibling sub-skill installed alongside it. Build the full path from that directory (Claude Code reports it as the skill's base directory when the skill loads) and keep the working directory at the project root — the scripts read and write project files such as `docs/brand-guidelines.md`, `assets/design-tokens.json` or `src/` relative to it.

## Logo Design (Built-in)

55+ styles, 30 color palettes, 25 industry guides. Gemini Nano Banana, Atlas
Cloud, and MuAPI image generation.

### Logo: Generate Design Brief

```bash
python3 scripts/logo/search.py "tech startup modern" --design-brief -p "BrandName"
```

### Logo: Search Styles/Colors/Industries

```bash
python3 scripts/logo/search.py "minimalist clean" --domain style
python3 scripts/logo/search.py "tech professional" --domain color
python3 scripts/logo/search.py "healthcare medical" --domain industry
```

### Logo: Generate with AI

**ALWAYS** generate output logo images with white background.

```bash
python3 scripts/logo/generate.py --brand "TechFlow" --style minimalist --industry tech
python3 scripts/logo/generate.py --prompt "coffee shop vintage badge" --style vintage
python3 scripts/logo/generate.py --brand "TechFlow" --provider atlas
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi --muapi-model nano-banana-pro
```

**IMPORTANT:** When scripts fail, try to fix them directly.

After generation, **ALWAYS** ask user about HTML preview via `AskUserQuestion`. If yes, use the bundled `ui-ux-pro-max` skill for the gallery.

## CIP Design (Built-in)

50+ deliverables, 20 styles, 20 industries. Gemini Nano Banana (Flash/Pro).

### CIP: Generate Brief

```bash
python3 scripts/cip/search.py "tech startup" --cip-brief -b "BrandName"
```

### CIP: Search Domains

```bash
python3 scripts/cip/search.py "business card letterhead" --domain deliverable
python3 scripts/cip/search.py "luxury premium elegant" --domain style
python3 scripts/cip/search.py "hospitality hotel" --domain industry
python3 scripts/cip/search.py "office reception" --domain mockup
```

### CIP: Generate Mockups

```bash
# With logo (RECOMMENDED)
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card" --industry "consulting"

# Full CIP set
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --industry "consulting" --set

# Pro model (4K text)
python3 scripts/cip/generate.py --brand "TopGroup" --logo logo.png --deliverable "business card" --model pro

# Without logo
python3 scripts/cip/generate.py --brand "TechFlow" --deliverable "business card" --no-logo-prompt
```

Models: `flash` (default, `gemini-2.5-flash-image`), `pro` (`gemini-3-pro-image`). Override the ids with `GEMINI_FLASH_IMAGE_MODEL` / `GEMINI_PRO_IMAGE_MODEL`.

### CIP: Render HTML Presentation

```bash
python3 scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images /path/to/cip-output
```

**Tip:** If no logo exists, use Logo Design section above first.

## Slides (Built-in)

Strategic HTML presentations with Chart.js, design tokens, copywriting formulas.

Load `references/slides-create.md` for the creation workflow.

### Slides: Knowledge Base

| Topic | File |
|-------|------|
| Creation Guide | `references/slides-create.md` |
| Layout Patterns | `references/slides-layout-patterns.md` |
| HTML Template | `references/slides-html-template.md` |
| Copywriting | `references/slides-copywriting-formulas.md` |
| Strategies | `references/slides-strategies.md` |

## Banner Design (Built-in)

22 art direction styles across social, ads, web, print. This workflow needs nothing outside the bundle: `references/banner-sizes-and-styles.md` and the bundled `ui-ux-pro-max` skill for style and palette guidance. Browser research, image generation, and screenshot capture are optional runtime capabilities; when unavailable, use supplied assets, CSS-built visuals, and the runtime's standard preview or capture workflow.

Load `references/banner-sizes-and-styles.md` for complete sizes and styles reference.

### Banner: Workflow

1. **Gather requirements** via `AskUserQuestion` — purpose, platform, content, brand, style, quantity
2. **Research** — Read `references/banner-sizes-and-styles.md` and use the bundled `ui-ux-pro-max` skill for style and palette guidance; if browser research is available and permitted, collect 3–5 references
3. **Design** — Create the HTML/CSS banner at exact platform dimensions; use supplied assets or CSS-built visuals, or an authorized image-generation capability if the runtime provides one
4. **Export** — Capture PNG at exact dimensions with the runtime's browser or screenshot capability; if unavailable, deliver the HTML/CSS source and mark PNG export as pending
5. **Present** — Show all options side-by-side, iterate on feedback

### Banner: Quick Size Reference

| Platform | Type | Size (px) |
|----------|------|-----------|
| Facebook | Cover | 820 x 312 |
| Twitter/X | Header | 1500 x 500 |
| LinkedIn | Personal | 1584 x 396 |
| YouTube | Channel art | 2560 x 1440 |
| Instagram | Story | 1080 x 1920 |
| Instagram | Post | 1080 x 1080 |
| Google Ads | Med Rectangle | 300 x 250 |
| Website | Hero | 1920 x 600-1080 |

### Banner: Top Art Styles

| Style | Best For |
|-------|----------|
| Minimalist | SaaS, tech |
| Bold Typography | Announcements |
| Gradient | Modern brands |
| Photo-Based | Lifestyle, e-com |
| Geometric | Tech, fintech |
| Glassmorphism | SaaS, apps |
| Neon/Cyberpunk | Gaming, events |

### Banner: Design Rules

- Safe zones: critical content in central 70-80%
- One CTA per banner, bottom-right, min 44px height
- Max 2 fonts, min 16px body, ≥32px headline
- Text under 20% for ads (Meta penalizes)
- Print: 300 DPI, CMYK, 3-5mm bleed

## Icon Design (Built-in)

15 styles, 12 categories. Gemini 3.1 Pro Preview generates SVG text output.

### Icon: Generate Single Icon

```bash
python3 scripts/icon/generate.py --prompt "settings gear" --style outlined
python3 scripts/icon/generate.py --prompt "shopping cart" --style filled --color "#6366F1"
python3 scripts/icon/generate.py --name "dashboard" --category navigation --style duotone
```

### Icon: Generate Batch Variations

```bash
python3 scripts/icon/generate.py --prompt "cloud upload" --batch 4 --output-dir ./icons
```

### Icon: Multi-size Export

```bash
python3 scripts/icon/generate.py --prompt "user profile" --sizes "16,24,32,48" --output-dir ./icons
```

### Icon: Top Styles

| Style | Best For |
|-------|----------|
| outlined | UI interfaces, web apps |
| filled | Mobile apps, nav bars |
| duotone | Marketing, landing pages |
| rounded | Friendly apps, health |
| sharp | Tech, fintech, enterprise |
| flat | Material design, Google-style |
| gradient | Modern brands, SaaS |

**Model:** `gemini-3.1-pro-preview` — text-only output (SVG is XML text). No image generation API needed.

## Social Photos (Built-in)

Multi-platform social image design: HTML/CSS → screenshot export. Uses the bundled `ui-ux-pro-max`, `brand`, and `design-system` skills; screenshot export runs through Chrome headless, Playwright, or Puppeteer (see the reference).

Load `references/social-photos-design.md` for sizes, templates, best practices.

### Social Photos: Workflow

1. **Orchestrate** — Track the steps below with the runtime's native task list; parallel subagents for independent work
2. **Analyze** — Parse prompt: subject, platforms, style, brand context, content elements
3. **Ideate** — 3-5 concepts, present via `AskUserQuestion`
4. **Design** — bundled `brand` → `design-system` → `ui-ux-pro-max` skills; HTML per idea × size
5. **Export** — Chrome headless, Playwright, or Puppeteer screenshot at exact px (2x device scale factor where the tool supports it; see the reference)
6. **Verify** — Open the exported PNGs in an available browser or image viewer and inspect them; fix layout/styling issues and re-export
7. **Report** — Summary to `plans/reports/` with design decisions
8. **Organize** — Sort output files and reports into the project's asset directories

### Social Photos: Key Sizes

| Platform | Size (px) | Platform | Size (px) |
|----------|-----------|----------|-----------|
| IG Post | 1080×1080 | FB Post | 1200×630 |
| IG Story | 1080×1920 | X Post | 1200×675 |
| IG Carousel | 1080×1350 | LinkedIn | 1200×627 |
| YT Thumb | 1280×720 | Pinterest | 1000×1500 |

## Workflows

### Complete Brand Package

1. **Logo** → `scripts/logo/generate.py` → Generate logo variants
2. **CIP** → `scripts/cip/generate.py --logo ...` → Create deliverable mockups
3. **Presentation** → Load `references/slides-create.md` → Build pitch deck

### New Design System

1. **Brand** (brand skill) → Define colors, typography, voice
2. **Tokens** (design-system skill) → Create semantic token layers
3. **Implement** (ui-styling skill) → Configure Tailwind, shadcn/ui

## References

| Topic | File |
|-------|------|
| Design Routing | `references/design-routing.md` |
| Logo Design Guide | `references/logo-design.md` |
| Logo Styles | `references/logo-style-guide.md` |
| Logo Colors | `references/logo-color-psychology.md` |
| Logo Prompts | `references/logo-prompt-engineering.md` |
| CIP Design Guide | `references/cip-design.md` |
| CIP Deliverables | `references/cip-deliverable-guide.md` |
| CIP Styles | `references/cip-style-guide.md` |
| CIP Prompts | `references/cip-prompt-engineering.md` |
| Slides Create | `references/slides-create.md` |
| Slides Layouts | `references/slides-layout-patterns.md` |
| Slides Template | `references/slides-html-template.md` |
| Slides Copy | `references/slides-copywriting-formulas.md` |
| Slides Strategy | `references/slides-strategies.md` |
| Banner Sizes & Styles | `references/banner-sizes-and-styles.md` |
| Social Photos Guide | `references/social-photos-design.md` |
| Icon Design Guide | `references/icon-design.md` |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/logo/search.py` | Search logo styles, colors, industries |
| `scripts/logo/generate.py` | Generate logos with Gemini AI |
| `scripts/logo/core.py` | BM25 search engine for logo data |
| `scripts/cip/search.py` | Search CIP deliverables, styles, industries |
| `scripts/cip/generate.py` | Generate CIP mockups with Gemini |
| `scripts/cip/render-html.py` | Render HTML presentation from CIP mockups |
| `scripts/cip/core.py` | BM25 search engine for CIP data |
| `scripts/icon/generate.py` | Generate SVG icons with Gemini 3.1 Pro |

## Prerequisites

**Python:** This skill uses Python scripts. On Windows, use `python` instead of `python3` (e.g., `python scripts/logo/search.py` instead of `python3 scripts/logo/search.py`).

Check if Python is installed:
```bash
python3 --version || python --version
```

## Setup

```bash
export GEMINI_API_KEY="your-key"  # https://aistudio.google.com/apikey
pip install google-genai pillow

# Optional MuAPI provider (no extra Python package required)
export MUAPI_API_KEY="your-key"
```

MuAPI uses the asynchronous model endpoint and prediction result API. See the
[MuAPI API reference](https://muapi.ai/docs/api-reference) for authentication
and the [nano-banana model contract](https://api.muapi.ai/api/v1/models/nano-banana)
or [nano-banana-pro model contract](https://api.muapi.ai/api/v1/models/nano-banana-pro)
for the current model-specific schemas. The logo generator supports both documented
model slugs and sends their shared required `prompt` plus optional `aspect_ratio`
fields; the Pro model also accepts an optional `resolution` field that this focused
logo workflow leaves at the provider default.

> **Note for Windows:** Use `python` instead of `pip` where needed (e.g., `python -m pip install ...`).

## Integration

**Bundled sub-skills:** brand, design-system, ui-styling
**Related Skills:** ui-ux-pro-max



---

## `data/cip/deliverables.csv`

````csv
No,Deliverable,Category,Keywords,Description,Dimensions,File Format,Logo Placement,Color Usage,Typography Notes,Mockup Context,Best Practices,Avoid
1,Primary Logo,Core Identity,logo main primary brand mark,Main logo used as primary brand identifier,Vector scalable,SVG AI EPS PNG,Center prominent,Full color palette,Primary typeface,Clean background product shots,Ensure clear space maintain proportions,Distortion crowding busy backgrounds
2,Logo Variations,Core Identity,logo alternate secondary horizontal vertical,Alternative logo formats for different applications,Vector scalable,SVG AI EPS PNG,Context dependent,Mono color reverse,Consistent with primary,Various application contexts,Create horizontal vertical stacked icon versions,Inconsistent modifications unauthorized changes
3,Business Card,Stationery,namecard card contact professional,Professional contact card with brand identity,3.5x2 inches 85x55mm,PDF AI print-ready,Front center or corner,Primary secondary colors,Name title contact details,Marble wood desk surface,Premium paper stock spot UV foil,Cluttered design too many fonts cheap paper
4,Letterhead,Stationery,letter paper document official,Branded document paper for official correspondence,A4 Letter size,PDF AI Word template,Top header or corner,Subtle brand colors,Body text headers,Flat lay with pen envelope,Consistent margins proper hierarchy,Overpowering logo excessive graphics
5,Envelope,Stationery,envelope mail correspondence,Branded envelopes for business mail,DL C4 C5 sizes,PDF AI print-ready,Flap or front corner,Primary brand color,Return address company name,Stacked with letterhead cards,Match letterhead design system,Misaligned printing poor paper quality
6,Folder,Stationery,folder presentation document holder,Presentation folder for documents,A4 Letter pocket folder,PDF AI die-cut template,Front cover spine,Full brand colors,Company tagline contact,Business documents inside,Pockets die-cuts premium finish,Flimsy material poor construction
7,Notebook,Stationery,notebook journal notepad branded,Branded notebooks for employees or gifts,A5 A6 sizes,Print cover design,Front cover emboss,Cover in brand colors,Logo minimal text,Desk flat lay with pen,Quality binding emboss or deboss,Cheap paper poor binding
8,Pen,Promotional,pen writing instrument promo,Branded pens for promotional use,Standard pen dimensions,Vector for print,Barrel clip,Limited color 1-2,Logo only or tagline,Product shot lifestyle,Quality mechanism smooth writing,Cheap mechanism poor print
9,ID Badge,Security Access,badge identification employee pass,Employee identification and access card,CR80 86x54mm,PDF AI template,Center or top,Photo area brand colors,Name department title,Lanyard neck office setting,Clear photo area security features,Poor photo quality cluttered design
10,Lanyard,Security Access,lanyard neck strap badge holder,Neck strap for ID badges,20-25mm width,Vector repeat pattern,Continuous pattern,Primary brand color,Logo repeated or continuous,Worn with badge professional,Quality material comfortable width,Scratchy material cheap clips
11,Access Card,Security Access,key card rfid access control,Electronic access control card,CR80 standard,PDF AI template,One side or both,Minimal brand colors,Card number access level,Security context door reader,Functional design clear hierarchy,Security info visible cluttered
12,Reception Signage,Office Environment,lobby reception wall sign 3D,Main reception area brand signage,Custom based on wall,3D fabrication files,Center of wall,Backlit or dimensional,Logo only or with tagline,Modern office lobby interior,Backlit LED brushed metal acrylic,Poor lighting cheap materials dim
13,Wayfinding Signage,Office Environment,directional signs navigation office,Interior navigation and directional signs,Various sizes,AI vector templates,Consistent placement,Secondary palette,Clear readable fonts,Hallway corridor office,Consistent system clear hierarchy,Inconsistent styles poor visibility
14,Meeting Room Signs,Office Environment,conference room name plate door,Meeting room identification signs,A5 A6 custom,AI templates,Center or left,Accent colors,Room name capacity,Glass door or wall mounted,Digital or static consistent style,Hard to read small text
15,Wall Graphics,Office Environment,mural wall art brand values,Large scale wall murals and graphics,Wall dimensions,Large format print,Full wall coverage,Full palette gradients,Mission values quotes,Open office space,Inspiring messaging quality install,Peeling edges poor resolution
16,Window Graphics,Office Environment,glass frosted privacy film,Frosted or printed window graphics,Window dimensions,Vector cut files,Privacy zones branding,Frosted with logo,Minimal text,Glass partitions entrance,Privacy function brand presence,Blocking natural light cluttered
17,Desk Accessories,Office Environment,desk organizer mousepad coaster,Branded desk items for employees,Various sizes,Print-ready files,Product surface,Subtle branding,Logo tagline,Desktop lifestyle shot,Useful quality materials,Purely decorative poor quality
18,Polo Shirt,Apparel,polo uniform employee clothing,Branded polo shirts for staff,S M L XL XXL,Embroidery vector,Left chest back,Garment brand colors,Logo small embroidered,Folded or worn lifestyle,Quality fabric embroidery,Cheap fabric poor embroidery
19,T-Shirt,Apparel,tshirt casual staff event,Casual branded t-shirts,S M L XL XXL,Screen print vector,Center chest back,Limited colors 1-3,Logo tagline graphic,Flat lay or worn model,Quality cotton proper sizing,Cheap material design too large
20,Cap Hat,Apparel,cap hat headwear baseball,Branded caps and hats,One size adjustable,Embroidery vector,Front center,1-2 colors embroidery,Logo small,Product shot worn,Quality embroidery structured cap,Cheap construction poor embroidery
21,Jacket,Apparel,jacket outerwear coat uniform,Branded jackets for outdoor staff,S M L XL XXL,Embroidery vector,Left chest back,Garment brand colors,Logo department,Lifestyle outdoor shot,Quality material practical design,Impractical poor quality
22,Apron,Apparel,apron uniform service hospitality,Branded aprons for service staff,Standard adjustable,Screen print embroidery,Center chest,Workwear colors,Logo business name,Hospitality setting,Durable material functional pockets,Poor material impractical design
23,Tote Bag,Promotional,bag shopping eco reusable,Branded reusable shopping bags,Various sizes,Screen print vector,Center both sides,1-2 colors typically,Logo tagline,Lifestyle shopping context,Quality canvas sturdy handles,Cheap material weak handles
24,Paper Bag,Promotional,shopping bag retail paper,Retail paper shopping bags,Small medium large,Print template,Side and front,Full color or kraft,Logo website,Retail product context,Quality paper rope or ribbon handles,Cheap paper weak handles
25,Gift Box,Promotional,packaging box gift premium,Premium gift packaging boxes,Various sizes,Die-cut templates,Lid or all sides,Brand colors patterns,Logo minimal text,Unboxing product shot,Quality board magnetic closure,Cheap cardboard poor construction
26,USB Drive,Promotional,flash drive storage tech promo,Branded USB flash drives,Standard USB size,Print area template,Drive surface,Limited 1-2 colors,Logo only,Product shot tech context,Quality drive sufficient storage,Cheap mechanism low storage
27,Water Bottle,Promotional,bottle drink drinkware hydration,Branded water bottles,500ml 750ml 1L,Print wrap template,Wrap or pad print,Bottle brand colors,Logo tagline,Lifestyle fitness outdoor,Quality insulated BPA-free,Cheap plastic leaking poor insulation
28,Mug Cup,Promotional,mug cup drinkware coffee,Branded mugs and cups,Standard 11oz 15oz,Sublimation vector,Wrap or one side,Full color sublimation,Logo tagline graphic,Lifestyle office desk,Quality ceramic dishwasher safe,Cheap material poor print durability
29,Umbrella,Promotional,umbrella rain promotional,Branded umbrellas,Standard compact golf,Panel print template,Panels or handle,Limited panel colors,Logo repeated,Lifestyle rainy weather,Quality mechanism wind resistant,Cheap mechanism breaks easily
30,Car Sedan,Vehicle,company car sedan branding,Sedan vehicle branding wrap,Vehicle template,Vehicle wrap template,Doors hood trunk,Partial or full wrap,Logo contact URL,Side angle motion blur,Professional installation quality vinyl,Amateur install bubbles peeling
31,Van,Vehicle,delivery van transport branding,Van and delivery vehicle branding,Vehicle template,Vehicle wrap template,All sides back,Bold visible colors,Logo contact services,Street delivery context,Maximum visibility contact info,Cluttered hard to read
32,Truck,Vehicle,truck lorry freight branding,Large truck and lorry branding,Vehicle template,Large format wrap,Sides rear trailer,High contrast visible,Logo contact large scale,Highway road context,High visibility fleet consistency,Inconsistent fleet poor visibility
33,Social Media Profile,Digital,avatar profile picture social,Social media profile pictures,Various platform sizes,PNG JPG optimized,Center crop safe,Simplified for small,Logo icon only,Platform context preview,Recognizable at small size,Too detailed loses clarity
34,Social Media Cover,Digital,banner cover header social,Social media cover and header images,Platform specific sizes,PNG JPG optimized,Safe zone placement,Full brand expression,Tagline campaign message,Platform context preview,Platform-specific safe zones,Text in unsafe crop zones
35,Email Signature,Digital,email signature footer contact,Professional email signature,600px max width,HTML responsive,Left aligned,Limited colors web-safe,Name title contact links,Email client preview,Responsive clean links,Images blocked heavy files
36,Website Favicon,Digital,favicon browser icon tab,Browser tab icon,16x16 32x32 ICO,ICO PNG SVG,Centered square,Simplified colors,Icon only,Browser tab context,Recognizable at tiny size,Too complex loses form
37,PowerPoint Template,Digital,presentation slides deck,Branded presentation templates,16:9 4:3 widescreen,PPTX template,Footer header title,Full brand system,Heading body fonts,Presentation meeting context,Master slides consistent layouts,Inconsistent slides poor hierarchy
38,Document Template,Digital,word document letterhead template,Branded document templates,A4 Letter,DOCX template,Header footer,Subtle consistent,Body heading styles,Document printed digital,Easy to use consistent,Hard to edit breaks formatting
39,Invoice Template,Digital,invoice billing financial document,Branded invoice templates,A4 Letter,PDF XLSX template,Header corner,Professional minimal,Clear hierarchy amounts,Financial context payment,Clear totals payment details,Confusing layout unclear totals
40,Packaging Box,Product,product box retail package,Product packaging boxes,Product specific,Dieline templates,Principal display panel,Retail appeal,Product name features,Retail shelf context,Stand out shelf appeal,Lost among competitors bland
41,Packaging Label,Product,label sticker product tag,Product labels and stickers,Various sizes,Vector dieline,Product surface,Brand compliant,Product required info,Applied to product,Regulatory compliant appealing,Missing required info poor adhesion
42,Product Tag,Product,hang tag swing tag retail,Hang tags and swing tags,Standard custom sizes,Die-cut template,Front centered,Brand colors,Product price info,Attached to product,Quality card stock string,Cheap card tears easily
43,Retail Display,Product,POP display stand retail,Point of purchase displays,Custom dimensions,Structural design,Display surfaces,Bold attention-getting,Brand product promo,Retail store context,Sturdy eye-catching,Flimsy unstable falls apart
44,Trade Show Booth,Events,exhibition stand booth display,Trade show booth design,10x10 10x20 custom,Large format print,Backdrop walls,Bold visible colors,Company key messages,Exhibition hall context,Professional portable modular,Cheap materials hard to assemble
45,Banner Stand,Events,roll up pull up banner,Retractable banner stands,80x200cm standard,Large format print,Full height center,Bold readable,Key message CTA,Event lobby entrance,Quality print mechanism,Flimsy curling edges poor mechanism
46,Table Cover,Events,tablecloth throw event,Branded table covers,6ft 8ft standard,Fabric print,Front and sides,Full brand expression,Logo tagline contact,Event booth table,Wrinkle-resistant fitted,Wrinkles cheap fabric poor fit
47,Backdrop,Events,media wall step repeat backdrop,Event backdrops and media walls,Custom event size,Large format print,Repeat pattern logo,Limited colors works on camera,Logo repeated pattern,Event photo opportunity,Photo-friendly repeat pattern,Random placement looks awkward
48,Name Badge Event,Events,event badge conference delegate,Event name badges,CR80 custom sizes,Template design,Top with logo,Event brand colors,Name company title,Conference event context,Clear name large enough,Name too small hard to read
49,Lanyard Event,Events,event lanyard conference sponsor,Event branded lanyards,20-25mm width,Repeat pattern,Continuous or repeat,Event sponsor colors,Event name sponsors,Worn at event,Quality material sponsor visibility,Scratchy poor print quality
50,Certificate,Documents,certificate award achievement,Achievement and recognition certificates,A4 Letter,Print template,Top header,Gold premium accents,Achievement details,Framed or presented,Premium paper emboss seal,Cheap paper looks unofficial
````



---

## `data/cip/industries.csv`

````csv
No,Industry,Keywords,CIP Style,Primary Colors,Secondary Colors,Typography,Key Deliverables,Mood,Best Practices,Avoid
1,Technology,tech software saas startup digital,Modern Tech Geometric,#6366F1 #0EA5E9 #10B981,#8B5CF6 #F8FAFC,Geometric sans modern,Business cards office signage digital templates vehicle,Innovative forward-thinking,Clean lines digital-first responsive,Dated fonts clip art overly complex
2,Finance Banking,bank finance investment wealth,Corporate Minimal Classic,#003366 #1E3A8A #D4AF37,#0F766E #F8FAFC,Traditional serif modern sans,Premium stationery office signage certificates,Trustworthy established,Conservative premium materials security,Trendy effects casual playful
3,Legal,law firm attorney legal services,Classic Traditional,#0F172A #1E3A8A #D4AF37,#713F12 #F5F5F4,Serif traditional professional,Letterhead certificates folders office,Authoritative trustworthy,Traditional balanced symmetrical,Playful colors casual fonts
4,Healthcare,medical hospital clinic wellness,Fresh Modern Minimal,#0077B6 #10B981 #FFFFFF,#0891B2 #F0FDF4,Clean professional sans,Staff uniforms ID badges signage,Caring professional clean,Calming colors simple shapes,Red aggressive clinical harsh
5,Real Estate,property housing development agency,Corporate Minimal Fresh,#0F766E #1E3A8A #D4AF37,#0369A1 #F8FAFC,Clean professional sans,Signage vehicle branding folders,Professional trustworthy,Premium materials quality finish,Cheap materials trendy effects
6,Hospitality,hotel resort restaurant hospitality,Luxury Premium Elegant,#D4AF37 #0F172A #FFFFFF,#8B4513 #FAFAF9,Elegant serif script,Uniforms stationery room signage,Welcoming luxurious,Consistent guest experience,Inconsistent cheap materials
7,Food Beverage,restaurant cafe food service,Warm Organic Vintage,#DC2626 #F97316 #8B4513,#CA8A04 #DEB887,Friendly script bold sans,Uniforms packaging signage menus,Appetizing inviting,Warm colors friendly appeal,Cold clinical sterile
8,Fashion,clothing apparel luxury brand,Luxury Premium Monochrome,#000000 #FFFFFF #D4AF37,#44403C #F5F5F5,Elegant serif thin sans,Shopping bags packaging tags,Sophisticated elegant,Minimal premium refined,Trendy clipart cheap materials
9,Beauty Cosmetics,skincare makeup salon spa,Soft Elegant,#F472B6 #D4AF37 #FFFFFF,#FDA4AF #FDF2F8,Elegant script thin sans,Packaging uniforms salon signage,Elegant feminine,Soft premium quality,Harsh masculine industrial
10,Education,school university learning,Fresh Modern Classic,#4F46E5 #059669 #FFFFFF,#7C3AED #F0FDF4,Clear readable professional,Certificates ID badges signage stationery,Trustworthy growth,Clear readable balanced,Overly playful unprofessional
11,Sports Fitness,gym athletic sports club,Bold Dynamic,#DC2626 #F97316 #000000,#FBBF24 #FFFFFF,Bold condensed strong,Uniforms gym signage merchandise,Energetic powerful,Bold dynamic movement,Weak passive static
12,Entertainment,music events media gaming,Bold Dynamic Gradient,#7C3AED #EC4899 #F59E0B,#06B6D4 #FFFFFF,Bold display creative,Event materials merchandise promotional,Exciting dynamic,Vibrant unique memorable,Conservative boring static
13,Automotive,car dealership service repair,Bold Dynamic Industrial,#DC2626 #1E3A8A #000000,#F97316 #FFFFFF,Bold modern sans,Vehicle branding uniforms signage,Powerful reliable,Strong clean professional,Weak delicate feminine
14,Construction,building contractor development,Industrial Bold,#F97316 #334155 #FFFFFF,#CA8A04 #1F2937,Strong bold sans,Vehicles signage uniforms safety gear,Strong reliable,Bold simple recognizable,Delicate complex trendy
15,Agriculture,farm organic produce natural,Warm Organic Natural,#228B22 #8B4513 #DEB887,#22C55E #F5F5DC,Organic friendly readable,Packaging vehicles signage,Natural sustainable,Earth tones organic materials,Industrial cold synthetic
16,Non-Profit,charity organization foundation,Fresh Modern Warm,#0891B2 #10B981 #F97316,#F472B6 #FFFFFF,Clear readable warm,Stationery event materials certificates,Caring hopeful,Clear message warm colors,Corporate cold complex
17,Consulting,business strategy management,Corporate Minimal Swiss,#0F172A #3B82F6 #FFFFFF,#10B981 #F8FAFC,Professional clean sans,Premium stationery presentations,Professional expert,Clean simple professional,Playful casual complex
18,Retail,shop store marketplace,Fresh Modern Playful,#6366F1 #F97316 #10B981,#EC4899 #FFFFFF,Modern friendly sans,Shopping bags signage uniforms,Modern friendly,Simple memorable scalable,Complex dated traditional
19,Manufacturing,factory production industrial,Industrial Raw Bold,#374151 #F97316 #FFFFFF,#1F2937 #D6D3D1,Strong bold condensed,Vehicle branding uniforms signage safety,Strong reliable industrial,Durable visible functional,Delicate decorative impractical
20,Logistics,shipping transport freight,Bold Dynamic Corporate,#0369A1 #F97316 #FFFFFF,#1E3A8A #F8FAFC,Bold modern sans,Fleet vehicles uniforms ID badges,Efficient reliable,Clear visible scalable fleet,Inconsistent fleet hard to read
````



---

## `data/cip/mockup-contexts.csv`

````csv
No,Context Name,Category,Keywords,Scene Description,Lighting,Environment,Props,Camera Angle,Background,Style Notes,Best For,Prompt Modifiers
1,Marble Desk,Stationery,marble luxury desk surface premium,Business cards on white marble desk surface,Soft natural daylight,Minimalist desk setup,Pen plant small decor,45 degree overhead,White grey marble veins,Clean shadows soft edges,Business cards letterhead,photorealistic soft shadows luxury
2,Wooden Table,Stationery,wood natural warm rustic table,Stationery items on warm wooden table,Warm natural light,Cozy workspace,Coffee cup notebook,Flat lay overhead,Warm wood grain texture,Natural warm tones,Notebooks folders organic brands,warm tones natural textures
3,Concrete Surface,Modern,concrete industrial urban minimalist,Items on raw concrete surface,Dramatic directional,Industrial minimal,Minimal geometric,Direct overhead,Grey concrete texture,High contrast dramatic,Tech modern industrial brands,dramatic lighting industrial minimal
4,Dark Background,Premium,dark moody black sophisticated,Items floating on dark background,Dramatic rim light,Studio dark,None minimal,Product centered,Deep black gradient,Dramatic luxurious,Luxury premium dark brands,dramatic rim lighting luxury
5,White Studio,Clean,white clean studio bright minimal,Clean studio shot white background,Bright even lighting,White infinity curve,None clean,Product centered,Pure white seamless,Clean professional,All brands product focused,clean white professional studio
6,Office Lobby,Environment,reception lobby corporate office,Reception area with brand signage,Bright modern office,Modern office interior,Plants furniture,Wide architectural,Glass wood modern materials,Architectural modern,Office signage reception,architectural photography modern office
7,Meeting Room,Environment,conference meeting corporate glass,Meeting room with brand elements,Natural window light,Modern glass walls,Conference table chairs,Interior wide angle,Glass partitions wood,Contemporary professional,Meeting room signs presentations,corporate interior photography
8,Retail Store,Environment,shop retail display store,Retail environment with branded elements,Bright retail lighting,Modern retail space,Displays products,Interior wide,Modern retail fixtures,Retail contemporary,Shopping bags displays retail,retail interior photography
9,Street Scene,Vehicle,urban street city car,Vehicle on urban street,Daylight golden hour,City street scene,Buildings pedestrians,3/4 front angle,Urban architecture,Dynamic urban,Vehicle branding fleet,urban photography dynamic
10,Parking Lot,Vehicle,parking corporate lot fleet,Fleet vehicles in parking,Overcast soft light,Corporate parking,Multiple vehicles,Wide establishing,Modern building,Fleet organized,Fleet multiple vehicles,fleet photography corporate
11,Highway Motion,Vehicle,road highway motion blur,Vehicle in motion on highway,Daylight clear,Highway motion,Road markings blur,Side tracking shot,Blurred background motion,Dynamic speed,Vehicle branding dynamic,motion photography speed
12,Trade Show,Events,exhibition booth event show,Trade show booth setup,Bright exhibition,Convention center,Displays banners,Wide booth view,Exhibition hall,Professional event,Booth banners displays,exhibition photography trade show
13,Conference,Events,conference event professional,Conference event setup,Stage lighting,Conference venue,Podium screens,Wide room view,Professional venue,Professional formal,Backdrops badges lanyards,event photography conference
14,Outdoor Event,Events,outdoor festival event brand,Outdoor event with brand presence,Natural daylight,Outdoor venue,Tents flags banners,Wide establishing,Sky outdoor space,Fresh dynamic,Outdoor banners flags tents,outdoor event photography
15,Lifestyle Desk,Digital,workspace laptop desk lifestyle,Modern workspace with digital devices,Soft natural light,Modern workspace,Laptop phone notebook,Overhead angle,Clean desk surface,Lifestyle modern,Digital mockups social media,lifestyle photography workspace
16,Hand Holding,Product,hand holding product lifestyle,Hand holding branded item,Soft natural light,Neutral environment,Human hand product,Close-up detail,Blurred background,Human connection,Business cards products,lifestyle product photography
17,Flat Lay,Product,flat lay arranged organized,Organized flat lay arrangement,Even overhead light,Neutral surface,Multiple items arranged,Direct overhead,Clean surface,Organized aesthetic,Multiple items stationery,flat lay photography arranged
18,Unboxing,Product,unboxing packaging reveal,Package opening reveal moment,Soft directional,Clean surface,Packaging tissue,Overhead angle,Neutral background,Premium reveal,Gift boxes packaging,unboxing photography premium
19,Fashion Model,Apparel,model wearing fashion lifestyle,Model wearing branded apparel,Fashion lighting,Studio or location,Model styling,Fashion portrait,Clean or contextual,Fashion lifestyle,Uniforms apparel clothing,fashion photography lifestyle
20,Product Grid,Catalog,grid multiple products organized,Multiple products organized grid,Even lighting,White background,Multiple items,Direct overhead,Pure white,Catalog clean,Multiple variations colors,catalog photography grid
````



---

## `data/cip/styles.csv`

````csv
No,Style Name,Category,Keywords,Description,Primary Colors,Secondary Colors,Typography,Materials,Finishes,Mood,Best For,Avoid For
1,Corporate Minimal,Professional,minimal clean corporate professional,Clean minimal corporate aesthetics with restrained color use,#0F172A #1E3A8A #FFFFFF,#64748B #E2E8F0,Sans-serif geometric clean,Premium paper quality materials,Matte spot UV,Professional trustworthy,Finance legal consulting tech,Playful consumer youth brands
2,Modern Tech,Professional,tech modern digital startup,Contemporary tech-forward visual identity,#6366F1 #8B5CF6 #0EA5E9,#10B981 #F8FAFC,Geometric sans modern,Smooth surfaces metals,Metallic gradients gloss,Innovative forward-thinking,Tech SaaS startups digital,Traditional heritage conservative
3,Luxury Premium,Premium,luxury premium elegant exclusive,High-end sophisticated premium aesthetics,#1C1917 #D4AF37 #FFFFFF,#44403C #FAFAF9,Elegant serif thin sans,Leather metal glass,Gold foil emboss deboss,Prestigious exclusive,Luxury fashion jewelry hotels,Budget mass market casual
4,Classic Traditional,Heritage,classic traditional timeless established,Timeless traditional corporate aesthetics,#0F172A #1E3A8A #D4AF37,#713F12 #F5F5F4,Serif traditional classic,Quality paper leather wood,Emboss letterpress gold,Established trustworthy,Law finance heritage established,Trendy modern startups
5,Fresh Modern,Contemporary,fresh modern contemporary clean,Light fresh contemporary visual style,#10B981 #0EA5E9 #FFFFFF,#22D3EE #F0FDF4,Modern sans-serif rounded,Light materials glass acrylics,Matte clean minimal,Fresh approachable,Wellness tech healthcare green,Heavy industrial traditional
6,Bold Dynamic,Energetic,bold dynamic energetic vibrant,High energy bold visual presence,#DC2626 #F97316 #FBBF24,#000000 #FFFFFF,Bold condensed strong,Strong materials metals,Gloss vibrant finishes,Energetic powerful,Sports entertainment media,Conservative corporate calm
7,Warm Organic,Natural,warm organic natural sustainable,Warm natural organic visual aesthetics,#8B4513 #228B22 #DEB887,#F5F5DC #2F4F4F,Organic serif friendly,Natural materials kraft recycled,Uncoated natural textures,Authentic sustainable,Organic food eco wellness,Tech corporate industrial
8,Soft Elegant,Feminine,soft elegant feminine delicate,Soft elegant feminine visual approach,#F472B6 #D4AF37 #FFFFFF,#FBCFE8 #FDF2F8,Elegant script thin sans,Soft materials quality paper,Rose gold soft touch,Elegant romantic,Beauty wedding fashion spa,Industrial masculine aggressive
9,Dark Premium,Sophisticated,dark premium sophisticated mysterious,Dark sophisticated premium aesthetics,#0F0F0F #1A1A1A #D4AF37,#3D3D3D #FFFFFF,Clean modern bold sans,Dark materials metals glass,Matte metallic accents,Sophisticated mysterious,Nightlife luxury tech fashion,Children medical bright
10,Playful Colorful,Fun,playful colorful fun vibrant,Fun colorful playful visual identity,#F472B6 #FBBF24 #4ADE80,#A78BFA #22D3EE,Rounded friendly bold,Bright materials plastics,Gloss vibrant playful,Fun energetic friendly,Children entertainment gaming,Corporate serious medical
11,Industrial Raw,Industrial,industrial raw urban authentic,Raw industrial urban aesthetics,#374151 #78716C #F97316,#1F2937 #D6D3D1,Strong condensed bold,Raw materials concrete metal,Raw exposed textures,Strong authentic,Manufacturing construction craft,Soft luxury feminine
12,Scandinavian Minimal,Minimal,scandinavian nordic minimal clean,Nordic-inspired minimal clean design,#FFFFFF #F5F5F5 #0F172A,#D4D4D4 #1E3A8A,Clean geometric sans,Light wood white materials,Matte minimal clean,Calm sophisticated clean,Design home wellness nordic,Bold colorful traditional
13,Retro Vintage,Nostalgic,retro vintage nostalgic classic,Nostalgic retro-inspired visual identity,#8B4513 #CA8A04 #DC2626,#2F4F4F #DEB887,Vintage serif script display,Heritage materials aged textures,Letterpress aged effects,Nostalgic authentic,Food beverage craft artisan,Modern tech digital
14,Geometric Modern,Abstract,geometric abstract modern shapes,Contemporary geometric abstract approach,#6366F1 #0EA5E9 #F97316,#10B981 #FFFFFF,Geometric sans modern,Smooth contemporary materials,Clean precise finishes,Modern innovative,Architecture design tech creative,Traditional conservative organic
15,Monochrome Elegant,Sophisticated,monochrome black white elegant,Sophisticated black and white aesthetics,#000000 #FFFFFF #D4AF37,#374151 #F5F5F5,Elegant serif sans contrast,Premium monochrome materials,Matte foil emboss,Sophisticated timeless,Luxury fashion photography,Colorful playful vibrant
16,Gradient Modern,Digital,gradient colorful digital modern,Modern gradient-based visual style,#6366F1 #EC4899 #F97316,#8B5CF6 #22D3EE,Modern geometric sans,Digital smooth surfaces,Glossy gradient effects,Modern dynamic digital,Tech gaming digital media,Traditional print-focused
17,Nature Biophilic,Organic,nature biophilic green organic,Nature-inspired biophilic design approach,#228B22 #8B4513 #0EA5E9,#22C55E #0891B2,Organic friendly readable,Natural sustainable materials,Natural textures matte,Natural calming authentic,Wellness outdoor eco organic,Industrial urban tech
18,Art Deco,Heritage,art deco geometric luxury vintage,Art Deco inspired geometric elegance,#D4AF37 #0F172A #FFFFFF,#8B4513 #1E3A8A,Geometric display serif,Premium metals marble,Gold metallics geometric,Elegant luxurious artistic,Hotels luxury events venues,Casual modern minimal
19,Swiss Minimal,Clean,swiss minimal international clean,Swiss International style minimal design,#FFFFFF #000000 #DC2626,#0F172A #F5F5F5,Helvetica-style sans grid,High quality precision materials,Clean precise matte,Clear precise professional,Corporate architecture design,Decorative ornate playful
20,Memphis Bold,Playful,memphis bold colorful patterns,Memphis-inspired bold colorful patterns,#F472B6 #FBBF24 #4ADE80,#6366F1 #22D3EE,Bold geometric display,Bold colorful materials,Gloss bold patterns,Fun bold creative,Creative entertainment youth,Conservative corporate serious
````



---

## `data/icon/styles.csv`

````csv
id,name,description,stroke_width,fill,best_for,keywords
outlined,Outlined,"Clean stroke-based icons with no fill, open paths",2px,none,"UI interfaces, web apps, dashboards","outline line stroke open clean"
filled,Filled,"Solid filled shapes with no stroke, bold presence",0,solid,"Mobile apps, nav bars, toolbars","solid fill bold flat shape"
duotone,Duotone,"Two-tone layered icons with primary and 30% opacity secondary",0,dual,"Marketing, landing pages, feature sections","two-tone layer opacity dual color"
thin,Thin,"Delicate thin line icons, minimal weight",1-1.5px,none,"Luxury brands, editorial, minimal UI","thin light delicate minimal hairline"
bold,Bold,"Heavy weight icons with thick strokes",3px,none,"Headers, hero sections, emphasis","bold heavy thick strong impactful"
rounded,Rounded,"Rounded line caps and joins, soft corners",2px,none,"Friendly apps, children, health","rounded soft friendly warm approachable"
sharp,Sharp,"Square line caps, mitered joins, precise edges",2px,none,"Tech, fintech, enterprise","sharp angular precise crisp exact"
flat,Flat,"Solid flat fills, no gradients or shadows",0,solid,"Material design, Google-style UI","flat material simple geometric clean"
gradient,Gradient,"Linear or radial gradient fills",0,gradient,"Modern brands, SaaS, creative","gradient color transition vibrant modern"
glassmorphism,Glassmorphism,"Semi-transparent fills simulating frosted glass",1px,semi-transparent,"Modern UI, overlays, cards","glass frosted transparent blur modern"
pixel,Pixel,"Pixel art style on grid, retro 8-bit aesthetic",0,solid,"Gaming, retro, nostalgia","pixel retro 8bit grid blocky"
hand-drawn,Hand-drawn,"Irregular strokes, organic sketch-like feel",varies,none,"Artisan, creative, casual","sketch organic hand drawn artistic"
isometric,Isometric,"3D isometric projection, 30-degree angles",1-2px,partial,"Tech docs, infographics, diagrams","3d isometric dimensional depth"
glyph,Glyph,"Single solid shape, minimal detail, pictogram style",0,solid,"System UI, status bar, compact","glyph pictogram symbol minimal compact"
animated-ready,Animated-ready,"SVG with named groups/IDs for CSS/JS animation",2px,varies,"Interactive UI, onboarding, micro-interactions","animation motion interactive css js"
````



---

## `data/logo/colors.csv`

````csv
No,Palette Name,Category,Keywords,Primary Hex,Secondary Hex,Accent Hex,Background Hex,Text Hex,Psychology,Best For,Avoid For
1,Classic Blue Trust,Professional,"trust, stability, corporate, reliable",#003366,#0055A4,#FFD700,#FFFFFF,#1A1A1A,Trust reliability professionalism,Finance legal healthcare corporate,Entertainment children playful
2,Tech Gradient,Technology,"modern, innovative, digital, future",#6366F1,#8B5CF6,#06B6D4,#0F172A,#F8FAFC,Innovation technology forward-thinking,Tech startups SaaS AI companies,Traditional heritage artisan
3,Eco Green,Nature,"sustainable, natural, growth, fresh",#228B22,#2E8B57,#8FBC8F,#F0FFF0,#1A1A1A,Growth sustainability health nature,Organic eco wellness environmental,Luxury tech industrial
4,Luxury Gold,Premium,"elegance, premium, wealth, sophisticated",#1C1917,#44403C,#D4AF37,#FAFAF9,#0C0A09,Luxury prestige exclusivity wealth,Luxury fashion jewelry hotels,Budget casual children
5,Vibrant Coral,Energetic,"warm, friendly, approachable, exciting",#FF6B6B,#FFE66D,#4ECDC4,#FFFFFF,#2C3E50,Energy warmth friendliness excitement,Food social media lifestyle,Corporate medical serious
6,Modern Purple,Creative,"creative, innovative, unique, premium",#7C3AED,#A78BFA,#F472B6,#FAF5FF,#1E1B4B,Creativity innovation imagination premium,Creative tech beauty brands,Traditional conservative
7,Fresh Mint,Clean,"fresh, clean, calm, modern",#10B981,#34D399,#6EE7B7,#ECFDF5,#064E3B,Freshness calmness cleanliness,Health wellness fintech apps,Industrial heavy traditional
8,Bold Red,Power,"passion, energy, urgency, bold",#DC2626,#EF4444,#F97316,#FEF2F2,#1F2937,Power passion urgency action,Food sports entertainment sale,Healthcare meditation calm
9,Navy Professional,Corporate,"professional, serious, trustworthy, established",#0F172A,#1E3A8A,#3B82F6,#F8FAFC,#020617,Authority trust professionalism,Legal finance consulting,Playful children casual
10,Warm Earth,Organic,"natural, authentic, grounded, warm",#8B4513,#D2691E,#DEB887,#FFF8DC,#2F1810,Authenticity warmth earthiness natural,Coffee craft artisan organic,Tech modern digital
11,Soft Blush,Feminine,"gentle, feminine, romantic, delicate",#F472B6,#FBCFE8,#FDA4AF,#FDF2F8,#831843,Femininity softness romance elegance,Beauty wedding fashion skincare,Industrial tech masculine
12,Electric Neon,Nightlife,"vibrant, exciting, youthful, digital",#FF00FF,#00FFFF,#39FF14,#0D0D0D,#FFFFFF,Energy excitement youth nightlife,Gaming entertainment clubs apps,Corporate traditional mature
13,Sunrise Gradient,Warm,"optimistic, warm, energetic, hopeful",#F97316,#FBBF24,#FCD34D,#FFFBEB,#78350F,Optimism warmth energy hope,Food lifestyle travel,Medical corporate serious
14,Ocean Deep,Calm,"calm, deep, trustworthy, serene",#0077B6,#00B4D8,#90E0EF,#CAF0F8,#023E8A,Calmness depth trust serenity,Wellness travel spa finance,Energy sports aggressive
15,Monochrome Gray,Minimal,"sophisticated, modern, neutral, elegant",#18181B,#3F3F46,#71717A,#FAFAFA,#09090B,Sophistication neutrality elegance,Luxury tech minimal design,Children playful vibrant
16,Forest Natural,Biophilic,"natural, sustainable, outdoors, growth",#14532D,#166534,#22C55E,#F0FDF4,#052E16,Nature growth sustainability,Outdoor eco wellness,Urban industrial digital
17,Candy Pop,Playful,"fun, youthful, colorful, energetic",#F472B6,#A78BFA,#22D3EE,#FFFFFF,#1E1B4B,Fun playfulness youth energy,Children toys games candy,Serious corporate medical
18,Vintage Sepia,Retro,"nostalgic, authentic, heritage, classic",#704214,#A0522D,#D2B48C,#FAF0E6,#3D2914,Nostalgia heritage authenticity,Craft heritage artisan vintage,Modern tech digital
19,Ice Cool,Fresh,"cool, fresh, professional, clean",#0891B2,#22D3EE,#A5F3FC,#ECFEFF,#164E63,Coolness freshness cleanliness,Tech healthcare dental spa,Warm food traditional
20,Sunset Warm,Inviting,"warm, inviting, comfortable, friendly",#EA580C,#F59E0B,#FACC15,#FFFBEB,#431407,Warmth comfort friendliness welcome,Hospitality food home,Medical tech cold
21,Royal Purple,Regal,"regal, creative, luxurious, wise",#581C87,#7C3AED,#C084FC,#FAF5FF,#3B0764,Royalty creativity wisdom luxury,Beauty creative luxury,Budget casual everyday
22,Olive Sage,Calm,"calm, natural, sophisticated, mature",#365314,#4D7C0F,#84CC16,#F7FEE7,#1A2E05,Calm maturity nature sophistication,Wellness food organic beauty,Tech gaming children
23,Cherry Bold,Passionate,"passionate, bold, exciting, romantic",#9F1239,#E11D48,#FB7185,#FFF1F2,#4C0519,Passion boldness romance excitement,Fashion cosmetics food,Corporate healthcare calm
24,Steel Industrial,Strong,"strong, industrial, modern, reliable",#374151,#4B5563,#9CA3AF,#F9FAFB,#111827,Strength reliability industrial modern,Industrial tech automotive,Soft feminine playful
25,Lavender Dream,Soft,"soft, calming, creative, spiritual",#6D28D9,#8B5CF6,#C4B5FD,#F5F3FF,#2E1065,Calm creativity spirituality softness,Wellness beauty spiritual,Industrial sports aggressive
26,Autumn Harvest,Warm,"warm, cozy, natural, seasonal",#9A3412,#C2410C,#EA580C,#FFF7ED,#431407,Warmth coziness natural seasonal,Food craft seasonal,Modern tech clinical
27,Arctic Blue,Cool,"cool, professional, clean, modern",#0C4A6E,#0369A1,#0EA5E9,#F0F9FF,#082F49,Cool professional clean trust,Tech healthcare finance,Warm food cozy
28,Terracotta Earth,Grounded,"grounded, warm, natural, artisan",#7C2D12,#9A3412,#EA580C,#FFF7ED,#431407,Warmth groundedness natural,Home craft pottery,Tech digital modern
29,Midnight Dark,Sophisticated,"sophisticated, luxurious, mysterious, elegant",#0F0F0F,#1A1A1A,#3D3D3D,#000000,#FFFFFF,Sophistication mystery elegance,Luxury fashion tech nightlife,Children medical friendly
30,Pastel Rainbow,Gentle,"gentle, playful, approachable, soft",#FED7AA,#D8B4FE,#A5F3FC,#FFFFFF,#374151,Gentleness playfulness approachability,Children wellness creative,Serious corporate traditional
31,Dark Academia,Moody,"scholarly, vintage, intellectual, mysterious",#0D0D0D,#594636,#4B3E15,#2C3850,#DEB887,Intellectualism mystery heritage sophistication,Education publishing vintage libraries,Children playful bright modern
32,Tiffany Blue,Luxury,"elegant, feminine, luxurious, iconic",#0ABAB5,#81D8D0,#FFFFFF,#F0FFFF,#0F172A,Elegance luxury femininity sophistication,Jewelry luxury fashion wedding,Industrial budget masculine
33,Rose Gold,Feminine,"feminine, luxurious, modern, warm",#B76E79,#E8C4C4,#F4E4E4,#FFF5F5,#4A1C1C,Femininity luxury warmth elegance,Beauty jewelry fashion wedding,Industrial tech masculine
34,Obsidian Dark,Premium,"mysterious, elegant, powerful, sophisticated",#0B1215,#1C2833,#566573,#212F3D,#ECF0F1,Mystery power sophistication elegance,Luxury tech fashion automotive,Children medical friendly
35,Champagne Pink,Soft,"soft, romantic, elegant, feminine",#FDE4CF,#FFCFD2,#F1C0E8,#FBF8CC,#5C4033,Romance softness elegance femininity,Wedding beauty skincare,Industrial tech aggressive
36,Lemon Fresh,Bright,"optimistic, cheerful, fresh, energetic",#FBF8CC,#FFE66D,#98F5E1,#FFFFFF,#334155,Optimism cheerfulness freshness energy,Food wellness children lifestyle,Corporate serious formal
37,Periwinkle Dream,Calm,"calming, creative, dreamy, gentle",#CCCCFF,#B4B4DC,#E6E6FA,#F8F8FF,#2E2E5C,Calmness creativity dreaminess gentleness,Wellness beauty creative spiritual,Industrial aggressive sports
38,Coffee Brew,Warm,"warm, cozy, artisan, authentic",#3C2415,#6F4E37,#A67B5B,#DEB887,#1A0F09,Warmth coziness authenticity artisan,Coffee bakery craft organic,Tech modern cold
39,Marine Navy,Nautical,"trustworthy, nautical, classic, strong",#0C2461,#1B4F72,#2E86AB,#EBF5FB,#0A1628,Trust strength reliability nautical,Maritime finance corporate,Playful warm tropical
40,Mint Chocolate,Fresh,"fresh, indulgent, balanced, appetizing",#98F5E1,#3D2914,#C4A484,#F5FFFA,#1A0F09,Freshness balance indulgence,Food beverage cafe dessert,Corporate serious industrial
41,Coral Sunset,Warm,"warm, inviting, tropical, energetic",#FF6B6B,#FF8E72,#FFA07A,#FFF5EE,#8B2500,Warmth energy vibrancy invitation,Travel hospitality food lifestyle,Corporate cold clinical
42,Dusty Rose,Vintage,"vintage, romantic, sophisticated, muted",#DCAE96,#C9A9A6,#E8D5D5,#FAF5F3,#5C4033,Romance sophistication nostalgia vintage,Fashion beauty interior vintage,Tech modern vibrant
43,Electric Cyan,Modern,"futuristic, energetic, digital, bold",#00FFFF,#00CED1,#20B2AA,#0A1628,#FFFFFF,Energy innovation futurism technology,Tech gaming digital startups,Traditional vintage warm
44,Sage Green,Natural,"calming, natural, sophisticated, organic",#9CAF88,#B2BDA3,#DCE4D3,#F5F5F0,#3D4F39,Calmness nature sophistication organic,Wellness organic home spa,Industrial aggressive bold
45,Burgundy Rich,Luxurious,"luxurious, sophisticated, bold, rich",#722F37,#800020,#A52A2A,#FDF5E6,#2C1810,Luxury sophistication richness boldness,Wine luxury fashion restaurants,Children budget casual
46,Slate Professional,Modern,"professional, modern, neutral, sophisticated",#2F4F4F,#708090,#778899,#F5F5F5,#1C1C1C,Professionalism sophistication neutrality,Corporate tech consulting,Playful children warm
47,Peachy Keen,Friendly,"friendly, approachable, warm, youthful",#FFCBA4,#FFB347,#FFE5B4,#FFFAF0,#8B4513,Friendliness warmth approachability,Food lifestyle social media,Corporate serious formal
48,Nordic Frost,Clean,"clean, minimal, sophisticated, calm",#E8F4F8,#B0C4DE,#87CEEB,#FFFFFF,#2C3E50,Cleanliness minimalism calm sophistication,Scandinavian tech wellness,Warm tropical vibrant
49,Emerald Luxury,Premium,"luxurious, natural, prestigious, rich",#046307,#228B22,#50C878,#F0FFF0,#022002,Luxury nature prestige richness,Luxury eco jewelry finance,Budget casual playful
50,Mauve Elegant,Sophisticated,"sophisticated, feminine, calm, elegant",#E0B0FF,#DDA0DD,#D8BFD8,#FAF0FA,#4A2040,Sophistication femininity calm elegance,Beauty spa fashion interior,Industrial aggressive bold
51,Charcoal Minimal,Sophisticated,"sophisticated, modern, bold, minimal",#36454F,#2F4F4F,#696969,#F8F8F8,#1A1A1A,Sophistication minimalism boldness,Luxury tech fashion architecture,Children playful warm
52,Honey Gold,Warm,"warm, luxurious, natural, inviting",#EB9605,#DAA520,#FFD700,#FFFEF0,#5C4033,Warmth luxury nature invitation,Food luxury organic hospitality,Cold tech clinical
53,Berry Fresh,Vibrant,"vibrant, fresh, energetic, youthful",#8E4585,#C71585,#DA70D6,#FFF0F5,#4A1040,Vibrancy freshness energy youth,Beauty food lifestyle entertainment,Corporate serious traditional
54,Ocean Teal,Calming,"calming, trustworthy, fresh, professional",#008080,#20B2AA,#5F9EA0,#E0FFFF,#0F4C5C,Calmness trust freshness professionalism,Healthcare spa finance wellness,Warm food aggressive
55,Rust Vintage,Warm,"warm, authentic, vintage, earthy",#B7410E,#CD5C5C,#E97451,#FFF8DC,#3C1414,Warmth authenticity vintage earthiness,Craft vintage food artisan,Modern tech cold
````



---

## `data/logo/industries.csv`

````csv
No,Industry,Keywords,Recommended Styles,Primary Colors,Typography,Common Symbols,Mood,Best Practices,Avoid
1,Technology,tech startup saas software app,Minimalist Abstract Mark Gradient Geometric,#6366F1 #0EA5E9 #10B981,Modern sans-serif geometric,Circuit nodes data infinity loop,Innovative forward-thinking modern,Clean lines scalable simple shapes,Overly complex clip art dated fonts
2,Healthcare,medical hospital clinic health wellness,Corporate Professional Minimal Line Art,#0077B6 #00A896 #059669,Clean professional sans-serif,Cross heart pulse human figure caduceus,Trustworthy caring professional,Simple recognizable calming colors,Red (blood) overly clinical aggressive
3,Finance,bank investment fintech insurance,Corporate Emblem Lettermark Wordmark,#003366 #1E3A8A #0F766E,Traditional serif or modern sans,Shield graph growth arrow pillars,Stable trustworthy established,Conservative colors timeless design,Trendy effects casual playful
4,Legal,law firm attorney legal services,Wordmark Emblem Crest Lettermark,#0F172A #1E3A8A #713F12,Serif traditional professional,Scales pillar gavel shield book,Authoritative trustworthy serious,Traditional balanced symmetrical,Playful colors casual fonts
5,Real Estate,property homes housing agency,Combination Mark Wordmark Abstract,#0F766E #0369A1 #334155,Clean professional sans-serif,House roof key door building,Professional trustworthy growth,Simple memorable scalable,Overly detailed houses trendy
6,Food Restaurant,cafe restaurant bakery food service,Vintage Badge Mascot Combination,#DC2626 #F97316 #CA8A04,Friendly script or bold sans,Utensils chef hat food items,Appetizing warm inviting,Warm colors clear readable,Cold colors overly complex
7,Fashion,clothing apparel luxury brand,Wordmark Luxury Monogram Line Art,#000000 #FFFFFF #D4AF37,Elegant serif or thin sans,Abstract marks letters,Sophisticated elegant modern,Minimal timeless refined,Trendy effects dated fonts
8,Beauty Cosmetics,skincare makeup salon spa,Script Wordmark Feminine Organic,#F472B6 #FDA4AF #D4AF37,Elegant script or thin sans,Face lips flower leaf,Elegant feminine luxurious,Soft colors elegant simple,Harsh colors masculine style
9,Education,school university learning edtech,Wordmark Emblem Combination Mark,#4F46E5 #7C3AED #059669,Clear readable professional,Book cap torch owl shield,Trustworthy growth knowledge,Clear readable balanced,Overly playful unprofessional
10,Sports Fitness,gym athletic sports team fitness,Dynamic Mark Bold Abstract Emblem,#DC2626 #F97316 #000000,Bold condensed strong sans,Figure motion lines dumbbell,Energetic powerful dynamic,Bold dynamic movement implied,Weak passive overly complex
11,Entertainment,music gaming events media,Abstract Bold Neon Wordmark,#7C3AED #EC4899 #F59E0B,Bold display experimental,Sound waves stars abstract,Exciting dynamic creative,Vibrant unique memorable,Conservative boring static
12,Automotive,car dealership repair transport,Abstract Emblem Dynamic Mark,#DC2626 #3B82F6 #000000,Bold modern sans-serif,Speed lines wheel car silhouette,Powerful reliable dynamic,Strong clean scalable,Weak delicate complex
13,Construction,building contractor architecture,Bold Emblem Wordmark,#F97316 #CA8A04 #334155,Strong bold sans-serif,Building gear hammer tools,Strong reliable professional,Bold simple recognizable,Delicate complex trendy
14,Agriculture,farm organic produce natural,Organic Hand-Drawn Vintage Badge,#228B22 #8B4513 #DEB887,Organic friendly readable,Leaf plant sun tractor,Natural authentic sustainable,Earth tones organic shapes,Industrial cold synthetic
15,Travel Tourism,hotel airline vacation agency,Wordmark Abstract Combination,#0EA5E9 #F97316 #10B981,Clean modern friendly,Globe plane compass location,Exciting trustworthy adventurous,Vibrant clear memorable,Overly complex small details
16,Pet Care,veterinary pet shop grooming,Mascot Playful Combination,#F97316 #4ADE80 #8B5CF6,Friendly rounded sans-serif,Paw print animal silhouette heart,Friendly caring playful,Warm colors friendly shapes,Cold clinical aggressive
17,Non-Profit,charity organization foundation,Wordmark Combination Emblem,#0891B2 #10B981 #F97316,Clear readable warm,Heart hands globe people,Trustworthy caring hopeful,Clear message warm colors,Corporate cold complex
18,Gaming,esports video games streaming,Bold Neon Abstract Mascot Modern,#7C3AED #EC4899 #06B6D4,Bold display futuristic,Controller joystick abstract shapes,Exciting dynamic immersive,Vibrant unique scalable,Conservative dated boring
19,Photography,studio photographer creative,Wordmark Minimal Line Art,#000000 #FFFFFF #D4AF37,Clean elegant sans or serif,Camera aperture lens frame,Creative professional artistic,Minimal elegant timeless,Clipart trendy effects
20,Consulting,business strategy management,Wordmark Lettermark Corporate,#0F172A #3B82F6 #10B981,Professional clean sans,Abstract marks arrows charts,Professional trustworthy expert,Clean simple professional,Playful casual complex
21,E-commerce,online shop marketplace retail,Modern Abstract Wordmark,#6366F1 #F97316 #10B981,Modern friendly sans-serif,Cart bag arrow abstract,Modern trustworthy easy,Simple memorable scalable,Complex dated traditional
22,Crypto Web3,blockchain defi nft,Gradient Abstract Geometric,#8B5CF6 #06B6D4 #F97316,Modern geometric futuristic,Hexagon chain node abstract,Innovative futuristic secure,Modern unique memorable,Traditional dated conservative
23,Wedding Events,planner venue coordinator,Script Elegant Combination,#D4AF37 #F472B6 #FFFFFF,Elegant script serif,Rings heart flowers,Romantic elegant memorable,Soft elegant refined,Bold harsh industrial
24,Coffee,cafe roaster shop,Vintage Badge Wordmark Hand-Drawn,#8B4513 #2F4F4F #DEB887,Script or vintage serif,Cup beans steam circle badge,Warm artisan authentic,Warm tones heritage feel,Cold clinical modern
25,Brewery,craft beer pub taproom,Vintage Badge Emblem Hand-Drawn,#8B4513 #CA8A04 #2F4F4F,Bold vintage slab serif,Hops barrel mug wheat badge,Authentic craft heritage,Vintage feel craft aesthetic,Corporate clean modern
26,Insurance,insurance protection coverage policy,Corporate Emblem Shield Abstract,#003366 #0077B6 #10B981,Professional clean sans-serif,Shield umbrella hands family house,Trustworthy protective secure,Blue tones stability protection symbols,Playful trendy aggressive red
27,Logistics,shipping transportation freight delivery,Dynamic Abstract Wordmark Bold,#0369A1 #F97316 #1E3A8A,Bold modern sans-serif,Arrow globe truck plane box,Efficient reliable global,Motion arrows connection symbols,Static delicate complex
28,Dental,dentist clinic oral health teeth,Minimal Line Art Professional,#0891B2 #10B981 #0077B6,Clean modern sans-serif,Tooth smile cross sparkle,Clean trustworthy caring,Blue teal simple shapes,Red harsh clinical
29,Cleaning Service,maid housekeeping janitorial residential,Playful Combination Badge Mascot,#0EA5E9 #10B981 #F472B6,Friendly rounded sans-serif,Broom mop sparkle house spray,Fresh clean friendly trustworthy,Bright clean colors sparkle elements,Dark muddy harsh
30,Security,guard protection surveillance alarm,Bold Emblem Shield Corporate,#0F172A #1E3A8A #10B981,Strong bold sans-serif,Shield lock eagle key badge,Strong protective trustworthy,Dark blues greens shields eagles,Playful soft delicate
31,Energy Renewable,solar power wind green sustainable,Modern Abstract Gradient Organic,#22C55E #F97316 #0EA5E9,Clean modern sans-serif,Sun leaf wind turbine lightning,Sustainable innovative clean,Green orange nature elements,Dark industrial polluting
32,Pharmacy,drugstore medical prescription health,Professional Minimal Cross Abstract,#10B981 #0077B6 #059669,Clean professional sans-serif,Cross pill capsule heart mortar,Trustworthy caring health,Green blue teal cross symbols,Red aggressive harsh
33,Childcare,daycare nursery preschool kids,Playful Colorful Mascot Combination,#F472B6 #FBBF24 #4ADE80,Rounded friendly playful,Children tree rainbow hands sun,Warm nurturing playful safe,Bright primary colors friendly shapes,Dark corporate serious
34,Aerospace Aviation,airline airport flight aircraft,Modern Abstract Dynamic Emblem,#1E3A8A #0EA5E9 #FFFFFF,Clean modern geometric sans,Plane wing arrow globe bird,Innovative precise reliable,Blue white clean dynamic shapes,Cluttered heavy grounded
35,Jewelry,jeweler gemstone diamond luxury,Elegant Luxury Monogram Line Art,#D4AF37 #8B5CF6 #F472B6,Elegant serif thin sans,Diamond ring gem crystal hand,Elegant luxurious precious,Gold purple elegant line art,Cheap bold industrial
36,Marine Maritime,ocean shipping nautical boat,Vintage Emblem Badge Bold,#0C4A6E #0891B2 #FFFFFF,Bold serif or strong sans,Anchor ship wheel wave compass,Strong reliable nautical,Navy blue teal white anchors,Landlocked desert dry
37,Accounting,bookkeeping CPA tax financial,Corporate Wordmark Lettermark Minimal,#1E3A8A #10B981 #334155,Professional clean sans-serif,Chart graph calculator checkmark,Professional trustworthy precise,Blue green conservative charts,Playful creative chaotic
38,Music Recording,studio artist label sound,Bold Abstract Neon Dynamic,#7C3AED #EC4899 #F59E0B,Bold display creative,Sound wave note microphone vinyl,Creative energetic expressive,Vibrant unique creative shapes,Conservative corporate bland
39,Architecture,design firm building interior,Minimal Geometric Line Art Abstract,#0F172A #6366F1 #D4AF37,Clean geometric modern sans,Building structure line blueprint,Sophisticated precise creative,Clean lines geometric shapes,Cluttered ornate traditional
40,Hotel Hospitality,resort lodge accommodation lodging,Elegant Wordmark Emblem Combination,#D4AF37 #0F766E #1E3A8A,Elegant serif or modern sans,Bed key building star crown,Welcoming luxurious comfortable,Elegant warm inviting colors,Cold industrial unwelcoming
41,Telecommunications,network mobile phone internet,Modern Abstract Gradient Tech,#6366F1 #0EA5E9 #10B981,Modern geometric sans-serif,Signal wave globe connection node,Connected innovative reliable,Blue gradients tech patterns,Dated heavy disconnected
42,Biotechnology,biotech research lab science,Modern Abstract Minimal Gradient,#10B981 #6366F1 #0891B2,Clean modern scientific sans,DNA helix cell molecule leaf,Innovative precise scientific,Green blue scientific clean,Industrial polluting harsh
43,Cybersecurity,infosec data protection digital,Modern Abstract Shield Tech,#0F172A #6366F1 #10B981,Modern technical sans-serif,Shield lock key binary code,Secure trustworthy technical,Dark blues greens tech elements,Weak exposed vulnerable
44,Interior Design,decorator home staging space,Elegant Minimal Line Art Script,#D4AF37 #8B5CF6 #F472B6,Elegant serif or thin script,Chair lamp house frame,Sophisticated creative stylish,Elegant refined neutral tones,Cluttered cheap industrial
45,Laundry,dry cleaning garment care wash,Friendly Combination Badge Playful,#0EA5E9 #10B981 #F472B6,Friendly rounded sans-serif,Shirt hanger water droplet bubble,Clean fresh convenient,Blue green fresh clean,Dirty muddy harsh
46,Printing,print shop graphics copy,Bold Combination Abstract Modern,#DC2626 #0EA5E9 #F97316,Bold modern sans-serif,Printer paper CMYK drop,Creative professional reliable,Bold CMYK colors print elements,Dull monochrome static
47,Florist,flower shop botanical garden,Organic Script Elegant Hand-Drawn,#F472B6 #10B981 #F97316,Elegant script or organic,Flower leaf petal bouquet,Beautiful natural romantic,Soft natural floral colors,Industrial harsh synthetic
48,Bakery,pastry bread artisan sweets,Vintage Hand-Drawn Badge Script,#8B4513 #F97316 #DEB887,Friendly script or vintage,Wheat bread rolling pin cupcake,Warm artisan homemade,Warm brown cream gold,Cold clinical industrial
49,Landscaping,garden lawn outdoor yard,Organic Bold Combination Badge,#22C55E #8B4513 #0EA5E9,Strong friendly sans-serif,Tree leaf lawn mower sun,Natural professional reliable,Green earth tones natural,Industrial urban concrete
50,Plumbing,pipe repair water fixture,Bold Badge Combination Emblem,#0EA5E9 #F97316 #334155,Strong bold sans-serif,Pipe wrench water drop faucet,Reliable professional skilled,Blue orange professional,Weak delicate dirty
51,Electrical,electrician power wiring contractor,Bold Dynamic Badge Combination,#F97316 #FBBF24 #334155,Strong bold sans-serif,Lightning bolt plug outlet wire,Reliable skilled powerful,Orange yellow electric symbols,Weak dim powerless
52,HVAC,heating cooling ventilation air,Bold Corporate Badge Combination,#0EA5E9 #DC2626 #334155,Strong professional sans-serif,Flame snowflake fan thermometer,Reliable comfortable professional,Blue red temperature symbols,Weak uncomfortable extreme
53,Pest Control,exterminator bug removal service,Bold Badge Combination Mascot,#22C55E #DC2626 #334155,Strong bold sans-serif,Bug shield spray target,Effective reliable protective,Green red action symbols,Weak ineffective infested
54,Moving Relocation,movers packing storage transport,Bold Dynamic Combination Badge,#F97316 #0EA5E9 #334155,Strong friendly sans-serif,Box truck house arrow,Reliable efficient careful,Orange blue movement symbols,Fragile broken scattered
55,Spa Wellness,massage retreat relaxation therapy,Elegant Organic Script Minimal,#0891B2 #10B981 #F472B6,Elegant thin script or sans,Lotus water drop stone bamboo,Calm relaxing rejuvenating,Soft calming natural colors,Harsh loud aggressive
````



---

## `data/logo/styles.csv`

````csv
No,Style Name,Category,Keywords,Primary Colors,Secondary Colors,Typography,Effects,Best For,Avoid For,Complexity,Era
1,Minimalist,General,"clean, simple, essential, whitespace, geometric, modern",#000000 #FFFFFF #F5F5F5,Single accent only,Sans-serif thin weight,"None, sharp edges, high contrast",Tech startups SaaS apps professional services,Playful brands children entertainment,Low,2010s-Present
2,Wordmark,Typography,"logotype, text-only, custom lettering, brand name",Brand-specific,Monochromatic,Custom modified typeface,"Kerning adjustments, ligatures",Established brands name recognition,Complex names visual-heavy industries,Low,Classic
3,Lettermark,Typography,"monogram, initials, abbreviated, compact",Brand-specific usually 2 colors,Minimal accent,Bold geometric sans-serif,"Interlocking letters, negative space",Long company names professional firms,Consumer brands needing recognition,Medium,Classic
4,Pictorial Mark,Symbol,"icon, image, symbol, standalone graphic",Brand-specific,Supporting colors,Paired with wordmark,"Clean lines, scalable shapes",Recognizable brands global companies,Startups unknown brands,Medium,Classic
5,Abstract Mark,Symbol,"geometric, non-representational, unique shape",Bold vibrant colors,Gradient or flat,Modern sans-serif pairing,"Gradients, 3D effects, flat design",Tech companies differentiating brands,Traditional industries,Medium,Modern
6,Mascot,Illustrated,"character, cartoon, friendly, approachable",Warm vibrant palette,Multiple supporting colors,Rounded friendly typeface,"Illustrated, expressions, poses",Food brands sports teams children products,Luxury finance professional services,High,Various
7,Emblem,Badge,"seal, crest, enclosed, official",#1E3A8A #FFD700 #000000,Metallic accents,Serif or gothic typeface,"Banners, shields, circular frame",Universities government traditional brands,Modern tech startups,High,Classic
8,Combination Mark,Hybrid,"icon + text, versatile, complete",Brand-specific,Coordinated palette,Balanced with icon,"Lockup variations, responsive",New brands versatile applications,Simple recognition needs,Medium,Various
9,Vintage/Retro,Aesthetic,"nostalgic, heritage, classic, established",#8B4513 #F5DEB3 #2F4F4F,Muted earth tones,Serif script or slab serif,"Distressed, worn, textured",Craft brands heritage products artisan goods,Modern tech forward brands,Medium,1920s-1970s
10,Art Deco,Aesthetic,"geometric, elegant, 1920s, glamorous",#FFD700 #000000 #1C1C1C,Metallic gold silver,Geometric display typeface,"Sharp angles, symmetry, luxury feel",Luxury hotels fashion high-end products,Budget casual brands,High,1920s-1930s
11,Hand-Drawn,Illustrated,"organic, authentic, imperfect, artisan",Earth tones warm colors,Natural palette,Script or hand-lettered,"Sketched, brush strokes, uneven lines",Artisan products bakeries creative brands,Corporate tech professional,Medium,Timeless
12,Geometric,Modern,"shapes, mathematical, precise, structured",Bold primary colors,Contrasting accent,Geometric sans-serif,"Clean angles, perfect shapes, symmetry",Tech architecture modern brands,Organic natural brands,Low,Modern
13,Gradient,Modern,"color transition, vibrant, dynamic, dimensional",Multi-color spectrum,Smooth transitions,Modern sans-serif,"Color flow, blur effects, 3D depth",Tech apps social media modern brands,Traditional conservative industries,Medium,2015-Present
14,Flat Design,Modern,"2D, solid colors, no shadows, minimal",Bright solid colors,Limited palette 3-4 max,Clean sans-serif,"No gradients, no shadows, simple shapes",Apps websites digital products,Luxury traditional premium,Low,2010s-Present
15,3D/Isometric,Modern,"dimensional, perspective, layered, technical",Cool tech colors,Highlight shadows,Modern geometric,"Depth, shadows, highlights, perspective",Tech gaming architecture firms,Simple classic brands,High,2018-Present
16,Negative Space,Clever,"hidden element, dual meaning, optical illusion",Usually 2 colors max,High contrast pairs,Clean readable font,"Clever cutouts, figure-ground reversal",Creative agencies clever brands,Straightforward industries,Medium,Timeless
17,Line Art,Minimal,"outline, single weight, continuous, elegant",#000000 or single color,Monochromatic,Thin weight sans-serif,"Stroke only, no fills, continuous lines",Fashion beauty boutique brands,Bold energetic brands,Low,Modern
18,Neon/Glow,Aesthetic,"vibrant, electric, nightlife, digital",#FF00FF #00FFFF #39FF14,Dark backgrounds,Bold display typeface,"Glow effect, light emission, bright",Entertainment nightlife gaming,Corporate healthcare traditional,Medium,1980s/Modern
19,Brutalist,Bold,"raw, stark, bold, anti-design",#FF0000 #0000FF #FFFF00 #000000,Primary colors only,Heavy bold sans-serif,"No effects, raw, bold blocks",Art creative counter-culture tech blogs,Conservative corporate healthcare,Low,1950s/2020s Revival
20,Luxury/Premium,Aesthetic,"elegant, sophisticated, high-end, refined",#000000 #FFFFFF #FFD700,Gold silver metallics,Elegant serif thin sans,"Foil, emboss, minimal, premium feel",Fashion jewelry luxury real estate,Budget mass-market casual,Medium,Timeless
21,Playful/Fun,Aesthetic,"colorful, whimsical, energetic, youthful",Rainbow bright palette,Multi-color variety,Rounded bubbly typeface,"Bouncy, irregular, decorative elements",Children brands toys entertainment,Serious finance legal medical,Medium,Various
22,Corporate/Professional,Business,"trustworthy, stable, serious, established",#003366 #666666 #FFFFFF,Conservative blues grays,Clean professional sans,"Subtle, refined, balanced",Financial legal consulting corporate,Creative entertainment youth,Low,Classic
23,Tech/Digital,Industry,"modern, innovative, forward, digital",#0080FF #00D4FF #6366F1,Gradient tech colors,Geometric modern sans,"Circuit, pixel, data visualization",Technology startups software apps,Traditional handmade artisan,Medium,Modern
24,Organic/Natural,Aesthetic,"flowing, nature, sustainable, eco",#228B22 #8B4513 #87CEEB,Earth tones greens,Organic flowing typeface,"Leaf, water, natural textures",Eco brands wellness organic food,Industrial tech urban,Medium,Timeless
25,Swiss/International,Design,"grid-based, rational, clean, functional",#000000 #FFFFFF neutral,Minimal color use,Helvetica style sans-serif,"Grid alignment, mathematical spacing",Corporate design professional,Decorative playful brands,Low,1950s-Present
26,Bauhaus,Design,"geometric, functional, primary colors, modernist",#FF0000 #FFFF00 #0000FF #000000,Primary colors only,Geometric sans-serif,"Circles squares triangles, functional",Architecture design schools modern brands,Traditional ornate decorative,Medium,1920s-1930s
27,Grunge,Aesthetic,"distressed, rough, textured, alternative",Dark muted colors,Earth tones blacks,Distressed or stencil type,"Scratched, worn, dirty textures",Music alternative fashion street brands,Luxury corporate clean,Medium,1990s
28,Watercolor,Artistic,"soft, artistic, fluid, organic",Soft pastel washes,Blended transitions,Script or delicate serif,"Paint bleeding, soft edges, artistic",Art galleries wedding florists beauty,Tech corporate industrial,High,Artistic
29,Monogram Luxury,Typography,"intertwined initials, fashion, heritage",#000000 #FFD700 #FFFFFF,Gold black combinations,Custom serif letterforms,"Interlocking, overlapping, refined",Fashion houses luxury brands hotels,Casual budget consumer,Medium,Classic
30,Vintage Badge,Retro,"circular, heritage, authentic, craft",#8B4513 #2F4F4F #D4AF37,Muted vintage palette,Serif or slab serif,"Banners, stars, established dates",Breweries coffee shops craft brands,Modern minimalist tech,High,1900s-1950s
31,Responsive/Adaptive,Modern,"scalable, flexible, multi-format",Brand-specific,Consistent across sizes,Legible at all sizes,"Multiple lockups, favicon version",Digital-first brands multi-platform,Print-only traditional,Medium,2015-Present
32,Motion-Ready,Digital,"animated, dynamic, kinetic, digital",Vibrant animated-friendly,Colors that transition well,Sans-serif legible in motion,"Designed for animation, morphing shapes",Digital brands apps social media,Static print-only brands,High,2018-Present
33,Duotone,Modern,"two-color, high contrast, bold, graphic",Two contrasting colors,No additional colors,Bold sans-serif,"Two-color overlay, high contrast",Graphic design music modern brands,Multi-color needs complex imagery,Low,2016-Present
34,Split/Fragmented,Experimental,"broken, deconstructed, modern, artistic",Bold contrasting,Highlight fragments,Modern experimental type,"Sliced, separated, glitch-like",Creative agencies art design studios,Conservative traditional corporate,High,2018-Present
35,Outline/Stroke,Minimal,"hollow, transparent, modern, light",Single color or gradient,Background contrast,Matching weight typeface,"Stroke only, no fill, see-through",Fashion tech modern minimal brands,Bold impactful needs,Low,Modern
36,Stamp/Seal,Vintage,"official, authentic, approved, certified",#8B0000 #000080 #006400,Ink-like colors,Bold condensed typeface,"Circular, aged, ink texture",Artisan coffee postal craft brands,Modern digital tech,Medium,Classic
37,Calligraphic,Typography,"flowing, elegant, hand-written, artistic",#000000 gold metallics,Minimal accent colors,Custom calligraphy,"Flourishes, swashes, elegant strokes",Wedding luxury fashion beauty,Tech corporate industrial,High,Timeless
38,Pixel Art,Digital,"8-bit, retro gaming, nostalgic, digital",Bright limited palette,Classic game colors,Pixel or blocky typeface,"Pixelated, grid-based, retro game feel",Gaming retro apps indie games,Luxury professional corporate,Medium,1980s Revival
39,Symmetrical,Balanced,"mirror, balanced, harmonious, stable",Balanced color scheme,Matching halves,Centered balanced type,"Perfect mirror, radial symmetry",Corporate wellness balanced brands,Dynamic energetic brands,Low,Timeless
40,Asymmetrical,Dynamic,"unbalanced, modern, dynamic, interesting",Bold accent placement,Contrasting weights,Off-center experimental,"Intentional imbalance, visual tension",Creative modern art fashion,Traditional stable corporate,Medium,Modern
41,Mascot Modern,Character,"simplified mascot, flat character, friendly",Bright character colors,Supporting brand colors,Rounded friendly sans,"Flat design mascot, simple shapes",Tech apps startups modern food brands,Serious luxury traditional,Medium,2015-Present
42,Monoline,Minimal,"single line weight, consistent, clean",Single color typically,Monochromatic,Matching weight typeface,"Uniform stroke, no weight variation",Coffee shops boutiques craft brands,Bold impactful industrial,Low,Modern
43,Letterform,Typography,"single letter, initial, bold statement",Brand primary color,Background contrast,Custom letter design,"One letter, modified, distinctive",Personal brands design studios agencies,Multi-initial brands corporations,Medium,Classic
44,Wordmark Script,Typography,"handwritten, signature, personal, elegant",#000000 or gold,Minimal supporting,Custom script typeface,"Flowing, connected, signature-like",Fashion designers personal brands,Corporate tech industrial,Medium,Timeless
45,Crest/Heraldic,Traditional,"coat of arms, royal, established, heritage",#1E3A8A #8B0000 #FFD700,Traditional regal colors,Serif blackletter,"Shield, crown, banners, symbols",Universities sports teams luxury brands,Modern casual startups,High,Classic
46,Circular,Shape,"round, infinite, complete, unified",Enclosed palette,Internal colors,Curved or circular type,"Full circle, badge-like, contained",Global brands apps communities,Angular sharp brands,Medium,Timeless
47,Hexagonal,Shape,"modern, tech, honeycomb, structured",Tech-forward colors,Geometric accent,Modern geometric sans,"Six-sided, tessellating, tech feel",Tech blockchain chemical science,Traditional organic natural,Medium,Modern
48,Dynamic Mark,Motion,"movement, speed, progress, forward",Energetic warm colors,Motion blur colors,Italic or forward-leaning,"Motion lines, implied movement",Sports logistics transportation,Static calm wellness,Medium,Modern
49,Eco/Sustainable,Values,"green, sustainable, recycling, earth-friendly",#228B22 #8FBC8F #2E8B57,Natural greens browns,Organic rounded typeface,"Leaf, recycle, earth, natural elements",Eco brands organic sustainable business,Luxury industrial chemical,Medium,2000s-Present
50,Healthcare/Medical,Industry,"trust, care, health, professional",#0077B6 #00A896 #FFFFFF,Calming blues greens,Clean professional sans,"Cross, heart, human figures, care",Hospitals clinics health wellness,Entertainment gaming fashion,Medium,Classic
51,Legal/Financial,Industry,"trust, stability, establishment, serious",#003366 #1E3A8A #4A5568,Navy blue conservative,Traditional serif,"Scales, pillars, shields, professional",Law firms banks financial services,Playful creative casual,Low,Classic
52,Food/Restaurant,Industry,"appetizing, warm, inviting, delicious",#DC2626 #F97316 #CA8A04,Warm appetizing colors,Friendly readable type,"Utensils, chef hat, food imagery",Restaurants cafes food delivery,Tech healthcare professional,Medium,Various
53,Real Estate,Industry,"home, trust, growth, property",#0F766E #0369A1 #000000,Blues greens professional,Clean professional sans,"House, roof, key, door imagery",Property agencies home services,Entertainment gaming tech,Medium,Classic
54,Education,Industry,"knowledge, growth, trust, achievement",#4F46E5 #7C3AED #059669,Blues purples greens,Clear readable typeface,"Book, cap, torch, learning symbols",Schools universities edtech,Entertainment luxury consumer,Medium,Classic
55,Music/Entertainment,Industry,"dynamic, creative, expressive, bold",#7C3AED #EC4899 #F59E0B,Vibrant expressive colors,Bold display typeface,"Sound waves, notes, dynamic shapes",Labels studios streaming venues,Corporate healthcare financial,Medium,Various
````



---

## `references/banner-sizes-and-styles.md`

# Banner Sizes & Art Direction Styles Reference

## Complete Banner Sizes

### Social Media
| Platform | Type | Size (px) | Aspect Ratio |
|----------|------|-----------|--------------|
| Facebook | Cover (desktop) | 820 × 312 | ~2.6:1 |
| Facebook | Cover (mobile) | 640 × 360 | ~16:9 |
| Facebook | Event cover | 1920 × 1080 | 16:9 |
| Twitter/X | Header | 1500 × 500 | 3:1 |
| Twitter/X | Ad banner | 800 × 418 | ~2:1 |
| LinkedIn | Company cover | 1128 × 191 | ~6:1 |
| LinkedIn | Personal banner | 1584 × 396 | 4:1 |
| YouTube | Channel art | 2560 × 1440 | 16:9 |
| YouTube | Safe area | 1546 × 423 | ~3.7:1 |
| Instagram | Stories | 1080 × 1920 | 9:16 |
| Instagram | Post | 1080 × 1080 | 1:1 |
| Pinterest | Pin | 1000 × 1500 | 2:3 |

### Web / Display Ads (Google Display Network)
| Name | Size (px) | Notes |
|------|-----------|-------|
| Medium Rectangle | 300 × 250 | Highest CTR |
| Leaderboard | 728 × 90 | Top of page |
| Wide Skyscraper | 160 × 600 | Sidebar |
| Half Page | 300 × 600 | Premium |
| Large Rectangle | 336 × 280 | High performer |
| Mobile Banner | 320 × 50 | Mobile default |
| Large Mobile | 320 × 100 | Mobile hero |
| Billboard | 970 × 250 | Desktop hero |

### Website
| Type | Size (px) |
|------|-----------|
| Full-width hero | 1920 × 600–1080 |
| Section banner | 1200 × 400 |
| Blog header | 1200 × 628 |
| Email header | 600 × 200 |

### Print
| Type | Size |
|------|------|
| Roll-up | 850mm × 2000mm |
| Step-and-repeat | 8ft × 8ft |
| Vinyl outdoor | 6ft × 3ft |
| Trade show | 33in × 78in |

## 22 Art Direction Styles

1. **Minimalist** — White space dominant, single focal element, 1-2 colors, clean sans-serif
2. **Bold Typography** — Type IS the design; oversized, expressive letterforms fill canvas
3. **Gradient / Color Wash** — Smooth transitions, mesh gradients, chromatic blends
4. **Photo-Based** — Full-bleed photography with text overlay; hero lifestyle imagery
5. **Illustrated / Hand-Drawn** — Custom illustrations, bespoke icons, artisan feel
6. **Geometric / Abstract** — Shapes, lines, grids as primary visual elements
7. **Retro / Vintage** — Distressed textures, muted palettes, serif type, halftone dots
8. **Glassmorphism** — Frosted glass panels, blur backdrop, subtle border glow
9. **3D / Sculptural** — Rendered objects, depth, shadows; product-centric
10. **Neon / Cyberpunk** — Dark backgrounds, glowing neon accents, high contrast
11. **Duotone** — Two-color photo treatment; bold brand color overlay on image
12. **Editorial / Magazine** — Grid-heavy layouts, pull quotes, journalistic composition
13. **Collage / Mixed Media** — Cut-paper textures, photo cutouts, layered elements
14. **Retro Futurism** — Space-age nostalgia, chrome, gradients, optimism
15. **Expressive / Anti-Design** — Chaotic layouts, mixed fonts, deliberate "wrong" composition
16. **Digi-Cute / Kawaii** — Rounded shapes, pastel gradients, pixel art, playful characters
17. **Tactile / Sensory** — Puffy/squishy textures, hyper-real materials, embossed feel
18. **Data / Infographic** — Stats front-and-center, charts, numbers as heroes
19. **Dark Mode / Moody** — Near-black backgrounds, rich jewel tones, high contrast
20. **Flat / Solid Color** — Single background color, clean icons, no gradients
21. **Nature / Organic** — Earthy tones, botanical motifs, sustainable brand feel
22. **Motion-Ready / Kinetic** — Designed for animation; layered elements, loopable

## Design Principles

### Visual Hierarchy (3-Zone Rule)
- **Top**: Logo or main value prop
- **Middle**: Supporting message + visuals
- **Bottom**: CTA (button/QR/URL)

### Safe Zones
- Critical content in central 70-80% of canvas
- Avoid text/CTA within 50-100px of edges
- YouTube: 1546 × 423px safe area inside 2560 × 1440
- Meta/Instagram: central 80% to avoid UI chrome

### CTA Rules
- One CTA per banner
- High contrast vs background
- Bottom-right placement (terminal area)
- Min 44px height for mobile tap targets
- Action verbs: "Get", "Start", "Download", "Claim"

### Typography
- Max 2 typefaces per banner
- Min 16px body, ≥32px headline (digital)
- Min 4.5:1 contrast ratio
- Max 7 words/line, 3 lines for ads

### Text-to-Image Ratio
- Ads: under 20% text (Meta penalizes)
- Social covers: 60/40 image-to-text
- Print: 70pt+ headlines for 3-5m viewing distance

### Print Specs
- 300 DPI minimum (150 DPI for large format)
- 3-5mm bleed all sides
- CMYK color mode
- 1pt per foot viewing distance rule

## Pinterest Research Queries

Use these search queries on Pinterest for art direction references:
- `[purpose] banner design [style]` (e.g., "social media banner minimalist")
- `[platform] cover design inspiration` (e.g., "youtube channel art design")
- `creative banner layout [industry]` (e.g., "creative banner layout tech startup")
- `[style] graphic design 2026` (e.g., "gradient graphic design 2026")
- `banner ad design [product type]` (e.g., "banner ad design saas")



---

## `references/cip-deliverable-guide.md`

# CIP Deliverable Guide

## Core Identity

### Primary Logo
- Vector format (SVG, AI, EPS)
- Clear space rules defined
- Scalable from favicon to billboard

### Logo Variations
- Horizontal, vertical, stacked
- Icon/symbol only
- Monochrome versions (black, white, reversed)

## Stationery Set

### Business Card
- Standard: 3.5x2 inches / 85x55mm
- Premium paper stock (300-400gsm)
- Finishes: matte, spot UV, foil, emboss

### Letterhead
- A4 or Letter size
- Header area for logo/contact
- Digital and print versions

### Envelope
- DL, C4, C5 sizes
- Logo on flap or front
- Return address styling

## Office Environment

### Reception Signage
- 3D dimensional letters
- Backlit LED options
- Materials: acrylic, metal, wood

### Wayfinding System
- Consistent icon system
- Clear hierarchy
- ADA compliance

### Wall Graphics
- Mission/values displays
- Large-scale murals
- Window frosting

## Apparel

### Polo Shirt
- Embroidery preferred
- Left chest placement
- Quality fabric (pique cotton)

### Uniforms
- Department color coding
- Name badge integration
- Safety requirements if applicable

## Vehicle Branding

### Car/Sedan
- Door panel branding
- Partial or full wrap
- Contact information visible

### Fleet Vehicles
- Consistent design across fleet
- High visibility contact details
- Professional installation

## Digital Assets

### Social Media
- Profile pictures (icon version)
- Cover images (platform-specific)
- Post templates

### Email Signature
- HTML responsive
- Max 600px width
- Essential contact only

## Events & Promotional

### Trade Show Booth
- Modular design
- Easy assembly
- Key messaging visible

### Promotional Items
- Quality over quantity
- Useful items preferred
- Brand colors prominent



---

## `references/cip-design.md`

# CIP Design Reference

Corporate Identity Program design with 50+ deliverables, 20 styles, 20 industries. Generate mockups with Gemini Nano Banana (Flash/Pro).

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/cip/search.py` | Search deliverables, styles, industries; generate CIP briefs |
| `scripts/cip/generate.py` | Generate CIP mockups with Gemini (Flash/Pro) |
| `scripts/cip/render-html.py` | Render HTML presentation from CIP mockups |
| `scripts/cip/core.py` | BM25 search engine for CIP data |

## Commands

### CIP Brief (Start Here)

```bash
python3 scripts/cip/search.py "tech startup" --cip-brief -b "BrandName"
```

### Search Domains

```bash
# Deliverables
python3 scripts/cip/search.py "business card letterhead" --domain deliverable

# Design styles
python3 scripts/cip/search.py "luxury premium elegant" --domain style

# Industry guidelines
python3 scripts/cip/search.py "hospitality hotel" --domain industry

# Mockup contexts
python3 scripts/cip/search.py "office reception" --domain mockup
```

### Generate Mockups

```bash
# With logo (RECOMMENDED - uses image editing)
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card" --industry "consulting"

# Full CIP set with logo
python3 scripts/cip/generate.py --brand "TopGroup" --logo /path/to/logo.png --industry "consulting" --set

# Pro model for 4K text rendering
python3 scripts/cip/generate.py --brand "TopGroup" --logo logo.png --deliverable "business card" --model pro

# Custom deliverables with aspect ratio
python3 scripts/cip/generate.py --brand "GreenLeaf" --logo logo.png --industry "organic food" --deliverables "letterhead,packaging,vehicle" --ratio 16:9

# Without logo (AI generates interpretation)
python3 scripts/cip/generate.py --brand "TechFlow" --deliverable "business card" --no-logo-prompt
```

### Render HTML Presentation

```bash
python3 scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images /path/to/cip-output
python3 scripts/cip/render-html.py --brand "TopGroup" --industry "consulting" --images ./topgroup-cip --output presentation.html
```

## Models

- `flash` (default): `gemini-2.5-flash-image` - Fast, cost-effective
- `pro`: `gemini-3-pro-image` - Quality, 4K text rendering

Set `GEMINI_FLASH_IMAGE_MODEL` or `GEMINI_PRO_IMAGE_MODEL` to use another Gemini model id.

## Deliverable Categories

| Category | Items |
|----------|-------|
| Core Identity | Logo, Logo Variations |
| Stationery | Business Card, Letterhead, Envelope, Folder, Notebook, Pen |
| Security/Access | ID Badge, Lanyard, Access Card |
| Office Environment | Reception Signage, Wayfinding, Meeting Room Signs, Wall Graphics |
| Apparel | Polo Shirt, T-Shirt, Cap, Jacket, Apron |
| Promotional | Tote Bag, Gift Box, USB Drive, Water Bottle, Mug, Umbrella |
| Vehicle | Car Sedan, Van, Truck |
| Digital | Social Media, Email Signature, PowerPoint, Document Templates |
| Product | Packaging Box, Labels, Tags, Retail Display |
| Events | Trade Show Booth, Banner Stand, Table Cover, Backdrop |

## Design Styles

| Style | Colors | Best For |
|-------|--------|----------|
| Corporate Minimal | Navy, White, Blue | Finance, Legal, Consulting |
| Modern Tech | Purple, Cyan, Green | Tech, Startups, SaaS |
| Luxury Premium | Black, Gold, White | Fashion, Jewelry, Hotels |
| Warm Organic | Brown, Green, Cream | Food, Organic, Artisan |
| Bold Dynamic | Red, Orange, Black | Sports, Entertainment |

## HTML Presentation Features

- Hero section with brand name, industry, style, mood
- Deliverable cards with mockup images
- Descriptions: concept, purpose, specifications
- Responsive desktop/mobile, dark theme
- Images embedded as base64 (single-file portable)

## Workflow

1. Generate CIP brief → `scripts/cip/search.py --cip-brief`
2. Generate mockups with logo → `scripts/cip/generate.py --brand --logo --industry --set`
3. Render HTML presentation → `scripts/cip/render-html.py --brand --industry --images`

**Tip:** If no logo exists, use Logo Design (built-in) to generate one first.

## Detailed References

- `references/cip-deliverable-guide.md` - Deliverable specifications
- `references/cip-style-guide.md` - Design style descriptions
- `references/cip-prompt-engineering.md` - AI generation prompts

## Setup

```bash
export GEMINI_API_KEY="your-key"
pip install google-genai pillow
```



---

## `references/cip-prompt-engineering.md`

# CIP Mockup Prompt Engineering

## Base Prompt Structure

```
Professional corporate identity mockup photograph showing [DELIVERABLE] for brand '[BRAND_NAME]', [STYLE] design style, using colors [COLORS], [TYPOGRAPHY] typography, logo placement: [PLACEMENT], [MATERIALS] materials with [FINISHES] finish, [CONTEXT] setting, [MOOD] mood, photorealistic product photography, soft natural lighting, high quality professional shot, 8k resolution detailed
```

## Deliverable-Specific Modifiers

### Business Card
```
business card on marble surface, stack of cards, premium paper texture, soft shadows, 45 degree angle
```

### Letterhead
```
letterhead flat lay with envelope and pen, velvet fabric background, brand stationery set, overhead view
```

### Office Signage
```
3D logo signage on office wall, modern lobby interior, backlit LED, brushed metal finish, architectural photography
```

### Vehicle Branding
```
branded vehicle on urban street, 3/4 front angle view, professional car wrap, motion blur background optional
```

### Apparel (Polo/T-Shirt)
```
folded polo shirt on clean background, embroidered logo on chest, premium fabric texture, product photography
```

## Style Modifiers

### Corporate Minimal
```
clean minimal aesthetic, white space, subtle shadows, matte finish, professional
```

### Luxury Premium
```
dark background, dramatic rim lighting, gold accents, premium materials, sophisticated
```

### Modern Tech
```
gradient colors, geometric elements, clean surfaces, futuristic, innovative
```

### Warm Organic
```
natural materials, kraft paper texture, warm lighting, authentic, artisan
```

## Lighting Modifiers

- **Studio:** `professional studio lighting, even illumination`
- **Natural:** `soft natural daylight, window light`
- **Dramatic:** `dramatic rim light, dark background, high contrast`
- **Warm:** `warm golden hour lighting, cozy atmosphere`

## Context Modifiers

- **Marble desk:** `white marble surface, soft shadows, luxury`
- **Wooden table:** `warm wood grain, natural, artisan`
- **Office interior:** `modern office environment, architectural`
- **Flat lay:** `overhead view, organized arrangement`
- **Lifestyle:** `in-use context, human element`

## Quality Modifiers

Always include:
```
photorealistic, professional photography, high quality, 8k resolution, detailed, sharp focus
```

## Negative Prompts (what to avoid)

```
blurry, low quality, distorted text, misspelled, amateur, clipart, cartoon, illustration, watermark
```



---

## `references/cip-style-guide.md`

# CIP Design Style Guide

## Corporate Minimal
**Industries:** Finance, Legal, Consulting, Tech
**Colors:** Navy (#0F172A), White (#FFFFFF), Blue accents
**Typography:** Clean sans-serif (Inter, Helvetica)
**Materials:** Premium matte paper, subtle textures
**Finishes:** Matte, spot UV on logo

## Modern Tech
**Industries:** Tech, SaaS, Startups, AI
**Colors:** Purple (#6366F1), Cyan (#0EA5E9), Green (#10B981)
**Typography:** Geometric sans (Outfit, Poppins)
**Materials:** Smooth surfaces, gradient prints
**Finishes:** Gloss, metallic accents

## Luxury Premium
**Industries:** Fashion, Jewelry, Hotels, Fine Dining
**Colors:** Black (#1C1917), Gold (#D4AF37), White
**Typography:** Elegant serif (Playfair), thin sans
**Materials:** Heavy cotton paper, leather, metal
**Finishes:** Gold foil, emboss, deboss, soft-touch

## Classic Traditional
**Industries:** Law Firms, Heritage Brands, Finance
**Colors:** Navy, Burgundy, Gold
**Typography:** Traditional serif (Times, Garamond)
**Materials:** Quality laid paper, wood
**Finishes:** Letterpress, gold emboss

## Warm Organic
**Industries:** Food, Organic, Wellness, Craft
**Colors:** Brown (#8B4513), Green (#228B22), Cream
**Typography:** Friendly serif, organic script
**Materials:** Kraft paper, recycled materials
**Finishes:** Uncoated, natural textures

## Bold Dynamic
**Industries:** Sports, Entertainment, Gaming
**Colors:** Red (#DC2626), Orange (#F97316), Black
**Typography:** Bold condensed sans
**Materials:** High-contrast, metallic
**Finishes:** Gloss, vibrant colors

## Fresh Modern
**Industries:** Healthcare, Wellness, Fintech
**Colors:** Mint (#10B981), Sky (#0EA5E9), White
**Typography:** Modern rounded sans
**Materials:** Light, clean surfaces
**Finishes:** Matte, clean minimal

## Soft Elegant
**Industries:** Beauty, Wedding, Spa, Fashion
**Colors:** Pink (#F472B6), Gold, White
**Typography:** Elegant script, thin sans
**Materials:** Soft-touch, quality paper
**Finishes:** Rose gold foil, emboss

## Color Psychology

| Color | Meaning | Best Use |
|-------|---------|----------|
| Blue | Trust, stability | Finance, Tech, Healthcare |
| Green | Growth, nature | Eco, Wellness, Organic |
| Gold | Luxury, prestige | Premium, Jewelry |
| Red | Energy, passion | Food, Sports |
| Black | Sophistication | Luxury, Fashion |
| White | Clean, minimal | Tech, Healthcare |



---

## `references/design-routing.md`

# Design Routing Guide

When to use each design sub-skill.

## Skill Overview

| Skill | Purpose | Key Files |
|-------|---------|-----------|
| brand | Brand identity, voice, assets | SKILL.md + 10 references + 3 scripts |
| design-system | Token architecture, specs | SKILL.md + 7 references + 2 scripts |
| ui-styling | Component implementation | SKILL.md + 7 references + 2 scripts |
| logo-design | AI logo generation (55 styles, 30 palettes) | SKILL.md + 4 references + 2 scripts |
| cip-design | Corporate Identity Program (50 deliverables) | SKILL.md + 3 references + 3 scripts |
| slides | HTML presentations with Chart.js | SKILL.md + 4 references |
| banner-design | Banners for social, ads, web, print (22 styles) | SKILL.md + 1 reference |
| icon-design | SVG icon generation (15 styles, Gemini 3.1 Pro) | SKILL.md + 1 reference + 1 script |

## Routing by Task Type

### Brand Identity Tasks
**→ brand**

- Define brand colors and typography
- Create logo usage guidelines
- Establish brand voice and tone
- Organize and validate assets
- Create messaging frameworks
- Audit brand consistency

### Token System Tasks
**→ design-system**

- Create design tokens JSON
- Generate CSS variables
- Define component specifications
- Map tokens to Tailwind config
- Validate token usage in code
- Document state and variants

### Implementation Tasks
**→ ui-styling**

- Add shadcn/ui components
- Style with Tailwind classes
- Implement dark mode
- Create responsive layouts
- Build accessible components

### Logo Design Tasks
**→ logo-design**

- Create logos with AI (Gemini Nano Banana)
- Search logo styles, color palettes, industry guidelines
- Generate design briefs
- Explore 55+ styles (minimalist, vintage, luxury, geometric, etc.)

### Corporate Identity Program Tasks
**→ cip-design**

- Generate CIP deliverables (business cards, letterheads, signage, vehicles, apparel)
- Create CIP briefs with industry/style analysis
- Generate mockups with/without logo (Gemini Flash/Pro)
- Render HTML presentations from CIP mockups

### Presentation Tasks
**→ slides**

- Create strategic HTML presentations
- Data visualization with Chart.js
- Apply copywriting formulas to slide content
- Use layout patterns and design tokens

### Banner Design Tasks
**→ banner-design**

- Design banners for social media (Facebook, Twitter, LinkedIn, YouTube, Instagram)
- Create ad banners (Google Ads, Meta Ads)
- Website hero banners and headers
- Print banners and covers
- 22 art direction styles (minimalist, bold typography, gradient, glassmorphism, etc.)

### Icon Design Tasks
**→ icon-design**

- Generate SVG icons with AI (Gemini 3.1 Pro Preview)
- Batch icon variations in multiple styles
- Multi-size export (16px, 24px, 32px, 48px)
- 15 styles: outlined, filled, duotone, rounded, sharp, gradient, etc.
- 12 categories: navigation, action, communication, media, commerce, data

## Routing by Question Type

| Question | Skill |
|----------|-------|
| "What color should this be?" | brand |
| "How do I create a token for X?" | design-system |
| "How do I build a button component?" | ui-styling |
| "Is this on-brand?" | brand |
| "Should I use a CSS variable here?" | design-system |
| "How do I add dark mode?" | ui-styling |
| "Create a logo for my brand" | logo-design |
| "Generate business card mockups" | cip-design |
| "Create a pitch deck" | slides |
| "Design brand identity package" | cip-design |
| "What logo style fits my industry?" | logo-design |
| "Design a Facebook cover" | banner-design |
| "Create ad banners for Google" | banner-design |
| "Make a website hero banner" | banner-design |
| "Generate a settings icon" | icon-design |
| "Create SVG icons for my app" | icon-design |
| "Design an icon set" | icon-design |

## Multi-Skill Workflows

### New Project Setup

```
1. brand → Define identity
   - Colors, typography, voice

2. design-system → Create tokens
   - Primitive, semantic, component

3. ui-styling → Implement
   - Configure Tailwind, add components
```

### Design System Migration

```
1. brand → Audit existing
   - Extract brand colors, fonts

2. design-system → Formalize tokens
   - Create three-layer architecture

3. ui-styling → Update code
   - Replace hardcoded values
```

### Component Creation

```
1. design-system → Reference specs
   - Button states, sizes, variants

2. ui-styling → Implement
   - Build with shadcn/ui + Tailwind
```

## Skill Dependencies

```
brand
    ↓ (colors, typography)
design-system
    ↓ (tokens, specs)
ui-styling
    ↓ (components)
Application Code
```

## Quick Commands

**Brand:**
```bash
node ../brand/scripts/inject-brand-context.cjs
node ../brand/scripts/validate-asset.cjs <path>
```

**Tokens:**
```bash
node ../design-system/scripts/generate-tokens.cjs -c tokens.json
node ../design-system/scripts/validate-tokens.cjs -d src/
```

**Components:**
```bash
npx shadcn@latest add button card input
```

## When to Use Multiple Skills

Use **all eight** when:
- Complete brand package from scratch (logo → CIP → presentation)

Use **brand + design-system + ui-styling** when:
- Design system setup and implementation

Use **logo-design + cip-design** when:
- Complete brand identity package with deliverable mockups

Use **logo-design + cip-design + slides** when:
- Brand pitch: generate logo, create CIP mockups, build pitch deck

Use **banner-design + brand** when:
- Social media presence: branded banners across all platforms

Use **icon-design + design-system** when:
- Custom icon set matching design tokens and component specs

Use **brand + design-system** when:
- Defining design language without implementation

Use **design-system + ui-styling** when:
- Implementing existing brand in code
- Building component library



---

## `references/icon-design.md`

# Icon Design Reference

AI-powered SVG icon generation using Gemini 3.1 Pro Preview. 15 styles, 12 categories, multi-size export.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/icon/generate.py` | Generate SVG icons with Gemini 3.1 Pro Preview |

## Commands

### Generate Single Icon

```bash
python3 scripts/icon/generate.py --prompt "settings gear" --style outlined
python3 scripts/icon/generate.py --prompt "shopping cart" --style filled --color "#6366F1"
python3 scripts/icon/generate.py --name "dashboard" --category navigation --style duotone
```

### Generate Batch Variations

```bash
python3 scripts/icon/generate.py --prompt "cloud upload" --batch 4 --output-dir ./icons
python3 scripts/icon/generate.py --prompt "notification bell" --batch 6 --style outlined --output-dir ./icons
```

### Generate Multiple Sizes

```bash
python3 scripts/icon/generate.py --prompt "user profile" --sizes "16,24,32,48" --output-dir ./icons
```

### List Styles/Categories

```bash
python3 scripts/icon/generate.py --list-styles
python3 scripts/icon/generate.py --list-categories
```

## CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `--prompt, -p` | Icon description | required |
| `--name, -n` | Icon name (for filename) | - |
| `--style, -s` | Icon style (15 options) | - |
| `--category, -c` | Icon category for context | - |
| `--color` | Primary hex color | currentColor |
| `--size` | Display size in px | 24 |
| `--viewbox` | SVG viewBox size | 24 |
| `--output, -o` | Output file path | auto |
| `--output-dir` | Output directory (batch) | ./icons |
| `--batch` | Number of variations | - |
| `--sizes` | Comma-separated sizes | - |

## Available Styles

| Style | Stroke | Fill | Best For |
|-------|--------|------|----------|
| outlined | 2px | none | UI interfaces, web apps |
| filled | 0 | solid | Mobile apps, nav bars |
| duotone | 0 | dual | Marketing, landing pages |
| thin | 1-1.5px | none | Luxury brands, editorial |
| bold | 3px | none | Headers, hero sections |
| rounded | 2px | none | Friendly apps, health |
| sharp | 2px | none | Tech, fintech, enterprise |
| flat | 0 | solid | Material design, Google-style |
| gradient | 0 | gradient | Modern brands, SaaS |
| glassmorphism | 1px | semi | Modern UI, overlays |
| pixel | 0 | solid | Gaming, retro |
| hand-drawn | varies | none | Artisan, creative |
| isometric | 1-2px | partial | Tech docs, infographics |
| glyph | 0 | solid | System UI, compact |
| animated-ready | 2px | varies | Interactive UI, onboarding |

## Icon Categories

| Category | Icons |
|----------|-------|
| navigation | arrows, menus, home, chevrons |
| action | edit, delete, save, download, upload |
| communication | email, chat, phone, notification |
| media | play, pause, volume, camera |
| file | document, folder, archive, cloud |
| user | person, group, profile, settings |
| commerce | cart, bag, wallet, credit card |
| data | chart, graph, analytics, dashboard |
| development | code, terminal, bug, git, API |
| social | heart, star, bookmark, trophy |
| weather | sun, moon, cloud, rain |
| map | pin, location, compass, globe |

## SVG Best Practices

- **ViewBox**: Use `0 0 24 24` (standard) or `0 0 16 16` (compact)
- **Colors**: Use `currentColor` for CSS inheritance, avoid hardcoded colors
- **Accessibility**: Always include `<title>` element
- **Optimization**: Minimal path nodes, no embedded fonts or raster images
- **Sizing**: Design at 24px, test at 16px and 48px for clarity
- **Stroke**: Use `stroke-linecap="round"` and `stroke-linejoin="round"` for outlined styles

## Model

- **gemini-3.1-pro-preview**: Best thinking, token efficiency, factual consistency
- Text-only output (SVG is XML text) — no image generation API needed
- Supports structured output for consistent SVG formatting

## Workflow

1. Describe icon → `--prompt "settings gear"`
2. Choose style → `--style outlined`
3. Generate → script outputs .svg file
4. Optionally batch → `--batch 4` for variations
5. Multi-size export → `--sizes "16,24,32,48"`

## Setup

```bash
export GEMINI_API_KEY="your-key"
pip install google-genai
```



---

## `references/logo-color-psychology.md`

# Logo Color Psychology

## Primary Color Meanings

### Blue
- **Psychology:** Trust, stability, professionalism, calm
- **Industries:** Finance, healthcare, tech, corporate
- **Hex Examples:** Navy #003366, Royal #0055A4, Sky #0EA5E9
- **Pairings:** White, gold, light gray

### Red
- **Psychology:** Energy, passion, urgency, excitement
- **Industries:** Food, sports, entertainment, sales
- **Hex Examples:** Crimson #DC2626, Scarlet #EF4444, Burgundy #9F1239
- **Pairings:** White, black, gold
- **Caution:** Avoid for healthcare (blood connotation)

### Green
- **Psychology:** Growth, nature, health, sustainability
- **Industries:** Eco, wellness, organic, finance (growth)
- **Hex Examples:** Forest #228B22, Sage #2E8B57, Mint #10B981
- **Pairings:** White, brown, blue

### Yellow/Gold
- **Psychology:** Optimism, warmth, luxury, attention
- **Industries:** Food, children, luxury (gold), energy
- **Hex Examples:** Gold #D4AF37, Amber #F59E0B, Lemon #FACC15
- **Pairings:** Black, navy, dark brown

### Purple
- **Psychology:** Creativity, wisdom, luxury, mystery
- **Industries:** Beauty, creative, spiritual, premium
- **Hex Examples:** Royal #7C3AED, Lavender #A78BFA, Deep #581C87
- **Pairings:** Gold, white, pink

### Orange
- **Psychology:** Friendly, energetic, confident, youthful
- **Industries:** Food, sports, entertainment, retail
- **Hex Examples:** Tangerine #F97316, Coral #FB923C, Burnt #EA580C
- **Pairings:** White, navy, dark gray

### Black
- **Psychology:** Sophistication, power, elegance, authority
- **Industries:** Luxury, fashion, tech, premium
- **Pairings:** White, gold, silver
- **Note:** Use for high-end positioning

### White
- **Psychology:** Purity, simplicity, cleanliness, modern
- **Use:** Backgrounds, negative space, contrast
- **Pairings:** Any color (universal neutral)

## Color Combinations by Industry

| Industry | Primary | Secondary | Accent | Avoid |
|----------|---------|-----------|--------|-------|
| Tech | Blue, Purple | Gray, White | Teal, Green | Brown, Beige |
| Healthcare | Blue, Green | Teal, White | Light Purple | Red, Black |
| Finance | Navy, Blue | Gold, Gray | Green | Bright colors |
| Food | Red, Orange | Yellow, Brown | Green | Blue (appetite suppressant) |
| Fashion | Black, White | Gold, Blush | Navy | Neon (unless intentional) |
| Eco | Green, Brown | Beige, Blue | Yellow | Neon, Black |
| Children | Multi-color | Pastels | Bright accents | Dark, muted |

## Color Harmony Types

### Monochromatic
Single color with tints/shades. Safe, cohesive.

### Complementary
Opposite colors (blue-orange). High contrast, vibrant.

### Analogous
Adjacent colors (blue-teal-green). Harmonious, natural.

### Triadic
Three evenly spaced colors. Balanced, dynamic.

## Accessibility Considerations

- Minimum contrast ratio: 4.5:1 (WCAG AA)
- Avoid red-green only indicators
- Test in grayscale for clarity
- Consider colorblind users (~8% of males)

## Quick Reference Palettes

**Tech Professional:**
Primary: #6366F1 | Secondary: #8B5CF6 | Accent: #06B6D4

**Eco Sustainable:**
Primary: #228B22 | Secondary: #2E8B57 | Accent: #DEB887

**Luxury Premium:**
Primary: #1C1917 | Secondary: #D4AF37 | Accent: #FFFFFF

**Healthcare Trust:**
Primary: #0077B6 | Secondary: #00A896 | Accent: #FFFFFF

**Food Warm:**
Primary: #DC2626 | Secondary: #F97316 | Accent: #CA8A04



---

## `references/logo-design.md`

# Logo Design Reference

AI-powered logo design with 55+ styles, 30 color palettes, 25 industry guides. Gemini Nano Banana is the default provider; Atlas Cloud and MuAPI are also available as explicit opt-in providers.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/logo/search.py` | Search styles, colors, industries; generate design briefs |
| `scripts/logo/generate.py` | Generate logos with Gemini Nano Banana, Atlas Cloud, or MuAPI |
| `scripts/logo/core.py` | BM25 search engine for logo data |

## Commands

### Design Brief (Start Here)

```bash
python3 scripts/logo/search.py "tech startup modern" --design-brief -p "BrandName"
```

### Search Domains

```bash
# Styles
python3 scripts/logo/search.py "minimalist clean" --domain style

# Color palettes
python3 scripts/logo/search.py "tech professional" --domain color

# Industry guidelines
python3 scripts/logo/search.py "healthcare medical" --domain industry
```

### Generate Logo

**ALWAYS** use white background for output logos.

```bash
python3 scripts/logo/generate.py --brand "TechFlow" --style minimalist --industry tech
python3 scripts/logo/generate.py --prompt "coffee shop vintage badge" --style vintage
python3 scripts/logo/generate.py --brand "TechFlow" --provider atlas
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi
python3 scripts/logo/generate.py --brand "TechFlow" --provider muapi --muapi-model nano-banana-pro
```

Options: `--style`, `--industry`, `--prompt`, `--provider`, `--atlas-model`, `--muapi-model`

## Available Styles

| Category | Styles |
|----------|--------|
| General | Minimalist, Wordmark, Lettermark, Pictorial Mark, Abstract Mark, Mascot, Emblem, Combination Mark |
| Aesthetic | Vintage/Retro, Art Deco, Luxury, Playful, Corporate, Organic, Neon, Grunge, Watercolor |
| Modern | Gradient, Flat Design, 3D/Isometric, Geometric, Line Art, Duotone, Motion-Ready |
| Clever | Negative Space, Monoline, Split/Fragmented, Responsive/Adaptive |

## Color Psychology

| Color | Psychology | Best For |
|-------|------------|----------|
| Blue | Trust, stability | Finance, tech, healthcare |
| Green | Growth, natural | Eco, wellness, organic |
| Red | Energy, passion | Food, sports, entertainment |
| Gold | Luxury, premium | Fashion, jewelry, hotels |
| Purple | Creative, innovative | Beauty, creative, tech |

## Industry Defaults

| Industry | Style | Colors | Typography |
|----------|-------|--------|------------|
| Tech | Minimalist, Abstract | Blues, purples, gradients | Geometric sans |
| Healthcare | Professional, Line Art | Blues, greens, teals | Clean sans |
| Finance | Corporate, Emblem | Navy, gold | Serif or clean sans |
| Food | Vintage Badge, Mascot | Warm reds, oranges | Friendly, script |
| Fashion | Wordmark, Luxury | Black, gold, white | Elegant serif |

## Workflow

1. Generate design brief → `scripts/logo/search.py --design-brief`
2. Generate logo variations → `scripts/logo/generate.py --brand --style --industry`
3. Ask user about HTML preview → `AskUserQuestion` tool
4. If yes, use the bundled `ui-ux-pro-max` skill for the HTML gallery

## Detailed References

- `references/logo-style-guide.md` - Detailed style descriptions
- `references/logo-color-psychology.md` - Color meanings and combinations
- `references/logo-prompt-engineering.md` - AI generation prompts

## Setup

```bash
export GEMINI_API_KEY="your-key"
pip install google-genai

# Optional Atlas Cloud provider (no extra Python package required)
export ATLASCLOUD_API_KEY="your-key"

# Optional MuAPI provider (no extra Python package required)
export MUAPI_API_KEY="your-key"
```

MuAPI uses the asynchronous model endpoint and prediction result API. See the
[MuAPI API reference](https://muapi.ai/docs/api-reference) for authentication
and the [nano-banana model contract](https://api.muapi.ai/api/v1/models/nano-banana)
or [nano-banana-pro model contract](https://api.muapi.ai/api/v1/models/nano-banana-pro)
for the current model-specific schemas. The logo generator supports both documented
model slugs and sends their shared required `prompt` plus optional `aspect_ratio`
fields; the Pro model also accepts an optional `resolution` field that this focused
logo workflow leaves at the provider default.



---

## `references/logo-prompt-engineering.md`

# Logo AI Prompt Engineering

## Core Prompt Structure

```
Professional logo design for [brand/industry]:
[Visual description]
Style: [style keywords]
Colors: [color palette]
Requirements: [technical specs]
```

## Effective Keywords by Style

### Minimalist
```
minimalist, clean lines, simple geometric shapes, essential elements only,
high white space, flat design, single color, modern, uncluttered,
negative space, subtle, refined
```

### Vintage/Retro
```
vintage, retro, heritage, established, classic, nostalgic, weathered,
distressed texture, badge style, hand-lettered, craft, artisan,
sepia tones, muted colors, aged paper effect
```

### Luxury/Premium
```
luxury, elegant, sophisticated, premium, refined, exclusive, high-end,
gold accents, metallic, minimal, tasteful, upscale, prestige,
thin lines, serif typography, foil effect
```

### Modern/Tech
```
modern, innovative, digital, tech-forward, sleek, futuristic,
gradient colors, geometric, abstract, dynamic, cutting-edge,
clean sans-serif, circuit-like, data visualization
```

### Playful/Fun
```
playful, fun, colorful, friendly, approachable, cheerful, whimsical,
bouncy, rounded shapes, bright colors, cartoon-like, energetic,
bubbly, hand-drawn elements
```

### Organic/Natural
```
organic, natural, flowing, botanical, eco-friendly, sustainable,
earth tones, leaf elements, hand-drawn, imperfect lines, growth,
green, nature-inspired, biophilic
```

## Negative Prompts (What to Avoid)

Always include to prevent unwanted results:
```
NOT: photorealistic, 3D render with realistic textures, photograph,
stock image, clip art, multiple logos, busy background, text watermarks,
low quality, blurry, distorted, complex detailed patterns
```

## Industry-Specific Prompts

### Tech Startup
```
Modern tech company logo, abstract geometric mark, gradient blue to purple,
clean minimal design, innovative feel, scalable vector style,
professional quality, silicon valley aesthetic
```

### Healthcare
```
Healthcare medical logo, clean professional design, cross or heart symbol,
calming blue and teal colors, trustworthy appearance, caring feel,
simple scalable mark, HIPAA-appropriate conservative style
```

### Restaurant/Food
```
Restaurant logo, warm inviting colors, appetizing feel, vintage badge style,
chef or utensil iconography, friendly welcoming design, rustic charm,
established look, readable at small sizes
```

### Fashion Brand
```
Fashion brand logo, elegant sophisticated wordmark, luxury aesthetic,
black and gold color scheme, thin refined typography, haute couture feel,
minimal exclusive design, high-end positioning
```

### Eco/Sustainable
```
Eco-friendly sustainable brand logo, organic natural elements, leaf motif,
earth green and brown colors, growth symbolism, environmental awareness,
clean modern yet natural feel, recyclable-look design
```

## Technical Requirements to Include

### Scalability
```
vector-style, scalable at any size, clear silhouette,
works as favicon, recognizable small scale, simple shapes
```

### Versatility
```
works on light and dark backgrounds, single color version possible,
horizontal and stacked layouts, brand mark can stand alone
```

### Quality
```
professional quality, print-ready, high resolution,
crisp edges, balanced composition, centered design
```

## Prompt Templates

### Quick Generation
```
Professional [industry] logo, [style] design, [color] colors,
clean modern aesthetic, scalable vector style
```

### Detailed Brief
```
Professional logo design for [brand name], a [industry] company.

Visual style: [style keywords]
Primary colors: [hex codes]
Mood: [emotional keywords]
Symbols: [iconography hints]

Technical: Vector-style illustration, scalable, works in single color,
centered on plain background, no text unless specified.
```

### Variation Request
```
Alternative version of [brand] logo:
Keep: [elements to preserve]
Change: [elements to modify]
Style direction: [new style keywords]
```

## Common Pitfalls

1. **Too detailed** - AI generates complexity; request "simple"
2. **Unclear background** - Specify "plain white background"
3. **Text issues** - AI struggles with text; generate mark separately
4. **Wrong aspect** - Specify "1:1 square" or "horizontal"
5. **Realistic style** - Add "illustration, vector-style, not photorealistic"



---

## `references/logo-style-guide.md`

# Logo Style Guide

## Core Logo Types

### 1. Wordmark (Logotype)
Text-only logo using custom typography.
- **Best for:** Established brands, distinctive names
- **Examples:** Google, Coca-Cola, FedEx
- **Typography:** Custom letterforms, unique kerning
- **Tip:** Name must be memorable and pronounceable

### 2. Lettermark (Monogram)
Initials or abbreviated letters.
- **Best for:** Long company names, professional firms
- **Examples:** IBM, HBO, NASA
- **Typography:** Bold geometric sans-serif
- **Tip:** Works well for brands with 2-4 letter abbreviations

### 3. Pictorial Mark (Brand Mark)
Standalone icon or symbol.
- **Best for:** Global brands with recognition
- **Examples:** Apple, Twitter, Target
- **Design:** Simple, scalable, memorable shape
- **Tip:** Requires brand equity to work alone

### 4. Abstract Mark
Non-representational geometric shapes.
- **Best for:** Tech companies, differentiating brands
- **Examples:** Pepsi, Airbnb, Spotify
- **Design:** Unique shape conveying brand values
- **Tip:** Can represent complex ideas simply

### 5. Mascot
Character representing the brand.
- **Best for:** Family brands, sports teams, food
- **Examples:** KFC, Pringles, Michelin
- **Design:** Friendly, expressive, versatile
- **Tip:** Can evolve with brand while maintaining recognition

### 6. Emblem
Symbol enclosed within a shape.
- **Best for:** Traditional brands, organizations
- **Examples:** Starbucks, Harley-Davidson, NFL
- **Design:** Badge, seal, or crest style
- **Tip:** May have scalability challenges

### 7. Combination Mark
Icon + text in unified design.
- **Best for:** New brands, versatile applications
- **Examples:** Burger King, Lacoste, Doritos
- **Design:** Lockup with flexible arrangements
- **Tip:** Most versatile, can separate elements later

## Aesthetic Styles

### Minimalist
- Clean lines, essential elements only
- High white space, simple geometry
- Limited color palette (1-2 colors)
- **Use:** Tech, professional services, modern brands

### Vintage/Retro
- Nostalgic, heritage feel
- Distressed textures, muted colors
- Script or slab serif typography
- **Use:** Craft brands, artisan products

### Luxury/Premium
- Elegant, refined aesthetic
- Gold, black, white color scheme
- Thin serifs or sophisticated sans
- **Use:** Fashion, jewelry, high-end services

### Geometric
- Mathematical precision
- Circles, triangles, squares
- Perfect symmetry
- **Use:** Architecture, tech, modern brands

### Organic/Natural
- Flowing, imperfect lines
- Earth tones, natural colors
- Hand-drawn feel
- **Use:** Eco brands, wellness, organic products

### Gradient/Modern
- Color transitions, vibrant palettes
- Dimensional depth
- Contemporary feel
- **Use:** Apps, tech startups, digital products

## Style Selection Matrix

| Brand Type | Primary Style | Secondary Options |
|------------|---------------|-------------------|
| Tech Startup | Minimalist, Abstract | Geometric, Gradient |
| Law Firm | Wordmark, Emblem | Lettermark |
| Restaurant | Mascot, Badge | Vintage, Combination |
| Fashion | Wordmark, Luxury | Monogram, Line Art |
| Healthcare | Professional, Line Art | Abstract, Combination |
| Non-Profit | Combination, Emblem | Organic, Hand-Drawn |

## Scalability Checklist

- [ ] Recognizable at 16x16 pixels (favicon)
- [ ] Clear at business card size
- [ ] Works in single color
- [ ] Maintains clarity in black/white
- [ ] No tiny details that disappear when scaled



---

## `references/slides-copywriting-formulas.md`

# Copywriting Formulas

25 formulas for persuasive slide copy.

## Core Formulas

### PAS (Problem-Agitate-Solution)
**Use:** Problem slides, pain points
**Components:** Problem → Agitate → Solution
**Template:** "[Pain point]? Every [time frame], [consequence]. [Solution] fixes this."

### AIDA (Attention-Interest-Desire-Action)
**Use:** CTAs, closing slides
**Components:** Attention → Interest → Desire → Action
**Template:** "[Bold statement]. [Benefit detail]. [Social proof]. [CTA]."

### FAB (Features-Advantages-Benefits)
**Use:** Feature slides, product showcases
**Components:** Feature → Advantage → Benefit
**Template:** "[Feature] lets you [advantage], so you can [benefit]."

### Cost of Inaction
**Use:** Agitation slides, urgency
**Components:** Status Quo → Loss → Time Decay
**Template:** "Without [solution], you're losing [amount] every [timeframe]."

### Before-After-Bridge
**Use:** Transformation slides, case studies
**Components:** Before → After → Bridge
**Template:** "[Pain point before]. [Desired state after]. [Your solution] is the bridge."

## Formula-to-Slide Mapping

| Slide Type | Primary Formula | Emotion |
|------------|-----------------|---------|
| Title/Hook | AIDA, Hook | curiosity |
| Problem | PAS, Agitate | frustration |
| Cost/Risk | Cost of Inaction | fear |
| Solution | FAB, BAB | hope |
| Features | FAB | confidence |
| Traction | Proof Stack | trust |
| Social Proof | Testimonial | trust |
| Pricing | Value Stack | confidence |
| CTA | AIDA, Urgency | urgency |

## Headline Patterns

### Power Words
- "Stop [bad thing]"
- "Get [desired result] in [timeframe]"
- "The [adjective] way to [action]"
- "Why [audience] choose [product]"
- "[Number] ways to [achieve goal]"

### Contrast Patterns
- "[Old way] is dead. Meet [new way]."
- "Don't [bad action]. Instead, [good action]."
- "From [pain point] to [benefit]."

### Social Proof Patterns
- "[Number]+ [users/companies] trust [product]"
- "Join [notable company] and [notable company]"
- "As seen in [publication]"

## Search Commands

```bash
# Find formula for slide type
python ../design-system/scripts/search-slides.py "problem agitation" -d copy

# Get emotion-appropriate formula
python ../design-system/scripts/search-slides.py "urgency cta" -d copy
```

## Quick Reference

| Need | Use Formula |
|------|------------|
| Create urgency | Cost of Inaction, Scarcity |
| Build trust | Social Proof, Testimonial |
| Show value | FAB, Value Stack |
| Drive action | AIDA, CTA |
| Tell story | BAB, Story Arc |
| Present data | Proof Stack |



---

## `references/slides-create.md`

Invoke `slides` skill to create persuasive HTML slides using design tokens, Chart.js, and the slide knowledge database.

## Task
<task>$ARGUMENTS</task>



---

## `references/slides-html-template.md`

# HTML Slide Template

Complete HTML structure with navigation, tokens, and Chart.js integration.

## Base Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentation Title</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
    <style>
        /* Paste embed-tokens.cjs output here */
        :root {
            --color-primary: #FF6B6B;
            --color-background: #0D0D0D;
            /* ... more tokens */
        }

        /* Base slide styles */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            background: var(--color-background);
            color: #fff;
            font-family: var(--typography-font-body, 'Inter', sans-serif);
            overflow: hidden;
        }

        /* 16:9 Aspect Ratio Container (desktop) */
        .slide-deck {
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }

        @media (min-width: 769px) {
            .slide-deck {
                /* Lock to 16:9 — letterbox if viewport ratio differs */
                max-width: calc(100vh * 16 / 9);
                max-height: calc(100vw * 9 / 16);
                margin: auto;
                position: absolute;
                inset: 0;
            }
        }

        .slide {
            position: absolute;
            width: 100%; height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 60px;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.4s;
            background: var(--color-background);
            overflow: hidden; /* Prevent content overflow */
        }

        .slide.active { opacity: 1; visibility: visible; }

        /* Slide inner wrapper — constrains content within safe area */
        .slide-content {
            width: 100%;
            max-width: 100%;
            max-height: 100%;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 16px;
        }

        /* Typography */
        h1, h2 { font-family: var(--typography-font-heading, 'Space Grotesk', sans-serif); }
        .slide-title {
            font-size: clamp(32px, 6vw, 80px);
            background: var(--primitive-gradient-primary, linear-gradient(135deg, #FF6B6B, #FF8E53));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
        }

        /* ===== RESPONSIVE BREAKPOINTS ===== */

        /* Tablet (portrait) */
        @media (max-width: 768px) {
            .slide { padding: 32px 24px; }
            .slide-title { font-size: clamp(28px, 5vw, 48px); }
            h2 { font-size: clamp(20px, 4vw, 32px); }
            p, li { font-size: clamp(14px, 2.5vw, 18px); }
        }

        /* Mobile */
        @media (max-width: 480px) {
            .slide { padding: 24px 16px; }
            .slide-title { font-size: clamp(22px, 6vw, 36px); }
            h2 { font-size: clamp(18px, 4.5vw, 28px); }
            p, li { font-size: clamp(12px, 3vw, 16px); }
            .nav-controls { bottom: 16px; gap: 12px; }
            .nav-btn { width: 32px; height: 32px; font-size: 14px; }
        }

        /* Navigation */
        .progress-bar {
            position: fixed;
            top: 0; left: 0;
            height: 3px;
            background: var(--color-primary);
            transition: width 0.3s;
            z-index: 1000;
        }
        .nav-controls {
            position: fixed;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            align-items: center;
            gap: 20px;
            z-index: 1000;
        }
        .nav-btn {
            background: rgba(255,255,255,0.1);
            border: none;
            color: #fff;
            width: 40px; height: 40px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 18px;
        }
        .nav-btn:hover { background: rgba(255,255,255,0.2); }
        .slide-counter { color: rgba(255,255,255,0.6); font-size: 14px; }
    </style>
</head>
<body>
    <!-- Progress Bar -->
    <div class="progress-bar" id="progressBar"></div>

    <!-- Slide Deck Container (16:9 on desktop) -->
    <div class="slide-deck">

    <!-- Slides -->
    <div class="slide active">
        <div class="slide-content">
            <h1 class="slide-title">Title Slide</h1>
            <p>Subtitle or tagline</p>
        </div>
    </div>

    <!-- More slides... (always wrap content in .slide-content) -->

    </div><!-- /.slide-deck -->

    <!-- Navigation -->
    <div class="nav-controls">
        <button class="nav-btn" onclick="prevSlide()">←</button>
        <span class="slide-counter"><span id="current">1</span> / <span id="total">9</span></span>
        <button class="nav-btn" onclick="nextSlide()">→</button>
    </div>

    <script>
        let current = 1;
        const total = document.querySelectorAll('.slide').length;
        document.getElementById('total').textContent = total;

        function showSlide(n) {
            if (n < 1) n = 1;
            if (n > total) n = total;
            current = n;
            document.querySelectorAll('.slide').forEach((s, i) => {
                s.classList.toggle('active', i === n - 1);
            });
            document.getElementById('current').textContent = n;
            document.getElementById('progressBar').style.width = (n / total * 100) + '%';
        }

        function nextSlide() { showSlide(current + 1); }
        function prevSlide() { showSlide(current - 1); }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
            if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
        });

        document.addEventListener('click', (e) => {
            if (!e.target.closest('.nav-controls')) nextSlide();
        });

        showSlide(1);
    </script>
</body>
</html>
```

## Chart.js Integration

```html
<div class="chart-container" style="width: min(80%, 600px); height: clamp(200px, 40vh, 350px);">
    <canvas id="revenueChart"></canvas>
</div>

<script>
new Chart(document.getElementById('revenueChart'), {
    type: 'line', // or 'bar', 'doughnut', 'radar'
    data: {
        labels: ['Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'MRR ($K)',
            data: [5, 12, 28, 45],
            borderColor: '#FF6B6B',
            backgroundColor: 'rgba(255, 107, 107, 0.1)',
            borderWidth: 3,
            fill: true,
            tension: 0.4
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
            x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#B8B8D0' } },
            y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#B8B8D0' } }
        }
    }
});
</script>
```

## Animation Classes

```css
/* Fade Up */
.animate-fade-up {
    animation: fadeUp 0.6s ease-out forwards;
    opacity: 0;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Count Animation */
.animate-count { animation: countUp 1s ease-out forwards; }

/* Scale */
.animate-scale {
    animation: scaleIn 0.5s ease-out forwards;
}
@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
}

/* Stagger Children */
.animate-stagger > * {
    opacity: 0;
    animation: fadeUp 0.5s ease-out forwards;
}
.animate-stagger > *:nth-child(1) { animation-delay: 0.1s; }
.animate-stagger > *:nth-child(2) { animation-delay: 0.2s; }
.animate-stagger > *:nth-child(3) { animation-delay: 0.3s; }
.animate-stagger > *:nth-child(4) { animation-delay: 0.4s; }
```

## Background Images

```html
<div class="slide slide-with-bg" style="background-image: url('https://images.pexels.com/...')">
    <div class="overlay" style="background: linear-gradient(135deg, rgba(13,13,13,0.9), rgba(13,13,13,0.7))"></div>
    <div class="content" style="position: relative; z-index: 1;">
        <!-- Slide content -->
    </div>
</div>
```

## CSS Variables Reference

| Variable | Usage |
|----------|-------|
| `--color-primary` | Brand primary (CTA, highlights) |
| `--color-background` | Slide background |
| `--color-secondary` | Secondary elements |
| `--primitive-gradient-primary` | Title gradients |
| `--typography-font-heading` | Headlines |
| `--typography-font-body` | Body text |



---

## `references/slides-layout-patterns.md`

# Layout Patterns

25 slide layouts with CSS structures and animation classes.

## Layout Selection by Use Case

| Layout | Use Case | Animation |
|--------|----------|-----------|
| Title Slide | Opening/first impression | `animate-fade-up` |
| Problem Statement | Establish pain point | `animate-stagger` |
| Solution Overview | Introduce solution | `animate-scale` |
| Feature Grid | Show capabilities (3-6 cards) | `animate-stagger` |
| Metrics Dashboard | Display KPIs (3-4 metrics) | `animate-stagger-scale` |
| Comparison Table | Compare options | `animate-fade-up` |
| Timeline Flow | Show progression | `animate-stagger` |
| Team Grid | Introduce people | `animate-stagger` |
| Quote Testimonial | Customer endorsement | `animate-fade-up` |
| Two Column Split | Compare/contrast | `animate-fade-up` |
| Big Number Hero | Single powerful metric | `animate-count` |
| Product Screenshot | Show product UI | `animate-scale` |
| Pricing Cards | Present tiers | `animate-stagger` |
| CTA Closing | Drive action | `animate-pulse` |

## CSS Structures

### Title Slide
```css
.slide-title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
```

### Two Column Split
```css
.slide-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 48px;
    align-items: center;
}
@media (max-width: 768px) {
    .slide-split { grid-template-columns: 1fr; gap: 24px; }
}
```

### Feature Grid (3 columns)
```css
.slide-features {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
@media (max-width: 768px) {
    .slide-features { grid-template-columns: repeat(2, 1fr); gap: 16px; }
}
@media (max-width: 480px) {
    .slide-features { grid-template-columns: 1fr; }
}
```

### Metrics Dashboard (4 columns)
```css
.slide-metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}
@media (max-width: 768px) {
    .slide-metrics { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 480px) {
    .slide-metrics { grid-template-columns: 1fr; }
}
```

## Component Variants

### Card Styles
| Style | CSS Class | Use For |
|-------|-----------|---------|
| Icon Left | `.card-icon-left` | Features with icons |
| Accent Bar | `.card-accent-bar` | Highlighted features |
| Metric Card | `.card-metric` | Numbers/stats |
| Avatar Card | `.card-avatar` | Team members |
| Pricing Card | `.card-pricing` | Price tiers |

### Metric Styles
| Style | Effect |
|-------|--------|
| `gradient-number` | Gradient text on numbers |
| `oversized` | Extra large (120px+) |
| `sparkline` | Small inline chart |
| `funnel-numbers` | Conversion stages |

## Visual Treatments

| Treatment | When to Use |
|-----------|-------------|
| `gradient-glow` | Title slides, CTAs |
| `subtle-border` | Problem statements |
| `icon-top` | Feature grids |
| `screenshot-shadow` | Product screenshots |
| `popular-highlight` | Pricing (scale 1.05) |
| `bg-overlay` | Background images |
| `contrast-pair` | Before/after |
| `logo-grayscale` | Client logos |

## Search Commands

```bash
# Find layout for specific use
python ../design-system/scripts/search-slides.py "metrics dashboard" -d layout

# Contextual recommendation
python ../design-system/scripts/search-slides.py "traction slide" \
  --context --position 4 --total 10
```

## Layout Decision Flow

```
1. What's the slide goal?
   └─> Search layout-logic.csv

2. What emotion should it trigger?
   └─> Search color-logic.csv

3. What's the content type?
   └─> Search typography.csv

4. Should it break pattern?
   └─> Check position (1/3, 2/3) → Use full-bleed
```



---

## `references/slides-strategies.md`

# Slide Strategies

15 proven deck structures with emotion arcs.

## Strategy Selection

| Strategy | Slides | Goal | Audience |
|----------|--------|------|----------|
| YC Seed Deck | 10-12 | Raise seed funding | VCs |
| Guy Kawasaki | 10 | Pitch in 20 min | Investors |
| Series A | 12-15 | Raise Series A | Growth VCs |
| Product Demo | 5-8 | Demonstrate value | Prospects |
| Sales Pitch | 7-10 | Close deal | Qualified leads |
| Nancy Duarte Sparkline | Varies | Transform perspective | Any |
| Problem-Solution-Benefit | 3-5 | Quick persuasion | Time-pressed |
| QBR | 10-15 | Update stakeholders | Leadership |
| Team All-Hands | 8-12 | Align team | Employees |
| Conference Talk | 15-25 | Thought leadership | Attendees |
| Workshop | 20-40 | Teach skills | Learners |
| Case Study | 8-12 | Prove value | Prospects |
| Competitive Analysis | 6-10 | Strategic decisions | Internal |
| Board Meeting | 15-20 | Update board | Directors |
| Webinar | 20-30 | Generate leads | Registrants |

## Common Structures

### YC Seed Deck (10 slides)
1. Title/Hook
2. Problem
3. Solution
4. Traction
5. Market
6. Product
7. Business Model
8. Team
9. Financials
10. The Ask

**Emotion arc:** curiosity→frustration→hope→confidence→trust→urgency

### Sales Pitch (9 slides)
1. Personalized Hook
2. Their Problem
3. Cost of Inaction
4. Your Solution
5. Proof/Case Studies
6. Differentiators
7. Pricing/ROI
8. Objection Handling
9. CTA + Next Steps

**Emotion arc:** connection→frustration→fear→hope→trust→confidence→urgency

### Product Demo (6 slides)
1. Hook/Problem
2. Solution Overview
3. Live Demo/Screenshots
4. Key Features
5. Benefits/Pricing
6. CTA

**Emotion arc:** curiosity→frustration→hope→confidence→urgency

## Duarte Sparkline Pattern

Alternate between "What Is" (current pain) and "What Could Be" (better future):

```
What Is → What Could Be → What Is → What Could Be → New Bliss
(pain)     (hope)         (pain)     (hope)         (resolution)
```

Pattern breaks at 1/3 and 2/3 positions create engagement peaks.

## Search Commands

```bash
# Find strategy by goal
python ../design-system/scripts/search-slides.py "investor pitch" -d strategy

# Get emotion arc
python ../design-system/scripts/search-slides.py "series a funding" -d strategy --json
```

## Matching Strategy to Context

| Context | Recommended Strategy |
|---------|---------------------|
| Raising money | YC Seed, Series A, Guy Kawasaki |
| Selling product | Sales Pitch, Product Demo |
| Internal update | QBR, All-Hands, Board Meeting |
| Public speaking | Conference Talk, Workshop |
| Proving value | Case Study, Competitive Analysis |
| Lead generation | Webinar |



---

## `references/slides.md`

# Slides Reference

Strategic HTML presentation design with Chart.js data visualization, design tokens, responsive layouts, and copywriting formulas.

## Usage

Activate the `design` skill and specify slides task, e.g. "create a pitch deck".

## Knowledge Base

| Topic | File | Purpose |
|-------|------|---------|
| Creation Guide | `references/slides-create.md` | Step-by-step slide creation workflow |
| Layout Patterns | `references/slides-layout-patterns.md` | Slide layout templates and grid systems |
| HTML Template | `references/slides-html-template.md` | Base HTML structure for presentations |
| Copywriting | `references/slides-copywriting-formulas.md` | AIDA, PAS, FAB for slide content |
| Strategies | `references/slides-strategies.md` | Contextual strategies by presentation type |

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js visualizations
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content
- Investor decks, sales presentations, team updates

## Key Features

- **Chart.js Integration**: Bar, line, pie, doughnut, radar charts
- **Design Tokens**: Consistent spacing, colors, typography
- **Responsive**: Works on desktop and mobile
- **Copywriting**: Built-in AIDA, PAS, FAB formulas
- **Layout Patterns**: Hero, split, grid, comparison, timeline

## Workflow

1. Parse presentation type from user request
2. Load `references/slides-create.md` for creation guide
3. Select layout patterns from `references/slides-layout-patterns.md`
4. Apply copywriting formulas from `references/slides-copywriting-formulas.md`
5. Use HTML template from `references/slides-html-template.md`
6. Apply strategy from `references/slides-strategies.md`



---

## `references/social-photos-design.md`

# Social Photos Design Guide

Design social media images via HTML/CSS rendering + screenshot export. Orchestrates the bundled `ui-ux-pro-max`, `brand`, and `design-system` skills; screenshot export runs through Chrome headless, Playwright, or Puppeteer.

## Platform Sizes

| Platform | Type | Size (px) | Aspect |
|----------|------|-----------|--------|
| Instagram | Post | 1080 x 1080 | 1:1 |
| Instagram | Story/Reel | 1080 x 1920 | 9:16 |
| Instagram | Carousel | 1080 x 1350 | 4:5 |
| Facebook | Post | 1200 x 630 | ~1.9:1 |
| Facebook | Story | 1080 x 1920 | 9:16 |
| Twitter/X | Post | 1200 x 675 | 16:9 |
| Twitter/X | Card | 800 x 418 | ~1.91:1 |
| LinkedIn | Post | 1200 x 627 | ~1.91:1 |
| LinkedIn | Article | 1200 x 644 | ~1.86:1 |
| Pinterest | Pin | 1000 x 1500 | 2:3 |
| YouTube | Thumbnail | 1280 x 720 | 16:9 |
| TikTok | Cover | 1080 x 1920 | 9:16 |
| Threads | Post | 1080 x 1080 | 1:1 |

## Workflow

### Step 1: Plan the Work

Create TODO tasks with the runtime's native task list. Break down into:
- Requirement analysis task
- Idea generation task(s)
- HTML design task(s) — can parallelize per size/variant
- Screenshot export task(s) — can parallelize per file
- Report generation task

Spawn parallel subagents for independent tasks (e.g., multiple HTML files for different sizes).

### Step 2: Analyze Requirements

Parse user input for:
- **Subject/topic** — what the social photo represents
- **Target platforms** — which sizes needed (default: Instagram Post 1:1 + Story 9:16)
- **Visual style** — minimalist, bold, gradient, photo-based, etc.
- **Brand context** — read from `docs/brand-guidelines.md` if exists
- **Content elements** — headline, subtext, CTA, images, icons
- **Quantity** — how many variations (default: 3)

### Step 3: Generate Ideas

Create 3-5 concept ideas that:
- Match the input prompt/requirements
- Consider platform-specific best practices
- Vary in composition, color, typography approach
- Align with brand guidelines if available

Present ideas to user via `AskUserQuestion` for approval before designing.

### Step 4: Design HTML Files

Use these bundled skills in sequence:

1. **`brand`** — Extract brand colors, fonts, voice from user's project
2. **`design-system`** — Get design tokens (spacing, typography scale, color palette)
3. **`ui-ux-pro-max`** — Layout, hierarchy, visual balance; search a different style, palette, or font pairing per concept for design variety.

For each approved idea + each target size, create an HTML file:

```
output/social-photos/
├── idea-1-instagram-post-1080x1080.html
├── idea-1-instagram-story-1080x1920.html
├── idea-2-instagram-post-1080x1080.html
├── idea-2-instagram-story-1080x1920.html
└── ...
```

#### HTML Design Rules

- **Viewport** — Set exact pixel dimensions matching target size
- **Self-contained** — Inline all CSS, embed fonts via Google Fonts CDN
- **No scrolling** — Everything fits in one viewport
- **High contrast** — Text readable at thumbnail size
- **Brand-aligned** — Use extracted brand colors/fonts
- **Safe zones** — Critical content within central 80% area
- **Typography** — Min 24px for headlines, min 16px for body at 1080px width
- **Visual hierarchy** — One focal point, clear reading flow

#### HTML Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width={WIDTH}, initial-scale=1.0">
  <link href="https://fonts.googleapis.com/css2?family={FONT}&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body {
      width: {WIDTH}px;
      height: {HEIGHT}px;
      overflow: hidden;
      font-family: '{FONT}', sans-serif;
    }
    .canvas {
      width: {WIDTH}px;
      height: {HEIGHT}px;
      position: relative;
      /* Background: gradient, solid, or image */
    }
    /* Design tokens from brand/design-system */
  </style>
</head>
<body>
  <div class="canvas">
    <!-- Content layers -->
  </div>
</body>
</html>
```

### Step 5: Screenshot Export

Use Chrome headless, Playwright, or Puppeteer to capture exact-size screenshots.

**IMPORTANT:** Always add a delay (3-5s) after page load for fonts/images to fully render before capture.

#### Option A: Chrome Headless CLI (Recommended — zero dependencies)

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DELAY=5  # seconds for fonts/images to load

"$CHROME" \
  --headless \
  --disable-gpu \
  --no-sandbox \
  --hide-scrollbars \
  --window-size="${WIDTH},${HEIGHT}" \
  --virtual-time-budget=$((DELAY * 1000)) \
  --screenshot="output.png" \
  "file:///path/to/file.html"
```

Key flags:
- `--virtual-time-budget=5000` — waits 5s virtual time for assets (Google Fonts, images) to load
- `--hide-scrollbars` — prevents scrollbar artifacts in screenshots
- `--window-size=WxH` — sets exact pixel dimensions

#### Option B: Browser automation provided by the runtime

If the runtime offers a browser-automation or screenshot capability (for example a browser MCP server), use it to:
1. Open each HTML file in browser
2. Set viewport to exact target dimensions
3. Wait 3-5s for fonts/images to fully load
4. Screenshot full page to PNG
5. Save to `output/social-photos/exports/`

#### Option C: Playwright script

```javascript
const { chromium } = require('playwright');

async function captureScreenshots(htmlFiles) {
  const browser = await chromium.launch();

  for (const file of htmlFiles) {
    const [width, height] = file.match(/(\d+)x(\d+)/).slice(1).map(Number);

    const page = await browser.newPage();
    await page.setViewportSize({ width, height });
    await page.goto(`file://${file}`, { waitUntil: 'networkidle' });
    // Wait for fonts/images to fully render
    await page.waitForTimeout(3000);

    const outputPath = file.replace('.html', '.png').replace('social-photos/', 'social-photos/exports/');
    await page.screenshot({ path: outputPath, type: 'png' });
    await page.close();
  }

  await browser.close();
}
```

#### Option D: Puppeteer script

```javascript
const puppeteer = require('puppeteer');

async function captureScreenshots(htmlFiles) {
  const browser = await puppeteer.launch();

  for (const file of htmlFiles) {
    const [width, height] = file.match(/(\d+)x(\d+)/).slice(1).map(Number);

    const page = await browser.newPage();
    await page.setViewport({ width, height, deviceScaleFactor: 2 }); // 2x for retina
    await page.goto(`file://${file}`, { waitUntil: 'networkidle0' });
    // Wait for fonts/images to fully render
    await new Promise(r => setTimeout(r, 3000));

    const outputPath = file.replace('.html', '.png').replace('social-photos/', 'social-photos/exports/');
    await page.screenshot({ path: outputPath, type: 'png' });
    await page.close();
  }

  await browser.close();
}
```

**IMPORTANT:** Use `deviceScaleFactor: 2` for retina-quality output (Puppeteer only).

### Step 6: Verify & Fix Designs

Open each exported PNG in an available browser or image viewer and inspect it:

1. Open exported screenshots and check for layout/styling issues
2. Verify: fonts rendered correctly, colors match brand, text readable at thumbnail size
3. Check: no overflow, no cut-off content, safe zones respected, visual hierarchy clear
4. If issues found → fix HTML source → re-export screenshot → verify again
5. Repeat until all designs pass visual QA

**Common issues to check:**
- Fonts not loaded (fallback to system fonts)
- Text overflow or clipping
- Elements outside safe zone (central 80%)
- Low contrast text (below WCAG AA 4.5:1)
- Misaligned elements or broken layouts

### Step 7: Generate Summary Report

Save the report as `plans/reports/{YYMMDD}-social-photos-{topic}.md`.

Report structure:

```markdown
# Social Photos Design Report

## Overview
- Prompt/requirements: {original input}
- Platforms: {target platforms}
- Variations: {count}
- Style: {chosen style}

## Ideas Generated
1. **{Idea name}** — {brief description, rationale}
2. ...

## Design Decisions
- Color palette: {colors used, why}
- Typography: {fonts, sizes, why}
- Layout: {composition approach, why}
- Brand alignment: {how brand guidelines influenced design}

## Output Files
| File | Size | Platform | Preview |
|------|------|----------|---------|
| exports/{filename}.png | {WxH} | {platform} | {description} |

## Why This Works
- {Platform-specific reasoning}
- {Brand alignment reasoning}
- {Visual hierarchy reasoning}
- {Engagement potential reasoning}

## Recommendations
- {A/B test suggestions}
- {Platform-specific tips}
- {Iteration opportunities}
```

### Step 8: Organize Output

Organize all output files and reports:
- Move/copy exported PNGs to proper asset directories
- Ensure reports are in `plans/reports/` under the name from Step 7
- Clean up intermediate HTML files if requested
- Tag outputs with metadata (platform, size, concept name)

## Design Best Practices

### Platform-Specific Tips

- **Instagram** — Visual-first, minimal text (<20%), strong colors, lifestyle feel
- **Facebook** — Informative, can have more text, eye-catching in feed
- **Twitter/X** — Bold headlines, contrast for dark/light mode, clear message
- **LinkedIn** — Professional, clean, data-driven visuals, thought leadership
- **Pinterest** — Vertical format, text overlay on images, how-to style
- **YouTube** — Face close-ups perform best, bright colors, readable at small size
- **TikTok** — Trendy, energetic, bold typography, youth-oriented

### Art Direction Styles (Reuse from Banner)

| Style | Best For | Key Elements |
|-------|----------|--------------|
| Minimalist | SaaS, tech, luxury | Whitespace, single accent color, clean type |
| Bold Typography | Announcements, quotes | Large type, high contrast, minimal imagery |
| Gradient Mesh | Modern brands, apps | Fluid color transitions, floating elements |
| Photo-Based | Lifestyle, e-commerce | Hero image, subtle overlay, text on image |
| Geometric | Tech, fintech | Shapes, patterns, structured layouts |
| Glassmorphism | SaaS, modern apps | Frosted glass, blur effects, transparency |
| Flat Illustration | Education, health | Custom illustrations, friendly, approachable |
| Duotone | Creative, editorial | Two-color treatment on photos |
| Collage | Fashion, culture | Mixed media, overlapping elements |
| 3D/Isometric | Tech, product | Depth, shadows, modern perspective |

### Color & Contrast

- Ensure WCAG AA contrast ratio (4.5:1 min) for all text
- Test designs at 50% size to verify readability
- Consider platform dark/light mode compatibility
- Use brand primary color as dominant, secondary as accent

### Typography Hierarchy

| Element | Min Size (at 1080px) | Weight |
|---------|---------------------|--------|
| Headline | 48px | Bold/Black |
| Subheadline | 32px | Semibold |
| Body | 24px | Regular |
| Caption | 18px | Regular/Light |
| CTA | 28px | Bold |

## Security & Scope

This sub-skill handles social media image design only. Does NOT handle:
- Video content creation
- Animation/motion graphics
- Print production files (CMYK, bleed)
- Direct social media posting/scheduling
- AI image generation (supply images, or generate them with a separate authorized capability)



---

## `scripts/cip/core.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIP Design Core - BM25 search engine for Corporate Identity Program design guidelines
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "cip"
MAX_RESULTS = 3

CSV_CONFIG = {
    "deliverable": {
        "file": "deliverables.csv",
        "search_cols": ["Deliverable", "Category", "Keywords", "Description", "Mockup Context"],
        "output_cols": ["Deliverable", "Category", "Keywords", "Description", "Dimensions", "File Format", "Logo Placement", "Color Usage", "Typography Notes", "Mockup Context", "Best Practices", "Avoid"]
    },
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Name", "Category", "Keywords", "Description", "Mood"],
        "output_cols": ["Style Name", "Category", "Keywords", "Description", "Primary Colors", "Secondary Colors", "Typography", "Materials", "Finishes", "Mood", "Best For", "Avoid For"]
    },
    "industry": {
        "file": "industries.csv",
        "search_cols": ["Industry", "Keywords", "CIP Style", "Mood"],
        "output_cols": ["Industry", "Keywords", "CIP Style", "Primary Colors", "Secondary Colors", "Typography", "Key Deliverables", "Mood", "Best Practices", "Avoid"]
    },
    "mockup": {
        "file": "mockup-contexts.csv",
        "search_cols": ["Context Name", "Category", "Keywords", "Scene Description"],
        "output_cols": ["Context Name", "Category", "Keywords", "Scene Description", "Lighting", "Environment", "Props", "Camera Angle", "Background", "Style Notes", "Best For", "Prompt Modifiers"]
    }
}


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
        "deliverable": ["card", "letterhead", "envelope", "folder", "shirt", "cap", "badge", "signage", "vehicle", "car", "van", "stationery", "uniform", "merchandise", "packaging", "banner", "booth"],
        "style": ["style", "minimal", "modern", "luxury", "vintage", "industrial", "elegant", "bold", "corporate", "organic", "playful"],
        "industry": ["tech", "finance", "legal", "healthcare", "hospitality", "food", "fashion", "retail", "construction", "logistics"],
        "mockup": ["mockup", "scene", "context", "photo", "shot", "lighting", "background", "studio", "lifestyle"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "deliverable"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["deliverable"])
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
    """Search across all domains and combine results"""
    all_results = {}
    for domain in CSV_CONFIG.keys():
        result = search(query, domain, max_results)
        if result.get("results"):
            all_results[domain] = result["results"]
    return all_results


def get_cip_brief(brand_name, industry_query, style_query=None):
    """Generate a comprehensive CIP brief for a brand"""
    # Search industry
    industry_results = search(industry_query, "industry", 1)
    industry = industry_results.get("results", [{}])[0] if industry_results.get("results") else {}

    # Search style (use industry style if not specified)
    style_query = style_query or industry.get("CIP Style", "corporate minimal")
    style_results = search(style_query, "style", 1)
    style = style_results.get("results", [{}])[0] if style_results.get("results") else {}

    # Get recommended deliverables for the industry
    key_deliverables = industry.get("Key Deliverables", "").split()
    deliverable_results = []
    for d in key_deliverables[:5]:
        result = search(d, "deliverable", 1)
        if result.get("results"):
            deliverable_results.append(result["results"][0])

    return {
        "brand_name": brand_name,
        "industry": industry,
        "style": style,
        "recommended_deliverables": deliverable_results,
        "color_system": {
            "primary": style.get("Primary Colors", industry.get("Primary Colors", "")),
            "secondary": style.get("Secondary Colors", industry.get("Secondary Colors", ""))
        },
        "typography": style.get("Typography", industry.get("Typography", "")),
        "materials": style.get("Materials", ""),
        "finishes": style.get("Finishes", "")
    }
````



---

## `scripts/cip/generate.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIP Design Generator - Generate corporate identity mockups using Gemini Nano Banana

Uses Gemini's native image generation (Nano Banana Flash/Pro) for high-quality mockups.
Supports text-and-image-to-image generation for using actual brand logos.

- gemini-2.5-flash-image: Fast generation, cost-effective (default)
- gemini-3-pro-image: Pro quality, 4K text rendering

Set GEMINI_FLASH_IMAGE_MODEL or GEMINI_PRO_IMAGE_MODEL to use another Gemini
model id, for example when Google retires one of these.

Image Editing (text-and-image-to-image):
  When --logo is provided, the script uses Gemini's image editing capability
  to incorporate the actual logo into CIP mockups instead of generating one.

Each mockup is saved with the extension of the image type Gemini returns
(.png, .jpg or .webp). Exit status is 1 when nothing was generated: a failed
single deliverable, or a set where every deliverable failed. A set where some
deliverables succeed exits 0 and reports how many were generated.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent))
from core import search, get_cip_brief


def load_logo_image(logo_path):
    """Load logo image using PIL for Gemini image editing"""
    try:
        from PIL import Image
    except ImportError:
        print("Error: pillow package not installed.")
        print("Install with: pip install pillow")
        return None

    logo_path = Path(logo_path)
    if not logo_path.exists():
        print(f"Error: Logo file not found: {logo_path}")
        return None

    try:
        img = Image.open(logo_path)
        # Convert to RGB if necessary (Gemini works best with RGB)
        if img.mode in ('RGBA', 'P'):
            # Create white background for transparent images
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
            else:
                background.paste(img)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        return img
    except Exception as e:
        print(f"Error loading logo: {e}")
        return None

# Load environment variables
def load_env():
    """Load environment variables from .env files"""
    env_paths = [
        Path(__file__).parent.parent.parent / ".env",
        Path.home() / ".claude" / "skills" / ".env",
        Path.home() / ".claude" / ".env"
    ]
    for env_path in env_paths:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        if key not in os.environ:
                            os.environ[key] = value.strip('"\'')

load_env()

# Model options (read after load_env so .env files can override the ids)
MODELS = {
    "flash": os.environ.get("GEMINI_FLASH_IMAGE_MODEL") or "gemini-2.5-flash-image",  # Nano Banana Flash - fast, default
    "pro": os.environ.get("GEMINI_PRO_IMAGE_MODEL") or "gemini-3-pro-image"  # Nano Banana Pro - quality, 4K text
}
DEFAULT_MODEL = "flash"

# File extensions for the image types Gemini returns as inline data
IMAGE_EXTENSIONS = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}


def build_cip_prompt(deliverable, brand_name, style=None, industry=None, mockup=None, use_logo_image=False):
    """Build an optimized prompt for CIP mockup generation

    Args:
        deliverable: Type of deliverable (business card, letterhead, etc.)
        brand_name: Name of the brand
        style: Design style preference
        industry: Industry for style recommendations
        mockup: Mockup context override
        use_logo_image: If True, prompt is optimized for image editing with logo
    """

    # Get deliverable details
    deliverable_info = search(deliverable, "deliverable", 1)
    deliverable_data = deliverable_info.get("results", [{}])[0] if deliverable_info.get("results") else {}

    # Get style details
    style_info = search(style or "corporate minimal", "style", 1) if style else {}
    style_data = style_info.get("results", [{}])[0] if style_info.get("results") else {}

    # Get industry details
    industry_info = search(industry or "technology", "industry", 1) if industry else {}
    industry_data = industry_info.get("results", [{}])[0] if industry_info.get("results") else {}

    # Get mockup context
    mockup_context = deliverable_data.get("Mockup Context", "clean professional")
    if mockup:
        mockup_info = search(mockup, "mockup", 1)
        if mockup_info.get("results"):
            mockup_data = mockup_info["results"][0]
            mockup_context = mockup_data.get("Scene Description", mockup_context)

    # Build prompt components
    deliverable_name = deliverable_data.get("Deliverable", deliverable)
    description = deliverable_data.get("Description", "")
    dimensions = deliverable_data.get("Dimensions", "")
    logo_placement = deliverable_data.get("Logo Placement", "center")

    style_name = style_data.get("Style Name", style or "corporate")
    primary_colors = style_data.get("Primary Colors", industry_data.get("Primary Colors", "#0F172A #FFFFFF"))
    typography = style_data.get("Typography", industry_data.get("Typography", "clean sans-serif"))
    materials = style_data.get("Materials", "premium quality")
    finishes = style_data.get("Finishes", "professional")

    mood = style_data.get("Mood", industry_data.get("Mood", "professional"))

    # Construct the prompt - different for image editing vs pure generation
    if use_logo_image:
        # Image editing prompt: instructs to USE the provided logo image
        prompt_parts = [
            f"Create a professional corporate identity mockup photograph of a {deliverable_name}",
            f"Use the EXACT logo from the provided image - do NOT modify or recreate the logo",
            f"The logo MUST appear exactly as shown in the input image",
            f"Place the logo on the {deliverable_name} at: {logo_placement}",
            f"Brand name: '{brand_name}'",
            f"{description}" if description else "",
            f"Design style: {style_name}",
            f"Color scheme matching the logo colors",
            f"Materials: {materials} with {finishes} finish",
            f"Setting: {mockup_context}",
            f"Mood: {mood}",
            "Photorealistic product photography",
            "Soft natural lighting, professional studio quality",
            "8K resolution, sharp details"
        ]
    else:
        # Pure text-to-image prompt
        prompt_parts = [
            f"Professional corporate identity mockup photograph",
            f"showing {deliverable_name} for brand '{brand_name}'",
            f"{description}" if description else "",
            f"{style_name} design style",
            f"using colors {primary_colors}",
            f"{typography} typography",
            f"logo placement: {logo_placement}",
            f"{materials} materials with {finishes} finish",
            f"{mockup_context} setting",
            f"{mood} mood",
            "photorealistic product photography",
            "soft natural lighting",
            "high quality professional shot",
            "8k resolution detailed"
        ]

    prompt = ", ".join([p for p in prompt_parts if p])

    return {
        "prompt": prompt,
        "deliverable": deliverable_name,
        "style": style_name,
        "brand": brand_name,
        "colors": primary_colors,
        "mockup_context": mockup_context,
        "logo_placement": logo_placement
    }


def generate_with_nano_banana(prompt_data, output_dir=None, model_key="flash", aspect_ratio="1:1", logo_image=None):
    """Generate image using Gemini Nano Banana (native image generation)

    Supports two modes:
    1. Text-to-image: Pure prompt-based generation (logo_image=None)
    2. Image editing: Text-and-image-to-image using provided logo (logo_image=PIL.Image)

    Models:
    - flash: gemini-2.5-flash-image (fast, cost-effective) - DEFAULT
    - pro: gemini-3-pro-image (quality, 4K text rendering)

    Args:
        prompt_data: Dict with prompt, deliverable, brand, etc.
        output_dir: Output directory for generated images
        model_key: 'flash' or 'pro'
        aspect_ratio: Output aspect ratio (1:1, 16:9, etc.)
        logo_image: PIL.Image object of the brand logo for image editing mode
    """
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("Error: google-genai package not installed.")
        print("Install with: pip install google-genai")
        return None

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY or GOOGLE_API_KEY not set")
        return None

    client = genai.Client(api_key=api_key)

    prompt = prompt_data["prompt"]
    model_name = MODELS.get(model_key, MODELS[DEFAULT_MODEL])

    # Determine mode
    mode = "image-editing" if logo_image else "text-to-image"

    print(f"\n🎨 Generating CIP mockup...")
    print(f"   Mode: {mode}")
    print(f"   Deliverable: {prompt_data['deliverable']}")
    print(f"   Brand: {prompt_data['brand']}")
    print(f"   Style: {prompt_data['style']}")
    print(f"   Model: {model_name}")
    print(f"   Context: {prompt_data['mockup_context']}")
    if logo_image:
        print(f"   Logo: Using provided image ({logo_image.size[0]}x{logo_image.size[1]})")

    try:
        # Build contents: either just prompt or [prompt, image] for image editing
        if logo_image:
            # Image editing mode: pass both prompt and logo image
            contents = [prompt, logo_image]
        else:
            # Text-to-image mode: just the prompt
            contents = prompt

        # Use generate_content with response_modalities=['IMAGE'] for Nano Banana
        response = client.models.generate_content(
            model=model_name,
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=['IMAGE'],  # Uppercase required
                image_config=types.ImageConfig(
                    aspect_ratio=aspect_ratio
                )
            )
        )

        # Extract image from response
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'inline_data') and part.inline_data:
                    # Save image
                    output_dir = output_dir or Path.cwd()
                    output_dir = Path(output_dir)
                    output_dir.mkdir(parents=True, exist_ok=True)

                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    brand_slug = prompt_data["brand"].lower().replace(" ", "-")
                    deliverable_slug = prompt_data["deliverable"].lower().replace(" ", "-")
                    mime_type = (part.inline_data.mime_type or "").split(";")[0].strip().lower()
                    extension = IMAGE_EXTENSIONS.get(mime_type, ".png")
                    filename = f"{brand_slug}-{deliverable_slug}-{timestamp}{extension}"
                    filepath = output_dir / filename

                    image_data = part.inline_data.data
                    with open(filepath, "wb") as f:
                        f.write(image_data)

                    print(f"\n✅ Generated: {filepath}")
                    return str(filepath)

        print("No image generated in response")
        return None

    except Exception as e:
        print(f"Error generating image: {e}")
        return None


def generate_cip_set(brand_name, industry, style=None, deliverables=None, output_dir=None, model_key="flash", logo_path=None, aspect_ratio="1:1"):
    """Generate a complete CIP set for a brand

    Args:
        brand_name: Brand name to generate for
        industry: Industry type for style recommendations
        style: Optional specific style override
        deliverables: List of deliverables to generate (default: core set)
        output_dir: Output directory for images
        model_key: 'flash' (fast) or 'pro' (quality)
        logo_path: Path to brand logo image for image editing mode
        aspect_ratio: Output aspect ratio
    """

    # Load logo image if provided
    logo_image = None
    if logo_path:
        logo_image = load_logo_image(logo_path)
        if not logo_image:
            print("Warning: Could not load logo, falling back to text-to-image mode")

    # Get CIP brief for the brand
    brief = get_cip_brief(brand_name, industry, style)

    # Default deliverables if not specified
    if not deliverables:
        deliverables = ["business card", "letterhead", "office signage", "vehicle", "polo shirt"]

    results = []
    for deliverable in deliverables:
        prompt_data = build_cip_prompt(
            deliverable=deliverable,
            brand_name=brand_name,
            style=brief.get("style", {}).get("Style Name"),
            industry=industry,
            use_logo_image=(logo_image is not None)
        )

        filepath = generate_with_nano_banana(
            prompt_data,
            output_dir,
            model_key=model_key,
            aspect_ratio=aspect_ratio,
            logo_image=logo_image
        )
        if filepath:
            results.append({
                "deliverable": deliverable,
                "filepath": filepath,
                "prompt": prompt_data["prompt"]
            })

    return results


def check_logo_required(brand_name, skip_prompt=False):
    """Check if logo is required and suggest logo-design skill if not provided

    Returns:
        str: 'continue' to proceed without logo, 'generate' to use logo-design skill, 'exit' to abort
    """
    if skip_prompt:
        return 'continue'

    print(f"\n⚠️  No logo image provided for '{brand_name}'")
    print("   Without a logo, AI will generate its own interpretation of the brand logo.")
    print("")
    print("   Options:")
    print("   1. Continue without logo (AI-generated logo interpretation)")
    print("   2. Generate a logo first using 'logo-design' skill")
    print("   3. Exit and provide a logo path with --logo")
    print("")

    try:
        choice = input("   Enter choice [1/2/3] (default: 1): ").strip()
        if choice == '2':
            return 'generate'
        elif choice == '3':
            return 'exit'
        return 'continue'
    except (EOFError, KeyboardInterrupt):
        return 'continue'


def main():
    parser = argparse.ArgumentParser(
        description="Generate CIP mockups using Gemini Nano Banana",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate with brand logo (RECOMMENDED)
  python generate.py --brand "TopGroup" --logo /path/to/logo.png --deliverable "business card"

  # Generate CIP set with logo
  python generate.py --brand "TopGroup" --logo /path/to/logo.png --industry "consulting" --set

  # Generate without logo (AI interprets brand)
  python generate.py --brand "TechFlow" --deliverable "business card" --no-logo-prompt

  # Generate with Pro model (higher quality, 4K text)
  python generate.py --brand "TechFlow" --logo logo.png --deliverable "business card" --model pro

  # Specify output directory and aspect ratio
  python generate.py --brand "MyBrand" --logo logo.png --deliverable "vehicle" --output ./mockups --ratio 16:9

Models:
  flash (default): gemini-2.5-flash-image - Fast, cost-effective
  pro: gemini-3-pro-image - Quality, 4K text rendering

Image Editing Mode:
  When --logo is provided, uses Gemini's text-and-image-to-image capability
  to incorporate your ACTUAL logo into the CIP mockups.
        """
    )

    parser.add_argument("--brand", "-b", required=True, help="Brand name")
    parser.add_argument("--logo", "-l", help="Path to brand logo image (enables image editing mode)")
    parser.add_argument("--deliverable", "-d", help="Single deliverable to generate")
    parser.add_argument("--deliverables", help="Comma-separated list of deliverables")
    parser.add_argument("--industry", "-i", default="technology", help="Industry type")
    parser.add_argument("--style", "-s", help="Design style")
    parser.add_argument("--mockup", "-m", help="Mockup context")
    parser.add_argument("--set", action="store_true", help="Generate full CIP set")
    parser.add_argument("--output", "-o", help="Output directory")
    parser.add_argument("--model", default="flash", choices=["flash", "pro"], help="Model: flash (fast) or pro (quality)")
    parser.add_argument("--ratio", default="1:1", help="Aspect ratio (1:1, 16:9, 4:3, etc.)")
    parser.add_argument("--prompt-only", action="store_true", help="Only show prompt, don't generate")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    parser.add_argument("--no-logo-prompt", action="store_true", help="Skip logo prompt, proceed without logo")

    args = parser.parse_args()

    # Check if logo is provided, prompt user if not
    logo_image = None
    if args.logo:
        logo_image = load_logo_image(args.logo)
        if not logo_image:
            print("Error: Could not load logo image")
            sys.exit(1)
    elif not args.prompt_only:
        # No logo provided - ask user what to do
        action = check_logo_required(args.brand, skip_prompt=args.no_logo_prompt)
        if action == 'generate':
            print("\n💡 To generate a logo, use the logo-design skill:")
            # Resolved from this file so the hint is correct from any cwd and in
            # every install layout (plugin cache, project or --global install).
            logo_script = Path(__file__).resolve().parents[1] / "logo" / "generate.py"
            print(f"   python \"{logo_script}\" --brand \"{args.brand}\" --industry \"{args.industry}\"")
            print("\n   Then re-run this command with --logo <generated_logo.png>")
            sys.exit(0)
        elif action == 'exit':
            print("\n   Provide logo with: --logo /path/to/your/logo.png")
            sys.exit(0)
        # else: continue without logo

    use_logo = logo_image is not None

    if args.set or args.deliverables:
        # Generate multiple deliverables
        deliverables = args.deliverables.split(",") if args.deliverables else None

        if args.prompt_only:
            results = []
            deliverables = deliverables or ["business card", "letterhead", "office signage", "vehicle", "polo shirt"]
            for d in deliverables:
                prompt_data = build_cip_prompt(d, args.brand, args.style, args.industry, args.mockup, use_logo_image=use_logo)
                results.append(prompt_data)
            if args.json:
                print(json.dumps(results, indent=2))
            else:
                for r in results:
                    print(f"\n{r['deliverable']}:\n{r['prompt']}\n")
        else:
            results = generate_cip_set(
                args.brand, args.industry, args.style, deliverables, args.output,
                model_key=args.model, logo_path=args.logo, aspect_ratio=args.ratio
            )
            if args.json:
                print(json.dumps(results, indent=2))
            else:
                print(f"\n✅ Generated {len(results)} CIP mockups")
            if not results:
                sys.exit(1)
    else:
        # Generate single deliverable
        deliverable = args.deliverable or "business card"
        prompt_data = build_cip_prompt(deliverable, args.brand, args.style, args.industry, args.mockup, use_logo_image=use_logo)

        if args.prompt_only:
            if args.json:
                print(json.dumps(prompt_data, indent=2))
            else:
                print(f"\nPrompt:\n{prompt_data['prompt']}")
        else:
            filepath = generate_with_nano_banana(
                prompt_data, args.output, model_key=args.model,
                aspect_ratio=args.ratio, logo_image=logo_image
            )
            if args.json:
                print(json.dumps({"filepath": filepath, **prompt_data}, indent=2))
            if filepath is None:
                sys.exit(1)


if __name__ == "__main__":
    main()
````



---

## `scripts/cip/render-html.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIP HTML Presentation Renderer

Generates a professional HTML presentation from CIP mockup images
with detailed descriptions, concepts, and brand guidelines.
"""

import argparse
import json
import os
import sys
import base64
from pathlib import Path
from datetime import datetime

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent))
from core import search, get_cip_brief

# Deliverable descriptions for presentation
DELIVERABLE_INFO = {
    "business card": {
        "title": "Business Card",
        "concept": "First impression touchpoint for professional networking",
        "purpose": "Creates memorable brand recall during business exchanges",
        "specs": "Standard 3.5 x 2 inches, premium paper stock"
    },
    "letterhead": {
        "title": "Letterhead",
        "concept": "Official correspondence identity",
        "purpose": "Establishes credibility and professionalism in written communications",
        "specs": "A4/Letter size, digital and print versions"
    },
    "document template": {
        "title": "Document Template",
        "concept": "Branded document system for internal and external use",
        "purpose": "Ensures consistent brand representation across all documents",
        "specs": "Multiple formats: Word, PDF, Google Docs compatible"
    },
    "reception signage": {
        "title": "Reception Signage",
        "concept": "Brand presence in physical office environment",
        "purpose": "Creates strong first impression for visitors and reinforces brand identity",
        "specs": "3D dimensional letters, backlit LED options, premium materials"
    },
    "office signage": {
        "title": "Office Signage",
        "concept": "Wayfinding and brand presence system",
        "purpose": "Guides visitors while maintaining consistent brand experience",
        "specs": "Modular system with directional and informational signs"
    },
    "polo shirt": {
        "title": "Polo Shirt",
        "concept": "Professional team apparel",
        "purpose": "Creates unified team identity and brand ambassadorship",
        "specs": "Premium pique cotton, embroidered logo on left chest"
    },
    "t-shirt": {
        "title": "T-Shirt",
        "concept": "Casual brand apparel",
        "purpose": "Extends brand reach through everyday wear and promotional events",
        "specs": "High-quality cotton, screen print or embroidery options"
    },
    "vehicle": {
        "title": "Vehicle Branding",
        "concept": "Mobile brand advertising",
        "purpose": "Transforms fleet into moving billboards for maximum visibility",
        "specs": "Partial or full wrap, vinyl graphics, weather-resistant"
    },
    "van": {
        "title": "Van Branding",
        "concept": "Commercial vehicle identity",
        "purpose": "Professional fleet presence for service and delivery operations",
        "specs": "Full wrap design, high-visibility contact information"
    },
    "car": {
        "title": "Car Branding",
        "concept": "Executive vehicle identity",
        "purpose": "Professional presence for corporate and sales teams",
        "specs": "Subtle branding, door panels and rear window"
    },
    "envelope": {
        "title": "Envelope",
        "concept": "Branded mail correspondence",
        "purpose": "Extends brand identity to all outgoing mail",
        "specs": "DL, C4, C5 sizes with logo placement"
    },
    "folder": {
        "title": "Presentation Folder",
        "concept": "Document organization with brand identity",
        "purpose": "Professional presentation of proposals and materials",
        "specs": "A4/Letter pocket folder with die-cut design"
    }
}


def get_image_base64(image_path):
    """Convert image to base64 for embedding in HTML"""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        print(f"Warning: Could not load image {image_path}: {e}")
        return None


def get_deliverable_info(filename):
    """Extract deliverable type from filename and get info"""
    filename_lower = filename.lower()
    for key, info in DELIVERABLE_INFO.items():
        if key.replace(" ", "-") in filename_lower or key.replace(" ", "_") in filename_lower:
            return info
    # Default info
    return {
        "title": filename.replace("-", " ").replace("_", " ").title(),
        "concept": "Brand identity application",
        "purpose": "Extends brand presence across touchpoints",
        "specs": "Custom specifications"
    }


def generate_html(brand_name, industry, images_dir, output_path=None, style=None):
    """Generate HTML presentation from CIP images"""

    images_dir = Path(images_dir)
    if not images_dir.exists():
        print(f"Error: Directory not found: {images_dir}")
        return None

    # Get all PNG images
    images = sorted(images_dir.glob("*.png"))
    if not images:
        print(f"Error: No PNG images found in {images_dir}")
        return None

    # Get CIP brief for brand info
    brief = get_cip_brief(brand_name, industry, style)
    style_info = brief.get("style", {})
    industry_info = brief.get("industry", {})

    # Build HTML
    html_parts = [f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{brand_name} - Corporate Identity Program</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #0a0a0a;
            color: #ffffff;
            line-height: 1.6;
        }}
        .hero {{
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, #1a1a2e 0%, #0a0a0a 100%);
        }}
        .hero h1 {{
            font-size: 4rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #ffffff 0%, #888888 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero .subtitle {{
            font-size: 1.5rem;
            color: #888;
            margin-bottom: 3rem;
        }}
        .hero .meta {{
            display: flex;
            gap: 3rem;
            flex-wrap: wrap;
            justify-content: center;
        }}
        .hero .meta-item {{
            text-align: center;
        }}
        .hero .meta-label {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #666;
            margin-bottom: 0.5rem;
        }}
        .hero .meta-value {{
            font-size: 1rem;
            color: #ccc;
        }}
        .section {{
            padding: 6rem 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .section-title {{
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #fff;
        }}
        .section-subtitle {{
            font-size: 1.1rem;
            color: #888;
            margin-bottom: 4rem;
            max-width: 600px;
        }}
        .deliverable {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            margin-bottom: 8rem;
            align-items: center;
        }}
        .deliverable:nth-child(even) {{
            direction: rtl;
        }}
        .deliverable:nth-child(even) > * {{
            direction: ltr;
        }}
        .deliverable-image {{
            position: relative;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
        }}
        .deliverable-image img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        .deliverable-content {{
            padding: 2rem 0;
        }}
        .deliverable-title {{
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: #fff;
        }}
        .deliverable-concept {{
            font-size: 1.1rem;
            color: #aaa;
            margin-bottom: 1.5rem;
            font-style: italic;
        }}
        .deliverable-purpose {{
            font-size: 1rem;
            color: #888;
            margin-bottom: 1.5rem;
            line-height: 1.8;
        }}
        .deliverable-specs {{
            display: inline-block;
            padding: 0.5rem 1rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 8px;
            font-size: 0.85rem;
            color: #666;
        }}
        .color-palette {{
            display: flex;
            gap: 1rem;
            margin-top: 2rem;
        }}
        .color-swatch {{
            width: 60px;
            height: 60px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }}
        .footer {{
            text-align: center;
            padding: 4rem 2rem;
            border-top: 1px solid #222;
            color: #666;
        }}
        .footer p {{
            margin-bottom: 0.5rem;
        }}
        @media (max-width: 900px) {{
            .hero h1 {{
                font-size: 2.5rem;
            }}
            .deliverable {{
                grid-template-columns: 1fr;
                gap: 2rem;
            }}
            .deliverable:nth-child(even) {{
                direction: ltr;
            }}
        }}
    </style>
</head>
<body>
    <section class="hero">
        <h1>{brand_name}</h1>
        <p class="subtitle">Corporate Identity Program</p>
        <div class="meta">
            <div class="meta-item">
                <div class="meta-label">Industry</div>
                <div class="meta-value">{industry_info.get("Industry", industry.title())}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Style</div>
                <div class="meta-value">{style_info.get("Style Name", "Corporate")}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Mood</div>
                <div class="meta-value">{style_info.get("Mood", "Professional")}</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Deliverables</div>
                <div class="meta-value">{len(images)} Items</div>
            </div>
        </div>
    </section>

    <section class="section">
        <h2 class="section-title">Brand Applications</h2>
        <p class="section-subtitle">
            Comprehensive identity system designed to maintain consistency
            across all brand touchpoints and communications.
        </p>
''']

    # Add each deliverable
    for i, image_path in enumerate(images):
        info = get_deliverable_info(image_path.stem)
        img_base64 = get_image_base64(image_path)

        if img_base64:
            img_src = f"data:image/png;base64,{img_base64}"
        else:
            img_src = str(image_path)

        html_parts.append(f'''
        <div class="deliverable">
            <div class="deliverable-image">
                <img src="{img_src}" alt="{info['title']}" loading="lazy">
            </div>
            <div class="deliverable-content">
                <h3 class="deliverable-title">{info['title']}</h3>
                <p class="deliverable-concept">{info['concept']}</p>
                <p class="deliverable-purpose">{info['purpose']}</p>
                <span class="deliverable-specs">{info['specs']}</span>
            </div>
        </div>
''')

    # Close HTML
    html_parts.append(f'''
    </section>

    <footer class="footer">
        <p><strong>{brand_name}</strong> Corporate Identity Program</p>
        <p>Generated on {datetime.now().strftime("%B %d, %Y")}</p>
        <p style="margin-top: 1rem; font-size: 0.8rem;">Powered by CIP Design Skill</p>
    </footer>
</body>
</html>
''')

    html_content = "".join(html_parts)

    # Save HTML
    output_path = output_path or images_dir / f"{brand_name.lower().replace(' ', '-')}-cip-presentation.html"
    output_path = Path(output_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ HTML presentation generated: {output_path}")
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate HTML presentation from CIP mockups",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate HTML from CIP images directory
  python render-html.py --brand "TopGroup" --industry "consulting" --images ./topgroup-cip

  # Specify output path
  python render-html.py --brand "TopGroup" --industry "consulting" --images ./cip --output presentation.html
        """
    )

    parser.add_argument("--brand", "-b", required=True, help="Brand name")
    parser.add_argument("--industry", "-i", default="technology", help="Industry type")
    parser.add_argument("--style", "-s", help="Design style")
    parser.add_argument("--images", required=True, help="Directory containing CIP mockup images")
    parser.add_argument("--output", "-o", help="Output HTML file path")

    args = parser.parse_args()

    generate_html(
        brand_name=args.brand,
        industry=args.industry,
        images_dir=args.images,
        output_path=args.output,
        style=args.style
    )


if __name__ == "__main__":
    main()
````



---

## `scripts/cip/search.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CIP Design Search CLI - Search corporate identity design guidelines
"""

import argparse
import json
import sys
from pathlib import Path

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent))
from core import search, search_all, get_cip_brief, CSV_CONFIG


def format_results(results, domain):
    """Format search results for display"""
    if not results:
        return "No results found."

    output = []
    for i, item in enumerate(results, 1):
        output.append(f"\n{'='*60}")
        output.append(f"Result {i}:")
        for key, value in item.items():
            if value:
                output.append(f"  {key}: {value}")
    return "\n".join(output)


def format_brief(brief):
    """Format CIP brief for display"""
    output = []
    output.append(f"\n{'='*60}")
    output.append(f"CIP DESIGN BRIEF: {brief['brand_name']}")
    output.append(f"{'='*60}")

    if brief.get("industry"):
        output.append(f"\n📊 INDUSTRY: {brief['industry'].get('Industry', 'N/A')}")
        output.append(f"   Style: {brief['industry'].get('CIP Style', 'N/A')}")
        output.append(f"   Mood: {brief['industry'].get('Mood', 'N/A')}")

    if brief.get("style"):
        output.append(f"\n🎨 DESIGN STYLE: {brief['style'].get('Style Name', 'N/A')}")
        output.append(f"   Description: {brief['style'].get('Description', 'N/A')}")
        output.append(f"   Materials: {brief['style'].get('Materials', 'N/A')}")
        output.append(f"   Finishes: {brief['style'].get('Finishes', 'N/A')}")

    if brief.get("color_system"):
        output.append(f"\n🎯 COLOR SYSTEM:")
        output.append(f"   Primary: {brief['color_system'].get('primary', 'N/A')}")
        output.append(f"   Secondary: {brief['color_system'].get('secondary', 'N/A')}")

    output.append(f"\n✏️ TYPOGRAPHY: {brief.get('typography', 'N/A')}")

    if brief.get("recommended_deliverables"):
        output.append(f"\n📦 RECOMMENDED DELIVERABLES:")
        for d in brief["recommended_deliverables"]:
            output.append(f"   • {d.get('Deliverable', 'N/A')}: {d.get('Description', '')[:60]}...")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Search CIP design guidelines",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search deliverables
  python search.py "business card"

  # Search specific domain
  python search.py "luxury elegant" --domain style

  # Generate CIP brief
  python search.py "tech startup" --cip-brief -b "TechFlow"

  # Search all domains
  python search.py "corporate professional" --all

  # JSON output
  python search.py "vehicle branding" --json
        """
    )

    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()),
                        help="Search domain (auto-detected if not specified)")
    parser.add_argument("--max", "-m", type=int, default=3, help="Max results (default: 3)")
    parser.add_argument("--all", "-a", action="store_true", help="Search all domains")
    parser.add_argument("--cip-brief", "-c", action="store_true", help="Generate CIP brief")
    parser.add_argument("--brand", "-b", default="BrandName", help="Brand name for CIP brief")
    parser.add_argument("--style", "-s", help="Style override for CIP brief")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.cip_brief:
        brief = get_cip_brief(args.brand, args.query, args.style)
        if args.json:
            print(json.dumps(brief, indent=2))
        else:
            print(format_brief(brief))
    elif args.all:
        results = search_all(args.query, args.max)
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            for domain, items in results.items():
                print(f"\n{'#'*60}")
                print(f"# {domain.upper()}")
                print(format_results(items, domain))
    else:
        result = search(args.query, args.domain, args.max)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\nDomain: {result['domain']}")
            print(f"Query: {result['query']}")
            print(f"Results: {result['count']}")
            print(format_results(result.get("results", []), result["domain"]))


if __name__ == "__main__":
    main()
````



---

## `scripts/icon/generate.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icon Generation Script using Gemini 3.1 Pro Preview API
Generates SVG icons via text generation (SVG is XML text format)

Model: gemini-3.1-pro-preview - best thinking, token efficiency, factual consistency

Usage:
    python generate.py --prompt "settings gear icon" --style outlined
    python generate.py --prompt "shopping cart" --style filled --color "#6366F1"
    python generate.py --name "dashboard" --category navigation --style duotone
    python generate.py --prompt "cloud upload" --batch 4 --output-dir ./icons
    python generate.py --prompt "user profile" --sizes "16,24,32,48"
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime


def load_env():
    """Load .env files in priority order"""
    env_paths = [
        Path(__file__).parent.parent.parent / ".env",
        Path.home() / ".claude" / "skills" / ".env",
        Path.home() / ".claude" / ".env"
    ]
    for env_path in env_paths:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        if key not in os.environ:
                            os.environ[key] = value.strip('"\'')

load_env()

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai package not installed.")
    print("Install with: pip install google-genai")
    sys.exit(1)


# ============ CONFIGURATION ============
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL = "gemini-3.1-pro-preview"

# Icon styles with SVG-specific instructions
ICON_STYLES = {
    "outlined": "outlined stroke icons, 2px stroke width, no fill, clean open paths",
    "filled": "solid filled icons, no stroke, flat color fills, bold shapes",
    "duotone": "duotone style with primary color at full opacity and secondary color at 30% opacity, layered shapes",
    "thin": "thin line icons, 1px or 1.5px stroke width, delicate minimalist lines",
    "bold": "bold thick line icons, 3px stroke width, heavy weight, impactful",
    "rounded": "rounded icons with round line caps and joins, soft corners, friendly feel",
    "sharp": "sharp angular icons, square line caps and mitered joins, precise edges",
    "flat": "flat design icons, solid fills, no gradients or shadows, geometric simplicity",
    "gradient": "linear or radial gradient fills, modern vibrant color transitions",
    "glassmorphism": "glassmorphism style with semi-transparent fills, blur backdrop effect simulation, frosted glass",
    "pixel": "pixel art style icons on a grid, retro 8-bit aesthetic, crisp edges",
    "hand-drawn": "hand-drawn sketch style, slightly irregular strokes, organic feel, imperfect lines",
    "isometric": "isometric 3D projection, 30-degree angles, dimensional depth",
    "glyph": "simple glyph style, single solid shape, minimal detail, pictogram",
    "animated-ready": "animated-ready SVG with named groups and IDs for CSS/JS animation targets",
}

ICON_CATEGORIES = {
    "navigation": "arrows, menus, hamburger, chevrons, home, back, forward, breadcrumb",
    "action": "edit, delete, save, download, upload, share, copy, paste, print, search",
    "communication": "email, chat, phone, video call, notification, bell, message bubble",
    "media": "play, pause, stop, skip, volume, microphone, camera, image, gallery",
    "file": "document, folder, archive, attachment, cloud, database, storage",
    "user": "person, group, avatar, profile, settings, lock, key, shield",
    "commerce": "cart, bag, wallet, credit card, receipt, tag, gift, store",
    "data": "chart, graph, analytics, dashboard, table, filter, sort, calendar",
    "development": "code, terminal, bug, git, API, server, database, deploy",
    "social": "heart, star, thumbs up, bookmark, flag, trophy, badge, crown",
    "weather": "sun, moon, cloud, rain, snow, wind, thunder, temperature",
    "map": "pin, location, compass, globe, route, directions, map marker",
}

# SVG generation prompt template
SVG_PROMPT_TEMPLATE = """Generate a clean, production-ready SVG icon.

Requirements:
- Output ONLY valid SVG code, nothing else
- ViewBox: "0 0 {viewbox} {viewbox}"
- Use currentColor for strokes/fills (inherits CSS color)
- No embedded fonts or text elements unless specifically requested
- No raster images or external references
- Optimized paths with minimal nodes
- Accessible: include <title> element with icon description
{style_instructions}
{color_instructions}
{size_instructions}

Icon to generate: {prompt}

Output the SVG code only, wrapped in ```svg``` code block."""

SVG_BATCH_PROMPT_TEMPLATE = """Generate {count} distinct SVG icon variations for: {prompt}

Requirements for EACH icon:
- Output ONLY valid SVG code
- ViewBox: "0 0 {viewbox} {viewbox}"
- Use currentColor for strokes/fills (inherits CSS color)
- No embedded fonts, raster images, or external references
- Optimized paths with minimal nodes
- Include <title> element with icon description
{style_instructions}
{color_instructions}

Generate {count} different visual interpretations. Output each SVG in a separate ```svg``` code block.
Label each variation (e.g., "Variation 1: [brief description]")."""


def extract_svgs(text):
    """Extract SVG code blocks from model response"""
    svgs = []

    # Try ```svg code blocks first
    pattern = r'```svg\s*\n(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        svgs.extend(matches)

    # Fallback: try ```xml code blocks
    if not svgs:
        pattern = r'```xml\s*\n(.*?)```'
        matches = re.findall(pattern, text, re.DOTALL)
        svgs.extend(matches)

    # Fallback: try bare <svg> tags
    if not svgs:
        pattern = r'(<svg[^>]*>.*?</svg>)'
        matches = re.findall(pattern, text, re.DOTALL)
        svgs.extend(matches)

    # Clean up extracted SVGs
    cleaned = []
    for svg in svgs:
        svg = svg.strip()
        if not svg.startswith('<svg'):
            # Try to find <svg> within the extracted text
            match = re.search(r'(<svg[^>]*>.*?</svg>)', svg, re.DOTALL)
            if match:
                svg = match.group(1)
            else:
                continue
        cleaned.append(svg)

    return cleaned


def apply_color(svg_code, color):
    """Replace currentColor with specific color if provided"""
    if color:
        # Replace currentColor with the specified color
        svg_code = svg_code.replace('currentColor', color)
        # If no currentColor was present, add fill/stroke color
        if color not in svg_code:
            svg_code = svg_code.replace('<svg', f'<svg color="{color}"', 1)
    return svg_code


# Root <svg ...> opening tag; quoted attribute values may contain ">".
_SVG_ROOT_TAG = re.compile(r"""<svg\b(?:[^>"']|"[^"]*"|'[^']*')*>""")


# One token of an opening tag: name[=value], or a stray quoted string.
# Quoted values are consumed whole, so text inside them is never a name.
_TAG_ATTR = re.compile(
    r"""([^\s=/>"']+)(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s>"']+))?|"[^"]*"|'[^']*'""")


def _set_root_attr(tag, attr, value):
    """Set attr on a single <svg ...> opening tag, whatever quote style it uses."""
    for m in _TAG_ATTR.finditer(tag, len('<svg')):
        if m.group(1) == attr:
            return tag[:m.start()] + f'{attr}="{value}"' + tag[m.end():]
    return tag.replace('<svg', f'<svg {attr}="{value}"', 1)


def apply_viewbox_size(svg_code, size):
    """Set width/height on the root <svg> tag only, leaving the viewBox alone"""
    if size:
        match = _SVG_ROOT_TAG.search(svg_code)
        if match:
            tag = _set_root_attr(match.group(0), 'width', size)
            tag = _set_root_attr(tag, 'height', size)
            svg_code = svg_code[:match.start()] + tag + svg_code[match.end():]
    return svg_code


def _finish_reason(response):
    """Return the first candidate's finish reason as a string ('' if unknown)"""
    try:
        reason = response.candidates[0].finish_reason
    except (AttributeError, IndexError, TypeError):
        return ""
    return str(getattr(reason, "name", reason) or "")


def _response_text(response):
    """Collect the text of a response; '' when it has none (blocked, empty)"""
    text = getattr(response, 'text', None) or ""
    if not text:
        candidates = response.candidates or []
        content = candidates[0].content if candidates else None
        for part in (content.parts or []) if content else []:
            if getattr(part, 'text', None):
                text += part.text
    return text


def _report_no_svg(response, response_text, what="SVG"):
    """Say why no SVG came back: truncated, empty, or malformed output"""
    if "MAX_TOKENS" in _finish_reason(response):
        print("Error: output hit the token limit (finish_reason MAX_TOKENS) "
              "before the SVG was complete. Try a simpler prompt or style.")
    elif not response_text.strip():
        print("Error: model returned an empty response.")
    else:
        print(f"No valid {what} generated. Model response:")
        print(response_text[:500])


def generate_icon(prompt, style=None, category=None, name=None,
                  color=None, size=24, output_path=None, viewbox=24):
    """Generate a single SVG icon using Gemini 3.1 Pro Preview"""

    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not set")
        print("Set it with: export GEMINI_API_KEY='your-key'")
        return None

    client = genai.Client(api_key=GEMINI_API_KEY)

    # Build style instructions
    style_instructions = ""
    if style and style in ICON_STYLES:
        style_instructions = f"- Style: {ICON_STYLES[style]}"

    # Build color instructions
    color_instructions = "- Use currentColor for all strokes and fills"
    if color:
        color_instructions = f"- Use color: {color} for primary elements, currentColor for secondary"

    # Build size instructions
    size_instructions = f"- Design for {size}px display size, optimize detail level accordingly"

    # Build final prompt
    icon_prompt = prompt
    if category and category in ICON_CATEGORIES:
        icon_prompt = f"{prompt} (category: {ICON_CATEGORIES[category]})"
    if name:
        icon_prompt = f"'{name}' icon: {icon_prompt}"

    full_prompt = SVG_PROMPT_TEMPLATE.format(
        prompt=icon_prompt,
        viewbox=viewbox,
        style_instructions=style_instructions,
        color_instructions=color_instructions,
        size_instructions=size_instructions
    )

    print(f"Generating icon with {MODEL}...")
    print(f"Prompt: {prompt}")
    if style:
        print(f"Style: {style}")
    print()

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=16384,
            )
        )

        # Extract SVG from response
        response_text = _response_text(response)

        svgs = extract_svgs(response_text)

        if not svgs:
            _report_no_svg(response, response_text)
            return None

        svg_code = svgs[0]

        # Apply color if specified
        svg_code = apply_color(svg_code, color)

        # Apply size
        svg_code = apply_viewbox_size(svg_code, size)

        # Determine output path
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            slug = name or prompt.split()[0] if prompt else "icon"
            slug = re.sub(r'[^a-zA-Z0-9_-]', '_', slug.lower())
            style_suffix = f"_{style}" if style else ""
            output_path = f"{slug}{style_suffix}_{timestamp}.svg"

        # Save SVG
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(svg_code)

        print(f"Icon saved to: {output_path}")
        return output_path

    except Exception as e:
        print(f"Error generating icon: {e}")
        return None


def generate_batch(prompt, count, output_dir, style=None, color=None,
                   viewbox=24, name=None):
    """Generate multiple icon variations"""

    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY not set")
        return []

    client = genai.Client(api_key=GEMINI_API_KEY)
    os.makedirs(output_dir, exist_ok=True)

    # Build instructions
    style_instructions = ""
    if style and style in ICON_STYLES:
        style_instructions = f"- Style: {ICON_STYLES[style]}"

    color_instructions = "- Use currentColor for all strokes and fills"
    if color:
        color_instructions = f"- Use color: {color} for primary elements"

    full_prompt = SVG_BATCH_PROMPT_TEMPLATE.format(
        prompt=prompt,
        count=count,
        viewbox=viewbox,
        style_instructions=style_instructions,
        color_instructions=color_instructions
    )

    print(f"\n{'='*60}")
    print(f"  BATCH ICON GENERATION")
    print(f"  Model: {MODEL}")
    print(f"  Prompt: {prompt}")
    print(f"  Variants: {count}")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}\n")

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                temperature=0.9,
                max_output_tokens=16384,
            )
        )

        response_text = _response_text(response)

        svgs = extract_svgs(response_text)

        if not svgs:
            _report_no_svg(response, response_text, "SVGs")
            return []

        results = []
        slug = name or re.sub(r'[^a-zA-Z0-9_-]', '_', prompt.split()[0].lower())
        style_suffix = f"_{style}" if style else ""

        for i, svg_code in enumerate(svgs[:count]):
            svg_code = apply_color(svg_code, color)
            filename = f"{slug}{style_suffix}_{i+1:02d}.svg"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(svg_code)

            results.append(filepath)
            print(f"  [{i+1}/{len(svgs[:count])}] Saved: {filename}")

        if len(results) < count and "MAX_TOKENS" in _finish_reason(response):
            print("Warning: output hit the token limit (finish_reason MAX_TOKENS); "
                  "the last icon was cut off. Try fewer variants or a simpler prompt.")

        print(f"\n{'='*60}")
        print(f"  BATCH COMPLETE: {len(results)}/{count} icons generated")
        print(f"{'='*60}\n")

        return results

    except Exception as e:
        print(f"Error generating icons: {e}")
        return []


def generate_sizes(prompt, sizes, style=None, color=None, output_dir=None, name=None):
    """Generate same icon at multiple sizes"""
    if output_dir is None:
        output_dir = "."
    os.makedirs(output_dir, exist_ok=True)

    results = []
    slug = name or re.sub(r'[^a-zA-Z0-9_-]', '_', prompt.split()[0].lower())
    style_suffix = f"_{style}" if style else ""

    for size in sizes:
        print(f"Generating {size}px variant...")
        filename = f"{slug}{style_suffix}_{size}px.svg"
        filepath = os.path.join(output_dir, filename)

        result = generate_icon(
            prompt=prompt,
            style=style,
            color=color,
            size=size,
            output_path=filepath,
            viewbox=size
        )

        if result:
            results.append(result)

        time.sleep(1)

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Generate SVG icons using Gemini 3.1 Pro Preview"
    )
    parser.add_argument("--prompt", "-p", type=str, help="Icon description")
    parser.add_argument("--name", "-n", type=str, help="Icon name (for filename)")
    parser.add_argument("--style", "-s", choices=list(ICON_STYLES.keys()),
                        help="Icon style")
    parser.add_argument("--category", "-c", choices=list(ICON_CATEGORIES.keys()),
                        help="Icon category for context")
    parser.add_argument("--color", type=str,
                        help="Primary color (hex, e.g. #6366F1). Default: currentColor")
    parser.add_argument("--size", type=int, default=24,
                        help="Icon size in px (default: 24)")
    parser.add_argument("--viewbox", type=int, default=24,
                        help="SVG viewBox size (default: 24)")
    parser.add_argument("--output", "-o", type=str, help="Output file path")
    parser.add_argument("--output-dir", type=str, help="Output directory for batch")
    parser.add_argument("--batch", type=int,
                        help="Number of icon variants to generate")
    parser.add_argument("--sizes", type=str,
                        help="Comma-separated sizes (e.g. '16,24,32,48')")
    parser.add_argument("--list-styles", action="store_true",
                        help="List available icon styles")
    parser.add_argument("--list-categories", action="store_true",
                        help="List available icon categories")

    args = parser.parse_args()

    if args.list_styles:
        print("Available icon styles:")
        for style, desc in ICON_STYLES.items():
            print(f"  {style}: {desc[:70]}...")
        return

    if args.list_categories:
        print("Available icon categories:")
        for cat, desc in ICON_CATEGORIES.items():
            print(f"  {cat}: {desc}")
        return

    if not args.prompt and not args.name:
        parser.error("Either --prompt or --name is required")

    prompt = args.prompt or args.name

    # Multi-size mode
    if args.sizes:
        sizes = [int(s.strip()) for s in args.sizes.split(",")]
        generated = generate_sizes(
            prompt=prompt,
            sizes=sizes,
            style=args.style,
            color=args.color,
            output_dir=args.output_dir or "./icons",
            name=args.name
        )
    # Batch mode
    elif args.batch:
        output_dir = args.output_dir or "./icons"
        generated = generate_batch(
            prompt=prompt,
            count=args.batch,
            output_dir=output_dir,
            style=args.style,
            color=args.color,
            viewbox=args.viewbox,
            name=args.name
        )
    # Single icon
    else:
        generated = generate_icon(
            prompt=prompt,
            style=args.style,
            category=args.category,
            name=args.name,
            color=args.color,
            size=args.size,
            output_path=args.output,
            viewbox=args.viewbox
        )

    # Exit 1 when nothing was generated; a partly generated batch or size set exits 0
    if not generated:
        sys.exit(1)


if __name__ == "__main__":
    main()
````



---

## `scripts/logo/core.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logo Design Core - BM25 search engine for logo design guidelines
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "logo"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Name", "Category", "Keywords", "Best For"],
        "output_cols": ["Style Name", "Category", "Keywords", "Primary Colors", "Secondary Colors", "Typography", "Effects", "Best For", "Avoid For", "Complexity", "Era"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Palette Name", "Category", "Keywords", "Psychology", "Best For"],
        "output_cols": ["Palette Name", "Category", "Keywords", "Primary Hex", "Secondary Hex", "Accent Hex", "Background Hex", "Text Hex", "Psychology", "Best For", "Avoid For"]
    },
    "industry": {
        "file": "industries.csv",
        "search_cols": ["Industry", "Keywords", "Recommended Styles", "Mood"],
        "output_cols": ["Industry", "Keywords", "Recommended Styles", "Primary Colors", "Typography", "Common Symbols", "Mood", "Best Practices", "Avoid"]
    }
}


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
        "style": ["style", "minimalist", "vintage", "modern", "retro", "geometric", "abstract", "emblem", "badge", "wordmark", "mascot", "luxury", "playful", "corporate"],
        "color": ["color", "palette", "hex", "#", "rgb", "blue", "red", "green", "gold", "warm", "cool", "vibrant", "pastel"],
        "industry": ["tech", "healthcare", "finance", "legal", "restaurant", "food", "fashion", "beauty", "education", "sports", "fitness", "real estate", "crypto", "gaming"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
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
    """Search across all domains and combine results"""
    all_results = {}
    for domain in CSV_CONFIG.keys():
        result = search(query, domain, max_results)
        if result.get("results"):
            all_results[domain] = result["results"]
    return all_results
````



---

## `scripts/logo/generate.py`

````python
#!/usr/bin/env python3
"""Logo generation with Gemini, Atlas Cloud, or MuAPI.

Gemini remains the default provider. Atlas Cloud is opt-in with
``--provider atlas`` and uses its asynchronous image generation API. MuAPI is
opt-in with ``--provider muapi`` and uses its asynchronous image generation API
with the selected model's prompt/aspect-ratio contract.

Models:
- Nano Banana (default): gemini-2.5-flash-image - fast, high-volume, low-latency
- Nano Banana Pro (--pro): gemini-3-pro-image - professional quality, advanced reasoning
- MuAPI Nano Banana (--provider muapi): nano-banana - hosted asynchronous image generation

Set GEMINI_FLASH_IMAGE_MODEL or GEMINI_PRO_IMAGE_MODEL to use another Gemini
model id, for example when Google retires one of these.

Gemini returns PNG or JPEG data. The file gets the extension of the returned
type, so ``--output logo.png`` can be saved as ``logo.jpg``; the path actually
written is printed.

Exit status is 1 when nothing was generated: a failed single request, or a
batch where every variant failed. A batch where some variants succeed exits 0
and reports how many were generated.

Usage:
    python generate.py --prompt "tech startup logo minimalist blue"
    python generate.py --prompt "coffee shop vintage badge" --style vintage --output logo.png
    python generate.py --brand "TechFlow" --industry tech --style minimalist
    python generate.py --brand "TechFlow" --pro  # Use Nano Banana Pro model
    python generate.py --brand "TechFlow" --provider atlas
    python generate.py --brand "TechFlow" --provider muapi
    python generate.py --brand "TechFlow" --provider muapi --muapi-model nano-banana-pro

Batch mode (generates multiple variants):
    python generate.py --brand "Unikorn" --batch 9 --output-dir ./logos --pro
"""

import argparse
import ipaddress
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


# Load environment variables
def load_env():
    """Load .env files in priority order"""
    env_paths = [
        Path(__file__).parent.parent.parent / ".env",
        Path.home() / ".claude" / "skills" / ".env",
        Path.home() / ".claude" / ".env",
    ]

    for env_path in env_paths:
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        if key not in os.environ:
                            os.environ[key] = value.strip("\"'")


load_env()


# ============ CONFIGURATION ============
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
ATLASCLOUD_API_KEY = os.environ.get("ATLASCLOUD_API_KEY")
MUAPI_API_KEY = os.environ.get("MUAPI_API_KEY")

# Gemini "Nano Banana" model configurations for image generation
GEMINI_FLASH = (
    os.environ.get("GEMINI_FLASH_IMAGE_MODEL") or "gemini-2.5-flash-image"
)  # Nano Banana: fast, high-volume, low-latency
GEMINI_PRO = (
    os.environ.get("GEMINI_PRO_IMAGE_MODEL") or "gemini-3-pro-image"
)  # Nano Banana Pro: professional quality, advanced reasoning

# File extensions for the image types Gemini returns as inline data
IMAGE_EXTENSIONS = {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}

# Atlas Cloud model validated against the live model catalog and schema.
ATLAS_MODEL = "google/nano-banana-2-lite/text-to-image"
ATLAS_API_BASE = "https://api.atlascloud.ai/api/v1"
MUAPI_MODEL = "nano-banana"
MUAPI_MODELS = ("nano-banana", "nano-banana-pro")
MUAPI_API_BASE = "https://api.muapi.ai/api/v1"
HTTP_USER_AGENT = "ui-ux-pro-max/2.5 (logo generation)"
ATLAS_POLL_INTERVAL = 2
ATLAS_MAX_POLLS = 90
MUAPI_POLL_INTERVAL = 2
MUAPI_MAX_POLLS = 90

# Supported aspect ratios
ASPECT_RATIOS = ["1:1", "16:9", "9:16", "4:3", "3:4"]
DEFAULT_ASPECT_RATIO = "1:1"  # Square is ideal for logos

# Logo-specific prompt templates
LOGO_PROMPT_TEMPLATE = """Generate a professional logo image: {prompt}

Style requirements:
- Clean vector-style illustration suitable for a logo
- Simple, scalable design that works at any size
- Clear silhouette and recognizable shape
- Professional quality suitable for business use
- Centered composition on plain white or transparent background
- No text unless specifically requested
- High contrast and clear edges
- Square format, perfectly centered
- Output as a clean, high-quality logo image
"""

STYLE_MODIFIERS = {
    "minimalist": "minimalist, simple geometric shapes, clean lines, lots of white space, single color or limited palette",
    "vintage": "vintage, retro, badge style, distressed texture, heritage feel, warm earth tones",
    "modern": "modern, sleek, gradient colors, tech-forward, innovative feel",
    "luxury": "luxury, elegant, gold accents, refined, premium feel, serif typography",
    "playful": "playful, fun, colorful, friendly, approachable, rounded shapes",
    "corporate": "corporate, professional, trustworthy, stable, conservative colors",
    "organic": "organic, natural, flowing lines, earth tones, sustainable feel",
    "geometric": "geometric, abstract, mathematical precision, symmetrical",
    "hand-drawn": "hand-drawn, artisan, sketch-like, authentic, imperfect lines",
    "3d": "3D, dimensional, depth, shadows, isometric perspective",
    "abstract": "abstract mark, conceptual, symbolic, non-literal representation, artistic interpretation",
    "lettermark": "lettermark, single letter or initials, typographic, monogram style, distinctive character",
    "wordmark": "wordmark, logotype, custom typography, brand name as logo, distinctive lettering",
    "emblem": "emblem, badge, crest style, enclosed design, traditional, authoritative feel",
    "mascot": "mascot, character, friendly face, personified, memorable figure",
    "gradient": "gradient, color transition, vibrant, modern digital feel, smooth color flow",
    "lineart": "line art, single stroke, continuous line, elegant simplicity, wire-frame style",
    "negative-space": "negative space, clever use of white space, hidden meaning, dual imagery, optical illusion",
}

INDUSTRY_PROMPTS = {
    "tech": "technology company, digital, innovative, modern, circuit-like elements",
    "healthcare": "healthcare, medical, caring, trust, cross or heart symbol",
    "finance": "financial services, stable, trustworthy, growth, upward elements",
    "food": "food and beverage, appetizing, warm colors, welcoming",
    "fashion": "fashion brand, elegant, stylish, refined, artistic",
    "fitness": "fitness and sports, dynamic, energetic, powerful, movement",
    "eco": "eco-friendly, sustainable, natural, green, leaf or earth elements",
    "education": "education, knowledge, growth, learning, book or cap symbol",
    "real-estate": "real estate, property, home, roof or building silhouette",
    "creative": "creative agency, artistic, unique, expressive, colorful",
}


def enhance_prompt(base_prompt, style=None, industry=None, brand_name=None):
    """Enhance the logo prompt with style and industry modifiers"""
    prompt_parts = [base_prompt]

    if style and style in STYLE_MODIFIERS:
        prompt_parts.append(STYLE_MODIFIERS[style])

    if industry and industry in INDUSTRY_PROMPTS:
        prompt_parts.append(INDUSTRY_PROMPTS[industry])

    if brand_name:
        prompt_parts.insert(0, f"Logo for '{brand_name}':")

    combined = ", ".join(prompt_parts)
    return LOGO_PROMPT_TEMPLATE.format(prompt=combined)


class _SafeRedirectHandler(HTTPRedirectHandler):
    """Reject redirects to non-public or non-HTTPS destinations."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _validate_public_https_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _validate_public_https_url(url):
    parsed = urlparse(url)
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username
        or parsed.password
    ):
        raise ValueError("Provider returned an invalid media URL")

    hostname = parsed.hostname.lower().rstrip(".")
    if hostname == "localhost" or hostname.endswith(
        (".localhost", ".local", ".internal")
    ):
        raise ValueError("Provider media URL used a local hostname")

    try:
        ip = ipaddress.ip_address(hostname)
    except ValueError:
        return
    else:
        if not ip.is_global:
            raise ValueError("Provider media URL used a non-public address")


def _json_request(
    url, api_key, method="GET", payload=None, api_key_header="Authorization"
):
    if api_key_header == "Authorization":
        auth_value = f"Bearer {api_key}"
    elif api_key_header == "x-api-key":
        auth_value = api_key
    else:
        raise ValueError("Unsupported API key header")

    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = Request(
        url,
        data=body,
        method=method,
        headers={
            api_key_header: auth_value,
            "Accept": "application/json",
            "User-Agent": HTTP_USER_AGENT,
            **({"Content-Type": "application/json"} if body is not None else {}),
        },
    )
    try:
        with build_opener(_SafeRedirectHandler()).open(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Provider request failed ({exc.code}): {detail[:300]}"
        ) from exc
    except (URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Provider request failed: {exc}") from exc


def _atlas_prediction_data(response):
    if not isinstance(response, dict):
        raise TypeError("Atlas Cloud returned an invalid response")
    if response.get("code") not in (None, 0, 200):
        raise RuntimeError(response.get("message") or "Atlas Cloud request failed")
    data = response.get("data")
    if not isinstance(data, dict):
        raise TypeError("Atlas Cloud response did not include prediction data")
    return data


def _download_atlas_image(url, output_path):
    _download_image(url, output_path, "image provider")


def _download_image(url, output_path, provider_name):
    _validate_public_https_url(url)
    request = Request(
        url,
        headers={"Accept": "image/*", "User-Agent": HTTP_USER_AGENT},
    )
    try:
        with build_opener(_SafeRedirectHandler()).open(
            request, timeout=120
        ) as response:
            content_type = response.headers.get_content_type()
            if not content_type.startswith("image/"):
                raise RuntimeError(
                    f"{provider_name} output is not an image ({content_type})"
                )
            image_data = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        raise RuntimeError(f"Unable to download {provider_name} image: {exc}") from exc

    if not image_data:
        raise RuntimeError(f"{provider_name} returned an empty image")
    with open(output_path, "wb") as output_file:
        output_file.write(image_data)


def _generate_with_atlas(prompt, output_path, aspect_ratio, api_key, model):
    if not api_key:
        raise RuntimeError("ATLASCLOUD_API_KEY not set")

    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
    }
    response = _json_request(
        f"{ATLAS_API_BASE}/model/generateImage",
        api_key,
        method="POST",
        payload=payload,
    )
    data = _atlas_prediction_data(response)
    prediction_id = data.get("id")
    if not prediction_id:
        raise RuntimeError("Atlas Cloud did not return a prediction ID")

    for poll_number in range(ATLAS_MAX_POLLS + 1):
        status = str(data.get("status", "")).lower()
        if status == "completed":
            outputs = data.get("outputs")
            if (
                not isinstance(outputs, list)
                or not outputs
                or not isinstance(outputs[0], str)
            ):
                raise RuntimeError("Atlas Cloud completed without an image URL")
            _download_atlas_image(outputs[0], output_path)
            return
        if status in {"failed", "timeout", "canceled", "cancelled"}:
            raise RuntimeError(data.get("error") or f"Atlas Cloud prediction {status}")
        if poll_number == ATLAS_MAX_POLLS:
            break
        time.sleep(ATLAS_POLL_INTERVAL)
        data = _atlas_prediction_data(
            _json_request(
                f"{ATLAS_API_BASE}/model/prediction/{prediction_id}",
                api_key,
            )
        )

    raise RuntimeError("Atlas Cloud prediction timed out while polling")


def _muapi_response_objects(response):
    """Return the response and common MuAPI envelopes without guessing fields."""
    if not isinstance(response, dict):
        raise TypeError("MuAPI returned an invalid response")

    objects = [response]
    for key in ("data", "output", "result"):
        value = response.get(key)
        if isinstance(value, dict) and value not in objects:
            objects.append(value)
    return objects


def _muapi_response_value(response, keys):
    for item in _muapi_response_objects(response):
        for key in keys:
            value = item.get(key)
            if value not in (None, ""):
                return value
    return None


def _muapi_error(response):
    value = _muapi_response_value(response, ("error", "message", "detail"))
    if isinstance(value, str):
        return value[:300]
    return "MuAPI request failed"


def _muapi_result_url(response):
    """Return the documented result URL from the creation response."""
    for item in _muapi_response_objects(response):
        urls = item.get("urls")
        if not isinstance(urls, dict) or "get" not in urls:
            continue

        result_url = urls.get("get")
        if not isinstance(result_url, str) or not result_url:
            raise RuntimeError(
                "MuAPI creation response did not include a valid HTTPS result URL"
            )
        try:
            _validate_public_https_url(result_url)
        except ValueError as exc:
            raise RuntimeError(
                "MuAPI creation response did not include a valid HTTPS result URL"
            ) from exc
        return result_url

    raise RuntimeError(
        "MuAPI creation response did not include a valid HTTPS result URL"
    )


def _muapi_output_url(response):
    for item in _muapi_response_objects(response):
        outputs = item.get("outputs")
        if isinstance(outputs, list):
            for output in outputs:
                if isinstance(output, str) and output.startswith("https://"):
                    return output
                if isinstance(output, dict):
                    for key in ("url", "image_url"):
                        value = output.get(key)
                        if isinstance(value, str) and value.startswith("https://"):
                            return value
    raise RuntimeError("MuAPI completed without an HTTPS image URL")


def _download_muapi_image(url, output_path):
    _download_image(url, output_path, "MuAPI")


def _generate_with_muapi(prompt, output_path, aspect_ratio, api_key, model):
    if not api_key:
        raise RuntimeError("MUAPI_API_KEY not set")
    if model not in MUAPI_MODELS:
        raise RuntimeError(
            f"Unsupported MuAPI logo model: {model}. "
            f"Choose one of: {', '.join(MUAPI_MODELS)}"
        )

    payload = {
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
    }
    response = _json_request(
        f"{MUAPI_API_BASE}/{model}",
        api_key,
        method="POST",
        payload=payload,
        api_key_header="x-api-key",
    )
    request_id = _muapi_response_value(response, ("request_id", "id"))
    if not isinstance(request_id, str) or not request_id:
        raise RuntimeError("MuAPI did not return a request ID")
    result_url = _muapi_result_url(response)

    data = response
    for poll_number in range(MUAPI_MAX_POLLS + 1):
        status = _muapi_response_value(data, ("status",))
        normalized_status = str(status or "").lower()
        if normalized_status in {"completed", "succeeded", "success"}:
            _download_muapi_image(_muapi_output_url(data), output_path)
            return
        if normalized_status in {
            "failed",
            "error",
            "timeout",
            "canceled",
            "cancelled",
        }:
            raise RuntimeError(f"MuAPI generation {normalized_status}: {_muapi_error(data)}")
        if poll_number == MUAPI_MAX_POLLS:
            break

        time.sleep(MUAPI_POLL_INTERVAL)
        data = _json_request(
            result_url,
            api_key,
            api_key_header="x-api-key",
        )

    raise RuntimeError("MuAPI prediction timed out while polling")


def _path_for_image_type(output_path, mime_type):
    """Return output_path with the extension of the returned image type.

    An unknown image type keeps the requested path.
    """
    extension = IMAGE_EXTENSIONS.get(mime_type.split(";")[0].strip().lower())
    path = Path(output_path)
    suffix = path.suffix.lower()
    if extension is None or suffix == extension or (suffix, extension) == (".jpeg", ".jpg"):
        return output_path
    return str(path.with_suffix(extension))


def _generate_with_gemini(prompt, output_path, aspect_ratio, use_pro):
    """Generate with Gemini and return the path the image was saved to."""
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY not set")

    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise RuntimeError(
            "google-genai package not installed; run: pip install google-genai"
        ) from exc

    client = genai.Client(api_key=GEMINI_API_KEY)
    model = GEMINI_PRO if use_pro else GEMINI_FLASH
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE", "TEXT"],
            image_config=types.ImageConfig(aspect_ratio=aspect_ratio),
            safety_settings=[
                types.SafetySetting(
                    category="HARM_CATEGORY_HATE_SPEECH",
                    threshold="BLOCK_LOW_AND_ABOVE",
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_DANGEROUS_CONTENT",
                    threshold="BLOCK_LOW_AND_ABOVE",
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    threshold="BLOCK_LOW_AND_ABOVE",
                ),
                types.SafetySetting(
                    category="HARM_CATEGORY_HARASSMENT",
                    threshold="BLOCK_LOW_AND_ABOVE",
                ),
            ],
        ),
    )

    for part in response.candidates[0].content.parts:
        if (
            hasattr(part, "inline_data")
            and part.inline_data
            and part.inline_data.mime_type.startswith("image/")
        ):
            saved_path = _path_for_image_type(output_path, part.inline_data.mime_type)
            if saved_path != output_path:
                print(
                    f"Gemini returned {part.inline_data.mime_type}, "
                    f"so saving as {saved_path} instead of {output_path}"
                )
            with open(saved_path, "wb") as output_file:
                output_file.write(part.inline_data.data)
            return saved_path
    raise RuntimeError("Gemini did not return an image")


def generate_logo(
    prompt,
    style=None,
    industry=None,
    brand_name=None,
    output_path=None,
    use_pro=False,
    aspect_ratio=None,
    provider="gemini",
    atlas_model=ATLAS_MODEL,
    muapi_model=MUAPI_MODEL,
):
    """Generate a logo using Gemini, Atlas Cloud, or MuAPI image generation.

    Args:
        aspect_ratio: Image aspect ratio. Options: "1:1", "16:9", "9:16", "4:3", "3:4"
                      Default is "1:1" (square) for logos.
    """

    # Enhance the prompt
    full_prompt = enhance_prompt(prompt, style, industry, brand_name)

    # Set aspect ratio (default to 1:1 for logos)
    ratio = aspect_ratio if aspect_ratio in ASPECT_RATIOS else DEFAULT_ASPECT_RATIO

    if output_path is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # noqa: DTZ005
        brand_slug = brand_name.lower().replace(" ", "_") if brand_name else "logo"
        output_path = f"{brand_slug}_{timestamp}.png"

    if provider == "atlas":
        model_label = f"Atlas Cloud ({atlas_model})"
    elif provider == "muapi":
        model_label = f"MuAPI ({muapi_model})"
    else:
        model_label = (
            f"Nano Banana Pro ({GEMINI_PRO})"
            if use_pro
            else f"Nano Banana ({GEMINI_FLASH})"
        )

    print(f"Generating logo with {model_label}...")
    print(f"Aspect ratio: {ratio}")
    print(f"Prompt: {full_prompt[:150]}...")
    print()

    try:
        if provider == "atlas":
            _generate_with_atlas(
                full_prompt,
                output_path,
                ratio,
                ATLASCLOUD_API_KEY,
                atlas_model,
            )
        elif provider == "muapi":
            _generate_with_muapi(
                full_prompt,
                output_path,
                ratio,
                MUAPI_API_KEY,
                muapi_model,
            )
        else:
            output_path = _generate_with_gemini(full_prompt, output_path, ratio, use_pro)

        print(f"Logo saved to: {output_path}")
        return output_path

    except Exception as exc:  # noqa: BLE001 - provider SDK errors are not standardized
        print(f"Error generating logo: {exc}")
        return None


def generate_batch(
    prompt,
    brand_name,
    count,
    output_dir,
    use_pro=False,
    brand_context=None,
    aspect_ratio=None,
    provider="gemini",
    atlas_model=ATLAS_MODEL,
    muapi_model=MUAPI_MODEL,
):
    """Generate multiple logo variants with different styles"""

    # Select appropriate styles for batch generation
    batch_styles = [
        ("minimalist", "Clean, simple geometric shape with minimal details"),
        ("modern", "Sleek gradient with tech-forward aesthetic"),
        ("geometric", "Abstract geometric patterns, mathematical precision"),
        ("gradient", "Vibrant color transitions, modern digital feel"),
        ("abstract", "Conceptual symbolic representation"),
        ("lettermark", "Stylized letter 'U' as monogram"),
        ("negative-space", "Clever use of negative space, hidden meaning"),
        ("lineart", "Single stroke continuous line design"),
        ("3d", "Dimensional design with depth and shadows"),
    ]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    results = []
    model_label = (
        f"Atlas Cloud ({atlas_model})"
        if provider == "atlas"
        else f"MuAPI ({muapi_model})"
        if provider == "muapi"
        else f"Nano Banana {'Pro' if use_pro else 'Flash'}"
    )
    ratio = aspect_ratio if aspect_ratio in ASPECT_RATIOS else DEFAULT_ASPECT_RATIO

    print(f"\n{'=' * 60}")
    print(f"  BATCH LOGO GENERATION: {brand_name}")
    print(f"  Model: {model_label}")
    print(f"  Aspect Ratio: {ratio}")
    print(f"  Variants: {count}")
    print(f"  Output: {output_dir}")
    print(f"{'=' * 60}\n")

    for i in range(min(count, len(batch_styles))):
        style_key, style_desc = batch_styles[i]

        # Build enhanced prompt with brand context
        enhanced_prompt = f"{prompt}, {style_desc}"
        if brand_context:
            enhanced_prompt = f"{brand_context}, {enhanced_prompt}"

        # Generate filename
        filename = f"{brand_name.lower().replace(' ', '_')}_{style_key}_{i + 1:02d}.png"
        output_path = os.path.join(output_dir, filename)

        print(f"[{i + 1}/{count}] Generating {style_key} variant...")

        result = generate_logo(
            prompt=enhanced_prompt,
            style=style_key,
            industry="tech",
            brand_name=brand_name,
            output_path=output_path,
            use_pro=use_pro,
            aspect_ratio=aspect_ratio,
            provider=provider,
            atlas_model=atlas_model,
            muapi_model=muapi_model,
        )

        if result:
            results.append(result)
            print(f"  ✓ Saved: {os.path.basename(result)}\n")
        else:
            print(f"  ✗ Failed: {style_key}\n")

        # Rate limiting between requests
        if i < count - 1:
            time.sleep(2)

    print(f"\n{'=' * 60}")
    print(f"  BATCH COMPLETE: {len(results)}/{count} logos generated")
    print(f"{'=' * 60}\n")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Generate logos using Gemini, Atlas Cloud, or MuAPI"
    )
    parser.add_argument("--prompt", "-p", type=str, help="Logo description prompt")
    parser.add_argument("--brand", "-b", type=str, help="Brand name")
    parser.add_argument(
        "--style", "-s", choices=list(STYLE_MODIFIERS.keys()), help="Logo style"
    )
    parser.add_argument(
        "--industry", "-i", choices=list(INDUSTRY_PROMPTS.keys()), help="Industry type"
    )
    parser.add_argument("--output", "-o", type=str, help="Output file path")
    parser.add_argument(
        "--output-dir", type=str, help="Output directory for batch generation"
    )
    parser.add_argument(
        "--batch", type=int, help="Number of logo variants to generate (batch mode)"
    )
    parser.add_argument(
        "--brand-context", type=str, help="Additional brand context for prompts"
    )
    parser.add_argument(
        "--pro",
        action="store_true",
        help=f"Use Nano Banana Pro ({GEMINI_PRO}) for professional quality",
    )
    parser.add_argument(
        "--provider",
        choices=["gemini", "atlas", "muapi"],
        default="gemini",
        help="Image provider (default: gemini)",
    )
    parser.add_argument(
        "--atlas-model",
        default=ATLAS_MODEL,
        help=f"Atlas Cloud image model (default: {ATLAS_MODEL})",
    )
    parser.add_argument(
        "--muapi-model",
        choices=MUAPI_MODELS,
        default=MUAPI_MODEL,
        help=f"MuAPI image model (default: {MUAPI_MODEL})",
    )
    parser.add_argument(
        "--aspect-ratio",
        "-r",
        choices=ASPECT_RATIOS,
        default=DEFAULT_ASPECT_RATIO,
        help=f"Image aspect ratio (default: {DEFAULT_ASPECT_RATIO} for logos)",
    )
    parser.add_argument(
        "--list-styles", action="store_true", help="List available styles"
    )
    parser.add_argument(
        "--list-industries", action="store_true", help="List available industries"
    )

    args = parser.parse_args()

    if args.provider != "gemini" and args.pro:
        parser.error(
            "--pro is only available with --provider gemini; "
            "use --muapi-model nano-banana-pro for MuAPI"
        )

    if args.list_styles:
        print("Available styles:")
        for style, desc in STYLE_MODIFIERS.items():
            print(f"  {style}: {desc[:60]}...")
        return

    if args.list_industries:
        print("Available industries:")
        for industry, desc in INDUSTRY_PROMPTS.items():
            print(f"  {industry}: {desc[:60]}...")
        return

    if not args.prompt and not args.brand:
        parser.error("Either --prompt or --brand is required")

    prompt = args.prompt or "professional logo"

    # Batch mode
    if args.batch:
        output_dir = (
            args.output_dir or f"./{args.brand.lower().replace(' ', '_')}_logos"
        )
        results = generate_batch(
            prompt=prompt,
            brand_name=args.brand or "Logo",
            count=args.batch,
            output_dir=output_dir,
            use_pro=args.pro,
            brand_context=args.brand_context,
            aspect_ratio=args.aspect_ratio,
            provider=args.provider,
            atlas_model=args.atlas_model,
            muapi_model=args.muapi_model,
        )
        if not results:
            sys.exit(1)
    else:
        saved_path = generate_logo(
            prompt=prompt,
            style=args.style,
            industry=args.industry,
            brand_name=args.brand,
            output_path=args.output,
            use_pro=args.pro,
            aspect_ratio=args.aspect_ratio,
            provider=args.provider,
            atlas_model=args.atlas_model,
            muapi_model=args.muapi_model,
        )
        if saved_path is None:
            sys.exit(1)


if __name__ == "__main__":
    main()
````



---

## `scripts/logo/search.py`

````python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Logo Design Search - CLI for searching logo design guidelines
Usage: python search.py "<query>" [--domain <domain>] [--max-results 3]
       python search.py "<query>" --design-brief [-p "Brand Name"]

Domains: style, color, industry
"""

import argparse
from core import CSV_CONFIG, MAX_RESULTS, search, search_all


def format_output(result):
    """Format results for Claude consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    output.append(f"## Logo Design Search Results")
    output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    output.append(f"**Source:** {result['file']} | **Found:** {result['count']} results\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### Result {i}")
        for key, value in row.items():
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


def generate_design_brief(query, brand_name=None):
    """Generate a comprehensive logo design brief based on query"""
    results = search_all(query, max_results=2)

    output = []
    output.append("=" * 60)
    if brand_name:
        output.append(f"  LOGO DESIGN BRIEF: {brand_name.upper()}")
    else:
        output.append("  LOGO DESIGN BRIEF")
    output.append("=" * 60)
    output.append(f"  Query: {query}")
    output.append("=" * 60)
    output.append("")

    # Industry recommendations
    if "industry" in results:
        output.append("## INDUSTRY ANALYSIS")
        for r in results["industry"]:
            output.append(f"**Industry:** {r.get('Industry', 'N/A')}")
            output.append(f"- Recommended Styles: {r.get('Recommended Styles', 'N/A')}")
            output.append(f"- Colors: {r.get('Primary Colors', 'N/A')}")
            output.append(f"- Typography: {r.get('Typography', 'N/A')}")
            output.append(f"- Symbols: {r.get('Common Symbols', 'N/A')}")
            output.append(f"- Mood: {r.get('Mood', 'N/A')}")
            output.append(f"- Best Practices: {r.get('Best Practices', 'N/A')}")
            output.append(f"- Avoid: {r.get('Avoid', 'N/A')}")
            output.append("")

    # Style recommendations
    if "style" in results:
        output.append("## STYLE RECOMMENDATIONS")
        for r in results["style"]:
            output.append(f"**{r.get('Style Name', 'N/A')}** ({r.get('Category', 'N/A')})")
            output.append(f"- Colors: {r.get('Primary Colors', 'N/A')} | {r.get('Secondary Colors', 'N/A')}")
            output.append(f"- Typography: {r.get('Typography', 'N/A')}")
            output.append(f"- Effects: {r.get('Effects', 'N/A')}")
            output.append(f"- Best For: {r.get('Best For', 'N/A')}")
            output.append(f"- Complexity: {r.get('Complexity', 'N/A')}")
            output.append("")

    # Color recommendations
    if "color" in results:
        output.append("## COLOR PALETTE OPTIONS")
        for r in results["color"]:
            output.append(f"**{r.get('Palette Name', 'N/A')}**")
            output.append(f"- Primary: {r.get('Primary Hex', 'N/A')}")
            output.append(f"- Secondary: {r.get('Secondary Hex', 'N/A')}")
            output.append(f"- Accent: {r.get('Accent Hex', 'N/A')}")
            output.append(f"- Background: {r.get('Background Hex', 'N/A')}")
            output.append(f"- Psychology: {r.get('Psychology', 'N/A')}")
            output.append("")

    output.append("=" * 60)
    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Logo Design Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--design-brief", "-db", action="store_true", help="Generate comprehensive design brief")
    parser.add_argument("--brand-name", "-p", type=str, default=None, help="Brand name for design brief")

    args = parser.parse_args()

    if args.design_brief:
        result = generate_design_brief(args.query, args.brand_name)
        print(result)
    else:
        result = search(args.query, args.domain, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
````
