# Shorts Factory — daily run instructions

Channel: Diogo's YouTube channel (UC_ryAJnvgz6qWCSiOy-g3UQ), photography. Shorts are in **English**, faceless,
motion-graphics explainers with a synthetic voice (Kokoro `af_bella`, sid 1). Diogo makes the long videos himself;
these Shorts are 100 % ours. Talk to Diogo in **European Portuguese**, briefly.

Cadence (from 2026-10-03, 2-week test until 2026-10-16): **3 Shorts per day**, each on **YouTube Shorts + TikTok**
via Metricool, in 3 slots (Europe/Lisbon; picked from Metricool best-time data for this brand):
| slot | publish | run starts | content |
|---|---|---|---|
| A | 10:00 | 05:49 | educational |
| B | 14:00 | 09:49 | educational |
| C | 18:00 | 13:49 | Diogo's personal/vlog clip if one is in his inbox (see §1b), otherwise educational |
Each scheduled run produces **only its own slot**. **First step of every run:** `getScheduledPosts` for today; if a
YouTube post already exists within ±60 min of the slot time (e.g. Diogo or a previous session filled it), stop and
report "slot já ocupado" — do not produce anything. Diogo reviews each video (~5 min) between the notification and
publication and can delete the post in Metricool. Usage is limited: work efficiently (few snapshot rounds, no
re-renders unless something is actually wrong).

## 0. Setup (every fresh session)
```bash
cd /home/claude/shorts-factory && bash engine/setup.sh      # TTS model, gsap, fonts into .cache/ (gitignored)
```

## 1. Pick today's topic
- Read `log.json` (what was published) and `backlog.md`.
- Take the first unused backlog item whose **format differs from the last 2 published** (formats: `explainer`, `myth`,
  `before-after`, `why`, `data`, `history`, `from-long-video`). Rotation is required (YouTube "inauthentic /
  mass-produced content" policy): vary the format, layout, colour accents, music chords/bpm and hook style each day.
- Items tagged `NEEDS-DIOGO` need his material: never make them the same day. Ask for the material **the day before**
  in the final message ("Amanhã preciso de …, até às 9h") and only produce it once the material is in the repo
  under `inbox/`. If it is not there, skip to the next item.
- If Diogo said a long video came out (see `inbox/long-videos.md`), a `from-long-video` Short may take priority.
- **Backlog refill:** if fewer than 12 unused items remain, research and append 15 new topics (tagged by format,
  each with one source link) before producing.
- **Vary everything, not just the topic** (Diogo explicitly wants it, and it keeps the channel safe from the
  mass-produced policy). Compared with the last 2 published Shorts, change: format, visual style (§4), **voice**,
  **tone** and hook type. Voices (Kokoro `voice_sid` in video.json): 1 af_bella, 3 af_sarah, 5 am_adam, 6 am_michael,
  7 bf_emma, 9 bm_george — never the same sid as the previous Short. Tones: `curious` (questions, wonder),
  `punchy` (short sentences, myth-busting), `calm-explainer` (slower, speed ~1.0), `storyteller` (history/anecdote).
  Store `voice_sid` and `tone` in the log entry. If a voice mispronounces a key word in a test, respell it in `say`.

## 1b. Diogo's brand formats — his face and voice (slot C)
Diogo's brand for Shorts is a MIX of three formats (his decision, 2026-10-03). He records ONE clip per day.
| format | what | who records |
|---|---|---|
| `talking` | Diogo talks to camera (story, opinion, behind the scenes); we cut, caption, punch-in, add b-roll from his archive (e.g. `E:\Eclipse 26`) and music | Diogo, free speech from 3 bullet points |
| `voiceover` | our motion-graphics explainer (any of the 3 styles) narrated by DIOGO's recorded voice instead of Kokoro; his face appears in a circle bubble (lower-left, ~300 px, cream ring) at key moments and full-screen for the hook and the ending | Diogo reads OUR script once to camera (vertical phone); the same take gives voice + face |
| `synthetic` | the current format, Kokoro voice | nobody (fills the other slots) |
- Default split: slot C = Diogo's format (alternate `talking` / `voiceover`), slots A and B = `synthetic`.
- Language of his recordings: pt-PT for `talking` (burned-in ENGLISH captions translated from what he says);
  for `voiceover` scripts ask/obey the latest decision in log notes (default until he decides: English script). Never
  change his words' meaning in captions; keep translations faithful.
- **The day before**, the slot C run's final report gives Diogo tomorrow's assignment: format, topic, and either 3
  bullet points (`talking`) or the full ~110-word script (`voiceover`), plus recording tips (vertical, eye level, window
  light, quiet room/lavalier, 2-3 takes).
- **Delivery (current):** Diogo attaches the clip in his main chat session; the main session edits and schedules it.
  Planned: a PC folder read via the desktop bridge (needs his PC on). Until that is ACTIVE, the slot C run checks
  Metricool first (a post already in the slot = done); if the slot is empty it produces a `synthetic` Short.
- Editing rules for his footage: follow the `short-motion-captions` skill (keep his cuts, hook first, caption chunks,
  punch-ins, ducked music bed, his voice untouched at -14 LUFS). For `voiceover`: replace voice.wav with his cleaned
  audio and derive word timings from the known script spread over the detected speech regions (as voice.py does).
- **RESERVED: 2026-10-06 slot C (18:00) = Diogo's `talking` clip "Cameras I'd swap my Canon R8 for" (tier-list
  format; brief in `videos/2026-10-06-r8-swap-tierlist/brief.md`), recorded by him on 2026-10-05 and edited in the
  main session.** The slot C run on 2026-10-06 must NOT produce anything: stop and report "slot C reservado para o
  vídeo do Diogo". The 2026-10-05 slot C report must NOT give a new assignment (this one is already given).
  (2026-10-04 slot C was left empty on Diogo's decision.)
- YouTube/TikTok flags for his formats: `isAiGeneratedContent` false (real person, real voice); TikTok `isAigc` false
  for `talking`, true for `voiceover` only if any synthetic voice remains.

## 2. Research (mandatory)
- Verify every number, date, name and claim with WebSearch/WebFetch (primary or reputable sources). No claim without a
  source. Put sources in `video.json` → `sources`. When unsure, cut the claim. Round honestly ("about 70%").
- Look at what already exists on the topic (WebSearch "<topic> shorts") and find a sharper angle/hook.

## 3. Script rules (`videos/<YYYY-MM-DD-slug>/video.json`)
- 35–50 s, ~110–130 words. **Hook ≤ 2 s**: a surprising, specific, true claim, a question, or a contradiction. No intro, no "hey guys".
- One idea per scene; 7–10 scenes (ids A, B, C…). Show data, numbers, a mechanism, a real simulation.
- The last line should loop into the first line (seamless replay).
- `lines`: `[say, show|null, pause_s, sceneId]`. `say` is what the TTS reads (spell numbers/years/acronyms phonetically
  if needed: "nineteen seventy-six", "dee-mosaicing"); `show` is the caption text (digits, "%"). Same meaning, any word count.
- Add `hits` (1–2 big impact words), `chords` (from Am F C G Em Dm D E), `bpm` (88–110), `youtube` block
  (title ≤ 70 chars with the hook, description with the facts + sources summary + 3 hashtags, tags, pinned_comment
  that asks a question to drive comments), `cta` (top chip in the last 2.8 s).
- Copy `videos/2026-10-02-bayer-filter/video.json` as the template.

## 4. Visuals (`scenes.py` + `anim.js` + `gen_images.py` in the video folder)
**Visual style rotates** (Diogo likes the variety). There are 3 looks; pick one **different from the last published
Short** (check `style` in `log.json`), cycling `impact` → `poster-editorial` → `glass-editorial`. Record it as
`"style"` in the log entry. Each look has an exemplar folder — copy its `scenes.py`/`anim.js`/`style.css` patterns:
| style | exemplar | look |
|---|---|---|
| `impact` | `videos/2026-10-02-bayer-filter/` | dark, Anton caps, gold/red, cards + stamps (house `engine/style.css`) |
| `poster-editorial` | `videos/2026-10-03-lens-compression-myth/` | printed posters on paper, Archivo wide caps, mono meta lines, one red accent, halftone images, black-pill captions |
| `glass-editorial` | `videos/2026-10-03-fstops-sqrt2/` | blurred bokeh photo bg, frosted glass panels, serif italic headlines, mono labels, gold accent |
Keep the content rules identical across styles (hook ≤ 2 s, real computed visuals, captions, loop ending). Never
copy a previous video's layouts/headlines verbatim — reuse the *style*, not the *scenes*.
- Impact exemplar building blocks: card, kicker, stamp, chip, tiles, bars, pills, tags, wipe, trio. House style is in
  `engine/style.css` (dark #0b0c10, cream #f4f1ea, gold #ffc542, red #ff3b2f, Anton + Inter). Extra CSS goes in
  `make()["css"]` (the editorial styles keep theirs in the video folder's `style.css`; all fonts come from setup.sh).
- In `impact`, every scene: `<div class="kicker" id="k<ID>">SHORT HEADLINE</div>` (≤ 22 chars, one line) — popped
  automatically. The editorial styles put headlines inside the poster/panel instead.
- Layout safe zones (1080×1920): headline y 150; graphics y 290–1150, x 90–990; captions y 1270–1520 (automatic);
  nothing important below y 1550 or right of x 990 (Shorts UI).
- Prefer **real computed visuals** (numpy simulations: blur, noise, exposure, diffraction, mosaics…) over clip-art.
  `gen_images.py` writes PNGs into `img/`. No copyrighted images, no logos, no real people's photos.
- `anim.js` uses helpers from `engine/base_pre.js`: `tl, $, F(el,from,to,at), pop, out, slam, pulse`, and `KT`
  (word times you compute in `scenes.py` with `ctx.wt(scene, word, n)`). Sync key moments to spoken words.
  Elements that appear later need class `hid` (opacity 0). No `repeat:-1`.

## 5. Produce
```bash
V=videos/<slug>
(cd $V && mkdir -p img && python3 gen_images.py)
python3 engine/voice.py $V && python3 engine/mix.py $V && python3 engine/build.py $V
bash engine/render.sh $V 0.5,3,8,14,20,27,34,40     # lint + validate + snapshots only
# look at $V/build/snaps/contact-sheet*.jpg: fix overlaps, empty scenes, text overflow, wrong sync; repeat
bash engine/render.sh $V                            # full render (~5 min) -> $V/final.mp4
```
Checks before publishing: 0 lint/validate errors; duration 30–58 s; `ffmpeg -i final.mp4 -af ebur128 -f null -`
≈ -14 LUFS; extract and look at 2 frames from final.mp4; re-read the script against the sources.

## 6. Publish
```bash
git add $V/video.json $V/scenes.py $V/anim.js $V/gen_images.py $V/final.mp4 log.json backlog.md
git commit -m "Short: <slug>" && git pull --rebase && git push
```
Then Metricool `createScheduledPost` with blogId `7128060`, date today at **your slot's time** (A 10:00, B 14:00,
C 18:00 Europe/Lisbon; if it is already less than 30 min away, use the slot time +1 h and say so), info:
```json
{"autoPublish": true, "draft": false, "text": "<description>", "firstCommentText": "<pinned_comment>",
 "media": ["https://raw.githubusercontent.com/DiogoARJ/shorts-factory/main/videos/<slug>/final.mp4"],
 "providers": [{"network": "youtube"}],
 "publicationDate": {"dateTime": "YYYY-MM-DDT<HH:MM>:00", "timezone": "Europe/Lisbon"},
 "youtubeData": {"title": "<title>", "type": "short", "privacy": "public", "tags": [...],
                 "category": "EDUCATION", "madeForKids": false, "isAiGeneratedContent": false},
 "descendants": [], "shortener": false, "smartLinkData": {"ids": []}, "mediaAltText": [], "hasNotReadNotes": false}
```
(`isAiGeneratedContent` is for realistic synthetic people/events; our animated explainers are not that.)

**Also post the same video to TikTok** (account `restolhofoto`, same Metricool brand) as a **separate**
`createScheduledPost` at the same slot time, so the two platforms can be compared:
```json
{"autoPublish": true, "draft": false,
 "text": "<hook sentence + emoji> <2-line explanation> #photography #camera #photographytips #learnontiktok #<topic tag>",
 "firstCommentText": "", "media": ["<same raw.githubusercontent URL>"], "providers": [{"network": "tiktok"}],
 "publicationDate": {"dateTime": "YYYY-MM-DDT<HH:MM>:00", "timezone": "Europe/Lisbon"},
 "tiktokData": {"privacyOption": "PUBLIC_TO_EVERYONE", "title": "<same title>", "isAigc": true,
                "disableComment": false, "disableDuet": false, "disableStitch": false,
                "commercialContentThirdParty": false, "commercialContentOwnBrand": false, "autoAddMusic": false},
 "descendants": [], "shortener": false, "smartLinkData": {"ids": []}, "mediaAltText": [], "hasNotReadNotes": false}
```
TikTok caption ≤ 300 chars, more casual than YouTube; `isAigc: true` (synthetic voice — TikTok's AI label).
**Never post to the Instagram account** in this brand (Diogo keeps Instagram for his own non-AI content).
Add the entry to `log.json` (date, slug, slot, format, style, voice_sid, tone, title, both plannerUrls; later the public URLs) and push again.

## 7. Report to Diogo (final message, Portuguese, short)
Send the MP4 with SendUserFile, then: topic + format in one line, title, publication time, "para cancelar apaga o
post no Metricool antes da hora" + plannerUrl, anything uncertain (pronunciation, a fact), and **what you need from him
for tomorrow, if anything**. If anything failed, say exactly what and leave the video committed for manual upload.

## Never
- Publish a claim you could not source. Reuse the exact same template/hook twice in a row.
- Post anywhere other than YouTube + TikTok (never Instagram), or to another Metricool brand.
- Delete or edit Diogo's long videos or other posts.
