# 5 concrete ideas — with exact keywords to validate

Paste each **primary keyword** into the free Ahrefs Keyword Generator
(ahrefs.com/keyword-generator, US). Then run the 2-minute SERP check below it.

**Target:** KD Easy/Medium, volume 100–9,999, and a SERP where the ranking sites are
weak (low DR, or blog posts / PDFs rather than tools).

**The 30-second reject test** (verified across 26 SERPs): search the primary keyword and
count domains containing *calc* or *tool* that you've never heard of — `usecalcpro`,
`calcimator`, `enbilex`, `niftool`, `found-tools`, `everycalculators`, `mycalcbuddy`,
`agentcalc`, `claycalc`, `hqcalculator`. **4+ → reject** (the task is a pure formula,
already cloned infinitely). **0 farms + PDFs/forums/vendor pages → build it.**

---

## 1. DTF / heat-press transfer size & placement  ⭐ strongest

**SERP verified 2026-08-22:** page 1 is **8 DTF-vendor blog posts with static tables** —
transferkingdom · housedtf · dtfnewengland · indianadtfprint · dtfdatabase · uploaddtf ·
samsdtftransfers · dtfjersey. **Zero interactive tools. Zero calculator farms.** The
tables even contradict each other (adult width 10–12" vs 12–14"; collar drop 3–4" vs 2–3").

**Keywords to check**
```
dtf transfer size chart          <- primary
dtf transfer size chart for shirts
shirt placement guide
heat press placement chart
dtf transfer size chart youth
dtf transfer size chart toddler
where to place design on shirt
htv placement guide
```

**Build:** pick garment + size + placement → to-scale SVG shirt with the design outline
drawn on it, exact dimensions and collar drop. Then the two features no vendor has:
**upload your PNG and see it composited at true scale**, and **print a 1:1 placement
ruler** (the SERP shows people buy that as a physical product).

**Why it wins:** not a formula — a garment × size × placement lookup whose real answer is
visual. Advertisers are heat presses, DTF film, blanks. Repeat use on every design.

---

## 2. Stage-lighting gel cross-reference (Lee ↔ Rosco ↔ GAM ↔ Apollo)

**SERP verified:** Scribd paywall · Rosco vendor page · Lee vendor tool · **4 PDFs** ·
ControlBooth forum · `barriemacarthur.com/funlights/lgtgelLto.htm` (a 1990s page on plain
HTTP) · Wikipedia. **Zero neutral cross-brand tools. Zero farms.**

**Keywords to check**
```
lee to rosco                     <- primary
rosco to lee equivalent
gel color conversion chart
lee filter equivalent
e colour to rosco
gam to rosco conversion
lighting gel cross reference
```

**Build:** searchable N×N table with real colour swatches, transmission %, mired shift.
Filter by hue/family. One page per gel number for the long tail (~250 real pages with
genuine distinct data, not thin).

**Why it's open:** each vendor publishes only its own biased crosswalk as a PDF. Nobody
has commercial incentive to build the neutral version — and unlike embroidery thread or
pottery glaze (both already solved), gel is bought via trade distributors, so no
e-commerce pull-through funded a tool.

**Caveat:** smallest audience of the five. Check volume first.

---

## 3. Board & batten / wall panel layout planner

Omni has `board-and-batten`, and it answers *how many battens*. Nobody answers the actual
question: **where does each one go so the spacing comes out even.**

**Keywords to check**
```
board and batten calculator      <- primary
board and batten spacing calculator
board and batten layout
board and batten spacing
wainscoting calculator
wainscoting layout calculator
accent wall calculator
```

**Build:** enter wall width/height, batten width, target spacing → SVG wall elevation with
every batten positioned, a mark-out list in inches you read straight onto a tape measure,
and a printable cut list. Handle doors, windows, and outlets.

**Why it wins:** live DIY trend, strong advertisers (lumber, tools, paint), and the answer
is a drawing — which neither Omni nor the AI farms can generate.

---

## 4. Website image extractor  ← your instinct, backed by your own data

Your Ahrefs screenshot is the strongest evidence in this whole document:
**`websiteimageextractor.com` is DR 0 ranking #2 with 588 monthly traffic.** A DR-0 site
at #2 is direct proof Google will rank an independent site here. `image extractor` is
KD 30 / >1,000 vol; `pdf image extractor` came back **KD Easy**.

I previously dismissed this on competitor *count*. That was wrong — competitor *strength*
is what matters, and it is low.

**Keywords to check**
```
website image extractor          <- primary
extract images from website
image extractor from website
bulk image downloader from website
download all images from a webpage
pdf image extractor
extract images from url
```

**Build the version none of them have:** paste a URL → grid of every image with dimensions,
file size, and format; filter by min-size (kill the 1px trackers and icons); handle
`srcset`/`<picture>` to grab the **highest-resolution** variant rather than the thumbnail;
lazy-loaded and CSS background images; select-all → ZIP.

**Watch out:** needs a small server-side fetch (CORS blocks pure client-side), so it's the
only one of the five with running cost. Keep it a tiny serverless function.

---

## 5. Recessed lighting layout planner

Omni has `recessed-lighting` and returns *how many lights*. The real question is the
**grid** — spacing, and how far off each wall.

**Keywords to check**
```
recessed lighting spacing calculator   <- primary
recessed lighting layout calculator
can light spacing calculator
recessed lighting layout
how many recessed lights
recessed light spacing chart
pot light spacing calculator
```

**Build:** room dimensions + ceiling height → top-down ceiling plan with every fixture
placed, wall-offset and spacing rules applied, warnings for joists, and a printable
ceiling plan to mark out from.

**Why it wins:** same shape as #3 — DIY money, visual answer, Omni's card is inadequate.

---

## Structure to build (copied from what actually worked)

`realonlineruler.com` is **one page** plus `/about`, `/contact`, `/privacy-policy`,
`/terms` — no blog, no other tools. Its single page carries 8 `<h2>` blocks covering every
sub-intent, ending in an FAQ.

So: **one tool, one page, exhaustive on-page coverage of the sub-intents, FAQ, trust
pages.** Add long-tail tool pages later only once the main term ranks — which is what
`fontfinderai.com` did (`/tools/screenshot-font-finder`, `/logo-font-identifier`,
`/pdf-font-detector`, `/handwriting-font-finder`, `/free-font-alternative-finder`).

**Do not** ship 72 pages on a new domain. That is the single clearest difference between
`realonlineruler.com` and `calcyourfinance`.
