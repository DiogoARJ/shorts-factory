# taste-skill

Original: https://github.com/Leonxlnx/taste-skill/tree/9b4bf93/skills/taste-skill

Referências citadas como `references/x.md`, `assets/...` ou `scripts/...` estão mais abaixo neste ficheiro, numa secção com esse caminho. Para correr um script, copiar o bloco de código para um ficheiro com esse nome.

Ficheiros não incluídos (binários, imagens ou demos; ver o original no link acima): 638.

*Quando usar:* tasteskill 2.5.0, the anti-slop frontend skill. Builds professional company websites at the level of figma.com and x.ai: plain copy, one system, one section per screen, equal edges, real photographs and real product UI (product renders when there are no photographs), with shader effects, scenes and moments only on tech, gaming and software pages, quiet micro-interactions, and a checker that enforces it in a real browser. Use this whenever you build, design, redesign, restyle, polish or review a landing page, company, product, shop, cafe, hotel, studio, SaaS, AI, developer-tool or game site, in any stack (HTML/CSS, React, Next.js, Vue, Svelte, Astro, Tailwind), or when the user says a page looks generic, templated or "AI-made".


# tasteskill 2.5

Build the website a good company would ship: it says plainly what is sold, shows the real thing on
every screen, and looks made for this client, not from a template and not like an art piece.
figma.com and x.ai are the bar (in words: `layout-v4.md` section 1).

`<skill>` is this folder. It needs Node 22+ and Chrome, Edge or Chromium (ffmpeg optional). Copy `<skill>/assets` into the project's
`assets` and start from `assets/starter.html`.

## House rules

These nine win over everything else in this skill.

1. **No caption or description under any image, render or visual.** Licence credits go in one
   footer line.
2. **Every visual renders, never an empty ground,** at 1440, 1024, 768 and 390.
3. **One section per screen:** the hero alone on the first screen, every section exactly one or
   two screens tall at 1440x900, no second section heading peeking in.
4. **Equal left and right content edges.**
5. **Hover micro-animations:** a linked card lifts 2px, a photo zooms 1.02-1.03 inside its frame,
   buttons step on hover and press on click, underlines draw, card loops cycle in 2.5-4 s, repeat
   and restart on hover. The motion layer does it; never strip or override it. No tilt, carousels
   or timed tabs.
6. **More and better real photographs where they fit;** nicer backgrounds; better heroes, layouts
   and fonts.
7. **Real full-colour icons** (a known product's real icon, never a drawn one); small diagram
   visuals in cards (a hub with branches; one input, a main processor, three parallel lanes;
   pulses running along the lines).
8. **The big award-site scenes and creative moments are part of the skill,** but shader effects
   only where the trade has a technical subject (tech, AI, developer tools, gaming, fintech,
   hardware), never on a local cafe, bakery, guesthouse or shop: those get photographs.
9. **Addresses:** street and district only (no street given: the district), no house number, postcode or coordinates; no register
   or VAT numbers; no phone in a real format; contacts on `.example`.

## 1. The kind of business decides everything

Write the kind on the plan's first line and declare it on the page: the page type on
`<html data-type>` and `<meta name="page-type">` (the same value), and `<meta name="site-kind">`;
a place adds `<meta name="page-kind" content="place">`. The dealers take the last column
(`start.mjs --page`, `moments.mjs --page`), the hero dealer the page type; `consistency.mjs` reads
the metas.

| Brief | page type | site-kind | kind |
|---|---|---|---|
| App, SaaS, AI, developer tool, fintech or banking app, a studio selling its own software | software | software | software |
| A game, a studio launching its game | software | gaming | gaming |
| Hardware or a tech device (a drone, a robot arm, a keyboard) | product | tech | tech |
| Any other physical product or brand (a chair, a bike, coffee beans sold online) | product | other | product |
| People are hired: clinic, law firm, agency, creative studio, trade | service | other | service |
| People come to it: cafe, bar, bakery, restaurant, guesthouse, small hotel, shop, florist, bike shop, gym, local studio | place | other | place |

A maker that also opens its door or teaches (a ceramics studio, a bakery with a web shop) is a
**place**; its web shop becomes the goods section. It is a product only when nothing happens at the door.

"Tech" below means site-kind software, gaming or tech; "other" is everything else. Effects,
scenes, moments, loops, counts, CSS grounds, dark pages and dark heroes are tech only. An other
page is photographs, flat colour, type, real icons and the hover layer.

## 2. The page plan by kind

The full plans, deal lists and section order: `references/sections.md`.

- **Place** (a cafe, bakery, guesthouse, shop). Photographs lead: 12 to 20 on the full page, 8 to
  12 compact, under 8 frames the 3-screen short page, whatever the trade; no client photographs: the draft path
  (`photos.md`), then count. The hero a photograph whenever a frame fits (a remote place: its region's
  landscape), the visit block on screen two, the offer, the place, orders or booking.
  **Variety without effects** (`sections.md` section 4): the offer and the place deal different
  compositions, never two sections round one picture; one type moment (the address or name set large); one main action a screen; list text 16px. Flat grounds, square
  photographs, one button style, the phone bar; no effect, ground, moment, loop, fragment, diagram
  or tab.
- **Product and service** (site-kind other). Photographs lead: the product, the people, the rooms,
  the work, two or more a screen on a product page. Real icons for the tools a studio uses; one
  still diagram at most; flat grounds and one brand band. No shader effect, print, grain, gradient,
  moment, scene or loop; WebGL only for the product render. **A physical product with no
  photographs is shown:** its render (`assets/objects/product-render`, stills) leads the hero,
  then the full product page, never a drawing or mood stock (`sections.md`).
- **Every product page** (photographed or rendered, hardware too; the bar is Figure and 1X;
  `sections.md`, Product): the product **big** where it stands
  whole (most of its frame, or on the ground at anchor scale), never mid-size in a grey rounded
  panel on a grey ground; **a different picture each section**, never one view twice; **every headline promise pictured** (a family bike shows the child bench); dealt
  compositions, no structure twice, one contrasting ground; the **swatch changes the picture**,
  every colour shown once; **no fact twice**; buttons step and press (rule 5).
- **Tech** (software, gaming, hardware). The client's own subject leads at true size. Software: its
  own UI as live HTML showing what it works on (a code-review tool: a red and green diff with its
  Accept action) in one `app-frame`, never a generic dashboard or only fragments on panels; cards:
  fragments on lit panels, pulsing diagrams, real icons. Hardware: its photographs, else its
  render (as above), never a split hero of only an order form or a drawn SVG. A game: its name in
  the h1, a launch line, its world as full-bleed key art (else its render), an effect never in its
  place (`sections.md`, Gaming). **60 to 80 words a screen** outside UI mocks (`copy.md`). By
  deal: **one effect** (a shader ground in the hero or the one `[data-visual]` frame, a WebGL
  part, an object or one big scene) and **one or two moments** in their own sections; four live
  WebGL contexts at most; no card moves with the scroll (`effects-usage.md`).
- **One object never carries the page.** The product or hero object whole leads the hero and **two more sections at
  most**; another kind of visual the brief supports carries the rest (`sections.md` section 1,
  its table): a game's world, crew and map; hardware's use at the bench, an exploded or parts
  view; a still diagram card, a type moment, a context photograph where the trade allows.
- **The client's own assets get slots.** A trailer, key art, screenshots, CAD renders or a motion
  video the brief names each get a frame that reads finished now (a real `<video>` with a kit
  poster, a play control only when there is a page or file to play, three to five world
  captures from the kit, a CAD frame), named in a comment for the client's file, never empty
  (`sections-library.md`, client-slots).

## 3. What serves which page

Open the reference of every asset family the page uses first. A dash means never.

| Need | Asset | Software, gaming | Hardware | Product, service | Place | Reference |
|---|---|---|---|---|---|---|
| Heights, edges, heroes, type | `system.css`, `assets/layout` | dealt hero | dealt hero | dealt hero | place hero | `layout-v4.md` |
| Sections and recipes | `starter.html` | its plan | product plan | its plan | place plan | `sections.md`, `sections-library.md` |
| Tokens, grid, buttons, nav, footer, colour | `system.css`, `system.js` | yes | yes | yes | place tokens | `system.md` |
| Copy, contacts, credits | | yes | yes | yes | yes | `copy.md` |
| Hover, press, focus, nav, tabs | `assets/motion` | yes | yes | yes | yes | `motion.md` |
| Card loops, a count | `assets/motion`, `assets/ui` | yes | yes | - | - | `motion.md`, `cards.md` |
| Photographs | `scripts/photos.mjs` | people, customers; a game's art | lead | lead | lead, 12-20 | `photos.md` |
| Real tool, app and file icons | `scripts/icons.mjs` | yes | yes | tools really used | - | `icons.md` |
| Feature cards, UI fragments | `assets/ui` | lead (gaming: none) | its app | an app the client runs | - | `cards.md` |
| Diagram cards (hub, lanes, pulses) | `assets/diagrams` | 0-2, pulsing | 0-2, pulsing | 0-1, still | - | `diagrams.md` |
| CSS grounds | `assets/backgrounds` | 0-2 dealt | 0-2 dealt | flat tokens | flat tokens | `backgrounds.md` |
| Shader grounds | `assets/effects` | the one effect | the one effect | - | - | `effects-usage.md` |
| Creative parts (`fx-*`) | `assets/components` | yes | yes | `fx-photo` plain, `fx-map` still | `fx-map` still | `effects-creative.md` |
| Objects and prints | `assets/objects` | one, as the effect; a game without art: its render | its render without photographs | its render without photographs | - | `effects-objects.md` |
| Award-site moments | `assets/moments` | 0-2 | 0-2 | - | - | `moments.md` |
| Big scenes | `assets/scenes` | 0-1 | 0-1 | - | - | `scenes.md` |
| Speed and weight | `scripts/perf.mjs` | yes | yes | yes | yes | `perf.md` |

Read `copy.md`, `system.md`, `layout-v4.md` and `sections.md` in full before the first page.

## 4. The run

1. **Read the brief.** Write down the kind (section 1), what is sold, who buys it, the one main
   action (the transaction: Book a room, Order a cake, Start a free trial; a place with neither:
   Get directions) and the real material: logo, screens, photographs, prices, address, hours.

2. **Write all the copy first,** as `copy.md` says: the h1 names the category
   and the buyer or the place (a game: its name and genre), one hard fact on the first screen, a noun in every heading, buttons
   as a verb and an object. Nothing is invented but a coined brand name (searched first, the result
   kept in `names.json` beside the page) and, on a place, plausible hours and prices.

3. **Plan the page as screens.** Line 1: the kind. Line 2: the deal (step 4). Then one line per
   section: its id, its one idea, its picture and its kind (object, use, parts, world, slot, diagram, type; three object lines at most), its
   screens (1 or 2, from its content height, `layout-v4.md` section 2), and on tech which section
   holds the effect, the scene or a moment. Pick the photographs now (`photos.md`); their count,
   stand-ins included, sets a place's length (section 2). Then read `cards.md` and the recipe of
   every id you use in `sections-library.md`.

4. **Deal, never choose by taste.** Each command keeps a history, so pages differ:

   ```bash
   node <skill>/assets/layout/deal.mjs --type <page type> --has <photo,ui,object,film> --history .taste-skill/layout-history.json   # the hero; a game adds --kind gaming, hardware --kind tech
   node <skill>/scripts/start.mjs deal --page <kind> --history .taste-skill/history.json    # three palettes, three pairings; add --axis after a word or editorial hero
   node <skill>/scripts/start.mjs css --page <kind> --palette <id> --type <id> --radius soft --history .taste-skill/history.json
   node <skill>/scripts/start.mjs brand --page place --bg "#.." --ink "#.." --accent "#.." [--surface "#.."] [--muted "#.."] --type <id> --radius soft   # a place: its own colours, in place of css
   node -e "for(const l of process.argv.slice(1)){const o=l.split('|');console.log(o[Math.floor(Math.random()*o.length)])}" <the kind's lists in sections.md>
   ```

   A product, hardware or a game with no photographs or art deals with `--has object`: always the
   `product` hero, its render's widest view across the wrap, no box (a game always passes `--has`). A place's hero is printed, never dealt (`--type
   place`). A dealt part that needs a photograph the page lacks is dealt again (`sections.md` section 2). Take the palette and pairing that suit
   the client (its own colours: `start.mjs brand`, always on a place, with `sections.md` section 4,
   Look); never violet: deal again. Keep the `:root` block as printed. Radius: `sharp` for fintech and developer tools, `soft` by default,
   `round` for consumer apps, square on a place. On tech only: the lit ground (`<html data-ground>`:
   `sand|sky|sage` through the one-liner), the CSS grounds (`backgrounds.md`), the one effect
   (`effects-usage.md`) and the moments (`moments.md`). Write every result on plan line 2 and in
   the comment at the top of `<body>`, and build exactly that (a short page drops what it has no section for: `sections.md` section 4).

5. **Build.** In `starter.html`: set `<html data-type data-radius data-buttons data-motion>` and the
   three metas, the nav class; copy only the `<section class="hero …">` of
   `assets/layout/hero-<id>.html` (never its nav, other sections, footer or credit line; every word
   and picture becomes the client's); move the dealt close and footer out of their `<template>`s
   and delete the rest. Every section is `main > section` with
   one `.wrap`, its h2 first, `--h: 1` or `2`. Build each to its recipe with the system's classes
   and tokens; write page CSS only where a reference says page CSS (inside a visual, `--p-h`,
   `.wall`, `.rail`, `.device`). Paste UI from `assets/ui/<name>/fragment.html` and rewrite every
   name, number and logo to the client's (kit icons become `data-icon`, `cards.md`); a diagram card is `data-diagram="<preset>"`
   with the client's labels; run `icons.mjs scan index.html --out assets/icons --colour` last, so every icon
   the page names is a local file. Mount an effect, object, moment or scene exactly as its
   reference says, never from your own script. Credits: the one footer line from
   `photos.mjs credits`, once the markup uses the photographs (it reads the page).

6. **Check and look.** Only the skill's scripts, each running one headless Chrome with WebGL on the
   CPU, closed by its own PID, one at a time; never a windowed browser or a browser tool.
   Each serves the page file itself over http on 127.0.0.1 (never `file://`), so no server is needed;
   for a built page whose links start at the site root (`/_astro/page.css`), pass `--root` with the build folder (`dist`). Then:

   ```bash
   node <skill>/scripts/consistency.mjs index.html --widths 1440,1024,820,768,390 --rhythm-widths 1440,820,768,390 --profile <dir> --page <kind> --category "<what is sold>" --primary "<main action>"
   node <skill>/assets/layout/check.mjs --url index.html --profile <dir> --sizes 1440x900,1024x768,820x1180,768x1024,390x844 --shots shots/layout
   node <skill>/scripts/shoot.mjs --url index.html --w 1440 --out shots/1440.png --profile <dir>
   node <skill>/scripts/perf.mjs index.html --profile <dir>
   ```

   Shoot 1024, 820x1180, 768x1024 and 390 as well. Every `check.mjs` finding fails the page (no `--no-stress`).
   Fix every FAIL (one you judge false goes in the report with its reason), shoot again, and read
   every screenshot against the checklist.

7. **Report:** the kind, the deal (palette, pairing, hero, grounds, effect, moments, scene); the
   checker, layout and perf results; what you could not check; every assumed price, hour or
   address and the coined name's search; the photographs and art the client must supply, every
   stand-in frame among them; every client slot, its file and its stand-in.

## 5. Checklist

Each line names its checks: `consistency.mjs` ids in brackets, `check.mjs` findings in braces,
`perf.mjs` rows. The last line is for your eyes.

- **First screen:** says what is sold, for whom or where, with one hard fact [copy-headline,
  copy-fact]; the hero fills it alone at every width, its main button inside it [hero-screen,
  hero-fill, fold-action, fold-cut] {hero-fold}.
- **One section per screen:** every section 1 or 2 screens, its h2 first and top-aligned, no
  neighbour's heading or picture in its tile, nothing sparse [section-height, one-section,
  one-heading, section-air, one-screen, section-gaps] {screen-short, screen-height, sparse,
  neighbour, neighbour-ground}.
- **Equal edges:** every block on the `.wrap` lines or the grid's columns, nothing out to one side,
  no sideways scroll [container-edges, row-lines, split-pair, off-grid, right-edge, col-edge,
  spill, off-viewport, stagger, top-stagger] {edge-left, edge-right, spill, bleed-one-side,
  one-sided, lines}.
- **Every visual draws** at 1440, 1024, 768 and 390; a refused effect shows its still fallback
  [visual-empty, empty-visual, gl-fallback, shader-lint, no-visual, photo-weight].
- **No caption** explains, apologises for or labels a picture; credits in one footer line
  [visual-caption, caption, credit-wall, photo-credit]; no placeholder, sample note or printed
  `.example` address [placeholder, sample-label].
- **The right things for the kind:** no effect ground, print, scene or moment outside tech
  (WebGL only for a product render) [effect-kind, effects-fit, photo-print]; the subject itself
  shows: the product big, whole in three sections at most, a new picture each [product-shown,
  same-object, photo-repeat]; each asset the brief names in its slot; a game's name and its world as key art,
  the diff of a code-review tool, software's `app-frame`;
  real photographs where they fit, none twice [photo-set, photo-repeat, photo-upscale]; real icons in their own
  colours; flat grounds on other [grounds]; a place deals two different compositions and one type
  moment.
- **Motion:** every button, link, linked card and linked photograph visibly answers the pointer,
  nothing tilts [motion-layer, hover, hover-move, tilt]; card loops cycle in 2.5-4 s [loop-cycle]; nothing moves because the page scrolled except a dealt moment or the big
  scene inside its own section on tech [scroll-linked, scroll-reveal, pinned: expected only there]; anything
  moving past 5 s has a pause button [loop-pause]; under reduced motion everything rests and nothing
  stays hidden [reduced-motion, hidden-content]; at most four live contexts [webgl].
- **Contacts** as rule 9 [street-number, postcode, coordinates, company-number, phone-number].
- **One system:** one button pair, one card style, one radius scale, one link look [button-styles,
  button-shape, card-family, card-layout, link-styles]; two boxes deep at most [nesting]; one
  heading scale, its faces loaded [heading-scale, font-load]; text contrast [text-contrast,
  contrast].
- **Copy and links:** headings name things, buttons a verb and an object, at most two hero actions
  [copy-headings, copy-buttons, copy-actions, action-count]; one fact, one wording [fact-agree];
  every link lands, forms send [links, forms].
- **Fast:** no FAIL row in `perf.mjs` (image weight, contexts, layout shift).
- **820, 768 and 390:** sections on their screens [section-height], the first screen ending whole
  or on a clear bleed [fold-card] (`layout-v4.md`); splits stack text first, no row half empty; one column at 390, buttons full
  width, a full-screen menu; the place action bar.
- **Your eyes:** beside the figma.com and x.ai frames it reads as a professional company site;
  nothing tilted, staggered, cut or overlapping; the hero is the work, not a mood.

## 6. Never

- A card, row or tile that animates on scroll; a reveal, fade-in or parallax; random blinking.
- Stock photographs passed off as the client's product, people or place; a product page that
  never shows the product.
- A drawn look-alike of a real logo; invented reviews, quotes, customers or figures.
- Violet or lavender in the page's own design: accent, ground, gradient, effect colour or tint (a
  real third-party logo keeps its own colours, `icons.md`).
- Copying a reference site's code, copy, pictures or signature effect.
- Deleting or editing the kit's own files (`assets/`, `scripts/`) to clear a check: a check that
  flags a kit file is reported, and the page is checked again after any change.

## References

All in `references/`; section 3 names the one each asset needs.



---

## `assets/starter.html`

````html
<!doctype html>
<!-- data-type: the page's type, plan line 1 (SKILL.md section 1): software, product, place or service,
     the same value as <meta name="page-type">.
     data-radius: sharp, soft or round. data-ground: the lit ground behind UI (sand, sky, sage, or
     painting with painterly-landscape). data-buttons: the dealt button look (sections.md, section 2):
     solid, pill, tonal, arrow or block; the button markup stays the same. data-motion: the
     micro-interactions of assets/motion (references/motion.md); keep it. -->
<html lang="en" data-type="[software]" data-radius="soft" data-ground="sand" data-buttons="solid" data-motion>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>[Name]: [what it is] for [who or where]</title>
<meta name="description" content="[One sentence: what it is, for whom or where, the main benefit.]">
<!-- the kind decides every effect and motion allowance (SKILL.md section 1: data-type and page-type
     carry the page type, site-kind the kind). software: an app, SaaS, AI, developer tool or fintech
     (type software, site-kind software); a game (type software, site-kind gaming); hardware or a
     tech device (type product, site-kind tech). Every other product or brand (type product), a
     service firm or studio (type service) and a place (type place) are site-kind other:
     photographs, type and flat colour, nothing moving by itself. A place adds
     <meta name="page-kind" content="place">. -->
<meta name="site-kind" content="[software]">
<meta name="page-type" content="[software]">
<!-- Replace the next line and the :root block with the block from: node <skill>/scripts/start.mjs css ...
     (Google Fonts links, system.css and the :root palette). Keep the order: system.css, ui/cards.css,
     motion/motion.css, backgrounds/backgrounds.css, layout/layout.css, icons/icon.css (the .ic-tile
     and .ic-ink rules: a black mark such as GitHub or Apple needs them on a dark ground). -->
<link rel="stylesheet" href="assets/system.css">
<link rel="stylesheet" href="assets/ui/cards.css">
<link rel="stylesheet" href="assets/motion/motion.css">
<link rel="stylesheet" href="assets/backgrounds/backgrounds.css">
<link rel="stylesheet" href="assets/layout/layout.css">
<link rel="stylesheet" href="assets/icons/icon.css">
<style>:root { /* --p-* palette, --font-* and --display-* exactly as start.mjs prints them (it alone deals the type) */ }</style>
<!-- the UI fragments' own CSS, linked here so a fragment is drawn with scripts off or before they run (ui.js only
     adds what is missing: it skips a stylesheet that is already linked). One line per fragment the page uses
     (assets/ui/<name>/fragment.css); delete the line when the page uses none. -->
<link rel="stylesheet" href="assets/ui/base.css">
<link rel="stylesheet" href="assets/ui/[name]/fragment.css">
<!-- a diagram card (assets/diagrams, references/diagrams.md): its stylesheet here and mount.js after the
     other scripts; delete both lines when the page has no diagram -->
<link rel="stylesheet" href="assets/diagrams/diagram.css">
<!-- the grounds' page tokens before the first paint (assets/backgrounds; plain, not deferred) -->
<script src="assets/backgrounds/backgrounds.js"></script>
<!-- moments (only when moments.mjs dealt one; else delete these lines): the guard, then one preload
     for the core, its lib and each dealt moment (assets/moments/<id>/moment.js). system.js mounts them.
<script>document.documentElement.classList.add('mo-js');setTimeout(()=>document.documentElement.classList.add('mo-safe'),2500)</script>
<link rel="modulepreload" href="assets/moments/moments.js">
<link rel="modulepreload" href="assets/moments/lib.js">
<link rel="modulepreload" href="assets/moments/[dealt id]/moment.js">
-->
<!-- page CSS: only what sits inside a visual and the kit lacks, and one --p-h per card group -->
<style>
  #features .panel { --p-h: 300px; }
</style>
</head>
<!-- grounds (tech only; assets/backgrounds/pick.mjs deals 0 to 2 section grounds, never a page ground):
     a section ground is one class on its <section>; bg-topglow goes on a wrapper round the nav and the
     hero only when the deal lists it. On kind other (product, service, place: cafes, shops, studios) no
     ground class at all, and no data-ground on <html>: flat colour and photographs. -->
<body>
<!-- type: [software | product | place | service]
     deal: hero [..], nav [..], close [..], footer [..], rhythm [..], buttons [..], mark [..], grounds [..]
     moments: [dealt ids and their sections]
     The page is a stack of screens (layout-v4.md): the hero alone on the first, every other section
     and the footer exactly one or two (style="--h: 2" or class="g2"), its h2 first. Plan the content
     of each before building: one screen holds 708px of content at 1440x900.
     Every [bracket] in this file is replaced before the page ships: system.js outlines any left in red.
     One page: every link goes to an #id on it (a section's id, #contact, #top for the logo); Privacy,
     Terms and Imprint go to small pages you write (privacy.html ...) or are deleted (sections.md). -->

<!-- NAV (references/sections-library.md): one fixed, opaque bar on the page's .wrap. The dealt type is
     a class: nav-mega and nav-cards "nav", nav-centre "nav nav--centre", nav-split "nav nav--split";
     add nav--tone for the bar on the page's inverse ground. At least one word opens a full-width
     panel on hover and goes to its section on click; on a phone system.js turns the bar into a sheet.
     aria-current="page" marks the word of the page you are on, on an inner page only (pricing.html);
     a one-page site leaves it off every word.
     The logo: the client's own SVG; without one, the dealt mark and the name in the display face:
     arc, ring, stack, dots: <span class="mark" data-mark="arc" aria-hidden="true"></span>
     initial: <span class="mark mark--initial" aria-hidden="true">K</span> (the name's first letter)
     wordmark: no mark, the name alone. The footer repeats it. -->
<header class="nav">
  <div class="wrap nav__bar">
    <a class="nav__logo" href="#top"><span class="mark" data-mark="[dealt mark]" aria-hidden="true"></span>[Name]</a>
    <nav class="nav__links" aria-label="Main">
      <div class="nav__item">
        <a class="nav__link" href="#[section id]">[Word] <svg class="chev" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <div class="nav__menu">
          <div class="wrap grid">
            <!-- nav-mega: two or three link columns and one menu card. nav-cards and nav-split: three or
                 four a.menu-card.span-4 (or .span-3), each a .panel holding the client's photograph
                 (<img class="frame__img">) or one fragment at its corner, over a title and one line. -->
            <div class="menu-col span-3">
              <p class="t-label">[Group]</p>
              <a href="#[section id]">[Item]<span>[What it does, five words]</span></a>
              <a href="#[section id]">[Item]<span>[What it does, five words]</span></a>
              <a href="#[section id]">[Item]<span>[What it does, five words]</span></a>
            </div>
            <div class="menu-col span-3">
              <p class="t-label">[Group]</p>
              <a href="#[section id]">[Item]<span>[What it does, five words]</span></a>
              <a href="#[section id]">[Item]<span>[What it does, five words]</span></a>
            </div>
            <a class="menu-card span-3 start-10" href="#[section id]">
              <div class="panel"><img class="frame__img" src="[photo or screen]" alt="[what it shows]"></div>
              <span class="t-card">[What is new]</span>
              <span class="t-small muted">[One line]</span>
            </a>
          </div>
        </div>
      </div>
      <div class="nav__item"><a class="nav__link" href="#[section id]">[Word]</a></div>
      <div class="nav__item"><a class="nav__link" href="#[section id]">[Word]</a></div>
      <div class="nav__item"><a class="nav__link" href="#[section id]">[Word]</a></div>
    </nav>
    <!-- the main action is the one button; a plain word before it only for something the client really
         has (Sign in for an app with accounts, Gift cards it sells), else delete it -->
    <div class="nav__actions">
      <a class="nav__link" href="#[section id]">[Second action the client has]</a>
      <a class="btn btn--primary" href="#[section id]">[Main action]</a>
    </div>
    <button class="nav__toggle" type="button" aria-expanded="false" aria-label="Menu">
      <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
    </button>
  </div>
</header>

<main id="top">
  <!-- HERO: exactly the first screen; the fixed header lies over its top. Paste the dealt hero from
       assets/layout/hero-<id>.html (layout/deal.mjs deals it; heroes.json has its numbers) in place of
       this one, keeping its shape: section.hero > .wrap > .hero-text (+ one docked strip at most).
       A place's hero is never dealt: it is always assets/layout/hero-place.html (Recipe 3, the
       photograph under the header with nothing on it, the words under it on the ground).
       This default is the split: the words on span-6, the client's photograph on span-6 start-7 (the
       page's split pair, the same on every split: 6/6, 5/7 or 7/5), as tall as the hero's content box. The primary button carries the drawn arrow (svg.m-arrow). -->
  <section class="hero hero--split" aria-labelledby="hero-h">
    <div class="wrap">
      <div class="hero-text grid hero-split">
        <div class="hero-copy span-6">
          <!-- optional notice line: one line with a number (changed hours, a delivery cut-off) -->
          <p class="hero-notice">[One line with a number]</p>
          <h1 id="hero-h">[What it is] [for whom or where]</h1>
          <p class="t-lead">[How it works and the main benefit, with one hard fact.]</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="#[section id]">[Main action]<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg></a>
            <a class="btn btn--secondary" href="#[section id]">[Second action]</a>
          </div>
          <!-- three short facts at the foot of the column, on the picture's bottom line (desktop only); on a
               tech page one of them may count up once on load: <dd data-m-count>[1,240]</dd> -->
          <dl class="hero-facts">
            <div><dt>[Label]</dt><dd>[Fact]</dd></div>
            <div><dt>[Label]</dt><dd>[Fact]</dd></div>
            <div><dt>[Label]</dt><dd>[Fact]</dd></div>
          </dl>
        </div>
        <!-- a photograph of the client's work, place or product (its own frame: no caption under it);
             or a window, a phone or an object as the dealt hero says -->
        <div class="hero-visual frame frame--photo span-6 start-7">
          <img class="frame__img" src="[photo]" alt="[what it shows]" fetchpriority="high" data-source="[client | library | shoot]" data-subject="[what it is of]">
        </div>
      </div>
    </div>
  </section>

  <!-- SECTIONS: the type's plan (references/sections.md), each built to its recipe and planned to its
       screens. One example: the 2x2 of feature tiles, two boxes deep (.card--open: the words on the
       page ground, the panel under them), as two screens (.g2): row 1 the h2 and the first two tiles,
       row 2 the next two, starting --padt under the second screen's top. On a phone a section keeps
       its desktop count unless it says otherwise: style="--hm: 2" or class="g2m" when its stacked
       content needs two phone screens (check at 390x844: nothing may run into the next section).
       Each fragment is pasted from
       assets/ui/<name>/fragment.html and rewritten, at its recipe's place; one loop in the group
       (data-ui-loop); the others hold their finished picture and play while the pointer is on them. -->
  <section class="section g2" id="features" aria-labelledby="features-h">
    <div class="wrap">
      <div class="group">
        <div class="section-head">
          <h2 id="features-h">[What it does.] <span class="muted">[One sentence that sums up the four.]</span></h2>
        </div>
        <div class="grid">
          <article class="card card--row card--open span-6">
            <h3>[Verb + object]</h3>
            <p>[One or two short sentences with one concrete detail.]</p>
            <div class="panel" data-fx="[card effect: a tech page only]" data-fx-seed="21">
              <div class="stage stage--fade-b"><div class="at-rise fit" style="--fit-max:400px;--ax:max(24px, 50% - 200px);--ay:48px;--ay-sm:48px" data-ui-loop>
                <div class="ui ui-panel ui-chat" data-ui="chat">
                  <div class="ui-head"><span class="ui-agent" aria-hidden="true"></span><div class="ui-title">[Name]</div><span class="ui-chat__online">Online</span><span class="ui-spacer"></span></div>
                  <div class="ui-chat__body">
                    <div class="ui-chat__day">[Today, 9:41]</div>
                    <div class="ui-msg ui-msg--me" data-chat-q><span class="ui-msg__text">[A real customer question]</span></div>
                    <div class="ui-msg ui-msg--bot" data-chat-a>
                      <span class="ui-agent ui-msg__av" aria-hidden="true"></span>
                      <span class="ui-msg__col">
                        <span class="ui-chat__typing" aria-hidden="true"><i></i><i></i><i></i></span>
                        <span class="ui-chat__answer">[The answer in two lines, with <b>one real detail</b>.]</span>
                        <span class="ui-chat__srcs"><span class="ui-chat__src"><svg class="ui-icon" viewBox="0 0 16 16"><path d="M4 2.5h5l3 3v8H4z"/><path d="M9 2.5v3h3"/></svg>[Its source]</span></span>
                      </span>
                    </div>
                  </div>
                  <div class="ui-chat__input"><span class="ui-chat__ph">Write a message</span><span class="ui-chat__send" aria-hidden="true"><svg viewBox="0 0 16 16" width="14" height="14"><path d="M8 13V3.5M3.8 7.5 8 3.3l4.2 4.2" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></span></div>
                </div>
              </div></div>
            </div>
          </article>
          <!-- the second tile of row 1: a different fragment (notify, files with real icons, a diagram
               from assets/diagrams) or the client's photograph in the panel (<img class="frame__img">) -->
        </div>
      </div>
      <div class="grid">
        <!-- the third and fourth tiles, built like the first two, the same --p-h, so both rows match -->
      </div>
    </div>
  </section>

  <!-- FAQ: every answer open, always (no accordion): <div class="faq"><div class="faq__item"><h3>[Question]</h3>
       <p>[Answer in one or two sentences.]</p></div> ...</div>, the questions people really ask.
       QUOTE-STAT: a quote with the speaker's face beside one big number, still. One screen; merge it into
       the section above when alone it holds under 495px. A number that counts up (data-m-count,
       motion.js) is a tech page's one count, in its hero only (a fact in .hero-facts), never in a card,
       a panel or a section further down; a count, never a year or a price. -->
  <template data-part="quote-stat">
    <section class="section" id="[section id]" aria-labelledby="[quote id]">
      <div class="wrap">
        <div class="section-head"><h2 id="[quote id]">[Who uses it, plainly]</h2></div>
        <div class="grid fill">
          <figure class="quote span-8">
            <blockquote>[What the customer said, in their words, at most 40 words.]</blockquote>
            <div class="person"><img src="[portrait]" alt="[Full name]" width="40" height="40"><span><span class="person__name">[Full name]</span><span class="person__role">[Role], [Company]</span></span></div>
          </figure>
          <div class="stat-aside span-3 start-10">
            <p class="t-stat">[64%]</p>
            <p class="t-small muted">[What the number counts, over what time]</p>
          </div>
        </div>
      </div>
    </section>
  </template>

  <!-- PEEK-LIST (a place's or a service's moment): rows beside one photograph that changes at once to
       the row under the pointer, the focus or a tap (system.js). Text left, the photograph on the split
       line; every row's words on the left line (the row on show is marked by a dot after its name). -->
  <template data-part="peek-list">
    <section class="section" id="[section id]">
      <div class="wrap">
        <div class="section-head"><h2>[What the rows are: rooms, the house, services]</h2><p>[One line.]</p></div>
        <div class="grid grid--top fill" data-peek>
          <ul class="rows span-6">
            <li data-peek-to="[key 1]" tabindex="0"><span class="rows__name">[Name]</span><p>[One line with one concrete detail.]</p><span class="rows__value">[Price, hours or size]</span></li>
            <li data-peek-to="[key 2]" tabindex="0"><span class="rows__name">[Name]</span><p>[One line with one concrete detail.]</p><span class="rows__value">[Price, hours or size]</span></li>
          </ul>
          <div class="frame frame--photo frame--fill span-6 start-7">
            <img class="frame__img" data-peek-for="[key 1]" src="[photo of row 1]" alt="[what it shows]">
            <img class="frame__img" data-peek-for="[key 2]" src="[photo of row 2]" alt="[what it shows]" hidden>
          </div>
        </div>
      </div>
    </section>
  </template>

  <!-- VISIT (a place, screen 2, directly after the hero; sections.md): system.css's .visit, on the container's lines.
       Open type by default (no box). The full page puts it in a split column beside the client's photograph
       (.visit.visit--card on span-6, the photograph on span-6 start-7: the panel on --g-alt, 1024px and up only).
       The short page adds .visit--cols (address, hours and access as three columns, no rows) and puts the menu
       as .rows under it in the same section. Street and district only; a phone only when the brief gives one;
       at most two rows under the columns. -->
  <template data-part="visit">
    <section class="section" id="visit" data-place="visit" aria-label="Visit">
      <div class="wrap">
        <div class="visit">
          <div class="visit__head"><p class="t-label muted">Visit</p><p class="t-small" data-open-now></p></div>
          <div class="visit__cols">
            <div class="visit__col stack-4">
              <address class="visit__address">[Street]<br>[District]</address>
              <a class="link" href="https://www.openstreetmap.org/search?query=[street%20district%20city]">Get directions</a>
            </div>
            <div class="visit__col">
              <!-- data-tz: the venue's time zone; system.js marks today's row there -->
              <dl class="hours" data-tz="[Europe/Berlin]"><dt>[Mon to Fri]</dt><dd>[8 to 18]</dd><dt>[Sat]</dt><dd>[9 to 16]</dd><dt>Sun</dt><dd>Closed</dd></dl>
            </div>
          </div>
          <ul class="visit__rows">
            <li><span>[Access]</span><span>[Step-free at the front door]</span></li>
          </ul>
        </div>
      </div>
    </section>
  </template>

  <!-- DRAWING: only a dimension figure beside a product's specs (sections-library.md): the real side
       view with its measured spans, one SVG unit a millimetre, the viewBox the product plus 6% all
       round, --ar its width over height; every real part a g.part (lines .ln, a filled part .fill,
       one part .acc in the accent); two or three dimension lines (.dim) whose figures are the
       spans, placed in percent of the figure. Never the picture of a product that has no photograph
       (that is a shot ladder or a short page, sections.md, never a drawing), never hardware drawn as
       an SVG, clip-art or an icon. -->
  <template data-part="drawing">
    <figure class="drawing" style="--ar: [viewBox width / height]" role="img" aria-label="[The product, from the side, its main sizes]">
      <svg viewBox="0 0 [width] [height]" aria-hidden="true">
        <g class="part"><path class="fill" d="[a body or a top]"/></g>
        <g class="part"><path class="ln" d="[a frame, a leg, a strap]"/></g>
        <g class="part"><path class="acc" d="[the one part in the accent]"/></g>
        <g class="dim"><path d="[M x1 y H x2: the line]"/><path d="[the two end ticks]"/></g>
      </svg>
      <span class="drawing__dim" style="left: [x]%; top: [y]%">[1,400 mm]</span>
    </figure>
  </template>
</main>

<!-- FOOTER.CLOSING: the close and the footer in one last screen (system.css). Its .wrap holds exactly
     two children: the dealt close (row 1) and the links (row 2). The ground is dealt too: the page's
     ground (this one), "footer closing footer--dark ground-inverse", or "footer closing
     footer--statement" (the lit ground, full bleed). A place swaps row 2 for links-visit below.
     The close repeats the main action word for word; its h2 is eight words or fewer.
     Links go to the page's sections (#ids) and #contact; Privacy, Terms (and Imprint only when the
     brief gives the details) go to pages you write, never left dead. The legal row ends with the
     credits line when the page shows photographs that are not the client's: one short line naming the
     sources actually used, which opens the list. No address the brief does not give: street and
     district only, never a house number, a postcode, a phone in a real format or a register number. -->
<footer class="footer closing" id="contact" aria-labelledby="close-h">
  <div class="wrap">
    <!-- close--type (this one): the h2 and a line, the big button across the .wrap. Others below. -->
    <div class="closing__cta close--type">
      <div class="section-head">
        <h2 id="close-h">[The main action, plainly]</h2>
        <p>[One line: the trial, the price or the reply time.]</p>
      </div>
      <a class="btn btn--primary btn--xl btn--wide" href="#[section id]">[Main action]<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg></a>
    </div>
    <div class="closing__links">
      <div class="grid">
        <div class="span-4 stack-4">
          <a class="nav__logo" href="#top"><span class="mark" data-mark="[dealt mark]" aria-hidden="true"></span>[Name]</a>
          <p class="footer__lede">[What the company does, in one plain line.]</p>
        </div>
        <div class="span-2 footer__col"><h4>[Nav word]</h4><ul><li><a href="#[section id]">[Link]</a></li><li><a href="#[section id]">[Link]</a></li></ul></div>
        <div class="span-2 footer__col"><h4>[Nav word]</h4><ul><li><a href="#[section id]">[Link]</a></li><li><a href="#[section id]">[Link]</a></li></ul></div>
        <div class="span-2 footer__col"><h4>[Nav word]</h4><ul><li><a href="#[section id]">[Link]</a></li><li><a href="#[section id]">[Link]</a></li></ul></div>
        <div class="span-2 footer__col"><h4>[Nav word]</h4><ul><li><a href="#[section id]">[Link]</a></li><li><a href="#contact">Contact</a></li></ul></div>
      </div>
      <div class="footer__legal">
        <span>&copy; 2026 [Company] &nbsp; <a href="privacy.html">Privacy</a> &nbsp; <a href="terms.html">Terms</a></span>
        <div class="socials"><!-- empty unless the brief gives the client's accounts: node <skill>/scripts/icons.mjs
             get si:x si:instagram --mono --out assets/icons prints one <span class="icon-mono"> per mark;
             put each in <a href=".." aria-label="..">..</a> --></div>
        <a class="credits" href="credits.html">Photographs via [sources used]</a>
      </div>
    </div>
  </div>
</footer>

<template data-part="close-photo">
  <!-- row 1 as close--photo: the head row, then the client's photograph down to the links -->
  <div class="closing__cta close--photo">
    <div class="section-head--split">
      <div><h2 id="close-h">[The main action, plainly]</h2><p class="t-lead">[One line with the price or the hours.]</p></div>
      <a class="btn btn--primary" href="#[section id]">[Main action]<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg></a>
    </div>
    <div class="close__media"><img src="[a second photograph, never the hero's]" alt="[what it shows]" loading="lazy" data-source="[client | library | shoot]" data-subject="[what it is of]"></div>
  </div>
</template>

<template data-part="close-word">
  <!-- row 1 as close--word: the h2 and the button, then the name across the .wrap -->
  <div class="closing__cta close--word">
    <div class="section-head--split">
      <div><h2 id="close-h">[The main action, plainly]</h2><p class="t-lead">[One line: the trial or the reply time.]</p></div>
      <a class="btn btn--primary" href="#[section id]">[Main action]<svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true"><path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg></a>
    </div>
    <p class="close__word" aria-hidden="true">[Name]</p>
  </div>
</template>

<template data-part="links-visit">
  <!-- row 2 on a place (footer closing footer--visit): where it is, set large, with the way there;
       the hours from the split line; one row of the nav's words. Street and district only. -->
  <div class="closing__links">
    <div class="grid">
      <div class="span-6 stack-4">
        <address class="footer__address">[Street], [district]</address>
        <p><a class="link" href="https://www.openstreetmap.org/search?query=[street%20district%20city]">Get directions</a></p>
      </div>
      <div class="span-6 start-7 stack-4">
        <h4>Opening hours</h4>
        <!-- data-tz: the venue's time zone; system.js marks today's row there. Never .is-today by hand. -->
        <dl class="hours" data-tz="[Europe/Berlin]"><dt>[Mon to Fri]</dt><dd>[8 to 18]</dd><dt>[Sat]</dt><dd>[9 to 16]</dd><dt>Sun</dt><dd>Closed</dd></dl>
      </div>
    </div>
    <div class="footer__legal">
      <span>&copy; 2026 [Company] &nbsp; <a href="privacy.html">Privacy</a></span>
      <a class="credits" href="credits.html">Photographs via [sources used]</a>
    </div>
  </div>
</template>

<!-- ACTION BAR (a place: required; other types may use it): fixed at the phone's foot, the main
     action, or Get directions and Book, as the brief allows. Delete it on other pages.
<nav class="actionbar" aria-label="Quick actions">
  <a class="btn btn--primary" href="#[section id]">[Main action]</a>
</nav>
-->

<!-- nav, tabs, highlights, effects, fragments, moments, pause buttons and the guards: system.js;
     hovers, presses, the nav's current word, tabs, focus, counts and card loops: motion.js;
     the heroes' small moments: layout.js. Add no script for these. -->
<script type="module" src="assets/system.js"></script>
<script type="module" src="assets/motion/motion.js"></script>
<script type="module" src="assets/layout/layout.js"></script>
<script type="module" src="assets/diagrams/mount.js"></script>
<!-- a print object (data-print) loads its script after these (assets/objects/_print-core/README.md):
<script type="module" src="assets/objects/_print-core/auto.js"></script>
     a big scene (data-big-scene) loads assets/scenes/scenes.js instead (references/scenes.md) -->
</body>
</html>
````



---

## `assets/system.css`

````css
/*
  taste-skill system.css - the one system for the page. Link it first, then assets/ui/cards.css (the
  feature card, its panel and the fragment placements), then set the palette (--p-*), the fonts and
  the radius set on :root in the page (node scripts/start.mjs prints that block).
  Do not add a second grid, spacing scale, type scale, radius scale, button or card style.
*/

/* ---------------------------------------------------------------- tokens */
:root {
  /* palette (hex only; fx.js reads --bg --surface --ink --muted --accent --accent-ink) */
  --p-bg: #ffffff;
  --p-surface: #f4f4f4;
  --p-ink: #111111;
  --p-muted: #6b6b6b;
  --p-accent: #1a4be0;
  --p-accent-ink: #ffffff;
  --p-action: #1a4be0;      /* buttons, links, focus: the accent, or the ink when the accent is too pale */
  --p-action-ink: #ffffff;
  --p-inv-bg: #111111;
  --p-inv-surface: #1c1c1c;
  --p-inv-ink: #f4f4f4;
  --p-inv-muted: #a3a3a3;
  --p-inv-accent: #ffffff;
  --p-inv-accent-ink: #111111;
  --p-inv-action: #ffffff;
  --p-inv-action-ink: #111111;
  /* the lit ground behind UI and in the closing band (references/cards.md), one per page, tech pages only
     (none on kind other, which is flat): <html data-ground="sand|sky|sage|painting">. system.js gives it to every ground
     that holds UI, on light and dark pages alike; --hue on one panel changes only its accent */
  --ground-bg: #d9ccb7; --ground-surface: #e9e0d2; --ground-ink: #2a2622; --ground-muted: #5a534a; --ground-accent: #a8794a;

  /* fonts */
  --font-display: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-text: system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  --display-weight: 400;    /* headlines 400; 500 on a tech page (software, gaming, hardware) */
  --display-tracking: -0.025em;

  /* the page rhythm (references/layout-v4.md): one section per screen. The header is fixed and
     --nav tall; every section is padded --padt above and --padb (plus the phone action bar, --bar)
     below, and is exactly one or two screens tall (--h: 1 or 2; --hm on a phone). The hero's words
     start --hgap under the header and its content ends --hpadb above the fold. */
  --nav: 72px;
  --padt: 120px;
  --padb: 72px;
  --hgap: 48px;
  --hpadb: 64px;
  --bar: 0px;
  /* grid: one .wrap (alias .container) for the header, every section and the footer, the same
     --gut on both sides: 1280 wide at x 80-1360 at 1440, 342 at x 24-366 at 390 */
  --container: 1280px;
  --gut: 80px;
  --pad: var(--gut);
  --gutter: 24px;

  /* spacing: 4/8 scale */
  --s-1: 4px;  --s-2: 8px;  --s-3: 12px; --s-4: 16px; --s-5: 24px;
  --s-6: 32px; --s-7: 48px; --s-8: 64px; --s-9: 96px; --s-10: 128px;
  --section: 40px;      /* only a .section outside main (the kit's demo pages); every main > section and
                           footer.closing take --padt and --padb */
  --section-band: 56px; /* the same for an older footer outside footer.closing */
  --head-gap: 48px;     /* the one heading-to-content gap, 32 on a phone (layout.css reads it as --ly-head-gap) */
  --card-pad: 16px;     /* card padding (cards.css sets its own for cards with a panel) */
  --card-gap: 16px;     /* gap between cards */

  /* type scale (the only sizes on the page) */
  --t-label: 13px;
  --t-small: 14px;
  --t-body: 16px;
  --t-lead: 18px;
  --t-card: 18px;
  --t-h3: 24px;
  /* straight lines from the phone size at 390 to the desktop size at 1440 (system.md's table) */
  --t-h2: clamp(30px, 1.72vw + 23.3px, 48px);
  --t-h1: clamp(38px, 3.24vw + 25.4px, 72px);
  /* a big number stays a step under the h2 (VI-11): 38 at 1440, 28 at 390, so it never reads as a
     section heading; a stats row and a price set their own, smaller still */
  --t-stat: clamp(28px, .952vw + 24.29px, 38px);

  /* radius: one scale (soft by default; data-radius on <html> switches it) */
  --r-sm: 8px;  --r-md: 12px; --r-lg: 20px; --r-btn: 8px;

  /* controls (fixed here; a page never adds its own) */
  --btn-h: 44px;
  --btn-h-sm: 36px;
  --nav-h: var(--nav);  /* the older name, kept for the kit's files */
  --icon: 16px;         /* small icons: socials, menu chevrons, mono brand marks */

  /* motion */
  --ease: cubic-bezier(.2, .7, .2, 1);
  --dur: 180ms;
}
html[data-radius="sharp"] { --r-sm: 4px; --r-md: 6px;  --r-lg: 8px;  --r-btn: 4px; }
html[data-radius="soft"]  { --r-sm: 8px; --r-md: 12px; --r-lg: 20px; --r-btn: 8px; }
html[data-radius="round"] { --r-sm: 10px; --r-md: 16px; --r-lg: 24px; --r-btn: 999px; }
/* the four lit grounds (references/cards.md); sand is the default above. painting goes with
   painterly-landscape (x.ai's daylight sky over olive hills) */
html[data-ground="sky"]      { --ground-bg: #c6d3df; --ground-surface: #d6e0e9; --ground-ink: #25303a; --ground-muted: #4d5964; --ground-accent: #3f6a92; }
html[data-ground="sage"]     { --ground-bg: #cdd6c6; --ground-surface: #dce3d6; --ground-ink: #262d24; --ground-muted: #535b51; --ground-accent: #6c8e63; }
html[data-ground="painting"] { --ground-bg: #79a8d6; --ground-surface: #a6c4e2; --ground-ink: #16212c; --ground-muted: #273949; --ground-accent: #9c9b3c; }
/* cards.css takes its card and panel radii from this scale */
html[data-radius] .card { --c-r: var(--r-lg); }
html[data-radius] .panel { --p-r: var(--r-md); }

/* a phone: the header 56, the sections padded 96 / 48, the hero's words 40 under the header and its
   content ending 24 above the fold, 24 at both sides, 12 between columns */
@media (max-width: 639px) {
  :root { --nav: 56px; --padt: 96px; --padb: 48px; --hgap: 40px; --hpadb: 24px; --gut: 24px; --gutter: 12px; --card-gap: 12px; --head-gap: 32px; }
}
@media (min-width: 640px) {
  :root { --gut: 48px; --section: 48px; --section-band: 72px; --card-pad: 24px; }
}
@media (min-width: 1024px) {
  :root { --gut: 80px; --section: 56px; --section-band: 96px; --card-gap: 24px;
          --t-lead: 20px; --t-card: 20px; --t-h3: 28px; }
  /* a place (and a local service): the 1200 column at x 120-1320 */
  html[data-type="place"] { --gut: 120px; --container: 1200px; }
}
/* a place (VI-06, ST-96, PH-23): its own smaller type (h1 48/53 and 32/37, h2 32/40 and 24/30, titles
   and the sub-line 20 and 18), the Recipe 3 hero's gap under its photograph (40, 24 on a phone),
   square photographs and cards and 2px buttons, whatever data-radius and data-buttons say */
:root[data-type="place"] {
  --hgap: 40px;
  --t-h1: clamp(32px, 1.524vw + 26.06px, 48px);
  --t-h2: clamp(24px, .762vw + 21px, 32px);
  --t-h3: clamp(20px, .381vw + 18.51px, 24px);
  --r-sm: 2px; --r-md: 0px; --r-lg: 0px; --r-btn: 2px;
}
:root[data-type="place"] :is(h1, .t-h1) { line-height: 1.104; }
:root[data-type="place"] :is(h2, .t-h2) { line-height: 1.25; }
@media (max-width: 639px) {
  :root[data-type="place"] { --hgap: 24px; }
  :root[data-type="place"] :is(h1, .t-h1) { line-height: 1.156; }
}

/* ---------------------------------------------------------------- grounds (at most three) */
:root, .ground-base {
  --bg: var(--p-bg); --surface: var(--p-surface); --ink: var(--p-ink); --muted: var(--p-muted);
  --accent: var(--p-accent); --accent-ink: var(--p-accent-ink); --card: var(--p-surface);
  --action: var(--p-action); --action-ink: var(--p-action-ink);
}
.ground-surface {
  --bg: var(--p-surface); --surface: var(--p-bg); --ink: var(--p-ink); --muted: var(--p-muted);
  --accent: var(--p-accent); --accent-ink: var(--p-accent-ink); --card: var(--p-bg);
  --action: var(--p-action); --action-ink: var(--p-action-ink);
}
.ground-inverse {
  --bg: var(--p-inv-bg); --surface: var(--p-inv-surface); --ink: var(--p-inv-ink); --muted: var(--p-inv-muted);
  --accent: var(--p-inv-accent); --accent-ink: var(--p-inv-accent-ink); --card: var(--p-inv-surface);
  --action: var(--p-inv-action); --action-ink: var(--p-inv-action-ink);
}
:root, .ground-base, .ground-surface, .ground-inverse {
  --line: color-mix(in oklab, var(--ink) 11%, transparent);
  --line-strong: color-mix(in oklab, var(--ink) 20%, transparent);
  /* effects (fx.js) and UI fragments (assets/ui) take the colours of the ground they sit on */
  --fx-bg: var(--bg); --fx-surface: var(--surface); --fx-ink: var(--ink); --fx-muted: var(--muted);
  --fx-accent: var(--accent); --fx-accent-ink: var(--accent-ink);
  --ui-font: var(--font-text); --ui-mono: var(--font-mono); --ui-radius: var(--r-md);
}
.ground-base, .ground-surface, .ground-inverse { background: var(--bg); color: var(--ink); }

/* ---------------------------------------------------------------- base */
*, *::before, *::after { box-sizing: border-box; }
/* an anchor lands on the section's top (the judge's frame): the fixed header covers --nav of its --padt */
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 0; scroll-behavior: auto; margin: 0; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font: 400 var(--t-body)/1.55 var(--font-text);
  -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; overflow-x: clip;
}
img, svg, video, canvas { display: block; max-width: 100%; }
/* hidden means hidden, also on an img the line above makes a block (a menu tab's photograph, a peek photograph) */
[hidden] { display: none !important; }
img, video { height: auto; }
a { color: inherit; text-decoration: none; }
button { font: inherit; color: inherit; }
h1, h2, h3, h4, p, ul, ol, figure, blockquote { margin: 0; }
ul, ol { padding: 0; list-style: none; }
h1, h2, h3, h4 {
  font-family: var(--font-display); font-weight: var(--display-weight);
  letter-spacing: var(--display-tracking); text-wrap: balance; overflow-wrap: break-word;
}
h1, .t-h1 { font-size: var(--t-h1); line-height: 1.04; }
h2, .t-h2 { font-size: var(--t-h2); line-height: 1.1; }
h3, .t-h3 { font-size: var(--t-h3); line-height: 1.2; }
h4, .t-card { font-family: var(--font-text); font-weight: 500; font-size: var(--t-card); line-height: 1.3; letter-spacing: -0.01em; }
p { text-wrap: pretty; }
.t-lead  { font-size: var(--t-lead); line-height: 1.5; }
.t-body  { font-size: var(--t-body); line-height: 1.55; }
.t-small { font-size: var(--t-small); line-height: 1.5; }
.t-label { font-size: var(--t-label); font-weight: 500; line-height: 1.4; letter-spacing: 0.01em; }
.t-stat  { font-family: var(--font-display); font-weight: var(--display-weight); font-size: var(--t-stat);
           line-height: 1; letter-spacing: var(--display-tracking); font-variant-numeric: tabular-nums; }
.muted { color: var(--muted); }
.mono  { font-family: var(--font-mono); }
.measure { max-width: 62ch; }
:focus-visible { outline: 2px solid var(--action); outline-offset: 2px; border-radius: 2px; }
::selection { background: color-mix(in oklab, var(--accent) 30%, transparent); }

/* ---------------------------------------------------------------- grid */
.wrap, .container { width: min(100% - 2 * var(--gut), var(--container)); margin-inline: auto; padding-inline: 0; }
.grid { display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); column-gap: var(--gutter); row-gap: var(--card-gap); }
.grid > * { min-width: 0; grid-column: 1 / -1; }
.section { padding-block: var(--section); }

/* ---------------------------------------------------------------- one section per screen
   The page is a stack of screens. Framed at scrollY = k x the screen height, a shot shows exactly one
   section: the hero alone on the first screen, every other section (and footer.closing, the close and
   the footer in one) exactly one or two screens tall, its h2 first, --padt under its top. Heights
   and padding do it: no pinning, snapping or script.
     <section class="section" id=".." style="--h: 2">     (2 screens; --hm sets a phone's count alone)
       <div class="wrap"> the h2 first, then the content </div>     (the one in-flow child)
     </section>
   A layer (a full-bleed photograph or ground behind the words) is an <img class="layer" aria-hidden="true">
   beside the .wrap. Content must fit: one screen holds 708px of content at 1440x900 (900 - 120 - 72),
   two hold 1,608 (the second screen's part starts --padt under its top with .g2). From 640 to 1279 a
   section keeps at least its screens and grows past them rather than overlap the next. */
main > :is(section, .section), footer.closing {
  position: relative; box-sizing: border-box;
  height: calc(var(--h, 1) * 100vh); height: calc(var(--h, 1) * 100svh);
  padding: var(--padt) 0 calc(var(--padb) + var(--bar));
}
main > :is(section, .section) > :is(.wrap, .container), footer.closing > .wrap { position: relative; z-index: 1; height: 100%; }
main > :is(section, .section) > :is(.wrap, .container):not(.grid) { display: flex; flex-direction: column; }
/* a .wrap that is the section's grid too (class="wrap grid"): its rows start at the top */
main > :is(section, .section) > :is(.wrap, .container).grid { align-content: start; }
/* .fill: the block that takes what the screen leaves under the heading (a photograph, a frame) */
main > :is(section, .section) > .wrap > .fill { flex: 1 1 0; min-height: 0; }
/* two screens as two groups: row 1 the h2 and the first group, row 2 the rest (no second h2), starting
   --padt under the second screen's top, so the second shot looks like any other section */
main > :is(section, .section).g2, footer.closing.g2 { --h: 2; }
main > :is(section, .section).g2 > :is(.wrap, .container), footer.closing.g2 > .wrap { display: grid; grid-template-rows: minmax(0, 1fr) minmax(0, 1fr); row-gap: calc(var(--padt) + var(--padb) + var(--bar)); }
main > :is(section, .section).g2 > :is(.wrap, .container) > *, footer.closing.g2 > .wrap > * { min-height: 0; align-self: start; }
main > :is(section, .section).g2 > :is(.wrap, .container) > :is(.group, .fill) { align-self: stretch; }
/* a group: one screen's part of a .g2 section (its h2 and first rows, or the rest) */
.group { display: flex; flex-direction: column; min-height: 0; }
/* each screen's card row runs down to that screen's foot (the cards stretch, their panels grow), so
   the second screen of a .g2 is never a short row over an empty ground; both rows end on the same line */
@media (min-width: 1024px) {
  main > :is(section, .section).g2 > .wrap > .grid:last-child,
  main > :is(section, .section).g2 > .wrap > .group > .grid:last-child { align-self: stretch; flex: 1 1 auto; min-height: 0; }
}
.group > .fill { flex: 1 1 0; min-height: 0; }
@media (min-width: 640px) and (max-width: 1279px) {
  main > :is(section, .section):not(.hero, .section--hero), footer.closing {
    height: auto; min-height: calc(var(--h, 1) * 100vh); min-height: calc(var(--h, 1) * 100svh);
  }
  /* the section is a column and its .wrap takes all of it, so a .fill (a photograph, a frame) still
     grows to the section's foot (a min-height percentage would not resolve, leaving it at its least) */
  main > :is(section, .section):not(.hero, .section--hero), footer.closing { display: flex; flex-direction: column; }
  main > :is(section, .section):not(.hero, .section--hero) > :is(.wrap, .container), footer.closing > .wrap { flex: 1 0 auto; height: auto; min-height: 0; }
}
/* a phone: lvh (the screen with its bars hidden) for every section but the hero; --hm when stacking
   makes the content taller than the desktop count */
@media (max-width: 639px) {
  main > :is(section, .section):not(.hero, .section--hero), footer.closing {
    height: calc(var(--hm, var(--h, 1)) * 100vh); height: calc(var(--hm, var(--h, 1)) * 100lvh);
  }
  main > :is(section, .section).g2m, footer.closing.g2m { --hm: 2; }
  main > :is(section, .section).g2m > :is(.wrap, .container), footer.closing.g2m > .wrap { display: grid; grid-template-rows: minmax(0, 1fr) minmax(0, 1fr); row-gap: calc(var(--padt) + var(--padb) + var(--bar)); }
  main > :is(section, .section).g2:not(.g2m) > :is(.wrap, .container) { display: flex; row-gap: 0; }
  main > :is(section, .section).g2:not(.g2m) > :is(.wrap, .container) > * { align-self: stretch; }
}
/* a layer: the photograph or ground of a whole section, under its words, edge to edge */
main > :is(section, .section) > :is(img, video, canvas, picture).layer,
footer.closing > :is(img, video, canvas, picture).layer {
  position: absolute; inset: 0; z-index: 0; width: 100%; height: 100%; max-width: none; object-fit: cover; object-position: var(--pos, 50% 50%);
}
main > :is(section, .section) > picture.layer > img { width: 100%; height: 100%; object-fit: cover; }

/* the hero: exactly the first screen, the fixed header over its top. Its words start --hgap under the
   header (--photo adds a full-bleed photograph's height above them on a place); its content ends
   --hpadb above the fold, and nothing of the next section shows, at 1440, 1024, 820 and 390.
     <section class="hero hero--<type>"><div class="wrap"><div class="hero-text"> .. </div>[one strip]</div></section>
   .hero-text holds the whole composition (the words, and the picture or window beside or under them);
   one docked strip (logos, three facts) may follow it, at most 96px, desktop only. */
main > :is(.hero, .section--hero) {
  height: 100vh; height: 100svh; min-height: 0;
  padding: calc(var(--nav) + var(--photo, 0px) + var(--hgap)) 0 calc(var(--hpadb) + var(--bar));
}
:is(.hero, .section--hero) > .wrap { height: 100%; display: grid; grid-template-rows: minmax(0, 1fr) auto; row-gap: var(--s-7); }
:is(.hero, .section--hero) > .wrap > .hero-text { min-height: 0; }
:is(.hero, .section--hero) > .wrap > .hero-strip { grid-row: 2; max-height: 96px; }
@media (max-width: 639px) { :is(.hero, .section--hero) > .wrap > .hero-strip { display: none; } }
.section--hero .section-head { max-width: 860px; }
/* the starter's own hero (hero-split): the words on span-5 top-aligned, the picture on span-6 start-7
   as tall as the hero's content box (at most 716 at 1440x900); a phone stacks words, then the picture
   in what is left */
.hero-text.hero-split { height: 100%; align-items: stretch; }
.hero-split > .hero-copy { align-self: start; }
.hero-split > .hero-visual { position: relative; min-height: 0; height: 100%; }
@media (max-width: 1023px) {
  .hero-text.hero-split { display: flex; flex-direction: column; gap: var(--s-6); }
  .hero-split > .hero-visual { flex: 1 1 0; min-height: 200px; height: auto; }
}
.hero-copy > * + * { margin-top: var(--s-5); }
/* the h1 first in the words' column: its capitals start on the picture's top line, not the line box's
   (the leading above the capitals would put the words about 12px under the photograph's top) */
.hero-copy > h1:first-child { text-box: trim-start cap alphabetic; }
.hero-copy > .btn-row { margin-top: var(--s-6); }
/* three short facts at the foot of the words' column, on the picture's bottom line (no dead space
   under the buttons): <dl class="hero-facts"><div><dt>..</dt><dd>..</dd></div> x3</dl> */
@media (min-width: 1024px) {
  .hero-split > .hero-copy { height: 100%; display: flex; flex-direction: column; }
  .hero-split > .hero-copy > .hero-facts { margin-top: auto; }
}
.hero-facts { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--s-5) var(--gutter); margin: 0; }
.hero-facts > div { display: grid; gap: var(--s-1); align-content: start; }
.hero-facts dt { font-size: var(--t-small); color: var(--muted); }
.hero-facts dd { margin: 0; font-weight: 500; }
@media (max-width: 1023px) { .hero-facts { display: none; } }
/* a notice line above the h1 (changed hours, a delivery cut-off): one line with a number, static,
   starting on the left line like the h1 under it */
.hero-notice { font-size: var(--t-small); font-weight: 500; color: var(--ink); }
.hero-notice b, .hero-notice strong { font-weight: 500; color: var(--accent); }
.hero-copy > .hero-notice + h1 { margin-top: var(--s-5); }

/* a phone: open tiles from a row of three or four (rooms, goods, beans) go two-up, an odd last one
   across the row, so a row of three fits one 844px screen (stacked one under another they need two) */
@media (max-width: 639px) {
  .grid > .tile:is(.span-3, .span-4) { grid-column: auto / span 6; }
  .grid > .tile:is(.span-3, .span-4):nth-child(odd of .tile):nth-last-child(1 of .tile) { grid-column: 1 / -1; }
  .grid > .tile:is(.span-3, .span-4) .tile__head { flex-wrap: wrap; gap: 0 var(--s-2); }
}
/* a phone: open cards (words on the ground, the panel under them) stacked one under another keep 32px
   between a panel's foot and the next card's title, so a title never reads as the panel's caption */
@media (max-width: 639px) { .grid:has(> .card--open) { row-gap: var(--s-6); } }
/* spans: desktop >= 1024. Tablet 640-1023: text cards on span-3 and span-6 go two-up; cards with a
   panel (a visual needs the width; the one exception is a span-6 pair, below)
   and everything else (split text and visuals, span-4 cards, span-5/7/8 blocks) take the full row, so a split stacks and no row is left half empty. Phone < 640: one column. */
@media (min-width: 640px) and (max-width: 1023px) {
  .grid > .card.span-3:not(:has(> .panel)), .grid > .card.span-6:not(:has(> .panel)) { grid-column: auto / span 6; }
  /* the one exception with a panel: a 2x2 (or a pair) of span-6 cards stays two-up from 720px (a panel
     of about 310px and more, wide enough for a kit fragment), so four cards take one or two screens
     at 768-820 instead of a card per row (four stacked panels run past two screens). Split cards and
     every other span keep the full row. Under 720 a card per row. */
  @media (min-width: 720px) {
    .grid > .card.span-6:has(> .panel):not(.card--split) { grid-column: auto / span 6; }
    .grid > .card.span-6:has(> .panel):not(.card--split):nth-child(odd of .card.span-6):nth-last-child(1 of .card.span-6) { grid-column: 1 / -1; }
  }
  /* open tiles (rooms, models, people, a photo pair) go two-up; an odd last one takes the row */
  .grid > .tile:is(.span-3, .span-4, .span-6) { grid-column: auto / span 6; }
  .grid > .tile:is(.span-3, .span-4, .span-6):nth-child(odd of .tile):nth-last-child(1 of .tile) { grid-column: 1 / -1; }
}
@media (min-width: 1024px) {
  .span-2  { grid-column: auto / span 2; }
  .span-3  { grid-column: auto / span 3; }
  .span-4  { grid-column: auto / span 4; }
  .span-5  { grid-column: auto / span 5; }
  .span-6  { grid-column: auto / span 6; }
  .span-7  { grid-column: auto / span 7; }
  .span-8  { grid-column: auto / span 8; }
  .span-9  { grid-column: auto / span 9; }
  .span-10 { grid-column: auto / span 10; }
  .span-12 { grid-column: auto / span 12; }
  .start-1 { grid-column-start: 1; } .start-2 { grid-column-start: 2; } .start-3 { grid-column-start: 3; }
  .start-5 { grid-column-start: 5; } .start-6 { grid-column-start: 6; } .start-7 { grid-column-start: 7; }
  .start-4 { grid-column-start: 4; } .start-8 { grid-column-start: 8; } .start-9 { grid-column-start: 9; }
  .start-10 { grid-column-start: 10; }
  /* a split is top-aligned: the words' first line and the picture's top on one line (never centred
     against each other, never mirrored: text left, the visual right, on every split of the page) */
  .grid--middle, .grid--top { align-items: start; }
}
/* card rows: every card in a row the same height (a plain .grid stretches them) */
.grid:is(.grid--middle, .grid--top) > .card { align-self: stretch; }
/* 1024-1279: a span-4 card's panel would be about 220px wide, too narrow for real UI. Cards with a
   panel on span-4 go two-up, a span-8 one takes the row, and an odd last one takes the row too
   (steps, proof row: two, then one wide; bento: the wide card, then the four small ones two by two) */
@media (min-width: 1024px) and (max-width: 1279px) {
  .grid > .card.span-4:has(> .panel) { grid-column: auto / span 6; }
  .grid > .card.span-8:has(> .panel),
  .grid > .card.span-4:has(> .panel):nth-child(odd of .card.span-4):nth-last-child(1 of .card.span-4) { grid-column: 1 / -1; }
}

/* ---------------------------------------------------------------- section heading */
.section-head { max-width: 760px; margin-bottom: var(--head-gap); display: grid; gap: var(--s-4); }
/* every heading starts on the left line (a centred head among left ones reads as a mistake): the
   old centred head is left-aligned too */
.section-head--center { text-align: left; justify-items: start; }
/* a head row: the h2 (and its line) left, one link or the section's button at the right line */
.section-head--split { max-width: none; display: flex; align-items: end; justify-content: space-between; gap: var(--s-5); flex-wrap: wrap; }
.section-head--split > div { display: grid; gap: var(--s-4); max-width: 760px; }
.section-head p { color: var(--ink); font-size: var(--t-lead); line-height: 1.5; max-width: 60ch; }
.section-head--row { max-width: none; display: flex; align-items: end; justify-content: space-between; gap: var(--s-5); flex-wrap: wrap; }
.section-head--row > div { display: grid; gap: var(--s-4); max-width: 760px; }
/* the hero row (hero-product, hero-cycle): the h1 and its line left, the buttons right, across 1280 */
.section--hero .section-head--row { max-width: none; }

/* ---------------------------------------------------------------- buttons (one pair, a dealt look)
   One pair a page, .btn--primary and .btn--secondary, in the look dealt with the page (sections.md)
   and set once on <html data-buttons>; the markup never changes:
     solid  filled primary, outlined secondary, the radius scale (Figma; the default)
     pill   pills, a chevron after the primary's label, a tinted secondary (x.ai)
     tonal  the radius scale, a tinted secondary with no outline (Linear, Vercel)
     arrow  an arrow after the primary's label; the secondary is a text link with an arrow (Stripe)
     block  near-square corners, 48px tall; the secondary is an underlined text link (shops, hotels) */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--s-2);
  height: var(--btn-h); padding: 0 var(--s-5); border-radius: var(--r-btn); border: 1px solid transparent;
  font: 500 var(--t-body)/1 var(--font-text); letter-spacing: 0; white-space: nowrap; cursor: pointer;
  transition: background-color var(--dur) var(--ease), color var(--dur) var(--ease), border-color var(--dur) var(--ease), text-decoration-color var(--dur) var(--ease);
}
.btn--primary { background: var(--action); color: var(--action-ink); }
.btn--primary:hover { background: color-mix(in oklab, var(--action) 86%, var(--ink)); }
/* an inverted primary (the action is the ground's ink: a brand band, a lit ground): its hover steps toward the ground, as the filled one steps toward the ink */
.ground-brand .btn--primary:hover { background: color-mix(in oklab, var(--action) 88%, var(--bg)); }
/* the ground's own colour with a clear border: never grey on grey, readable on an effect too */
.btn--secondary { background: var(--bg); color: var(--ink); border-color: var(--line-strong); }
.btn--secondary:hover { background: color-mix(in oklab, var(--bg) 94%, var(--ink)); border-color: color-mix(in oklab, var(--ink) 35%, transparent); }
.btn--sm { height: var(--btn-h-sm); padding: 0 var(--s-4); font-size: var(--t-small); }
html[data-buttons="pill"] { --r-btn: 999px; }
html[data-buttons="block"] { --r-btn: 2px; --btn-h: 48px; }
html:is([data-buttons="pill"], [data-buttons="tonal"]) .btn--secondary { background: color-mix(in oklab, var(--ink) 8%, var(--bg)); border-color: transparent; }
html:is([data-buttons="pill"], [data-buttons="tonal"]) .btn--secondary:hover { background: color-mix(in oklab, var(--ink) 14%, var(--bg)); border-color: transparent; }
/* arrow and block: the secondary is a text link at the button's height (no box: one button look) */
html:is([data-buttons="arrow"], [data-buttons="block"]) .btn--secondary {
  background: none; border-color: transparent; padding-inline: var(--s-2);
  text-decoration: underline; text-underline-offset: 4px; text-decoration-color: var(--line-strong);   /* the .link look */
}
html:is([data-buttons="arrow"], [data-buttons="block"]) .btn--secondary:hover { background: none; border-color: transparent; text-decoration-color: currentColor; }
/* the glyph after a label: a chevron (pill) or an arrow (arrow), drawn so every font shows the same */
html[data-buttons="pill"] .btn--primary::after,
html[data-buttons="arrow"] :is(.btn--primary, .btn--secondary)::after {
  content: ""; flex: none; width: 12px; height: 12px; margin-right: -2px; background: currentColor;
  -webkit-mask: var(--btn-glyph) center / contain no-repeat; mask: var(--btn-glyph) center / contain no-repeat;
  transition: transform var(--dur) var(--ease);
}
html[data-buttons="pill"] { --btn-glyph: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M4.5 2.5 8 6l-3.5 3.5' fill='none' stroke='black' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"); }
html[data-buttons="arrow"] { --btn-glyph: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M1.5 6h8.5M6.5 2.5 10 6l-3.5 3.5' fill='none' stroke='black' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"); }
html:is([data-buttons="pill"], [data-buttons="arrow"]) .btn:hover::after { transform: translateX(3px); }
.btn:active { transform: translateY(1px) scale(.985); }
.btn--arrow::after { content: "\2192"; transition: transform var(--dur) var(--ease); }
.btn--arrow:hover::after { transform: translateX(3px); }
/* the drawn arrow (assets/motion: its stem grows and its head moves 3px on hover), the last child of
   a primary button, a pill or a link: <svg class="m-arrow" viewBox="0 0 12 12" aria-hidden="true">
   <path class="m-arrow__stem" d="M1 6h8"/><path class="m-arrow__head" d="M4.5 2.5 8 6l-3.5 3.5"/></svg>.
   It replaces the dealt glyph, so a button never shows two */
.m-arrow { flex: none; width: 12px; height: 12px; margin-right: -2px; overflow: visible;
           fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.btn--xl .m-arrow { width: 0.62em; height: 0.62em; stroke-width: 1.4; }
:is(.btn, .link, .pill):has(> .m-arrow)::after { content: none; display: none; }
.btn-row { display: flex; flex-wrap: wrap; gap: var(--s-3); align-items: center; }
.section-head--center .btn-row { justify-content: center; }
/* on the phone every button row stacks full width */
@media (max-width: 639px) {
  .btn-row { flex-direction: column; align-items: stretch; width: 100%; justify-self: stretch; }
  /* full width, the second action is a text link at the button's height under the filled one (an
     outline across the whole screen reads as a rule, a pale fill as a switched-off button) */
  .btn-row > .btn--secondary { background: none; border-color: transparent; text-decoration: underline; text-underline-offset: 4px; text-decoration-color: var(--line-strong); }
  .section-head--split > .btn { width: 100%; }
}
.link { display: inline-flex; align-items: center; gap: var(--s-2); font-weight: 500; color: var(--ink);
        text-decoration: underline; text-decoration-color: var(--line-strong); text-underline-offset: 4px;
        transition: text-decoration-color var(--dur) var(--ease); }
.link:hover { text-decoration-color: currentColor; }
.link::after { content: "\2192"; display: inline-block; text-decoration: none; transition: transform var(--dur) var(--ease); }
.link:hover::after { transform: translateX(3px); }
.pill { display: inline-flex; align-items: center; gap: var(--s-2); height: 32px; padding: 0 var(--s-3);
        border-radius: 999px; border: 1px solid var(--line); background: var(--card);
        font-size: var(--t-label); color: var(--ink); }
.pill .muted { color: var(--muted); }

/* ---------------------------------------------------------------- card (one style) */
.card {
  display: flex; flex-direction: column; gap: var(--s-2); min-width: 0;
  background: var(--card); border: 1px solid var(--line); border-radius: var(--r-lg); padding: var(--card-pad);
}
/* small titles in the text face: a display face at 20px (a condensed or hairline serif) reads smaller than the body */
.card > h3, .card > h4, .card--plan h3 { font-family: var(--font-text); font-weight: 500; font-size: var(--t-card); line-height: 1.3; letter-spacing: -0.01em; }
/* the type floor (system.md): text people read is 16px or more in ink; cards.css sets it for its
   card text, this for a plain card's lines */
.card > p { color: var(--ink); font-size: var(--t-body); max-width: 52ch; }
/* at most two boxes one inside the other (sections.md): a card whose panel holds UI drops its own
   box, so its title and lines sit on the page ground over the panel (Figma's tiles), or runs the
   panel flush to its sides and bottom (cards.css .panel--flush) */
.card.card--open { --c-pad: 0px; background: none; border: 0; box-shadow: none; padding: 0; overflow: visible; }
.card.card--open > .panel { margin: var(--s-5) 0 0; border-radius: var(--r-lg); }
.card.card--open > .panel--top { margin: 0 0 var(--s-5); }
.card--plan.is-featured { border-color: var(--action); box-shadow: inset 0 0 0 1px var(--action); }
/* cards.css (linked after this file) sets .card { gap: 0 } for feature cards; a plan keeps its 16px rows */
.card.card--plan { gap: var(--s-4); }

/* ---------------------------------------------------------------- visuals: panels and frames
   A card's .panel (the inset visual), .stage and the placements (.at-corner, .at-rise, .at-over,
   .at-right, .at-center, .stage--fade-*) come from assets/ui/cards.css (references/cards.md).
   This file adds the frames (hero, split, square, closing band) and lets a .stage work inside them.
   The grounds' colours: system.js lights every ground that holds UI (see there). */
:not(.card) > .panel { border-radius: var(--p-r, var(--r-md)); }   /* a panel on its own: four round corners */
.menu-card .panel { --p-h: 160px; }
.frame {
  position: relative; isolation: isolate; overflow: clip; display: flex; align-items: center; justify-content: center;
  background: var(--surface); border-radius: var(--r-lg); border: 1px solid var(--line);
  padding: clamp(var(--s-4), 4vw, var(--s-7));
}
/* a zero-width spacer keeps --ratio (height / width) as the frame's minimum height */
.frame::before { content: ""; flex: none; width: 0; padding-top: var(--ratio, 0px); }
/* an object or scene (assets/objects) and a photograph (.frame__img) fill the frame themselves */
.frame > :not(canvas, .stage, .loop-pause, .frame__fx, .frame__img, [data-print], [data-scene], .print3d) { position: relative; max-width: 100%; min-width: 0; }
/* a photograph is a plain rectangle in its frame: no border, no print, no filter */
.frame--photo { padding: 0; border: 0; }
/* .frame--fill: as tall as its row (a split's picture beside the words, down to the section's foot);
   stacked on a tablet or a phone it takes what the screen leaves, at least 200px */
.frame--fill { height: 100%; }
@media (max-width: 1023px) {
  .grid.fill:has(> .frame--fill) { display: flex; flex-direction: column; gap: var(--s-6); }
  .grid.fill > .frame--fill { flex: 1 1 0; height: auto; min-height: 200px; }
}
/* a split's words as a column: the last block (stats, a link) on the picture's bottom line */
.split-col { display: flex; flex-direction: column; gap: var(--s-5); }
@media (min-width: 1024px) { .split-col { height: 100%; } .split-col > .split-col__end { margin-top: auto; } }
:is(.frame, .panel) > .frame__img { position: absolute; inset: 0; z-index: 0; width: 100%; height: 100%; max-width: none; object-fit: cover; }
.frame--portrait { --ratio: 125%; }
/* the product stage (hero-product): wide, the product whole on it; a phone gets a tall stage */
.frame--stage { --ratio: 50%; }
@media (max-width: 639px) { .frame--stage, .frame--portrait { --ratio: 120%; } }
.frame--hero { padding: clamp(24px, 5vw, 64px); }
.frame--split { --ratio: 80%; }
.frame--square { --ratio: 100%; }
/* the closing band: the hero's echo, lit with the page's ground (sand, sky, sage or painting) on light
   and dark pages alike, so its text and buttons take that ground's ink. Its effect sits on a layer of
   its own, <div class="frame__fx" data-fx="..">, held still and calm where the text sits (system.js) */
.frame--cta { min-height: 420px; }
/* .frame--lit: the same for an object's frame that holds a few words in its clear half (the
   product statement's facts in a .frame__text, lower left; the object stands right of centre) */
.frame--cta, .frame--lit {
  border-color: transparent; background: var(--ground-bg); color: var(--ground-ink);
  --bg: var(--ground-surface); --surface: var(--ground-surface); --ink: var(--ground-ink); --muted: var(--ground-muted);
  --action: var(--ground-ink); --action-ink: var(--ground-surface);
  --line: color-mix(in oklab, var(--ground-ink) 12%, transparent); --line-strong: color-mix(in oklab, var(--ground-ink) 24%, transparent);
}
.frame > .frame__fx { position: absolute; inset: 0; z-index: 0; }
/* on a light page the buttons on a lit ground keep the page's own action colour: one action, one look
   (a dark page keeps the lit ground's ink, which reads on the bright ground) */
html:not([data-tone="dark"]) :is(.frame--cta, .frame--lit, .footer--statement) { --action: var(--p-action); --action-ink: var(--p-action-ink); }
/* a card on a photograph (a booking form over the room): the card holds the page's colours */
.frame--photo:has(> .card) { padding: clamp(var(--s-5), 5vw, var(--s-8)) clamp(var(--s-4), 4vw, var(--s-7)); }
.frame--photo > .card { position: relative; z-index: 1; width: min(100%, 480px); }   /* flat: no shadow at rest (ST-97) */
.frame--cta > .frame__fx { opacity: .85; }
.frame--lit > .frame__text { z-index: 2; align-self: flex-end; margin-right: auto; width: min(100%, 360px); display: grid; gap: var(--s-5); }
/* 2:1 on a desktop; a phone gets 2:3, the words at the top and the object smaller and low under
   them (its hero preset), so the facts never touch the object */
.frame--lit { --ratio: 50%; }
@media (max-width: 639px) { .frame--lit { --ratio: 150%; } .frame--lit > .frame__text { align-self: flex-start; } }
@media (max-width: 639px) { .frame--split { --ratio: 100%; } }
/* A hero, wide or split frame (x.ai's hero window): --w on the rising fragment's slot (its true width)
   centres it while it fits; anchored 24px in and cut by the right edge once the frame is narrower.
   --pair on the .stage (the main fragment's width plus the part of the second that sticks out)
   centres the pair; below 1024 the main one alone. In a card's panel cards.css places it (.at-corner,
   .at-rise, .at-right; a centred .at-rise.fit narrows with the panel), as its recipe says. */
.frame > .stage > .at-rise { --ax: max(24px, calc(50% - var(--w, 64%) / 2)); }
.frame--hero > .stage > .at-rise { --ax: max(24px, calc(50% - var(--pair, var(--w, 64%)) / 2)); }
.frame--hero > .stage > .at-over { --bx: max(24px, calc(50% - var(--pair, 800px) / 2)); }
@media (max-width: 1023px) { .frame--hero > .stage > .at-rise { --ax: max(24px, calc(50% - var(--w, 64%) / 2)); } }
/* a frame holding a cards.css .stage: the stage fills it and places the fragments (references/cards.md);
   the hero and wide frames are 16:7 and square on a phone; below 1024 only the main fragment shows */
.frame:has(> .stage) { padding: 0; }
.frame--hero:has(> .stage) { aspect-ratio: 16 / 7; }
@media (max-width: 1023px) {
  .frame--hero:has(> .stage) { aspect-ratio: 3 / 2; }   /* a tablet: room for the main fragment's rows */
}
/* a tablet held upright (820x1180): a taller frame, so the hero fills the screen without a gap */
@media (min-width: 640px) and (max-width: 1023px) and (orientation: portrait) {
  .frame--hero:has(> .stage) { aspect-ratio: 4 / 3; }
}
@media (max-width: 1023px) {
  .frame--hero > .stage > :is(.at-over, .at-over-l) { display: none; }
}
/* a split frame is about 440-560px wide from 1024 to 1279: the main piece alone there */
@media (min-width: 1024px) and (max-width: 1279px) {
  .frame--split > .stage > :is(.at-over, .at-over-l) { display: none; }
}
@media (max-width: 639px) {
  .frame--hero:has(> .stage) { aspect-ratio: 1; }
  .frame > .stage > :is(.at-over, .at-over-l) { display: none; }
  /* phone: cards.css sets a fragment 16px in on both sides, and system.js holds every loop on its
     finished picture, so no pause button lands on the UI */
}
/* a small object on a focal tile (.at-center): its true width (--w, 288px for the slider), narrowed
   on a small panel so 24px of ground always shows on both sides (a span-4 panel is 304px at 1280) */
.stage > .at-center { width: calc(100% - 48px); max-width: var(--w, 288px); }
.stage > .at-center > :is([data-ui], .ui) { width: 100%; max-width: none; }
/* .to-edge stretches a fragment's surface past the bottom (cards.css); doc's surface is its page */
.stage > .to-edge > .ui-doc > .ui-doc__page { min-height: 100%; }
/* .hero-stage: whole fragments side by side in a frame, never overlapping or cut (a row of app
   screens); the first is the main one, and the ones that no longer fit drop out from the end */
.hero-stage { container: hero-stage / inline-size; width: 100%; }
.hero-stage__row { display: flex; align-items: center; justify-content: center; gap: var(--s-5); }
.hero-stage__row > * { flex: none; max-width: 100%; }
@container hero-stage (max-width: 1060px) { .hero-stage__row > :nth-child(n + 3) { display: none; } }
@container hero-stage (max-width: 740px)  { .hero-stage__row > :nth-child(n + 2) { display: none; } }
/* the pause button on every visual that moves by itself for more than 5 s (WCAG 2.2.2): ui.js adds it
   to a loop when it starts to move, system.js to the hero's ground. Write a button.loop-pause into
   the frame only for a loop of your own (hero-cycle). The same solid 32px disc in the page colours as
   assets/ui/base.css's, 12px in from the bottom-right corner, with a 44px hit area. */
.loop-pause {
  position: absolute; right: 12px; bottom: 12px; z-index: 6; display: grid; place-items: center;
  width: 32px; height: 32px; margin: 0; padding: 0; border-radius: 50%; cursor: pointer;
  border: 1px solid color-mix(in oklab, var(--ink) 16%, transparent); background: var(--bg); color: var(--ink);
  box-shadow: 0 1px 2px rgb(0 0 0 / .12), 0 4px 12px -4px rgb(0 0 0 / .28);
}
.loop-pause::before { content: ""; position: absolute; inset: -6px; border-radius: 50%; }
.loop-pause svg { width: 14px; height: 14px; fill: currentColor; }
@media (prefers-reduced-motion: reduce) { .loop-pause { display: none; } }

/* ---------------------------------------------------------------- navigation */
/* The header: fixed, opaque, one hairline under it, the same at every depth (no blur, no shadow, no
   floating pill, never hidden on scroll). Its .wrap is the page's, so the logo starts on the left line
   and the main button ends on the right one. Plain words, 15px, sentence case; one filled button. */
.nav {
  position: fixed; inset: 0 0 auto 0; z-index: 50; height: var(--nav);
  background: var(--bg); color: var(--ink); border-bottom: 1px solid var(--line);
}
.nav__bar { height: 100%; display: flex; align-items: center; gap: var(--s-8); }
/* a text logo: the display face at 500, 22px (the client's SVG logo replaces it when there is one) */
.nav__logo { display: inline-flex; align-items: center; gap: var(--s-2); font: 500 22px/1 var(--font-display); letter-spacing: -0.02em; flex: none; }
@media (max-width: 639px) { .nav__logo { font-size: 20px; } }
.nav__logo svg, .nav__logo img { height: 24px; width: auto; }
/* the brand's mark beside its name, in the accent (the client's logo replaces both). Dealt shapes:
   <span class="mark" data-mark="dots|arc|ring|petal|leaf|stack" aria-hidden="true"></span> */
.mark { display: inline-block; flex: none; width: 22px; height: 22px; background: var(--accent);
        -webkit-mask: var(--mark) center / contain no-repeat; mask: var(--mark) center / contain no-repeat; }
.mark[data-mark="dots"]  { --mark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='6.5' cy='6.5' r='4.5'/%3E%3Ccircle cx='17.5' cy='6.5' r='4.5'/%3E%3Ccircle cx='6.5' cy='17.5' r='4.5'/%3E%3Crect x='13' y='13' width='9' height='9' rx='1.5'/%3E%3C/svg%3E"); }
.mark[data-mark="arc"]   { --mark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M2.5 21.5V12a9.5 9.5 0 0 1 19 0v9.5h-6V12a3.5 3.5 0 0 0-7 0v9.5z'/%3E%3C/svg%3E"); }
.mark[data-mark="ring"]  { --mark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill-rule='evenodd' d='M12 2a10 10 0 1 1 0 20 10 10 0 0 1 0-20zm0 5.5a4.5 4.5 0 1 0 0 9 4.5 4.5 0 0 0 0-9z'/%3E%3C/svg%3E"); }
.mark[data-mark="petal"] { --mark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='12' cy='6.6' r='5'/%3E%3Ccircle cx='17.4' cy='12' r='5'/%3E%3Ccircle cx='12' cy='17.4' r='5'/%3E%3Ccircle cx='6.6' cy='12' r='5'/%3E%3Ccircle cx='12' cy='12' r='4'/%3E%3C/svg%3E"); }
.mark[data-mark="leaf"]  { --mark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M3 21C3 10 10 3 21 3c0 11-7 18-18 18z'/%3E%3C/svg%3E"); }
.mark[data-mark="stack"] { --mark: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='2' y='2.5' width='20' height='5.5' rx='2.75'/%3E%3Crect x='2' y='9.25' width='14' height='5.5' rx='2.75'/%3E%3Crect x='2' y='16' width='8' height='5.5' rx='2.75'/%3E%3C/svg%3E"); }
/* initial: the name's first letter on a small accent tile (<span class="mark mark--initial" aria-hidden="true">K</span>);
   wordmark: no mark, the name alone */
.mark.mark--initial { -webkit-mask: none; mask: none; display: inline-grid; place-items: center; border-radius: calc(var(--r-sm) * 0.75);
  color: var(--accent-ink); font: var(--display-weight, 400) 13px/1 var(--font-display); letter-spacing: 0; }
.footer__mark .mark, .footer .nav__logo .mark { width: 0.8em; height: 0.8em; margin-right: 0.18em; vertical-align: -0.04em; }
.footer__mark .mark--initial, .footer .nav__logo .mark--initial { width: 1em; height: 1em; font-size: 0.6em; }
.nav--split .nav__logo .mark--initial { width: 26px; height: 26px; font-size: 15px; }
.nav__links { display: flex; align-self: stretch; gap: var(--s-1); flex: 1; min-width: 0; }
.nav__item { display: flex; align-items: center; height: 100%; }
.nav__link {
  position: relative; display: inline-flex; align-items: center; gap: var(--s-1); height: 36px; padding: 0 var(--s-3); border-radius: var(--r-sm);
  font-size: 15px; font-weight: 500; color: var(--ink); white-space: nowrap; transition: background-color var(--dur) var(--ease), color var(--dur) var(--ease);
}
/* a small laptop (1024-1279): the words sit closer, so a bar of four words never wraps or reaches the logo */
@media (min-width: 1024px) and (max-width: 1279px) {
  .nav__bar { gap: var(--s-6); }
  .nav__link { padding: 0 var(--s-2); }
  .nav__link::before, .nav__link[aria-current="page"]::after { left: var(--s-2); right: var(--s-2); }
  .nav__links { gap: 0; }
}
/* the words take no pill or fill (ST-08, ST-11): a 2px line draws under the word from the left on hover and focus and leaves to the right */
.nav__link::before { content: ""; position: absolute; left: var(--s-3); right: var(--s-3); bottom: -2px; height: 2px; border-radius: 2px; background: currentColor;
  transform: scaleX(0); transform-origin: right; transition: transform var(--dur) var(--ease); pointer-events: none; }
.nav__link:hover::before, .nav__link:focus-visible::before, .nav__item:hover > .nav__link::before, .nav__item:focus-within > .nav__link::before { transform: scaleX(1); transform-origin: left; }
.nav__actions > .nav__link::before { left: var(--s-2); right: var(--s-2); }
.nav__link .chev { width: 12px; height: 12px; opacity: .6; transition: transform var(--dur) var(--ease); }
/* the page you are on: a 2px bar under its word (still, the same inset as the hover line) */
.nav__link[aria-current="page"]::after { content: ""; position: absolute; left: var(--s-3); right: var(--s-3); bottom: -2px; height: 2px; border-radius: 2px; background: currentColor; }
.nav__expand { display: none; }
.nav__actions { display: flex; align-items: center; gap: var(--s-4); flex: none; }
/* the bar's button: the page's primary at the one button height (44, 48 with data-buttons="block"; ST-09) */
.nav__actions .btn { height: var(--btn-h); padding-inline: var(--s-5); font-size: 15px; }
.nav__actions > .nav__link { padding-inline: var(--s-2); }
.nav__toggle { display: none; }

.nav__menu {
  position: absolute; left: 0; right: 0; top: 100%; background: var(--bg); color: var(--ink);
  border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);
  padding: var(--s-7) 0 var(--s-8); opacity: 0; visibility: hidden; transform: translateY(-6px);
  transition: opacity 120ms var(--ease), transform 120ms var(--ease), visibility 0s linear 120ms;
}
@media (min-width: 1024px) {
  /* hover opens the full-width panel after 150ms of intent; a click on the word goes to its page */
  .nav__item:hover > .nav__menu, .nav__item:focus-within > .nav__menu {
    opacity: 1; visibility: visible; transform: none; transition-duration: 200ms, 200ms, 0s; transition-delay: 150ms, 150ms, 150ms;
  }
  .nav__item:hover > .nav__link .chev, .nav__item:focus-within > .nav__link .chev { transform: rotate(180deg); }
}
.menu-col { display: grid; gap: var(--s-2); align-content: start; }
.menu-col > .t-label { color: var(--muted); margin-bottom: var(--s-2); }
.menu-col a { display: grid; gap: var(--s-1); padding: var(--s-2) 0; font-weight: 500; }
.menu-col a span { font-weight: 400; color: var(--muted); font-size: var(--t-small); }
.menu-col a:hover { color: var(--action); }
.menu-card { display: grid; gap: var(--s-3); }
.menu-card .panel { --ratio: 56.25%; }

@media (max-width: 1023px) {
  .nav__links, .nav__actions { display: none; }
  /* the menu button takes the secondary button's look on a 44px tap area */
  .nav__toggle {
    display: inline-grid; place-items: center; margin-left: auto; width: 44px; height: 44px; border-radius: var(--r-btn);
    border: 1px solid var(--line-strong); background: transparent; color: var(--ink); cursor: pointer; flex: none;
  }
  .nav.is-open .nav__links {
    display: flex; flex-direction: column; position: fixed; top: var(--nav); left: 0; right: 0; bottom: 0;
    padding: var(--s-4) var(--gut) calc(var(--btn-h) * 2 + 56px); background: var(--bg); overflow-y: auto; gap: 0;
  }
  .nav.is-open .nav__item { display: grid; grid-template-columns: 1fr auto; height: auto; border-bottom: 1px solid var(--line); }
  .nav.is-open .nav__link { height: 56px; padding: 0; font-size: 20px; background: none; }
  .nav.is-open .nav__link[aria-current="page"]::after { left: 0; right: auto; width: 24px; bottom: 10px; }
  .nav.is-open .nav__link::before { display: none; }
  .nav.is-open .nav__link .chev { display: none; }
  .nav.is-open .nav__expand {
    display: inline-grid; place-items: center; width: 44px; height: 56px; border: 0; background: none; color: var(--ink); cursor: pointer;
  }
  .nav__expand svg { width: 16px; height: 16px; transition: transform var(--dur) var(--ease); }
  .nav__item.is-expanded .nav__expand svg { transform: rotate(180deg); }
  .nav.is-open .nav__menu {
    position: static; grid-column: 1 / -1; display: none; opacity: 1; visibility: visible; transform: none;
    box-shadow: none; border: 0; padding: 0 0 var(--s-4);
  }
  .nav.is-open .nav__item.is-expanded .nav__menu { display: block; }
  .nav.is-open .nav__menu :is(.container, .wrap) { width: 100%; }
  .nav.is-open .nav__menu .grid { row-gap: var(--s-4); }
  /* menu cards become plain rows in the sheet (their title and line), the picture panel hidden */
  .nav.is-open .menu-card { display: grid; gap: var(--s-1); padding: var(--s-2) 0; }
  .nav.is-open .menu-card .panel { display: none; }
  .nav.is-open .nav__actions {
    display: grid; gap: var(--s-2); position: fixed; left: 0; right: 0; bottom: 0; z-index: 51;
    padding: var(--s-4) var(--gut) calc(var(--s-4) + env(safe-area-inset-bottom)); background: var(--bg); border-top: 1px solid var(--line);
  }
  .nav.is-open .nav__actions .btn { width: 100%; height: 48px; font-size: var(--t-body); }
  /* a text action (Sign in, a phone line) under the buttons, centred at their height */
  .nav.is-open .nav__actions .nav__link { display: inline-flex; order: 2; justify-content: center; height: var(--btn-h); font-size: var(--t-body); }
  body.nav-locked { overflow: hidden; }
}
/* a tablet and a phone (1023 and below, ST-15): the main button stays in the bar, at the right line
   with the menu button 12px after it; the plain words go to the sheet */
@media (max-width: 1023px) {
  .nav__bar { gap: var(--s-3); }
  .nav:not(.is-open) .nav__actions { display: flex; margin-left: auto; }
  .nav:not(.is-open) .nav__actions > :not(.btn--primary) { display: none; }
  .nav:not(.is-open) .nav__actions + .nav__toggle { margin-left: 0; }
}
@media (max-width: 639px) {
  /* a long name (15 characters, "Verdigris Works"), the main button and the menu button fit 342px (390 wide) on
     one line each, with no page CSS: the name steps down with the screen (18px at 390), the button is the small
     size, and the three sit 8px apart. A name of 17 characters or more is the client's to shorten to its mark. */
  .nav__bar { gap: var(--s-2); }
  .nav__logo { font-size: clamp(16px, 4.6vw, 20px); gap: 6px; white-space: nowrap; }
  .nav__logo .mark:not(.mark--initial) { width: 20px; height: 20px; }
  .nav:not(.is-open) .nav__actions .btn { height: 44px; padding-inline: var(--s-3); font-size: var(--t-small); }
}
/* no script: the sheet cannot open, so the words stay in the bar (it scrolls sideways) and the dead menu button goes */
@media (scripting: none) and (max-width: 1023px) {
  .nav__links { display: flex; overflow-x: auto; scrollbar-width: none; margin-right: var(--s-3); padding-right: var(--s-2); border-right: 1px solid var(--line); }   /* stops short of the button, and a hairline marks where the row is cut (it scrolls) */
  .nav__toggle { display: none; }
}

/* nav types (dealt, sections.md). Every one is the same fixed bar on the page's .wrap; the full-width
   hover panel on a desktop and the full-screen sheet on a phone are shared, so only the bar's order
   and its panel's contents differ.
   (default) nav-mega: the logo, the words 64px right of it, the actions at the right line; the panel
              holds two or three link columns and one picture card (Figma)
   nav-cards: the same bar; its panel holds three or four picture cards (a.menu-card, span-4 or span-3)
   .nav--centre: the words in the middle of the bar (Linear, Vercel)
   .nav--split: the words left, the name in the middle, the actions right (shops, hotels, restaurants)
   .nav--tone: the bar on the page's inverse ground, a band of colour over a light page (x.ai's black
              bar); the panel under it stays on the page ground */
@media (min-width: 1024px) {
  .nav--split .nav__bar, .nav--centre .nav__bar { display: grid; grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr); }
  .nav--split .nav__logo { grid-column: 2; grid-row: 1; font-size: 26px; }
  .nav--split .nav__links { grid-column: 1; grid-row: 1; }
  /* the first word starts on the left line (its box, its letters and its underline) */
  .nav--split .nav__links > .nav__item:nth-child(1 of .nav__item) > .nav__link { padding-left: 0; }
  .nav--split .nav__links > .nav__item:nth-child(1 of .nav__item) > .nav__link::before,
  .nav--split .nav__links > .nav__item:nth-child(1 of .nav__item) > .nav__link[aria-current="page"]::after { left: 0; }
  .nav--split .nav__actions, .nav--centre .nav__actions { grid-column: 3; grid-row: 1; justify-self: end; }
  .nav--centre .nav__logo { grid-column: 1; grid-row: 1; justify-self: start; }
  .nav--centre .nav__links { grid-column: 2; grid-row: 1; justify-content: center; flex: none; }
}
.nav--tone { --bg: var(--p-inv-bg); --ink: var(--p-inv-ink); --muted: var(--p-inv-muted); --accent: var(--p-inv-accent); --accent-ink: var(--p-inv-accent-ink);
             --action: var(--p-inv-action); --action-ink: var(--p-inv-action-ink); --card: var(--p-inv-surface);
             --line: color-mix(in oklab, var(--p-inv-ink) 14%, transparent); --line-strong: color-mix(in oklab, var(--p-inv-ink) 26%, transparent); }
.nav--tone .nav__menu { --bg: var(--p-bg); --ink: var(--p-ink); --muted: var(--p-muted); --action: var(--p-action); --line: color-mix(in oklab, var(--p-ink) 11%, transparent); }
/* the older float type is the plain bar now (a floating, frosted pill is not a header) */

/* ---------------------------------------------------------------- logo row */
.logos { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: var(--s-5) var(--s-6); }
.logos > * { height: 28px; width: auto; max-width: 100%; color: var(--ink); }
.logos .wordmark { height: auto; font: 500 var(--t-card)/1 var(--font-display); letter-spacing: -0.02em; white-space: nowrap; }
/* --mono marks in a logo row: 28px tall, each in the same box (the mask keeps its shape) */
.logos .icon-mono { width: 120px; height: 28px; }
/* tablet and phone: a grid, so a wrapped row never leaves one logo on its own */
@media (max-width: 1023px) { .logos { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); justify-items: center; } }
@media (max-width: 639px)  { .logos { grid-template-columns: repeat(2, minmax(0, 1fr)); } }

/* ---------------------------------------------------------------- lists, quote, steps */
.checks { display: grid; gap: var(--s-3); }
.checks li { display: grid; grid-template-columns: 20px 1fr; gap: var(--s-3); align-items: start; }
.checks li::before {
  content: ""; width: 20px; height: 20px; margin-top: 2px; background: var(--action);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cmask id='m'%3E%3Crect width='20' height='20' fill='white'/%3E%3Cpath d='M6 10.2l2.6 2.6L14 7.4' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/mask%3E%3Ccircle cx='10' cy='10' r='10' mask='url(%23m)'/%3E%3C/svg%3E") center / 20px no-repeat;
          mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 20 20'%3E%3Cmask id='m'%3E%3Crect width='20' height='20' fill='white'/%3E%3Cpath d='M6 10.2l2.6 2.6L14 7.4' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/mask%3E%3Ccircle cx='10' cy='10' r='10' mask='url(%23m)'/%3E%3C/svg%3E") center / 20px no-repeat;
}
.quote blockquote { font-family: var(--font-display); font-weight: var(--display-weight); font-size: var(--t-h3);
                    line-height: 1.3; letter-spacing: var(--display-tracking); text-wrap: pretty; }
/* cards.css styles .quote as quote text; who said it stays in the text face */
.quote figcaption, .quote .person { font: 400 var(--t-small)/1.45 var(--font-text); letter-spacing: 0; color: var(--ink); }
.person { display: flex; align-items: center; gap: var(--s-3); }
.person img, .person .avatar { width: 40px; height: 40px; border-radius: 999px; object-fit: cover; background: var(--surface); flex: none; }
.person .avatar { display: grid; place-items: center; font: 500 var(--t-small)/1 var(--font-text); color: var(--muted); }
/* the number beside a quote (quote-stat): below 1024 it sits under the quote, by space alone (ST-43) */
@media (max-width: 1023px) { .stat-aside { margin-top: var(--s-7); } }
/* a stats row: two to four short facts, the number above its label (data-m-count on a count) */
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: var(--s-5) var(--gutter); margin: 0; }
.stats > div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: var(--s-2); }
.stats dd { margin: 0; }
.stats .t-stat { font-size: clamp(26px, 1vw + 22px, 36px); }
@media (max-width: 639px) { .stats .t-stat { font-size: 26px; } }
.step-num { display: inline-grid; place-items: center; width: 32px; height: 32px; border-radius: 999px;
            border: 1px solid var(--line-strong); font: 500 var(--t-small)/1 var(--font-text); font-variant-numeric: tabular-nums; }

/* ---------------------------------------------------------------- tabs */
.tabs { display: flex; flex-wrap: wrap; gap: var(--s-2); }
.tab {
  height: var(--btn-h-sm); padding: 0 var(--s-4); border-radius: var(--r-btn); border: 1px solid var(--line);
  background: transparent; color: var(--muted); font-size: var(--t-small); font-weight: 500; cursor: pointer;
  transition: background-color var(--dur) var(--ease), color var(--dur) var(--ease), border-color var(--dur) var(--ease);
}
.tab:hover { color: var(--ink); border-color: var(--line-strong); }
.tab[aria-selected="true"] { background: var(--ink); color: var(--bg); border-color: var(--ink); }
/* the panel shown at load is there on the first frame (MO-62); system.js fades a chosen one in */
[role="tabpanel"][hidden] { display: none; }

/* ---------------------------------------------------------------- pricing */
.price { display: flex; align-items: baseline; gap: var(--s-2); }
.price .t-stat { font-size: var(--t-stat); }
.card--plan { gap: var(--s-4); }
.card--plan .btn { width: 100%; }
.card--plan .checks { margin-top: var(--s-2); }
.badge { display: inline-flex; align-items: center; height: 24px; padding: 0 var(--s-3); border-radius: 999px; vertical-align: middle;
         background: var(--action); color: var(--action-ink); font: 500 var(--t-label)/1 var(--font-text); letter-spacing: 0; }
.card--plan h3 .badge { margin-left: var(--s-2); }

/* ---------------------------------------------------------------- FAQ
   Every answer is open, always (ST-47, MO-70): no accordion, no +/- marker, nothing changes height.
     <div class="faq"><div class="faq__item"><h3>[Question]</h3><p>[Answer]</p></div> ...</div>
   Older <details> markup shows its answer open too (system.js also sets [open]). */
.faq > :is(.faq__item, details) { display: grid; gap: var(--s-2); padding: var(--s-5) 0; border-bottom: 1px solid var(--line); }   /* each row closes with its rule (ST-43) */
.faq > :is(.faq__item, details):first-child { padding-top: 0; }
.faq :is(.faq__item > h3, summary) { display: block; font: 500 var(--t-lead)/1.4 var(--font-text); letter-spacing: 0; list-style: none; cursor: text; }
.faq summary { pointer-events: none; }
.faq summary::-webkit-details-marker { display: none; }
.faq details::details-content { content-visibility: visible; }
.faq :is(.faq__item, details) p { color: var(--ink); max-width: 64ch; }
@media (max-width: 639px) { .faq > :is(.faq__item, details) { padding: var(--s-4) 0; } }

/* ---------------------------------------------------------------- footer */
.footer { padding-block: var(--section) var(--s-6); border-top: 1px solid var(--line); }   /* an older footer after the last section; footer.closing (below) replaces it */
.footer .grid { row-gap: var(--s-7); }
.footer h4 { font: 500 var(--t-small)/1.4 var(--font-text); letter-spacing: 0; color: var(--muted); margin-bottom: var(--s-4); }
.footer ul { display: grid; gap: var(--s-3); font-size: var(--t-small); }
.footer ul a:hover { color: var(--action); }
.footer__legal { display: flex; flex-wrap: wrap; gap: var(--s-4) var(--s-6); justify-content: space-between;
                 margin-top: var(--s-8); padding-top: var(--s-5); border-top: 1px solid var(--line);
                 font-size: var(--t-label); color: var(--muted); }
.socials { display: flex; gap: var(--s-2); }
.socials a { display: inline-grid; place-items: center; width: 36px; height: 36px; border-radius: 999px; border: 1px solid var(--line); color: var(--ink); }
.socials a:hover { border-color: var(--line-strong); }
.socials svg, .socials img, .socials .icon-mono { width: var(--icon); height: var(--icon); }
/* a brand mark in the text colour (icons.mjs --mono prints these): the SVG is a mask, so it
   follows currentColor on every ground. The mask image is set in the tag's style attribute. */
.icon-mono { display: inline-block; flex: none; width: var(--icon); height: var(--icon); background: currentColor;
             -webkit-mask: center / contain no-repeat; mask: center / contain no-repeat; }
@media (max-width: 1023px) { .footer .footer__col { grid-column: auto / span 6; } .footer .grid > .span-4 { grid-column: 1 / -1; } }
@media (min-width: 640px) and (max-width: 1023px) { .footer .footer__col { grid-column: auto / span 3; } }

/* the company block's one line, set in the display face (footer-columns) */
.footer__lede { font: var(--display-weight) var(--t-h3)/1.25 var(--font-display); letter-spacing: var(--display-tracking); max-width: 22ch; }
/* the legal row's end: the socials sit right of the copyright line */
.footer__legal .socials a { width: 32px; height: 32px; }

/* footer types (dealt, sections.md).
   .footer--dark (Figma, x.ai): a dark ground (with .ground-inverse), the name set large top left, the
   link columns on the right. On a dark page it stays dark: a step darker than the page, a hairline
   on top (system.js sets <html data-tone="dark">), never a light slab under a dark page. */
.footer--dark { border-top: 0; padding-block: var(--section-band) var(--s-6); }   /* a change of ground: the gap a band gets */
html[data-tone="dark"] .footer--dark {
  --bg: color-mix(in oklab, var(--p-bg) 72%, #000); --surface: var(--p-surface); --ink: var(--p-ink); --muted: var(--p-muted);
  --accent: var(--p-accent); --accent-ink: var(--p-accent-ink); --action: var(--p-action); --action-ink: var(--p-action-ink);
  border-top: 1px solid var(--line);
}
.footer__mark { display: inline-flex; align-items: center; font: var(--display-weight) var(--t-h2)/1 var(--font-display); letter-spacing: var(--display-tracking); }
/* .footer--visit (a place): the address set large with the way there, the hours beside it, then
   one row of the nav's words; no third ask for the main action */
.footer__address { font: var(--display-weight) var(--t-h2)/1.1 var(--font-display); letter-spacing: var(--display-tracking); font-style: normal; }
.footer__nav { display: flex; flex-wrap: wrap; align-items: center; gap: var(--s-3) var(--s-6); margin-top: var(--s-8); padding-top: var(--s-5); border-top: 1px solid var(--line); font-weight: 500; }
.footer__nav a:hover { color: var(--action); }
.footer__nav .socials { margin-left: auto; }
.footer--visit .footer__legal { margin-top: var(--s-5); border-top: 0; padding-top: 0; }
/* .footer--statement: the close and the footer in one inset slab on the page's lit ground (sand,
   sky, sage or painting): one big line, one full-width button, then the columns */
.footer--statement {
  margin: 0; border: 0; border-radius: 0; padding-block: var(--s-10) var(--s-6);
  background: var(--ground-bg); color: var(--ground-ink);
  --bg: var(--ground-bg); --surface: var(--ground-surface); --ink: var(--ground-ink); --muted: var(--ground-muted);
  --action: var(--ground-ink); --action-ink: var(--ground-surface); --accent: var(--ground-accent);
  --line: color-mix(in oklab, var(--ground-ink) 14%, transparent); --line-strong: color-mix(in oklab, var(--ground-ink) 28%, transparent);
}
.footer--statement .cta-type { padding-bottom: var(--s-9); margin-bottom: var(--s-8); border-bottom: 1px solid var(--line); }
@media (max-width: 639px) { .footer--statement:not(.closing) { padding-top: var(--s-9); } }
/* opening hours: <dl class="hours" data-tz="Europe/Berlin">, one dt (its days: "Mon to Fri", "Sat and
   Sun", or data-days="mon-fri") and one dd a row. system.js marks today's row .is-today in the venue's
   time zone (never the visitor's clock); the labels are read, so they stay in ink */
.hours { display: grid; grid-template-columns: auto 1fr; gap: var(--s-2) var(--s-5); font-variant-numeric: tabular-nums; }
.hours dt { color: var(--ink); } .hours dd { margin: 0; }
.hours .is-today { font-weight: 500; }
.hours dt.is-today::after { content: ""; display: inline-block; width: 6px; height: 6px; margin-left: var(--s-2); border-radius: 999px; background: var(--accent); vertical-align: 0.2em; }
/* the visit block (a place, sections.md), on the container's lines. Open by default: the words on the page ground,
   no box (a box as wide as the section on a ground of its own reads as a band to the rhythm check, and a phone's
   padding moves its words off the left line). .visit--card is the panel on --g-alt for the full page, where it
   stands in a split column beside the client's photograph: from 1024px up only, at most half the container,
   48px inside; under 1024 it is open type again. .visit--cols is the short page's: address, hours and access as
   three columns, then the menu as .rows under it in the same section.
   Its head is the label "Visit" left and the open-now line right; under it the address column and the hours column 24
   apart; under both at most two 44px rows (access, a guesthouse's check-in, "By appointment").
   <section class="section" data-place="visit" aria-label="Visit"><div class="wrap"><div class="visit">
     <div class="visit__head"><p class="t-label muted">Visit</p><p class="t-small" data-open-now></p></div>
     <div class="visit__cols">
       <div class="visit__col stack-4"><address class="visit__address">Street<br>District</address>
         <a class="link" href="https://www.openstreetmap.org/search?query=..">Get directions</a></div>
       <div class="visit__col"><dl class="hours" data-tz="Europe/Berlin"><dt>Mon to Fri</dt><dd>8 to 18</dd></dl></div>
     </div>
     <ul class="visit__rows"><li><span>Access</span><span>Step-free at the front door</span></li></ul>
   </div></div></section> */
.visit { display: grid; gap: var(--s-5); color: var(--ink); }
.visit__head { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s-4); flex-wrap: wrap; }
.visit__head > * { margin: 0; }
.visit__cols { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: var(--s-5); row-gap: var(--s-5); }   /* the columns stretch to one height (row-lines) */
.visit--cols .visit__cols { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.visit__col { min-width: 0; }
.visit__col > .t-label { margin-bottom: var(--s-3); color: var(--muted); }
.visit__address { font: 400 20px/30px var(--font-text); font-style: normal; }
.visit__rows { display: grid; margin: 0; padding: 0; list-style: none; }
.visit__rows > li { display: flex; align-items: center; justify-content: space-between; gap: var(--s-5); min-height: 44px; border-top: 1px solid var(--line); }
.visit__rows > li > :first-child { color: var(--muted); }
.visit__rows > li > :last-child { text-align: right; }
@media (min-width: 1024px) {
  .visit--card { --bg: var(--p-surface); --surface: var(--p-bg); --card: var(--p-bg); background: var(--bg); border-radius: var(--r-lg); padding: var(--s-7); }
}
@media (max-width: 1023px) { .visit--cols .visit__cols { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 639px) {
  .visit__cols, .visit--cols .visit__cols { grid-template-columns: minmax(0, 1fr); }
  .visit__address { font-size: 18px; line-height: 28px; }
  .visit__rows > li { align-items: flex-start; flex-direction: column; justify-content: center; gap: 0; padding-block: var(--s-2); }
  .visit__rows > li > :last-child { text-align: left; }
}
/* photo credits: one short line that opens the full list (copy.md), at the end of the legal row:
   <details class="credits"><summary>Photographs via Unsplash and Wikimedia Commons</summary>
   <p>one line a photograph, as photos.mjs credits prints them</p></details> */
.credits { flex-basis: 100%; font-size: var(--t-label); color: var(--muted); }
.credits > summary { display: inline; cursor: pointer; list-style: none; }
.credits > summary::-webkit-details-marker { display: none; }
.credits > summary::after { content: "Credits"; margin-left: var(--s-2); color: var(--ink); text-decoration: underline; text-decoration-color: var(--line-strong); text-underline-offset: 3px; }
.credits[open] > summary::after { content: "Hide"; }
.credits > :not(summary) { margin-top: var(--s-2); max-width: 110ch; }
.credits a { text-decoration: underline; text-decoration-color: var(--line-strong); text-underline-offset: 3px; }

/* ---------------------------------------------------------------- footer.closing: the close and the footer, one screen
   The page ends on one more section: <footer class="footer closing [footer--dark | footer--statement |
   footer--visit]"> whose .wrap holds exactly two children, the close (.closing__cta, row 1, the
   rest of the screen) and the links (.closing__links, row 2: the columns, then the legal row). The
   close sits on the footer's own ground, so it is never a slab flush on a footer under it. Its three
   looks (dealt, sections.md):
     .close--photo  the h2 and the button on one head row, then the client's photograph across the
                    .wrap down to the links (never the hero's photograph)
     .close--type   the h2 and a line, then the big button across the .wrap (Figma's close)
     .close--word   the name set across the .wrap in the display face under the h2 and the button
   A phone stacks it in one screen; add .g2m when the links need a screen of their own. */
footer.closing { border-top: 0; }
footer.closing > .wrap { display: grid; grid-template-rows: minmax(0, 1fr) auto; row-gap: var(--s-8); }
footer.closing.g2 > .wrap { grid-template-rows: minmax(0, 1fr) minmax(0, 1fr); }
.closing__cta { min-height: 0; display: flex; flex-direction: column; gap: var(--s-6); }
.closing__cta > .section-head--split, .closing__cta > .section-head { margin-bottom: 0; }
.closing__cta h2 { max-width: 20ch; }
.closing__cta > .close__media { flex: 1 1 0; min-height: clamp(120px, 18svh, 160px); position: relative; overflow: clip; border-radius: var(--r-lg); background: var(--surface); }
.close__media > img { position: absolute; inset: 0; width: 100%; height: 100%; max-width: none; object-fit: cover; object-position: var(--pos, 50% 50%); }
.closing__cta.close--type > .btn--xl { align-self: stretch; }
/* the name across the .wrap: sized in layout.js-free CSS from the container (8 letters fill 1280) */
.close__word { margin-top: auto; font: var(--display-weight) clamp(64px, 14.5vw, 216px)/.86 var(--font-display); letter-spacing: -0.045em;
               white-space: nowrap; overflow: clip; color: var(--ink); }
.closing__links { display: grid; gap: var(--s-7); }
.closing__links > .footer__legal { margin-top: 0; }
.closing__links .footer__lede { font-size: var(--t-lead); max-width: 30ch; }
/* a phone: a close with a photograph takes a screen of its own (the photograph fills what the words
   leave) and the links the next; a close in type stays one screen with its links */
@media (max-width: 639px) {
  footer.closing:has(> .wrap > .closing__cta > .close__media) { --hm: 2; }
  footer.closing:has(> .wrap > .closing__cta > .close__media) > .wrap { grid-template-rows: minmax(0, 1fr) minmax(0, 1fr); row-gap: calc(var(--padt) + var(--padb) + var(--bar)); }
  footer.closing:has(> .wrap > .closing__cta > .close__media) .closing__links { align-self: start; }
}
@media (max-width: 639px) {
  footer.closing > .wrap { row-gap: var(--s-7); }
  .closing__links { gap: var(--s-5); }
  .closing__links > .grid { row-gap: var(--s-5); }
  .closing__links .footer__col { grid-column: auto / span 6; }
  .closing__cta > .close__media { min-height: 140px; }
  .close__word { font-size: clamp(56px, 19vw, 96px); }
}

/* ---------------------------------------------------------------- the big close (closing-type) */
/* the close starts on the left line like every other heading; the big button runs across the .wrap */
.cta-type { display: grid; justify-items: start; gap: var(--s-6); text-align: left; }
.cta-type h2 { max-width: 22ch; }
/* the primary button at its one large size, once a page: 640px wide and centred; .btn--wide runs it
   across the container (Figma's close), on a software page only (system.md) */
.btn--xl { width: min(100%, 640px); height: clamp(64px, 1.4vw + 48px, 72px); font: var(--display-weight) clamp(20px, 0.6vw + 16px, 26px)/1 var(--font-display); letter-spacing: var(--display-tracking); }
.btn--xl.btn--wide { width: 100%; height: clamp(64px, 3vw + 40px, 88px); font-size: clamp(22px, 0.95vw + 18px, 32px); justify-content: space-between; padding-inline: var(--s-7); }
html[data-buttons] .btn--xl::after { width: 0.6em; height: 0.6em; }
/* on a phone it is the page's own button at full width, one step taller, so the pair stays one look */
@media (max-width: 639px) { .btn--xl, .btn--xl.btn--wide { width: 100%; height: 48px; font: 500 18px/1 var(--font-text); letter-spacing: 0; } }

/* ---------------------------------------------------------------- photographs
   .photo-band: one photograph (or film) and a few words. Three uses: the older photo hero
   (.photo-band--hero.photo-band--bleed), one media band mid-page (rhythm media-band) and the close
   (closing-photo). Nothing is laid over the photograph to make words readable: no scrim, gradient,
   veil or blurred panel (PH-31, VI-49). From 640 the words stand in a solid box in the section's own
   colours, lower left on the photograph (.photo-band--left: centred on the left side; --light is the
   same box, kept for old markup). On a phone, and on a place at every width (a place photograph
   carries no words), the photograph stands alone and the words go under it on the ground. */
.photo-band { position: relative; isolation: isolate; overflow: clip; display: grid; align-items: end;
              min-height: clamp(440px, 46vw, 720px); border-radius: var(--r-lg); background: var(--surface); }
.photo-band--bleed { border-radius: 0; }
.photo-band--hero { min-height: calc(100svh - var(--nav-h)); }
/* the older photo hero first in main (layout/hero-photo.html replaces it): the first screen, under the fixed header */
main > .photo-band--hero:first-child { height: 100svh; min-height: 0; }
main > .photo-band--hero:first-child > .photo-band__text { padding-top: calc(var(--nav) + var(--hgap)); }
.photo-band > :is(img, video, picture) { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; max-width: none; object-fit: cover; }
.photo-band > picture > img { width: 100%; height: 100%; object-fit: cover; }
.photo-band__text { position: relative; display: grid; gap: var(--s-4); justify-items: start; color: var(--ink); }
.photo-band__text > :is(h1, h2, p) { max-width: 18ch; }
.photo-band__text > p { max-width: 44ch; font-size: var(--t-lead); }
/* from 640: a solid box in the section's colours, 32px in from the photograph's lower-left corner;
   on a full-bleed band it starts on the page's left line */
@media (min-width: 640px) {
  :root:not([data-type="place"]) .photo-band__text {
    width: fit-content; max-width: min(560px, calc(100% - 2 * var(--s-6))); margin: var(--s-6);
    padding: var(--s-6); background: var(--bg); border-radius: var(--r-md);
  }
  :root:not([data-type="place"]) .photo-band--bleed > .photo-band__text { margin: var(--s-8) max(var(--gut), (100% - var(--container)) / 2); }
  :root:not([data-type="place"]) main > .photo-band--hero:first-child > .photo-band__text { margin-top: calc(var(--nav) + var(--hgap)); padding-top: var(--s-6); }
  .photo-band--left { align-items: center; }
}
@media (max-width: 639px) {
  .photo-band { display: block; min-height: 0; overflow: visible; background: none; border-radius: 0; }
  .photo-band > :is(img, video, picture) { position: relative; inset: auto; height: auto; aspect-ratio: 4 / 5; border-radius: var(--r-lg); }
  .photo-band--bleed > :is(img, video, picture) { border-radius: 0; }
  .photo-band__text { padding: var(--s-5) 0 0; }
  .photo-band--bleed > .photo-band__text { padding: var(--s-5) var(--pad) 0; }
  .photo-band--hero > .photo-band__text { padding-bottom: var(--section); }
  /* the hero's photograph grows to fill the first screen above its words */
  .photo-band--hero { display: flex; flex-direction: column; min-height: calc(100svh - var(--nav-h)); }
  .photo-band--hero > :is(img, video, picture) { flex: 1 0 0; min-height: 100vw; aspect-ratio: auto; object-fit: cover; }
}
:root[data-type="place"] .photo-band { display: flex; flex-direction: column; min-height: 0; overflow: visible; background: none; border-radius: 0; }
:root[data-type="place"] .photo-band > :is(img, video, picture) { position: relative; inset: auto; flex: 1 1 auto; min-height: 0; height: auto; aspect-ratio: 4 / 3; }
:root[data-type="place"] .photo-band__text { padding: var(--s-6) 0 0; }
:root[data-type="place"] .photo-band--bleed > .photo-band__text { padding-inline: max(var(--gut), (100% - var(--container)) / 2); }

/* .pl-photo: every single in-flow photograph on a place (visit, menu, story, booking, close; PH-80).
   It keeps its ratio (--pl-r as a number: 1.3333 for 4:3, .8 for 4:5, 1 for 1:1) and its column, and
   when the screen is short it gets shorter, narrowing from its column's outer edge (.pl-photo--end
   for a photograph in the right-hand column). Square corners, nothing on it.
     <figure class="pl-photo" style="--pl-r: .8"><img src=".." alt=".." loading="lazy"></figure> */
:root { --pl-room: calc(100svh - var(--padt) - var(--padb) - var(--bar)); }
.pl-photo { container-type: inline-size; margin: 0; min-width: 0; }
.pl-photo > img, .pl-photo > picture > img {
  display: block; aspect-ratio: var(--pl-r, 1.3333); width: auto; max-width: 100%;
  height: min(calc(100cqw / var(--pl-r, 1.3333)), var(--pl-cap, calc(var(--pl-room) - var(--pl-head, 0px))));
  object-fit: cover; object-position: var(--pos, 50% 50%); border-radius: var(--r-lg);
}
.pl-photo--end > img, .pl-photo--end > picture > img { margin-left: auto; }
@media (max-width: 1023px) { .pl-photo > img, .pl-photo > picture > img { width: 100%; height: auto; } }

/* .tile: an open tile, the picture on top and its words on the page ground under it, no box
   (a room, a model, a person, a case). One --tile-ratio per row so the pictures line up. */
.tile { display: grid; gap: var(--s-4); align-content: start; color: inherit; }
.tile__media { position: relative; overflow: clip; aspect-ratio: var(--tile-ratio, 4 / 3); border-radius: var(--r-lg); background: var(--surface); }
.tile__media > img { width: 100%; height: 100%; object-fit: cover; transition: transform 600ms var(--ease); }
a.tile:hover .tile__media > img { transform: scale(1.03); }   /* inside its mask; the tile never grows (motion.css has the same) */
.tile--portrait { --tile-ratio: 4 / 5; }
.tile--wide { --tile-ratio: 16 / 9; }
.tile__head { display: flex; align-items: baseline; justify-content: space-between; gap: var(--s-4); }
.tile__head > :is(h3, h4) { font: 500 var(--t-card)/1.3 var(--font-text); letter-spacing: -0.01em; }
.tile__price { flex: none; font-variant-numeric: tabular-nums; white-space: nowrap; }
.tile__facts { color: var(--muted); font-size: var(--t-small); margin-top: calc(-1 * var(--s-3)); }
.tile > p { color: var(--ink); max-width: 52ch; }
/* an object render or a drawing in a tile (line-up): on the lit ground, the object filling the tile */
.tile__media:has(> [data-print], > .drawing) { display: grid; place-items: center; background: var(--ground-bg); }
.tile__media > [data-print] { position: absolute; inset: 0; }
.tile__media > .drawing { width: min(84%, calc(84% * var(--ar, 1.5))); }

/* .drawing: a product with no photograph and no object of its kind, drawn (sections.md, the weak
   case): one inline SVG in true proportions, its lines a fixed 1.5px at every size, one part in the
   accent, dimension lines with their figures as HTML labels placed in percent of the figure.
   <figure class="drawing" style="--ar: 1.6" role="img" aria-label="..">
     <svg viewBox="0 0 1600 1000" aria-hidden="true">
       <g class="part"><path class="fill" d=".."/><path class="ln" d=".."/></g>
       <g class="dim"><path d="M100 960H1500"/><path d="M100 945v30M1500 945v30"/></g>
     </svg>
     <span class="drawing__dim" style="left: 50%; top: 96%">1,400 mm</span>
   </figure>
   In a frame it fits the frame whole (--ar: the viewBox's width over its height); a crop for a
   feature section is the same SVG with the viewBox set round the part. */
.drawing { position: relative; margin: 0; flex: none; aspect-ratio: var(--ar, 1.5); color: var(--ink); }
.frame > .drawing { width: min(100%, calc(var(--ratio, 50%) * var(--ar, 1.5) * 0.86)); }
/* a crop (a feature section's close-up of one part): it fills the frame and runs out of its edges,
   <svg preserveAspectRatio="xMidYMid slice">, no figures on it */
.frame > .drawing.drawing--crop { position: absolute; inset: 0; width: 100%; height: 100%; aspect-ratio: auto; }
.drawing > svg { display: block; width: 100%; height: 100%; overflow: visible; }
.drawing :is(.ln, .fill, .acc, .dim) { vector-effect: non-scaling-stroke; stroke-linecap: round; stroke-linejoin: round; }
.drawing .ln { fill: none; stroke: currentColor; stroke-width: 1.5; }
.drawing .fill { fill: color-mix(in oklab, var(--ink) 6%, var(--bg)); stroke: currentColor; stroke-width: 1.5; }
.drawing .acc { fill: var(--accent); stroke: currentColor; stroke-width: 1.5; }
/* a dark part (a black steel frame, a rubber foot) solid in ink, its seams .ink-ln */
.drawing .ink { fill: var(--ink); stroke: var(--ink); stroke-width: 1.5; }
.drawing .ink-ln { fill: none; stroke: color-mix(in oklab, var(--bg) 45%, var(--ink)); stroke-width: 1; vector-effect: non-scaling-stroke; }
.drawing .dim, .drawing .dim * { fill: none; stroke: var(--muted); stroke-width: 1; }
.drawing .part { pointer-events: bounding-box; }
.drawing .part :is(.ln, .fill, .ink, .acc) { transition: stroke var(--dur) var(--ease), fill var(--dur) var(--ease); }
@media (hover: hover) {
  .drawing .part:hover :is(.ln, .fill) { stroke: var(--accent); }
  .drawing .part:hover .fill { fill: color-mix(in oklab, var(--accent) 14%, var(--bg)); }
  .drawing .part:hover .ink { fill: var(--accent); stroke: var(--accent); }
}
.drawing__dim { position: absolute; transform: translate(-50%, -50%); padding: 2px var(--s-2); border-radius: 999px;
  background: var(--bg); color: var(--ink); font: 500 var(--t-label)/1.3 var(--font-text); font-variant-numeric: tabular-nums; white-space: nowrap; }
@media (max-width: 639px) {
  .drawing__dim { font-size: var(--t-label); padding: 1px 6px; }
  /* room for a figure at the drawing's edge, which keeps its 13px while the drawing shrinks */
  .frame > .drawing:not(.drawing--crop) { width: min(84%, calc(var(--ratio, 50%) * var(--ar, 1.5) * 0.8)); }
  /* a whole drawing (wider than tall) in a phone frame: the frame shortens to it, so a desk or a bike is
     not a small line across a tall empty box (a hero stage still grows to the first screen) */
  .frame:not(:has(> .frame__text)):has(> .drawing:not(.drawing--crop)) { --ratio: 80%; }
}

/* .peek: a list beside one photograph that changes to the row under the pointer (a place's or a
   service's one moment: rooms, spaces, classes, services, the menu's kinds). system.js runs it:
   <div class="grid grid--middle" data-peek>
     <div class="frame frame--photo frame--portrait span-5">
       <img class="frame__img" data-peek-for="garden" src=".." alt="..">
       <img class="frame__img" data-peek-for="kitchen" src=".." alt=".." hidden> ...</div>
     <ul class="rows span-6 start-7"><li data-peek-to="garden">..</li><li data-peek-to="kitchen">..</li></ul>
   </div> */
/* every row's words stay on the left line; the row on show darkens its rule to ink and marks its name
   with a dot after it. The photograph swaps at once (MO-07). The list runs as tall as the photograph
   (the row's two boxes match), its rows from the top. */
[data-peek] > .rows { align-self: stretch; }
[data-peek-to] { cursor: default; transition: border-color var(--dur) var(--ease); }
[data-peek-to].is-on { border-bottom-color: var(--ink); }
[data-peek-to] .rows__name::after { content: ""; display: inline-block; width: 8px; height: 8px; margin-left: var(--s-2); vertical-align: .1em;
  border-radius: 999px; background: var(--accent); opacity: 0; }
[data-peek-to].is-on .rows__name::after { opacity: 1; }
@media (max-width: 1023px) { [data-peek-to] .rows__name::after { display: none; } }
/* a tablet shows the photograph under the list, full width: 5:4, not a portrait taller than the screen */
@media (min-width: 640px) and (max-width: 1023px) { [data-peek] .frame--portrait { --ratio: 80%; } }

/* .rows: a list read across, a name (and a line) left, a value right, hairlines between: a menu, a
   price list, services with prices, specs, hours. Never cards for these. */
.rows { border-top: 0; }   /* each row closes with its own rule; no rule above the first (ST-43) */
.rows > li { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: var(--s-1) var(--s-5); padding-block: var(--s-4); border-bottom: 1px solid var(--line); }
/* no rule above the first row, so no padding either: its words start on the line beside it (a photograph's top) */
.rows > li:first-child { padding-top: 0; }
.rows__name { font-weight: 500; }
.rows__value { grid-column: 2; grid-row: 1; text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
.rows > li > p { grid-column: 1; color: var(--ink); max-width: 56ch; }
.rows--spec .rows__name { font-weight: 400; color: var(--muted); }

/* forms (booking-form): fields on the system's control height, one radius, labels above */
.form { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--s-4); }
.form > :is(.field--full, .btn-row, p) { grid-column: 1 / -1; }
.field { display: grid; gap: var(--s-2); font-size: var(--t-small); font-weight: 500; }
.field :is(input, select, textarea) {
  width: 100%; height: var(--btn-h); padding: 0 var(--s-3); border: 1px solid var(--line-strong); border-radius: var(--r-sm);
  background: var(--bg); color: var(--ink); font: 400 var(--t-body)/1.4 var(--font-text);
}
.field textarea { height: auto; min-height: 120px; padding-block: var(--s-3); resize: vertical; }
@media (max-width: 639px) { .form { grid-template-columns: minmax(0, 1fr); } }

/* sections part by a change of ground or by space only: no rule between them (.section--rule is plain) */

/* the phone action bar (a place's directions and booking; other types may use it): fixed at the foot
   under 640px, one 342x48 button or two of 165, and every section's foot pads for it (--bar) */
.actionbar { display: none; }
@media (max-width: 639px) {
  :root:has(> body > nav.actionbar) { --bar: calc(64px + env(safe-area-inset-bottom)); }
  .actionbar {
    position: fixed; left: 0; right: 0; bottom: 0; z-index: 40; display: grid; grid-auto-flow: column; grid-auto-columns: minmax(0, 1fr);
    gap: var(--s-3); align-items: center; height: calc(64px + env(safe-area-inset-bottom));
    padding: var(--s-2) var(--gut) env(safe-area-inset-bottom); background: var(--bg); border-top: 1px solid var(--line);
  }
  .actionbar .btn { width: 100%; height: 48px; }
}

/* a brand-colour band (product and place may add one, in the page's second half): the accent as the
   section's ground, its words in the accent's ink */
.ground-brand { --bg: var(--p-accent); --surface: color-mix(in oklab, var(--p-accent) 88%, var(--p-accent-ink)); --ink: var(--p-accent-ink);
  --muted: color-mix(in oklab, var(--p-accent-ink) 82%, var(--p-accent)); --card: var(--surface);
  --action: var(--p-accent-ink); --action-ink: var(--p-accent); background: var(--bg); color: var(--ink); }
.ground-brand { --line: color-mix(in oklab, var(--ink) 16%, transparent); --line-strong: color-mix(in oklab, var(--ink) 30%, transparent); }

/* a [bracketed placeholder] or a "(sample)" tag left in visible text: system.js marks it so it shows
   in every screenshot; nothing like it ships (copy.md) */
[data-placeholder] { outline: 2px dashed #d92d20; outline-offset: 2px; }

/* ---------------------------------------------------------------- highlight + entrance + motion */
/* data-hl (older markup) is plain ink from the first frame: nothing on the page changes colour on load
   (MO-62); a heading's second half in .muted is the one highlight */
/* the hero's words are set on the first frame: no entrance (.enter stays a no-op for old markup) */
.enter { animation: none; }
@keyframes fade { from { opacity: 0; } }
@media (prefers-reduced-motion: reduce) {
  /* a card loop of motion.css ([data-m-loop]) holds its own finished frame */
  :not([data-m-loop], [data-m-loop] *), ::before, ::after { animation-duration: .001ms !important; animation-iteration-count: 1 !important;
                           transition-duration: .001ms !important; scroll-behavior: auto !important; }
}

/* ---------------------------------------------------------------- helpers */
.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0; }
.stack-2 > * + * { margin-top: var(--s-2); }
.stack-4 > * + * { margin-top: var(--s-4); }
.stack-5 > * + * { margin-top: var(--s-5); }
.stack-6 > * + * { margin-top: var(--s-6); }
````



---

## `assets/system.js`

````js
/*
  taste-skill system.js - the page behaviour every build shares. Load it once, at the end of <body>:
    <script type="module" src="assets/system.js"></script>
  Write no second script for any of this.

  - nav: hover menus are CSS; this adds the phone sheet, the accordion, Escape and aria-expanded, and
    closes the sheet after a tap on any link in it.
  - tabs: [role=tablist] with [role=tab][aria-controls] and [role=tabpanel]. aria-controls may name
    several ids (the tab's text and its screen in a frame); they are shown and hidden together.
  - text highlight: none. <p data-hl> (older markup) stays plain ink from the first frame; nothing
    changes colour on load (MO-62).
  - FAQ: every .faq answer is open (ST-47): a <details> in .faq is opened and stays open.
  - opening hours: <dl class="hours" data-tz="Europe/Berlin"> marks today's dt and dd .is-today in the
    venue's time zone (each dt names its days, "Mon to Fri", "Sat and Sun", "Daily", or carries
    data-days="mon-fri" / "sat,sun"). Without data-tz no row is marked: never the visitor's clock,
    and an .is-today written in the markup is taken out (it would be wrong six days a week). A
    [data-open-now] line reads "Open now, until 16:00" or "Closed, opens Tuesday at 7:30" from them.
  - moments: a page with [data-moment] loads assets/moments/moments.js (references/moments.md), which
    mounts the dealt moments once; data-ready waits for them.
  - peek: [data-peek] holds rows [data-peek-to="key"] and photographs [data-peek-for="key"] (all but
    the first hidden); the photograph changes at once (MO-07) to the row under the pointer, the
    keyboard focus or a tap. A place's or a service's one moment (references/sections.md).
  - visuals (assets/effects/fx.js and assets/ui/ui.js are loaded only when the page has any):
    * mounts every [data-fx] ground; only a ground inside the hero (.hero) moves, and not when its frame
      holds an object or a scene ([data-print], [data-scene], assets/objects). Every other one is
      drawn once when it nears the screen, kept as a plain picture and its WebGL context freed
      (ui.grounds), so a page holds at most
      3 live WebGL contexts (4 while an object moves on screen); a ground a fragment drives (the
      slider) stays live near the screen. The featured plan's lit border (data-glow="edge-glow",
      data-glow-params) rests on a quiet hairline and runs one light round its edge on hover or
      focus;
    * lights every ground that holds UI (a .panel, .panel__screen or .frame) and the closing band's
      (.frame--cta > .frame__fx) with the page's lit ground: <html data-ground="sand|sky|sage|painting">
      (system.css --ground-*), on light and dark pages alike; without data-ground the page palette
      picks one. data-fx-palette on the element wins; --hue on it changes only its accent;
    * starts every pasted [data-ui] fragment (assets/ui/<name>/fragment.html, its names, numbers and
      logos rewritten to the client's) and loads every [data-ui-load] one (the kit's sample text: a
      draft only, never shipped). Each holds its
      finished picture (system.js marks it data-ui-still, so ui.js holds it the moment its own load
      resolves) unless it, or an element around it, carries data-ui-loop (one per card group) or
      data-ui-cycles. On a phone (under 640px), on kind other (<meta name="site-kind"
      content="other">) and on a place nothing loops, voice included, and the hero's ground is drawn
      once: every fragment holds its finished picture and plays only while the pointer is on its card;
    * pause buttons: ui.js puts one on every loop when it starts to move (a 32px disc 12px in from
      the bottom-right corner of its panel or frame); system.js gives the hero's moving ground the
      same button, shared with a loop in that frame. A box that already holds a .loop-pause (a loop
      the page runs itself) gets none;
    * sets <html data-ready="1"> when all of it is drawn (shoot.mjs and consistency.mjs wait for it).
  - page tone: <html data-tone="dark|light"> from the palette's base (a dark footer stays dark).
  - pictures: lazy images are fetched once the page has loaded, so no photograph shows as an empty
    frame; one that fails to load is outlined in red and counted (<html data-broken>).
  - guards: a [bracketed placeholder], a "(sample)" tag, a line that explains or apologises ("Names
    and figures on this page are examples") or a printed .example address gets a red dashed outline
    and <html data-placeholders="n">; an effect id in more than two sections sets <html data-fx-repeat>.
*/
const reduced = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const HERE = new URL('./', import.meta.url);
/* kind other (a cafe, a shop, a studio, a service firm) and a place: nothing moves by itself (MO-07) */
const kindOther = () => {
  const m = document.querySelector('meta[name="site-kind"]');
  return document.documentElement.dataset.type === 'place' || (!!m && m.content.trim().toLowerCase() === 'other');
};

function nav() {
  const nav = document.querySelector('.nav');
  if (!nav) return;
  const toggle = nav.querySelector('.nav__toggle');
  const bars = '<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 5h14M2 13h14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
  const cross = '<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M4 4l10 10M14 4L4 14" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
  const setOpen = open => {
    nav.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-locked', open);
    if (toggle) { toggle.setAttribute('aria-expanded', String(open)); toggle.innerHTML = open ? cross : bars; }
  };
  toggle?.addEventListener('click', () => setOpen(!nav.classList.contains('is-open')));
  nav.querySelectorAll('.nav__item').forEach(item => {
    if (!item.querySelector('.nav__menu')) return;
    let btn = item.querySelector('.nav__expand');
    if (!btn) {
      btn = document.createElement('button');
      btn.className = 'nav__expand';
      btn.type = 'button';
      btn.innerHTML = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>';
      item.querySelector('.nav__link').after(btn);
    }
    const label = item.querySelector('.nav__link')?.textContent.trim() || 'section';
    btn.setAttribute('aria-label', `Show ${label} links`);
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', () => {
      const open = !item.classList.contains('is-expanded');
      item.classList.toggle('is-expanded', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('keydown', e => {
    if (e.key !== 'Escape') return;
    if (nav.classList.contains('is-open')) { setOpen(false); toggle?.focus(); return; }
    if (nav.contains(document.activeElement)) document.activeElement.blur();
  });
  // a tap on any link in the open sheet closes it (a top-level word, a menu link, an action, an
  // in-page #anchor alike), so the page it leads to is never left under the sheet
  nav.addEventListener('click', e => {
    if (nav.classList.contains('is-open') && e.target.closest?.('a[href]')) setOpen(false);
  });
  window.matchMedia('(min-width: 1024px)').addEventListener('change', e => { if (e.matches) setOpen(false); });
}

function tabs() {
  const parts = t => (t.getAttribute('aria-controls') || '').split(/\s+/).filter(Boolean).map(id => document.getElementById(id)).filter(Boolean);
  document.querySelectorAll('[role="tablist"]').forEach(list => {
    const tabs = [...list.querySelectorAll('[role="tab"]')];
    let first = true;
    const select = (tab, focus) => {
      tabs.forEach(t => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        parts(t).forEach(el => {
          const was = el.hidden;
          el.hidden = !on;
          // a panel or a screen in a frame fades in on a chosen tab only (opacity only, nothing moves;
          // the panel shown at load is there on the first frame, MO-62)
          if (on && was && !first && !reduced()) el.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 280, easing: 'ease-out' });
        });
      });
      if (focus) tab.focus();
    };
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', e => {
        const d = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : e.key === 'ArrowLeft' || e.key === 'ArrowUp' ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        select(tabs[(i + d + tabs.length) % tabs.length], true);
      });
    });
    select(tabs.find(t => t.getAttribute('aria-selected') === 'true') || tabs[0]);
    first = false;
  });
}

/* every FAQ answer open, for good: a <details> in .faq is opened and its summary no longer closes it */
function faq() {
  document.querySelectorAll('.faq details').forEach(d => {
    d.open = true;
    d.addEventListener('toggle', () => { if (!d.open) d.open = true; });
    const s = d.querySelector(':scope > summary');
    if (s) s.addEventListener('click', e => e.preventDefault());
  });
}

/* ------------------------------------------------------------------ opening hours
   today's row in the venue's time zone, from data-tz on the dl; never the visitor's clock */
const DAYS = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'];
function daySet(text) {
  const t = String(text || '').toLowerCase().replace(/\bweekdays\b/g, 'mon to fri').replace(/\bweekends?\b/g, 'sat and sun');
  if (/\b(daily|every day|all week|mon(day)?\s*(?:-|–|to)\s*sun(day)?)\b/.test(t)) return new Set(DAYS);
  const hits = [...t.matchAll(/\b(sun|mon|tue|wed|thu|fri|sat)[a-z]*\.?/g)];
  if (!hits.length) return null;
  const set = new Set();
  for (let i = 0; i < hits.length; i++) {
    const a = DAYS.indexOf(hits[i][1]);
    const next = hits[i + 1];
    const between = next ? t.slice(hits[i].index + hits[i][0].length, next.index) : '';
    if (next && /^\s*(?:-|–|to|till|until|through)\s*$/.test(between)) {
      const b = DAYS.indexOf(next[1]);
      for (let d = a; ; d = (d + 1) % 7) { set.add(DAYS[d]); if (d === b) break; }
      i++;
    } else set.add(DAYS[a]);
  }
  return set;
}
function hours() {
  document.querySelectorAll('dl.hours').forEach(dl => {
    dl.querySelectorAll('.is-today').forEach(el => el.classList.remove('is-today'));
    const tz = dl.dataset.tz;
    if (!tz) return;
    let today;
    try { today = new Intl.DateTimeFormat('en-US', { weekday: 'short', timeZone: tz }).format(new Date()).slice(0, 3).toLowerCase(); }
    catch { console.warn(`system.js: hours: unknown time zone ${tz}`); return; }
    for (const dt of dl.querySelectorAll('dt')) {
      const days = daySet(dt.dataset.days ? dt.dataset.days.replace(/,/g, ' and ') : dt.textContent);
      if (!days?.has(today)) continue;
      dt.classList.add('is-today');
      for (let dd = dt.nextElementSibling; dd && dd.tagName === 'DD'; dd = dd.nextElementSibling) dd.classList.add('is-today');
      break;
    }
  });
  openNow();
}
/* [data-open-now] (a line in the visit block or the hero's notice) reads "Open now, until 16:00" or
   "Closed, opens Tuesday at 7:30" from the first dl.hours with data-tz, in the venue's time zone; its
   own text stays when the hours cannot be read (no data-tz, a row without times) */
const DAY_NAMES = { sun: 'Sunday', mon: 'Monday', tue: 'Tuesday', wed: 'Wednesday', thu: 'Thursday', fri: 'Friday', sat: 'Saturday' };
function openNow() {
  const outs = document.querySelectorAll('[data-open-now]');
  const dl = document.querySelector('dl.hours[data-tz]');
  if (!outs.length || !dl) return;
  let parts;
  try {
    parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { weekday: 'short', hour: '2-digit', minute: '2-digit', hourCycle: 'h23', timeZone: dl.dataset.tz })
      .formatToParts(new Date()).map(p => [p.type, p.value]));
  } catch { return; }
  const today = DAYS.indexOf(parts.weekday.slice(0, 3).toLowerCase());
  const nowMin = (+parts.hour % 24) * 60 + +parts.minute;
  const span = day => {
    for (const dt of dl.querySelectorAll('dt')) {
      const days = daySet(dt.dataset.days ? dt.dataset.days.replace(/,/g, ' and ') : dt.textContent);
      if (!days?.has(DAYS[day])) continue;
      const dd = dt.nextElementSibling;
      const m = dd && dd.tagName === 'DD' && dd.textContent.match(/(\d{1,2})(?:[:.](\d{2}))?\s*(?:to|-|–|until)\s*(\d{1,2})(?:[:.](\d{2}))?/);
      return m ? { open: +m[1] * 60 + (+m[2] || 0), close: +m[3] * 60 + (+m[4] || 0), from: m[1] + (m[2] ? ':' + m[2] : ''), to: m[3] + (m[4] ? ':' + m[4] : ':00') } : { closed: true };
    }
    return null;
  };
  const t = span(today);
  let text = null;
  if (t && !t.closed && nowMin >= t.open && nowMin < t.close) text = `Open now, until ${t.to}`;
  else {
    for (let k = 0; k < 8 && !text; k++) {
      const d = (today + k) % 7, s2 = span(d);
      if (!s2 || s2.closed || (k === 0 && nowMin >= s2.open)) continue;
      text = `Closed, opens ${k === 0 ? 'today' : k === 1 ? 'tomorrow' : DAY_NAMES[DAYS[d]]} at ${s2.from}`;
    }
  }
  if (text) outs.forEach(o => { o.textContent = text; });
}

/* ------------------------------------------------------------------ peek
   a list beside one photograph that changes to the row under the pointer, the focus or a tap */
function peek() {
  document.querySelectorAll('[data-peek]').forEach(root => {
    const rows = [...root.querySelectorAll('[data-peek-to]')];
    const pics = [...root.querySelectorAll('[data-peek-for]')];
    if (!rows.length || !pics.length) return;
    let cur = null;
    // the swap is instant (MO-07): the row's photograph shows, the others hide, nothing fades
    const show = row => {
      const pic = pics.find(p => p.dataset.peekFor === row.dataset.peekTo);
      if (!pic || row === cur) return;
      cur = row;
      // the row on show is marked beside its photograph only (from 1024); stacked, the list stays plain
      const wide = matchMedia('(min-width: 1024px)').matches;
      rows.forEach(r => r.classList.toggle('is-on', wide && r === row));
      pics.forEach(p => { p.hidden = p !== pic; });
    };
    // every photograph is fetched now, so a swap never shows an empty frame
    pics.forEach(p => { if (p.loading === 'lazy') p.loading = 'eager'; });
    show(rows.find(r => pics.some(p => !p.hidden && p.dataset.peekFor === r.dataset.peekTo)) || rows[0]);
    rows.forEach(r => {
      r.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') show(r); });
      r.addEventListener('focusin', () => show(r));
      r.addEventListener('click', e => { if (!e.target.closest('a, button, input, select, textarea')) show(r); });
    });
  });
}

/* ------------------------------------------------------------------ visuals */
let probe;
function rgb(value) {
  value = (value || '').trim();
  if (!value) return null;
  probe = probe || document.createElement('canvas').getContext('2d', { willReadFrequently: true });
  probe.canvas.width = probe.canvas.height = 1;
  probe.clearRect(0, 0, 1, 1);
  probe.fillStyle = '#000';
  probe.fillStyle = value;
  probe.fillRect(0, 0, 1, 1);
  const d = probe.getImageData(0, 0, 1, 1).data;
  return d[3] ? [d[0], d[1], d[2]] : null;
}
const hex = c => '#' + c.map(v => Math.round(v).toString(16).padStart(2, '0')).join('');

// The page's lit ground (references/cards.md: sand, sky, sage or painting, <html data-ground>, picked at
// random from the three on a tech page; a page of kind other has none, it is flat). Without data-ground the
// page palette picks one, so two sites never share it by default.
const GROUNDS = ['sand', 'sky', 'sage'];
function groundTokens() {
  const html = document.documentElement;
  if (!html.dataset.ground) {
    const first = document.querySelector('.card [data-fx], .frame [data-fx], .frame[data-fx]');
    const root = getComputedStyle(html);
    const key = `${root.getPropertyValue('--p-bg')}${root.getPropertyValue('--p-accent')}`.replace(/\s/g, '');
    let h = 0;
    for (const c of key) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    html.dataset.ground = first?.dataset.fx === 'painterly-landscape' ? 'painting' : GROUNDS[h % GROUNDS.length];
  }
  const cs = getComputedStyle(html);
  const t = k => cs.getPropertyValue(`--ground-${k}`).trim();
  return { bg: t('bg'), surface: t('surface'), ink: t('ink'), muted: t('muted'), accent: t('accent') };
}
// every ground that holds UI, and the closing band's, takes the lit ground on light and dark pages
// alike: clearly lighter than a dark card, a clear step darker than white UI, so page, card, panel and
// UI are never four near-black layers. data-fx-palette on the element wins; --hue changes its accent.
function lightGrounds() {
  const g = groundTokens();
  document.querySelectorAll('[data-fx]').forEach(el => {
    if (el.dataset.fxPalette) return;
    const band = el.matches('.frame--cta > .frame__fx');
    if (!band && !el.matches('.panel, .panel__screen, .frame')) return;
    const hue = rgb(getComputedStyle(el).getPropertyValue('--hue'));
    el.dataset.fxPalette = JSON.stringify({ ...g, ...(hue ? { accent: hex(hue) } : {}) });
    // the box itself takes the lit colour too: an effect that keeps its host's own background (a
    // frame's dark surface on a dark page) then still draws on the lit ground, and nothing flashes dark
    if (!band) el.style.backgroundColor = g.bg;
  });
}

// the featured plan's lit border (cards.css .plan.is-featured): it rests on a quiet accent hairline;
// on hover or keyboard focus one light runs round its edge (edge-glow, mounted for that lap, then
// faded and freed), so nothing moves on its own or because the page scrolled
function glowOnHover(fx, els) {
  for (const el of els) {
    let busy = false;
    const lap = async () => {
      if (busy || reduced()) return;
      busy = true;
      try {
        let params = {};
        try { params = JSON.parse(el.dataset.glowParams || '{}'); } catch { /* defaults */ }
        const c = await fx.mount(el, el.dataset.glow, { palette: fx.readPalette(el), params, seed: 2 });
        const r = el.getBoundingClientRect(), per = 2 * (r.width + r.height);
        await new Promise(res => setTimeout(res, per / Math.max(40, Math.min(c.params?.speed || 400, per / 4)) * 1000));
        el.classList.add('is-fading');
        await new Promise(res => setTimeout(res, 650));
        c.destroy();
      } catch (e) { console.warn('system.js: glow', e); }
      el.classList.remove('is-fading');
      busy = false;
    };
    el.addEventListener('pointerenter', lap);
    el.addEventListener('focusin', lap);
    fx.load(el.dataset.glow).catch(() => {});
  }
}

async function visuals() {
  // a lit border written as data-fx="edge-glow" is the hover light (data-glow), never a ground
  document.querySelectorAll('[data-fx="edge-glow"]').forEach(el => {
    el.dataset.glow = 'edge-glow';
    if (el.dataset.fxParams && !el.dataset.glowParams) el.dataset.glowParams = el.dataset.fxParams;
    el.removeAttribute('data-fx');
  });
  const grounds = [...document.querySelectorAll('[data-fx]')];
  const glows = [...document.querySelectorAll('[data-glow]')];
  const frags = [...document.querySelectorAll('[data-ui-load], [data-ui]')].filter(el => !el.parentElement?.closest('[data-ui-load]'));
  if (!grounds.length && !frags.length && !glows.length) return;
  // only the hero's ground moves, and not when its frame holds an object (assets/objects: data-print),
  // which is then that visual's one motion and its pause button the only one in the corner. On a phone
  // (under 640px), on kind other and on a place nothing loops: the hero's ground is drawn once like the
  // rest and every fragment holds its finished picture (as most good sites cut motion there), so no
  // pause button covers the UI. A held fragment still plays while the pointer is on its card.
  const phone = window.matchMedia('(max-width: 639px)').matches || kindOther();
  const box = el => el.closest('.frame, .panel__screen, .panel') || el;
  const moving = phone ? [] : grounds.filter(el => el.closest('.hero, .section--hero') && !box(el).querySelector('[data-print], [data-scene]'));
  const live = el => moving.includes(el);
  const [fx, ui] = await Promise.all([
    grounds.length || glows.length ? import(new URL('effects/fx.js', HERE).href).then(m => m.default) : null,
    import(new URL('ui/ui.js', HERE).href).then(m => m.default),
  ]);
  const name = el => el.dataset.uiLoad || el.dataset.ui || '';
  const loops = el => !phone && !!el.closest('[data-ui-loop], [data-ui-cycles]');
  // a fragment that does not loop is held on its finished picture as soon as its own load resolves
  frags.forEach(el => { if (!loops(el)) el.setAttribute('data-ui-still', ''); });
  const opts = el => { try { return JSON.parse(el.dataset.uiOpts || '{}'); } catch { return {}; } };
  const run = el => (el.dataset.uiLoad ? ui.load(el, el.dataset.uiLoad, opts(el)) : ui.start(el)).catch(e => console.warn(e));

  if (fx) lightGrounds();
  await Promise.all([
    // the hero's ground moves and keeps its context; every other ground is baked to a picture
    fx && Promise.all(moving.map(el => fx.mountAll(el))),
    fx && grounds.length && ui.grounds(document, fx, { skip: live }),
    ...frags.map(run),
  ]);
  // the hero's ground moves, so it gets the pause button every loop has (one per frame, shared)
  if (fx && ui) moving.forEach(el => { const c = fx.get(el); if (c) ui.pausable(el.closest('.panel__screen, .panel, .frame') || el, c); });
  if (fx && glows.length) glowOnHover(fx, glows);
}

/* ------------------------------------------------------------------ page tone
   <html data-tone="dark|light"> from the palette's base, so a dark footer stays dark on a dark page
   (system.css .footer--dark) instead of turning into the light inverse */
function tone() {
  const c = rgb(getComputedStyle(document.documentElement).getPropertyValue('--p-bg'));
  if (!c) return;
  const lin = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
  const L = 0.2126 * lin(c[0]) + 0.7152 * lin(c[1]) + 0.0722 * lin(c[2]);
  document.documentElement.dataset.tone = L < 0.18 ? 'dark' : 'light';
}

/* ------------------------------------------------------------------ pictures always draw
   A photograph never shows as an empty frame: once the page has loaded, every lazy image is fetched
   (so one far down the page is there when a visitor or a screenshot reaches it), and one that fails
   to load is outlined in red and counted (<html data-broken="n">), like a placeholder. */
function pictures() {
  const html = document.documentElement;
  let broken = 0;
  const fail = img => {
    if (img.dataset.broken != null) return;
    img.dataset.broken = '';
    img.setAttribute('data-placeholder', '');
    html.dataset.broken = String(++broken);
    console.warn(`system.js: a picture did not load: ${img.currentSrc || img.src}`);
  };
  document.querySelectorAll('img').forEach(img => {
    // an SVG with only a viewBox reports no natural width though it draws: decode() tells
    if (img.complete && img.getAttribute('src') && !img.naturalWidth) img.decode().catch(() => fail(img));
    else img.addEventListener('error', () => fail(img), { once: true });
  });
  const eager = () => document.querySelectorAll('img[loading="lazy"]').forEach(img => { img.loading = 'eager'; });
  const idle = window.requestIdleCallback || (f => setTimeout(f, 200));
  if (document.readyState === 'complete') idle(eager);
  else window.addEventListener('load', () => idle(eager), { once: true });
}

/* ------------------------------------------------------------------ guards
   Faults that shipped before: a [bracketed placeholder] or a "(sample)" tag in visible text, a line that
   explains or apologises ("Names and figures on this page are examples", "made in code", "photographs
   follow"), a printed .example address, and one effect in more than two sections. Each is marked so it
   shows in every screenshot and the checker can read it: [data-placeholder] (a red dashed outline,
   system.css) and <html data-placeholders="n">; <html data-fx-repeat="id ...">. */
const PLACEHOLDER = /\[[^\]\n]{1,60}\]|\((?:sample|placeholder|example)[^)]{0,30}\)|\bsample (?:figure|price|name|quote|number|photo|page)s?\b|\bplaceholder\b|\bnames and figures\b|\b(?:are|is) (?:examples?|illustrative|invented)\b|\bfor illustration\b|\b(?:made|drawn|rendered) in code\b|\bphotographs? (?:follow|to follow|coming)\b|\bto be replaced\b|[\w.+-]+@[\w-]+\.example\b|\bwww\.[\w-]+\.example\b/i;
function guards() {
  const html = document.documentElement;
  let n = 0;
  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
    acceptNode: t => (t.parentElement?.closest('script, style, template, noscript') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT),
  });
  for (let t = walk.nextNode(); t; t = walk.nextNode()) {
    if (PLACEHOLDER.test(t.textContent)) { t.parentElement.setAttribute('data-placeholder', ''); n++; }
  }
  document.querySelectorAll('img[alt]').forEach(img => { if (PLACEHOLDER.test(img.alt)) { img.setAttribute('data-placeholder', ''); n++; } });
  // the old figures note, whatever its words
  document.querySelectorAll('.figures-note').forEach(el => { if (!el.hasAttribute('data-placeholder')) { el.setAttribute('data-placeholder', ''); n++; } });
  if (n) { html.dataset.placeholders = String(n); console.warn(`system.js: ${n} placeholder, sample tag, apology or .example address left in visible text`); }
  // an effect id in at most two sections (a card group counts once; the closing band is a section)
  const seen = new Map();
  document.querySelectorAll('[data-fx]').forEach(el => {
    if (el.closest('.nav')) return;   // the menu card's panel is hidden until hover: not counted
    const sec = el.closest('section, footer') || el;
    if (!seen.has(el.dataset.fx)) seen.set(el.dataset.fx, new Set());
    seen.get(el.dataset.fx).add(sec);
  });
  const repeat = [...seen].filter(([, s]) => s.size > 2).map(([id]) => id);
  if (repeat.length) { html.dataset.fxRepeat = repeat.join(' '); console.warn(`system.js: effect in more than two sections: ${repeat.join(', ')}`); }
}

/* ------------------------------------------------------------------ moments
   The page's one or two dealt moments (assets/moments, references/moments.md): loaded only when the page
   holds a [data-moment]; data-ready waits for them. mount is idempotent, so nothing mounts twice. */
async function moments() {
  if (!document.querySelector('[data-moment]')) return;
  const m = await import(new URL('moments/moments.js', HERE).href);
  await m.ready;
}

function init() {
  try { tone(); } catch (e) { console.warn('system.js: tone', e); }
  nav();
  tabs();
  try { faq(); } catch (e) { console.warn('system.js: faq', e); }
  try { hours(); } catch (e) { console.warn('system.js: hours', e); }
  try { peek(); } catch (e) { console.warn('system.js: peek', e); }
  try { pictures(); } catch (e) { console.warn('system.js: pictures', e); }
  try { guards(); } catch (e) { console.warn('system.js: guards', e); }
  Promise.all([
    visuals().catch(e => console.warn('system.js: visuals', e)),
    moments().catch(e => console.warn('system.js: moments', e)),
  ]).finally(() => { document.documentElement.dataset.ready = '1'; });
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
else init();

export default { init };
````



---

## `assets/effects/README.md`

# Effects

25 effect grounds drawn in code, for hero frames, feature cards and bands. Each one takes all its
colours from the page palette. Nothing here loads a video or another library; only the photo grade
takes an image, the section's own photograph.

- `gallery.html` shows every effect live, with a palette switcher, a random pick and the UI kit's
  feature cards. `lab.html` has a slider for every param and card, wide and hero layouts.
- Both pages need http, not `file://`. Run `node scripts/effects.mjs serve --port 5230` and open
  `/assets/effects/gallery.html`.

## Mount

Give an element a size and a `data-fx` id, then mount every one on the page:

```html
<div class="panel" data-fx="caustics" data-fx-seed="21"></div>

<script type="module">
  import fx from './assets/effects/fx.js';
  fx.mountAll(document);
</script>
```

- **Palette.** Each element reads `--bg`, `--surface`, `--ink`, `--muted`, `--accent` and
  `--accent-ink`, or `--fx-bg` and the other `--fx-*` names, which win. You can also pass one:
  `fx.mountAll(document, { bg, surface, ink, muted, accent, accentInk })`. To change a single colour
  on one element, use `data-fx-palette='{"accent":"#..."}'`.
- **Seed.** `data-fx-seed` fixes the composition. Without a seed you get a new picture on every load.
- **Params.** `data-fx-params='{"speed":0.3}'`. `index.json` lists each param with its range. Text on
  an effect: set `calmX` and `calmY` (0 to 1 of the frame) to where the text sits. The effect keeps that
  area quiet.
- **One element.** `const c = await fx.mount(el, 'caustics', { palette, seed, params })`. The result `c`
  has `pause()`, `resume()`, `set(params)`, `setPalette(p)` and `destroy()`.
- **Built in.** An effect stops drawing when it leaves the screen or the tab is hidden. Under
  `prefers-reduced-motion` it shows one still frame. Without WebGL it shows a CSS picture in the same
  colours. Device pixel ratio is capped (1.75 unless an effect needs crisp pixels). When a page has
  more than 14 live WebGL contexts, the idle off-screen ones are freed first.
- Put text and UI fragments inside the element. The canvas sits under them (`z-index: -1` in an
  isolated element).

## Random pick

A page gets its effects dealt, never chosen by taste. One effect per slot: `hero` is the hero or a
large split frame, `card` is a card group, `band` is a wide band or the closing call to action, and
`footer` is the footer. Only effects made for the page's palette kind (`palettes` in meta.json) and
that slot are dealt, never the same id twice on one page (when every effect for a slot is on the
page already, one repeats with its own seed and pick prints a note). The command needs `--palette`;
in the browser, a call without a palette deals only effects made for all three kinds. Ids from
recent pages and second picks from a family already dealt are less likely. Two effects that list
each other in `avoidWith` never share a page.

A **focal** ground (`"focal": true`) has its own subject: a sphere, a beam, peaks, a pool of light.
It takes one compact UI piece, never a big window, a screenshot or text. `--quiet` (`quiet: true` in
the browser) deals only the even, **quiet** grounds, for a slot that carries a big window.

Four effects are never dealt (`"random": false` in meta.json): `dotted-globe` (a literal subject, only
for a product whose reach is global: payments, infrastructure, logistics, networks), `duotone-grade`
(grades the section's own photograph), `edge-glow` (the lit border of the one key object, a prompt box
or the featured plan) and `ridgeline` (the divider band in `assets/components/fx-band`). Name one in
its slot when the content calls for it. It is still refused on a palette kind or a slot it is not made
for, when the same id is named twice, and next to an effect it avoids (named or passed in `--exclude`):

```bash
node scripts/effects.mjs pick --palette dark --slots hero,card,band --seed 4821 --history .taste-skill/effects-history.json
node scripts/effects.mjs pick --palette dark --slots hero:dotted-globe,card,band --seed 4821 --history .taste-skill/effects-history.json
```

In the browser, the same code:

```js
import { pick } from './assets/effects/pick.js';
const index = await fetch('./assets/effects/index.json').then(r => r.json());
const { picks } = pick(index.effects, { palette: fx.paletteKind(palette), slots: ['hero', 'card', 'card'], history });
// picks: [{ slot: 'hero', id: 'god-rays' }, ...]; history: the ids of earlier picks, oldest first
// a named slot: slots: ['hero:dotted-globe', 'card'] (or { slot: 'hero', id: 'dotted-globe' })
```

`fx.paletteKind(palette)` gives `light`, `dark` or `colour` from the background colour.

## The list

| id | Name | Family | Slots | Palettes | Ground | Motion |
|---|---|---|---|---|---|---|
| `film-light-leak` | Film light leak | Grain | hero, card, band | dark, colour | focal | slow |
| `grain-gradient` | Grain gradient | Grain | hero, card, band, footer | light, dark, colour | quiet | slow |
| `ascii-shade` | ASCII shade | Dither | hero, card, footer | light, dark, colour | focal | slow |
| `bayer-dither` | Bayer dither | Dither | hero, card, band, footer | light, dark, colour | quiet | slow |
| `halftone-screen` | Halftone screen | Dither | hero, band | light, dark, colour | quiet | slow |
| `line-engraving` | Line engraving | Dither | hero, card, band | light, dark, colour | quiet | still |
| `aurora-curtains` | Aurora curtains | Mesh | hero, band, footer | dark, colour | focal | slow |
| `gradient-mesh` | Gradient mesh | Mesh | hero, card, band | light, dark, colour | quiet | slow |
| `painterly-landscape` | Painterly landscape | Mesh | hero, card | light, dark, colour | quiet | slow |
| `god-rays` | God rays | Light | hero, band | dark, colour | focal | slow |
| `orb-sphere` | Light orb | Light | hero, card, band | light, dark, colour | focal | slow |
| `prism-dispersion` | Prism light | Light | hero, card, band | dark | focal | slow |
| `soft-light-bars` | Soft light bars | Light | hero, card, band, footer | light, dark, colour | focal | slow |
| `spotlight-cone` | Stage spotlight | Light | hero, card | dark, colour | focal | slow |
| `caustics` | Water caustics | Light | hero, card, band | light, dark, colour | focal | slow |
| `edge-glow` | Edge glow (named only) | Light | card | light, dark, colour | border | slow |
| `dot-terrain` | Dot terrain | Pattern | hero, card, band | light, dark, colour | quiet | slow |
| `grid-pulse` | Grid pulse | Pattern | hero, card, band | light, dark, colour | quiet | slow |
| `ruled-grounds` | Ruled dot ground | Pattern | card, band | light, dark, colour | quiet | slow |
| `contour-lines` | Topographic contours | Pattern | hero, card, band, footer | light, dark, colour | quiet | slow |
| `dotted-globe` | Dotted globe (named only) | Pattern | hero, card, band | light, dark, colour | focal | slow |
| `ridgeline` | Ridgeline (named only) | Pattern | band | light, dark, colour | focal | slow |
| `fluted-glass` | Fluted glass | Material | hero, card, band | light, dark, colour | quiet | slow |
| `silk-folds` | Silk folds | Material | hero, card, band | light, dark, colour | quiet | slow |
| `duotone-grade` | Duotone grade (named only) | Photo | hero, card, band | light, dark, colour | quiet | still |

Each effect's one-line description is the `look` field in `index.json`. `node scripts/effects.mjs list`
prints this table, and you can filter it with `--family`, `--on`, `--palette`, `--motion` and
`--quiet`. A filter value that does not exist is an error, not an empty list.

Retired on 31 Oct because they looked bad or cheap: `riso-print`, `ink-bloom`, `liquid-chrome`,
`metaballs`, `brushed-metal` and `paper-texture`, then `terrazzo-speckle` (a kitchen floor),
`marble-warp` (zebra stripes), `pixel-mosaic` (broken JPEG blocks), `truchet-arcs` (thick grey
worms) and `soft-particles` (stock bokeh). They are not in the
index. `ridgeline` reads as a record cover when dealt on its own, so it is named only.

## Commands

```bash
node scripts/effects.mjs index      # rebuild index.json from every <id>/meta.json and effect.js
node scripts/effects.mjs gallery    # write gallery.html and lab.html from scripts/*.template.html
node scripts/effects.mjs publish    # the gallery as one folder: publish/index.html, effects/, ui/, files.json
```

Edit the templates in `scripts/`, not `gallery.html` or `lab.html`. `publish` rebuilds both pages,
then copies only the files the gallery loads. `files.json` lists them, all at relative paths.

## Adding an effect

A folder `<id>/` with two files:

- `meta.json`: `id`, `name`, `family` (grain, dither, mesh, light, pattern, material or photo),
  `look` (one sentence), `bestOn`, `palettes`, `motion` (`still`, `slow` or `interactive`) and `cost`.
  Optional: `"random": false` for a literal subject that is only named, never dealt; `"focal": true`
  for a ground with its own subject; `avoidWith` (ids that never share its page); `subjects` (what a
  named effect is for).
- `effect.js`: `export default { id, name, family, params, mount(el, { palette, params, seed }) }`.
  `mount` returns `{ destroy, pause, resume }`.
  - For a fragment shader, use `fx.shader(el, { frag, schema, params, palette, seed, fallback })`. It
    handles the canvas, the lifecycle, the DPR cap, the context budget and the CSS fallback.
  - For canvas 2D, use `fx.lifecycle(el, { draw })`.
  - An effect that makes its own WebGL context calls `fx.glBudget(holder)` just before, so the
    context counts in the page's budget (see `dotted-globe`).

Every colour comes from the palette, mixed in OKLab (`fx.color`). Never use a fixed hue, and never
default to violet or lavender. Text on an effect must read at 4.5:1. Keep shader code small enough to
compile fast: the D3D compiler behind Chrome on Windows inlines every function call. A helper called
16 times took 40 s to compile. Loops counted by a uniform avoid that (see `halftone-screen`). Run
`index`, then check the effect in the gallery in light, dark and colour.



---

## `assets/objects/_print-core/README.md`

# Objects (`assets/objects/print-*`)

Everyday things modelled in 3D in code: a cup and saucer, a bicycle wheel, a desk lamp, a desk globe,
playing cards. Each one is shown as a **render** (the default: a studio render in its own materials,
the page's accent on one part, soft shadows and the reflections of a softbox) or as a **print** of
that render (halftone, engraving, dither or type). It turns slowly, leans toward the pointer and
takes one small step on a click (the lamp switches on, the cards fan out).

**Where it goes**
- **A product page without photographs**: the object of the product's own kind is the product's
  picture: the hero (`hero` preset, or `tile` in a hero split) and the statement's picture, as a
  render. A desk lamp for a lamp maker, a cup for a tableware maker, a wheel for a maker of wheels.
  Never an object of another kind: a wheel does not show a whole bicycle, a cup does not show a
  coffee machine. No object of its kind: compose the product itself from a spec of its parts
  with `../product-render` (its README), never `hero-product` without the product's picture.
- **A software, tech or games page**: the one moment on a feature card or a wide frame, about the
  thing the card says (a globe for regions, cards for a games feature). Here a print fits.
- **Not on a place page** (a cafe, a shop, a hotel, a studio people visit) and not beside the
  client's own photographs: those lead with photographs.
- Prints (halftone, engraving, dither, type) only on software, tech, AI and games pages. A product
  page shows the render.
- No caption under it, and no words calling it a render, a drawing, an illustration, a model, a
  sample or a stand-in. The section's heading and text say what the product is. Leave
  `aria-label` alone or name the thing plainly ("A desk lamp, switched on").

| id | the render | prints | click |
|---|---|---|---|
| `print-cup` | porcelain cup of coffee on its saucer, the glaze in the accent | halftone, engraving | rings run across the coffee |
| `print-wheel` | road wheel: tan-wall tyre, alloy rim, 24 spokes, hub in the accent | halftone (spokes as solid lines) | it spins up |
| `print-lamp` | balanced-arm desk lamp: stepped base, paired rods, chrome springs, a domed shade; base and shade enamelled in the accent | halftone | it switches on |
| `print-globe` | desk globe, real coastlines, brass meridian, walnut stand | engraving | it spins |
| `print-cards` | playing cards, the ace of diamonds face up, backs in the accent | halftone | the cards fan out |

`index.json` lists them; each folder's `meta.json` has the object's own notes, and `demo.html` shows
it full screen with switches for the picture and the paper.

## Put one on a page

```html
<!-- a split section's visual (references/sections-library.md): whole, standing low -->
<div class="frame frame--square">
  <div data-print="print-lamp" data-print-place="tile"></div>
</div>

<!-- a feature card: large, cut by the panel's bottom-left edge -->
<article class="card card--row">
  <h3>Regions</h3>
  <p>Pick where your data lives: 14 regions on four continents.</p>
  <div class="panel" data-fx="grain-gradient" data-fx-params='{"speed":0,"grainMotion":0}'>
    <div data-print="print-globe" data-print-params='{"effect":"engrave"}'></div>
  </div>
</article>

<!-- once, after system.js -->
<script type="module" src="assets/objects/_print-core/auto.js"></script>
```

- `auto.js` mounts every `[data-print]`. The host is an empty `div`; in a `.panel`,
  `.panel__screen` or `.frame` it fills it and draws over the panel's ground.
- **Where it sits** (`data-print-place`, or picked from the box it is in):
  - `card` in a `.panel`: large, cut by the bottom-left edge, as on x.ai's and Figma's feature
    cards; the bottom-right corner stays clear for the pause button. In a panel about as tall as wide
    (a card on a phone) it is cut less, so the thing still reads. The card's text sits above the
    panel, never over the object.
  - `tile` in a `.panel--top` or a square frame: whole, standing low.
  - `hero` in a wide `.frame`: large, right of centre, the text in the clear left half. In a frame
    about as tall as wide (a phone) it sits smaller and low, under the text.
  - `none`: centred on its own paper.
- **Options**: `data-print-params='{"angle":-20}'` over the preset (every param is in `meta.json`);
  a print: `data-print-params='{"effect":"halftone"}'`. `data-print-palette='{"bg":..,"ink":..,"accent":..}'`.
- **Colours**: on a dealt ground it draws on that ground's paper with an ink that reads on it and the
  page's accent; elsewhere in the page tokens (`--bg`, `--surface`, `--ink`, `--accent`). The accent
  goes on one part (the glaze, the hub, the shade and base, the card backs; the globe's sea when the
  accent is a blue or teal).
  Until that ground has drawn (it bakes one panel at a time, slowly on a CPU renderer, and a bake can
  fail), the object lays the ground's paper under itself, flat, and gives it back when the ground
  draws (`data-print-paper` is `own` or `ground`), so a print for dark paper never stands on a pale,
  undrawn panel. `blank-ground.html` tests it (`data-ready` is `pass` or `fail`).
- **One loop per group**: one object per card group turns by itself (the first, or the one with
  `data-print-loop`); the others hold still until the pointer reaches their card. A turning object
  puts its own round pause button in the panel's bottom-right corner once it has drawn (never on a
  poster): keep that corner clear.
- **Script**: `import obj from '<assets>/objects/print-cup/object.js'; const ctrl = obj.mount(el,
  { place: 'card', params: {...}, palette: {...} })`. The controller has `pause()`, `resume()`,
  `step(on)`, `set(params)`, `setPalette(p | null)`, `destroy()`. `auto.js` exports `prints`, a Map
  from element to controller; on a theme change call `setPalette(null)` on each.

## Do and don't

- One object per card group, at most two in view, and never over a moving ground: the ground holds
  still (`"speed":0,"grainMotion":0`). On a product page a plain lit ground or the page's surface.
- The object is the picture. No UI fragment over it, no second effect beside it.
- Never centred dead in a card panel with even ground all round: use the presets.
- Never animated by scroll. It moves only by its own slow turn, the pointer and a click.
- The client's own photographs and screenshots come first; an object never takes their place.

## It always shows a picture

- A **poster** shows at once: the object drawn ahead of time (`fallback-render.png`, or
  `fallback.png` for a print), in the page's palette, where the live picture will be. The live
  picture fades in over it.
- Every shader source is checked for words a laptop's GPU rejects before it is compiled
  (`glslProblems` in `print3d.js`: GLSL ES reserved words, a qualifier such as `flat` used as a
  name, names of built-in functions, double underscores). CPU-rendered Chrome compiles some of
  these, so a screenshot never proves a shader builds on a real GPU. Run
  `node assets/objects/_print-core/lint-glsl.mjs` after changing a model (exit 1 on a problem).
- A shader that fails the check, fails to compile or link, no WebGL2, a lost context, or a first
  frame that comes out empty: the poster stays, never an empty ground. Tests force each case with
  `window.__printBreak = 'compile' | 'link' | 'reserved' | 'empty'` before the object mounts, or
  `?fallback=1` on a demo page (no WebGL2).

## Light on a laptop GPU

- All objects of a page share **2 live WebGL contexts** (`config.maxLive` in `print3d.js`), so a page
  with its baked grounds and one other effect stays within 3.
- An object holds a context only while something on it moves near the screen (its turn, the
  pointer, a step). A still object draws once, keeps that frame as a plain picture and frees its
  context; it takes one again when the pointer comes onto its card. Off screen (beyond 40% of a
  screen) or in a hidden tab its context is freed.
- The raymarch runs at most 1 texel per CSS pixel (0.75 x 0.75 once the frame passes about 0.48
  megapixels); dither runs 1 texel per cell and its canvas holds one pixel per cell, scaled up
  crisp; no canvas passes about 1.5 megapixels. Slow frames lower the texels, then the march steps,
  then stop the turn.
- A render at rest (an object that does not turn, the frame kept when its context is freed, a
  reduced-motion frame) is drawn once more at up to one texel per canvas pixel (`config.fineTexels`,
  1.2 megatexels), so the picture that stays on the page is sharp. One frame, never a loop.
- Under `prefers-reduced-motion`: one still frame, kept as a picture, and the context freed at once
  (none held at rest); no hover, no pause button; a click shows the step at once.

## Posters

`make-fallbacks.html` makes every object's posters (open `?ids=print-cup` for one): `fallback.png`
and `fallback-dark.png` are print plates (red ink, green accent, blue the silhouette);
`fallback-render.png` and `fallback-render-dark.png` are twice as wide: the plates on the left (red
the floor's shadow, green the accent part, blue the coverage) and the render in colour on the right,
its accent part in a neutral grey that the page's accent replaces. An object whose picture depends on
the palette lists extra plates (`plates`) and picks them with `poster(palette, dark, render)`: the
globe has `-sea` posters for a blue accent. Make them again after every change to a model.

## A new object

`definePrint({ id, name, label, press, base: import.meta.url, glsl, pivot, radius, extent, camera,
turn, step, params, place, update, texture, poster, plates, posterPrint })` in `<id>/object.js`,
where `glsl` defines `vec2 map(vec3 p)` (distance, material id; y up, the floor at y = 0) and
`void surf(float id, vec3 p, vec3 n, inout Surf s)`, which sets the print's tone (`albedo`, `gloss`,
`wire`, `lo`, `hi`) and, when `u_render > 0.5`, the render's material (`col` in linear colour,
`metal`, `gloss`, `shine`, `accent`). The header of `print3d.js` lists the rest. Model it as the
real thing (proportions, parts, materials) so the render reads as a product shot, not a drawing;
run the lint, make its posters, and check it at 1440, 820 and 390 on light and dark paper. If it
still looks cheap after two honest tries, drop it.



---

## `assets/objects/_scenes/README.md`

# Scene objects (`assets/objects/<id>`, runtime in `_scenes`)

Real things shown through a print effect, alive under the pointer. Four of them take the client's
own photographs (`src`); one models a generic thing in code. Each is the picture of one card or one
hero frame: still or nearly still at rest, and it moves under the pointer, never on scroll.

| id | what it shows | moves by itself | hover / touch |
|---|---|---|---|
| `split-reveal` | one photograph, half printed as a halftone, a line between | no | the line follows the pointer; drag on touch; a slider for the keyboard |
| `dither-sequence` | 2 to 6 photographs that belong together, dithered, cut one to the next | yes: holds, then wipes (pause disc) | the pointer scrubs the frames; drag on touch |
| `dot-object` | one object cut out of its photograph and set in dots | no | under the pointer the dots take the photograph's real colour, like a loupe |
| `exploded-layers` | one photograph (or up to four) as four printed sheets in perspective | no | the sheets open apart; with `names` each gets a label; tap on touch |
| `product-turntable` | a generic camera, chair, speaker or cup on a turntable, dithered | yes: one step every 1.7 s (pause disc) | moving across turns it step by step; drag on touch |

`index.json` lists them; each folder's `meta.json` has every param (and its `for` and `never`), and
`demo.html` (served, not from disk) shows the object in a hero and two cards with a palette switch.

## Where they go: software pages only

**A scene is a print (halftone, dither, dots) and prints belong to software, tech, AI, developer
tool and games pages**, as their one moment: a hero frame or one feature card. House rule: effects
fit tech or gaming sites, a local coffee shop never.

- **Place, service and local-business pages** (a cafe, a bar, a shop, a hotel, a clinic, a studio
  people visit): no scene. Their photographs show plain, never printed as a halftone, a dither or
  dots (`references/photos.md`).
- **Product pages** (a maker of bikes, furniture, lamps, devices): no scene. The product's own
  photographs show plain; without photographs its object render (`assets/objects/print-*`,
  `_print-core/README.md`), never a scene and never stock of something else.
- **On a software page**, a scene shows a real thing the product works on or with:
  - `split-reveal`, `exploded-layers`: a photograph a photo, design or print tool works on, the
    device a tech company makes, a game's key art. `exploded-layers` labels only with `names` in the
    client's words (the layers its software works on); without names it opens without labels, and
    never names the sheets after the techniques (halftone, dither).
  - `dither-sequence`: two to six photographs that belong together (a device from several sides,
    the stages of what the software makes, a game's scenes), never a random or mood set.
  - `dot-object`: only an object shot on a seamless plain ground (lighter or darker than the object,
    or another colour), or a cut-out PNG with a clear ground. A busy or sunlit background does not
    cut out: use `split-reveal` instead.
  - `product-turntable` draws a generic thing, never the client's product: a card about a kind of
    thing the software handles (cameras in a rental platform's inventory, a chair in a furniture
    marketplace, a speaker an audio app controls).
- One scene per screen, at most two on a page, and the page's other WebGL counted with them.
- No caption under a scene that explains it or apologises for it ("made in code", "a print of",
  "a stand-in"); the card's heading and text say what the thing is.
- The demo photographs are test pictures. Never ship them as the client's.

## Put one on a page

```html
<article class="card">
  <h3>Every edit on its own layer</h3>
  <p>Turn any adjustment off later without touching the rest.</p>
  <div class="panel">
    <div data-scene="exploded-layers" data-scene-src="assets/img/sample-edit.jpg"
         data-scene-params='{"names":["Photo","Colour","Shade","Masks"]}'
         aria-label="A portrait taken apart into its four edit layers"></div>
  </div>
</article>
<!-- once, after system.js -->
<script type="module" src="assets/objects/_scenes/auto.js"></script>
```

One per object, copy and change the `src` and the words:

```html
<div data-scene="split-reveal" data-scene-src='{"src":"assets/img/raw-scan.jpg","alt":"A scanned print, half of it screened","focus":[0.5,0.4]}' data-scene-params='{"split":0.6}'></div>
<div data-scene="dither-sequence" data-scene-src='[{"src":"assets/img/a.jpg","alt":"Front"},{"src":"assets/img/b.jpg","alt":"Side"},{"src":"assets/img/c.jpg","alt":"Back"}]'></div>
<div data-scene="dot-object" data-scene-src="assets/img/sensor-on-white.jpg" aria-label="The sensor the app reads"></div>
<div data-scene="exploded-layers" data-scene-src="assets/img/map-tile.png" data-scene-params='{"names":["Imagery","Roads","Labels","Terrain"]}'></div>
<div data-scene="product-turntable" data-scene-params='{"form":"chair"}' aria-label="A side chair from the catalogue"></div>
```

- The host is an empty `div`. In a `.panel`, `.panel__screen` or `.frame` it fills the box (give
  the box its size: an aspect ratio or a height); elsewhere give it a size yourself.
- `data-scene-src`: a page-relative path or URL, or JSON: `{ src, alt, focus: [x, y], by, page,
  licence, licenceUrl }`, or an array of them. Serve photographs from the site itself (a host that
  sends no CORS headers cannot be printed: the plain photograph shows instead).
- `data-scene-params`: JSON, every param in `meta.json`. `data-scene-palette`: JSON `{ bg, ink,
  muted, accent }`. `aria-label`: what the picture shows (else the photograph's alt).
- **Colours**: without a palette the scene prints in the page tokens (`--bg`, `--surface`, `--ink`,
  `--muted`, `--accent`) on the ground of the box it sits in (a `.panel` on `--surface` prints on
  `--surface`; a dark band prints in a light ink). It paints its own ground: put it in a plain
  panel, never over a dealt effect ground.
- **One moving scene per group**: in a section (or a `[data-scene-group]`) only the first
  `product-turntable` or `dither-sequence` moves by itself, or the one with `data-scene-loop`; the
  others hold still until the pointer reaches them. A moving scene puts the shared 32 px pause disc
  (`.loop-pause`) in the box's bottom-right corner: keep that corner clear.
- Text goes above or beside the panel, never over the scene. No caption that explains the effect,
  no chips; the photograph's credit goes in the page's one credit line.
- **Credits**: `import { credits } from 'assets/objects/_scenes/kit.js'`; `credits([entry, ...])`
  returns the footer's one line of small print for every photograph the scenes print, each named
  once ("Photographs: A on Unsplash, adapted; B, CC BY-SA 4.0, via Wikimedia Commons, adapted.").
  Never a credit under the picture, never a line per photograph. The client's own photographs need
  none.
- **Script**: `import obj from 'assets/objects/split-reveal/object.js'; const ctrl = obj.mount(el,
  { src, params, palette })`. The controller has `pause()`, `resume()`, `setPalette(p | null)`,
  `destroy()` and `ready` (a promise, once the photographs are in). `auto.js` exports `scenes`, a Map
  from element to controller; after a theme change call `setPalette(null)` on each.

## Behaviour

- **Still at rest**: `split-reveal`, `dot-object` and `exploded-layers` draw once and again only
  while the pointer moves them. `product-turntable` and `dither-sequence` draw only while they step
  or wipe (30 frames a second at most) and nothing while they hold.
- **Never on scroll**: nothing animates as it comes on screen; it is drawn finished.
- **Reduced motion**: one still frame, no pause disc; the pointer still moves the line, the frame,
  the loupe and the turntable, at once.
- **No WebGL, a shader that fails, or a photograph that fails**: the plain photograph
  (cover-cropped at its focus) takes the panel and the overlays go; the turntable shows a still of
  its form (`fallback-<form>-light|dark.png`, made by `make-fallbacks.html`). A sequence leaves a
  failed photograph out of the loop. The panel never stays empty: the still also goes in when a
  shader breaks a rule of GLSL ES 1.00 or 3.00 (`glslLint` in `kit.js` reads every shader before it
  is compiled), fails to compile or link, a frame throws, or the first frame comes out one flat
  colour. Only a photograph that cannot load at all (its host down or blocked) leaves the panel's
  own ground: the host gets `data-scene-empty` and the console an error. Serve the photographs from
  the site itself.
- **Shaders**: the test Chromes render WebGL on the CPU (SwiftShader), which compiles words a
  laptop's GPU rejects (a struct field named `flat` once left a hero empty). After changing a
  shader run `node assets/objects/_scenes/lint-glsl.mjs`: it checks every scene shader as compiled
  and exits 1 on a reserved word, a keyword or type used as a name or field, a double underscore, an
  unknown `gl_` name, or a name that hides a built-in function.

## Light on a laptop GPU

- Each scene has one canvas and one WebGL context, paused off screen and with the tab hidden, and
  freed 1.5 s after it leaves the screen; it is made again before it returns.
- At most 2 scene contexts live at once (`config.live` in `kit.js`), a hard cap: off-screen ones
  give theirs up first, then idle ones, then still ones (each keeps its last frame as a picture).
  Count them with the page's grounds and other effects: keep a page to 4 live contexts.
- A smooth canvas renders at most 1 canvas px per CSS px (0.75 in a frame over 1 MP for the
  layers) and never over 1.5 MP; a dithered one holds one canvas px per dither cell. No MSAA.
  Dots and layers draw from static buffers; nothing runs per frame on the CPU.



---

## `assets/objects/photo-kit/README.md`

# Photo prints

A photograph printed whole by a shader in the page's ink on its own sheet: a halftone, an engraving
or a dither. Hover (a tap on a phone) shows the photograph itself under the print. A print is one
crafted moment on a page, never the way a page shows its photographs.

| Object | Looks like | Hover |
|---|---|---|
| `photo-halftone` | a one-ink halftone: round dots on a 45° screen, clean paper in the light, solid ink in the deepest shadow | a loupe (round lens, hairline rim, soft shadow) shows the photograph in its own colours |
| `photo-engraving` | an engraved plate: diagonal lines that swell in shadow and bend over the forms, over a light wash of the photograph's colour | the lines part around the cursor and the photograph shows through |
| `photo-dither` | a three-colour grain: the photograph's deepest and most colourful colours on the paper | the photograph develops through the grain in a soft circle |

Each folder's `demo.html` (served over http) shows it in the light, dark and colour palettes.
`meta.json` lists its params, touch behaviour, fallback and cost.

## Where a print goes, and where not

- **Yes:** one moment on a software, AI, design-tool or gaming page: the page's one photograph band,
  or a feature tile whose subject is the photograph (an imaging or design tool printing a picture,
  `tint: 1` for the brand's ink). One print per page; a row of three only on a page about prints.
- **Never** over the hero photograph or a section's main photograph (`references/photos.md`): a
  print there reads as broken or low-resolution. Never on a café, guesthouse, shop or other local
  business page: those show their photographs plain.
- **Never** a caption under it that explains the effect, and no note that it is a print.

## The photograph

The client's own photograph first. Else one from the vetted library that prints well (one clear
subject, a plain ground, clear light):

```bash
node <skill>/scripts/photos.mjs list --trade office --json     # entries with "prints": true
node <skill>/scripts/photos.mjs fetch <id> --out .             # the files, credits.json and the <img>
```

On a dark page pick a darker photograph (`"tone": "dark"` or `"mid"`): a pale one prints as a large
light plate there.

## Mount

Paste the `<img>` that `photos.mjs fetch` prints into the frame. The print reads that picture (the
largest `srcset` size), keeps its `alt`, and takes its `object-position` as the subject's place.

```html
<div class="print-frame" style="aspect-ratio: 4 / 5; border-radius: var(--radius-card)">
  <img src="assets/img/photo-d88.jpg" srcset="..." sizes="(max-width: 1023px) 100vw, 50vw"
       width="1280" height="1757" alt="Cream ceramic table lamp in low sun" loading="lazy" decoding="async"
       style="object-position: 50% 40%">
</div>
<script type="module">
  import fx from './assets/effects/fx.js';
  import halftone from './assets/objects/photo-halftone/object.js';
  const el = document.querySelector('.print-frame');
  halftone.mount(el, { palette: fx.readPalette(el) });
</script>
```

- The frame needs a size (an `aspect-ratio` or a height). The print fills it, prints on the page's
  `--surface` so the frame reads as a sheet (`ground: 0` prints on `--bg`), and follows the page's
  palette (`ctrl.setPalette(fx.readPalette(el))` after a palette switch).
- `focusX`/`focusY` (0..1) override the `<img>`'s `object-position`.
- The print is there from its first frame: no entry, no dissolve, nothing moves at rest.
- A small UI card may sit on a corner of the frame (`cards.md`), never over the subject; never text
  over the print.

## Credit

Credits go in the footer's one credits line, never under the print. A printed photograph counts as
adapted:

```bash
node <skill>/scripts/photos.mjs credits --out . --adapted <id>
```

For a photograph that did not come through `photos.mjs`, `creditsBlock(entries, { adapted: [id] })`
in `photo.js` writes the same footer block from `{ id, by, page, licence, licenceUrl, source }` (one
line, "Photographs via ...", that opens the list). The client's own photograph needs none.

## When it cannot draw

Before the first frame, while the canvas is released off screen, and whenever WebGL is missing, the
shader fails to compile or link, or the photograph's host sends no CORS headers, the photograph
itself shows, greyed into the palette: a still picture, never an empty frame. The runtime also refuses
a shader that uses a GLSL ES reserved word (`flat`, `smooth`, `sample`, `filter`, `input`...) and shows
the still, because a laptop's GPU rejects what CPU WebGL (SwiftShader) compiles. `glslLint(src)` and
`photoShader(object)` in `photo.js` check a shader from Node.

## Cost

One canvas and one WebGL context per print, paused off screen and with the tab hidden, released 1.5 s
after it leaves the screen. At most 3 prints hold a context; a fourth waits (showing its still) until
one leaves, and a frame scrolling away gives way to one coming in. Count them with the page's other
WebGL effects (keep a page to 3 live contexts). The halftone and engraving render up to 2 canvas px
per CSS px so dots and lines stay sharp; every print stays under 1.5 MP of canvas. Each pixel reads
the photograph 2 to 5 times from its mipmaps; no loops.



---

## `assets/objects/product-render/README.md`

# Product render (`assets/objects/product-render`)

A studio render of **any physical product**, composed from a short JSON spec: a list of parts with
sizes and positions in the product's own units. `build.js` turns the spec into a model and
`_print-core/print3d.js` renders it: real materials (painted metal, alloy, chrome, rubber, wood,
fabric, leather, plastic, a light), soft studio light with soft shadows, a softbox in glossy parts, a
floor shadow, the page's accent on the parts that ask for it. It sways slowly as a turntable, or holds
still; a lamp switches on and off on a click; a robot's joints move.

Use it for a **product without photographs**: the render is the product's picture, in the hero and
the statement. Never for a product that has photographs, never on a place page, never captioned,
never a product of another kind. One product render a page.

## Mount: the product at anchor scale

```html
<div class="frame" id="bike" data-product="assets/objects/product-render/specs/my-bike.json"
     data-product-place="stage" data-product-view="side" data-product-color="blue"></div>
<script type="module" src="assets/objects/product-render/auto.js"></script>
```

The frame is the picture: the product's own bounds fill a share of it (the tighter way, width or height)
and it stands on the page's ground with its floor shadow, transparent round it: **no panel, no grey box**.
Give the frame its size (a hero column as tall as the screen, a full-width stage, a tile); the product
fills it.

| attribute | |
|---|---|
| `data-product-place` | `hero` 0.88, `stage` 0.86, `tile` 0.84, `card` 0.9 of the frame (`legacy`: the old turntable right of the words) |
| `data-product-view` | `three-quarter` (default), then only the views the spec lists in `supports` (`side`, `front`, `top`, a close-up of its own such as `detail-saddle`); `product.views` lists them; any other (the bike's `top`) throws and the frame carries `data-product-error`; or `detail:<part name>` |
| `data-product-scene` | a scene of the spec: the product loaded or in use (`loaded`, `desk`, `work`) |
| `data-product-color` | a colourway id of the spec (`spec.colors`); default its first |
| `data-product-mode` | `auto` (default): the still make-posters made, else the turn, else one frame rendered here; `image`, `still`, `live` force one |
| `data-product-fill` | 0.3-1.2, over the place's share |
| `data-product-params` | `{"turn":1}` asks for the live turn; `{"x":0.1,"y":-0.05}` moves it; `{"step":0}` a lamp off |
| `data-product-palette` | `{ bg, surface, ink, accent }`; else the page's tokens `--bg`, `--ink`, `--accent` |

**Each section a different view.** A product page shows the product big, whole in three sections at most, and never the
same view twice: the widest view in the hero (a bike's `side`; a lamp's or an arm's `three-quarter`), another angle by the specs, a close-up on the part a section
talks about, the loaded scene where the copy promises what it carries. Every promise in a headline is
shown in a picture (a child seat with its belts, the crates, a lamp's light on the desk).

**A close-up** (`detail-*`, `detail:<part>`) frames the named parts and centres them on the frame (their box, `focus`
in the manifest, fills the place's share); the rest of the product runs off the frame's edges (the frame clips it),
never a hard cut inside it. So that holds in a wide tile too, a close-up's shot is made wide enough (`cover`, default 2:
a frame up to twice as wide as tall, 1 : 1.25 tall) with the product running on past the parts as far as it goes, and its
still is cropped evenly round the parts' centre, never to the product's own box.

**Colour from an order card.** A swatch drives the frames it names, no script needed:

```html
<button type="button" data-product-swatch="#bike, #bike-loaded" value="red" aria-pressed="false">Signal red</button>
<input type="radio" name="colour" value="red" data-product-swatch="#bike">
```

On click (a button: `aria-pressed` is kept, one pressed per group) or change (an input), the named frames
(default: every frame whose spec has that colourway) set `data-product-color` and swap to that colour's
still. Setting `data-product-color`, `-view` or `-scene` on a mounted frame does the same, and so does
an event: `el.dispatchEvent(new CustomEvent('product:set', { detail: { color: 'red', view: 'side' } }))`,
or on `document` with `detail.target` a selector.

**What a frame tells** (for checkers and tests): `data-product-mode`, `data-product-state` (`image` |
`still` | `live` | `poster`), `data-product-view`, `data-product-color-shown`; the picture is
`img.product-render__img`; `window.__tpProduct` = `{ stills, images, live, freed }`. In `image` mode
the page holds no canvas and no WebGL context; a `still` renders once, keeps an `<img>`, frees its
context and removes its canvases; only `live` keeps a context (and counts in `window.__tpGl`). A
product page uses the stills (the default once make-posters has run). A `still` is measured (its opaque pixels, and a
close-up's parts) and placed by the same layout as a poster still, so it fills its place's share exactly (tile .84) and is centred.

Script: `import { loadProduct } from '.../product-render/build.js'; const p = await loadProduct(url);
const ctrl = p.mount(el, { place: 'stage', view: 'side', scene, color, mode });` The controller:
`setColor(id)`, `setView(v)`, `setScene(s)`, `ready()`, `pause()`, `resume()`, `step(on)`,
`set(params)`, `setPalette(p | null)`, `destroy()`. `auto.js` exports `products` (frame to controller)
and `ready`. `views.html` beside this file is the worked example (every view, a scene per spec, two
colour switches, one `still` mount).

## Stills and posters: run this after every change to a spec

```
node assets/objects/product-render/make-posters.mjs path/to/spec.json --profile <own chrome dir> [--port 5905]
     [--variants side,detail-saddle,three-quarter+loaded] [--grounds light,dark] [--px 1100] [--timeout 9] [--quiet] [--legacy]
node assets/objects/product-render/make-posters.mjs --check path/to/spec.json      (spec, views, scenes and shaders only)
```

It checks the spec (unknown parts, props or materials, a part a view or scene names that is not there,
too many parts, shader words a laptop GPU rejects), then renders in a headless, software-rendered Chrome
(its own profile, closed by its own PID, never port 3000) every variant in `spec.make.variants`
(`view` or `view+scene`) on each ground in `spec.make.grounds`, and writes beside the spec:
`stills/<id>-<variant>-<colour>[-dark].webp` and `-half.webp` (one still per colourway, transparent,
cropped to the product and its shadow), `<id>-<variant>.fallback-render[-dark].png` (the live render's
poster) and `<id>.stills.json` (what was made, where the product and a close-up's framed parts sit, and
which sides a close-up cuts). A colourway costs no render: the accent part is lit again in each colour.
Each variant is written as soon as it is made; a CPU takes one to four minutes a variant for 60-90
parts, so pass `--variants` a few at a time. `--legacy` also writes the turntable's four posters. A view
with no still renders itself once on the page (`still` mode) and frees its context.

## The spec

```json
{
  "id": "city-bike", "name": "City bicycle", "label": "A city bicycle with a front basket",
  "units": "m", "angle": -34, "turn": { "mode": "sway", "amp": 22, "period": 24 },
  "materials": { "frame": { "kind": "paint", "color": "accent", "finish": "gloss" } },
  "parts": [
    { "type": "wheel", "at": [-0.53, 0.35, 0], "r": 0.35, "spokes": 36, "wall": "#c7a57a" },
    { "type": "tube", "from": [-0.07, 0.29, 0], "to": [-0.23, 0.81, 0], "r": 0.017, "mat": "frame", "blend": 0.01 }
  ]
}
```

Axes: **x forward** (the product's front), **y up**, **z across** (toward the viewer at angle 0). Any
unit; the model is scaled so its largest side is one unit and set on the floor at its lowest point.
Model the product from its real measurements: proportions are most of what makes it read as a render.

| key | what |
|---|---|
| `id`, `name`, `label` | the label is what a screen reader hears ("A desk lamp, switched on") |
| `poster` | the posters' file name (default the id) |
| `angle` | its turn at rest and in the still, degrees (default -32: a three-quarter view) |
| `turn` | `{ "mode": "sway", "amp": 26, "period": 22 }` (default), `{ "mode": "spin", "speed": 10 }`, `{ "mode": "still" }` |
| `camera` | `{ "elev": 12 }` degrees above the floor |
| `click` | `"light"`: a click switches every `light` material (and `glow`) on and off; it starts on |
| `pool` | `{ "at": [x, 0, z], "r": 0.2 }`: the light it throws on the floor while on |
| `materials` | named materials for the parts |
| `motion` | moving groups (joints), below |
| `colors` | colourways: `[{ "id": "blue", "name": "Deep blue", "accent": "#2c4f7c" }]` (the accent parts take it; `materials` swaps materials too, at a render each) |
| `views` | close-ups and own views: `{ "detail-saddle": { "part": ["saddle*", "seat post"], "angle": -42, "elev": 16, "margin": 1.3, "cover": 2 } }` (a name ending in `*` takes every part it begins; `cover` the widest frame the shot fills, 1 for the margin alone: a close-up render of 2-3 MP takes a CPU 2-9 minutes) |
| `scenes` | the product loaded or in use, below |
| `supports` | the views the product draws well, `["three-quarter", "side", "front", "detail-saddle"]`: only these are offered (`product.views`), made (`make.variants` outside it fails `--check`) and mounted; list a view only after looking at its still (a bike from above reads as lying on its side, so the city bike omits `top`). Keep `three-quarter` (the default view) |
| `make` | `{ "variants": ["three-quarter", "side", "detail-saddle", "three-quarter+loaded"], "grounds": ["light", "dark"], "px": 1100 }`: what make-posters makes |
| `parts` | the parts, below (keep it under about 90) |

### Parts

Every part takes `mat` (a material name or an inline material), `blend` (a fillet in units where it
meets the parts listed before it: welded tubes, a cast body), `in` (a motion group) and `name` (for you).
It is placed by `from` + `to` (a linear part runs between them; `up` turns its section), or by `at`
plus `axis` (`"x"`, `"y"`, `"z"` or a vector) and/or `rot` ([x, y, z] degrees).

| type | sizes | use |
|---|---|---|
| `tube` | `r`, `r2` (taper), `cap` `flat`/`round`, `round`, `seams` | frame tubes, posts, rods, handles, a tapered robot link |
| `beam` | `w`, `d` (section), `round`, `seams` | flat bars, cranks, rails |
| `box` | `size` [x, y, z], `round`, `seams` | housings, bodies, pedals, a gripper |
| `panel` | `size` (thin), rounder | plates, lids, a screen's back |
| `cylinder` / `disc` | `r`, `h`, `round`, `seams` | bases, hubs, motor housings, caps |
| `sphere`, `ellipsoid` | `r` / `size` | a bulb, a bell, a knob |
| `torus` | `R`, `r` | rings, a chainring, a status light |
| `joint` | `r`, `w`, `capMat` | a hinge: knuckle about `axis` (default z) with caps on both faces |
| `wheel` | `r`, `tyre` [width, height], `rim` [depth, width], `hub` [r, length], `spokes`, `spokeR`, `style` `spoked`/`disc`/`solid`, `wall` (sidewall colour), `rimMat`, `hubMat`, `spin` (deg/s) | bicycles, strollers, carts, casters; axle along `axis` (default z) |
| `shade` | `from` (closed end) `to` (open end), `r1`, `r2`, `t`, `bulge` 0..1, `innerMat` | lamp shades, bells, horns, a speaker cone |
| `seat` | `size` [length, height, width], `style` `saddle`/`cushion` | saddles, seats, cushions (local x forward) |
| `basket` | `size`, `style` `wire`/`slats`/`solid`, `pitch`, `wire`, `rimMat` | baskets, crates, bins, trays (open top) |
| `arc` | `R`, `a0`, `a1` (degrees), `r` or `size` [radial, axial] | mudguards, handles, bent frames, hoops |
| `spring` | `from`, `to`, `R`, `r`, `turns` | springs, coiled cords |
| `path` | `points` [[x,y,z]...], `r`, `smooth` (on with 3+ points) | handlebars, cables, bent tubes |

`seams`: panel lines cut round the part at heights along its length (-1..1 of its half length):
the seams of a robot's shell, a base's groove. `seamWidth`, `seamDepth` in units.

### Materials

A name from `materials`, a built-in name, or `{ "kind": ..., "color": "#hex" | "accent", "finish": "gloss" | "satin" | "matte" }`.

| kind | | built-in names |
|---|---|---|
| `paint` | enamel or powder coat; `color: "accent"` takes the page's accent | `accent`, `paint`, `white`, `black`, `graphite` |
| `metal` | brushed alloy | `alloy`, `aluminium` |
| `chrome` | polished | `chrome` |
| `steel` | dark stainless (spokes, wire) | `steel` |
| `rubber` | tyres, pads, grips | `rubber` |
| `plastic` | satin plastic | `plastic` |
| `wood` | oiled wood with rings; `grain` x/y/z, `scale` | `wood`, `oak`, `walnut` |
| `fabric` | a fine weave; `weave` | `fabric` |
| `leather` | | `leather` |
| `light` | gives light; with `click: "light"` it switches | `light` |

Any material takes `glow` (0..1): a lit inner face (a shade's inside when the lamp is on).

### Motion

```json
"motion": [
  { "id": "yaw", "pivot": [0, 0.14, 0], "axis": "y", "amp": 26, "period": 13 },
  { "id": "shoulder", "parent": "yaw", "pivot": [0, 0.32, 0], "axis": "z", "amp": 9, "period": 11, "phase": 0.2 }
]
```

A group turns its parts (`"in": "shoulder"`) about `pivot` and `axis` by `rest` + `amp` x a sine of
`period` seconds, after its parent. Pivots are given at rest, in the spec's units. Up to four groups.
The joints move only while the product turns: a still, a phone and reduced motion show the rest pose.

### Scenes and props: the product loaded or in use

```json
"scenes": {
  "loaded": { "label": "A city bicycle with a child seat on the rack, a crate of fruit and a pannier",
    "hide": ["basket"],
    "props": [ { "prop": "child-seat", "at": [-0.578, 0.796, 0] },
               { "prop": "crate", "at": [0.6, 0.76, 0], "size": [0.3, 0.2, 0.32], "contents": "fruit" },
               { "prop": "bag", "at": [-0.62, 0.42, 0.152], "hooks": true } ] },
  "desk": { "lit": { "at": [0.53, 0.11], "r": 0.19, "k": 3.6 }, "pool": null,
    "props": [ { "prop": "desk", "at": [0.2, -0.032, 0.02] }, { "prop": "book", "at": [0.3, 0, -0.15], "count": 2 } ] }
}
```

A scene adds props (and plain `parts`), hides parts by name, and may change `label`, `pool`, `click`
and `materials`. `lit` throws a lamp's warm pool of light on the props' upward faces. Props are made of
ordinary parts at the size of the real thing, standing on y = 0 and facing x, in metres (`scale`
converts: 1000 for a spec in millimetres); each takes `at`, `yaw`, `scale`, `size`, `color`,
`mats` { role: material }, `in` (a motion group: a parcel held in a gripper) and `name`.

| prop | what | options |
|---|---|---|
| `child-seat` | a rack seat: high back, wings, cushion, shoulder and lap belts to a red buckle, footrests | `color`; roles shell, pad, belt, buckle |
| `bench` | a padded bench for 1-3 children or passengers in a row (a cargo box): two belts and a buckle a seat | `seats`, `width`, `color`; roles frame, pad, belt, buckle |
| `crate` | a slatted wooden crate, open on top | `size`, `contents` fruit / bottles / loaves / parcels / none |
| `bag` | a pannier (flap, straps, handle, `hooks` for a rack) or `style: "tote"` | `size`, `color` |
| `parcel` | a cardboard box with tape and a label | `size`, `color` |
| `tray` | a low open bin with parcels standing in it | `size`, `parcels` 0-4 |
| `desk` | a tabletop | `size`, `color` |
| `book` | 1-3 stacked books | `count`, `colors` |
| `mug` | a mug of coffee | `r`, `h`, `color` |
| `sheet` | a sheet of paper | `size` |

Keep a scene under about 110 parts. Its props must read at the size the page shows them (belts,
buckles, a crate's slats, a bag's flap), and a scene goes where the copy promises it.

## Behaviour and limits

- **It always shows a picture**: the view's still (no WebGL); without one, the poster at once and the
  render over it, the poster staying when WebGL fails. Under `prefers-reduced-motion`, and on a phone (max-width 700px or a coarse pointer),
  one still frame, drawn sharp, and the context freed. A turning product has a pause button in its
  frame's bottom-right corner.
- **At most one live context** for a product: only the first product render mounted turns (when the
  page asks for the turn, or no still was made); a second holds still. The page's cap of 4 contexts
  (`window.__tpGl`) counts it.
- **Cost**: every part is evaluated per ray step, skipped when its bounding sphere is further than
  the nearest part so far. About 20 parts renders like a print object; 60-70 (a bicycle with its
  spokes) is fine on a laptop GPU and slow on a CPU renderer (posters: about 90 s). Keep under 90.
- **What it cannot do**: text or logos on the product, transparent glass, cloth that drapes, a
  freeform organic shell (a shoe, a face, a car body), anything thinner than about a texel (it is
  thickened). For those: the client's photographs or renders, never this.
- **Never** a product of another kind, never on a place page, never a caption under it.

The three specs in `specs/` (a city bicycle, a desk lamp, a robot arm) are worked examples, each with
its views, a scene and colourways (run `make-posters.mjs` on a spec to make its stills; until then each frame renders itself once): `views.html` shows them at anchor scale with colour switches
(`?only=bike|lamp|arm`, `?mode=still|live`); `demo.html` the turntable (`?turn=0`, `?fallback=1`).



---

## `references/backgrounds.md`

# Backgrounds

Better grounds come from fewer, better colours (house rule 6: "nicer backgrounds"), and on tech
from a small catalogue of grounds drawn in CSS. Every kind uses the three ground tokens; only tech
adds CSS grounds.

## The three tokens (every kind)

Section and panel grounds use `--g-main`, `--g-alt` and `--g-dark` only (system.css: the base,
`.ground-surface`, `.ground-inverse`): one to three colours down the page, footer included, in the
same order at 390. Photograph layers and the tech grounds below do not count among them.

- **`--g-main`:** white, or a tint of lightness 0.80 to 0.97 with low saturation (channel spread
  0.12 or less), taken from the client: a place's walls, paper or shopfront (warm off-white by
  default, `#F7F3EC`; white for a shop that sells mostly online), a product's photo backdrop, warm
  greys for a service, blue-leaning or cool grey for software. It covers 55% of the page's height or
  more (60% on software and product). Never pure-white panels on a cream page.
- **`--g-alt`:** the same hue (within 20 degrees), 0.06 to 0.15 darker, never under 0.70
  (`#ffffff` to `#f2f2ef`, `#f7f3ec` to `#ede6da`). Panels, tiles, cards and at most one full band.
- **`--g-dark`:** lightness 0.05 or less: near-black (`#111` to `#1a1a1a`) or the deepest shade of
  the brand hue, never charcoal, never violet. One dark body section at most (one screen tall), at
  the page's middle or later, never right under the hero; the footer may be dark. A dark page (main
  ground 0.02 or darker) and a dark hero are for tech only.
- **The brand band** (`.ground-brand`, product and place): one section in the brand's own colour
  (from the product or the shopfront) may replace the dark band, once, in the second half. On a
  place its lightness is 0.03 to 0.60 and its saturation 0.25 or more, never a neutral near-black;
  every word on it (heading, text, label, link) takes the colour that passes 7:1, the one number: darken the brand colour until it does (`check.mjs` and `consistency.mjs` ask 7:1 for text people read and 4.5:1 for labels, so 7:1 clears both); the primary button is inverted. Otherwise
  saturated colour lives in the accent and the pictures; one mid-tone section at most, never as the
  main ground.
- Grounds change in big blocks at the section edge: never on `.wrap` or a wrapper, no border-top or
  rule between sections, no band inside a section (a box of 80% of its width or more with its own
  ground holding the heading), no inset coloured box standing in for a ground. A frame holding a
  visual is fine.

## Other kinds stay flat

Product, service and place (site-kind other): every ground and panel is a flat CSS colour and
photographs are shown as they are. No gradient (a hard-stop two-tone included), grain, paper,
halo, texture, pattern, glass, contour, canvas, `backdrop-filter`, gradient mask, or shadow or tint
on the interface. Never run `pick.mjs` for them: its `index.json` still lists grounds for product,
service and place, and those are not used. A product page with site-kind tech is dealt as tech.

## Tech: the CSS grounds

Sixteen grounds drawn in CSS (no WebGL) in `assets/backgrounds`. Link `backgrounds.css` after
`system.css` and `cards.css`; load `backgrounds.js` plain at the end of `<head>`. One class on a
section or the hero's wrapper (`<section class="section bg-halo">`); `stage` only as `<div
class="bg-stage">` around one visual card; `paper` on `<body>` and `topglow` around the nav and hero
set no tokens, the thirteen section grounds set the page tokens so cards and buttons work unchanged.
Ink keeps 7:1 and muted 4.5:1 on every palette (`check.mjs` measures it). `index.json` holds each
ground's mood, roles, pairs, avoids and sections.

- **Soft:** `mist` colour wash; `halo` light behind a heading; `ruled` fine grid on the container's
  edges, clear behind the heading; `dots` dots in the margins; `arcs` rings rising, for the close;
  `liquid` a slow mesh of colour ellipses, the only ground that moves.
- **Hard:** `grain` tint with film grain; `dusk` one tone melting into the page; `band` the lit
  ground's second tone; `field` a grainy gradient (Figma's sand tile); `photo` a photograph layer;
  `horizon` a dark band with a lit rim; `deep` near-black with a cool pool (x.ai's).
- **Deal:**

  ```bash
  node <skill>/assets/backgrounds/pick.mjs --type software --sections <the plan's ids> --mode light|dark --history .taste-skill/bg-history.json
  ```

  Hardware runs it as `--type product --kind tech`; with an effect or scene already dealt, add
  `--effect`, and leave the section that holds it (an effect hero, the `[data-visual]` section, the
  scene's section) out of `--sections`: it brings its own ground.

  Mark a section the rhythm already makes a band: `id:dark`, `id:band` (lit ground), `id:surface`.
  Build what it prints, then hold the rules: at most two dealt grounds a page beyond the tokens, each
  once, never on a card, never two strong ones as neighbours, one loud one at most, never two that
  list each other in `avoids`.
- **The effect rule:** a ground with grain, dither or texture (`grain`, `field`, `stage`, `deep`) or
  motion (`liquid`) is the page's one effect (`effects-usage.md`); with another effect dealt, deal
  again without them. `liquid` runs on a clock from load with a pause disc and holds still under
  reduced motion.
- **The lit ground** (`<html data-ground="sand|sky|sage|painting">`) is tech only: behind UI, in a
  closing band, in `footer-statement`; it is the tone of `band` and `field`.
- **Words on `photo`** sit on its calm, dark part (`--g-photo-pos`, `--g-photo-pos-m` for the
  subject); only in the hero and one closing band (`system.md`).
- **Tune:** `--g-hue` tint, `--g-k` strength, `--tone` second tone, `--halo-x`/`--halo-y`,
  `--stage-w`. Tints lean to the accent, never violet.
- A ground never changes a section's height (`layout-v4.md`); a soft one fades over 120px, a hard
  one keeps its colour on the whole box; a panel takes `bg-inset` on the `.wrap` lines.

## Tech: code-drawn grounds, how they look

Calm and specific as a studio photograph: one light, one palette, grain you notice only up close.
Colours from the tokens (`--ground`, `--ground-2`, `--ink`, `--tone`, `--tone-hi` = L +0.12,
`--tone-lo` = L -0.18), mixed in OKLCH, ground chroma under 0.12. A gradient is built light first:
a radial with four to six stops in one hue, then grain (4 to 10%); every dark gradient gets a static
dither; never a two-stop linear gradient as decoration (linear only as an edge fade inside a
visual); a two-tone seam is a hard stop. Grain only inside the one effect: one tile made at load,
never animated, never over UI, text or photographs. Recipes, all still:

- **Lit studio sweep:** behind a cut-out or a UI window: an elliptical radial (50-60% x 40-50%,
  centre 35-42% down), a faint floor bounce, grain 4-6%, a soft contact shadow.
- **Corner glow:** a dark footer, closing band or pricing card: a radial near one corner, radius
  110-130%, five eased stops so no ring shows.
- **Painterly field:** under a UI window or a closing band: four to six large ellipses in the tones,
  blurred 60-120px, drawn 10% oversize and cropped, grain.
- **Spotlight floor:** a hardware stage or a dark hero on a dark page: a light pool 70% wide, a
  blurred shadow running away from the object, side vignettes.
- **Product-colour wash:** a hardware card or model switch: a radial from below in the product's
  tint; it cross-fades on a click, never on scroll.
- **Woven tile and ordered dither:** one texture a page at most: a band, the footer, a technical
  panel.
- **Grid marks** (dots or plus signs at column crossings, 12-18% ink) only on one dark technical
  band, a data panel or the footer, never over text. A hairline ledger (header cells, a line-up,
  footer frame) is 1px repeated sibling rules at 12-15% ink, never between sections.



---

## `references/cards.md`

# Cards

How a feature card is built so it looks like x.ai's and Figma's, not a template. Measured from
the reference recording (x.ai Grok Bot 2x2, Figma's tile wall) and a study of 41 company sites.
Showcase: `assets/ui/cards.html` (nine layouts: 2x2, bento, split, stat, integrations,
testimonial, pricing, tall cards, developer tools; light and dark). Every fragment on its own: `assets/ui/index.html`.
Styles: `assets/ui/cards.css` (card, panel, placements) and `assets/ui/base.css` (fragments).
Motion: `assets/ui/ui.js`. Objects instead of photographs: `assets/ui/_lab/object-card.html`.

## Why theirs look expensive

1. The card is barely there: one step off the page, a hairline, generous padding. The colour is
   inside the panel.
2. The panel holds a real, lit picture (a painted landscape, a grain field, a mesh, satin), never a
   flat two-stop gradient and never a pattern of lines or dots. On a dark page it is the brightest
   thing in the card: x.ai puts a daylight painting behind its dark UI.
3. The UI on it is a real product at true size, cut by the panel's edge: a glimpse of something
   bigger, not a toy floating in the middle.
4. One thing moves per card group, inside a panel (tech pages). The card never moves by itself; a
   card with a link lifts 2px on hover (`motion.md`).
5. Everything lines up: panel edge with text edge, radii nested, titles level across a row.

## The card

- Fill `--card`, one clear step off the page (light: white on `#f3f3f1`; dark: `#151517` on
  `#070708`, as x.ai's dark cards read against their page), or no border at all when the photograph
  or flat fill is the card.
- Border 1px, ink at 8 to 14%; inner top highlight 1px (white 5-7%, dark only). No blurred shadow at
  rest (a hard zero-blur offset is allowed as the rest style); a card with a link may show a soft
  shadow on hover only (`motion.md`). A card with a link lifts 2px on hover; a card without one
  carries `.m-nolift`. Never tilted, never a carousel: rows show whole cards; press quotes stack.
- Rows on the grid: two-up 6+6, three-up 4+4+4, four-up 3+3+3+3, the first card on the left line,
  the last on the right, one height per row, every row full (`layout-v4.md` section 4). Mark every
  frame that holds a visual or UI with `.frame` or `[data-visual]` so it never counts as a band.
- Radius `--r-lg` (20 on `soft`; 18 on a phone). Padding 32 from 1024px, 28 below, 24 on a phone:
  never under 24, and the text always inside it. A filled split panel pads 48.
- Title one line at the card-title token (20/18), weight 500. 8px, then at most two lines at 16/24
  in the ink (`--c-text`, 84% ink: never small grey text), at most 46ch. All running text in a card
  is 16/24 in that ink: points, the line under a stat, plan lines and lists, a quote's name and role, a
  result's bar labels. Muted small text is for labels only (a price's "/ month", a section tag).
  `.card--row` holds the lines at 2 from 1024px so titles and panels line up across a row.
- 32px from the last line to the panel. One `--p-h` per card group (page CSS).

## Two levels, never three

A card holds a picture, and the picture holds the product. That is all:

- **card > panel (a lit picture) > fragment.** The panel must read as a picture, not as a box: a
  soft field with no border lines, grid, ruling or dots of its own, so the fragment sits *on a
  picture*, not in a frame in a frame.
- Never card > patterned panel > white UI card (in testing, "card, grid-paper panel, white UI card"
  read as three nested boxes). Never a fragment that is itself a card holding cards of text.
- Never a card inside a card for text, never glass.

## The panel

- Default (x.ai): side edges on the text column, runs off the card's bottom edge, top radius 12,
  the lower 60-65% of the card (`--p-h` 264-340px).
- `.panel--inset`: even 8px margin; radius = card radius - margin (20 - 8 = 12), never under 6,
  so the corners read as one family. Every panel in a row has one ratio (4:3 or 16:10) and one
  inset. A smaller UI card on a panel is solid (never frosted), 40 to 60% of the panel's width,
  offset so the panel's bottom or right edge cuts it.
- `.panel--flush`: runs to the card's side and bottom edges (Figma's image band).
- `.panel--top`: on top with an 8px margin, the card's lines below (tall cards).
- `.panel--device`: a status row on the card itself (app, muted context, a quiet status with a
  still dot), then the ground as its screen, radius 12, running off the bottom: x.ai's "Computer"
  card. The row is not a frame of its own (a filled device frame made a fourth box).
- A 1px inner edge (`::after`) sits over the ground and over any fragment it cuts.
- The vignette (`::before`: `--vx`, `--vy`, `--calm-k`) calms the ground where the fragment sits.
  On a lit ground set `--calm-k: 0%` and use the effect's own `calm` params.

## The fragment on it

- **The product's own subject**: the fragment shows what this product works on, as its
  users see it. A code-review tool shows a real diff, red and green, with the comment and its
  Accept or Apply action (`diff-review`); an invoicing app an invoice; a booking app its calendar; a
  CI product its pipeline (`pipeline-board`, `terminal-run`). Never a generic dashboard, chat or stat
  card standing in for it; when no fragment shows the subject, build it from the client's screens.
  Cards show parts; the product is shown whole once, big, in an `app-frame` (`sections-library.md`:
  `window` as the list beside the open item, one window across the `.wrap`). A software page whose
  product appears only as small fragments centred on coloured panels reads as fragments, not as
  the product (in testing: about 3.5 points under Linear).
  A gaming page takes no fragment at all: it shows the game (`sections.md`, Gaming). Its feature cards are open cards for what you do in it, one verb each (sail, salvage, rebuild), each holding an in-engine shot, else the still render of the object that verb uses (`data-product-place="card"`).
- The product's real UI as live HTML at true size, complete and legible, never a flat picture:
  13px text, 12px meta, never under 11px; weights 400 and 500. Real data (names, amounts, order
  numbers, times) and real app marks (`icons.md`). Each fragment keeps its minimum width (chat
  140, checklist 160, slider 215, toggles 230, search 240, terminal-run 280, calendar 280, stat 285,
  cursor 290, files 300, diff-review 280, pipeline-board 280, notify 340, code 365, doc 400, window 456).
  A phone mock or UI card runs past its panel
  only where the panel clips it, never past `.wrap`.
- Surface white on light, `#1c1d20` on dark (one step lighter than the `#151517` card; `--frag`
  sets it); 1px border at 12%; radius 12; the layered shadow lives only inside the panel.
- The primary button is the ink; switches that are on are ink; the product's own mark
  (`.ui-agent`) is ink. **The accent appears once per fragment**: the row being worked on, the
  marked date, the marked line's bar, the last bar, the slider being dragged. A range, keywords,
  numbers, today's dot and status chips are ink tints. Never a row of green dots.
- **Real icons in their own colours** (house rule: "more colour, more official"): a mark on a
  tile (`.ui-logo`, `.ui-file__icon`, `.ui-field__tile`) sits on a light tile on every surface, in
  its brand colours: a colour file from `assets/icons` (`icons.mjs fetch` or `scan`,
  `references/icons.md`) as `<img>`. The kit's sample marks are local files in `assets/ui/icons`
  (`<img src="assets/ui/icons/x.svg">`): after pasting, write each as the client's tool,
  `<img data-icon="<id>" src="assets/icons/<id>.svg" alt="">`, and `icons.mjs scan --colour` fetches it; no page calls a CDN for an icon. One treatment per set: never colour marks beside ink marks. A small mark inline beside text (a breadcrumb, a source chip) stays in the ink.
  Glyph marks only; a wordmark (Zoom's) is illegible at tile size.
- Placement (`.stage` holds them, absolute in the panel; each `meta.json` has its own `place`):
  - `.at-corner`: 28-40px from the top-left, cut by the right and bottom (19 of 41 sites).
  - `.at-rise`: starts 24-56px down and leaves through the bottom (chat, voice, a calendar).
  - `.at-right`: anchored top-right; it narrows on a small panel rather than cut its text.
  - A short stack (notify) sits low: `--ay` and `--ay-sm` `calc(100% - 180px)`, its last row cut.
  - `.at-over`: a second fragment over the first one's lower-right edge. The `cursor` dialog only
    ever sits here, over a window: never alone on a ground, never centred.
  - `.at-center`: only a small control (at most about 250 x 130) on a focal tile: the compact
    slider driving its ground (Figma's Texture tile). Never a window or a dialog. It never runs
    past the panel (cards.css caps it at the panel less 24px a side, 16px on a phone).
  - `.fit` + `--fit-max: <true width>`: keeps its width on a wide panel, centred between the
    insets (even ground at both sides), and narrows on a small one, so 1024 never shows a 1-23px
    sliver or cut. `window` lays itself out for the width it gets
    (rows stack under 540px, the sidebar goes under 420px), so it may sit in a `.fit`.
  - `.wide` + `--w`: a fluid grid (files) set wider than the panel, so it is cut by the right
    edge like a window; it always runs 64px or more past it.
  - `.to-edge`: the wrapper reaches 72px past the bottom, whatever the panel's height; `chat`,
    `doc`, `stat` (`fill`) and `voice` grow into it, so they are always cut, never a few px short.
  - Developer tools (tech and software pages only; all three lay themselves out for the width they
    get, so none is ever sliced):
    - `diff-review` (a code review on a diff): `.at-corner.fit` (or `.at-rise.fit` in a wide panel)
      with `--fit-max: 480px` (up to 760px wide), 32-40px in, cut by the bottom with `.stage--fade-b`:
      the reviewed line, its suggestion, the comment and the Apply button stay in the top 250px, and
      the diff runs two context lines further, so a 352px panel at 36px down cuts it by 32px or more
      at every width (never leave less than 24px of it past the edge). Never cut it by the right edge.
      Under 440px it keeps one gutter and drops the function name from the hunk header; on a phone give
      its panel 340px or more. The file's real mark (TypeScript) sits on a light tile in its header.
      The accent is the short bar beside the comment's text, set in from the comment's edge.
    - `terminal-run` (a test run in a terminal): `.at-rise.fit` with `--fit-max: 440px`, 32-40px in
      and 32-40px down, always whole with 24px or more of ground under it (a 352px panel at 40px
      down). Never cut or faded: the status line with its green check sits one row above the bottom.
      In a wide panel or a split card `--fit-max` goes up to 560px (the path column stops at 28
      characters). The counts go under 380px; the branch and the repo's parent folder under 300px.
      The status check is the one green and the strongest mark; the meter's thin bar is the one
      accent; the per-file ticks stay ink.
    - `pipeline-board` (a CI run on a rail of steps) sits whole: `.at-rise.fit` with
      `--fit-max: 420px`, 32-40px down, 24px or more of ground under it and no fade, since the
      running step reaches the last row. In a large panel or a split card it goes `.at-corner.fit`
      at its full width (680px or more), where it becomes a row of nodes with a log about 300px
      tall, and the bottom-right corner stays clear for the pause button. Waiting steps say
      "Queued" in the markup, so no node is an empty box. Each step names the real mark of its tool
      (Git, npm, Node.js, Docker, Kubernetes) on a light tile, one treatment for all five. The cycle
      starts and ends on the markup as written, so write the picture to rest on (the run part done).
- Vary the placements across a group: a 2x2 shows at least three (rise, corner or device, a low
  stack, right). Never one card layout four times.

## Edges and fades

- Every edge keeps 24px of ground or is cut by 24px or more (16px a side on a phone, by design).
  A cut never slices text: `.stage--fade-b`, `--fade-r`, `--fade-br` dissolve the last
  `--fade-h` (64px; 40px on a short panel such as the tall cards) into the ground.
- **A fade never crops the point.** It only covers context: the row below the one that changes,
  a chat's input, a page's later paragraphs, a list's last rows. The thing the card is about (the
  row being worked on, the connecting app, the number, the button, the orb and its transcript line) sits
  above `100% - --fade-h`. Put the moving row near the top (the integrations target third, not
  last), or lower the fragment's start, or shorten the fade.
- A fade only where an edge cuts: a fragment that keeps 24px of ground on a side has no fade on
  that side (`--fade-br` on a window that ends inside the panel fades it for nothing).
- Measure at 1440, 1024, 768 and 390; on a phone cards.css places the fragment 16px in on both
  sides, cut only at the bottom.

## Grounds

Shader grounds in panels are for tech pages (software and hardware; a gaming page has no feature
cards of UI), one card group a page, still, from the family of the
page's one effect (`effects-usage.md`). On a product or service page a panel holds the client's
photograph (`<img class="frame__img">`, zooming 1.02 to 1.03 inside it when the card links), real
icons or a still diagram on a flat `--g-alt` or `--g-main` panel; a place has no feature cards.
Other tech card groups take a flat panel, the lit ground plain, a photograph or a diagram.

- One ground id for the card group, a new `data-fx-seed` per panel, never the id of the hero's
  effect (one effect in hero, cards and close reads as a stock motif).
- **Behind a fragment, a soft field**: `painterly-landscape`, `grain-gradient`, `gradient-mesh`,
  `silk-folds` (and other mesh, grain and material families). Never a pattern that fights the UI:
  no `grid-pulse`, `ruled-grounds`, `contour-lines`, `dot-terrain`, `ridgeline`, `halftone-screen`
  or `bayer-dither` behind a window, list or card. Those are pictures on their own: a panel with
  no fragment, an object's print, or the data cut out of the UI (below).
- Lit behind UI, on both themes: give each panel that holds UI a light `data-fx-palette` of its
  own, the same in light and dark. On the dark page it is clearly lighter than the card (3:1 or
  more), so page, card, panel and UI are never four near-black layers; on the light page it is a
  clear step darker than the white UI. The palettes in the showcase:
  - painting: `{"bg":"#a3b0b6","accent":"#c49a6c"}` with params `"blur":1,"brush":0.35,"slope":0,
    "hillY":0.3,"horizon":0.62` (a level mist over warm sand, fully soft). Never a blue sky over a
    green hill with a diagonal crest: it reads as a stock desktop wallpaper, not a crafted ground.
    At most one painted panel in a card group (one per page is better); the others take the sand, sky
    or sage palette on grain, mesh or silk.
  - sand: `{"bg":"#d9ccb7","surface":"#e9e0d2","ink":"#2a2622","accent":"#a8794a"}`
  - sky: `{"bg":"#c6d3df","surface":"#d6e0e9","ink":"#25303a","accent":"#3f6a92"}` (silk-folds
    takes a softer accent, `#7f9fbd`, with `"tone":1`)
  - sage: `{"bg":"#cdd6c6","surface":"#dce3d6","ink":"#262d24","accent":"#6c8e63"}`
- A calm hue of its own keeps the page's accent rare. Never violet or lavender.
- Hold every ground still in a card: `speed` 0 or `drift` 0, and `grainMotion` 0 on
  grain-gradient (its film grain moves otherwise). Where the bottom fade shows the ground, calm it
  there (`calmY` near 1) so the fade meets a quiet field, not a bright highlight.
- A ground shows something behind something. A strip of effect under a stat or a line of text, holding
  nothing, is decoration: leave the card plain (Figma's "64%" is a number and one line).

## Light on a laptop GPU

Every page must run on an integrated laptop GPU (2 GB shared), so:

- system.js mounts card grounds through `ui.grounds(document, fx)` (a page without system.js calls
  it itself, never `fx.mountAll`): each still ground is drawn once as it nears the screen, at up to
  2 device pixels (sharp on a 1.25-2x laptop), kept as a plain picture, and its WebGL context freed,
  one at a time, the panel on screen first (a scroll past a group never makes the one in view
  wait). A ground a fragment drives (the slider) carries `data-fx-live`: it is live near the
  screen only, at 1 device pixel, and draws only when it changes; under reduced motion it is baked
  like the rest.
- Live contexts: the page's one effect is the moving hero ground (system.js keeps it live) or one
  of these: the driven ground, the voice orb (dark surfaces only; on light it is CSS), a hover
  light (the featured plan's lap), an object (`effects-usage.md`). Never two of them on a page.
  `ui.grounds` bakes the card grounds one at a time (one context while baking, none after:
  `effects-creative.md`, Cost) and caps the `fx` library at 3 live contexts; the page's cap of 4
  (`perf.md`) counts everything live at once, the effect, a scene and a moment's canvas included.
  It leaves `fx.config.maxDpr` alone.
- An object or any raymarched canvas mounts when its panel nears the screen and is destroyed when
  it leaves (`_lab/object-card.html`); one per card group; never two objects and a moving ground in
  one view. It renders at most 1 CSS px per pixel (0.75 when large), about 1.5 megapixels, and
  stops off screen and in a hidden tab.

## Motion

Card loops are for tech pages; every number (cycle, restart, pause disc, life signs) is in
`motion.md`. The same rule as system.js, in one line: **put `data-ui-loop` on the group's one loop;
every other fragment holds its finished picture.**

- With system.js nothing else is needed: it marks every other fragment `data-ui-still` before it
  loads, and on a phone (under 640px) every fragment but `voice`.
- Without system.js (`cards.html`), `ui.loadAll` / `ui.startAll` do the same as soon as the page
  holds any `data-ui-loop`. A page with none (the kit's `index.html`) lets every fragment loop.
- The group's loop is the one whose motion shows the point (the slider that drives the ground,
  the chat answering). `voice` always runs (held, it loses its orb), so it is its group's loop.
  `data-ui-still` holds a fragment by hand; `data-ui-cycles="2"` plays two cycles when first
  seen, then rests on the finished picture, with no button.
- Below the hero, two loops are never on one screen: a group next to a looping one holds still.
- ui.js puts a pause button on every loop when it starts to move: a solid 32px disc in the page
  colours. In a `.card` it sits beside the card's title, at the right of the text column (the
  title keeps 44px clear for it), so it never covers a cropped panel's UI, which runs into every
  corner. In `[data-ui-pause-host]`, or a `.panel`/`.frame` outside a card, it sits 12px in from
  the bottom-right corner (keep that corner clear); a fragment with no panel gets it under its
  bottom-right corner, in 44px kept free. A place that already holds a `.loop-pause` gets no
  second one. Keyboard focus in a card plays a held fragment's cycle once; only a pointer resting
  on the card repeats it (a held fragment has no button).
- Anything else that moves on its own for more than 5 s (an object, a moving ground) gets the
  same button: `ui.pausable(panel, ctrl)`, where `ctrl` has `pause()` and `resume()`.
- Loops start on the finished picture and never show an empty window or greyed text: the chat
  writes only its answer's last sentence again, and the voice its transcript line, each in under 0.8 s
  with no word below 72% ink (4.5:1 on white), then hold the finished text for the rest of the cycle. The files
  status line shows only the page's words (`data-reading="Reading {n} of {total}"` on the root,
  in the page's language; without it only the line's number counts). A tile the panel cuts
  hides its name, never half a word. They stop off screen and hold still under
  reduced motion (no buttons then). Nothing moves because the page scrolled.
- **Cadence and hover** (house rule 5): one cycle of 2.5 to 4 s that repeats and restarts when the
  pointer or focus enters the card; every number is in `motion.md`, Loops inside a card's visual. A
  card whose fragments are all held plays its top fragment while the pointer stays. The card itself
  never moves by itself.
- **From the page**: `ui.restart(el)` restarts every fragment in `el` (a tab or panel shown
  again); a held one plays once. Every fragment root fires a bubbling `ui-cycle` event as each
  cycle starts, for a page that keeps a second piece in step.
- **The page's words, never the kit's**: a fragment's script shows only text from the markup. Its
  finished picture is the markup as written (the doc's note, the slider's value, the stat's number,
  the voice transcript and timer); its other states are written beside the text they change
  (`data-done`, `data-busy`, `data-note`, `data-msg`, `data-work`) or passed as opts. A count
  keeps its words and only its figure follows ("4 of 5 on" reads "3 of 5 on").

## Effects that are not backgrounds

- **The control drives the ground**: `slider` with `{"drive":{"param":"grain"}}` changes the
  panel effect as the thumb moves. Make it the group's loop. `{"compact":true}` keeps the name and
  the one slider, small enough for `.at-center` on a focal tile.
- **Data cut out of the UI**: `stat` with `{"window":true}` cuts its bars out, so the ground shows
  through them.
- **A number filled with an effect**: `.knock`, a still canvas under white text with
  `mix-blend-mode: darken` on dark (black text, `lighten`, on light); the card fill must be exactly
  `--card`.
- **A live object in the UI**: on a dark surface `voice` mounts `orb-sphere` as the call's orb, a
  pale nebula with specks of light (x.ai's voice orb); on a light surface it is a pearl drawn in
  CSS with clouds of the accent and the ink turning slowly inside it and a few specks of light, never
  a plain white disc. The accent is only the thin ring round it. Never a dark glass ball on a light card.
- **A real object, no photograph** (tech only): an object from `assets/objects` is the whole
  picture of a `.panel--top` on one of the lit palettes above, centred because it is the subject;
  how to mount, print and pause it is in `effects-objects.md`. It turns, never tilts the card.
- **A lit border** on the one featured object: `data-glow="edge-glow"` and
  `data-glow-params='{"fill":1,"wash":0,"speed":400,...}'` on the featured plan (never `data-fx`).
  It rests on a quiet accent hairline; on hover or keyboard focus one light runs round the edge
  (about 4.6 s, mounted for that lap only), then fades. Never on scroll or on view. The hairline is
  the plan's one accent, so its badge is quiet ink.

## Never

- A big fragment dead centre with even ground all round; a dialog alone on a ground.
- Three levels of boxes: a card, a patterned panel, a white card on it.
- A pattern (grid, ruling, contours, dots) behind a window or a list.
- A fade over the point of a fragment; a sliver of 1-23px at any edge.
- A dark ground behind dark UI on a dark page.
- The accent on every chip, date and keyword; brand colours mixed with ink marks; glossy 3D blobs.
- A loop over 5 s with no pause button; a spinner, caret or pulse running on in a still picture.
- A card or panel that moves with scroll or lights up when it scrolls into view.
- One WebGL context per panel, or a still ground left running its frame loop.
- A "sample", "example" or "to follow" note anywhere, even one line in the footer (in testing:
  "Names and figures on this page are examples" read as an apology), a caption under a visual
  that explains or apologises, and a placeholder (`[Name]`, `Example Street 1`, a `.example`
  address, lorem ipsum). Licence credits go in one footer line.
- Small grey card text (15px muted): card text is 16px in the ink.



---

## `references/copy.md`

# Copy

Say what it is and what it does, in words a stranger understands in five seconds. Every sentence is
one you would say out loud to a customer. No metaphors, poetry, invented terms or ad wording. Every
studied site is a description only: copy how the examples are written (plain, category first),
never their words, code, pictures or signature effect.

## Five rules

1. **The h1 names the category, and for a brand nobody knows, the buyer or the place,** in 2 to 8
   words: payroll app, dental clinic, standing desk, plus who it is for or where. A place: what and
   where in 40 characters at most ("Bakery on Mill Street, Leith"; "Six-room guesthouse on a fjord").
   A game: its name and genre ("Kelpmoor, a co-op sailing game"), or its wordmark over an h1 naming
   the genre; the launch date or status the brief gives is the hard fact. Never a riddle, a command, a mood, or a brand line over a plain sub-line.
2. **The first screen holds one hard fact:** a number, a place, a price or a date.
3. **Every heading has a noun that names a thing:** the product, a part of it, the place, a section
   noun (prices, rooms, menu, opening hours, questions, getting here, visit) or a digit. One brand
   line a page at most, never the h1.
4. **Buttons are a verb plus what the visitor gets,** 1 to 5 words, starting with book, buy, order,
   pre-order, reserve, try, start, get, download, compare, see, watch, read, find, join, subscribe,
   sign up, contact, configure, add, send, email or request; a bare noun only where the link opens
   that thing. Never "Learn more", "Read more", "Discover", "Explore", "More" or "Click here".
5. **Few actions, each with one wording:** at most 2 in the hero (one on a place), 10 different
   labels a page at most. The main action names the transaction (Book a room, Order a cake, Start a
   free trial; on a place the brief's order or booking, else Get directions, never a side event) and
   reads the same in the nav, the hero, the close and the phone bar, and nowhere else.

## Plain versions

When a line is vague: the category noun first, then one count, place or price from the brief, no
figure of speech.

| Vague | Plain |
| --- | --- |
| "Every shift, sorted" | Shift planning for restaurant teams |
| "Where the city climbs" | Climbing gym with 180 routes in Leipzig-Plagwitz |
| "Come climb" | Day pass 14 €, shoes included |
| "A second read of every word" | AI proofreader for book publishers |

## Headlines and text

- **Hero sub-line:** software, product and service: how it works and the main benefit, 15 to 30
  words, one line to two sentences. A place: the fact, 80 characters at most, with today's hours
  ("Sourdough, rye and cardamom buns from 7:30, Tuesday to Sunday."); a hotel the rooms and the town.
- **Section headings** name the thing ("Rooms and prices", "Works with your tools") or make a short
  plain claim ("Pays staff on the same day"), 1 to 6 words, at most two lines. A noun phrase or "we
  do X for Y", never a command, a question (FAQ entries may be questions), a colon heading or a line
  that only makes sense after the page ("Continuity slips", "It reads everything you decide").
  **Card titles:** a verb and an object ("Warns about double shifts"), one line, real words, never a
  coy label ("The market run").
- **Under a heading** one line to two sentences (10 to 40 words); a card body 1 or 2 sentences, 25
  words at most, in the buyer's words with one concrete detail; no paragraph over five lines at
  1440. A price does the selling, not a mood heading ("Rooms from 140 € a night, breakfast
  included").
- **Words per screen** stay low: product 47, place 44, service 34; a page about 900 words at most,
  the footer aside. Long copy goes to sub-pages.
- **The tech word budget** (software, gaming, hardware): 60 to 80 words a screen at 1440, counted
  outside UI mocks, diagrams and code (headings, lines, card titles and bodies, buttons, labels);
  over 80 the checker WARNs (in testing: a fintech page at 117 words a screen read as wordy). Cut in
  this order: a second sentence under a heading, card bodies to one sentence of 12 to 18 words, a
  fourth card, a list a fragment already shows. The UI says the rest.
- **Numbers** sit in sentences with their unit ("4.5 hours a week"), uneven where real (212, 38%).
  A real claim from the brief that needs a source gets a numbered footnote near the footer (13px
  and up).
- **Pictures** stand beside short copy, never in place of it, and words never stand where a
  photograph fits. Every word is live text.
- **Self-check:** read each line aloud to a customer. Is it clear what the product does? If not,
  rewrite it.

## What may be assumed

- **Prices, address, hours and dates come from the brief;** the report lists any you assumed. Only
  two things may be assumed when the brief lacks them: a coined brand name (below), and on a place
  plausible hours and prices for the trade, uneven and in the local currency (3.60, not 4.00).
  Nothing else is invented.
- **No invented proof:** no invented reviews, ratings, review counts, quotes, testimonials,
  statistics, customer counts, customer names, portraits, clients, awards, press lines or products.
  Customer logos only for real customers the brief names and that may be shown; a real tool the
  product works with keeps its real icon in its own colours (`icons.md`), never a drawn imitation.
  Without proof, a strip of plain facts from the brief, or nothing.
- **No sample notes:** no "sample", "(sample)", "examples", "illustrative" tag, note or asterisk
  footnote anywhere. A target value the brief itself gives is worded inside it ("target 2 days").
- **No placeholders:** no square brackets, "lorem ipsum", "your name here", "to be added", TODO,
  kit sample text, and no link to `#` or an empty href. Write the real words, or leave the element
  out. "Coming soon" only for what the brief says is coming.
- **No caption, label or description under or on any visual** (house rule): not "A drawing made in code",
  "Photographs follow", "Representative image", not a name, price or link line under a bare picture,
  no hashtags. A heading names the set; a sold item's name and price sit inside its card's padding.
  The picture shows the thing or is left out; the report lists the photographs the client must
  supply.
- **Credits:** one short line at the end of the footer naming only the sources used, never the
  photographers: "Photographs via Unsplash and Wikimedia Commons" (as `photos.mjs credits` prints
  it; 110 characters at most, one line from 1024) that links or opens the credits list. Paste the
  line and the list exactly as `photos.mjs credits` prints them; never write a credit link per
  photograph into the footer (in testing: 18 and 20 credit links in a footer read as a credit wall).
  Map data credits join it. A page that shows real logos
  adds "Product names and logos are trademarks of their owners".
- **Each fact once:** an opening time, a price or an address has one value and one wording,
  repeated word for word only where it belongs (the hero, the visit panel, the phone sheet, the
  close, the footer); never two hours for one day.

## Contacts the brief does not give

What the brief gives is printed exactly as given. Each kind is separate: a brief that gives only a
phone number still gets the address, email and imprint rules.

- **Address: a street and a district only** ("Elmgatan, Malmö-Möllevången"). Never a house number,
  a postcode or map coordinates. One street address a page (the visit block and the footer, at 390
  too), never readable only on a sign in a photograph. Several shops: each name, then its street. A
  studio by appointment says so.
- **A brief with no street:** print the district only ("Eimsbüttel, Hamburg"), the town when no district is named,
  and never an invented street or number; the type moment `address` sets that district. List the missing street in the report
  as the client's to supply.
- **Maps:** no map loads with the page. Get directions opens
  `https://www.openstreetmap.org/search?query=<street>+<district>` (no street given:
  `?query=<district>+<town>`), with no coordinates and no route; on the phone the address opens the
  same search. A map is drawn only for a street the brief gives (`fx-map` baked still, the pin on the
  street line, never a building); a builder's real street never gets a real map, since it pins a
  stranger's door. Never an iframe.
- **Phone: none, unless the brief gives one.** No number, no `tel:` link, no Call button. A
  "Request a call" form may stand in.
- **No imprint page and no company details:** no register number (HRB), VAT or tax id, company
  number, managing director or court. The legal row holds the brand, the current year, Privacy,
  Terms and the credits line; an Imprint link only when the brief gives the company's own details.
- **Email and web:** a form, or a button ("Email us") whose `mailto:` is on `.example`
  (`hello@brand.example`). Never print an email address, a domain or a social handle, not even a
  `.example` one. `.socials` stays empty unless the brief gives the accounts.
- **Names are coined,** not dictionary words and not a business that exists, unless the brief gives
  the name; person names come only from the brief. Search a coined name with its trade ("name
  coffee") and as a domain; if a business of that trade or a famous person has that exact name in
  the first 10 results, coin another. Write each query and result in `names.json` beside the page
  (`"searched": false` with no search tool).
- **Links** go where their label says: a part of the page (`#rooms`) or a page that exists; never
  "here", never two different labels to one target, never a link to a closed answer.
- **Newsletter:** asked once, in or just above the footer, "Subscribe" or "Sign up", an email field
  only; never in a modal, never twice.

## Banned

Metaphors and "where X meets Y"; slogans, greetings and boasts in the hero; questions as headlines;
exclamation marks; all-caps labels; invented capitalised concepts ("the Proof Layer"); unexplained
programme names; jokes or slang in labels; mood paragraphs; a literary quote as a full-screen band;
filler (seamless, effortless, cutting-edge, unlock, elevate, supercharge, reimagine,
next-generation, game-changing, powerful, robust).



---

## `references/diagrams.md`

# Diagrams

`assets/diagrams/diagram.js` draws a node-and-line visual for a card panel (about 560 by 340) or a
section (1200 by 560) from a small JSON spec. `presets.json` holds 27 ready specs, each tagged with the page
kinds it suits (`types`: software, tech, gaming, product, service); `demo.html` shows them in feature cards, light and dark
(`?type=gaming`); `lab.html` is the tool to build one (below).

## When a diagram, when a UI fragment

- A diagram, when the point is how things connect: the tools it reads from, one input split into
  parallel jobs, many sources into one place, two systems in sync, steps in order, regions.
- A UI fragment (`assets/ui`), when the point is what the user sees or does: a drafted reply, a
  calendar, a dashboard. Never a diagram of a screen.
- One diagram a section, two a page at most (tech; a product or service page one, held still). A
  place page has none. On a gaming page a diagram shows a system of the game (matchmaking, saves,
  stores), never in place of the game's own pictures.

## Pick a layout and a preset

| layout | shows | presets |
|---|---|---|
| `hub` | a centre and its tools; with `children` a mind map, or a web with `"shape": "radial"` | hub-tools, hub-branches, hub-web, hub-stack (tech), hub-stores (gaming) |
| `ring` | logos or regions on an orbit | ring-apps, ring-regions, ring-edge (tech), ring-servers (gaming) |
| `tree` | one thing branching out | tree-orders, tree-release (tech) |
| `lanes` | one input, a core, parallel lanes (three threads) | lanes-agent, lanes-media, lanes-deploy, lanes-render (tech), lanes-matchmaking (gaming) |
| `fanin`, `bowtie` | many into one; and out to many | fanin-warehouse, fanin-telemetry (tech), bowtie-events, bowtie-model (tech) |
| `sync` | two systems, records crossing | sync-crm, sync-saves (gaming) |
| `timeline` | steps done in turn | timeline-onboarding, timeline-season (gaming) |
| `grid` | files into a pipeline | grid-documents, grid-assets (gaming) |
| `free` | your own nodes and edges | free-approval |

Filter by kind: `dg.presets()` gives the object; keep the ones whose `types` has the page's kind. Gaming and tech pages take the tech
and gaming presets with pulses; a product or service page takes at most one, held still.

```html
<link rel="stylesheet" href="assets/diagrams/diagram.css">
<div class="panel"><div class="dg" data-diagram="lanes-agent"></div></div>
<script type="module" src="assets/diagrams/mount.js"></script>
```

Copy a preset into `data-diagram='{...}'`, then rename every label, icon and number to the client's own. A label with an apostrophe
or a quote (`it's`) ends a single-quoted attribute, so then put the spec in a script inside the element:

```html
<div class="panel"><div class="dg" data-diagram><script type="application/json">{"layout": "hub", ...}</script></div></div>
```

A spec that does not parse logs a `console.error` and leaves only the names it could read.

## The builder page (the tool for building one fast)

Open `assets/diagrams/lab.html` over http. Pick a page kind and a preset, edit the JSON (it redraws while you type) or use the controls
(ground, light, line shape, cycle 2.5 to 4 s), switch card, section, phone and light, dark, restart the loop, then copy the
markup and the icon line. Inside a card it shows the real thing, never a mock-up. A new diagram is a preset plus the client's words;
`free` takes nodes at fractions of the box and the edges you list.

## Icons: one resolver, run it last

`diagram.js` reads icon files and nothing else: no CDN, no tinting, no Simple Icons call at runtime. From the site root:

`node <skill>/scripts/icons.mjs scan index.html --out assets/icons`

fetches every id the page's diagrams name (curated short names such as `gmail`, `steam`, `google-docs`; `logos:`, `file:`, `si:` ids; `ui:` glyphs).
Colour marks come from the logos set in full colour; where none exists (Google Docs, Sheets, Slides) the Simple Icons mark in its brand hex,
painted by `icons.mjs`. An icon that is missing shows the name's first letter, and the console says
`diagram.js: N icons are not in .../assets/icons ...` with the fetch line: run it. A finished page has no such line.
Marks that are mostly violet (Stripe, Twitch) are drawn in the text colour, black marks take the ink, a wordmark gets a 2:1 slot and its
tile becomes a pill: all decided by `icons.mjs` and baked into the file (`data-ic`). `data-icon-base` on the element or around it
moves the folder.

## Motion: one cycle of 2.5 to 4 s

- A diagram card's pulse is its own loop (not one per card group). The program is laid out as a ripple: each spoke, branch or route
  starts a beat after the one before it (0.24 to 0.5 s, the stagger), and the whole program is then fitted to ONE cycle of 3.2 s
  (`"motion": {"cycle": 2.5..4}`), the lines fading in the rest. `d.T` is always 2.5 to 4 s. It repeats.
  Below the hero two loops never share a screen: beside a looping fragment one of the two holds (`motion.md`).
- It restarts from its first beat when the pointer enters the card (mouse and pen) or focus moves into it by keyboard.
- It runs only on screen. On a phone (under 640px) and under reduced motion it holds one still, the busiest moment; `"pulse": "none"`
  holds it too. `data-dg-still` holds it by hand and plays it while the pointer is on the card. `data-ui-still` does not hold a
  diagram. A loop that runs gets the pause disc.
- The light is a gradient comet with a glow and a bright head (`"pulse": "dot"` is the head alone). The accent is only the light
  and what it reaches; lines are hairlines; the core is an ink tile. The card never moves, nothing starts on scroll.
- Grounds vary by default (`rings` round a hub, `none` under an orbit, a timeline or a sync, `dots` for flows; the diagram that leads
  a section adds `glow`); `ground` sets it. On kind other (the one still diagram of a product or service page) set
  `"ground": "none"` and `"motion": {"pulse": "none"}`: pattern, glow and pulses are tech only. Size: a flat drawing takes the next size up when that fits; `"size": "band"` or `"card"` forces it.
- Lines: hub spokes are straight rays from the core's rim (`"curve": "curve"`, `"elbow"` or `"swirl"` change them); flows bend in rounded elbows.

## Labels plain

- A tool by its name (Gmail, Zendesk), a step by its result (Reply drafted, Label printed), a place by its city. One to three words.
- Real-looking numbers in `meta` (2,481, 14 ms).
- No jargon nodes ("Orchestration layer", "AI engine"): the core is called what the product calls it.
- Up to 8 spokes, up to 12 nodes in a card. Crowded means it should be a list.
- No caption under the diagram. The card title says what it shows; `alt` in the spec says it for screen readers.
- Tool marks in their own colours, never a letter in a circle. A core without an icon is a pill with its name.



---

## `references/effects-creative.md`

# Effects beyond backgrounds

An effect can be a part of the page, not only its ground: the picture in a feature card, a real object
drawn in dither, the letters of a headline, a button's fill, a border, an icon chip, a chart's area, a
map. The parts are in `assets/components/` (a folder each: `component.html`, `.css`, `.js`,
`meta.json`); `index.html` there shows them live with a palette switcher, starting each part only
while it is near the screen.

**Tech pages only** (site-kind software, gaming or tech: hardware), except `fx-photo` (every kind, as
a plain photograph) and `fx-map` (every kind with a door, a place included, baked still, and only
for a street the brief gives). What each kind may carry: `effects-usage.md`. `fx-band` is out: a
drawn band between sections is not a section. `fx-logos` is out: real logos show in their full
colours and never move (rule 7, MO-57; `sections-library.md` logo-row).

## Under the one-effect rule

- **Every part that holds a WebGL context is the page's one effect** (`effects-usage.md`): the
  dither object, a filled headline or stat, the globe, the avatar ring, the logo light, the progress
  light, the prompt glow, the edge-glow plan, `fx-spotlight`, and `fx-button`'s fill (on the one
  primary call to action, or one pair, fading in on hover or focus). It sits in the hero or the one
  `[data-visual]` frame, or serves a dealt moment in its own section; never beside a live hero
  ground. Painted panels in a 2x2 are card grounds drawn still, not the effect.
- **One pointer effect a page:** `fx-button`, `fx-spotlight`, a turning object, or a hover or liquid
  moment (`moments.md`), never two. The street map and a photograph are content, not effects.
- Everything else stays **quiet**: a search glow only while focused, one ring on the recommended
  plan, chips with a still grain. **One lit border a page** (`fx-prompt` or `fx-pricing`).
- A glow only on a dark ground, once, behind the key object in the hero or `[data-visual]`, still,
  never spilling onto text or round a button. One-shot transitions (a tile flip, a melt, a crack)
  only once, on a click or as a hero reveal, inside the `[data-visual]`; scroll-driven only as a
  dealt section moment. Ray marching only in a dark hero, at half resolution; halftone and dither
  only as a still ground, never on a photograph.
- Nothing moves with scroll; a card never moves by itself. Motion lives inside a visual: a pointer
  clicking in a UI window, rotors that spin up under the pointer, a seat that swivels after it.

## Cost: light enough for a laptop's integrated GPU

A laptop's graphics chip shares about 2 GB with everything else; too many live canvases crash it.

- **At most 4 live WebGL contexts per page** (house rule; `perf.md`), and only for things that move: the
  one effect and a dealt moment's own canvas. Everything still holds none at rest.
- **Stills render once.** An effect that does not move (speed and drift 0) goes through `still()` in
  `shared.js` (or `fill(el, id, { still: true })` for type): drawn once as it nears the screen,
  copied into a plain picture, its context freed. Stills draw one after another, so they never hold
  more than one context at a time. Never leave a still effect mounted with its frame loop running,
  and never give a still to a pause button (Play would start its loop).
- **Screenshots wait for the stills.** On a CPU renderer each still takes about a second (a new
  context, its shader compiled, one frame), so a screen captured a fixed time after a scroll catches
  some blank and a panel cut by two screens comes out half lit. While stills near the screen have no
  picture yet, `<html data-cx-baking="n">` says how many. A screenshot must wait until it is gone;
  `shoot.mjs` and `consistency.mjs` do not wait on it yet, so shoot a page with stills (filled stats,
  type in an effect, painted panels) with `--wait 1500` and look for unfilled digits before judging.
- **Per-pixel and raymarched work at 1 sample per CSS pixel at most** (0.75 when the canvas is large)
  and about 1.5 megapixels at most, whatever the screen's DPR. `fx-dither-object` runs once per
  dither cell (a ninth of the CSS pixels); `painterly-landscape` at 0.6.
- **Everything pauses** off screen and in a hidden tab (fx.js does it for every mounted effect), and
  a loop that runs on its own for more than about 5 s has a pause button.
- What holds a context on a page: `fx-dither-object` (20 fps), `fx-prompt`, `fx-globe`, `fx-avatar`
  and `fx-progress`, each only while near the screen; `fx-button` only while
  pointed at (freed 4 s later), `fx-search` only while focused. A page carries one of these (the
  effect). Every other part is a still, and so is the dither object under reduced motion. `fx-map`
  (plain SVG) and `fx-photo` (the photograph itself) hold no context at all.

## Feature cards with inset panels (`fx-feature-card`)

The card reviewers point at, as x.ai and Figma build it: a 2x2 of cards, each a title and two grey lines,
then an inset panel with its own 8px margin (radius = card radius - margin). The panel holds a bright
ground and one UI window that runs out through the panel's bottom edge.

- Ground: `painterly-landscape` (default) or `grain-gradient`, still, drawn once as pictures (the
  cards hold no context at rest).
- A landscape is a picture, so it takes a natural light near the page, never one hue over everything.
  Each panel names its light in `data-cx-scene` and its composition in `data-cx-params` (horizon,
  side, slope), so no two panels look alike:
  - `day`: a pale sky over hills that step down to a near slope; graphite hills under a warm accent,
    blue-grey under a cool one, the accent itself when it is green or neutral, deeper shades of the
    page colour on a colour page.
  - `dusk`: an evening as it looks: a deep blue sky that lights up in gold only along the horizon,
    dark hills with a lit crest, whatever the accent (a blue glow under a blue accent read as the
    `day` panel again, only darker); the gold leans toward a warm accent but stays between amber and
    gold (red-orange turns the crests rust). On a colour page, a light shade of the page colour.
  - `meadow`: daylight as a photograph shows it, whatever the page: a clear blue sky paling to the
    horizon, a blue far ridge, a sunlit field of grass (on a blue colour page the sky is the page colour).
    The natural picture among the panels, as on x.ai's cards; one per grid.
  - A grid of four mixes them: for example `day`, a grain, `dusk`, `meadow`.
- A grain panel: a light warm ground under a warm accent, a deep one under a cool accent, the page
  colour's own shades on a colour page.
- The window shows the feature with real labels: an invoice, a checkout, a list of payouts, an invite.
  Its content runs out through the panel's bottom edge: no empty space under the last row.
- Two panels at most run a short pointer demo (glide, click, the state changes, rest), one per row.
- Rejected: a small dialog centred on an empty ground; an orb or sphere ground; a landscape painted in
  the accent's hue only (it reads as a filter, and an orange accent turns rust-red); a warm accent mixed
  into a dark ground or a complementary accent mixed into a colour page (mud).

## Objects in dither (`fx-dither-object`)

A real thing built in code as a lit 3D form and printed in ordered dither in the page tones: ground,
shade, ink, accent and a deep accent. Use it when the product has no photograph yet, as the hero
picture or the visual of one split section.

- Objects: `headphones` (over-ear, on their cups), `chair` (an office chair on five castors),
  `camera` (a mirrorless camera with a zoom lens), `drone` (a camera drone with four rotors). Set
  `data-cx-object` on the figure.
- Idle: it sways slowly on its spot. Pointed at, it turns to the pointer, the light comes from the
  pointer, and it answers with its own working part: sound rings out of the cups, the seat swivels
  after the pointer (the base stays), the lens zooms out as the pointer rises and its focus ring
  turns, the rotors spin up into discs and the drone lifts off its legs and tips toward the pointer.
- The accent paints one part: the ear cups, the seat and back, the camera's body band and shutter,
  the drone's shell; their shaded side is a deep accent, never grey.
- Only an object the product really is or sells, on a tech page (a drone, a camera, headphones as
  hardware). One per page, with no caption under the stage: the section
  heading or copy says what it is and gives one real fact from the client.
- A product none of the four fits gets its own photographs or a render from `assets/objects`, never
  the nearest of these four and never mood stock in its place.
- The print is the render to use. `data-cx-render="studio"` (the same form as a smooth shaded render)
  is not for pages yet: at one sample per CSS pixel its edges stair-step, and next to a real product
  shot its forms read as toys. Never pick it for a shop or a product page; use the print, or the
  client's own photographs.
- Under reduced motion it is one still picture with no context and no pause button; without WebGL a
  line drawing of the same object, its accent part filled.
- It is a drawing of the product, never a filter: no photograph is ever dithered, halftoned or
  printed (in testing: a halftone over the hero photograph read as broken and low-res at every width).

## Street map of the place (`fx-map`)

A visit or contact section shows the real streets around the place, as a map app would, in the page's
colours: the judges marked a contour pattern standing in for a map as a fake drawing.

- **Bake once** at build time: `node assets/components/fx-map/bake.mjs --lat <lat> --lon <lon> --out
  map.json` fetches the streets, water, parks, rails and stations from OpenStreetMap (one request to
  an Overpass server) and writes a small JSON (about 55 KB, 18 KB gzipped, for 3 x 2 km of a city):
  streets in four classes, water (the sea built from coastlines too), parks, rails and trams, up to
  14 street names placed along the straightest part of each street. `--from none` (the default) leaves
  the walk out; only on a tech page whose brief names a station, `--from auto` (the nearest station
  150 m to 1.6 km away) or `--from lat,lon --from-name` adds the walk with its minutes at 80 m a minute. Paste the JSON inline
  (`<script type="application/json" class="cx-map__data">`) or name the file in `data-cx-map`.
- The part fits the pin, the walk and both names into the free part of the frame (right of the card
  from 900px of width; under 900px the card sits below and the map keeps the whole width), never
  closer than about 1 m a pixel; names go on the side the walk does not leave by (above or below on a
  phone). Street names show only where they fit their street and clear every other label.
- Light pages: white streets with a hairline casing on a land one step darker than the page. Dark
  pages: lighter streets on a land one step lighter. Water and parks keep a natural blue and green
  mixed into the land (natural colour, like the `meadow` landscape).
- Pointed at, or its directions link focused, the walk is drawn from the station to the door and the
  pin's halo answers once. Nothing moves at rest or on scroll.
- Drawn only for a street the brief gives; the pin sits on the street line, never on a building;
  the card says the walk in words ("5 minutes on foot from The Shore tram stop") and names street and
  district only (`copy.md`, Contacts). Get directions opens
  `https://www.openstreetmap.org/search?query=<street>+<district>`, never coordinates or a route
  link. On a place, and on any other page of kind other, it is baked with `--from none` (no walk, no
  minutes chip) and nothing moves. The coordinates go only to the bake, never onto the page. The
  OpenStreetMap credit ("Map data © OpenStreetMap contributors") joins the footer's one credits line,
  never on or under the map.
- No network at build time, or a street the brief does not give: no map; the visit shows its
  photograph. Never ship a contour or dot fallback as a map.

## A photograph with copy (`fx-photo`)

- The client's photograph in its natural colour, the copy on its calm, dark corner (white type, no
  scrim), as figma.com and x.ai show theirs; in a link it zooms 1.02 to 1.03 inside its frame
  (`motion.md`). Words on a photograph only in the hero and one band a page, never on a place.
- No filter over it: no halftone, dither, dissolve, print, duotone or blur (`data-cx-grade` stays
  off).
- The photographer's credit goes in the page's one footer credit line, never under the picture.
- It takes no dealt effect: its `effects` list is empty on purpose and `data-cx-effect` is ignored.
  No WebGL and nothing at rest; under reduced motion the zoom is off.

## The techniques (`components/shared.js`)

- `still(el, id)`: an effect that does not move, drawn once and kept as a picture (see Cost).
- `fill(el, id)`: the glyphs of `el` (or its `[data-fill]` parts) show the effect. The overlay sits
  next to `el`, never inside it, so the text and HTML stay clean. `{ still: true }` for a still fill.
- `windows(host, targets)`: one canvas seen through many shapes (chips, bars, cards).
- `cx-ring`: a host shown only in its padding, a 1.5px border of the effect.
- `cx-glow`: a host blurred into a soft light behind one object.
- `pauser(host)`: a round pause button in one corner of a looping visual. **Every loop that runs on
  its own for more than about 5 s gets one** (WCAG 2.2.2): the panel demos, the dither object, the
  prompt glow, the globe, the logo light, the call preview, the import preview. Under reduced motion
  the loops hold one state and the button is hidden. Stills (the map, the band) need none.

## When to use each

| Part | Use it for | Not for |
|---|---|---|
| `fx-feature-card` | A 2x2 of product features | Features with nothing to show in a window |
| `fx-dither-object` | The product as an object, with no photograph (the print render) | Decoration that is not the product; a studio render |
| `fx-headline` | The hero line or closing line; fill 2-3 words | Body text, two filled lines on a page |
| `fx-stat` | 2-4 proof numbers from the brief, at the stat size (`--t-stat`, 38 at 1440) | Small numbers, count-ups, invented figures |
| `fx-button` | The one primary call to action | Every button |
| `fx-prompt` | The hero prompt box of an AI or dev product | Ordinary forms |
| `fx-search` | Docs or command search | A field that always glows |
| `fx-tabs` | A product tour or dashboard preview | Navigation |
| `fx-icon-tiles` | A feature grid with drawn glyphs | Brand logos |
| `fx-spotlight` | A row of plain feature cards (security, admin) | A page with another pointer effect |
| `fx-globe` | Products with global reach | Local businesses |
| `fx-map` | Visit or contact: the real streets around the door, baked still | A product without a place |
| `fx-chart` | One metric over time | Decoration without numbers |
| `fx-bars` | Monthly figures on a labelled scale | More than 16 bars |
| `fx-photo` | The client's own photograph of the subject, in colour | Mood stock, blank notebooks, filters |
| `fx-avatar` | Calls, presence, a team list | Static team grids |
| `fx-pricing` | The recommended plan | All plans |
| `fx-progress` | Only inside a product window, as its own import or setup step (a UI fragment) | A progress bar as a card or visual of its own (the judge marks it); page loaders |

## Picking the effect

- **Panels in feature cards:** `painterly-landscape` (with a scene), `grain-gradient`;
  `ruled-grounds` for a technical product's panel that holds no UI (never behind a window or fragment, `cards.md`).
- **Inside letters and digits:** `silk-folds`, `aurora-curtains` (dark and colour pages), still. On a
  light page, stat digits get a plain ink fade instead (an effect in digits on white reads as scratched
  metal). Never `fluted-glass` in type: on a colour ground it paints thick accent bars through the
  letters. Never `caustics`, `halftone-screen` or `line-engraving` in type.
- **Inside small shapes** (chips, pills, bars): `grain-gradient` with still grain, low contrast. No
  silk, glass or metal sheen in a pill or a bar.
- **Inside data:** a plain accent fade under a line (the chart default) or a still `ruled-grounds`;
  bars take a still, low-contrast `grain-gradient`. Never an effect that draws its own grid or moving
  traces over a chart, and never `halftone-screen` in a chart area (its tone runs across the frame,
  so half the area goes empty).
- **A map** (`fx-map`) is the baked streets, never an effect, and has no fallback ground.
- Each part keeps a table of params per effect it takes and passes only that effect's own: one
  effect's numbers mean something else to another (contour-lines' opacity 0.32 and calm 0.55 left
  dot-terrain almost blank).
- **A button's fill:** an even, low-contrast grain that moves only while pointed at; no blobs that
  settle at one end of the button.
- When the page's deal gives an effect listed in a part's `meta.json` `effects`, use it there
  (`data-cx-effect`, `data-cx-fill` for type); otherwise its `default`. A part with an empty list
  (`fx-photo`, `fx-dither-object`) takes no dealt effect: a photograph is never filtered.
- Retired effects (`marble-warp`, `truchet-arcs`, `pixel-mosaic` and the others listed in
  `assets/effects/README.md`) are in no part's list. `grid-pulse` stays out of charts: its traces
  blink at random.

## Colour

Every part reads the page tokens. `inkPalette` draws an effect as ink (pale on dark pages, deep on
light ones); `accentPalette` keeps it near the accent with the label at 4.5:1; `tone(p, k)` matches
the CSS card steps. No fixed hues, with three exceptions, all natural colour as a photograph or a map
app would show it: the `meadow` landscape (a blue sky over grass), the gold horizon of `dusk` (the
other landscapes are built from the page's own hues and greys), and the map's water and parks (a blue
and a green mixed into the land). Never violet or lavender.

## Use

Link `system.css`, `components/base.css` and the part's `component.css`, paste its markup, then
`const part = init(root)` from its `component.js` (`part.destroy()` to remove). Text, controls and
data stay real HTML; the effect is the picture or the light on them. Replace every number, name and
the stand-in photograph with the client's own; a figure the brief does not give is left out, never
invented and never tagged "sample" (`copy.md`).



---

## `references/effects-objects.md`

# Objects and prints (`assets/objects`)

Thirteen objects in three families and one builder; each family's README is the contract, each `meta.json` the params.
`assets/objects/index.html` shows the objects; `product-render/views.html` the builder's three worked specs, every view at anchor scale.

| Family | Objects | What it is |
|---|---|---|
| Print objects | `print-cup`, `print-wheel`, `print-lamp`, `print-globe`, `print-cards` | a thing modelled in code: a studio render (default) or a print of it (halftone, engraving, dither); `_print-core/README.md` |
| Photo prints | `photo-halftone`, `photo-engraving`, `photo-dither` | one real photograph printed by a shader, the photograph under the pointer; `photo-kit/README.md` |
| Scenes | `split-reveal`, `dither-sequence`, `dot-object`, `exploded-layers`, `product-turntable` | photographs (the turntable: a generic form) through a print, alive under the pointer; `_scenes/README.md` |
| Product render | `product-render` (a builder, no fixed object) | any physical product composed from a JSON spec of its parts, rendered in real materials as a studio still (live only when asked); `product-render/README.md` |

## When to use one

- **One strong object moment a page.** Never beside a second effect or over a moving ground.
- **Place, service and every page of site-kind other** (cafe, guesthouse, shop, studio, clinic,
  product brand): no object, print or scene; plain photographs lead. House rule: shader
  effects only where the trade has a technical subject. The one exception is below: a physical
  product with no photographs shows its own render.
- **Product with photographs**: the photograph leads.
- **Any physical product without photographs** (a lamp, a chair, a bike, a stroller, a robot arm),
  of site-kind other or tech: **the product is rendered, never hidden** (in testing: a cargo bike's
  page that never showed the bike scored 3 of 10). The client's own render or CAD view comes
  first; else `assets/objects/product-render` composes this product from a JSON spec of its own
  parts, sizes and materials (Product renders, below) and it leads the hero (`deal.mjs --type
  product --has object`), then whole in at most two more sections, each a different view, big in
  its frame, never in a grey panel; its use (a scene whose setting fills the frame), close-ups of
  its parts and an exploded view carry the other sections (Views, below; `sections.md` section 1,
  One object, and Product, its seven rules). It is the product's picture, not
  an effect: on the page's flat ground or the lit ground on tech, stills by default, live only when
  asked (`data-product-mode="live"`), at most one live context, no print,
  no shader ground or moment beside it on site-kind other. A `print-*` object of the product's own
  kind (a lamp maker's lamp) may stand in for the spec; never an object of another kind (a wheel is
  not a bicycle), a drawn SVG, a model of loose primitives the helper did not compose, mood stock
  or another maker's product. **Hardware and devices too** (a robot arm, a drone, a camera, a
  sensor; in testing: a robot arm shown as a silk shader and an order form lost): with no photographs
  or client renders it takes its product render, `deal.mjs --type product --kind tech --has
  object`. A curved shell is composed of rounded boxes, cylinders and fillets at its real
  measurements; never a `split` hero holding only an order form, never an effect in its place.
- **A game without art files**: its key art is a product render of its hero object (the ship, the
  crane barge, the mech) or a scene of its world composed from its own objects on one floor, on the
  `product` stage (`deal.mjs --type software --kind gaming --has object`) and full bleed in the
  world section; an effect may sit behind it, never replace it (`sections.md`, Gaming).
- **Software, AI, games with art**: a print object as a print on the card it is about (a globe for
  regions); a game's own world object for `fixed-hero-object` (`scenes.md`).
- **Photo prints and the photo scenes** print a photograph, and no page prints, dithers or grades a
  photograph (`photos.md`, `effects-usage.md`): they stay in the kit's gallery, never on a page.
  `product-turntable` (a generic form, no photograph) is a technical product's object only when the
  form is its own.

## Mount

```html
<div class="panel"><div data-print="print-globe" data-print-place="card"
  data-print-params='{"effect":"engrave"}'></div></div>
<script type="module" src="assets/objects/_print-core/auto.js"></script>
```

(The kit's photo scenes mount the same way with `data-scene` and `_scenes/auto.js`, for the gallery
only; `data-scene` here is not a big scene, which is `data-big-scene`, `scenes.md`.)

- **Script**: `obj.mount(el, opts)` from `<id>/object.js`. Print objects take `{ place, params,
  palette }`; photo prints and scenes `{ src, params, palette }`. Controllers have `pause()`,
  `resume()`, `setPalette()`, `destroy()`.
- **Placement** (print objects): `card` large, cut by the bottom-left edge; `tile` whole, low in a square
  tile; `hero` right of centre in a wide frame. Never centred dead. Photo prints and scenes fill their
  box: give it an aspect ratio.
- **Palette**: the tokens `--bg`, `--surface`, `--ink`, `--muted`, `--accent`, or that object. After a
  theme switch call `setPalette(null)` (photo prints: `setPalette(fx.readPalette(el))`). The globe's sea
  is the accent: give it a blue or teal.
- **Pause**: a turning or looping object puts a round pause button in the panel's bottom-right corner
  once it has drawn. Keep that corner clear; one mover per group.
- **Credits**: photographs a print or scene shows go in the footer's one credit line (`photos.mjs
  credits --adapted`, `creditsLine()` in `photo.js`, `credits()` in `kit.js`). A render needs none.

## Product renders

`assets/objects/product-render`: the picture of a physical thing that has no photographs or client
renders: a product of site-kind other (a bike, a lamp, a chair), hardware (a robot arm, a drone, a
device) and a game's hero object or world without art files (`sections.md`, Product and Gaming).
`build.js` turns a JSON spec of the thing's own parts into a raymarched studio render (real
materials, soft light and shadows, a softbox in glossy parts, a floor shadow, the page's accent on
the parts that ask for it); `auto.js` mounts it; `make-posters.mjs` checks the spec and prints its
posters and stills. The README beside them is the full contract; `views.html` shows the three worked
specs in `specs/` (`city-bike` 64 parts, `desk-lamp` 19, `robot-arm` 28) in every view, a scene each
and two colour switches (`?only=bike|lamp|arm`, `?mode=still|live`); `demo.html` the turntable. Copy
their format, never ship one as the client's product.

### Mount

```html
<div class="frame" data-product="assets/objects/product-render/specs/<id>.json"
     data-product-place="stage"></div>
<script type="module" src="assets/objects/product-render/auto.js"></script>
```

- `data-product`: the spec's URL from the page; its posters sit beside it. Keep the spec under
  `assets/objects` (`make-posters.mjs` refuses one outside it), e.g. `product-render/specs/<id>.json`.
- `data-product-place`: only the share of the frame the product's own bounds fill, the tighter
  way, always centred in the frame (`build.js`): `stage` 0.86, `hero` 0.88, `tile` 0.84,
  `card` 0.9; `legacy` the old turntable right of the words in one wide frame. Unset: `hero` in a
  `.frame`, `card` in a `.panel`, `tile` in a square or portrait frame. No place lays words
  over the product or sets it beside them: the page's CSS gives the frame its size and position,
  and the words stand outside it. Use `stage` in the `product` hero's `.hero__stage` (`layout.css`
  3b: the stage across the wrap, the frame 7% past its top and bottom, so the product is as tall as
  the stage) and in a `split` or full-width frame; `tile` in a square or portrait tile. Every
  place is transparent over the frame's ground, the floor shadow included, and `layout.css` takes
  the `.frame`'s fill, border and padding off a `[data-product]` frame, so it stands on the page's
  ground with no panel.
- `data-product-view` (`three-quarter` default, `side`, `front`, `top`, a close-up), `data-product-scene`,
  `data-product-color` (a colourway id), `data-product-mode` (`auto` the still, the default; `live`
  only when asked; `image`, `still`),
  `data-product-fill` (0.3-1.2): Views, below. Changing `-color`, `-view` or `-scene` on a mounted
  frame shows that variant.
- `data-product-params` (JSON over the place's preset): `{"angle":-20}`, `{"step":0}` a lamp off, `{"size":0.7,"x":0.1,"y":-0.05}`.
- `data-product-palette`: `{ bg, surface, ink, accent }`; else the page's `--bg`, `--ink`,
  `--accent`. `aria-label` overrides the spec's `label`; the render sets `role="img"` with it (a button when a click
  switches it), which `product-shown` reads.
- Script: `import { loadProduct, checkSpec } from '…/product-render/build.js'`;
  `(await loadProduct(url)).mount(el, { place, params, palette })`. The controller: `pause()`,
  `resume()`, `step(on)`, `set(params)`, `setPalette(p | null)` (call `setPalette(null)` after a
  theme switch), `destroy()`. `auto.js` exports `products` (element to controller), `ready` and
  `mountAll(root)`. A spec that fails to load sets `data-product-error` on its element.

### Views (a different one in every section; the product whole in three at most)

All from the one spec, with the kit's own names (`build.js`, the three worked specs show each);
write each section's view on its plan line, no two alike (`sections.md`, Product: the six-section recipe names them: `side`, `three-quarter`, the use scene, `detail:<part>` or an `exploded` scene, a `rear-quarter` of the spec's own; whole views in three sections at most).

| spec key | what it gives |
|---|---|
| (none needed) | the standard views `three-quarter` (the spec's `angle`), `side` (a long product's widest: its hero), `side-left`, `front`, `rear`, `top`, `low` (only those the spec's `supports` lists); `detail:<part>[,<part>]` (or `detail-<part>`) frames the named parts and runs the rest off the frame: a close-up |
| `views` | the spec's own views, `{ "detail-saddle": { "part": ["saddle*", "seat post"], "angle": -42, "elev": 16, "margin": 1.3 } }` (`from` a standard view; a part name takes the parts it begins, `*` any) |
| `scenes` | the product in use or loaded: `{ "loaded": { "label", "hide": [parts], "props": [{ "prop", "at", "size", … }], "parts", "lit", "pool", "click" } }`. Props: `crate`, `bag`, `child-seat`, `bench`, `parcel`, `desk`, `book`, `mug`, `sheet`, `tray`; `lit` lights the props round a lamp. A scene shows the headline's promise at a size the section can read |
| `colors` | the colourways offered, `[{ "id", "name", "accent", "materials"? }]`: the accent re-lights the parts painted `"color": "accent"`, `materials` swaps others |
| `make` | what `make-posters.mjs` prints: `{ "variants": ["three-quarter", "side", "front", "detail-saddle", "three-quarter+loaded"], "grounds": ["light", "dark"] }` (`view+scene`) |
| a lamp's light | the spec's `click: "light"` and `pool`; `{"step":0}` off |

**Mount a view.** `<div class="frame" data-product="…/specs/<id>.json" data-product-place="stage"
data-product-view="side" data-product-color="blue">`. Once `make-posters.mjs` has run, every view is
its still by default: the `<img class="product-render__img">` it wrote,
`specs/stills/<poster>-<variant>-<colour>.webp` (`-half.webp` in its `srcset`, `-dark` on a dark
ground; `<poster>.stills.json` lists them with the box the product fills), placed so the product
fills the place's share: no canvas and no WebGL on the page. **Stills by default, live only when
asked (`data-product-mode="live"`), at most one live context:** `auto` (the default) shows the still
(run `make-posters.mjs` first: with no still made it would turn), `image` the still only, `still`
rendered once at the frame's size and kept as an `<img>`, its context freed, `live` the turn. A close-up (`detail-*`, `detail:<part>`) keeps the sides where the rest
of the product runs off at or past the frame's edge (the frame clips it), never a hard cut inside.
By script: `(await loadProduct(url)).mount(el, { place, view, scene, color, mode })`; the controller
adds `setView(v)`, `setScene(s)`, `setColor(id)` (a page's swatches use `data-product-swatch`, below, never this), `ready()`. **What a frame tells** checkers and
tests: `data-product-mode`, `data-product-state` (`image` | `still` | `live` | `poster`),
`data-product-view`, `data-product-color-shown`, and `window.__tpProduct` `{ stills, images, live,
freed }`; only `live` counts in `window.__tpGl`, and canvases inside a `[data-product]` frame are the
product's own render, never an effect.

**Big:** a render is transparent, so it stands on the section's ground at anchor scale, never in a
grey `.panel`: the place's fill is 0.84 to 0.9 of the frame (`size` 0.3 to 1.2 overrides it); in
the hero and one more section the product's long side is 80 to 100% of its frame, or a `detail:`
view runs it off the edges; in the `product` hero its widest view spans 80% or more of the wrap
at 1440 (`layout.css` 3b; the city bike's `side` 1046 of 1280, its `three-quarter` 818). **The colour swatch:** the order card's colour buttons or radios carry
`data-product-swatch="#hero-bike, #loaded-bike"` (the frames they drive; empty: every frame whose spec
has that colour) and `value="<colour id>"`; on click or change the frames swap to that colour's still
and a button group keeps one `aria-pressed`. No script of the page's own; or
`frame.dispatchEvent(new CustomEvent('product:set', { detail: { color } }))`, or set
`data-product-color`. Every colour offered shows once on the page. A still counts as the
render: one picture per view and colour (its `-half` file only in that picture's `srcset`), never
the same view twice on a page in two sizes.

### The spec

```json
{
  "id": "city-bike", "name": "City bicycle", "label": "A city bicycle with a front basket",
  "units": "m", "angle": -34, "turn": { "mode": "sway", "amp": 22, "period": 24 },
  "materials": { "frame": { "kind": "paint", "color": "accent", "finish": "gloss" } },
  "parts": [
    { "type": "wheel", "at": [-0.53, 0.35, 0], "r": 0.35, "spokes": 36, "wall": "#c7a57a" },
    { "type": "tube", "from": [-0.07, 0.29, 0], "to": [-0.23, 0.81, 0], "r": 0.017, "mat": "frame", "blend": 0.01 }
  ]
}
```

- **Axes**: x the product's front, y up, z across (toward the viewer at angle 0). Any unit; the
  model is scaled so its largest side is one unit and set on the floor at its lowest point. Model
  from real measurements: proportions are most of what makes it read as the thing.
- **Keys**: `id`, `name`, `label` (what a screen reader hears), `poster` (the posters' file name,
  default the id), `angle` (rest and still turn, default -32, a three-quarter view), `turn`
  (`{"mode":"sway","amp":26,"period":22}` default, `{"mode":"spin","speed":10}`,
  `{"mode":"still"}`), `camera` (`{"elev":12}`), `click: "light"` (a click switches every `light`
  material and `glow`; it starts on), `pool` (`{"at":[x,0,z],"r":0.2}`: its light on the floor),
  `materials`, `motion`, `parts`.
- **Every part** takes `mat` (a name or an inline material), `blend` (a fillet in units where it
  meets the parts before it: welded tubes, a cast body), `in` (a motion group), `name`. It is placed
  by `from` + `to` (a linear part between them; `up` turns its section) or by `at` with `axis`
  (`"x"`, `"y"`, `"z"` or a vector) and/or `rot` ([x, y, z] degrees). `seams` on a tube, beam, box or
  cylinder (heights -1..1 along its half length, `seamWidth`, `seamDepth`) cut panel lines: a robot's shell, a base's groove.

| type | sizes | for |
|---|---|---|
| `tube` | `r`, `r2` (taper), `cap` `flat`/`round`, `round` | frame tubes, posts, rods, a tapered robot link |
| `beam` | `w`, `d`, `round` | flat bars, cranks, rails, a drone's arms |
| `box` | `size` [x,y,z], `round` | housings, bodies, pedals, grippers, crates |
| `panel` | `size` (thin) | plates, lids, a screen's back, a hull's deck |
| `cylinder` / `disc` | `r`, `h`, `round` | bases, hubs, motors, lenses, rotors |
| `sphere`, `ellipsoid` | `r` / `size` | a bulb, a bell, a knob, a buoy |
| `torus` | `R`, `r` | rings, a chainring, a status light |
| `joint` | `r`, `w`, `capMat` | a hinge knuckle about `axis` (default z) with caps |
| `wheel` | `r`, `tyre`, `rim`, `hub`, `spokes`, `spokeR`, `style` `spoked`/`disc`/`solid`, `wall`, `rimMat`, `hubMat`, `spin` | bikes, strollers, carts, casters |
| `shade` | `from` (closed) `to` (open), `r1`, `r2`, `t`, `bulge`, `innerMat` | lamp shades, bells, horns, a speaker cone |
| `seat` | `size` [length,height,width], `style` `saddle`/`cushion` | saddles, seats, cushions |
| `basket` | `size`, `style` `wire`/`slats`/`solid`, `pitch`, `wire`, `rimMat` | baskets, crates, bins, trays |
| `arc` | `R`, `a0`, `a1`, `r` or `size` | mudguards, handles, hoops, bent frames |
| `spring` | `from`, `to`, `R`, `r`, `turns` | springs, coiled cords |
| `path` | `points` (2 or more), `r`, `smooth` | handlebars, cables, bent tubes, a crane's rope |

- **Materials**: a name from `materials`, a built-in name, or `{ "kind", "color": "#hex" |
  "accent", "finish": "gloss" | "satin" | "matte" }`. Kinds: `paint` (`color: "accent"` takes the
  page's accent), `metal` (brushed alloy), `chrome`, `steel` (dark stainless: spokes, wire),
  `rubber`, `plastic`, `wood` (rings; `grain`, `scale`), `fabric` (`weave`), `leather`, `light`
  (gives light; switches with `click`). Any material takes `glow` 0..1 (a lit inner face).
  Built-in names: `accent`, `paint`, `white`, `black`, `graphite`, `alloy`, `aluminium`, `chrome`,
  `steel`, `rubber`, `plastic`, `wood`, `oak`, `walnut`, `fabric`, `leather`, `light`.
- **Motion**: up to four groups, `{ "id", "parent", "pivot": [x,y,z], "axis", "amp", "period",
  "phase", "rest" }`; a part joins with `"in"`. Each turns about its pivot (given at rest, in the
  spec's units) by `rest` + `amp` x a sine of `period` seconds, after its parent (a robot's yaw,
  shoulder, elbow, wrist). Joints move only while the product turns.

### Posters

Run after every change to a spec, on a free port (default 5905 and the 4
after it):

```bash
node assets/objects/product-render/make-posters.mjs <spec.json> --profile <own chrome dir> --port <port> [--variants side,detail-saddle,three-quarter+loaded] [--grounds light,dark] [--px 1100] [--legacy]
node assets/objects/product-render/make-posters.mjs --check <spec.json>     # spec, views, scenes and shader, no browser
```

It exits 1 on a fault (an unknown part type, prop or material, a view or scene naming a part that
is not there, an `in` naming no group, more than 90 parts, a shader word a laptop GPU rejects),
else, in one headless, software-rendered Chrome, writes for each variant (`make.variants` or
`--variants`) and ground `<poster>-<variant>.fallback-render[-dark].png` (its poster), one
transparent still per colourway in `stills/` and `<poster>.stills.json`; `--legacy` adds the old
turntable posters. The poster shows at once and stays for good when WebGL2 is missing, a shader
fails or a frame comes out empty; a spec without posters shows nothing until WebGL draws. One to
four minutes a variant for 60-90 parts on a CPU renderer (20-30 parts: under a minute); each variant
is written as soon as it is made, so `--timeout <minutes>` cuts a run without losing the done ones,
and `--variants` with a part of the list keeps a run short (the manifest is merged). `--quiet`
leaves out the file lines.

### Limits

- **Stills by default, live only when asked (`data-product-mode="live"`), at most one live
  context:** run `make-posters.mjs` so every view has its still (with none made, `auto` would
  turn); the one live render, when asked, counts in the page's four contexts (`window.__tpGl`). Phones (max-width 700px or a coarse
  pointer) and reduced motion get one sharp still frame and the context freed. A turning product
  has a pause button in its frame's bottom-right corner.
- **Cost**: every part is evaluated per ray step (skipped when its bounding sphere is beyond the
  nearest hit). About 20 parts costs like a print object; 60-70 is fine on a laptop GPU, slow on a
  CPU. Keep a spec under 90.
- **It cannot**: text or logos on the product, transparent glass, cloth that drapes, a freeform
  organic shell (a shoe, a car body, a face, a creature), anything thinner than about a texel (it
  is thickened). Those need the client's photographs or renders; a game composes its machines,
  buildings and props, never a character. A hard device shell (a drone, a camera, a sensor) is
  rounded boxes, cylinders and fillets at its real measurements, never a reason for a `split` hero
  with only an order form.
- **Craft**: include the details that name the thing (a bike's spokes, chain, mudguards, saddle
  springs; a lamp's springs, knobs, cord; a robot's caps, seams, gripper pads; a barge's bollards,
  cables and lamps). Accent on the part a maker would paint; metals and rubber stay themselves.
  Check it at 1440 and 390 before it ships.
- **Never** a product of another kind, never on a place page, never captioned or called a render,
  model or illustration on the page; it is the thing's picture, not an effect (on tech an effect
  may sit behind it, never beside it as a second beat).

## GPU cost

| Family | Class | Contexts |
|---|---|---|
| Print objects | high per frame (raymarch), only while it moves near the screen; at rest one sharp frame, kept | share 2 |
| Photo prints | low, still at rest | 1 each, at most 3 |
| Scenes | low, drawn only while moved or stepping | at most 2 |
| Product render | none for its stills (`<img>`); `still` mode one render, then freed; `live`: high per frame (raymarch, cost grows with parts), only while it turns near the screen | 0 (`live`: 1) |

With the page's grounds and effects: **at most 4 live WebGL contexts**. Freed off screen and in a hidden
tab; one still frame under reduced motion.

## Never

- **Captioned.** No line under a render or print explaining or apologising ("made in code", "a
  stand-in"). The heading says what the thing is; credits go in the footer.
- **Animated on scroll,** except inside the dealt big scene (`fixed-hero-object`,
  `object-through-giant-type`). Elsewhere only its own slow turn, the pointer and a click.
- **Over the hero photograph**, or in place of the client's photographs.
- **Empty.** A failed shader or missing WebGL leaves its poster. After a shader change run
  `_print-core/lint-glsl.mjs` and `_scenes/lint-glsl.mjs`: no GLSL ES reserved words as names. A
  product spec: `product-render/make-posters.mjs` (the check and the posters in one).



---

## `references/effects-usage.md`

# Effects usage

Who gets effects, how many, how they are dealt and where they sit. An effect is anything a shader,
canvas, WebGL, a print pass or a scroll drive makes: effect grounds (`data-fx`, `assets/effects`),
the WebGL creative parts (`effects-creative.md`), objects and prints (`effects-objects.md`), big
scenes (`scenes.md`), moments (`moments.md`), a film or 3D hero and timed loops. `cards.md` wins on
any card detail; `motion.md` holds every timing.

## The gate (house rule 8)

Effects are for site-kind tech, software and gaming (AI and developer tools count as software) and
for a product page with a technical subject (hardware, devices). Never on a place, an ordinary
product brand or shop, a service firm, an agency or a studio: they are site-kind other.

On other, photographs, type and flat colour carry the page. Banned there: canvas and WebGL, autoplay
video, any CSS gradient (grounds, panels, glows, scrims), SVG pattern or texture grounds,
`backdrop-filter` (the nav too), `filter`, `mix-blend-mode`, `mask-image`, glass, grain, halftone,
dither, duotone, print, `[data-fx]`, `[data-print]`, `[data-scene]`, `[data-big-scene]`,
`[data-moment]`, `[data-ui-loop]`, `[data-m-loop]`, `[data-m-count]`, SVG animation, GIFs, Lottie, a
custom cursor and any scroll or animation library. Allowed: `fx-map` baked still, `fx-photo` as a
plain photograph, real icons, a still diagram (not on a place), and on a physical product with no
photographs its own product render (`[data-product]`, `effects-objects.md`): the product's
picture, not an effect: stills by default, live only when asked (`data-product-mode="live"`), at
most one live context, on the flat ground, its poster beneath.

## What each kind gets

| | tech | product, service (other) | place |
|---|---|---|---|
| Lead picture | the client's UI (hardware: its photographs or render, else its product render, never an effect or an order form alone; a game: its name and its art, else its key art rendered with the product-render helper, an effect at most behind it) | its photographs; a product without them: its product render | its photographs (a remote place: its region's landscape) |
| The one effect | a live ground, a WebGL part, an object or a big scene | none | none |
| Card panel grounds | one card group, still, from the effect's family; with a big scene the lit ground (`data-ground`), no `data-fx` | the client's photograph | none |
| Moments | up to 2 in sections, at most 1 in the hero | none | none |
| Big scene | 0 or 1 (it is the effect) | none | none |
| Diagram cards | 0 to 2, pulsing | 0 or 1, still | none |
| Loops | one timed loop, one per card group | none | none |
| CSS grounds | 0 to 2 (`backgrounds.md`) | flat tokens | flat tokens |

**The subject before the effect** (in testing: a robot arm shown as a silk shader and an order form,
and an unnamed game shown as an abstract effect, both lost to pages that showed the thing). An
effect never stands where the product, the device or the game's world should be. Hardware with no
photographs or client renders, and a game with no art files, take a product render
(`effects-objects.md`, Product renders) as their picture: the hardware itself, the game's hero
object or a scene of its own objects, whole on the stage and full bleed in the world section. The
render is the picture, not the effect: the page's one effect may sit behind it as the stage's
ground (every render placement is transparent over its frame), counts as the beat and shares the
four contexts with it; it never replaces it and never sits beside it as a second focal visual.

Every visual that is not the effect, a card ground, a moment, the scene or a product render is a
real UI capture or a real photograph. A photograph is never filtered, printed, dithered or graded on any page.

## Tech budget

- **One effect:** one live ground (the hero ground, or a ground inside the one framed
  `[data-visual]` window under an h2), or one WebGL part (an `fx-*` that holds a context: the button
  fill, a search or prompt glow, the edge-glow plan, spotlight, globe, avatar, logos, progress,
  dither object, filled headline or stat), or one object, or one big scene. A grain, dither or
  texture CSS ground counts as it. Never in a fixed layer, never behind body copy, never a
  page-long canvas; a 3D world lives in the hero only.
- **Card grounds** (house rule: "gradients and effects ... as a card's background with a smaller
  card of text or UI on top"): one card group may hold quiet grounds from the effect's family,
  drawn once and held as pictures (system.js frees their contexts); not a second live effect. With
  a big scene there is no `data-fx` outside a moment (the checker FAILs it, MO-16, MO-23): the card
  panels take the lit ground (`data-ground`).
- **Moments** (house rule): up to two section moments that may follow the scroll (letters, liquid,
  a section transition, a counter, a marquee row), each in its own section, and at most one
  non-scroll moment (load, hover or click) in the hero or `[data-visual]`, never in or beside the
  scene's section; two moments in all at most. A moment built as an `fx` part carries its own `data-fx` id on its
  own section; it is not a second ground.
- **Beats:** the effect, the scene and the moments are the page's beats, up to three on tech. Name
  each and its section in the plan; never two in one section or in neighbouring sections; a calm
  section between them; the back third of the page calm before the close. CSS grounds, card
  grounds, diagrams, card loops and hovers are not beats.
- **One pointer effect** a page: a hover or liquid moment, `fx-button`, `fx-spotlight` or an object
  that turns to the pointer, never two. Never a replaced cursor, never a magnetic button.
- **At most four live WebGL contexts** at once (house rule): the effect plus the moments' own canvases;
  `perf.mjs` fails above four.

## Deal the effect, never by taste

`node <skill>/scripts/effects.mjs list` shows each id with its family, `quiet` or `focal`, and its
slots. `<kind>` is the page's ground: `light`, `dark` or `colour`; `<site-kind>` is software, gaming or tech.

```bash
# the effect: an effect hero takes --slots hero; a photograph or UI hero puts it in the one [data-visual] frame: --slots band
node <skill>/scripts/effects.mjs pick --page <site-kind> --palette <kind> --slots hero --quiet --seed <S> --history .taste-skill/effects-history.json
# one card group's still grounds, same family (a pattern or dither effect: --family mesh)
node <skill>/scripts/effects.mjs pick --page <site-kind> --palette <kind> --slots card --family <the effect's family> --exclude <the effect>,<NOUI> --quiet --seed <S> --history .taste-skill/effects-history.json
```

`--quiet` leaves out only the focal grounds, not the patterns. When the slot holds UI (a window, a
fragment, a card group), add the patterns and prints to `--exclude`; `<NOUI>` is
`ruled-grounds,grid-pulse,contour-lines,dot-terrain,dotted-globe,ridgeline,halftone-screen,bayer-dither,ascii-shade,line-engraving,duotone-grade`.

- **Quiet** grounds are an even field that holds UI (`grain-gradient`, `painterly-landscape`,
  `gradient-mesh`, `silk-folds`, `fluted-glass`): a soft field behind UI, never a pattern. **Focal**
  grounds have a subject (`orb-sphere`, `spotlight-cone`, `god-rays`, `aurora-curtains`,
  `caustics`): alone in the hero, nothing over them.
- Two ids a page at most outside the moments; each panel its own `data-fx-seed`. No echo of the
  effect in the close, no pattern panel, no focal tile. `dotted-globe` only by name, for global
  reach, as the effect; `duotone-grade` never on a client's photograph. If `pick` says nothing fits
  a slot, drop the slot.
- A visual on `.ground-inverse` takes an id made for that kind (`--palette dark`).
- Retired or renamed ids never appear: `mesh-gradient` is `gradient-mesh`, `iridescent-foil` is
  `fluted-glass`; `riso-print`, `paper-texture` and `liquid-chrome` are gone.

## Deal the moments and the scene

**Moments** (0 to 2): dealt with `moments.mjs pick --page <kind>`, the excludes and the hero rule
exactly as `moments.md` (Deal them) says; pass the scene and the effect so the WebGL total stays
within four. Never a moment in the scene's section or beside it.

**Big scene** (0 or 1, the page's effect): one at random from the scenes whose `types` in
`assets/scenes/index.json` hold the page's site-kind and whose `needs` the brief meets (the table in
`scenes.md`), away from the last three:

```bash
node -e "const fs=require('fs'),f='.taste-skill/scenes-history.json';let h=[];try{h=JSON.parse(fs.readFileSync(f))}catch{}const a=process.argv.slice(1),k=Math.min(3,a.length-1),p=a.filter(i=>!(k?h.slice(-k):[]).includes(i));const id=p[Math.floor(Math.random()*p.length)];fs.mkdirSync('.taste-skill',{recursive:true});fs.writeFileSync(f,JSON.stringify([...h,id]));console.log(id)" <the fitting ids>
```

When the dealt scene's `needs` turn out unmet, deal again without that id; none when no id is
left. A scene is the hero only when its `restH` is 1; the three hero scenes rest in two screens
today, so they go below the dealt hero as a two-screen section (`scenes.md`, Who gets one). Never
a scene with a moment its `avoidMoments` (in `index.json`) lists, or with its twin: pass the scene
as `--scene <id>` to the moments deal, and `pick` leaves out its avoidMoments and twins itself.
Markup and checks: `scenes.md`.

**Its height (rule 3):** `{"hold": 1}` and `--h` = the scene's `restH`, as `scenes.md` (Its
height) says; no page CSS; the scene's section stays one or two screens like every other.

## Where things sit

- **The effect:** the hero (`.frame.frame--hero` holding a `.stage.stage--fade-b`, or the hero's
  layer), or the one `[data-visual]` frame under an h2 (a window up to 1280x540 at 1440, 342x256 at
  390), or the scene's own section. One `[data-visual]` a page. A hero with an effect in a frame is
  a 5/7 or 6/6 split with the visual right, or moves the effect to its own section; an effect as the
  hero's layer (a game's world, a focal ground) keeps the words on its calm part at 4.5:1.
- **Split frame:** `.frame.frame--split` holding a `.stage`; a window `.at-corner.to-edge` at 56/56,
  cut by the right and bottom; a second piece (`cursor`, `notify`) only over a window's lower-right
  edge (`.at-over`), hidden from 1024 to 1279 and on a phone. Text and UI never share a half.
- **Card panels:** `cards.md` (the panel, the fragment on it, fades, the lit palettes, the loop).
- **Text over an effect** only on its quiet part at 4.5:1 or more; a noise or fog ground never holds
  content.
- **Video** (tech, hero or `[data-visual]` only, as the effect or loop): muted, inline, poster
  first, a 6 to 12 s loop or a story that plays once and holds its last frame, a pause button,
  separate phone and desktop files. On other a still that opens the film on a click.
- **The lit ground** (`<html data-ground>`, tech): system.js gives it to every ground that holds UI,
  so page, card, panel and UI are never four near-black layers.

## Motion and cost

- The effect reacts to the pointer or to time (the scene and a moment may react to scroll); after
  assembling it holds, with no constant churn; ambient cycles 4 s or longer, a drift of a few px a
  second, 2 to 10% of pixels changing in 0.9 s; it is still at rest or has a pause button; it shows
  a poster first and a still fallback under reduced motion, on a phone and when WebGL fails. Never
  sound on entry; pointer play off on touch.
- Draw an effect 20 to 25px larger than its box and clip it. One sample per CSS px or less (0.75
  when large), about 1.5 megapixels, pixel ratio 1.5 at most; noise, particles and ray marching at
  half resolution and 30fps or less. A noise ground is one baked texture drifting on time; a caustic
  net is its flat floor net only.
- Blend modes only for a job inside the effect (a glint), never on text. No glass or frosted look on
  any kind: a menu curtain is a flat 40% dim.
- system.js mounts grounds (`ui.grounds`), never `fx.mountAll` from a page script. After any shader
  change run `lint-glsl.mjs` in `assets/objects/_print-core` and `_scenes`: never a GLSL ES reserved
  word (`flat`, `smooth`, `sample`, `filter`, `input`, `output`...) as a name; every WebGL piece
  shows its still fallback when its shader fails. Speed: `perf.md`.

## Never

- An effect, print, grain, gradient or WebGL on a page of kind other; an effect where a photograph
  belongs.
- A print, dither, grade or filter over a photograph, on any kind.
- A live effect or a moving canvas inside a card; a card that animates on scroll.
- A caption explaining a visual (credits go in the one footer line); blinking or random effects;
  violet or lavender.
- A site's code, assets or signature device copied: take only the generic idea, built from the
  skill's own scenes and moments with the client's content.



---

## `references/icons.md`

# Icons

A page that names a tool shows that tool's real logo, in its own colours. A file card that says Google Docs
carries the Google Docs icon, a Word file the Word file icon. Never draw a look-alike, never put a letter in a
circle or a generic page glyph where a real icon exists. A fictional client's own mark is designed, never borrowed.

`scripts/icons.mjs` is the one resolver. Pages, `diagram.js` and every other part read the SVG files it writes;
nothing fetches, tints or judges an icon at runtime, and no page calls a CDN for an icon.

## Where they come from

| set | source (pinned) | holds | drawings licence |
|---|---|---|---|
| `logos` | `cdn.jsdelivr.net/gh/gilbarbara/logos` at commit `d6960edc1b73` (26 Oct 2026; the repository has no tags) | about 1,500 brands in full colour: the first choice | CC0 (LICENSE.txt at the commit) |
| `si` | `simple-icons` 16.30.0 | one-colour marks painted in the brand hex: the fallback, only where no colour mark exists | CC0 |
| `file` | `@iconify-json/vscode-icons` 1.2.30 | file types in colour (pdf, markdown, zip, Word, Excel, PowerPoint): a document type, never a brand | MIT |
| `ui` | `@iconify-json/lucide` 1.2.100 | interface glyphs, one line set | ISC |

`si` is used for Google Docs, Sheets, Slides, Forms, Chat and Tasks, Calendly, Evernote, QuickBooks, Revolut and the
console and game-store marks (PlayStation, Epic Games, Riot, Battle.net, itch.io, Roblox, EA, Ubisoft, Rockstar, Valve,
CurseForge, Modrinth, GOG). Xbox and Nintendo are in no permitted set: name the console in type, never a drawn
mark; a game's store row is Steam, PlayStation and Epic Games (`apps --tag gaming`). The Google editors are in their brand blue, green and yellow; the Microsoft Office
marks exist in no permitted source, so a Word, Excel or PowerPoint file card uses the file-type icon (`docx`, `xlsx`, `pptx`).

**theSVG (the `brands` set) was dropped.** Its package is MIT, which covers the compilation only; the licence it
records per mark is its own label, not a grant by the owner, and 37 of its Microsoft marks say "no express redistribution
licence supplied". A press-kit download is not a path this skill takes. `brands:` ids now fail with a message that says so.

Every mark is still its owner's trademark: nominative use only. Name tools the product really works with, never imply
endorsement. The footer carries "Product names and logos are trademarks of their owners" and the site carries
`icons-credits.json` (file, set, source with the commit, licence, trademark flag, the brand's site).

## Commands

`node <skill>/scripts/icons.mjs ...` from the site root:

- `find google docs`: what matches, in every set, with licence.
- `apps --tag gaming`: the curated list, 458 apps and 38 file types by short name (`google-docs`, `steam`, `pdf`);
  `list --tags` shows the tags (dev, ai, gaming, engine, hardware, chips, cloud, db, monitoring, payments, social ...).
  Interface glyphs: `list --set ui --tag gaming` (435: gamepad-2, swords, microchip, circuit-board ...).
- `fetch google-docs slack file:pdf2 ui:arrow-right --out assets/icons`: writes the files, prints the tags to paste.
- `scan index.html --out assets/icons`: fetches every icon a page names (diagram specs, `data-diagram` preset names, `data-icon`).
  Run it last, so a finished page has no missing icon.
- `check`: does every entry resolve; lists wordmarks, one-colour fallbacks, black and violet marks.
- `measure`: maintenance. Measures every colour mark's drawn box in headless Chrome (CPU flags, closed by its own PID) into
  `index.json` `boxes`; `fetch` crops to it. Run it when the curated list changes (`--profile <dir>` sets the Chrome profile).
- From code: `import { resolveIcon } from './icons.mjs'`.

Each written file carries the decision: `data-ic="violet"`, `"ink"` or `"paper"` on the root, so `diagram.js` and any page treat it
as `icons.mjs` printed it.

## Which one

- Brand or file type: the colour icon, from the curated list first (`logos`), a `si` mark only where the list says so.
- Interface glyphs (search, arrow, check, a feature point): `ui:` only, never a second line set. A glyph is an inline svg and takes the text colour.
- One-colour (`--mono`) is better in a row of customer logos, in footer social links, and where a brand has no colour version.
  A multi-tone mark keeps its detail in one colour: its paper-coloured parts are cut out of the silhouette instead of filling solid.
- Black marks (GitHub, Apple, X) carry `ic-ink`: icon.css turns them white on a dark ground. A wordmark-only logo (Stripe, NVIDIA, Go)
  carries `ic-wide`: print it with `--tile`, which gives it a wide tile.
- Light marks that vanish on a light tile are not in the list (Wise, Klarna were dropped for it).

### The violet rule (a judgement, stated)

"Never violet or lavender" is a rule for the page's own design. A third-party logo is its owner's mark and is not
recoloured, but a block of violet breaks the palette. By the share of coloured fills that are violet (`check` prints it; deep navy is not violet):

- Half or more (Stripe, Twitch, Google Forms, Terraform, Datadog, ClickUp, Loom, Kotlin, C#, .NET, Bootstrap, ESLint ...): flagged
  `[violet]`. A tool the product really works with keeps its own colours: `fetch` or `scan` it with `--colour` (without it the mark
  prints in the text colour, and a grey stand-in of a known logo is a fault). The violet ban covers the page's
  palette, never a third-party logo; `--mono` only for a row of customer logos.
- Under half (Figma 20%, Google Drive 14%): printed as drawn; the real logo is what makes the page look official. `--mono` prints it in one colour.

## How they sit

Link `assets/icons/icon.css` after system.css. `.ic-tile` is the soft tile behind a logo (a light tile on a dark
ground, so every colour reads); `.ic-row` a list row; `.ic-chip` a name with an icon; `.ic-stack` overlapping
tiles; `.ic-grid--mosaic` with `.ic-cell` an integration grid; `.ic-file` and `.ic-file--tile` a file card;
`.ic-point` a glyph with a short text. Sizes 16, 20, 24, 28, 32, 36, 40, 48, 56. Nothing animates. `assets/icons/demo.html`
shows the mosaic, the file cards, all 458 tools by kind, a dark page and the glyphs (every icon sits in `assets/icons/demo/`).

Shapes: `fetch` crops a mark to its measured drawing (2% margin) and gives it a shape class from the cropped proportions:
`ic-wide` (over 1.8:1), `ic-land` (over 1.25:1), `ic-tall` (under 0.8:1: Google Docs, Figma). A tile sizes a landscape mark to 70% of its
width and a portrait one to 68% of its height. The `file` set is not cropped on purpose.

File cards, integration grids and "reads from" lists use real icons at 20 to 40px, never a grey box. A logo keeps its own
proportions and colours.



---

## `references/layout-v4.md`

# Layout: one section per screen, equal edges, heroes, type

The layout spec for every page (house rules 3, 4 and 6). `system.css` implements the tokens, the
section box, the grid and the hero frame; `assets/layout/` holds the heroes (`layout.css`,
`layout.js`, `heroes.json`, `hero-<id>.html`), the hero dealer (`deal.mjs`) and the check
(`layout-check.js`, `check.mjs`). Link `layout.css` after `system.css`, `ui/cards.css`,
`motion/motion.css` and (tech) `backgrounds/backgrounds.css`; load `layout.js` after `system.js`
(`starter.html` does both). Tokens, buttons and the nav: `system.md`.

## 1. What the good sites do

- figma.com and x.ai (the reference recording): the hero fills the first screen and nothing of the next
  section shows at load; sections hold 0.45 to 1.25 screens of content with about a quarter screen
  between them. Both still show a neighbour in a shot of one section: the look the house asks us to go
  past.
- A study of 327 sites at 1440x900 and 390x844: the hero is alone on the first screen on 78% of
  company sites; a section shows alone more often the taller it is (0.29 under 0.6 screens, 0.80
  at 0.95 to 1.1) and the wider the gap (0.42 under 60px, 0.82 at 220px and more). Its place sample
  holds no local shops, so the place numbers below are the house's own ask and taste, not measurements.
- So the look comes from heights and padding only: every section is exactly one or two screens.

## 2. One section per screen

**The judge tile.** The "shot" is the screen at scrollY = k x H (k x 900 at 1440x900, k x 844
at 390x844). Every tile shows exactly one section, the hero included. Plan the page as a list of
screens before building. `html { scroll-padding-top: 0; scroll-behavior: auto }`, so an anchor jump
lands on a tile (the fixed header covers the top of the section's padding).

**The shell.** `body` renders only `header.nav`, `main`, `footer.closing` and, on a phone,
`nav.actionbar` (plus script, style, template). No popups, newsletter modals, chat bubbles, help
pills, back-to-top squares, badges, award strips or asks in a modal; nothing else is fixed.

**The section box.** `main > section` and `footer.closing` are `height: calc(var(--h,1) * 100svh)`,
padded `--padt` above and `--padb + --bar` below; `--h` is 1 or 2. Under 640px non-hero sections use
`100lvh` and `--hm` (set it when stacking makes the content taller). `.wrap` is a section's only
in-flow child (`z-index: 1`); a layer sits beside it. Never `min-height` alone, never `dvh`, never a
third screen, never a height set by script.

```html
<section class="section" id="features" style="--h: 2"><div class="wrap"> the h2 first, then the content </div></section>
```

**Content windows** (content height c, the h2's top to the last content's bottom; one screen holds
708px at 1440x900, y 120 to 828):

| c at 1440x900 | Screens |
|---|---|
| under 360 | merge into the section above, or add the picture it lacks |
| 360 to 495 | one screen, a warning: give it its picture |
| 495 to 708 | one screen |
| 708 to 1,320 | no height fits: cut to 708, split into two sections (each 495+ with its own h2), or `.g2` |
| 1,320 to 1,608 | two screens (1,200 to 1,320 warns) |
| over 1,608 | split |

At 390 (`--padt` 96, `--padb` 48 plus the bar): one screen holds 464 to 700 - bar, two hold 1,268
to 1,544 - bar; between, use `.g2m` or cut the phone copy. Split or cut a long feature grid; never
shrink it.

**The tablet (640 to 1023; the judges hold it upright at 768x1024 and 820x1180).** There the box
grows past its screens rather than overlap, so a section a little too tall pushes every later
section off the screen grid and each tile shows one section's tail and the next one's head, cards
cut by the tile's edge (seen at 768). Stacked content c at 768x1024 (the stricter):

| c at 768x1024 | Do |
|---|---|
| up to 832 | one screen |
| 832 to 1,130 | cut to one screen: a lower `--p-h` for the group at tablet, the split's frame as `.fill` (it takes what is left), the grey line or a fourth card out |
| 1,130 to 1,856 | two screens there, `@media (min-width: 640px) and (max-width: 1023px) { #<id> { --h: 2 } }` (the one page-CSS rule on a section), no card row across the screen line at 1024 |

Run `consistency.mjs` with `--rhythm-widths 1440,820,768,390`: its SR-2 `section-height` then
fails a section that is not one or two screens at the tablet too (the default runs 1440, 768 and 390; this adds 820). The system's 48px tablet gutter is right: never widen it.

- **Two screens as two groups:** `.g2` (or `.g2m`, phone only) makes the `.wrap` two rows, each at
  most 708px; row 1 holds the h2 and the first group (360 to 708), row 2 the rest (420 to 708) with
  no second h2, starting `--padt` under the second screen's top, so the second tile looks like any
  other section. A total of 708 to 780 has no legal height: add or cut up to 72px.
- **Top-aligned:** the one h2 is the first content, `--padt` (120, 96 on a phone) under the section
  top, 48 under the header in the tile, like the hero's h1. Never centre content vertically; never a
  second h2.
- **Fill** 0.55 or more; the gap to the next content is then 2 x padding at least (192px; 144 + bar
  on a phone). A short block is merged or given its picture, never centred alone in an empty screen.
  A quote, logo row, stat row or FAQ that alone holds under 495px (464 at 390) merges into the
  section above as its last element, with no heading or ground of its own. No strip sections.
- **Separation** by a full-width ground change or space only: no rules, shadows or inner hairlines
  between or inside sections, and no inset coloured box standing in for a ground. A list may close
  each row with a 1px rule inside the content edges.
- **The close and the footer are one section,** `footer.closing` (one screen; `.g2m` allowed on a
  phone): `footer.closing > .wrap` holds exactly two children, row 1 the dealt close and row 2 the
  links and the legal row. No separate closing band.
- **No scroll tricks:** no scroll-snap, scroll-jacking or smooth-scroll library. The one exception
  is tech: the big scene and a dealt scroll moment run inside their own section (`data-big-scene`,
  `data-moment`), which stays exactly 1H or 2H (a scene with `{"hold": 1}`: two screens live; its
  composition at rest one or two, `scenes.md`, Its height); they may pin only with
  `position: sticky` inside that box. Nothing else on any page is sticky.

## 3. The hero

- **Exactly the first screen,** `100svh`, `--h: 1; --hm: 1`, the fixed header over its top:
  padding-top `--nav + --photo + --hgap` (120 at 1440, 96 on a phone), padding-bottom `--hpadb +
  --bar` (64, 24 + bar on a phone). Content ends by y 836 at 1440x900. Nothing of the next section
  shows at 1440, 1280, 1024, 820, 768 and 390.
- **Content:** `.wrap > .hero-text` holds the composition: an optional notice line, the h1, the
  sub-line (`p.hero__lead`, layout.css), at most two buttons (a place one), and the picture. One plain claim, never a slogan;
  no caption under the picture, no second float card, no three button styles. The buttons sit above
  the fold at every width.
- **The h1** first, top at y 120 (96 on a phone), at most three lines at every width, never
  smaller than an h2 (28 to 60px on a phone). A notice line (one 14px line in the body face with a
  number, 4.5:1: changed hours, a delivery cut-off) sits 16px above it; never a bar above the header.
- **The picture ends inside the hero:** a layer behind the words, beside them in a split, or above
  or below them only if the whole hero ends by H - 24. A frame under the words ends by y 836 (about
  296px under a 356px text block); larger becomes a layer. Never a first screen that ends on a
  visual cut by the fold, never half a picture under the text.
- **The first screen at 768 and 820.** The split stacks: the words, then the picture in what is
  left. Its bottom edge ends on a whole element or clearly bleeds a large picture on purpose:
  - whole: the picture (a fragment, a phone, a render) ends 24px or more above the hero's foot;
  - a bleed: a photograph or ground filling its frame (`.frame--photo`, `object-fit: cover`), or a
    fragment in `.frame > .stage` cut by the frame's bottom through 96px or more of its rows under
    `.stage--fade-b`, the point (the comment, the button, the row worked on) above the fade.
  Never a card, window or diff in a wrapper of your own whose lower edge the fold slices (in testing:
  a 480x688 diff in `div.hero__art` lost its lower edge at 820, `fold-card` FAIL); never 1 to 95px
  of a box under the fold. Below 1024 `.at-over` pieces hide; give the main piece a `.fit` width
  (it narrows), never a fixed one. Shoot 820x1180 and 768x1024 and read the first screen's foot.
- **Docked strip:** software and product may dock one row under the hero's content (real customer
  logos with permission, a rating line the brief gives, or three facts), at most 96px, still, hidden
  on a phone unless it ends by H - 24 - bar. Service and place dock nothing.
- **Phone:** the text first; a photograph above it only when the whole hero ends by H - 24 - bar.
  Hero buttons stack at one width, unless both fit on one line.
- **Allowed types:** a full-bleed still photograph, a product whole on a stage, an inset frame, a
  statement followed by the work. Tech only: a film in a frame or behind the text (muted, inline,
  poster first, a pause button: the page's effect or loop) or a 3D hero (poster first, the canvas
  swapped in when ready). On other a film is a still that plays on a click. Never a slider or
  crossfade between screens or products, an entry gate, a loader or an entrance that hides words.
- **Pictures in the hero are the work:** the client's product, place or work, never a colour field
  or a mood.

### The eleven heroes

Dealt by kind and by the material the brief really has, never by taste, never the same within three
pages; a place never deals (the place hero below):

```bash
node <skill>/assets/layout/deal.mjs --type software|product|place|service [--kind gaming|tech] --has photo,ui,film,object --history .taste-skill/layout-history.json
```

`--type` is the page type (`SKILL.md` section 1: a game is `software`, hardware `product`). A game
adds `--kind gaming` (its own weights, never `ui`): `--has film,photo` when the brief supplies its
trailer or key art, `--has object` without art files (its key art rendered with the product-render
helper on the `product` stage; a game never deals `statement` or `word`, and always passes `--has`);
hardware adds `--kind tech`. A product or hardware with no photographs passes `--has object`, which
always prints the `product` hero: its render whole on the full-width stage, its widest view, never a
`split` column or an order form alone (`sections.md`, Product). Printed, never dealt: the place hero.

It prints the hero (its demo, numbers, and the moment, ground and effect ids that fit the kind; on
other only the hero itself counts). Copy only its `<section class="hero …">` from
`assets/layout/hero-<id>.html`: each file is a whole demo page, and its nav, other sections, footer
and credit line (which names photographers, against `copy.md` Credits) never come with it;
`hero-place.html`'s latte close-up is a demo, never the place hero. `word` and `statement` are
dealt only without a strong photograph.

| id | composition at 1440 | at 390 | its motion |
|---|---|---|---|
| `split` | text span-5; the picture span-6 start-7, top-aligned with the h1, ending on the right line; one opaque float card on its lower left | text, then the picture (at least 240 tall) | the float card's dot (tech) |
| `photo` | a full-bleed photograph layer, the words on its calm, dark side on six columns (h1 80, two lines), four facts at the foot | the photograph cut to the top, the words under it on the ground | none |
| `product` | a head row (h1 cols 1-7 on two lines; the lead and the buttons stacked on cols 9-12, their foot on the h1's), then the product itself big with one to three hotspots: a render (its widest view, `data-product-place="stage"`) or a cut-out on the page's ground across the wrap, no box, gradient or radius, the stage down to 24 above the fold (1280x566 at 1440x900: the city bike's side 1046 wide, 82% of the wrap); a product photograph edge to edge down to the fold, square corners. A game names itself in the h1; a `[data-print]` or `[data-scene]` on the stage keeps the lit, rounded stage | stacked; the render 86% of the column (294 of 342), the photograph the screen width; a tap opens a hotspot | hotspots on click; a render is a still (live only when asked, `data-product-mode="live"`) |
| `editorial` | the headline is the picture: 156px on three lines across the wrap, one or two photographs set in the line as pills | 56px on four lines | the pills open once on load (tech); still elsewhere |
| `collage` | text span-5; a lit frame span-6 start-7 with the product window cut by its bottom, one result card that loops | the window alone | one card loop (tech) |
| `word` | an oversized h1 (144px, two lines) with one live word last, underlined; lead and buttons span-6, four facts span-5 start-8 | 54px on three lines | the live word, two rounds then rest (tech only) |
| `film` | a cinema frame on the lines holding the poster, h1 white on a calm part, the play disc at its foot | the frame, then the words | plays on a click |
| `statement` | one calm sentence (56px, two lines) over the page ground (tech: a dark ground on a dark page), lead, buttons, four facts | 34px on three lines | none |
| `triptych` | h1 52 on span-3, a collage of three to five pieces on span-6 start-4 whose sets change every 2.8 s, one large button ending on the right line | collage 342 wide, button full width | set change (tech only; still elsewhere) |
| `centred` | pill, centred h1 72 with the mark inline, lead, two pill buttons, then a lit frame across the wrap holding the product window, fading over its last 18% | the window less its list column | the window's story (tech) |

Every hero is one screen, stands on the edge lines, has one h1 within its `maxChars`
(`heroes.json`) and one motion of its own at most, which rests under reduced motion and on a phone.
A hero fails with a picture out to one viewport edge, a hero taller than the screen, the visual
above the text on a phone, words over the busy part of a picture, a second float card, a slogan, a
caption under the picture.

### The place hero

Every place page, never dealt: one still, full-bleed photograph of the place under the header with
nothing on it (no text, scrim, gradient, fade or box), the words on the ground below. No moment, no
move.

- 1440: `.hero.hero--photo` on `html[data-type="place"]`, `--photo: 480px` (the photograph at y 72
  to 552, its subject in the middle 640px), `--hgap: 40px`. Under it: the h1 at 48/53 on columns 1
  to 6 (x 120 to 708, y 592, at most three lines); from the split line (x 732) the sub-line at 20/30
  (the kind of place and where, with today's hours; at most two lines, 80 characters) and one filled
  48px main-action button 24px under it. The row ends by about y 760, never past 836.
- A shop or bookshop may take a letterbox inside the column instead: 1200 x 504, 24px under the
  header (`--photo: 528px`).
- 640 to 1023: the photograph at most 56vw tall, the words stacked under it, the hero ending by
  H - 24. 390: the photograph 390 x 292 (a phone crop, subject centred), `--hgap` 24, the h1 at
  32/37 (three lines at most), the sub-line at 18/28, one 342 x 48 button; the stack ends by
  H - 24 - bar.
- The photograph is real and of this place in daylight: the room from the door, the counter with
  the machine, bread on shelves, the shopfront with customers, the workshop stand, an arrangement in
  a real room, the best room or the house. Never a mood shot, scenery, a cut-out or a hazy file; a
  florist never opens without flowers. The visit block is screen two, never inside the first.

## 4. Equal edges and the grid

- **One `.wrap`** for the header, every section and the footer: `width: min(100% - 2 * var(--gut),
  1280px)`. Lines at x 80 and 1360 at 1440 (a place: 1200 at x 120 to 1320), x 24 and 366 at 390.
  The same all the way down.
- **12 columns, 24px gutter** (12 on a phone). Column starts at 1440: 80, 189, 297, 406, 515, 623,
  732, 841, 949, 1058, 1167, 1275; spans 3 = 302, 4 = 410, 5 = 519, 6 = 628, 7 = 737. On a place
  (1200): starts 120, 222, 324, 426, 528, 630, 732, 834, 936, 1038, 1140, 1242; spans 282, 384, 486,
  588, 690. On a phone one 342 column or two 165 tiles 12 apart; nothing narrower than 165.
- **Every block starts on the left line or a column start,** and every block that ends on the right
  ends on a column end, the last on the right line. Anything wider than half the `.wrap` runs the
  full `.wrap`. Card rows (6+6, 4+4+4, 3+3+3+3): the first card on the left line, the last on the
  right, all one height, every row full. Text inside a card or visual is not a page line.
- **Two text lines:** the left line and the page's split line (the right column's start: k = 5, 6
  or 7, x 623, 732 or 841; a place always 6/6 at 732). Pick the split pair before building and use
  it on every split, the hero split, FAQ and visit included. Centred text moves left: the h1,
  section heads, the close and pricing heads all start on the left line (the `centred` hero is the
  one exception, on the page axis). No centred or right-aligned block wider than half the `.wrap`.
- **Splits:** text left, the visual right, top-aligned, on every split of the page: never mirrored,
  never alternating. The h2 and its intro sit on the left line above the grid. A filled column is a
  card and may pad its text 48px; text never sits inset in a bare column. Phone: text, then the
  visual, both 342.
- **Pictures:** a photograph spans 0 to the viewport as a layer, or starts and ends on the column
  lines (628, 410, 302 wide; place 588, 384, 282), one ratio per row (4:5, 4:3, 3:2 or 1:1; a place
  4:5, 4:3, 1:1). No photograph taller than 708px outside the hero.
- **Bleed:** full width only for layers: a section's photograph or ground behind its words
  (`img.layer`, `aria-hidden`, covering 90% or more of the section; the hero holds one layer).
  Never out to one side only: a cut window is cut by its frame inside the `.wrap`. A picture wall
  is `.wall` (gap 0 or 2px), from line to line.
- **Nothing** crosses a section edge, is cut off (no sliced heading, no ellipsis), staggered or
  peeking out behind another, and there is no dead space beside a short text.
- **1024 to 1279:** span-4 cards with a panel go two-up. **640 to 1023** (checked at 820 and 768):
  splits stack text first, panel cards take the full row, no row half empty. Nothing scrolls
  sideways at any width; no swipe rows.

## 5. Type

- **Dealt, never picked:** `start.mjs deal --page <kind>` deals three Google pairings for the
  kind; take the one that suits the client, then `start.mjs css --page <kind>`. A `word` or
  `editorial` hero needs a face with a weight or width axis: deal with `--axis`. Every pairing a
  kind can be dealt, with its exact Google Fonts link: `start.mjs types --page <kind>`.
  `library/type.json` is the one source of every face, weight, tracking and `--ly-scale`: keep the
  `:root` block as start.mjs prints it. (`assets/layout/fonts.html` reads type.json and shows every
  pairing; a hero demo's face is a specimen, not a source.) Load from Google
  Fonts with `display=swap`; a fallback face never shows (`font-load` warns a family that
  never loaded).
- One family, or a display face plus a text face with fixed jobs; never three; at most four font
  files. Never Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Space Grotesk, Plus Jakarta Sans
  or the system look.
- **Weights:** headlines at `--display-weight`, as start.mjs prints it: 400 on product, service and
  place, 500 on tech; size and tight tracking (-0.5% to -4.5% at 40px and up) carry them, never
  bold-and-big. Text 400 and 500 only (labels, buttons, today's row, strong). 600 is loaded for
  one thing, the nav mark's initial tile (`.mark--initial`); a static face (Instrument Serif) sets
  that tile in `var(--display-weight)`. Never 700 or 800 (the letters moment's own 700 aside). No
  light weight under 20px.
- **Sizes** (1440/390): h1 72/38 (the hero; each hero's own token in `heroes.json`), h2 48/30, h3
  and quotes 28/24, lead and card titles 20/18, body 16/26, small 14, labels 13/500 in sentence
  case, a stat 38/28 (`--t-stat`, under the h2). A place: h1 48/53 and 32/37, h2 32/40 and 24/30, names 20/28 and
  18/26, sub-line 20/30 and 18/28, body 16/26, small 14/20, labels 13/16. Each level at least 1.3x
  the next from 1024 (1.2x below); nothing under 13px; lines at most 62 characters.
- Display text of 40px or more outside a grid item counts as a heading; a statement set at h2 size
  is a fault. A footer wordmark may be larger.

## 6. The check

`layout-check.js` frames every section as a reviewer frames a shot; `check.mjs` runs it in one headless
Chrome (WebGL on the CPU, closed by its own PID) and writes the framed shots:

```bash
node <skill>/assets/layout/check.mjs --url index.html --profile <own dir> \
     --sizes 1440x900,1024x768,820x1180,768x1024,390x844 [--shots <dir>] [--json]     # pass these five: the judges shoot the tablet at 768x1024 and 820x1180
```

| Finding | Means |
|---|---|
| `hero-fold` | the hero does not fill the first screen, runs past it, or the next section shows |
| `hero-maxchars`, `hero-lines` | with the h1 lengthened to its `maxChars`, the hero runs past the screen or the h1 takes too many lines |
| `screen-short`, `screen-height` | a section shorter than one screen, or not exactly one or two |
| `sparse` | content fills under half the section (a picture's own frame counts whole) |
| `neighbour`, `neighbour-ground` | another section's ink or ground shows in a section's tile |
| `edge-left`, `edge-right`, `spill`, `bleed-one-side`, `one-sided` | a block off the lines, past them, out to one viewport edge, or visuals stopping short of the right line |
| `lines` | text starts on more than two left lines |
| `overflow-x` | the page scrolls sideways |

Run it without `--no-stress`; every finding fails the page. In another script:
`await page.evaluate(src + ';window.lyCheck()')` returns `{ vw, vh, L, R, nav, screen, hero, sections, findings }`.



---

## `references/moments.md`

# Moments

A moment is the award-site part of a page (house rule 8; with the house overrides): the one place, or
two, where a page does something a visitor remembers; the rest stays still. Each is a folder in
`assets/moments/<id>/` (`moment.js`, `moment.css`, `meta.json`, a full `demo.html`); `index.json`
lists them, `gallery.html` links the demos and `moments.js` runs them. Seventeen folders: two
retired (`headline-arrives`, `closing-lift`), four left out of the house deal (below), and eleven
dealt: letters that fly into a statement, liquid type, a circle or a line that changes the ground,
a statement that lights up word by word, a photograph seen through giant type, pinned chapters, a counter, a marquee row, a pointer
light, a liquid photograph.

**Which pages.** Kind software, gaming or tech (hardware: a product page with a technical subject)
only: one moment on a short page, two on a long one (eight sections or more, in two different
sections), never three. **A plain product, a service, a place, shop, cafe or guesthouse gets none**:
they lead with photographs, type and flat colour (the house overrides, point 3). `pick` makes this
the rule: it needs `--page`, and any other kind returns an empty deal. A moment counts against the
page's big scene (`effects-usage.md`) as one of its beats.

## Deal them, never choose by taste

```bash
# the section moments: one on a short page, two on eight sections or more (less a hero moment)
node <skill>/scripts/moments.mjs pick --page <kind> --count 1|2 --fits section,statement \
  --exclude lines-rise,picture-develops,window-parallax,word-rotate \
  [--scene <id>] [--effects <ids>] [--contexts <n>] [--photo] --history .taste-skill/history.json
# a hero moment (0 or 1): the same with --count 1 --fits hero; kept only when the dealt hero lists it
```

- **`--page`** is the page's kind (`SKILL.md` section 1: `software`, `gaming` or `tech`; `ai`,
  `saas` and `technical-product` are read too). Any other kind prints `no moment: ...` and an empty
  deal (`--json`: `"picks": []` with a `reason`), exit 0: the plan then writes "no moment".
- **`--fits section,statement`:** a statement is a section of its own, so the letters, liquid type,
  word-highlight and the counter come only with it; `section` alone deals none of them.
- **Always out:** `lines-rise` (a reveal), `picture-develops` (a photograph that develops),
  `window-parallax` (parallax on a photograph) and `word-rotate` (the `word` hero carries its own
  live word, `layout-v4.md`). A dealt scene's twins and avoidMoments are left out by `--scene <id>`
  itself.
- **The hero moment** (0 or 1, never on a big-scene hero) is kept only when the dealt hero lists it
  in `heroes.json` (`moments[].id`): after the excludes that is `liquid-hover` on `split` and
  `photo`, `cursor-spotlight` on `product`, `collage`, `film` and `centred`, `liquid-type` on
  `statement` (tech, a headline of six words or fewer), and none on the others. Off touch only;
  reduced motion rests. Two moments in all at most.
- **The WebGL budget.** A page holds at most 4 live contexts (`perf.md`). The deal adds up what the
  page already spends and never deals a moment whose own `webgl` (in its `meta.json`: only
  `liquid-hover` has 1) would push the total over 4: pass the big scene as `--scene <id>` (its `webgl`
  is read from `assets/scenes/index.json`), each dealt effect in `--effects a,b` (counted as one
  each, the worst case) and anything else in `--contexts <n>` (an object, a component with a canvas).
  The deal prints the total it reached.
- **The rest of the deal.** Placed in different sections. The history's `moments` list is read as
  cycles: once every moment that fits has been dealt, the next cycle starts empty, so an id comes
  back only after all the others and never straight after itself (the three dealt last stay out
  even across a cycle's end). Never two of one kind (hover and liquid count as one: one pointer
  effect a page), never two of one slot, never two that avoid each other, a moment that needs a
  photograph only with `--photo`. Write each id and its section in the plan. A dealt moment with
  nothing to carry is dealt again with it added to `--exclude`.
- **Retired** (`meta.retired`, weight 0, never dealt): `headline-arrives` (MO-62, the headline never
  hides on load) and `closing-lift` (it needs a closing band of its own and its words stand on a
  gradient over the photograph). `magnetic-button` (CK-94) is gone.

## Where each fits

| id | kind · fits | phone and reduced motion |
|---|---|---|
| word-rotate | text · hero, three rounds then rests | the written word stands |
| lines-rise | text · one section or statement, once | the heading and its lines stand |
| counter-rolls | text · the proof figures, once; never in a card | the figures stand |
| word-highlight | scroll · one statement | the whole statement in ink |
| giant-type-pass | scroll · one statement with a photograph of mid to dark tones | the photograph stands in the letters, smaller type |
| letters-assemble | scroll · one statement of 2-5 words, set very large: its letters fly into the line | the statement as written |
| pinned-chapters | scroll · one feature section of 2-4 steps, two screens live | static rows (or each step with its visual under it) |
| window-parallax | scroll · one wide photograph | the photograph stands in its frame |
| marquee-row | scroll · a row of real words (trades, cities, formats; never logos: a logo never moves), with a pause button | the words in a wrapped row |
| line-carries-colour | transition · a section on a new ground keeps it edge to edge; inside, an inset panel in the old ground (even gutter, card corners) is cleared by a line climbing from its foot; each block shows whole once the line has passed it | the section on its own ground, no panel, no line |
| iris-opens | transition · a section on a new ground keeps it edge to edge; inside, an inset panel in the old ground (even gutter, card corners) opens a disc with a hairline accent ring; each block shows whole once the disc holds it | the section on its own ground, no panel, no ring |
| picture-develops | transition · one photograph with a clear subject, once | the photograph stands |
| closing-lift | transition · the close, with a photograph | a plain closing section |
| cursor-spotlight | hover · the hero frame | the light rests |
| liquid-type | liquid · a hero or statement headline ripples like water under the pointer, an SVG filter, no WebGL | the headline as written |
| liquid-hover | liquid · one photograph with edges and detail, one WebGL context | the plain photograph, no canvas |

## The still rule (every moment, no exception)

Every moment has a static variant for a **phone** and for **reduced motion**, and a finished state
without script or when its module fails. The loader decides: it hands each moment a `lib` whose
`reduced()` answers `lib.still()`, which is true under `prefers-reduced-motion` and on a phone (under
640px wide, or a touch screen turned sideways under 500px tall). A moment written against `reduced()`
therefore shows its finished state there, and the host carries `data-moment-still="reduced"`,
`"phone"` or `"card"`. The answer is taken when the moment mounts (a window resized across 640px
applies it on the next load; `pinned-chapters` asks again on resize). Each `meta.json` says what the
still shows (`reduced`, `phone`). Hover moments do nothing on touch screens either.

**Nothing on a card moves on scroll** (house rule). A moment sits on a hero, a statement, one
section, a transition or the close, never in a card, a plan, a result or a bento cell: the loader
leaves one that does still (`data-moment-still="card"`, `data-moments-card` on `<html>`) and
`moments.mjs check` calls it a fault.

## Put one on the page

The host is a section of the page (or, for the text moments, the headline or the row inside it);
mark it as the moment's header comment shows (`data-moment="<id>"`, options in `data-moment-opts`).
Every section stays one or two screens tall (`layout-v4.md`, `--h`), live and at rest: a transition's
host is the whole section that sits on the new ground, a statement moment is one section with its h2
first, a marquee or counter row merges into the section above as its last row. In `<head>`, the one line plus a `modulepreload` for
the loader, its lib and the dealt moment:

```html
<script>document.documentElement.classList.add('mo-js');setTimeout(()=>document.documentElement.classList.add('mo-safe'),2500)</script>
<link rel="modulepreload" href="assets/moments/moments.js"><link rel="modulepreload" href="assets/moments/lib.js"><link rel="modulepreload" href="assets/moments/<id>/moment.js">
```

Then the loader once. On a page with `system.js`, `system.js` imports it and waits for it. On a page
without, the demo pages' tag at the end of `<body>`:

```html
<script type="module" src="assets/moments/moments.js"></script>
```

The loader links each moment's CSS and starts it; `<html data-moments-ready>` says when. A failed
module gets `data-moment-failed` and the class `mo-safe` on its own element, which the moment's CSS
reads as "show the finished state now". A demo's copy and photographs are placeholders. Every moment
takes the page's tokens (`--bg`, `--ink`, `--muted`, `--accent`, `--line`, the display face).

## Rules

- **The kind's count, an id once.** `data-moments-over` and `data-moments-repeat` on `<html>` are faults.
- **No random effects as you scroll.** A scroll moment is scrubbed to the scrollbar inside its own
  section, which stays one or two screens tall, and does one purposeful thing; at the section's top
  and bottom it shows a finished state (every transition and `letters-assemble` finish before the
  section's top is a fifth of the screen down), so each judge tile shows one whole section. No card,
  row or tile ever enters on scroll. `consistency.mjs` reports a scroll finding inside the dealt
  `[data-moment]` section; that one is expected, any other is a fault.
- **Content is readable without the motion:** the words are in the HTML, in their finished place; a
  moment never hides a headline on load (`headline-arrives` is retired for it).
- **One count a page:** `counter-rolls` or `data-m-count` (`motion.md`), never both.
- **Nothing blinks, bounces or overshoots.** Ease-outs, 600-1,000 ms for a reveal; a loop runs its
  rounds and rests, or carries a pause button.
- **The page's edges.** A moment's text sits in a `.container` or `.wrap` like every other section: its
  words end on the page's left and right edges. A transition's cover is an inset panel inside the host
  section with an even gutter on every side (card corners, never touching the section's edges), its
  line or ring inside the panel; every heading, paragraph, button and picture appears whole, never cut
  by the line or the disc (each moment's `meta.json`, `look`, says how).
- **Cost:** no WebGL but `liquid-hover` (one context, only near the screen; a plain photograph without
  WebGL or when the shader fails). `liquid-type` is one SVG filter on one headline, on only while a
  ripple is alive. Every other moment costs CSS variables, a transform or a clip and a passive
  listener.
- **One pointer effect a page:** a hover or liquid moment rules out `fx-button`, `fx-spotlight` and an
  object that turns to the pointer, and the reverse; `pick` never deals two of them.
- **Photographs:** `giant-type-pass` and `liquid-hover` want mid to dark tones with edges and detail; a
  pale dusk sky reads lavender in a letter and a flat sea shows no ripple. Never violet or lavender.
- **No captions;** the photograph's credit goes in the footer line.

## Check it

- `node <skill>/scripts/moments.mjs check <page.html> --page tech [--scene <id>] [--effects a,b] [--contexts n]`
  reads the built page: how many moments, any twice, retired, off its page kind, in a card, holding a
  figcaption, two that avoid each other, the WebGL total against 4, a missing loader. Exit 1 on a fault.
- `node <skill>/scripts/moments.mjs shoot --out shots/moments --profile <own chrome dir> --port 5720 --only <id> [--reduced]`
  shoots the demo's start, middle and end states at 1440 and 390 in the skill's headless Chrome (WebGL
  on the CPU); the end must be the finished section. At 390 and under `--reduced` it also checks the
  still rule: the host must say `data-moment-still` and no animation may run inside it (a line
  `STILL?` otherwise). `--probe "<js expression>"` prints a value after each state.
- The headless Chrome draws WebGL on the CPU, so `liquid-hover` shows a fainter ripple there than on a
  GPU and its end state waits 6 s to be the plain picture; a text or scroll moment looks the same on both.



---

## `references/motion.md`

# Motion

Every page loads the micro-interaction layer: `<html data-motion>`, `assets/motion/motion.css`
after `ui/cards.css`, `assets/motion/motion.js` (module) after `system.js` (`starter.html` has all
three). **It is not optional:** never remove, skip or override it; if a check complains about it,
fix the markup, not the layer. A missing or invisible hover layer is a fault on every kind (round
C: a fintech, a cafe and a guesthouse page lost motion points because a hovered card or button
showed no change); a still page is not. Give it markup to act on: a linked card is a `.card`
holding its link (never `.m-nolift`), a photograph that leads somewhere is `<a class="m-zoom">`
round its `<img>` (or `img.frame__img` inside a linked frame), buttons are `.btn`, links in
running text `.link`. Shoot a hovered card and a hovered photograph at 1440 and see
them change: the card 2px up, the photograph at 1.03. `assets/motion/demo.html` shows every interaction. This file
holds every hover, press, loop and reduced-motion number; other files point here.

What may move, by kind (house rules 5 and 8):
- **Every kind:** the hover and focus layer below, and swaps a click or a tap makes (a tab on
  software, a peek-list's photograph). Every change is the visitor's.
- **Tech:** also loops inside a card's visual (diagram pulses included), one timed loop in the hero
  or the `[data-visual]` frame, one count, and the effect, moments and scene `effects-usage.md`
  deals.
- **Other (product, service, place):** the hover layer alone. Nothing moves by itself, on load, by
  time or on scroll: no entrance, ticker, marquee, slideshow, looping picture, pulsing dot, count or
  moment. An open-now line may be filled once at load; the panel reads right without it. A
  product render is a still by default; live only when asked (`data-product-mode="live"`), at
  most one live context, with its pause button in the corner, a still on a phone and under reduced
  motion (`effects-objects.md`).

## Tokens

`--m-in` 140ms (hover in), `--m-out` 200ms, `--m-press` 90ms, `--m-panel` 200ms, `--m-slide`
240ms (an indicator travelling), `--m-image` 600ms, `--m-cycle` 3.2s; tech loop tokens:
`--m-roll` 700ms, `--m-count` 1000ms, `--m-level` .6s, `--m-bob` 3.2s. Ease `--m-ease`
cubic-bezier(.2,.8,.2,1) for every UI step; `--m-ease-io` cubic-bezier(.65,0,.35,1) only for
travel; cubic-bezier(.22,1,.36,1) only for digit rolls; linear for loops and drifts. No bounce or
overshoot. Distances: card lift 2px, photo zoom 1.02 to 1.03, arrow 3px, menu drop 6px, button step 1px
up (2px on `.btn--xl`; none on the text-link secondary of the `arrow` and `block` looks), press 1px
down and scale .985 (that secondary: scale only); no others (`assets/motion/motion.css`, buttons).

## The hover layer

Hover only for a fine pointer; every hover control also works by tap and keyboard and has a focus
state; nothing resizes or pushes a neighbour; no rotate, skew, glow, shine sweep or chip glide.

| Part | Motion | Time |
|---|---|---|
| Button | on hover the fill steps 14% toward the ink (an outline gains a faint fill and a stronger border) and the box steps up 1px (2px on `.btn--xl`); press sinks it to 1px below rest and scales .985, so a hover shot and a press shot each show a move; the text-link secondary of the `arrow` and `block` button looks keeps its underline and does not step (its press scales .985 only); fine pointer only; page CSS never sets a `.btn`'s `transform` or `transition` | 140ms in, 200ms out, 90ms press |
| Arrow | `svg.m-arrow` moves 3px right and settles back; one arrow style a page | 140 / 200ms |
| Link | one underline style at regular weight: running text and `.link` rest on a faint 1px hairline and an ink line draws left to right, leaving to the right; nav and footer words rest bare, darken and draw a 1px line 4px under the word | 140 / 200ms |
| Nav | the words take the drawn underline (no gliding pill on any kind); the panel opens after 150ms of intent, fades in with a 6px drop, its columns together, closes in 120ms; with one open the next word swaps it at once; the chevron turns 180 degrees on tech, flips at once on other | 200ms, 120ms |
| Current page | a 2px bar under its nav word (`aria-current="page"`) | still |
| Tabs (software, click only) | one indicator slides to the clicked tab: the ink pill `system.css` draws, its label in the ground colour; the panel swaps (200ms at most); every panel one fixed height; on other no tabs | 240ms |
| Card with a link | lifts 2px, its border darkens a step, an optional soft shadow (blur 24px, 10% ink at most, only on hover) | 180ms, border 140 / 200ms |
| Card without a link | nothing (`.m-nolift`) | |
| Photograph in a linked card or link | scales 1.02 to 1.03 inside its frame (`overflow: hidden`); the frame, card and boxes never grow; never dims, fades or takes an overlay; a product card's name underlines with it (`.m-zoom` for any other wrapper) | 600ms |
| Focus | a 2px ring in the accent, its offset settling from 6px to 2px | 200ms |
| Field | the action border and a 3px soft ring | 140ms |
| `.m-switch`, `.m-check` (tech) | the knob slides 16px and stretches 4px while pressed; the tick draws; on other they jump | 180, 90, 160ms |
| Copy button (tech) | the glyph swaps to a check in place, holds 1.5 to 2 s, returns | 150ms |

FAQs show every answer open (`system.css`): no accordion, and nothing ever animates height,
max-height or padding. Hooks: `[data-m-loop]` (your own CSS loop, tech), `data-ui-loop` (a card
group's one fragment loop, tech), `data-m-count` (tech hero only), `.m-link`, `.m-zoom`, `.m-nolift`.

## Loops inside a card's visual (tech)

House rule: a bit faster, and repeating.

- One cycle is 2.5 to 4 s (`--m-cycle`, 3.2 s default), then it starts again. It is seeded on its
  finished picture and never shows an empty window: a ui.js fragment rests 600ms on it before the
  first cycle; a `[data-m-loop]` starts at once; the last 10 to 15% of each cycle holds the finished
  picture, and a reset dims and rewrites, never blanks.
- The pointer or keyboard focus entering its card restarts it from the top (not in its first
  800ms). A paused loop stays paused. The card, its panel and the window never move: no zoom, tilt
  or camera pan inside the window.
- One subject per cycle (a pointer clicks, a status turns, a bar fills, a line is written): one
  change every 1 to 2 s, each change 300ms or less. Several subjects: the next one each cycle. A
  changing label never shows two words at once.
- One fragment loop per card group (`data-ui-loop`); the other fragments hold their finished
  picture and play while the pointer rests on their card. A small diagram card's pulse is that
  card's own loop, on the same cycle, restart and pause rules (house rule: pulses running along the
  lines); system.js never holds it (`data-ui-still` does not reach a diagram). Below the hero, two
  loops are never on one screen: in a group with a pulsing diagram, give the fragments
  `data-ui-still` too, or hold the diagram with `data-dg-still` (it then plays under the pointer).
- A page's own CSS loop sits in `[data-m-loop]`, every keyframe on `var(--m-cycle)`, `--m-still`
  (0 to 1) the finished frame, a 48px band (`--m-safe`) kept clear for the pause button.
- Life signs inside the looping visual only: spinner 1s (12 to 16px, then a check), live dot 2.4s
  (the dot still, a ring grows and fades), caret 1s with a hard step inside a field, level bars .6s.
  No typing dots, no lone pulsing dot elsewhere, no block cursor after a headline.
- Kinds of card story (each in a box of fixed height): a prompt types at 12 to 20 characters a
  second and holds; an answer streams about a bubble a second; a notification enters at the top and
  the oldest leaves through the fade; a checklist ticks about once a second; a calendar's events
  fade in one by one; a pointer glides about 200px in 1 s, presses (scale .96 at least, a 28px ring)
  and holds. A speaker or avatar front item changes no more than every 3 s. A chart stays still.
- Not yet placed, so not used: a stepping slot strip, a before/after divider, path-following items,
  a dock tab that grows, a pointer-linked mascot, a comet along a hero strand.

## Tech budget

- **One timed loop** a page, in the hero or the `[data-visual]` frame, in whatever form (a story, a
  reel, a lit border, a live ground, a turning object, a marquee); its life signs are part of it.
  One timed loop plus the one effect at most; with a live effect in the hero, no other timed loop
  runs. Never two self-moving things in one 900px window, never two loops in one panel. Card loops
  (one per card group), diagram pulses (one per diagram card) and the dealt moments are outside
  this count.
- **A count** once a page (`data-m-count` or the `counter-rolls` moment, never both): on load in the
  hero (1000ms, 1.2 s at most), or as the dealt counter moment in its own section. On the open
  ground, never in a card, panel or `[data-visual]`; its width reserved; the final figure in the
  HTML, shown under reduced motion, without script and on phones; never a year, price or phone
  number. A live counter changes only its last one to three digits.
- **Load:** hero text is in place on the first frame on every kind, never faded or moved. On tech at
  most one load-once motion inside the hero or `[data-visual]` (a visual assembling, 600 to
  1200ms), settled by 1.5 s; a click swap 400 to 600ms. No gate, loader or intro.
- **Pause:** anything still moving 5 s after it is seen has one round pause button per panel: a
  solid 32px disc, 12px in from the bottom-right (in a card beside its title), always shown or
  fading in on hover and focus, the same size and place on every card, never over copy, never on a
  still. A click freezes the frame and swaps to a play glyph (`ui.pausable(panel, ctrl)` for your
  own movers). Scroll-driven moments need none.
- **Timed loops start on load** and never start, stop or resume on scroll; an IntersectionObserver
  only mounts lazily. A canvas may skip drawing off screen only on a clock from load, so no visible
  start shows on return. A hidden tab may pause everything.

## Scroll

- **Other kinds, and every card on every kind:** nothing animates on scroll. No pinned or sticky
  scene, scroll-snap, scroll or view timeline, reveal of any kind (fade, rise, stagger, mask wipe,
  letters filling, words lighting, lines drawing), parallax, drift, scroll-tinted ground, progress
  line, scroll-spy marker or count on view.
- **Tech:** the big scene and one or two dealt section moments may follow the scroll, each inside
  its own section (`data-big-scene` with `{"hold": 1}`, `data-moment`), which stays 1H or 2H
  (`scenes.md`, Its height), pinned only with `position: sticky` inside that box. Its text is live and visible without the motion (opacity 1,
  4.5:1 at every step); reduced motion and no script show the finished still; phones get the still
  or a light version (transform and opacity, no WebGL); `perf.mjs` passes. It never moves a card, a
  photograph, pricing, an FAQ, a quote block or the footer. Driven by native `animation-timeline`, a
  passive scroll read written to a custom property once a frame, or GSAP ScrollTrigger scoped to that
  section without its pin. No smooth-scroll library (Lenis, Locomotive, ScrollSmoother) on any page,
  no animation library at all on other.
- The header and the phone bar look the same at every scroll position.

## Reduced motion, no script, phones

Colours still change; menus fade; the tab indicator jumps; the underline appears without travelling
(`transition-property: opacity, color, background-color, border-color` on links, `.m-tab-ind`,
`.m-switch::before`, `.m-check::before`). Every loop, effect, moment and scene shows its finished
frame, marquees stand as a still row, numbers show their final text, pause buttons are hidden. On a
phone card loops and effects hold their finished picture or poster, heavy canvases become stills,
there are no hover states and no pointer simulations.

## Never

- A card, row or tile that reveals, staggers, slides or fades in as the page scrolls; parallax or a
  scroll scrub outside the tech page's dealt moments and scene.
- A card that tilts, flips, scales, follows the pointer or glows at the cursor; a magnetic button.
- A carousel, a slider that advances by itself, timed tabs, a rotating notice, a logo marquee.
- Blinking at random: twinkling dots, glitter, flicker, hue cycling, scrambled text; every change
  shows a state, a step or real data.
- A loop that plays once (outside a card story's replay), a card loop's cycle over 4 s, two loops in
  one panel.
- A hover slower than its token, an overshooting ease, a delay before a button reacts, a second
  underline or indicator style.



---

## `references/perf.md`

# Performance budget

Run `node scripts/perf.mjs <site/index.html>` (Node 22 or later) on every finished page. It loads the page in headless CPU Chrome at 1440 and 390 wide, waits until the effects near the viewport are mounted, scrolls to the bottom and prints PASS, WARN or FAIL. Fix every FAIL. `--json <file>` also writes the result to that file; `--runs N` sets the number of timing loads (default 3).

Reading the numbers:

- **Timing is a median of 3 loads** with the spread printed (`runs 3, 33..161`). One load on a CPU is noise; a wide spread means the host was busy.
- **Host load** is sampled before and after. Above 50% the check says so and caps timing at WARN: rerun when the machine is idle before believing a timing FAIL.
- **FCP and LCP are CPU-rendered.** Compare pages with each other, never with field data.
- **WebGL off is a proxy, not a verdict.** SwiftShader runs shaders on the CPU and would swamp the main thread, so long tasks and blocking time come from loads where every WebGL piece shows its still fallback. That is different work from the shader: shader compile and link on a real GPU is not measured, and the INFO line with WebGL on is for orientation only.
- Counts (images, contexts, modules) and bytes are exact; they do not depend on host load.

| Check | WARN | FAIL |
|---|---|---|
| Transfer (text gzipped) | above 1500 KiB | above 3000 KiB |
| Images total / largest single image | above 1200 / 350 KiB | above 2400 / 700 KiB |
| JS parsed / CSS | above 450 / 120 KiB | above 900 / 250 KiB |
| Requests | above 60 | above 110 |
| Font families / files / bytes | above 2 / 4 / 160 KiB | above 3 / 6 / 320 KiB |
| `<img>` without width and height (or CSS aspect-ratio) | 1 to 3 | 4 or more |
| `<img>` below the fold and not lazy | 1 to 3 | 4 or more |
| Oversized images, `<img>`, CSS background and SVG (natural over 2.2x the shown width) | 1 to 3 | 4 or more |
| Photos as CSS or SVG background below the fold (cannot be lazy) | 1 to 3 | 4 or more |
| WebGL contexts live (load, bottom, peak) | | above 4 (hard cap) |
| WebGL contexts made over the whole scroll | above 12 | above 24 |
| Long tasks / blocking time, median, WebGL off | above 8 / 1.5 s | above 20 / 4 s |
| FCP / LCP, median | above 2.5 / 4.5 s | above 4.5 / 8 s |
| Layout shift, median | above 0.1 | above 0.25 |
| Effect, object or component module loaded, never mounted | 1 or 2 | 3 or more |
| Broken request, sideways overflow | | any |

Sizes are KiB (1024 bytes). The 2.2x rule already covers a 2x screen; a photo that is also upscaled (natural under 0.75x shown) warns. "Never mounted" counts entry files only (`effect.js`, `object.js`, `component.js`, a ui `fragment.js`); shared helpers such as `photo-kit` never count. An object has no marker, so objects are judged by count: more object modules loaded than canvases or fallback hosts drawn.

## Every visual renders

A visual that shows only its ground (a blank canvas, a photograph never loaded, a reveal that never fired, a picture caught half drawn) is a fault at every width (house rule 2): every picture slot has a real `src`, `width` and `height`; `consistency.mjs` `empty-visual` and `gl-fallback` find the rest, system.js outlines a failed visual in red, `shoot.mjs` names pictures still loading.

## Usual fixes

- **WebGL cost (tech only; 0 contexts on kind other).** At most 4 live contexts per page (house rule): the one effect or big scene plus a dealt moment's own canvas, each showing a poster first, mounted at load or lazily as its section nears the screen (an IntersectionObserver only mounts, it never starts or stops visible motion: `motion.md`). One sample per CSS px or less (0.75 when large), about 1.5 megapixels, pixel ratio 1.5 at most; noise, particles and ray marching at half resolution and 30fps or less; drop the pixel ratio when frames take over 21 to 24ms. Every WebGL piece keeps its still when its shader fails (`effects-usage.md`). After any shader change, `lint-glsl.mjs` in `assets/objects/_print-core` and `_scenes` must exit 0.
- **Draw still grounds once.** A ground that does not move is drawn one frame, kept as a picture, its context released.
- **Fonts.** At most four font files (`layout-v4.md` section 5; perf.mjs warns above four): preload the regular and the display weight, `font-display: swap`, request only used weights.
- **Size images.** AVIF or WebP through `srcset` at 2x the shown width, never more (a full-bleed hero 2880w at 1440, 780w at 390), the hero under 400 KiB and every other photograph under 250 KiB (the check warns at 350 for one image), the page's images under 2,400 KiB at 1440 (the table's FAIL; 1,200 warns), `width` and `height` (or an `aspect-ratio`) on every one and a `--g-alt` fill while it loads. Lazy and `decoding="async"` below the first screen, never lazy in it; the hero eager with `fetchpriority="high"`. A photo below the fold is an `<img>`, not a CSS background. A place with 8 to 20 photographs stays fast this way.
- **No shift (CLS under 0.1).** Reserve space for images, nav and counters. Animate transform and opacity (colours too); `background-position` only on small text spans; never height, padding or layout. Import only modules the page mounts.
- **Scripts.** Deferred modules, no scroll listeners (the tech moments read the scroll as `motion.md` says), no layout reads in move handlers. No entry gate or loader; kind other loads no animation library and no WebGL; a real-time 3D model stays near 2 MB compressed with a poster; video ships separate phone and desktop files.
- **Ready flag.** A page may set `document.documentElement.dataset.ready = '1'` when its first screen is built; the check then stops waiting for effects to mount.



---

## `references/photos.md`

# Photographs

A place (café, bakery, guesthouse, shop, studio) is its photographs: two or three on every screen, the
client's own. Software leads with its real interface; a photograph there is a real person or the real
product. A game leads with its own art (key art, in-engine shots, the trailer's poster), never library frames; with no art files its key art is a product render of its hero object or world (`sections.md`, Gaming), never a photograph or an effect in its place. A photograph never stands where an effect, a drawing or an empty box would.

## Where pictures come from (PH-01, PH-02, PH-05)

1. **The client's own**, shot for the page or on a phone, each file named in the brief. Every `<img>` carries
   `data-source` (`client`, `commissioned`, `phone`, `supplier`, `illustration`, `library-057`) and
   `data-subject`.
2. **The library** (`scripts/photos.mjs`): Wikimedia Commons and Unsplash frames, vetted one by one. They are
   stock of another place, so they fill **detail slots only**: hands, tools, materials, a process (an oven, dough, a
   roasting drum, stems, a hammer on a bar). Never the hero, a room, a shopfront, a product or a person, and never more
   than **1 in 3 of the page's pictures**. `pick` deals exactly that by default and prints the cap with the deal;
   the draft path below lifts both limits.
   `fetch` prints `data-source="library-057"`. Every frame was looked at again at 100% (the subject and the centre of
   the 2400 file) for softness, grade, readable brands and recognisable people; a frame that failed is out of
   `photos.json` and off disk, and a frame that is a car, a sign or another business's whole room stays
   `weak` (kept with its credit and its why, no file on disk) and is never dealt; a rating below 7 is never dealt either (`quality`): a whole meeting room, lounge or breakfast room is the same fault. The thin trades get at most as many
   frames as they hold: wine 0, bar 0, office 3 (a notebook, stacked books, sheets of card), florist 3, farm 3, shop 3, wellness 3, bakery 4, and a
   workshop by its craft (smith 4, instrument 1, weaving 0, letterpress 0). The rest of the page is the client's own photographs, the object, the real UI or type.
3. **Nothing**: a product's own render (`effects-objects.md`, Product renders), the real UI, or type. Never a near
   fit, never mood in place of the subject.

With no client photographs, say so plainly in the report: strong pages run on a half-day shoot with a local
photographer, then a one-morning phone shoot, then products on one backdrop; the library covers details only. The
shot list: shopfront straight on, the room from the door, the counter or bench, three products on one surface, hands
at work, one detail, each room of a guesthouse; 1x lens, window light, no flash, no filter, landscape and portrait.
**The draft path (a place with no client photographs):** `pick --trade <trade> --sections <words> --draft-lead
--pictures 12` lifts the 1-in-3 cap. `pick` deals one frame per word, so repeat a word for each row or detail
(`bar,bar,coffee,coffee,beans,beans`, `rooms,rooms,rooms,breakfast,breakfast`) until it returns 8 or more: a cafe
reaches 8 to 12, a guesthouse 9 detail frames. The page stays a whole place page that leads with photographs (house
rule 6), the compact page at 8 to 12 frames. The hero is the lead `pick` returns (a
cafe's bar). A place whose trade leads with land (a guesthouse, a lodge, a remote inn) passes the region its brief
names as `--place "<region>"` (or the brief itself, `--brief BRIEF.md`, which reads the region from it) and leads with that region's landscape: a place hero always carries a photograph when
any frame fits, and the `statement` hero is left for a place the library holds no frame of (`sections.md` section 4). Every frame is listed in the report as a stand-in to replace; nothing on the page says so
(no caption, no note). **The count decides, not the trade:** when `pick`, with each word repeated until it says "no new
motif left", still returns under eight frames, the page is the short page (PH-07: 2,700 px at most at 1440; `sections.md`
section 4, The short page), whatever the trade: a bakery (4), florist, wellness, office, pottery or a restaurant are examples. No drawn box, grid
or effect takes the place of a photograph.

Two exceptions, both for a draft or the short page and both named in the report as stand-ins to replace:

- **A hero** (`--draft-lead`): the client has no hero photograph yet. A place hero is still Recipe 3: the frame is the
  full-bleed top photograph with nothing on it.
- **The land around a place** (`--place "<region>"`): a place whose brief names its region (Westfjords, Lofoten, the
  Lake District, a town) is dealt that region's landscape as its lead, because a remote place is sold by where it
  stands. `--own-land` adds the land sections (area, road) when the brief says the business is that landscape (a
  tour, a lodge on its own land). Another region's land, a cafe's street and the sky are never dealt (PH-03, PH-50).

## A product without photographs (PH-04)

A maker of a physical thing (a bike, a chair, a lamp, a stroller, a device) with no photographs of its own gets **no
stock photographs**: no forest for "the ride", no groceries for "what it carries", no other trade dealt to fill the page.
`pick --product-without-photos` (or a maker's, brand's or company's word: "backpack brand", "electric scooter")
deals nothing and says so. **The product is still shown, never hidden:** it is rendered with the objects kit's
product-render helper (`assets/objects/product-render`, `effects-objects.md` Product renders), one crafted studio
render composed from a JSON spec of its own parts, sizes and materials, and the page is the full product page
(`sections.md`, Product: hero, the product, what it carries, how it is used, specs as rows, a live order card), never
the short page (in testing: a cargo bike's page that never showed the bike scored 3 of 10). The render is the product's
picture on a flat ground, not an effect, on a product of site-kind other as on hardware. Never a drawn SVG, mood
stock, another maker's product or an object of another kind (a wheel is not a bicycle). A render or CAD view the
brief supplies comes first; renders it names but does not supply count as missing. The report lists the shots to
take: the product on one plain backdrop, three angles, a detail of each part the page names, the product in use. A
shop, workshop or rental for every make is a place (`--trade "bike shop"`): it is dealt parts and a basket load for
those sections only.

## Pick and fetch

```bash
node <skill>/scripts/photos.mjs list                       # trades: detail frames dealt by default, land, can lead
node <skill>/scripts/photos.mjs list --places              # the place names the library knows, for --place
node <skill>/scripts/photos.mjs pick --trade bakery --sections oven,dough,bread --pictures 14 \
     --history .taste-skill/history.json
node <skill>/scripts/photos.mjs pick --trade cafe --sections hero,bar,bar,coffee,coffee,beans,beans,hands --draft-lead --pictures 12 \
     --history .taste-skill/history.json                                                     # no client photographs
node <skill>/scripts/photos.mjs pick --trade guesthouse --sections hero,rooms,rooms --pictures 12 \
     --draft-lead --own-land --place "Lofoten, Norway" --history .taste-skill/history.json   # a draft only
node <skill>/scripts/photos.mjs fetch <ids> [--hero <lead id>] --out . [--big id] [--lqip]   # run from the project root
node <skill>/scripts/photos.mjs credits --out . --write     # the footer line and credits.html; --text for a report
```

- **Order and places.** `pick` prints its follow-up `fetch` with the script's absolute path (forward slashes, quoted when it holds a
  space) and `--out .`, so it runs as printed from the site folder (from elsewhere, give `--out` the site's path). `fetch` writes the files into `assets/img/` under `--out` (the project's own folder, `--dir` changes it; `--out .` from the
  project root, so the markup says `assets/img/photo-<id>-1200.webp`), and prints the `<img>` or `<picture>` to paste; if the
  folder it prints differs, use that one. `credits` reads the page, so run it last, after the markup references the
  photographs: before that it exits 1 with "none of the fetched photographs is on the page".

- `--trade`: cafe, bakery, hotel, bike (--shop only), food, florist, workshop, studio, office, shop, books,
  outdoors, wellness, farm, wine, bar; a brief's word works (roastery, bread, inn, bookshop, yoga studio, blacksmith). No trade for a
  restaurant, a ceramics studio, a patisserie, a salon, a jeweller, a goldsmith, a locksmith: its own photographs, else type. A **workshop**
  names its craft (`--trade blacksmith`, `weaving`, `letterpress`): only that craft's frames are dealt, so a smith's page
  never shows a weaver's loom; no craft named, nothing is dealt.
- `--sections`: the page's sections in order, in plain words (bar, roastery, oven, dough, rooms, breakfast, workshop,
  stems...). Each gets a detail of its subject; a section the library cannot show comes back empty and goes to the
  client's own photograph, the object, UI or type. Repeat a word for a row (`rooms,rooms,rooms`: three details, one
  orientation). **Dealt nothing, on purpose:** hero (unless `--draft-lead`), menu, visit, contact, booking, closing and
  call to action, and, without `--own-land`, area, landscape, road, street and sky.
- `--pictures N`: how many pictures the whole page carries, the client's own included (12 if not said). At most N/3
  library frames are dealt, earlier sections first; the later ones come back empty and say so. With `--draft-lead`
  the cap lifts: every section that is not text gets a frame when the library has one.
- Only photographs rated 7 or more, with no whole figure, no animal, no vehicle, no landmark and no mood frame (a
  curtain or plant shadows, a sky, fog, an aurora, a waterfall, a viewpoint), are dealt. A frame the curators or this
  review held back (`weak`, with its reason in `photos.json`) is never dealt.
- **The land is only ever the client's own.** Library land is a draft stand-in, dealt only for the region a `--place` or the `--brief` names (as the lead; `--own-land` adds the land sections).
  A photograph's source names its places, the most exact first (Westfjords, Iceland), and a frame is dealt when its
  most exact name is the client's place, or the client's place is a broader one it lies in. `--place "Lofoten, Norway"`
  deals Lofoten; `--place Iceland` every photograph of Iceland; `--place "Reykjavik, Iceland"` neither the Westfjords nor
  a frame tagged only "Iceland" (a broader tag than the client's place is never dealt); names match whole, so "Senjavegen"
  is not Senja. Several places go in one value: `--place "Iceland; Norway; Faroe Islands"`. A place the source names
  overrides `--setting`; `--setting coast,mountain,...` only narrows frames whose source names no place, and never
  deals land by itself. With a `--place` and no photograph of it, the land sections stay empty.
- Frames marked `moodOnly` (the file names a business, or it is another's named room) are never the client's room,
  counter or product: not the lead, not dealt to a trade that has its own premises (cafe, bakery, hotel, bar, bike,
  florist, workshop, food, shop, farm), and into a mood or interior section only for the rest.
- `--draft-lead`: a lead may be dealt (a sharp landscape frame of the trade's lead subjects; a latte-art close-up or a
  soft, hazy older file never opens a page). A hero the library cannot fill comes back empty: never a row picture blown
  up. `--own-land`: see above. `--detail-only` is accepted and does nothing: it is the default.
- `--commons-only`: Wikimedia Commons files only (the credit line then reads "Photographs via Wikimedia Commons").
- `--tone light|dark`, `--mono` (black and white, one deliberate frame), `--shop` (every make).
- A place page's `pick` prints its hints for a place: words **under** the photograph on the ground, no band, no tab, no
  closing text. Product and service pages get the band and calm-side hints.
- When `pick` says the library is short, search the open collections with the queries it prints (CC0, CC BY, CC BY-SA,
  looked at full size) before leaving the slot to the client's own or type. Detail frames held by default (`list` prints them live, after the full-size review that dropped 27 frames and merged 4; the 3 office rooms of the second merge were then set `weak`, as whole rooms; the third merge looked at 8 more at full size and kept none: a shopfront with its sign, two bars' counters and back bars, a breakfast room, a made-bed room, two breakfast tables rated below 7 and a half-eaten breakfast with a diner in the frame are all `weak`): cafe 19,
  bakery 4 (oven 3, dough 1), hotel 9 (7 details and 2 breakfast frames; its land only with `--own-land`), bike 6 (parts and a load, --shop only), workshop 5
  (smith 4, instrument 1, weaving 0, letterpress 0: a craft is dealt only its own), studio 5, books 5 (desk only: a pencil on a notebook, a binding, stacked books, pencils; the hands frames beside a laptop are not dealt, and the bookbinder's gilding is dealt only to a bindery, `craft: bookbinding`), food 5, shop 3, florist 3, farm 3, wellness 3, office 3 (2 desk, 1 card),
  bar 0, outdoors 0 (land only), wine 0. A trade that
  holds 3 or fewer gives a page at most that many; the rest is the client's own. `list` marks those trades `thin`.
- **Sections and subjects:** `hands`, `writing`, `notebook`, `paper` deal a hands or desk frame; `detail`, `texture`, `surface`, `linen`, `material` a detail, texture or desk frame; `breakfast` a hotel's breakfast frame (never a deli's);
  `rooms` a detail of a room, never the room. When a section's frames exist but these options keep them out (no `--own-land`, another craft, a motif already dealt), `pick` says so instead of "nothing in the library shows it".
- **Variety:** the seed ranks the deal (a frame rated 8 or more has a head start of 0.3 in a 0-1 draw, not a place at the top), so a cafe's or a bike shop's deals differ from seed to seed; a trade with only a few frames (bakery 4, office 3, the two breakfast frames) returns the same set in every seed, in a different order. `--history` is the only way to vary those: pass it every time, and a frame dealt before goes behind the fresh ones. A frame marked `soft` (the rusty chain on a cassette, bike) is dealt only when no sharper frame of its subject is left, and never leads.

## Place them

- A place page uses 4:5, 4:3 and 1:1 only; other kinds add 3:2. One ratio per row, equal sizes in a row, one dominant
  picture per screen or a row of three or four. Frames sit on the container lines (x 120-1320 on a place, 80-1360
  elsewhere; 342 wide at 390): full-bleed only as a hero or section layer. Left and right edges stay the same down the page.
- One visual world: one light, one grade, one register across the set. Hard sun on one product, a low-key set on
  dark timber or steel only when the whole set matches. Never studio black with daylight, HDR beside a snapshot,
  two photographers' grades. Black and white is one deliberate frame. Never the same frame twice on a page (a smaller
  file, a crop or a mirror of a frame is the same frame) and never three near-identical ones. On a product page
  the product whole in three sections at most, its use, its parts and the people with it in the rest (`sections.md`, Product, rule 2).
- **Hero**: plain full colour, as the client's own (Recipe 3 on a place: a full-bleed top photograph, 480 px tall, with
  nothing on it and the words below it); a software or product hero ends inside the screen. **Rooms**: one detail per
  room beside its facts, a place's rooms are the client's own photographs first. **Menu or goods**: the list in plain
  text beside the offer's composition, never one photograph per line, never a tab. **Photo bands**: product one or
  two; a place one, its `bleed` composition, never next to the hero, and a place closes on a 1:1 shopfront with no
  words (PH-72). **Compositions** on a place (`bleed`, `pair`, `trio`, `strip`, `tall-small`): `sections.md`
  section 4, Designed variety; never two sections built round one picture.
- Text on a photograph: never on a place; elsewhere the hero and one closing band only, on a calm part that is empty and
  dark (or light) at the desktop and the phone crop, or in a solid box, or off the photograph. No scrim, gradient, fade
  or blur. For product, service and software `pick` prints `words:` from the photograph's calm side; for a place it
  prints "under it on the ground". At 768 a 3:2 lead is cropped to its middle: when that puts the words over the
  subject, they go under it as on a phone.
- Every full-bleed photograph that carries words has a crop for 390 (`<picture>`, subject inside the middle 342px).
- Cut-outs only of the client's own subject (transparent WebP, `data-subject="product"`), on the page ground or one
  backdrop, no drop or fake shadow, never stock, never people or buildings. Supplier or maker images only inside a
  product grid, only what is sold, never the hero. Illustration only when the client already owns it, still.

## Show them

- Paste the `<img>` fetch prints. **What a library file is:** WebP, always a 1200 wide, some also a 1600, 1800, 2144
  or 2400 (list them with `list --trade`; the largest is the frame's own pixel width). The older Unsplash and Commons
  frames are downloaded at 500, 960 and 1280 (1920 for the hero) and converted to WebP when `ffmpeg` is on the path,
  else kept as JPEG. `fetch` leaves any file over its cap out of the `srcset` (hero 400 KB, any other 250 KB) and says so,
  so the 2400 of a busy frame often does not ship; it then prints the page estimate against 2,400 KiB, the figure
  `perf.mjs` FAILs above. **The hero's 2x at 1440 (2880 wide,
  PH-27) is not in the library**: the library hero is the largest file within 400 KB (1200 to 1800) and looks soft on a
  retina desktop. Another reason to replace it with the client's own.
- A hero (`--hero id`): `sizes="100vw"` (Recipe 3's top photograph is full width; never a vh term, which sends a tablet
  and a 3x phone to the largest file), `fetchpriority="high"`, eager, and a 780x584 crop for the phone in a `<picture>`
  `<source media="(max-width: 639px)">` (needs `ffmpeg`; subject inside the middle 342 px via the frame's `focus`).
  Every other picture is `loading="lazy"` and `decoding="async"`, `width` and `height` set, `sizes` set to the shown
  width. `--big id` adds the largest file to a full-bleed band only when it is within the 250 KB cap; `--lqip` puts the
  picture's 24px colours behind it.
- A photograph in a nav menu or a tab panel drops `loading="lazy"`; neither holds more than it must (carousels and
  sideways rows are never built). `object-position` is the subject's place (`focus`), so a phone's square crop keeps the cup or the hand; a
  `wide` one (a row of three) keeps `--ratio: 66.7%` on its frame at every width.
- **A photograph is visible from the first paint**: never in an element that starts at opacity 0, clipped or moved for a
  scroll reveal, never under a print, dissolve or mask that develops on load, never a video in its place. Shoot 1440,
  1024, 768 and 390 and look for any empty frame (a grey, blank or half-loaded frame counts): an empty ground is a fault.
- **No print, grade or effect on any photograph**: no halftone, dither, duotone, engraving, grain, glitch, filter or
  blend mode, and no canvas over half of it. Mixed light gets a crop and one ratio system, not an effect. A print is a
  tech page's one effect, on a non-photo ground.
- **Hover** (PH-25, one wording with `motion.md`): a photograph in a card that links zooms to 1.03 (1.02 to 1.03 is the
  range) over 600 ms inside its own mask (the frame is `overflow: hidden`, never grows or moves); a photograph outside a
  linked card does nothing, so on a place every photograph that leads somewhere is a link (a room to its booking,
  goods to their card, the place to its story) and the hover shows in every section. No tilt, no rotation, no Ken Burns at rest; on a place the photograph never changes
  opacity. The linked card also lifts 2px (`motion.md`).
- Place photographs are square-cornered, with no border, shadow, overlay or frame; product and service use one radius
  for every photograph; software windows one radius of 12 to 20px.

## Credits and words (PH-38, CO-22)

No caption, label or description sits under or on any picture (house rule), and no credit, "sample" or example note: a sold
item's name and price sit inside its card's padding (`copy.md`), never as a line under a bare picture. The place's name
goes in the alt text. **Credits are ONE footer line** in the legal row that links or opens the credits list, never a
link per photograph in the footer (in testing: 18 and 20 credit links read as a credit wall). `photos.mjs credits --out .`
prints the line, "Photographs via Unsplash and Wikimedia Commons" (the sources used, never the photographers; at
most 110 characters), and the list; paste the line in the footer and the list on its own page: `--write` makes `credits.html` in the site's legal-page shell, `--href <page>` points the line elsewhere. The list gives each photographer, licence and
source page, `adapted` after any frame cropped beyond its frame (`--adapted id`). A
public-domain frame (the Public Domain Mark) is listed with the Mark's page and its photographer still named. `--text`
prints the same line and list as plain text for a report. Every word on a page is live text, never baked into an image.

## Never

- Another business's identifiable room, counter, sign, cup, bag or product shown as the client's (a whole meeting room, lounge or breakfast room counts: it would pass for the client's own); a machine with its
  maker's name; a named bar's whole room. A face as staff, guest or customer: the library holds hands, backs and faces
  out of frame only. Another place's coast, street or landmark as the client's; a lone house on a hotel page.
- The trade's stock shot: latte art from above, beans filling the frame, the croissant-and-cappuccino still life, a
  made bed, flour thrown on black, a whole figure.
- Mood stock (a curtain, plant shadows, a sky, grass, a forest, fog, an aurora, a waterfall), an animal or a vehicle in
  the frame, a recognisable viewpoint, AI images, composites, Street View, a sight far from the place, a gradient,
  grain, pattern or shader standing in for a photograph.
- The library's frames repeated across builds: pass `--history` every time, so a frame dealt before is not dealt again.



---

## `references/scenes.md`

# Big scenes

The one stretch of a tech page where the whole screen becomes a scene, driven by the scroll. Each is
a folder in `assets/scenes/<id>/` (`scene.js`, `scene.css`, `meta.json`, `demo.html`); `index.json`
lists them, `lib.js` is the held stage they share, `scenes.js` loads them, `print.js` mounts an
object render for the two object scenes.

## Who gets one

- **Tech pages only:** software (apps, AI, developer tools, fintech), tech (a technical product,
  hardware, a network) and gaming. A place, a service or a plain product (site-kind other: a cafe,
  a guesthouse, a shop, a studio) never gets a scene: it gets photographs. The `types` in `index.json` are exactly
  `software`, `tech` and `gaming`.
- **At most one a page,** and only when the brief has what the scene `needs` (its own photographs,
  its own screen, its own words; a game's key art and in-engine shots are its photographs). No need
  met, no scene: never a stand-in for the client's pictures. A game without art files renders its
  key art with the product-render helper (its hero object or a scene of its own objects) on the
  `product` stage and in its world section, never an effect in its place (`sections.md`, Gaming).
- **Deal at random** among the scenes whose `fits` has the section, whose `types` has the page's
  type and whose `needs` the brief meets, weighted by `weight`, away from the last three in
  `.taste-skill/scenes-history.json` (the command is in `effects-usage.md`). Name the scene and its
  section in the plan. A big scene is the page's one effect: no shader ground, no WebGL part beside
  it.
- **The hero holds one screen at rest,** so a scene is dealt as the hero only when its `restH` is 1.
  A scene whose `restH` is 2 (today all three hero scenes) goes below the hero only, as a
  two-screen section (`--h: 2`) whose heading is an h2; the hero is then dealt as usual.
- **The two object scenes** (`fixed-hero-object`, `object-through-giant-type`) draw a WebGL render
  of an object of the client's own trade (a deck of cards for a card-game engine, a globe for an
  edge network); never an object of another trade, never a cup on a cafe.
- **The rest of the page stays calm:** no card, row or tile moves because the page scrolled. Beside
  a scene the page may still take one or two section moments (the house overrides: one big scene and
  one or two scroll moments), dealt as `moments.md` says (one on a short page, two on eight
  sections or more), never in the scene's section or the one beside it, never one in the scene's
  `avoidMoments` or its twin (`effects-usage.md`, Big scene).

| id | fits | types | needs | WebGL | restH | phone |
| --- | --- | --- | --- | --- | --- | --- |
| `descend-through-weather` | hero (below it only) | tech, gaming | two photographs of the client's world, high and low | - | 2 | still |
| `shaped-window-over-fixed-world` | hero (below it only) | tech, gaming | one wide photograph of the client's world | - | 2 | still |
| `fixed-hero-object` | hero (below it only) | tech, gaming | an object render or cut-out, 1-4 chapters | 1 | 2 | still |
| `powers-of-ten-pullback` | product | software, tech | the product's UI at true size | - | 1 | still |
| `product-assembles-into-its-action` | product | software, tech | the screen as HTML, 4-6 steps | - | 1 | still |
| `parts-lock-into-the-whole` | product | software, tech | the screen cut along its panels | - | 1 | still |
| `fly-into-the-shape` | between, product | software, tech, gaming | the mark as one path, one dark photograph | - | 1 | still |
| `letter-physics` | statement | software, tech, gaming | a claim and its answer | - | 1 | light |
| `object-through-giant-type` | statement | software, tech, gaming | a quote of 3-5 short lines, an object | 1 | 1 | still |
| `dot-becomes-the-full-stop` | statement | software, tech, gaming | one claim of 4-6 words | - | 1 | light |
| `letter-bar-floods-the-ground` | between, statement | software, tech, gaming | two statements, an inverse section after | - | 1 | still |

`powers-of-ten-pullback` is never the hero: its first screen has no headline and no action.
Every scene's header comment in `scene.js` holds its markup and options; `meta.json` holds its
`look`, `needs`, `never` and `avoidWith`.

## Put one on the page

Copy the scene's folder and the shared files (`scenes.js`, `lib.js`, `scenes.css`, and `print.js`
for an object scene) into `assets/scenes`. Write the markup from the scene's header comment with
the client's own words and pictures. In `<head>`, the one line that marks script early and both
stylesheets, so the finished composition is styled without script and nothing jumps when the scene
mounts; at the end of `<body>`, the runtime once:

```html
<head>
  …
  <script>document.documentElement.classList.add('sc-js');setTimeout(()=>document.documentElement.classList.add('sc-safe'),2500)</script>
  <link rel="stylesheet" href="assets/scenes/scenes.css">
  <link rel="stylesheet" href="assets/scenes/<id>/scene.css">
</head>
…
<section class="sc" data-big-scene="<id>" data-big-scene-opts='{"hold": 1}' style="--h: <the scene's restH>" aria-labelledby="…">
  <div class="sc__stage">…</div>
</section>
…
<script type="module" src="assets/scenes/scenes.js"></script>
```

The section is a direct child of `main`. `<html data-scenes-ready>` says it is mounted;
`data-scenes-over` is a fault. Scenes take the page's tokens, face, radius and buttons.

### Its height (rule 3)

The scene's section stays in the page rhythm like every other: exactly one or two screens, its
words under the nav. Live it is (hold + 1) screens; `lib.js` and every scene default `hold` to 1,
so the live section is two screens (1800px at 1440x900). At rest (a phone, reduced motion, no
script) `scenes.css` keeps the section's `--h` and padding as a minimum height, so give it `--h` =
the scene's `restH` (the table above) and write no page CSS for it: a fixed height would cut the
composition and run it over the next section. Never hide a scene from the check with
`data-screen="free"`. Look at the 390 shot: a rest composition that fills under half its screen
reads empty (rule 2).

## Rules

- **The demo is a placeholder:** every picture, word and object in a shipped scene is the client's.
  Credit the photographs in the footer line, with "adapted" for one cropped beyond its frame.
- **Readable without it:** the scene's words are real text in the markup, in reading order; the
  finished composition says everything the scene says.
- **Native scroll only:** the stage sticks for `hold` screens; nothing captures the wheel.
- **Phones get the still or the light version, never the full scene:** under 768px every scene
  shows its finished composition, except the two type scenes marked light (no depth, nothing
  overlapping).
- **Reduced motion, no script, a failed module:** the finished composition, which is also the
  hold's end. The object scenes then show the object's still picture and mount no WebGL.
- **WebGL:** one context at most a scene, taken from the page's shared budget (`lib.glBudget`,
  `window.__tpGl`, four on a page), mounted only while the section is live and within a screen of
  the viewport, destroyed when it leaves; a still picture under it whenever WebGL or the shader
  fails. Never a GLSL ES reserved word as a name.
- **Nothing moving crosses words being read;** statements read whole at every rest. Text over a
  photograph stands on a flat band of the page's ground or on the photograph's calm, dark part at
  4.5:1 (3:1 for display text); never a scrim or gradient over a photograph (`system.md`).
- **Cost:** transform, opacity and clip-path on fixed-size layers; never width, height or an SVG
  clip repainted every frame.
- **No captions** that explain the scene, under it or beside it; no card chrome, chips or labels
  flying with the scroll.

## Check it

```bash
node <skill>/assets/scenes/_demo/shoot.mjs shoot --out <dir> --profile <your own Chrome profile dir> [--only <id>] [--page <url>] [--reduced] [--port 5836]
node <skill>/assets/scenes/_demo/shoot.mjs index [--out <file|dir>]   # from the project folder: its own index.json
```

`index` writes the project's own `assets/scenes/index.json` when run from a project folder that has `assets/scenes` (or with `--out <file|dir>`).
Inside the installed skill it refuses and writes nothing; `--in-skill` rewrites the skill's own index on purpose, which
is not a page's work. A page needs it only after a scene's `meta.json` changes, so on a normal page skip it.

One headless Chrome with WebGL on the CPU, closed by its own PID: start, middle and end at 1440 and
390, a contact sheet a scene. Read every sheet; shoot `--reduced` once.



---

## `references/sections-library.md`

# Section library

The recipe of every section id in `sections.md`. Read only the recipes you use. Each gives the job,
the numbers at 1440 and 390, the copy with an example, the visual, the motion and the mistakes the
checker or a reviewer catches. A place page follows `sections.md` section 4 wherever it differs.

## What every recipe assumes

- **Frame.** `system.css` at 1440: `.wrap` 1280 at x 80 (a place 1200 at x 120), gutter 24, h1 72,
  h2 48; at 390: 342 at x 24. Every section is one or two screens, its h2 first, `--padt` under its
  top (`layout-v4.md`). Never add a number the system lacks; a missing value becomes a token.
- **Splits** are the page's one split pair, text left and the visual right, top-aligned
  (`.grid`, never `.grid--middle` on a split), never mirrored; on a phone text first.
- **Cards.** `cards.md` builds the card, its panel, the ground and the UI on it, and wins over
  anything here except the depth rule: two boxes at most. A card whose panel holds UI is
  `.card--open` (no box: its words on the page ground, the panel under them with four round
  corners) or runs its panel flush (`.panel--flush`); an inset panel holds only a picture. From 640
  to 1023 a card with a panel takes the full row; from 1024 to 1279 span-4 cards with a panel go
  two-up, so a span-4 panel is never under 304px.
- **Grounds in frames (tech).** The page has one effect and one card group's still grounds
  (`effects-usage.md`). Where a recipe below says "the card ground", it means that group's dealt id
  with its own seed per panel; "the effect" means the page's one effect, only in the hero or the one
  `[data-visual]` frame. Every other frame takes the lit ground plain (`.frame--lit`), a flat
  `--g-alt` panel, a photograph or a diagram. Product, service and place frames hold photographs on
  flat colour: never a code ground.
- **Fragments** are pasted from `assets/ui/<name>/fragment.html` into their slot and rewritten:
  every name, number, subject, app and logo becomes the client's (`data-ui-load` shows the kit's
  sample text: drafts only). They sit in a `.stage` at their true size (`meta.json` `size`,
  `fluid`), never scaled, at the place the recipe names (else `meta.json`'s `place`). A `.fit` slot
  takes only a fragment whose minimum width fits it (`cards.md`): 324 in a 2x2 card at 1024, 256 in
  a span-4 card. The edge rule (every edge 24px clear, or cut by 24px or more with a fade) holds at
  1440, 1280, 1024 and 768; move `--ax`/`--ay` until it does. On the phone cards.css places each
  fragment 16px in, its top at `--ay-sm` (24px unless set).
- **Motion.** Fragments hold their finished picture; the one loop of a card group, split or wide
  frame carries `data-ui-loop` and its pause button; below the hero two loops are never on one
  screen; nothing moves because the page scrolled. Every timing: `motion.md`. Other kinds: no loops.
- **Classes.** Only the system's, cards.css's and the kit's. Where a recipe needs one more rule it
  says "page CSS"; that only ever sits inside a visual, plus a place's visit panel (`sections.md` section 4).
- **Photographs** lead every main section of a product, place or service page: the client's own,
  else picked with `photos.mjs` (`photos.md`), one look, shown plain, credited in the one footer
  line. No caption, name, price or link line under a bare picture: a sold item's name and price sit
  inside its card's padding.
- **Names** in the examples (Ferrow, Rotaro, Kestrow, Ledgewick, Clausewise, Fenn, Halden...) are
  invented to show the form. Copy how they are written, never the words. Proof, quotes, customers
  and figures come only from the brief (`copy.md`).
- **Logo, buttons, links.** `.nav__logo` holds the client's SVG, else the dealt mark and the name
  (the same in the footer). Buttons take the dealt look from `<html data-buttons>`; the nav's main
  action is `.btn.btn--primary` at the one button height (`system.md` Nav). Nav words, buttons and footer links go to `#ids`, the logo
  to `#top`, Contact to `#contact`; Privacy and Imprint to pages you write, or left out.

# Navigation

All four share the bar in `system.md`: fixed, opaque, 72px (56 on a phone), a 1px hairline, the
same at every depth; a panel opens after 150ms of hover with a fade and a 6px drop, a click on the
word goes to its section, never `preventDefault`. system.js adds the phone sheet, Esc and
`aria-expanded`; never write a second handler.

## nav-mega

**Job and use.** The company's map one hover away: the product grouped by what the visitor wants,
each link named and explained in one grey line, the newest release in one picture card. Software
with 6 to 12 feature pages, or a company with several product lines.

**At 1440.** `header.nav` > `.wrap.nav__bar`: the logo, 4 to 6 one-word `.nav__link`s (a `.chev`
only on those that open), then `.nav__actions` with Sign in (a plain `.nav__link`, only for an app
with accounts) and the primary. A menu is the item's `.nav__menu`, full width under the bar,
holding `.wrap.grid`: two or three `.menu-col.span-3`, then one `a.menu-card.span-3` ending at x
1360 (`start-10` with two columns). A column is a `.t-label` heading over 3 or 4 links, each the
feature's name with one grey line of at most 30 characters. Small menus (Resources, Company) open
the same panel with plain columns and no card.

**At 390.** The system's sheet: rows of 56px; a word with a menu opens its links in place under
it on a tap (system.js's `.nav__expand`; it opens at once, nothing animates height), the menu
card as a plain row, the two buttons full width at the foot.

**Copy.** Bar labels: one plain word in the buyer's words. Links: the feature's name (1 to 3 words)
and what it does (3 to 7 words). Example, Ferrow (booking and notes software for physio clinics):
bar Product, Clinics, Pricing, Resources, Company; Product: Front desk (Online booking / Patients
book a free slot; Reminders / Texts before each visit) and Treatment (Patient notes / Templates for
every treatment). Card: New / Online payments / Take a deposit at booking.

**Visual.** Only the menu card: its `.panel` (160px) holding a `.stage.stage--fade-br` with one
fragment `.at-corner` (24px in) cut by the right and bottom, rewritten to the newest feature, held
still, on the lit ground plain. No icons in the columns.

**Mistakes.** A bar narrower than the `.wrap` or links wrapping; chevrons on plain links; a menu off
the grid; a second picture card; grey lines over 30 characters; vague labels ("Solutions",
"Platform").

## nav-cards

**Job and use.** Two to four distinct products shown as picture cards with a plain name and one
line; resources as plain link columns. A company with two to four products that each have a screen
or a real photograph, a studio with three service lines and real work, or a place's offer (four
photograph cards).

**At 1440.** The bar as in nav-mega. Product's `.nav__menu` holds `.wrap.grid` with three
`a.menu-card.span-4` (410 wide): a `.panel` (page CSS `.menu-card .panel { --p-h: 200px }`) with
that product's fragment `.at-corner` in a `.stage.stage--fade-br`, or its photograph filling the
panel; the title in `.t-card`, one grey line of at most 52 characters, inside the card. A place:
three span-4 cards at 384x288 (4:3), each the client's photograph, the name at 16/500 and the price
from, no fragment, ground or shadow.

**At 390.** The sheet shows each menu card as a row, its title over its line, the picture hidden.

**Copy.** Card title: the product's name or plain job; the line what it does. Example, Ferrow: Online
booking / Patients book a free slot from your website; Patient notes / Notes from your own
templates.

**Mistakes.** One seed on all three; panels of different heights; text on the panel; titles
wrapping; names that mean nothing alone ("Flow", "Pulse").

## nav-centre

**Job and use.** The quietest bar: the words in the middle of the bar, the logo on the left line,
the main action on the right line. Software and services with four or five plain words.

**At 1440.** `header.nav.nav--centre`: system.css centres the `.nav__links` group on the page axis;
the logo and actions keep the `.wrap` lines. Four or five words, never wrapping at 1024. Menus as
nav-mega's small menus.

**At 390.** The logo left, the toggle right; the system's sheet.

**Mistakes.** A group so wide it touches the logo or the button at 1024; a second row.

## nav-split

**Job and use.** A place, shop, restaurant or studio people visit: the name in the middle, three
short words on the left, the main action on the right. One word (Rooms, Menu, Classes, Shop) opens
the panel with photograph cards of what is offered.

**At 1440.** `header.nav.nav--split`: system.css puts the links in the left third, the logo (mark and
name, 28px in the display face) on the page's centre line and the actions in the right third.
Four words, the low end of `system.md` Nav's four to six, since they share the left third; at
1024 a word never wraps.
The menu word's `.nav__menu` holds `.wrap.grid` with three or four `a.menu-card.span-3` (on a place
four at 282x212, 4:3), each the client's photograph (`img.frame__img`, no effect) with the name in
`.t-card` and the price from inside the card. Actions: the primary ("Book a table") and at most one
plain word the client really has (Gift cards when it sells them), else none.

**At 390.** The logo moves left, the toggle right; the sheet (a place adds the street and the week's
hours at its foot).

**Copy.** Example, Fenn (a pottery studio in Leipzig): Classes (menu: Taster evening / from €39;
Six-week course / from €260; Open studio / €18 a day), Shop, Studio, Visit; "Gift cards", "Book a
class".

**Mistakes.** Unequal thirds pushing the logo off centre; more than four words; UI fragments in the
menu; a second row of links; a shadow on the open panel.

# Heroes

The ten heroes and the place hero, with their numbers at 1440 and 390, are in `layout-v4.md`
section 3; paste the dealt one from `assets/layout/hero-<id>.html` and rewrite its words and
pictures. What the recipes add:

- **Copy** (`copy.md`): the h1 names the category and the buyer or place in 2 to 8 words; the
  sub-line 15 to 30 words on how it works and the main benefit, with one hard fact (a place: 80
  characters with today's hours); the primary as a verb and an object, word for word in the nav, the
  close and the phone bar, and one quieter action (a place: none). Example, Halden Dental (a clinic
  in Malmö): "Dental clinic in central Malmö"; "Check-ups, cleaning and fillings from €95. Book
  online, most visits within a week."; "Book a check-up", "See prices".
- **Pictures** are the work: a photograph of the product in use, the place or the people (product,
  place, service); a phone for an app (a `.device` 280x570 built in page CSS, an 8px bezel, radius
  32, one fragment in its phone layout, `role="img"`); one window for a web app (`.frame--split` with
  `window` `.at-corner.to-edge` 56/56 and `cursor` or `notify` `.at-over` its lower-right edge); a
  technical product's object (`<div data-print="print-…">` on the lit ground, tech only). App
  buttons in text ("Download for iPhone"), never store badges beside the system buttons.
- **Window heroes** (`centred`, `collage`, a split window): the fragments pasted and rewritten to the
  client's names; the main one may loop (tech, with the frame's pause button), the second holds
  still; never more than two pieces, never tilted or scaled, never the kit's sample text, never a
  lone fragment floating in the middle of the frame.
- **The drawing** (`figure.drawing`, `starter.html`): only as a dimension figure beside a
  product's specs, on a page whose photographs already show the product: its side view as one
  inline SVG in true proportions (one unit a millimetre; `viewBox` the product plus 6%; `--ar` its
  width over height), two or three dimension lines (`.dim`) with their figures as
  `span.drawing__dim`. Never the hero, never the product's only picture, never on hardware (a
  technical product shows its photographs or the client's render), never on a page without
  photographs: that page shows its product render (`sections.md`, Product; in testing: a drawn SVG
  arm as a robot maker's hero).

# Proof

Proof only from the brief: real customers, quotes, reviews, press and figures (`copy.md`). Without
it, leave proof out; never invent it.

## logo-row

**Job and use.** Real organisations that use the product, docked under the hero's content (software
and product only): only the client's real customers whose logos may be shown.

**At 1440.** The hero's docked row (`layout-v4.md`, at most 96px): `p.t-small.muted` (14px, grey,
on the left line, 24px above the row), then `.logos`, one row from x 80 to 1360: up to six logos
28px tall, each the customer's own SVG in its full colours (rule 7, `icons.md`). Still: no
marquee, light band, fade or tiles; a logo never moves (MO-57).

**At 390.** Hidden, unless the hero still ends by H - 24 - bar; then a 3-column grid.

**Copy.** The line over the row: who uses it, plain ("Clinics using Ferrow").

**Mistakes.** Logos of non-customers or invented wordmarks; a marquee; mono or dimmed marks; a boasting line; a logo
row on a service or place page.

## quote-stat

**Job and use.** A named customer the brief gives says what changed, beside one number that backs
it up. Merged into the section above when it would hold under 495px (`sections.md`).

**At 1440.** As the last block of the section above, or its own `section.section.ground-surface`.
`.grid`: `figure.quote.span-8` and a `div.stat-aside.span-3.start-10`, both from one top line. The
`blockquote` (28px, at most 40 words), then 32px under it `div.person` (a `div`, never a
`figcaption`): a 40px photograph of the person (a quote needs a face) or the company's logo, the
name over role and company. The stat: `p.t-stat` (38 at 1440, 28 at 390) and a grey line of up to eight words.

**At 390.** Quote, person, then the stat, a 1px hairline and 24px above it.

**Copy.** A before and an after, no praise words. Example form: "We used to rebuild the rota every
Sunday night. Now it takes twenty minutes on Friday." / name, role, home / "20 min", "to plan a week
of shifts".

**Visual and motion.** Still. On tech the number may be filled with the effect (`fx-stat`) only when
that is the page's one effect.

**Mistakes.** A quote the brief does not give; a stock or missing portrait; a stat that is a slogan;
a count-up.

## customer-proof-row

**Job and use.** Three named customers from the brief, one measured result each. B2B software,
studios, products sold to businesses.

**At 1440.** `.section-head.section-head--row`: the h2 left, `a.link` "All customer stories" right
on its bottom line. 48px below, three `article.card.span-4`: the customer's logo as an `img` 28px
high, or its name as `p.t-card`; 24px; the story title (one line, at most 7 words); one line;
`a.link` "Read the story"; then `.panel.panel--flush` with `stat` `.at-corner.to-edge` (`--ax: 24px;
--ay: 40px`, `data-ui-opts='{"fill":true}'`) in a `.stage.stage--fade-br`, cut by the right and
bottom, its number and change in view. A service or studio: a photograph of each customer's work
fills the panel instead.

**At 1024 to 1279.** Two cards, then the third across the row. **At 768 and 390.** One column.

**Copy.** Title: who did what. Stat: what was counted (at most 28 characters), whole numbers, the
change chip, "Before x · After y".

**Motion.** Tech: the first card's stat loops; the other two hold still.

**Mistakes.** Customers the brief does not name; a percentage as the count; a carousel; cards turned
into quote cards.

# Features

## product-statement

**Job and use.** One plain paragraph on what the product is and what makes it different, then the
product in one wide picture with three facts. Products (never on a place). Never straight after a
hero frame of the same width.

**At 1440.** The statement on `span-8`: an h2 (48px, at most 4 lines), the first sentence in ink,
the rest in `<span class="muted">`. 48px below, `.frame.frame--hero` on `span-12` (page CSS
`aspect-ratio: 2 / 1`) holding the cut-out photograph, centred, at least 64px from every edge; 48px
below, three facts on `span-4`: a 1px hairline, the value at 28px with its unit, a grey line. A
technical product may show the client's render or its object of its own kind instead (`.frame--lit`
with `<div data-print="print-…">`, its `hero` preset large and right of centre, the facts in
`div.frame__text` at the lower left). A product or hardware with no photograph shows its product render
(`data-product`, place `stage`) the same way, on the page's flat ground (the lit ground on hardware) (`sections.md`, Product; `effects-objects.md`, Product renders).

**At 390.** The h2 at 30px; the frame square, facts under it as a list.

**Copy.** Example, Pellum (a desk lamp): "Pellum lights a whole desk without glare. <grey>One dial
dims it and turns it from warm light to daylight.</grey>"; facts "1,100 lm" Brightness, "2,700 to
6,500 K" Colour, "9 W" Power.

**Motion.** A cut-out: none. A technical product's object: its slow turn and its answer to the
pointer (the page's effect), with its own pause button.

**Mistakes.** A slogan; the grey part in a second paragraph; a cut-out in a box or touching the
edge; an object that is not the client's kind of product; facts that are claims.

## features-2x2

**Job and use.** What it does, in one screen: four features of equal weight, each with its own
small working visual (the 2x2: a headline, two lines, an inset panel with a smaller card on it).
When one feature matters more, use the bento.

**At 1440.** `.section-head` with an h2 that runs on in grey. 48px below, `.grid` with four
`article.card.card--row.span-6`, two boxes deep: on a light page `.card--open` (the title and lines
on the page ground, the panel under them), on a dark page the card's box with `.panel.panel--flush`
(x.ai's cards). Each card: the title, two lines in ink (16 to 20 words), then the panel (page CSS
`#<section> .panel { --p-h: 336px }`) holding a `.stage.stage--fade-b` with one pasted fragment:
- `chat` `.at-rise.fit` (`--fit-max: 400px; --ax: max(24px, 50% - 200px)`, `--ay` and `--ay-sm`
  56px): out through the bottom by 24px or more; `search` or `stat` the same with `.to-edge`
  (`stat` with `data-ui-opts='{"fill":true}'`);
- a short stack (`notify` with titles of at most 26 characters, `checklist`, `integrations`)
  `.at-rise.fit` low, `--ay` and `--ay-sm` `calc(100% - 180px)`, its last row cut;
- `toggles` `.at-right.to-edge` (`--ax: 32px; --ay: 56px`), cut by the bottom;
- `window` (`{"compact":true}`) `.at-corner` 24/28 on a flush `.panel--device` whose bar names the
  app and its status;
- a diagram card (`diagrams.md`): `<div class="dg" data-diagram="<preset>">` filling the panel.
Not `calendar` (its month must show whole), `doc` or `code` (wider than the 324px slot at 1024).

**At 1024.** The panels are 372 wide: a `.fit` fragment narrows to 324, the others stay cut.
**At 768 and 390.** One card per row; each fragment at its corner in its own layout.

**Copy.** The h2 at most 12 words with its grey part. Titles: a verb and a concrete object. Lines:
one or two sentences with one concrete detail. No buttons in the cards. Example, Ferrow: "Run your
practice from one app. <grey>Bookings, notes and payments.</grey>"; "Takes online bookings", "Takes
card payments", "Builds treatment plans", "Sends text reminders".

**Visual.** Tech: the card ground, one seed per panel, `data-fx-params='{"drift":0}'`, lit by
system.js; four different fragments or diagrams, real app icons where it names an app. Product or
service: a photograph of each feature fills the panel.

**Motion.** Tech: the first card's fragment or diagram loops (`data-ui-loop`); the others hold still
and play while the pointer rests on their card. Linked cards lift 2px.

**Mistakes.** A card that moves on scroll; panels out of line; a fourth line of text; the kit's
sample text; noun titles ("Peace of mind"); three boxes deep; a widget floating dead centre; a
1-23px strip of ground under a fragment.

## bento

**Job and use.** One main feature large and four small. Software with one lead feature, or a
product with real photographs of its main part and four details.

**At 1440.** `.grid`: row one `article.card.card--row.span-8` and `.span-4`, row two three
`.span-4`. Every card: title, two lines in ink, then the panel, two boxes deep as in features-2x2,
one `--p-h` for the group (336px). Wide card: `window` `.at-corner` (40/48, cut by the right and
bottom, `.stage--fade-br`), or `files` `.at-corner.wide` (`--w: 680px`). Small cards (panel 347 at
1440, a `.fit` slot of 256): one fragment cut by the bottom: one that narrows to 256 centred
`.at-rise.fit` (`chat`, `search` with `.to-edge`, a short stack low); `toggles`
`.at-right.to-edge`; or a wider one (`stat`, `notify`, `cursor`) at its true width `.at-corner`
(`--ax: 24px; --ay: 40px`), cut by the right and bottom. A `voice` call goes where its `meta.json`
says and is then the group's loop.

**At 1024 to 1279.** The wide card across the row, the four small ones two by two.
**At 768 and 390.** One card per row.

**Copy.** Wide card: the main feature as a verb and an object; small ones 2 to 4 words. Example,
Ledgewick (bookkeeping for freelance designers): "Reads every receipt" / "Drop in PDFs or phone
photos. The date, amount and VAT are filled in."; small: "Matches bank payments", "Tracks VAT",
"Sends invoices", "Exports for your accountant".

**Visual.** As features-2x2. A product: photographs in every panel, one look.

**Motion.** Tech: the wide card loops; the four small ones hold still. Never two loops in one bento.

**Mistakes.** Text in different places on different cards; small-card copy over two lines;
`calendar`, `doc` or `code` in a small card; a bento next to another card grid.

## split-text-left

**Job and use.** One thing the product does, in a few sentences and three facts, beside a picture
that shows exactly that. The workhorse for software, products and studios.

**At 1440.** `.grid`, top-aligned: the text on `span-5` (h2; 24px; two or three sentences at 20px;
24px; up to three short facts as plain lines; 24px; one `.link`) and
`.frame.frame--split.span-6.start-7` (5:4, square on a phone) holding a `.stage.stage--fade-br`. The
main piece is cut by the bottom, never floating with ground on all four sides:
- `window` or the client's screenshot `.at-corner.to-edge` at `--ax`/`--ay` 56px, cut by the right
  and bottom; `files` the same with `.wide` (`--w: 680px`);
- a narrower piece (`doc`, `code`, `chat`, `search`, `checklist`) `.at-rise.to-edge`, centred by
  `--w` and 56px down; a short one (`slider`, `toggles`) `.at-rise.fit` 40px down, cut below its
  second row.
One small piece that shows the result (`cursor`, `notify`) only over a `window` or screenshot:
`.at-over` its lower-right edge (`--bx: 24px; --by: -40px`), never over its first rows (Figma's
panel with a small card over the product UI).
A product or service: the frame holds the photograph of the part or the work the text names
(`.frame--photo`, 628x471), never UI.

**At 1024 to 1279.** The frame is 436 to 564 wide: the main piece alone.
**At 768 and 390.** Text first, the frame 48px below, full width.

**Copy.** Heading: the job and its result. Sentences in the order the picture plays. Example,
Clausewise (contract review for small law firms): "Finds risky clauses in contracts"; "Upload a
contract and every clause is checked against your firm's playbook."; link "See how review works";
`doc` rising out of the bottom with "unlimited liability" marked.

**Visual.** Tech: the effect when this frame is the page's `[data-visual]`, else the lit ground
plain. The main piece shows the text step for step; the small one shows what comes out.

**Motion.** Tech: one loop, in the small piece or the main one.

**Mistakes.** Text and frame not top-aligned; a four-line h2; a picture that shows something the
text does not say; a button pair instead of one link; a second split on the other side.

## tabs-tour

**Job and use.** Software only: three to six jobs, one at a time, in a frame that stays still.
Click only, never timed.

**At 1440.** `.grid`, top-aligned: left `span-5`, the `.section-head` (h2, grey line), then
`div.tabs[role=tablist]` with 3 to 6 `button.tab[role=tab]`, each with `aria-controls` naming its
`[role=tabpanel]` (two sentences and a `.link`) and its screen (`aria-controls="tab-1 screen-1"`).
Right, `.frame.frame--split.span-6.start-7` with a `.stage.stage--fade-br`: one slot per tab (all
but the first `hidden`), each placed as split-text-left's main piece, cut by the bottom; every panel
one fixed height, so the frame never resizes. system.js shows a tab's panel and screen together.

**At 390.** The tabs wrap onto rows (never a swipe row); the frame 48px under the active panel.

**Copy.** Tab labels: a verb and an object, 2 or 3 words, one grammar. Example, Ferrow: "Book a
session", "Move an appointment", "Pay by card", "Follow exercises".

**Motion.** The indicator slides on a click (`motion.md`); only the shown screen loops.

**Mistakes.** Tabs built as divs; noun labels; a frame that changes size; the same fragment on two
tabs; tabs on a product, service or place page.

## chapter

**Job and use.** One feature area in depth: a paragraph, a link, a wide frame of the product doing
it, four feature names. Two to four in a row for a platform: a chapter series is the one place
where neighbours share a layout. Usually a two-screen section (`.g2`).

**At 1440.** `.grid`, top-aligned: the h2 on `span-5`, and on `span-6 start-7` a grey paragraph
(about 25 words) with a `.link`. 64px below, `.frame.frame--hero` with a `.stage` (16:7): the area's
main screen (`window`, `code`, `doc` or `files`) `.at-rise.to-edge` 64px down and the one action
(`cursor`, `notify`, `stat`, `search`) `.at-over` its right edge. 48px below, four `div.span-3`: a
feature name and one grey line.

**At 390.** Text first; the square frame keeps the main screen; the four names as a list.

**Copy.** Example, Kestrow (freight booking for haulage firms): "Book loads in one place"; "See
every load your customers send, quote it and book a truck from one screen."; names "Imports orders"
/ "From email or a CSV file".

**Motion.** One loop per chapter; in a series only every other chapter loops. Nothing revealed or
scrubbed by scroll.

**Mistakes.** Fragments half-transparent or tilted; the action covering the main screen's only
readable rows; repeats that change the template.

## app-frame

**Job and use.** The product itself, big, the way Linear, Cursor and Vercel show it: one real app
window across the `.wrap`, the list beside the open item, the app's own chrome. Every software page
has one, in the hero or within the first three sections (in testing: a code-review page whose review
was one small diff card centred on a sage panel scored about 3.5 points under Linear, whose review
band puts the pull-request list beside a full-width diff in one app frame). Never on gaming,
product, service or place.

**The two panes** (kit fragments, rewritten to the client's names; the list is always `window`):

| Product | List pane | Open pane |
|---|---|---|
| Code review | `window`: pull requests | `diff-review` (the comment and Apply in its top 250px) |
| Support, inbox, CRM, agents | `window`: conversations | `chat` (the open thread) |
| Docs, contracts, knowledge | `window`: documents | `doc` (the page with its marked phrase) |
| CI, deploys | `window`: runs | `pipeline-board` (wide: nodes and log) or `terminal-run` |
| Booking, scheduling | `window`: bookings | `calendar` |

The `window`'s rows: `.ui-win__who` the person (author, customer, owner), `.ui-win__sub` the item
and its detail ("Retry settle jobs · +4 −3"), the status chip the product's own states (`data-open`,
`data-work`, `data-done`), sidebar labels one word each. Write 9 or more rows and enough lines in
the open item (24 or more for a diff) that both panes run past the frame's bottom: the frame cuts
them under its fade, never an empty strip of pane under the last row.

**At 1440.** One screen. `.grid`, top-aligned: the h2 on `span-5`, a grey paragraph (about 25
words) with one `.link` on `span-6 start-7`. 48px below, the frame takes the rest of the screen as
`.fill` (about 1280 x 550):

```html
<div class="ui app fill" role="img" aria-label="[what the window shows]" data-ui-pause-host>
  <div class="app__pane app__pane--list"> [window fragment] </div>
  <div class="app__pane app__pane--open" data-ui-loop> [the open item's fragment] </div>
</div>
```

`class="ui"` gives the frame the kit's tokens, and tells the checks it is one drawn window. Page
CSS (the whole recipe):

```css
.app.ui { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); margin-top: var(--s-7); background: var(--u-bg); border: 1px solid var(--u-border); border-radius: var(--u-r); box-shadow: var(--u-shadow); }
.app > .app__pane { position: relative; min-width: 0; min-height: 0; overflow: hidden; }
.app > .app__pane + .app__pane { border-left: 1px solid var(--u-line); }
.app > .app__pane > .ui-panel { width: 100%; border: 0; border-radius: 0; box-shadow: none; }
.app > .app__pane::after { content: ""; position: absolute; inset: auto 0 0 0; height: 64px; background: linear-gradient(transparent, var(--u-bg)); pointer-events: none; }
@media (min-width: 1024px) and (max-width: 1279px) { .app.ui { grid-template-columns: minmax(0, 4fr) minmax(0, 8fr); } }
@media (max-width: 1023px) {
  .app.ui { grid-template-columns: minmax(0, 1fr); grid-template-rows: auto minmax(0, 1fr); }
  .app > .app__pane--list { max-height: 252px; }
  .app > .app__pane--list::after { display: none; }
  .app .ui-win__side { display: none; }
  .app .ui-win__body { grid-template-columns: minmax(0, 1fr); }
  .app > .app__pane + .app__pane { border-left: 0; border-top: 1px solid var(--u-line); }
}
@media (max-width: 639px) {
  .app.ui { grid-template-rows: minmax(0, 1fr); }
  .app > .app__pane--list { display: none; }
  .app > .app__pane + .app__pane { border-top: 0; }
}
```

The `window` lays itself out for its pane (rows stacked name over item at 1440, columns on a
tablet). The fragments keep their natural height: the pane cuts them, never their own box. One box:
the frame is the window, the panes are its columns, no panel, card or ground behind it (it sits on
the section's ground; on a `dark-band` the kit's dark surface). A second piece over it (`cursor`,
`notify`) only `.at-over` the open pane's lower-right, never over the list.

**At 1024 to 1279.** The list narrows to 4 columns (its sidebar goes); the open item takes 8.
**At 768 to 1023.** The list on top (its bar, column heads and four whole rows, 252px), the open
item under it to the section's foot. **At 390.** The open item alone, its own header as the chrome.

**Copy.** The h2 names what the window shows ("Every pull request, reviewed in one place"); the
paragraph says the steps in the order the window shows them.

**Motion.** One loop: the open item (`data-ui-loop` on its pane: the Apply pressed, the answer
written); the list holds still. Nothing scrolls inside the window.

**Mistakes.** The open item alone on a lit panel (that is a card, not the product); the list and
the item as two boxes side by side with ground between; a pane that ends in empty white; the kit's
sample rows; a fragment stretched to the pane's height (its own overflow then cuts its text).

## steps

**Job and use.** How the product is used, in order, each step's result shown. Only with three real
steps.

**At 1440.** `.section-head`, then `.grid` with three `article.card.card--row.span-4`:
`span.step-num`, the title (a verb and an object, one line), one or two lines in ink, then the
panel, two boxes deep (336px; a service: a photograph of the step fills it), with one fragment
placed as in the bento's small cards. Not `calendar`, `files`, `doc` or `cursor`. No arrows or lines
between the cards.

**At 1024 to 1279.** Two cards, then the third across the row. **At 768 and 390.** One column.

**Copy.** The heading holds the count. Example, Ledgewick: "Set up Ledgewick in 3 steps"; "Upload
your receipts" / "Drop in PDFs or phone photos."; "Check the matches" / "You confirm the few it is
unsure about."

**Motion.** Tech: the first card loops; the others hold still. Never chained or staggered.

**Mistakes.** Arrows or stair-stepped cards; huge display numerals; panels of different heights.

# Photographs, rooms, services and people

## photo-band

**Job and use.** The page's media section (rhythm `media-band`, product and service, never a place):
one photograph across the screen as the section's layer, a headline on its calm, dark part.

**At 1440.** `section.photo-band.photo-band--bleed` in `main`, one screen: the `img` as the layer,
then `div.photo-band__text` in a `.wrap`: an h2 of at most eight words, one line, an optional
`.link`, on the photograph's calm side (`--left`, or `--light` with dark words on a pale crop). No
scrim, gradient or box. A muted film (tech only) plays with a pause button.

**At 390.** The photograph's phone crop with a calm area, or the words under it on the ground.

**Copy.** Example, Brinwood (standing desks made in Porto): "Built to order in Porto"; "Each desk is
cut, oiled and tested in our workshop before it ships."

**Mistakes.** Two bands on a page; words over the subject or a busy area; the hero's photograph
again.

## photo-pair

**Job and use.** Two photographs side by side: inside and out, a detail and the whole, two cases of
work. A light section between heavier ones.

**At 1440.** The h2 and one line above, then `.grid` with two photographs on `span-6`, 4:5 or 4:3,
one ratio, one light. Nothing under them; what they show is said in the line above.

**At 390.** One column.

**Mistakes.** Two photographs in different light; captions or titles under the pictures; three or
more (use a row of three).

## line-up

**Job and use.** The models or sizes of a product, picture first, each with a price from, so the
buyer can choose (8 of 15 good product sites show the range early).

**At 1440.** `.section-head.section-head--row` (h2 "Three sizes", `.link` "Compare sizes"), then
`.grid` with three `a.tile.span-4` (four `span-3` for four), each a card: the cut-out on `--g-alt`
(`object-fit: contain`, 32px in) or a photograph from one angle at the top, then inside the card's
padding the name in `h3`, "from €1,290" and one facts line ("Top 140 x 70 cm · 65 to 130 cm").

**At 390.** One column, or two-up at 165.

**Visual.** Every model at one scale on one backdrop, or one camera angle; a technical product may
show the client's render per size. No line-up without pictures of every model.

**Mistakes.** Plan cards with checks and a featured badge; a monthly price; mixed angles and scales.

## rooms-list

**Job and use.** Rooms, cabins or studios to rent. On a place the rooms are `sections.md` section 4
(Rooms: tiles, row or side). A service or product with rooms (a co-working space) uses the same
tiles: a 4:3 photograph of the whole room, the name, the facts, the price from with its season,
"Book this room".

**Mistakes.** Rooms as plan cards with checks or badges; a calendar standing in for the photographs;
a price without its season; rooms that alternate sides.

## services-list

**Job and use.** What a clinic, firm or trade does, each service with one line and a price from: a
list beside one photograph of the work, never a grid of icon cards.

**At 1440.** `.grid`, top-aligned: the h2, one line and `ul.rows` on `span-5` (per service
`span.rows__name`, a `<p>` line, `span.rows__value` "from €95"; a `.link` under the list), and the
photograph on `span-6 start-7` (`.frame.frame--photo`, 4:5 or 4:3).

**At 390.** The text and list first, the photograph 48px under it.

**Copy.** Example, Halden Dental: "Check-up and clean" / "Every six months, 40 minutes" / "from
€95".

**Mistakes.** Services as icon cards; prices missing; more than eight rows (link to a page).

## peek-list

**Job and use.** A short list beside one photograph that changes to the row under the pointer, the
focus or a tap: a studio's rooms, a clinic's treatments, a bakery's kinds of bread. Every row needs
its own photograph; with fewer, use services-list.

**At 1440.** `starter.html` `peek-list`: `.grid[data-peek]`, top-aligned: on `span-5` `ul.rows` of
three to six `li[data-peek-to][tabindex="0"]` (the name, one line in ink, the value right), and on
`span-6 start-7` the photograph frame holding one `img.frame__img[data-peek-for]` per row (all but
the first `hidden`, none lazy). system.js swaps the photograph (instant on other kinds; a 200ms
fade on tech) and marks the row in view.

**At 768 and 390.** The list first, the photograph 48px under it; a tap on a row changes it.

**Mistakes.** A row without its own photograph; the same photograph twice; a caption on the
photograph; more than six rows; the list on the right.

## people-row

**Job and use.** The people a client will meet, a portrait each, for a service or a small maker,
only the real team the brief gives.

**At 1440.** `.section-head`, then `.grid` with four `.tile.tile--portrait.span-3` cards: the
portrait (4:5) at the top, then inside the card's padding the name in `h3`, the role and one line
on what they do.

**At 390.** Two-up at 165, the names under in the card.

**Mistakes.** Stock or invented portraits; mixed light and grounds; more than eight people.

# Sections for a kind of content

## integrations-grid

**Job and use.** Which tools and file types the product works with, by their real full-colour icons
(house rule). When the point is what feeds the product, a `fanin-warehouse` or `hub-tools` diagram card
with the real icons on its spokes, inside a feature section. Up to eight tools: four cards. The big
grid only for 9 or more tools the brief lists.

**At 1440.** Four cards: `.section-head`, then four `article.card.card--row.span-6`, each a title
naming the tool ("Syncs with Notion and Dropbox"), two lines, and the panel (336px) holding one
fragment: `integrations` with its apps swapped for the client's real tools, `.at-rise.fit` low
(`--fit-max: 380px`, `--ay` and `--ay-sm` `calc(100% - 180px)`); `files` with the real files and
icons, `.at-corner.wide` (`--w: 680px`); or a hub diagram (`hub-tools`) with the product at the
centre and its real tools on the spokes. Big grid: `.frame` on `span-12` (48px padding) with eight
72px tiles across (24px column gap, 32px row gap), each a real icon over the tool's name in
`.t-label`; no "See all integrations" link (a one-page site has nowhere to send it).

**At 390.** Cards in one column; tiles four across at 64px.

**Visual.** Icons from `icons.mjs fetch` in their own colours (`icons.md`), never drawn or tinted.

**Motion.** Tech: the first card loops (or the hub pulses); the rest hold still.

**Mistakes.** Drawn or recoloured logos; tools the product does not support; more than five tiles
in a card.

## calendar-frame

**Job and use.** The dates the product deals with, on the client's real month, beside what they are
for. Tech only, with real dates.

**At 1440.** As split-text-left, with the frame one height at every width so the month shows whole
(page CSS `#dates .frame--split { --ratio: 0px; min-height: 600px }`), holding the pasted `calendar`
alone, `.at-rise.fit.to-edge` 48px down (`--fit-max: 440px; --ax: max(48px, 50% - 220px)`). No
second piece.

**At 390.** Text first; the frame 600 tall, the calendar in its phone layout.

**Copy.** A heading that says what the dates are for. Example, Keelday (booking for sailing
schools): "Plan the season's courses".

**Visual.** Set the month label, `data-month`, the leading `.is-out` days for the weekday of the 1st,
`data-d` on every real day, `data-start`/`data-end`, one `is-mark`, the three `[data-ev]` rows, as
the calendar's `meta.json` says; `is-today` only in the current month.

**Mistakes.** The wrong weekday for the 1st; the kit's sample month; the calendar scaled or cut
through its rows.

## timeline-rail

**Job and use.** Four dated moments in order on one line, each with a small panel: releases, a
history. Software and product only, never a place.

**At 1440.** `.section-head--row` with the h2 and a `.link`. 48px below, `ol.grid.rail`: four
`li.span-3`, each with a `.panel` on top (200px), then the rail row (page CSS: a 1px line to the
next column, an 8px still dot, the newest in `--accent`), the date in `.t-label`, the title in
`.t-card`, one sentence of at most 10 words.

**At 390.** One column; the rail vertical.

**Motion.** At most one loop, in the newest panel (tech). Nothing on the rail moves.

**Mistakes.** Points zig-zagging; a pulsing dot; panels of different heights.

## menu-in-type

**Job and use.** A menu or price list in readable type beside a photograph. On a place it is
`sections.md` section 4 (Menu or prices: open groups, no tabs). A product sold by weight or size
reads the same way ("250 g · €14").

**Mistakes.** Ragged prices or two currency formats; each dish in its own card; the menu only as a
PDF or an image; tabs or an accordion.

## visit-map

**Job and use.** Where the place is, when it opens and how to get there, with the practical facts
(parking, dogs, step-free access, check-in) as two to six rows. Showrooms, studios, services with a
door; on a place the visit section is `sections.md` section 4 (Visit) and this recipe gives only
the map.

**At 1440.** The page's split: the text (h2, the `<address>` as street and district (no street in the brief: the district, `copy.md`), the hours as
`dl.hours` with `data-tz`, the phone and email only when the brief gives them, the main action and
Get directions); on the right the street map: `fx-map` baked from OpenStreetMap
(`effects-creative.md`) only for a street the brief gives, the pin on the street line, still on
other kinds; otherwise a photograph of the shopfront.

**At 390.** Text first; the map or photograph 342 wide.

**Copy.** Example, Fenn (a pottery studio): "Visit the studio"; "Book a class", "Get directions".

**Mistakes.** A map embed or screenshot; a map of a street the brief does not give; a moving route
on an other page; the credit on the map (it joins the footer line); today from the visitor's clock.

## booking-form

**Job and use.** The one task of a place or service page: send a booking request. When the client
books through a system, its link is the button instead.

**At 1440.** The page's split: text on the left (h2 "Book a room", what happens next, the phone
and email only when the brief gives them); on the right the form on `--g-alt` (48px padding, never
over a photograph, texture or glass), beside or under a photograph of the room or counter on a
place (`sections.md`, Booking): dates, guests, name, email, at most six fields, the `.btn-row` with
the primary. `method="post"`, `action` the client's booking address. Text fields, not
`type="date"`, on a page not in English.

**At 390.** Text first, the form full width, one field a row.

**Copy.** Labels say what goes in ("Arrival", "Guests"); the button is the main action word for
word; a line says when the reply comes ("We reply within a day").

**Mistakes.** A form that sends nowhere; more than six fields; a fake success message; a modal.

## client-slots

**Job and use.** The client's own trailer, key art, in-engine screenshots, CAD renders, exploded
model or motion video, when the brief says the client has them (`sections.md` section 1): each
gets a frame that reads finished now and takes the client's file later with one line changed. Tech
pages (software, gaming, hardware); a product page's CAD frame too. The stand-in is always from the
kit (a product-render still or scene of the client's own spec), never stock, a drawing or an empty
or grey frame; nothing on the page says it is a stand-in.

**The comment.** Every slot opens with one comment the client's team can search for:
`<!-- CLIENT FILE trailer: assets/client/trailer.mp4 (1920x1080, H.264, the 60 s trailer) and
assets/client/trailer.jpg (its poster); stand-in poster: <spec>-<view>.webp -->`. The report lists
each slot: its name, file, ratio and stand-in.

**Trailer or motion video frame.** Its own section after the hero (or the world's section), the
h2 above it, the frame across the wrap: `figure.frame.frame--photo.fit-screen` (page CSS `--ratio: 56.25%`; at 16:9 the frame across
the wrap is about 700px tall at 1440x900, taller than one screen with its heading, so `fit-screen` (`layout.css`: the height one
screen leaves under the heading, 720px at most, `auto` under 1024px so a tablet and a phone keep 16:9) or a `max-height` on the
frame keeps the section one screen; the contained poster then sits letterboxed on the dark ground)
holding `<video class="frame__img" playsinline preload="none" poster="<the stand-in still>">`, the
poster a kit still that already reads as the film's first frame (a game: the world's widest view;
hardware: the use scene, the arm at the bench mid-move). The play control is real or absent, never
dead. With the file: `controls`, `preload="metadata"`, `<source src="assets/client/trailer.mp4"
type="video/mp4">`, the client's poster. Without it: no `<source>` and no `controls` (a missing
file or a dead control bar is a broken frame); the stand-in still is transparent, so the video
also takes `.slot__poster` and page CSS `.frame > .frame__img.slot__poster { object-fit: contain }`
(the kit's `cover` crops the still to a fragment of the product), the frame the world's or the
page's dark ground, its stills made on that ground (`make-posters.mjs --grounds dark`: a light-ground still keeps a pale floor patch on dark); the play control is `<a
class="ly-play" href="<the trailer's page the brief gives: the store page>"
aria-label="Watch the trailer">` with its `.ly-play__disc`: the `.frame` is a centring flex box, but system.css's rule `.frame > :not(canvas, .stage, .loop-pause, .frame__fx, .frame__img, [data-print], [data-scene], .print3d)` makes the
control `position: relative`, so `.ly-play`'s `left` and `bottom` (`--s-6` each) move the disc 32px right and up of dead centre, not
to a corner; page CSS `.frame > .ly-play { left: auto; bottom: auto }` centres it; with no such page,
no control: the poster stands as the section's still until the file lands. With its file, a
motion video on tech may play muted and looped instead (`autoplay muted loop`), with its pause
button (`motion.md`), the poster alone under reduced motion and on a phone; never with sound.

**Screenshot strip.** The world shown as the game is played: three to five frames framed like
captures, 16:9, the same size (a `trio` or a row of four on the `.wrap`; a phone: one column), square
corners or the page radius, no device chrome, no shadow, no caption. With the files: each
`<img class="frame__img">` in `figure.frame.frame--photo`. Without them: each frame holds one job
scene of the world spec (`sections.md`, Gaming), `data-product-place="stage"`,
the frame itself the `[data-product]` element (`div.frame.slot`, page CSS `.frame.slot[data-product]
{ --ratio: 56.25%; background: <the world's water, fog or night colour> }`: `layout.css` clears a
`.frame[data-product]`'s ground, so a weaker selector leaves the render on white), the scene's props spread so it spans
the frame, a still, no two the same scene. Never `data-product-fill` over 1 (in testing the
frame drew empty). As the "what you do" cards it is three to five open cards, each a
verb over its capture.

**CAD or render frame.** The client's CAD render of the whole product: the product section's
split frame (`frame--split`) or a `bleed`, the render on a light flat ground, square corners. Its
stand-in is the product-render view no other section uses (`front` or `top`), so it counts as one of
the object's three sections. **Exploded frame:** the parts section's picture, the client's exploded
model, else the spec's `exploded` scene (`sections.md`, Product, section 4).

**Key art.** The hero's stage (the `product` stage, or the `film` hero's poster) and the world's
band: the stand-in render there, the comment naming `assets/client/key-art.jpg`.

**Mistakes.** A slot the brief names and the page leaves out; an empty, grey or black frame; a
play button that does nothing; a `<source>` pointing at a file that is not there; a caption saying
the file is coming; the hero object as the stand-in in every slot.

# Price and questions

## pricing-three

**Job and use.** Software: three plans side by side, the middle one recommended, an optional
monthly or yearly switch.

**At 1440.** `.section-head` on the left line: "Pricing", one grey line, and the switch (two
`role=tab` buttons). 48px below, three `.card.card--plan.span-4`, the middle `.is-featured` with a
"Most popular" `.badge`. Each: the name, who it is for, the `.price` with "/month", a billing line
in both modes, a full-width button (`.btn--primary` only in the middle), 5 to 7 lines of what it
includes. From 1024 each card is a subgrid of its rows so buttons and lines align. Every price
carries `data-monthly` and `data-yearly`.

**At 390.** One column in plan order.

**Copy.** Example, Rotaro: "Priced per restaurant. Try any plan free for 14 days."; Team: "For
restaurants with 15 to 50 staff", €59/month.

**Visual and motion.** No ground; still. On tech the featured plan's border may be lit
(`fx-pricing`, or `data-glow="edge-glow"`: one light round its edge on hover or focus) when that is
the page's one effect.

**Mistakes.** Cards that change height on the switch; a saving that does not match the prices; plans
for something that is no subscription (a product, a place).

## pricing-two

**Job and use.** A free and a paid plan, or two fixed prices for a service; what both include said
once.

**At 1440.** `.grid`: on `span-4` the h2 "Pricing", a grey line, what every plan includes and a
`.link`; on `span-4 start-5` and `span-4 start-9` two `.card.card--plan` (name, who for, price,
button, 5 to 7 lines), the recommended one `.is-featured`.

**At 390.** One column.

**Mistakes.** Buttons at different heights; the every-plan list repeated in the cards.

## comparison-table

**Job and use.** Plans or models, or the product against how the job is done today, row by row.

**At 1440.** `.section-head`, then rows of `.grid` with `role=table` and its roles: the feature on
`span-4`; two options on `span-4 start-5` and `span-4 start-9`, three on `span-2`. A header row on
`--g-main` with each option's name, price and a button (`.btn--primary` only for the recommended).
Group headings in `.t-label`; 48px rows, each closed by a 1px rule; a check with an `.sr-only`
"Included", a grey dash ("Not included") or a short value. Nothing sticky.

**At 390.** Each option as its own block of rows; never sideways scroll.

**Mistakes.** Sideways scroll on the phone; columns off the grid; a sticky header.

## faq

**Job and use.** The buyer's last questions (price, data, cancelling, formats), every answer open.
Merged into the section above under 495px.

**At 1440.** The page's split: on the left the h2 "Questions", a grey line and a `.link` to
`#contact` (a `mailto:` or `tel:` only with an address or number the brief gives); on the right
`.faq` with 5 to 8 `.faq__item`s (the question in `h3`, the answer under it, each closed by a 1px
rule). No accordion: answers are open on load.

**At 390.** One column.

**Copy.** Questions in the buyer's words, at most 60 characters; answers under 50 words, starting
with the answer. Example, Ferrow: "Can I cancel at any time?" "Yes. Cancel in Settings and you are
not billed again."

**Mistakes.** Questions the company wants asked; answers that dodge; closed answers.

# Closes

The close is row 1 of `footer.closing` (`layout-v4.md`), on the footer's own ground, never a band of
its own. It asks for the main action once more, word for word.

## close-type

**Job and use.** One big line and one big primary button. Any kind; no picture: the button is the
picture.

**At 1440.** `.closing__cta.close--type`: the h2 (at most eight words, on the left line), an optional
`.t-small.muted` line (the trial terms, the opening hours), then `a.btn.btn--primary.btn--xl`
across the `.wrap` (88px tall, its label in the display face at 32px) on software, 640 wide and 72
tall on product and service (a slab that wide reads blunt on a clinic).

**At 390.** The button full width, 48px tall with an 18px label.

**Copy.** Example, Rotaro: "Plan next week's rota in ten minutes" / "Start free trial" / "Free for
14 days. No card needed."

**Mistakes.** A second button; the big button anywhere else on the page; a ground behind it.

## close-photo

**Job and use.** The close for a place, a product or a service: the main action beside a photograph
of the place or the product in use. Always the close on a place.

**At 1440.** `.closing__cta.close--photo`: a head row (the h2 of at most eight words, one line such
as "Open today 7:30 to 16:00", the main action), then the client's photograph down to the links,
from line to line, never used above, never with words on it. A place: the 1:1 photograph on
`span-5` and the words beside it (`sections.md`, Close).

**At 390.** The words and the full-width button, then the photograph.

**Copy.** Example, Fenn: "Book a Saturday wheel class"; "Three hours, €65, clay and firing
included."; "Book a class".

**Mistakes.** The hero's photograph again; words over the photograph; a band out to the viewport.

## close-word

**Job and use.** The h2 and the button, then the client's name set across the `.wrap` in the display
face. Software, product and service (never on a place's `colour-band`).

**At 1440.** `.closing__cta.close--word`: the h2 and the button on one head row, then the name as
one line from line to line (hand-set size per breakpoint, never scaled by transform).

**At 390.** The head stacked; the name across 342.

**Mistakes.** The name larger than the page can hold at 1024; the name repeated in a footer
wordmark.

# Footers

Row 2 of `footer.closing`: the directory on one ground and the legal row (`system.md`).

## footer-columns

**Job and use.** The quiet footer on the base ground: the company in one plain line, the sitemap,
the legal row. Software, products, services.

**At 1440.** As `starter.html`: the company block on `span-4` (the logo, then `p.footer__lede`, one
line of at most eight words in the display face at 28px), four `.footer__col.span-2` named and
ordered as the nav, each link a section of the page and Contact `#contact`; the newsletter field
(once, "Subscribe") when the page has one; then `.footer__legal`: the brand and year, Privacy, Terms
(an Imprint only when the brief gives the company's own details), the empty `.socials`, the credits
line last.

**At 390.** Columns two-up, the legal row stacked.

**Mistakes.** Columns that differ from the nav; links to pages the build does not have; drawn or
coloured social icons; effects in the footer.

## footer-dark

**Job and use.** Figma's and x.ai's footer: a dark ground, the name set large, the link columns.
Software and product (the one dark band at the end).

**At 1440.** `footer.closing.footer--dark.ground-inverse`: `.grid` with the company block on
`span-4` (the mark and the name at 48px in the display face), four `.footer__col.span-2`, the legal
row. On a dark page system.css keeps it a step darker than the page with a hairline on top.

**At 390.** The name at 30px, columns two-up.

**Mistakes.** A second dark section right above it.

## footer-visit

**Job and use.** A place's or a local firm's footer: where it is, set large, with the way there
and the hours, so a visitor needs nothing else.

**At 1440.** `footer.closing.footer--visit` as `starter.html` (`links-visit`): on `span-7`
`address.footer__address` (street and district on two lines, the district alone when the brief names no street, 32/40 on a place, 48px elsewhere, in the
display face), one line on the way there (the stop, minutes on foot) and `a.link` "Get directions"
(the OpenStreetMap search, `copy.md`); on `span-4 start-9` "Opening hours" over `dl.hours` with
`data-tz` (system.js marks today). Then the nav row (the logo, the nav's words, Contact), the legal
row with the credits line last; then on a place the name set wide across the `.wrap` in the display
face at 400, except on `colour-band`. No button.

**At 390.** The address at 24 to 30px, the hours under it, the nav row wrapping.

**Mistakes.** Hours that differ from the visit section; today from the visitor's clock; a map in
the footer; a printed email or phone the brief does not give.

## footer-statement

**Job and use.** The close and the footer as one designed slab on the page's lit ground (sand, sky,
sage or painting): one big line, one full-width button, then the columns (Figma's close and footer).
Tech only.

**At 1440.** `footer.closing.footer--statement`: system.css insets it 8px from the window's sides
and bottom with `--r-lg` corners. The close as close-type's, 96px to the columns, the legal row.

**At 390.** Full bleed, square corners.

**Mistakes.** A second big button; an effect on it.

# Page plans

Five worked deals, one per kind (a game apart from software). Yours comes from the dealers, so the same kind looks different
every time. Neighbours never share a layout, splits keep one side, a calm section follows at most
two visual ones, a card layout shows at most twice.

## Software

*Fernbill: invoicing for agencies of 2 to 20 people.* Dealt: hero `split`, `nav-mega`,
`footer-dark`, close `close-type`, rhythm `dark-band`, buttons `pill`, mark `ring`; effect
`painterly-landscape` in the hero frame, card ground `grain-gradient`; one moment,
`word-highlight` (one statement section of its own).

Order: hero (the open invoice as a `doc`, `notify` "Invoice 2041 paid" over its edge),
app-frame (the invoice list in `window` beside the open invoice's thread with its client as `chat`),
features-2x2 (the card ground; `notify` payments matched, `toggles` reminder rules, a lanes
diagram for one invoice split to three ledgers, `chat` a client's question), the statement with
`word-highlight` (its own one-screen section), split-text-left (`files` with real receipts, the lit
ground plain), tabs-tour on the dark band, integrations (a `fanin-warehouse` diagram card with the real icons on its spokes, beside its text),
pricing-three, faq, footer.closing. No logo row: the brief names no
customers; no quote either.

## Product

*Brinwood: solid-oak standing desks, built to order in Porto.* Dealt: hero `photo`, `nav-cards`,
`footer-columns`, close `close-photo`, rhythm `media-band`, buttons `arrow`, mark `stack`.

Order: hero (the desk in a real room), product-statement (the cut-out and three facts: load 120 kg,
height 65 to 130 cm, delivery in 3 weeks), line-up (three sizes from €1,290), split-text-left (the
oak top: a photograph of the grain), photo-band ("Built to order in Porto"), split-text-left again
(the handset with its presets: a photograph, since a product never shows UI it does not have),
specs (`rows--spec` beside a photograph of the frame), proof (a review the brief gives, merged),
faq (four questions), footer.closing. Flat grounds, no effect, no moment.

**With no photographs yet** (*Pellum, a desk lamp*): the lamp is rendered, never hidden. The hero
(`deal.mjs --type product --has object`: `product` or `split`) holds its product render whole on
the stage, switched on; product-statement shows the dial close up with three facts (parts);
what it does as a split (the desk scene: the warm pool of light on the books and the mug across
the frame, the lamp cut by its edge; use); how it is used as three steps; specs as `rows--spec` with the real icons of the component brands the brief names;
ordering as a live order card (finish swatches that recolour the render, delivery, the price):
the lamp whole twice, never in every section;
faq; footer.closing. Flat grounds, no effect, no drawing, no line about missing photographs; the
report lists the shots to take.

## Gaming

*Kelpmoor: a co-op sailing game on a drowned coast, coming to Steam.* Dealt: hero `film` (the
trailer the brief supplies), `nav-centre`, `footer-dark`, close `close-word`, rhythm `media-band`,
buttons `solid`, mark `wordmark`; effect none (the trailer is the hero's motion); one moment,
`letters-assemble` (a statement of its own).

Order: hero (the trailer's poster in the cinema frame, plays on a click; h1 "Kelpmoor, a co-op
sailing game"; "For 1 to 4 players. Coming to Steam in spring."; "Add to Steam wishlist"), the
world (two in-engine shots as a photo-pair, one grade), the statement with `letters-assemble`, what
you do (three open cards, one verb each with its in-engine shot: sail the drowned coast, salvage
the sunken towns, rebuild the harbour), the world again as the media band (key art full bleed, the
h2 on its calm sky), platforms and editions (the real Steam, PlayStation and Epic Games marks,
`icons.mjs apps --tag gaming`; Xbox and Nintendo are in no permitted set: name the console in
type, never a drawn mark; prices from), faq, footer.closing. No UI fragment, dashboard or widget
anywhere.

**With no art files** (named but not supplied, or none): the key art is rendered, never an effect
in its place. Two product-render specs in the game's palette (`effects-objects.md`, Product
renders): the salvage sloop (hull and deck as rounded boxes and panels, mast and boom as tubes,
rigging as paths, a furled sail as a tube, two `light` lanterns; about 40 parts) and the world
scene (the drowned pier and the sunken town's roofs: posts as cylinders, planks as beams, crates
as boxes, a crane's rope as a path, the sloop small at the pier, under 90 parts; one scene per
job: a hull cut open under a `light` lantern, a crate swung up on the crane, the harbour rebuilt). Dealt `deal.mjs --type software --kind gaming --has
object`: hero `product`, the effect `aurora-curtains` dealt for the hero slot (dark, read as a
dusk sky over water) as the stage's ground behind the turning sloop (`data-product-mode="live"`), h1 "Kelpmoor, a co-op sailing
game", "Coming to Steam in spring." and "Add to Steam wishlist" in the head row. Then the
trailer frame (client-slots: the pier scene's widest still as the poster, the play control to
the trailer on the store page the brief gives); the world: the pier scene from above (its `top`
view, the map of the coast), full bleed on the dark band, the h2 above it; what you do: the
screenshot strip as three open cards, each a verb over one job scene of the world, 16:9, filled
to the edges on the world's water (client-slots); a section holding the dealt moment; platforms
with the real store icons and the sloop's second whole view; faq; footer.closing. The sloop whole
twice; the world carries the rest. One render turns, the rest are stills; nothing says "render";
each slot names the client's file in its comment. The
report names the art to replace.

## Place

*Fenn: a pottery studio and shop on Karl-Heine-Straße, Leipzig-Plagwitz.* Dealt: `nav-split`,
`footer-visit`, rhythm `surface-pairs`, buttons `block`, mark `arc`, the offer `tall-small`, the place
`trio`, the type moment `address`, rooms none.

Order: the place hero (the workshop in morning light; "Pottery classes in Leipzig-Plagwitz";
"Wheel classes on Saturdays, open studio Tuesday to Sunday from 10."; "Book a class"), visit
(screen 2: "Karl-Heine-Straße, Plagwitz" set large across the `.wrap`, linked to the map; the week's
hours; step-free entrance; the shopfront 4:3), the offer on the surface band (classes and prices as
two open groups beside `tall-small`: a class at the wheel tall, a glazed bowl small, each linking to
its class), the place (`trio`: the workshop, a shelf of drying pots, a hand trimming a foot ring,
tops on one line), booking (a photograph of the class room beside the form), footer.closing
(`footer-visit`, the name capped at 12vw, the one credits line, `data-tz="Europe/Berlin"`).
Fourteen photographs, all the studio's own; no effect, no moment; every linked photograph zooms
1.03 under the pointer.

## Service

*Halden Dental: a dental clinic in central Malmö.* Dealt: hero `split`, `nav-mega`,
`footer-visit`, close `close-photo`, rhythm `surface-pairs`, buttons `tonal`, mark `dots`.

Order: hero (a treatment room, 4:5), services-list (six treatments from €95 beside a photograph of
the reception), steps (book online, the check-up, the plan: a photograph each), people-row (the four
dentists the brief names), pricing-two (Check-up and Check-up with cleaning as fixed prices), faq
(merged with a patient's quote the brief gives), booking-form with the address and hours,
footer.closing. Flat grounds, no effect.



---

## `references/sections.md`

# Sections

A page is built from its kind's plan; a deal changes the parts a template would fix. Every id has a
recipe in `sections-library.md`. The kind and what it may carry: `SKILL.md` sections 1 to 3 and
`effects-usage.md`. Heights and edges: `layout-v4.md`.

## 1. Plan in screens

Write the plan before building: line 1 the kind, line 2 the deal, then one line per section: its
id, its one idea, its picture, its screens (1 or 2, from the content height: `layout-v4.md`
section 2) and, on tech, the section that holds the effect, the scene or a moment.

- **Every section shows the real thing:** a photograph, a portrait, real icons, the client's UI, a
  diagram card or (tech only) the effect. A section without a picture is allowed only for a price
  list, an FAQ, a specs table, a booking form or a dealt statement moment's own section, once each,
  and two picture-less sections are never neighbours (the short page's statement hero and its one
  section are the one exception, section 4). A quote needs a face or merges into the section above. The picture takes a real share:
  half a tile or more, 50/50 in a split, a whole screen as a layer. The close is its own picture (a
  photograph, the big button or the name set wide).
- **One object never carries the page** (in testing: a robot arm in six sections and a game's
  salvage rig in six, each "one object six times", both capped at 4 to 4.5). The object shown whole
  (the product, its photograph or render, a game's hero object) leads the hero and **at most two
  more sections**; every other picture section is carried by another kind of visual the brief
  supports, from its row below, no kind more than twice. A new angle, a recolour, a crop of the
  whole, or the object on its floor with one prop beside it, is the object again; a use scene counts
  as use only when its setting fills the frame (a `desk` as the bench across the frame, trays,
  parcels and sheets on it, half the picture or more; the object one thing among them). The check counts a declared scene as use, so whether one prop makes it the object again is the builder's call. Write each plan line's kind; three object
  lines at most.

  | Kind | the object whole: hero + 2 | carries the other sections |
  |---|---|---|
  | Software | the `app-frame` | UI fragments of its subject on cards, a diagram card, real tool icons, a type moment, a named quote with its face, the effect or scene |
  | Gaming | the hero object (ship, rig, mech) or the client's key art | the world (a scene of the world's own objects, the hero object small or absent; its `top` view as a map), the crew at work (the client's screenshots, else one scene a job), the trailer frame, the screenshot strip, a type moment, the real platform marks |
  | Tech hardware | the product (photograph, CAD render or its render) | its use (the arm at a bench among trays and parts, the device in its place), an exploded or parts view, the motion video frame, a diagram card held still, a type moment (one figure set large), a context photograph of the trade (a workshop, a lab) |
  | Product | the product (photograph or render) | its use (loaded, carried, at home), people with it, close-ups of its parts, a diagram card held still, a type moment, a context photograph of where it lives |

- **The client's own assets get designed slots.** When the brief says the client has a trailer,
  key art, in-engine screenshots, CAD renders, an exploded model or a motion video, each gets a slot
  that reads finished now: the frame at the file's final ratio, holding a stand-in from the kit
  (a still of the world or the product in use), named in a comment for the client's file, never an
  empty, grey or broken frame and never a line saying the file is missing. The slots
  (`sections-library.md`, client-slots): the **trailer or motion video frame** (a real `<video>`
  with a kit poster, and a play control only when there is a page or file to play), the **screenshot strip** (three to five frames of the
  world composed from the kit, framed like captures), the **CAD or render frame**, the **exploded
  frame**; key art fills the hero's stage. The report lists every slot, its file and its stand-in.
- **One idea per section,** one h2, one action at most besides the main one (a pair only in the
  hero, or where a product needs "compare" beside "buy"). A two-screen section holds one list, table
  or form, or one idea in two groups, never two ideas.
- **The main action** reads the same, word for word, in the nav, the hero, the close (or the
  booking) and the phone bar, and nowhere else as a filled button (a place whose action is Get
  directions keeps it out of the nav, section 4).
- **Merge short blocks:** a quote, logo row, stat row or FAQ that alone would hold under 495px (464
  at 390) goes into the section above as its last element, 64 to 96px under its content, with no
  heading or ground of its own. An FAQ that reaches 495px with its answers open is its own section.
- **Repeats:** a card layout (2x2, bento, three cards, split card, open tiles) at most twice a page;
  neighbours never share a layout; on software, product and service a calmer section (quote, prices,
  FAQ) after at most two visual ones, and the back third of the page calm before the close. Repeat
  the section scaffold (head, padding, ground logic) so it is learned once.
- **Proof as small exact objects,** only from the brief: a named quote with a face, a footnoted
  figure, press lines, a rating line, real customer logos with permission. No row of big stat
  numbers, no filler stat strips, no check-icon lists, no customer-logo wall.
- **Two boxes deep at most:** a card and its picture panel, or a panel and its UI. A card whose
  panel holds UI drops its box (`.card--open`) or runs the panel flush (`.panel--flush`).
- **One page, real links:** every nav word, button and footer link goes to an `#id` on the page, the
  logo to `#top`. The main action goes where it is done: the booking form's or the order section's
  id, `#visit` (the visit block) for Get directions, or, when the page has no form or booking system,
  a `mailto:` on `.example` (`copy.md`). Never `#contact` from outside the footer: `footer.closing`
  carries that id, and the checker WARNs a link that lands in the footer. Privacy, Terms and
  Imprint go to small pages you write (Imprint only when the brief gives the company's own details),
  or are left out. Never `/contact`, `/[page]` or a bare `#`.
- **At 390** the page keeps the desktop's grounds, photographs and order, each photograph after
  its text.
- **At 768 and 820** (the judges' tablet, held upright) plan the screens again: each section's
  stacked content within its screens (832px a screen at 768x1024), else two screens there or less
  that stacks; the first screen ends on a whole picture or a clear bleed (`layout-v4.md` sections 2
  and 3). Write the tablet count on the plan line when it differs ("2 at 768").

## 2. The deal

Deal the parts a template fixes from your kind's lists, never by taste:

```bash
node -e "for(const l of process.argv.slice(1)){const o=l.split('|');console.log(o[Math.floor(Math.random()*o.length)])}" "<nav>" "<footer>" "<close>" "<rhythm>" "<buttons>" "wordmark|initial|arc|ring|stack|dots"
```

The hero comes from `assets/layout/deal.mjs` and the pairing from `start.mjs` (`layout-v4.md`),
never from this line; a place takes the place hero. Write the results on plan line 2 and in the
comment at the top of `<body>`, and build exactly those. Deal one part again only when its recipe's
"use" does not fit. With no photograph to show, these dealt parts do not fit, and each is dealt
again from its own list without them, never drawn: `nav-cards` (and any nav panel of photograph
cards) to `nav-split` with no panel, or `nav-centre`; `close-photo` to the head row of `close-word`
without the name (the h2 and one line on the left, the main button on the right, both on the
`.wrap` lines); `media-band` to `space` (a game without art keeps it: its world render is the layer); a place's hero to the `statement` hero on `.ground-brand`.
Write the change and its reason on plan line 2.

- **Nav** (one fixed, opaque bar on the `.wrap`; `system.md`): `nav-mega` (link columns and one
  picture card in the panel), `nav-cards` (three or four picture cards), `nav-centre` (the words in
  the middle), `nav-split` (the words left, the name in the middle). `nav--tone` puts the bar on the
  inverse ground (tech only).
- **Footer** (`footer.closing` row 2): `footer-columns`, `footer-dark`, `footer-statement` (the lit
  ground, tech only), `footer-visit` (a place or a service with a door).
- **Close** (`footer.closing` row 1): `close-type` (the h2, a line, the big button across the
  `.wrap`), `close-photo` (the head row, then the client's photograph down to the links),
  `close-word` (the h2 and the button, then the name set across the `.wrap`).
- **Rhythm:** `dark-band` (one `.ground-inverse` section at the page's middle or later, holding the
  strongest visual), `media-band` (one full-width photograph layer section mid-page, never on a
  place), `surface-pairs` (one `.ground-surface` band of one or two sections), `space` (one ground,
  sections parted by space only), `brand-band` (product: one section in the brand's own colour,
  `.ground-brand`, in the second half). No hairline rhythm.
- **Buttons** on `<html data-buttons>`: `solid`, `pill`, `tonal`, `arrow`, `block`.
- **Mark** beside the name in the nav and footer (`system.md`); a client's own logo replaces it.

## 3. The plans

Optional parts in brackets; each list is the order on the page. Tell it as a story: say what it
does, show it, prove it, let people explore. Tabs only on software, click only.

**Software** (and AI, developer tools, fintech). nav, hero, [logo-row docked in the hero],
**app-frame** (the product big: its list beside the open item in one app window across the
`.wrap`, as section 2 or 3; `sections-library.md`), two or three feature sections in different layouts (features-2x2, bento, split-text-left,
tabs-tour, chapter, steps), [integrations as a `fanin-warehouse` or `hub-tools` diagram card;
integrations-grid only for 9 or more tools the brief lists],
[quote-stat (a quote the brief gives) or customer-proof-row (customers the brief names); with
neither, the calm section is pricing or the FAQ], [pricing-three, pricing-two or
comparison-table], faq, footer.closing. Pictures:
the client's screens as live HTML, else fragments from `assets/ui` rewritten to its names, each
showing the product's own subject (`cards.md`, The fragment on it: a code-review tool shows a red
and green diff with its Accept action); diagram cards for how things connect; real icons for the
tools it works with. The effect, moments and scene as `effects-usage.md` deals them.
Nav `nav-mega|nav-cards|nav-centre` · footer `footer-dark|footer-statement|footer-columns` · close
`close-type|close-word` · rhythm `dark-band|surface-pairs|space` · buttons `solid|pill|tonal|arrow`.
Never: stock people at screens; an object render in place of the product; a page whose product
shows only as small fragments centred on coloured panels (in testing: about 3.5 points under Linear).

**Gaming** (a game, a studio launching its game; page type software, site-kind gaming). nav, hero
(the game, named), [the trailer frame], the world (one or two sections, full bleed), what you do
(the screenshot strip as three to five open cards, one verb each, sail, salvage, rebuild, each
with its capture), [a system of
the game as a diagram card: matchmaking, saves, stores], platforms and editions (the real store and
platform icons, prices from), [press lines or a quote the brief gives], [faq], footer.closing with
the main action (Add to Steam wishlist, Pre-order). In testing, a game page that never named the game
and showed an abstract effect for key art lost 3.5 to 5.5 to one with a launch date, a scene of the
game's world, feature cards and real platform icons. So:
- **The hero names the game:** the h1 is its name and genre ("Northline, a co-op survival game",
  40 characters at most on the `product` stage), or its wordmark (the client's logo file) over an
  h1 naming the genre. The lead or a line under it carries the launch date or status the brief
  gives ("Out 12 March on Steam", "Early access now"); with no date, the status ("Coming to PC"),
  never an invented date.
- **Key art in the hero and the world sections, full bleed:** the client's trailer (a film hero),
  key art and in-engine shots, one grade, as layers or on the column lines. Deal the hero with
  `deal.mjs --type software --kind gaming --has film,photo` when the art is supplied.
- **The world and the crew carry the page, not the hero object** (section 1, One object): the
  hero object whole in the hero and two more sections at most; the world, the crew at their jobs,
  the trailer frame and the screenshot strip carry the rest. Art the brief names gets its slot
  either way (section 1, client slots): a trailer frame, the screenshot strip, key art on the
  stage.
- **No art files** (the brief names art it does not supply, or none): the key art is **rendered**,
  never replaced by an effect. Write a product-render spec (`effects-objects.md`, Product renders)
  of the game's hero object (its ship, crane barge, mech, car) or a scene of its world composed from
  its own objects on one floor (the barge at the quay with its crates, lanterns and cables; under 90
  parts), in the game's palette, `light` material for its fires, lamps and screens; make its
  posters. Write two: the hero object and the world (its quay, wrecks with hulls cut open, cranes,
  crates, lanterns, the hero object small in it or left out), the world with one scene per job
  (`"scenes"`: the torch's `light` in a cut hull, the winch over a crate stack, the helm lanterns
  by night). Deal `deal.mjs --type software --kind gaming --has object` (the `product` stage): the
  render whole on the stage, turning slowly (`data-product-mode="live"`: the page's one live render;
  every other frame a still). The one effect (`effects.mjs pick --page gaming
  --palette dark --slots hero --exclude ruled-grounds,grid-pulse,contour-lines,dot-terrain,dotted-globe,ridgeline,bayer-dither,halftone-screen,ascii-shade,line-engraving,duotone-grade`,
  again until it reads as water, fog, embers or light, or the product hero's `spotlight-cone`,
  `edge-glow`) may sit behind it as the stage's ground, the
  render drawn over it (every placement is transparent over its frame's ground), never instead of it. The world
  section: the world spec's widest view (or its `top` view as the map), `data-product-place="stage"` in a
  full-bleed `media-band` or `dark-band` frame, the h2 above the render, never on it. The feature
  cards are the screenshot strip: each card one job scene of the world spec, 16:9, its props
  spread so the scene spans the frame, on the world's own ground, never the hero object alone
  again (a `data-product-fill` over 1 drew an empty frame in testing: widen the scene instead). The trailer frame's poster is the world's widest still. One
  render turns; the rest are stills. The helper cannot model characters, faces, creatures, cloth
  or glass: compose the world's machines, buildings and props, never a character. The report
  names the art to replace.
- **Platforms:** the real Steam, PlayStation and Epic Games marks (`icons.mjs apps --tag gaming`);
  Xbox and Nintendo named in type, never a drawn mark.
Nav `nav-mega|nav-centre|nav-cards` · footer `footer-dark|footer-statement` · close
`close-word|close-type` · rhythm `dark-band|media-band|space` · buttons `solid|pill|block`.
Never: a hero that never names the game; an abstract effect, pattern or `statement` hero in place
of key art; UI fragments from `assets/ui` (no UI kit on gaming), a dashboard, SaaS widgets on
panels; a toy object of another kind, a drawn SVG or an empty panel in place of the world; stock
players at screens.

**Product.** nav, hero, the range or line-up within the first three sections, two or three feature
sections (one benefit each, each its own composition, below), specs (`rows--spec` or
comparison-table), proof (a review or press line the brief gives), [visit-map for a showroom],
[faq, five questions at most], footer.closing with the newsletter. Every main section shows the
product's world, two or three photographs a screen (one per feature section of the part it names;
a grid of 4 to 8 cut-outs on one backdrop): the product whole in three at most (section 1, One
object), its use, its parts and the people with it in the rest. Prices are "from" prices on cards or in a table, never a plan
table or a monthly switch. A technical product (site-kind tech) may take its render or the effect;
any other product takes no effect, and its render only when it has no photographs (below).
- **The product is the hero, not every frame.** The bar is Figure and 1X: where the product is
  shown whole it fills the frame at large scale, and its use, parts and place carry the rest. In testing, a rendered product page scored 5.5,
  creativity 4.5 ("a safe grey template"), because every visual was a mid-size product in a grey
  rounded panel on a grey ground, five pictures in three poses, one structure three times. With
  photographs or with the render alike:
  1. **Big.** In the hero and at least one more section the product fills most of its frame (its
     long side 80 to 100% of the frame's width, or cropped so it runs off an edge) or stands on the
     section's own ground at anchor scale (8 or more of the 12 columns at 1440, the full column at
     390). The `product` hero does it by itself (`layout.css` 3b): a render or a cut-out stands
     on the page's ground across the wrap, no box, no gradient, no radius, the stage down to 24px
     above the fold and the product as tall as the stage, so its widest view spans 80% or more of
     the wrap at 1440 (the kit's city bike: its `side` 1046 of 1280; its `three-quarter` only
     818, under 8 columns); a product photograph runs edge to edge down to the fold, cropped
     (`--ly-pos`) so the product spans 80% of the wrap. Never a mid-size product inside a grey
     rounded `.panel` on a grey ground: a render is transparent and stands on the ground itself
     (`layout.css` takes the fill, border and padding off every `.frame[data-product]`), a
     cut-out the same; a photograph is the frame.
  2. **The whole product in three sections at most, a different picture in every section.** The
     product whole (any angle, any colour) in the hero and two more; the rest carried by its use
     (loaded, at the bench, at home: the setting fills the frame), close-ups of its parts, an
     exploded view, people with it, a diagram card held still or a type moment (section 1, One
     object). Never one view twice: a smaller file (`-700`), a recolour or a mirror of a view is
     the same view. Each plan line names its section's picture and its kind; no two alike.
  3. **Every promise in a headline is shown in a picture.** A family bike shows the child bench
     with its belts; a lamp shows the light it throws on the table; "takes four crates" shows four
     crates, readable at the section's size. A promise with no picture: add the picture or cut
     the promise.
  4. **Dealt compositions, one contrasting ground.** Each picture section deals its composition
     from section 4's five (`bleed`, `pair`, `trio`, `strip`, `tall-small`), plus `split` (text
     beside one big picture, once a page: on the full product page below, section 2) and the order
     section (the order card beside the product, last, a form, never counted as the split);
     neighbours never the same, no structure (heading,
     panel, picture) twice. For the product: `bleed` the product at anchor scale across the
     viewport; `pair` two views at one ratio; `trio` the whole, a part, a detail; `strip` four
     close-ups of the parts the rows name; `tall-small` the product in use tall, a detail small.
     One section stands on a contrasting ground (the rhythm below, `dark-band` or `brand-band`)
     and holds the strongest view; the rest share one flat ground. Frames take the page radius,
     never a panel inside a panel.
  5. **The colour choice changes the picture.** The order card's swatches swap the product's
     picture beside it (a render: each swatch, a button or radio, carries `data-product-swatch="#<frame
     id>"` and `value="<colour id>"` (an id of the spec's `colors`), and `auto.js` swaps the frame's
     still with no page script, `effects-objects.md`, Views; photographs: one per colour, the swatch
     swaps the `src` and `alt`), and every colour offered is shown at least once on the
     page (one colour per section: the hero, the split, the use scene and the order frame each in
     another colour). A colour offered and never shown is a fault.
  6. **No fact twice.** A stat strip never repeats the spec rows below it: the strip takes the
     three figures that sell (load, range, price), the rows the rest (sizes, weight, motor,
     battery, warranty). One fact, one place, one wording.
  7. **Buttons step on hover and press on click.** The motion layer does it (`motion.md`,
     Button); no page CSS sets a `.btn`'s `transform` or `transition`. A feature card that leads
     somewhere is a linked card (it lifts 2px, its picture zooms 1.03).
- **No photographs: the product is shown, never hidden** (in testing: a cargo bike's page that never
  showed the bike scored 3 of 10). A picture the brief gives (a render, a CAD view, a cut-out) goes
  on the hero's stage. Else the product is **rendered**: one crafted studio render of this product,
  composed from its parts with the objects kit's product-render helper (`assets/objects/
  product-render`; `effects-objects.md`, Product renders): write a short JSON spec of its frame,
  wheels, box, arm or shade, sized from the brief's figures, in its own materials and colours (the
  kit's `specs/` show the format; never ship a kit spec as the client's product), make its posters
  with `make-posters.mjs`, and mount it as `<div class="frame" id="<name>-<view>" data-product="assets/objects/product-render/specs/<name>.json"
  data-product-place="stage" data-product-view="<view>">` with `product-render/auto.js`. A place
  is only the share of its frame the product's bounds fill, centred in it (`build.js`): `stage`
  0.86, `hero` 0.88, `tile` 0.84, `card` 0.9; the page's CSS gives the frame its size and the
  words always stand outside the frame. In the hero the frame goes straight inside the `product`
  hero's `.hero__stage` (`layout.css` 3b sizes it); `stage` in a `split` frame or a full-width
  one, `tile` in a square or portrait tile. The render is the product's picture, not an effect:
  **stills by default, live only when asked (`data-product-mode="live"`), at most one live
  context**, on the page's flat ground, no print, shader ground, moment or scene beside it; the same
  on a product of site-kind other and on hardware. The pictures of rule 2 come from the one spec
  (`effects-objects.md`, Views): the views its `supports` lists of `three-quarter`, `side`,
  `front`, `rear`, `top`, `low`, views of its own (`views`) and `detail:<part>` (a close-up), the
  spec's `scenes` (loaded or in use, from the props `crate`, `bag`, `child-seat`, `bench`,
  `parcel`, `desk`, `book`, `mug`, `sheet`, `tray`) and its `colors`; `make-posters.mjs` prints
  every `make.variants` entry as a still per colour. `deal.mjs --type product --has object`
  (hardware adds `--kind tech`) always prints the `product` hero: its full-width stage, never a
  `split` column. Then the **full product page**, never the short page, one picture a section,
  the product whole in sections 1, 2 and 6 only (put every view and scene in `make.variants`):
  1. hero, view **`side`** (the widest view; a tall product, a lamp or an arm: `three-quarter`)
     whole on the `product` stage, the h1 naming the product and its buyer, the order action;
  2. the product, view **`three-quarter`** (a tall product: `side`), the page's one `split`:
     the frame on 8 columns, the three selling figures on the other 4 (rule 6; `bleed` is never
     right after the hero);
  3. what it does or carries, its **use**: a scene (`three-quarter+loaded`, `work`) whose
     setting fills the frame (a `desk` as the bench across it, `tray`s, `parcel`s, `sheet`s,
     crates; the kit's arm with one tray reads as the arm again), the headline's promise
     readable (rule 3): `bleed` across the wrap with the uses in a row of three under it, or
     `tall-small` with a close-up; a motion video the brief names: its frame here, the poster this
     scene (client slots);
  4. the **parts**, views **`detail:<part>`**: a `strip` or `trio` of close-ups, one per part the
     section names (the box, the motor, the gripper, the stand), the part filling its frame; or an
     exploded view (a scene `exploded` that hides the assembled parts and adds them again as
     plain `parts` spaced along their axis, shot as `three-quarter+exploded`: a close-up view
     frames only the spec's own parts, so the spaced ones fall out of it; an exploded model the
     brief names: its slot); or how
     it is used: three steps or a lanes diagram card held still (charge, ride, park);
  5. specs as `rows--spec` (only the facts the strip does not hold) beside a diagram card held
     still or one figure set large (a type moment), and the real colour icons of the component
     brands the brief names; this or section 2 is the contrasting ground;
  6. ordering, view **`rear-quarter`**, a view of the spec's own (`"views": { "rear-quarter":
     { "from": "three-quarter", "angle": <the spec's angle + 180> } }`, listed in `supports`): a
     live order card (model or size, colour as swatches, delivery slot or town, the price that
     updates, the main action) beside the product whole in the chosen colour, which the swatch
     changes (rule 5); the order composition, not the split; [faq, five questions at most];
     footer.closing.
  Every view is a still. The heading and the text
  say what the thing is; no line calls it a render, model or illustration (house rule 1). The report lists the
  photographs to shoot (`photos.md`). Never a drawn SVG, a model of loose primitives the helper did
  not compose, mood stock, a photograph of another maker's product or an object of another kind (a
  wheel is not a bicycle). **Hardware without photographs or renders goes here too** (in testing: a
  robot arm's page with a silk shader and an order form lost; CAD renders or a film the brief names
  but does not supply count as missing, and each gets its slot: the CAD frame is section 2's
  picture, the motion video section 3's, the exploded model section 4's): a robot arm follows the kit's worked
  `robot-arm` spec, rebuilt to the client's own sizes, joints and colours; a drone is a rounded box body, beam arms, cylinder motors and disc rotors; a camera a
  rounded box and a cylinder lens; a curved shell is rounded boxes and fillets (`round`, `blend`,
  `seams`) at its real measurements. Never a `split` hero holding only an order form or the
  effect in place of the product; the order card is its own section (6).
Nav `nav-cards|nav-split|nav-mega` · footer `footer-columns|footer-dark` · close
`close-photo|close-type|close-word` · rhythm `dark-band|brand-band` (one contrasting ground,
rule 4) · buttons `arrow|solid|block|pill`.
Never: a photograph of something else; screens of an app the product does not have; logo rows;
tabs; anything that apologises for what is missing; the product mid-size in a grey panel; the
product whole in more than three sections; one
view twice; a promise not shown; a colour offered and never shown; a fact twice.

**Service** (clinics, firms, agencies, studios, trades). nav, hero, services-list (each with one line
and a price from; a peek-list when each service has its own photograph), work (a grid of 3 to 6
project photographs, or photo-pair, one per case), steps, people-row, proof (a quote the brief
gives), [pricing-two or a `rows` price list], [faq], booking-form with the address, footer.closing.
Pictures: photographs of the work, the team at work and the rooms, one or two a screen; real icons
for tools a studio really uses.
Nav `nav-mega|nav-split|nav-centre` · footer `footer-visit|footer-dark|footer-columns` · close
`close-type|close-photo` · rhythm `surface-pairs|dark-band|space` · buttons `solid|tonal|block|arrow`.
Never: product UI the firm does not run; stock handshakes; logos of invented clients; tabs.

## 4. Place

Cafes, bars, bakeries, restaurants, guesthouses and small hotels, shops, bookshops, florists, bike
shops, local studios (pottery, yoga; a creative agency stays service; a maker people visit who
also teaches or sells online stays a place: the door decides, the web shop is its goods section).
`<html data-type="place">`,
`<meta name="page-kind" content="place">`, place CSS under `html[data-type="place"]`. Real still
photographs, type and flat colour carry the page; the interface around them is one ground, one ink,
hairlines and one button style. Where a recipe and this section differ on a place, this section
wins. Open these references first for the feel (never copy one): Daunt Books, Prufrock, Bourke
Street Bakery, Gail's, Tartine, Bonanza (a still where Bonanza has film).

**Never on a place:** an effect, WebGL, canvas, CSS gradient, grain, glass, print, scene, moment,
loop, count, UI fragment or diagram; feature or plan cards, tabs, accordions, switches, logo rows,
timelines, fact strips (address or hours as labels), a calendar card, a map of a street the brief
does not give; a rating, review, figure or quote the brief does not give; words on a photograph, a
rounded or filtered photograph, a see-through or blurred nav; outline, pale, blurred or rotated
display type; SaaS furniture (a two-tone headline, a filled-plus-outline pair, a dotted timeline
rail, a carousel); a dark section except the one brand band.

### Plan and length

The nav is not a screen; `footer.closing` is one; a 2-screen section counts two.

- **Full page,** 12 to 20 photographs, 2 to 3 a screen, at most 6 screens: hero, visit, the offer
  (a second offer may follow: a roaster's beans after the menu), the place, then orders or booking
  when taken (last before the footer, its cards or form in place of the close), footer.closing.
  Over 6 screens drop the place, never the booking.
- **Compact page,** 8 to 12 photographs, 4 or 5 screens: hero, visit, the offer, [the place],
  footer.closing.
- **Short page,** under 8 usable photographs (below): 3 screens, 2,700px at most at 1440,
  `<html data-page-mode="short">`.
- **No client photographs (the draft path):** `photos.mjs pick --trade <trade> --sections <words>
  --draft-lead --pictures 12` lifts the 1-in-3 cap, and the page is a whole place page that leads
  with photographs when it reaches 8 frames. `pick` deals one frame per word: repeat a word for each
  row or detail (`bar,bar,coffee,coffee,beans,beans`; `rooms,rooms,rooms,breakfast,breakfast`)
  until it returns 8 or more (a cafe 8 to 12, a guesthouse 9). **The hero is always a photograph
  when any frame fits:** the lead `pick` returns (a cafe's bar); a place whose trade leads with land
  (a guesthouse, a lodge, a remote inn) and whose brief names its region (Westfjords, Lofoten, the
  Lake District, a town) passes that region as `--place "<region as written>"`, and the landscape
  of that region leads, because a remote place is sold by where it stands (in testing: a remote
  guesthouse shown as a type band scored 3.5). The `statement` hero on `.ground-brand` only when
  the library holds no frame of the region and no lead. Every frame is listed in the report as a
  stand-in to replace; nothing on the page says so. **The count decides, not the trade:** after
  the words are repeated until `pick` answers "no new motif left", under 8 frames in all (the
  client's own included) is the short page, whatever the trade (a bakery holds 4, a florist 3,
  pottery or a restaurant none: examples, not a list); 8 to 12 is the compact page, 12 or more the full page.

These three names mean only these lengths everywhere in the skill.
- **Photographs by section,** all distinct: hero 1; visit 1 (0 with a map); menu or prices 1; rooms
  2 to 6; goods 4; the place 3 (row), 1 (story) or a wall; orders 2 or 3, or booking 1; close 1. Nav
  panel photographs do not count.

### The deal

Never by taste; the hero and the splits are never dealt, the close is `close-photo` while a
photograph is left to show (else the re-deal of section 2):

```bash
node -e "for(const l of process.argv.slice(1)){const o=l.split('|');console.log(o[Math.floor(Math.random()*o.length)])}" "nav-split|nav-cards" "footer-visit|footer-columns" "surface-pairs|space|colour-band" "block|solid|arrow" "dots|arc|ring|petal|leaf|stack" "pair|strip|tall-small" "bleed|trio|strip|pair|wall|story" "address|name" "row|side"
```

Read them in order: nav, footer, rhythm, buttons, mark, the offer's composition, the place's
composition (deal it again while it equals the offer's), the type moment, the rooms layout. Rhythm:
`surface-pairs` (the offer on one full `--g-alt` band; the visit section on the page ground with its
panel on `--g-alt`), `space` (one ground throughout, sections parted by space), `colour-band` (the
close on `.ground-brand`, a flat fill in the place's own colour; then the footer has no name across
it).

### Designed variety without effects

A place earns its creativity from photographs, their arrangement and one moment of type, never
from an effect (in testing: correct cafe and guesthouse pages scored creativity 2.5 to 4 and motion 3
to 4.5 because every section was text beside one picture and nothing answered the pointer).

- **Never two sections built round one picture.** The visit keeps its 6/6 split with one
  photograph; every other photographed section takes a composition, the offer and the place each a
  different one, neighbours never the same. Text beside a single photograph happens once a page
  besides the visit (`story`, or the booking form).
- **The five compositions** (1200 column, gap 24; grid widths span-3 282, span-4 384, span-5 486,
  span-6 588; square corners, one grade, no words on any photograph):

  | id | at 1440 | at 390 |
  |---|---|---|
  | `bleed` | the head row on the `.wrap` (its line at the right), then one photograph across the whole viewport, 1440x560, nothing on it; once a page, never right after the hero | 390x488 (4:5 crop) |
  | `pair` | two photographs on span-6, the same ratio (4:3 at 588x441 or 4:5 at 588x735 in a 2-screen section), tops level; the head row above | stacked, 342 wide, 24 apart |
  | `trio` | the offset trio: three photographs on span-5 (4:5, 486x607), span-4 (1:1, 384x384) and span-3 (4:3, 282x212), tops on one line, three sizes of one subject family (the room, its table, a cup) | the first 342 wide, the other two two-up at 165 |
  | `strip` | the detail strip: four 1:1 details on span-3 (282x282) or six on span-2 (180x180) from line to line, hands, tools and materials of one trade, under the section's text or groups | two-up at 165, four at most |
  | `tall-small` | a tall 4:5 photograph on span-6 (588x735) at the left line; on span-5 at the right the h2, its lines and link at the top and a 1:1 on span-3 (282x282) at the bottom, its foot level with the tall one's | text, the tall one at 342, the small one at 165 |

  The offer deals `pair`, `strip` or `tall-small`: `strip` runs under the menu's groups, `pair`
  and `tall-small` take the photograph slot beside them (the groups narrow to span-6). The place
  deals `bleed`, `trio`, `strip`, `pair`, `wall` or `story` (below). Rooms keep their own grid.
- **One display-type moment** (dealt `address|name`): `address` sets the street and district large (no street in the brief: the
  district alone, never an invented street, `copy.md`) right under the visit section's h2 ("Find us" at the page's h2 size, so the heading scale holds):
  `<p class="type-moment"><a href="<map search>">Mill Street, Leith</a></p>`, page CSS
  `.type-moment { font: var(--display-weight) clamp(48px, 7vw, 104px)/1.02 var(--font-display);
  letter-spacing: -0.03em }`, one or two lines on the `.wrap`'s left line, the drawn underline on
  hover; `name` makes the
  close `close-word` (the h2 and the button, then the name across the `.wrap`), its photograph
  going to the place's composition. Ink on the ground or on the brand
  band, never outline, pale, rotated or on a photograph. One a page; the footer's name set wide is
  then capped at `12vw` (about 170px at 1440) or left out.
- **Hover you can see:** every photograph that leads somewhere is a link (a room to its booking, a
  goods photograph to its card, the place to its story) and zooms 1.03 inside its frame while its
  card lifts 2px; the head row's link carries the arrow; the nav words draw their underline
  (`motion.md`). Each section after the hero holds at least one such link.
- **One main action a screen:** a transaction (Book a room, Order a cake) is the nav's button and
  the hero's, as on any page, and nowhere else but the booking or close and the phone bar. Get
  directions is never repeated: the hero's one button and the phone bar's; the nav says "Visit"
  as a word to `#visit`, the visit block adds no second button for it, and the footer gives the
  address linked to the map, never a button (in testing: Get directions in the bar, the hero and the
  footer read as clutter).
- **List text at 16px:** menu rows, descriptions, room facts and hours at 16/24 at least (the muted
  colour, never a smaller size, marks a description); 13px only for a group label.
- **Credits:** the one footer line that links the credits list (`photos.md`, Credits), never one
  link per photograph in the footer.

### The sections (1200 column, x 120 to 1320)

- **Hero:** the place hero (`layout-v4.md` section 3). What, where and one fact: h1 "Bakery on Mill
  Street, Leith" (40 characters at most); sub-line "Sourdough, rye and cardamom buns from 7:30,
  Tuesday to Sunday." (80 at most); one button, the main action.
- **Visit, always screen 2,** marked `data-place="visit"` and `id="visit"`, directly after the hero:
  a panel on `--g-alt` (page CSS: `.visit { background: var(--g-alt); padding: 48px }`, on span-6
  only: a ground box 80% of the section or wider is a band and FAILs `one-section`) and a 1:1 or 4:3 photograph of the shopfront straight-on or the
  room from the door, 6/6, the panel left. With the `address` type moment the h2 and the street
  set large run across the `.wrap` above the split (the photograph then 4:3) and the panel opens
  with the open-now line; else the panel's top line is the h2 "Visit", the open-now line
  (`[data-open-now]`) at its right, never a 13px eyebrow. 16px below, two columns 24 apart: the address on two lines at
  20/30, linked to the map search, the phone as a `tel:` link only when the brief gives one, then
  one secondary button: "Get directions" when the main action is something else, "Call" only when
  the brief gives a phone, else none; and
  the week's hours (days left, times right in tabular figures, one line per day or range, one size;
  a holiday change as one line above). Under both, at most two 44px rows: access, a florist's
  delivery (area, price, cut-off), a guesthouse's check-in and check-out, a bike shop's repair
  turnaround, or "By appointment" for a studio. At 390 the panel first (24px padding, address
  18/28), then the photograph at 342. Hours, address and directions are never only in the footer.
- **Map** only when the brief gives the street: `fx-map` baked still (`effects-creative.md`) in the
  photograph's frame, the pin on the street line; never an embed, a contour or a dot pattern.
- **The offer** opens with a head row: the h2 on the left line, one line, 40 characters at most
  (32/40; 24/30 at 390); at its right, on its baseline, one 16px line and a link ("Full menu", "See
  all"); 56px to the content.
  - **Menu or prices** (drinks, a bakery counter, repairs, bouquet sizes, classes): the groups with
    the offer's dealt composition (Designed variety): `strip`: three groups on span-4, the strip of
    four details under them; `pair` or `tall-small`: two groups on span-3 at the left, the
    photographs on the right span-6, their top level with the group labels; the two groups hold
    the same number of rows (4 against 5 fails `row-lines`, SR-7: 245/303px). A group: a 13px label
    (`.t-label`, weight 500, ink), 12px of air under it and no rule (a rule under a label fails
    `section-air`, SR-3: parts are told apart by air and weight), then `.rows` (each row closes
    with its own 1px rule, none above the first): the name at 16/24/500 left, the price right in tabular
    figures, an optional description at 16/24 muted; rows 44px (64 with a description), at most 6
    with descriptions or 8 without, the rest behind the head row's link. Always text, whole, prices
    visible: never an image, a PDF, tabs or an accordion. At 390 one column, the photographs after
    the first group.
  - **Rooms:** h2 "Rooms and prices", the side line "Breakfast 8 to 10. Check-in from 15, check-out
    by 11." Each room: a 4:3 photograph of the whole room, straight-on, window light; 20px; the name
    (`h3.t-card`, 20/28); the facts at 16/24 muted ("2 guests · 18 m² · garden side"); the price
    from with its season at 16/24; a "Book this room" link. `row`: three rooms on span-4 (384x288)
    or four on span-3 (282x212); two rooms always `side`. `side`: the head as the first cell at the
    left line, top-aligned with the tiles (two rooms span-4; three span-3; four: rooms 2x2 on span-4,
    `--h: 2`). Five or six rooms: rows of three on span-4 in a two-screen section. At 390 one column,
    342x256, 48px apart.
  - **Goods** (beans, bread, books, parts, bouquets): four linked cards on span-3, 1:1 at 282x282
    (bouquets 4:5 at 282x352), one ratio per grid, one backdrop, angle and light. Each card a flat
    fill one step off the ground or a 1px hairline, no shadow, radius or pill; inside its padding
    under the photograph only the name (a two-line slot, 16/500) and the price; an outline Add
    button aligned across the row where it sells online. One or two full rows. At 390 two-up at 165,
    four or six, then a full-width button to the range; no swipe row.
- **The place** (dealt): one of the five compositions under the head row (Designed variety), `wall`
  (the head row, then a wall of photographs from line to line, gap 0 or 2px) or `story` (6/6, text
  left: the h2 on one or two lines, three to six lines at 20/30 on who runs it, since when and what
  exactly, one link; a 4:3 photograph of people at work right, 588x441). One story row a page. No
  names under the photographs. At 390 `wall` two-up, `story` text first.
- **Orders** (cakes, a bike service, weddings, classes): three kinds on span-4 under the head row,
  or two beside the head in the first span-4. Each: a 4:3 photograph of this business's own goods
  (384x288), a 1px hairline, a 13px label, the title at 20/28, one or two sentences at 16/26 with the
  lead time, where to collect and the price from, one text link with an arrow. A florist's events
  kind says what to send: date, venue, guests, budget.
- **Booking** (rooms, or classes with dates): the head row ("Book a room"; "We reply within a
  day."), then a 4:3 photograph on span-6 (588x441) and beside it the form on `--g-alt`, the same
  height, 48px padding: arrival and departure on one row, guests and name on the next, email, the
  main action, the reply line at 14px. Text fields, not `type=date`, on a page not in English. Never
  a photograph, texture or glass under the form. A booking system the brief names replaces the form.
- **Close:** `close-photo`: the h2 (eight words at most), one line ("Open today 7:30 to 16:00"), the
  main action, a 1:1 photograph never used above and never with words on it. On `colour-band` it
  sits on `.ground-brand`, every word at 7:1 (`backgrounds.md`), the button inverted.
- **Footer:** `footer-visit` (the address at 32/40 on span-7, linked to the map search, with one
  line on the way there and no button, the hours from the split line with today marked, the nav
  row, the legal row with the one credits line; then the name set wide across the `.wrap` in the
  display face at 400, at most `12vw`, except on `colour-band` or with the `name` moment) or
  `footer-columns` (Visit, Contact as given, the nav's words, delivery or check-in or the
  newsletter; the legal row).
- **Phone bar** (`nav.actionbar`, required): the order or booking as one full-width button; without
  either, Get directions (primary) and Call (secondary, only with a phone the brief gives).
- **Notice line** (a florist's delivery cut-off, changed or holiday hours): one still 14px line with
  a number above the h1 (`layout-v4.md`), repeated where the fact belongs; never rotating.
- **Splits** 6/6, text left, top-aligned, never mirrored; on a phone the text first.

### Order by trade

Each starts hero, visit; the rest in this order, 4 to 6 screens:
- **Cafe:** menu as text with its composition; the place (its composition or a story row); beans
  or goods only if sold.
- **Bakery:** what it bakes (goods with prices); orders (one card per kind); the process (its
  composition, a `strip` or `trio`, one screen at most). Several shops: a ruled list, each with its street.
  Under 8 frames (the library deals a bakery 4) it is the short page (section 4, The short page).
- **Guesthouse or small hotel:** the hero is the landscape of its region when the brief names one
  (a remote house is sold by where it stands, as Fogo Island Inn is); location as the visit (how to
  arrive, the `address` moment fits); rooms; the house (shared spaces and breakfast in its
  composition, `bleed` for the land around it, no labels); booking. Check-in and check-out beside the rooms and in the footer.
- **Shop or bookshop:** new in (goods with Add); categories as a plain text list; one story row; the
  footer with each shop's address and hours and the newsletter. Nav: four to six category words (`system.md` Nav; four on nav-split).
- **Bike shop:** visit and workshop (usual repair turnaround); workshop prices as ruled rows with
  "Book a service"; new in (cut-outs on white, name and price); brands as a plain text list; story.
- **Florist:** a notice line with delivery area, cut-off and price; delivery and visit as screen 2;
  bouquets (four 4:5 tiles, each with a price from); weddings and events (three photographs of real
  installations, what to send); workshops as ruled rows.

### Look

- **Grounds:** the page ground from the place's walls, paper or shopfront: warm off-white by default
  (`#F7F3EC`; white for a shop that sells mostly online), the surface one step darker (`#EDE6DA`),
  ink `#2A2622`, muted `#665E55` (5.8:1 on the ground), hairline `#DAD3C8`; then
  `start.mjs brand --bg "#F7F3EC" --surface "#EDE6DA" --ink "#2A2622" --muted "#665E55" --accent "#<hex>" --type <pairing>` (colours quoted: a bare `#` starts a shell comment).
  One full surface band at most; one brand band (`backgrounds.md`); no dark section except that
  band (the nav bar may take the dark ink). Flat colour only (`backgrounds.md`).
- **Accent:** one, from the place (the shopfront paint, the tiles, a bag label) on the primary
  button, the focus ring and the `colour-band` close; darken it in steps until its label passes
  4.5:1 and it passes 3:1 on both grounds.
- **Type:** a pairing from `start.mjs deal --page place`, display 400, text 400 and 500: a serif head
  with a plain sans for a bakery, roaster, guesthouse or bookshop; one plain sans in two weights for
  a shop, bike shop, florist or studio; a soft sans for a cafe. Sizes in `layout-v4.md` section 5.
- **Motion:** the hover layer only (`motion.md`), and it must show: the nav words and links draw
  their underline, a linked photograph zooms 1.03 inside its frame while its card lifts 2px,
  buttons step and press, arrows move 3px. Nothing moves by itself, on load or on scroll.

### The short page (under 8 photographs)

Under 8 usable, whatever the trade (the count in Plan and length): three screens, 2,700px at most at 1440 (the tablet
runs longer, below): hero, one `--h: 1` section holding the
visit and the offer, footer.closing. With one or two good photographs, the best is the hero's and
the other is the section's, in one row with the groups (With its photograph, below). With none, the hero is a statement on `.ground-brand` (`deal.mjs --hero statement`: the
h1, the sub-line, the inverted button) and the section has no picture on purpose (the one
exception to "two picture-less sections are never neighbours").
- **The section** is open type on the page ground, never a card or a ground box (across the `.wrap`
  that is a band): the offer as ruled text in groups (a maker's tableware and its classes are two
  groups of rows, prices visible), then the visit block as three `span-4` columns on the grid
  (address, hours with today marked, access; a phone only when the brief gives one). A maker's
  story is one 20/30 paragraph at the head of the visit block, never a section of its own.
- **With its photograph** (a bakery deals 4 frames, so this is the usual case): the groups and the
  photograph in one `.grid.grid--top` row, the photograph last (the next frame after the hero's, its
  `<img>` as `photos.mjs fetch` prints it), its top level with the group
  labels; the visit block across under the row at `margin-top: var(--s-7)`. Three groups: each on
  `span-3` and `<figure class="pl-photo span-3" style="--pl-r: 1">` (1:1, 282x282). Two groups: each
  on `span-3` and `<figure class="pl-photo span-6" style="--pl-r: 1.5">` (3:2, 588x392). Content
  about 560px at 1440, the page 2,700. A 4:3 `span-6` beside the groups runs to 852px, past 828
  (`section-height`). Every group holds the same number of rows and every name fits one line
  beside its price on `span-3` (about 24 characters: "Rye chocolate cake, 10 slices" wraps,
  245/270px, `row-lines`; shorten it, "Rye cake, 10 slices"). Under 640, `--hm: 2` on the section
  (`style="--h: 1; --hm: 2"`) and the photograph after the groups at 16:9, a
  second page-CSS rule: `@media (max-width: 639px) { #shop .pl-photo > img { aspect-ratio: 16 / 9;
  } }` (at 1:1 the section runs 119px past its two screens).
- **Nav and the main action:** three or four words, one per group, each pointing at an `id` on that
  group (`#tableware`, `#classes`, `#visit`); the main action points at the group that does it
  (section 1, One page). One section has no scroll-marked word: leave `aria-current` off.
- **Re-dealt without pictures** (section 2): `nav-split` with no panel, the close as the head row
  of `close-word` without the name. Either the brand band (the close on `colour-band`) or the name
  set wide in the footer, not both.
- **What the deal drops.** The page has no place section, no second offer and no room for a moment:
  of the printed deal build the nav, footer, rhythm (`space`), buttons, mark and the offer's
  groups, and skip the place's composition, the type moment and the rooms layout (the `address`
  moment is not built; the visit block's three columns are the address). Write "not used" beside
  each skipped part on plan line 2.
- **At the tablet (640 to 1023) the section stays one screen,** content 600 to 830px at 768x1024.
  Stacked, the groups and the visit block run to about 1,600px: `section-height` and `one-section`
  FAIL, and `--h: 2` on that stack leaves a `hole` (768) and a `section-air` WARN, 48% (820). So keep
  the three groups and the three visit columns across, one page-CSS rule (use the ids as built):
  `@media (min-width: 640px) and (max-width: 1023px) { #shop .grid { grid-template-columns:
  repeat(3, minmax(0, 1fr)); } #shop .grid > .span-4 { grid-column: auto; } #shop .visit__cols {
  grid-template-columns: repeat(3, minmax(0, 1fr)); } }`, which makes the content about 700px, and
  `--hm` under 640. With a photograph in the section, `--h: 2` at the tablet, read as two screens:
  screen 1 the h2 and the photograph full width down to the screen's bottom padding, screen 2 the
  groups across and the three visit columns, `--padt` under its top (no `hole`; content 1,640 of
  2,048 at 768). This rule replaces the one above (with two groups `repeat(2, minmax(0, 1fr))` on
  `#shop .grid`): `@media (min-width: 640px) and (max-width: 1023px) { #shop { --h: 2; } #shop .grid {
  grid-template-columns: repeat(3, minmax(0, 1fr)); } #shop .grid > :not(.pl-photo) { grid-column:
  auto; } #shop .grid > .pl-photo { grid-column: 1 / -1; order: -1; } #shop .pl-photo > img {
  aspect-ratio: auto; height: calc(var(--pl-room) - 1.25 * var(--t-h2) - var(--head-gap));
  margin-bottom: calc(var(--padt) + var(--padb) + var(--bar) - var(--card-gap)); } #shop .visit__cols
  { grid-template-columns: repeat(3, minmax(0, 1fr)); } }` (the photograph's height leaves room for
  an h2 of one line: keep the h2 to one line at the tablet). The page is 3
  screens at 1440 and 3 or 4 at the tablet.

No mood stock, code ground, drawing, empty box or note. The report lists the shots to take
(`photos.md`). At 8 good photographs it grows to the compact page, at 12 to the full page. A place
with no photographs of its own takes the draft path first (Plan and length); the short page is for
a trade the library cannot fill (`photos.mjs` names no trade for it: pottery, a restaurant, a salon)
or whose frames, counted as in Plan and length, total under 8.

## 5. Visuals

- **UI** (`cards.md`): paste `assets/ui/<name>/fragment.html` into the slot its recipe gives and
  rewrite every name, number, subject and logo, and a loop's arriving text in `data-ui-opts` (its
  `meta.json` `edit`). A pasted `<img src="assets/ui/icons/x.svg">` is the kit's sample mark: write
  each as the client's tool, `<img data-icon="<id>" src="assets/icons/<id>.svg" alt="">`, and
  `icons.mjs scan --colour` fetches it. The product UI section shows the product's own subject, never a stand-in
  fragment. `data-ui-load` shows the kit's sample text: drafts only. None on gaming.
- **Diagram cards** (`diagrams.md`): when the point is how things connect; tech 0 to 2 with pulses,
  product and service one held still, place none.
- **Real icons** (`icons.md`): every tool, app or file type the page names, in its own colours; on
  other pages only tools the client really uses.
- **Shader grounds** (tech only): the one effect and the card group's still grounds
  (`effects-usage.md`).
- **Photographs** (`photos.md`): the client's, else `photos.mjs pick`; every `<img>` carries
  `data-source` and `data-subject`.



---

## `references/system.md`

# System

One system for the whole page, in `assets/system.css` and `system.js`. Use its classes and tokens;
never add a second grid, spacing scale, type scale, radius, button, card, hairline, fade or link
style. One strict system per page: one button shape, one radius family, one card recipe, one
hairline, one corner-control size, one link look, one block template repeated. Section heights,
the hero frame, edges, splits and type sizes: `layout-v4.md`. Grounds: `backgrounds.md`. Every hover
and loop number: `motion.md`.

## Base

- `*{box-sizing:border-box}`, `html,body{margin:0}` and `<meta name="viewport" content="width=device-width,
  initial-scale=1, viewport-fit=cover">` (without the reset the hero ends at 908 and `.wrap` at x 88).
- Spacing scale 4, 8, 12, 16, 24, 32, 48, 64, 96, 128 (`--s-1` to `--s-10`) for every margin, gap
  and padding you write. Heading to content 48px (32 on a phone); cards 24px apart (12).
- One height per card row and per tile kind, page-wide; sections at H or 2H.
- The skip link is the first child of the header's `.wrap`, `position: absolute; width: 1px;
  height: 1px; clip-path: inset(50%)` until focused, so it never pushes the logo off the left line.

## Rhythm tokens

On `:root`, used everywhere (desktop / under 640px):

| Token | Value | Use |
|---|---|---|
| `--nav` | 72 / 56 | the fixed header |
| `--padt` | 120 / 96 | a section's top padding: the h2 sits here |
| `--padb` | 72 / 48 | a section's bottom padding (plus `--bar`) |
| `--gut` | 80 / 24 (place 120 from 1024) | the `.wrap`'s side margin: 1280 wide, 1200 on a place |
| `--hgap` | 48 / 40 (place 40 / 24) | the header to the hero's words, under `--photo` on a place |
| `--hpadb` | 64 / 24 | the hero's bottom padding (plus `--bar`) |
| `--bar` | 0, or `calc(64px + env(safe-area-inset-bottom))` with `nav.actionbar` under 640 | added to every bottom padding; content is never cut to hide behind the bar |

Grid: `.grid` is 12 columns with a 24px gap (12 under 640); the column numbers are in
`layout-v4.md` section 4. A picture wall is its own grid with a gap of 0 or 2px (page CSS
`.wall`), so the base grid keeps its gap.

## Type

The dealt pairing (`layout-v4.md` section 5) at the tokens `--t-h1`, `--t-h2`, `--t-h3`,
`--t-lead`, `--t-card`, `--t-body` 16, `--t-small` 14, `--t-label` 13, `--t-stat` (38/28,
under the h2). A place sets `--t-h2: clamp(24px, .762vw + 21px, 32px)`.

- Headline and text weights: `layout-v4.md` section 5 (the one place they are set); tight tracking.
- Text people read (sub-lines, card lines, list items, answers) is 16px or more, line height 1.5 to
  1.8, in `--ink` at 7:1 or more. `--muted` (4.5:1 or more) only for labels, dates, meta and a
  heading's grey run-on: `<h2>Send invoices in minutes. <span class="muted">Clients pay by
  card.</span></h2>`. Large text (24px+) in a muted half or an inactive row 3:1 at least. On a place
  every text is 4.5:1 or more, and every word on the brand band 7:1. Never 14px paragraphs or 15px grey card text.
- The hero has one quieter level of small text at most (a grey fact line, or a pill above the h1).
- Highlight by contrast, never by colour: no marker highlights or coloured bars behind words; colour
  inside a word once a page at most, never on a place.
- Sentence case everywhere; labels 13px at 500, never tracked capitals or small caps; italic only
  for quotes, attributions and contact lines. Curly quotes; a number never breaks from its unit
  (never "250 / W"); lines at most 62 characters (`.measure`). Nothing under 13px: notes, the legal
  line, dropdown heads, image text.
- One size per kind of element across the page (every card title, address, figure). A figure never
  outgrows the h2 or the h1, at 390 too. Every word is live text, never baked into a picture; text
  never shrinks to fit.

## Colour

- **The interface stays 90 to 95% neutral;** colour comes from the photographs, the product, the
  work and real logos. One near-black ink, often warm, never #000, for text, hairlines (12 to 15% of
  it), button borders, interface glyphs and a designed mark.
- **Real logos keep their own full colours** (house rule): a client's logo or a known product's icon (the
  Google Docs icon) from `icons.mjs` or the brand's press kit, never redrawn or tinted
  (`icons.md`). A fictional client's own mark is designed, not borrowed.
- **One accent at most,** from the client (its product, shopfront paint, tiles, a bag label): the
  primary button (the only filled accent), the focus ring, links, state in visuals, small marks and
  the one brand band; under 3% of a screen elsewhere; its label 4.5:1 on it and it 3:1 on the
  ground. `--action` drives buttons, links and focus.
- **Grounds:** three tokens (`--g-main`, `--g-alt`, `--g-dark`), a brand band on product and place,
  and the tech CSS grounds: `backgrounds.md`. Dark pages and dark heroes are for tech only.
- **The grade** (light or evening) is chosen once on load or by a click, never by scrolling; the dark
  evening grade is tech only.
- **Words on a photograph** only in the hero and one closing band, on tech, product and service, on
  a crop whose calm part is dark and empty at the phone crop too, or on a solid box; no scrim or
  gradient over a photograph; never on a place.
- **Never violet or lavender:** a token whose OKLCH hue falls between about 270 and 330 degrees is
  turned to 255 (blue) or 345 (rose), whichever is nearer; a deal that returns violet is dealt again.

## Radius and buttons

- `<html data-radius>`: `sharp` 4/6/8, `soft` 8/12/20 (default), `round` 10/16/24. `--r-lg` cards
  and frames, `--r-md` panels, `--r-sm` controls, `--r-btn` buttons; software windows one radius
  (12 to 20) with a 1px line. A place: `--r-lg: 0; --r-md: 0; --r-sm: 2px; --r-btn: 2px` (square
  photographs and cards, 2px buttons).
- `.btn.btn--primary` and `.btn.btn--secondary`, 44px high (48 on a place, with
  `data-buttons="block"` and in the phone bar; the nav's button is the same `--btn-h`, never
  smaller), label 16px, 24px side padding, at most two in a `.btn-row`, full width on a phone.
  The look is dealt once on `<html data-buttons="solid|pill|tonal|arrow|block">`; the markup never
  changes. Exactly one filled button marks the main action in any view; every secondary takes one
  style; text links use `.link`. `.btn--xl` once, in the type close. Never a slanted, gradient,
  ghost or shadowed button, or a third style. Their hover and press: `motion.md`.
- The primary carries the drawn arrow `svg.m-arrow` as its last child where the look shows one; one
  arrow style a page, only on the actions that need one.

## Nav

- `header.nav`: `position: fixed`, full width, `--nav` tall, opaque ground, a 1px hairline under it
  from the first paint, `z-index: 10`, the same at every scroll depth: no blur, transparency,
  shrink, hide, shadow, colour flip or floating pill, and nothing else on the page is sticky. Its
  `.wrap` is the page's: the logo on the left line, the main button ending on the right one.
- The dealt type is a class (`sections.md`): `nav` (nav-mega, nav-cards), `nav nav--centre`,
  `nav nav--split`; `nav--tone` puts the bar on the inverse ground (tech).
- The logo: the client's SVG; else the dealt mark and the name at 20px in the display face
  (each kind deals from its own list in `sections.md`: `<span class="mark"
  data-mark="arc|ring|stack|dots|petal|leaf">`, `<span class="mark mark--initial">K</span>`, or the
  name alone for `wordmark`). The footer repeats it.
- Four to six plain one-word nouns (ST-09; a place: Menu, Rooms, Workshop, Visit, About) at
  15px/500 that never wrap, each with its own anchor; a second action as a plain word only when the client has one
  (Sign in for an app with accounts, Gift cards for a shop that sells them); the main action as the
  one button. One word opens a full-width flat panel on hover after 150ms (link columns and a
  picture card, or picture cards; a place: its photographs with the name and the price from); a click
  on the word goes to its section. On other the panel has no shadow, only its ground and a 1px line.
  The current page: `aria-current="page"` on one word at most, a 2px bar under it.
- 640 to 1023: the bar keeps the primary button beside the 44x44 menu button, never a bar of only
  the logo and the menu. The menu button takes the secondary button's look.
- Under 640: the menu opens a full-screen sheet (56px rows, closes on any tap; a place adds the
  street and the week's hours at its foot). `nav.actionbar` (required on a place, optional
  elsewhere) is fixed at the foot, on the ground with a 1px top hairline: one 342x48 main action or
  two 165x48 buttons; `--bar` is then its height. It never covers a label or link.

## Footer

`footer.closing` is the page's last section (`layout-v4.md`): row 1 the dealt close, row 2 the
directory on one ground (link columns, the legal row). Types: `footer-columns`, `footer--dark` (the
name large, columns right; on a dark page a step darker), `footer--statement` (the lit ground; tech),
`footer--visit` (the address set large with the way there and the hours beside it). The legal row:
the brand, the current year, Privacy, Terms (Imprint only with the company's own details from the
brief) and the one credits line (`<details class="credits">`, `copy.md`). `.socials` stays empty
unless the brief gives the accounts.

## Cards, lists and forms

- `.card` as `cards.md` builds it; one height per row; never text in a box in a box. Open tiles
  (`.tile`) for rooms, models and people; `.rows` for menus, prices and specs (a 1px rule closing
  each row); FAQs open in full (`.faq`, no accordion).
- Opening hours: `<dl class="hours">` of `dt`/`dd` pairs with `data-days="tue-sun"` or `data-days="sat,sun"` on each `dt` (the row's label; the `dd` takes none) and
  `data-tz="Europe/Berlin"` on the `dl.hours` itself (the venue's zone; system.js reads it only there): system.js marks today's row (weight 500) and
  fills `[data-open-now]` ("Open now, until 16:00"; "Closed, opens Tuesday at 7:30"); never
  `.is-today` by hand. Without `data-tz` the rows read as plain text, and the panel must read right
  without the script.
- Forms: fields 48px with 13px labels and 16px text (on the phone too), tap targets 44px, six fields
  at most, `method="post"` to the client's address, the button repeats the main action, a line says
  when the reply comes, fields checked on submit; never a fake success or a modal. A booking system
  the brief names replaces the form with its link.
- A `[bracketed placeholder]` or "(sample)" tag left in visible text is outlined in red by
  system.js, as is a visual that fails to draw: fix both.

## Motion

`motion.md`.
