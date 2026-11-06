# brand

Original: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/b7d5353/.claude/skills/brand

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

*Quando usar:* Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style guides.


# Brand

Brand identity, voice, messaging, asset management, and consistency frameworks.

## When to Use

- Brand voice definition and content tone guidance
- Visual identity standards and style guide development
- Messaging framework creation
- Brand consistency review and audit
- Asset organization, naming, and approval
- Color palette management and typography specs

## Script Paths

Script paths in this skill and its `references/` are relative to the directory that contains this SKILL.md, not to the project: `scripts/<file>` is this skill's own `scripts/` folder, and `../<skill>/scripts/<file>` is a sibling sub-skill installed alongside it. Build the full path from that directory (Claude Code reports it as the skill's base directory when the skill loads) and keep the working directory at the project root — the scripts read and write project files such as `docs/brand-guidelines.md`, `assets/design-tokens.json` or `src/` relative to it.

## Quick Start

**Inject brand context into prompts:**
```bash
node scripts/inject-brand-context.cjs
node scripts/inject-brand-context.cjs --json
```

**Validate an asset:**
```bash
node scripts/validate-asset.cjs <asset-path>
```

**Extract/compare colors:**
```bash
node scripts/extract-colors.cjs --palette
node scripts/extract-colors.cjs <image-path>
```

## Brand Sync Workflow

```bash
# 1. Edit docs/brand-guidelines.md (or use /brand update)
# 2. Sync to design tokens
node scripts/sync-brand-to-tokens.cjs
# 3. Verify
node scripts/inject-brand-context.cjs --json | head -20
```

The sync stops when it detects existing token files, `:root` custom properties
or Tailwind v4 `@theme` variables in common CSS entry points and their local
CSS imports, or Tailwind theme colors and presets. Review the reported source
before proceeding. If the detected files are the managed
`assets/design-tokens.*` outputs from an earlier sync and replacing them is
intentional, re-run with `--force`.

**Files synced:**
- `docs/brand-guidelines.md` → Source of truth
- `assets/design-tokens.json` → Token definitions
- `assets/design-tokens.css` → CSS variables

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `update` | Update brand identity and sync to all design systems | `references/update.md` |

## References

| Topic | File |
|-------|------|
| Voice Framework | `references/voice-framework.md` |
| Visual Identity | `references/visual-identity.md` |
| Messaging | `references/messaging-framework.md` |
| Consistency | `references/consistency-checklist.md` |
| Guidelines Template | `references/brand-guideline-template.md` |
| Asset Organization | `references/asset-organization.md` |
| Color Management | `references/color-palette-management.md` |
| Typography | `references/typography-specifications.md` |
| Logo Usage | `references/logo-usage-rules.md` |
| Approval Checklist | `references/approval-checklist.md` |

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/inject-brand-context.cjs` | Extract brand context for prompt injection |
| `scripts/sync-brand-to-tokens.cjs` | Sync brand-guidelines.md → design-tokens.json/css |
| `scripts/validate-asset.cjs` | Validate asset naming, size, format |
| `scripts/extract-colors.cjs` | Extract and compare colors against palette |

## Templates

| Template | Purpose |
|----------|---------|
| `templates/brand-guidelines-starter.md` | Complete starter template for new brands |

## Routing

1. Parse subcommand from `$ARGUMENTS` (first word)
2. Load corresponding `references/{subcommand}.md`
3. Execute with remaining arguments



---

## `references/approval-checklist.md`

# Asset Approval Checklist

Comprehensive checklist for reviewing marketing assets before approval.

## Quick Review

Before detailed review, verify:
- [ ] Asset serves stated purpose
- [ ] Target audience appropriate
- [ ] No obvious errors or issues
- [ ] Aligns with campaign goals

## Visual Elements

### Logo Usage
- [ ] Correct logo variant for context
- [ ] Proper clear space maintained
- [ ] Minimum size requirements met
- [ ] Approved colors only
- [ ] No unauthorized modifications
- [ ] Appropriate for background

### Color Compliance
- [ ] Uses brand palette colors only
- [ ] Primary/secondary ratio appropriate (60/30/10)
- [ ] Semantic colors used correctly
- [ ] No off-brand colors introduced
- [ ] Consistent across all elements

### Typography
- [ ] Brand fonts used throughout
- [ ] Correct font weights applied
- [ ] Proper type hierarchy
- [ ] Appropriate sizes for medium
- [ ] Line heights adequate
- [ ] No orphans/widows in body text

### Imagery
- [ ] Matches brand photography style
- [ ] Appropriate subjects/content
- [ ] Quality meets requirements
- [ ] Properly licensed/credited
- [ ] Optimized for intended use

## Accessibility

### Visual Accessibility
- [ ] Text contrast ratio >= 4.5:1 (AA)
- [ ] Large text contrast >= 3:1
- [ ] Interactive elements have visible focus
- [ ] Color not sole indicator of meaning
- [ ] Alt text for all images

### Content Accessibility
- [ ] Clear and scannable layout
- [ ] Readable font sizes
- [ ] Logical reading order
- [ ] Meaningful headings structure
- [ ] Links describe destination

## Content Quality

### Copy Review
- [ ] Matches brand voice
- [ ] Appropriate tone for context
- [ ] No prohibited terms used
- [ ] Value proposition clear
- [ ] CTA compelling and clear
- [ ] Proofread for errors

### Messaging
- [ ] Aligns with key messages
- [ ] Differentiators highlighted
- [ ] Benefits over features
- [ ] Target audience addressed
- [ ] No conflicting claims

## Technical Requirements

### File Specifications
- [ ] Correct file format
- [ ] Appropriate resolution
- [ ] File size optimized
- [ ] Proper naming convention
- [ ] Metadata included

### Platform Requirements
| Platform | Verified |
|----------|----------|
| Instagram | [ ] Correct dimensions |
| Twitter/X | [ ] Meets requirements |
| LinkedIn | [ ] Professional standards |
| Facebook | [ ] Guidelines compliant |
| Email | [ ] Size under 1MB |
| Web | [ ] Optimized for web |

## Legal & Compliance

### Intellectual Property
- [ ] Stock images licensed
- [ ] Music/audio cleared
- [ ] No trademark violations
- [ ] User content authorized
- [ ] Credits included where needed

### Regulatory
- [ ] Required disclosures present
- [ ] No misleading claims
- [ ] Pricing accurate
- [ ] Terms linked where needed
- [ ] Privacy compliant

## Review Status

### Reviewer Sign-off

| Review Area | Reviewer | Date | Status |
|-------------|----------|------|--------|
| Visual Design | | | [ ] Pass / [ ] Revisions |
| Copy/Content | | | [ ] Pass / [ ] Revisions |
| Brand Compliance | | | [ ] Pass / [ ] Revisions |
| Technical | | | [ ] Pass / [ ] Revisions |
| Legal | | | [ ] Pass / [ ] Revisions |

### Final Approval

- [ ] All review areas passed
- [ ] Revisions completed (if any)
- [ ] Final version uploaded
- [ ] Metadata updated
- [ ] Ready for publish/use

**Approved By:** _______________

**Date:** _______________

**Version:** _______________

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Logo too small | Increase to minimum size |
| Wrong font | Replace with brand font |
| Low contrast | Adjust colors for accessibility |
| Off-brand color | Replace with palette color |
| Blurry image | Use higher resolution source |
| Missing alt text | Add descriptive alt text |
| Weak CTA | Strengthen action-oriented copy |

## Automation Support

The `validate-asset.cjs` script can auto-check:
- Color palette compliance
- Minimum dimensions
- File format/size
- Naming convention
- Basic metadata

Run: `node scripts/validate-asset.cjs <asset-path>`

## Archival

After approval:
1. Update asset status in manifest.json
2. Add approver and timestamp
3. Move previous versions to archive
4. Update campaign tracking
5. Notify relevant teams



---

## `references/asset-organization.md`

# Asset Organization Guide

Guidelines for organizing marketing assets in a structured, searchable system.

## Directory Structure

```
project-root/
├── .assets/                          # Git-tracked metadata
│   ├── manifest.json                 # Central asset registry
│   ├── tags.json                     # Tagging system
│   ├── versions/                     # Version history
│   │   └── {asset-id}/
│   │       └── v{n}.json
│   └── metadata/                     # Type-specific metadata
│       ├── designs.json
│       ├── banners.json
│       ├── logos.json
│       └── videos.json
├── assets/                           # Raw files
│   ├── designs/
│   │   ├── campaigns/                # Campaign-specific designs
│   │   ├── web/                      # Website graphics
│   │   └── print/                    # Print materials
│   ├── banners/
│   │   ├── social-media/             # Platform banners
│   │   ├── email-headers/            # Email template headers
│   │   └── landing-pages/            # Hero/section images
│   ├── logos/
│   │   ├── full-horizontal/          # Full logo with wordmark
│   │   ├── icon-only/                # Symbol only
│   │   ├── monochrome/               # Single color versions
│   │   └── variations/               # Special versions
│   ├── videos/
│   │   ├── ads/                      # Promotional videos
│   │   ├── tutorials/                # How-to content
│   │   └── testimonials/             # Customer videos
│   ├── infographics/                 # Data visualizations
│   └── generated/                    # AI-generated assets
│       └── {YYYYMMDD}/               # Date-organized
```

## Naming Convention

### Format
```
{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}
```

### Components
| Component | Format | Required | Examples |
|-----------|--------|----------|----------|
| type | lowercase | Yes | banner, logo, design, video |
| campaign | kebab-case | Yes* | claude-launch, q1-promo, evergreen |
| description | kebab-case | Yes | hero-image, email-header |
| timestamp | YYYYMMDD | Yes | 20251209 |
| variant | kebab-case | No | dark-mode, 1x1, mobile |

*Use "evergreen" for non-campaign assets

### Examples
```
banner_claude-launch_hero-image_20251209_16-9.png
logo_brand-refresh_horizontal-full-color_20251209.svg
design_holiday-campaign_email-hero_20251209_dark-mode.psd
video_product-demo_feature-walkthrough_20251209.mp4
infographic_evergreen_pricing-comparison_20251209.png
```

## Metadata Schema

### Asset Entry (manifest.json)
```json
{
  "id": "uuid-v4",
  "name": "Campaign Hero Banner",
  "type": "banner",
  "path": "assets/banners/landing-pages/banner_claude-launch_hero-image_20251209.png",
  "dimensions": { "width": 1920, "height": 1080 },
  "fileSize": 245760,
  "mimeType": "image/png",
  "tags": ["campaign", "hero", "launch"],
  "status": "approved",
  "source": {
    "model": "imagen-4",
    "prompt": "...",
    "createdAt": "2025-12-09T10:30:00Z"
  },
  "version": 2,
  "createdBy": "agent:content-creator",
  "approvedBy": "user:john",
  "approvedAt": "2025-12-09T14:00:00Z"
}
```

### Version Entry (versions/{id}/v{n}.json)
```json
{
  "version": 2,
  "previousVersion": 1,
  "path": "assets/banners/landing-pages/banner_claude-launch_hero-image_20251209_v2.png",
  "changes": "Updated CTA button color to match brand refresh",
  "createdAt": "2025-12-09T12:00:00Z",
  "createdBy": "agent:ui-designer"
}
```

## Tagging System

### Standard Tags
| Category | Values |
|----------|--------|
| status | draft, review, approved, archived |
| platform | instagram, twitter, linkedin, facebook, youtube, email, web |
| content-type | promotional, educational, brand, product, testimonial |
| format | 1x1, 4x5, 9x16, 16x9, story, reel, banner |
| source | imagen-4, veo-3, user-upload, canva, figma |

### Tag Usage
- Each asset should have: status + platform + content-type
- Optional: format, source, campaign

## File Organization Best Practices

1. **One file per variant** - Don't combine dark/light in one file
2. **Source files separate** - Keep .psd/.fig in same structure
3. **AI assets timestamped** - Auto-organize by generation date
4. **Archive don't delete** - Move to `archived/` with date prefix
5. **Large files external** - Videos > 100MB use cloud storage links

## Search Patterns

### By Type
```bash
# Find all banners
ls assets/banners/**/*
```

### By Campaign
```bash
# Find all assets for specific campaign
grep -l "claude-launch" .assets/manifest.json
```

### By Status
```bash
# Find approved assets only
jq '.assets[] | select(.status == "approved")' .assets/manifest.json
```

## Cleanup Workflow

1. Run `extract-colors.cjs` on new assets
2. Validate against brand guidelines
3. Update manifest.json with new entries
4. Tag appropriately
5. Remove duplicates/outdated versions



---

## `references/brand-guideline-template.md`

# Brand Guidelines Template

Use this template to create comprehensive brand guidelines for any project.

## Document Structure

```markdown
# Brand Guidelines v{X.Y}

## Quick Reference
- **Primary Color:** #XXXXXX
- **Secondary Color:** #XXXXXX
- **Primary Font:** {font-family}
- **Voice:** {3 key traits}

## 1. Color Palette

### Primary Colors
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| {Name} | #{hex} | rgb({r},{g},{b}) | Primary brand color, CTAs, headers |
| {Name} | #{hex} | rgb({r},{g},{b}) | Supporting accent |

### Secondary Colors
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| {Name} | #{hex} | rgb({r},{g},{b}) | Secondary elements |
| {Name} | #{hex} | rgb({r},{g},{b}) | Highlights |

### Neutral Palette
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Background | #{hex} | rgb({r},{g},{b}) | Page backgrounds |
| Text Primary | #{hex} | rgb({r},{g},{b}) | Body text |
| Text Secondary | #{hex} | rgb({r},{g},{b}) | Captions, muted text |
| Border | #{hex} | rgb({r},{g},{b}) | Dividers, borders |

### Accessibility
- Text/Background Contrast: {ratio}:1 (WCAG {level})
- CTA Contrast: {ratio}:1
- All interactive elements meet WCAG 2.1 AA

## 2. Typography

### Font Stack
```css
--font-heading: '{Font}', sans-serif;
--font-body: '{Font}', sans-serif;
--font-mono: '{Font}', monospace;
```

### Type Scale
| Element | Font | Weight | Size (Desktop/Mobile) | Line Height |
|---------|------|--------|----------------------|-------------|
| H1 | {font} | 700 | 48px / 32px | 1.2 |
| H2 | {font} | 600 | 36px / 28px | 1.25 |
| H3 | {font} | 600 | 28px / 24px | 1.3 |
| H4 | {font} | 600 | 24px / 20px | 1.35 |
| Body | {font} | 400 | 16px / 16px | 1.5 |
| Small | {font} | 400 | 14px / 14px | 1.5 |
| Caption | {font} | 400 | 12px / 12px | 1.4 |

## 3. Logo Usage

### Variants
- **Primary:** Full horizontal logo with wordmark
- **Stacked:** Vertical arrangement for square spaces
- **Icon:** Symbol only for favicons, app icons
- **Monochrome:** Single color for limited palettes

### Clear Space
Minimum clear space = height of logo mark

### Minimum Size
- Digital: 80px width minimum
- Print: 25mm width minimum

### Don'ts
- Don't rotate or skew
- Don't change colors outside approved palette
- Don't add effects (shadows, gradients)
- Don't crop or modify proportions
- Don't place on busy backgrounds

## 4. Voice & Tone

### Brand Personality
{Trait 1}: {Description}
{Trait 2}: {Description}
{Trait 3}: {Description}

### Voice Chart
| Trait | We Are | We Are Not |
|-------|--------|------------|
| {Trait} | {Description} | {Anti-description} |

### Tone by Context
| Context | Tone | Example |
|---------|------|---------|
| Marketing | {tone} | "{example}" |
| Support | {tone} | "{example}" |
| Error Messages | {tone} | "{example}" |
| Success | {tone} | "{example}" |

### Prohibited Terms
- {term 1} (reason)
- {term 2} (reason)

## 5. Imagery Guidelines

### Photography Style
- {Lighting preference}
- {Subject guidelines}
- {Color treatment}

### Illustrations
- Style: {description}
- Colors: Brand palette only
- Stroke: {weight}px

### Icons
- Style: {outlined/filled/duotone}
- Size: 24px base grid
- Corner radius: {value}px
```

## Usage

1. Copy template above
2. Fill in brand-specific values
3. Save as `docs/brand-guidelines.md`
4. Reference in content workflows

## Extractable Fields

Scripts can extract:
- `colors.primary`, `colors.secondary`, `colors.neutral`
- `typography.heading`, `typography.body`
- `voice.traits`, `voice.prohibited`
- `logo.variants`, `logo.minSize`



---

## `references/color-palette-management.md`

# Color Palette Management

Guidelines for defining, extracting, and enforcing brand colors.

## Color System Structure

### Hierarchy
```
Primary Colors (1-2)
├── Main brand color - Used for CTAs, headers, key elements
└── Supporting primary - Secondary emphasis

Secondary Colors (2-3)
├── Accent colors - Highlights, interactive states
└── Supporting visuals - Icons, illustrations

Neutral Palette (3-5)
├── Background colors - Page, card, modal backgrounds
├── Text colors - Headings, body, muted text
└── UI elements - Borders, dividers, shadows

Semantic Colors (4)
├── Success - #22C55E (green)
├── Warning - #F59E0B (amber)
├── Error - #EF4444 (red)
└── Info - #3B82F6 (blue)
```

## Color Documentation Format

### Markdown Table
```markdown
| Name | Hex | RGB | HSL | Usage |
|------|-----|-----|-----|-------|
| Primary Blue | #2563EB | rgb(37,99,235) | hsl(217,91%,53%) | CTAs, links |
```

### CSS Variables
```css
:root {
  /* Primary */
  --color-primary: #2563EB;
  --color-primary-light: #3B82F6;
  --color-primary-dark: #1D4ED8;

  /* Secondary */
  --color-secondary: #8B5CF6;
  --color-accent: #F59E0B;

  /* Neutral */
  --color-background: #FFFFFF;
  --color-surface: #F9FAFB;
  --color-text-primary: #111827;
  --color-text-secondary: #6B7280;
  --color-border: #E5E7EB;
}
```

### Tailwind Config
```javascript
colors: {
  primary: {
    DEFAULT: '#2563EB',
    50: '#EFF6FF',
    100: '#DBEAFE',
    500: '#3B82F6',
    600: '#2563EB',
    700: '#1D4ED8',
  }
}
```

## Accessibility Requirements

### Contrast Ratios (WCAG 2.1)
| Level | Normal Text | Large Text | UI Components |
|-------|-------------|------------|---------------|
| AA | 4.5:1 | 3:1 | 3:1 |
| AAA | 7:1 | 4.5:1 | 4.5:1 |

### Checking Contrast
```javascript
// Formula for relative luminance
function luminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(v => {
    v /= 255;
    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function contrastRatio(l1, l2) {
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}
```

## Color Extraction

### From Images
Use `extract-colors.cjs` script to:
1. Load image file
2. Extract dominant colors using k-means clustering
3. Map to nearest brand colors
4. Report compliance percentage

### From Brand Guidelines
Parse markdown to extract:
- Hex values from tables
- CSS variable definitions
- Color names and usage descriptions

## Brand Compliance Validation

### Rules
1. **Primary color ratio**: 60-70% of design
2. **Secondary color ratio**: 20-30% of design
3. **Accent color ratio**: 5-10% of design
4. **Off-brand tolerance**: Max 20% non-palette colors

### Validation Output
```json
{
  "compliance": 85,
  "colors": {
    "brand": ["#2563EB", "#8B5CF6", "#FFFFFF"],
    "offBrand": ["#FF5500"],
    "dominant": "#2563EB"
  },
  "issues": [
    "Off-brand color #FF5500 detected (15% coverage)",
    "Primary color underused (45% vs 60% target)"
  ]
}
```

## Color Usage Guidelines

### Do's
- Use primary for main CTAs and key elements
- Maintain consistent hover/active states
- Test all combinations for accessibility
- Document color decisions

### Don'ts
- Use more than 2-3 colors in single component
- Mix warm and cool tones without intent
- Use pure black (#000) for text (use #111 or similar)
- Rely solely on color for meaning (use icons/text too)

## Color Palette Examples

### Tech/SaaS
```
Primary: #2563EB (Blue)
Secondary: #8B5CF6 (Purple)
Accent: #10B981 (Emerald)
Background: #F9FAFB
Text: #111827
```

### Marketing/Creative
```
Primary: #F97316 (Orange)
Secondary: #EC4899 (Pink)
Accent: #14B8A6 (Teal)
Background: #FFFFFF
Text: #1F2937
```

### Professional/Corporate
```
Primary: #1E40AF (Navy)
Secondary: #475569 (Slate)
Accent: #0EA5E9 (Sky)
Background: #F8FAFC
Text: #0F172A
```

## Tools & Resources

- [Coolors](https://coolors.co) - Palette generation
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Tailwind Color Reference](https://tailwindcss.com/docs/customizing-colors)
- [Color Hunt](https://colorhunt.co) - Curated palettes



---

## `references/consistency-checklist.md`

# Brand Consistency Checklist

## Visual Consistency

### Logo
- [ ] Correct logo version used
- [ ] Proper clear space maintained
- [ ] Approved colors only
- [ ] Legible at all sizes
- [ ] No unauthorized modifications

### Colors
- [ ] Only brand palette colors
- [ ] Consistent color application
- [ ] Proper contrast for accessibility
- [ ] Color ratios maintained

### Typography
- [ ] Brand fonts used
- [ ] Correct weights/styles
- [ ] Proper hierarchy
- [ ] Consistent formatting

### Imagery
- [ ] Matches brand style
- [ ] Consistent editing/filters
- [ ] Appropriate subjects
- [ ] Quality standards met

## Voice Consistency

### Tone
- [ ] Matches brand personality
- [ ] Appropriate for context
- [ ] Consistent across channels
- [ ] No conflicting messages

### Language
- [ ] Brand terminology used
- [ ] Consistent capitalization
- [ ] Proper abbreviations
- [ ] Jargon level appropriate

### Messaging
- [ ] Aligns with key messages
- [ ] Value prop clear
- [ ] Differentiators highlighted
- [ ] CTAs consistent

## Channel Audit

### Website
- [ ] Homepage
- [ ] Product pages
- [ ] Blog/content
- [ ] Footer/navigation

### Social Media
- [ ] Profile images
- [ ] Cover images
- [ ] Bio/about sections
- [ ] Post templates

### Email
- [ ] Header/footer
- [ ] Templates
- [ ] Signatures
- [ ] Automated messages

### Collateral
- [ ] Presentations
- [ ] One-pagers
- [ ] Business cards
- [ ] Promotional materials

## Common Issues

| Issue | Fix |
|-------|-----|
| Outdated logo | Replace with current version |
| Off-brand colors | Update to palette |
| Wrong font | Replace with brand font |
| Inconsistent voice | Apply style guide |
| Mixed messaging | Align to framework |

## Audit Frequency

| Asset Type | Frequency |
|------------|-----------|
| Website | Monthly |
| Social profiles | Quarterly |
| Email templates | Quarterly |
| Sales materials | Quarterly |
| Full brand audit | Annually |



---

## `references/logo-usage-rules.md`

# Logo Usage Rules

Guidelines for proper logo implementation across all marketing materials.

## Logo Variants

### Primary Variants
| Variant | File Name | Use Case |
|---------|-----------|----------|
| Full Horizontal | logo-full-horizontal.{ext} | Website headers, documents |
| Stacked | logo-stacked.{ext} | Square spaces, social avatars |
| Icon Only | logo-icon.{ext} | Favicons, app icons, small spaces |
| Wordmark Only | logo-wordmark.{ext} | When icon already present |

### Color Variants
| Variant | Use Case |
|---------|----------|
| Full Color | Default on white/light backgrounds |
| Reversed | On dark backgrounds |
| Monochrome Dark | On light backgrounds when color not possible |
| Monochrome Light | On dark backgrounds when color not possible |

## Clear Space

### Minimum Clear Space
The clear space around the logo should equal the height of the logo mark (icon portion).

```
    ┌─────────────────────────────┐
    │           [x]               │
    │   ┌───────────────────┐     │
    │   │                   │     │
[x] │   │    [LOGO]         │ [x] │
    │   │                   │     │
    │   └───────────────────┘     │
    │           [x]               │
    └─────────────────────────────┘
```

Where [x] = height of logo mark

## Minimum Size

### Digital
| Format | Minimum Width | Notes |
|--------|---------------|-------|
| Full Logo | 120px | All elements legible |
| Icon Only | 24px | Favicon/small icons |
| Icon Only | 32px | UI elements |

### Print
| Format | Minimum Width | Notes |
|--------|---------------|-------|
| Full Logo | 35mm | Business cards, letterhead |
| Icon Only | 10mm | Small print items |

## Color Usage

### Approved Backgrounds
| Background | Logo Version |
|------------|--------------|
| White | Full color or dark mono |
| Light gray (#F5F5F5+) | Full color or dark mono |
| Brand primary | Reversed (white) |
| Dark (#333 or darker) | Reversed (white) |
| Photography | Ensure sufficient contrast |

### Color Rules
1. Never change logo colors outside approved palette
2. Don't use gradients on the logo
3. Don't apply transparency to logo elements
4. Don't add shadows or effects

## Incorrect Usage

### Absolute Don'ts
- ❌ Stretch or compress logo
- ❌ Rotate at angles
- ❌ Add drop shadows
- ❌ Apply gradient fills
- ❌ Use unapproved colors
- ❌ Add strokes or outlines
- ❌ Place on busy backgrounds
- ❌ Crop any portion
- ❌ Rearrange elements
- ❌ Add additional elements

### Visual Examples
```
WRONG: Stretched      WRONG: Rotated       WRONG: Wrong color
┌──────────────┐      ┌────────┐          ┌────────┐
│   L O G O    │      │  /    │          │ LOGO   │ <- wrong color
└──────────────┘      │ /LOGO │          └────────┘
                      └───────/
```

## Co-branding

### Partner Logo Guidelines
1. Equal visual weight (same height)
2. Adequate separation between logos
3. Use divider line if needed
4. Both logos in their approved colors
5. Clear space applies to both

### Layout Options
```
Option A: Side by side with divider
[OUR LOGO] | [PARTNER LOGO]

Option B: Stacked
    [OUR LOGO]
        +
  [PARTNER LOGO]
```

## File Formats

### Recommended Formats
| Usage | Format | Notes |
|-------|--------|-------|
| Web | SVG | Preferred, scalable |
| Web fallback | PNG | With transparency |
| Print | PDF | Vector, high quality |
| Print alt | EPS | Legacy systems |
| Documents | PNG | High res (300dpi) |

### File Organization
```
assets/logos/
├── full-horizontal/
│   ├── logo-full-color.svg
│   ├── logo-full-color.png
│   ├── logo-reversed.svg
│   ├── logo-mono-dark.svg
│   └── logo-mono-light.svg
├── icon-only/
│   ├── icon-full-color.svg
│   ├── icon-reversed.svg
│   └── favicon.ico
└── monochrome/
    ├── logo-black.svg
    └── logo-white.svg
```

## Platform-Specific Guidelines

### Social Media
| Platform | Format | Size | Notes |
|----------|--------|------|-------|
| LinkedIn | PNG | 300x300px | Icon only |
| Twitter/X | PNG | 400x400px | Icon only |
| Facebook | PNG | 180x180px | Icon only |
| Instagram | PNG | 320x320px | Icon only |

### Website
| Location | Variant | Size |
|----------|---------|------|
| Header | Full horizontal | 120-200px width |
| Footer | Full horizontal | 100-150px width |
| Favicon | Icon only | 32x32px |
| Apple Touch | Icon only | 180x180px |

### Documents
| Document | Variant | Placement |
|----------|---------|-----------|
| Letterhead | Full horizontal | Top left |
| Presentation | Icon + wordmark | Title slide |
| Report | Full horizontal | Cover + footer |

## Logo Approval Process

### Before Using Logo
1. Verify you have the correct version
2. Check background compatibility
3. Ensure minimum size requirements
4. Confirm clear space allocation
5. Review against these guidelines

### Requesting Approval
For non-standard uses:
1. Submit mockup showing proposed usage
2. Include context (medium, audience)
3. Wait for brand team approval
4. Document approved exceptions



---

## `references/messaging-framework.md`

# Messaging Framework

## Framework Structure

```
Mission (Why we exist)
    ↓
Vision (Where we're going)
    ↓
Value Proposition (What we offer)
    ↓
Positioning Statement (How we're different)
    ↓
Key Messages (What we say)
    ↓
Proof Points (Why to believe)
```

## Core Statements

### Mission Statement
```
We [action] for [audience] by [method] so they can [outcome].
```

### Vision Statement
```
A world where [aspiration/change we want to see].
```

### Value Proposition
```
For [target customer] who [need/problem],
[Product/Brand] is a [category]
that [key benefit].
Unlike [competitors],
we [unique differentiator].
```

### Positioning Statement
```
[Brand] is the [category] for [audience]
who want [desired outcome]
because [reason to believe].
```

## Message Architecture

### Primary Message
One sentence that captures your core value.

### Supporting Messages (3-5)
Each addresses a different benefit or audience need.

| Message | Audience Need | Proof Point |
|---------|---------------|-------------|
| [Message 1] | [Need] | [Evidence] |
| [Message 2] | [Need] | [Evidence] |
| [Message 3] | [Need] | [Evidence] |

### Elevator Pitches

**10-second:**
[One sentence that sparks interest]

**30-second:**
[Problem + solution + differentiation]

**60-second:**
[Full pitch with proof points]

## Message by Audience

| Audience | Pain Point | Key Message | CTA |
|----------|------------|-------------|-----|
| [Segment 1] | [Pain] | [Message] | [Action] |
| [Segment 2] | [Pain] | [Message] | [Action] |

## Message Testing

1. Is it clear? (No jargon)
2. Is it differentiated? (Competitors can't say it)
3. Is it credible? (Can we prove it)
4. Is it compelling? (Does audience care)
5. Is it consistent? (Aligns with brand)



---

## `references/typography-specifications.md`

# Typography Specifications

Guidelines for defining and implementing brand typography.

## Font Stack Structure

### Primary Fonts
```css
/* Headings - Display font for impact */
--font-heading: 'Inter', system-ui, -apple-system, sans-serif;

/* Body - Readable for long-form content */
--font-body: 'Inter', system-ui, -apple-system, sans-serif;

/* Monospace - Code, technical content */
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### Font Loading
```html
<!-- Google Fonts (recommended) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

## Type Scale

### Base System
- Base size: 16px (1rem)
- Scale ratio: 1.25 (Major Third)

### Scale Definition
| Element | Size (rem) | Size (px) | Weight | Line Height |
|---------|------------|-----------|--------|-------------|
| Display | 3.815rem | 61px | 700 | 1.1 |
| H1 | 3.052rem | 49px | 700 | 1.2 |
| H2 | 2.441rem | 39px | 600 | 1.25 |
| H3 | 1.953rem | 31px | 600 | 1.3 |
| H4 | 1.563rem | 25px | 600 | 1.35 |
| H5 | 1.25rem | 20px | 600 | 1.4 |
| Body Large | 1.125rem | 18px | 400 | 1.6 |
| Body | 1rem | 16px | 400 | 1.5 |
| Small | 0.875rem | 14px | 400 | 1.5 |
| Caption | 0.75rem | 12px | 400 | 1.4 |

### Responsive Adjustments
```css
/* Mobile (< 768px) */
h1 { font-size: 2rem; }    /* 32px */
h2 { font-size: 1.5rem; }  /* 24px */
h3 { font-size: 1.25rem; } /* 20px */
body { font-size: 1rem; }  /* 16px */

/* Desktop (>= 768px) */
h1 { font-size: 3rem; }    /* 48px */
h2 { font-size: 2.25rem; } /* 36px */
h3 { font-size: 1.75rem; } /* 28px */
body { font-size: 1rem; }  /* 16px */
```

## Font Weights

### Weight Scale
| Name | Value | Usage |
|------|-------|-------|
| Regular | 400 | Body text, paragraphs |
| Medium | 500 | Buttons, nav items |
| Semibold | 600 | Subheadings, emphasis |
| Bold | 700 | Headings, CTAs |

### Weight Pairing
- Headings: 600-700
- Body: 400
- Links: 500
- Buttons: 600

## Line Height Guidelines

### Rules
| Content Type | Line Height | Notes |
|--------------|-------------|-------|
| Headings | 1.1-1.3 | Tighter for visual impact |
| Body text | 1.5-1.6 | Optimal readability |
| Small text | 1.4-1.5 | Slightly tighter |
| Long-form | 1.6-1.75 | Extra comfortable |

## Letter Spacing

### Guidelines
| Element | Tracking | Value |
|---------|----------|-------|
| Display | Tighter | -0.02em |
| Headings | Normal | 0 |
| Body | Normal | 0 |
| All caps | Wider | 0.05em |
| Small caps | Wider | 0.1em |

## Paragraph Spacing

### Margins
```css
/* Heading spacing */
h1, h2 { margin-top: 2rem; margin-bottom: 1rem; }
h3, h4 { margin-top: 1.5rem; margin-bottom: 0.75rem; }

/* Paragraph spacing */
p { margin-bottom: 1rem; }
p + p { margin-top: 0; }
```

### Maximum Line Length
- Body text: 65-75 characters (optimal)
- Headings: Can be wider
- Code blocks: 80-100 characters

```css
.prose {
  max-width: 65ch;
}
```

## CSS Implementation

### Full Variables
```css
:root {
  /* Font Families */
  --font-heading: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Font Sizes */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;

  /* Font Weights */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
}
```

### Tailwind Config
```javascript
theme: {
  fontFamily: {
    heading: ['Inter', 'system-ui', 'sans-serif'],
    body: ['Inter', 'system-ui', 'sans-serif'],
    mono: ['JetBrains Mono', 'monospace'],
  },
  fontSize: {
    xs: ['0.75rem', { lineHeight: '1rem' }],
    sm: ['0.875rem', { lineHeight: '1.25rem' }],
    base: ['1rem', { lineHeight: '1.5rem' }],
    lg: ['1.125rem', { lineHeight: '1.75rem' }],
    xl: ['1.25rem', { lineHeight: '1.75rem' }],
    '2xl': ['1.5rem', { lineHeight: '2rem' }],
    '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
    '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
    '5xl': ['3rem', { lineHeight: '1.1' }],
  }
}
```

## Common Font Pairings

### Clean & Modern
- Heading: Inter
- Body: Inter

### Professional
- Heading: Playfair Display
- Body: Source Sans Pro

### Startup/Tech
- Heading: Poppins
- Body: Open Sans

### Editorial
- Heading: Merriweather
- Body: Lato

## Accessibility

### Minimum Sizes
- Body text: 16px minimum
- Small text: 14px minimum, not for long content
- Caption: 12px minimum, use sparingly

### Contrast Requirements
- Text on background: 4.5:1 minimum (AA)
- Large text (18px+): 3:1 minimum

### Best Practices
- Don't use all caps for long text
- Avoid justified text (use left-align)
- Ensure adequate line spacing
- Don't use thin weights (<400) at small sizes



---

## `references/update.md`

Update brand colors, typography, and style - automatically syncs to all design system files.

<args>$ARGUMENTS</args>

## Overview

This command systematically updates:
1. `docs/brand-guidelines.md` - Human-readable brand doc
2. `assets/design-tokens.json` - Token source of truth
3. `assets/design-tokens.css` - Generated CSS variables

## Workflow

### Step 1: Gather Brand Input

Use `AskUserQuestion` to collect:

**Theme Selection:**
- Theme name (e.g., "Ocean Professional", "Electric Creative", "Forest Calm")

**Primary Color:**
- Color name (e.g., "Ocean Blue", "Coral", "Forest Green")
- Hex code (e.g., #3B82F6)

**Secondary Color:**
- Color name (e.g., "Golden Amber", "Electric Purple")
- Hex code

**Accent Color:**
- Color name (e.g., "Emerald", "Neon Mint")
- Hex code

**Brand Mood (for AI image generation):**
- Mood keywords (e.g., "professional, trustworthy, premium" or "bold, creative, energetic")

### Step 2: Update Brand Guidelines

Edit `docs/brand-guidelines.md`:

1. **Quick Reference table** - Update color names and hex codes
2. **Brand Concept section** - Update theme name and description
3. **Color Palette section** - Update Primary, Secondary, Accent colors with shades
4. **AI Image Generation section** - Update base prompt, keywords, mood descriptors

### Step 3: Sync to Design Tokens

Run the sync script:
```bash
node scripts/sync-brand-to-tokens.cjs
```

If the script reports an existing token source, inspect the named file before
continuing. Detection covers `:root` custom properties, Tailwind v4 `@theme`
variables in common CSS entry points and their local imports, and Tailwind
theme colors or presets. Do not create a parallel token system beside those
sources. Use `--force` only when the detected source is the managed
`assets/design-tokens.*` output from an earlier sync and replacing it is
intentional:
```bash
node scripts/sync-brand-to-tokens.cjs --force
```

This will:
- Update `assets/design-tokens.json` with new color names and values
- Regenerate `assets/design-tokens.css` with correct CSS variables

### Step 4: Verify Sync

Confirm all files are updated:
```bash
# Check brand context extraction
node scripts/inject-brand-context.cjs --json | head -30

# Check CSS variables
grep "primary" assets/design-tokens.css | head -5
```

### Step 5: Report

Output summary:
- Theme: [name]
- Primary: [name] ([hex])
- Secondary: [name] ([hex])
- Accent: [name] ([hex])
- Files updated: brand-guidelines.md, design-tokens.json, design-tokens.css

## Files Modified

| File | Purpose |
|------|---------|
| `docs/brand-guidelines.md` | Human-readable brand documentation |
| `assets/design-tokens.json` | Token definitions (primitive→semantic→component) |
| `assets/design-tokens.css` | CSS variables for UI components |

## Skills Used

- `brand` - Brand context extraction and sync
- `design-system` - Token generation

## Examples

```bash
# Interactive mode
/brand:update

# With theme hint
/brand:update "Ocean Professional"

# Quick preset
/brand:update "midnight purple"
```

## Color Presets

If user specifies a preset name, use these defaults:

| Preset | Primary | Secondary | Accent |
|--------|---------|-----------|--------|
| ocean-professional | #3B82F6 Ocean Blue | #F59E0B Golden Amber | #10B981 Emerald |
| electric-creative | #FF6B6B Coral | #9B5DE5 Electric Purple | #00F5D4 Neon Mint |
| forest-calm | #059669 Forest Green | #92400E Warm Brown | #FBBF24 Sunlight |
| midnight-purple | #7C3AED Violet | #EC4899 Pink | #06B6D4 Cyan |
| sunset-warm | #F97316 Orange | #DC2626 Red | #FACC15 Yellow |

## Important

- **Always sync all three files** - Never update just brand-guidelines.md alone
- **Verify extraction** - Run inject-brand-context.cjs after update to confirm
- **Test image generation** - Optionally generate a test image to verify brand application



---

## `references/visual-identity.md`

# Visual Identity Basics

## Core Visual Elements

### Logo
- **Primary:** Full logo (horizontal/stacked)
- **Secondary:** Abbreviated version
- **Icon/Mark:** Symbol only
- **Clear space:** Minimum padding around logo
- **Minimum size:** Smallest readable size

### Color Palette
```
Primary Colors (1-2)
├── Main brand color
└── Supporting primary

Secondary Colors (2-3)
├── Accent colors
└── Supporting visuals

Neutrals (3-4)
├── Text colors
├── Background colors
└── UI elements
```

### Typography
| Usage | Font | Weight | Size |
|-------|------|--------|------|
| H1 | [Font] | Bold | 32-48px |
| H2 | [Font] | Semibold | 24-32px |
| Body | [Font] | Regular | 16-18px |
| Caption | [Font] | Regular | 12-14px |

## Visual Guidelines Template

```markdown
## Logo Usage

### Correct Usage
- [Guidelines for proper logo use]

### Incorrect Usage
- Don't stretch or distort
- Don't change colors (unless approved)
- Don't add effects
- Don't place on busy backgrounds

## Color Specifications

### Primary Palette
| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| [Name] | #XXXXXX | r,g,b | [Where to use] |

### Accessibility
- Text contrast ratio: 4.5:1 minimum
- Button contrast: WCAG AA compliant

## Imagery Style

### Photography
- [Lighting preferences]
- [Subject guidelines]
- [Composition rules]
- [Editing style]

### Illustrations
- [Style description]
- [Color usage]
- [Complexity level]

### Icons
- [Style: outlined/filled/duotone]
- [Stroke weight]
- [Corner radius]
```

## Quick Checks

### Logo
- [ ] Correct version for context
- [ ] Sufficient clear space
- [ ] Legible at size used
- [ ] Correct color for background

### Colors
- [ ] From approved palette
- [ ] Accessible contrast
- [ ] Consistent across materials

### Typography
- [ ] Correct fonts
- [ ] Appropriate hierarchy
- [ ] Readable size



---

## `references/voice-framework.md`

# Brand Voice Framework

## Voice vs. Tone

**Voice** = Brand's personality (consistent)
**Tone** = How voice adapts to context (variable)

Example: A friendly brand (voice) might be celebratory in a win announcement but empathetic in a support response (tone).

## Voice Dimensions

### Tone Spectrum
```
Formal ←――――――――――――――→ Casual
[Legal docs]     [Social media]
```

### Language Spectrum
```
Simple ←――――――――――――――→ Complex
[Consumer]       [Technical B2B]
```

### Character Spectrum
```
Serious ←――――――――――――――→ Playful
[Finance]        [Entertainment]
```

### Emotion Spectrum
```
Reserved ←――――――――――――――→ Expressive
[Corporate]      [Lifestyle brand]
```

## Voice Development Process

### Step 1: Define Personality Traits
Choose 3-5 traits that describe your brand:
- Confident, not arrogant
- Friendly, not unprofessional
- Knowledgeable, not condescending
- Innovative, not gimmicky
- Authentic, not casual

### Step 2: Create Voice Chart

| Trait | Description | Do | Don't |
|-------|-------------|-----|-------|
| [Trait] | [Meaning] | [Example] | [Example] |

### Step 3: Context Adaptation

| Context | Tone Shift | Example |
|---------|------------|---------|
| Social media | More casual | "Hey there!" |
| Support | More empathetic | "We understand..." |
| Legal | More formal | "In accordance with..." |
| Sales | More confident | "You'll see results..." |

## Voice Testing

Ask these questions:
1. Does this sound like our brand?
2. Would a competitor say this?
3. Does it resonate with our audience?
4. Is it consistent with our values?

## Voice Guide Template

```markdown
## [Brand] Voice Guide

### We Are
- [Trait 1]: [Description]
- [Trait 2]: [Description]
- [Trait 3]: [Description]

### We Sound Like
[Example phrases]

### We Don't Sound Like
[Anti-examples]

### Sample Rewrites
Before: [Generic copy]
After: [Branded copy]
```



---

## `scripts/extract-colors.cjs`

````js
#!/usr/bin/env node
/**
 * extract-colors.cjs
 *
 * Extract dominant colors from an image and compare against brand palette.
 * Uses pure Node.js without external image processing dependencies.
 *
 * For full color extraction from images, integrate with ai-multimodal skill
 * or use ImageMagick via shell commands.
 *
 * Usage:
 *   node extract-colors.cjs <image-path>
 *   node extract-colors.cjs <image-path> --brand-file <path>
 *   node extract-colors.cjs --palette  # Show brand palette from guidelines
 *
 * Integration:
 *   For image color analysis, use: ai-multimodal skill or ImageMagick
 *   magick <image> -colors 10 -depth 8 -format "%c" histogram:info:
 */

const fs = require("fs");
const path = require("path");

// Default brand guidelines path
const DEFAULT_GUIDELINES_PATH = "docs/brand-guidelines.md";

/**
 * Extract hex colors from markdown content
 */
function extractHexColors(text) {
  const hexPattern = /#[0-9A-Fa-f]{6}\b/g;
  return [...new Set(text.match(hexPattern) || [])];
}

/**
 * Parse brand guidelines for color palette
 */
function parseBrandColors(guidelinesPath) {
  const resolvedPath = path.isAbsolute(guidelinesPath)
    ? guidelinesPath
    : path.join(process.cwd(), guidelinesPath);

  if (!fs.existsSync(resolvedPath)) {
    return null;
  }

  const content = fs.readFileSync(resolvedPath, "utf-8");

  const palette = {
    primary: [],
    secondary: [],
    neutral: [],
    semantic: [],
    all: [],
  };

  // Extract colors from different sections
  const sections = [
    { name: "primary", regex: /### Primary[\s\S]*?(?=###|##|$)/i },
    { name: "secondary", regex: /### Secondary[\s\S]*?(?=###|##|$)/i },
    { name: "neutral", regex: /### Neutral[\s\S]*?(?=###|##|$)/i },
    { name: "semantic", regex: /### Semantic[\s\S]*?(?=###|##|$)/i },
  ];

  sections.forEach(({ name, regex }) => {
    const match = content.match(regex);
    if (match) {
      const colors = extractHexColors(match[0]);
      palette[name] = colors;
      palette.all.push(...colors);
    }
  });

  // Dedupe all
  palette.all = [...new Set(palette.all)];

  return palette;
}

/**
 * Convert hex to RGB
 */
function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result
    ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16),
      }
    : null;
}

/**
 * Convert RGB to hex
 */
function rgbToHex(r, g, b) {
  return (
    "#" +
    [r, g, b]
      .map((x) => {
        const hex = Math.round(x).toString(16);
        return hex.length === 1 ? "0" + hex : hex;
      })
      .join("")
      .toUpperCase()
  );
}

/**
 * Calculate color distance (Euclidean in RGB space)
 */
function colorDistance(color1, color2) {
  const rgb1 = typeof color1 === "string" ? hexToRgb(color1) : color1;
  const rgb2 = typeof color2 === "string" ? hexToRgb(color2) : color2;

  if (!rgb1 || !rgb2) return Infinity;

  return Math.sqrt(
    Math.pow(rgb1.r - rgb2.r, 2) +
      Math.pow(rgb1.g - rgb2.g, 2) +
      Math.pow(rgb1.b - rgb2.b, 2)
  );
}

/**
 * Find nearest brand color
 */
function findNearestBrandColor(color, brandColors) {
  let nearest = null;
  let minDistance = Infinity;

  brandColors.forEach((brandColor) => {
    const distance = colorDistance(color, brandColor);
    if (distance < minDistance) {
      minDistance = distance;
      nearest = brandColor;
    }
  });

  return { color: nearest, distance: minDistance };
}

/**
 * Calculate brand compliance percentage
 * Distance threshold: 50 (out of max ~441 for RGB)
 */
function calculateCompliance(extractedColors, brandColors, threshold = 50) {
  if (!extractedColors || extractedColors.length === 0) return 100;
  if (!brandColors || brandColors.length === 0) return 0;

  let matchCount = 0;

  extractedColors.forEach((color) => {
    const nearest = findNearestBrandColor(color, brandColors);
    if (nearest.distance <= threshold) {
      matchCount++;
    }
  });

  return Math.round((matchCount / extractedColors.length) * 100);
}

/**
 * Generate ImageMagick command for color extraction
 */
function generateImageMagickCommand(imagePath, numColors = 10) {
  return `magick "${imagePath}" -colors ${numColors} -depth 8 -format "%c" histogram:info:`;
}

/**
 * Parse ImageMagick histogram output to extract colors
 */
function parseImageMagickOutput(output) {
  const colors = [];
  const lines = output.trim().split("\n");

  lines.forEach((line) => {
    // Match pattern like: 12345: (255,128,64) #FF8040 srgb(255,128,64)
    const hexMatch = line.match(/#([0-9A-Fa-f]{6})/);
    const countMatch = line.match(/^\s*(\d+):/);

    if (hexMatch) {
      colors.push({
        hex: "#" + hexMatch[1].toUpperCase(),
        count: countMatch ? parseInt(countMatch[1]) : 0,
      });
    }
  });

  // Sort by count (most common first)
  colors.sort((a, b) => b.count - a.count);

  return colors;
}

/**
 * Display brand palette
 */
function displayPalette(palette) {
  console.log("\n" + "=".repeat(50));
  console.log("BRAND COLOR PALETTE");
  console.log("=".repeat(50));

  if (palette.primary.length > 0) {
    console.log("\nPrimary Colors:");
    palette.primary.forEach((c) => console.log(`  ${c}`));
  }

  if (palette.secondary.length > 0) {
    console.log("\nSecondary Colors:");
    palette.secondary.forEach((c) => console.log(`  ${c}`));
  }

  if (palette.neutral.length > 0) {
    console.log("\nNeutral Colors:");
    palette.neutral.forEach((c) => console.log(`  ${c}`));
  }

  if (palette.semantic.length > 0) {
    console.log("\nSemantic Colors:");
    palette.semantic.forEach((c) => console.log(`  ${c}`));
  }

  console.log("\n" + "=".repeat(50));
  console.log(`Total: ${palette.all.length} colors in brand palette`);
  console.log("=".repeat(50) + "\n");
}

/**
 * Main function
 */
function main() {
  const args = process.argv.slice(2);
  const jsonOutput = args.includes("--json");
  const showPalette = args.includes("--palette");
  const brandFileIdx = args.indexOf("--brand-file");
  const brandFile =
    brandFileIdx !== -1 ? args[brandFileIdx + 1] : DEFAULT_GUIDELINES_PATH;
  const brandFileValue = brandFileIdx !== -1 ? args[brandFileIdx + 1] : null;
  const imagePath = args.find(
    (a) => !a.startsWith("--") && a !== brandFileValue
  );

  // Load brand palette
  const brandPalette = parseBrandColors(brandFile);

  if (!brandPalette) {
    console.error(`Brand guidelines not found at: ${brandFile}`);
    console.error(`Create brand guidelines or specify path with --brand-file`);
    process.exit(1);
  }

  // Show palette mode
  if (showPalette || !imagePath) {
    if (jsonOutput) {
      console.log(JSON.stringify(brandPalette, null, 2));
    } else {
      displayPalette(brandPalette);

      if (!imagePath) {
        console.log("To extract colors from an image:");
        console.log("  node extract-colors.cjs <image-path>");
        console.log("\nOr use ImageMagick directly:");
        console.log('  magick image.png -colors 10 -depth 8 -format "%c" histogram:info:');
      }
    }
    return;
  }

  // Resolve image path
  const resolvedPath = path.isAbsolute(imagePath)
    ? imagePath
    : path.join(process.cwd(), imagePath);

  if (!fs.existsSync(resolvedPath)) {
    console.error(`Image not found: ${resolvedPath}`);
    process.exit(1);
  }

  // Generate extraction instructions
  const result = {
    image: resolvedPath,
    brandPalette: brandPalette,
    extractionCommand: generateImageMagickCommand(resolvedPath),
    instructions: [
      "1. Run the ImageMagick command to extract colors:",
      `   ${generateImageMagickCommand(resolvedPath)}`,
      "",
      "2. Or use an image-analysis skill (e.g. ai-multimodal, if installed) to extract the 10 most dominant colors as hex values",
      "",
      "3. Then compare extracted colors against brand palette",
    ],
    complianceCheck: {
      threshold: 50,
      description:
        "Colors within distance 50 (RGB space) are considered brand-compliant",
      brandColors: brandPalette.all,
    },
  };

  if (jsonOutput) {
    console.log(JSON.stringify(result, null, 2));
  } else {
    console.log("\n" + "=".repeat(60));
    console.log("COLOR EXTRACTION HELPER");
    console.log("=".repeat(60));
    console.log(`\nImage: ${result.image}`);
    console.log(`\nBrand Colors: ${brandPalette.all.length} colors loaded`);
    console.log("\nTo extract colors from this image:\n");
    result.instructions.forEach((line) => console.log(line));
    console.log("\n" + "=".repeat(60));

    // Show brand palette for reference
    console.log("\nBrand Palette Reference:");
    console.log(`  Primary: ${brandPalette.primary.join(", ") || "none"}`);
    console.log(`  Secondary: ${brandPalette.secondary.join(", ") || "none"}`);
    console.log(`  Neutral: ${brandPalette.neutral.join(", ") || "none"}`);
    console.log("=".repeat(60) + "\n");
  }
}

// Export functions for use as module
module.exports = {
  parseBrandColors,
  hexToRgb,
  rgbToHex,
  colorDistance,
  findNearestBrandColor,
  calculateCompliance,
  parseImageMagickOutput,
};

// Run if called directly
if (require.main === module) {
  main();
}
````



---

## `scripts/inject-brand-context.cjs`

````js
#!/usr/bin/env node
/**
 * inject-brand-context.cjs
 *
 * Extracts brand context from markdown brand guidelines
 * and outputs a formatted system prompt addition.
 *
 * Usage:
 *   node inject-brand-context.cjs [path-to-guidelines]
 *   node inject-brand-context.cjs --json [path-to-guidelines]
 *
 * Default path: docs/brand-guidelines.md
 */

const fs = require("fs");
const path = require("path");

// Default brand guidelines path
const DEFAULT_GUIDELINES_PATH = "docs/brand-guidelines.md";

/**
 * Extract hex colors from text
 */
function extractHexColors(text) {
  const hexPattern = /#[0-9A-Fa-f]{6}\b/g;
  return [...new Set(text.match(hexPattern) || [])];
}

/**
 * Extract color data from markdown table
 */
function extractColorsFromTable(content) {
  const colors = {
    primary: [],
    secondary: [],
    neutral: [],
    semantic: [],
  };

  // Find color tables
  const primaryMatch = content.match(
    /### Primary Colors[\s\S]*?\|[\s\S]*?(?=###|$)/i
  );
  const secondaryMatch = content.match(
    /### Secondary Colors[\s\S]*?\|[\s\S]*?(?=###|$)/i
  );
  const neutralMatch = content.match(
    /### Neutral[\s\S]*?\|[\s\S]*?(?=###|$)/i
  );
  const semanticMatch = content.match(
    /### Semantic[\s\S]*?\|[\s\S]*?(?=###|$)/i
  );

  if (primaryMatch) colors.primary = extractHexColors(primaryMatch[0]);
  if (secondaryMatch) colors.secondary = extractHexColors(secondaryMatch[0]);
  if (neutralMatch) colors.neutral = extractHexColors(neutralMatch[0]);
  if (semanticMatch) colors.semantic = extractHexColors(semanticMatch[0]);

  return colors;
}

/**
 * Extract typography info
 */
function extractTypography(content) {
  const typography = {
    heading: null,
    body: null,
    mono: null,
  };

  // Look for font definitions
  const headingMatch = content.match(/--font-heading:\s*['"]([^'"]+)['"]/);
  const bodyMatch = content.match(/--font-body:\s*['"]([^'"]+)['"]/);
  const monoMatch = content.match(/--font-mono:\s*['"]([^'"]+)['"]/);

  // Fallback: look in tables
  const fontStackMatch = content.match(/### Font Stack[\s\S]*?(?=###|##|$)/i);
  if (fontStackMatch) {
    const stackText = fontStackMatch[0];
    const headingAlt = stackText.match(/heading[^']*['"]([^'"]+)['"]/i);
    const bodyAlt = stackText.match(/body[^']*['"]([^'"]+)['"]/i);

    if (headingAlt) typography.heading = headingAlt[1];
    if (bodyAlt) typography.body = bodyAlt[1];
  }

  if (headingMatch) typography.heading = headingMatch[1];
  if (bodyMatch) typography.body = bodyMatch[1];
  if (monoMatch) typography.mono = monoMatch[1];

  return typography;
}

/**
 * Extract voice/tone information
 */
function extractVoice(content) {
  const voice = {
    traits: [],
    prohibited: [],
    personality: "",
  };

  // Extract personality traits from table
  const personalityMatch = content.match(
    /### Brand Personality[\s\S]*?\|[\s\S]*?(?=###|##|$)/i
  );
  if (personalityMatch) {
    const traits = personalityMatch[0].match(
      /\*\*([^*]+)\*\*\s*\|\s*([^|]+)/g
    );
    if (traits) {
      voice.traits = traits.map((t) => {
        const match = t.match(/\*\*([^*]+)\*\*/);
        return match ? match[1].trim() : "";
      }).filter(Boolean);
    }
  }

  // Extract prohibited terms
  const prohibitedMatch = content.match(
    /### Prohibited[\s\S]*?(?=###|##|$)/i
  );
  if (prohibitedMatch) {
    const terms = prohibitedMatch[0].match(/\|\s*([^|]+)\s*\|/g);
    if (terms) {
      voice.prohibited = terms
        .map((t) => t.replace(/\|/g, "").trim())
        .filter((t) => t && !t.includes("Avoid") && !t.includes("---"));
    }
  }

  // Fallback: look for Forbidden Phrases
  const forbiddenMatch = content.match(
    /### Forbidden Phrases[\s\S]*?(?=###|##|$)/i
  );
  if (forbiddenMatch && voice.prohibited.length === 0) {
    const items = forbiddenMatch[0].match(/-\s*["']?([^"'\n(]+)/g);
    if (items) {
      voice.prohibited = items
        .map((item) => item.replace(/^-\s*["']?/, "").trim())
        .filter(Boolean);
    }
  }

  voice.personality = voice.traits.join(", ");

  return voice;
}

/**
 * Extract core attributes
 */
function extractCoreAttributes(content) {
  const attributes = [];

  const attributesMatch = content.match(
    /### Core Attributes[\s\S]*?\|[\s\S]*?(?=###|##|$)/i
  );
  if (attributesMatch) {
    const rows = attributesMatch[0].match(
      /\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\|/g
    );
    if (rows) {
      rows.forEach((row) => {
        const match = row.match(/\*\*([^*]+)\*\*\s*\|\s*([^|]+)/);
        if (match) {
          attributes.push({
            name: match[1].trim(),
            description: match[2].trim(),
          });
        }
      });
    }
  }

  return attributes;
}

/**
 * Extract AI image generation context
 */
function extractImageStyle(content) {
  const imageStyle = {
    basePrompt: "",
    keywords: [],
    mood: [],
    donts: [],
    examplePrompts: [],
  };

  // Extract base prompt template (content between ``` blocks after "Base Prompt Template")
  const basePromptMatch = content.match(
    /### Base Prompt Template[\s\S]*?```\n?([\s\S]*?)```/i
  );
  if (basePromptMatch) {
    imageStyle.basePrompt = basePromptMatch[1].trim().replace(/\n/g, " ");
  }

  // Extract style keywords from table
  const keywordsMatch = content.match(
    /### Style Keywords[\s\S]*?\|[\s\S]*?(?=###|##|$)/i
  );
  if (keywordsMatch) {
    const keywordRows = keywordsMatch[0].match(/\|\s*\*\*[^*]+\*\*\s*\|\s*([^|]+)\|/g);
    if (keywordRows) {
      keywordRows.forEach((row) => {
        const match = row.match(/\|\s*\*\*[^*]+\*\*\s*\|\s*([^|]+)\|/);
        if (match) {
          const keywords = match[1].split(",").map((k) => k.trim()).filter(Boolean);
          imageStyle.keywords.push(...keywords);
        }
      });
    }
  }

  // Extract visual mood descriptors (bullet points)
  const moodMatch = content.match(
    /### Visual Mood Descriptors[\s\S]*?(?=###|##|$)/i
  );
  if (moodMatch) {
    const moodItems = moodMatch[0].match(/-\s*([^\n]+)/g);
    if (moodItems) {
      imageStyle.mood = moodItems.map((item) => item.replace(/^-\s*/, "").trim());
    }
  }

  // Extract visual don'ts from table
  const dontsMatch = content.match(
    /### Visual Don'ts[\s\S]*?\|[\s\S]*?(?=###|##|$)/i
  );
  if (dontsMatch) {
    const dontRows = dontsMatch[0].match(/\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|/g);
    if (dontRows) {
      dontRows.forEach((row) => {
        const match = row.match(/\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|/);
        if (match && !match[1].includes("Avoid") && !match[1].includes("---")) {
          imageStyle.donts.push(match[1].trim());
        }
      });
    }
  }

  // Extract example prompts (content between ``` blocks after specific headers)
  const exampleMatch = content.match(/### Example Prompts[\s\S]*?(?=##|$)/i);
  if (exampleMatch) {
    const prompts = exampleMatch[0].match(/\*\*([^*]+)\*\*:\s*```\n?([\s\S]*?)```/g);
    if (prompts) {
      prompts.forEach((p) => {
        const match = p.match(/\*\*([^*]+)\*\*:\s*```\n?([\s\S]*?)```/);
        if (match) {
          imageStyle.examplePrompts.push({
            type: match[1].trim(),
            prompt: match[2].trim().replace(/\n/g, " "),
          });
        }
      });
    }
  }

  return imageStyle;
}

/**
 * Generate system prompt addition
 */
function generatePromptAddition(brandContext) {
  const { colors, typography, voice, attributes, imageStyle } = brandContext;

  let prompt = `
BRAND CONTEXT:
==============

VISUAL IDENTITY:
- Primary Colors: ${colors.primary.join(", ") || "Not specified"}
- Secondary Colors: ${colors.secondary.join(", ") || "Not specified"}
- Typography: ${typography.heading || typography.body || "System fonts"}

BRAND VOICE:
- Personality: ${voice.personality || "Professional"}
- Core Attributes: ${attributes.map((a) => a.name).join(", ") || "Not specified"}

CONTENT RULES:
- Prohibited Terms: ${voice.prohibited.join(", ") || "None specified"}
`;

  // Add image style context if available
  if (imageStyle && imageStyle.basePrompt) {
    prompt += `
IMAGE GENERATION:
- Base Prompt: ${imageStyle.basePrompt}
- Style Keywords: ${imageStyle.keywords.slice(0, 10).join(", ") || "Not specified"}
- Visual Mood: ${imageStyle.mood.slice(0, 5).join("; ") || "Not specified"}
- Avoid: ${imageStyle.donts.join(", ") || "None specified"}
`;
  }

  prompt += `
Apply these brand guidelines to all generated content.
Maintain consistent voice, colors, and messaging.
`;

  return prompt.trim();
}

/**
 * Main function
 */
function main() {
  const args = process.argv.slice(2);
  const jsonOutput = args.includes("--json");
  const guidelinesPath = args.find((a) => !a.startsWith("--")) || DEFAULT_GUIDELINES_PATH;

  // Resolve path
  const resolvedPath = path.isAbsolute(guidelinesPath)
    ? guidelinesPath
    : path.join(process.cwd(), guidelinesPath);

  // Check if file exists
  if (!fs.existsSync(resolvedPath)) {
    console.error(`Error: Brand guidelines not found at ${resolvedPath}`);
    console.error(`Create brand guidelines at ${DEFAULT_GUIDELINES_PATH} or specify a path.`);
    process.exit(1);
  }

  // Read file
  const content = fs.readFileSync(resolvedPath, "utf-8");

  // Extract brand context
  const brandContext = {
    colors: extractColorsFromTable(content),
    typography: extractTypography(content),
    voice: extractVoice(content),
    attributes: extractCoreAttributes(content),
    imageStyle: extractImageStyle(content),
    source: resolvedPath,
    extractedAt: new Date().toISOString(),
  };

  // Output
  if (jsonOutput) {
    console.log(JSON.stringify(brandContext, null, 2));
  } else {
    console.log(generatePromptAddition(brandContext));
  }
}

main();
````



---

## `scripts/sync-brand-to-tokens.cjs`

````js
#!/usr/bin/env node
/**
 * sync-brand-to-tokens.cjs
 *
 * Syncs brand-guidelines.md colors → design-tokens.json → design-tokens.css
 *
 * Usage:
 *   node sync-brand-to-tokens.cjs
 *   node sync-brand-to-tokens.cjs --dry-run
 *   node sync-brand-to-tokens.cjs --force
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

// Paths
const BRAND_GUIDELINES = 'docs/brand-guidelines.md';
const DESIGN_TOKENS_JSON = 'assets/design-tokens.json';
const DESIGN_TOKENS_CSS = 'assets/design-tokens.css';
const CSS_TOKEN_SOURCES = [
  'src/index.css',
  'src/main.css',
  'src/app.css',
  'src/global.css',
  'src/globals.css',
  'src/styles/global.css',
  'src/styles/globals.css',
  'src/styles/index.css',
  'src/styles/main.css',
  'src/styles/tokens.css',
  'src/app/global.css',
  'src/app/globals.css',
  'app/global.css',
  'app/globals.css',
  'styles/global.css',
  'styles/globals.css',
  'styles/tokens.css'
];
// Directories shallow-scanned for any *.css that already declares tokens.
// A hardcoded filename list alone misses real projects by a single letter
// (e.g. styles/global.css vs styles/globals.css), which silently defeats the
// overwrite guard.
const CSS_SCAN_DIRS = [
  'src',
  'src/styles',
  'src/css',
  'src/assets/styles',
  'app',
  'app/styles',
  'styles',
  'css'
];
const TAILWIND_CONFIGS = [
  'tailwind.config.js',
  'tailwind.config.cjs',
  'tailwind.config.mjs',
  'tailwind.config.ts'
];
// Sibling sub-skill, resolved from this file's location so it works in every
// install context (plugin cache, project or --global CLI install), not only
// when the process runs from a project root that contains .claude/skills/.
const GENERATE_TOKENS_SCRIPT = path.resolve(__dirname, '..', '..', 'design-system', 'scripts', 'generate-tokens.cjs');

/**
 * Find project files that already act as design-token sources.
 */
function findExistingTokenSources(projectRoot) {
  const sources = new Set();
  const addIfPresent = (relativePath) => {
    if (fs.existsSync(path.resolve(projectRoot, relativePath))) {
      sources.add(relativePath);
    }
  };

  const scanCssSource = (absolutePath, visited = new Set()) => {
    const normalizedPath = path.resolve(absolutePath);
    const relativePath = path.relative(projectRoot, normalizedPath);
    if (
      visited.has(normalizedPath) ||
      relativePath.startsWith('..') ||
      path.isAbsolute(relativePath) ||
      !fs.existsSync(normalizedPath)
    ) {
      return;
    }

    visited.add(normalizedPath);
    const content = fs.readFileSync(normalizedPath, 'utf-8');
    const uncommented = content.replace(/\/\*[\s\S]*?\*\//g, '');
    const hasRootTokens = /:root\b[^{}]*\{[^}]*--[A-Za-z0-9_-]+\s*:/.test(uncommented);
    const hasTailwindTheme = /@theme(?:\s+[A-Za-z-]+)?\s*\{[^}]*--[A-Za-z0-9_-]+\s*:/.test(uncommented);
    if (hasRootTokens || hasTailwindTheme) {
      sources.add(relativePath.split(path.sep).join('/'));
    }

    const importPattern = /@import\s+(?:url\(\s*)?(['"])([^'"]+)\1\s*\)?[^;]*;/g;
    for (const match of uncommented.matchAll(importPattern)) {
      const importTarget = match[2].split(/[?#]/, 1)[0];
      let importedPath;
      if (importTarget.startsWith('.')) {
        importedPath = path.resolve(path.dirname(normalizedPath), importTarget);
      } else if (importTarget.startsWith('/')) {
        importedPath = path.resolve(projectRoot, `.${importTarget}`);
      } else {
        continue;
      }
      scanCssSource(importedPath, visited);
    }
  };

  addIfPresent(DESIGN_TOKENS_JSON);
  addIfPresent(DESIGN_TOKENS_CSS);

  const candidates = new Set(CSS_TOKEN_SOURCES);
  for (const dir of CSS_SCAN_DIRS) {
    const absoluteDir = path.resolve(projectRoot, dir);
    let entries;
    try {
      entries = fs.readdirSync(absoluteDir, { withFileTypes: true });
    } catch {
      continue;
    }
    for (const entry of entries) {
      if (entry.isFile() && entry.name.toLowerCase().endsWith('.css')) {
        candidates.add(`${dir}/${entry.name}`);
      }
    }
  }

  for (const relativePath of candidates) {
    const absolutePath = path.resolve(projectRoot, relativePath);
    scanCssSource(absolutePath);
  }

  for (const relativePath of TAILWIND_CONFIGS) {
    const absolutePath = path.resolve(projectRoot, relativePath);
    if (!fs.existsSync(absolutePath)) continue;
    const content = fs.readFileSync(absolutePath, 'utf-8');
    const hasInlineColors = /\btheme\s*:\s*\{[\s\S]*?\bcolors\s*:/.test(content);
    const hasPreset = /\bpresets\s*:/.test(content);
    const hasThemeSpread = /\btheme\s*:\s*\{[\s\S]*?\.\.\.[A-Za-z_$]/.test(content);
    if (hasInlineColors || hasPreset || hasThemeSpread) {
      sources.add(relativePath);
    }
  }

  return [...sources];
}

/**
 * Extract color info from brand guidelines markdown
 */
function extractColorsFromMarkdown(content) {
  const colors = {
    primary: { name: 'primary', shades: {} },
    secondary: { name: 'secondary', shades: {} },
    accent: { name: 'accent', shades: {} }
  };

  // Match a "| Label | #hex |" markdown table row. Bold around the label
  // (**Label**) is optional, so this handles both the bundled starter template
  // ("| Primary Blue | #2563EB |") and bolded variants.
  const rowRe = /\|\s*\*{0,2}([^*|]+?)\*{0,2}\s*\|\s*#([A-Fa-f0-9]{6})\b/g;

  // 1) Quick Reference table — hex only, no parenthesized name required.
  const quickRef = {
    primary: /Primary Color\s*\|\s*#([A-Fa-f0-9]{6})/i,
    secondary: /Secondary Color\s*\|\s*#([A-Fa-f0-9]{6})/i,
    accent: /Accent Color\s*\|\s*#([A-Fa-f0-9]{6})/i
  };
  for (const key of Object.keys(quickRef)) {
    const m = content.match(quickRef[key]);
    if (m) colors[key].base = `#${m[1]}`;
  }

  // 2) Dedicated "### <Role> Colors" tables — assign base/dark/light by the
  //    row label keyword.
  const assignFromSection = (heading, target) => {
    const section = content.match(new RegExp(`### ${heading}[\\s\\S]*?(?=\\n###|$)`, 'i'));
    if (!section) return;
    for (const m of section[0].matchAll(rowRe)) {
      const label = m[1].trim().toLowerCase();
      const hex = `#${m[2]}`;
      if (label.includes('dark')) target.dark = hex;
      else if (label.includes('light')) target.light = hex;
      else if (!target.base) target.base = hex;
    }
  };
  assignFromSection('Primary Colors', colors.primary);
  assignFromSection('Secondary Colors', colors.secondary);
  assignFromSection('Accent Colors', colors.accent);

  // 3) Fallback: an accent swatch may live in another table (the starter
  //    lists "Accent Green" under Secondary Colors).
  if (!colors.accent.base) {
    for (const m of content.matchAll(rowRe)) {
      if (m[1].trim().toLowerCase().includes('accent')) {
        colors.accent.base = `#${m[2]}`;
        break;
      }
    }
  }

  return colors;
}

/**
 * Generate color scale from base color (simple approach)
 */
function generateColorScale(baseHex, darkHex, lightHex) {
  // Use provided shades or generate approximations
  return {
    "50": { "$value": lightHex || adjustBrightness(baseHex, 0.9), "$type": "color" },
    "100": { "$value": lightHex || adjustBrightness(baseHex, 0.8), "$type": "color" },
    "200": { "$value": adjustBrightness(baseHex, 0.6), "$type": "color" },
    "300": { "$value": adjustBrightness(baseHex, 0.4), "$type": "color" },
    "400": { "$value": adjustBrightness(baseHex, 0.2), "$type": "color" },
    "500": { "$value": baseHex, "$type": "color" },
    "600": { "$value": darkHex || adjustBrightness(baseHex, -0.15), "$type": "color" },
    "700": { "$value": adjustBrightness(baseHex, -0.3), "$type": "color" },
    "800": { "$value": adjustBrightness(baseHex, -0.45), "$type": "color" },
    "900": { "$value": adjustBrightness(baseHex, -0.6), "$type": "color" }
  };
}

/**
 * Adjust hex color brightness.
 *
 * Blends each channel proportionally toward white (percent > 0) or toward
 * black (percent < 0) instead of adding/subtracting a flat 255*percent to
 * every channel. The flat-shift approach clamped all three channels to 0
 * (or 255) whenever the base color's channels were already low (or high)
 * relative to the shift — e.g. darkening a dark brand color like #4A3228
 * by -0.3/-0.45/-0.6 produced #000000 for all three, collapsing shades
 * 700/800/900 into an identical, useless black.
 */
function adjustBrightness(hex, percent) {
  if (typeof hex !== 'string') return '#000000';
  const num = parseInt(hex.replace('#', ''), 16);
  const r = (num >> 16) & 0xFF;
  const g = (num >> 8) & 0xFF;
  const b = num & 0xFF;

  const adjustChannel = (channel) => {
    const adjusted = percent >= 0
      ? channel + (255 - channel) * percent
      : channel * (1 + percent);
    return Math.min(255, Math.max(0, Math.round(adjusted)));
  };

  const newR = adjustChannel(r);
  const newG = adjustChannel(g);
  const newB = adjustChannel(b);
  return `#${((newR << 16) | (newG << 8) | newB).toString(16).padStart(6, '0').toUpperCase()}`;
}

/**
 * Update design tokens JSON
 */
function updateDesignTokens(tokens, colors) {
  // Update brand name
  const brandName = `ClaudeKit Marketing - ${colors.primary.name.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')}`;
  tokens.brand = brandName;

  // Update primitive colors with new names
  tokens.primitive = tokens.primitive || {};
  const primitiveColors = tokens.primitive.color || {};

  // Remove old color keys, add new ones
  delete primitiveColors.coral;
  delete primitiveColors.purple;
  delete primitiveColors.mint;

  // Add new named colors. Skip any role with no base hex rather than crashing
  // on an unexpected guidelines format.
  for (const role of ['primary', 'secondary', 'accent']) {
    const c = colors[role];
    if (!c.base) {
      console.warn(`⚠️  No base hex found for ${role} color — skipping its token scale.`);
      continue;
    }
    primitiveColors[c.name] = generateColorScale(c.base, c.dark, c.light);
  }

  tokens.primitive.color = primitiveColors;

  // Update ALL semantic color references
  if (tokens.semantic?.color) {
    const sem = tokens.semantic.color;
    const p = colors.primary.name;
    const s = colors.secondary.name;
    const a = colors.accent.name;

    // Primary variants
    sem.primary = { "$value": `{primitive.color.${p}.500}`, "$type": "color" };
    sem['primary-hover'] = { "$value": `{primitive.color.${p}.600}`, "$type": "color" };
    sem['primary-active'] = { "$value": `{primitive.color.${p}.700}`, "$type": "color" };
    sem['primary-light'] = { "$value": `{primitive.color.${p}.400}`, "$type": "color" };
    sem['primary-lighter'] = { "$value": `{primitive.color.${p}.100}`, "$type": "color" };
    sem['primary-dark'] = { "$value": `{primitive.color.${p}.600}`, "$type": "color" };

    // Secondary variants
    sem.secondary = { "$value": `{primitive.color.${s}.500}`, "$type": "color" };
    sem['secondary-hover'] = { "$value": `{primitive.color.${s}.600}`, "$type": "color" };
    sem['secondary-light'] = { "$value": `{primitive.color.${s}.300}`, "$type": "color" };
    sem['secondary-dark'] = { "$value": `{primitive.color.${s}.600}`, "$type": "color" };

    // Accent variants
    sem.accent = { "$value": `{primitive.color.${a}.500}`, "$type": "color" };
    sem['accent-hover'] = { "$value": `{primitive.color.${a}.600}`, "$type": "color" };
    sem['accent-light'] = { "$value": `{primitive.color.${a}.300}`, "$type": "color" };

    // Status colors (use accent for success, primary for error/info)
    sem.success = { "$value": `{primitive.color.${a}.500}`, "$type": "color" };
    sem['success-light'] = { "$value": `{primitive.color.${a}.300}`, "$type": "color" };
    sem.error = { "$value": `{primitive.color.${p}.500}`, "$type": "color" };
    sem['error-light'] = { "$value": `{primitive.color.${p}.300}`, "$type": "color" };
    sem.info = { "$value": `{primitive.color.${s}.500}`, "$type": "color" };
    sem['info-light'] = { "$value": `{primitive.color.${s}.300}`, "$type": "color" };
  }

  // Update component references (button uses primary color with opacity)
  if (tokens.component?.button?.secondary && colors.primary.base) {
    const primaryBase = colors.primary.base;
    tokens.component.button.secondary['bg-hover'] = {
      "$value": `${primaryBase}1A`,
      "$type": "color"
    };
  }

  return tokens;
}

/**
 * Main
 */
function main() {
  const dryRun = process.argv.includes('--dry-run');
  const force = process.argv.includes('--force');
  const projectRoot = process.cwd();

  console.log('🔄 Syncing brand guidelines → design tokens\n');

  // Read brand guidelines
  const guidelinesPath = path.resolve(projectRoot, BRAND_GUIDELINES);
  if (!fs.existsSync(guidelinesPath)) {
    console.error(`❌ Brand guidelines not found: ${guidelinesPath}`);
    process.exit(1);
  }
  const guidelinesContent = fs.readFileSync(guidelinesPath, 'utf-8');

  const existingSources = findExistingTokenSources(projectRoot);
  if (existingSources.length > 0 && !force) {
    const details = existingSources.map(source => `   - ${source}`).join('\n');
    const message =
      `Existing design-token source${existingSources.length === 1 ? '' : 's'} detected:\n${details}\n` +
      'Refusing to create or replace token files. Review the detected source and re-run with --force only if replacement is intentional.';
    if (dryRun) {
      console.warn(`⚠️  ${message}\n`);
    } else {
      console.error(`❌ ${message}`);
      process.exit(1);
    }
  }

  // Extract colors
  const colors = extractColorsFromMarkdown(guidelinesContent);
  console.log('📊 Extracted colors:');
  console.log(`   Primary: ${colors.primary.name} (${colors.primary.base})`);
  console.log(`   Secondary: ${colors.secondary.name} (${colors.secondary.base})`);
  console.log(`   Accent: ${colors.accent.name} (${colors.accent.base})\n`);

  // Read existing tokens
  const tokensPath = path.resolve(projectRoot, DESIGN_TOKENS_JSON);
  let tokens = {};
  if (fs.existsSync(tokensPath)) {
    tokens = JSON.parse(fs.readFileSync(tokensPath, 'utf-8'));
  }

  // Update tokens
  tokens = updateDesignTokens(tokens, colors);

  if (dryRun) {
    console.log('📋 Would update design-tokens.json:');
    console.log(JSON.stringify(tokens.primitive.color, null, 2).slice(0, 500) + '...');
    console.log('\n⏭️  Dry run - no files changed');
    return;
  }

  // Write updated tokens
  fs.mkdirSync(path.dirname(tokensPath), { recursive: true });
  fs.writeFileSync(tokensPath, JSON.stringify(tokens, null, 2));
  console.log(`✅ Updated: ${DESIGN_TOKENS_JSON}`);

  // Regenerate CSS
  const generateScript = GENERATE_TOKENS_SCRIPT;
  if (fs.existsSync(generateScript)) {
    try {
      execFileSync('node', [generateScript, '--config', DESIGN_TOKENS_JSON, '-o', DESIGN_TOKENS_CSS], {
        cwd: process.cwd(),
        stdio: 'inherit'
      });
      console.log(`✅ Regenerated: ${DESIGN_TOKENS_CSS}`);
    } catch (e) {
      console.error('⚠️  Failed to regenerate CSS:', e.message);
    }
  } else {
    console.warn(`⚠️  design-system sub-skill not found at ${generateScript}; ${DESIGN_TOKENS_CSS} not regenerated`);
  }

  console.log('\n✨ Brand sync complete!');
}

main();
````



---

## `scripts/validate-asset.cjs`

````js
#!/usr/bin/env node
/**
 * validate-asset.cjs
 *
 * Validates marketing assets against brand guidelines.
 * Checks: file naming, dimensions, file size, metadata.
 *
 * Usage:
 *   node validate-asset.cjs <asset-path>
 *   node validate-asset.cjs <asset-path> --json
 *   node validate-asset.cjs <asset-path> --fix
 *
 * For color validation of images, use with extract-colors.cjs
 */

const fs = require("fs");
const path = require("path");

// Validation rules
const RULES = {
  naming: {
    pattern: /^[a-z]+_[a-z0-9-]+_[a-z0-9-]+_\d{8}(_[a-z0-9-]+)?\.[a-z]+$/,
    description:
      "{type}_{campaign}_{description}_{timestamp}_{variant}.{ext}",
    examples: [
      "banner_claude-launch_hero-image_20251209.png",
      "logo_brand-refresh_horizontal_20251209_dark.svg",
    ],
  },
  dimensions: {
    banner: { minWidth: 600, minHeight: 300 },
    logo: { minWidth: 100, minHeight: 100 },
    design: { minWidth: 800, minHeight: 600 },
    video: { minWidth: 640, minHeight: 480 },
    default: { minWidth: 100, minHeight: 100 },
  },
  fileSize: {
    image: { max: 5 * 1024 * 1024, recommended: 1 * 1024 * 1024 },
    video: { max: 100 * 1024 * 1024, recommended: 50 * 1024 * 1024 },
    svg: { max: 500 * 1024, recommended: 100 * 1024 },
  },
  formats: {
    image: ["png", "jpg", "jpeg", "webp", "gif"],
    vector: ["svg"],
    video: ["mp4", "mov", "webm"],
    document: ["pdf", "psd", "ai", "fig"],
  },
};

/**
 * Parse asset filename
 */
function parseFilename(filename) {
  const parts = filename.replace(/\.[^.]+$/, "").split("_");

  if (parts.length < 4) {
    return null;
  }

  return {
    type: parts[0],
    campaign: parts[1],
    description: parts[2],
    timestamp: parts[3],
    variant: parts.length > 4 ? parts[4] : null,
    extension: path.extname(filename).slice(1).toLowerCase(),
  };
}

/**
 * Validate filename convention
 */
function validateFilename(filename) {
  const issues = [];
  const suggestions = [];

  // Check pattern match
  if (!RULES.naming.pattern.test(filename)) {
    issues.push("Filename does not match naming convention");
    suggestions.push(`Expected format: ${RULES.naming.description}`);
    suggestions.push(`Examples: ${RULES.naming.examples.join(", ")}`);
  }

  // Parse and check components
  const parsed = parseFilename(filename);
  if (parsed) {
    // Check timestamp format
    if (!/^\d{8}$/.test(parsed.timestamp)) {
      issues.push("Timestamp should be YYYYMMDD format");
    }

    // Check kebab-case for campaign and description
    if (parsed.campaign && !/^[a-z0-9-]+$/.test(parsed.campaign)) {
      issues.push("Campaign name should be kebab-case");
    }

    if (parsed.description && !/^[a-z0-9-]+$/.test(parsed.description)) {
      issues.push("Description should be kebab-case");
    }

    // Check valid type
    const validTypes = [
      "banner",
      "logo",
      "design",
      "video",
      "infographic",
      "icon",
      "photo",
    ];
    if (!validTypes.includes(parsed.type)) {
      suggestions.push(`Consider using type: ${validTypes.join(", ")}`);
    }
  }

  return { valid: issues.length === 0, issues, suggestions, parsed };
}

/**
 * Validate file size
 */
function validateFileSize(filepath, extension) {
  const issues = [];
  const warnings = [];

  const stats = fs.statSync(filepath);
  const size = stats.size;

  let limits;
  if (RULES.formats.video.includes(extension)) {
    limits = RULES.fileSize.video;
  } else if (extension === "svg") {
    limits = RULES.fileSize.svg;
  } else {
    limits = RULES.fileSize.image;
  }

  if (size > limits.max) {
    issues.push(
      `File size (${formatBytes(size)}) exceeds maximum (${formatBytes(
        limits.max
      )})`
    );
  } else if (size > limits.recommended) {
    warnings.push(
      `File size (${formatBytes(size)}) exceeds recommended (${formatBytes(
        limits.recommended
      )})`
    );
  }

  return { valid: issues.length === 0, issues, warnings, size };
}

/**
 * Validate file format
 */
function validateFormat(extension) {
  const issues = [];
  const info = { category: null };

  const allFormats = [
    ...RULES.formats.image,
    ...RULES.formats.vector,
    ...RULES.formats.video,
    ...RULES.formats.document,
  ];

  if (!allFormats.includes(extension)) {
    issues.push(`Unsupported file format: .${extension}`);
    return { valid: false, issues, info };
  }

  // Determine category
  if (RULES.formats.image.includes(extension)) info.category = "image";
  else if (RULES.formats.vector.includes(extension)) info.category = "vector";
  else if (RULES.formats.video.includes(extension)) info.category = "video";
  else if (RULES.formats.document.includes(extension))
    info.category = "document";

  return { valid: true, issues, info };
}

/**
 * Check if asset exists in manifest
 */
function checkManifest(filepath) {
  const manifestPath = path.join(process.cwd(), ".assets", "manifest.json");

  if (!fs.existsSync(manifestPath)) {
    return { registered: false, message: "Manifest not found" };
  }

  try {
    const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf-8"));
    const relativePath = path.relative(process.cwd(), filepath);
    const found = manifest.assets?.find(
      (a) => a.path === relativePath || a.path === filepath
    );

    return {
      registered: !!found,
      message: found ? "Asset registered in manifest" : "Asset not in manifest",
      asset: found,
    };
  } catch {
    return { registered: false, message: "Error reading manifest" };
  }
}

/**
 * Generate suggested filename
 */
function suggestFilename(original, parsed) {
  if (!parsed) return null;

  const today = new Date().toISOString().slice(0, 10).replace(/-/g, "");
  const type = parsed.type || "asset";
  const campaign = parsed.campaign || "general";
  const description = parsed.description || "untitled";
  const ext = parsed.extension || "png";

  return `${type}_${campaign}_${description}_${today}.${ext}`;
}

/**
 * Format bytes to human readable
 */
function formatBytes(bytes) {
  if (bytes === 0) return "0 Bytes";
  const k = 1024;
  const sizes = ["Bytes", "KB", "MB", "GB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
}

/**
 * Main validation function
 */
function validateAsset(assetPath) {
  const results = {
    path: assetPath,
    filename: path.basename(assetPath),
    valid: true,
    issues: [],
    warnings: [],
    suggestions: [],
    checks: {},
  };

  // Check file exists
  if (!fs.existsSync(assetPath)) {
    results.valid = false;
    results.issues.push(`File not found: ${assetPath}`);
    return results;
  }

  const filename = path.basename(assetPath);
  const extension = path.extname(filename).slice(1).toLowerCase();

  // 1. Validate filename
  const filenameResult = validateFilename(filename);
  results.checks.filename = filenameResult;
  if (!filenameResult.valid) {
    results.issues.push(...filenameResult.issues);
    results.suggestions.push(...filenameResult.suggestions);
  }

  // 2. Validate format
  const formatResult = validateFormat(extension);
  results.checks.format = formatResult;
  if (!formatResult.valid) {
    results.issues.push(...formatResult.issues);
  }

  // 3. Validate file size
  const sizeResult = validateFileSize(assetPath, extension);
  results.checks.fileSize = sizeResult;
  if (!sizeResult.valid) {
    results.issues.push(...sizeResult.issues);
  }
  results.warnings.push(...sizeResult.warnings);

  // 4. Check manifest registration
  const manifestResult = checkManifest(assetPath);
  results.checks.manifest = manifestResult;
  if (!manifestResult.registered) {
    results.warnings.push("Asset not registered in manifest.json");
    results.suggestions.push(
      "Register asset in .assets/manifest.json for tracking"
    );
  }

  // 5. Suggest corrected filename if needed
  if (!filenameResult.valid && filenameResult.parsed) {
    const suggested = suggestFilename(filename, filenameResult.parsed);
    if (suggested) {
      results.suggestions.push(`Suggested filename: ${suggested}`);
    }
  }

  // Overall validity
  results.valid = results.issues.length === 0;

  return results;
}

/**
 * Format output for console
 */
function formatOutput(results) {
  const lines = [];

  lines.push("\n" + "=".repeat(60));
  lines.push(`ASSET VALIDATION: ${results.filename}`);
  lines.push("=".repeat(60));

  lines.push(`\nStatus: ${results.valid ? "PASS" : "FAIL"}`);
  lines.push(`Path: ${results.path}`);

  if (results.issues.length > 0) {
    lines.push("\nISSUES:");
    results.issues.forEach((issue) => lines.push(`  - ${issue}`));
  }

  if (results.warnings.length > 0) {
    lines.push("\nWARNINGS:");
    results.warnings.forEach((warning) => lines.push(`  - ${warning}`));
  }

  if (results.suggestions.length > 0) {
    lines.push("\nSUGGESTIONS:");
    results.suggestions.forEach((suggestion) =>
      lines.push(`  - ${suggestion}`)
    );
  }

  // File size info
  if (results.checks.fileSize?.size) {
    lines.push(`\nFile Size: ${formatBytes(results.checks.fileSize.size)}`);
  }

  lines.push("\n" + "=".repeat(60));

  return lines.join("\n");
}

/**
 * Main
 */
function main() {
  const args = process.argv.slice(2);
  const jsonOutput = args.includes("--json");
  const assetPath = args.find((a) => !a.startsWith("--"));

  if (!assetPath) {
    console.error("Usage: node validate-asset.cjs <asset-path> [--json]");
    console.error("\nExamples:");
    console.error(
      "  node validate-asset.cjs assets/banners/social-media/banner_launch_hero_20251209.png"
    );
    console.error(
      "  node validate-asset.cjs assets/logos/icon-only/logo-icon.svg --json"
    );
    process.exit(1);
  }

  // Resolve path
  const resolvedPath = path.isAbsolute(assetPath)
    ? assetPath
    : path.join(process.cwd(), assetPath);

  // Validate
  const results = validateAsset(resolvedPath);

  // Output
  if (jsonOutput) {
    console.log(JSON.stringify(results, null, 2));
  } else {
    console.log(formatOutput(results));
  }

  // Exit with appropriate code
  process.exit(results.valid ? 0 : 1);
}

main();
````



---

## `templates/brand-guidelines-starter.md`

# Brand Guidelines v1.0

> Last updated: {DATE}
> Status: Draft

## Quick Reference

| Element | Value |
|---------|-------|
| Primary Color | #2563EB |
| Secondary Color | #8B5CF6 |
| Primary Font | Inter |
| Voice | Professional, Helpful, Clear |

---

## 1. Color Palette

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Primary Blue | #2563EB | rgb(37,99,235) | CTAs, headers, links |
| Primary Dark | #1D4ED8 | rgb(29,78,216) | Hover states, emphasis |

### Secondary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Secondary Purple | #8B5CF6 | rgb(139,92,246) | Accents, highlights |
| Accent Green | #10B981 | rgb(16,185,129) | Success, positive states |

### Neutral Palette

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Background | #FFFFFF | rgb(255,255,255) | Page backgrounds |
| Surface | #F9FAFB | rgb(249,250,251) | Cards, sections |
| Text Primary | #111827 | rgb(17,24,39) | Headings, body text |
| Text Secondary | #6B7280 | rgb(107,114,128) | Captions, muted text |
| Border | #E5E7EB | rgb(229,231,235) | Dividers, borders |

### Semantic Colors

| State | Hex | Usage |
|-------|-----|-------|
| Success | #22C55E | Positive actions, confirmations |
| Warning | #F59E0B | Cautions, pending states |
| Error | #EF4444 | Errors, destructive actions |
| Info | #3B82F6 | Informational messages |

### Accessibility

- Text on white background: 7.2:1 contrast ratio (AAA)
- Primary on white: 4.6:1 contrast ratio (AA)
- All interactive elements meet WCAG 2.1 AA standards

---

## 2. Typography

### Font Stack

```css
--font-heading: 'Inter', system-ui, -apple-system, sans-serif;
--font-body: 'Inter', system-ui, -apple-system, sans-serif;
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### Type Scale

| Element | Size (Desktop) | Size (Mobile) | Weight | Line Height |
|---------|----------------|---------------|--------|-------------|
| H1 | 48px | 32px | 700 | 1.2 |
| H2 | 36px | 28px | 600 | 1.25 |
| H3 | 28px | 24px | 600 | 1.3 |
| H4 | 24px | 20px | 600 | 1.35 |
| Body | 16px | 16px | 400 | 1.5 |
| Body Large | 18px | 18px | 400 | 1.6 |
| Small | 14px | 14px | 400 | 1.5 |
| Caption | 12px | 12px | 400 | 1.4 |

### Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

---

## 3. Logo Usage

### Variants

| Variant | File | Use Case |
|---------|------|----------|
| Full Horizontal | logo-full-horizontal.svg | Headers, documents |
| Stacked | logo-stacked.svg | Square spaces |
| Icon Only | logo-icon.svg | Favicons, small spaces |
| Monochrome | logo-mono.svg | Limited color contexts |

### Clear Space

Minimum clear space = height of the logo icon (mark)

### Minimum Size

| Context | Minimum Width |
|---------|---------------|
| Digital - Full Logo | 120px |
| Digital - Icon | 24px |
| Print - Full Logo | 35mm |
| Print - Icon | 10mm |

### Don'ts

- Don't rotate or skew the logo
- Don't change colors outside approved palette
- Don't add shadows or effects
- Don't crop or modify proportions
- Don't place on busy backgrounds without sufficient contrast

---

## 4. Voice & Tone

### Brand Personality

| Trait | Description |
|-------|-------------|
| **Professional** | Expert knowledge, authoritative yet approachable |
| **Helpful** | Solution-focused, actionable guidance |
| **Clear** | Direct communication, jargon-free |
| **Confident** | Assured without being arrogant |

### Voice Chart

| Trait | We Are | We Are Not |
|-------|--------|------------|
| Professional | Expert, knowledgeable | Stuffy, corporate |
| Helpful | Supportive, empowering | Patronizing |
| Clear | Direct, concise | Vague, wordy |
| Confident | Assured, trustworthy | Arrogant, overselling |

### Tone by Context

| Context | Tone | Example |
|---------|------|---------|
| Marketing | Engaging, benefit-focused | "Create campaigns that convert." |
| Documentation | Clear, instructional | "Run the command to start." |
| Error messages | Calm, solution-focused | "Try refreshing the page." |
| Success | Brief, celebratory | "Campaign published!" |

### Prohibited Terms

| Avoid | Reason |
|-------|--------|
| Revolutionary | Overused |
| Best-in-class | Vague claim |
| Seamless | Overused |
| Synergy | Corporate jargon |
| Leverage | Use "use" instead |

---

## 5. Imagery Guidelines

### Photography Style

- **Lighting:** Natural, soft lighting preferred
- **Subjects:** Real people, authentic scenarios
- **Color treatment:** Maintain brand colors in post
- **Composition:** Clean, focused subjects

### Illustrations

- Style: Modern, flat design with subtle gradients
- Colors: Brand palette only
- Line weight: 2px consistent stroke
- Corners: 4px rounded

### Icons

- Style: Outlined, 24px base grid
- Stroke: 1.5px consistent
- Corner radius: 2px
- Fill: None (outline only)

---

## 6. Design Components

### Buttons

| Type | Background | Text | Border Radius |
|------|------------|------|---------------|
| Primary | #2563EB | #FFFFFF | 8px |
| Secondary | Transparent | #2563EB | 8px |
| Tertiary | Transparent | #6B7280 | 8px |

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| xs | 4px | Tight spacing |
| sm | 8px | Compact elements |
| md | 16px | Standard spacing |
| lg | 24px | Section spacing |
| xl | 32px | Large gaps |
| 2xl | 48px | Section dividers |

### Border Radius

| Element | Radius |
|---------|--------|
| Buttons | 8px |
| Cards | 12px |
| Inputs | 8px |
| Modals | 16px |
| Pills/Tags | 9999px |

---

## AI Image Generation

### Base Prompt Template

Always prepend to image generation prompts:

```
{DESCRIBE YOUR VISUAL STYLE HERE - mood, colors with hex codes, lighting, atmosphere}
```

### Style Keywords

| Category | Keywords |
|----------|----------|
| **Lighting** | {e.g., soft lighting, dramatic, natural} |
| **Mood** | {e.g., professional, energetic, calm} |
| **Composition** | {e.g., centered, rule of thirds, minimal} |
| **Treatment** | {e.g., high contrast, muted, vibrant} |
| **Aesthetic** | {e.g., modern, vintage, minimalist} |

### Visual Mood Descriptors

- {Mood descriptor 1}
- {Mood descriptor 2}
- {Mood descriptor 3}

### Visual Don'ts

| Avoid | Reason |
|-------|--------|
| {Item to avoid} | {Why to avoid it} |

### Example Prompts

**Hero Banner:**
```
{Example prompt for hero banners}
```

**Social Media Post:**
```
{Example prompt for social graphics}
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | {DATE} | Initial guidelines |
